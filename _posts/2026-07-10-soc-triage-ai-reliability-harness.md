---
layout: post
title: "soc-triage-ai v1: From 43% to 100% on a Reliability Harness"
date: 2026-07-10 09:00:00 -0700
categories: projects ai security
description: "How I shipped a RAG-grounded SOC alert triage system. Guardrails, MITRE ATT&CK mapping, a 7-case reliability harness, and the chunking bug that looked like a prompt problem."
image: /assets/images/headshot.jpg
---

Security alert triage fails in a specific way: the model sounds confident while being wrong. For a SOC workflow, that is worse than abstaining.

I shipped [soc-triage-ai](https://github.com/SolomonSmith-dev/soc-triage-ai) v1 to attack that failure mode directly. The system maps alerts to MITRE ATT&CK techniques with RAG grounding, validates structured output, and refuses low-similarity inputs instead of guessing.

This post is the v1 teardown: what shipped, what broke, and what the numbers actually mean. For the v2 platform rewrite (FastAPI, PostgreSQL, Next.js), see the earlier [architecture notes](/2026/04/30/building-soc-triage-copilot.html).

## What shipped

- RAG-grounded triage over a MITRE ATT&CK corpus
- Claude API generation with strict JSON schema validation
- Guardrail logic that refuses low-similarity retrievals
- Streamlit UI with evidence panels and analyst overrides
- A 7-case reliability harness at **100% pass rate**
- Tagged release: `v1.0-codepath-final`
- [Loom walkthrough](https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9)

Stack: Python, Claude API, sentence-transformers, ChromaDB, Streamlit, pytest.

## The failure mode that mattered

Early versions looked fine in demos and failed under evaluation.

The first reliability harness pass rate was **43%**. The tempting diagnosis was "bad prompting." The actual root cause was **corpus chunking**: retrieval returned partial technique context, so the model filled gaps with fluent but incorrect mappings.

That distinction matters for production AI work. If you only tune prompts, you can paper over a retrieval bug and ship a system that fails the same way in production.

## Guardrails before cleverness

Two constraints made the system safer:

1. **Similarity gate.** If retrieved context is too weak, the system refuses to triage instead of inventing a technique mapping.
2. **Schema validation.** Output must match a strict JSON shape. Free-form prose cannot sneak through as a "successful" answer.

In security contexts, abstention is a feature. Confident wrong answers create analyst debt and false trust.

## What the harness proved

The 7-case harness is small on purpose. It is not a leaderboard claim. It is a regression gate for the failure modes I actually care about:

- grounded technique mapping when evidence exists
- refusal when evidence is weak
- structurally valid output every time
- no silent drift after prompt or corpus changes

Improving from 43% to 100% came from fixing chunking and retrieval quality, then re-running the same cases. The model card documents that path so the next change has a baseline.

## Why this project is on the portfolio

Recruiters and hiring managers do not need another chatbot demo. They need evidence that you can:

- define a measurable reliability target
- find the real failure (retrieval vs prompt vs schema)
- add guardrails that change production behavior
- document the tradeoffs honestly

That is the systems side of applied AI. Notebooks are easy. Evaluation and refusal behavior are the hard part.

## Links

- Source: [github.com/SolomonSmith-dev/soc-triage-ai](https://github.com/SolomonSmith-dev/soc-triage-ai)
- Walkthrough: [Loom demo](https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9)
- v2 architecture notes: [Building a SOC Triage Copilot](/2026/04/30/building-soc-triage-copilot.html)
- Project index: [/projects/](/projects/)

If you are hiring for RAG backend, AI platform, or applied ML roles, this is the kind of work I want to keep shipping. Reach me at [solomonsmithdev@gmail.com](mailto:solomonsmithdev@gmail.com).
