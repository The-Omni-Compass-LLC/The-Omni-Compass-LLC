#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Where a pod's start wait goes, read from a kind run's own files: the record behind the "pod start wait, mean" row.

Each serving pod started inside the measured window is split, from Kubernetes' own timestamps (pod_watch.json), into
    scheduling     created -> PodScheduled
    node side      PodScheduled -> its container running (kubelet, the container runtime, the network setup on the node)
    app and probe  container running -> Ready (php-apache's start and its 2 s readiness probe)
and placed by the host's busy share over its start (host_cpu.csv, the real machine under kind) and by whether its node
already carried a serving pod. Then the change in the mean between the arms is split in two (a two-fold decomposition over
strata s, each a band of the host's busy share and the node's state, empty or already serving; p the share of an arm's starts
in a stratum, W its mean wait there):
    ΔW̄ = W̄[omni] − W̄[native] = Σ_s (p[omni,s] − p[native,s]) · W[native,s]  +  Σ_s p[omni,s] · (W[omni,s] − W[native,s])
         the shift of starts into other strata (a busier host, an empty node)    the wait in the same stratum
A stratum native never reaches is counted in the first term at the omni arm's own wait there (no native wait exists), so the
two terms add up to ΔW̄ exactly.

  python3 tools/pod_phases.py RUN [RUN ...] [--out results/live/POD_START_PHASES.md]
RUN is a run folder under results/live/raw/ holding bench-native-<n>/ and bench-compass-<n>/ (directly or in http/ or
both/); open it first with scripts/raw_archive.sh open /RUN/.
"""
from __future__ import annotations

import argparse
import bisect
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "results" / "live" / "raw"
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as _legal_stamp  # noqa: E402  (the legal notice every generated report carries)
from tools.readings import OWN_RUNS, receipt_key  # noqa: E402
BANDS = ((0.0, 0.5), (0.5, 0.7), (0.7, 1.01))


def ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()


def pods(d):
    """Every pod in pod_watch.json: created, scheduled, container running, Ready, node."""
    f = d / "pod_watch.json"
    if not f.exists():
        return []
    text, dec, i, out = f.read_text(), json.JSONDecoder(), 0, {}
    while i < len(text):
        while i < len(text) and text[i].isspace():
            i += 1
        if i >= len(text):
            break
        try:
            ev, i = dec.raw_decode(text, i)
        except ValueError:
            break
        o = ev.get("object", ev); m = o.get("metadata", {}); uid = m.get("uid")
        if not uid or not m.get("creationTimestamp"):
            continue
        r = out.setdefault(uid, {"created": ts(m["creationTimestamp"]), "scheduled": None, "running": None, "ready": None, "node": ""})
        r["node"] = (o.get("spec") or {}).get("nodeName") or r["node"]
        for c in (o.get("status") or {}).get("conditions") or []:
            when = c.get("lastTransitionTime")
            if c.get("status") != "True" or not when:
                continue
            if c.get("type") == "PodScheduled" and r["scheduled"] is None:
                r["scheduled"] = ts(when)
            if c.get("type") == "Ready" and r["ready"] is None:
                r["ready"] = ts(when)
        for cs in (o.get("status") or {}).get("containerStatuses") or []:
            started = ((cs.get("state") or {}).get("running") or {}).get("startedAt")
            if started and r["running"] is None:
                r["running"] = ts(started)
    return list(out.values())


def host(d):
    t, b = [], []
    f = d / "host_cpu.csv"
    for line in (f.read_text().splitlines()[1:] if f.exists() else []):
        p = line.split(",")
        try:
            t.append(float(p[0])); b.append(float(p[1]))
        except (ValueError, IndexError):
            continue
    return t, b


def busy(t, b, t0, t1):
    i, j = bisect.bisect_left(t, t0 - 2), bisect.bisect_right(t, t1 + 2)
    v = b[i:j]
    return sum(v) / len(v) if v else None


def arm_dirs(run):
    base = RAW / run
    for sub in ("", "http", "both"):
        d = base / sub if sub else base
        if any(d.glob("bench-*-*")):
            yield sub or "-", d


def starts(run):
    """[(arm, test, wait, scheduling, node side, app and probe, busy, node already serving)] for every pod started and Ready
    inside a repetition's measured window."""
    rows = []
    for test, d in arm_dirs(run):
        for rep in sorted(d.glob("bench-*-*")):
            arm = rep.name.split("-")[1]
            try:
                t0 = float((rep / "window_start.txt").read_text().split()[0]); t1 = float((rep / "window_end.txt").read_text().split()[0])
            except (OSError, ValueError, IndexError):
                continue
            t, b = host(rep); ps = pods(rep)
            for p in ps:
                if not t0 <= p["created"] <= t1 or p["running"] is None or p["ready"] is None:
                    continue
                sched = (p["scheduled"] or p["created"]) - p["created"]
                serving = any(q is not p and q["node"] == p["node"] and q["ready"] and q["ready"] < p["created"] for q in ps)
                rows.append((arm, test, p["ready"] - p["created"], sched, p["running"] - p["created"] - sched,
                             p["ready"] - p["running"], busy(t, b, p["created"], p["ready"]), serving))
    return rows


def band(x):
    for lo, hi in BANDS:
        if x is not None and lo <= x < hi:
            return (lo, hi)
    return None


def decompose(rows):
    """(ΔW̄, shift term, same-stratum term, means) between the omni arm ('compass') and native, over strata of the host's busy
    band and the node's state."""
    strata = [(bd, serving) for bd in BANDS for serving in (False, True)]
    by = {a: [r for r in rows if r[0] == a and band(r[6])] for a in ("native", "compass")}
    if not by["native"] or not by["compass"]:
        return None
    of = lambda r: (band(r[6]), r[7])
    mean = {a: statistics.mean(r[2] for r in by[a]) for a in by}
    p = {a: {s: sum(1 for r in by[a] if of(r) == s) / len(by[a]) for s in strata} for a in by}
    w = {a: {s: statistics.mean([r[2] for r in by[a] if of(r) == s] or [float("nan")]) for s in strata} for a in by}
    shift = same = 0.0
    for s in strata:
        wn = w["native"][s] if p["native"][s] else w["compass"][s]     # a stratum native never reaches: omni's own wait
        if p["compass"][s] or p["native"][s]:
            shift += (p["compass"][s] - p["native"][s]) * wn
        if p["compass"][s] and p["native"][s]:
            same += p["compass"][s] * (w["compass"][s] - w["native"][s])
    return mean["compass"] - mean["native"], shift, same, mean


def table(rows, title):
    out = [f"### {title}", "", "| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |",
           "|---|---|---|---:|---:|---:|---:|---:|"]
    for arm, label in (("native", "native"), ("compass", "omni")):
        for lo, hi in BANDS:
            for serving in (False, True):
                s = [r for r in rows if r[0] == arm and band(r[6]) == (lo, hi) and r[7] == serving]
                if s:
                    out.append(f"| {label} | {lo:.1f} to {min(hi, 1.0):.1f} | {'already serving' if serving else 'empty'} | {len(s)} | "
                               f"{statistics.mean(r[2] for r in s):.2f} | {statistics.mean(r[3] for r in s):.2f} | "
                               f"{statistics.mean(r[4] for r in s):.2f} | {statistics.mean(r[5] for r in s):.2f} |")
    d = decompose(rows)
    if d:
        dw, shift, same, mean = d
        out += ["", f"Mean wait: native {mean['native']:.2f} s, omni {mean['compass']:.2f} s, ΔW̄ = {dw:+.2f} s "
                f"({100 * dw / mean['native']:+.1f}%). Of it, the shift of starts into other strata (a busier host, an empty node): "
                f"{shift:+.2f} s; the wait in the same stratum: {same:+.2f} s."]
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", nargs="+")
    ap.add_argument("--engine", action="append", default=[], help="RUN=engine label, shown beside the run")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    label = dict(x.split("=", 1) for x in a.engine)
    lines, groups = [], {}
    for run in a.runs:
        r = starts(run)
        eng = label.get(run, "engine not named")
        for row in r:                                       # one table per engine and test: never two tests' starts mixed
            groups.setdefault((eng, row[1]), []).append(row)
        lines.append(f"- `results/live/raw/{run}/`: {len(r)} starts ({eng})")
    body = ["# Where the pod start wait goes: every serving pod's start, phase by phase", "", *receipt_key(), "", OWN_RUNS, "",
            "Read by `tools/pod_phases.py` from the runs' own files (Kubernetes' pod watch and the host's processor record; "
            "evidence class L, the real thing on one GitHub runner). Each serving pod started inside a measured window is split "
            "into scheduling, the node side (the kubelet, the container runtime and the image) and the app with its readiness "
            "probe, and placed by the host's busy share over its start and by whether its node already carried a serving pod. "
            "Every number here is shown, not judged: the judged row is the three-run table's \"pod start wait, mean\". The "
            "mechanism and its physics: `docs/POD_START_WAIT.md`.", "", "## The runs read", ""] + lines + [""]
    for (eng, test), r in groups.items():
        body += table(r, f"{eng}, test {test}: every serving pod started in a measured window") + [""]
    text = "\n".join(_legal_stamp(body))
    if a.out:
        Path(a.out).write_text(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
