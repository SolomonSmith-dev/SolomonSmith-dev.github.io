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

## Interactive verifier demo: FRCP 6(a) fail-closed quote check

Test how the citation gate handles claims against a filed standing order. A claim renders **only** when the quoted span appears verbatim in the indexed source text; paraphrased or fabricated quotes fail closed even when paired with a valid source index.

<div class="frcp-demo" id="frcp-demo">
  <div class="frcp-demo__source">
    <div class="frcp-demo__label">Indexed Source · <code>standing_order_p12.txt</code> (Source ID: <code>ord-6a-01</code>)</div>
    <blockquote id="frcp-source-text">Unless otherwise ordered by the Court, all opposition briefs to noticed motions shall be filed and served no later than fourteen (14) calendar days after service of the moving papers, computed in accordance with Federal Rule of Civil Procedure 6(a)(1). When the final day falls on a Saturday, Sunday, or legal holiday, the filing period continues to run until the end of the next day that is not a Saturday, Sunday, or legal holiday.</blockquote>
  </div>

  <div class="frcp-demo__presets" role="group" aria-label="Verifier test cases">
    <button type="button" class="btn frcp-preset" data-case="valid">1. Verbatim quote (Pass)</button>
    <button type="button" class="btn frcp-preset" data-case="bypass">2. Plausible paraphrase + valid ID (Blocked)</button>
    <button type="button" class="btn frcp-preset" data-case="unsupported">3. Out-of-scope deadline guess (Refused)</button>
  </div>

  <label class="frcp-demo__field">
    <span>Candidate model quote</span>
    <textarea id="frcp-quote-input" rows="2">no later than fourteen (14) calendar days after service of the moving papers</textarea>
  </label>

  <div class="frcp-demo__actions">
    <button type="button" class="btn btn--primary" id="frcp-verify-btn">Run fail-closed verifier</button>
    <span class="frcp-demo__meta">Source ID: <code>ord-6a-01</code></span>
  </div>

  <div class="frcp-demo__result" id="frcp-result" aria-live="polite"></div>
</div>

<style>
.frcp-demo { border: 1px solid currentColor; border-opacity: 0.2; padding: 1.25rem; margin: 1.5rem 0; border-radius: 6px; }
.frcp-demo__label { font-size: 0.85rem; opacity: 0.8; margin-bottom: 0.5rem; }
.frcp-demo__source blockquote { margin: 0 0 1rem; padding-left: 0.9rem; border-left: 3px solid currentColor; font-size: 0.95rem; line-height: 1.55; }
.frcp-demo__presets { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem; }
.frcp-demo__presets .btn { font-size: 0.85rem; padding: 0.35rem 0.7rem; cursor: pointer; }
.frcp-demo__field { display: block; margin-bottom: 0.85rem; }
.frcp-demo__field span { display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.35rem; }
.frcp-demo__field textarea { width: 100%; font: inherit; font-size: 0.92rem; padding: 0.6rem; border: 1px solid currentColor; border-radius: 4px; background: transparent; color: inherit; }
.frcp-demo__actions { display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }
.frcp-demo__result { padding: 0.85rem 1rem; border-radius: 4px; font-size: 0.92rem; line-height: 1.5; border-left: 4px solid currentColor; }
.frcp-demo__result--pass { background: rgba(34, 197, 94, 0.12); border-left-color: #16a34a; }
.frcp-demo__result--fail { background: rgba(239, 68, 68, 0.12); border-left-color: #dc2626; }
</style>

<script>
(function () {
  const presets = {
    valid: "no later than fourteen (14) calendar days after service of the moving papers",
    bypass: "all opposition briefs must be submitted within fourteen (14) business days of service",
    unsupported: "reply briefs are due seven (7) calendar days prior to the noticed hearing date"
  };
  const norm = (s) => s.replace(/\s+/g, " ").trim();
  const srcEl = document.getElementById("frcp-source-text");
  const inputEl = document.getElementById("frcp-quote-input");
  const outEl = document.getElementById("frcp-result");

  function verify() {
    const source = norm(srcEl.textContent);
    const quote = norm(inputEl.value);
    if (!quote || quote.length < 12) {
      outEl.className = "frcp-demo__result frcp-demo__result--fail";
      outEl.innerHTML = "<strong>FAIL-CLOSED REFUSAL (EMPTY_OR_SHORT_SPAN):</strong> No claim rendered. Verifier requires a verbatim span of at least 12 characters present in <code>ord-6a-01</code>.";
      return;
    }
    const idx = source.indexOf(quote);
    if (idx !== -1) {
      outEl.className = "frcp-demo__result frcp-demo__result--pass";
      outEl.innerHTML = "<strong>VERIFIED · CLAIM RENDERED:</strong> Exact substring match confirmed in <code>ord-6a-01</code> at char offset <code>" + idx + "–" + (idx + quote.length) + "</code>. Safe to stream to lawyer.";
    } else {
      outEl.className = "frcp-demo__result frcp-demo__result--fail";
      outEl.innerHTML = "<strong>FAIL-CLOSED REFUSAL (SUBSTRING_MISMATCH):</strong> Blocked despite valid source index <code>ord-6a-01</code>. Quoted text does not appear verbatim in the filed order; returning refusal instead of an unverified deadline.";
    }
  }

  document.querySelectorAll(".frcp-preset").forEach((btn) => {
    btn.addEventListener("click", () => {
      inputEl.value = presets[btn.dataset.case];
      verify();
    });
  });
  document.getElementById("frcp-verify-btn").addEventListener("click", verify);
  verify();
})();
</script>
