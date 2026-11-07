#!/usr/bin/env python3
"""Ingest a public URL into the evidence corpus (metadata only; stores hash of body)."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "evidence" / "sources"


def slugify(url: str) -> str:
    leaf = re.sub(r"[^a-zA-Z0-9]+", "-", url.split("//", 1)[-1])[:60].strip("-").lower()
    return leaf or "source"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--type", default="policy", choices=["policy", "vendor", "news", "record", "other"])
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    SOURCES.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        args.url,
        headers={"User-Agent": "school-data-exposure-research/0.1 (+local; public corpus ingest)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read()
        final_url = resp.geturl()
        content_type = resp.headers.get("Content-Type", "")

    digest = hashlib.sha256(body).hexdigest()
    retrieved = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    eid = f"SRC-{slugify(args.url)[:40]}-{digest[:8]}"
    record = {
        "id": eid,
        "title": args.title,
        "type": args.type,
        "url": args.url,
        "final_url": final_url,
        "retrieved_at": retrieved,
        "content_type": content_type,
        "sha256": digest,
        "bytes": len(body),
        "notes": args.notes,
        "claim_use": "Documented source candidate",
    }
    out = SOURCES / f"{eid}.json"
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"wrote": str(out), "id": eid, "sha256": digest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
