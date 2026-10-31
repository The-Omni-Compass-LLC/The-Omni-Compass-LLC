#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The seven organisms with the real cluster inside: fourteen columns, one report.

Reads every bench-<arm>-<rep>/ under DIR that carries organism.json (tools/run_kil.py, started by scripts/kind_bench.sh
with ORGANISM set), groups the runs by organism, and pairs each Omni arm with native by repetition. Each organism gives
two columns, native and native with Omni-Compass on top: seven organisms, fourteen columns.

Two kinds of rows, kept apart:
  the cluster  real Kubernetes, measured (response times from the probe, pods, replicas and CPU from the API server;
               energy from the declared power model; on AKS the bill from Azure's own count of machines)
  the organism the simulated stacks around it (evidence S, models): work, energy, time over the line

Each organism's line names which gauges read GAIN, LOSS or power given against native, by any amount, and which read
STEADY because they are inside the noise (the interval crosses zero). The word is decided by what the gauge is for, never by
the sign of its number (tools/readings.py, the founder's order of 13 October): the organism's work and work per energy are
work done; response times, time over the line and failed requests are time waited, missed or failed; replicas, pods,
machines, energy and the bill are resources spent, so a rise reads power given. CPU and host load are shown, not judged.
No line is drawn.

  python3 tools/six_kube_report.py DIR [DIR ...] [--out FILE.md]   ->  DIR/SIX_KUBE.md and .json (the first DIR), or FILE.md and
  FILE.json; several DIRs when one benchmark's cells were archived from more than one run (the big organisms: the tower from
  the job-bound run, the stack from the detached machine's collection)
"""
from __future__ import annotations

import gzip
import json

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.live_reps import arm_rep, arm_gauges, T95, LABEL, NEUTRAL, SAME_REL  # noqa: E402
from tools.run_hil import NAMES, REALMS  # noqa: E402
from tools.run_realms_v5 import SPINE  # noqa: E402  (the seventh organism, listed first)
from realms.harness import STACK, TOWER, organism_name  # noqa: E402
from tools.readings import word as gel_word, aim as gel_aim, receipt_key, WORK_PER  # noqa: E402  (the words every table uses)

ORDER = [SPINE] + list(REALMS) + [TOWER, STACK]      # the spine first (16 October); a report with the spine in it crashed without it
OMNI = ("compass", "omni")
CLUSTER = ["response time (ms), 95th percentile", "response time (ms), 99th percentile",
           "time over the response line (% of samples)", "failed requests (%)", "HPA replicas, mean", "pods started",
           "worker nodes in service, mean", "energy, parked workers still on at idle power (Wh)", "energy (Wh)",
           "CPU used with Omni's own (cores), mean", "host CPU busy, the real machine under kind (%)",
           "machines billed, machine-hours", "compute bill at list price ($)"]
ORG = ["organism work", "organism energy (J)", "organism time over the line (% of steps)", "organism work per energy",
       "organism behind its window (s)"]
BEHIND = "organism behind its window (s)"                  # shown, not judged: how long after the measured window the organism's
                                                           # last step ended (0 = on the clock); past 5% of the window the cell is off the clock
OFF_CLOCK_SHARE = 0.05
SHOWN = {"host CPU busy, the real machine under kind (%)", BEHIND}
AIM_HIGHER = {"organism work"}
AIM_WORK_PER = {"organism work per energy"}            # work bought per joule: a fall is power given (17 October)


def aim_of(k):
    """What a gauge is for: work done aims higher; a resource spent or held is spent; everything else here is time waited,
    missed or failed (tools/readings.py)."""
    return "higher" if k in AIM_HIGHER else WORK_PER if k in AIM_WORK_PER else gel_aim("lower", k)


def scale_of(key):
    return int(key.split("@")[1]) if "@" in key else 1


def name_of(key):
    """An organism's name, with its size when it runs as more than one copy on one clock."""
    o = organism_name(key.split("@")[0])                     # v1 run folders carry the old count-names
    return NAMES[o] + (f", {scale_of(key):,} copies" if scale_of(key) > 1 else "")


def organism_gauges(rec):
    pl = rec["plants"]
    work = sum(p["work"] for p in pl)
    energy = sum(p["energy_j"] for p in pl)
    steps = sum(p["steps"] for p in pl) or 1
    window = float(rec.get("steps", 0)) * float(rec.get("step_s", 0))
    behind = rec.get("behind_s")
    if behind is None:                                     # older records: the wall time past the window
        behind = max(0.0, float(rec.get("wall_s", window)) - window) if window else float("nan")
    return {"organism work": work, "organism energy (J)": energy,
            "organism time over the line (% of steps)": 100.0 * sum(p["viol"] for p in pl) / steps,
            "organism work per energy": work / energy if energy else float("nan"),
            BEHIND: float(behind), "_window_s": window}


def organism_record(d):
    """The repetition's organism.json, or organism.json.gz where the archive compressed it (a raw file over 50 MB is
    stored gzipped, byte-exact inside, because GitHub refuses a file over 100 MB; .github/workflows/archive-run.yml)."""
    if (d / "organism.json").exists():
        return json.loads((d / "organism.json").read_text())
    if (d / "organism.json.gz").exists():
        return json.loads(gzip.decompress((d / "organism.json.gz").read_bytes()))
    return None


def collect(root, *more):
    """{organism: {arm: {rep: gauges}}}. A repetition is paired within one run only (native and Omni from the same run's
    files, run-<id>/six-<organism>-x<size>-<rep>[-arm]/bench-<arm>-<rep>): a repetition started again after a failed job
    (scripts/dispatch_grid.py) takes the latest run where native and an Omni arm are both valid, never one arm of each."""
    found = {}
    for d in sorted(x for r in (root, *more) for x in Path(r).rglob("bench-*-*")):
        if not d.is_dir() or (d / "INVALID").exists() or not (d / "capture.csv").exists():
            continue
        rec = organism_record(d)
        if rec is None:
            continue
        _, arm, rep = arm_rep(d)
        g = arm_gauges(d)
        g.update(organism_gauges(rec))
        g["_restore_ok"] = rec.get("sim_restore_ok", True)
        sc = int(rec.get("scale", 1))
        org = rec["organism"] if sc == 1 else f"{rec['organism']}@{sc}"
        found.setdefault((org, rep), {}).setdefault(str(d.parent.parent), {})[arm] = g
    runs = {}
    for (org, rep), by_run in found.items():
        whole = [arms for _, arms in sorted(by_run.items()) if "native" in arms and len(arms) > 1]
        for arm, g in (whole[-1] if whole else max(by_run.values(), key=len)).items():
            runs.setdefault(org, {}).setdefault(arm, {})[rep] = g
    return runs


def paired(runs_o, a, k):
    reps = sorted(set(runs_o.get(a, {})) & set(runs_o.get("native", {})))
    xs = [(runs_o["native"][r].get(k, math.nan), runs_o[a][r].get(k, math.nan)) for r in reps]
    xs = [(n, o) for n, o in xs if not (math.isnan(n) or math.isnan(o))]
    if not xs:
        return None
    d = [o - n for n, o in xs]
    nb = sum(n for n, _ in xs) / len(xs); m = sum(d) / len(d)
    if len(d) > 1:
        sd = math.sqrt(sum((x - m) ** 2 for x in d) / (len(d) - 1)); h = T95.get(len(d) - 1, 1.96) * sd / math.sqrt(len(d))
    else:
        h = math.nan
    pct = 100.0 * m / abs(nb) if abs(nb) > 1e-12 else math.nan
    same = abs(m) <= SAME_REL * max(abs(nb), 1e-12)   # under one part in a million of the value is rounding: the same
    w = gel_word(m < 0, aim_of(k))                     # GAIN, LOSS or power given, by what the gauge is for
    # gain: the gauge moved toward its declared aim, for the tools that score the headline (the wiring verdicts, the benefit
    # sheet); word: the row's word whatever the noise (the page marks a change inside the noise STEADY)
    return {"n": len(d), "native": nb, "omni": nb + m, "diff": m, "lo": m - h, "hi": m + h, "pct": pct,
            "gain": w == "GAIN", "word": w, "lower": bool(m < 0), "neutral": k in NEUTRAL, "same": bool(same)}


def main(root, *more, out=None, reps=None):
    root = Path(root)
    runs = collect(root, *more)
    if reps:          # the grid's nested squares: the first N repetitions of every organism (1, 10 and 100 are nested)
        runs = {o: {a: {r: g for r, g in by.items() if int(r) <= reps} for a, by in arms.items()} for o, arms in runs.items()}
    orgs = sorted(runs, key=lambda o: (scale_of(o), ORDER.index(organism_name(o.split("@")[0]))))
    keys = [k for k in CLUSTER + ORG if any(not math.isnan(g.get(k, math.nan)) for o in orgs for arms in runs[o].values()
                                             for g in arms.values())]
    out_json = {"organisms": {}}
    L = ["# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top", "", *receipt_key(), "",
         "Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its "
         "own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own "
         "controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the "
         "cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared "
         "power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).", "",
         *([f"Each square here is its first {reps} repetition{'s' if reps > 1 else ''} (repetitions 1 to {reps}; the grid's "
            "1-, 10- and 100-repetition squares are nested).", ""] if reps else []),
         "How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column "
         "gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: "
         "`docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or "
         "failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, "
         "replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, "
         "never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: "
         "the row \"organism behind its window\" says how long after the window its last step ended (0 is on the clock), and a "
         "repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, "
         "because its last steps saw a cluster whose load schedule had already ended.", "",
         "## Twelve columns, mean over repetitions", ""]
    cols = []
    for o in orgs:
        arm = next((a for a in OMNI if a in runs[o]), None)
        cols += [(o, "native")] + ([(o, arm)] if arm else [])
    L.append("| Gauge | " + " | ".join(f"{name_of(o)}: {'native' if a == 'native' else 'omni'}" for o, a in cols) + " |")
    L.append("|---|" + "---:|" * len(cols))
    for k in keys:
        cells = []
        for o, a in cols:
            v = [g.get(k, math.nan) for g in runs[o][a].values()]
            v = [x for x in v if not math.isnan(x)]
            cells.append(f"{sum(v) / len(v):.4g}" if v else "")
        L.append(f"| {LABEL.get(k, k)} | " + " | ".join(cells) + " |")
    L += ["", "## Each organism: omni against native, paired by repetition", ""]
    for o in orgs:
        arm = next((a for a in OMNI if a in runs[o]), None)
        if not arm or "native" not in runs[o]:
            L += [f"### {name_of(o)}", "", "No paired arms.", ""]
            continue
        rows = {k: paired(runs[o], arm, k) for k in keys}
        rows = {k: v for k, v in rows.items() if v}
        n = max((v["n"] for v in rows.values()), default=0)
        restored = all(g["_restore_ok"] for g in runs[o][arm].values())
        sure = lambda v: v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
        judged = {k: v for k, v in rows.items() if not v["neutral"] and k not in SHOWN and not v["same"]}
        # off the clock: in a repetition where either arm's organism ended more than 5% of the window after it, the
        # organism's last steps saw a cluster whose load schedule had already ended; the pairing stands, the cell is marked
        pairs = set(runs[o][arm]) & set(runs[o]["native"])
        off = sorted({r for a in ("native", arm) for r, g in runs[o][a].items()
                      if r in pairs and g.get("_window_s") and g.get(BEHIND, 0.0) > OFF_CLOCK_SHARE * g["_window_s"]})
        worst = max((g.get(BEHIND, 0.0) for a in ("native", arm) for r, g in runs[o][a].items() if r in pairs), default=0.0)
        by = {w: [LABEL.get(k, k) for k, v in judged.items() if sure(v) and v["word"] == w] for w in ("GAIN", "LOSS", "power given")}
        noise = [LABEL.get(k, k) for k, v in judged.items() if not sure(v)]
        verdict = (", ".join(f"{w} on {len(xs)}" + (f" ({'; '.join(xs)})" if xs else "") for w, xs in by.items())
                   + f", STEADY (inside the noise) on {len(noise)}") if n >= 2 else "ONE REPETITION"
        if not restored:
            verdict += "; INVALID: a simulated knob was not handed back"
        if off:
            verdict += (f"; OFF THE CLOCK in {len(off)} of {n} repetitions (the organism ended up to {worst:,.0f} s after its "
                        f"window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)")
        out_json["organisms"][o] = {"arm": arm, "repetitions": n, "verdict": verdict, "rows": rows, "off_the_clock_reps": off,
                               "behind_max_s": worst}
        L += [f"### {name_of(o)}: {verdict}", "", f"{n} paired repetitions.", "",
              "| Gauge | native | omni | Change | 95% interval of the difference | Reading |", "|---|---:|---:|---:|---:|---|"]
        for k, v in rows.items():
            ch = f"{v['pct']:+.1f}%" if not math.isnan(v["pct"]) else f"{v['diff']:+.3g}"
            ci = f"{v['lo']:+.4g} to {v['hi']:+.4g}" if v["n"] > 1 else ""
            if k == BEHIND:
                rd = "shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock)"
            elif v["neutral"] or k in SHOWN:
                rd = "shown, not judged"
            elif v["same"]:
                rd = "STEADY, the same" if v["diff"] == 0.0 else "STEADY, the same (under one part in a million)"
            else:
                sure = v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
                rd = v["word"] if sure else f"STEADY, inside the noise ({'cut' if v['diff'] < 0 else 'up'})"
            L.append(f"| {LABEL.get(k, k)} | {v['native']:.4g} | {v['omni']:.4g} | {ch} | {ci} | {rd} |")
        L.append("")
    missing = [o for o in ORDER if not any(organism_name(k.split("@")[0]) == o for k in runs)]
    if missing:
        L += ["## Not in this run", ""] + [f"- {name_of(o)}" for o in missing] + [""]
    md = Path(out) if out else root / "SIX_KUBE.md"
    md.write_text("\n".join(_legal_stamp(L)) + "\n")
    md.with_suffix(".json").write_text(json.dumps(out_json, indent=1) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    out = args[args.index("--out") + 1] if "--out" in args else None
    reps = int(args[args.index("--reps") + 1]) if "--reps" in args else None
    dirs = [a for i, a in enumerate(args) if a not in ("--out", "--reps") and (i == 0 or args[i - 1] not in ("--out", "--reps"))]
    sys.exit(main(dirs[0], *dirs[1:], out=out, reps=reps))
