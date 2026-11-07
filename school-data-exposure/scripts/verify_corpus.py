#!/usr/bin/env python3
"""Verification QA for evidence corpus and publishable findings."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "evidence" / "sources"
FINDINGS = ROOT / "evidence" / "findings"
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    re.compile(r"\bapi[_-]?key\b\s*[:=]\s*\S+", re.I),
    re.compile(r"\bbearer\s+[a-z0-9\-_\.]{20,}", re.I),
    re.compile(r"\beyJ[a-zA-Z0-9_-]{20,}\.[a-zA-Z0-9_-]{10,}\."),
]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    sources = {json.loads(p.read_text())["id"]: json.loads(p.read_text()) for p in SOURCES.glob("SRC-*.json")}
    # reload cleanly
    sources = {}
    for p in SOURCES.glob("SRC-*.json"):
        sources[json.loads(p.read_text())["id"]] = json.loads(p.read_text())

    for sid, s in sources.items():
        for field in ("id", "title", "url", "retrieved_at", "sha256"):
            if not s.get(field):
                errors.append(f"{sid} missing {field}")
        if len(s.get("sha256", "")) != 64:
            errors.append(f"{sid} sha256 not 64 hex chars")

    findings = []
    for p in FINDINGS.glob("FIND-*.json"):
        f = json.loads(p.read_text())
        findings.append(f)
        if f.get("claim_grade") not in {"Alleged", "Documented", "Verified"}:
            errors.append(f"{f.get('id')} bad claim_grade")
        if f.get("claim_grade") in {"Documented", "Verified"}:
            eids = f.get("evidence_ids") or []
            if not eids:
                errors.append(f"{f.get('id')} Documented/Verified without evidence_ids")
            for eid in eids:
                if eid not in sources:
                    errors.append(f"{f.get('id')} cites missing evidence {eid}")

    # secret scan over text artifacts
    for path in ROOT.rglob("*"):
        if path.is_dir():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}:
            continue
        if "node_modules" in path.parts:
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                errors.append(f"possible secret in {path.relative_to(ROOT)}")
                break

    documented = [f for f in findings if f.get("claim_grade") in {"Documented", "Verified"}]
    report = {
        "sources": len(sources),
        "findings": len(findings),
        "documented_or_verified": len(documented),
        "errors": errors,
        "warnings": warnings,
        "pass": not errors,
    }
    out = ROOT / "evidence" / "verification-report.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
