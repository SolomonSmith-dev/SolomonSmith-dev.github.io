---
layout: page
wide: true
title: "Projects"
heading: "Work"
eyebrow: "Projects"
permalink: /projects/
description: "Projects by Solomon Smith: applied AI systems, LLM evaluation, security tooling, and the self-hosted infrastructure under them."
lede: "Production LLM features and the services and infrastructure behind them. Every number on these cards is reproduced by a command in that project's README, or comes from my resume where the code is private. Every entry links to its source or live product."
---

<h2 class="visually-hidden">All projects</h2>
<div class="projects">
  {% include card-courtrules.html %}
  {% include card-arda.html %}
  {% include card-soc-triage.html %}
  {% include card-sentinel.html %}
  {% include card-phishguard.html %}
  {% include card-agentic-engineering-os.html %}
  {% include card-docmind.html %}
</div>

<section class="contact" aria-labelledby="contact-title">
  <h2 class="contact__title" id="contact-title">Want to see one of these up close?</h2>
  <p class="contact__body">Each card links to a page with what the project does, why it is hard, and the command that reproduces every number. I'm happy to walk through the architecture, the tradeoffs, or the bugs behind any of them.</p>
  <div class="btn-row">
    <a class="btn btn--primary" href="mailto:{{ site.email }}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>
    <a class="btn" href="https://github.com/{{ site.github_username }}" rel="noopener">GitHub profile</a>
  </div>
</section>
