#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
THEMES = list((ROOT / "themes").rglob("*.json"))
README = (ROOT / "README.md").read_text(encoding="utf-8")

# 1) JSON parse
bad = []
for p in THEMES:
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        bad.append((p, str(e)))

if bad:
    print("Invalid JSON files:")
    for p, e in bad:
        print(f" - {p.relative_to(ROOT)}: {e}")
    sys.exit(1)

# 2) README image paths exist
paths = re.findall(r"\!\[[^\]]*\]\(([^)]+)\)", README)
missing = []
for rel in paths:
    # Ignore URLs if any
    if "://" in rel:
        continue
    p = ROOT / rel
    if not p.exists():
        missing.append(rel)

if missing:
    print("Missing README images:")
    for m in missing:
        print(f" - {m}")
    sys.exit(1)

print("OK: JSON valid and README images resolved.")
