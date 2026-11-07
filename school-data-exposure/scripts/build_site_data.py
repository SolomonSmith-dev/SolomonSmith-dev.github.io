#!/usr/bin/env python3
"""Compile evidence + plan status into web/data for the static site."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB_DATA = ROOT / "web" / "data"


def load_json_dir(path: Path, prefix: str) -> list[dict]:
    items = []
    if not path.exists():
        return items
    for f in sorted(path.glob(f"{prefix}*.json")):
        items.append(json.loads(f.read_text()))
    return items


def main() -> None:
    WEB_DATA.mkdir(parents=True, exist_ok=True)
    sources = load_json_dir(ROOT / "evidence" / "sources", "SRC-")
    findings = load_json_dir(ROOT / "evidence" / "findings", "FIND-")
    vendors = json.loads((ROOT / "evidence" / "vendors.json").read_text())
    graph = json.loads((ROOT / "evidence" / "graph.json").read_text())
    decisions = json.loads((ROOT / "decisions" / "index.json").read_text())
    status = json.loads((ROOT / "plan" / "status.json").read_text())
    completion = json.loads((ROOT / "plan" / "master-plan.json").read_text())["completion_subtasks"]

    payload = {
        "project": "school-data-exposure",
        "target_provisional": "CSUSB",
        "disclaimer": "Not legal advice. Public-source research plus optional own-account audit only. No unauthorized access.",
        "sources": sources,
        "findings": findings,
        "vendors": vendors,
        "graph": graph,
        "decisions": decisions,
        "status": status,
        "completion_subtasks": completion,
        "stats": {
            "sources": len(sources),
            "findings": len(findings),
            "vendors": len(vendors.get("vendors", [])),
            "decision_interviews": len(decisions.get("interviews", [])),
            "documented_findings": sum(1 for f in findings if f.get("claim_grade") in {"Documented", "Verified"}),
        },
    }
    (WEB_DATA / "site.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload["stats"], indent=2))


if __name__ == "__main__":
    main()
