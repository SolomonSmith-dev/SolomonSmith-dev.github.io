---
layout: page
title: "About"
heading: "I build LLM systems that hold up in production."
eyebrow: "About"
permalink: /about/
description: "About Solomon Smith: AI/ML engineer focused on RAG, LLM evaluation, and agent infrastructure. CS senior at CSU San Bernardino after ten years as a professional chef."
lede: "AI/ML engineer and Computer Science senior at Cal State San Bernardino, graduating December 2026."
---

<img class="about-photo" src="{{ '/assets/images/headshot.jpg' | relative_url }}" alt="Portrait of Solomon Smith" width="410" height="600" loading="lazy" decoding="async">

I work on the systems side of AI: retrieval pipelines, evaluation harnesses, and the agent infrastructure that runs on top of them. Getting a model to answer is the easy part. The work I care about is proving the answer is grounded, catching a regression before it ships, and keeping the service running after the demo.

At Recursa AI I built ingestion and RAG over a legal corpus of 200K+ documents and an evaluation harness scored against human-labeled answers. That harness caught a 12% hallucination regression after a model swap, and the release was blocked. My own projects follow the same pattern: soc-triage-ai refuses to answer when retrieval is weak, and phishguard publishes the leakage tests that killed its first version.

## How I work

<ul class="principles">
  <li><strong>Measure first.</strong> I set up an eval or a test before I start tuning, so I can tell whether a change actually helped.</li>
  <li><strong>Find the real cause.</strong> soc-triage-ai's harness went from 43% to 100% because the problem was chunking, not the prompt.</li>
  <li><strong>Write it down.</strong> Model cards, LIMITATIONS files, and runbooks, so the next person doesn't have to reverse-engineer my decisions.</li>
</ul>

## Before engineering

I spent more than ten years in professional kitchens and worked my way from dishwasher to Head Chef in high-volume restaurants. I learned to run a team through a rush, fix problems in real time, and refine a process until it holds up every night. That is still how I approach production systems.

## What I'm looking for

Full-time AI/ML engineering roles starting January 2027, especially RAG and retrieval backends, LLM evaluation, or AI platform work. I'm based in Montclair, CA, and open to remote work or relocation.

## Education

<div class="entry">
  <div class="entry__head">
    <p class="entry__title">B.S. Computer Science <span class="entry__org">&middot; California State University, San Bernardino</span></p>
    <p class="entry__meta">Expected December 2026</p>
  </div>
  <ul>
    <li>Dean's List, Spring 2025 and Fall 2025</li>
    <li>Coursework: Machine Learning, Artificial Intelligence, Algorithms, Operating Systems, Computer Architecture, Statistics</li>
  </ul>
</div>

<div class="btn-row" style="margin-top: 2rem">
  <a class="btn btn--primary" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
  <a class="btn" href="{{ '/resume/' | relative_url }}">Read the resume</a>
  <a class="btn" href="https://linkedin.com/in/{{ site.linkedin_username }}" rel="noopener">LinkedIn</a>
</div>
