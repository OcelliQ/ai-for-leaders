# Student course setup

Open this repository directly in a GitHub Codespace. The parent workshop checkout is for the instructor; startup refuses to activate its student submodules. Setup activates the student templates, installs Anthropic's document skills plugin (including `pptx`), configures Claude and checks PPTX/PDF export. When setup finishes, open Claude Code and sign in with your own account, or run `claude` in the terminal. No workshop key or course sign-in is supplied.

The public task contains no inference key. The terminal launcher and VS Code extension use your personal Claude login and normal Claude profile. You can also supply your own Anthropic environment variables. Model choices come from your account or provider; there are no workshop model restrictions. The helper performs no enrollment, keyserver requests, transcript collection or uploads, and starts no background watcher. Claude keeps its usual local conversation history. You are responsible for your own subscription or provider usage.

For a custom Anthropic-compatible provider, copy `.course/config.example.json` to `.course/config.local.json` and fill in your own HTTPS endpoint, key and main/auxiliary model IDs. The local file is ignored by Git and excluded from container builds. Run `course start`, reload VS Code and start a new chat. This explicitly selected configuration overrides inherited authentication for course launches; it is not required for personal Claude login. Remove the local configuration to return to your own account, and remove its corresponding `claudeCode.environmentVariables` from VS Code settings if you previously applied it.

The container installs Node 24.18.0, Python 3.12.13, uv 0.12.6, Claude Code CLI 2.1.289, LibreOffice Impress, Poppler and Open Sans, plus the tools the `pptx` skill expects: `pptxgenjs` 4.0.1 (global, on `NODE_PATH`), `markitdown[pptx]` 0.1.8, Pillow 12.3.0, defusedxml 0.7.1 and lxml 6.1.3. The skill itself is the `document-skills` plugin from the `anthropics/skills` marketplace; its licence does not allow redistribution, so setup installs it from GitHub into the Claude profile, and the profile settings keep it enabled. Students build decks from `templates/astar-template.pptx`; see `templates/README.md`. The editor requests official extension `anthropic.claude-code@2.1.289` and PDF viewer `mathematic.vscode-pdf@0.2.6`. Built-in VS Code chat and Copilot are disabled. The PDF viewer's one-time support prompt is marked shown. The CLI package has a committed integrity-checked npm lockfile; the extension has its own bundled runtime.

Useful commands:

- `course start`: prepare Claude and remove old workshop editor overrides. Sign in with your own account; reload VS Code and start a new chat after changing provider configuration.
- `course status`: show the authentication mode and any local provider endpoint/model IDs, without displaying credentials.
- `course setup`: activate student templates, install the document skills plugin if it is missing, configure Claude and run the tool/export checks.
- `course dependencies`: install or update the document skills plugin.
- `course smoke`: check tool versions and the `pptx` skill's tools, and render the presentation template to PDF, without making a model call.
- `course activate`: activate tracked `.student` files and folders in a standalone student checkout.

The helper uses your normal `~/.claude/` profile, or your existing `CLAUDE_CONFIG_DIR`, and preserves personal Claude settings while enabling the document skills plugin. Existing unrelated editor settings are preserved. An optional local provider configuration applies matching authentication to the CLI and editor, keeps extended thinking and tool search off as in the original exercise, and excludes those editor settings from Settings Sync.

After updating an existing workshop Codespace, rebuild the container, run `course start`, reload VS Code and start a new chat. The helper recognises and removes the former AIHub editor overrides and avoids the former `~/.local/state/course/` Claude profile. The old `.course/config.json` is never read. Old profiles and queues are not scanned or uploaded. The former bundled key was rejected with HTTP 401 by AIHub's inference endpoint on 8 October 2026. A browser Codespaces rehearsal is still needed to verify the extension UI.

Student activation handles tracked files and hidden directories, skips generated output and dependency folders, and keeps a private rename journal for interrupted startup recovery. It preflights collisions and never overwrites an existing destination. Preserve edits and resolve duplicate activated/template files before rerunning setup.

For a local check, build with `docker build -f .devcontainer/Dockerfile -t course-student .` from a standalone clone, mount that clone at `/workspaces/task`, and run `course dependencies` followed by `course setup`. Regression tests use disposable homes and synthetic credentials; they verify personal login setup, optional provider configuration and migration without making model calls.

References: [Claude settings](https://code.claude.com/docs/en/settings) and [VS Code extension configuration](https://code.claude.com/docs/en/vs-code).
