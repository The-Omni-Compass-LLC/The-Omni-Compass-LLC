#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The main engine's tune, searched and checked in our own models (docs/THE_TUNE.md; the founder's order of 22 October,
evening: the benchmarks prove one tuned engine, and that tune is the one found to serve the organism best).

Every tune in a declared grid of the Kubernetes governor's knobs (its beat, the compass's balance point) runs on the model's
plant that moves every 5 s, seed by seed against native and against the main engine's tune, and is read by the one key
(tools/model_gate.reading). The rule, written before the run (docs/THE_TUNE.md, section 3):

  admissible   no gauge reads LOSS against native; in the cloud's setting the machine-hours, the bill, are not above native's
  dominates    against the main tune: no service gauge reads LOSS (in the cloud no rise in the bill), and one at least reads
               GAIN; such a tune is a candidate for the next version, through the model gate, never a change by itself
  ranked       admissible tunes by the service gauges that read GAIN against native, then by their summed improvement

The main tune stands in the searched set when it is admissible and no admissible tune dominates it. Evidence class S,
our own models: the search says which tune the models favour, never what a benchmark found.

  python3 tools/tune_study.py --tree <checkout> --seeds 101-108 --days 1 --jobs 4 --out <dir>
  python3 tools/tune_study.py --judge <dir>/TUNE.json --page results/model_gate/V17_TUNE
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.model_gate import GAUGES, PACE_GAUGES, reading, run  # noqa: E402

# the knobs searched and their values, declared before the run (docs/THE_TUNE.md, section 4); the main tune is one point of
# each grid: the beat the founder set (60 s) and the compass's balance point the dial ships (0.3 at the max, 0.4 at the tune-down)
GRIDS = {"kind": {"beat": [15, 30, 60, 75, 90, 120], "compass-center": [0.2, 0.3, 0.4]},
         "cloud": {"beat": [15, 30, 60, 75, 90, 120], "compass-center": [0.3, 0.4, 0.5]}}
MAIN = {"kind": {"beat": 60, "compass-center": 0.3}, "cloud": {"beat": 60, "compass-center": 0.4}}
WORDS = {"kind": "the kind benchmark's setting: the compass law at the max, every autoscaler sensed",
         "cloud": "the cloud's setting: the compass law on top of the cloud's own autoscaler (the tune-down on the machines alone "
                  "until 31 October; the max from then, the founder's order of that day)"}
# what the organism is served by: time waited, missed or short (the one key's LOSS gauges in this model)
SERVICE = ("pending_pod_minutes_per_hour", "p95_ms", "alert_minutes", "hpa_shortfall_minutes_per_hour")
BILL = "machine_hours"                       # the cloud's aim: the same work for a bill never bigger than native's


def tunes(setting):
    g = GRIDS[setting]
    names = list(g)
    return [dict(zip(names, vals)) for vals in itertools.product(*(g[n] for n in names))]


def key(t):
    return "-".join(f"{k}{v:g}" for k, v in t.items())


def ctl(t):
    """The governor's own arguments for a tune, the beat apart (the model sets it as the period)."""
    return " ".join(f"--{k} {v:g}" for k, v in t.items() if k != "beat")


def collect(tree, settings, seeds, days, jobs, out):
    """Every job of every setting, kept by model_gate.run in its own folder so a stopped study resumes."""
    res = {}
    for setting in settings:
        todo = [("native", None, s) for s in seeds] + [("omni", t, s) for t in tunes(setting) for s in seeds]

        def one(j):
            arm, t, s = j
            name = "native" if t is None else key(t)
            args = ["--worker", arm, "--seed", str(s), "--days", str(days), "--fine", "--setting", setting,
                    "--period", str(60.0 if t is None else float(t["beat"]))]
            if t is not None and ctl(t):
                args += ["--ctl", ctl(t)]
            return name, s, run(tree, args + ["--dir", str(Path(out) / setting / f"{name}-{s}")])
        with ThreadPoolExecutor(jobs) as ex:
            for name, s, r in ex.map(one, todo):
                res.setdefault(setting, {}).setdefault(name, {})[str(s)] = r
    return {"tree": str(Path(tree).resolve()), "seeds": [int(s) for s in seeds], "days": days, "grids": GRIDS, "main": MAIN,
            "per_seed": res}


def judge(study):
    """Each tune of each setting against native and against the main tune, with the rule's verdicts."""
    seeds = [str(s) for s in study["seeds"]]
    out = {}
    for setting, per in study["per_seed"].items():
        native, main_key = per["native"], key(study["main"][setting])
        main = per[main_key]
        aims = SERVICE + ((BILL,) if setting == "cloud" else ())
        rows = {}
        for name, by in per.items():
            if name == "native":
                continue
            vn = {g: reading(g, [by[s][g] - native[s].get(g, 0.0) for s in seeds], [native[s].get(g, 0.0) for s in seeds])
                  for g in GAUGES}
            vm = None if name == main_key else {
                g: reading(g, [by[s][g] - main[s][g] for s in seeds], [main[s][g] for s in seeds], PACE_GAUGES) for g in PACE_GAUGES}
            admissible = all(vn[g]["word"] != "LOSS" for g in GAUGES) and \
                not (setting == "cloud" and vn[BILL]["word"] == "power given")
            dominates = vm is not None and admissible and \
                all(vm[g]["word"] not in ("LOSS", "power given") for g in aims) and any(vm[g]["word"] == "GAIN" for g in aims)
            gains = [g for g in aims if vn[g]["word"] == "GAIN"]
            score = (len(gains), sum(-vn[g]["relative"] for g in gains))
            mean = {g: sum(by[s][g] for s in seeds) / len(seeds) for g in PACE_GAUGES}
            rows[name] = {"tune": next(t for t in tunes(setting) if key(t) == name), "mean": mean, "vs_native": vn,
                          "vs_main": vm, "admissible": admissible, "dominates_main": dominates, "score": score}
        ranked = sorted((n for n in rows if rows[n]["admissible"]), key=lambda n: rows[n]["score"], reverse=True)
        out[setting] = {"main": main_key, "rows": rows, "ranked": ranked,
                        "main_admissible": rows[main_key]["admissible"],
                        "dominating": [n for n in rows if rows[n]["dominates_main"]],
                        "native": {g: sum(native[s].get(g, 0.0) for s in seeds) / len(seeds) for g in GAUGES}}
        out[setting]["stands"] = out[setting]["main_admissible"] and not out[setting]["dominating"]
    return out


SHORT = {"pending_pod_minutes_per_hour": "pods waiting (min an hour)", "p95_ms": "95th percentile (ms)",
         "alert_minutes": "minutes over the line (a day)", "hpa_shortfall_minutes_per_hour": "autoscaler short (min an hour)",
         "machine_hours": "machine-hours (a day)", "kwh_per_core_hour": "energy per core-hour (kWh)"}


def cell(d):
    return "" if d is None else (f"{100 * d['relative']:+.1f}% {d['word']}" if d["relative"] == d["relative"] else d["word"])


def render(study, verdict, out_md):
    from tools.legal import stamp
    lines = ["# The main engine's tune, searched in our own models", "",
             "Every tune in a declared grid of the Kubernetes governor's knobs, run on the model's plant that moves every 5 s, "
             f"seeds {study['seeds'][0]} to {study['seeds'][-1]} (development seeds, kept apart from the gate's 1 to 8), "
             f"{study['days']:g} day each, every tune paired by seed against native and against the main engine's tune and read "
             "by the one key (`tools/model_gate.reading`). The rule was written before the run (`docs/THE_TUNE.md`, section 3): "
             "a tune is admissible when no gauge reads LOSS against native (in the cloud's setting, and no rise in the bill); "
             "it dominates the main tune when, against it, no service gauge reads LOSS (in the cloud no rise in the bill) and "
             "one at least reads GAIN. The main tune stands in the searched set when it is admissible and no admissible "
             "tune dominates it; a tune that dominates it is a candidate for the next version, read in the model gate on the "
             "untouched seeds before anything changes. Evidence class S, our own models: this says which tune the models "
             "favour, never what a benchmark found.", ""]
    for setting, v in verdict.items():
        lines += [f"## {WORDS[setting][0].upper()}{WORDS[setting][1:]}", "",
                  f"The main tune: `{v['main']}`. "
                  + ("**It stands in the searched set**: it is admissible and no admissible tune dominates it." if v["stands"] else
                     ("**It does not stand**: " + ("it is not admissible (a gauge reads LOSS against native). " if not v["main_admissible"] else "")
                      + (f"dominated by {', '.join('`' + n + '`' for n in v['dominating'])}, each a candidate for the next version, "
                         "the model gate first." if v["dominating"] else ""))), "",
                  "| Tune | Admissible | Dominates the main tune | Reads a day | " + " | ".join(SHORT[g] for g in SHORT) +
                  " | Against the main tune, service |", "|---|---|---|---:|" + "---|" * len(SHORT) + "---|"]
        aims = SERVICE + ((BILL,) if setting == "cloud" else ())
        order = v["ranked"] + [n for n in v["rows"] if n not in v["ranked"]]
        for n in order:
            r = v["rows"][n]
            name = f"**{n} (main)**" if n == v["main"] else n
            lines.append(f"| {name} | {'yes' if r['admissible'] else 'no'} | {'yes' if r['dominates_main'] else '—' if n == v['main'] else 'no'} | "
                         f"{24 * r['mean']['reads_per_hour']:,.0f} | " + " | ".join(cell(r["vs_native"][g]) for g in SHORT) + " | "
                         + ("" if r["vs_main"] is None else "; ".join(f"{SHORT[g].split(' (')[0]} {cell(r['vs_main'][g])}" for g in aims)) + " |")
        lines += ["", "Admissible tunes in rank order (the service gauges that read GAIN against native, then their summed "
                  "improvement): " + ", ".join(f"`{n}`" for n in v["ranked"]) + ".", ""]
    lines += ["Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    Path(out_md).write_text("\n".join(stamp(lines)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tree", help="the checkout whose engine is tuned")
    ap.add_argument("--settings", default="kind,cloud")
    ap.add_argument("--seeds", default="101-108", help="development seeds, kept apart from the gate's 1 to 8")
    ap.add_argument("--days", type=float, default=1.0)
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--out", help="the study's folder: every job's reading is kept there and TUNE.json written")
    ap.add_argument("--judge", help="a TUNE.json to judge and write as a page (with --page)")
    ap.add_argument("--page", help="path without extension: writes <page>.json and <page>.md")
    a = ap.parse_args(argv)
    if a.judge:
        study = json.loads(Path(a.judge).read_text())
    else:
        lo, _, hi = a.seeds.partition("-")
        seeds = list(range(int(lo), int(hi or lo) + 1))
        study = collect(a.tree, a.settings.split(","), seeds, a.days, a.jobs, a.out)
        Path(a.out, "TUNE.json").write_text(json.dumps(study, indent=1))
    verdict = judge(study)
    for setting, v in verdict.items():
        print(f"{setting}: main {v['main']} {'stands' if v['stands'] else 'does not stand'}; "
              f"dominating {v['dominating'] or 'none'}; ranked {', '.join(v['ranked'][:5])}")
    if a.page:
        page = Path(a.page)
        page.with_suffix(".json").write_text(json.dumps({"study": {k: study[k] for k in ("tree", "seeds", "days", "grids", "main")},
                                                         "verdict": verdict}, indent=1, default=list) + "\n")
        render(study, verdict, page.with_suffix(".md"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
