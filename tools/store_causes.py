#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Why the data stores read as they do: the omni arms' own audits and the consumers' own records, read back
(docs/STORE_ROOT_CAUSES_2026-10-30.md). Every number that page states is printed here from the raw runs on the branch `raw`.

  gate     for every omni arm of a run: the seconds the service stood over its line; how many of them the verdict held or
           clamped the knob ("gated"), and how many of those the brain's own rule had asked to go up (add, grow, fail up) and
           was kept from it ("refused"); the allowance at the start and at the end
  trials   how each verdict trial ended: allowed, refused or abandoned, or ended by the wall (a fail-up in the second it ended)
  stalls   (Kafka) the extra wait the messages saw after each consumer change made in calm: the rebalance a change costs
  rate     (Kafka) a backlogged consumer's own messages a second, in its own record (native arms)

  python3 tools/store_causes.py gate RUN_DIR [RUN_DIR ...]
  python3 tools/store_causes.py trials RUN_DIR
  python3 tools/store_causes.py stalls RAW_ROOT
  python3 tools/store_causes.py rate RAW_ROOT
"""
from __future__ import annotations

import argparse
import collections
import glob
import gzip
import json
import os
import statistics


def audits(run):
    return sorted(glob.glob(os.path.join(run, "*", "*", "rep-*", "omni", "audit.jsonl")))


def records(path):
    out = []
    with open(path) as fh:
        for line in fh:
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if "why" in r:
                out.append(r)
    return out


def line_ms(audit):
    wl = os.path.dirname(os.path.dirname(os.path.dirname(audit)))
    for j in glob.glob(os.path.join(wl, "*.json")):
        try:
            return json.load(open(j)).get("line_ms")
        except (ValueError, OSError):
            continue
    return None


def gate(runs):
    for run in runs:
        tot = collections.Counter(); ends = collections.Counter(); store = "?"
        for a in audits(run):
            store = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(a)))).split("-")[0]
            line = line_ms(a); rs = records(a)
            if not rs:
                continue
            for r in rs:
                over = line is not None and r.get("reading_ms", 0) > line
                gated = "held by the verdict" in r["why"] or "the verdict allows" in r["why"]
                asked = r["why"].split(";")[0]
                wanted_more = any(w in asked for w in ("add", "grow", "fail up"))
                tot["seconds"] += 1; tot["over the line"] += over; tot["gated"] += gated; tot["gated while over"] += gated and over
                tot["asked for more and refused while over"] += over and gated and wanted_more
            ends[(rs[0].get("allowed_low"), rs[0].get("allowed_high"), rs[-1].get("allowed_low"), rs[-1].get("allowed_high"))] += 1
            tot["arms"] += 1
        print(f"{run} ({store}): " + ", ".join(f"{k} {v}" for k, v in tot.items()))
        print("   allowance (low, high) at the start -> at the end, arms: " +
              "; ".join(f"({a}, {b}) -> ({c}, {d}): {n}" for (a, b, c, d), n in sorted(ends.items(), key=str)))


def trials(run):
    ends = collections.Counter()
    for a in audits(run):
        prev = None; prev_lo = prev_hi = None
        for r in records(a):
            ph = (r.get("verdict_direction"), r.get("verdict_phase"))
            if prev is not None and prev[1] is not None and ph[1] is None:
                if r["why"].startswith("fail up"):
                    ends[(prev[0], "ended by the wall")] += 1
                elif prev[0] == "spend" and (r.get("allowed_high") or 0) > (prev_hi or 0):
                    ends[(prev[0], "allowed")] += 1
                elif prev[0] == "give back" and (r.get("allowed_low") or 0) < (prev_lo or 0):
                    ends[(prev[0], "allowed")] += 1
                else:
                    ends[(prev[0], "refused or abandoned")] += 1
            prev, prev_lo, prev_hi = ph, r.get("allowed_low"), r.get("allowed_high")
    for (d, how), n in sorted(ends.items()):
        print(f"{run}: {d} trials {how}: {n}")


def text_lines(f):
    op = gzip.open if f.endswith(".gz") else open
    with op(f, "rt") as fh:
        yield from fh


def consumer_rows(arm_dir):
    rows = []
    for f in glob.glob(os.path.join(arm_dir, "consumer-*.log*")):
        for line in text_lines(f):
            p = line.split()
            if len(p) >= 3:
                rows.append((float(p[0]), float(p[2])))
    rows.sort()
    return rows


def stalls(root):
    adds, removes = [], []
    for arm in sorted(glob.glob(os.path.join(root, "run-*", "kafka-*", "kafka-*", "rep-*", "omni"))):
        rs = [json.loads(x) for x in open(os.path.join(arm, "audit.jsonl"))]
        if not any(r.get("target") != r.get("consumers") for r in rs):
            continue
        rows = consumer_rows(arm)
        if not rows:
            continue
        t0 = rows[0][0]
        cnt = collections.Counter(int(t - t0) for t, _ in rows)
        lat = collections.defaultdict(list)
        for t, l in rows:
            lat[int(t - t0)].append(l)
        aud = {int(round(r["t"])): r.get("consumed_last_s", 0) for r in rs}
        off = min((sum(abs(cnt.get(s - o, 0) - aud.get(s, 0)) for s in range(20, max(aud) - 10)), o) for o in range(-15, 16))[1]
        for r in rs:
            if r.get("target") == r.get("consumers") or r.get("lag", 0) > 50:
                continue                       # a change made in calm: the stall is the change's own
            t = int(round(r["t"]))
            before = [x for s in range(t - 3, t) for x in lat.get(s - off, [])]
            after = [x for s in range(t, t + 4) for x in lat.get(s - off, [])]
            if len(before) < 20 or not after:
                continue
            (adds if r["target"] > r["consumers"] else removes).append((max(after) - statistics.median(before)) / 1000.0)
    for name, xs in (("added", adds), ("removed", removes)):
        xs.sort()
        if xs:
            print(f"a consumer {name} in calm, {len(xs)} changes: the extra wait after it (s): median {statistics.median(xs):.3f}, "
                  f"quartiles {xs[len(xs) // 4]:.3f} and {xs[3 * len(xs) // 4]:.3f}, least {xs[0]:.3f}, most {xs[-1]:.3f}")


def rate(root):
    res = collections.defaultdict(list)
    for arm in sorted(glob.glob(os.path.join(root, "run-*", "kafka-*", "kafka-*", "rep-*", "native"))):
        wl = arm.split(os.sep)[-3].split("-")[1]
        for f in glob.glob(os.path.join(arm, "consumer-*.log*")):
            per = collections.Counter(); worst = collections.defaultdict(float); t0 = None
            for line in text_lines(f):
                p = line.split()
                if len(p) < 3:
                    continue
                t = float(p[0]); t0 = t if t0 is None else t0
                s = int(t - t0); per[s] += 1; worst[s] = max(worst[s], float(p[2]))
            busy = sorted(per[s] for s in per if worst[s] > 200 and s > 2 and worst.get(s + 1, 0) > 200)
            if len(busy) >= 5:
                res[wl].append(statistics.median(busy))
    for wl, v in sorted(res.items()):
        print(f"{wl}: a backlogged consumer's own messages a second, the median over {len(v)} consumers: {statistics.median(v):.0f} "
              f"(from {min(v):.0f} to {max(v):.0f})")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("what", choices=("gate", "trials", "stalls", "rate"))
    ap.add_argument("paths", nargs="+")
    a = ap.parse_args(argv)
    if a.what == "gate":
        gate(a.paths)
    elif a.what == "trials":
        for p in a.paths:
            trials(p)
    elif a.what == "stalls":
        stalls(a.paths[0])
    else:
        rate(a.paths[0])


if __name__ == "__main__":
    main()
