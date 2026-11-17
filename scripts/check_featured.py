#!/usr/bin/env python3
"""Re-derive the Featured numbers and fail when one has drifted.

Reads _data/featured.json. For each `derived` row it runs the `rederive`
command with cwd set to the source repo and CLAIM_REF set to the row's `ref`,
then compares the last non-empty stdout line to `value`. `manual` rows are
listed and never fail.

SECURITY: the data file is trusted input. Every `rederive` string runs in a
shell, so only point --data at a file you wrote or reviewed.

Exit codes: 0 all verified or manual, 1 any drift or error, 2 malformed file.
Standard library only; Python 3.9 compatible.
"""

import argparse
import json
import os
import signal
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ("id", "name", "url", "value", "label", "kind", "repo", "ref",
          "rederive", "public_source", "evidence")
KINDS = ("derived", "manual")


class DataError(Exception):
    pass


def validate(data):
    """Return the list of rows, or raise DataError."""
    if not isinstance(data, dict) or not isinstance(data.get("projects"), list):
        raise DataError("top level must be an object with a 'projects' list")
    seen = set()
    for i, r in enumerate(data["projects"]):
        where = "projects[%d]" % i
        if not isinstance(r, dict):
            raise DataError("%s is not an object" % where)
        for f in FIELDS:
            if f not in r:
                raise DataError("%s missing field '%s'" % (where, f))
            if not isinstance(r[f], str):
                raise DataError("%s field '%s' must be a string" % (where, f))
        if not r["id"]:
            raise DataError("%s has an empty id" % where)
        if r["id"] in seen:
            raise DataError("duplicate id '%s'" % r["id"])
        seen.add(r["id"])
        if r["kind"] not in KINDS:
            raise DataError("%s unknown kind '%s'" % (r["id"], r["kind"]))
        if r["kind"] == "manual":
            if r["rederive"]:
                raise DataError("%s is manual but has a command" % r["id"])
            if not r["evidence"]:
                raise DataError("%s is manual but has no evidence" % r["id"])
        else:
            if not r["rederive"]:
                raise DataError("%s is derived but has no command" % r["id"])
            if not r["repo"] or not r["ref"]:
                raise DataError("%s is derived but has no repo or ref" % r["id"])
    return data["projects"]


def _norm(text):
    return text.strip().replace(",", "")


def same(expected, actual):
    a, b = _norm(expected), _norm(actual)
    try:
        return float(a) == float(b)
    except ValueError:
        return a == b


def _run(command, cwd, ref, timeout):
    env = dict(os.environ, CLAIM_REF=ref)
    proc = subprocess.Popen(command, shell=True, cwd=str(cwd), env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True, start_new_session=True)
    try:
        out, err = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.communicate()
        raise
    return proc.returncode, out, err


def check_row(r, repo_root, timeout):
    res = {"id": r["id"], "name": r["name"], "kind": r["kind"],
           "expected": r["value"], "actual": "", "sha": "", "status": "",
           "detail": ""}
    if r["kind"] == "manual":
        res["status"] = "manual"
        res["detail"] = r["evidence"]
        return res
    repo = Path(repo_root) / r["repo"]
    if not repo.is_dir():
        res.update(status="error", detail="repo not found: %s" % repo)
        return res
    sha = subprocess.run(
        ["git", "rev-parse", "--short", r["ref"] + "^{commit}"], cwd=str(repo),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if sha.returncode != 0:
        res.update(status="error", detail="ref not found: %s" % r["ref"])
        return res
    res["sha"] = sha.stdout.strip()
    try:
        code, out, err = _run(r["rederive"], repo, r["ref"], timeout)
    except subprocess.TimeoutExpired:
        res.update(status="error", detail="timeout after %ss" % timeout)
        return res
    if code != 0:
        tail = err.strip().splitlines()[-1:] or [""]
        res.update(status="error", detail="exit %d %s" % (code, tail[0]))
        return res
    lines = [ln for ln in out.splitlines() if ln.strip()]
    if not lines:
        res.update(status="error", detail="command printed nothing")
        return res
    res["actual"] = lines[-1].strip()
    if same(r["value"], res["actual"]):
        res["status"] = "verified"
    else:
        res["status"] = "drift"
        res["detail"] = "site says %s, command printed %s" % (
            r["value"], res["actual"])
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description="Re-derive Featured numbers.")
    ap.add_argument("--data", default=str(ROOT / "_data" / "featured.json"))
    ap.add_argument("--repo-root", default=os.environ.get(
        "CLAIMS_REPO_ROOT", str(Path.home() / "Projects")))
    ap.add_argument("--json", action="store_true", help="print JSON")
    ap.add_argument("--timeout", type=float, default=60,
                    help="seconds per command (default 60)")
    args = ap.parse_args(argv)

    try:
        rows = validate(json.loads(Path(args.data).read_text()))
    except (OSError, ValueError, DataError) as exc:
        print("malformed data file: %s" % exc, file=sys.stderr)
        return 2

    results = [check_row(r, args.repo_root, args.timeout) for r in rows]
    summary = {k: sum(1 for x in results if x["status"] == k)
               for k in ("verified", "drift", "error", "manual")}
    ok = summary["drift"] == 0 and summary["error"] == 0

    if args.json:
        print(json.dumps({"ok": ok, "summary": summary, "results": results},
                         indent=2))
    else:
        width = max([len(x["id"]) for x in results] + [1])
        for x in results:
            shown = x["actual"] or x["expected"]
            tail = x["detail"] if x["status"] != "verified" else ""
            line = "%-8s %-*s  %-8s %-9s %s" % (
                x["status"], width, x["id"], shown, x["sha"] or "-", tail)
            print(line.rstrip())
        print("%d verified, %d drift, %d error, %d manual" % (
            summary["verified"], summary["drift"], summary["error"],
            summary["manual"]))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
