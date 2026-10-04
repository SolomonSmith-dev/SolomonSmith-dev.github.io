# Editorial Redesign

Date: 2026-10-03
Branch: `redesign/editorial-2026`
Content corrected 2026-10-03 against the master resume (`swe-job-hunt/OUTPUTS/resumes/2026-09-28_master_newgrad_resume.md`): the Recursa internship and its metrics were removed and replaced by Founding Engineer, Jul 2026 to present.

Decisions (Solomon, 2026-10-03): full departure from the Matrix theme; light and dark modes; availability is full-time from January 2027 only; no case-study pages this round (they come with the resume, portfolio and LinkedIn cleanup).

## 1. Current portfolio audit

| Area | What was wrong | Why it matters | Replacement |
|---|---|---|---|
| First impression | H1 was the name only. Title lived in a side rail ("Focus"). Lede opened with the chef story. | A recruiter could not tell the role in 5 seconds. | H1 = name + "AI/ML Engineer" + one specific value statement. Chef story moved to its own section. |
| Primary CTA | "View Resume" (PDF) was primary. Every page repeated a three-button CTA row. | CTA noise. Nothing set the order of the visit. | Primary: View selected work. Secondary: resume, email. One contact band per page. |
| Hierarchy | Home order: proof, skills, work, currently, writing. | Skills before evidence is backwards. | Order: hero, metrics, work, experience, skills, background, contact. |
| Project presentation | Paragraph blobs. Titles linked off-site. | Hard to scan. Problem, approach and result were mixed together. | Cards with a Problem / Built / Result list. Only rows backed by real facts. |
| Redundancy | Full experience bullets duplicated on About and Resume. | Two copies drift apart. | About is the narrative. Resume holds the detail. Home gets one line per role. |
| Readability | All-mono body text, green on black, rain canvas, blinking cursor. | Long mono prose reads slowly, and the motif reads as a hobby theme. | Serif display, sans body, mono only for data labels. |
| Stale copy | "Fall 2026 internships" in October 2026. | Signals a site nobody maintains. | "Graduating Dec 2026. Full-time from January 2027." |
| Nav | `~/about`, `cd ../projects`, `[/]` terminal button. | A cute idiom that costs scannability. | Work, About, Resume, Writing, plus a Contact button. |
| Accessibility | Good base (skip link, focus ring, reduced motion). | Keep it. | Kept. Added `aria-current`, a theme toggle with a label, and print styles. |

## 2. Positioning

Software engineer building LLM-backed backend features that fail closed. Evidence: the CourtRules citation verifier (7 tests, caught a bypass before release), ARDA's 425 offline tests, SOC Triage AI's harness (43% to 100%), PhishGuard's leakage fixes (test AUC 0.9943). Differentiator: ten years running professional kitchens.

Targets: full-time AI/ML and backend engineering from January 2027. RAG and retrieval backends, LLM evaluation, AI platform and backend work.

## 3. Visitor journey

5 seconds: name, role, value statement, availability. 30 seconds: three metrics, four project cards. 2 minutes: experience timeline, skills, About. Exit: email, resume PDF or LinkedIn from the hero, header, contact band and footer.

## 4. Sitemap

`/` home, `/projects/` work (grouped), `/about/`, `/resume/`, `/blog/`. Later: `/projects/<slug>/` case studies. `/card` unchanged (separate Vite build).

## 5-6. Sections and copy

Live in `index.md`, `projects.md`, `about.md`. All copy is rewritten from existing facts only. Nothing was added that was not already on the site.

## 7-9. Design system, typography, color

- Display: Newsreader 400/500. Body: IBM Plex Sans 400/500/600, 17px / 1.65. Data labels: IBM Plex Mono 13px uppercase.
- Scale: 13 / 14 / 17 / 20 / 26 / clamp(30-36) / clamp(36-52).
- Spacing: 8px rhythm. Container 68rem, prose measure 40rem.

| Token | Light | Dark |
|---|---|---|
| bg | #F7F6F2 | #111210 |
| surface | #FFFFFF | #181A17 |
| surface-2 | #EFEDE6 | #20221F |
| text | #161614 | #ECEBE5 |
| text-2 | #55554F | #B0AFA7 |
| text-3 | #6E6D66 | #93928A |
| border | #E2DFD6 | #2B2D29 |
| accent (links, primary CTA) | #1E5B47 | #8BCFB2 |
| live dot | #23935F | #4CC38A |

## 10. Components

`.btn` pill (primary filled, secondary outline, 44px min height), `.project` card, `.status` pill, `.stack` mono tags, `.metrics` strip, `.timeline`, `.entry`, `.skills` (grouped lists, no bars), `.split`, `.contact` band, footer link row. There are no testimonials because none exist. Do not invent any.

## 11. Case-study template (deferred)

Context, Problem, Role, Approach, Solution, Result, Reflection. Ship one page per project at `/projects/<slug>/` once the resume and LinkedIn cleanup locks the facts. Candidates: CourtRules judge assistant (needs employer clearance), ARDA, PhishGuard, SOC Triage AI.

## 12. Mobile

The header wraps to two rows (brand + actions, then a scrollable nav). The Contact button is hidden under 720px because the hero and footer carry it. Hero photo becomes an 80px avatar above the text. Metrics stack. Project fact rows go from two columns to one. Hero buttons stretch to fill the row. Verified at 390px with no horizontal overflow.

## 13. Accessibility

Focus ring, skip link, `aria-current`, labelled toggle, alt text on the portrait, reduced motion, landmark headings per section. The theme persists through localStorage, guarded with try/catch, and defaults to the system setting.

## 14. Motion

One 500ms fade-up on the hero. 150ms hover color and border transitions. Nothing loops.

## 15. Removed

`rain.js`, `easter-eggs.js` (terminal and console art), blinking cursor, `[01]` section markers, `>` button glyphs, `~/` nav, amber, the "Currently" bullet list, the home writing list, duplicated experience on About, the "Reach" list.

## 16. Blueprint

See the branch. Home: hero, metrics, Selected work (CourtRules, ARDA, PhishGuard, SOC Triage AI), Experience, Skills, Background, Contact.

## 17. Priorities after merge

1. Done in this branch: new OG image (1200x630) and favicon set (SVG, 32px, 180px).
2. Done: skills now come from one include that matches the master resume.
3. Case-study pages (section 11).
4. Rewrite or retire the 2024 "first post".
5. Search Console and analytics (open items from the 2026-07-10 audit).
