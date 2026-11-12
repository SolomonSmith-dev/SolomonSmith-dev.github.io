---
title: "PhishGuard"
eyebrow: "Project &middot; PhishGuard"
heading: "A phishing URL classifier I had to break before I could trust it."
lede: "A LightGBM URL classifier served by FastAPI through ONNX Runtime. The public dataset's labels were upside down and every legitimate URL in it began with https://www. The model that ships is the one that still passes the leakage tests after those shortcuts were removed."
description: "PhishGuard by Solomon Smith: LightGBM phishing URL classifier, test AUC 0.9943 and 1.54% false positives on Tranco top-5,000, with the PhiUSIIL dataset leakage found, fixed and locked by regression tests."
order: 5
status: "Active"
stack: [Python, LightGBM, scikit-learn, ONNX Runtime, FastAPI, Docker, PostgreSQL]
links:
  - label: "Source"
    url: "https://github.com/SolomonSmith-dev/phishguard"
---

## What it does

Hand it a URL and `POST /predict` returns a calibrated phishing probability from 47 numeric URL features plus the TLD. Predictions log to Postgres with credentials redacted. The HTML and screenshot models are scaffolded, not trained; the service answers on the URL alone today, and the README says so.

## Why it is hard

PhiUSIIL (about 235k URLs) hands a URL-only model an AUC above 0.99 on its own holdout. Three things made that number worthless, and hand-written smoke tests caught all three. Raw `label=1` meant legitimate, so obvious phishing URLs scored 0.0. Every legitimate URL was `https://www.` with no path, so the model was learning "has www, no path." And even after those fixes, `has_https` carried 47.6% of model gain.

The fixes are code and tests, not a footnote. Label polarity is normalized in the loader and locked by `tests/test_label_polarity.py`. URLs are canonicalized at train and serve time. v0.2 drops `has_https`, `has_http` and the length features, and `tests/test_no_leakage.py` enforces a 50% single-feature cap and an 80% top-3 cap. The leaky v0.1 model is kept as an xfail regression marker.

## Evidence

| Number | Reproduce with |
|---|---|
| Test AUC 0.9943 | `reports/url_baseline_v0_2.txt`; the `make eval` rerun in `reports/evaluation_v0_2.md` rounds to 0.9942 |
| AP 0.9948, F1 0.9782, Brier 0.0157 | `reports/url_baseline_v0_2.txt` |
| 1.54% false positives on Tranco top-5,000 at threshold 0.7 | `reports/evaluation_v0_2.md`; 2.52% at 0.5, 0.90% at 0.9. Tranco was never trained on |
| Top feature gain 27.16% (`subdomain_depth`), top-3 57.9% | `reports/url_baseline_v0_2.txt` |
| ONNX output within 8.9e-8 of the native booster over all 23,537 test URLs and 5,000 Tranco URLs | `reports/url_onnx_2026-11-03.md`, `tests/test_onnx_serving.py` |
| 35 test functions, 1 xfail on purpose | `grep -c "^def test_" tests/*.py`; run with `make test` |
{: .evidence}

ONNX Runtime is the production serving path, not a scaffold: `POST /predict` runs the exported LightGBM graph in an `onnxruntime.InferenceSession`, then applies the isotonic calibrator in Python (`src/phishguard/serving/url_onnx.py`). The export restores the float64 split thresholds the converter rounds to float32, and the parity check above runs on every re-export.

The leakage tests run as a pre-commit hook on every commit (planting an inverted label makes the commit fail) and again in GitHub Actions CI. The before-and-after write-up is `LIMITATIONS.md`.
