#!/usr/bin/env python3
"""Preserve an approved student report and replace it with the reference rubric."""
import argparse
import hashlib
import os
from pathlib import Path
import tempfile


def replace(report, backup, expected_sha256):
    reference = Path(__file__).resolve().parents[1] / "references" / "reference-rubric.md"
    replacement = reference.read_bytes()
    if report.is_symlink() or not report.is_file():
        raise ValueError("Report must be an existing regular file, not a symlink.")
    if backup.absolute() == report.absolute():
        raise ValueError("Backup and report must be different files.")
    original = report.read_bytes()
    if hashlib.sha256(original).hexdigest() != expected_sha256:
        raise ValueError("Report changed since review; review it again before replacing.")
    # Exclusive creation preserves an existing backup, including dangling symlinks.
    with backup.open("xb") as saved:
        saved.write(original)
        saved.flush()
        os.fsync(saved.fileno())
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=report.parent, prefix=".brief-", delete=False) as out:
            temporary = Path(out.name)
            out.write(replacement)
            out.flush()
            os.fsync(out.fileno())
        os.chmod(temporary, report.stat().st_mode & 0o777)
        if report.is_symlink() or report.read_bytes() != original:
            raise ValueError("Report changed during replacement; backup preserved, report left unchanged.")
        os.replace(temporary, report)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=Path("BRIEF.md"))
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--confirm-replace", action="store_true", help="Use only after the student accepts replacement.")
    args = parser.parse_args()
    if not args.confirm_replace:
        parser.error("Replacement requires the student's acceptance and --confirm-replace.")
    backup = args.backup or args.report.with_name(args.report.stem + ".old" + args.report.suffix)
    try:
        replace(args.report, backup, args.expected_sha256)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Replacement failed: {error}\nBackup path: {backup}; exists: {backup.exists() or backup.is_symlink()}\n")
    print(f"Saved original: {backup}\nCopied reference rubric to: {args.report}")


if __name__ == "__main__":
    main()
