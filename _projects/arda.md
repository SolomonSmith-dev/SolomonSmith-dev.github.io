---
title: "ARDA"
eyebrow: "Project &middot; ARDA"
heading: "A Claude orchestrator in front of a shell, with numbers on where the routing fails."
lede: "A multi-agent service on one FastAPI surface: a LangGraph orchestrator on native Anthropic tool_use, a Redis-backed shell executor, LlamaIndex retrieval and an MCP server. The whole test suite runs with no API key."
description: "ARDA by Solomon Smith: LangGraph multi-agent service on FastAPI with 577 offline tests, labelled prompt-injection evals and a demo mode that refuses shell execution structurally."
order: 2
status: "Deployed"
live: true
stack: [Python, FastAPI, LangGraph, LlamaIndex, Redis, MCP, Docker]
image: /assets/img/projects/arda-demo-page.png
image_alt: "ARDA demo page in mock mode: a question, the retrieved answer, and a trace of specialist, tool calls, latency and tokens"
image_width: 760
image_height: 958
image_caption: "The demo page in mock mode. Shell execution is refused in the router, the agent and the worker."
links:
  - label: "Source"
    url: "https://github.com/SolomonSmith-dev/arda"
---

## What it does

One LangGraph `StateGraph` (Sauron) classifies each request through native `tool_use` and dispatches it to a shell executor, a RAG retriever or a Discord film-club specialist. Seven agents sit behind 17 HTTP routes and 4 MCP tools, running 24/7 on my Debian home server.

## Why it is hard

The routing is not the hard part. The shell-bound path is. An injected prompt that reaches the executor runs a command. So the repo ships a labelled eval set with 16 injection cases and a committed baseline showing the offline router leaking 12 of them. That number stays in the README on purpose: the low block rate is the finding.

Demo mode closes the gap structurally instead of hoping the router improves. Shell is refused at the router, inside the agent and in the worker, and one test reads every operation from the OpenAPI schema and asserts a refusal on each non-allowlisted route.

Every LLM has a deterministic mock, and a parity test introspects the installed Anthropic SDK so a mock cannot accept a parameter the real client rejects. CI runs the mock evals twice and fails if they differ or drift from the committed baseline.

## Evidence

| Number | Reproduce with |
|---|---|
| 577 passed, 5 skipped, 582 collected, 29 s | `uv run pytest tests/ -q` from a clean clone, no network; the skips need a real `ANTHROPIC_API_KEY` |
| 12 of 16 injections leak (mock) | `evals/results/2026-10-05-mock.json`; routing accuracy 75.9% (n=54), recall@5 81.6% |
| 17 demo-mode safety tests | `tests/test_demo_mode.py`, including the OpenAPI sweep |
| 7 agents, 17 routes, 4 MCP tools | `agents/`, `api/`, `mcp_server/server.py` |
{: .evidence}

These measure the offline mocks, not Claude. The live column stays empty until a run against the real API is committed.
