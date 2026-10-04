---
layout: page
wide: true
title: "Projects"
heading: "Work"
eyebrow: "Projects"
permalink: /projects/
description: "Projects by Solomon Smith: applied AI systems, LLM evaluation, security tooling, and the self-hosted infrastructure under them."
lede: "Applied AI systems, the infrastructure that runs them, and coursework with tests behind it. Every entry links to its source where the source is public."
---

<div class="project-group">
<h2 class="project-group__title">Applied AI systems</h2>
<div class="projects">

  <article class="project">
    <div class="project__head">
      <h3 class="project__title">soc-triage-ai</h3>
      <span class="status status--live">Shipped v1.0</span>
    </div>
    <p class="project__summary">RAG-grounded security alert triage that maps alerts to MITRE ATT&amp;CK techniques and refuses to answer when the evidence is weak.</p>
    <dl class="project__facts">
      <dt>Problem</dt>
      <dd>In a security context, a confident wrong answer from an LLM is worse than no answer.</dd>
      <dt>Built</dt>
      <dd>Retrieval over ATT&amp;CK, strict JSON schema validation, and a guardrail that rejects low-similarity inputs. Streamlit UI with evidence panels and analyst overrides.</dd>
      <dt>Result</dt>
      <dd>Reliability harness went from 43% to 100% (7 cases) after I traced the failures to corpus chunking, not prompt design.</dd>
      <dt>Next</dt>
      <dd>v2 platform rewrite in progress on a feature branch (FastAPI, PostgreSQL, Next.js).</dd>
    </dl>
    <div class="project__foot">
      <ul class="stack"><li>Python</li><li>Claude API</li><li>sentence-transformers</li><li>ChromaDB</li><li>Streamlit</li><li>pytest</li></ul>
      <div class="project__links">
        <a href="https://github.com/SolomonSmith-dev/soc-triage-ai" rel="noopener">Source</a>
        <a href="https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9" rel="noopener">Video walkthrough</a>
        <a href="{{ '/blog/building-soc-triage-copilot/' | relative_url }}">Build notes</a>
      </div>
    </div>
  </article>

  <article class="project">
    <div class="project__head">
      <h3 class="project__title">phishguard</h3>
      <span class="status">v0.2 in development</span>
    </div>
    <p class="project__summary">Multi-modal phishing URL detector that fuses three independent models, with its failures documented in the repo.</p>
    <dl class="project__facts">
      <dt>Built</dt>
      <dd>URL-feature GBDT, HTML DistilBERT, and page-screenshot EfficientNet, fused by a calibrated logistic meta-learner. Served with FastAPI and ONNX.</dd>
      <dt>Result</dt>
      <dd>AUC 0.9943 on the v0.2 holdout.</dd>
      <dt>Rigor</dt>
      <dd>Leakage tests retired v0.1. LIMITATIONS.md records what they found.</dd>
    </dl>
    <div class="project__foot">
      <ul class="stack"><li>Python</li><li>PyTorch</li><li>LightGBM</li><li>ONNX</li><li>FastAPI</li></ul>
      <div class="project__links"><a href="https://github.com/SolomonSmith-dev/phishguard" rel="noopener">Source</a></div>
    </div>
  </article>

  <article class="project">
    <div class="project__head">
      <h3 class="project__title">DocMind</h3>
      <span class="status status--live">Active</span>
    </div>
    <p class="project__summary">Document Q&amp;A over uploaded PDFs, with page-level citations and defenses against prompt injection.</p>
    <dl class="project__facts">
      <dt>Built</dt>
      <dd>Retrieval with page-level citations, magic-byte PDF validation, rate-limited upload and ask endpoints, and structured JSON logs with request IDs.</dd>
      <dt>Resilience</dt>
      <dd>Keeps working in a degraded mode when the local LLM is unavailable.</dd>
    </dl>
    <div class="project__foot">
      <ul class="stack"><li>Python</li><li>FastAPI</li><li>ChromaDB</li><li>sentence-transformers</li><li>Ollama</li></ul>
      <div class="project__links"><a href="https://github.com/SolomonSmith-dev/DocMind" rel="noopener">Source</a></div>
    </div>
  </article>

  <article class="project">
    <div class="project__head">
      <h3 class="project__title">arda</h3>
      <span class="status status--live">Active</span>
    </div>
    <p class="project__summary">Self-hosted LLM agent platform for long-running workflows with persistent state.</p>
    <dl class="project__facts">
      <dt>Built</dt>
      <dd>LangChain agents with tool use, memory, and multi-agent planning behind a FastAPI orchestrator, an MCP server, and a Redis-backed task queue.</dd>
    </dl>
    <div class="project__foot">
      <ul class="stack"><li>Python</li><li>FastAPI</li><li>LangChain</li><li>MCP</li><li>Redis</li></ul>
      <div class="project__links"><a href="https://github.com/SolomonSmith-dev/arda" rel="noopener">Source</a></div>
    </div>
  </article>

</div>
</div>

<div class="project-group">
<h2 class="project-group__title">Agent infrastructure</h2>
<div class="projects">

  <article class="project">
    <div class="project__head">
      <h3 class="project__title">claude-agents</h3>
      <span class="status status--live">Production</span>
    </div>
    <p class="project__summary">Backend for running Claude SDK agents on self-hosted hardware, with tool use and persistent state.</p>
    <dl class="project__facts">
      <dt>Built</dt>
      <dd>Express API with a BullMQ and Redis job queue and SQLite state.</dd>
      <dt>Security</dt>
      <dd>Command allowlist and audit logging on every agent action.</dd>
    </dl>
    <div class="project__foot">
      <ul class="stack"><li>Node.js</li><li>Express</li><li>BullMQ</li><li>Redis</li><li>SQLite</li></ul>
      <div class="project__links"><a href="https://github.com/SolomonSmith-dev/claude-agents" rel="noopener">Source</a></div>
    </div>
  </article>

  <article class="project">
    <div class="project__head">
      <h3 class="project__title">Sauron Stack</h3>
      <span class="status status--live">Self-hosted</span>
    </div>
    <p class="project__summary">A multi-agent system that runs around the clock on my Debian home server.</p>
    <dl class="project__facts">
      <dt>Built</dt>
      <dd>PM2-managed services: a router, an executor, an orchestrator, and a security daemon. They share a Redis-backed memory store over a Tailscale mesh.</dd>
      <dt>Incidents</dt>
      <dd>Traced a 401 crash-loop cascade to rate-limit headers and fixed it with exponential backoff and request queuing. Resolved a native-module ABI mismatch by rebuilding under Node v24.</dd>
    </dl>
    <div class="project__foot">
      <ul class="stack"><li>Python</li><li>Node.js</li><li>Claude API</li><li>Redis</li><li>PM2</li><li>Tailscale</li><li>Docker</li></ul>
      <div class="project__links"><span class="status">Private</span></div>
    </div>
  </article>

</div>
</div>

<div class="project-group">
<h2 class="project-group__title">Algorithms</h2>
<div class="projects">

  <article class="project">
    <div class="project__head">
      <h3 class="project__title">adversarial-search-csp</h3>
      <span class="status">Shipped v1.0</span>
    </div>
    <p class="project__summary">Game-playing agents and a constraint solver, with tests behind both.</p>
    <dl class="project__facts">
      <dt>Built</dt>
      <dd>Minimax, Negamax, and Alpha-Beta pruning for large-board Tic-Tac-Toe, plus a CSP backtracking solver for knight placement and vehicle scheduling.</dd>
      <dt>Tested</dt>
      <dd>21 pytest cases, run in CI with GitHub Actions.</dd>
    </dl>
    <div class="project__foot">
      <ul class="stack"><li>Python</li><li>pygame</li><li>numpy</li><li>pytest</li></ul>
      <div class="project__links"><a href="https://github.com/SolomonSmith-dev/adversarial-search-csp" rel="noopener">Source</a></div>
    </div>
  </article>

</div>
</div>

<section class="contact" aria-labelledby="contact-title">
  <h2 class="contact__title" id="contact-title">Want to see one of these up close?</h2>
  <p class="contact__body">I'm happy to walk through the architecture, the tradeoffs, or the bugs behind any of these projects.</p>
  <div class="btn-row">
    <a class="btn btn--primary" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
    <a class="btn" href="https://github.com/{{ site.github_username }}" rel="noopener">GitHub profile</a>
  </div>
</section>
