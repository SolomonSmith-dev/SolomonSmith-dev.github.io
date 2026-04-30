---
layout: page
title: "Projects"
permalink: /projects/
description: "Projects by Solomon Smith — AI/ML, backend, infrastructure, and full-stack work."
---

A mix of applied ML systems, backend tools, and infrastructure work. Each entry links to
source code where available.

<h2 class="section-heading">Featured</h2>

<div class="project-grid">

  <article class="project-card">
    <span class="project-card__status">Shipped · AI / Security</span>
    <h3 class="project-card__title">SOC Triage AI</h3>
    <p class="project-card__desc">
      RAG-grounded security alert triage system mapping alerts to MITRE ATT&amp;CK
      techniques with strict JSON schema validation. Achieved 100% pass rate across a
      7-case reliability harness. Guardrail logic refuses low-similarity alerts and
      validates LLM output structurally, preventing fabrication in security contexts.
      v2 platform rewrite (FastAPI + PostgreSQL + Next.js) in progress.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>Claude API</li><li>sentence-transformers</li><li>RAG</li><li>Streamlit</li><li>pytest</li>
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
      (Balrog). Redis-backed memory store, 24/7 uptime over Tailscale mesh. Built and
      diagnosed crash-loop cascades and ABI mismatches in a live distributed environment.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>Node.js</li><li>Anthropic Claude API</li><li>Redis</li><li>PM2</li><li>Tailscale</li><li>Docker</li>
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
      social-handle discovery — outputting a clean report-style summary for downstream
      investigation.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>argparse</li><li>requests</li><li>OSINT</li><li>JSON</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

</div>

<h2 class="section-heading">Live</h2>

<div class="project-grid">

  <article class="project-card">
    <span class="project-card__status">Live · Discord Bot</span>
    <h3 class="project-card__title">Tom Bombadil Discord Bot</h3>
    <p class="project-card__desc">
      Gemini-powered Discord bot deployed on my home server. Handles natural-language
      queries, command routing, and multi-turn conversation context. Systemd service
      with automatic restart and structured logging.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>Gemini API</li><li>discord.py</li><li>systemd</li><li>Linux</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

  <article class="project-card">
    <span class="project-card__status">Live · Self-Hosted Infra</span>
    <h3 class="project-card__title">Plex Home Server</h3>
    <p class="project-card__desc">
      Self-hosted media server on a Raspberry Pi. Docker-containerized, with secured
      remote access, automated nightly backups of media metadata and Plex configuration,
      and dynamic DNS for stable external reachability.
    </p>
    <ul class="project-card__stack">
      <li>Raspberry Pi</li><li>Linux</li><li>Docker</li><li>Plex</li><li>Networking</li><li>Bash</li>
    </ul>
  </article>

  <article class="project-card">
    <span class="project-card__status">Live · Web</span>
    <h3 class="project-card__title">Personal Portfolio Site</h3>
    <p class="project-card__desc">
      This site. Custom Jekyll build on GitHub Pages with a custom domain. Hand-written
      Sass dark theme on top of Minima, custom layouts, SEO-tagged pages, automatic
      sitemap and RSS feed.
    </p>
    <ul class="project-card__stack">
      <li>Jekyll</li><li>Ruby</li><li>Sass</li><li>GitHub Pages</li><li>Liquid</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev/SolomonSmith-dev.github.io" target="_blank" rel="noopener">Source →</a>
      <a href="https://solomon-smith-dev.tech" target="_blank" rel="noopener">Live →</a>
    </div>
  </article>

</div>

<h2 class="section-heading">In the Pipeline</h2>

<div class="project-grid">

  <article class="project-card">
    <span class="project-card__status">Planned · AI / ML</span>
    <h3 class="project-card__title">Fantasy Football Draft Helper</h3>
    <p class="project-card__desc">
      Draft-time recommendation tool that ingests historical player stats and projection
      data, ranks remaining players by value-over-replacement, and surfaces AI-driven
      pick suggestions tuned to the user's roster construction.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>pandas</li><li>scikit-learn</li><li>FastAPI</li><li>React</li>
    </ul>
  </article>

  <article class="project-card">
    <span class="project-card__status">Planned · Security</span>
    <h3 class="project-card__title">Home Network Monitoring</h3>
    <p class="project-card__desc">
      Hardened home network with Suricata IDS for traffic inspection and Pi-hole for
      DNS-level filtering. Logs forwarded to a central dashboard for traffic analysis
      and alerting on suspicious patterns.
    </p>
    <ul class="project-card__stack">
      <li>Suricata</li><li>Pi-hole</li><li>Linux</li><li>Networking</li><li>Grafana</li>
    </ul>
  </article>

</div>

<p style="margin-top: 1rem;">
  Project write-ups land on the <a href="{{ '/blog/' | relative_url }}">blog</a> as
  they ship. The full source tree lives on
  <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub</a>.
</p>
