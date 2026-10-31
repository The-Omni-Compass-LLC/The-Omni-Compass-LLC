# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The injection grid: one batch of the Python's 500 Monte Carlo injections through every organism, native and with
Omni-Compass on native, and through every governor sitting on each organism, at 1, 10, 100 and 500 runs and 1, 10, 100
and 500 organisms stacked.

The founder's order of 25 October: "the 20 also have to be a one run, 10 run, 100 run [and 500] ... One organism, 10
organism, 100 organism [and 500] ... In line with python Monte Carlo [RK4] and c++ ... All injections come from the Python
through the C++ through any organism native and or with OmniCompass on it ... the same injection to all the organisms to see
how each react ... all the orchestrators to have the same injection ran through. Those orchestrators sit on the same
organism. And there lies the third arm."

The batch. One set of the Python's jump generator (tools/engine_runs.py): base B, 500 injections, injection k drawing its
seed from seed_k = B + k·0x9E3779B9 mod 2³² (engine_runs.jump), the same seeds the Python's 500 runs of the engine use, the
same seeds the C++ engine runs (cpp/tools/engine_runs.cpp) and the live benchmark engine's page recomputes; the batch is named by its
base and by the SHA-256 digest of those runs' receipts, and carries the C++ engine's digest of the same runs. An injection is
one seed: every plant of every organism draws its demand noise, its weather and its disturbances from it
(realms/harness.py seed_for, keyed by the muscle and the seed), under the climb (CLIMB: the load stepping by one, 1 2 3 2 3
4 ..., level 4 the organism's own load, 8 twice it), for 240 decisions of 15 s, the brain going silent at 80% and the lease
walking every setting back to native. The same injection reaches every organism and every arm.

The organisms. The nine organisms the realms harness runs (tools/scenarios_20.py ORGANISMS: the spine, the four realms, the
four stacked, the whole tower, the orchestra, the live benchmark engine's sixty muscles); the tenth, the whole organism, is a
composition of real measured tables and takes no injection (tools/scenarios_20.py reads it).

The arms. Native (every plant under its own native controller) and Omni-Compass on native (the max, realms/compass_arm_v5.py
V5CFG, on top of every native controller). Omni-Compass is never by itself (the founder's order of 25 October).

The governors, the third arm. Each of the fourteen governors and orchestrators the founder named is its own body of the
catalog muscles that stand for its knobs (tools/run_orchestra.py bodies, the mapping of tools/governors_page.py). On an
organism the governor sits as one more body on the organism's clock, run on the same injection: "the governor on the
organism" is the organism and the governor's body, each under its own native controllers; "Omni-Compass on top of the
governor" is the same two bodies with Omni-Compass on top of both. The bodies share the clock and the injection, not a power
line or a room, so the pair is the organism's run joined with the governor's own run, muscle for muscle. The orchestra is the
governors' own muscles, every governor already inside it, so no governor is added to it.

The grid. Runs N in 1, 10, 100, 500 and organisms stacked M in 1, 10, 100, 500. Run k of a cell (k = 0 to N−1) stacks M
copies of the organism, copy c receiving injection k + c (mod 500): every cell is drawn from the one batch of 500, so a cell
whose N × M passes 500 reuses injections across its runs (with 500 organisms stacked, every run holds the whole batch). The
copies are separate clusters on one clock: they share no power line or room, so a stacked run's every gauge is the mean of its
copies', decision by decision. (The scale grid of the page's section 4c stacks its copies in one body instead.)

Per muscle. Every gauge is read per muscle: the work index (already the mean over the muscles of each one's work against native's
own mean rate), the share of the muscles over their line, and the power per muscle. Two ways on the same muscles read the same
change either way; a governor's way carries its own body's muscles beside the organism's, and per muscle it is read against the
organism alone like for like, never counted worse for having more muscles. A governor's knobs run under their own native
controllers in our models, so its way reads native's work index by construction (each native body's index averages 1 over a
run); what it moves is the share over the line and the power of its knobs.

The reading. For each pair (Omni-Compass on native against native; the governor on the organism against native; Omni-Compass
on top of the governor against the governor, and against native) and each gauge (work, up; muscles over the line, down; power,
spent), each run's change per decision against its reference, averaged over the run's 24 blocks of ten decisions, with its
95% interval by Student t over the blocks (docs/engine/export_harness_trace.py gauges, interval), relative to the reference's
mean; the cell's word by the founder's rule of 24 October (tools/readings.py three_run_reading) over its N runs: the mean of
the runs' changes, under 0.5% STEADY, from 0.5% up GAIN, LOSS or power given by the gauge's aim, in all N of our runs when every
run is clear of the noise the same way, else by the mean of our N runs with the count beyond the noise; runs that moved 0.5%
or more in opposite directions disagree. One batch is one run in the sense of the key's three-run rule; its three-run reading
is three batches (three bases). Evidence class S (our own models).

  python3 tools/injection_grid.py [--base B] [--workers N] [--organisms a,b] [--runs 500] [--cache DIR]
  python3 tools/injection_grid.py --shard I/N --cache-only   (one of N shards of the bodies, cached for the run that reads them;
                                                              .github/workflows/injection-grid.yml)
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime
import hashlib
import json
import math
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.legal import stamp  # noqa: E402
from tools.readings import (GAIN, STEADY, LOSS, GIVEN, DISAGREE, IN_ALL_THREE, MEAN_OF_THREE, OWN_RUNS, HIGHER, LOWER,  # noqa: E402
                            SPENT, aim, classify, three_run_reading)
from omnicompass.student_t import t95  # noqa: E402
import tools.scenarios_20 as S  # noqa: E402
from tools.engine_runs import jump  # noqa: E402
from tools.run_orchestra import bodies as orchestra_bodies  # noqa: E402
from tools.governors_page import GOVERNORS  # noqa: E402

OUT = ROOT / "results" / "injection_grid"
CACHE = ROOT / ".cache" / "injection_grid"
BATCH = 500
RUNS = (1, 10, 100, 500)
COPIES = (1, 10, 100, 500)
STEPS = S.ORGANISM_STEPS
BLOCK = 10
GAUGES = (("work", "work", "up", HIGHER), ("over", "share of muscles over the line", "down", LOWER), ("power", "power per muscle", "spent", SPENT))
ARMS = ("native", "on_native")
HARNESS_ARM = {"native": "native", "on_native": "v5"}
GOV_NAMES = {k: name for k, name, *_ in GOVERNORS}
ORGS = [(k, name) for k, name, _ in S.ORGANISMS if k != S.WHOLE]


def newest_batch(base=None):
    """The Python's newest 500-run set (or the one with this base): its base, digest and the C++ engine's digest."""
    fs = sorted((ROOT / "results" / "engine_runs").glob("ENGINE_RUNS_*.json"),
                key=lambda f: (json.loads(f.read_text(encoding="utf-8")).get("written", ""), f.name))
    if base is not None:
        fs = [f for f in fs if json.loads(f.read_text(encoding="utf-8")).get("base") == base]
    if not fs:
        raise SystemExit("no record of the Python's runs for that base in results/engine_runs")
    d = json.loads(fs[-1].read_text(encoding="utf-8"))
    c = d.get("cpp") or {}
    return {"file": str(fs[-1].relative_to(ROOT)), "base": d["base"], "runs": d["runs"], "jump": d.get("jump"),
            "python_digest": d["digest"], "cpp_digest": c.get("digest"), "cpp_same": c.get("same"), "cpp_agree": c.get("agree"),
            "written": d.get("written"), "engine": d.get("engine")}


# ------------------------------------------------------------------------------------------------------------ the runs
def series(name, rs, seed, arm):
    """One body (or the four stacked) on one injection: the per-decision work, muscles over the line and power, native's
    per-muscle mean rate the work's reference (export_harness_trace.gauges), for native and the arm on the same seed."""
    nat, _ = S.recorded_run(name, rs, seed, "native")
    out = {}
    if arm == "native":
        g = S.H.gauges(nat, nat)
        out["native"] = np.array([g["work"][0], g["over"][0], g["power"][0]], dtype=np.float64)
        return out
    other, _ = S.recorded_run(name, rs, seed, HARNESS_ARM[arm])
    g = S.H.gauges(nat, other)
    out["native"] = np.array([g["work"][0], g["over"][0], g["power"][0]], dtype=np.float64)
    out[arm] = np.array([g["work"][1], g["over"][1], g["power"][1]], dtype=np.float64)
    return out


def job(args):
    """(kind, key, k, base): one body on injection k, native and Omni-Compass on native, as float32 (3, 240) each."""
    kind, key, k, base = args
    seed = jump(base, k)
    rows = ORG_ROWS[key] if kind == "org" else GOV_ROWS[key]
    name = key if kind == "org" else S.ORCHESTRA          # a governor's body runs as one body, as the orchestra's do
    out = series(name, rows, seed, "on_native")
    return kind, key, k, out["native"].astype(np.float32), out["on_native"].astype(np.float32)


ORG_ROWS, GOV_ROWS = {}, {}
CACHED = []       # the cached bodies' own record of when they were computed (a run that reads a cache says so)


def setup(organisms=None):
    rows = S.R.catalog(str(ROOT / "realms" / "catalog_v5.csv"))
    g = S.organism_rows(rows)
    for k, _ in ORGS:
        if not organisms or k in organisms:
            ORG_ROWS[k] = g[k]
    for k, rs in orchestra_bodies(rows).items():
        if k != S.ORCHESTRA:
            GOV_ROWS[k] = rs
    return rows


def muscles(kind, key):
    rs = ORG_ROWS[key] if kind == "org" else GOV_ROWS[key]
    return len(S.flat(key, rs)) if kind == "org" else len(rs)


def shard_of(bodies, shard):
    """Shard I of N (1-based): the bodies dealt out heaviest first, each to the shard with the fewest muscles so far."""
    if not shard:
        return bodies
    i, n = shard
    load, mine = [0] * n, []
    for b in sorted(bodies, key=lambda b: (-muscles(*b), b)):
        j = load.index(min(load))
        load[j] += muscles(*b)
        if j == i - 1:
            mine.append(b)
    return mine


def run_all(base, workers, n_inj, cache: Path, shard=None):
    """Every organism and every governor's body on every injection of the batch, cached per body so a cut run resumes."""
    cache.mkdir(parents=True, exist_ok=True)
    data = {}
    todo = []
    bodies = shard_of([("org", k) for k in ORG_ROWS] + [("gov", k) for k in GOV_ROWS], shard)
    for kind, key in bodies:
        f = cache / f"{base}_{kind}_{key}_{n_inj}.npz"
        if f.exists():
            z = np.load(f)
            data[(kind, key)] = (z["native"], z["on_native"])
            side = f.with_suffix(".json")
            if side.exists():
                CACHED.append(json.loads(side.read_text(encoding="utf-8")))
        else:
            data[(kind, key)] = (np.zeros((n_inj, 3, STEPS), np.float32), np.zeros((n_inj, 3, STEPS), np.float32))
            todo.append((kind, key))
    left = {b: n_inj for b in todo}
    jobs = [(kind, key, k, base) for kind, key in sorted(todo, key=lambda b: -muscles(*b)) for k in range(n_inj)]
    t0 = time.time()
    if jobs:
        with cf.ProcessPoolExecutor(workers, initializer=setup, initargs=(list(ORG_ROWS),)) as ex:
            for n, (kind, key, k, nat, arm) in enumerate(ex.map(job, jobs, chunksize=4), 1):
                data[(kind, key)][0][k], data[(kind, key)][1][k] = nat, arm
                left[(kind, key)] -= 1
                if not left[(kind, key)]:
                    np.savez_compressed(cache / f"{base}_{kind}_{key}_{n_inj}.npz", native=data[(kind, key)][0], on_native=data[(kind, key)][1])
                    (cache / f"{base}_{kind}_{key}_{n_inj}.json").write_text(json.dumps(
                        {"body": f"{kind}:{key}", "computed": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                         "after_s": round(time.time() - t0)}), encoding="utf-8")
                    print(f"  {kind} {key}: {n_inj} injections done ({time.time() - t0:.0f} s)", flush=True)
    return data, round(time.time() - t0)


# --------------------------------------------------------------------------------------------------------- the reading
def stacked(a, m):
    """The batch's runs stacked m at a time: run k = copies on injections k ... k+m−1 (mod the batch). a: (n, 3, steps), per
    muscle; every gauge the mean of the copies'."""
    n = a.shape[0]
    reps = -(-(n + m - 1) // n)                            # the batch wrapped as often as m copies need (copy c: injection k + c mod n)
    ext = np.concatenate([a] * reps, axis=0)[:n + m - 1]
    cs = np.concatenate([np.zeros((1,) + a.shape[1:]), np.cumsum(ext.astype(np.float64), axis=0)], axis=0)
    return (cs[m:m + n] - cs[0:n]) / m


def per_muscle(a, n):
    """One body's gauges per muscle: the work index as it is (a mean over the muscles already), over and power divided by n."""
    out = a.copy()
    out[:, 1:, :] /= n
    return out


def joined(org, gov, n_org, n_gov):
    """The organism and a governor's body on one clock, per muscle of both: the work index the mean over every muscle, the share
    over the line and the power per muscle their sums over every muscle."""
    out = (org + gov) / (n_org + n_gov)
    out[:, 0, :] = (n_org * org[:, 0, :] + n_gov * gov[:, 0, :]) / (n_org + n_gov)
    return out


def run_changes(x, y):
    """Each run's change against its reference, per gauge: (n, 3) relative change, lower and upper 95% bounds, and the
    reference's mean, from the run's 24 blocks of ten decisions (export_harness_trace.interval)."""
    d = y - x
    nb = d.shape[2] // BLOCK
    b = d[:, :, :nb * BLOCK].reshape(d.shape[0], d.shape[1], nb, BLOCK).mean(axis=3)
    m = b.mean(axis=2)
    half = t95(nb - 1) * b.std(axis=2, ddof=1) / math.sqrt(nb)
    base = x.mean(axis=2)
    scale = np.where(np.abs(base) > 1e-12, np.abs(base), 1.0)
    return m / scale, (m - half) / scale, (m + half) / scale, base, m


def words_for(n):
    return ("in our one run", "by our one run") if n == 1 else (f"in all {n} of our runs", f"by the mean of our {n} runs")


def cell_reading(rel, lo, hi, base, diff, n, aim_):
    """The founder's rule of 24 October over n runs (tools/readings.py three_run_reading), its words for n runs."""
    rs = [{"native": float(base[i]), "diff": float(diff[i]), "ci95": [float(lo[i] * abs(base[i]) if abs(base[i]) > 1e-12 else lo[i]),
                                                                       float(hi[i] * abs(base[i]) if abs(base[i]) > 1e-12 else hi[i])]}
          for i in range(n)]
    text = three_run_reading(rs, aim_).replace("**", "")
    allw, meanw = words_for(n)
    text = text.replace(IN_ALL_THREE, allw).replace(MEAN_OF_THREE, meanw).replace("the three runs' mean", f"the {n} runs' mean")
    c = classify(text, aim_)
    word = {"gain": GAIN, "loss": LOSS, "given": GIVEN, "noise": STEADY, "same": STEADY, "disagree": DISAGREE}.get(c, STEADY)
    return text, word


def pair_cells(xa, ya):
    """Every (N, M) cell of one pair: per gauge the mean change of its runs, its word and reading, the runs beyond the noise,
    the smallest and largest run's change, and every run's change (the page recomputes the means from the runs)."""
    out = {}
    for m in COPIES:
        X, Y = stacked(xa, m), stacked(ya, m)
        rel, lo, hi, base, diff = run_changes(X, Y)
        for n in RUNS:
            if n > X.shape[0]:
                continue
            cell = {}
            for gi, (gk, _, _, aim_) in enumerate(GAUGES):
                r, l, h = rel[:n, gi], lo[:n, gi], hi[:n, gi]
                text, word = cell_reading(r, l, h, base[:n, gi], diff[:n, gi], n, aim_)
                cell[gk] = {"mean": round(float(r.mean()), 6), "word": word, "reading": text,
                            "beyond": int(((l > 0) | (h < 0)).sum()), "min": round(float(r.min()), 6), "max": round(float(r.max()), 6)}
            out[f"{n}x{m}"] = cell
    return out


def build(base=None, workers=None, organisms=None, n_inj=BATCH, cache=CACHE):
    batch = newest_batch(base)
    setup(organisms)
    from tools.omni_version import engine_files, version_of, digest
    snap = engine_files()
    git = lambda *a: subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    frozen = S.FROZEN + ["tools/injection_grid.py", "tools/scenarios_20.py", "tools/engine_runs.py"]
    run = {"started": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "commit": git("rev-parse", "HEAD"),
           "dirty": bool(git("status", "--porcelain", "--", *frozen)), "engine": version_of(snap) or "undeclared",
           "engine_digest": digest(snap), "class": "S", "load": "climb", "steps": STEPS, "decision_s": S.DECISION_S,
           "workers": workers or os.cpu_count() or 2, "injections": n_inj}
    data, run["elapsed_s"] = run_all(batch["base"], run["workers"], n_inj, Path(cache))
    if CACHED:
        run["cached"] = {"bodies": len(CACHED), "first": min(c["computed"] for c in CACHED), "last": max(c["computed"] for c in CACHED),
                         "note": "these bodies' runs were read from the cache their own run wrote (on GitHub, the shards); elapsed_s is this read"}
    rec = {"title": "The injection grid: the Python's 500 injections through every organism, native and with Omni-Compass on native, "
                    "and through every governor on each organism, at 1, 10, 100 and 500 runs and 1, 10, 100 and 500 organisms",
           "class": "S", "own_runs": OWN_RUNS, "batch": batch, "run": run, "tiers": {"runs": list(RUNS), "copies": list(COPIES)},
           "rule": ("run k of a cell stacks M copies, copy c on injection k + c (mod 500); the copies are separate clusters on one "
                    "clock; every gauge per muscle (the work index, the share of muscles over the line, the power per muscle; a "
                    "governor's way per muscle of the organism and the governor's body together) and the mean of the copies'; "
                    "each run's change per decision "
                    "against its reference over 24 blocks of ten decisions with its 95% interval (Student t); the cell's word by the "
                    "founder's rule of 24 October over its N runs (tools/readings.py three_run_reading)"),
           "gauges": [{"key": k, "name": n, "aim": a} for k, n, a, _ in GAUGES],
           "organisms": [{"key": k, "name": nm, "muscles": muscles("org", k)} for k, nm in ORGS if k in ORG_ROWS],
           "governors": [{"key": k, "name": GOV_NAMES.get(k, k), "muscles": muscles("gov", k)} for k in GOV_ROWS],
           "whole": "the whole organism is a composition of real measured tables (tools/whole_system.py) and takes no injection; "
                    "tools/scenarios_20.py reads it, native and with Omni-Compass on native",
           "means_note": "each run's mean over its decisions, per body as the harness counts it (work index, muscles over the line, "
                         "power in kW), native and with Omni-Compass on native; the cells read them per muscle (over and power divided "
                         "by the body's muscles, a governor's way by the organism's and the body's together)",
           "cells": {}, "runs_m1": {}, "means": {"org": {}, "gov": {}}}
    for (kind, key), (nat, arm) in data.items():
        rec["means"][kind][key] = {"native": np.round(nat.mean(axis=2).astype(np.float64), 6).tolist(),
                                   "on_native": np.round(arm.mean(axis=2).astype(np.float64), 6).tolist()}
    for key in ORG_ROWS:
        nat_raw, arm_raw = (a.astype(np.float64) for a in data[("org", key)])
        n_org = muscles("org", key)
        nat, arm = per_muscle(nat_raw, n_org), per_muscle(arm_raw, n_org)
        cells = {"on_native|native": pair_cells(nat, arm)}
        rel, _, _, _, _ = run_changes(nat, arm)
        rec["runs_m1"][key] = {"on_native|native": np.round(rel, 6).tolist()}
        if key != S.ORCHESTRA:
            for g in GOV_ROWS:
                gn, ga = (a.astype(np.float64) for a in data[("gov", g)])
                n_gov = muscles("gov", g)
                gov_nat, gov_omni = joined(nat_raw, gn, n_org, n_gov), joined(arm_raw, ga, n_org, n_gov)
                cells[f"gov:{g}|native"] = pair_cells(nat, gov_nat)
                cells[f"omni_gov:{g}|gov:{g}"] = pair_cells(gov_nat, gov_omni)
                cells[f"omni_gov:{g}|native"] = pair_cells(nat, gov_omni)
        rec["cells"][key] = cells
        print(f"  cells {key}: {len(cells)} pairs × {len(RUNS) * len(COPIES)} cells", flush=True)
    rec["best"] = best_ways(rec)
    rec["loss_cells"] = loss_counts(rec)
    return rec


def best_ways(rec):
    """For every organism and cell, every way ranked against native: work first (a rise is GAIN), then muscles over the line
    (a fall is GAIN), power shown beside (a rise is power given)."""
    out = {}
    for key, cells in rec["cells"].items():
        ways = [("on_native", "on_native|native")] + [(p.split("|")[0], p) for p in cells if p.endswith("|native") and p != "on_native|native"]
        out[key] = {}
        for nm in next(iter(cells.values())):
            rows = []
            for w, p in ways:
                c = cells[p][nm]
                rows.append({"way": w, "work": c["work"]["mean"], "over": c["over"]["mean"], "power": c["power"]["mean"],
                             "words": [c["work"]["word"], c["over"]["word"], c["power"]["word"]]})
            rows.sort(key=lambda r: (-r["work"], r["over"]))
            out[key][nm] = rows
    return out


def digest_of(rec):
    """The SHA-256 of every cell's mean, rounded to six decimals, in a fixed order: the page computes the same from the runs."""
    lines = []
    for key in sorted(rec["cells"]):
        for p in sorted(rec["cells"][key]):
            for nm in sorted(rec["cells"][key][p], key=lambda s: tuple(int(x) for x in s.split("x"))):
                c = rec["cells"][key][p][nm]
                lines.append(f"{key}|{p}|{nm}|" + "|".join(f"{c[g]['mean']:.6f}" for g, *_ in GAUGES))
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def write_md(out: Path, rec):
    b, run = rec["batch"], rec["run"]
    L = ["# The injection grid: the Python's 500 injections through every organism and every governor (modelled)", ""]
    L += [f"Evidence class **S** (our own models). The batch: base **{b['base']}**, {b['runs']} injections, injection k's seed "
          f"{b['jump']}; the Python's runs of it digest `{b['python_digest'][:16]}…` (`{b['file']}`), the C++ engine's "
          f"`{(b['cpp_digest'] or 'not run')[:16]}…` ({'the same' if b['cpp_same'] else 'not compared'}, {b['cpp_agree']} runs agree). "
          f"Engine **{run['engine']}**, commit `{run['commit'][:12]}`{' (uncommitted changes in the files it stands on)' if run['dirty'] else ''}, "
          f"run {run['started']}, {run['elapsed_s']} s on {run['workers']} processes. Written by `python3 tools/injection_grid.py`; every "
          f"cell's every gauge, and every run's change, in `{out.name}/INJECTION_GRID_{b['base']}.json`.", "",
          "**How it is built.** " + rec["rule"] + ". " + rec["whole"][0].upper() + rec["whole"][1:] + ".", "",
          "## Omni-Compass on native against native, every organism, every cell", "",
          "Each cell: work · muscles over the line · power, the mean change of its runs and its word (the number carries the word's sign).", ""]
    tiers = [f"{n}x{m}" for m in COPIES for n in RUNS]
    L += ["| Organism | Muscles | " + " | ".join(f"{t.split('x')[0]} run{'s' if t.split('x')[0] != '1' else ''} × {t.split('x')[1]} org." for t in tiers) + " |",
          "|---|---:|" + "---|" * len(tiers)]
    from tools.readings import by_word
    def short(c):
        return " · ".join(f"{c[g]['word']} {by_word(100 * c[g]['mean'], c[g]['word'] if c[g]['word'] in (GAIN, LOSS, GIVEN, STEADY) else None, digits=2)}" for g, *_ in GAUGES)
    for o in rec["organisms"]:
        cells = rec["cells"][o["key"]]["on_native|native"]
        L.append(f"| {o['name']} | {o['muscles']:,} | " + " | ".join(short(cells[t]) for t in tiers if t in cells) + " |")
    L += ["", "## Every way on each organism at 500 runs × 1 organism, ranked by work, then by muscles over the line", "",
          "The governor's way is the organism with the governor's body on its clock, on the same injections; Omni-Compass on top "
          "of the governor is both with Omni-Compass on top. Read against native, the organism alone.", ""]
    for o in rec["organisms"]:
        rows = rec["best"][o["key"]].get("500x1") or []
        L += [f"**{o['name']}**: " + "; ".join(f"{i + 1}. {way_name(r['way'])} (work {r['words'][0]}, over {r['words'][1]}, power {r['words'][2]})"
                                                 for i, r in enumerate(rows[:6])) + (f"; {len(rows) - 6} more in the record" if len(rows) > 6 else ""), ""]
    losses = [(o["name"], p, nm, g, rec["cells"][o["key"]][p][nm][g]["reading"]) for o in rec["organisms"] for p in rec["cells"][o["key"]]
              for nm in rec["cells"][o["key"]][p] for g, *_ in GAUGES if rec["cells"][o["key"]][p][nm][g]["word"] == LOSS]
    mine = [x for x in losses if is_omni(x[1])]
    theirs = [x for x in losses if not is_omni(x[1])]
    L += [f"## Every LOSS cell of Omni-Compass ({len(mine)})", "",
          "A LOSS counts against Omni-Compass only where the way read is Omni-Compass's: on native against native, on top of a "
          "governor against that governor, or on top of a governor against native.", ""]
    L += [f"- {n}, {pair_name(p)}, {nm.replace('x', ' runs × ')} organisms: {g}, {r}" for n, p, nm, g, r in mine[:400]] or ["- none"]
    if len(mine) > 400:
        L.append(f"- and {len(mine) - 400} more, every one in the record")
    L += ["", f"## The governors' own LOSS cells against native ({len(theirs)})", "",
          "Each governor on the organism, read against native: the governor's own reading, shown as the governor's, never counted "
          "as Omni-Compass's.", ""]
    L += [f"- {n}, {pair_name(p)}, {nm.replace('x', ' runs × ')} organisms: {g}, {r}" for n, p, nm, g, r in theirs[:400]] or ["- none"]
    if len(theirs) > 400:
        L.append(f"- and {len(theirs) - 400} more, every one in the record")
    (out / f"INJECTION_GRID_{b['base']}.md").write_text("\n".join(stamp(L + ["", OWN_RUNS])) + "\n", encoding="utf-8")


def is_omni(pair):
    """A pair whose way is Omni-Compass's (its LOSS is Omni-Compass's); a governor's way against native is the governor's own."""
    return pair.split("|")[0] == "on_native" or pair.startswith("omni_gov:")


def loss_counts(rec):
    """Every LOSS cell, Omni-Compass's and the governors' own, counted apart."""
    out = {"omni": 0, "governors": 0}
    for key, pairs in rec["cells"].items():
        for p, cells in pairs.items():
            n = sum(c[g]["word"] == LOSS for c in cells.values() for g, *_ in GAUGES)
            out["omni" if is_omni(p) else "governors"] += n
    return out


def way_name(w):
    if w == "on_native":
        return "Omni-Compass on native"
    if w.startswith("omni_gov:"):
        return f"Omni-Compass on top of {GOV_NAMES.get(w[9:], w[9:])}"
    if w.startswith("gov:"):
        return GOV_NAMES.get(w[4:], w[4:])
    return w


def pair_name(p):
    a, b = p.split("|")
    return f"{way_name(a)} against {'native' if b == 'native' else way_name(b)}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", type=int, default=None, help="the batch's base (default: the Python's newest set)")
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--organisms", default="", help="a comma-separated subset of the organisms (a look; the record holds all nine)")
    ap.add_argument("--runs", type=int, default=BATCH, help="injections to run (a look below 500; the record holds 500)")
    ap.add_argument("--cache", default=str(CACHE))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--shard", default="", help="I/N: run only shard I of N of the bodies (with --cache-only)")
    ap.add_argument("--cache-only", action="store_true", help="run the bodies into the cache and write no record")
    a = ap.parse_args(argv)
    if a.cache_only:
        shard = tuple(int(x) for x in a.shard.split("/")) if a.shard else None
        batch = newest_batch(a.base)
        setup([x for x in a.organisms.split(",") if x])
        mine = shard_of([("org", k) for k in ORG_ROWS] + [("gov", k) for k in GOV_ROWS], shard)
        print(f"injection grid, batch {batch['base']}{f', shard {a.shard}' if shard else ''}: {', '.join(f'{k} {b}' for k, b in mine)} "
              f"({sum(muscles(*b) for b in mine):,} muscles)", flush=True)
        _, el = run_all(batch["base"], a.workers, a.runs, Path(a.cache), shard)
        print(f"cached in {a.cache} ({el} s)")
        return 0
    rec = build(a.base, a.workers, [x for x in a.organisms.split(",") if x], a.runs, a.cache)
    rec["cells_digest"] = digest_of(rec)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    name = f"INJECTION_GRID_{rec['batch']['base']}" + ("" if a.runs == BATCH and not a.organisms else f"_look_{a.runs}")
    (out / f"{name}.json").write_text(json.dumps(rec, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")
    if a.runs == BATCH and not a.organisms:
        write_md(out, rec)
    print(f"injection grid: batch {rec['batch']['base']}, {len(rec['organisms'])} organisms, {len(rec['governors'])} governors, "
          f"{rec['run']['elapsed_s']} s -> {out / (name + '.json')} (cells digest {rec['cells_digest'][:16]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
