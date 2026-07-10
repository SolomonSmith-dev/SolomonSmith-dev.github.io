---
layout: home
title: "AI, ML and Software Engineering Portfolio"
description: "Solomon Smith, CS senior at CSU San Bernardino. AI/ML engineer building LLM pipelines, RAG systems, and multi-agent infrastructure. Open to Fall 2026 internships and full-time roles starting January 2027."
permalink: /
hero_subtitle: "Chef turned engineer. Ten years on the line before this, dishwasher to head chef. Same discipline, new craft. Building production RAG systems and multi-agent backends, including evaluation harnesses that caught a 12% hallucination regression before release."
---

<section class="section-marker">
  <span class="section-marker__roman">[01]</span>
  <span class="section-marker__label">&gt; proof</span>
</section>

<ul class="proof-list">
  <li><span class="proof-list__metric">200K+</span> legal documents ingested at 99%+ extraction accuracy</li>
  <li><span class="proof-list__metric">4s &rarr; &lt;600ms</span> RAG query latency on a production legal corpus</li>
  <li><span class="proof-list__metric">12%</span> hallucination regression caught and blocked before release</li>
</ul>

<section class="section-marker">
  <span class="section-marker__roman">[02]</span>
  <span class="section-marker__label">&gt; stations</span>
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
  <span class="section-marker__roman">[03]</span>
  <span class="section-marker__label">&gt; featured_work</span>
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

<p class="section-link">
  <a href="{{ '/projects/' | relative_url }}">cd ../projects &rarr;</a>
</p>

<section class="section-marker">
  <span class="section-marker__roman">[04]</span>
  <span class="section-marker__label">&gt; currently</span>
</section>

<div class="prose">

- Finishing B.S. Computer Science at CSUSB, graduating <strong>December 2026</strong>
- Most recent role: Software Engineering Intern at <strong>Recursa AI</strong>, shipping RAG over a legal corpus with an evaluation harness that caught a 12% hallucination regression before release
- Building LLM pipelines, RAG systems, and multi-agent infrastructure on my home server stack
- Open to <strong>Fall 2026 internships</strong> and <strong>full-time AI/ML engineering roles starting January 2027</strong>
- Strongest fit: RAG backend, AI platform/backend, and applied ML for production systems

<p class="cta-row">
  <a class="btn btn--primary" href="mailto:solomonsmithdev@gmail.com?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
  <a class="btn" href="{{ '/assets/resume/SolomonSmithResume.pdf' | relative_url }}" target="_blank" rel="noopener">Resume PDF</a>
  <a class="btn" href="{{ '/resume/' | relative_url }}">Full resume</a>
</p>

</div>
