---
layout: page
title: "Resume"
eyebrow: "Resume"
heading: "Solomon Smith"
wide: true
permalink: /resume/
description: "Resume of Solomon Smith, AI/Backend Engineer. LLM-backed features that refuse correctly, with the tests that prove it. B.S. Computer Science, CSU San Bernardino, December 2026."
lede: "AI/Backend Engineer. LLM-backed features for products where a confident wrong answer costs more than no answer, and the tests that prove they refuse correctly."
---

<div class="btn-row">
  <a class="btn btn--primary" href="{{ '/assets/resume/SolomonSmithResume.pdf' | relative_url }}">Download PDF</a>
  <a class="btn" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
</div>

<p class="resume-tagline">AI/Backend Engineer &middot; B.S. Computer Science, Dec 2026 &middot; Available January 2027</p>
<p class="resume-contact">Montclair, CA &middot; <a href="mailto:solomonsmithdev@gmail.com">solomonsmithdev@gmail.com</a> &middot; <a href="https://linkedin.com/in/solomonsmithdev">linkedin.com/in/solomonsmithdev</a> &middot; <a href="https://github.com/SolomonSmith-dev">github.com/SolomonSmith-dev</a> &middot; <a href="https://solomonsmith.dev">solomonsmith.dev</a></p>

## Education

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">B.S. Computer Science <span class="entry__org">&middot; California State University, San Bernardino</span></p>
    <p class="entry__meta">Dec 2026</p>
  </div>
  <p class="entry__meta">Relevant coursework: Machine Learning, Algorithms and Data Structures, Database Systems, Operating Systems</p>
</div>

## Experience

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Founding Engineer (2nd engineer) <span class="entry__org">&middot; Recursa AI / CourtRules (courtrules.app)</span></p>
    <p class="entry__meta">Jul 2026 to present &middot; Remote</p>
  </div>
  <p class="entry__meta">legal-data platform covering filing rules for 1,653 judges</p>
  <ul>
    <li>Shipped retrieval-grounded Q&amp;A on judge pages, which carry 57% of site pageviews: fetches filed court orders from object storage, extracts per-page text, grounds the model in it, and streams answers as NDJSON (Next.js, Supabase).</li>
    <li>Designed a fail-closed citation verifier: a claim renders only if its quote appears verbatim in the source. Its tests caught a bypass where an invented quote passed on a plausible source index, fixed before release.</li>
    <li>Built query analytics that classify questions into a 14-type rule taxonomy, plus a Postgres view ranking unanswered questions to separate data gaps from retrieval failures (service-write-only RLS).</li>
    <li>Added iCal and CSV court-calendar exports (RFC 5545, RFC 4180) with a formula-injection guard (CWE-1236).</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Full-Stack Developer (Contract) <span class="entry__org">&middot; RideSplits</span></p>
    <p class="entry__meta">Jun 2025 to Sep 2025 &middot; San Bernardino, CA</p>
  </div>
  <ul>
    <li>Migrated auth from custom JWT to Firebase Auth for rider and driver roles with role-based Firestore rules.</li>
    <li>Built the Team B user-system backend in Node.js, Express and MySQL: bcrypt auth with university-email validation, profile, verification and payment-account endpoints, a shell test script, and API integration docs for the other teams.</li>
    <li>Built a multi-step ID-verification upload flow with client-side file-type and size validation.</li>
  </ul>
</div>

## Open source

<div class="entry">
  <div class="entry__head">
    <p class="entry__title"><a href="https://github.com/civicband/clerk-fetchers/pull/85">CivicBand clerk-fetchers</a> <span class="entry__org">&middot; PR #85, merged Jul 2026</span></p>
  </div>
  <ul>
    <li>Built a generic Swagit fetcher (Python): any Swagit-hosted city is added with two registry entries and no new code.</li>
    <li>Normalized meeting dates to ISO-8601 and added offline pytest coverage against recorded HTML fixtures.</li>
  </ul>
</div>

## Projects

<div class="entry">
  <div class="entry__head">
    <p class="entry__title"><a href="https://github.com/SolomonSmith-dev/arda">ARDA, multi-agent service</a> <span class="entry__org">&middot; LangGraph, LlamaIndex, Redis, MCP</span></p>
  </div>
  <ul>
    <li>Built a LangGraph orchestrator on native Anthropic tool_use with a Redis-backed executor, LlamaIndex RAG, and an MCP server behind 17 documented FastAPI routes.</li>
    <li>Designed a mock LLM and embedder layer so the 425-test suite runs offline in 13 seconds; runs 24/7 on a self-hosted Debian server.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title"><a href="https://github.com/SolomonSmith-dev/soc-triage-ai">SOC Triage AI, RAG alert triage</a> <span class="entry__org">&middot; Claude, Streamlit</span></p>
  </div>
  <ul>
    <li>Built a six-stage pipeline: regex observable extraction, retrieval over MITRE ATT&amp;CK, a guardrail that refuses out-of-scope alerts, context-constrained generation, and JSON schema validation.</li>
    <li>Raised reliability-harness pass rate from 3 of 7 to 7 of 7 cases by reworking corpus chunking; shipped a Streamlit analyst UI.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title"><a href="https://github.com/SolomonSmith-dev/phishguard">PhishGuard</a> <span class="entry__org">&middot; LightGBM, ONNX Runtime, FastAPI</span></p>
  </div>
  <ul>
    <li>Found and fixed label-polarity and distribution leakage in the PhiUSIIL dataset (every legitimate URL began with https://www). Documented the methodology in LIMITATIONS.md and added leakage tests to pre-commit.</li>
    <li>Trained a LightGBM URL classifier to 0.9943 test AUC at a 1.54% false-positive rate on Tranco top-5,000 domains; served via FastAPI with ONNX Runtime.</li>
  </ul>
</div>

## Skills

{% include skills.html %}

<div class="btn-row" style="margin-top: 2rem">
  <a class="btn btn--primary" href="{{ '/assets/resume/SolomonSmithResume.pdf' | relative_url }}">Download PDF</a>
  <a class="btn" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
</div>
