---
layout: page
title: "Resume"
permalink: /resume/
description: "Resume of Solomon Smith — Computer Science student and aspiring software engineer."
---

<p>
  <a class="btn btn--primary" href="{{ '/assets/resume/SolomonJobResume2025.pdf' | relative_url }}" target="_blank" rel="noopener">Download PDF Resume</a>
  <a class="btn btn--ghost" href="mailto:solomonsmithdev@gmail.com">Email Me</a>
</p>

<h2 class="section-heading">Summary</h2>

Computer Science student at CSU San Bernardino focused on AI/ML and full-stack engineering.
Comfortable across the stack — Python, C++, JavaScript, FastAPI, React — and with the
infrastructure to ship: Docker, Linux, Git/GitHub. Bringing a decade of culinary-industry
discipline (precision, ownership, working under pressure) into software. Seeking
**Summer / Fall 2026 software engineering or AI/ML internships**.

<h2 class="section-heading">Education</h2>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">B.S. Computer Science — California State University, San Bernardino</p>
    <p class="entry__meta">Expected 2026</p>
  </div>
  <ul>
    <li>Coursework: Data Structures &amp; Algorithms, OOP, Computer Architecture, Discrete Math</li>
    <li>Self-directed study: Applied Machine Learning, Backend Systems, Linux/Networking</li>
  </ul>
</div>

<h2 class="section-heading">Technical Skills</h2>

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

<h2 class="section-heading">Selected Projects</h2>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">SOC Triage Copilot — AI Security Triage System</p>
    <p class="entry__meta">Python · FastAPI · PostgreSQL · Next.js · TypeScript · Docker</p>
  </div>
  <ul>
    <li>Designing and building a full-stack AI triage system: ingests raw security alerts,
      classifies severity via a rules-free ML engine, and maps findings to MITRE ATT&amp;CK
      techniques.</li>
    <li>FastAPI backend with argon2id auth, alembic-managed Postgres schema, append-only
      analyst override log, full audit trail. Next.js TypeScript dashboard for analyst review.</li>
    <li>43+ tests across engine and API layers; GitHub Actions CI with parallel test jobs.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Earendil Distributed Task System</p>
    <p class="entry__meta">Python · FastAPI · OAuth · systemd · Linux · Tailscale</p>
  </div>
  <ul>
    <li>Built a self-hosted distributed task execution system running on a home Mac Mini
      server, exposed via REST API for dispatching and monitoring long-running tasks.</li>
    <li>OAuth/token auth, systemd-managed daemon with automatic restart, structured logging;
      33/33 tests passing. Powers several personal automation pipelines.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">TargetRecon CLI — Python OSINT Tool</p>
    <p class="entry__meta">Open Source · In Progress</p>
  </div>
  <ul>
    <li>Designing a CLI that takes a username, domain, or IP and runs a structured set of
      OSINT lookups (DNS, WHOIS, social handle discovery, public breach data).</li>
    <li>Modular command structure with <code>argparse</code> subcommands; JSON-first output
      for downstream tooling.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Plex Home Server — Self-Hosted Media Infra</p>
    <p class="entry__meta">Raspberry Pi · Linux · Docker</p>
  </div>
  <ul>
    <li>Built a Dockerized Plex media server on a Raspberry Pi with secured remote access.</li>
    <li>Automated nightly backups of media metadata and Plex configuration; configured
      dynamic DNS for stable external reachability.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Personal Portfolio Site — Jekyll on GitHub Pages</p>
    <p class="entry__meta">Live at solomon-smith-dev.tech</p>
  </div>
  <ul>
    <li>Custom Jekyll build with hand-written Sass theme on top of Minima; custom
      layouts, SEO-tagged pages, sitemap, and RSS feed.</li>
    <li>Deployed via GitHub Pages with custom domain and TLS.</li>
  </ul>
</div>

<h2 class="section-heading">Experience</h2>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Culinary Industry — 10+ years</p>
    <p class="entry__meta">Pre-CS career</p>
  </div>
  <ul>
    <li>Worked across high-volume operations where precision, repeatability, and recovery
      under pressure decided whether the night shipped on time.</li>
    <li>Trained and led junior staff; owned end-to-end stations the way I now own
      end-to-end services.</li>
  </ul>
</div>

<p style="margin-top: 1.5rem; opacity: 0.8;">
  For the formatted PDF version, use the <strong>Download PDF Resume</strong> button at
  the top of this page.
</p>
