#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Seven organisms, native and Omni, over many runs and at many sizes (evidence class S: the realm models).

  1 Compute / AI / Cloud
  2 Physics / Robotics / Autonomous
  3 Energy / Facility / Industrial
  4 Distribution / Specialized
  5 the four stacked, every duplicate kept, one body on one clock
  6 the whole tower, every muscle once
  7 the spine, the muscles every stack runs on (every muscle that sits in all four realms)
  (sizes: realms/catalog_provenance.json; the spine: tools/run_realms_v5.py, spine_rows)

Every organism runs native (its own controllers) and native with Omni on top on the same seed: --arm v5 (the engine's
law, realms/compass_arm_v5.py, on the v5 catalog) or --arm compass (the v3 law, realms/compass_arm.py, on v3's catalog,
for v3's stored grid); --runs paired seeds (7000 on); --scale copies of the organism on one clock (each copy its own
seeds), so 10x is ten clusters of that organism governed together. Receipts: per organism, work per energy, work, energy
and violations with their 95% intervals over runs, the label by the round-3 rule, and the raw per-run contrasts.

The four stacked (5), two ways (--stack): "realms" (the v5 default) keeps each realm's own body on the one clock, so
every muscle in the stack runs exactly the native it runs in its own realm, plant by plant (the founder's order: the
native identical in all seven); "body" (v3's stored grid) puts all four realms in one body, each copy its own series.

Every finished run is written as it ends (SCALE.json, rewritten whole), with its plant sums, its own time and the worker's
peak memory; --deadline-min starts no run that would end after the deadline, so a shard cut short by a runner's six-hour
limit hands in every run it finished. The plant sums let bodies that share nothing on the clock be joined afterwards: the
four stacked in v5 are the four realms' own bodies side by side, so its run on a seed is the four realms' runs on that seed
joined plant for plant (joined(); tools/pool_scale.py uses it where the four stacked is too big for one machine).

  python3 tools/run_scale.py --runs 100 --scale 1 --out results/scale/r100-x1 [--arm v5] [--workers N] [--organisms 1,2,5]
"""
from __future__ import annotations

import argparse

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
import json
import os
import resource
import subprocess
import sys
import time
from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.harness import (catalog, run_organism_arm, run_bodies, Body, paired_organism, summarize, label, STACK,  # noqa: E402
                            TOWER, organism_name, scale_load, LINE)
from tools.run_realms_v5 import label_max, SPINE, spine_rows  # noqa: E402  the max's label; the spine, the seventh organism

ARM, CATALOG, STACK_MODE = "compass", None, "body"       # set by main() (and passed to each worker)
CATALOGS = {"compass": str(ROOT / "realms" / "catalog.csv"), "v5": str(ROOT / "realms" / "catalog_v5.csv")}

REALMS = ("compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized")
ORGS = {"1": ("compute_ai_cloud", "Compute / AI / Cloud"), "2": ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
        "3": ("energy_facility_industrial", "Energy / Facility / Industrial"), "4": ("distribution_specialized", "Distribution / Specialized"),
        "5": (STACK, "The four stacked, duplicates kept"), "6": (TOWER, "The whole tower, every muscle once"),
        "7": (SPINE, "The spine, the muscles every stack runs on")}
SEED0 = 7000


def rows_for(key, scale, cat=None):
    rows = catalog(cat or CATALOG) if (cat or CATALOG) else catalog()
    key = organism_name(key)
    if key == STACK:
        base = [dict(r, muscle_id=f"{r['muscle_id']}@{realm}") for realm in REALMS for r in rows if realm in r["realms"].split(";")]
    elif key == TOWER:
        base = rows
    elif key == SPINE:
        base = spine_rows(rows)
    else:
        base = [r for r in rows if key in r["realms"].split(";")]
    return [dict(r, muscle_id=r["muscle_id"] + (f"~{c}" if c else "")) for c in range(scale) for r in base]


LOADS = {"normal": "its own load", "climb": "the climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it)",
         "line": f"work waiting in line ({LINE:.0%} of the run's own work at the start)"}


def run_arm(key, scale, seed, arm, cat, stack_mode, load="normal"):
    if organism_name(key) == STACK and stack_mode == "realms":
        bodies = [Body(rows_for(realm, scale, cat), seed) for realm in REALMS]
    else:
        bodies = [Body(rows_for(key, scale, cat), seed)]
    if load != "normal":
        for b in bodies:
            scale_load(b, load)
    return run_bodies(bodies, arm, [list(range(len(bodies)))])


def sums_of(om, nat):
    """The run's plant sums, from which its contrast is computed (realms/harness.py paired_organism): kept with every run
    so bodies that share nothing on the clock can be joined plant for plant afterwards (joined())."""
    ws = [a["work"] / n["work"] for a, n in zip(om["plants"], nat["plants"]) if n["work"] > 0]
    wear = [a["wear"] / n["wear"] - 1.0 for a, n in zip(om["plants"], nat["plants"]) if n.get("wear", 0) > 0]
    return {"w_sum": sum(ws), "w_n": len(ws),
            "e_omni": sum(p["energy_j"] for p in om["plants"]), "e_native": sum(p["energy_j"] for p in nat["plants"]),
            "v_omni": sum(p["viol"] for p in om["plants"]), "s_omni": sum(p["steps"] for p in om["plants"]),
            "v_native": sum(p["viol"] for p in nat["plants"]), "s_native": sum(p["steps"] for p in nat["plants"]),
            "wear_sum": sum(wear), "wear_n": len(wear), "plants": len(nat["plants"])}


def contrast(s, restore_ok):
    """A run's record from its plant sums: the same numbers paired_organism gives on the plants themselves."""
    w, e = s["w_sum"] / s["w_n"], s["e_omni"] / s["e_native"]
    c = {"primary": w / e - 1.0, "work": w - 1.0, "energy": e - 1.0,
         "viol_pp": (s["v_omni"] / s["s_omni"] - s["v_native"] / s["s_native"]) * 100.0}
    c.update(restore_ok=restore_ok, energy_native_j=s["e_native"], energy_omni_j=s["e_omni"], misses_native=s["v_native"],
             misses_omni=s["v_omni"], decisions=s["s_native"], wear=s["wear_sum"] / s["wear_n"] if s["wear_n"] else 0.0)
    return c


def joined(parts):
    """One run of bodies that share nothing on the clock, from each body's run on the same seed: the four stacked in v5
    are the four realms' own bodies side by side (--stack realms), so its run is theirs joined, plant for plant."""
    s = {k: sum(p["sums"][k] for p in parts) for k in parts[0]["sums"]}
    c = contrast(s, all(p["restore_ok"] for p in parts))
    c["sums"] = s
    c["joined_from"] = len(parts)
    return c


LADDER = (1, 10, 100, 500)   # the ladder (the founder's order of 25 October): copies and runs alike


def cut_plants(key, scale, cat, stack_mode, m):
    """The plants of the stack's first m copies, in the run's plant order: every body lists its rows copy by copy (rows_for:
    copy 0's muscles, then copy 1's, ...), and the bodies one after another, so the first m copies of a body are its first
    m times its muscles. The stack of 500 copies cut down to its first 100, 10 or 1 is the first part of the same stack."""
    bases = ([len(rows_for(r, 1, cat)) for r in REALMS] if organism_name(key) == STACK and stack_mode == "realms"
             else [len(rows_for(key, 1, cat))])
    idx, off = [], 0
    for nb in bases:
        idx += list(range(off, off + nb * m))
        off += nb * scale
    return idx


def cuts_of(key, scale, cat, stack_mode, om, nat):
    """The run read at the first 1, 10 and 100 copies of its stack (each rung under the run's own size): the same run, cut."""
    out = {}
    for m in LADDER:
        if m >= scale:
            continue
        idx = cut_plants(key, scale, cat, stack_mode, m)
        part = lambda r: {"plants": [r["plants"][i] for i in idx]}
        out[str(m)] = contrast(sums_of(part(om), part(nat)), om["restore_ok"])
    return out


def job(args):
    key, scale, seed, arm, cat, stack_mode, load = args
    t = time.time()
    nat = run_arm(key, scale, seed, "native", cat, stack_mode, load)
    om = run_arm(key, scale, seed, arm, cat, stack_mode, load)
    c = paired_organism(om, nat)
    c["restore_ok"] = om["restore_ok"]
    c["energy_native_j"] = sum(p["energy_j"] for p in nat["plants"])
    c["energy_omni_j"] = sum(p["energy_j"] for p in om["plants"])
    c["misses_native"] = sum(p["viol"] for p in nat["plants"])
    c["misses_omni"] = sum(p["viol"] for p in om["plants"])
    c["decisions"] = sum(p["steps"] for p in nat["plants"])
    wear = [a["wear"] / n["wear"] - 1.0 for a, n in zip(om["plants"], nat["plants"]) if n.get("wear", 0) > 0]
    c["wear"] = sum(wear) / len(wear) if wear else 0.0
    c["sums"] = sums_of(om, nat)
    if scale > 1:                                              # the stack cut down: its first 1, 10 and 100 copies, the same run
        c["cuts"] = cuts_of(key, scale, cat, stack_mode, om, nat)
    c["wall_s"] = round(time.time() - t, 1)                    # the run's own time and the worker's peak memory, for planning
    c["rss_gb"] = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2)
    return key, seed, c


def engine():
    """The engine this checkout runs (tools/omni_version.py): results are pooled only within one engine."""
    try:
        from tools.omni_version import engine_files, version_of
        return version_of(engine_files()) or "undeclared"
    except Exception as e:                                     # noqa: BLE001  (a file outside a partial checkout)
        return f"unknown ({type(e).__name__})"


def label_for(arm, per, valid):
    """The arm's own label: the max's (work and misses) for v5, the round-3 rule (work per energy) for v3's grid."""
    return label_max(per, valid) if arm == "v5" else label(per, valid=valid)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=int, default=100)
    ap.add_argument("--scale", type=int, default=1)
    ap.add_argument("--organisms", default="1,2,3,4,5,6,7")
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--out", required=True)
    ap.add_argument("--first", type=int, default=0, help="first run index (a shard of a larger run starts here)")
    ap.add_argument("--arm", choices=("v5", "compass"), default="v5",
                    help="v5: the engine's law on the v5 catalog; compass: the v3 law on v3's catalog (its stored grid)")
    ap.add_argument("--catalog", default="", help="a muscle catalog (default: the arm's own)")
    ap.add_argument("--stack", choices=("realms", "body"), default="",
                    help="the four stacked: each realm's own body (v5 default) or one body (v3's stored grid)")
    ap.add_argument("--load", choices=tuple(LOADS), default="normal",
                    help="the organisms' work demand: their own, the climb, or work waiting in line (realms/harness.py)")
    ap.add_argument("--deadline-min", type=float, default=0.0,
                    help="start no run that would end after this many minutes (each finished run is kept as it ends; "
                         "a runner's job is cut at 6 hours, so a shard hands in what it finished, never nothing)")
    a = ap.parse_args(argv)
    cat = a.catalog or CATALOGS[a.arm]
    stack_mode = a.stack or ("realms" if a.arm == "v5" else "body")
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    keys = [ORGS[k][0] for k in a.organisms.split(",")]
    jobs = [(k, a.scale, SEED0 + a.first + i, a.arm, cat, stack_mode, a.load) for i in range(a.runs) for k in keys]
    t0 = time.time()
    res = {k: {} for k in keys}
    commit = subprocess.run(["git", "-c", "safe.directory=*", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    head = {"runs": a.runs, "first": a.first, "scale": a.scale, "commit": commit, "engine": engine(), "arm": a.arm,
            "load": a.load, "catalog": str(Path(cat).relative_to(ROOT)), "stack": stack_mode}

    def save(complete):
        """SCALE.json as it stands: rewritten whole after every finished run (never half-written), so a shard cut short
        still hands in every run it finished."""
        tmp = out / "SCALE.json.tmp"
        tmp.write_text(json.dumps({**head, "complete": complete, "runs_done": sum(len(v) for v in res.values()),
                                   "summary": summary, "per_run": {k: {str(s): c for s, c in v.items()} for k, v in res.items()}}) + "\n")
        tmp.replace(out / "SCALE.json")

    summary, longest, todo, stopped = {}, {}, iter(jobs), False
    with ProcessPoolExecutor(a.workers) as ex:
        running = {}
        while True:
            while not stopped and len(running) < a.workers:
                j = next(todo, None)
                if j is None:
                    break
                left = a.deadline_min * 60.0 - (time.time() - t0)
                # it would not finish: hand in what is done. A run's time is known once a run of its organism has finished;
                # until then it starts (the job's own limit is the backstop), so a shard always hands in its first run
                known = longest.get(j[0])
                if a.deadline_min and known is not None and left < 1.25 * known:
                    print(f"deadline: {left / 60:.0f} min left, a run of {organism_name(j[0])} takes "
                          f"{known / 60:.0f}; no more runs started", flush=True)
                    stopped = True
                    break
                running[ex.submit(job, j)] = j
            if not running:
                break
            done, _ = wait(running, return_when=FIRST_COMPLETED)
            for f in done:
                del running[f]
                k, seed, c = f.result()
                res[k][seed] = c
                longest[k] = max(longest.get(k, 0.0), c["wall_s"])
                save(False)
                n = sum(len(v) for v in res.values())
                if n % max(1, len(jobs) // 20) == 0:
                    print(f"{n}/{len(jobs)} done, {time.time() - t0:.0f} s", flush=True)
    names = {v[0]: v[1] for v in ORGS.values()}
    L = [f"# Seven organisms, {a.runs} runs, {a.scale}x size, {LOADS[a.load]}", "",
         f"Evidence class **S** (models). Commit `{commit[:12]}`, seeds {SEED0 + a.first}-{SEED0 + a.first + a.runs - 1}"
         + (f" ({sum(len(v) for v in res.values())} of {len(jobs)} runs finished before the deadline)" if stopped else "")
         + f", {a.scale} cop{'y' if a.scale == 1 else 'ies'} "
         f"of each organism on one clock, {time.time() - t0:.0f} s on {a.workers} workers. Native: each organism's own "
         "controllers. Omni: " + (f"the v5 muscle law (`realms/compass_arm_v5.py`), engine {head['engine']}" if a.arm == "v5" else
                                  "the v3 compass law on every muscle (`realms/compass_arm.py`)")
         + f", catalog `{Path(cat).relative_to(ROOT)}`, the four stacked as "
         + ("each realm's own body on one clock (the native identical to each realm's)" if stack_mode == "realms" else "one body")
         + ". Harness `tools/run_scale.py`.", "",
         "Band first (the founder's rule): no win unless the time over the service line is no higher than native's "
         "(violations, mean over runs, at or under 0 pp).", "",
         "| # | Organism | Muscles | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |",
         "|---|---|---:|---|---|---:|---:|---:|---:|---|"]
    for num, (k, nm) in ORGS.items():
        if not res.get(k):                                     # not in this shard, or no run of it finished in time
            continue
        per = [res[k][s] for s in sorted(res[k])]
        sm = summarize(per)
        lab = label_for(a.arm, per, all(c["restore_ok"] for c in per))
        summary[k] = {"label": lab, **{q: list(v) for q, v in sm.items()}, "runs": len(per)}
        f = lambda q, s=100.0, u="%": f"{s * sm[q][0]:+.3f}{u} ({s * sm[q][1]:+.3f} to {s * sm[q][2]:+.3f})"
        band = "held" if sm["viol_pp"][0] <= 0.0 else "NOT held"
        summary[k]["band_first"] = band
        L.append(f"| {num} | {nm} | {sum(len(rows_for(r, a.scale, cat)) for r in REALMS) if organism_name(k) == STACK else len(rows_for(k, a.scale, cat))} | **{lab}** | {band} | {f('work')} | "
                 f"{f('viol_pp', 1.0, '')} | {f('energy')} | {f('primary')} | {all(c['restore_ok'] for c in per)} |")
    cut_rows = []
    for num, (k, nm) in ORGS.items():
        per = [res[k][s] for s in sorted(res.get(k, {}))]
        rungs = sorted({m for c in per for m in c.get("cuts", {})}, key=int)
        for m in rungs:
            sm = summarize([c["cuts"][m] for c in per if m in c.get("cuts", {})])
            summary.setdefault(k, {}).setdefault("cuts", {})[m] = {q: list(v) for q, v in sm.items()}
            f = lambda q, s=100.0, u="%": f"{s * sm[q][0]:+.3f}{u} ({s * sm[q][1]:+.3f} to {s * sm[q][2]:+.3f})"
            cut_rows.append(f"| {num} | {nm} | the first {m} of {a.scale} | {f('work')} | {f('viol_pp', 1.0, '')} | {f('energy')} | {f('primary')} |")
    if cut_rows:
        L += ["", f"## The stack cut down: the same {a.scale}-copy runs read at their first 1, 10 and 100 copies", "",
              "The stack of copies is one organism; the first m copies of it are read from the same run, plant for plant, so a "
              "rung holds those copies and no others (the founder's order of 25 October).", "",
              "| # | Organism | Copies | Work | Misses (pp) | Power given | Work per energy |", "|---|---|---|---:|---:|---:|---:|", *cut_rows]
    (out / "SCALE.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    save(not stopped)
    print("\n".join(L))


if __name__ == "__main__":
    main()
