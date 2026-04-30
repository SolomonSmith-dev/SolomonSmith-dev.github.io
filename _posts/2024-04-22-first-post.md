---
layout: post
title: "Building My Portfolio Site"
date: 2024-04-22 12:00:00 -0700
categories: portfolio update
description: "Notes from shipping the first version of solomon-smith-dev.tech — Jekyll, GitHub Pages, custom domain, and the bugs I hit along the way."
---

Today I shipped the first real version of my portfolio site at
[solomon-smith-dev.tech](https://solomon-smith-dev.tech). Hosted on GitHub Pages,
generated with Jekyll, written from scratch instead of cloning a template.

This post is the build log.

## What I shipped

- A fresh Jekyll project, no template — `index.md`, About, Projects, Blog, Resume
- GitHub Pages deployment with a custom domain (`CNAME` + DNS)
- The Minima theme as a starting point
- SEO, sitemap, and RSS feed plugins wired up
- A first blog post (this one) and a downloadable resume

## Skills I practiced

- Git fundamentals — branching, fixing wrong-remote pushes, clean commits
- GitHub Pages deployment workflow end-to-end
- Jekyll's YAML front matter, layouts, and the `_pages` collection
- Basic SEO — meta descriptions, OpenGraph, sitemap submission
- Debugging Liquid/Sass issues inside the Minima theme
- Configuring a custom domain with TLS

## Obstacles I hit

- Bundler / Jekyll install friction on a fresh machine
- A pre-existing GitHub Pages repo conflicting with the custom domain — had to
  archive the old one before DNS would point cleanly
- A footer rendering bug caused by Minima expecting `author` as a string when I had
  it set as an object — fixed by updating `_config.yml` to match the schema
- Generally, learning to read theme source code instead of guessing at fixes

## What's next

- Document each project in more depth (TargetRecon CLI, Plex server, future ML work)
- Replace Minima's default look with my own Sass theme on top of it
- Start writing about the AI/ML side — model experiments, NLP, classification

First sprint is done. Site is live. More to come.
