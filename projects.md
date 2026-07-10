---
layout: page
title: "Projects"
permalink: /projects/
description: "Projects by Solomon Smith. Applied AI and ML systems, security tooling, multi-agent backends, and the infrastructure under them."
lede: "Applied AI and ML systems, security tooling, and multi-agent backends. Each entry links to source where available."
---

<div class="course-list">

  <article class="course">
    <span class="course__num">01</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title"><a href="https://github.com/SolomonSmith-dev/soc-triage-ai" target="_blank" rel="noopener">soc-triage-ai</a></h3>
        <span class="course__status">Shipped &middot; v1.0</span>
      </div>
      <p class="course__desc">
        RAG-grounded security alert triage. Maps alerts to MITRE ATT&amp;CK techniques with strict JSON schema validation. Guardrail logic refuses low-similarity inputs to prevent confident wrong-answer failures. 100% pass rate across a 7-case reliability harness. Streamlit UI with evidence panels and analyst overrides. v2 platform rewrite in progress on a feature branch (FastAPI, PostgreSQL, Next.js).
      </p>
      <ul class="course__stack">
        <li>Python</li><li>Claude API</li><li>sentence-transformers</li><li>ChromaDB</li><li>Streamlit</li><li>pytest</li>
      </ul>
      <div class="course__links">
        <a href="https://github.com/SolomonSmith-dev/soc-triage-ai" target="_blank" rel="noopener">github</a>
        <a href="https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9" target="_blank" rel="noopener">walkthrough</a>
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

  <article class="course">
    <span class="course__num">04</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title"><a href="https://github.com/SolomonSmith-dev/claude-agents" target="_blank" rel="noopener">claude-agents</a></h3>
        <span class="course__status">Production</span>
      </div>
      <p class="course__desc">
        Local multi-agent orchestration backend. Express, BullMQ, Redis, and SQLite. Runs Claude SDK agents on self-hosted hardware with tool use and persistent state. Includes a command allowlist security layer and audit logging.
      </p>
      <ul class="course__stack">
        <li>Node.js</li><li>Express</li><li>BullMQ</li><li>Redis</li><li>SQLite</li>
      </ul>
      <div class="course__links">
        <a href="https://github.com/SolomonSmith-dev/claude-agents" target="_blank" rel="noopener">github</a>
      </div>
    </div>
  </article>

  <article class="course">
    <span class="course__num">05</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title"><a href="https://github.com/SolomonSmith-dev/DocMind" target="_blank" rel="noopener">DocMind</a></h3>
        <span class="course__status">Active</span>
      </div>
      <p class="course__desc">
        RAG document Q&amp;A with page-level citations and prompt injection defense. Magic-byte PDF validation, rate-limited upload and ask endpoints, structured JSON logging with request IDs, and graceful degradation when the local LLM is unavailable.
      </p>
      <ul class="course__stack">
        <li>Python</li><li>FastAPI</li><li>ChromaDB</li><li>sentence-transformers</li><li>Ollama</li>
      </ul>
      <div class="course__links">
        <a href="https://github.com/SolomonSmith-dev/DocMind" target="_blank" rel="noopener">github</a>
      </div>
    </div>
  </article>

  <article class="course">
    <span class="course__num">06</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title"><a href="https://github.com/SolomonSmith-dev/adversarial-search-csp" target="_blank" rel="noopener">adversarial-search-csp</a></h3>
        <span class="course__status">Shipped &middot; v1.0</span>
      </div>
      <p class="course__desc">
        Minimax, Negamax, and Alpha-Beta pruning on large-board Tic-Tac-Toe with a CSP backtracking solver for knight placement and vehicle scheduling. 21 pytest cases, CI-tested.
      </p>
      <ul class="course__stack">
        <li>Python</li><li>pygame</li><li>numpy</li><li>pytest</li>
      </ul>
      <div class="course__links">
        <a href="https://github.com/SolomonSmith-dev/adversarial-search-csp" target="_blank" rel="noopener">github</a>
      </div>
    </div>
  </article>

  <article class="course">
    <span class="course__num">07</span>
    <div class="course__body">
      <div class="course__head">
        <h3 class="course__title">Multi-Agent AI System &middot; Sauron Stack</h3>
        <span class="course__status">Self-hosted</span>
      </div>
      <p class="course__desc">
        Production multi-agent system on a Debian home server. PM2-managed services: router (Earendil), executor (Sauron), orchestrator (Morgoth), and a security daemon (Balrog). Redis-backed memory store with 24/7 uptime over a Tailscale mesh. Diagnosed and resolved a 401 crash-loop cascade and a native-module ABI mismatch live.
      </p>
      <ul class="course__stack">
        <li>Python</li><li>Node.js</li><li>Claude API</li><li>Redis</li><li>PM2</li><li>Tailscale</li><li>Docker</li>
      </ul>
    </div>
  </article>

</div>

<p class="prose mt-lg">
  Project write-ups land on the <a href="{{ '/blog/' | relative_url }}">blog</a> as they ship. The full source tree lives on <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub</a>.
</p>
