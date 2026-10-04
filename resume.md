---
layout: page
title: "Resume"
eyebrow: "Resume"
heading: "Solomon Smith"
wide: true
permalink: /resume/
description: "Resume of Solomon Smith. Software engineer building LLM-backed backend features that fail closed. B.S. Computer Science, CSU San Bernardino, December 2026."
lede: "Software engineer. LLM-backed backend features that fail closed, and the tests that prove it."
---

<div class="btn-row">
  <a class="btn btn--primary" href="{{ '/assets/resume/SolomonSmithResume.pdf' | relative_url }}">Download PDF</a>
  <a class="btn" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
</div>

## Summary

Software engineer building LLM-backed backend features that fail closed. Shipped a production retrieval-grounded assistant with a citation-verification layer at a legal-data startup; built a multi-agent FastAPI service with a 400+ test suite that runs offline. Python, TypeScript, Postgres, FastAPI, Next.js. B.S. Computer Science, Dec 2026. Seeking **AI/ML or backend engineering roles, January 2027**.

## Experience

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Founding Engineer <span class="entry__org">&middot; Recursa AI / CourtRules (courtrules.app)</span></p>
    <p class="entry__meta">Jul 2026 to present &middot; Remote</p>
  </div>
  <p class="entry__meta">Second engineer, two-person team. Legal-data platform covering filing rules for 1,653 judges.</p>
  <ul>
    <li>Shipped the product's retrieval-grounded Q&amp;A feature on judge pages: fetches filed court orders from object storage, extracts text per page, grounds the model in that text, and streams verified answers as NDJSON (TypeScript, Next.js, Supabase).</li>
    <li>Designed the answer path to fail closed: a claim renders only if its quoted sentence appears verbatim in the source; 7 unit tests on the verifier caught a bypass where an invented quote passed on a plausible source index, fixed before release.</li>
    <li>Built query analytics that classify user questions into the product's 14-type rule taxonomy and a Postgres view ranking unanswered questions to separate data gaps from retrieval failures (service-write-only RLS).</li>
    <li>Added iCal and CSV court-calendar exports with RFC 5545 line folding, RFC 4180 quoting, a CSV formula-injection guard (CWE-1236), and schema.org Dataset markup; 35 tests.</li>
    <li>Authored the repository's first README and .env.example and automated the shared-package build so a fresh clone runs without manual steps. 4 merged PRs, 42 commits into an 800-commit codebase.</li>
    <li>Judge pages carry 57% of site pageviews (PostHog, 90 days).</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Full-Stack Developer (contract) <span class="entry__org">&middot; RideSplits</span></p>
    <p class="entry__meta">Jun 2025 to Sep 2025 &middot; San Bernardino, CA</p>
  </div>
  <p class="entry__meta">Early-stage logistics startup.</p>
  <ul>
    <li>Migrated authentication from custom JWT to Firebase Auth across rider and driver roles and implemented role-based access rules for Firestore and Storage.</li>
    <li>Built a multi-step ID-verification upload flow with client-side validation, file-type and size limits, and documented the security rules for the team.</li>
  </ul>
</div>

## Projects

<div class="entry">
  <div class="entry__head">
    <p class="entry__title"><a href="https://github.com/SolomonSmith-dev/arda">ARDA</a> <span class="entry__org">&middot; multi-agent service on FastAPI</span></p>
    <p class="entry__meta">Python &middot; LangGraph &middot; LlamaIndex &middot; Redis &middot; MCP</p>
  </div>
  <ul>
    <li>Built a LangGraph orchestrator on native Anthropic tool_use with a Redis-backed executor, LlamaIndex RAG, and an MCP server, exposed through 17 documented routes on one FastAPI surface.</li>
    <li>Designed a mock LLM and embedder layer so the full 425-test suite runs with no API keys or network in 13 seconds; CI gates on ruff, mypy, and pytest. 41 test files, roughly 6,300 lines of tests against 7,800 of source.</li>
    <li>Deployed and operate it 24/7 on a self-hosted Debian server under PM2 over a Tailscale mesh; hardened startup to fail closed on a missing API key.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title"><a href="https://github.com/SolomonSmith-dev/phishguard">PhishGuard</a> <span class="entry__org">&middot; phishing URL classifier</span></p>
    <p class="entry__meta">Python &middot; LightGBM &middot; FastAPI &middot; ONNX Runtime</p>
  </div>
  <ul>
    <li>Trained a LightGBM URL classifier to test AUC 0.9943 with a 1.54% false-positive rate on Tranco top-5000 domains; served via FastAPI with ONNX Runtime.</li>
    <li>Found and fixed label-polarity and distribution leakage in the PhiUSIIL dataset (100% https://www on legit rows), added leakage tests to pre-commit, and documented the methodology in LIMITATIONS.md; 34 tests.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title"><a href="https://github.com/SolomonSmith-dev/soc-triage-ai">SOC Triage AI</a> <span class="entry__org">&middot; RAG-grounded alert triage</span></p>
    <p class="entry__meta">Python &middot; Claude API &middot; sentence-transformers &middot; Streamlit</p>
  </div>
  <ul>
    <li>Built a six-stage pipeline: regex observable extraction, sentence-transformer retrieval over a MITRE ATT&amp;CK corpus, a similarity guardrail that refuses out-of-scope alerts, Claude generation constrained to retrieved context, and strict JSON schema validation.</li>
    <li>Raised the reliability harness from 43% to 100% (7 of 7) by reworking corpus chunking; shipped a Streamlit analyst UI with evidence panels and override tracking.</li>
  </ul>
</div>

## Education

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">B.S. Computer Science <span class="entry__org">&middot; California State University, San Bernardino</span></p>
    <p class="entry__meta">Dec 2026</p>
  </div>
</div>

## Skills

{% include skills.html %}

<div class="btn-row" style="margin-top: 2rem">
  <a class="btn btn--primary" href="{{ '/assets/resume/SolomonSmithResume.pdf' | relative_url }}">Download PDF</a>
  <a class="btn" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
</div>
