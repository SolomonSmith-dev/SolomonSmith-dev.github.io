#!/usr/bin/env python3
"""Validate decision interview gate state.

Exit 0 if required interviews are provisional or locked.
Exit 1 if a required interview is missing or open when --strict-locked is set.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEC = ROOT / "decisions"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require", nargs="*", default=["DI-01"], help="Interview IDs that must exist")
    parser.add_argument("--strict-locked", action="store_true", help="Require status=locked (not provisional)")
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
            errors.append(f"missing file: {path.name}")
            continue
        data = json.loads(path.read_text())
        status = data.get("status") or meta.get("status")
        if status == "open":
            errors.append(f"{req} is open; decision interview required before forward move")
        elif args.strict_locked and status != "locked":
            errors.append(f"{req} status={status}; need locked")
        elif status not in {"provisional", "locked"}:
            errors.append(f"{req} has invalid status={status}")

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
    sys.exit(main())
