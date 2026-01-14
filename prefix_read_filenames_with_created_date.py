#!/usr/bin/env python3
"""
Prefix filenames in the 'read/' folder with their filesystem created date.

Example:
  read/MyPaper.md  ->  read/2026-01-01_MyPaper.md

Rules:
  - If a filename already starts with a YYYY-MM-DD prefix, it is skipped.
  - Uses the filesystem "birth time" when available (macOS st_birthtime).
    Falls back to st_ctime (metadata change time on Unix; creation time on Windows).
  - Avoids overwriting existing files by appending __N if needed.

Usage:
  python prefix_read_filenames_with_created_date.py --dry-run
  python prefix_read_filenames_with_created_date.py
  python prefix_read_filenames_with_created_date.py --dir read --glob "*.md"
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from pathlib import Path


DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([_\-\s].*)?$")


def has_date_prefix(name: str) -> bool:
    # Accept "YYYY-MM-DD" alone, or "YYYY-MM-DD_<rest>", "YYYY-MM-DD-<rest>", "YYYY-MM-DD <rest>"
    return bool(DATE_PREFIX_RE.match(name))


def created_date(path: Path) -> dt.date:
    st = path.stat()
    # macOS: st_birthtime exists and is the actual creation time.
    birth = getattr(st, "st_birthtime", None)
    ts = birth if isinstance(birth, (int, float)) else st.st_ctime
    return dt.datetime.fromtimestamp(ts).date()


def unique_target(target: Path) -> Path:
    if not target.exists():
        return target
    stem, suffix = target.stem, target.suffix
    parent = target.parent
    i = 1
    while True:
        cand = parent / f"{stem}__{i}{suffix}"
        if not cand.exists():
            return cand
        i += 1


def iter_files(base_dir: Path, glob_pat: str) -> list[Path]:
    # Only files directly under base_dir (not recursive) to avoid surprising renames.
    return sorted([p for p in base_dir.glob(glob_pat) if p.is_file()])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prefix files in 'read/' with their created date (YYYY-MM-DD_)."
    )
    parser.add_argument(
        "--dir",
        default="read",
        help="Directory to process (default: read).",
    )
    parser.add_argument(
        "--glob",
        default="*",
        help='Filename glob to include (default: "*"). Example: "*.md"',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned renames without changing anything.",
    )
    args = parser.parse_args()

    base_dir = Path(args.dir).expanduser().resolve()
    if not base_dir.exists():
        raise SystemExit(f"Directory not found: {base_dir}")
    if not base_dir.is_dir():
        raise SystemExit(f"Not a directory: {base_dir}")

    files = iter_files(base_dir, args.glob)
    if not files:
        print(f"No files matched {args.glob!r} in {str(base_dir)!r}.")
        return 0

    planned: list[tuple[Path, Path]] = []
    for src in files:
        if has_date_prefix(src.name):
            continue
        d = created_date(src).strftime("%Y-%m-%d")
        dst = src.with_name(f"{d}_{src.name}")
        dst = unique_target(dst)
        planned.append((src, dst))

    if not planned:
        print("Nothing to do (all files already appear prefixed).")
        return 0

    for src, dst in planned:
        rel_src = os.path.relpath(src, base_dir.parent)
        rel_dst = os.path.relpath(dst, base_dir.parent)
        if args.dry_run:
            print(f"[dry-run] {rel_src} -> {rel_dst}")
        else:
            src.rename(dst)
            print(f"{rel_src} -> {rel_dst}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
