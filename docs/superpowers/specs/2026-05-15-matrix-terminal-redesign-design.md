---
title: Matrix Terminal Redesign
date: 2026-05-15
status: approved-for-planning
sitemap: false
---

# Matrix Terminal Redesign: Design Spec

## Purpose

Replace the editorial (warm iron / serif) visual identity of
solomonsmith-dev.github.io with a unique Matrix style terminal aesthetic:
phosphor green on near black, all monospace, with subtle ambient digital
rain. The redesign must simultaneously fix every accessibility and
responsiveness defect found in the 2026-05-15 frontend audit, because a
new skin on broken a11y is not acceptable for a hiring portfolio.

Audience: technical recruiters and hiring managers for full time AI/ML
engineering roles starting January 2027. The look must be distinctive but
must not sacrifice content legibility.

## Constraints

- No em dashes anywhere (frontmatter, body, CSS comments, commit message).
- No content rewrites. Copy, project list, and resume content are unchanged.
- Token driven. Identity changes route through `:root` custom properties
  and targeted rule edits in `assets/main.scss`. No layout teardown.
- No new build tooling. Jekyll on GitHub Pages stays as is.
- No JS framework or animation library. Rain is hand written vanilla JS.
- Resume PDF link unchanged.

## Architecture

The current site is a design token system: every color, font, and spacing
value resolves through `:root` custom properties in `assets/main.scss`
(714 lines). The layout primitives (`.hero`, `.course`, `.course-list`,
`.section-marker`, `.stations`, `.station`, `.entry`, `.prose`,
`.post-list`, `.btn`, `.site-header`, `.site-footer`) keep their structure.
Only the skin and a small number of structural reskin rules change.

Three units of work, each independently testable:

1. **Token and rule reskin** (`assets/main.scss`): palette swap,
   typography collapse to one mono family, terminal language details,
   plus the audit fixes that live in CSS.
2. **Digital rain module** (new `assets/js/rain.js`, wired in
   `_layouts/default.html`): one canvas, fixed behind content, guarded.
3. **Template detox** (`_layouts/home.html`, `404.html`): replace inline
   `style=` blocks with real classes so the token system has no leaks.

## Detailed Design

### 1. Palette (token swap in `:root`)

| Token | Old | New |
|---|---|---|
| `--color-iron` | `#13110F` | `#0A0E0A` (near black, faint green cast) |
| `--color-iron-2` | `#1A1714` | `#0F140F` (code block / panel) |
| `--color-cream` | `#EDE6D6` | `--color-green: #00D936` (primary text, dimmed phosphor for lower eye strain on text heavy pages) |
| `--color-cream-soft` | rgba cream .78 | `#7CFF9E` (secondary text, AA on new black) |
| `--color-cream-muted` | rgba cream .55 | `rgba(0,255,65,0.72)` (retuned to pass AA for small text) |
| `--color-cream-faint` | rgba cream .35 | `rgba(0,255,65,0.58)` (retuned, course numbers now legible) |
| `--color-hairline` | rgba cream .16 | `rgba(0,255,65,0.20)` |
| `--color-amber` | `#E8A05B` | kept, demoted to status LED only |

Variable names stay the same to avoid a 714 line rename. `--color-cream`
keeps its name but holds green. A short comment block at the top of
`:root` documents this so the name/value mismatch does not confuse later
edits.

Contrast targets (verify with a contrast checker during build):
- Primary green `#00D936` on `#0A0E0A`: very high, passes AAA.
- `--color-cream-muted` and `--color-cream-faint` retuned so all small
  text (section labels, course numbers, meta) clears WCAG AA 4.5:1.
  This is the fix for audit findings on faint and muted contrast.

Amber (`--color-amber`) is used in exactly one place: `.course__status`
and `.status-board__list .tag` when the value is a live or active state.
It reads as a signal LED, not decoration.

### 2. Typography

- Delete the Google Fonts request for Fraunces and Newsreader from
  `_layouts/default.html`. Load only JetBrains Mono (weights 400, 500,
  700). This also resolves the audit finding on heavy multi font first
  paint.
- `--font-display`, `--font-body`, `--font-mono` all resolve to the
  JetBrains Mono stack. Names kept; values collapsed.
- Hierarchy by weight and size, not family: name and `.hero__name` at
  weight 700 large; `h2`/`h3` weight 500; body weight 400.
- Remove italic dependent rules (e.g. `.hero__name em`,
  `.entry__role` italic) and replace emphasis with weight or a leading
  `>` glyph, since mono italic is weak.

### 3. Terminal language (structural reskin, same HTML where possible)

- `.section-marker__roman`: Roman numeral becomes a mono `[01]` index.
  `.section-marker__label`: prefixed with `> ` and lowercased
  (`> stations`, `> featured work`, `> writing`). HTML text edits in
  `index.md` and the post list in `home.html` only.
- Hero: `.hero__name` stays large. `.hero__lede` ends with a CSS only
  blink cursor (`_`) via a pseudo element and `@keyframes`. The blink is
  disabled under `prefers-reduced-motion`.
- `.course__title` hover: replace the amber underline `::after` with a
  box drawing frame effect (corner borders) on `:hover` and
  `:focus-within`. Keyboard reachable.
- `.site-nav`: labels become path style (`~/about`, `~/projects`,
  `~/blog`, `~/resume`). Active state is bright green with a leading
  `>` and a non color cue (underline or weight) so state is not color
  only. This fixes the color only nav state audit finding.
- `.btn`: green border, on hover inverts to solid green on black. Mono
  uppercase retained.

### 4. Digital rain module

New file `assets/js/rain.js`, referenced once with `defer` at the end of
`<body>` in `_layouts/default.html`. A single `<canvas id="rain">` is
inserted, `position: fixed; inset: 0; z-index: -1; pointer-events: none`.

Behavior:
- Katakana plus digits glyph set, classic Matrix column fall.
- Low opacity. Content sits on the page background which is near opaque,
  so body copy never competes with rain. No per block dimming needed
  because the canvas is behind everything at `z-index: -1` and the body
  background is `--color-iron`.
- Guards:
  - If `window.matchMedia('(prefers-reduced-motion: reduce)').matches`,
    the script does not start and no canvas is added. This is the same
    switch as the CSS reduced motion fix.
  - Page Visibility API: cancel the animation frame when
    `document.hidden`, resume on focus.
  - `requestAnimationFrame` throttled to about 20 fps via timestamp gate
    to keep CPU and battery low.
  - Resize handler debounced; canvas re sized to viewport.
- About 60 lines, no dependencies.

### 5. Audit fixes folded in (ship together, non negotiable)

| Finding | Severity | Fix |
|---|---|---|
| No `:focus-visible` anywhere | HIGH | Global `:focus-visible` rule: 2px solid green outline, 2px offset, on all interactive elements. |
| Faint and muted text fail WCAG AA | HIGH | Retune `--color-cream-muted` and `--color-cream-faint` (see palette table) to clear 4.5:1. |
| No `prefers-reduced-motion` | MED | `@media (prefers-reduced-motion: reduce)`: disable `scroll-behavior`, zero all transitions, disable cursor blink. Rain JS self disables (section 4). |
| `.stations` / `.station` dangling borders on wrap | MED | Replace `:last-child` border removal with grid `gap` plus a single outer border on `.stations`. Per cell borders dropped. |
| Nav state is color only | MED | Active nav adds leading `>` and weight or underline (section 3). |
| Inline `style=` in `home.html` and `404.html` | LOW | Replace with classes: `.section-link` for the "All projects / All writing" links, `.page-404` block for the 404 layout. |
| `main.shell { min-height: 60vh }` floats footer | LOW | Use `min-height: calc(100vh - <header+footer>)` via flex column on `body` so footer sits at viewport bottom on short pages. |

### 6. Scope

In scope: `index.md`, `about.md`, `projects.md`, `resume.md`, `blog.md`,
`_layouts/*.html`, `404.html`, `assets/main.scss`, new
`assets/js/rain.js`, and `_config.yml` (add `docs/` to `exclude:` so
spec files are not built into the deployed site; confirmed 2026-05-15).

Pages without dedicated audit changes (about, projects, resume, blog,
post) still inherit the reskinned primitives and are visually verified.

Out of scope (YAGNI): interactive command input, simulated filesystem,
sound, light or theme toggle, content rewrites, custom domain.

## Data Flow

Static site. No runtime data flow. The only dynamic element is the rain
canvas, which is purely presentational, reads no state, and writes
nothing. It depends only on viewport size, the reduced motion media
query, and the Page Visibility API.

## Error Handling

- Rain script is defensive: if `<canvas>` or 2D context is unavailable,
  it returns silently. The site is fully functional with zero rain
  (progressive enhancement). Rain is never required for content.
- No network calls, no failure modes beyond canvas absence.

## Testing and Verification

Local: `bundle exec jekyll build` must succeed (note: Solomon's machine
had a bundler mismatch on 2026-05-13; if local build fails for that
reason, rely on Pages CI and visual checks).

Visual verification (real browser, the audit answer asked for a visual
pass):
1. Home, about, projects, resume, blog, a post, and 404 at desktop
   (1280px), tablet (768px), mobile (375px).
2. Keyboard tab through every page: focus ring visible on all links and
   buttons.
3. Toggle OS reduced motion: rain absent, no transitions, no cursor
   blink, page fully usable.
4. Contrast check the three smallest text tiers against `#0A0E0A`.
5. `.stations` grid at a width that forces a second row: no dangling
   borders.
6. Footer sits at viewport bottom on a short page (404).
7. Tab to background, confirm rain animation pauses (DevTools
   performance or a console log during dev only, removed before commit).

Done means: all seven checks pass and the diff is reviewed before commit.

## Open Questions

None. Amber as status LED confirmed. Subtle ambient rain confirmed. Full
site scope confirmed.
