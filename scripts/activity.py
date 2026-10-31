#!/usr/bin/env python3
"""Build one week of GitHub activity for the portfolio.

Writes _data/activity.json (the week just built) and upserts that week into
_data/activity_log.json (newest first). Every value comes from the GitHub REST
API; nothing is summarized or rewritten.

Private repos are reduced to counts unless listed in private_named in
.github/activity-config.json. Their names, commit messages and PR titles never
reach the output.

Usage: GH_TOKEN=... python3 scripts/activity.py [--week-start YYYY-MM-DD]
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / ".github" / "activity-config.json"
LATEST = ROOT / "_data" / "activity.json"
LOG = ROOT / "_data" / "activity_log.json"
API = "https://api.github.com"
MAX_MESSAGES = 5


def get(path, token):
    """GET one API path, following Link pagination. Returns a list or dict."""
    url = path if path.startswith("http") else API + path
    out = None
    while url:
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.load(resp)
            link = resp.headers.get("Link", "")
        if not isinstance(body, list):
            return body
        out = (out or []) + body
        url = next((p.split(";")[0].strip("<> ") for p in link.split(",")
                    if 'rel="next"' in p), None)
    return out or []


def parse_ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")) if value else None


def last_full_week(tz):
    today = datetime.now(tz).date()
    return today - timedelta(days=today.weekday() + 7)


def list_repos(user, token):
    """Owned, non-fork repos. A PAT for the user also returns private ones."""
    try:
        if get("/user", token).get("login") == user:
            repos = get("/user/repos?affiliation=owner&per_page=100", token)
        else:
            raise PermissionError
    except (urllib.error.HTTPError, PermissionError):
        repos = get(f"/users/{user}/repos?type=owner&per_page=100", token)
    return [r for r in repos if r["owner"]["login"] == user and not r["fork"]]


def repo_activity(repo, user, since, until, token):
    full = repo["full_name"]
    window = f"since={since.isoformat()}&until={until.isoformat()}"
    try:
        commits = get(f"/repos/{full}/commits?author={user}&{window}&per_page=100", token)
    except urllib.error.HTTPError as err:
        if err.code != 409:  # 409 = empty repository
            raise
        commits = []

    prs = []
    for pr in get(f"/repos/{full}/pulls?state=closed&sort=updated&direction=desc&per_page=100", token):
        merged = parse_ts(pr.get("merged_at"))
        if merged and since <= merged < until and pr["user"]["login"] == user:
            prs.append({"number": pr["number"], "title": pr["title"], "url": pr["html_url"]})

    releases = []
    for rel in get(f"/repos/{full}/releases?per_page=30", token):
        published = parse_ts(rel.get("published_at"))
        if published and since <= published < until and not rel["draft"]:
            releases.append({"tag": rel["tag_name"], "name": rel["name"] or rel["tag_name"],
                             "url": rel["html_url"]})

    messages = [c["commit"]["message"].splitlines()[0] for c in commits]
    # Merge commits and squash commits ("... (#12)") repeat what the PR list shows.
    pr_suffixes = tuple(f"(#{p['number']})" for p in prs)
    messages = [m for m in messages
                if not m.startswith("Merge ") and not (pr_suffixes and m.endswith(pr_suffixes))]
    messages = messages[:MAX_MESSAGES]
    created = parse_ts(repo["created_at"])
    return {
        "name": repo["name"],
        "url": repo["html_url"],
        "new": since <= created < until,
        "commits": len(commits),
        "commit_messages": messages,
        "prs": sorted(prs, key=lambda p: p["number"]),
        "releases": releases,
    }


def build_week(week_start, config, token):
    tz = ZoneInfo(config["timezone"])
    since = datetime.combine(week_start, time(), tz).astimezone(timezone.utc)
    # Resolve each local Monday separately so DST weeks can span 167 or 169 hours.
    week_end = week_start + timedelta(days=7)
    until = datetime.combine(week_end, time(), tz).astimezone(timezone.utc)
    user = config["user"]
    named = set(config.get("private_named", []))
    exclude = set(config.get("exclude", []))

    public, private, hidden_names = [], [], []
    for repo in list_repos(user, token):
        if repo["name"] in exclude:
            continue
        pushed = parse_ts(repo.get("pushed_at"))
        if pushed and pushed < since and parse_ts(repo["created_at"]) < since:
            # Nothing pushed since the window opened: no commits, merges or tags.
            continue
        act = repo_activity(repo, user, since, until, token)
        if not (act["commits"] or act["prs"] or act["releases"] or act["new"]):
            continue
        if repo["private"] and repo["name"] not in named:
            private.append(act)
            hidden_names.append(repo["name"])
        else:
            if repo["private"]:
                act["url"] = None  # named, but the link would 404 for visitors
            public.append(act)

    public.sort(key=lambda r: (-r["commits"], r["name"].lower()))
    anon = None
    if private:
        anon = {
            "repos": len(private),
            "commits": sum(r["commits"] for r in private),
            "prs": sum(len(r["prs"]) for r in private),
            "releases": sum(len(r["releases"]) for r in private),
            "new_repos": sum(r["new"] for r in private),
        }
    everything = public + private
    week = {
        "week_start": week_start.isoformat(),
        "week_end": (week_start + timedelta(days=6)).isoformat(),
        "repos": public,
        "private": anon,
        "totals": {
            "repos": len(everything),
            "commits": sum(r["commits"] for r in everything),
            "prs": sum(len(r["prs"]) for r in everything),
            "releases": sum(len(r["releases"]) for r in everything),
            "new_repos": sum(r["new"] for r in everything),
        },
    }
    assert_no_leak(week, hidden_names)
    return week


def assert_no_leak(week, hidden_names):
    """Fail the run if an anonymized repo shows up as a listed repo or link."""
    hidden = {n.lower() for n in hidden_names}
    listed = {r["name"].lower() for r in week["repos"]}
    links = " ".join(r["url"] or "" for r in week["repos"]).lower()
    leaked = [n for n in hidden if n in listed or f"/{n}" in links]
    if leaked:
        sys.exit(f"refusing to write: anonymized private repo name in output ({len(leaked)} repo(s))")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--week-start", help="Monday of the week to build, YYYY-MM-DD")
    args = parser.parse_args()

    token = os.environ.get("GH_TOKEN") or sys.exit("GH_TOKEN is not set")
    config = json.loads(CONFIG.read_text())
    tz = ZoneInfo(config["timezone"])
    week_start = date.fromisoformat(args.week_start) if args.week_start else last_full_week(tz)
    if week_start.weekday() != 0:
        sys.exit(f"--week-start must be a Monday, got {week_start:%A}")

    week = build_week(week_start, config, token)
    log = json.loads(LOG.read_text()) if LOG.exists() else []
    log = [w for w in log if w["week_start"] != week["week_start"]] + [week]
    log.sort(key=lambda w: w["week_start"], reverse=True)

    LATEST.write_text(json.dumps(log[0], indent=2) + "\n")
    LOG.write_text(json.dumps(log, indent=2) + "\n")
    print(week["week_start"])
    if out := os.environ.get("GITHUB_OUTPUT"):
        with open(out, "a") as fh:
            fh.write(f"week_start={week['week_start']}\n")


if __name__ == "__main__":
    main()
