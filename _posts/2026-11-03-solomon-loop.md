---
layout: post
title: "SolomonLoop: risk before code, challenge before merge"
date: 2026-11-03 00:30:00 -0800
categories: projects ai tooling
description: "Why I built SolomonLoop, a Claude Code plugin that makes subagents write risk before code, cite fetched sources, verify with commands, and survive a reviewer that tries to break the work."
---


The first time I ran a plan through subagents, the reviews came back clean. Every task, every report, zero findings. Then I read the diffs myself and started finding what the reviews had not: a check missing here, an edge value nobody had tried there. The reviewer had read the code. It had not tried to break the code. Those are different jobs.

I spent ten years in kitchens before I wrote software, dishwasher to head chef. The rule that kept a line alive on a Friday night was mise en place: everything prepped, labeled and in reach before the first ticket prints. Nobody figures out the sauce during service. SolomonLoop is that rule applied to coding agents. The risk gets written before the code. The review tries to break the claim instead of reading it.

## What it is

SolomonLoop is a Claude Code plugin. Nine steps, three loops.

The steps: define, research, assess risk, implement, verify, challenge, learn, validate, promote.

The loops. Delivery finishes real work against observable acceptance criteria. Learning finds why something failed and proposes a testable fix. Optimization compares a proposed fix against a frozen baseline in isolated copies and keeps only clear wins.

It first ran on top of obra/superpowers, inside its subagent-driven-development skill, and it still defers to that dispatcher when the skill is loaded. Standalone, the plugin ships its own `/solomon-loop:setup` and `/solomon-loop:run` commands and works with vanilla Claude Code.

## Why each step exists

Each step is there because I watched an agent skip it and paid for it.

**Define.** The dispatch carries the acceptance check as a command plus its expected output, not a sentence. Catches: "task complete" with no way to tell whether it is.

**Research.** Every library or external API touched gets a Sources section: URL and date, fetched this session. Catches: an agent writing against an SDK method that was renamed two versions ago, from memory.

**Assess risk.** The implementer writes a Risk section before the first line of code, naming which Review Focus items and security surfaces the task touches and the test that covers each. "None" needs a reason. Catches: the ownership check nobody thought about because the task said "add endpoint" and not "add endpoint that another tenant can reach."

**Implement.** Test-first, real integration over mocks. A mock is allowed only at a boundary named in the plan's loop-lens file. Catches: a test suite that passes because the database was a dictionary.

**Verify.** Every verify command that exists by this task gets run, with the command and the tail of its output pasted. Catches: "tests pass" when the agent ran one file and the suite had three others failing.

**Challenge.** The reviewer makes one concrete break attempt per named risk, and per risk the implementer missed. Each attempt is reported as target, attack, result: HELD or BROKE with file and line. The reviewer may write one throwaway test to do it and must delete it. Catches: the review that re-reads the diff and calls it good.

**Learn.** Every Critical or Important finding becomes one lesson line: finding class, why the worker missed it, a testable improvement. Catches: fixing the same class of bug in task 4 and task 7 and never noticing it was the same class.

**Validate.** A lesson is a candidate until the same finding class recurs in a second task group. One occurrence proves nothing. Catches: rewriting the process after every single finding until the brief is 40 rules long and nobody reads it.

**Promote.** Supported lessons are shown to the human with the exact proposed edit and where it goes. Only approved ones land. Catches: the agent quietly editing its own rules mid-run.

## What changed

Before the loop, a reviewer report was a paragraph that said the code looked fine. After, it is a table of attempts. On the example run shipped in the repo (a small todo API), the reviewer's Challenge section produced one BROKE, with a file and line, and the implementer fixed it in a second round. The report is in `examples/todo-api/`, produced by the run, not written by hand. Without the Challenge step that report would have said "looks good."

The second change is slower to notice. Lessons that recur get promoted into the loop-lens defaults, so the next plan starts with the failure modes the last plan found. The process gets better on evidence, not on vibes. Passing tests alone does not prove the workflow is improving; recurrence counts do.

I do not pretend this is finished. The optimization loop needs fixed eval tasks and A/B worktrees, and I have run it by hand, not as a command. The lesson table is a markdown file, not a database. What exists today is the delivery and learning loops, packaged, installable, with a real run as the example.

## Install

```
/plugin marketplace add SolomonSmith-dev/solomon-loop
/plugin install solomon-loop@solomon-loop
```

Then, on any plan file:

```
/solomon-loop:setup docs/plans/your-plan.md
/solomon-loop:run docs/plans/your-plan.md
```

MIT. Repo: https://github.com/SolomonSmith-dev/solomon-loop

## What I want from you

Run it on one plan. Open an issue with your reviewer's BROKE lines, the Risk section that missed them, and the lesson line the reviewer wrote. That is the data the loop needs: finding classes that recur across projects I have never seen. A BROKE on your codebase is worth more to me than a star.

Issues and PRs at the repo. PRs that change the rules follow the loop's own promote rule: cite the finding class and two task groups where it recurred. Docs and packaging PRs need no evidence.

Solomon Smith, CS senior at CSUSB. Available on GitHub at SolomonSmith-dev.
