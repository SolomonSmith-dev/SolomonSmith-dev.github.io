# Portfolio Audit: Traffic and Hiring

Date: 2026-07-10
Site: https://solomonsmith.dev

## Verdict

The site already reads as a strong personal brand: clear target roles, quantified internship impact, shipped AI/ML projects with honest metrics, and a distinctive Matrix terminal aesthetic that is memorable without looking like a template. The biggest gaps are conversion (recruiters had no primary CTA), shareability (weak social preview image, no favicon on the main site), and distribution (thin writing surface area and no measurement).

This pass hardens the professional conversion path and SEO plumbing. Traffic growth and hiring outcomes still depend on off-site distribution and continued technical writing.

## What is already working

- Clear positioning: AI/ML, RAG, multi-agent systems, Fall 2026 internships / Jan 2027 full-time
- Strong project proof: soc-triage-ai reliability harness, Recursa hallucination catch, phishguard AUC + LIMITATIONS.md honesty
- Distinctive visual system that stands out in a sea of generic portfolios
- jekyll-seo-tag, sitemap, RSS feed already wired
- Custom domain with HTTPS
- Resume page + downloadable PDF
- Digital card at `/card`

## Changes shipped in this PR

1. Primary hiring CTAs on home, about, projects, resume, and footer (`View Resume` / `Email me` / `Resume PDF`)
2. Person JSON-LD with skills, school, location, and social sameAs
3. Site favicon (phosphor green SS monogram)
4. 1200x630 Open Graph image + `summary_large_image` Twitter card
5. Skip-to-content link, theme-color, nav aria-label
6. `robots.txt` and `llms.txt` for crawlers and AI assistants
7. Education honors listed before GPA (Dean's List first)
8. Removed inline styles from about/resume CTAs; headshot uses a proper class

## Traffic: what moves the needle next

### Technical SEO (done or near-done)

- [x] Favicon, OG card, Person schema, robots/llms
- [x] Clean `/blog/:slug/` permalinks with redirects from old category URLs
- [x] Apple touch icon + web manifest
- [x] Optional Plausible analytics hook (`plausible_domain` in `_config.yml`)
- [ ] Verify Google Search Console property for `solomonsmith.dev` and submit sitemap
- [ ] Verify Bing Webmaster Tools
- [ ] Confirm Cloudflare managed `robots.txt` is not over-blocking discovery you want (it currently blocks several AI training bots; search indexing remains allowed)
- [ ] Uncomment/set `plausible_domain` after creating a Plausible site

### Content SEO (highest leverage for organic traffic)

Search traffic for a personal portfolio comes almost entirely from technical writing and project pages that answer specific queries.

Ship 4 to 6 posts over the next few months on topics you already have proof for:

1. How the Recursa eval harness caught a 12% hallucination regression
2. Why corpus chunking beat prompt tweaks in soc-triage-ai (43% to 100% harness)
3. Leakage tests that killed phishguard v0.1 (honest ML post; rare and shareable)
4. Self-hosting multi-agent infra on Debian + PM2 + Tailscale
5. Prompt injection defenses in DocMind

Each post should target one concrete problem, include architecture notes, and link back to the GitHub repo and `/projects/`.

Do not generate filler posts. Depth beats cadence.

### Distribution (off-site)

The site will not grow on its own. Push work outward:

- LinkedIn: weekly project or learning posts with a link to the site or Loom
- Fix LinkedIn profile mismatches noted in CLAUDE.md (degree field, role titles)
- Share the soc-triage Loom in AI/security Discords, CodePath alumni channels, and relevant Subreddits when the post is ready
- Pin the best three repos on GitHub with READMEs that link to solomonsmith.dev
- Add the site URL to resume header, email signature, and application forms
- Consider a short demo video for phishguard and DocMind (even 2 to 3 minutes)

### Measurement

Add a privacy-friendly analytics option (Plausible, GoatCounter, or Cloudflare Web Analytics) so you can see which pages and referrers convert. Without this, traffic advice stays guesswork.

## Hiring: what gets you interviews

### Conversion path (improved here)

Recruiters and hiring managers typically spend under 30 seconds on a portfolio. They need:

1. Who you are
2. What you want
3. Proof you can do the job
4. How to contact you

Before this PR, (4) was buried in text links. Hero and footer now lead with email + resume.

### Proof stack to keep strengthening

| Signal | Status | Next step |
|--------|--------|-----------|
| Quantified internship impact | Strong | Keep Recursa metrics on LinkedIn and resume PDF in sync |
| Shipped projects with tests/CI | Strong | Add live demos or short Looms for arda, DocMind, phishguard |
| Technical writing | Thin (2 posts) | Publish the eval-harness and leakage-test posts |
| Production ops story | Good (Sauron Stack) | One write-up turns this into a differentiator |
| Public presence | Partial | LinkedIn consistency + GitHub pin READMEs |

### Resume and application hygiene

- Lead with Dean's List and coursework; keep GPA available but secondary (done on site)
- Mirror site language on LinkedIn: Software Engineering Intern (Recursa), Full-Stack Developer Intern (RideSplits), Computer Science (not Computational Science)
- For each application, deep-link the most relevant project (not just the homepage)
- Keep the PDF in `assets/resume/` current whenever experience changes

### Aesthetic note

Keep the Matrix terminal look. It is a brand asset, not a liability, as long as hiring CTAs remain obvious. Do not flatten the site into a generic light SaaS portfolio. The easter-egg terminal can stay; it is discoverable, not blocking.

## Professional polish still worth doing later

1. Live demo links or Loom for every featured project
2. Case-study pages (`/projects/soc-triage-ai/`) with architecture diagrams for the top 2 to 3 projects
3. Privacy-friendly analytics
4. Compress/crop headshot for faster LCP on about
5. Optional: lighten GPA emphasis on the PDF if it is still leading the education block there
6. Keep blog categories clean so post URLs stay readable

## Success criteria

- Recruiter can email or download resume from the first viewport without hunting
- LinkedIn/Twitter/Slack unfurls show a clear name + role + availability card
- Search Console shows indexing of home, about, projects, resume, and key posts
- At least one technical post per major project that can be shared in applications
