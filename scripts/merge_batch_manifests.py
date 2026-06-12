#!/usr/bin/env python3
"""Merge _batch_manifests/*.txt into _manifest_source.txt.

Batch files use the same format as _manifest_source.txt:
    name|category|tag1,tag2|description

The merge is idempotent and fails on malformed rows, duplicate batch entries,
or missing Python/MATLAB template files.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "_manifest_source.txt"
BATCH_DIR = ROOT / "_batch_manifests"
PY_DIR = ROOT / "templates" / "python"
M_DIR = ROOT / "templates" / "matlab"
NAME_RE = re.compile(r"^[a-z0-9_]+$")


def rows_from(path: Path) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for ln, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("|")
        if len(parts) != 4:
            raise SystemExit(f"{path}:{ln}: expected 4 fields: {line!r}")
        name, category, tags, desc = [p.strip() for p in parts]
        if not NAME_RE.match(name):
            raise SystemExit(f"{path}:{ln}: bad template name: {name!r}")
        if not category or not tags or not desc:
            raise SystemExit(f"{path}:{ln}: empty category/tags/description")
        if not (PY_DIR / f"{name}.py").exists():
            raise SystemExit(f"{path}:{ln}: missing Python template for {name}")
        if not (M_DIR / f"{name}.m").exists():
            raise SystemExit(f"{path}:{ln}: missing MATLAB template for {name}")
        out.append((name, f"{name}|{category}|{tags}|{desc}"))
    return out


def batch_sort_key(path: Path) -> tuple[int, str]:
    m = re.search(r"S(\d+)", path.stem)
    return (int(m.group(1)) if m else 9999, path.name)


def main() -> int:
    source_lines = SOURCE.read_text(encoding="utf-8").splitlines()
    existing = {
        line.split("|", 1)[0].strip()
        for line in source_lines
        if line.strip() and not line.startswith("#")
    }

    batch_rows: list[tuple[str, str]] = []
    seen_batch: set[str] = set()
    for path in sorted(BATCH_DIR.glob("*.txt"), key=batch_sort_key):
        for name, line in rows_from(path):
            if name in seen_batch:
                raise SystemExit(f"duplicate batch entry: {name}")
            seen_batch.add(name)
            batch_rows.append((name, line))

    appended = [line for name, line in batch_rows if name not in existing]
    if appended:
        text = "\n".join(source_lines).rstrip() + "\n" + "\n".join(appended) + "\n"
        SOURCE.write_text(text, encoding="utf-8")

    print(f"batch rows: {len(batch_rows)}; appended: {len(appended)}; source total: {len(existing) + len(appended)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
