# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is
Personal portfolio site for Solomon Smith. Jekyll + GitHub Pages, editorial design with light and dark themes.
Live at: https://solomonsmith.dev (CNAME in repo root; falls back to https://solomonsmith-dev.github.io)

## Owner
Solomon Smith. CS senior at CSUSB, targeting AI/ML engineering roles starting January 2027.
Email: solomonsmithdev@gmail.com | GitHub: SolomonSmith-dev | LinkedIn: solomonsmithdev

## Commands

```bash
# Use Homebrew Ruby 3.3 -- system Ruby 2.6 is incompatible with bundler 2.6.8
PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH" bundle install
PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH" bundle exec jekyll serve --livereload
PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH" bundle exec jekyll build
scripts/sync-resume.sh   # copy the canonical resume .md and .pdf from ~/Projects/swe-job-hunt/MATERIALS, regenerate resume.md and _includes/skills.html
```

Pages CI triggers on every push to `main` (30-60s build). Local build requires Homebrew Ruby 3.3 -- system Ruby is 2.6 and incompatible with bundler 2.6.8.

## Stack
- Jekyll 4.4.x on GitHub Pages.
- `assets/main.scss` is the single, standalone stylesheet. It does NOT import Minima. Minima is still declared as the gem `theme` but all layouts and styles are fully overridden.
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-sitemap, jekyll-redirect-from.
- Fonts (Google Fonts, loaded in `_layouts/default.html`): Newsreader (display serif), IBM Plex Sans (body), IBM Plex Mono (labels, stack tags, data only).
- No site JS beyond two inline snippets in `default.html`: a pre-paint theme loader and the theme toggle. `/card` is a separate Vite build with its own assets; it is not styled by `main.scss`.

## Architecture

### The only stylesheet that matters
`assets/main.scss` is the entire design system: tokens on `:root`, dark palette via a `dark-palette` mixin applied under `prefers-color-scheme: dark` (unless `data-theme="light"`) and under `:root[data-theme="dark"]`.

### `_sass/minima/` is dead weight
Not imported anywhere. Do not edit.

### Layout inheritance chain
All layouts extend `default.html`:
- `default.html`: HTML shell, sticky header (Work / About / Resume / Writing + theme toggle + Contact), footer, JSON-LD.
- `home.html`: hero (name + title "AI/Backend Engineer", the one-line thesis as the display heading, CTAs, availability line, headshot). Front matter `hero_lede` and `availability` in `index.md` feed it.
- `page.html`: `.intro` (optional `eyebrow`, `heading` overrides `title` for the H1, `lede`) + `.prose`. `wide: true` lets components span the container.
- `project.html`: extends `page.html` for the `_projects/` collection. Front matter: `heading` (hero line), `lede` (what it does), `status`, `live`, `stack`, `links`, optional `image` fields. Body sections: What it does, Why it is hard, Evidence (a table with `{: .evidence}` whose rows pair each number with the command or file that reproduces it).
- `post.html`: date, title, description, prose, back link.

### `docs/` -- plans and specs, excluded from build
`docs/superpowers/specs/` holds design specs. Current: `2026-10-03-editorial-redesign.md`.

## Design System (editorial, Oct 2026)
Replaced the Matrix terminal theme. No terminal motifs, no rain, no katakana, no `>` glyphs, no `~/` nav.

**Palette** (light / dark): bg `#F7F6F2` / `#111210`, surface `#FFFFFF` / `#181A17`, text `#161614` / `#ECEBE5`, secondary `#55554F` / `#B0AFA7`, border `#E2DFD6` / `#2B2D29`, accent `#1E5B47` / `#8BCFB2`, live dot `#23935F` / `#4CC38A`. One accent only.

**Components**: `.btn` / `.btn--primary` (pill), `.section` + `.section__head`, `.metrics`, `.project` cards with `.project__facts` dl (Problem / Built / Result rows: only rows backed by real facts), `.stack` tags, `.status` (`--live` adds dot), `.timeline` (compact experience), `.entry` (full resume rows), `.skills` grid, `.split`, `.contact` band, `.principles`.

**Accessibility**: global `:focus-visible` ring, skip link, `aria-current` nav, reduced-motion kills the single hero fade-in.

## File Map
- `index.md`: metrics strip (CourtRules 1,653 judges, ARDA 577 tests, PhishGuard AUC 0.9943), Selected work (CourtRules, ARDA, SOC Triage AI, Sentinel), Last week on GitHub, Experience timeline, Skills, Background split, Contact band.
- `about.md`: positioning bio, How I work, Before engineering, What I am looking for, Education. Experience lives on the resume only.
- `projects.md`: seven cards in order: CourtRules, ARDA, SOC Triage AI, Sentinel, PhishGuard, agentic-engineering-os, DocMind. Each card title links to its `/projects/<slug>/` page. claude-agents, adversarial-search-csp (removed 2026-10-03) and the Sauron Stack card (folded into ARDA 2026-11-03) are gone; do not re-add.
- `_projects/<slug>.md`: one page per project at `/projects/<slug>/`, 150 to 300 words, numbers only from that repo's README (CourtRules: the resume). Screenshots live in `assets/img/projects/` and are copied only from images the README already references.
- `resume.md`: generated by `scripts/sync-resume.sh` from the canonical resume. Front matter is hand-kept; the body (Education, Experience, Open source, Projects, Skills) is overwritten on every sync.
- `blog.md`: post index (layout: page, Liquid for-loop renders posts).
- `_posts/`: blog posts (Solomon writes these himself -- do not generate unless asked).
- `404.html`: "Off the menu." 404.
- `log.md` (`/log/`): weekly activity log, newest first, from `_data/activity_log.json` plus Solomon's notes in `_data/log_notes.yml` (keyed by the week's Monday).
- `_includes/activity-week.html`: renders one week; used by the home "Last week on GitHub" section and `/log/`.
- `activity.json` (`/activity.json`): the latest week, published for the profile README workflow.
- `assets/resume/SolomonSmithResume.pdf`: current downloadable resume.

## Key Content Rules
- **No em dashes anywhere** -- in frontmatter, body copy, descriptions, or commit messages. Use a colon, a period, `--`, or rewrite.
- No emojis on the rendered site unless explicitly requested.
- Target language: "Graduating December 2026. Open to full-time AI/ML and backend engineering roles starting January 2027." No internship language.
- **No GPA and no Dean's List anywhere on the site.** Do not add either back without Solomon's explicit confirmation.
- **Source of truth for experience and skills:** `~/Projects/swe-job-hunt/MATERIALS/Solomon-Smith_AI-Backend-Engineer_resume.md` and the PDF beside it. `resume.md` and `_includes/skills.html` are generated from it by `scripts/sync-resume.sh`; never hand-edit them. The phone number in the resume's contact line is deliberately left off the page. **Source of truth for project numbers:** each project's README (CourtRules: the resume). Every number on the site must appear in one of those files. Exception: the weekly GitHub activity block (home) and `/log/` show API counts that are exempt from this rule (Solomon, 2026-10-25).
- **There was no Recursa internship (Dec 2025 to Mar 2026).** Never reintroduce it or its metrics: 200K documents, 99% extraction, 4s to 600ms, 12% hallucination regression, 70% fewer incidents.
- RideSplits is "Full-Stack Developer (contract)". No percentages for that role.
- ARDA uses LangGraph, not LangChain. LangChain, Milvus, Django, React, R, Stripe, and Socket.IO are not skills on this site.
- Skills live once in `_includes/skills.html` (used by `index.md` and `resume.md`) and are regenerated from the resume's SKILLS block by `scripts/sync-resume.sh`.
- Solomon writes blog posts himself. Do not generate blog posts unless explicitly asked.

## Active Projects (for portfolio accuracy, aligned to GitHub pin slate)

1. **soc-triage-ai**: RAG-grounded SOC alert triage. Tagged `v1.0-codepath-final`. Streamlit UI, Loom walkthrough.
2. **arda**: LangGraph orchestrator on native Anthropic tool_use, Redis executor, LlamaIndex RAG, MCP server. 577 of 582 tests pass offline. Deployed 24/7.
3. **phishguard**: LightGBM URL classifier, test AUC 0.9943, 1.54% FPR on Tranco top-5000. PhiUSIIL leakage found and fixed; 35 test functions, 1 xfail. ONNX Runtime is scaffolded only (README), so the site does not list it as the serving layer.
4. **DocMind**: RAG document Q&A with prompt injection defense. 113 tests. Active.

5. **sentinel**: home-network monitor. 119 vitest, 197 pytest, 4 ctest. Dashboard is private (Cloudflare Access).
6. **agentic-engineering-os**: `agent-team` orchestrator. 524 tests, 14 of 15 build steps merged.

Sauron Stack no longer has its own card; it is ARDA's deployment.

## Work Experience (for resume accuracy)
1. Founding Engineer, Recursa AI / CourtRules (Jul 2026 to present). Second engineer, two-person team.
2. Full-Stack Developer (contract), RideSplits (Jun 2025 to Sep 2025).
3. IT Student Assistant, Cañada College (Jun 2023 to May 2025). Dates only, no bullets.
4. Culinary Leadership, 10+ years (Head Chef, Chef de Cuisine, Kitchen Manager).

## Common Tasks
- **Add a project**: write `_projects/<slug>.md` (see `project.html` fields), add `_includes/card-<slug>.html` with the title linking to `/projects/<slug>/`, and include the card in `projects.md` (and `index.md` if it is selected work).
- **Update resume**: edit the canonical resume in `~/Projects/swe-job-hunt/MATERIALS/`, run `scripts/sync-resume.sh`, then check the `index.md` timeline, the `_includes/card-*.html` facts, and the hero metrics against it.
- **Change target language**: update `availability` front matter and the contact band in `index.md`, `about.md` "What I am looking for", `_config.yml` description, bio and og alt, `llms.txt`, `site.webmanifest`.
- **Add a skill**: add it to the canonical resume's SKILLS block and run `scripts/sync-resume.sh`.
- **Recolor or retype**: edit the `:root` CSS variables at the top of `assets/main.scss`. Token-driven; one change cascades.
- **Update resume PDF**: `scripts/sync-resume.sh` copies it to `assets/resume/SolomonSmithResume.pdf` (same filename; linked from header-adjacent CTAs, footer, home, resume).

## Weekly Activity
- `.github/workflows/weekly-activity.yml` runs Monday 15:00 UTC (and on workflow_dispatch with an optional `week_start`). It runs `scripts/activity.py` and commits only `_data/activity.json` and `_data/activity_log.json` straight to `main` (standing approval for those bot commits only), then requests a Pages build.
- Never hand-edit those two JSON files. Rerun the workflow for a week instead; it upserts by `week_start`.
- Token: `ACTIVITY_TOKEN` secret (fine-grained PAT, read-only Metadata, Contents, Pull requests on all repos) adds private repos; without it the run is public only. Private repos are totals only unless listed in `.github/activity-config.json` `private_named`. The script refuses to write if an anonymized repo name appears as a listed repo or link.
- Commits are counted on default branches, authored by SolomonSmith-dev. Forks are skipped.

## Build Notes
- Local build: `bundle exec jekyll serve --livereload`. Pages CI: every push to `main` triggers `pages-build-deployment`.
- HTTPS enforced. HSTS set by GitHub Pages once HTTPS enforcement is on.
- Custom domain: `solomonsmith.dev` via `CNAME` file in repo root. If the domain lapses, remove `CNAME` and update `url:` in `_config.yml` back to `https://solomonsmith-dev.github.io`.

## Reconciliation Notes (pending)
- LinkedIn degree field shows "Computational Science" but should be "Computer Science".
- Recursa role title: standardize to "Software Engineering Intern" on LinkedIn.
- RideSplits title: standardize to "Full-Stack Developer Intern" on LinkedIn.
