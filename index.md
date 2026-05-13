---
layout: home
title: "AI, ML and Software Engineering Portfolio"
description: "Solomon Smith, CS senior at CSU San Bernardino. AI/ML engineer building LLM pipelines, RAG systems, and multi-agent infrastructure. Open for full-time roles January 2027."
permalink: /
hero_subtitle: "Chef turned engineer. Ten years on the line before this, dishwasher to head chef. Same discipline, new craft. Building LLM pipelines, RAG systems, and the backend that makes them production-worthy."
---

<section class="section-marker">
  <span class="section-marker__roman">I</span>
  <span class="section-marker__label">Stations</span>
</section>

<div class="stations">
  <div class="station">
    <p class="station__name">Languages</p>
    <ul class="station__list">
      <li>Python</li>
      <li>TypeScript</li>
      <li>JavaScript</li>
      <li>C++</li>
      <li>SQL</li>
      <li>Bash</li>
    </ul>
  </div>
  <div class="station">
    <p class="station__name">AI / ML</p>
    <ul class="station__list">
      <li>LangChain</li>
      <li>Claude API</li>
      <li>RAG, pgvector, ChromaDB</li>
      <li>sentence-transformers</li>
      <li>PyTorch, scikit-learn</li>
      <li>Multi-agent orchestration, MCP</li>
    </ul>
  </div>
  <div class="station">
    <p class="station__name">Backend</p>
    <ul class="station__list">
      <li>FastAPI</li>
      <li>Express, Node.js</li>
      <li>PostgreSQL, MySQL, Redis</li>
      <li>Firebase, Supabase</li>
      <li>REST APIs</li>
    </ul>
  </div>
  <div class="station">
    <p class="station__name">Infra</p>
    <ul class="station__list">
      <li>Docker, Linux, systemd</li>
      <li>PM2, Tailscale, Nginx</li>
      <li>GitHub Actions</li>
      <li>GCP, AWS</li>
    </ul>
  </div>
</div>

<section class="section-marker">
  <span class="section-marker__roman">II</span>
  <span class="section-marker__label">Featured Work</span>
</section>

<div class="course-list">

  <article class="course">
    <span class="course__num">01</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title"><a href="https://github.com/SolomonSmith-dev/soc-triage-ai" target="_blank" rel="noopener">soc-triage-ai</a></h3>
        <span class="course__status">Shipped &middot; v1.0</span>
      </div>
      <p class="course__desc">
        RAG-grounded security alert triage. Maps alerts to MITRE ATT&amp;CK techniques with strict JSON schema validation. Guardrail logic refuses low-similarity inputs to prevent confident wrong-answer failures. 100% pass rate across a 7-case reliability harness. Streamlit UI with evidence panels and analyst overrides.
      </p>
      <ul class="course__stack">
        <li>Python</li><li>Claude API</li><li>sentence-transformers</li><li>ChromaDB</li><li>Streamlit</li><li>pytest</li>
      </ul>
      <div class="course__links">
        <a href="https://github.com/SolomonSmith-dev/soc-triage-ai" target="_blank" rel="noopener">github</a>
        <a href="https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9" target="_blank" rel="noopener">loom walkthrough</a>
      </div>
    </div>
  </article>

  <article class="course">
    <span class="course__num">02</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title"><a href="https://github.com/SolomonSmith-dev/arda" target="_blank" rel="noopener">arda</a></h3>
        <span class="course__status">Active</span>
      </div>
      <p class="course__desc">
        Python LLM agents with LangChain. Tool use, memory, and multi-agent planning. FastAPI orchestrator with an MCP server and a Redis-backed task queue. Designed for self-hosted, long-running agent workflows with persistent state.
      </p>
      <ul class="course__stack">
        <li>Python</li><li>FastAPI</li><li>LangChain</li><li>MCP</li><li>Redis</li>
      </ul>
      <div class="course__links">
        <a href="https://github.com/SolomonSmith-dev/arda" target="_blank" rel="noopener">github</a>
      </div>
    </div>
  </article>

  <article class="course">
    <span class="course__num">03</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title"><a href="https://github.com/SolomonSmith-dev/phishguard" target="_blank" rel="noopener">phishguard</a></h3>
        <span class="course__status">v0.2 in development</span>
      </div>
      <p class="course__desc">
        Multi-modal phishing URL detector. Three independent models (URL feature GBDT, HTML DistilBERT, page-screenshot EfficientNet) fused via a calibrated logistic meta-learner. AUC 0.9943 on the v0.2 holdout. Honest LIMITATIONS.md documents the leakage tests that killed v0.1.
      </p>
      <ul class="course__stack">
        <li>Python</li><li>PyTorch</li><li>LightGBM</li><li>ONNX</li><li>FastAPI</li>
      </ul>
      <div class="course__links">
        <a href="https://github.com/SolomonSmith-dev/phishguard" target="_blank" rel="noopener">github</a>
      </div>
    </div>
  </article>

</div>

<p style="margin-top: 2rem; font-family: var(--font-mono); font-size: 0.74rem; letter-spacing: 0.16em; text-transform: uppercase;">
  <a href="{{ '/projects/' | relative_url }}" style="color: var(--color-cream-soft);">All projects →</a>
</p>

<section class="section-marker">
  <span class="section-marker__roman">III</span>
  <span class="section-marker__label">Currently</span>
</section>

<div class="prose">

- Finishing B.S. Computer Science at CSUSB, graduating <strong>December 2026</strong>
- Most recent role: Software Engineering Intern at <strong>Recursa AI</strong>, shipping RAG over a legal corpus with an evaluation harness that caught a 12% hallucination regression before release
- Building LLM pipelines, RAG systems, and multi-agent infrastructure on my home server stack
- Targeting <strong>full-time AI/ML engineering roles starting January 2027</strong>
- Reach me at <a href="mailto:solomonsmithdev@gmail.com">solomonsmithdev@gmail.com</a>

</div>
