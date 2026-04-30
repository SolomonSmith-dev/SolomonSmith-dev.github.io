---
layout: page
title: "Resume"
permalink: /resume/
description: "Resume of Solomon Smith — CS senior at CSUSB and AI/ML engineer."
---

<p>
  <a class="btn btn--primary" href="{{ '/assets/resume/SolomonJobResume2025.pdf' | relative_url }}" target="_blank" rel="noopener">Download PDF Resume</a>
  <a class="btn btn--ghost" href="mailto:solomonsmithdev@gmail.com">Email Me</a>
</p>

<h2 class="section-heading">Summary</h2>

CS senior at CSUSB with a background in high-pressure kitchens (dishwasher to Head Chef,
~10 years) redirected into software engineering and AI. Strong foundation in Python, C++,
and systems thinking. Currently building LLM pipelines, RAG systems, and multi-agent
infrastructure. Targeting **AI/ML engineering roles starting January 2027**.

<h2 class="section-heading">Experience</h2>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Software Engineering Intern — Recursa AI (courtrules.app)</p>
    <p class="entry__meta">Dec 2025 – Mar 2026 · Remote</p>
  </div>
  <ul>
    <li>Built distributed scraping pipeline ingesting court rules across 50+ U.S. jurisdictions; retry, backoff, and deduplication layers handling 200K+ documents at 99%+ extraction accuracy.</li>
    <li>Shipped RAG system over normalized legal corpus using vector embeddings and hybrid keyword search; reduced query latency from 4s to under 600ms.</li>
    <li>Designed evaluation harness scoring legal-text answer accuracy against human-labeled ground truth; caught a 12% hallucination regression after a model swap and blocked the release.</li>
    <li>Authored Python data pipelines (Postgres, S3, scheduled jobs) and CI checks for schema drift; reduced production data incidents by 70%.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Full-Stack Developer Intern — RideSplits</p>
    <p class="entry__meta">Jun 2025 – Sep 2025 · San Bernardino, CA</p>
  </div>
  <ul>
    <li>Migrated 100% of authentication flows from JWT to Firebase Auth across multiple user roles; reduced login-related bugs by 60%.</li>
    <li>Designed secure multi-screen document upload pipeline with validation and size limits, enabling ID verification for 50+ users.</li>
    <li>Integrated Stripe Connect for secure driver onboarding, payments, and webhook-based transaction tracking.</li>
    <li>Designed and executed MySQL schema migrations; implemented real-time sync infrastructure with Socket.IO.</li>
    <li>Developed RESTful APIs supporting user authentication, profiles, rides, and real-time features.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Student Administrative Assistant — Office of Student Research and Innovation, CSUSB</p>
    <p class="entry__meta">Feb 2026 – Present · San Bernardino, CA</p>
  </div>
  <ul>
    <li>Supporting operational coordination for university-wide student research and innovation initiatives.</li>
    <li>Assisting in onboarding, documentation management, and research compliance tracking.</li>
    <li>Contributing to workflow optimization and event logistics for research workshops and innovation programs.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">IT Student Assistant — Cañada College</p>
    <p class="entry__meta">Jun 2023 – May 2025 · Redwood City, CA</p>
  </div>
  <ul>
    <li>Improved system reliability by 20% through troubleshooting hardware, software, and networking for 100+ institutional users.</li>
    <li>Resolved 90% of technical support requests within 24 hours; maintained Linux, Windows, and macOS lab systems.</li>
    <li>Standardized laboratory software environments and documented system configurations to eliminate setup inconsistencies.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Culinary Leadership — Head Chef / Chef de Cuisine / Kitchen Manager</p>
    <p class="entry__meta">~10 years · Various</p>
  </div>
  <ul>
    <li>Progressed from dishwasher to Head Chef across multiple high-volume operations.
      The same discipline — precision, ownership, and recovery under pressure — now
      applied to production systems.</li>
  </ul>
</div>

<h2 class="section-heading">Technical Skills</h2>

<div class="skills-grid">
  <div class="skills-grid__cell">
    <h4>Languages</h4>
    <ul>
      <li>Python</li><li>C++</li><li>JavaScript</li><li>TypeScript</li><li>SQL</li><li>Bash</li><li>R</li>
    </ul>
  </div>
  <div class="skills-grid__cell">
    <h4>AI / ML</h4>
    <ul>
      <li>LangChain</li><li>Anthropic Claude API</li><li>RAG</li><li>pgvector</li><li>Milvus</li><li>sentence-transformers</li><li>scikit-learn</li><li>PyTorch</li><li>NLP</li><li>Multi-agent orchestration</li><li>MCP</li>
    </ul>
  </div>
  <div class="skills-grid__cell">
    <h4>Backend &amp; Data</h4>
    <ul>
      <li>FastAPI</li><li>Express</li><li>Django</li><li>Node.js</li><li>React</li><li>PostgreSQL</li><li>MySQL</li><li>Redis</li><li>Firebase</li><li>Supabase</li><li>REST APIs</li><li>Stripe Connect</li><li>Socket.IO</li>
    </ul>
  </div>
  <div class="skills-grid__cell">
    <h4>Infra &amp; Cloud</h4>
    <ul>
      <li>Docker</li><li>Linux</li><li>systemd</li><li>PM2</li><li>Nginx</li><li>Tailscale</li><li>GitHub Actions</li><li>GCP</li><li>AWS (S3, EC2)</li>
    </ul>
  </div>
</div>

<h2 class="section-heading">Selected Projects</h2>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">SOC Triage AI — RAG-Grounded Security Alert Triage</p>
    <p class="entry__meta">Python · Claude API · sentence-transformers · Streamlit · pytest · <a href="https://github.com/SolomonSmith-dev/soc-triage-ai" target="_blank" rel="noopener">GitHub →</a></p>
  </div>
  <ul>
    <li>Built RAG-grounded security alert triage system mapping alerts to MITRE ATT&amp;CK techniques with strict JSON schema validation; achieved 100% pass rate across a 7-case reliability harness.</li>
    <li>Engineered guardrail logic that refuses to triage low-similarity alerts and validates LLM output structurally, preventing fabrication and confident wrong-answer failures in security contexts.</li>
    <li>Diagnosed root cause of 43% harness failure rate as corpus chunking rather than prompt design; improved to 100% pass rate after corpus rebuild.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Multi-Agent AI System — Sauron Stack</p>
    <p class="entry__meta">Python · Node.js · Redis · PM2 · Anthropic Claude API · Tailscale · Docker</p>
  </div>
  <ul>
    <li>Built production multi-agent system on Debian server with PM2-managed services: router (Earendil), executor (Sauron), orchestrator (Morgoth), security daemon (Balrog); 24/7 uptime over Tailscale mesh.</li>
    <li>Diagnosed 401 crash-loop cascade in executor by tracing rate-limit headers; implemented exponential backoff and request queuing to restore stability.</li>
    <li>Resolved Node/native module ABI mismatch by rebuilding under Node v24, unblocking Redis-backed memory store across distributed agents.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Adversarial Search and Intelligent Agents</p>
    <p class="entry__meta">Python · Pygame</p>
  </div>
  <ul>
    <li>Implemented Minimax with alpha-beta pruning for a 5x5 Tic-Tac-Toe agent at depth 4 with sub-500ms latency across 1,000+ game states; center-and-corner heuristic cut effective search space by ~40%.</li>
    <li>Solved Constraint Satisfaction Problems for 5 vehicles and 20+ constraints using backtracking with arc-consistency, achieving 100% conflict-free assignment.</li>
  </ul>
</div>

<h2 class="section-heading">Education</h2>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">B.S. Computer Science — California State University, San Bernardino</p>
    <p class="entry__meta">Jul 2024 – Dec 2026 (Expected)</p>
  </div>
  <ul>
    <li><strong>Honors:</strong> Dean's List Spring 2025, Dean's List Fall 2025</li>
    <li><strong>Coursework:</strong> Machine Learning, Artificial Intelligence, Algorithms, Operating Systems, Computer Architecture, Statistics</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Computer Science — Skyline College</p>
    <p class="entry__meta">Aug 2022 – Jun 2024</p>
  </div>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Computer Science — Butte College</p>
    <p class="entry__meta">2020 – 2022</p>
  </div>
</div>

<h2 class="section-heading">Certifications</h2>

- Google IT Support Specialization
- Google Cloud Computing Foundations Certificate

<p style="margin-top: 1.5rem; opacity: 0.8;">
  For the formatted PDF version, use the <strong>Download PDF Resume</strong> button at
  the top of this page.
</p>
