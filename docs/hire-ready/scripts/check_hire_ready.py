#!/usr/bin/env python3
"""One-shot hire-ready checks for this branch (not a substitute for DI locks)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HR = ROOT / "docs" / "hire-ready"
errors: list[str] = []
warns: list[str] = []


def ok(msg: str) -> None:
    print(f"OK  {msg}")


def err(msg: str) -> None:
    errors.append(msg)
    print(f"ERR {msg}")


def warn(msg: str) -> None:
    warns.append(msg)
    print(f"WARN {msg}")


def main() -> int:
    # Plan structure
    master = json.loads((HR / "plan" / "master-plan.json").read_text())
    if len(master["tasks"]) != 20:
        err(f"expected 20 tasks, got {len(master['tasks'])}")
    else:
        ok("20 tasks")
    for t in master["tasks"]:
        if len(t["steps"]) != 20:
            err(f"{t['id']} has {len(t['steps'])} steps")
    else:
        ok("20 steps each")
    if len(master["completion_subtasks"]) != 10:
        err("expected 10 completion subtasks")
    else:
        ok("10 completion subtasks")

    # Decisions
    index = json.loads((HR / "decisions" / "index.json").read_text())
    if len(index["interviews"]) < 20:
        err("expected >=20 decision interviews")
    else:
        ok(f"{len(index['interviews'])} decision interviews indexed")
    di1 = json.loads((HR / "decisions" / "DI-01-positioning.json").read_text())
    if di1.get("status") not in {"provisional", "locked"}:
        err("DI-01 must be provisional or locked before hire conversion ships")
    else:
        ok(f"DI-01 status={di1.get('status')}")
    if di1.get("status") != "locked":
        warn("DI-01 not Solomon-locked yet")

    # Hero CTA order
    home = (ROOT / "_layouts" / "home.html").read_text()
    order = re.findall(r'class="btn[^"]*"[^>]*>([^<]+)</a>', home)
    # first btn-row only
    m = re.search(r'class="btn-row">(.*?)</div>', home, re.S)
    labels = re.findall(r">([^<]+)</a>", m.group(1)) if m else []
    if labels[:3] != ["Email me", "Download resume", "View selected work"]:
        err(f"hero CTA order unexpected: {labels[:3]}")
    else:
        ok("hero CTA Email → Resume → Work")

    header = (ROOT / "_layouts" / "default.html").read_text()
    if "Resume</a>" not in header or "Contact</a>" not in header:
        err("header missing Resume/Contact")
    else:
        ok("header Resume + Contact")

    # Constraints grep on content surfaces
    paths = list((ROOT / "_projects").glob("*.md")) + [
        ROOT / "index.md",
        ROOT / "about.md",
        ROOT / "projects.md",
        ROOT / "resume.md",
        ROOT / "_layouts" / "home.html",
        ROOT / "_layouts" / "default.html",
    ]
    paths += list((ROOT / "_includes").glob("card-*.html"))
    banned = re.compile(r"(—|\binternship\b|\bgpa\b|dean.?s list|langchain)", re.I)
    for p in paths:
        text = p.read_text()
        if banned.search(text):
            # allow CLAUDE-style negatives? these files shouldn't have them
            err(f"banned pattern in {p.relative_to(ROOT)}")
    else:
        ok("no banned patterns in core content surfaces")

    # PhishGuard serving claim
    pg = (ROOT / "_projects" / "phishguard.md").read_text()
    if re.search(r"exported to ONNX and served", pg, re.I):
        err("PhishGuard still claims ONNX serving in lede")
    if "not ONNX as production serving" not in pg and "scaffolded" not in pg.lower():
        warn("PhishGuard missing explicit ONNX scaffold note")
    else:
        ok("PhishGuard ONNX not claimed as production serving")

    # Evidence tables
    for p in (ROOT / "_projects").glob("*.md"):
        if "{: .evidence}" not in p.read_text():
            err(f"missing evidence table: {p.name}")
    else:
        ok("all project pages have evidence tables")

    print()
    print(f"{len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
