# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is
Personal portfolio site for Solomon Smith. Jekyll + GitHub Pages with a Matrix terminal aesthetic.
Live at: https://solomonsmith.dev (CNAME in repo root; falls back to https://solomonsmith-dev.github.io)

## Owner
Solomon Smith. CS senior at CSUSB, targeting AI/ML engineering roles starting January 2027.
Email: solomonsmithdev@gmail.com | GitHub: SolomonSmith-dev | LinkedIn: solomonsmithdev

## Commands

```bash
bundle install                              # install dependencies
bundle exec jekyll serve --livereload       # local dev at http://localhost:4000
bundle exec jekyll build                   # production build only
```

Pages CI triggers on every push to `main` (30-60s build). If `bundle exec` fails, run `gem install bundler` -- Solomon's machine has had a Ruby/bundler version mismatch.

## Stack
- Jekyll 4.4.x on GitHub Pages.
- `assets/main.scss` is the single, standalone stylesheet. It does NOT import Minima. Minima is still declared as the gem `theme` but all layouts and styles are fully overridden.
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-sitemap.
- Fonts: JetBrains Mono only, loaded from Google Fonts in `_layouts/default.html`.

## Architecture

### The only stylesheet that matters
`assets/main.scss` (~930 lines) is the entire design system. Every CSS custom property, layout primitive, and component lives here. Do not look elsewhere for styles.

### `_sass/minima/` is dead weight
`_sass/minima/custom-variables.scss` and `_sass/minima/custom-styles.scss` exist as leftover Minima override scaffolding. They are **not imported anywhere** and have no effect on the rendered site. Do not edit them; they are inert.

### `assets/js/rain.js`
Self-contained vanilla-JS canvas module. Wired with `defer` in `_layouts/default.html`. Renders low-opacity katakana rain at `z-index: -1`. Guards: self-disables under `prefers-reduced-motion: reduce`, pauses via Page Visibility API, throttled to ~18 fps, debounced resize. Site is fully functional with JS off.

### Layout inheritance chain
All layouts extend `default.html`:
- `default.html`: HTML shell, sticky header with active-nav state, footer, Google Fonts `<link>`, `rain.js` `<script defer>`.
- `home.html` extends default: hero + status board on `/`, recent-posts list at bottom.
- `page.html` extends default: `.intro` (heading + lede) + `.prose` body wrapper.
- `post.html` extends default: post title, date, prose body.

### `docs/` -- plans and specs, excluded from build
`docs/superpowers/plans/` and `docs/superpowers/specs/` hold design plans and specs. `docs/` is in `_config.yml` exclude list and will not deploy.

## Design System
Matrix terminal aesthetic: dimmed phosphor green on near-black, all monospace, with a subtle ambient digital-rain canvas behind content.

**Token naming caveat:** token NAMES are retained from the prior editorial system to avoid a mass rename. The VALUES are the terminal palette. `--color-cream*` names now hold phosphor-green tiers. Read the value, not the name.

**Palette (in `assets/main.scss` as CSS custom properties):**
- `--color-iron: #0A0E0A` (near-black page background), `--color-iron-2: #0F140F` (panels/code)
- `--color-cream: #00D936` (primary text: dimmed phosphor)
- `--color-cream-soft / muted / faint`: `#5FE07F` / `#3FB85C` / `#2E9E48` (green tiers, WCAG AA on near-black)
- `--color-amber: #E8A05B` (demoted -- live/active status LED only, never decorative)
- `--color-hairline: rgba(0, 217, 54, 0.22)` (green dividers)

**Typography:** JetBrains Mono everywhere. Hierarchy by weight (700 display, 500 headings, 400 body) and size, not family.

**Accessibility:** global `:focus-visible` ring (green, 2px), `@media (prefers-reduced-motion: reduce)` disables smooth scroll, transitions, cursor blink, and rain.

**Layout primitives** (all in `assets/main.scss`):
- `.hero`: asymmetric 1.6fr / 1fr grid; `.hero__lede` has a CSS blinking cursor
- `.status-board`: mono right-rail with FOCUS / BUILDING / OPEN FOR / BASED IN blocks
- `.section-marker`: bracketed index like `[01]` left, `> label` right, hairline below
- `.course-list` / `.course`: numbered project entries, hairline dividers, amber corner-bracket on hover
- `.stations`: skills grid with 1px gap over hairline background + outer border
- `.entry`: experience / education rows on about.md and resume.md
- `.prose`: markdown content wrapper used by page.html
- `.btn` / `.btn--primary`: mono uppercase CTAs with leading `>` glyph
- `.section-link`, `.post-meta-line`, `.page-404*`: utility classes replacing former inline styles

## File Map
- `index.md`: hero (via layout), Stations + Featured Work + Currently sections.
- `about.md`: bio, "What I Build", Experience entries, Education, Reach.
- `projects.md`: full project list aligned to GitHub pin slate + Sauron Stack.
- `resume.md`: Summary, Experience, Technical Skills (.stations grid), Projects, Education, Certifications.
- `blog.md`: post index (layout: page, Liquid for-loop renders posts).
- `_posts/`: blog posts (Solomon writes these himself -- do not generate unless asked).
- `404.html`: terminal "SIGNAL LOST" 404.
- `assets/resume/SolomonSmithInternship.pdf`: current downloadable resume.

## Key Content Rules
- **No em dashes anywhere** -- in frontmatter, body copy, descriptions, or commit messages. Use a colon, a period, `--`, or rewrite.
- No emojis on the rendered site unless explicitly requested.
- Target language: "full-time AI/ML engineering roles starting January 2027" (not internships).
- GPA: 3.14 (confirmed). Dean's List Spring 2025, Dean's List Fall 2025.
- Solomon writes blog posts himself. Do not generate blog posts unless explicitly asked.

## Active Projects (for portfolio accuracy, aligned to GitHub pin slate)

1. **soc-triage-ai**: RAG-grounded SOC alert triage. Tagged `v1.0-codepath-final`. Streamlit UI, Loom walkthrough.
2. **arda**: Python LLM agents with LangChain. FastAPI + MCP + Redis. Active.
3. **phishguard**: Multi-modal phishing URL detector. v0.2 in development.
4. **claude-agents**: Local multi-agent orchestration backend. Node.js. Production.
5. **DocMind**: RAG document Q&A with prompt injection defense. Active.
6. **adversarial-search-csp**: Minimax, Negamax, Alpha-Beta + CSP solver. 21 pytest cases, CI-tested.

Sauron Stack (PM2-managed Debian server) appears on `projects.md` and `resume.md` but is not a GitHub pin.

## Work Experience (for resume accuracy)
1. Software Engineering Intern, Recursa AI (Dec 2025 to Mar 2026)
2. Full-Stack Developer Intern, RideSplits (Jun 2025 to Sep 2025)
3. Student Administrative Assistant, OSRI, CSUSB (Feb 2026 to present)
4. IT Student Assistant, Cañada College (Jun 2023 to May 2025)
5. Culinary Leadership, 10+ years (Head Chef, Chef de Cuisine, Kitchen Manager)

## Common Tasks
- **Add a project**: edit `projects.md` (add a `.course` entry) and consider updating the top 3 in `index.md` "Featured Work".
- **Update resume**: edit `resume.md`. Mirror key changes to `about.md` Experience section.
- **Change target language**: update `index.md` Currently section, `about.md` "What I am Looking For", `_config.yml` description.
- **Add a `.station` skill**: edit the `.stations` grid in `index.md`, `about.md`, and `resume.md` (all three for consistency).
- **Recolor or retype**: edit the `:root` CSS variables at the top of `assets/main.scss`. Token-driven; one change cascades.
- **Update resume PDF**: drop new PDF into `assets/resume/`, update the href in `resume.md` line 9.

## Build Notes
- Local build: `bundle exec jekyll serve --livereload`. Pages CI: every push to `main` triggers `pages-build-deployment`.
- HTTPS enforced. HSTS set by GitHub Pages once HTTPS enforcement is on.
- Custom domain: `solomonsmith.dev` via `CNAME` file in repo root. If the domain lapses, remove `CNAME` and update `url:` in `_config.yml` back to `https://solomonsmith-dev.github.io`.

## Reconciliation Notes (pending)
- LinkedIn degree field shows "Computational Science" but should be "Computer Science".
- Recursa role title: standardize to "Software Engineering Intern" on LinkedIn.
- RideSplits title: standardize to "Full-Stack Developer Intern" on LinkedIn.
