---
layout: page
title: "Projects"
permalink: /projects/
description: "Projects by Solomon Smith — AI/ML, backend, infrastructure, and full-stack work."
---

A mix of open-source tools, infrastructure projects, and applied ML work. Each entry
links to source code where available, plus the stack and current status.

<h2 class="section-heading">Featured</h2>

<div class="project-grid">

  <article class="project-card">
    <span class="project-card__status">In Progress · AI / Security</span>
    <h3 class="project-card__title">SOC Triage Copilot</h3>
    <p class="project-card__desc">
      An AI-powered Security Operations Center triage system. Ingests raw security
      alerts, classifies severity, maps findings to MITRE ATT&amp;CK techniques, and
      surfaces structured case summaries for analyst review. Built with a FastAPI
      backend, PostgreSQL event store, Next.js analyst dashboard, and a rules-free ML
      triage engine. Analyst overrides are append-only with full audit trail.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>FastAPI</li><li>PostgreSQL</li><li>Next.js</li><li>TypeScript</li><li>Docker</li><li>NLP</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

  <article class="project-card">
    <span class="project-card__status">Live · Distributed Systems</span>
    <h3 class="project-card__title">Earendil Task System</h3>
    <p class="project-card__desc">
      A self-hosted distributed task execution system running on a home Mac Mini server.
      Exposes a REST API for dispatching, querying, and monitoring long-running tasks
      across processes. Built with OAuth/token auth, a systemd-managed daemon, and a
      full test suite (33/33 passing). Powers several of my personal automation pipelines.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>FastAPI</li><li>OAuth</li><li>systemd</li><li>Linux</li><li>Tailscale</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

  <article class="project-card">
    <span class="project-card__status">Open Source · In Progress</span>
    <h3 class="project-card__title">TargetRecon CLI</h3>
    <p class="project-card__desc">
      Python CLI for the reconnaissance phase of cybersecurity engagements. Takes a
      username, domain, or IP and runs a structured set of OSINT lookups — public
      breach data, DNS info, WHOIS, and social-handle discovery — outputting a clean,
      report-style summary for downstream investigation.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>argparse</li><li>requests</li><li>OSINT</li><li>JSON</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

  <article class="project-card">
    <span class="project-card__status">Self-Hosted Infra</span>
    <h3 class="project-card__title">Plex Home Server</h3>
    <p class="project-card__desc">
      Self-hosted media server running on a Raspberry Pi. Docker-containerized for
      portability, with secured remote access, automated nightly backups of the
      media library and Plex configuration, and dynamic DNS for stable external
      reachability.
    </p>
    <ul class="project-card__stack">
      <li>Raspberry Pi</li><li>Linux</li><li>Docker</li><li>Plex</li><li>Networking</li><li>Bash</li>
    </ul>
  </article>

  <article class="project-card">
    <span class="project-card__status">Live</span>
    <h3 class="project-card__title">Personal Portfolio Site</h3>
    <p class="project-card__desc">
      This site. A custom Jekyll build deployed on GitHub Pages with a custom domain.
      Hand-written Sass theme on top of Minima, custom layouts, SEO-tagged pages,
      automatic sitemap and RSS feed.
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
    <span class="project-card__status">Live · Discord Bot</span>
    <h3 class="project-card__title">Tom Bombadil Discord Bot</h3>
    <p class="project-card__desc">
      A Gemini-powered Discord bot deployed on my home server. Handles natural-language
      queries, command routing, and multi-turn conversation context. Deployed as a
      systemd service with automatic restart and structured logging.
    </p>
    <ul class="project-card__stack">
      <li>Python</li><li>Gemini API</li><li>discord.py</li><li>systemd</li><li>Linux</li>
    </ul>
    <div class="project-card__links">
      <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub →</a>
    </div>
  </article>

  <article class="project-card">
    <span class="project-card__status">Planned · AI / ML</span>
    <h3 class="project-card__title">Fantasy Football Draft Helper</h3>
    <p class="project-card__desc">
      A draft-time recommendation tool that ingests historical player stats and
      projection data, ranks remaining players by value-over-replacement, and
      surfaces AI-driven pick suggestions tuned to the user's roster construction.
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
  More project write-ups land on the <a href="{{ '/blog/' | relative_url }}">blog</a> as
  they ship. The full source tree lives on
  <a href="https://github.com/SolomonSmith-dev" target="_blank" rel="noopener">GitHub</a>.
</p>
