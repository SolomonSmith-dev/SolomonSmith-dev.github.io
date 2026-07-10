---
layout: post
title: "Building My Portfolio Site"
date: 2024-04-22 12:00:00 -0700
categories: portfolio update
description: "Notes from shipping the first version of my portfolio site. Jekyll, GitHub Pages, and the bugs I hit along the way."
redirect_from:
  - /portfolio/update/2024/04/22/first-post.html
  - /2024/04/22/first-post.html
---

Today I shipped the first real version of my portfolio site. Hosted on GitHub Pages,
generated with Jekyll, written from scratch instead of cloning a template.

This post is the build log.

## What I shipped

- A fresh Jekyll project, no template: `index.md`, About, Projects, Blog, Resume
- GitHub Pages deployment with a custom domain (`CNAME` + DNS)
- The Minima theme as a starting point
- SEO, sitemap, and RSS feed plugins wired up
- A first blog post (this one) and a downloadable resume

## Skills I practiced

- Git fundamentals: branching, fixing wrong-remote pushes, clean commits
- GitHub Pages deployment workflow end-to-end
- Jekyll's YAML front matter, layouts, and the `_pages` collection
- Basic SEO: meta descriptions, OpenGraph, sitemap submission
- Debugging Liquid/Sass issues inside the Minima theme
- Configuring a custom domain with TLS

## Obstacles I hit

- Bundler / Jekyll install friction on a fresh machine
- A pre-existing GitHub Pages repo conflicting with the custom domain. Had to
  archive the old one before DNS would point cleanly
- A footer rendering bug caused by Minima expecting `author` as a string when I had
  it set as an object. Fixed by updating `_config.yml` to match the schema
- Generally, learning to read theme source code instead of guessing at fixes

## What came next

- Rewrote all pages with real project content (TargetRecon CLI, Earendil, SOC Triage Copilot)
- Built a custom dark Sass theme on top of Minima -- project cards, skills grid, sticky header
- Started writing about the AI/ML work: see [Building a SOC Triage Copilot](/blog/building-soc-triage-copilot/)

First sprint done. Site is live. The work continues.
