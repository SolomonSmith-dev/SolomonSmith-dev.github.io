#!/usr/bin/env python3
"""Convert the canonical plain-text resume into the site's resume.md body.

Reads the resume at --source (the .md in swe-job-hunt/MATERIALS, which is a
plain-text layout, not Markdown), keeps the YAML front matter already in
--page, and rewrites everything below it. Also rewrites --skills (the shared
_includes/skills.html) from the SKILLS block so index.md and resume.md show
the same skills as the resume.

Stdlib only. Deterministic: the same input always produces the same output.

Source layout the parser expects:

    NAME
    contact | fields | separated | by pipes
    tagline | separated | by pipes

    SECTION HEADING IN CAPS
    Entry title | org or detail | dates | location      <- pipe-separated head
    optional one-line description                      <- no leading "- "
    - bullet
    - bullet

    SKILLS
    Category: comma, separated, items

Run through scripts/sync-resume.sh rather than by hand.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

URL_RE = re.compile(r"^(?:https?://)?((?:github\.com|linkedin\.com|[\w.-]+\.(?:app|dev|com|io|org))(?:/\S*)?)$")
PHONE_RE = re.compile(r"^\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}$")
EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.]+$")
EM_DASH = "\u2014"  # written as an escape so this file passes the no-em-dash rule


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def is_heading(line: str) -> bool:
    return bool(line) and line == line.upper() and any(c.isalpha() for c in line) and " | " not in line


def title_case_heading(h: str) -> str:
    """EDUCATION -> Education, OPEN SOURCE -> Open source."""
    words = h.lower().split()
    return " ".join([words[0].capitalize()] + words[1:])


def link_or_text(field: str) -> str:
    """Bare domain paths become links; everything else is escaped text."""
    m = URL_RE.match(field.strip())
    if m:
        return f'<a href="https://{esc(m.group(1))}">{esc(field.strip())}</a>'
    return esc(field.strip())


def parse(text: str) -> dict:
    lines = [ln.rstrip() for ln in text.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    if len(lines) < 3:
        sys.exit("resume_md: source has fewer than three header lines")
    name, contact, tagline = lines[0].strip(), lines[1].strip(), lines[2].strip()
    sections: list[tuple[str, list]] = []
    current: list | None = None
    entry: dict | None = None
    for raw in lines[3:]:
        line = raw.strip()
        if not line:
            entry = None
            continue
        if is_heading(line):
            current = []
            sections.append((line, current))
            entry = None
            continue
        if current is None:
            sys.exit(f"resume_md: text before the first section heading: {line!r}")
        if line.startswith("- "):
            if entry is None:
                sys.exit(f"resume_md: bullet with no entry: {line!r}")
            entry["bullets"].append(line[2:].strip())
        elif " | " in line:
            entry = {"head": [f.strip() for f in line.split(" | ")], "desc": [], "bullets": []}
            current.append(entry)
        elif ": " in line and entry is None and sections[-1][0] == "SKILLS":
            cat, items = line.split(": ", 1)
            # A value with its own colon is a sentence ("10+ years: Dishwasher promoted to Head Chef"), not a list.
            parts = [items.strip()] if ": " in items else [i.strip() for i in items.split(", ")]
            current.append({"category": cat.strip(), "items": parts})
        elif entry is not None:
            entry["desc"].append(line)
        else:
            # A one-line entry with no pipes (rare); treat as its own head.
            entry = {"head": [line], "desc": [], "bullets": []}
            current.append(entry)
    return {"name": name, "contact": contact, "tagline": tagline, "sections": sections}


def render_contact(contact: str) -> str:
    """Location, email and profile links. The phone number stays off the public page."""
    parts = []
    for field in contact.split(" | "):
        f = field.strip()
        if PHONE_RE.match(f):
            continue
        if EMAIL_RE.match(f):
            parts.append(f'<a href="mailto:{esc(f)}">{esc(f)}</a>')
        else:
            parts.append(link_or_text(f))
    return " &middot; ".join(parts)


def render_entry(e: dict, kind: str) -> str:
    head = e["head"]
    out = ['<div class="entry">', '  <div class="entry__head">']
    if kind == "EXPERIENCE":
        title = esc(head[0])
        org = esc(head[1]) if len(head) > 1 else ""
        meta = " &middot; ".join(esc(h) for h in head[2:])
        out.append(f'    <p class="entry__title">{title}{f" <span class=\"entry__org\">&middot; {org}</span>" if org else ""}</p>')
        if meta:
            out.append(f'    <p class="entry__meta">{meta}</p>')
    elif kind == "EDUCATION":
        org = esc(head[0])
        degree = esc(head[1]) if len(head) > 1 else ""
        meta = " &middot; ".join(esc(h) for h in head[2:])
        out.append(f'    <p class="entry__title">{degree or org}{f" <span class=\"entry__org\">&middot; {org}</span>" if degree else ""}</p>')
        if meta:
            out.append(f'    <p class="entry__meta">{meta}</p>')
    else:  # PROJECTS, OPEN SOURCE and anything else: title [| detail] [| link]
        link = next((h for h in head[1:] if URL_RE.match(h)), None)
        details = [h for h in head[1:] if h != link]
        title = esc(head[0])
        if link:
            title = f'<a href="https://{esc(URL_RE.match(link).group(1))}">{title}</a>'
        sub = f' <span class="entry__org">&middot; {esc(details[0])}</span>' if details else ""
        out.append(f'    <p class="entry__title">{title}{sub}</p>')
        if len(details) > 1:
            out.append(f'    <p class="entry__meta">{" &middot; ".join(esc(d) for d in details[1:])}</p>')
    out.append("  </div>")
    for d in e["desc"]:
        out.append(f'  <p class="entry__meta">{esc(d)}</p>')
    if e["bullets"]:
        out.append("  <ul>")
        out.extend(f"    <li>{esc(b)}</li>" for b in e["bullets"])
        out.append("  </ul>")
    out.append("</div>")
    return "\n".join(out)


def render_skills(items: list) -> str:
    out = ['<div class="skills">']
    for s in items:
        out.append("  <div>")
        out.append(f'    <h3 class="skills__title">{esc(s["category"])}</h3>')
        out.append("    <ul>" + "".join(f"<li>{esc(i)}</li>" for i in s["items"]) + "</ul>")
        out.append("  </div>")
    out.append("</div>")
    return "\n".join(out) + "\n"


def render_body(r: dict, pdf: str, email: str) -> str:
    buttons = (
        '<div class="btn-row">\n'
        f"  <a class=\"btn btn--primary\" href=\"{{{{ '{pdf}' | relative_url }}}}\">Download PDF</a>\n"
        f'  <a class="btn" href="mailto:{{{{ site.email }}}}?subject=Opportunity%20for%20Solomon%20Smith">Email me</a>\n'
        "</div>"
    )
    parts = [
        buttons,
        "",
        f'<p class="resume-tagline">{" &middot; ".join(esc(t.strip()) for t in r["tagline"].split(" | "))}</p>',
        f'<p class="resume-contact">{render_contact(r["contact"])}</p>',
    ]
    for heading, items in r["sections"]:
        parts.append("")
        parts.append(f"## {title_case_heading(heading)}")
        parts.append("")
        if heading == "SKILLS":
            parts.append("{% include skills.html %}")
        else:
            parts.append("\n\n".join(render_entry(e, heading) for e in items))
    parts += ["", buttons.replace('<div class="btn-row">', '<div class="btn-row" style="margin-top: 2rem">'), ""]
    return "\n".join(parts)


def split_front_matter(page: str) -> str:
    if not page.startswith("---\n"):
        sys.exit("resume_md: resume.md has no front matter to preserve")
    end = page.find("\n---\n", 4)
    if end < 0:
        sys.exit("resume_md: unterminated front matter in resume.md")
    return page[: end + 5]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", required=True, type=Path, help="canonical resume .md (plain-text layout)")
    ap.add_argument("--page", required=True, type=Path, help="site resume.md; front matter is kept")
    ap.add_argument("--skills", required=True, type=Path, help="_includes/skills.html to regenerate")
    ap.add_argument("--pdf", required=True, help="site path of the synced PDF, e.g. /assets/resume/SolomonSmithResume.pdf")
    args = ap.parse_args()

    text = args.source.read_text(encoding="utf-8")
    if EM_DASH in text:
        sys.exit("resume_md: source contains an em dash; fix the resume first")
    resume = parse(text)
    skills = next((items for h, items in resume["sections"] if h == "SKILLS"), None)
    if not skills:
        sys.exit("resume_md: no SKILLS section in source")
    for required in ("EDUCATION", "EXPERIENCE", "PROJECTS"):
        if required not in {h for h, _ in resume["sections"]}:
            sys.exit(f"resume_md: no {required} section in source")

    front = split_front_matter(args.page.read_text(encoding="utf-8"))
    body = render_body(resume, args.pdf, "")
    args.page.write_text(front + "\n" + body, encoding="utf-8")
    args.skills.write_text(render_skills(skills), encoding="utf-8")
    print(f"wrote {args.page} ({len(resume['sections'])} sections) and {args.skills} ({len(skills)} skill groups)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
