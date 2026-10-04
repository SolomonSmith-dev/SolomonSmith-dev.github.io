---
layout: home
title: "AI/ML Engineer"
description: "Solomon Smith, AI/ML engineer building RAG, evaluation, and multi-agent systems. CS senior at CSU San Bernardino, graduating December 2026. Open to full-time AI/ML engineering roles starting January 2027."
permalink: /
hero_lede: "Most recently at Recursa AI, I shipped RAG over 200K+ legal documents and built the evaluation harness that blocked a 12% hallucination regression before release. Before engineering, I spent ten years running professional kitchens."
availability: "Graduating Dec 2026, B.S. Computer Science. Open to full-time AI/ML engineering roles from January 2027."
---

<ul class="metrics" aria-label="Selected results">
  <li class="metric"><span class="metric__value">200K+</span><span class="metric__label">legal documents ingested at 99%+ extraction accuracy</span></li>
  <li class="metric"><span class="metric__value">4s &rarr; &lt;600ms</span><span class="metric__label">RAG query latency on a production legal corpus</span></li>
  <li class="metric"><span class="metric__value">12%</span><span class="metric__label">hallucination regression caught and blocked before release</span></li>
</ul>
<p class="metrics__source">Software Engineering Intern, Recursa AI, Dec 2025 to Mar 2026.</p>

<section class="section" id="work" aria-labelledby="work-title">
  <div class="section__head">
    <h2 class="section__title" id="work-title">Selected work</h2>
    <a class="text-link" href="{{ '/projects/' | relative_url }}">All projects</a>
  </div>

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
      </dl>
      <div class="project__foot">
        <ul class="stack"><li>Python</li><li>Claude API</li><li>sentence-transformers</li><li>ChromaDB</li><li>Streamlit</li><li>pytest</li></ul>
        <div class="project__links">
          <a href="https://github.com/SolomonSmith-dev/soc-triage-ai" rel="noopener">Source</a>
          <a href="https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9" rel="noopener">Video walkthrough</a>
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
        <div class="project__links">
          <a href="https://github.com/SolomonSmith-dev/phishguard" rel="noopener">Source</a>
        </div>
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
        <div class="project__links">
          <a href="https://github.com/SolomonSmith-dev/arda" rel="noopener">Source</a>
        </div>
      </div>
    </article>

  </div>
</section>

<section class="section" aria-labelledby="exp-title">
  <div class="section__head">
    <h2 class="section__title" id="exp-title">Experience</h2>
    <a class="text-link" href="{{ '/resume/' | relative_url }}">Full resume</a>
  </div>

  <ol class="timeline">
    <li class="timeline__item">
      <p class="timeline__date">Dec 2025 to Mar 2026</p>
      <div>
        <p><span class="timeline__role">Software Engineering Intern</span> <span class="timeline__org">&middot; Recursa AI</span></p>
        <p class="timeline__note">Scraping pipeline across 50+ U.S. jurisdictions, RAG with hybrid keyword search over the resulting legal corpus, and an evaluation harness scored against human-labeled ground truth.</p>
      </div>
    </li>
    <li class="timeline__item">
      <p class="timeline__date">Jun 2025 to Sep 2025</p>
      <div>
        <p><span class="timeline__role">Full-Stack Developer Intern</span> <span class="timeline__org">&middot; RideSplits</span></p>
        <p class="timeline__note">Moved every auth flow from JWT to Firebase Auth (60% fewer login bugs), integrated Stripe Connect, and built real-time sync with Socket.IO.</p>
      </div>
    </li>
    <li class="timeline__item">
      <p class="timeline__date">Feb 2026 to present</p>
      <div>
        <p><span class="timeline__role">Student Administrative Assistant</span> <span class="timeline__org">&middot; Office of Student Research and Innovation, CSUSB</span></p>
        <p class="timeline__note">Onboarding, documentation, and research compliance tracking for university-wide programs.</p>
      </div>
    </li>
    <li class="timeline__item">
      <p class="timeline__date">Jun 2023 to May 2025</p>
      <div>
        <p><span class="timeline__role">IT Student Assistant</span> <span class="timeline__org">&middot; Ca&ntilde;ada College</span></p>
        <p class="timeline__note">Hardware, software, and network support for 100+ users across Linux, Windows, and macOS labs.</p>
      </div>
    </li>
    <li class="timeline__item">
      <p class="timeline__date">10+ years</p>
      <div>
        <p><span class="timeline__role">Head Chef, Chef de Cuisine, Kitchen Manager</span> <span class="timeline__org">&middot; High-volume restaurants</span></p>
        <p class="timeline__note">Dishwasher to Head Chef. Ran teams and service under pressure with no room for error.</p>
      </div>
    </li>
  </ol>
</section>

<section class="section" aria-labelledby="skills-title">
  <div class="section__head">
    <h2 class="section__title" id="skills-title">Skills</h2>
  </div>
  <div class="skills">
    <div>
      <h3 class="skills__title">AI / ML</h3>
      <ul><li>RAG, hybrid search</li><li>LLM evaluation harnesses</li><li>Claude API, LangChain, MCP</li><li>pgvector, ChromaDB</li><li>sentence-transformers</li><li>PyTorch, scikit-learn</li></ul>
    </div>
    <div>
      <h3 class="skills__title">Backend</h3>
      <ul><li>FastAPI</li><li>Node.js, Express</li><li>PostgreSQL, MySQL, Redis</li><li>Firebase, Supabase</li><li>REST APIs</li></ul>
    </div>
    <div>
      <h3 class="skills__title">Infrastructure</h3>
      <ul><li>Docker, Linux, systemd</li><li>PM2, Nginx, Tailscale</li><li>GitHub Actions</li><li>GCP, AWS</li></ul>
    </div>
    <div>
      <h3 class="skills__title">Languages</h3>
      <ul><li>Python</li><li>TypeScript, JavaScript</li><li>SQL</li><li>C++</li><li>Bash</li></ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="bg-title">
  <div class="split">
    <h2 class="split__lead" id="bg-title">Ten years in professional kitchens taught me how to run a system under pressure.</h2>
    <div class="split__body">
      <p>I worked my way from dishwasher to Head Chef in high-volume restaurants. Service runs on preparation, clear handoffs, and catching problems before they reach the guest.</p>
      <p>I apply the same habits to software. I measure before I ship, I find the root cause when something breaks, and I write things down so the next person can keep it running. <a href="{{ '/about/' | relative_url }}">More about me</a>.</p>
    </div>
  </div>
</section>

<section class="contact" aria-labelledby="contact-title">
  <h2 class="contact__title" id="contact-title">Hiring for an AI/ML or backend role?</h2>
  <p class="contact__body">I'm available full-time from January 2027, based in Montclair, CA, and open to remote work or relocation. Email reaches me fastest.</p>
  <div class="btn-row">
    <a class="btn btn--primary" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
    <a class="btn" href="{{ '/assets/resume/SolomonSmithResume.pdf' | relative_url }}">Download resume</a>
    <a class="btn" href="https://linkedin.com/in/{{ site.linkedin_username }}" rel="noopener">LinkedIn</a>
  </div>
  <p class="contact__email">{{ site.email }}</p>
</section>
