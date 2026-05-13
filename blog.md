---
layout: page
title: "Writing"
permalink: /blog/
description: "Writing by Solomon Smith. Project updates, build logs, and technical notes from the work in progress."
lede: "Project updates, build logs, and technical notes from the work in progress."
---

<ul class="post-list">
  {%- for post in site.posts -%}
  <li>
    <p class="post-list__meta">{{ post.date | date: "%b %-d, %Y" }}</p>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
    {%- if post.excerpt -%}
    <p>{{ post.excerpt | strip_html | truncate: 200 }}</p>
    {%- endif -%}
  </li>
  {%- endfor -%}
</ul>
