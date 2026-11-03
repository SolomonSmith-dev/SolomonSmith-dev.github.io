---
title: "agentic-engineering-os"
eyebrow: "Project &middot; agentic-engineering-os"
heading: "Claude Code workers in sandboxed worktrees, and a draft PR only after an independent reviewer approves."
lede: "agent-team runs coding agents in isolated git worktrees, records every tool call in SQLite, re-runs the tests itself, and opens a draft pull request only when a separate reviewer approves the diff."
description: "agentic-engineering-os by Solomon Smith: an orchestrator that runs Claude Code workers in sandboxed worktrees, records every tool call, and gates draft PRs on an independent review. 524 tests, 14 of 15 build steps merged."
order: 6
status: "v0.1.0"
stack: [Python, Typer, SQLite, Claude Code, srt sandbox, GitHub CLI]
links:
  - label: "Source"
    url: "https://github.com/SolomonSmith-dev/agentic-engineering-os"
---

## What it does

`agent-team run --workflow bug-fix` walks a fixed chain: intake, discovery, plan, implementation, test, code review, PR, human decision. Each run owns a git worktree. Workers run under `srt` with no network beyond an allowlist and no read of `.env`, key files or the GitHub credential. `git push` and `gh` stay in the orchestrator's process, so no worker holds the token.

## Why it is hard

An agent's word is a claim, not evidence. The orchestrator re-runs the reproduction command before the fix, runs the tests itself at the reviewed commit, and hands the reviewer the plan, the diff and the test output, never the implementer's transcript. A blocker or major finding turns an approve into changes, and a second changes verdict ends the run blocked at the human decision.

The eval harness has the same rule. Ten tasks carry hidden verifiers that are copied into a fresh export of the arm's final tree only after the arm exits, so no arm can read the answer.

## Evidence

| Number | Reproduce with |
|---|---|
| 524 tests | `uv run pytest --collect-only -q`; CI runs them on Ubuntu and macOS under the real sandbox (`AGENT_TEAM_REQUIRE_SRT=1`) |
| 14 of 15 build steps merged | `docs/ARCHITECTURE.md`, section 11; one PR per step. Step 15 is dogfood on a real team repository |
| 10 eval tasks, 3 arms, $1.00 per cell, $15.00 per eval | `evals/tasks/`; `agent-team eval run` prints the matrix before calling any model |
{: .evidence}

No paid eval has been run yet, so there is no measured result to report, and the Codex reviewer adapter has not met a real Codex. Both gaps are in the README. A tool that checks agents' claims should not make unchecked claims about itself.
