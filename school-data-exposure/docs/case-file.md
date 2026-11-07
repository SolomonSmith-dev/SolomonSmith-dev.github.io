# Case file: CSUSB student data surface (provisional)

**Claim standard:** only Documented/Verified findings are treated as facts below.  
**Active gates:** DI-01 provisional; DI-15 narrative not locked.

## 1. Executive summary

CSUSB publishes FERPA and student-records policies and a website Privacy and Security Notice. The same public web also documents Canvas (Instructure), myCoyote, DUO MFA, and Canvas learning apps including Turnitin and Respondus LockDown Browser/Monitor (webcam proctoring). The Privacy Notice names Google Analytics and vendor categories (including education management and marketing) but does not present a student-facing named processor inventory for the LMS stack. The abuse risk is opacity + high-sensitivity monitoring inside course workflows, not the mere existence of an LMS.

## 2. How we know

- Public page ingest with URL, retrieval timestamp, and SHA-256 (`evidence/sources/`)
- No unauthorized access
- Own-account telemetry audit not yet run (blocked on DI-10)

## 3. System inventory (documented)

- Public Sites + Google Analytics
- myCoyote portal / mobile
- DUO MFA
- Canvas @ csusb.instructure.com (SAML)
- Turnitin, Respondus Monitor, Zoom via Canvas Learning Apps
- Coyote OneCard, campus WiFi docs
- Registrar / records policies

## 4. Priority findings

- FIND-006 Google Analytics + cookies/clear gifs (S2)
- FIND-007 Privacy Notice scope gap vs LMS stack (S2)
- FIND-008 Vendor sharing categories without named inventory (S3)
- FIND-009 Canvas/Instructure LMS (S1)
- FIND-010 Respondus webcam proctoring + Turnitin (S3)
- FIND-011 myCoyote + DUO identity linkage (S1)

## 5. Recommendations (schools)

1. Publish a living student-data processor list.
2. Link LMS/app privacy addenda from login pages.
3. Require written notice + retention limits for webcam proctoring.
4. Separate marketing processors from education-record processors in notices.

## 6. Open questions

- What exact trackers fire inside authenticated Canvas/myCoyote sessions?
- Retention for Respondus Monitor recordings?
- Full DPA set for learning apps?

## 7. Decision log pointer

See `decisions/index.json` and the Methods page on the site.
