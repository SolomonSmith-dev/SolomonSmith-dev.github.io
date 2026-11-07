# Launch checklist (C10)

**DI-19:** locked `yes_after_ci` + `live_verify: required`  
**PR:** https://github.com/SolomonSmith-dev/SolomonSmith-dev.github.io/pull/12

## Pre-merge

- [x] DI-01..DI-20 locked (keep-current)
- [x] `check_hire_ready.py` 0 errors
- [x] Local Lighthouse mobile: home 90/100/100/100; projects & resume 100s
- [ ] CI green on `cursor/hire-ready-portfolio-58be`
- [ ] Merge PR #12 into `main`

## Post-merge live verify (https://solomonsmith.dev)

- [ ] Home hero CTA order: Email me → Download resume → View selected work
- [ ] Mobile header shows Contact
- [ ] CourtRules / ARDA / SOC / Sentinel selected work present
- [ ] Resume PDF downloads
- [ ] PhishGuard project page does not claim ONNX as production serving
- [ ] No em dashes / internship / GPA on hire surfaces

## C10 status

**pending** until live checks above are green after Pages deploy
