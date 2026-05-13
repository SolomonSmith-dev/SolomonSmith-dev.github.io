# CLAUDE.md, SolomonSmith-dev.github.io

## What This Is
Personal portfolio site for Solomon Smith. Jekyll + GitHub Pages with a fully custom editorial design system. The lapsed `solomon-smith-dev.tech` custom domain has been removed from Pages config.
Live at: https://solomonsmith-dev.github.io

## Owner
Solomon Smith. CS senior at CSUSB, targeting AI/ML engineering roles starting January 2027.
Email: solomonsmithdev@gmail.com
GitHub: SolomonSmith-dev
LinkedIn: solomonsmithdev

## Stack
- Jekyll on GitHub Pages.
- `assets/main.scss` is the single, standalone stylesheet. It does NOT import Minima. Minima is still declared as the gem `theme` but its layouts and styles are overridden in this repo.
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-sitemap.
- Fonts loaded from Google Fonts in `_layouts/default.html`: Fraunces (display), Newsreader (body), JetBrains Mono (labels).

## Design System
A custom editorial layout built around Solomon's chef-to-engineer narrative. The discipline of a Michelin pass made visible as web design, without literal kitchen iconography.

**Palette (in `assets/main.scss` as CSS custom properties):**
- `--color-iron: #13110F` (warm iron background, not GitHub black)
- `--color-cream: #EDE6D6` (parchment cream type)
- `--color-amber: #E8A05B` (kitchen-pass amber, single accent used surgically)
- `--color-cream-soft / muted / faint`: alpha layers on the cream
- `--color-hairline: rgba(237, 230, 214, 0.16)` (subtle dividers)

**Typography:**
- Display: Fraunces (variable serif with italic axis)
- Body: Newsreader (transitional serif)
- Mono labels and status info: JetBrains Mono

**Layout primitives (defined in `assets/main.scss`):**
- `.hero` (asymmetric 1.6fr / 1fr grid on the homepage)
- `.status-board` (mono right-rail with FOCUS / BUILDING / OPEN FOR / BASED IN blocks)
- `.section-marker` (Roman numeral on the left, mono label on the right, hairline below)
- `.course-list` and `.course` (numbered project entries with hairline dividers, no boxes, amber underline on title hover)
- `.stations` (skills grid with hairline-bordered cells)
- `.entry` (experience / education entries on about.md and resume.md)
- `.prose` (markdown content wrapper used by page.html)
- `.btn` and `.btn--primary` (mono uppercase CTAs)

## File Map
- `index.md`: home page (hero handled by layout, body has Stations + Featured Work + Currently sections).
- `about.md`: bio, "What I Build" prose, Experience entries, Education, Reach.
- `projects.md`: full course list aligned to the pin slate (soc-triage-ai, arda, phishguard, claude-agents, DocMind, adversarial-search-csp) plus Sauron Stack.
- `resume.md`: Summary, Experience entries, Technical Skills (.stations grid), Selected Projects, Education, Certifications.
- `blog.md`: full post list (uses `layout: page` and renders posts via Liquid for-loop).
- `_posts/`: blog posts (Solomon writes these himself).
- `_layouts/default.html`: shell wrapped around every page (head, sticky header with active-nav state, footer). Replaces Minima's default.
- `_layouts/home.html`: extends default. Hero + status board on `/`, recent-posts list at bottom of `/`. Loads on `/` and `/blog/`.
- `_layouts/page.html`: extends default. Renders `.intro` (heading + lede) and `.prose` body wrapper.
- `_layouts/post.html`: extends default. Post title, date, and prose body.
- `404.html`: editorial "Off the menu." 404.
- `assets/resume/SolomonSmithInternship.pdf`: current downloadable resume.

## Key Content Rules
- Solomon writes blog posts himself. Do not generate blog posts unless explicitly asked.
- **No em dashes anywhere**, including frontmatter, body copy, descriptions, and commit messages. Use a colon, a period, `--`, or rewrite. This was last enforced site-wide on 2026-05-13.
- No emojis on the rendered site unless explicitly requested.
- Target language: "full-time AI/ML engineering roles starting January 2027" (not internships).
- GPA: 3.14 (confirmed). Dean's List Spring 2025, Dean's List Fall 2025.

## Active Projects (for portfolio accuracy, aligned to GitHub pin slate)
The site's "Featured Work" (index.md top 3) and "Projects" list (projects.md) align to the actual GitHub pin slate, in this order:

1. **soc-triage-ai**: RAG-grounded SOC alert triage. Tagged `v1.0-codepath-final`. Streamlit UI, Loom walkthrough.
2. **arda**: Python LLM agents with LangChain. FastAPI + MCP + Redis. Active.
3. **phishguard**: Multi-modal phishing URL detector. v0.2 in development.
4. **claude-agents**: Local multi-agent orchestration backend. Node.js. Production.
5. **DocMind**: RAG document Q&A with prompt injection defense. Active.
6. **adversarial-search-csp**: Minimax, Negamax, Alpha-Beta + CSP solver. 21 pytest cases, CI-tested.

Sauron Stack (PM2-managed Debian server with Earendil/Sauron/Morgoth/Balrog) is on `projects.md` and `resume.md` but is not pinned on GitHub.

TargetRecon CLI is no longer on the site (was a placeholder for an in-progress project that did not graduate to a pin).

## Work Experience (for resume accuracy)
1. Software Engineering Intern, Recursa AI (Dec 2025 to Mar 2026)
2. Full-Stack Developer Intern, RideSplits (Jun 2025 to Sep 2025)
3. Student Administrative Assistant, OSRI, CSUSB (Feb 2026 to present)
4. IT Student Assistant, Cañada College (Jun 2023 to May 2025)
5. Culinary Leadership, 10+ years (Head Chef, Chef de Cuisine, Kitchen Manager)

## Resume PDF
Current file: `assets/resume/SolomonSmithInternship.pdf`
To update: drop new PDF into `assets/resume/`, update the href in `resume.md` line 9.

## Common Tasks
- **Add a project**: edit `projects.md` (add a `.course` entry) and consider adding to the top 3 in `index.md` "Featured Work".
- **Update resume**: edit `resume.md`. Mirror key changes to `about.md` Experience section.
- **Change target language**: update `index.md` Currently section, `about.md` "What I am Looking For" section, `_config.yml` description.
- **Add a `.station` skill**: edit the `.stations` grid in `index.md`, `about.md`, and `resume.md` (all three for consistency).
- **Recolor or retype**: edit the `:root` CSS variables at the top of `assets/main.scss`. The design system is token-driven; changing one variable cascades.

## Build Notes
- Local build: `bundle exec jekyll build`. Solomon's machine had a bundler-version mismatch with system Ruby on 2026-05-13; install a matching bundler or use Pages CI to verify.
- Pages CI: every push to `main` triggers `pages-build-deployment`. Typical build time 30 to 60 seconds.
- HTTPS is enforced. HSTS header is set by GitHub Pages once HTTPS enforcement is on.

## Reconciliation Notes (pending)
- LinkedIn degree field shows "Computational Science" but should be "Computer Science". Fix on LinkedIn.
- Recursa role title: standardize to "Software Engineering Intern" on LinkedIn.
- RideSplits title: standardize to "Full-Stack Developer Intern" on LinkedIn.
- `solomon-smith-dev.tech` domain lapsed. Pages config no longer references it. If Solomon repurchases later, drop a `CNAME` file at repo root and set `https_enforced` after the cert provisions.
