# School Data Exposure

Investigative / technical-audit project that documents how school systems collect, use, and abuse student data -- starting with a provisional CSUSB case.

## Hard rules

- Decision interviews always before moving forward past a major gate
- No unauthorized access, no doxxing, no secret dumps
- Public sources first; own-account observations only with redaction
- Not legal advice

## Deliverables in this repo folder

| Path | What it is |
| --- | --- |
| `plan/` | 20 tasks × 20-step plans + 10 completion subtasks |
| `decisions/` | Decision interview files (DI-01..DI-21) |
| `evidence/` | Hashed sources, findings, vendor map, data-flow graph |
| `web/` | Public exposé static site |
| `toolkit/` | Student self-audit checklist + request template |
| `charter.md` | Legal/ethics charter (pending DI-02) |

## Quickstart

```bash
python3 scripts/generate_plan.py
python3 scripts/validate_decisions.py --require DI-01
python3 scripts/build_site_data.py
python3 -m http.server 8765 --directory web
```

Open http://127.0.0.1:8765/

## Ingest a public source

```bash
python3 scripts/ingest_evidence.py \
  --url "https://www.csusb.edu/about-csusb/privacy-and-security-notice" \
  --title "CSUSB Privacy and Security Notice" \
  --type policy
python3 scripts/build_site_data.py
```

## Current gate

**DI-01 Scope Lock** is `provisional`. Confirm or revise answers before locking public naming and finishing T03.

## Plan counts

- 20 primary tasks (`plan/T01.md` … `plan/T20.md`)
- 20 completion steps per task
- 10 completion subtasks (`plan/README.md`)
- 21 decision interviews (DI-01 required before target lock; DI-02..DI-21 gate later tasks)
