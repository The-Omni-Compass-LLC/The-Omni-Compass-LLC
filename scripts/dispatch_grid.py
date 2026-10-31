#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The free GitHub grid: all seven organisms (the spine, the four realms, the four stacked, the whole tower) at 1, 10, 100
and 500 copies, with nested 1, 10, 100 and 500 paired runs: the ladder of the Python's 500-run Monte Carlo (tools/engine_runs.py),
the founder's order of 25 October. Paid cloud and GPU jobs retain their separate 100-copy/100-run ceiling.
The planner never rents hardware for an oversized free cell: memory/time refusals are listed explicitly.

The conductor (tick) starts the grid and keeps every runner GitHub gives this repository busy without flooding the queue:
it finds which runs of each square are already started (the dispatches named by their squares, plus the manifest of the
first night's runs), and starts the next ones (the 10-run squares of every size first, then 100) until the repository's
queued and running jobs reach what GitHub is running now plus a margin. grid.yml runs it every 15 minutes; the six and
six-kube buttons run it once when started with their defaults. Nothing is started twice: a started run is read back from
its own name. Azure goes first (the founder's order of 13 October): while an Azure run, a grid run's report or the push's
verify waits for a runner, the conductor starts nothing new, so that job is next in GitHub's queue.

Shards are cut from run times measured on the max (12 Oct, work waiting in line, GitHub's own machines) so that no job
nears GitHub's six-hour limit; each shard also stops starting runs at its deadline and hands in every run it finished.

  python3 scripts/dispatch_grid.py plan                 every square, how many of its runs are started, what is left
  python3 scripts/dispatch_grid.py tick [--dry]         start what fits now (GITHUB_TOKEN, or Claude Code's gh api)
  python3 scripts/dispatch_grid.py matrix ...           six.yml's shards for one dispatch (used by the workflow)
  python3 scripts/dispatch_grid.py kube-matrix ...      six-kube.yml's cells for one dispatch (used by the workflow)
"""
from __future__ import annotations

import argparse
import calendar
import contextlib
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results" / "grid_v23" / "DISPATCHED.json"
REPO = os.environ.get("GITHUB_REPOSITORY", "The-Omni-Compass-LLC/The-Omni-Compass-LLC")   # tools/repo.py HOME: the conductor runs from its own fetched copy, alone
SINCE = "2026-10-31T20:00:00Z"  # only this campaign, omni-v23 (the founder's order of 17 October: every fix makes the next version and everything runs again); earlier engines are historical
ENGINE = "omni-v23"                 # the engine whose grid this is (tools/omni_version.py)
SIZES = (1, 10, 100, 500)           # free GitHub only: the ladder of the Python's 500-run Monte Carlo (the founder's order of 25 October)
RUNS = 500                         # nested 1/10/100/500 runs on free GitHub runners
TIERS = (10, 100, 500)              # smaller prefixes first
MAX_JOBS = 250                     # GitHub: at most 256 jobs in one run's matrix (a few kept for the plan and the receipt)
ORGS = ["1", "2", "3", "4", "5", "6", "7"]   # tools/run_scale.py: the four realms, the four stacked, the whole tower, the spine
KUBE = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized",
        "stack", "tower", "spine"]  # tools/run_kil.py names of the same seven, in the same order (5 the four stacked, 6 the
                                   # tower, 7 the spine: the muscles every stack runs on, an organism since 16 October)
LOAD = "line"                      # the founder's order: work waiting in line in every organism (six.yml)

# Seconds per paired run (native then Omni on one seed), measured on the max with work waiting in line (12 Oct): 1 copy
# on GitHub's machines (the night's shards), 10 copies of every organism and 100 copies of the compute realm and the tower
# on a 4-core machine that runs as fast as GitHub's; the other figures are scaled from those (a run grows 9 to 11 times
# per tenfold size). CAL: the calibration run each worker makes once per organism (a native run on the calibration seed).
# MEM: a worker's peak memory (GB). The spine's figures (7) are the distribution realm's scaled by its muscle count (267 of
# 484), a planning estimate until its first shards are measured.
SEC = {1: {"1": 7.2, "2": 6.5, "3": 5.1, "4": 5.0, "5": 28.8, "6": 17.4, "7": 3.0},
       10: {"1": 77, "2": 95, "3": 79, "4": 67, "5": 359, "6": 250, "7": 40},
       100: {"1": 660, "2": 850, "3": 710, "4": 600, "5": 2820, "6": 1780, "7": 350}}
CAL = {1: {o: 2 for o in ORGS}, 10: {o: 15 for o in ORGS},
       100: {"1": 150, "2": 200, "3": 170, "4": 150, "5": 670, "6": 500, "7": 90}}
MEM = {1: {o: 0.2 for o in ORGS}, 10: {o: 0.4 for o in ORGS},
       100: {"1": 0.9, "2": 0.9, "3": 0.9, "4": 0.9, "5": 3.2, "6": 1.8, "7": 0.6}}
# Planning estimates only, extrapolated from the measured 100-copy timings/memory above.
# They are not 500-copy benchmark measurements. Oversized cells remain explicit, never sent to Azure.
for table in (SEC, CAL, MEM):
    table[500] = {o: value * 5 for o, value in table[100].items()}
RUNNER_GB, RUNNER_CPUS = 14.0, 4   # GitHub's machine for a public repository: 4 cores, 16 GB (2 kept for the system)
JOB_S = 4 * 3600                   # a shard's planned work (a single run that needs more gets up to LONG_S)
LONG_S = 5 * 3600
DEADLINE_MIN = 320                 # run_scale starts no run that would end after this; the job is cut at 355 minutes
# with the real cluster inside, the organism steps on the window's clock (240 steps), so the window must be long enough
# for the max's arm to make each step in time (tools/six_kube_report.py marks a repetition more than 5% late OFF THE
# CLOCK): seconds per arm by size, and by organism where the default is too short
KUBE_WINDOW = {1: 960, 10: 960, 100: 1440, 500: 7200}
KUBE_WINDOW_ORG = {(100, "tower"): 2400, (100, "stack"): 3600,
                   (500, "tower"): 12000, (500, "stack"): 18000}
KUBE_BUILD = {1: 1, 10: 1, 100: 8, 500: 40}         # minutes to build the organism (calibration, plants, the max's bone)
# the test rig's protocol with the real cluster inside (scripts/kind_bench.sh), carried in each run's name. Protocol 2 (12
# Oct): the governor at the organism's own CPU priority, never below the rig beside it; its decisions counted inside the
# measured window; kind, kubectl and the metrics-server manifest tried again when a download is refused. Protocol 3 (13
# Oct): the model of the organism on the runner's last core and the kind nodes on the others, the same in both arms; the
# window lengthened (never shortened) from the heavier arm's step timed on that core before either arm. Protocol 4 (18
# Oct): protocol 3 with the served image pulled onto every kind worker before each arm (deploy/kind/prepull.yaml,
# docs/POD_START_WAIT.md), so no pod started inside the window unpacks its image on the host every node shares. The runs of
# earlier protocols are kept as they stand and counted in no square, so every square with the cluster inside is filled on
# protocol 4 alone (no omni-v11 run with the cluster inside had started on protocol 3)
KUBE_PROTOCOL = "4"
MAX_TRIES = 3                      # a repetition whose job failed this many times is started no more (the report lists it)
# the runs that go before the grid: Azure first (the founder's order of 13 October: Kubernetes on Azure is finished first),
# the other clouds when he starts them, the push's verify and the archive of finished runs. While one of them waits for a
# runner (or a grid run's report does), the conductor starts nothing new, so the job that waits is next in GitHub's queue
# instead of behind the grid
# every benchmark run again on the engine that stands (the founder's order of 13 October, night: everything on the newest
# engine), three times each (A, B and C), released by this conductor a few at a time: A of every benchmark first, then B,
# then C, and never while a run that goes first waits for a runner. A workflow's runs started since RERUN_SINCE are read
# back by count, in the queue's own order, so nothing is started twice (a run dispatched by hand counts as started)
RERUNS = ROOT / "scripts" / "reruns.txt"
RERUN_SINCE = "2026-10-31T20:00:00Z"   # omni-v23: every benchmark runs again from a little after the moment the engine landed on main (24 October)
# the kind rig as amended on 18 October (scripts/kind_bench.sh pulls the served image onto every worker before each arm,
# docs/POD_START_WAIT.md): a run of a workflow that builds a kind cluster counts only when its own commit carries the
# pre-puller (RIG_FILE, read from GitHub at the run's head commit), so no table mixes the two rigs and no run is counted on
# the wrong one; its runs on the rig before run to their end (nothing is cancelled) and stay as their own record
RIG_FILE = "deploy/kind/prepull.yaml"
RIG_WORKFLOWS = ("benchmark.yml", "benchmark-reps.yml", "big-organism.yml", "capacity.yml", "kind-addons.yml",
                 "kind-crane.yml", "kind-cruisekube.yml", "kind-godel.yml", "kind-goldilocks.yml", "kind-group.yml",
                 "kind-orchestrators.yml", "robustness.yml")
RERUN_JOBS = 10                    # jobs one rerun is counted as toward the queue's target
# the workflows whose run records the label it was started with (A, B or C): the conductor passes the rerun's own letter
# (19 October; before, a run it started read the workflow's default, A, in its own record)
LABELLED = ("capacity.yml", "kind-crane.yml", "kind-godel.yml", "kind-group.yml", "kind-orchestrators.yml")
RERUN_PER_TICK = 6                 # reruns released at most in one tick
# The clouds, their sets following one another without a hand on the button. Azure first (the founder's order of 13
# October): scripts/azure_queue.txt lists every Azure set in release order, A of every line, then B, then C. A set starts
# when its machine family's queue (its region and machine size, the workflow's own concurrency group) has no run waiting
# or running, one a tick in each queue, and is read back by its run's title since AZURE_SINCE (a cancelled run counts for
# nothing), so nothing is started twice and a set dispatched by hand counts as started. Google Cloud and Amazon carry the
# same four sets at the same settings on the same harness (scripts/google_queue.txt, scripts/amazon_queue.txt; the
# founder's order of 16 October: the Azure run is the measure of the other two), each behind its own switch line
# (switch=on | off): off until that cloud's secrets are in the repository, so nothing is rented before the founder says
AZURE_QUEUE = ROOT / "scripts" / "azure_queue.txt"
AZURE_SINCE = "2026-10-31T20:00:00Z"   # omni-v23: every Azure set runs again on the engine that stands; the sets of earlier engines already
                                       # started run to their end (nothing is cancelled) and stay as their own engine's record, counted in no v23 table
AZURE_WF = "aks-metered.yml"
# The clouds whose cluster a tester builds in the provider's own console and hands over by its kubeconfig (byoc-metered.yml,
# scripts/byoc_paired.sh, docs/BYOC_SETUP.md): the same four sets on the same harness, each queue behind its own switch,
# off until a tester has the cluster, its kubeconfig in KUBECONFIG_<CLOUD> and the founder's word (written, not yet run).
BYOC_WF = "byoc-metered.yml"
BYOC = {"Oracle": "oracle", "DigitalOcean": "digitalocean", "Alibaba Cloud": "alibaba", "Linode": "linode", "IBM Cloud": "ibm"}
CLOUDS = (("Azure", AZURE_WF, AZURE_QUEUE),
          ("Google Cloud", "gke-metered.yml", ROOT / "scripts" / "google_queue.txt"),
          ("Amazon", "eks-metered.yml", ROOT / "scripts" / "amazon_queue.txt"),
          *((name, BYOC_WF, ROOT / "scripts" / f"{key}_queue.txt") for name, key in BYOC.items()))
# A cloud starts a set only after its $0 check passed (.github/workflows/cloud-check.yml: the login, the key's shape, the
# machine type and every quota a set needs; 18 October, when a key cut short and an account on Amazon's Free plan failed
# every set started there at the login, each using up its A or B; Azure since 22 October, after its stored key held, for a
# while on 21 October, a text Azure's login refuses, and a failed set counts as started). The conductor starts a check itself when the cloud
# has none, the last failed CHECK_RETRY_MIN ago or more, or the last pass is CHECK_FRESH_H old; a fix the founder stores is
# so taken up within the hour, and a cloud that cannot rent never uses up a set.
CHECK_WF = "cloud-check.yml"
CHECKS = {"Google Cloud": "google", "Amazon": "amazon", "Azure": "azure", **BYOC}
CHECK_FRESH_H = 24
CHECK_RETRY_MIN = 60
FIRST = ("aks-metered-full.yml", "aks-metered.yml", "big-organism-detached.yml", "big-organism.yml", "cloud-organism.yml", "gke-metered.yml",
         "eks-metered.yml", "byoc-metered.yml", "verify.yml", "archive-run.yml", "peek.yml")


# ------------------------------------------------------------------------------------------------- shard shapes
def shape(size, org):
    """(runs per shard, workers per runner) for a modelled square, or None where it cannot run on GitHub."""
    if MEM[size][org] > RUNNER_GB:
        return None
    workers = max(1, min(RUNNER_CPUS, int(RUNNER_GB // MEM[size][org])))
    cal, sec = CAL[size][org], SEC[size][org]
    budget = JOB_S if cal + sec <= JOB_S else LONG_S
    per_worker = int((budget - cal) // sec)
    if per_worker < 1:
        return None
    return min(RUNS, per_worker * workers), workers


def kube_minutes(size, org, split):
    """Planned minutes of one six-kube job: each arm builds a fresh cluster, builds the organism, warms up and runs its
    window."""
    win = KUBE_WINDOW_ORG.get((size, org), KUBE_WINDOW[size])
    arm = 6 + KUBE_BUILD[size] + 2 + win / 60.0 + 2
    cal = KUBE_BUILD[size] + 2                       # the heavier arm's step timed once a job, before its arms (protocol 3)
    return arm + cal if split else 2 * arm + cal


def kube_fits(size, organism):
    org = ORGS[KUBE.index(organism)]
    return MEM[size][org] <= RUNNER_GB and kube_minutes(size, organism, size >= SIZES[-1]) < 330


def free_runner_refusals():
    """All requested cells remain visible, including those too large for the free runner."""
    out = []
    for size in SIZES:
        for org, name in zip(ORGS, KUBE):
            if shape(size, org) is None:
                out.append(("six", size, org))
            if not kube_fits(size, name):
                out.append(("six-kube", size, name))
    return out


def matrix(scale, orgs, first, runs, per=None, workers=None):
    """six.yml's shards for one dispatch: each organism's runs first .. first+runs-1 cut into shards of its shape."""
    inc = []
    for o in orgs:
        sh = shape(scale, o)
        n = int((per or {}).get(o) or (sh[0] if sh else 1))
        w = int((workers or {}).get(o) or (sh[1] if sh else 1))
        for f in range(first, first + runs, n):
            inc.append({"org": o, "first": f, "n": min(n, first + runs - f), "w": w})
    return {"include": inc}


def kube_matrix(sizes, organisms, rep_first, reps, durations, split):
    cells = []
    for i, sz in enumerate(sizes):
        dur = durations[min(i, len(durations) - 1)]
        for o in organisms:
            for r in range(rep_first, rep_first + reps):
                for arm in (("native", "compass") if split else ("native compass",)):
                    cells.append({"organism": o, "size": sz, "rep": r, "duration": dur, "arms": arm,
                                  "tag": f"-{arm}" if split else ""})
    return cells


# ------------------------------------------------------------------------------------------------- what is started
SIX_NAME = re.compile(r"^six x(\d+) (\w+) orgs ([\d,]+) runs (\d+)\+(\d+)$")
KUBE_NAME = re.compile(r"^six-kube x(\d+) orgs ([\w,]+) reps (\d+)\+(\d+) arms ([\w ]+?) split (\w+) window (\d+)"
                       r"(?: protocol (\w+))?$")
JOB_NAME = re.compile(r"^run \((\w+), (\d+), (\d+), \d+, [\w ]+?(?:, -\w+)?\)$")   # six-kube's cell: organism, size, rep


def six_title(size, org, first, n):
    return f"six x{size} {LOAD} orgs {org} runs {first}+{n}"


def kube_title(size, orgs, r0, reps, split, window):
    return (f"six-kube x{size} orgs {','.join(orgs)} reps {r0}+{reps} arms native compass split {'yes' if split else 'no'} "
            f"window {window} protocol {KUBE_PROTOCOL}")


def coverage(runs, manifest, failed=None):
    """Which runs of each square are started (in flight or finished, not cancelled): {("six", size, org): set of run
    indices from 0, ("kube", size, organism): set of repetitions from 1 with both arms}. With the cluster inside only
    runs of protocol KUBE_PROTOCOL count, and a repetition whose job failed counts as not started (failed: {run id: set of
    (organism, rep)}, read from the runs' own job lists by failed_reps), so it is started again."""
    cov, failed = {}, failed or {}
    add = lambda key, xs: cov.setdefault(key, set()).update(xs)
    for d in manifest.get("dispatches", []):
        if d.get("status") != "kept":
            continue
        if d["grid"] == "six" and d.get("load", "normal") == LOAD:
            for o in d["orgs"]:
                add(("six", d["size"], o), range(d["first"], d["first"] + d["runs"]))
        elif d["grid"] == "six-kube" and str(d.get("protocol", "1")) == KUBE_PROTOCOL:
            for o in KUBE:
                add(("kube", d["size"], o), range(d["rep_first"], d["rep_first"] + d["reps"]))
    for r in runs:
        if r.get("conclusion") == "cancelled":
            continue
        t = r.get("display_title") or ""
        m = SIX_NAME.match(t)
        if m and m.group(2) == LOAD:
            size, first, n = int(m.group(1)), int(m.group(4)), int(m.group(5))
            for o in m.group(3).split(","):
                add(("six", size, o), range(first, first + n))
            continue
        m = KUBE_NAME.match(t)
        if m and m.group(8) == KUBE_PROTOCOL and r.get("conclusion") in (None, "success", "failure"):
            size, r0, n = int(m.group(1)), int(m.group(3)), int(m.group(4))
            bad = failed.get(r.get("id"), set())
            for o in m.group(2).split(","):
                add(("kube", size, o), [x for x in range(r0, r0 + n) if (o, x) not in bad])
    return cov


def kube_failures(runs, failed):
    """{(size, organism, rep): how many runs of protocol KUBE_PROTOCOL failed that repetition's job}."""
    out = {}
    for r in runs:
        m = KUBE_NAME.match(r.get("display_title") or "")
        if m and m.group(8) == KUBE_PROTOCOL:
            for o, x in failed.get(r.get("id"), ()):
                out[(int(m.group(1)), o, x)] = out.get((int(m.group(1)), o, x), 0) + 1
    return out


def gaps(have, lo, hi):
    """Runs lo..hi-1 not yet started, as (first, count) stretches."""
    out, i = [], lo
    while i < hi:
        if i in have:
            i += 1
            continue
        j = i
        while j < hi and j not in have:
            j += 1
        out.append((i, j - i))
        i = j
    return out


def next_dispatches(cov):
    """Every dispatch still to start, in order: tier by tier (10, then 100 runs), small sizes first, modelled then with
    the cluster inside."""
    out, cov = [], {k: set(v) for k, v in cov.items()}      # what is planned here counts as started for the next tier
    for tier in TIERS:
        for size in SIZES:
            for o in ORGS:
                sh = shape(size, o)
                if sh is None:
                    continue
                for f, n in gaps(cov.get(("six", size, o), set()), 0, tier):
                    step = sh[0] * MAX_JOBS
                    for f2 in range(f, f + n, step):
                        k = min(step, f + n - f2)
                        out.append({"grid": "six", "size": size, "orgs": [o], "first": f2, "runs": k,
                                    "jobs": math.ceil(k / sh[0]), "per": sh[0], "workers": sh[1],
                                    "hours": round(k * SEC[size][o] / sh[1] / 3600.0 + math.ceil(k / sh[0]) * CAL[size][o] / 3600.0, 1),
                                    "title": six_title(size, o, f2, k)})
                        cov.setdefault(("six", size, o), set()).update(range(f2, f2 + k))
            # with the cluster inside: organisms that share a window and the same runs still to start go in one dispatch
            split, hi = size >= SIZES[-1], tier + 1          # both arms of a repetition on one runner (paired)
            groups = {}
            for o in KUBE:
                if not kube_fits(size, o):
                    continue
                win = KUBE_WINDOW_ORG.get((size, o), KUBE_WINDOW[size])
                groups.setdefault((win, tuple(gaps(cov.get(("kube", size, o), set()), 1, hi))), []).append(o)
            for (win, todo), orgs in groups.items():
                for r0, n in todo:
                    step = MAX_JOBS // (len(orgs) * (2 if split else 1))
                    for r in range(r0, r0 + n, step):
                        k = min(step, r0 + n - r)
                        jobs = k * len(orgs) * (2 if split else 1)
                        out.append({"grid": "six-kube", "size": size, "orgs": orgs, "rep_first": r, "reps": k,
                                    "split": split, "window": win, "jobs": jobs,
                                    "hours": round(jobs * kube_minutes(size, orgs[0], split) / 60.0, 1),
                                    "title": kube_title(size, orgs, r, k, split, win)})
                        for o in orgs:
                            cov.setdefault(("kube", size, o), set()).update(range(r, r + k))
    return out


# ------------------------------------------------------------------------------------------------- GitHub
def campaign_open(now=None):
    """True once the campaign's start (SINCE, a UTC time) has passed. Every count of runs started (the grid, the reruns, the
    clouds) reads from SINCE, and a new engine's SINCE is set a little after the moment it is pushed: the conductor of the
    engine before it may start runs until the push, which then fall before SINCE and are counted in no campaign of the new
    engine, and the new conductor starts nothing until SINCE, so none of its runs falls before it either."""
    now = now or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    return now >= SINCE                                # both ISO 8601 in UTC, so the strings order as the times do


def engine():
    """The engine the runs started now will carry. On GitHub that is the newest commit of the branch they start on, which
    every tick fetches (FETCH_HEAD), read by that commit's own version tool and fingerprints: a tick that began before a new
    engine landed starts the new engine's runs at its next round, not after its five hours (17 October: omni-v8 landed during
    a tick). The conductor keeps no copy of the tool's scope or rule: its copy went stale once (omni-v15 took eight wires into
    the fingerprint, the copy read every commit after it as unknown, and nothing started; 22 October).
    Elsewhere, this checkout's HEAD, by its version tool; a partial checkout without the engine's files reads it from git."""
    def git(*a, text=True, check=False):
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=text, check=check, timeout=120)
    try:
        if os.environ.get("GITHUB_ACTIONS") == "true" and git("rev-parse", "-q", "--verify", "FETCH_HEAD").returncode == 0:
            with tempfile.TemporaryDirectory() as tmp:
                # the fetched commit's version tool and fingerprints, run on that commit's tree in this repository: with
                # GIT_DIR naming the repository, git takes the folder it runs in as the top of the tree
                (Path(tmp) / "tools").mkdir()
                prints = [f for f in git("ls-tree", "--name-only", "FETCH_HEAD").stdout.split() if re.fullmatch(r"OMNI_V\d+\.json", f)]
                for f in ("tools/omni_version.py", *prints):
                    (Path(tmp) / f).write_bytes(git("show", f"FETCH_HEAD:{f}", text=False, check=True).stdout)
                env = {k: v for k, v in os.environ.items() if k != "GIT_WORK_TREE"}
                env["GIT_DIR"] = git("rev-parse", "--absolute-git-dir", check=True).stdout.strip()
                r = subprocess.run([sys.executable, str(Path(tmp) / "tools" / "omni_version.py"), "--commit", "FETCH_HEAD"],
                                   cwd=tmp, env=env, capture_output=True, text=True, timeout=600)
        else:
            r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", "HEAD"], cwd=ROOT,
                               capture_output=True, text=True, timeout=120)
        out = r.stdout.split()
        return out[0] if r.returncode == 0 and out and re.fullmatch(r"omni-v\d+", out[0]) else "unknown"
    except (OSError, subprocess.SubprocessError, ValueError):
        return "unknown"


def api(path, method="GET", data=None, tries=4):
    """GitHub's REST API with the workflow's token, or Claude Code's gh api where there is none; a server error or a
    dropped connection is tried again (2, 4 and 8 seconds apart)."""
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    for i in range(tries):
        try:
            if tok:
                req = urllib.request.Request(f"https://api.github.com/{path}", method=method,
                                             data=json.dumps(data).encode() if data is not None else None,
                                             headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                                                      "X-GitHub-Api-Version": "2022-11-28"})
                with urllib.request.urlopen(req, timeout=60) as r:
                    body = r.read()
                return json.loads(body) if body else {}
            cmd = ["gh", "api", "-X", method, path] + (["--input", "-"] if data is not None else [])
            r = subprocess.run(cmd, input=json.dumps(data) if data is not None else None, capture_output=True, text=True)
            if r.returncode != 0:
                raise RuntimeError(f"gh api {path}: {r.stderr.strip()[:300]}")
            return json.loads(r.stdout) if r.stdout.strip() else {}
        except urllib.error.HTTPError as e:
            if e.code < 500 or i == tries - 1:
                raise
        except (urllib.error.URLError, TimeoutError, RuntimeError) as e:
            if i == tries - 1 or (isinstance(e, RuntimeError) and "HTTP 5" not in str(e) and "timeout" not in str(e).lower()):
                raise
        time.sleep(2 ** (i + 1))


def grid_runs():
    """Every run of six.yml and six-kube.yml started since the max's grid began."""
    out = []
    for wf in ("six.yml", "six-kube.yml"):
        page = 1
        while True:
            d = api(f"repos/{REPO}/actions/workflows/{wf}/runs?per_page=100&page={page}&created=>={SINCE}")
            out += d.get("workflow_runs", [])
            if len(d.get("workflow_runs", [])) < 100:
                break
            page += 1
    return out


def failed_reps(runs):
    """{run id: set of (organism, rep)}: the repetitions whose job did not succeed, in every finished run of protocol
    KUBE_PROTOCOL that failed. A finished run's jobs do not change, so each is read once per conductor (a file in the
    runner's temporary folder); a list GitHub does not give now is read again at the next tick, its run counted as started
    meanwhile (nothing is started twice)."""
    path = Path(os.environ.get("RUNNER_TEMP") or "/tmp") / "omni_grid_failed_jobs.json"
    try:
        cache = json.loads(path.read_text())
    except (OSError, ValueError):
        cache = {}
    out = {}
    for r in runs:
        m = KUBE_NAME.match(r.get("display_title") or "")
        if not m or m.group(8) != KUBE_PROTOCOL or r.get("conclusion") != "failure":
            continue
        rid = str(r["id"])
        if rid not in cache:
            bad, page = set(), 1
            try:
                while True:
                    j = api(f"repos/{REPO}/actions/runs/{rid}/jobs?filter=latest&per_page=100&page={page}")
                    for x in j.get("jobs", []):
                        mm = JOB_NAME.match(x.get("name") or "")
                        if mm and x.get("conclusion") not in ("success", "skipped"):
                            bad.add((mm.group(1), int(mm.group(3))))
                    if len(j.get("jobs", [])) < 100:
                        break
                    page += 1
            except (RuntimeError, urllib.error.URLError) as e:
                print(f"run {rid}: jobs not readable now ({str(e)[:80]}); counted as started until the next tick", file=sys.stderr)
                continue
            cache[rid] = sorted(bad)
        out[r["id"]] = {(o, int(x)) for o, x in cache[rid]}
    try:
        path.write_text(json.dumps(cache))
    except OSError:
        pass
    return out


def give_up(cov, runs, failed):
    """The repetitions whose job failed MAX_TRIES times in runs of protocol KUBE_PROTOCOL: counted as started from now on
    (never started again) and returned, {(size, organism, rep): failures}, for the report to name."""
    out = {}
    for (size, o, x), n in sorted(kube_failures(runs, failed).items()):
        if n >= MAX_TRIES and x not in cov.get(("kube", size, o), set()):
            cov.setdefault(("kube", size, o), set()).add(x)
            out[(size, o, x)] = n
    return out


def waits_for_a_runner(path, jobs):
    """The runs that go before the grid (Azure first, the founder's order of 13 October; a grid run's report; the push's
    verify): True when such a run has a job queued and none running, so it waits for a runner and not for its own
    one-at-a-time matrix (aks-metered runs its repetitions one by one)."""
    wf = (path or "").rsplit("/", 1)[-1]
    open_ = [x for x in jobs if x["status"] in ("queued", "waiting", "pending", "requested")]
    if not open_ or any(x["status"] == "in_progress" for x in jobs):
        return False
    if wf in FIRST:
        return True
    return wf in ("six.yml", "six-kube.yml") and any((x.get("name") or "").startswith("report") for x in open_)


def max_parallel(path):
    """The largest max-parallel any job of a workflow sets, or None. A matrix job's jobs beyond it wait for their own run's
    slots, not for a runner (a 100-repetition Azure set at max-parallel 1 lists 99 jobs queued for hours)."""
    try:
        text = (ROOT / path).read_text(encoding="utf-8")
    except (OSError, TypeError):
        return None
    vals = [int(v) for v in re.findall(r"^\s*max-parallel:\s*(\d+)", text, re.M)]
    return max(vals) if vals else None


def jobs_in_flight():
    """(queued, running, waiting first) jobs across every workflow of the repository right now; waiting first: the runs
    that go before the grid and wait for a runner (waits_for_a_runner). A run's queued jobs count only up to the slots its
    own max-parallel leaves free: the rest wait for the run, not for a runner, and counting them starved the grid."""
    queued = running = 0
    first, seen = [], set()
    for st in ("queued", "in_progress", "waiting", "pending", "requested"):
        d = api(f"repos/{REPO}/actions/runs?status={st}&per_page=100")
        for r in d.get("workflow_runs", []):
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            page, jobs = 1, []
            while True:
                try:
                    j = api(f"repos/{REPO}/actions/runs/{r['id']}/jobs?filter=latest&per_page=100&page={page}")
                except (RuntimeError, urllib.error.URLError) as e:   # a run being cancelled can refuse its list
                    print(f"run {r['id']}: jobs not readable ({str(e)[:80]}); not counted", file=sys.stderr)
                    break
                jobs += j.get("jobs", [])
                if len(j.get("jobs", [])) < 100 or page >= 10:   # a run holds at most 256 jobs; a list that never ends stops
                    break
                page += 1
            q = sum(x["status"] in ("queued", "waiting", "pending", "requested") for x in jobs)
            on = sum(x["status"] == "in_progress" for x in jobs)
            mp = max_parallel(r.get("path"))
            if mp is not None:
                q = min(q, max(0, mp - on))
            queued += q
            running += on
            if waits_for_a_runner(r.get("path"), jobs):
                name, title = r.get("name") or "", r.get("display_title") or str(r["id"])
                first.append(title if title.startswith(name) else f"{name}: {title}")
    return queued, running, first


def rerun_blocks(path=None):
    """The queue file's entries, [[(name, workflow, inputs)]], one list per block. Every `added=<UTC>` line opens a new block:
    the entries added once the campaign was under way."""
    path = Path(path or RERUNS)
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    blocks = [[]]
    for ln in lines:
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        if ln.startswith("added="):
            blocks.append([])
            continue
        name, wf, inputs = (ln.split("|") + ["", ""])[:3]
        kv = dict(x.split("=", 1) for x in inputs.split(";") if "=" in x)
        wf = wf.strip()
        if wf in {"gke-metered.yml", "eks-metered.yml", "gpu-bench.yml", "lambda-gpu.yml", "cloud-organism.yml"}:
            raise ValueError(f"{wf} is excluded from the approved non-GPU campaign")
        blocks[-1].append((name.strip(), wf, kv))
    return [b for b in blocks if b]


def rerun_queue(path=None):
    """The queue in release order: [(run, name, workflow, inputs)], A of every benchmark, then B, then C, block by block. A
    run is read back by its count in its workflow, in this order, so an entry put among entries already started would take
    the place of one of them (18 October: three data-store entries put among started ones would have run one entry's C twice
    and another's A never). An entry added once the campaign is under way therefore stands in a block of its own, below an
    `added=<UTC>` line, released after every entry above it, A, B and C, and every run already started keeps its place."""
    return [(run, n, wf, kv) for block in rerun_blocks(path) for run in "ABC" for n, wf, kv in block]


def reruns_to_start(queue, started):
    """The entries not yet started: for each workflow, its first started[wf] entries in queue order count as started."""
    seen, out = {}, []
    for item in queue:
        wf = item[2]
        seen[wf] = seen.get(wf, 0) + 1
        if seen[wf] > started.get(wf, 0):
            out.append(item)
    return out


def carries(sha, path, seen):
    """True when the commit carries the file at path; read once a commit and file (seen caches it). A missing file is GitHub's
    404; any other failure raises, so a run is never counted on a commit it was not read on."""
    if (sha, path) not in seen:
        try:
            api(f"repos/{REPO}/contents/{path}?ref={sha}")
            seen[(sha, path)] = True
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise
            seen[(sha, path)] = False
        except RuntimeError as e:
            if "404" not in str(e):
                raise
            seen[(sha, path)] = False
    return seen[(sha, path)]


def on_rig(sha, seen):
    """True when the commit carries RIG_FILE (the kind rig as amended on 18 October)."""
    return carries(sha, RIG_FILE, seen)


ENGINE_FILE = f"OMNI_V{ENGINE.rsplit('v', 1)[1]}.json"   # the standing engine's fingerprint, written by tools/land_engine.py


def on_engine(sha, seen):
    """True when the commit carries the standing engine's fingerprint file, so a run counts in this campaign only where it ran
    the engine that stands (24 October: an engine's campaign opened at 21:19 UTC on 23 October, the engine reached main at 02:51
    UTC on 24 October, and the runs started between counted as its runs while they ran the engine before it; the tables they
    made held two engines)."""
    return carries(sha, ENGINE_FILE, seen)


def reruns_started(queue):
    """{workflow: runs dispatched since RERUN_SINCE on a commit that carries the standing engine, and not cancelled (a kind
    workflow's: on a commit that also carries RIG_FILE)}, read from GitHub. A cancelled run is not a run (the founder's order of
    16 October: nothing is cancelled; a run GitHub cancelled before it began is released again)."""
    out, seen = {}, {}
    for wf in sorted({q[2] for q in queue}):
        n, page = 0, 1
        while page <= 5:
            d = api(f"repos/{REPO}/actions/workflows/{wf}/runs?event=workflow_dispatch&created=>={RERUN_SINCE}&per_page=100&page={page}")
            rs = d.get("workflow_runs", [])
            n += sum(r.get("conclusion") != "cancelled" and on_engine(r.get("head_sha", ""), seen)
                     and (wf not in RIG_WORKFLOWS or on_rig(r.get("head_sha", ""), seen)) for r in rs)
            if len(rs) < 100:
                break
            page += 1
        out[wf] = n
    return out


# GitHub holds every run of one concurrency group in one line, with ONE waiting place: a second run waiting in the group
# cancels the first one waiting (17 October: about thirty Azure starts of 16 October, and the reruns of the Azure full-control
# burst and of the large organisms, were cancelled that way before any machine was made). Every Azure workflow shares the
# group azure-benchmark-<region>, every Google one google-benchmark-<zone>, every Amazon one amazon-benchmark-<region>; all our
# sets use one region or zone each, so each cloud is one line: one of its runs at a time, and none started while one waits.
CLOUD_FAMILIES = {"Azure": ("aks-metered.yml", "aks-metered-full.yml", "big-organism.yml"),
                  "Google Cloud": ("gke-metered.yml",), "Amazon": ("eks-metered.yml",),
                  **{name: (BYOC_WF,) for name in BYOC}}     # one workflow for the five: one of their runs at a time
ACTIVE = ("queued", "in_progress", "waiting", "pending", "requested")


def cloud_of(wf):
    """The cloud whose single line a workflow's runs stand in, or None."""
    return next((c for c, wfs in CLOUD_FAMILIES.items() if wf in wfs), None)


def cloud_busy(cloud):
    """True when any run of the cloud's workflows is waiting or running (its line is taken)."""
    for wf in CLOUD_FAMILIES.get(cloud, ()):
        d = api(f"repos/{REPO}/actions/workflows/{wf}/runs?per_page=30")
        if any(r.get("status") in ACTIVE for r in d.get("workflow_runs", [])):
            return True
    return False


def cloud_next(queue, started, reruns_left):
    """The one run to start in a cloud's free line: A of every queued set, then A of the cloud's reruns, then B of each, then
    C (queue: [(run, name, title, inputs)], started: {title: runs not cancelled}; reruns_left: [(run, name, wf, inputs)] not
    yet started). Returns (workflow or None for the queue's own, run, name, inputs) or None."""
    seen, sets = {}, []
    for run, name, title, kv in queue:
        seen[title] = seen.get(title, 0) + 1
        if seen[title] > started.get(title, 0):
            sets.append((run, None, name, kv))
    for letter in "ABC":
        for item in sets + [(r, wf, n, kv) for r, n, wf, kv in reruns_left]:
            if item[0] == letter:
                return (item[1], item[0], item[2], item[3])
    return None


def cloud_title(wf, kv):
    """The title a cloud workflow gives a run of these inputs (its run-name), so a started set is read back by it: what ran,
    the organism, the replica room, the dial, then the machine-family queue, the last two words (Azure: the region and the
    machine size or 'pools'; Google: the zone and the machine type; Amazon: the region and the instance type). A set run to
    the paid cap under the stopping rule (stop_looks; docs/K8S_COMPASS_PREREGISTRATION.md, 19 October) carries it in its
    title, so its A, B and C are counted apart from the sets run at five repetitions before it."""
    what = f"burst {kv['load_steps']}" if kv.get("load_steps") else "steady"
    org = f" organism {kv['organism']} x{kv.get('organism_scale') or '1'}" if kv.get("organism") else ""
    room = f" replica room {kv['replica_ceiling']}" if kv.get("replica_ceiling") else ""
    room += " to the cap, stopping rule" if kv.get("stop_looks") else ""   # a set run to the cap under the stopping rule counts on its own (19 October)
    dial = kv.get("dial") or "max"   # every cloud workflow's own default since 31 October (the founder's order: the cloud at the max)
    if wf == BYOC_WF:
        c = kv.get("cloud") or "other"
        return f"{wf[:-4]} {c} {what}{org}{room} dial {dial} {c} {kv.get('pool') or 'work0'}"
    if wf == "gke-metered.yml":
        loc, fam = kv.get("zone") or "us-central1-a", kv.get("machine") or "e2-standard-2"
    elif wf == "eks-metered.yml":
        loc, fam = kv.get("region") or "us-east-1", kv.get("instance") or "m5.large"
    else:
        loc = kv.get("location") or "eastus"
        fam = "pools" if kv.get("worker_pools") else (kv.get("vm_size") or "Standard_D2s_v4")
    return f"{wf[:-4]} {what}{org}{room} dial {dial} {loc} {fam}"


def azure_title(kv):
    """The title aks-metered.yml gives a run of these inputs."""
    return cloud_title(AZURE_WF, kv)


def cloud_switch(path):
    """The queue file's switch line: True when it reads switch=on, or when the file carries no switch (Azure's old form)."""
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return False
    for ln in lines:
        ln = ln.strip()
        if ln.startswith("switch="):
            return ln.split("=", 1)[1].strip().lower() == "on"
    return True


def check_state(runs, cloud, now=None):
    """Whether a cloud's sets may start, from cloud-check.yml's runs (any order): ("go" | "wait" | "check", why). "go": its
    newest check passed within CHECK_FRESH_H; "wait": a check runs, or the last failed under CHECK_RETRY_MIN ago; "check":
    start one (none yet, the last failed or was cancelled long enough ago, or the last pass is stale). Only the cloud's own
    title counts (cloud-check google | cloud-check amazon); a check of both, started by hand, is read by neither."""
    title = f"{CHECK_WF[:-4]} {CHECKS[cloud]}"
    mine = sorted((r for r in runs if (r.get("display_title") or "") == title), key=lambda r: r.get("created_at") or "")
    if not mine:
        return "check", "no $0 check yet"
    r = mine[-1]
    now = now or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    age = (calendar.timegm(time.strptime(now, "%Y-%m-%dT%H:%M:%SZ"))
           - calendar.timegm(time.strptime(r.get("created_at") or now, "%Y-%m-%dT%H:%M:%SZ"))) / 60
    link = r.get("html_url") or f"run {r.get('id')}"
    if r.get("status") in ACTIVE:
        return "wait", f"its $0 check runs ({link})"
    if r.get("conclusion") == "success":
        if age < CHECK_FRESH_H * 60:
            return "go", f"its $0 check passed {age:.0f} minutes ago"
        return "check", f"its last $0 check passed over {CHECK_FRESH_H} hours ago"
    if age < CHECK_RETRY_MIN:
        return "wait", f"its $0 check failed {age:.0f} minutes ago ({link}); checked again after {CHECK_RETRY_MIN} minutes"
    return "check", f"its last $0 check did not pass ({link})"


def azure_group(title):
    """A run's line at GitHub: its concurrency group's region or zone, the second-to-last word of its title (the machine size
    is not part of the group: two sizes in one region share one line)."""
    w = (title or "").split()
    return w[-2] if len(w) >= 2 else ""


def azure_queue(path=None, wf=AZURE_WF):
    """A cloud's sets in release order: [(run, name, title, inputs)], A of every line, then B, then C (the switch line and
    the comments are not sets)."""
    path = Path(path or AZURE_QUEUE)
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    entries = []
    for ln in lines:
        ln = ln.strip()
        if not ln or ln.startswith("#") or ln.startswith("switch="):
            continue
        name, inputs = (ln.split("|") + [""])[:2]
        kv = dict(x.split("=", 1) for x in inputs.split(";") if "=" in x)
        entries.append((name.strip(), cloud_title(wf, kv), kv))
    return [(run, n, t, kv) for run in "ABC" for n, t, kv in entries]


cloud_queue = azure_queue


def azure_to_start(queue, started, busy):
    """The sets to start now: in each line (region) not busy, its first set not yet started (the k-th line of a title counts
    as started when started[title] >= k); at most one a line, whatever the machine size."""
    seen, taken, out = {}, set(), []
    for item in queue:
        t = item[2]
        seen[t] = seen.get(t, 0) + 1
        if seen[t] <= started.get(t, 0):
            continue
        g = azure_group(t)
        if g in busy or g in taken:
            taken.add(g)                                  # the line's next set waits behind the one in front of it
            continue
        taken.add(g)
        out.append(item)
    return out


def azure_runs(wf=AZURE_WF):
    """A cloud workflow's dispatched runs since AZURE_SINCE: ({title: runs not cancelled}, {queues with a run waiting or
    running}). Only dispatched runs count: a push registers the Google and Amazon workflows and runs nothing."""
    started, busy, page = {}, set(), 1
    while page <= 5:
        d = api(f"repos/{REPO}/actions/workflows/{wf}/runs?event=workflow_dispatch&created=>={AZURE_SINCE}&per_page=100&page={page}")
        rs = d.get("workflow_runs", [])
        for r in rs:
            t = r.get("display_title") or ""
            if r.get("conclusion") != "cancelled":
                started[t] = started.get(t, 0) + 1
            if r.get("status") in ("queued", "in_progress", "waiting", "pending", "requested"):
                busy.add(azure_group(t))
        if len(rs) < 100:
            break
        page += 1
    return started, busy


def dispatch(d, ref):
    if d["grid"] == "six":
        o = d["orgs"][0]
        inputs = {"what": "runs", "scale": str(d["size"]), "orgs": ",".join(d["orgs"]), "first": str(d["first"]),
                  "runs": str(d["runs"]), "per_shard": json.dumps({o: d["per"]}), "workers": json.dumps({o: d["workers"]}),
                  "arm": "v5", "load": LOAD, "deadline_min": str(DEADLINE_MIN)}
        wf = "six.yml"
    else:
        inputs = {"what": "runs", "sizes": str(d["size"]), "organisms": ",".join(d["orgs"]), "reps": str(d["reps"]),
                  "rep_first": str(d["rep_first"]), "durations_s": str(d["window"]), "arms": "native compass",
                  "split": "yes" if d["split"] else "no"}
        wf = "six-kube.yml"
    api(f"repos/{REPO}/actions/workflows/{wf}/dispatches", method="POST", data={"ref": ref, "inputs": inputs})


def squares(cov):
    """The squares by organism and size: runs started of 100 (modelled; with the cluster inside)."""
    rows = []
    for size in SIZES:
        for o, k in zip(ORGS, KUBE):
            rows.append((size, o, len({x for x in cov.get(("six", size, o), ()) if x < RUNS}),
                         len({x for x in cov.get(("kube", size, k), ()) if 1 <= x <= RUNS})))
    return rows


def report(cov, started, queued, running, target, out=sys.stdout, gave_up=None, first=()):
    names = {"1": "Compute / AI / Cloud", "2": "Physics / Robotics / Autonomous", "3": "Energy / Facility / Industrial",
             "4": "Distribution / Specialized", "5": "The four stacked", "6": "The whole tower", "7": "The spine"}
    print(f"| Size | Organism | Modelled: runs started of {RUNS} | With the real cluster inside: runs started of {RUNS} |", file=out)
    print("|---:|---|---|---|", file=out)
    for size, o, six, kube in squares(cov):
        print(f"| {size:,} | {names[o]} | {six:,} | {kube:,} |", file=out)
    print(f"\nJobs now: {running} running, {queued} queued; target {target}. Started this time: {len(started)} dispatches, "
          f"{sum(d['jobs'] for d in started)} jobs.", file=out)
    for grid, size, org in free_runner_refusals():
        print(f"- pending runner capacity: {grid} {org} x{size}; exceeds free runner memory/time estimate; no paid fallback", file=out)
    for t in first:
        print(f"- held: {t} waits for a runner and goes before the grid", file=out)
    for d in started:
        print(f"- {d['title']} ({d['jobs']} jobs, about {d['hours']} runner-hours)", file=out)
    print(f"\nWith the cluster inside, only runs of protocol {KUBE_PROTOCOL} count (12 Oct: the governor never below the "
          "organism's priority, its decisions counted inside the window; 13 Oct: the model on its own core, the kind nodes on "
          "the others, the window set from the heavier arm's measured step; 18 Oct: the served image pulled onto every worker "
          "before each arm); a repetition whose job failed is started again, "
          f"up to {MAX_TRIES} times.", file=out)
    for (size, o, x), n in sorted((gave_up or {}).items()):
        print(f"- not started again: {o} at {size:,} copies, repetition {x} (its job failed {n} times; listed, never "
              "dropped silently)", file=out)


def yield_repair_coordinator():
    """One explicit maintenance request releases a sleeping coordinator, never measured benchmark jobs."""
    request_path = ROOT / 'scripts' / 'azure_runner_priority.json'
    if not request_path.exists():
        return False
    request = json.loads(request_path.read_text())
    current = os.environ.get('GITHUB_RUN_ID', '')
    if current != str(request['coordinator_run_id']):
        return False
    repair = api(f"repos/{REPO}/actions/runs/{request['repair_run_id']}")
    if repair['path'] != '.github/workflows/restart-aks.yml' or repair['status'] == 'completed':
        return False
    own = api(f"repos/{REPO}/actions/runs/{current}")
    if own['path'] != '.github/workflows/grid.yml' or own['head_branch'] != 'main':
        raise RuntimeError('only a main-branch coordinator may yield its runner')
    if request.get('stop_repair'):
        api(f"repos/{REPO}/actions/runs/{request['repair_run_id']}/cancel", method='POST')
        print("Pending Azure restart stopped at the owner's direction.", flush=True)
        return True
    # Exact repository run identities only: duplicate verification and coordinators contain no measured arm.
    pending = []
    for item in request['release_runs']:
        if item['path'] not in ('.github/workflows/grid.yml', '.github/workflows/verify.yml'):
            raise RuntimeError('refusing to cancel measured work')
        run = api(f"repos/{REPO}/actions/runs/{item['id']}")
        if run['path'] != item['path'] or run['head_branch'] != 'main':
            raise RuntimeError('maintenance runner request identity mismatch')
        if run['status'] != 'completed':
            pending.append(item['id'])
    for run_id in pending:
        api(f"repos/{REPO}/actions/runs/{run_id}/cancel", method='POST')
    print('Yielding the sleeping grid coordinator runner for the approved Azure restart; measured jobs continue.', flush=True)
    api(f"repos/{REPO}/actions/runs/{current}/cancel", method='POST')
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="what", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--offline", action="store_true", help="from the manifest alone (no GitHub calls)")
    t = sub.add_parser("tick")
    t.add_argument("--ref", default=os.environ.get("GITHUB_REF_NAME", "main"))
    t.add_argument("--dry", action="store_true", help="say what would start; start nothing")
    t.add_argument("--extra", type=int, default=60, help="jobs kept queued beyond what GitHub is running")
    t.add_argument("--floor", type=int, default=150, help="the least jobs kept in flight")
    t.add_argument("--max-dispatches", type=int, default=40)
    t.add_argument("--grid", choices=("six", "six-kube", "all"), default="all", help="which grid to start (the buttons: their own)")
    t.add_argument("--reruns-per-tick", type=int, default=RERUN_PER_TICK, help="reruns released at most in one tick")
    m = sub.add_parser("matrix")
    m.add_argument("--scale", type=int, required=True); m.add_argument("--orgs", required=True)
    m.add_argument("--first", type=int, default=0); m.add_argument("--runs", type=int, default=RUNS)
    m.add_argument("--per-shard", default=""); m.add_argument("--workers", default="")
    k = sub.add_parser("kube-matrix")
    k.add_argument("--sizes", required=True); k.add_argument("--organisms", default=",".join(KUBE))
    k.add_argument("--reps", required=True); k.add_argument("--rep-first", type=int, default=1)
    k.add_argument("--durations", required=True); k.add_argument("--split", default="no")
    a = ap.parse_args(argv)
    if a.what == 'tick' and not a.dry and yield_repair_coordinator():
        return 0

    if a.what == "matrix":
        js = lambda s: json.loads(s) if s.strip().startswith("{") else ({} if not s.strip() else None)
        per, wk = js(a.per_shard), js(a.workers)
        if wk is None:                                   # one number for every organism
            wk = {o: int(a.workers) for o in ORGS}
        print(json.dumps(matrix(a.scale, json.loads(a.orgs) if a.orgs.startswith("[") else a.orgs.split(","),
                                a.first, a.runs, per, wk)))
        return 0
    if a.what == "kube-matrix":
        sizes = [int(x) for x in a.sizes.split(",")]
        reps = [int(x) for x in a.reps.split(",")]          # one count for every size, or one per size
        durs = [int(x) for x in a.durations.split(",")]      # likewise
        pick = lambda xs, i: xs[min(i, len(xs) - 1)]
        cells = [c for i, sz in enumerate(sizes)
                 for c in kube_matrix([sz], a.organisms.split(","), a.rep_first, pick(reps, i), [pick(durs, i)], a.split == "yes")]
        print(json.dumps(cells))
        return 0

    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {"dispatches": []}
    runs = [] if getattr(a, "offline", False) else grid_runs()
    failed = failed_reps(runs) if runs else {}
    cov = coverage(runs, manifest, failed)
    gave_up = give_up(cov, runs, failed)
    todo = next_dispatches(cov)
    if a.what == "plan":
        report(cov, [], 0, 0, 0, gave_up=gave_up)
        left_jobs = sum(d["jobs"] for d in todo)
        left_h = sum(d["hours"] for d in todo)
        print(f"\nStill to start on GitHub: {left_jobs:,} jobs, about {left_h:,.0f} runner-hours "
              f"(about {left_h / 180 / 24:.1f} days at the 180 jobs GitHub ran at once on 12 Oct; free for this public repository).")
        return 0
    eng = engine()
    if eng != ENGINE:                                  # a grid belongs to one engine: never start its runs on another
        print(f"this checkout runs {eng}, the grid is {ENGINE}'s: nothing started (a new engine gets its own grid)")
        return 0
    if not campaign_open():                            # a run started before SINCE would be counted in no campaign
        print(f"{ENGINE}'s campaign starts at {SINCE} UTC: nothing started before it")
        return 0
    azure = []
    rq = rerun_queue() if a.grid == "all" else []
    rerun_counts = None
    for cloud, wf, qpath in CLOUDS:
        if not cloud_switch(qpath):
            print(f"{cloud} queue: switched off ({qpath.relative_to(ROOT)}); nothing started there until the founder turns it on")
            continue
        queue = azure_queue(qpath, wf)
        family_reruns = [q for q in rq if cloud_of(q[2]) == cloud]
        if not queue and not family_reruns:
            continue
        try:
            # one line a cloud at GitHub: one run at a time, and nothing started while one waits or runs
            if cloud_busy(cloud):
                azure.append(f"{cloud}: a run waits or runs in its line; nothing more started there this tick")
                continue
            if family_reruns and rerun_counts is None:
                rerun_counts = reruns_started(rq)
            left = reruns_to_start(family_reruns, rerun_counts or {}) if family_reruns else []
            nxt = cloud_next(queue, azure_runs(wf)[0], left)
            if nxt and cloud in CHECKS:
                # every cloud: a set starts only once the cloud's $0 check passed (CHECK_WF)
                checks = api(f"repos/{REPO}/actions/workflows/{CHECK_WF}/runs?event=workflow_dispatch&per_page=30")
                state, why = check_state(checks.get("workflow_runs", []), cloud)
                if state == "check" and not a.dry:
                    api(f"repos/{REPO}/actions/workflows/{CHECK_WF}/dispatches", method="POST",
                        data={"ref": a.ref, "inputs": {"cloud": CHECKS[cloud]}})
                if state != "go":
                    azure.append(f"{cloud}: {why}; no set started there until it passes"
                                 + (("; a check would start (dry run)" if a.dry else "; a new check started") if state == "check" else ""))
                    continue
            if nxt:
                run_wf, run, name, kv = nxt
                if not a.dry:
                    api(f"repos/{REPO}/actions/workflows/{run_wf or wf}/dispatches", method="POST", data={"ref": a.ref, "inputs": kv})
                    time.sleep(2)
                azure.append(f"{cloud} {'rerun' if run_wf else 'set'} started: {name} {run}")
        except (RuntimeError, urllib.error.URLError) as e:   # the cloud is read again at the next tick
            print(f"{cloud} queue not read ({str(e)[:120]}); tried again at the next tick", file=sys.stderr)
    for x in azure:
        print(x)
    queued, running, first = jobs_in_flight()
    target = max(a.floor, running + a.extra)
    inflight, started = queued + running, []
    for t in first:
        print(f"waits for a runner and goes first: {t}")
    reruns = []
    if a.grid == "all" and not first:
        queue = [q for q in rq if cloud_of(q[2]) is None]       # a cloud's reruns stand in its own line (above)
        if queue:
            for run, name, wf, kv in reruns_to_start(queue, reruns_started(queue))[:a.reruns_per_tick]:
                if inflight >= target:
                    break
                if not a.dry:
                    inputs = {**kv, "label": run} if wf in LABELLED else kv
                    api(f"repos/{REPO}/actions/workflows/{wf}/dispatches", method="POST", data={"ref": a.ref, "inputs": inputs})
                    time.sleep(2)
                reruns.append(f"{name} {run}")
                inflight += RERUN_JOBS
    for r in reruns:
        print(f"rerun started on the engine that stands: {r}")
    for d in todo:
        if a.grid != "all" and d["grid"] != a.grid:
            continue
        if first or len(started) >= a.max_dispatches or inflight >= target:   # a dispatch bigger than the margin still starts
            break
        if not a.dry:
            dispatch(d, a.ref)
            time.sleep(2)
        started.append(d)
        inflight += d["jobs"]
    for d in started:
        print(f"started: {d['title']} ({d['jobs']} jobs)")
    print(f"jobs now {running} running, {queued} queued; target {target}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    with (open(summary, "a") if summary else contextlib.nullcontext(sys.stdout)) as out:
        print("## Free GitHub grid: 1, 10, 100 and 500 copies; nested runs through 500" + (" (dry run: nothing started)" if a.dry else ""), file=out)
        print("", file=out)
        report(cov, started, queued, running, target, out, gave_up=gave_up, first=first)
        for r in reruns:
            print(f"- rerun started on the engine that stands: {r}", file=out)
        for x in azure:
            print(f"- the clouds: {x}", file=out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
