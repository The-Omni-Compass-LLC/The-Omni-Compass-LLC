#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C table for the drone swarms (docs/OMNI_V1.md's readings, docs/SWARM_PREREGISTRATION.md): each cell run three
times as separate GitHub runs on the same frozen engine (tools/run_swarm.py). PyBullet is deterministic for a fixed step,
so the runs must give the same numbers to within one part in a thousand (PyBullet's floating point differs by that much
from one GitHub machine to the next; amendment 1 of the preregistration, made after the first A, B, C were seen and said
so): a gauge reads GAIN or LOSS in all three of our runs when all three runs agree on the sign (judged by what the gauge is
for, never by its sign; energy is a resource spent, so a rise reads power given), STEADY when the change is under one part in a
billion (nine decimal places), and "the runs differ" when they do not reproduce. A cell whose paired physics trial left the cruise native is listed
as "nothing for Omni to move"; a cell with a collision in either arm is void and listed as such. From omni-v12's runs on
(amendment 2, written before them) a cell is void only when native itself collides, and a collision with Omni-Compass on top
is a judged row, any increase a LOSS. Every row is reported, LOSS included.
Usage: python tools/swarm_abc.py A_DIR B_DIR C_DIR --out results/live/V3_SWARM.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding swarm-<cell>/swarm-<cell>.json"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.readings import with_own_runs, in_all_three, aim, EVEN_SAME, SHOWN, DETERMINISTIC_RULE, ACROSS_HEAD, ACROSS_RULE, across_cells, across_counts, reproduced_reading  # noqa: E402  (every table says whose runs these are)
from tools.repo import NAME as REPO_NAME  # noqa: E402  (the repository's name, written once)
from tools.run_swarm import GAUGES, TRIAL_OVERRIDE, with_collisions

SAME_REL = 1e-9          # "the same" only to nine decimal places of the value (tools/readings.py EXACT_REL; the referee's work order of 25 October)
REPRO_REL = 1e-3        # PyBullet reproduces to about one part in a thousand across GitHub's machines, not to the bit (amendment 1)
COUNTS = {"late_share", "reserve_breaches", "near_miss_ticks", "collisions"}      # differences, not ratios


def load(d):
    out = {}
    for f in sorted(Path(d).glob("swarm-*/swarm-*.json")):
        out[f.stem.replace("swarm-", "")] = json.loads(f.read_text())
    if not out:
        raise SystemExit(f"{d}: no swarm-<cell>/swarm-<cell>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def change(rec, k):
    n, o = (rec.get("native") or {}).get(k), (rec.get("omni") or {}).get(k)
    if n is None or o is None:
        return None
    return (o - n) if (k in COUNTS or n == 0) else (o - n) / abs(n)


def reproduced(recs, k):
    for arm in ("native", "omni"):
        v = [(r.get(arm) or {}).get(k) for r in recs]
        if any(x is None for x in v):
            return all(x is None for x in v)
        if not all(abs(x - v[0]) <= REPRO_REL * max(1.0, abs(v[0])) for x in v):
            return False
    return True


def verdict(recs, k, direction):
    """The gauge's word over the three runs: GAIN, LOSS or power given in all three of our runs by what the gauge is for (its
    declared aim: a resource spent, higher, never more or never less), STEADY, or the runs differ."""
    if not reproduced(recs, k):
        return "**the runs differ**"
    ch = [change(r, k) for r in recs]
    if any(c is None for c in ch):
        return "no value"
    if direction == "shown":
        return SHOWN
    if all(abs(c) <= SAME_REL for c in ch):
        return EVEN_SAME
    signs = {(c > 0) - (c < 0) for c in ch}
    if len(signs) > 1:
        return "**the runs differ**"
    return reproduced_reading(ch, aim(direction, k))


def engine(run):
    try:
        sha = subprocess.run(["gh", "api", f"repos/{REPO_NAME}/actions/runs/{run}", "--jq", ".head_sha"],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            return "?", "unknown"
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                             capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
        return sha[:12], (out[0] if out else "unknown")
    except (OSError, subprocess.SubprocessError):
        return "?", "unknown"


def pct(c, k):
    if c is None:
        return "n/a"
    return f"{c:+.3f}" if k in COUNTS else f"{100 * c:+.2f}%"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c"); ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = ["# Drone swarms, gym-pybullet-drones: the A/B/C three-run table (Omni v3)", "",
         "gym-pybullet-drones (University of Toronto) integrates every Crazyflie 2.x quadrotor and flies it with the position "
         "controller it ships with; that autopilot at the planner's cruise is native. Omni sits on top of it on one knob, the "
         "cruise override, inside the autopilot's own limits, spending tracking slack as speed (`docs/SWARM_PREREGISTRATION.md`). "
         "Energy is a declared model from the simulator's own motor constants, the same in both arms, with the avionics draw "
         "charged over the whole fleet window. Three separate GitHub runs on the same frozen engine: PyBullet reproduces to about one "
         "part in a thousand across GitHub's machines (disclosed in the preregistration's amendment 1, made after the first three runs "
         "were seen), so a gauge reads **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its "
         "sign; energy is a resource spent, so a rise reads **power given**) when all three runs reproduce to that tolerance and give the same sign, **STEADY, the same** under one part in a billion (nine decimal places), and **the runs differ** when they do not reproduce. A cell whose paired physics trial found a faster "
         "mission no cheaper, or not inside the safe tracking error, is listed as nothing for Omni to move; a cell with a "
         "collision in either arm is void. Every row is shown, LOSS included.", "",
         "| Run | GitHub run | Commit | Engine | Cells in the run |", "|---|---|---|---|---:|"]
    off = []; seen = []
    for tag, (run, recs) in zip("ABC", runs):
        sha, ver = engine(run)
        seen.append(ver.split(" ")[0])
        if not ver.startswith("omni-v"):
            off.append(f"{tag} (run {run}: {ver})")
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {len(recs)} |")
    label = f"Omni {seen[0][5:]}" if len(set(seen)) == 1 and seen[0].startswith("omni-v") else "the runs' engines differ"
    L[0] = L[0].replace("(Omni v3)", f"({label})")
    if len({r for r, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    # amendment 2 holds from omni-v12's runs on; the earlier tables are rebuilt as they were scored
    amend2 = all(s.startswith("omni-v") and s[6:].isdigit() and int(s[6:]) >= 12 for s in seen)
    gauges = with_collisions(GAUGES) if amend2 else GAUGES
    if amend2:
        L[2] = L[2].replace("a cell with a collision in either arm is void.", "a cell where native itself collides is void, and a collision "
                            "with Omni-Compass on top is a judged row, any increase a **LOSS** (the preregistration's amendment 2, written "
                            "before omni-v12's runs).")
    if off:
        L[2:2] = [f"**Not three runs on one frozen engine: {'; '.join(off)}.**", ""]
    cells = sorted(set().union(*(set(r) for _, r in runs)), key=lambda c: (c != "tuning", c))
    tally = {}; idle = []; void = []
    L += ["", "## Cells where Omni moved the cruise", ""]
    for c in cells:
        recs = [r.get(c) for _, r in runs]
        if any(x is None for x in recs):
            void.append((c, "missing from a run")); continue
        if amend2 and any(x["native"]["collisions"] > 0 for x in recs):
            void.append((c, "native collided, its task unsafe before Omni-Compass touches it: native "
                         + "/".join(str(x["native"]["collisions"]) for x in recs) + ", omni " + "/".join(str(x["omni"]["collisions"]) for x in recs))); continue
        if not amend2 and any(x.get("void") for x in recs):
            void.append((c, "a collision in an arm: native " + "/".join(str(x["native"]["collisions"]) for x in recs)
                         + ", omni " + "/".join(str(x["omni"]["collisions"]) for x in recs))); continue
        if not all(x.get("omni_moves") for x in recs):
            idle.append((c, recs)); continue
        r0 = recs[0]
        L += [f"### {c}: {r0['drones']} drones x {r0['missions_per_drone']} missions, {r0['distance_m'][0]:.0f} to {r0['distance_m'][1]:.0f} m"
              + (" (the tuning swarm)" if r0.get("tuning") else "") + f"; handed back: {'yes' if all(x['omni'].get('handed_back') for x in recs) else 'NO'}", "",
              "| Gauge | native (A) | omni (A) | A | B | C | Reading |", "|---|---:|---:|---:|---:|---:|---|"]
        for k, name, direction in gauges:
            v = verdict(recs, k, direction)
            if v == "no value":
                continue
            if direction != "shown" and not r0.get("tuning"):
                tally.setdefault(k, {}).setdefault(v, []).append(c)
            L.append(f"| {name} | {r0['native'][k]:.4g} | {r0['omni'][k]:.4g} | {pct(change(recs[0], k), k)} | {pct(change(recs[1], k), k)} | "
                     f"{pct(change(recs[2], k), k)} | {v} |")
        L.append("")
    L += ["## Across the untouched cells Omni moved", "", f"| Gauge | {ACROSS_HEAD} |", ACROSS_RULE]
    for k, name, direction in gauges:
        t = tally.get(k)
        if not t:
            continue
        L.append(f"| {name} | {across_cells(t, direction, k)} |")
    L += ["", "## Cells where the paired trial left the cruise native: nothing for Omni to move", "",
          f"In native mode, before the counted missions, one mission at the planner's cruise and one at {TRIAL_OVERRIDE} x showed a faster "
          "mission no cheaper on the simulator's own figures, or not inside the safe tracking error, so Omni left the cruise at the "
          "planner's and both arms are the same.", "",
          "| Cell | Energy a mission at the planner's cruise (J) | At the trial speed (J) | Reproduced over A, B, C |", "|---|---:|---:|---|"]
    for c, recs in idle:
        t0 = recs[0]["physics_trial"]; f, s = t0["planner_cruise"], [v for kk, v in t0.items() if kk.startswith("override_")][0]
        rep = all(reproduced(recs, k) for k, _, _ in gauges)
        L.append(f"| {c} | {f['energy_per_mission_j']:.1f} | {s['energy_per_mission_j']:.1f} | {'yes' if rep else 'no'} |")
    L += ["", "## Void cells", "", "| Cell | Why |", "|---|---|"]
    for c, e in void:
        L.append(f"| {c} | {e} |")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(with_own_runs(L))) + "\n")
    ng, nl, nv, nd = across_counts(tally, {k: d for k, _, d in gauges}.get)
    print(f"{out}: {len(cells) - len(idle) - len(void)} cells moved ({ng} gauge-rows GAIN in all three of our runs, {nl} LOSS, {nv} power given, {nd} where the runs differ, "
          f"the tuning cell shown and not counted), {len(idle)} nothing to move, {len(void)} void")
    return 0


if __name__ == "__main__":
    sys.exit(main())
