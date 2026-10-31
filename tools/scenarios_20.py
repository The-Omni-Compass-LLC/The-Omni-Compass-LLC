# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The twenty scenarios: ten organisms, each native and with Omni-Compass on top of native, read by the one key.

The founder's words of 24 October set the organisms ("We have 4 realms ... the 4 realms stacked ... the spine of the 4 realms
... Then we have the whole thing native. And with OmniCompass on native ... 9 to 10 different organisms"); his order of 25
October took the third way out ("we don't need an omnicompass by itself ... Never is going to omnicompass be by itself. It
needs muscles somewhere, somehow"): Omni-Compass always sits on top of a native controller, so every organism runs two
ways, ten organisms by two, twenty scenarios.

The ten organisms, in this order:
  1  the spine                    every muscle in all four realms (tools/run_realms_v5.py spine_rows)
  2-5 the four realms             Compute / AI / Cloud; Physics / Robotics / Autonomous; Energy / Facility / Industrial;
                                  Distribution / Specialized
  6  the four stacked             each realm's own body on one clock (tools/run_realms_v5.py organism_run, STACK)
  7  the whole tower              every catalog muscle once (realms/catalog_v5.csv)
  8  the orchestra                the governors' and orchestrators' muscles, every one once (tools/run_orchestra.py bodies)
  9  the live benchmark engine's organism   the sixty muscles the live benchmark engine page draws (docs/engine/export_harness_trace.py)
  10 the whole organism           three sectors (the software, the cloud as the wire, the bare metal / the data center),
                                  a composition of the real tables (results/WHOLE_SYSTEM.json, regrouped by
                                  docs/engine/export_whole.py)

The two arms, on the same seeds (the same demand, weather and disturbances in both):
  native     Omni-Compass off: every plant under its own native controller (realms/harness.py run_bodies, arm native)
  on_native  Omni-Compass on native: the max (realms/compass_arm_v5.py, V5CFG), the factory tune, on top of every native
             controller (arm v5, as tools/run_realms_v5.py runs it)

Organisms 1-8 run here, under the climb (realms/harness.py CLIMB: the load stepping by one, 1 2 3 2 3 4 ..., level 4 the
organism's own load, 8 twice it), on run_bodies exactly as tools/run_realms_v5.py runs its organisms, for the full 240
decisions of 15 s, recording every decision as the live benchmark engine's harness record does (the service position the law reads,
the decisions over the line, the work each plant did, the body's power). Organism 9 is read from the harness export's own
functions (docs/engine/export_harness_trace.py run, gauges and interval), and checked decision by decision against the same
organism run here. Runs A, B and C are seeds 3000, 3001 and 3002 (the harness record's runs: the first three of the realms'
preregistered seeds 3000-3009).

The reading, gauge by gauge, of Omni-Compass on native against native: the harness record's own measurement
(export_harness_trace.gauges: the work index against native's own rate, the muscles over their line, the body's power, and
the spread of the service positions, shown), the paired change per decision averaged over blocks of ten decisions with its
95% interval by Student t over the blocks (export_harness_trace.interval), in each run; the word by the key (tools/readings.py
stack_reading, the founder's half-percent floor by in_all_three): GAIN, LOSS or power given in all three of our runs, STEADY (the
same, no difference beyond the noise, or under the floor), the runs disagree. The realms runner's own contrasts
(tools/run_realms_v5.py: paired_organism, plant_harms, the wear) and its label over the three seeds (label_max, 95% intervals
over the seeds) stand beside them. Evidence class S (our own models).

  python3 tools/scenarios_20.py [--out results/scenarios] [--workers N]
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import os
import statistics as st
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.legal import stamp  # noqa: E402
from tools.readings import (GAIN, STEADY, LOSS, GIVEN, DISAGREE, SHOWN, IN_ALL_THREE, OWN_RUNS, HIGHER, LOWER, SPENT,  # noqa: E402
                            SHOWN_AIM, aim, by_word, classify, in_all_three, interval_by_word, labelled, receipt_key,
                            stack_reading, with_own_runs)
import tools.run_realms_v5 as R  # noqa: E402
from tools.run_orchestra import bodies as orchestra_bodies  # noqa: E402
from realms.harness import (Body, STACK, TOWER, KILL_AT, WALK, CLIMB, paired_organism,  # noqa: E402
                            run_bodies, scale_load)
from realms.compass_arm_v5 import machines, v5_position  # noqa: E402
from realms.presets import ORGANISM_STEPS  # noqa: E402


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H = _load("export_harness_trace", "docs/engine/export_harness_trace.py")   # the live benchmark engine's harness record
W = _load("export_whole", "docs/engine/export_whole.py")                   # the whole organism, regrouped

OUT = ROOT / "results" / "scenarios"
RUNS = dict(zip("ABC", H.SEEDS))                    # runs A, B and C: the harness record's seeds, 3000, 3001 and 3002
assert list(RUNS.values()) == R.PREREG_SEEDS[:3]
LOAD = "climb"
DECISION_S = 15
SAME_REL = 1e-9          # "the same" only to nine decimal places of the value (tools/readings.py EXACT_REL; the referee's work order of 25 October)
ORCHESTRA, LIVE, WHOLE = "orchestra", "live_engine", "whole"
ARMS = ("native", "on_native")
ARM_NAMES = {"native": "Native (Omni-Compass off)", "on_native": "Omni-Compass on native"}
HARNESS_ARM = {"native": "native", "on_native": "v5"}        # realms/harness.py run_bodies
EXPORT_ARM = {"native": "native", "on_native": "omni"}       # docs/engine/export_harness_trace.py run
PAIRS = (("on_native", "native"),)
PAIR_KEY = {p: f"{p[0]}_vs_{p[1]}" for p in PAIRS}
PAIR_NAMES = {"on_native_vs_native": "Omni-Compass on native against native"}


def pool(template, knob):
    """A compute pool whose count is its knob (capacity or the autoscaler's target; not a power cap or an admission limit): the
    pools whose machines the record counts, as the harness export counts them."""
    return template == "compute_pool" and knob not in ("power", "admission")
AIMS = {"up": HIGHER, "down": LOWER, "spent": SPENT, "shown": SHOWN_AIM}  # the harness record's aims in the key's words
GAUGES = {
    "work": ("work", HIGHER, "the work index: each decision, the mean over the muscles of the work each did against the reference "
                             "arm's own mean rate (1.0 is the reference's own work)"),
    "over": ("muscles over the line", LOWER, "the muscles over their own line, counted each decision (a muscle-decision over "
                                             "the line is time over the line)"),
    "power": ("power", SPENT, "the organism's electrical draw each decision, kW, as its lines carry it (realms/harness.py Body.all_w, "
                              "the reading the bone grants from); the runner's energy beside it is each plant's own metered energy "
                              "with a battery's charge left below its start bought back at its round trip, so the two can move "
                              "apart"),
    "spread": ("spread", SHOWN_AIM, "the spread of the muscles' service positions each decision (shown, never judged)"),
}
ORGANISMS = [
    (R.SPINE, "The spine", "every muscle that sits in all four realms, the base every stack runs on (`docs/THE_SPINE.md`)"),
    ("compute_ai_cloud", "Compute / AI / Cloud", "the realm's own muscles, its families on the spine"),
    ("physics_robotics_autonomous", "Physics / Robotics / Autonomous", "the realm's own muscles, its families on the spine"),
    ("energy_facility_industrial", "Energy / Facility / Industrial", "the realm's own muscles, its families on the spine"),
    ("distribution_specialized", "Distribution / Specialized", "the realm's own muscles, its families on the spine"),
    (STACK, "The four stacked", "each realm's own body on one clock, every shared muscle in each (the spine once in each realm's "
                                "body), each realm keeping its own native"),
    (TOWER, "The whole tower", "every catalog muscle once (`realms/catalog_v5.csv`)"),
    (ORCHESTRA, "The orchestra", "every catalog muscle that stands for a knob of the governors and orchestrators "
                                 "named in `tools/governors_page.py`, every one once, as `tools/run_orchestra.py` makes it"),
    (LIVE, "The live engine's organism", "the sixty muscles the live benchmark engine page draws, twelve from the spine and twelve from "
                                         "each realm, in one body (`docs/engine/export_harness_trace.py`)"),
    (WHOLE, "The whole organism, three sectors", "the software (the cluster and the services on it), the cloud as the wire (the "
                                                 "machines it bills) and the bare metal / the data center (the card, the machine), "
                                                 "composed by the product law from the real tables (`tools/whole_system.py`, "
                                                 "`results/WHOLE_SYSTEM.json`, regrouped by `docs/engine/export_whole.py`)"),
]
NOT_RUN = "not yet run"


# ------------------------------------------------------------------------------------------------------------ the organisms
def organism_rows(rows):
    """{organism: rows} for the nine run in the harness (the stack: one list of rows per realm, each its own body)."""
    g = {R.SPINE: R.spine_rows(rows)}
    g.update({realm: [r for r in rows if realm in r["realms"].split(";")] for realm in R.REALMS})
    g[STACK] = [g[realm] for realm in R.REALMS]
    g[TOWER] = rows
    g[ORCHESTRA] = orchestra_bodies(rows)[ORCHESTRA]
    g[LIVE] = H.rows()
    return g


def flat(name, rs):
    return [r for x in rs for r in x] if name == STACK else rs


def recorded_run(name, rs, seed, arm, load=LOAD):
    """One organism, one arm, on realms/harness.py run_bodies exactly as tools/run_realms_v5.py organism_run runs it (the four
    stacked: each realm's own body on one clock), every decision recorded as the live benchmark engine's harness record records it:
    the service position the law reads, the decisions over the line and the work of every plant, the body's power, and the
    machines in service and starting over every pool whose own count is its knob. The
    record is read after each body's step and changes nothing in it. Returns (record, run_bodies' own result)."""
    bodies = [Body(x, seed) for x in rs] if name == STACK else [Body(rs, seed)]
    if load != "normal":
        for b in bodies:
            scale_load(b, load)
    per = []
    for b in bodies:
        rec = {"p": [], "over": [], "work": [], "w": [], "mach": []}
        pv, pw = [0] * len(b.plants), [0.0] * len(b.plants)
        pools = [i for i, (p, r) in enumerate(zip(b.plants, b.rows)) if pool(p.template, r["knob"])]

        def step(b=b, orig=b.step, rec=rec, pv=pv, pw=pw, pools=pools):
            orig()
            ps, ov, wk = [], [], []
            for i, p in enumerate(b.plants):
                ps.append(round(min(2.0, max(-0.5, v5_position(p))), 3))
                ov.append(p.m["viol"] - pv[i]); pv[i] = p.m["viol"]
                wk.append(p.m["work"] - pw[i]); pw[i] = p.m["work"]
            rec["p"].append(ps); rec["over"].append(ov); rec["work"].append(wk); rec["w"].append(b.all_w)
            rec["mach"].append(sum(machines(b.plants[i]) for i in pools))
        b.step = step
        per.append(rec)
    out = run_bodies(bodies, arm, [list(range(len(bodies)))])
    steps = len(per[0]["w"])
    rec = {key: [sum((r[key][k] for r in per), []) for k in range(steps)] for key in ("p", "over", "work")}
    rec["power_kw"] = [round(sum(r["w"][k] for r in per) / 1000.0, 3) for k in range(steps)]
    rec["mach"] = [sum(r["mach"][k] for r in per) for k in range(steps)]
    return rec, out


def pair_runs(base, other):
    """The harness record's gauges for one pair on one seed: the paired change per decision, its mean over blocks of ten
    decisions and its 95% interval (Student t over the blocks), and each arm's mean (export_harness_trace gauges, interval)."""
    out = {}
    for key, (x, y, a) in H.gauges(base, other).items():
        d = [b2 - a2 for a2, b2 in zip(x, y)]
        m, lo, hi = H.interval(d)
        out[key] = {"aim": AIMS[a], "base": st.mean(x), "other": st.mean(y), "diff": m, "lo": lo, "hi": hi}
    return out


def runner_contrast(arm_out, ref_out, ids, kinds):
    """The realms runner's own contrasts of one pair on one seed (tools/run_realms_v5.py): work, energy (a battery's charge
    left below where it started bought back at its round trip), the change in the share of decisions over the line
    (points), work per energy; the plants that did less work or spent more decisions over their line, and what kind of
    plant and knob each is (kinds: id -> (template, knob)); the wear, shown."""
    wear = [a["wear"] / n["wear"] - 1.0 for a, n in zip(arm_out["plants"], ref_out["plants"]) if n["wear"] > 0]
    harms = R.plant_harms(arm_out, ref_out, ids)
    by_kind = {}
    for mid, _, _ in harms:
        t, k = kinds[mid]
        key = f"{t} {k}"
        by_kind[key] = by_kind.get(key, 0) + 1
    return {"contrast": paired_organism(arm_out, ref_out), "wear": sum(wear) / len(wear) if wear else 0.0,
            "plants_less_work": sum(1 for _, dw, _ in harms if dw < -1e-9), "plants_more_misses": sum(1 for _, _, dv in harms if dv > 0),
            "plants_flagged_by_kind": dict(sorted(by_kind.items(), key=lambda kv: -kv[1])),
            "plants_flagged": [[mid, dw, dv] for mid, dw, dv in harms]}


def arm_totals(out, rec):
    pl = out["plants"]
    viol, n = sum(p["viol"] for p in pl), sum(p["steps"] for p in pl)
    mach = rec["mach"]
    return {"energy_mj": sum(p["energy_j"] for p in pl) / 1e6, "plant_decisions_over": viol, "plant_decisions": n,
            "misses_share": viol / n if n else 0.0, "writes": out["writes"], "lease_handed_back": out["restore_ok"],
            "pool_machines_first": mach[0] if mach else 0, "pool_machines_mean": st.mean(mach) if mach else 0.0,
            "pool_machines_peak": max(mach) if mach else 0}


def organism_job(args):
    """One organism on one seed: the two arms, the pair's gauges and the runner's contrasts."""
    name, rs, seed = args
    ids = ([f"{r['muscle_id']}@{realm}" for realm, x in zip(R.REALMS, rs) for r in x] if name == STACK
           else [r["muscle_id"] for r in rs])
    kinds = {i: (r["template"], r["knob"]) for i, r in zip(ids, flat(name, rs))}
    runs = {arm: recorded_run(name, rs, seed, HARNESS_ARM[arm]) for arm in ARMS}
    recs = {arm: runs[arm][0] for arm in ARMS}
    check = None
    if name == LIVE:                       # organism 9: the harness export's own run, checked against the run here
        exp = {arm: H.run(rs, seed, EXPORT_ARM[arm]) for arm in ARMS}
        check = all(exp[a][k] == recs[a][k] for a in ARMS for k in ("p", "over", "work", "power_kw", "mach"))
        recs = exp
    outs = {arm: runs[arm][1] for arm in ARMS}
    pairs = {PAIR_KEY[(x, y)]: {"gauges": pair_runs(recs[y], recs[x]), "runner": runner_contrast(outs[x], outs[y], ids, kinds)}
             for x, y in PAIRS}
    arms = {}
    for arm in ARMS:
        g = pairs[PAIR_KEY[(arm, "native")]]["gauges"] if arm != "native" else None
        ref = pairs[PAIR_KEY[("on_native", "native")]]["gauges"]
        own = {key: (g[key]["other"] if g else ref[key]["base"]) for key in GAUGES}
        tot = arm_totals(outs[arm], recs[arm])
        if arm != "native":
            rc = pairs[PAIR_KEY[(arm, "native")]]["runner"]
            tot.update(wear_vs_native=rc["wear"], plants_less_work_than_native=rc["plants_less_work"],
                       plants_more_misses_than_native=rc["plants_more_misses"])
        arms[arm] = {"gauges": own, "totals": tot}
    return name, seed, {"arms": arms, "pairs": pairs, "export_check": check}


# ------------------------------------------------------------------------------------------------------------- the reading
def three_run(runs, aim_):
    """The key's three-run reading of one gauge (tools/readings.py stack_reading, the founder's rule of 24 October: GAIN, LOSS or
    power given in all three of our runs, or by the mean of our three runs with the count beyond the noise, by the gauge's aim;
    STEADY under the floor or the same; the runs disagree), with the half-percent floor (in_all_three with the largest run's
    change) where the reference is not zero."""
    rs = [{"native": r["base"], "diff": r["diff"], "significant": r["lo"] > 0 or r["hi"] < 0} for r in runs]
    reading = stack_reading(rs, aim_, SAME_REL)
    if IN_ALL_THREE in reading and all(r["base"] for r in runs):
        reading = in_all_three(runs[0]["diff"] < 0, aim(aim_), max(abs(r["diff"] / r["base"]) for r in runs))
    return reading


def short(reading, aim_):
    """The reading's one word, as the key classifies it."""
    c = classify(reading, aim(aim_))
    return {"gain": GAIN, "loss": LOSS, "given": GIVEN, "noise": STEADY, "same": STEADY, "disagree": DISAGREE}.get(c, SHOWN)


def cell(r, word):
    """One run's change and its 95% interval as the key prints them: in percent of the reference where it is not zero, the
    number carrying the word's sign (tools/readings.py by_word, interval_by_word)."""
    w = word if word in (GAIN, LOSS, GIVEN, STEADY) else None
    if r["base"]:
        b = abs(r["base"])
        return f"{by_word(100 * r['diff'] / b, w, digits=2)} ({interval_by_word(100 * r['lo'] / b, 100 * r['hi'] / b, w, digits=2)})"
    return (f"{by_word(r['diff'], w, unit='', digits=3)} ({interval_by_word(r['lo'], r['hi'], w, unit='', digits=3)}; "
            "the reference is 0)")


def mean_change(runs):
    if all(r["base"] for r in runs):
        return sum(r["diff"] / abs(r["base"]) for r in runs) / len(runs), "%"
    return sum(r["diff"] for r in runs) / len(runs), ""


def read_organism(name, by_seed):
    """One organism's record from its three runs."""
    seeds = list(RUNS.values())
    rec = {"arms": {}, "readings": {}}
    for arm in ARMS:
        rec["arms"][arm] = {"runs": {letter: {"seed": s, "gauges": by_seed[s]["arms"][arm]["gauges"],
                                              "totals": by_seed[s]["arms"][arm]["totals"]} for letter, s in RUNS.items()}}
    for pk in PAIR_KEY.values():
        gauges = {}
        for key, (gname, a, _) in GAUGES.items():
            runs = [by_seed[s]["pairs"][pk]["gauges"][key] for s in seeds]
            reading = three_run(runs, a)
            w = short(reading, a)
            mc, unit = mean_change(runs)
            gauges[key] = {"name": gname, "aim": a, "reading": reading.strip("*"), "word": w,
                           "mean_change": mc, "unit": unit,
                           "runs": {letter: dict(run, change=(run["diff"] / abs(run["base"]) if run["base"] else None),
                                                 lo_rel=(run["lo"] / abs(run["base"]) if run["base"] else None),
                                                 hi_rel=(run["hi"] / abs(run["base"]) if run["base"] else None),
                                                 cell=cell(run, w))
                                    for letter, run in zip(RUNS, runs)}}
        rcs = [by_seed[s]["pairs"][pk]["runner"] for s in seeds]
        x, y = pk.split("_vs_")
        valid = all(by_seed[s]["arms"][arm]["totals"]["lease_handed_back"] for s in seeds for arm in (x, y))
        per = [r["contrast"] for r in rcs]
        label = R.label_max(per, valid)
        rec["readings"][pk] = {"gauges": gauges, "runner": {
            "label": label, "valid": valid, "summary": R.summarize(per),
            # the label's words name native as the reference; against Omni-Compass on native the reference is named so
            "labelled": labelled(label).replace("as native", "as Omni-Compass on native") if y == "on_native" else labelled(label),
            "runs": {letter: {"seed": s, **{k: v for k, v in rc.items() if k != "plants_flagged"},
                              "plants_flagged": rc["plants_flagged"]} for (letter, s), rc in zip(RUNS.items(), rcs)}}}
    return rec


# ------------------------------------------------------------------------------------------------------- the whole organism
SECTORS = (("software", "the software"), ("cloud", "the cloud as the wire"), ("hardware", "the bare metal / the data center"))


def whole_record():
    """Organism 10 from results/WHOLE_SYSTEM.json, regrouped into its three sectors by docs/engine/export_whole.py (its own
    run, written to a temporary file): the on-native factors as the composition carries them; native the reference of
    every factor."""
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "whole.json"
        with contextlib.redirect_stdout(io.StringIO()):
            W.main(str(f))
        d = json.loads(f.read_text(encoding="utf-8"))
    if "missing" in d:
        return {"state": "missing", "file": d["missing"]}
    ws = json.loads((ROOT / "results" / "WHOLE_SYSTEM.json").read_text(encoding="utf-8"))
    engines = sorted({t["engine"] for tests in ws["layers"].values() for t in tests})
    layers = {g["key"]: [{"no": lay["no"], "name": lay["name"], "state": lay["state"], "tests": lay["n_tests"], "class": lay["cls"]}
                         for lay in g["layers"]] for g in d["groups"]}

    def fac(v):
        if not v:
            return None
        return {"pct": v["pct"], "lo_pct": v["lo_pct"], "hi_pct": v["hi_pct"], "word": v["word"],
                "cell": f"{by_word(v['pct'], v['word'], digits=2)} ({interval_by_word(v['lo_pct'], v['hi_pct'], v['word'], digits=2)})"}
    scopes = {}
    for sk, res in d["results"].items():
        scopes[sk] = {"name": res["name"]}
        for rd in ("index", "carried"):
            if rd not in res:
                continue
            r = res[rd]
            sectors = {}
            for key, _ in SECTORS:
                g = r["groups"].get(key) or {}
                sectors[key] = {"layers_in": g.get("layers_in", []), "gauges": {k: fac(v) for k, v in (g.get("gauges") or {}).items()},
                                "index": ({"pct": g["index"]["pct"], "word": g["index"]["word"], "correlated": g["index"]["correlated"]}
                                          if g.get("index") else None)}
            ft = r["file_total"]
            idx = dict(ft["index"])
            tot = next((v for k, v in ws["totals"].items() if [x.strip() for x in k.split("|")] == [res["name"], rd]), None)
            if tot and tot.get("index") and idx.get("mu") is not None:      # the index's word by the exporter's own rule
                idx["word"] = W.word_of("index", tot["index"]["mu"], tot["index"]["sigma_correlated"])
            scopes[sk][rd] = {"sectors": sectors, "whole": {"gauges": {k: fac(v) for k, v in ft["gauges"].items() if v},
                                                            "index": idx}}
    return {"state": "composed", "gauges": W.GAUGE_WORDS, "rule": d["rule"], "layers": layers, "engines": engines,
            "separability": d["separability"]["n"], "separability_agree": d["separability"]["agree"], "scopes": scopes}


def whole_organism(no, key, name, what):
    w = whole_record()
    return {"no": no, "key": key, "name": name, "what": what, "class": "S (a composition of class P and class L measurements)",
            "muscles": None, "source": "results/WHOLE_SYSTEM.json, regrouped by docs/engine/export_whole.py",
            "arms": {"native": {"state": "the reference", "note": "every factor is a ratio against native, each layer measured with its "
                                                                  "own native as its own test ran it; native carries no number of its own"},
                     "on_native": {"state": w.get("state"), "composition": w}},
            "readings": {"on_native_vs_native": {"state": w.get("state"), "composition": w}}}


# ------------------------------------------------------------------------------------------------------------------- the page
def pct(x, word, unit="%", digits=2):
    return by_word(100 * x if unit == "%" else x, word if word in (GAIN, LOSS, GIVEN, STEADY) else None, unit=unit, digits=digits)


def summary_cell(rd):
    parts = []
    for key in ("work", "over", "power"):
        g = rd["gauges"][key]
        parts.append(f"{g['name']} **{g['word']}** {pct(g['mean_change'], g['word'], g['unit'] or '')}"
                     + ("" if g["unit"] else " muscles"))
    return " · ".join(parts)


def write_md(out, rec):
    run = rec["run"]
    L = ["# The twenty scenarios: ten organisms, each native and with Omni-Compass on native (modelled)", ""]
    L += receipt_key() + [""]
    L += ["The founder's words of 24 October set the organisms: \"We have 4 realms ... the 4 realms stacked ... the spine of the 4 "
          "realms ... Then we have the whole thing native. And with OmniCompass on native ... 9 to 10 different organisms.\" His "
          "order of 25 October took the third way out: \"we don't need an omnicompass by itself ... Never is going to omnicompass be "
          "by itself. It needs muscles somewhere, somehow.\" Omni-Compass always sits on top of a native controller. Ten organisms, "
          "each two ways: twenty scenarios, every one tabulated below, every row reported, LOSS included.", "",
          f"Evidence class **S** (our own models): a model's energy is not a meter's, and a plant written by the people who wrote "
          f"the law is not an independent test. Engine **{run['engine']}** (`tools/omni_version.py`, digest {run['engine_digest'][:16]}), "
          f"commit `{run['commit'][:12]}`{' (uncommitted changes in the files it stands on)' if run['dirty'] else ''}, run "
          f"{run['started']}, {run['elapsed_s']} s on {run['workers']} processes. Runs A, B and C are seeds "
          f"{', '.join(str(s) for s in run['seeds'])} (the live benchmark engine's harness record's runs, the first three of the realms' "
          f"preregistered seeds 3000-3009), the same seed in every arm. The load is the climb (the load stepping by one, "
          f"{' '.join(str(x) for x in CLIMB[:8])} ..., level 4 the organism's own load, 8 twice it), for {run['steps']} decisions "
          f"of {DECISION_S} s (an hour, every organism at full length); at {int(KILL_AT * 100)}% of every run the brain goes "
          f"silent and the lease walks every setting back to native over {WALK} decisions. Written by "
          "`python3 tools/scenarios_20.py`; every run's every gauge is in `results/scenarios/SCENARIOS_20.json`.", "",
          "## The two arms", "",
          "| Arm | What runs |", "|---|---|",
          "| Native (Omni-Compass off) | every plant under its own native controller alone (`realms/harness.py` `run_bodies`, arm native) |",
          "| Omni-Compass on native | the max (`realms/compass_arm_v5.py`, `V5CFG`), the factory tune, on top of every native controller: "
          "every muscle to its own limit, never past it and never below native, the bone granting only the power the body's lines "
          "and rooms have room for (arm v5, as `tools/run_realms_v5.py` runs it) |", "",
          "## How each scenario is read", "",
          "Omni-Compass on native is read against native gauge by gauge as the live "
          "engine's harness record reads it (`docs/engine/export_harness_trace.py` `gauges` and `interval`): in each run the paired "
          "change per decision, averaged over blocks of ten decisions, with its 95% interval by Student t over the 24 blocks. The "
          "word is the key's (`tools/readings.py` `stack_reading`, with the founder's half-percent floor through `in_all_three`): "
          "**GAIN**, **LOSS** or **power given in all three of our runs** when all three runs point the same way with every interval "
          "clear of zero, judged by what the gauge is for and never by its sign; **STEADY** when an interval includes zero (no "
          "difference beyond the noise), when nothing moved (the same), or when every run's change is under half of one percent "
          "(under the floor); **the runs disagree** when clear runs point different ways. The number beside a word carries the "
          "word's sign. The gauges:", "",
          "| Gauge | What it is for | What it measures |", "|---|---|---|"]
    for key, (gname, a, how) in GAUGES.items():
        L.append(f"| {gname} | {({HIGHER: 'work done: a rise is GAIN', LOWER: 'time over the line: a fall is GAIN', SPENT: 'a resource spent: a fall is a cut (GAIN), a rise is power given', SHOWN_AIM: 'shown, not judged'})[a]} | {how} |")
    L += ["", "Beside them stand the realms runner's own contrasts (`tools/run_realms_v5.py` `paired_organism`, `plant_harms`: the "
          "work, the energy with a battery's charge left below its start bought back at its round trip, the decisions over the "
          "line, the work per energy, the wear, and every plant that did less work or missed its line more often) and the runner's "
          "label over the three seeds (`label_max`: 95% intervals over the seeds, Student t with two degrees of freedom), in the "
          "words of the key.", ""]
    orgs = rec["organisms"]
    # the twenty
    L += ["## The twenty scenarios", "",
          "Native's own gauges (the mean of runs A, B and C), then Omni-Compass on native read against native (the word, and the "
          "mean of the three runs' changes). The per-run numbers and intervals follow.", "",
          "| # | Organism | Muscles | Native (Omni-Compass off) | Omni-Compass on native, against native |", "|---:|---|---:|---|---|"]
    for o in orgs:
        if o["key"] == WHOLE:
            comp = o["readings"]["on_native_vs_native"]["composition"]
            if comp.get("state") == "composed":
                sc = comp["scopes"]["without"]["index"]["whole"]
                c = " · ".join(f"{k} **{v['word']}** {by_word(v['pct'], v['word'], digits=1)}" for k, v in sc["gauges"].items())
                idx = sc["index"]
                c += (f"; the index **{idx.get('word', SHOWN)}** {by_word(idx['pct'], idx.get('word'), digits=1)} "
                      f"({interval_by_word(*idx['correlated'], idx.get('word'), digits=1)}, the gauges perfectly correlated) "
                      "(the composition, by the index's rule, without the card)")
            else:
                c = "the composition is not in this checkout"
            L.append(f"| {o['no']} | {o['name']} | layers | the reference of every factor | {c} |")
            continue
        nat = o["arms"]["native"]["runs"]
        ng = lambda k: sum(nat[x]["gauges"][k] for x in RUNS) / 3
        nt = lambda k: sum(nat[x]["totals"][k] for x in RUNS) / 3
        ncell = (f"work index {ng('work'):.3f}; {ng('over'):.2f} muscles over the line a decision ({100 * nt('misses_share'):.2f}% of "
                 f"muscle-decisions); {ng('power'):,.1f} kW ({nt('energy_mj'):,.1f} MJ)")
        L.append(f"| {o['no']} | {o['name']} | {o['muscles']:,} | {ncell} | "
                 + " | ".join(summary_cell(o["readings"][pk]) for pk in PAIR_KEY.values()) + " |")
    L += ["", "Muscles over the line: the mean change in muscles over their line each decision, as a share of the reference's "
          "own (a change counted in muscles where the reference had none). Power: the organism's electrical power against the "
          "reference's; a rise is power given, what Omni-Compass put in for the work and the time over the line beside it.", ""]
    # each pair, every run
    for pk, pname in PAIR_NAMES.items():
        L += [f"## {pname}: every gauge, every run", "",
              "| # | Organism | Gauge | Run A (seed 3000) | Run B (seed 3001) | Run C (seed 3002) | Reading |",
              "|---:|---|---|---|---|---|---|"]
        for o in orgs:
            rd = o["readings"][pk]
            if o["key"] == WHOLE:
                if pk == "on_native_vs_native" and rd.get("state") == "composed":
                    sc = rd["composition"]["scopes"]["without"]["index"]["whole"]
                    for k, v in sc["gauges"].items():
                        L.append(f"| {o['no']} | {o['name']} | {k} | composed: A, B and C pooled in each test | | | "
                                 f"**{v['word']}** {v['cell']} (the composition, by the index's rule, without the card) |")
                else:
                    L.append(f"| {o['no']} | {o['name']} | every gauge | {NOT_RUN} | {NOT_RUN} | {NOT_RUN} | **{NOT_RUN}** |")
                continue
            for key, g in rd["gauges"].items():
                L.append(f"| {o['no']} | {o['name']} | {g['name']} | " + " | ".join(g["runs"][x]["cell"] for x in RUNS)
                         + f" | **{g['reading']}** |")
        L.append("")
    # each arm's own gauges
    L += ["## Each arm's own gauges, run by run (A / B / C)", "",
          "The work index is each arm's work against native's own (native's is 1.0 less the share of plants that did no work in "
          "the hour); muscles over the line is the mean count each decision; power is the organism's mean electrical power; energy "
          "is the runner's total (a battery's charge left below its start bought back at its round trip); writes are the settings "
          "Omni-Compass changed before the brain went silent; the lease is every setting back at the operator's before the run "
          "ended; the pools' machines are the machines in service and starting over every pool whose own count is its knob, at "
          "the first decision, their mean over the hour and their peak (shown, never judged).", "",
          "| # | Organism | Arm | Work index | Muscles over the line a decision | Power (kW) | Energy (MJ) | Muscle-decisions over the line "
          "| Writes | Lease handed back | The pools' machines: first, mean, peak |", "|---:|---|---|---|---|---|---|---|---|---|---|"]
    for o in orgs:
        if o["key"] == WHOLE:
            continue
        for arm in ARMS:
            r = o["arms"][arm]["runs"]
            j = lambda f, key, sub="gauges": " / ".join(f.format(r[x][sub][key]) for x in RUNS)
            L.append(f"| {o['no']} | {o['name']} | {ARM_NAMES[arm]} | {j('{:.4f}', 'work')} | {j('{:.2f}', 'over')} | "
                     f"{j('{:,.1f}', 'power')} | {j('{:,.2f}', 'energy_mj', 'totals')} | {j('{:,}', 'plant_decisions_over', 'totals')} | "
                     f"{j('{:,}', 'writes', 'totals')} | {' / '.join('yes' if r[x]['totals']['lease_handed_back'] else 'NO' for x in RUNS)} | "
                     + " / ".join(f"{r[x]['totals']['pool_machines_first']:,}, {r[x]['totals']['pool_machines_mean']:,.0f}, "
                                  f"{r[x]['totals']['pool_machines_peak']:,}" for x in RUNS) + " |")
    L.append("")
    # the runner's contrasts
    L += ["## The realms runner's own contrasts and label", "",
          "`tools/run_realms_v5.py`'s measure of each pair, run by run (A / B / C): work (the mean over the plants of each plant's work "
          "against the reference's), the decisions over the line (the change in their share, points), the energy (power given "
          "when it rose), work per energy, the wear (shown, never judged), and the plants that did less work or missed their line "
          "more often than the reference. The label is the runner's own over the three seeds (95% intervals over the seeds). These "
          "numbers stand beside no word of their own: each carries its own direction (+ up, − down), and the label is the word.", "",
          "| # | Organism | Pair | The runner's label | Work | Misses (points) | Energy | Work per energy | Wear | Plants with less work, "
          "more misses |", "|---:|---|---|---|---|---|---|---|---|---|"]
    for o in orgs:
        if o["key"] == WHOLE:
            continue
        for pk, pname in PAIR_NAMES.items():
            rn = o["readings"][pk]["runner"]
            rr = rn["runs"]
            c = lambda k, s=100.0, u="%": " / ".join(by_word(rr[x]['contrast'][k] * s, None, unit=u, digits=2) for x in RUNS)
            L.append(f"| {o['no']} | {o['name']} | {pname} | **{rn['labelled']}**{'' if rn['valid'] else ' (INVALID: a lease not handed back)'} | "
                     f"{c('work')} | {c('viol_pp', 1.0, '')} | {c('energy')} | {c('primary')} | "
                     + " / ".join(by_word(rr[x]['wear'] * 100, None, digits=2) for x in RUNS) + " | "
                     + " / ".join(f"{rr[x]['plants_less_work']}, {rr[x]['plants_more_misses']}" for x in RUNS) + " |")
    L.append("")
    # organism 10
    w = next(o for o in orgs if o["key"] == WHOLE)
    comp = w["readings"]["on_native_vs_native"].get("composition") or {}
    L += [f"## Organism 10, {w['name'].lower()}", "", f"{w['what'][0].upper()}{w['what'][1:]}. {w['arms']['native']['note'][0].upper()}"
          f"{w['arms']['native']['note'][1:]}.", ""]
    if comp.get("state") == "composed":
        L += [f"The composition's rule: {comp['rule']}. The tests' engines: {'; '.join(comp['engines'])}. Separability (a layer's "
              f"ratio unchanged when the layer under it carries Omni-Compass), tested on the governors' four ways: "
              f"{comp['separability_agree']} of {comp['separability']} pairs agree.", "",
              "| Scope | Reading | Sector | Layers | " + " | ".join(comp["gauges"]) + " |", "|---|---|---|---|" + "---|" * len(comp["gauges"])]
        for sk, sc in comp["scopes"].items():
            for rd in ("index", "carried"):
                if rd not in sc:
                    continue
                rows = [(sname, sc[rd]["sectors"][key]) for key, sname in SECTORS] + [("the whole", dict(sc[rd]["whole"], layers_in="all"))]
                for sname, s in rows:
                    layers = s["layers_in"] if s["layers_in"] == "all" else (", ".join(str(x) for x in s["layers_in"]) or "none measured")
                    cells = []
                    for g in comp["gauges"]:
                        v = s["gauges"].get(g)
                        cells.append(f"**{v['word']}** {v['cell']}" if v else "—")
                    L.append(f"| {sc['name']} | {'by the index rule' if rd == 'index' else 'every interval carried'} | {sname} | {layers} | "
                             + " | ".join(cells) + " |")
        L += ["", "The layers: " + "; ".join(f"{lay['name']} ({lay['state']}, {lay['tests']} test{'' if lay['tests'] == 1 else 's'})"
                                             for g in comp["layers"].values() for lay in g) + ".", ""]
    else:
        L += ["`results/WHOLE_SYSTEM.json` is not in this checkout: the composition cannot be read.", ""]
    # organism 9's check
    live = next(o for o in orgs if o["key"] == LIVE)
    L += ["## What stands behind the numbers", "",
          f"- Organism 9 is read from the harness export's own functions (`docs/engine/export_harness_trace.py` `run`, `gauges`, "
          f"`interval`); the same sixty muscles run here on `run_bodies` gave, decision by decision in every arm and run, "
          f"{'the same record' if live.get('export_check') else 'a different record (named, not hidden: the export reads its own)'}.",
          "- Every LOSS row stands where it reads; a LOSS on the factory tune is a fault to be root-caused and fixed in the next "
          "version, never a number to accept.", ""]
    losses = [(o["name"], PAIR_NAMES[pk], g["name"], g["reading"]) for o in orgs if o["key"] != WHOLE
              for pk in PAIR_KEY.values() for g in o["readings"][pk]["gauges"].values() if g["word"] == LOSS]
    L += [f"## Every LOSS row ({len(losses)})", ""]
    L += [f"- {n}, {p}: {g}, {r}" for n, p, g, r in losses] or ["- none"]
    (out / "SCENARIOS_20.md").write_text("\n".join(stamp(with_own_runs(L))) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------------------------------------------------- main
def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()


FROZEN = R.FROZEN + ["tools/scenarios_20.py", "tools/run_orchestra.py", "tools/governors_page.py",
                     "docs/engine/export_harness_trace.py", "docs/engine/export_whole.py", "results/WHOLE_SYSTEM.json"]


def build(workers=None, organisms=None):
    """Run organisms 1-9 and read organism 10; return the record."""
    from tools.omni_version import engine_files, version_of, digest
    snap = engine_files()
    rows = R.catalog(str(ROOT / "realms" / "catalog_v5.csv"))
    groups = organism_rows(rows)
    want = [k for k, *_ in ORGANISMS if k != WHOLE and (not organisms or k in organisms)]
    size = {k: len(flat(k, groups[k])) for k in want}
    jobs = [(k, groups[k], s) for k in sorted(want, key=lambda k: -size[k]) for s in RUNS.values()]
    run = {"started": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "commit": git("rev-parse", "HEAD"),
           "dirty": bool(git("status", "--porcelain", "--", *FROZEN)), "engine": version_of(snap) or "undeclared",
           "engine_digest": digest(snap), "dial": "max", "class": "S", "runs": RUNS, "seeds": list(RUNS.values()), "load": LOAD,
           "steps": ORGANISM_STEPS, "decision_s": DECISION_S, "kill_at": int(KILL_AT * ORGANISM_STEPS), "walk": WALK,
           "workers": workers or os.cpu_count() or 2, "catalog": "realms/catalog_v5.csv"}
    t0 = time.time()
    raw = {}
    with ProcessPoolExecutor(run["workers"]) as ex:
        for name, seed, o in ex.map(organism_job, jobs):
            raw.setdefault(name, {})[seed] = o
    run["elapsed_s"] = round(time.time() - t0)
    orgs = []
    for no, (key, name, what) in enumerate(ORGANISMS, 1):
        if key == WHOLE:
            if not organisms or WHOLE in organisms:
                orgs.append(whole_organism(no, key, name, what))
            continue
        if key not in raw:
            continue
        rs = flat(key, groups[key])
        o = {"no": no, "key": key, "name": name, "what": what, "class": "S", "muscles": len(rs),
             "source": ("docs/engine/export_harness_trace.py (run, gauges, interval)" if key == LIVE
                        else "realms/harness.py run_bodies, recorded by tools/scenarios_20.py")}
        o.update(read_organism(key, raw[key]))
        if key == LIVE:
            o["export_check"] = all(raw[key][s]["export_check"] for s in RUNS.values())
        orgs.append(o)
    return {"title": "The twenty scenarios: ten organisms, each native and with Omni-Compass on native",
            "class": "S", "own_runs": OWN_RUNS, "run": run, "arms": ARM_NAMES, "pairs": PAIR_NAMES,
            "gauges": {k: {"name": n, "aim": a, "how": h} for k, (n, a, h) in GAUGES.items()},
            "organisms": orgs}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--organisms", default="", help="a comma-separated subset (a look; the record holds all ten)")
    a = ap.parse_args(argv)
    rec = build(a.workers, [x for x in a.organisms.split(",") if x])
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    (out / "SCENARIOS_20.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if len(rec["organisms"]) == len(ORGANISMS):
        write_md(out, rec)
    print(f"scenarios: {len(rec['organisms'])} organisms in {rec['run']['elapsed_s']} s -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
