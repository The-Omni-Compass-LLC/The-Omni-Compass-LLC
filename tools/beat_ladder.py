#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The heartbeat dial in our own models: every beat of the Kubernetes governor beside native and beside the main engine's
60 s (omni-v17, the founder's order of 22 October).

Reads the pace studies' reports (`tools/model_gate.py --models pace_cloud,pace_kind --pace-periods 60,...`, each a MODEL_GATE.json
whose first period is 60 s), checks that what two reports share reads the same seed by seed (native and the 60 s beat, on
every gauge the models compute; the governor's own processor is a measured time and is paired only inside its own report),
and pairs every beat by seed against the 60 s beat of its own report and against native (`tools/model_gate.reading`, the one
key). Writes the page and its JSON. Evidence class S, our own models, never a benchmark result.

  python3 tools/beat_ladder.py results/model_gate/V16_PACE.json <ladder>/MODEL_GATE.json --out results/model_gate/V17_LADDER
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.model_gate import GAUGES, PACE_GAUGES, reading  # noqa: E402

MAIN = "60"                                  # the main engine's beat, the reference of every pace report
MEASURED = ("governor_cpu_s_per_hour",)      # timed on the machine that ran the report, never compared across reports


def same(a, b) -> bool:
    """One modelled reading in two reports: equal, a float to the twelfth digit (a long sum of moves, the power cap's travel,
    differs in its last bits between Python 3.11's float sum and 3.12's compensated one)."""
    if isinstance(a, float) or isinstance(b, float):
        return isinstance(b, (int, float)) and isinstance(a, (int, float)) and math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-12)
    return a == b
SETTINGS = (("pace_cloud", "cloud", "the cloud's setting: the compass law on top of the cloud's own autoscaler (the ladder of 22 and "
                                    "23 October read it at the tune-down on the machines alone, the cloud's rule of 14 October; from "
                                    "31 October, the founder's order of that day, the max with every muscle, the bill judged)"),
            ("pace_kind", "kind", "the kind benchmark's setting: the compass law at the max, every autoscaler sensed, on the plant with "
                                  "the cloud's own autoscaler (from 31 October the same model as the cloud's at the max, "
                                  "docs/PACE_PREREGISTRATION.md amendment 5)"))
NAMES = {"machine_hours": "Machine hours (a day)", "kwh_per_core_hour": "Energy per core-hour (kWh)",
         "pending_pod_minutes_per_hour": "Pods waiting for a place (minutes an hour)",
         "hpa_shortfall_minutes_per_hour": "Pod autoscaler short of its target (minutes an hour)",
         "p95_ms": "95th percentile response (ms)", "alert_minutes": "Minutes over the line (a day)",
         "power_cap_moves": "Power-cap request: moves (a day)", "power_cap_reversals": "Power-cap request: reversals (a day)",
         "power_cap_travel": "Power-cap request: travel (a day)", "governor_cpu_s_per_hour": "Omni's own processor (s an hour)",
         "reads_per_hour": "Reads of the cluster (an hour)"}
SUMMARY = ("pending_pod_minutes_per_hour", "p95_ms", "alert_minutes", "hpa_shortfall_minutes_per_hour", "machine_hours",
           "kwh_per_core_hour")


def beat_key(per) -> str:
    return f"{float(per):g}"


def merge(reports):
    """{model: {"native" | beat: (report index, {seed: gauges})}} and the seeds; a beat two reports share must read the same
    on every seed and every modelled gauge, else the reports are not one ladder and nothing is written."""
    out, seeds = {}, None
    for i, rep in enumerate(reports):
        s = [str(x) for x in rep["seeds"]]
        if seeds is None:
            seeds = s
        elif s != seeds:
            raise SystemExit(f"the reports ran different seeds: {seeds} and {s}")
        for model, _, _ in SETTINGS:
            t = rep["models"][model]
            if t["reference"] != MAIN:
                raise SystemExit(f"{model} in report {i + 1} is read against {t['reference']} s, not the main engine's {MAIN} s")
            for key, by_seed in t["per_seed"].items():
                have = out.setdefault(model, {}).get(key)
                if have is not None:
                    for s_ in seeds:
                        a, b = have[1][s_], by_seed[s_]
                        diff = [g for g in a if g not in MEASURED and not same(a[g], b.get(g))]
                        if diff:
                            raise SystemExit(f"{model}: {key} on seed {s_} reads differently in two reports ({', '.join(diff)})")
                    continue
                out[model][key] = (i, by_seed)
    return out, seeds


def ladder(reports):
    """Every beat of every report, each paired by seed against its own report's 60 s beat and against native."""
    merged, seeds = merge(reports)
    models = {}
    for model, setting, _ in SETTINGS:
        beats = sorted((k for k in merged[model] if k != "native"), key=float)
        native = merged[model]["native"][1]
        rows = {}
        for b in beats:
            i, got = merged[model][b]
            ref = reports[i]["models"][model]["per_seed"][MAIN]
            r = {}
            for g in PACE_GAUGES:
                pv = [got[s_][g] for s_ in seeds]
                rv = [ref[s_][g] for s_ in seeds]
                nv = [native[s_].get(g, 0.0) for s_ in seeds]
                r[g] = {"value": sum(pv) / len(pv), "main": sum(rv) / len(rv), "native": sum(nv) / len(nv),
                        "vs_main": None if b == MAIN else reading(g, [p - q for p, q in zip(pv, rv)], rv, PACE_GAUGES),
                        "vs_native": reading(g, [p - n for p, n in zip(pv, nv)], nv, PACE_GAUGES) if g in GAUGES else None}
            rows[b] = r
        counts = {}
        for rep in reports:
            for k, v in rep["models"][model]["counts"].items():
                for b, n in v.items():
                    counts.setdefault(k, {}).setdefault(beat_key(b), n)
        models[model] = {"setting": setting, "beats": beats, "rows": rows,
                     "native": {g: sum(native[s_].get(g, 0.0) for s_ in seeds) / len(seeds) for g in PACE_GAUGES},
                     "counts": {k: {b: v[b] for b in beats if b in v} for k, v in counts.items()},
                     "per_seed": {"native": native, **{b: merged[model][b][1] for b in beats}},
                     "report_of_beat": {b: merged[model][b][0] for b in beats}}
    return {"seeds": [int(s) for s in seeds], "days": reports[0]["days"], "main_s": float(MAIN), "models": models}


def _cell(d):
    """A change beside its word, wearing the word's sign (the founder's sign rule, tools/readings.py `by_word`)."""
    if d is None:
        return ""
    from tools.readings import by_word
    return f"{by_word(100 * d['relative'], d['word'], digits=2)} {d['word']}" if d["relative"] == d["relative"] else d["word"]


def _num(x, g):
    return f"{x:.4f}" if g == "kwh_per_core_hour" else f"{x:,.2f}"


def render(lad, sources, out_md):
    from tools.legal import stamp
    seeds = lad["seeds"]
    lines = ["# The heartbeat dial in our own models: every beat beside native and beside the main engine's 60 s", "",
             "The Kubernetes governor's full decision, its heartbeat, is a dial from omni-v17 on (`docs/OMNI_V17.md`; the "
             "founder's order of 22 October): any beat can be set, the main engine ships at 60 s, and every beat is shown "
             "beside native with what it buys and what it costs, because an operator may want a fast beat for its reads and "
             "accept what it costs, or a slow one, and each beat may want its own combination of the other knobs. This page "
             "reads the beats in our own models (evidence class S): the engine alone on a plant that moves every 5 s (the model "
             "cluster's step cut to 5 s), the fast checks every 5 s at every beat, "
             f"seeds {seeds[0]} to {seeds[-1]}, {lad['days']:g} day each, the same seeds and plant at every beat. Each beat is "
             "paired by seed against the main engine's 60 s and against native (the mean change, its 95% interval over the "
             "seeds, the word by the gauge's aim: `tools/readings.py`). A reading here says what a beat does in a model, never "
             "what a benchmark found; the real runs at every beat are `docs/PACE_PREREGISTRATION.md`, amendment 3.", "",
             "Built by `tools/beat_ladder.py` from " + " and ".join(f"`{s}`" for s in sources) + ". What two of them share "
             "(native and the 60 s beat) reads the same seed by seed on every modelled gauge, to the twelfth digit (the power "
             "cap's travel, a long sum of moves, differs in its last bits between Python 3.11's float sum and 3.12's); Omni's "
             "own processor is timed on the machine that ran each report, so each beat's processor is read against the 60 s "
             "beat of its own report.",
             ""]
    # the settings this record carries (31 October: at the max one model reads the cloud's and the kind benchmark's, so a
    # record may hold one; tools/model_reread.py renders a record without main()'s filter)
    present = [s for s in SETTINGS if s[0] in lad["models"]]
    for model, setting, words in present:
        t = lad["models"][model]
        beats = t["beats"]
        name = lambda b: f"every {b} s" + (" (the main engine)" if b == MAIN else "")
        lines += [f"## {words[0].upper()}{words[1:].split(':')[0]}", "", f"{words[0].upper()}{words[1:]}.", "",
                  "What each beat buys and what it costs, against native (the value, then the word):", "",
                  "| Beat | Reads a day | Omni's own processor (s an hour) | " + " | ".join(NAMES[g] for g in SUMMARY) + " |",
                  "|---|---:|---:|" + "---:|" * len(SUMMARY)]
        nat = t["native"]
        lines.append("| native | | | " + " | ".join(_num(nat[g], g) for g in SUMMARY) + " |")
        for b in beats:
            r = t["rows"][b]
            lines.append(f"| {name(b)} | {24 * r['reads_per_hour']['value']:,.0f} | {r['governor_cpu_s_per_hour']['value']:.2f} | "
                         + " | ".join(f"{_num(r[g]['value'], g)} {r[g]['vs_native']['word']}" for g in SUMMARY) + " |")
        lines += ["", "Each beat against the main engine's 60 s:", "",
                  "| Beat | Reads a day | Omni's own processor | " + " | ".join(NAMES[g] for g in SUMMARY) + " |",
                  "|---|---|---|" + "---|" * len(SUMMARY)]
        for b in beats:
            if b == MAIN:
                continue
            r = t["rows"][b]
            lines.append(f"| {name(b)} | {_cell(r['reads_per_hour']['vs_main'])} | {_cell(r['governor_cpu_s_per_hour']['vs_main'])} | "
                         + " | ".join(_cell(r[g]["vs_main"]) for g in SUMMARY) + " |")
        lines.append("")
        for b in beats:
            r = t["rows"][b]
            lines += [f"### {name(b)[0].upper()}{name(b)[1:]}", ""]
            if b == MAIN:
                lines += ["| Gauge | Native | Every 60 s | Against native |", "|---|---:|---:|---|"]
                lines += [f"| {NAMES[g]} | {_num(x['native'], g)} | {_num(x['value'], g)} | {_cell(x['vs_native'])} |"
                          for g, x in r.items()]
            else:
                lines += [f"| Gauge | Native | Every 60 s | Every {b} s | Against every 60 s | Against native |",
                          "|---|---:|---:|---:|---|---|"]
                lines += [f"| {NAMES[g]} | {_num(x['native'], g)} | {_num(x['main'], g)} | {_num(x['value'], g)} | "
                          f"{_cell(x['vs_main'])} | {_cell(x['vs_native'])} |" for g, x in r.items()]
            lines.append("")
        lines += ["Counts over all seeds, by beat: " + "; ".join(
            f"{k} " + ", ".join(f"{b} s {v[b]:,}" for b in beats if b in v) for k, v in t["counts"].items()), ""]
    first = lad.get("first")
    if first:                                  # the reading that caught a fault, kept beside the corrected beats
        lines += [f"## The first reading of every {' and '.join(first['beats'])} s, before the fix", "", first["note"], "",
                  f"From `{first['source']}`; its native and 60 s read the same as this page's, seed by seed.", ""]
        for model, setting, words in [s for s in present if s[0] in first["models"]]:
            lines += [f"{words[0].upper()}{words[1:].split(':')[0]}, against native and against 60 s:", "",
                      "| Beat | " + " | ".join(NAMES[g] for g in SUMMARY) + " |", "|---|" + "---|" * len(SUMMARY)]
            for b in first["beats"]:
                r = first["models"][model][b]
                lines.append(f"| every {b} s, first | " + " | ".join(
                    f"{_num(r[g]['value'], g)}: {_cell(r[g]['vs_native'])}; {_cell(r[g]['vs_main'])}" for g in SUMMARY) + " |")
            lines.append("")
    lines += ["Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    Path(out_md).write_text("\n".join(stamp(lines)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("reports", nargs="+", help="pace reports (MODEL_GATE.json), each read against 60 s")
    ap.add_argument("--out", required=True, help="path without extension: writes <out>.json and <out>.md")
    ap.add_argument("--source-names", nargs="*", help="how the page names each report (default: its path)")
    ap.add_argument("--first", help="a report holding the first reading of beats a fix changed, kept on the page beside them")
    ap.add_argument("--first-beats", default="", help="those beats, comma separated (e.g. 90,120)")
    ap.add_argument("--first-name", help="how the page names that report (default: its path)")
    ap.add_argument("--first-note", default="", help="what the fix was and why the first reading is kept")
    a = ap.parse_args(argv)
    reports = [json.loads(Path(p).read_text()) for p in a.reports]
    # a report may carry one setting only (31 October: at the max the cloud's setting and the kind benchmark's are one model,
    # docs/PACE_PREREGISTRATION.md amendment 5, so one ladder reads both): the page writes the settings every report carries
    global SETTINGS
    SETTINGS = tuple(s for s in SETTINGS if all(s[0] in r["models"] for r in reports))
    if not SETTINGS:
        raise SystemExit("no pace setting is in every report")
    lad = ladder(reports)
    lad["sources"] = a.source_names or a.reports
    if a.first:
        rep = json.loads(Path(a.first).read_text())
        beats = [beat_key(b) for b in a.first_beats.split(",") if b.strip()]
        for model, _, _ in SETTINGS:             # the same native and 60 s as the ladder's, or it is not the same plant
            for key in ("native", MAIN):
                ours = lad["models"][model]["per_seed"][key]
                for s_ in ours:
                    a_, b_ = ours[s_], rep["models"][model]["per_seed"][key][s_]
                    if any(g not in MEASURED and not same(a_[g], b_.get(g)) for g in a_):
                        raise SystemExit(f"{model}: the first reading's {key} on seed {s_} differs from the ladder's")
        fl = ladder([rep])
        lad["first"] = {"source": a.first_name or a.first, "note": a.first_note, "beats": beats,
                        "models": {model: {b: fl["models"][model]["rows"][b] for b in beats} for model, _, _ in SETTINGS}}
    out = Path(a.out)
    out.with_suffix(".json").write_text(json.dumps(lad, indent=1) + "\n")
    render(lad, lad["sources"], out.with_suffix(".md"))
    for model, t in lad["models"].items():
        print(f"{model}: beats {', '.join(t['beats'])} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
