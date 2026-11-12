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

Try the citation gate with a public rule excerpt. This standalone illustration runs entirely in your browser, with no model, API, or production CourtRules code. It verifies quoted text only, not legal applicability or a calculated deadline.

<div class="frcp-demo" id="frcp-demo">
  <div class="frcp-demo__source">
    <p class="frcp-demo__label">Source <code>frcp-6a-1b</code> · <a href="https://www.law.cornell.edu/rules/frcp/rule_6">FRCP 6(a)(1)(B)</a></p>
    <blockquote id="frcp-source-text">count every day, including intermediate Saturdays, Sundays, and legal holidays;</blockquote>
    <p class="frcp-demo__meta">Excerpt for periods stated in days or a longer unit. This excerpt does not establish a motion's filing deadline.</p>
  </div>
  <div class="frcp-demo__presets" role="group" aria-label="Verifier test cases">
    <button type="button" class="btn frcp-preset" data-case="valid">Verbatim quote</button>
    <button type="button" class="btn frcp-preset" data-case="bypass">Paraphrase + valid ID</button>
    <button type="button" class="btn frcp-preset" data-case="unsupported">Unsupported deadline</button>
  </div>
  <label class="frcp-demo__field" for="frcp-source-id">Candidate source ID</label>
  <input id="frcp-source-id" value="frcp-6a-1b" spellcheck="false" autocomplete="off">
  <label class="frcp-demo__field" for="frcp-quote-input">Candidate model quote</label>
  <textarea id="frcp-quote-input" rows="3" aria-describedby="frcp-policy">count every day, including intermediate Saturdays, Sundays, and legal holidays;</textarea>
  <p id="frcp-policy" class="frcp-demo__meta">Exact, case-sensitive text only. Empty quotes and unknown source IDs are refused. A valid ID alone cannot pass.</p>
  <div class="frcp-demo__actions">
    <button type="button" class="btn btn--primary" id="frcp-verify-btn">Verify quote</button>
  </div>
  <div class="frcp-demo__result" id="frcp-result" role="status" aria-live="polite" aria-atomic="true">Not checked. Choose a test case or verify the quote.</div>
  <noscript>Enable JavaScript to run this local demo. No quote has been verified.</noscript>
</div>

<script>
(function () {
  "use strict";
  const root = document.getElementById("frcp-demo");
  const sourceText = document.getElementById("frcp-source-text").textContent;
  const sources = new Map([["frcp-6a-1b", sourceText]]);
  const presets = {
    valid: sourceText,
    bypass: "Count all days, including weekends and legal holidays.",
    unsupported: "Opposition briefs are due fourteen days after service."
  };
  const quoteInput = document.getElementById("frcp-quote-input");
  const sourceInput = document.getElementById("frcp-source-id");
  const result = document.getElementById("frcp-result");

  function show(state, message) {
    result.dataset.state = state;
    result.textContent = message;
  }

  function verify() {
    const source = sources.get(sourceInput.value);
    const quote = quoteInput.value;
    if (source === undefined) {
      show("refused", "REFUSED: Unknown source ID. No verified quote rendered.");
    } else if (!quote.trim()) {
      show("refused", "REFUSED: Empty quote. No verified quote rendered.");
    } else if (source.includes(quote)) {
      const offset = source.indexOf(quote);
      show("pass", "PASS: Exact quote found at offset " + offset +
        ". Verified quote: “" + quote + "” Text match only; no deadline validated.");
    } else if (quote === presets.unsupported) {
      show("refused", "REFUSED: The deadline guess is absent from this source. No verified quote rendered.");
    } else {
      show("blocked", "BLOCKED: Valid source ID, but the quote is not verbatim. No verified quote rendered.");
    }
  }

  root.querySelectorAll(".frcp-preset").forEach(function (button) {
    button.addEventListener("click", function () {
      sourceInput.value = "frcp-6a-1b";
      quoteInput.value = presets[button.dataset.case];
      verify();
    });
  });
  [quoteInput, sourceInput].forEach(function (input) {
    input.addEventListener("input", function () {
      show("pending", "Not checked. Input changed; verify the quote again.");
    });
  });
  document.getElementById("frcp-verify-btn").addEventListener("click", verify);
})();
</script>
