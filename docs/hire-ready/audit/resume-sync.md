# Resume sync audit

## Environment

`~/Projects/swe-job-hunt/MATERIALS` is **not available** in this cloud VM, so `scripts/sync-resume.sh` cannot be run here.

## Verified in-repo

- `assets/resume/SolomonSmithResume.pdf` present
- `resume.md` front matter + body present; phone omitted from contact line
- Download CTAs on resume page and (after this PR) home/header
- Site content grep clean for internship / GPA / Dean's List
- Skills include has LangGraph (not LangChain); lists ONNX Runtime as a skill

## Residual

- Solomon should run `scripts/sync-resume.sh` on a machine with MATERIALS before calling C06 fully green
- Confirm PDF text matches latest canonical resume offline
