#!/usr/bin/env python3
"""Check critical live portfolio URLs."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path

URLS = [
    "https://solomonsmith.dev/",
    "https://solomonsmith.dev/about/",
    "https://solomonsmith.dev/projects/",
    "https://solomonsmith.dev/resume/",
    "https://solomonsmith.dev/blog/",
    "https://solomonsmith.dev/log/",
    "https://solomonsmith.dev/card/",
    "https://solomonsmith.dev/assets/resume/SolomonSmithResume.pdf",
    "https://solomonsmith.dev/projects/courtrules/",
    "https://solomonsmith.dev/projects/arda/",
    "https://solomonsmith.dev/projects/soc-triage-ai/",
    "https://solomonsmith.dev/projects/sentinel/",
    "https://solomonsmith.dev/projects/phishguard/",
    "https://solomonsmith.dev/projects/docmind/",
    "https://solomonsmith.dev/projects/agentic-engineering-os/",
    "https://courtrules.app/",
    "https://github.com/SolomonSmith-dev/arda",
    "https://github.com/SolomonSmith-dev",
    "https://linkedin.com/in/solomonsmithdev",
]


def check(url: str) -> dict:
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "hire-ready-link-qa/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"url": url, "status": resp.status, "final": resp.geturl(), "ok": 200 <= resp.status < 400}
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "final": url, "ok": False, "error": str(e)}
    except Exception as e:  # noqa: BLE001
        return {"url": url, "status": None, "final": url, "ok": False, "error": str(e)}


def main() -> int:
    rows = [check(u) for u in URLS]
    out = Path(__file__).resolve().parents[1] / "audit" / "link-qa.json"
    out.write_text(json.dumps({"results": rows}, indent=2) + "\n")
    bad = [r for r in rows if not r["ok"]]
    md = ["# Link QA", "", "| URL | Status | OK |", "| --- | --- | --- |"]
    for r in rows:
        md.append(f"| `{r['url']}` | {r.get('status')} | {'yes' if r['ok'] else 'NO'} |")
    if bad:
        md += ["", "## Failures", ""]
        for r in bad:
            md.append(f"- {r['url']}: {r.get('error') or r.get('status')}")
    (out.with_suffix(".md")).write_text("\n".join(md) + "\n")
    print(json.dumps({"checked": len(rows), "failures": len(bad)}, indent=2))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
