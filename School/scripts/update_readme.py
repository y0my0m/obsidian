#!/usr/bin/env python3
"""Regenerate the subject lists in Main/README.md from notes in Main/."""
from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "Main"
README = MAIN / "README.md"
SUBJECTS = [
    ("Accounting", "💼"),
    ("Chemistry", "🧪"),
    ("Computer Science", "💻"),
    ("Physics", "⚛️"),
    ("Tution", "📖"),
]
DISPLAY_NAMES = {"Tution": "Tuition"}
START = "<!-- SUBJECT-LISTS:START -->"
END = "<!-- SUBJECT-LISTS:END -->"


def note_title(note: Path) -> str:
    """Use a note's H1 when present; otherwise use its filename."""
    for line in note.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1)
    return note.stem


def has_content(note: Path) -> bool:
    """Do not list empty placeholder notes."""
    return bool(note.read_text(encoding="utf-8").strip())


def subject_section(folder_name: str, icon: str) -> str:
    folder = MAIN / folder_name
    notes = sorted((p for p in folder.rglob("*.md") if has_content(p)), key=lambda p: p.as_posix().lower())
    heading = DISPLAY_NAMES.get(folder_name, folder_name)
    lines = [f"## {icon} {heading}", ""]
    if not notes:
        lines.append("*No notes yet.*")
    else:
        for note in notes:
            target = quote(note.relative_to(MAIN).as_posix(), safe="/")
            lines.append(f"- [{note_title(note)}]({target})")
    return "\n".join(lines)


def main() -> None:
    body = "\n\n".join(subject_section(name, icon) for name, icon in SUBJECTS)
    replacement = f"{START}\n\n{body}\n\n{END}"
    text = README.read_text(encoding="utf-8")
    pattern = re.escape(START) + r".*?" + re.escape(END)
    if not re.search(pattern, text, flags=re.DOTALL):
        raise SystemExit("README markers are missing; refusing to overwrite the file.")
    updated = re.sub(pattern, replacement, text, flags=re.DOTALL)
    README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
