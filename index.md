---
layout: home
title: "Solomon Smith — AI, ML & Software Engineering Portfolio"
description: "Portfolio of Solomon Smith, a CS student at CSU San Bernardino building AI/ML and full-stack systems."
permalink: /
hero_title: "Hi, I'm Solomon Smith."
hero_subtitle: "CS senior at CSUSB. I build LLM pipelines, RAG systems, and multi-agent infrastructure — and ship the backend to make them production-worthy."
eyebrow: "AI / ML Engineer · Backend · LLM Systems"
---

<h2 class="section-heading">What I Work On</h2>

<div class="skills-grid">
  <div class="skills-grid__cell">
    <h4>Languages</h4>
    <ul>
      <li>Python</li><li>C++</li><li>JavaScript</li><li>TypeScript</li><li>SQL</li><li>Bash</li>
    </ul>
  </div>
  <div class="skills-grid__cell">
    <h4>AI / ML</h4>
    <ul>
      <li>PyTorch</li><li>scikit-learn</li><li>NumPy</li><li>pandas</li><li>NLP</li><li>Image Classification</li>
    </ul>
  </div>
  <div class="skills-grid__cell">
    <h4>Backend &amp; Web</h4>
    <ul>
      <li>FastAPI</li><li>Node.js</li><li>React</li><li>REST APIs</li><li>MongoDB</li><li>PostgreSQL</li>
    </ul>
  </div>
  <div class="skills-grid__cell">
    <h4>Tools &amp; Infra</h4>
    <ul>
      <li>Git / GitHub</li><li>Docker</li><li>Linux</li><li>Raspberry Pi</li><li>CI/CD</li><li>Jekyll</li>
    </ul>
  </div>
</div>

<h2 class="section-heading">Featured Projects</h2>

<div class="project-grid">

  <article class="project-card">
    <span class="project-card__status">Shipped · AI / Security</span>
    <h3 class="project-card__title">SOC Triage AI</h3>
    <p class="project-card__desc">
      RAG-grounded security alert triage system mapping alerts to MITRE ATT&amp;CK
      with strict JSON schema validation. 100% pass rate on a 7-case reliability
      harness. Guardrail logic prevents fabrication and confident wrong-answer failures
      in security contexts.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>Claude API</li><li>sentence-transformers</li><li>RAG</li><li>Streamlit</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev/soc-triage-ai" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

  <article class="project-card">
    <span class="project-card__status">Live · Multi-Agent AI</span>
    <h3 class="project-card__title">Multi-Agent AI System (Sauron Stack)</h3>
    <p class="project-card__desc">
      Production multi-agent system on a Debian home server. PM2-managed services:
      router (Earendil), executor (Sauron), orchestrator (Morgoth), security daemon
      (Balrog). Redis-backed memory, 24/7 uptime over Tailscale mesh. Debugged
      crash-loop cascades and ABI mismatches live.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>Node.js</li><li>Claude API</li><li>Redis</li><li>PM2</li><li>Tailscale</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

  <article class="project-card">
    <span class="project-card__status">Open Source · In Progress</span>
    <h3 class="project-card__title">TargetRecon CLI</h3>
    <p class="project-card__desc">
      Python CLI for the reconnaissance phase of security engagements. Takes a username,
      domain, or IP and runs structured OSINT lookups — breach data, DNS, WHOIS,
      social-handle discovery — outputting a clean report-style summary.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>argparse</li><li>requests</li><li>OSINT</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

</div>

<p style="margin-top: -0.5rem;">
  <a href="{{ '/projects/' | relative_url }}">See all projects →</a>
</p>

<h2 class="section-heading">Currently</h2>

- Finishing B.S. Computer Science at CSUSB — graduating **December 2026**
- Building LLM pipelines, RAG systems, and multi-agent infrastructure
- Previously interned at Recursa AI (RAG / legal NLP) and RideSplits (full-stack)
- Targeting **full-time AI/ML engineering roles starting January 2027**
- Reach me at **[solomonsmithdev@gmail.com](mailto:solomonsmithdev@gmail.com)**
