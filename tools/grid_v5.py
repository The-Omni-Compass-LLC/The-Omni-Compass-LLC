# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The grid of the card version, every square in one page (results/grid_v5/GRID.md), built from the pooled receipts the
archive keeps: the seven organisms at 1, 10, 100 and 500 copies on one clock, each at its first 1, 10, 100 and 500 runs (nested),
native against Omni-Compass on top, twice: modelled (six.yml, pooled by six-pool: SIX_v5-x<size>.json) and with the real
Kubernetes cluster inside (six-kube.yml, pooled by six-kube-pool: SIX_KUBE_v5-x<size>_r<n>.json). Nothing is
recomputed here: every cell is the pooled receipt's own reading, and each half names the runs it was pooled from.

  python3 tools/grid_v5.py --modelled DIR [DIR ...] [--kube DIR [DIR ...]] --out results/grid_v5/GRID.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp                                   # noqa: E402
from tools.readings import OWN_RUNS, receipt_key, GAIN, LOSS, GIVEN, word, aim, labelled, WORK_PER, SPENT   # noqa: E402  (the words every table uses)

ORGS = ["spine", "compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized",
        "stack", "tower"]          # the seven organisms, the spine (the base every stack runs on) first
NAMES = {"spine": "The spine", "compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
         "stack": "The four stacked", "tower": "The whole tower"}
SIZES, RUNS = (1, 10, 100, 500), ("1", "10", "100", "500")   # the ladder of the Python's 500-run Monte Carlo (25 October)
copies = lambda n: f"{n} cop{'y' if int(n) == 1 else 'ies'}"


def run_of(path):
    """The GitHub run an archived receipt came from (results/live/raw/run-<id>/...)."""
    return next((p.name[4:] for p in Path(path).resolve().parents if p.name.startswith("run-")), "?")


def where(f):
    """A receipt's page (its .md beside the .json), as the repository names it."""
    f = Path(f).resolve().with_suffix(".md")
    return f.relative_to(ROOT).as_posix() if f.is_relative_to(ROOT) else f.name


from tools.repo import RAW as RAW_BRANCH  # noqa: E402  (the raw receipts' own branch, on the repository's name written once)


def link(md, out_dir):
    """A link to a receipt's page from the grid page: the repository's name for it, and the path from the page's folder;
    a receipt archived on the branch raw (results/live/raw/... when opened) links to that branch."""
    name = where(md)
    if name.startswith("results/live/raw/"):
        return f"[`{name}`]({RAW_BRANCH}{name[len('results/live/raw/'):]})"
    return f"[`{name}`]({Path(os.path.relpath(md, out_dir)).as_posix()})"


def modelled(dirs):
    """{size: (receipt, run id, page)} from every SIX_v5-x<size>.json under the given folders."""
    out = {}
    for d in dirs:
        for f in Path(d).rglob("SIX_v5-x*.json"):
            rec = json.loads(f.read_text())
            out[int(rec["scale"])] = (rec, run_of(f), f.resolve().with_suffix(".md"))
    return out


def kube(dirs):
    """{(size, runs): (report, run id, page)} from every SIX_KUBE_v5-x<size>_r<n>.json under the given folders."""
    out = {}
    for d in dirs:
        for f in Path(d).rglob("SIX_KUBE_v5-x*_r*.json"):
            size, n = f.stem.split("-x", 1)[1].split("_r")
            out[(int(size), n)] = (json.loads(f.read_text()), run_of(f), f.resolve().with_suffix(".md"))
    return out


def model_cell(s):
    if not s:
        return "not in the receipt"
    m, w, e = s["viol_pp"][0], 100 * s["work"][0], 100 * s["energy"][0]
    lab = labelled(s["label"])
    return f"{lab}: misses {m:+.3f} pp, work {w:+.3f}%, power given {e:+.3f}% ({s['runs']} of {s['of']} runs)"


SHOWN = {"host CPU busy, the real machine under kind (%)", "organism behind its window (s)"}   # tools/six_kube_report.py
AIM_HIGHER = {"organism work"}                                                                    # tools/six_kube_report.py
AIM_WORK_PER = {"organism work per energy"}                                                        # tools/six_kube_report.py
WORDS = (GAIN, LOSS, GIVEN)


def aim_of(k):
    """What a gauge of a square is for: work done aims higher; a resource spent or held is spent; the rest is time waited,
    missed or failed (tools/readings.py)."""
    return "higher" if k in AIM_HIGHER else WORK_PER if k in AIM_WORK_PER else aim("lower", k)


def directions(o):
    """A square's gauges by their word against native, from its rows (never from a reading's words): ({GAIN: [...], LOSS:
    [...], power given: [...]}, the count inside the noise). A gauge counts when it is judged (not shown-only, not the same to
    rounding) and its 95% interval is clear of zero; its word is decided by what it is for, never by its sign."""
    by, noise = {w: [] for w in WORDS}, 0
    for k, v in (o.get("rows") or {}).items():
        if v.get("neutral") or k in SHOWN or v.get("same"):
            continue
        if v.get("n", 0) > 1 and (v["lo"] > 0 or v["hi"] < 0):
            by[word(v["diff"] < 0, aim_of(k))].append(k)
        else:
            noise += 1
    return by, noise


def kube_verdict(o):
    """The square's line in GAIN, STEADY and LOSS, with the report's own facts kept (off the clock, invalid)."""
    if o["repetitions"] < 2:
        return "ONE REPETITION"
    by, noise = directions(o)
    facts = "".join("; " + f for f in re.findall(r"; ((?:OFF THE CLOCK|INVALID)[^;]*)", o["verdict"]))   # kept as recorded
    return (", ".join(f"{w} on {len(xs)}" + (f" ({'; '.join(xs)})" if xs else "") for w, xs in by.items())
            + f", STEADY (inside the noise) on {noise}" + facts)


def kube_cell(o):
    if not o:
        return "not in the report"
    if o["repetitions"] < 2:
        return "ONE REPETITION"
    return f"{o['repetitions']} repetitions: {kube_verdict(o)}"


def kube_key(org, size):
    return org if size == 1 else f"{org}@{size}"


def rng(xs):
    lo, hi = f"{min(xs):+.3f}%", f"{max(xs):+.3f}%"
    return lo if lo == hi else f"{lo} to {hi}"


HOST, FAILED, SVC_CPU = ("host CPU busy, the real machine under kind (%)", "failed requests (%)",
                         "CPU used with Omni's own (cores), mean")


def machine_note(kub):
    """The test machine at each size, from native's own rows (the most repetitions each size has): how busy the machine
    under the cluster was, native's own failed requests, the cluster's CPU in Omni's arm against native, the repetitions
    off the window's clock. At the size where the machine runs out, the squares read the machine, not the governor."""
    by_size = {}
    for (size, n), (rep, _, _) in kub.items():
        if size not in by_size or int(n) > int(by_size[size][0]):
            by_size[size] = (n, rep)
    rng_ = lambda xs, f="{:.0f}": (f.format(min(xs)) if f.format(min(xs)) == f.format(max(xs)) else f"{f.format(min(xs))} to {f.format(max(xs))}")
    rows_ = []
    for size in sorted(by_size):
        n, rep = by_size[size]
        orgs = (rep.get("organisms") or {}).values()
        host = [o["rows"][HOST]["native"] for o in orgs if HOST in o.get("rows", {})]
        fail = [o["rows"][FAILED]["native"] for o in orgs if FAILED in o.get("rows", {})]
        cpu = [o["rows"][SVC_CPU]["pct"] for o in orgs if SVC_CPU in o.get("rows", {})]
        off = [(name_of_square(k), re.search(r"OFF THE CLOCK in (\d+) of (\d+)", o["verdict"])) for k, o in (rep.get("organisms") or {}).items()]
        off = [f"{nm} {m.group(1)} of {m.group(2)}" for nm, m in off if m]
        if host and fail and cpu:
            rows_.append(f"| {copies(size)} ({n} repetitions) | {rng_(host)}% | {rng_(fail)}% | {rng_(cpu, '{:+.1f}')}% | "
                         f"{', '.join(off) or 'none'} |")
    if not rows_:
        return []
    return ["### The test machine at each size", "",
            "Native's own numbers on GitHub's four-core machine, which runs the real cluster, the model of the organism and, "
            "in Omni-Compass's arm, Omni-Compass's math for every modelled muscle, all at once:", "",
            "| Size | Machine busy (native) | Failed requests (native) | The cluster's CPU, Omni-Compass's arm against native | Off the window's clock |",
            "|---|---:|---:|---:|---|", *rows_, "",
            "The load is the same at every size; what grows with the copies is the model on the same four cores. Where the "
            "machine runs out, native's own failed requests rise with it, the cluster gets less CPU in the arm whose model "
            "also carries Omni-Compass's math, and the largest organisms fall behind the window's clock, so their last steps "
            "no longer follow the scheduled load: those squares read the test machine's limit, not Omni-Compass governing a "
            "cluster. They run again on the rewired test, the model on cores of its own.", ""]


def name_of_square(k):
    org = k.split("@")[0]
    return NAMES.get(org, org)


def across(data):
    """The grid in one line, counted from the squares themselves (the front page's reading of this table)."""
    sq = [s for cells in data["modelled"].values() for n, s in cells.items() if s]
    labs = Counter(labelled(s["label"]) for s in sq if s["runs"] >= 2)
    one = [s for s in sq if s["runs"] < 2]
    pg = [100 * s["energy"][0] for s in sq]
    parts = []
    if sq:
        parts.append("modelled, " + ", ".join(f"{c} of {sum(labs.values())} squares of 10 or more runs {lab}"
                                               for lab, c in labs.most_common())
                     + f"; the {len(one)} single runs: {sum(1 for s in one if s['viol_pp'][0] < 0)} with fewer misses"
                     + f"; work {rng([100 * s['work'][0] for s in sq])}; power given {rng(pg)}")
    ks = [o for cells in data["kube"].values() for o in cells.values() if o]
    if ks:
        judged = [o for o in ks if o["repetitions"] >= 2]
        cnt = {w: Counter(g for o in judged for g in o[w]) for w in WORDS}
        gauges = sorted(set().union(*cnt.values()), key=lambda g: (-sum(cnt[w][g] for w in WORDS), g))
        away = lambda g: GIVEN if aim_of(g) in (SPENT, WORK_PER) else LOSS        # the word a gauge reads when it moves away from its aim
        parts.append(f"with the cluster inside, {len(ks)} squares: {len(ks) - len(judged)} single repetitions (no reading); "
                     f"of the {len(judged)} of 10 or more repetitions, by gauge: "
                     + (", ".join(f'"{g}" GAIN in {cnt[GAIN][g]}, {away(g)} in {cnt[away(g)][g]}' for g in gauges)
                        or "no gauge clear of the noise")
                     + f"; off the clock in {sum(1 for o in ks if 'OFF THE CLOCK' in o['verdict'])}"
                     + f"; invalid in {sum(1 for o in ks if 'INVALID' in o['verdict'])}")
    return "**Across the grid: " + ("; ".join(parts) or "no squares") + ".**"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--modelled", nargs="+", required=True)
    ap.add_argument("--kube", nargs="*", default=[])
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    mod, kub = modelled(a.modelled), kube(a.kube)
    out = Path(a.out)
    od = out.resolve().parent
    L = ["# The grid of the card version: seven organisms at 1, 10, 100 and 500 copies, each at 1, 10, 100 and 500 runs", "", *receipt_key(), "",
         "Native against Omni-Compass on top of native, engine omni-v5 (digest 5648f290, every muscle its own card), work "
         "waiting in line in every organism. Each square is the pooled receipt's own reading; the 1-, 10- and 100-run "
         "squares of a size are nested (the first N runs). Every square is shown.", "",
         "How to read a modelled square: its reading, GAIN, STEADY or LOSS (one run carries no label; at 10, 100 and 500 runs the "
         "receipt's own label, its word first), then the change Omni-Compass made against native, averaged over the runs: "
         "misses, the share of time the plants were over their own line, in percentage points (a minus is fewer misses, a "
         "GAIN); work done, in percent; power given, the energy the max took for it, in percent (shown, never called a loss). "
         "A square with the cluster inside carries the report's verdict and the repetitions it pooled. The key to the words: "
         "`docs/HOW_TO_READ_THE_RESULTS.md`.", "", OWN_RUNS, ""]
    top = len(L)                                                 # the grid in one line goes here, once every square is read
    L += ["## Modelled (six.yml; evidence class S, our own models)", "",
          "Pooled receipts: " + ", ".join(f"{copies(s)}: run {mod[s][1]}" for s in sorted(mod)) + ". Every column of every "
          "square (the intervals, the band, the knobs handed back): " + ", ".join(link(mod[s][2], od) for s in sorted(mod))
          + ".", ""]
    data = {"modelled": {}, "kube": {}}
    for size in SIZES:
        rec = mod.get(size, (None,))[0]
        L += [f"### {copies(size)}", "", "| Organism | " + " | ".join(f"{n} run" + ("" if n == "1" else "s") for n in RUNS) + " |", "|---" * (len(RUNS) + 1) + "|"]
        for org in ORGS:
            cells = [model_cell((rec or {}).get("summary", {}).get(n, {}).get(org)) for n in RUNS]
            data["modelled"][f"{org}@{size}"] = {n: (rec or {}).get("summary", {}).get(n, {}).get(org) for n in RUNS}
            L.append(f"| {NAMES[org]} | " + " | ".join(cells) + " |")
        L.append("")
    if kub:
        L += ["## With the real Kubernetes cluster inside (six-kube.yml; the cluster measured, class L; the organism "
              "modelled, class S)", "",
              "Pooled reports: " + ", ".join(f"{copies(s)}: run {r}" for s, r in sorted({(s, r) for (s, _), (_, r, _) in kub.items()}))
              + ". Every gauge of every square, with its interval: " + ", ".join(link(kub[k][2], od) for k in sorted(kub, key=lambda k: (k[0], int(k[1]))))
              + ".", "",
              "How to read a square with the cluster inside: which gauges read GAIN, LOSS or power given against native, each "
              "only when its 95% interval is clear of zero (the rest are STEADY, inside the noise), read from the report's own "
              "rows (`tools/six_kube_report.py`) and judged by what each gauge is for, never by its sign: the cluster's response "
              "times, time over the response line and failed requests are time waited, missed or failed; the organism's work is "
              "work done; pods started, replicas, machines, declared energy and the organism's energy are resources spent, so a "
              "fall is a cut, a GAIN, and a rise is power given, and the organism's work per energy that fell is power given too "
              "(it falls when more power is given for the same work). The modelled receipts above show the power "
              "given beside the work. OFF THE CLOCK marks the repetitions where the organism ended more than 5% of the window late, "
              "its last steps seeing a cluster whose load schedule had ended: the runner could not step that many muscles in "
              "time.", ""]
        for size in SIZES:
            L += [f"### {copies(size)}", "", "| Organism | " + " | ".join(f"{n} run" + ("" if n == "1" else "s") for n in RUNS) + " |", "|---" * (len(RUNS) + 1) + "|"]
            for org in ORGS:
                cells = []
                for n in RUNS:
                    rep = kub.get((size, n), (None,))[0]
                    o = ((rep or {}).get("organisms") or {}).get(kube_key(org, size))
                    data["kube"].setdefault(f"{org}@{size}", {})[n] = o and {
                        "repetitions": o["repetitions"], "verdict": kube_verdict(o), "recorded_verdict": o["verdict"],
                        **directions(o)[0], "rows": o.get("rows") or {}}
                    cells.append(kube_cell(o))
                L.append(f"| {NAMES[org]} | " + " | ".join(cells) + " |")
            L.append("")
    if kub:
        L += machine_note(kub)
    L[top:top] = [across(data), ""]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")
    out.with_suffix(".json").write_text(json.dumps(data, indent=1) + "\n")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
