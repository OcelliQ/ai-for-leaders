#!/usr/bin/env python3
"""Save feedback for Gaurav locally and submit the whole file with this student's ID.

    python3 .claude/skills/tell-gaurav/send.py --add <<'EOF'
    **Category:** unclear · **Task:** /slides
    Step 3 was confusing.
    EOF

With --add, stdin is appended to .feedback/feedback.md as a new timestamped entry. Without it, the
existing file is resent. Every submission sends the full file and the same student ID, so the latest
one supersedes earlier ones. .feedback/ ignores itself in Git.
"""
import sys
import urllib.error
import urllib.request
import uuid
import json
from datetime import datetime
from pathlib import Path

ENDPOINT = "https://clm.ocelli.vision/feedback"
TOKEN = "vVyz1QjKc7rXJvNrD0_Bl8-W"  # ponytail: shared workshop token, only gates spam
DIR = Path(__file__).resolve().parents[3] / ".feedback"


def student_id():
    path = DIR / "student-id"
    if not path.exists():
        path.write_text(str(uuid.uuid4()) + "\n")
    return path.read_text().strip()


def main():
    DIR.mkdir(exist_ok=True)
    (DIR / ".gitignore").write_text("*\n")
    feedback = DIR / "feedback.md"
    if "--add" in sys.argv[1:]:
        entry = sys.stdin.read().strip()
        if not entry:
            sys.exit("Nothing to add: pass the entry on stdin.")
        with feedback.open("a") as f:
            f.write(f"{'' if not feedback.stat().st_size else chr(10)}## {datetime.now().astimezone():%Y-%m-%d %H:%M %Z}\n\n{entry}\n")
    if not feedback.exists() or not feedback.read_text().strip():
        sys.exit("No feedback saved yet.")
    body = json.dumps({"student": student_id(), "message": feedback.read_text()}).encode()
    request = urllib.request.Request(ENDPOINT, body, {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json",
                                                      "User-Agent": "tell-gaurav/1"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            print(response.read().decode().strip())
    except (urllib.error.URLError, OSError) as error:
        detail = error.read().decode().strip() if isinstance(error, urllib.error.HTTPError) else str(error)
        sys.exit(f"Not sent ({detail}). The feedback is saved in {feedback}; run this script again later to resend it.")
    print(f"Saved locally in {feedback}.")


if __name__ == "__main__":
    main()
