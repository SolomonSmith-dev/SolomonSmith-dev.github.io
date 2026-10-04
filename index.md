---
layout: home
title: "Software Engineer"
description: "Solomon Smith, software engineer building LLM-backed backend features that fail closed. Founding Engineer at Recursa AI / CourtRules. B.S. Computer Science, CSU San Bernardino, December 2026. Open to full-time AI/ML and backend engineering roles starting January 2027."
permalink: /
hero_lede: "As a founding engineer at Recursa AI / CourtRules, I shipped a retrieval-grounded assistant that shows a claim only when its quoted sentence appears verbatim in the filed court order. Before engineering, I spent ten years running professional kitchens."
availability: "Graduating Dec 2026, B.S. Computer Science. Open to full-time AI/ML and backend engineering roles from January 2027."
---

<ul class="metrics" aria-label="Selected results">
  <li class="metric"><span class="metric__value">7 tests</span><span class="metric__label">on the CourtRules citation verifier caught a quote-forgery bypass before release</span></li>
  <li class="metric"><span class="metric__value">425</span><span class="metric__label">ARDA tests that run offline, with no API keys or network, in 13 seconds</span></li>
  <li class="metric"><span class="metric__value">0.9943</span><span class="metric__label">test AUC on the PhishGuard URL classifier, 1.54% false positives on Tranco top-5000</span></li>
</ul>

<section class="section" id="work" aria-labelledby="work-title">
  <div class="section__head">
    <h2 class="section__title" id="work-title">Selected work</h2>
    <a class="text-link" href="{{ '/projects/' | relative_url }}">All projects</a>
  </div>

  <div class="projects">
{% include card-courtrules.html %}
{% include card-arda.html %}
{% include card-phishguard.html %}
{% include card-soc-triage.html %}
  </div>
</section>

<section class="section" aria-labelledby="exp-title">
  <div class="section__head">
    <h2 class="section__title" id="exp-title">Experience</h2>
    <a class="text-link" href="{{ '/resume/' | relative_url }}">Full resume</a>
  </div>

  <ol class="timeline">
    <li class="timeline__item">
      <p class="timeline__date">Jul 2026 to present</p>
      <div>
        <p><span class="timeline__role">Founding Engineer</span> <span class="timeline__org">&middot; Recursa AI / CourtRules</span></p>
        <p class="timeline__note">Second engineer on a two-person team. Shipped the retrieval-grounded judge assistant, query analytics that separate data gaps from retrieval failures, and iCal and CSV court-calendar exports.</p>
      </div>
    </li>
    <li class="timeline__item">
      <p class="timeline__date">Jun 2025 to Sep 2025</p>
      <div>
        <p><span class="timeline__role">Full-Stack Developer (contract)</span> <span class="timeline__org">&middot; RideSplits</span></p>
        <p class="timeline__note">Migrated authentication from custom JWT to Firebase Auth across rider and driver roles, with role-based access rules for Firestore and Storage.</p>
      </div>
    </li>
    <li class="timeline__item">
      <p class="timeline__date">Jun 2023 to May 2025</p>
      <div>
        <p><span class="timeline__role">IT Student Assistant</span> <span class="timeline__org">&middot; Ca&ntilde;ada College</span></p>
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
  {% include skills.html %}
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
