# Hire-ready portfolio program

Goal: make https://solomonsmith.dev convert hiring managers ASAP for full-time AI/ML and backend roles starting January 2027.

## Rule

**Decision interviews always before moving forward** past a major gate (`decisions/`).

## Structure

| Path | Contents |
| --- | --- |
| `plan/` | 20 tasks × 20-step plans + 10 completion subtasks |
| `decisions/` | DI-01..DI-20 interview records |
| `audit/` | Baseline and before/after evidence |
| `scripts/generate_plan.py` | Regenerates the plan files |

## Current gate

**DI-01 Positioning** is `open`. No hero/about/outreach edits until it is locked.

## Quick commands

```bash
python3 docs/hire-ready/scripts/generate_plan.py
```

## Tooling

```bash
python3 docs/hire-ready/scripts/generate_plan.py
python3 docs/hire-ready/scripts/validate_decisions.py --require DI-01
python3 docs/hire-ready/scripts/link_qa.py
```

## Provisional artifacts (no public site edits yet)

- `audit/link-qa.md` -- live links currently clean
- `audit/proof-density.md` -- all 7 cards have fact rows
- `audit/skim-90s.md` -- employer path draft
- `outreach/` -- cold email + LinkedIn blurb drafts
