#!/usr/bin/env python3
"""Validate hire-ready decision interview gates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEC = Path(__file__).resolve().parents[1] / "decisions"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require", nargs="*", default=["DI-01"])
    parser.add_argument("--allow-provisional", action="store_true")
    parser.add_argument("--strict-locked", action="store_true")
    args = parser.parse_args()

    index = json.loads((DEC / "index.json").read_text())
    by_id = {i["id"]: i for i in index["interviews"]}
    errors: list[str] = []

    for req in args.require:
        meta = by_id.get(req)
        if not meta:
            errors.append(f"missing from index: {req}")
            continue
        path = DEC / meta["file"]
        if not path.exists():
            errors.append(f"missing file: {meta['file']}")
            continue
        data = json.loads(path.read_text())
        status = data.get("status") or meta.get("status")
        if status == "open":
            errors.append(f"{req} is open; interview required before forward move")
        elif status == "blocked":
            errors.append(f"{req} is blocked")
        elif args.strict_locked and status != "locked":
            errors.append(f"{req} status={status}; need locked")
        elif status == "provisional" and not args.allow_provisional and not args.strict_locked:
            # provisional OK only when explicitly allowed
            errors.append(f"{req} is provisional; pass --allow-provisional or lock it")
        elif status not in {"provisional", "locked", "open", "blocked"}:
            errors.append(f"{req} invalid status={status}")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"- {e}")
        return 1
    print("OK")
    for req in args.require:
        data = json.loads((DEC / by_id[req]["file"]).read_text())
        print(f"- {req}: {data.get('status')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
