# School Data Exposure — Master Plan

> Provisional defaults are in force until Decision Interview #1 is confirmed by Solomon.

## Rule

Decision interviews always before moving forward past a major gate.

## Provisional DI-1 defaults

- **1_target:** `CSUSB (California State University, San Bernardino)`
- **2_thesis:** `Vendors + LMS / campus systems collect and share student data beyond clear educational necessity; policy theater vs practice`
- **3_evidence:** `Public docs + user-visible behavior on Solomon's own student accounts only`
- **4_legal:** `Strictly public-source + own-account audit; no unauthorized access`
- **5_deliverable:** `Standalone exposé site + evidence pipeline + portfolio project page`
- **6_tone:** `Technical audit with journalistic receipts`
- **7_audience:** `Primary: students/parents; secondary: hiring managers + policymakers`
- **8_constraints:** `{"no_unauthorized_access": true, "no_doxxing": true, "name_vendors_if_public": true, "name_school_publicly": true}`
- **9_complete_means:** `Working product with real evidence for one school, then reusable framework`
- **10_next:** `Full 20-task / 20-step plan, then evidence intake`

## 10 completion subtasks

### C01: Legal charter locked

- Requires: T01, DI-2
- Done when: decisions/DI-02-legal-charter.json status=locked and charter.md exists

### C02: All decision interviews recorded through current gate

- Requires: T02
- Done when: scripts/validate_decisions.py exits 0 for required DIs

### C03: Public policy corpus ingested

- Requires: T05, T12
- Done when: >= 8 evidence/sources records with hashes

### C04: Vendor inventory publishable

- Requires: T06, DI-7
- Done when: vendor map JSON lists classified vendors with sources

### C05: Data-flow map with confirmed edges

- Requires: T07, DI-8
- Done when: graph JSON has confirmed edges citing evidence IDs

### C06: Minimum verified findings set

- Requires: T13, DI-14
- Done when: >= 5 findings at Documented or Verified with citations

### C07: Public site builds and serves

- Requires: T15, T16
- Done when: web/index.html serves locally; core routes present

### C08: Redaction and secrets QA passed

- Requires: T18, DI-19
- Done when: verification report shows zero secrets and redaction checklist complete

### C09: Student toolkit shipped

- Requires: T17, DI-18
- Done when: toolkit checklists + request templates linked from site

### C10: Launch-ready demo with decision log

- Requires: T19, DI-20
- Done when: v1.0 tag or release candidate + methods page shows full decision log

## 20 primary tasks

1. [T01: Mission, legal charter, and non-negotiables](T01.md) — gate `DI-2 Legal Charter`
1. [T02: Decision interview system and gate log](T02.md) — gate `DI-3 Gate Map`
1. [T03: Target school profile and system inventory](T03.md) — gate `DI-4 Target Confirmation`
1. [T04: Harm model and stakeholder map](T04.md) — gate `DI-5 Harm Framing`
1. [T05: Public policy and notice corpus](T05.md) — gate `DI-6 Corpus Scope`
1. [T06: EdTech vendor inventory](T06.md) — gate `DI-7 Vendor Naming`
1. [T07: Data-flow mapping](T07.md) — gate `DI-8 Map Publish`
1. [T08: FERPA / CCPA / CPRA gap analysis](T08.md) — gate `DI-9 Legal Framing`
1. [T09: Own-account LMS / portal telemetry audit](T09.md) — gate `DI-10 Own-Account Audit`
1. [T10: Identity, SSO, and session surveillance surface](T10.md) — gate `DI-11 Identity Publish`
1. [T11: Public records / CPRA request pack](T11.md) — gate `DI-12 Request Send`
1. [T12: Evidence intake pipeline](T12.md) — gate `DI-13 Pipeline Freeze`
1. [T13: Finding taxonomy and severity rubric application](T13.md) — gate `DI-14 Finding Bar`
1. [T14: Case file builder](T14.md) — gate `DI-15 Narrative`
1. [T15: Public exposé web surface](T15.md) — gate `DI-16 Site Launch Shape`
1. [T16: Interactive evidence map](T16.md) — gate `DI-17 Map UX`
1. [T17: Student self-audit toolkit](T17.md) — gate `DI-18 Toolkit Scope`
1. [T18: Verification, redaction, and challenge QA](T18.md) — gate `DI-19 Publish Gate`
1. [T19: Portfolio integration and launch](T19.md) — gate `DI-20 Launch`
1. [T20: Maintenance, rebuttals, and multi-school expansion](T20.md) — gate `DI-21 Expansion`

