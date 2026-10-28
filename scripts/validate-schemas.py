#!/usr/bin/env python3
"""Validate JSON files against schemas/ (Draft 2020-12).

Usage:
  python3 scripts/validate-schemas.py [file.json ...]
  python3 scripts/validate-schemas.py --schema manifest path/to/manifest.json

Without args, validates sketchmind-template/manifest.json against manifest.schema.json.
Requires: pip install jsonschema  (optional; falls back to structural checks only)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def basic_manifest_checks(data: dict) -> list[str]:
    errs = []
    if not isinstance(data, dict):
        return ["root must be object"]
    for k in ("version", "updatedAt", "items"):
        if k not in data:
            errs.append(f"missing required key: {k}")
    items = data.get("items")
    if not isinstance(items, list):
        errs.append("items must be array")
        return errs
    for i, it in enumerate(items):
        if not isinstance(it, dict):
            errs.append(f"items[{i}] not object")
            continue
        for k in ("id", "title", "url"):
            if k not in it:
                errs.append(f"items[{i}] missing {k}")
        url = it.get("url", "")
        if isinstance(url, str) and not (url.startswith("http://") or url.startswith("https://")):
            errs.append(f"items[{i}].url must be http(s): {url!r}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--schema", default="manifest", help="schema stem under schemas/")
    args = ap.parse_args()
    files = args.files or [ROOT / "sketchmind-template" / "manifest.json"]
    schema_path = SCHEMAS / f"{args.schema}.schema.json"
    if not schema_path.exists():
        print(f"schema not found: {schema_path}", file=sys.stderr)
        return 2

    schema = load_json(schema_path)
    try:
        import jsonschema
        from jsonschema import Draft202012Validator
        validator_cls = Draft202012Validator
        use_jsonschema = True
    except ImportError:
        use_jsonschema = False
        print("note: jsonschema not installed; using built-in manifest checks only", file=sys.stderr)

    rc = 0
    for f in files:
        data = load_json(f)
        if use_jsonschema:
            v = validator_cls(schema)
            errors = sorted(v.iter_errors(data), key=lambda e: list(e.path))
            if errors:
                rc = 1
                print(f"FAIL {f}")
                for e in errors:
                    path = "/".join(str(p) for p in e.path) or "(root)"
                    print(f"  - {path}: {e.message}")
            else:
                print(f"OK   {f}")
        else:
            if args.schema != "manifest":
                print(f"SKIP {f} (install jsonschema for non-manifest schemas)")
                continue
            errs = basic_manifest_checks(data)
            if errs:
                rc = 1
                print(f"FAIL {f}")
                for e in errs:
                    print(f"  - {e}")
            else:
                print(f"OK   {f}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
