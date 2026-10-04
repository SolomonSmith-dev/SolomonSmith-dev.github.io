---
layout: page
wide: true
title: "Projects"
heading: "Work"
eyebrow: "Projects"
permalink: /projects/
description: "Projects by Solomon Smith: applied AI systems, LLM evaluation, security tooling, and the self-hosted infrastructure under them."
lede: "Production LLM features, the services and infrastructure behind them, and coursework with tests. Every entry links to its source or live product where one is public."
---

<div class="project-group">
<h2 class="project-group__title">LLM and ML systems</h2>
<div class="projects">

  {% include card-courtrules.html %}
  {% include card-arda.html %}
  {% include card-soc-triage.html %}

  {% include card-phishguard.html %}

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
