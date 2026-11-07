# Demo checklist (publishable research demo)

## Start

```bash
python3 scripts/validate_decisions.py --require DI-01 DI-02 DI-03
python3 scripts/verify_corpus.py
python3 scripts/build_site_data.py
python3 -m http.server 8765 --directory web
```

Open http://127.0.0.1:8765/

## Walkthrough (3 minutes)

1. **Home** — thesis + live stats (sources / findings / vendors)
2. **Findings** — open FIND-010 (Respondus webcam), FIND-008 (vendor sharing), FIND-012 (Instructure Identity hop)
3. **Case file** — executive narrative
4. **Map** — green edges are Documented flows (Canvas apps, GA, identity)
5. **Methods** — decision interview log (provisional vs blocked)
6. **Toolkit** — self-audit + CPRA pack (do not send until DI-12)

## What this demo proves

- Public evidence can expose LMS + proctoring + analytics without hacking
- Claim grades and hashed sources keep the project legally careful
- Decision interviews gate risky moves (own-account, CPRA send, launch)

## What it does not prove yet

- Live third-party requests inside an authenticated Canvas session (needs DI-10)
- Contract text / retention schedules (needs DI-12 responses)
- Portfolio launch on solomonsmith.dev (needs DI-20)
