---
layout: post
title: "Building a SOC Triage Copilot: AI-Assisted Security Alert Triage"
date: 2026-04-30 10:00:00 -0700
categories: projects ai security
description: "Architecture notes from building an AI-powered SOC triage system. FastAPI backend, ML alert classification, MITRE ATT&CK mapping, Next.js dashboard, and an append-only analyst override log."
---

Security operations centers drown in alerts. Most are noise. The ones that matter
get buried. I built a system to fix that.

**Quick context:** v1 is shipped -- RAG-grounded triage using the Claude API and
sentence-transformers, with a Streamlit UI and a 7-case reliability harness at 100%
pass rate. The source is on [GitHub](https://github.com/SolomonSmith-dev/soc-triage-ai).
This post covers the architecture of **v2**: a full platform rewrite with a FastAPI
backend, PostgreSQL event store, and a Next.js analyst dashboard. v2 is currently
in progress.

---

The v2 system ingests raw security alerts, classifies their severity via a rules-free ML
engine, maps findings to MITRE ATT&CK techniques, and surfaces structured case summaries
for analyst review. Below is a snapshot of the architecture and the decisions behind it.

## The core problem

A typical SOC analyst handles hundreds of alerts per shift. Manual triage is slow,
inconsistent, and misses context. The standard approach -- writing detection rules -- is
brittle: it catches only what you thought to write a rule for. I wanted something that
could generalize.

The approach: train a classification model on historical alert data, not hand-written
thresholds. Feed it features extracted from raw event envelopes. Let it score severity.
Separately, map the alert payload to MITRE ATT&CK tactics using keyword and pattern
matching on technique descriptions.

## Architecture overview

Three main layers:

**Triage engine** (`services/triage-worker/`) -- a standalone Python service. Takes a
raw alert envelope (JSONB), extracts features, runs classification, returns a structured
case with severity score, confidence, and a list of matched ATT&CK techniques. Fully
tested in isolation (34 tests, zero external deps in the test suite).

**API** (`apps/api/`) -- a FastAPI service backed by PostgreSQL. Receives alert ingestion
via `POST /alerts`, writes the raw envelope to `cases.envelope` (immutable -- the engine
output is facts, not opinions). Analyst overrides land in a separate `analyst_overrides`
table: append-only, one row per edit, latest-wins on read. `GET /cases/{id}` applies
overrides over the envelope at read time -- no mutation of source data.

**Dashboard** (`apps/web/`) -- Next.js with TypeScript. Analyst-facing UI for reviewing
cases, applying overrides (severity, escalation flag, MITRE technique list), and viewing
edit history. Auth via NextAuth credentials provider.

## Decisions worth explaining

**Immutable envelopes.** `cases.envelope` is never updated after write. If an analyst
changes the severity, that goes into `analyst_overrides`, not back into the envelope.
This keeps the raw ML output intact for retraining and audit -- you can always reconstruct
what the model saw and what the analyst decided.

**Append-only overrides.** Each analyst edit creates a new row. The read path materializes
the current case state by applying all overrides in order (latest wins per field). This
gives you a full decision log for free -- no separate audit table needed for the analyst
action history.

**argon2id for auth.** One hash library for both passwords and API keys. OWASP recommends
argon2id for new systems; bcrypt is fine but argon2id has better resistance to GPU-based
attacks. Using one library instead of bcrypt-for-passwords / argon2id-for-keys reduces
the surface area. Interactive seed CLI via `getpass` -- never via env var or argv, which
would leak into shell history and `ps` output.

**Thin API handlers.** Handlers validate, call a service function, return. No business
logic in routes. Override application is read-side only -- the handler that serves
`GET /cases/{id}` calls `case_service.get_materialized_case()` which does the merge.
The handler doesn't know overrides exist.

## Test structure

The engine and API have separate test suites and separate CI jobs that run in parallel.
This decouples their dependencies -- the engine tests don't need API packages installed,
and API tests don't need the ML model.

Engine: 34 tests covering the classifier, ATT&CK mapper, and case builder.
API: 9 tests on password hashing, API key auth round-trips, and length enforcement.
Auth integration tests: in progress (unauth 401, authed 200, bad token 401).

## What's next

The auth middleware layer and analyst override endpoints are currently in progress.
After that, the Next.js dashboard gets the EditPanel and HistoryPanel components wired
to the live API. The goal is a demo-able end-to-end flow: ingest an alert, see the
AI-generated case, apply an analyst override, see the history.

Source code will be on [GitHub](https://github.com/SolomonSmith-dev) once the v2
platform layer ships.
