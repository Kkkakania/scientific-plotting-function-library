#!/usr/bin/env python3
"""Check release metadata stays in sync.

This catches the easy-to-miss drift between manifest.json, README snippets,
API docs, gallery outputs, and palette metadata.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "2.0"


def fail(problems: list[str], message: str) -> None:
    problems.append(message)


def main() -> int:
    problems: list[str] = []

    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    templates = manifest["templates"]
    names = [item["name"] for item in templates]
    count = len(names)

    if manifest.get("version") != EXPECTED_VERSION:
        fail(problems, f"manifest version is {manifest.get('version')!r}, expected {EXPECTED_VERSION!r}")
    if manifest.get("count") != count:
        fail(problems, f"manifest count field {manifest.get('count')} != template list length {count}")

    py_files = {p.stem for p in (ROOT / "templates" / "python").glob("*.py")}
    m_files = {p.stem for p in (ROOT / "templates" / "matlab").glob("*.m")}
    missing_py = sorted(set(names) - py_files)
    missing_m = sorted(set(names) - m_files)
    extra_py = sorted(py_files - set(names))
    extra_m = sorted(m_files - set(names))
    for label, items in (
        ("missing Python templates", missing_py),
        ("missing MATLAB templates", missing_m),
        ("extra Python templates", extra_py),
        ("extra MATLAB templates", extra_m),
    ):
        if items:
            fail(problems, f"{label}: {items[:12]}")

    gallery = ROOT / "gallery"
    missing_gallery = [name for name in names if not (gallery / f"{name}.png").exists()]
    if missing_gallery:
        fail(problems, f"missing gallery PNGs: {missing_gallery[:12]}")
    dark_dir = gallery / "dark"
    if dark_dir.exists():
        missing_dark = [name for name in names if not (dark_dir / f"{name}.png").exists()]
        if missing_dark:
            fail(problems, f"missing dark gallery PNGs: {missing_dark[:12]}")

    sys.path.insert(0, str(ROOT / "palettes" / "python"))
    from sci_palettes import PALETTES_CAT, PALETTES_SEQ, PALETTES_DIV, PALETTES_CYC  # noqa: WPS433

    palette_count = sum(map(len, (PALETTES_CAT, PALETTES_SEQ, PALETTES_DIV, PALETTES_CYC)))

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    api = (ROOT / "docs" / "api_reference.md").read_text(encoding="utf-8")
    palette_readme = (ROOT / "palettes" / "README.md").read_text(encoding="utf-8")
    for file_label, text in (("README.md", readme), ("docs/api_reference.md", api)):
        if str(count) not in text:
            fail(problems, f"{file_label} does not mention template count {count}")
        if EXPECTED_VERSION not in text:
            fail(problems, f"{file_label} does not mention version {EXPECTED_VERSION}")
    if str(palette_count) not in readme:
        fail(problems, f"README.md does not mention palette count {palette_count}")
    if str(palette_count) not in palette_readme:
        fail(problems, f"palettes/README.md does not mention palette count {palette_count}")
    if not (ROOT / "palettes" / "palette_picker.html").exists():
        fail(problems, "palettes/palette_picker.html is missing")

    if problems:
        print("Release state check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(
        f"Release state check passed: v{EXPECTED_VERSION}, "
        f"{count} templates, {palette_count} palettes."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
