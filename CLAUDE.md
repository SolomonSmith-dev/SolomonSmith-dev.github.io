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
- `home.html`: hero (name + title, value statement, CTAs, availability line, headshot). Front matter `hero_lede` and `availability` in `index.md` feed it.
- `page.html`: `.intro` (optional `eyebrow`, `heading` overrides `title` for the H1, `lede`) + `.prose`. `wide: true` lets components span the container.
- `post.html`: date, title, description, prose, back link.

### `docs/` -- plans and specs, excluded from build
`docs/superpowers/specs/` holds design specs. Current: `2026-10-03-editorial-redesign.md`.

## Design System (editorial, Oct 2026)
Replaced the Matrix terminal theme. No terminal motifs, no rain, no katakana, no `>` glyphs, no `~/` nav.

**Palette** (light / dark): bg `#F7F6F2` / `#111210`, surface `#FFFFFF` / `#181A17`, text `#161614` / `#ECEBE5`, secondary `#55554F` / `#B0AFA7`, border `#E2DFD6` / `#2B2D29`, accent `#1E5B47` / `#8BCFB2`, live dot `#23935F` / `#4CC38A`. One accent only.

**Components**: `.btn` / `.btn--primary` (pill), `.section` + `.section__head`, `.metrics`, `.project` cards with `.project__facts` dl (Problem / Built / Result rows: only rows backed by real facts), `.stack` tags, `.status` (`--live` adds dot), `.timeline` (compact experience), `.entry` (full resume rows), `.skills` grid, `.split`, `.contact` band, `.principles`.

**Accessibility**: global `:focus-visible` ring, skip link, `aria-current` nav, reduced-motion kills the single hero fade-in.

## File Map
- `index.md`: metrics strip (CourtRules verifier 7 tests, ARDA 425 tests, PhishGuard AUC 0.9943), Selected work (4 included cards), Experience timeline, Skills, Background split, Contact band.
- `about.md`: positioning bio, How I work, Before engineering, What I am looking for, Education. Experience lives on the resume only.
- `projects.md`: grouped cards (Applied AI systems, Agent infrastructure, Algorithms).
- `resume.md`: Summary, Experience, Technical Skills (.skills grid), Projects, Education, Certifications.
- `blog.md`: post index (layout: page, Liquid for-loop renders posts).
- `_posts/`: blog posts (Solomon writes these himself -- do not generate unless asked).
- `404.html`: "Off the menu." 404.
- `assets/resume/SolomonSmithResume.pdf`: current downloadable resume.

## Key Content Rules
- **No em dashes anywhere** -- in frontmatter, body copy, descriptions, or commit messages. Use a colon, a period, `--`, or rewrite.
- No emojis on the rendered site unless explicitly requested.
- Target language: "Graduating December 2026. Open to full-time AI/ML and backend engineering roles starting January 2027." No internship language.
- **No GPA and no Dean's List anywhere on the site.** Do not add either back without Solomon's explicit confirmation.
- **Source of truth for experience, project facts, metrics, and skills:** the newest master resume in `~/Projects/swe-job-hunt/OUTPUTS/resumes/` (currently `2026-09-28_master_newgrad_resume.md`). `resume.md` mirrors it exactly. Every number on the site must appear in that file.
- **There was no Recursa internship (Dec 2025 to Mar 2026).** Never reintroduce it or its metrics: 200K documents, 99% extraction, 4s to 600ms, 12% hallucination regression, 70% fewer incidents.
- RideSplits is "Full-Stack Developer (contract)". No percentages for that role.
- ARDA uses LangGraph, not LangChain. LangChain, Milvus, Django, React, R, Stripe, and Socket.IO are not skills on this site.
- Skills live once in `_includes/skills.html` (used by `index.md` and `resume.md`) and must match the master resume's Skills section.
- Solomon writes blog posts himself. Do not generate blog posts unless explicitly asked.

## Active Projects (for portfolio accuracy, aligned to GitHub pin slate)

1. **soc-triage-ai**: RAG-grounded SOC alert triage. Tagged `v1.0-codepath-final`. Streamlit UI, Loom walkthrough.
2. **arda**: LangGraph orchestrator on native Anthropic tool_use, Redis executor, LlamaIndex RAG, MCP server. 425 offline tests. Deployed 24/7.
3. **phishguard**: LightGBM URL classifier, test AUC 0.9943, 1.54% FPR on Tranco top-5000. PhiUSIIL leakage found and fixed; 34 tests.
4. **claude-agents**: Local multi-agent orchestration backend. Node.js. Production.
5. **DocMind**: RAG document Q&A with prompt injection defense. Active.
6. **adversarial-search-csp**: Minimax, Negamax, Alpha-Beta + CSP solver. 21 pytest cases, CI-tested.

Sauron Stack (PM2-managed Debian server) appears on `projects.md` and `resume.md` but is not a GitHub pin.

## Work Experience (for resume accuracy)
1. Founding Engineer, Recursa AI / CourtRules (Jul 2026 to present). Second engineer, two-person team.
2. Full-Stack Developer (contract), RideSplits (Jun 2025 to Sep 2025).
3. IT Student Assistant, Cañada College (Jun 2023 to May 2025). Dates only, no bullets.
4. Culinary Leadership, 10+ years (Head Chef, Chef de Cuisine, Kitchen Manager).

## Common Tasks
- **Add a project**: project cards shown on both pages live in `_includes/card-*.html`. Add one there (or inline in `projects.md` if projects-only) and include it where needed.
- **Update resume**: mirror the new master resume into `resume.md`, then update the `index.md` timeline, the `_includes/card-*.html` facts, and the hero metrics.
- **Change target language**: update `availability` front matter and the contact band in `index.md`, `about.md` "What I am looking for", `_config.yml` description, bio and og alt, `llms.txt`, `site.webmanifest`.
- **Add a skill**: only if it is on the master resume. Edit `_includes/skills.html`.
- **Recolor or retype**: edit the `:root` CSS variables at the top of `assets/main.scss`. Token-driven; one change cascades.
- **Update resume PDF**: replace `assets/resume/SolomonSmithResume.pdf` (same filename; linked from header-adjacent CTAs, footer, home, resume).

## Build Notes
- Local build: `bundle exec jekyll serve --livereload`. Pages CI: every push to `main` triggers `pages-build-deployment`.
- HTTPS enforced. HSTS set by GitHub Pages once HTTPS enforcement is on.
- Custom domain: `solomonsmith.dev` via `CNAME` file in repo root. If the domain lapses, remove `CNAME` and update `url:` in `_config.yml` back to `https://solomonsmith-dev.github.io`.

## Reconciliation Notes (pending)
- LinkedIn degree field shows "Computational Science" but should be "Computer Science".
- Recursa role title: standardize to "Software Engineering Intern" on LinkedIn.
- RideSplits title: standardize to "Full-Stack Developer Intern" on LinkedIn.
