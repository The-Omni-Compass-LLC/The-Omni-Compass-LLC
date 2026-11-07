# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The numbers of docs/LOSS_CAUSES_2026-11-07.md, read again from Koordinator's runs on the branch raw.

For each of the six runs of Koordinator's two batch-stream tables on omni-v25 (ten repetitions each) it reads the governor's audit,
each request's response time, the cluster's capture and Koordinator's batch processor at the window's end, and prints:

  the conveyance's writes an arm   raises and hand-backs of a web pod's processor limit; writes of the web service's target
  the minutes by what it did       the web service's mean, 95th and 99th percentile in the minutes the conveyance held, raised
                                   only, or handed back, against native's in the same minutes (the requests of those minutes pooled)
  the batch processor              Koordinator's batch processor summed over the nodes at the window's end, each arm's mean
  the pod starts                   web pods started (rises in the capture's replicas), split by whether the target was written

  python3 tools/koordinator_causes.py [--repo PATH] [--ref origin/raw] [--json OUT.json]

PATH is a checkout whose git holds the branch raw (a partial clone serves, its blobs fetched as they are read).
"""
from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys

RUNS = {"cgroup root": [42173258848, 42173278954, 42185612749], "plain": [41800261877, 41800269022, 41802293120]}
BIN = 60


def reader(repo, ref):
    def show(path):
        r = subprocess.run(["git", "-C", repo, "show", f"{ref}:{path}"], capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else ""
    return show


def q(values, p):
    v = sorted(values)
    return v[int(p * (len(v) - 1))] if v else float("nan")


def pct(a, b):
    return (b / a - 1.0) * 100.0 if a else float("nan")


def arm(show, run, rep, which):
    return f"run-{run}/paired-{rep}/bench-{which}-{rep}"


def writes(show, path):
    raises = backs = target = 0
    for line in show(path + "/audit.jsonl").splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        w = d.get("write")
        if not w:
            continue
        if "pod" in w and "patch" in w and "-p" in w:
            v = json.loads(w[w.index("-p") + 1])[0]["value"]
            backs += v == "500m"
            raises += v != "500m"
        elif "hpa" in w and "patch" in w:
            target += 1
    return raises, backs, target


def minutes(show, runs):
    groups = {"held its raise (no write)": ([], [], 0), "raised only": ([], [], 0), "handed back in the minute": ([], [], 0)}
    for run in runs:
        for rep in range(1, 11):
            lat = {}
            for which in ("native", "compass"):
                bins = {}
                for line in show(arm(show, run, rep, which) + "/latency.csv").splitlines()[1:]:
                    x = line.split(",")
                    if len(x) >= 3:
                        bins.setdefault(int(float(x[0]) // BIN), []).append(float(x[1]))
                lat[which] = bins
            path = arm(show, run, rep, "compass")
            try:
                ws = int(show(path + "/window_start.txt").strip())
            except ValueError:
                continue
            ev = {}
            for line in show(path + "/audit.jsonl").splitlines():
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                w = d.get("write")
                if w and "pod" in w and "patch" in w and "-p" in w:
                    v = json.loads(w[w.index("-p") + 1])[0]["value"]
                    ev.setdefault(int((d["time"] - ws) // BIN), set()).add("h" if v == "500m" else "R")
            for k in set(lat["native"]) & set(lat["compass"]):
                e = ev.get(k, set())
                g = "handed back in the minute" if "h" in e else ("raised only" if e else "held its raise (no write)")
                n, c, m = groups[g]
                n.extend(lat["native"][k]); c.extend(lat["compass"][k])
                groups[g] = (n, c, m + 1)
    out = {}
    for g, (n, c, m) in groups.items():
        if n and c:
            out[g] = {"minutes": m, "mean": pct(statistics.mean(n), statistics.mean(c)),
                      "p95": pct(q(n, .95), q(c, .95)), "p99": pct(q(n, .99), q(c, .99))}
    return out


def batch_processor(show, runs):
    tot = {"native": [], "compass": []}
    for run in runs:
        for rep in range(1, 11):
            for which in tot:
                t = show(arm(show, run, rep, which) + "/batch_queue_end.json")
                if t:
                    v = [int(x["batch_cpu"]) for x in json.loads(t) if x.get("batch_cpu") not in (None, "")]
                    if v:
                        tot[which].append(sum(v))
    return {w: statistics.mean(v) for w, v in tot.items() if v}


def starts(show, path):
    cap = show(path + "/capture.csv").splitlines()
    if not cap:
        return 0
    h = cap[0].split(","); k = h.index("hpa_current_replicas"); prev, n = None, 0
    for line in cap[1:]:
        x = line.split(",")
        try:
            v = int(float(x[k]))
        except (ValueError, IndexError):
            continue
        if prev is not None and v > prev:
            n += v - prev
        prev = v
    return n


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=".")
    ap.add_argument("--ref", default="origin/raw")
    ap.add_argument("--json", default="")
    a = ap.parse_args(argv)
    show = reader(a.repo, a.ref)
    rec = {"runs": RUNS, "rigs": {}}
    split = {"with target writes": [0, 0, 0], "without": [0, 0, 0]}
    for rig, runs in RUNS.items():
        per = [writes(show, arm(show, r, i, "compass")) for r in runs for i in range(1, 11)]
        rec["rigs"][rig] = {"raises": [min(p[0] for p in per), max(p[0] for p in per)],
                            "hand_backs": [min(p[1] for p in per), max(p[1] for p in per)],
                            "target_writes": [min(p[2] for p in per), max(p[2] for p in per)],
                            "minutes": minutes(show, runs), "batch_processor": batch_processor(show, runs)}
        for r in runs:
            for i in range(1, 11):
                g = split["with target writes" if writes(show, arm(show, r, i, "compass"))[2] else "without"]
                g[0] += 1; g[1] += starts(show, arm(show, r, i, "native")); g[2] += starts(show, arm(show, r, i, "compass"))
    rec["pod_starts"] = {k: {"repetitions": v[0], "native": v[1], "omni": v[2]} for k, v in split.items()}
    print(json.dumps(rec, indent=1))
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
