#!/usr/bin/env python3
"""Public-release hygiene checks.

This is intentionally conservative. It catches files and text patterns that
should not appear in a clean-room public repository: local caches, private
paths, email addresses, and binary source packs that are hard to audit.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_SUFFIXES = {
    ".p",
    ".fig",
    ".mat",
    ".doc",
    ".docx",
    ".pdf",
    ".xls",
    ".xlsx",
    ".opj",
    ".opju",
    ".otpu",
    ".zip",
    ".rar",
    ".7z",
}

FORBIDDEN_NAMES = {
    ".DS_Store",
}

TEXT_SUFFIXES = {
    ".m",
    ".py",
    ".md",
    ".txt",
    ".json",
    ".yml",
    ".yaml",
    ".sh",
    ".html",
    ".css",
    ".mod",
}

TEXT_PATTERNS = [
    ("private macOS path", re.compile(r"/Users/")),
    ("email address", re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")),
    ("phone-like number", re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")),
    ("copied author marker", re.compile(r"\bAuthor\s*:", re.IGNORECASE)),
    ("copied copyright marker", re.compile(r"\bCopyright\b(?! \(c\) 2026 Research Figure Function Library Contributors)", re.IGNORECASE)),
]


def iter_files() -> list[Path]:
    ignored_parts = {".git", ".pytest_cache", "__pycache__", ".venv", "venv"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        files.append(path)
    return files


def main() -> int:
    problems: list[str] = []
    for path in iter_files():
        rel = path.relative_to(ROOT)
        if path.name in FORBIDDEN_NAMES:
            problems.append(f"forbidden local file: {rel}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            problems.append(f"forbidden public suffix {path.suffix}: {rel}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            if rel == Path("scripts/check_publication_ready.py"):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                problems.append(f"text file is not UTF-8: {rel}")
                continue
            for label, pattern in TEXT_PATTERNS:
                if pattern.search(text):
                    problems.append(f"{label}: {rel}")

    if problems:
        print("Publication readiness check failed:")
        for item in problems:
            print(f"- {item}")
        return 1

    print("Publication readiness check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
