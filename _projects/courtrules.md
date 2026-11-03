---
title: "CourtRules judge assistant"
eyebrow: "Project &middot; CourtRules judge assistant"
heading: "Ask a judge's page a filing question. Get the judge's own words back, or nothing."
lede: "The retrieval-grounded Q&A feature on CourtRules, a legal-data platform covering filing rules for 1,653 judges. I shipped it as the second engineer at Recursa AI."
description: "CourtRules judge assistant by Solomon Smith: retrieval-grounded Q&A over filed court orders with a fail-closed citation verifier, built as founding engineer at Recursa AI."
order: 1
status: "Production"
live: true
stack: [TypeScript, Next.js, Supabase, PostgreSQL, NDJSON streaming]
links:
  - label: "Product"
    url: "https://courtrules.app"
---

## What it does

A lawyer on a judge's page types a filing question. The service fetches that judge's filed orders from object storage, extracts text per page, grounds the model in that text, and streams the answer as NDJSON with the sentence each claim quotes.

## Why it is hard

Grounding a model in the source does not stop it from inventing a quote that sounds like the source. In a filing-rules product that is the worst failure available: a confident, specific, wrong instruction to a lawyer on a deadline. So the answer path fails closed. A claim renders only if its quoted sentence appears verbatim in the order. If nothing survives, the user sees a refusal, not a guess.

The verifier's tests earned their keep before release. One caught a bypass where an invented quote passed because it pointed at a plausible source index.

Around the assistant I built query analytics that classify questions into the product's 14-type rule taxonomy, with a Postgres view ranking unanswered questions so we can tell a data gap from a retrieval failure (service-write-only RLS). I also added iCal and CSV court-calendar exports that follow RFC 5545 and RFC 4180 and guard against CSV formula injection (CWE-1236).

## Evidence

The code is private, so these come from the product and my resume, not a public command.

| Number | Where it comes from |
|---|---|
| 1,653 judges | The platform's judge coverage |
| 57% of pageviews | Share carried by judge pages, from product analytics |
| 14 rule types | The taxonomy the query classifier writes into |
| RFC 5545, RFC 4180, CWE-1236 | The iCal and CSV export specs and the injection guard they implement |
{: .evidence}
