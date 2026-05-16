---
title: Matrix Terminal Redesign Implementation Plan
date: 2026-05-15
sitemap: false
---

# Matrix Terminal Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the editorial (warm iron / serif) identity of solomonsmith-dev.github.io with a dimmed-phosphor Matrix terminal aesthetic (monospace, near-black, subtle ambient digital rain), while fixing every accessibility and responsiveness defect from the 2026-05-15 frontend audit in the same change set.

**Architecture:** The site is a CSS design-token system. Identity lives in ~12 `:root` custom properties in `assets/main.scss` (714 lines); layout primitives keep their structure and are reskinned via token swaps plus a small number of targeted rule edits. One new vanilla-JS module renders the rain canvas. Verification is build + real-browser visual checks (no test framework exists in this repo).

**Tech Stack:** Jekyll on GitHub Pages, SCSS (single standalone stylesheet, no Minima import), Liquid templates, vanilla JS (canvas), JetBrains Mono via Google Fonts.

**Spec:** `docs/superpowers/specs/2026-05-15-matrix-terminal-redesign-design.md`

**No em dashes** in any file or commit message (CLAUDE.md hard rule). Do not stage `.claude/`, `.playwright-mcp/`, or local tooling state. No `Co-Authored-By` trailer on commits.

---

## File Structure

| File | Action | Responsibility |
|---|---|---|
| `_config.yml` | Modify | Add `docs/` to `exclude:` so spec/plan files never deploy. |
| `assets/main.scss` | Modify | Token swap (palette, fonts), a11y rules, terminal-language reskin, grid border fix, new utility classes replacing inline styles. |
| `_layouts/default.html` | Modify | Swap Google Fonts request to JetBrains Mono only; path-style nav labels; wire `rain.js`. |
| `_layouts/home.html` | Modify | Section-marker text to terminal style; replace inline-styled "All writing" link with a class. |
| `_layouts/post.html` | Modify | Replace inline-styled date and "All writing" link with classes. |
| `index.md` | Modify | Section-marker label text to terminal style. |
| `projects.md` | Modify | Replace one inline `style=` with a class. |
| `404.html` | Modify | Replace inline-styled block with a `.page-404` class. |
| `assets/js/rain.js` | Create | Self-contained, guarded digital-rain canvas renderer. |

---

## Task 0: Local build environment and baseline

**Files:** none modified (environment + baseline capture only)

- [ ] **Step 1: Confirm clean tree and branch**

Run:
```bash
git status --porcelain && git rev-parse --abbrev-ref HEAD
```
Expected: no output from `--porcelain` (clean), branch `main`. If not clean, stop and report.

- [ ] **Step 2: Get a working local build**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -20
```
Expected: `done in N seconds`. The `_site/` directory now exists.

If it fails with a bundler version error (known issue, CLAUDE.md note 2026-05-13), fix the bundler to match the lockfile, then retry:
```bash
BUNDLED_VERSION=$(tail -1 Gemfile.lock | tr -d ' ')
gem install bundler -v "$BUNDLED_VERSION"
bundle install
bundle exec jekyll build 2>&1 | tail -20
```
A working local render is required because the user explicitly asked for a visual audit. Do not skip to Pages-CI-only.

- [ ] **Step 3: Serve the built site**

Run in background:
```bash
ruby -run -e httpd _site -p 4555 >/tmp/jekyll-serve.log 2>&1 &
sleep 1 && curl -s -o /dev/null -w "%{http_code}" http://localhost:4555/
```
Expected: `200`.

- [ ] **Step 4: Capture baseline screenshots (before state)**

Use the Playwright MCP browser tools. Navigate to each URL at viewport 1280x900 and take a screenshot, then repeat at 375x812:
- `http://localhost:4555/`
- `http://localhost:4555/about/`
- `http://localhost:4555/projects/`
- `http://localhost:4555/resume/`
- `http://localhost:4555/blog/`
- `http://localhost:4555/2026/04/30/building-soc-triage-copilot/`
- `http://localhost:4555/404.html`

Save nothing to the repo. These baselines are for visual comparison only; keep them in the Playwright session output. This confirms the harness works before any change.

- [ ] **Step 5: No commit** (environment task, nothing changed)

---

## Task 1: Exclude docs/ from the Jekyll build

**Files:**
- Modify: `_config.yml:48-61` (the `exclude:` block)

- [ ] **Step 1: Add docs/ to exclude**

In `_config.yml`, change the `exclude:` list to add `docs/` as the first entry:
```yaml
# Exclude from processing
exclude:
  - docs/
  - .sass-cache/
  - .jekyll-cache/
  - gemfiles/
  - Gemfile
  - Gemfile.lock
  - node_modules/
  - vendor/bundle/
  - vendor/cache/
  - vendor/gems/
  - vendor/ruby/
  - README.md
  - vendor/
```

- [ ] **Step 2: Rebuild and verify docs/ is not output**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3 && test ! -d _site/docs && echo "EXCLUDED_OK"
```
Expected: build succeeds and prints `EXCLUDED_OK` (the `_site/docs` directory does not exist).

- [ ] **Step 3: Commit**

```bash
git add _config.yml
git commit -m "Exclude docs/ from Jekyll build so spec and plan files never deploy"
```

---

## Task 2: Palette and typography token swap

**Files:**
- Modify: `assets/main.scss:9-48` (the `:root` token block and `body`)

This is the cascade point. Variable *names* stay (renaming 714 lines is out of scope); only values change. A comment documents the name/value mismatch.

- [ ] **Step 1: Replace the `:root` token block**

Replace lines 9-29 (`:root { ... }`) with:
```scss
:root {
  /* NOTE: token NAMES are retained from the prior editorial system to
     avoid a 714-line rename. VALUES are the Matrix terminal palette.
     "cream" names now hold phosphor-green tiers. Do not infer color
     from the variable name; read the value. */

  --color-iron: #0A0E0A;        /* near-black page background */
  --color-iron-2: #0F140F;      /* code blocks, panels */

  --color-cream: #00D936;       /* primary text: dimmed phosphor */
  --color-cream-soft: #5FE07F;  /* secondary text */
  --color-cream-muted: #3FB85C; /* small mono labels, meta */
  --color-cream-faint: #2E9E48; /* course numbers, faintest tier */

  --color-amber: #E8A05B;       /* DEMOTED: live/active status LED only */
  --color-amber-soft: rgba(232, 160, 91, 0.18);
  --color-hairline: rgba(0, 217, 54, 0.22);

  --font-display: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --font-body: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;

  --container: 1180px;
  --gutter: clamp(1.25rem, 4vw, 3rem);

  --transition-fast: 0.18s cubic-bezier(0.22, 0.61, 0.36, 1);
  --transition-slow: 0.4s cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

- [ ] **Step 2: Make body a flex column (footer fix, audit finding #8)**

Replace the `body { ... }` rule (lines 37-48) with:
```scss
body {
  margin: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.7;
  color: var(--color-cream);
  background: var(--color-iron);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-feature-settings: "kern", "liga", "calt";
  text-rendering: optimizeLegibility;
}

main.shell { flex: 1 0 auto; }
```
(Mono reads slightly larger; 16px base with 1.7 line-height keeps long copy comfortable. The existing `main.shell` block at lines 66-70 keeps its padding; this adds `flex` growth so the footer sits at the viewport bottom on short pages. Delete the now-redundant `min-height: 60vh;` from the existing `main.shell` rule.)

- [ ] **Step 3: Remove min-height from existing main.shell**

In `assets/main.scss`, in the `main.shell` rule (around line 66-70), delete the line `min-height: 60vh;`. The flex rule from Step 2 replaces its purpose.

- [ ] **Step 4: Rebuild and visually verify palette**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
```
Then with Playwright, reload `http://localhost:4555/` and screenshot at 1280x900. Expected: near-black background, green text, amber still only on the `v1.0 / active / v0.2` status tags in the status board and project headers. Body text is monospace.

- [ ] **Step 5: Verify small-text contrast (audit finding #2)**

For each of these foreground/background pairs, compute the WCAG contrast ratio (use an inline node one-liner or an online checker; threshold is 4.5:1 for normal text):
- `#3FB85C` on `#0A0E0A` (muted: section labels, meta)
- `#2E9E48` on `#0A0E0A` (faint: course numbers)

Quick check command:
```bash
node -e '
const L=h=>{const c=[parseInt(h.slice(1,3),16),parseInt(h.slice(3,5),16),parseInt(h.slice(5,7),16)].map(v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)});return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]};
const R=(a,b)=>{const l1=L(a)+0.05,l2=L(b)+0.05;return (Math.max(l1,l2)/Math.min(l1,l2)).toFixed(2)};
console.log("muted",R("#3FB85C","#0A0E0A"));
console.log("faint",R("#2E9E48","#0A0E0A"));
'
```
Expected: both values >= 4.5. If `faint` is below 4.5, change `--color-cream-faint` to `#36B053` and re-run until both pass. Record the final values.

- [ ] **Step 6: Commit**

```bash
git add assets/main.scss
git commit -m "Reskin palette and typography to dimmed-phosphor Matrix terminal; fix footer min-height"
```

---

## Task 3: Swap web fonts to JetBrains Mono only

**Files:**
- Modify: `_layouts/default.html:11-13` (the Google Fonts links)

This resolves the audit finding on heavy multi-font first paint: Fraunces and Newsreader are no longer used.

- [ ] **Step 1: Replace the font preconnect and stylesheet links**

Replace lines 11-13 of `_layouts/default.html` with:
```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

- [ ] **Step 2: Rebuild and verify single font request**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
grep -c "Fraunces\|Newsreader" _site/index.html || echo "NO_SERIF_FONTS"
```
Expected: build succeeds; `grep -c` finds 0 matches so the `||` branch prints `NO_SERIF_FONTS` (no serif font references remain in the rendered head).

- [ ] **Step 3: Visual check**

With Playwright, reload `http://localhost:4555/` and confirm all text renders in JetBrains Mono (no serif fallback flash). Screenshot at 1280x900.

- [ ] **Step 4: Commit**

```bash
git add _layouts/default.html
git commit -m "Load only JetBrains Mono; drop unused Fraunces and Newsreader requests"
```

---

## Task 4: Global accessibility CSS (focus-visible, reduced-motion)

**Files:**
- Modify: `assets/main.scss` (append a new section after the Reset block, around line 56, before Layout primitives)

Fixes audit findings #1 (no focus-visible) and #3 (no reduced-motion).

- [ ] **Step 1: Add focus-visible and reduced-motion rules**

In `assets/main.scss`, immediately after the `a { ... }` rule (ends around line 56) and before the `/* ----- Layout primitives ----- */` comment, insert:
```scss
/* ----- Accessibility ---------------------------------------------------- */

:focus-visible {
  outline: 2px solid var(--color-cream);
  outline-offset: 2px;
}

a:focus-visible,
button:focus-visible,
.btn:focus-visible {
  outline: 2px solid var(--color-cream);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }
}
```

- [ ] **Step 2: Rebuild**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
```
Expected: build succeeds.

- [ ] **Step 3: Verify focus ring with keyboard**

With Playwright on `http://localhost:4555/`: press `Tab` several times to move focus through the nav links. After each Tab, take a screenshot. Expected: a visible 2px green outline appears around the focused link. Confirm the ring is visible on at least the first nav link and the first project link.

- [ ] **Step 4: Verify reduced-motion**

With Playwright, emulate reduced motion (the browser tool supports a reduced-motion media emulation; if not available via MCP, set it via `browser_run_code_unsafe` is not permitted, so instead verify via DevTools rendering emulation in the Playwright snapshot). Reload `/` and confirm no smooth scroll and no transition delay on hover. Screenshot.

If reduced-motion emulation is not controllable through the available MCP tools, document this as "verified by code inspection: the `@media (prefers-reduced-motion: reduce)` block is present and correctly scoped" and proceed. The rain module (Task 8) has its own JS-level guard verified separately.

- [ ] **Step 5: Commit**

```bash
git add assets/main.scss
git commit -m "Add global focus-visible ring and prefers-reduced-motion handling"
```

---

## Task 5: Stations grid border fix

**Files:**
- Modify: `assets/main.scss:366-405` (`.stations`, `.station`, `.station:last-child`)

Fixes audit finding #4 (dangling borders when the skills grid wraps to a second row).

- [ ] **Step 1: Replace the stations and station rules**

Replace the `.stations { ... }`, `.station { ... }`, and `.station:last-child { ... }` rules (lines 366-380) with a gap-plus-outer-border approach that has no per-cell side borders:
```scss
.stations {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1px;
  margin: 0;
  background: var(--color-hairline);
  border: 1px solid var(--color-hairline);
}

.station {
  padding: 1.5rem 1.25rem;
  background: var(--color-iron);
}
```
(The 1px grid `gap` over a hairline-colored grid background draws clean separators between every cell regardless of row count. No `:last-child` special-casing, so wrapped rows never leave a dangling edge. Leave `.station__name` and `.station__list` rules unchanged.)

- [ ] **Step 2: Rebuild**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
```
Expected: build succeeds.

- [ ] **Step 3: Verify no dangling borders at wrap width**

With Playwright, open `http://localhost:4555/` and set viewport width to 700px (forces the 4-column stations grid to wrap to 2 rows). Screenshot the Stations section. Expected: a clean grid with uniform hairline separators on all four cells, no border stub extending past the last cell in a row.

- [ ] **Step 4: Commit**

```bash
git add assets/main.scss
git commit -m "Fix stations grid dangling borders on wrap using gap-plus-outer-border"
```

---

## Task 6: Terminal-language reskin (CSS)

**Files:**
- Modify: `assets/main.scss` (`.section-marker__roman`, `.hero__lede`, `.course__title::after` and `.course:hover` rule, `.site-nav` rules, `.btn` rules)

Pure CSS changes. HTML text edits that pair with these come in Task 7.

- [ ] **Step 1: Section marker index style**

Replace the `.section-marker__roman { ... }` rule (lines 133-139) with:
```scss
.section-marker__roman {
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: clamp(1.25rem, 2.4vw, 1.75rem);
  letter-spacing: 0.04em;
  color: var(--color-cream-muted);
}
```

- [ ] **Step 2: Hero blinking cursor**

After the existing `.hero__lede { ... }` rule (ends around line 188), add:
```scss
.hero__lede::after {
  content: "_";
  display: inline-block;
  margin-left: 0.15em;
  color: var(--color-cream);
  animation: cursor-blink 1.1s steps(1) infinite;
}

@keyframes cursor-blink {
  0%, 50% { opacity: 1; }
  50.01%, 100% { opacity: 0; }
}
```
(The reduced-motion block from Task 4 already neutralizes this animation, so no extra guard is needed here.)

- [ ] **Step 3: Project title terminal frame on hover/focus**

Replace the `.course__title::after { ... }` rule and the `.course:hover .course__title::after { ... }` rule (lines 301-314) with a corner-bracket frame that also responds to keyboard focus:
```scss
.course__title::before,
.course__title::after {
  content: "";
  position: absolute;
  width: 10px;
  height: 10px;
  opacity: 0;
  transition: opacity var(--transition-fast);
  border-color: var(--color-amber);
  border-style: solid;
}

.course__title::before {
  top: -6px;
  left: -8px;
  border-width: 1px 0 0 1px;
}

.course__title::after {
  bottom: -6px;
  right: -8px;
  border-width: 0 1px 1px 0;
}

.course:hover .course__title::before,
.course:hover .course__title::after,
.course__title a:focus-visible ~ .course__title::before,
.course:focus-within .course__title::before,
.course:focus-within .course__title::after {
  opacity: 1;
}
```

- [ ] **Step 4: Nav path style and non-color active cue**

Replace the `.site-nav a` / `:hover` / `.active` rules (lines 106-115) with:
```scss
.site-nav a {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.06em;
  color: var(--color-cream-soft);
}

.site-nav a:hover { color: var(--color-cream); }

.site-nav a.active {
  color: var(--color-cream);
  text-decoration: underline;
  text-underline-offset: 5px;
  text-decoration-thickness: 1px;
}

.site-nav a.active::before {
  content: "> ";
  color: var(--color-amber);
}
```
(Active state now uses a leading `>` glyph and an underline, not color alone. Fixes audit finding #6.)

- [ ] **Step 5: Button terminal style**

Replace the `.btn { ... }`, `.btn:hover`, `.btn--primary`, `.btn--primary:hover` rules (lines 625-652) with:
```scss
.btn {
  display: inline-block;
  padding: 0.7rem 1.4rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  border: 1px solid var(--color-cream-soft);
  color: var(--color-cream);
  background: transparent;
  transition: background var(--transition-fast), color var(--transition-fast), border-color var(--transition-fast);
  margin-right: 0.5rem;
}

.btn::before { content: "> "; color: var(--color-cream-muted); }

.btn:hover {
  background: var(--color-cream);
  border-color: var(--color-cream);
  color: var(--color-iron);
}

.btn--primary {
  background: var(--color-cream);
  border-color: var(--color-cream);
  color: var(--color-iron);
}

.btn--primary:hover {
  background: transparent;
  color: var(--color-cream);
}
```

- [ ] **Step 6: Rebuild and visual check**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
```
With Playwright reload `http://localhost:4555/`, screenshot at 1280x900. Hover a project title: confirm amber corner brackets fade in. Tab to a project link: confirm brackets appear on focus. Check `/404.html`: buttons show a leading `>` and invert on hover.

- [ ] **Step 7: Commit**

```bash
git add assets/main.scss
git commit -m "Reskin section markers, hero cursor, project frames, nav, and buttons to terminal language"
```

---

## Task 7: HTML terminal-language text and inline-style detox

**Files:**
- Modify: `index.md` (section-marker labels)
- Modify: `_layouts/home.html` (section-marker label, replace inline-styled link)
- Modify: `_layouts/default.html` (nav labels to path style)
- Modify: `_layouts/post.html` (replace two inline `style=` blocks)
- Modify: `projects.md:144` (replace inline `style=`)
- Modify: `404.html` (replace inline-styled block)
- Modify: `assets/main.scss` (add `.section-link` and `.page-404` utility classes)

Fixes audit finding #7 (inline styles duplicating tokens) and applies terminal-language text.

- [ ] **Step 1: Add utility classes to main.scss**

At the end of `assets/main.scss` (after the `.muted` utility, line 715), append:
```scss
/* ----- Section link + 404 (replaces inline styles) ---------------------- */

.section-link {
  margin-top: 2rem;
  font-family: var(--font-mono);
  font-size: 0.74rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.section-link a { color: var(--color-cream-soft); }
.section-link a:hover { color: var(--color-cream); }

.post-meta-line {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--color-cream-muted);
}

.page-404 {
  text-align: center;
  padding: 6rem 0 4rem;
}

.page-404__code {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--color-cream-muted);
  margin: 0 0 1.5rem;
}

.page-404__title {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(2.5rem, 7vw, 4.5rem);
  line-height: 1;
  letter-spacing: -0.02em;
  color: var(--color-cream);
  margin: 0 0 1.5rem;
}

.page-404__body {
  font-size: 1rem;
  color: var(--color-cream-soft);
  max-width: 46ch;
  margin: 0 auto 2.5rem;
}
```

- [ ] **Step 2: Terminal section labels in index.md**

In `index.md`, change the three `.section-marker` blocks so the roman span holds a bracketed index and the label is lowercase prefixed. Replace the Stations marker (lines 9-12):
```html
<section class="section-marker">
  <span class="section-marker__roman">[01]</span>
  <span class="section-marker__label">&gt; stations</span>
</section>
```
Replace the Featured Work marker (lines 58-61):
```html
<section class="section-marker">
  <span class="section-marker__roman">[02]</span>
  <span class="section-marker__label">&gt; featured_work</span>
</section>
```
Replace the Currently marker (lines 129-132):
```html
<section class="section-marker">
  <span class="section-marker__roman">[03]</span>
  <span class="section-marker__label">&gt; currently</span>
</section>
```
Then replace the inline-styled "All projects" paragraph (lines 125-127) with:
```html
<p class="section-link">
  <a href="{{ '/projects/' | relative_url }}">cd ../projects &rarr;</a>
</p>
```

- [ ] **Step 3: Terminal section label and link in home.html**

In `_layouts/home.html`, replace the Writing section-marker (lines 48-51):
```html
<section class="section-marker">
  <span class="section-marker__roman">[04]</span>
  <span class="section-marker__label">&gt; writing</span>
</section>
```
Replace the inline-styled "All writing" paragraph (lines 65-67):
```html
<p class="section-link">
  <a href="{{ '/blog/' | relative_url }}">cd ../writing &rarr;</a>
</p>
```

- [ ] **Step 4: Path-style nav labels in default.html**

In `_layouts/default.html`, replace the four nav anchors (lines 23-26) with:
```html
      <a href="{{ '/about/' | relative_url }}" {% if page.url contains '/about' %}class="active"{% endif %}>~/about</a>
      <a href="{{ '/projects/' | relative_url }}" {% if page.url contains '/projects' %}class="active"{% endif %}>~/projects</a>
      <a href="{{ '/blog/' | relative_url }}" {% if page.url contains '/blog' or page.url contains '/20' %}class="active"{% endif %}>~/writing</a>
      <a href="{{ '/resume/' | relative_url }}" {% if page.url contains '/resume' %}class="active"{% endif %}>~/resume</a>
```

- [ ] **Step 5: Detox post.html inline styles**

In `_layouts/post.html`, replace line 8 (the inline-styled date paragraph) with:
```html
    <p class="page-lede post-meta-line">{{ page.date | date: "%B %-d, %Y" }}</p>
```
Replace lines 17-19 (the inline-styled back link) with:
```html
  <p class="section-link" style="margin-top: 4rem;">
    <a href="{{ '/blog/' | relative_url }}">cd ../writing &larr;</a>
  </p>
```
Note: a single `margin-top` override is acceptable here because it is a one-off layout nudge, not a token duplication. The font/color/letter-spacing now come from the class.

- [ ] **Step 6: Detox projects.md inline style**

In `projects.md`, replace line 144 (`<p style="margin-top: 3rem;" class="prose">`) with:
```html
<p class="prose" style="margin-top: 3rem;">
```
(Keep the single spacing override; the rule is "no token duplication in inline styles", and `margin-top` here is a layout nudge with no token equivalent class. Order corrected so `class` is not overridden.)

- [ ] **Step 7: Detox 404.html**

Replace the entire `<section>` block in `404.html` (the inline-styled block) with:
```html
<section class="page-404">
  <p class="page-404__code">404</p>
  <h1 class="page-404__title">Off the menu.</h1>
  <p class="page-404__body">
    The page you were looking for is not here. It may have moved, or it may have never existed.
  </p>
  <p>
    <a class="btn btn--primary" href="{{ '/' | relative_url }}">Back to home</a>
    <a class="btn" href="{{ '/projects/' | relative_url }}">See projects</a>
  </p>
</section>
```

- [ ] **Step 8: Rebuild and verify no token-duplicating inline styles remain**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
grep -rn 'style="[^"]*var(--' _layouts/ index.md projects.md 404.html || echo "NO_TOKEN_INLINE_STYLES"
```
Expected: build succeeds; the grep finds no inline styles referencing CSS variables, so it prints `NO_TOKEN_INLINE_STYLES`. (Plain `margin-top` overrides without `var(--...)` are allowed and intentionally not matched.)

- [ ] **Step 9: Visual check across pages**

With Playwright at 1280x900, screenshot `/`, `/blog/`, a post page, and `/404.html`. Confirm: bracketed section indices `[01]..[04]`, `> stations` style labels, `~/about` nav with active page underlined and prefixed `>`, 404 renders identically in layout to before but in terminal palette.

- [ ] **Step 10: Commit**

```bash
git add assets/main.scss index.md _layouts/home.html _layouts/default.html _layouts/post.html projects.md 404.html
git commit -m "Apply terminal-language text and remove token-duplicating inline styles"
```

---

## Task 8: Digital rain module

**Files:**
- Create: `assets/js/rain.js`
- Modify: `_layouts/default.html` (add script tag before `</body>`)

- [ ] **Step 1: Create the rain module**

Create `assets/js/rain.js` with exactly:
```js
(function () {
  "use strict";

  var reduce = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) { return; }

  var canvas = document.createElement("canvas");
  canvas.id = "rain";
  canvas.setAttribute("aria-hidden", "true");
  var s = canvas.style;
  s.position = "fixed";
  s.top = "0";
  s.left = "0";
  s.width = "100%";
  s.height = "100%";
  s.zIndex = "-1";
  s.pointerEvents = "none";
  document.body.appendChild(canvas);

  var ctx = canvas.getContext && canvas.getContext("2d");
  if (!ctx) { return; }

  var GLYPHS = "0123456789ABCDEFｱｲｳｴｵｶｷｸｹｺｻｼｽｾ".split("");
  var FONT_SIZE = 16;
  var columns = 0;
  var drops = [];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    columns = Math.floor(canvas.width / FONT_SIZE);
    drops = [];
    for (var i = 0; i < columns; i++) {
      drops[i] = Math.floor(Math.random() * (canvas.height / FONT_SIZE));
    }
  }

  var resizeTimer;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(resize, 150);
  });

  resize();

  var last = 0;
  var FRAME_MS = 55; // about 18 fps, low CPU
  var rafId = null;

  function draw(now) {
    rafId = window.requestAnimationFrame(draw);
    if (now - last < FRAME_MS) { return; }
    last = now;

    ctx.fillStyle = "rgba(10, 14, 10, 0.10)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "rgba(0, 217, 54, 0.55)";
    ctx.font = FONT_SIZE + "px monospace";

    for (var i = 0; i < drops.length; i++) {
      var ch = GLYPHS[Math.floor(Math.random() * GLYPHS.length)];
      ctx.fillText(ch, i * FONT_SIZE, drops[i] * FONT_SIZE);
      if (drops[i] * FONT_SIZE > canvas.height && Math.random() > 0.975) {
        drops[i] = 0;
      }
      drops[i]++;
    }
  }

  function start() { if (rafId === null) { last = 0; rafId = window.requestAnimationFrame(draw); } }
  function stop() { if (rafId !== null) { window.cancelAnimationFrame(rafId); rafId = null; } }

  document.addEventListener("visibilitychange", function () {
    if (document.hidden) { stop(); } else { start(); }
  });

  start();
})();
```

- [ ] **Step 2: Wire the script in default.html**

In `_layouts/default.html`, immediately before the closing `</body>` tag (line 46), add:
```html
<script defer src="{{ '/assets/js/rain.js' | relative_url }}"></script>
```

- [ ] **Step 3: Rebuild and verify rain renders**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
test -f _site/assets/js/rain.js && echo "RAIN_JS_DEPLOYED"
```
Expected: build succeeds and prints `RAIN_JS_DEPLOYED`.

With Playwright, reload `http://localhost:4555/`, wait 1 second, screenshot at 1280x900. Expected: faint green katakana/digit rain visible behind the content; body copy fully readable on the near-black background; rain does not sit on top of text (it is at `z-index: -1`).

- [ ] **Step 4: Verify the visibility pause**

With Playwright, open a second tab to background the portfolio tab, wait 1 second, return, and confirm the page is still responsive and rain resumes. (If MCP tab control is unavailable, verify by code inspection that the `visibilitychange` handler calls `stop()`/`start()` and note it.)

- [ ] **Step 5: Verify reduced-motion disables rain**

The script returns before creating the canvas when reduced motion is set. If Playwright can emulate reduced motion, reload and confirm no `<canvas id="rain">` exists in the DOM (use a DOM snapshot, check for absence of the canvas). If emulation is unavailable, verify by code inspection that the early `return` precedes `document.body.appendChild(canvas)` and note it.

- [ ] **Step 6: Commit**

```bash
git add assets/js/rain.js _layouts/default.html
git commit -m "Add guarded ambient digital-rain canvas (reduced-motion and visibility aware)"
```

---

## Task 9: Full-site visual verification pass

**Files:** none modified (verification only; fixes found here get their own follow-up commit)

This is the visual audit the user explicitly requested. Use the superpowers:verification-before-completion discipline: evidence before claims.

- [ ] **Step 1: Rebuild fresh**

Run:
```bash
bundle exec jekyll build 2>&1 | tail -3
```
Expected: build succeeds.

- [ ] **Step 2: Screenshot matrix**

With Playwright, for each URL below, screenshot at 1280x900 and at 375x812:
- `/`
- `/about/`
- `/projects/`
- `/resume/`
- `/blog/`
- `/2026/04/30/building-soc-triage-copilot/`
- `/404.html`

For each, confirm: near-black background, green text legible, amber only on live/active status, monospace throughout, rain visible but behind content, no horizontal scrollbar at 375px, footer at the bottom of the viewport on short pages (check `/404.html` specifically).

- [ ] **Step 3: Keyboard and focus pass**

On `/` and `/projects/`, Tab through all interactive elements. Confirm a visible green focus ring on every link and button, and the project-title corner brackets appear on focus, not just hover.

- [ ] **Step 4: Contrast re-confirm**

Re-run the contrast command from Task 2 Step 5 with the final committed values for `--color-cream-muted` and `--color-cream-faint`. Confirm both >= 4.5:1. Paste the numeric output into the task notes as evidence.

- [ ] **Step 5: Record findings**

If any page has a visual regression (overflow, unreadable text, broken grid, footer float), list each with the file and the exact rule to change. Apply the fixes, rebuild, re-verify the affected page, then commit:
```bash
git add <changed files>
git commit -m "Fix visual regressions found in full-site verification pass"
```
If there are zero regressions, make no commit and state explicitly: "Full-site verification: 7 pages x 2 breakpoints, keyboard pass, contrast pass. No regressions."

- [ ] **Step 6: Stop the local server**

Run:
```bash
pkill -f "httpd _site -p 4555" || true
```

---

## Task 10: CLAUDE.md update

**Files:**
- Modify: `CLAUDE.md` (Design System section)

The repo CLAUDE.md documents the editorial design system. It is now wrong. Update it so future sessions are not misled.

- [ ] **Step 1: Update the Design System and palette description**

In `CLAUDE.md`, replace the "Design System", "Palette", and "Typography" subsections under `## Design System` with an accurate description of the Matrix terminal system: dimmed-phosphor green (`#00D936`) on near-black (`#0A0E0A`), amber demoted to live/active status LED only, JetBrains Mono as the single typeface, the `assets/js/rain.js` ambient rain module and its reduced-motion/visibility guards, and the note that token variable names retain the old "cream/iron" naming while holding green values. Keep all other CLAUDE.md sections unchanged. No em dashes.

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "Update CLAUDE.md to document the Matrix terminal design system"
```

---

## Done Criteria

- All tasks committed.
- `bundle exec jekyll build` succeeds with no `_site/docs` directory.
- 7 pages x 2 breakpoints visually verified in a real browser.
- Keyboard focus ring visible site-wide; project frames keyboard-reachable.
- `--color-cream-muted` and `--color-cream-faint` both >= 4.5:1 on `#0A0E0A` (numeric evidence recorded).
- No inline styles referencing CSS variables remain.
- Rain renders, pauses when tab hidden, and is absent under reduced motion.
- CLAUDE.md reflects the new system.

## Self-Review Notes

- **Spec coverage:** palette swap (T2), typography collapse (T2/T3), terminal language CSS (T6) and HTML (T7), rain module with all three guards (T8), every audit finding mapped: #1 focus-visible (T4), #2 contrast (T2 step 5 + T9 step 4), #3 reduced-motion (T4 + T8), #4 grid borders (T5), #6 color-only nav (T6 step 4), #7 inline styles (T7), #8 footer (T2 step 2). `_config.yml` docs/ exclude (T1). All spec sections have a task.
- **Placeholder scan:** no TBD/TODO; all CSS and JS shown in full; verification commands have expected output.
- **Consistency:** token variable names (`--color-cream*`, `--color-iron*`) are referenced identically across T2, T6, T7, T8. Class names `.section-link`, `.post-meta-line`, `.page-404*` defined in T7 step 1 and used in T7 steps 2-7. `rain.js` uses the same `#0A0E0A` / `0,217,54` values as the T2 tokens.
