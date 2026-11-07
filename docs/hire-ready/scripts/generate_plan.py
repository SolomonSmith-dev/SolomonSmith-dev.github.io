#!/usr/bin/env python3
"""Generate 20 hire-ready portfolio tasks × 20 steps + 10 completion gates."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "plan"

TASKS = [
    ("T01", "Positioning lock for Jan 2027 full-time AI/ML + backend", "DI-01", "Freeze target role, geography, and one-line thesis."),
    ("T02", "Decision interview system for portfolio changes", "DI-02", "Require recorded interviews before major site moves."),
    ("T03", "Hero and first-viewport conversion pass", "DI-03", "Make the home hero hire-first in under 5 seconds."),
    ("T04", "Selected work ordering and proof density", "DI-04", "Put the strongest employer-facing proof above the fold."),
    ("T05", "Project pages: evidence tables and reproducible numbers", "DI-05", "Every project page cites README/resume-backed numbers only."),
    ("T06", "Resume page + PDF sync fidelity", "DI-06", "Resume surfaces match canonical MATERIALS without hand edits."),
    ("T07", "About page narrative for hiring managers", "DI-07", "About sells judgment, not biography filler."),
    ("T08", "Contact path speed and friction kill", "DI-08", "Email/LinkedIn/resume CTAs are impossible to miss."),
    ("T09", "Skills truth and stack tags audit", "DI-09", "Skills match resume SKILLS; no banned stacks."),
    ("T10", "SEO, OG, llms.txt, and social cards", "DI-10", "Search and link previews sell the same hire thesis."),
    ("T11", "Performance and Core Web Vitals on mobile", "DI-11", "Home/projects/resume feel instant on mid phones."),
    ("T12", "Accessibility and focus polish", "DI-12", "Keyboard, contrast, skip link, aria-current all solid."),
    ("T13", "Screenshots and demo proof for top projects", "DI-13", "Top projects have visual or Loom proof where allowed."),
    ("T14", "GitHub pin slate ↔ site project slate alignment", "DI-14", "Pins and site cards tell one coherent story."),
    ("T15", "Writing index signal (no fake posts)", "DI-15", "Blog/index either helps hiring or stays minimal honestly."),
    ("T16", "Broken link / 404 / redirect QA", "DI-16", "No dead CTAs; /card/ and resume PDF resolve."),
    ("T17", "Employer skim path (90-second script)", "DI-17", "Document and verify a 90s hiring-manager path."),
    ("T18", "Outreach kit: email + LinkedIn blurb from site facts", "DI-18", "Reusable outreach copy sourced only from site numbers."),
    ("T19", "Launch checklist and Pages deploy verification", "DI-19", "main build green; live site matches branch intent."),
    ("T20", "Weekly hire-ready maintenance loop", "DI-20", "Activity, resume sync, and proof stay current."),
]

GENERIC_STEPS = [
    "Restate the task goal in one sentence",
    "List current repo files that own this outcome",
    "Capture baseline screenshots or metrics",
    "Run Decision Interview for this task gate",
    "Write acceptance criteria checklist",
    "Inventory CLAUDE.md constraints that apply",
    "Draft the smallest change set",
    "Implement change set on feature branch",
    "Self-review for em dashes, GPA, internship language, banned skills",
    "Cross-check every number against README/resume sources",
    "Update related surfaces (home/about/projects/resume) for consistency",
    "Build or smoke-check locally if feasible",
    "Mobile pass for this surface",
    "Accessibility pass for this surface",
    "Record before/after evidence in docs/hire-ready/audit/",
    "Update plan/status.json steps_done",
    "Peer/self hiring-manager skim of the changed path",
    "Commit with descriptive message (no em dashes)",
    "Push and refresh PR notes",
    "Mark task complete only after gate interview is locked",
]

COMPLETION = [
    ("C01", "DI-01 positioning locked", "decisions/DI-01 status=locked"),
    ("C02", "All major gates have interview records", "validate_decisions passes for required DIs"),
    ("C03", "Hero converts in skim test", "90s path notes + screenshot evidence"),
    ("C04", "Top 4 project cards proof-dense", "each card has Problem/Built/Result with sourced facts"),
    ("C05", "All project pages evidence-clean", "no unsourced numbers; evidence tables present"),
    ("C06", "Resume PDF + page synced", "sync script output or verified match to canonical"),
    ("C07", "Contact path <2 clicks from home", "CTA audit screenshot"),
    ("C08", "Live Lighthouse/a11y bar met", "recorded scores for home + projects"),
    ("C09", "Outreach kit ready", "email + LinkedIn blurb files exist"),
    ("C10", "Live site hire-ready verified", "solomonsmith.dev matches accepted PR; checklist green"),
]


def main() -> None:
    PLAN.mkdir(parents=True, exist_ok=True)
    tasks = []
    for tid, title, gate, goal in TASKS:
        steps = []
        for i, action in enumerate(GENERIC_STEPS, 1):
            # Specialize a few steps with task goal language
            act = action
            if i == 1:
                act = f"Restate goal: {goal}"
            if i == 4:
                act = f"Complete decision interview {gate} before implementing"
            if i == 20:
                act = f"Mark {tid} complete only after {gate} is locked"
            steps.append(
                {
                    "step": i,
                    "action": act,
                    "exit_criteria": f"Artifact or status update proves step {i} for {tid}",
                }
            )
        tasks.append(
            {
                "id": tid,
                "title": title,
                "goal": goal,
                "decision_interview": gate,
                "status": "pending",
                "steps": steps,
            }
        )

    master = {
        "project": "hire-ready-portfolio",
        "objective": "Complete professional personal portfolio to get hired ASAP",
        "rule": "Decision interviews always before moving forward past a major gate",
        "constraints_from_site": [
            "No em dashes",
            "No GPA / Dean's List",
            "No internship language on site",
            "Target: full-time AI/ML + backend from January 2027",
            "Numbers only from resume or project READMEs",
            "No Recursa internship metrics",
            "ARDA uses LangGraph not LangChain",
        ],
        "tasks": tasks,
        "completion_subtasks": [
            {"id": c[0], "title": c[1], "done_when": c[2]} for c in COMPLETION
        ],
    }
    (PLAN / "master-plan.json").write_text(json.dumps(master, indent=2) + "\n")

    idx = [
        "# Hire-ready portfolio master plan",
        "",
        "Decision interviews always before moving forward.",
        "",
        "## 10 completion subtasks",
        "",
    ]
    for c in COMPLETION:
        idx += [f"### {c[0]}: {c[1]}", "", f"- Done when: {c[2]}", ""]
    idx += ["## 20 tasks", ""]
    for t in tasks:
        path = f"{t['id']}.md"
        lines = [
            f"# {t['id']}: {t['title']}",
            "",
            f"**Goal:** {t['goal']}",
            f"**Decision interview:** {t['decision_interview']}",
            "",
            "## 20-step completion plan",
            "",
        ]
        for s in t["steps"]:
            lines += [
                f"### Step {s['step']}: {s['action']}",
                "",
                f"- Exit criteria: {s['exit_criteria']}",
                "",
            ]
        (PLAN / path).write_text("\n".join(lines))
        idx.append(f"1. [{t['id']}: {t['title']}]({path}) — `{t['decision_interview']}`")
    (PLAN / "README.md").write_text("\n".join(idx) + "\n")
    status = {
        "active_gate": "DI-01",
        "tasks": {t["id"]: {"status": "pending", "steps_done": 0} for t in tasks},
        "completion_subtasks": {c[0]: "pending" for c in COMPLETION},
    }
    (PLAN / "status.json").write_text(json.dumps(status, indent=2) + "\n")
    print(f"wrote {len(tasks)} tasks x {len(tasks[0]['steps'])} steps, {len(COMPLETION)} completion gates")


if __name__ == "__main__":
    main()
