# Resume sync audit

## Environment

`~/Projects/swe-job-hunt/MATERIALS` is **not available** in this cloud VM, so `scripts/sync-resume.sh` cannot be run here.

## DI-06

Locked as `yes_in_repo_fidelity` with MATERIALS sync deferred to Solomon's machine.

## Verified in-repo (PDF ↔ resume.md)

- PASS: 1,653 judges
- PASS: 577 tests/ARDA
- PASS: AUC 0.9943
- PASS: Founding Engineer
- PASS: LangGraph
- PASS: phone omitted on page

- `assets/resume/SolomonSmithResume.pdf` present
- Download CTAs on resume page and home/header
- Site content grep clean for internship / GPA / Dean's List
- Skills include LangGraph (not LangChain); lists ONNX Runtime as a skill

## Residual (non-blocking for live hire path)

- Solomon should run `scripts/sync-resume.sh` on a machine with MATERIALS when the canonical resume changes
- PDF/resume.md still say PhishGuard is "served via FastAPI with ONNX Runtime"; CLAUDE.md treats ONNX as scaffolded for the **project page**. Project pages were aligned; resume remains MATERIALS-owned (do not hand-edit)

## C06 status

**met_in_repo_fidelity** (MATERIALS sync residual documented)
