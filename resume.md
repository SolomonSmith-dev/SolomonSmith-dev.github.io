---
layout: page
title: "Resume"
permalink: /resume/
description: "Resume of Solomon Smith. CS senior at CSUSB and AI/ML engineer."
lede: "AI/ML engineering, applied LLM systems, and the backend infrastructure that puts them in production."
---

<p class="cta-row cta-row--top">
  <a class="btn btn--primary" href="{{ '/assets/resume/SolomonSmithResume.pdf' | relative_url }}" target="_blank" rel="noopener">Download PDF</a>
  <a class="btn" href="mailto:solomonsmithdev@gmail.com?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
</p>

## Summary

CS senior at CSU San Bernardino. Over a decade in professional kitchens (dishwasher to Head Chef) before pivoting into engineering. Now building LLM pipelines, RAG systems, and multi-agent infrastructure. Strong foundation in Python, C++, and systems thinking. Targeting **internships for Summer 2026** and **full-time AI/ML engineering roles starting January 2027**.

## Experience

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Software Engineering Intern, Recursa AI (courtrules.app)</p>
    <p class="entry__meta">Dec 2025 to Mar 2026 &middot; Remote</p>
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
    <p class="entry__title">Full-Stack Developer Intern, RideSplits</p>
    <p class="entry__meta">Jun 2025 to Sep 2025 &middot; San Bernardino, CA</p>
  </div>
  <ul>
    <li>Migrated 100% of authentication flows from JWT to Firebase Auth across multiple user roles; reduced login-related bugs by 60%.</li>
    <li>Designed secure multi-screen document upload pipeline with validation and size limits, enabling ID verification for 50+ users.</li>
    <li>Integrated Stripe Connect for driver onboarding, payments, and webhook-based transaction tracking.</li>
    <li>Designed and executed MySQL schema migrations; implemented real-time sync infrastructure with Socket.IO.</li>
    <li>Developed RESTful APIs supporting user authentication, profiles, rides, and real-time features.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Student Administrative Assistant, Office of Student Research and Innovation, CSUSB</p>
    <p class="entry__meta">Feb 2026 to present &middot; San Bernardino, CA</p>
  </div>
  <ul>
    <li>Supporting operational coordination for university-wide student research and innovation initiatives.</li>
    <li>Onboarding, documentation management, and research compliance tracking.</li>
    <li>Workflow optimization and event logistics for research workshops and innovation programs.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">IT Student Assistant, Cañada College</p>
    <p class="entry__meta">Jun 2023 to May 2025 &middot; Redwood City, CA</p>
  </div>
  <ul>
    <li>Improved system reliability by 20% through troubleshooting hardware, software, and networking for 100+ institutional users.</li>
    <li>Resolved 90% of technical support requests within 24 hours; maintained Linux, Windows, and macOS lab systems.</li>
    <li>Standardized laboratory software environments and documented system configurations to eliminate setup inconsistencies.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Culinary Leadership: Head Chef, Chef de Cuisine, Kitchen Manager</p>
    <p class="entry__meta">10+ years &middot; Various</p>
  </div>
  <ul>
    <li>Progressed from dishwasher to Head Chef across multiple high-volume operations. The same discipline, precision, ownership, and recovery under pressure, now applied to production systems.</li>
  </ul>
</div>

## Technical Skills

<div class="stations">
  <div class="station">
    <p class="station__name">Languages</p>
    <ul class="station__list">
      <li>Python</li><li>C++</li><li>JavaScript</li><li>TypeScript</li><li>SQL</li><li>Bash</li><li>R</li>
    </ul>
  </div>
  <div class="station">
    <p class="station__name">AI / ML</p>
    <ul class="station__list">
      <li>LangChain</li><li>Claude API</li><li>RAG, pgvector, Milvus</li><li>sentence-transformers</li><li>scikit-learn, PyTorch</li><li>Multi-agent orchestration, MCP</li>
    </ul>
  </div>
  <div class="station">
    <p class="station__name">Backend &amp; Data</p>
    <ul class="station__list">
      <li>FastAPI, Express, Django</li><li>Node.js, React</li><li>PostgreSQL, MySQL, Redis</li><li>Firebase, Supabase</li><li>REST APIs, Stripe, Socket.IO</li>
    </ul>
  </div>
  <div class="station">
    <p class="station__name">Infra &amp; Cloud</p>
    <ul class="station__list">
      <li>Docker, Linux, systemd</li><li>PM2, Nginx, Tailscale</li><li>GitHub Actions</li><li>GCP, AWS (S3, EC2)</li>
    </ul>
  </div>
</div>

## Selected Projects

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">soc-triage-ai &middot; RAG-grounded security alert triage</p>
    <p class="entry__meta">Python &middot; Claude API &middot; sentence-transformers &middot; Streamlit &middot; pytest</p>
  </div>
  <ul>
    <li>Built RAG-grounded security alert triage system mapping alerts to MITRE ATT&amp;CK techniques with strict JSON schema validation; 100% pass rate across a 7-case reliability harness.</li>
    <li>Engineered guardrail logic that refuses to triage low-similarity alerts and validates LLM output structurally, preventing fabrication and confident wrong-answer failures in security contexts.</li>
    <li>Improved harness pass rate from 43% to 100% by diagnosing the root cause as corpus chunking rather than prompt design; documented full reflection in a model card.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Multi-Agent AI System (Sauron Stack)</p>
    <p class="entry__meta">Python &middot; Node.js &middot; Redis &middot; PM2 &middot; Claude API &middot; Tailscale &middot; Docker</p>
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
    <p class="entry__meta">Python &middot; pygame &middot; numpy &middot; pytest</p>
  </div>
  <ul>
    <li>Implemented Minimax with alpha-beta pruning for a 5x5 Tic-Tac-Toe agent at depth 4 with sub-500ms latency across 1,000+ game states; center-and-corner heuristic cut effective search space by ~40%.</li>
    <li>Solved Constraint Satisfaction Problems for 5 vehicles and 20+ constraints using backtracking with arc-consistency, achieving 100% conflict-free assignment.</li>
    <li>21-case pytest suite and GitHub Actions CI verify GameStatus, minimax/negamax behavior, and CSP solution validity.</li>
  </ul>
</div>

## Education

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">B.S. Computer Science, California State University, San Bernardino</p>
    <p class="entry__meta">Jul 2024 to Dec 2026 (Expected)</p>
  </div>
  <ul>
    <li><strong>Honors:</strong> Dean's List Spring 2025, Dean's List Fall 2025</li>
    <li><strong>GPA:</strong> 3.14</li>
    <li><strong>Coursework:</strong> Machine Learning, Artificial Intelligence, Algorithms, Operating Systems, Computer Architecture, Statistics</li>
  </ul>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Computer Science, Skyline College</p>
    <p class="entry__meta">Aug 2022 to Jun 2024</p>
  </div>
</div>

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">Computer Science, Butte College</p>
    <p class="entry__meta">2020 to 2022</p>
  </div>
</div>

## Certifications

- Google IT Support Specialization
- Google Cloud Computing Foundations Certificate

<p class="resume-note">
  For the formatted PDF version, use the <strong>Download PDF</strong> button at the top of this page.
</p>
