---
layout: page
title: "About"
heading: "I build LLM systems that hold up in production."
eyebrow: "About"
permalink: /about/
description: "About Solomon Smith, Forward Deployed Engineer for ML and AI systems. Founding Engineer at Recursa AI / CourtRules. CS senior at CSU San Bernardino after ten years as a professional chef."
lede: "Forward Deployed Engineer and Computer Science senior at Cal State San Bernardino, graduating December 2026."
---

<img class="about-photo" src="{{ '/assets/images/headshot.jpg' | relative_url }}" alt="Portrait of Solomon Smith" width="410" height="600" loading="lazy" decoding="async">

I build LLM-backed features for products where a confident wrong answer costs more than no answer, and I write the tests that prove they refuse correctly. Getting a model to answer is the easy part. The work I care about is proving the answer is grounded, refusing when it is not, and keeping the service running after the demo.

I'm a founding engineer at Recursa AI / CourtRules, the second engineer on a two-person team. I shipped the judge assistant, a retrieval-grounded Q&A feature that renders a claim only when its quoted sentence appears verbatim in the filed court order. Its tests caught a bypass, an invented quote passing on a plausible source index, before release. My own projects follow the same pattern: SOC Triage AI refuses out-of-scope alerts, ARDA's 577 passing tests run with no API keys or network, and PhishGuard documents the dataset leakage I found and fixed.

## How I work

<ul class="principles">
  <li><strong>Measure first.</strong> I set up an eval or a test before I start tuning, so I can tell whether a change actually helped.</li>
  <li><strong>Find the real cause.</strong> SOC Triage AI's reliability harness went from 3 of 7 to 7 of 7 cases because the problem was corpus chunking, not the prompt.</li>
  <li><strong>Write it down.</strong> READMEs, .env.example files, and LIMITATIONS.md, so the next person can run the code and understand my decisions without asking me.</li>
</ul>

## Before engineering

I spent more than ten years in professional kitchens and worked my way from dishwasher to Head Chef in high-volume restaurants. I learned to run a team through a rush, fix problems in real time, and refine a process until it holds up every night. That is still how I approach production systems.

## What I'm looking for

Full-time AI/ML and backend engineering roles starting January 2027, especially retrieval-grounded LLM features, LLM evaluation, or AI platform work. I'm based in Montclair, CA, and open to remote work or relocation.

## Education

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">B.S. Computer Science <span class="entry__org">&middot; California State University, San Bernardino</span></p>
    <p class="entry__meta">Expected December 2026</p>
  </div>
  <ul>
    <li>Coursework: Machine Learning, Artificial Intelligence, Algorithms, Operating Systems, Computer Architecture, Statistics</li>
  </ul>
</div>

<div class="btn-row" style="margin-top: 2rem">
  <a class="btn btn--primary" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
  <a class="btn" href="{{ '/resume/' | relative_url }}">Read the resume</a>
  <a class="btn" href="https://linkedin.com/in/{{ site.linkedin_username }}" rel="noopener">LinkedIn</a>
</div>
