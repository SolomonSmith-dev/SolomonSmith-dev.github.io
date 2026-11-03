---
title: "DocMind"
eyebrow: "Project &middot; DocMind"
heading: "Upload a PDF, ask a question, get an answer that names the page it came from."
lede: "Local document Q&A: Ollama for the model, ChromaDB for the vectors, no API key. The document is treated as hostile input and the answer as something a reader has to be able to check."
description: "DocMind by Solomon Smith: local RAG document Q&A with page-level citations, prompt-injection filtering on retrieved chunks, JWT auth and rate limits. 113 tests."
order: 7
status: "Active"
live: true
stack: [Python, FastAPI, ChromaDB, sentence-transformers, Ollama, PyMuPDF, React]
links:
  - label: "Source"
    url: "https://github.com/SolomonSmith-dev/DocMind"
---

## What it does

Every chunk keeps its 1-indexed page number from PyMuPDF through ChromaDB to the response, so `/api/ask` returns `citations[].page_number` beside the answer. Each answer carries a confidence score (0.5 top-chunk similarity, 0.3 retrieval coverage, 0.2 model self-report) and a `low_confidence` flag below 0.4. If Ollama is down, the endpoint returns the cited passages instead of a 500.

## Why it is hard

Most RAG demos stop at "retrieve, then prompt." The retrieved text is attacker-controlled: whoever wrote the PDF wrote the context. So each chunk is wrapped in `<DOCUMENT_CHUNK>` delimiters, six instruction patterns ("ignore previous instructions", "system prompt:", `<system>` and friends) are rewritten to `[FILTERED]` and logged, and the system prompt refuses instructions found inside chunks. Prior user turns in a session get the same treatment.

The upload path assumes the same: magic-byte detection instead of the Content-Type header, a MIME allowlist, a 25 MB cap, UUID storage paths. slowapi caps `/api/upload` at 10 a minute and `/api/ask` at 30 per client IP, and every `/api/*` route except `/health` needs an HS256 JWT.

The injection filter is regex. It raises the cost of an attack; it does not end it. That sentence is in the README too.

## Evidence

| Number | Reproduce with |
|---|---|
| 113 passed | `pytest -q` on Python 3.11, run 2026-11-03; security 13, confidence 22, session 15, ask 14 among them |
| CI on every push and PR | `.github/workflows/ci.yml`: `ruff check`, `ruff format --check`, `pytest -v`, `pip-audit` |
| 2 browser E2E specs | `.github/workflows/e2e.yml`: ChromaDB service, live API and Playwright, `web/e2e/upload-query.spec.ts` |
{: .evidence}

Retrieval quality is not measured. There is no eval set yet, and nothing here claims an accuracy number.
