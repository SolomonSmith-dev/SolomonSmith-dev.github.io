---
title: "SOC Triage AI"
eyebrow: "Project &middot; SOC Triage AI"
heading: "Paste a security alert. Get severity, ATT&CK techniques and the evidence, or a refusal."
lede: "Retrieval-grounded alert triage over a threat-intel corpus, with Claude held to the retrieved context and a strict JSON schema. It never invents a triage."
description: "SOC Triage AI by Solomon Smith: RAG-grounded SOC alert triage with MITRE ATT&CK mapping, a fail-closed refusal path and a 100-case harness replayed in CI."
order: 3
status: "Shipped v1.0"
stack: [Python, Claude API, sentence-transformers, FastAPI, PostgreSQL, Streamlit]
image: /assets/img/projects/soc-triage-streamlit-ui.png
image_alt: "SOC Triage AI Streamlit UI with a sample alert loaded; observables are extracted by regex before any model call"
image_width: 1280
image_height: 720
image_caption: "The analyst UI. Observables are extracted by regex before any model call."
links:
  - label: "Source"
    url: "https://github.com/SolomonSmith-dev/soc-triage-ai"
  - label: "3-minute walkthrough"
    url: "https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9"
---

## What it does

Six stages. Regex pulls IPs, hashes, processes and users before any model call. The alert is embedded with `all-MiniLM-L6-v2` and matched against an 11-document corpus (109 chunks). If no chunk scores at least 0.20, the system refuses. Otherwise the top 4 chunks go to Claude, held to that context, and the reply must parse against a strict schema.

## Why it is hard

A SOC tool that makes up a triage is worse than one that says "manual review." The failure path is the product. When retrieval finds nothing, the response is fixed: severity `informational`, escalate `false`, "Manual analyst review required." When retrieval found context but the model reply fails the schema, it fails toward review instead: severity `medium`, `escalate: true`.

The guardrail is measured, not asserted. At 0.20, none of the 84 labelled real alerts is refused wrongly, and 7 of 16 out-of-corpus inputs are caught. The other 9 reach the model, which answers `informational`. A Kubernetes ticket scores 0.525 against Linux log chunks, so no threshold removes every miss.

## Evidence

| Number | Reproduce with |
|---|---|
| 109 pytest tests, 94 offline | `pytest tests/unit packages/contracts/tests` needs no key; the rest run in CI against Postgres 16 |
| 100 harness cases, 60 standard and 40 adversarial | `python -m tests.harness.loader --validate`. 7 reviewed by me, 93 drafted by Claude and pending review |
| 76 of 100 passing, live, 0.59 USD | `tests/harness/harness_results.json`, run 2026-10-09 on `claude-sonnet-4-5` |
| Refusal precision 1.0, recall 0.438 | `retrieval_results.json`; retrieval hit@4 0.893 on 84 labelled queries |
{: .evidence}

The harness replays recorded model replies in CI, so these numbers rerun without an API key, and the gate fails on any case that passed before and does not now.
