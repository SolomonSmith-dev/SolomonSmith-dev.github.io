---
name: adhd-friendly-checklist
description: Turn plans and next steps into short ADHD-friendly checklists with one action per line, Done when criteria, and Now/Next/Later buckets. Use when the user asks for an ADHD-friendly checklist, ADHD checklist, simple checklist, next steps checklist, or says they have ADHD and need a clear action list.
---

# ADHD-Friendly Checklist

## When to use

Any time the user wants next steps, a launch plan, or a todo list and asks for it to be ADHD-friendly, simple, or easy to execute.

## Output rules

1. **Lead with the single most important next action** in one sentence.
2. **One action per checkbox.** No compound "do X and Y" items.
3. **Start each item with a verb** (Merge, Open, Paste, Send, Write).
4. **Add a `Done when:` line** under each item so completion is obvious.
5. **Bucket into Now / Next / Later.** Now = do today. Next = this week. Later = whenever.
6. **Keep the whole checklist scannable.** Prefer under 12 Now+Next items. Move the rest to Later.
7. **No walls of text.** No essays between items. One short note max per bucket if needed.
8. **No calendar-day estimates** unless the user asks. Use effort tags only if helpful: `[5 min]`, `[15 min]`, `[deep work]`.
9. **No em dashes.** Use a colon, period, or `--`.
10. **If the task needs an account the user must create** (Search Console, analytics, LinkedIn), say that plainly and stop at the boundary of what the agent can do in-repo.

## Template

Copy this structure:

```markdown
**Do this first:** [one concrete action]

### Now
- [ ] [Verb] [specific action] `[effort]`
  - Done when: [observable result]

### Next
- [ ] [Verb] [specific action] `[effort]`
  - Done when: [observable result]

### Later
- [ ] [Verb] [specific action]
  - Done when: [observable result]

### Parking lot
Things that matter but are not checklist items yet:
- [optional note]
```

## Good vs bad items

Bad:
- [ ] Improve SEO and set up analytics and fix LinkedIn

Good:
- [ ] Merge PR #4 `[5 min]`
  - Done when: PR shows Merged on GitHub
- [ ] Add `solomonsmith.dev` in Google Search Console `[15 min]`
  - Done when: property is Added / Verified
- [ ] Submit `https://solomonsmith.dev/sitemap.xml` `[5 min]`
  - Done when: sitemap shows as Submitted

## Domain extras for this portfolio repo

When the checklist is about solomonsmith.dev / hiring / traffic:

- Prefer merge → Search Console → LinkedIn fixes → analytics → distribution → writing.
- Do not generate blog posts unless the user explicitly asks.
- Keep Matrix terminal aesthetic; do not suggest a generic redesign.
- Target language: Fall 2026 internships and full-time AI/ML roles starting January 2027.
- No emojis on the rendered site unless explicitly requested.

## After delivering the checklist

Ask one question max, only if a blocker is real. Example: "Want me to turn the Next bucket into repo changes too?"
Otherwise stop. Do not expand into a second plan unless asked.
