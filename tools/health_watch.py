#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The repository's health watch: every workflow's runs of the last hour, read from GitHub, and an alarm when one goes wrong.

24 October 2026: the conductor failed in seconds and each failed conductor started the next, about one every 15 seconds from
07:05 UTC, more than 1,600 runs, and no benchmark started for eight hours before anyone read it. This watch reads every
workflow's runs started in the last hour (`.github/workflows/health.yml`, every 15 minutes) and raises an alarm when

  failing     a workflow failed FAIL_LIMIT times or more in the hour (a fault that repeats is a fault, never a flake)
  runaway     a workflow started RUN_LIMIT runs or more in the hour (a chain that starts itself, or a trigger that loops)

The alarm is the watch's own run going red with the reason in its summary, and one open issue titled HEALTH_TITLE updated
with the reason, so it reaches the owner's notifications. A workflow named in QUIET (its runs are many by design and never
fail together) is read with its own limits. Nothing here starts, stops or cancels a run.

  python3 tools/health_watch.py              read the last hour; exit 1 and print the alarms when there are any
  python3 tools/health_watch.py --json F     the same from a file of runs (GitHub's workflow_runs list), for the tests
"""
from __future__ import annotations

import datetime
import json
import os
import sys
import urllib.request
from collections import defaultdict

FAIL_LIMIT = 4                # failures of one workflow in one hour
RUN_LIMIT = 60                # runs of one workflow started in one hour
QUIET = {"six": 400, "six-kube": 400, "archive-run": 120}   # workflows whose runs are many by design: their own run limits
HEALTH_TITLE = "Health watch: a workflow is failing or running away"
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[1]))
from tools.repo import NAME as REPO  # noqa: E402  (the repository's name, written once)


def api(path, method="GET", data=None):
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    req = urllib.request.Request(f"https://api.github.com/{path}", method=method,
                                 data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                                          "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read() or b"{}")


def last_hour(now=None):
    """Every run started in the last hour, newest first (at most ten pages of 100)."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    since = (now - datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    for page in range(1, 11):
        rs = api(f"repos/{REPO}/actions/runs?created=>={since}&per_page=100&page={page}").get("workflow_runs", [])
        out += rs
        if len(rs) < 100:
            break
    return out


def alarms(runs):
    """The alarms the runs of one hour raise: [(workflow, what, count)], the worst first."""
    started, failed = defaultdict(int), defaultdict(int)
    for r in runs:
        name = r.get("name") or "?"
        started[name] += 1
        failed[name] += r.get("conclusion") == "failure"
    out = []
    for name in sorted(started):
        if failed[name] >= FAIL_LIMIT:
            out.append((name, "failing", failed[name]))
        if started[name] >= QUIET.get(name, RUN_LIMIT):
            out.append((name, "runaway", started[name]))
    return sorted(out, key=lambda a: -a[2])


def sentence(a):
    name, what, n = a
    return (f"{name}: {n} failures in the last hour (the limit is {FAIL_LIMIT})" if what == "failing" else
            f"{name}: {n} runs started in the last hour (the limit is {QUIET.get(name, RUN_LIMIT)})")


def notify(found):
    """One open issue titled HEALTH_TITLE carries the alarms: opened when none is open, commented on when one is."""
    body = ("The health watch (`tools/health_watch.py`) read the last hour of GitHub Actions and found:\n\n"
            + "\n".join(f"- {sentence(a)}" for a in found) + "\n\nNothing was started, stopped or cancelled by the watch.")
    issues = api(f"repos/{REPO}/issues?state=open&per_page=100")
    mine = next((i for i in issues if i.get("title") == HEALTH_TITLE and "pull_request" not in i), None)
    if mine:
        api(f"repos/{REPO}/issues/{mine['number']}/comments", "POST", {"body": body})
    else:
        api(f"repos/{REPO}/issues", "POST", {"title": HEALTH_TITLE, "body": body})


def main(argv):
    runs = json.load(open(argv[argv.index("--json") + 1])) if "--json" in argv else last_hour()
    found = alarms(runs.get("workflow_runs", runs) if isinstance(runs, dict) else runs)
    if not found:
        print(f"health: {len(runs)} runs in the last hour, no workflow failing or running away")
        return 0
    for a in found:
        print("ALARM  " + sentence(a))
    if "--notify" in argv:
        notify(found)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
