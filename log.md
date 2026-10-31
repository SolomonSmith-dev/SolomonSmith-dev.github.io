---
layout: page
title: "Log"
permalink: /log/
description: "A weekly log of what Solomon Smith is building, generated from GitHub activity every Monday."
eyebrow: "Log"
lede: "What I worked on, week by week. Activity is pulled from the GitHub API every Monday. Notes are mine."
---

{%- for w in site.data.activity_log %}
<section class="log-week" aria-labelledby="week-{{ w.week_start }}">
  <h2 class="log-week__title" id="week-{{ w.week_start }}">{{ w.week_start | date: "%b %-d" }} to {{ w.week_end | date: "%b %-d, %Y" }}</h2>
  {%- for n in site.data.log_notes %}
  {%- assign note_week = n.week | date: "%Y-%m-%d" %}
  {%- if note_week == w.week_start %}
  <p class="log-week__note">{{ n.note | escape }}</p>
  {%- endif %}
  {%- endfor %}
  {% include activity-week.html week=w %}
</section>
{%- endfor %}

<p class="activity__source">Commits are counted on each repo's default branch. Private repos are shown as totals only.</p>
