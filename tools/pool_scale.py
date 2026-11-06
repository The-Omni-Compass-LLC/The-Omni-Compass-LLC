#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Pool the shards of an organism run (tools/run_scale.py, one SCALE.json per shard) into one receipt.

  python3 tools/pool_scale.py OUT.md parts/*/SCALE.json
"""
import glob, json, sys

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.harness import summarize  # noqa: E402
from tools.run_scale import ORGS, REALMS, CATALOGS, LOADS, SEED0, rows_for, label_for, joined  # noqa: E402
from realms.harness import STACK, organism_name  # noqa: E402


def main(out, *paths):
    files = sorted({p for g in paths for p in glob.glob(g, recursive=True)})
    per, scale, commits, arms, loads, engines, scales = {}, None, set(), set(), set(), set(), set()
    cat, stack = None, "body"
    configurations, extent = set(), 0
    if not files:
        raise ValueError("no SCALE.json shards were found")
    for f in files:
        d = json.loads(Path(f).read_text())
        scale = d["scale"]; scales.add(scale); commits.add(d["commit"][:12])
        arms.add(d.get("arm", "compass")); stack = d.get("stack", "body"); loads.add(d.get("load", "normal"))
        engines.add(d.get("engine", "not recorded"))
        configurations.add((d.get("catalog"), stack))
        cat = str(ROOT / d["catalog"]) if d.get("catalog") else None
        extent = max(extent, int(d.get("first", 0)) + int(d.get("runs", 0)))
        for k, runs in d["per_run"].items():
            target = per.setdefault(k, {})
            for seed, record in runs.items():
                if not seed.isdecimal() or int(seed) < SEED0:
                    raise ValueError(f"invalid seed {seed!r} in {f}")
                extent = max(extent, int(seed) - SEED0 + 1)
                if seed in target and json.dumps(target[seed], sort_keys=True) != json.dumps(record, sort_keys=True):
                    raise ValueError(f"conflicting duplicate result for {k}, seed {seed}")
                target[seed] = record
    assert len(arms) == 1, f"shards from different arms cannot be pooled: {sorted(arms)}"
    assert len(loads) == 1, f"shards under different loads cannot be pooled: {sorted(loads)}"
    assert len(scales) == 1, f"shards of different sizes cannot be pooled: {sorted(scales)}"
    assert len(configurations) == 1, "shards from different catalogs or stack configurations cannot be pooled"
    assert len(engines) == 1, f"shards from different engines cannot be pooled: {sorted(engines)}"
    known = sorted(e for e in engines if e.startswith("omni-"))
    assert len(known) <= 1, f"shards from different engines cannot be pooled: {known}"
    arm, load = arms.pop(), loads.pop()
    # the four stacked in v5 are the four realms' own bodies side by side on the clock, sharing nothing: where it was too
    # big to run as one (1,000 copies is 1.9 million modelled muscles, past one runner's memory), its run on a seed is the
    # four realms' runs on that seed joined plant for plant (tools/run_scale.py joined(); equal to the direct run to
    # rounding, tests/test_run_scale.py)
    n_joined = 0
    if arm == "v5" and stack == "realms" and all(r in per for r in REALMS):
        st = per.setdefault(STACK, {})
        for s in set.intersection(*(set(per[r]) for r in REALMS)) - set(st):
            parts = [per[r][s] for r in REALMS]
            if all("sums" in p for p in parts):
                st[s] = joined(parts); n_joined += 1
        if not st:
            del per[STACK]
    if not any(per.values()):
        raise ValueError("shards contain no completed runs")
    total = max(len(v) for v in per.values())
    ladder = (1, 10, 100, 500)      # the ladder of the Python's 500-run Monte Carlo (the founder's order of 25 October)
    ceiling = next((n for n in ladder if n >= extent), extent)
    prefixes = [n for n in ladder if n <= ceiling]
    if ceiling not in prefixes:
        prefixes.append(ceiling)
    law = ("the v5 muscle law (`realms/compass_arm_v5.py`); engine identity recorded above" if arm == "v5" else
           "the v3 compass law on every muscle (`realms/compass_arm.py`)")
    count = lambda k: (sum(len(rows_for(r, scale, cat)) for r in REALMS) if organism_name(k) == STACK and stack == "realms"
                       else len(rows_for(k, scale, cat)))
    L = [f"# The organisms at {scale}x size, {LOADS[load]}, up to {total} completed runs; seed coverage through {extent} (pooled from {len(files)} shards)", "",
         f"Evidence class **S** (models). Engine {', '.join(known) or 'not recorded'}, commit(s) {', '.join(sorted(commits))}. "
         f"Native: each organism's own controllers. Omni: {law}. Each block is the first N runs (seeds {SEED0} on), so 1, 10, "
         "100 and 500 are nested; a block short of a run says so (Runs column: finished of the block). Band first: no win "
         "unless the time over the service line is no higher than native's. Labels describe only available observations; "
         "an incomplete block is not evidence of completing its requested prefix."
         + (f" The four stacked: {n_joined} of its runs are the four realms' runs on the same seeds joined plant for plant "
            "(its four bodies share nothing on the clock; equal to running it whole, to rounding)." if n_joined else ""), ""]
    summ = {}
    for n in prefixes:      # requested/observed seed positions, not the number of late-seed results
        L += [f"## {n} run{'s' if n > 1 else ''}", "",
              "| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |",
              "|---|---|---:|---:|---|---|---:|---:|---:|---:|---|"]
        for num, (k, nm) in ORGS.items():
            if k not in per:
                continue
            xs = [per[k][str(s)] for s in range(SEED0, SEED0 + n) if str(s) in per[k]]
            missing = [s for s in range(SEED0, SEED0 + n) if str(s) not in per[k]]
            coverage = {"runs": len(xs), "of": n, "complete": not missing, "missing_seeds": missing}
            if not xs:
                summ.setdefault(str(n), {})[k] = {**coverage, "label": "NO RUNS", "band_first": "not measured", "joined": 0}
                L.append(f"| {num} | {nm} | {count(k)} | 0 of {n} | **NO RUNS** | not measured | — | — | — | — | — |")
                continue
            ok = all(c["restore_ok"] for c in xs)
            if len(xs) >= 2:
                sm = summarize(xs); lab = label_for(arm, xs, ok)
            else:
                sm = {q: (xs[0][q], xs[0][q], xs[0][q]) for q in ("primary", "work", "energy", "viol_pp")}; lab = "ONE RUN (no label)"
            band = "held" if sm["viol_pp"][0] <= 0 else "NOT held"
            summ.setdefault(str(n), {})[k] = {**coverage, "label": lab, "band_first": band,
                                              "joined": sum(1 for c in xs if c.get("joined_from")),
                                              **{q: list(v) for q, v in sm.items()}}
            f = lambda q, s=100.0, u="%": f"{s * sm[q][0]:+.3f}{u}" + (f" ({s * sm[q][1]:+.3f} to {s * sm[q][2]:+.3f})" if len(xs) > 1 else "")
            runs = f"{len(xs)}" if len(xs) == n else f"{len(xs)} of {n}"
            L.append(f"| {num} | {nm} | {count(k)} | {runs} | **{lab}** | {band} | {f('work')} | {f('viol_pp', 1.0, '')} | "
                     f"{f('energy')} | {f('primary')} | {ok} |")
        L.append("")
    Path(out).write_text("\n".join(_legal_stamp(L)) + "\n")
    Path(out).with_suffix(".json").write_text(json.dumps({"scale": scale, "arm": arm, "load": load, "stack": stack,
                                                          "engine": known[0] if known else None, "joined_stack_runs": n_joined,
                                                          "available_runs": {k: len(v) for k, v in per.items()},
                                                          "seed_extent": extent, "summary": summ}, indent=1) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(*sys.argv[1:])
