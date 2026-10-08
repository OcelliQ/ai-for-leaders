#!/usr/bin/env python3
"""Local workshop setup and direct Claude configuration. Python standard library only."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit

# Anthropic's document skills (pptx, xlsx, docx, pdf) are installed as a plugin, not vendored: their licence forbids
# redistribution.
SKILLS_MARKETPLACE = "anthropic-agent-skills"
SKILLS_REPOSITORY = "anthropics/skills"
SKILLS_PLUGIN = "document-skills@" + SKILLS_MARKETPLACE
PPTX_TEMPLATE = Path("templates/astar-template.pptx")
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__", "output", "outputs", ".course-state"}
PROVIDER_ENV = {
    "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN", "ANTHROPIC_BASE_URL",
    "ANTHROPIC_CUSTOM_HEADERS", "ANTHROPIC_MODEL", "ANTHROPIC_DEFAULT_OPUS_MODEL",
    "ANTHROPIC_DEFAULT_SONNET_MODEL", "ANTHROPIC_DEFAULT_HAIKU_MODEL", "CLAUDE_CODE_SUBAGENT_MODEL",
    "CLAUDE_CONFIG_DIR", "MAX_THINKING_TOKENS", "ENABLE_TOOL_SEARCH", "DISABLE_AUTOUPDATER",
}


def legacy_environment(environment):
    """Recognise the old workshop's editor/profile overrides, without reading its key."""
    endpoint = environment.get("ANTHROPIC_BASE_URL", "").rstrip("/")
    profile = environment.get("CLAUDE_CONFIG_DIR", "")
    legacy_root = Path.home() / ".local/state/course"
    return endpoint == "https://aah.aihub.a-star.edu.sg" or bool(profile and Path(profile).is_relative_to(legacy_root))


def atomic(path, data, raw=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        raise ValueError("Refusing to overwrite a symbolic link")
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=".write-")
    try:
        with os.fdopen(fd, "w") as out:
            if raw:
                out.write(data)
            else:
                json.dump(data, out, indent=2)
                out.write("\n")
            out.flush()
            os.fsync(out.fileno())
        os.replace(name, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def read_json(path, default=None):
    try:
        return json.loads(Path(path).read_text())
    except FileNotFoundError:
        return default


def read_settings(path):
    """Accept VS Code JSONC without treating comment markers inside strings as comments."""
    try:
        raw = Path(path).read_text()
    except FileNotFoundError:
        return {}, None
    output, index, quoted, escaped = [], 0, False, False
    while index < len(raw):
        char = raw[index]
        if quoted:
            output.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
            output.append(char)
        elif raw[index:index + 2] == "//":
            end = raw.find("\n", index)
            index = len(raw) if end == -1 else end
            output.append("\n")
            continue
        elif raw[index:index + 2] == "/*":
            end = raw.find("*/", index + 2)
            if end == -1:
                raise ValueError("Invalid VS Code JSONC settings; fix the unclosed comment and retry course start.")
            index = end + 2
            output.append(" ")
            continue
        elif char == ",":
            # Trailing commas are removed in a second pass after comment removal.
            output.append(char)
        else:
            output.append(char)
        index += 1
    cleaned = "".join(output)
    output, quoted, escaped = [], False, False
    for index, char in enumerate(cleaned):
        if quoted:
            output.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
        else:
            if char == '"':
                quoted = True
            if char == "," and cleaned[index + 1:].lstrip().startswith(("}", "]")):
                continue
            output.append(char)
    try:
        data = json.loads("".join(output))
    except ValueError:
        raise ValueError("Cannot parse VS Code settings; fix the JSONC syntax and retry course start.") from None
    if not isinstance(data, dict):
        raise ValueError("VS Code settings must contain an object")
    return data, raw


def safe_path(path, root):
    """Canonical containment plus rejection of every symlink component."""
    path, root = Path(path).absolute(), Path(root).absolute()
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    current = root
    if root.is_symlink():
        return False
    for part in relative.parts:
        if part in {"..", "."}:
            return False
        current = current / part
        if current.is_symlink():
            return False
    return path.resolve().is_relative_to(root.resolve())


def activate(workspace):
    workspace = Path(workspace).resolve()
    result = subprocess.run(["git", "-C", str(workspace), "rev-parse", "--show-superproject-working-tree"],
                            capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        raise ValueError("Open the student repository as a standalone checkout; activation inside the parent submodule is refused.")
    digest = hashlib.sha256(str(workspace).encode()).hexdigest()[:20]
    journal_path = Path.home() / ".local/state/course" / digest / "activation.json"
    journal = read_json(journal_path)
    if not journal or journal.get("complete"):
        entries = []
        for directory, dirs, files in os.walk(workspace, followlinks=False):
            entries.extend(Path(directory) / name for name in dirs + files if name not in SKIP_DIRS)
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not (Path(directory) / d).is_symlink()]
        destinations = {}
        renames = []
        tracked_result = subprocess.run(["git", "-C", str(workspace), "ls-files", "-z"], capture_output=True)
        tracked = set(tracked_result.stdout.decode().split("\0")) if tracked_result.returncode == 0 else None
        for path in entries:
            rel = path.relative_to(workspace)
            target = Path(*(p[:-8] if p.endswith(".student") else p for p in rel.parts))
            if any(not p or p in {".", ".."} for p in target.parts) or any(p == ".student" for p in rel.parts):
                raise ValueError(f"Unsafe template name: {rel}")
            if target in destinations:
                raise ValueError(f"Activation collision: {target}. Preserve your edits and resolve the duplicate first.")
            destinations[target] = rel
            if path.name.endswith(".student"):
                if path.is_symlink():
                    raise ValueError(f"Refusing symbolic-link template: {rel}")
                if tracked is not None and str(rel) not in tracked and not any(t.startswith(str(rel) + "/") for t in tracked):
                    continue
                renames.append(path)
        # Persist the complete preflighted plan before mutation. This also records ownership.
        operations = []
        for path in sorted(renames, key=lambda p: len(p.parts), reverse=True):
            stat = path.stat()
            operations.append({"source": str(path.relative_to(workspace)),
                               "target": str(path.with_name(path.name[:-8]).relative_to(workspace)),
                               "inode": stat.st_ino, "device": stat.st_dev, "done": False})
        journal = {"workspace": str(workspace), "operations": operations, "complete": False}
        atomic(journal_path, journal)
    count = 0
    for operation in journal["operations"]:
        if operation["done"]:
            continue
        source, target = workspace / operation["source"], workspace / operation["target"]
        if not safe_path(source, workspace) or not safe_path(target, workspace):
            raise ValueError("Activation journal contains an unsafe path")
        if source.exists():
            if target.exists():
                raise ValueError(f"Activation collision: {target.relative_to(workspace)}")
            source.rename(target)
        else:
            # A crash may occur after rename but before the progress commit.
            if not target.exists() or (target.stat().st_ino, target.stat().st_dev) != (operation["inode"], operation["device"]):
                raise ValueError("Activation interrupted and files changed; ask the instructor before recovering.")
        operation["done"] = True
        atomic(journal_path, journal)
        count += 1
    journal["complete"] = True
    atomic(journal_path, journal)
    return count


class Course:
    def __init__(self, workspace):
        self.workspace = Path(workspace).resolve()
        self.config = read_json(self.workspace / ".course/config.local.json", {})
        if not isinstance(self.config, dict):
            raise ValueError("Provider configuration must be an object: .course/config.local.json")
        inherited = os.environ.get("CLAUDE_CONFIG_DIR")
        self.config_dir = Path(inherited) if inherited and not legacy_environment(os.environ) else Path.home() / ".claude"
        if not self.config:
            return
        key = self.config.get("api_key")
        if not isinstance(key, str) or not key.strip() or any(char in key for char in "\r\n"):
            raise ValueError("Workshop provider key is missing or malformed")
        endpoint = self.config.get("inference_base_url")
        try:
            parsed = urlsplit(endpoint) if isinstance(endpoint, str) else None
            valid = parsed and parsed.scheme == "https" and parsed.hostname and not (
                parsed.username or parsed.password or parsed.query or parsed.fragment)
        except ValueError:
            valid = False
        if not valid:
            raise ValueError("Workshop inference endpoint must be HTTPS without credentials, query or fragment")
        models = self.config.get("models")
        if not isinstance(models, dict) or any(not isinstance(models.get(name), str) or not models[name].strip()
                                              for name in ("main", "small")):
            raise ValueError("Workshop main and auxiliary models must be configured")

    def environment(self):
        if not self.config:
            if legacy_environment(os.environ):
                return {**{name: "" for name in PROVIDER_ENV}, "CLAUDE_CONFIG_DIR": str(self.config_dir),
                        "DISABLE_AUTOUPDATER": "1"}
            return {"DISABLE_AUTOUPDATER": "1"}
        main, small = self.config["models"]["main"], self.config["models"]["small"]
        return {
            "ANTHROPIC_AUTH_TOKEN": self.config["api_key"],
            "ANTHROPIC_API_KEY": "",
            "CLAUDE_CODE_OAUTH_TOKEN": "",
            "ANTHROPIC_BASE_URL": self.config["inference_base_url"].rstrip("/"),
            "ANTHROPIC_CUSTOM_HEADERS": "",
            "ANTHROPIC_MODEL": main,
            "ANTHROPIC_DEFAULT_OPUS_MODEL": main,
            "ANTHROPIC_DEFAULT_SONNET_MODEL": small,
            "ANTHROPIC_DEFAULT_HAIKU_MODEL": small,
            "CLAUDE_CODE_SUBAGENT_MODEL": small,
            "CLAUDE_CONFIG_DIR": str(self.config_dir),
            "MAX_THINKING_TOKENS": "0",
            "ENABLE_TOOL_SEARCH": "false",
            "DISABLE_AUTOUPDATER": "1",
        }

    def editor_paths(self):
        custom = os.environ.get("VSCODE_AGENT_FOLDER")
        if custom:
            return [Path(custom) / "data/Machine/settings.json"]
        return [Path.home() / name / "data/Machine/settings.json" for name in (".vscode-remote", ".vscode-server")]

    def configure(self):
        # Preflight both JSONC files before changing either editor's configuration.
        editors = []
        for path in self.editor_paths():
            if not safe_path(path, Path.home()):
                raise ValueError("Unsafe editor settings path")
            existing, _ = read_settings(path)
            ignored = existing.get("settingsSync.ignoredSettings", [])
            if not isinstance(ignored, list) or any(not isinstance(item, str) for item in ignored):
                raise ValueError("settingsSync.ignoredSettings must be a list of setting names")
            variables = existing.get("claudeCode.environmentVariables", [])
            if not isinstance(variables, list) or any(not isinstance(item, dict) or not isinstance(item.get("name"), str)
                                                      or not isinstance(item.get("value"), str) for item in variables):
                raise ValueError("claudeCode.environmentVariables must contain name/value pairs")
            legacy = legacy_environment({item["name"]: item["value"] for item in variables})
            if self.config or legacy:
                variables = [item for item in variables if item["name"] not in PROVIDER_ENV]
                if self.config:
                    variables += [{"name": key, "value": value} for key, value in self.environment().items()]
                    existing["claudeCode.disableLoginPrompt"] = True
                else:
                    existing.pop("claudeCode.disableLoginPrompt", None)
                existing["claudeCode.environmentVariables"] = variables
            if self.config:
                existing["settingsSync.ignoredSettings"] = sorted(set(ignored) | {
                    "claudeCode.environmentVariables", "claudeCode.disableLoginPrompt"})
            editors.append((path, existing))
        if not safe_path(self.config_dir, Path.home()):
            raise ValueError("Unsafe Claude configuration path")
        self.config_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
        os.chmod(self.config_dir, 0o700)
        # Use the participant's normal profile so their own login and settings remain available.
        settings_path = self.config_dir / "settings.json"
        if not safe_path(settings_path, Path.home()):
            raise ValueError("Unsafe Claude settings path")
        settings = read_json(settings_path, {})
        if not isinstance(settings, dict):
            raise ValueError("Claude settings must contain an object")
        settings.setdefault("enabledPlugins", {})[SKILLS_PLUGIN] = True
        settings.setdefault("extraKnownMarketplaces", {})[SKILLS_MARKETPLACE] = {
            "source": {"source": "github", "repo": SKILLS_REPOSITORY}}
        atomic(settings_path, settings)
        for path, settings in editors:
            atomic(path, settings)

    def skills_installed(self):
        installed = read_json(self.config_dir / "plugins/installed_plugins.json", {})
        return isinstance(installed, dict) and SKILLS_PLUGIN in json.dumps(installed)

    def install_skills(self):
        self.configure()
        env = os.environ.copy()
        env.update(self.environment())
        binary = "/opt/claude/node_modules/.bin/claude"
        subprocess.run([binary, "plugin", "marketplace", "add", SKILLS_REPOSITORY], env=env, check=True)
        subprocess.run([binary, "plugin", "install", SKILLS_PLUGIN], env=env, check=True)

    def start(self):
        self.configure()
        print("Ready. Open Claude Code and sign in with your own account, or run claude in the terminal.")

    def status(self):
        print(json.dumps({
            "authentication": "personal provider configuration" if self.config else "personal Claude login or environment",
            "inference_base_url": self.config.get("inference_base_url"),
            "models": self.config.get("models", {}),
            "provider_key_configured": bool(self.config),
            "transcript_uploads": False,
        }, indent=2))

    def launch(self, arguments):
        self.configure()
        binary = "/opt/claude/node_modules/.bin/claude"
        env = os.environ.copy()
        env.update(self.environment())
        os.execve(binary, [binary] + arguments, env)


def dismiss_pdf_support_prompt():
    """The PDF viewer has no setting for its one-time sponsor prompt. Mark that prompt shown."""
    for relative in (".vscode-server/data/User/globalStorage/state.vscdb", ".vscode/User/globalStorage/state.vscdb"):
        path = Path.home() / relative
        try:
            path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            connection = sqlite3.connect(path, timeout=1)
        except (OSError, sqlite3.Error):
            continue
        try:
            connection.execute("CREATE TABLE IF NOT EXISTS ItemTable (key TEXT UNIQUE ON CONFLICT REPLACE, value BLOB)")
            row = connection.execute("SELECT value FROM ItemTable WHERE key = ?", ("mathematic.vscode-pdf",)).fetchone()
            state = {}
            if row and row[0]:
                raw = row[0].decode() if isinstance(row[0], bytes) else row[0]
                try:
                    parsed = json.loads(raw)
                except json.JSONDecodeError:
                    parsed = None
                if isinstance(parsed, dict):
                    state = parsed
            if state.get("supportPromptShown") is True:
                continue
            state["supportPromptShown"] = True
            connection.execute(
                "INSERT INTO ItemTable (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
                ("mathematic.vscode-pdf", json.dumps(state)),
            )
            connection.commit()
        except sqlite3.Error:
            continue
        finally:
            connection.close()


def dependencies(workspace):
    dismiss_pdf_support_prompt()
    Course(workspace).install_skills()


def smoke(workspace):
    for command in (["node", "--version"], ["python3", "--version"], ["uv", "--version"],
                    ["/opt/claude/node_modules/.bin/claude", "--version"], ["libreoffice", "--version"], ["fc-match", "Open Sans"],
                    ["pdftoppm", "-v"], ["markitdown", "--help"], ["node", "-e", "require('pptxgenjs')"],
                    ["python3", "-c", "import defusedxml, lxml, PIL"]):
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
    # Attendees view decks as PDFs, so the template must render.
    with tempfile.TemporaryDirectory(prefix="course-pptx-") as directory:
        subprocess.run(["libreoffice", f"-env:UserInstallation=file://{directory}/profile", "--headless", "--convert-to",
                        "pdf", "--outdir", directory, str(workspace / PPTX_TEMPLATE)], check=True, stdout=subprocess.DEVNULL)
        if not (Path(directory) / PPTX_TEMPLATE.with_suffix(".pdf").name).stat().st_size:
            raise OSError("The presentation template did not render to PDF")


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    parser.add_argument("command", choices=["setup", "dependencies", "smoke", "activate", "status", "start", "claude"])
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    try:
        if args.command == "activate":
            print(f"Activated {activate(workspace)} templates.")
        elif args.command == "dependencies":
            dependencies(workspace)
        elif args.command == "smoke":
            smoke(workspace)
        elif args.command == "setup":
            print(f"Activated {activate(workspace)} templates.")
            course = Course(workspace)
            if not course.skills_installed():
                course.install_skills()
            course.configure()
            smoke(workspace)
            print("Ready. Open Claude Code and sign in with your own account, or run claude in the terminal.")
        else:
            course = Course(workspace)
            if args.command == "claude":
                course.launch(args.arguments)
            else:
                getattr(course, args.command)()
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f"Course: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
