# CLAUDE.md — SolomonSmith-dev.github.io

## What This Is
Personal portfolio site for Solomon Smith. Jekyll + GitHub Pages + custom dark Sass theme on Minima.
Live at: https://solomon-smith-dev.tech

## Owner
Solomon Smith — CS senior at CSUSB, targeting AI/ML engineering roles starting January 2027.
Email: solomonsmithdev@gmail.com
GitHub: SolomonSmith-dev
LinkedIn: solomonsmithdev

## Stack
- Jekyll (Minima base, dark skin override)
- Custom Sass: `_sass/minima/custom-styles.scss`, `_sass/minima/custom-variables.scss`
- `assets/main.scss` — dark theme variables injected before `@import "minima"`
- GitHub Pages deployment; custom domain via CNAME
- Plugins: jekyll-feed, jekyll-seo-tag, jekyll-sitemap

## File Map
- `index.md` — homepage (hero, skills grid, 3 featured project cards, Currently section)
- `about.md` — bio, skills, experience summary, education, looking-for, connect
- `projects.md` — Featured / Live / In the Pipeline sections
- `resume.md` — full resume: experience, skills, projects, education, certifications
- `blog.md` — blog index (uses `layout: home` to auto-list posts)
- `_posts/` — blog posts (Solomon writes these himself)
- `_layouts/home.html` — custom layout: hero on `/`, post list on all home-layout pages
- `assets/resume/SolomonSmithInternship.pdf` — current downloadable resume

## Key Content Rules
- Solomon writes blog posts himself. Do not generate blog posts unless explicitly asked.
- No em dashes in page copy (use -- or rewrite the sentence).
- Target language: "full-time AI/ML engineering roles starting January 2027" (not internships).
- GPA: 3.14 (confirmed). Dean's List Spring 2025, Dean's List Fall 2025.

## Active Projects (for portfolio accuracy)
- SOC Triage AI — v1 shipped (Claude API, RAG, Streamlit). GitHub: SolomonSmith-dev/soc-triage-ai. v2 rewrite in progress (FastAPI, PostgreSQL, Next.js).
- Multi-Agent AI System (Sauron Stack) — PM2-managed agents (Earendil, Sauron, Morgoth, Balrog), Redis, Tailscale, Debian server.
- TargetRecon CLI — OSINT tool, in progress.

## Work Experience (for resume accuracy)
1. Software Engineering Intern — Recursa AI (Dec 2025 – Mar 2026)
2. Full-Stack Developer Intern — RideSplits (Jun 2025 – Sep 2025)
3. Student Administrative Assistant — OSRI, CSUSB (Feb 2026 – Present)
4. IT Student Assistant — Cañada College (Jun 2023 – May 2025)

## Resume PDF
Current file: `assets/resume/SolomonSmithInternship.pdf`
To update: drop new PDF into `assets/resume/`, update the href in `resume.md` line 9.

## Common Tasks
- Add a project: edit `projects.md` (Featured/Live/Pipeline sections) and `index.md` featured grid.
- Update resume: edit `resume.md`. Mirror key changes to `about.md` experience section.
- Change target language: update `index.md` Currently section, `about.md` looking-for section, `_config.yml` bio field.

## Reconciliation Notes (pending)
- LinkedIn degree field shows "Computational Science" -- should be "Computer Science". Fix on LinkedIn.
- Recursa role title: standardize to "Software Engineering Intern" on LinkedIn.
- RideSplits title: standardize to "Full-Stack Developer Intern" on LinkedIn.
