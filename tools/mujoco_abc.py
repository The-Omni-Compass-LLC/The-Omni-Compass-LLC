# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C table for the robot arms (docs/OMNI_V1.md, docs/ROBOTICS_PREREGISTRATION.md): each robot run three times as
separate GitHub runs on the same frozen engine (tools/run_mujoco.py). MuJoCo is deterministic, so the runs must give the
same numbers: a gauge reads GAIN or LOSS in all three of our runs when all three runs agree on the sign (judged by what the
gauge is for, never by its sign; energy, force and copper heating are resources spent, so a rise reads power given), STEADY
when the change is under one part in a billion (nine decimal places), and "the runs differ" when they do not reproduce. A robot whose paired
physics trial left the override native is listed as "nothing for Omni to move"; a robot whose own servo cannot do the task
is listed with the runner's reason. Every row is reported, LOSS included.
Usage: python tools/mujoco_abc.py A_DIR B_DIR C_DIR --out results/live/V1_MUJOCO.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding mujoco-<robot>/<robot>.json"""
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
from tools.run_mujoco import GAUGES

SAME_REL = 1e-9          # "the same" only to nine decimal places of the value (tools/readings.py EXACT_REL; the referee's work order of 25 October)
REPRO_REL = 1e-9


def load(d):
    out = {}
    for f in sorted(Path(d).glob("mujoco-*/*.json")):
        out[f.stem] = json.loads(f.read_text())
    if not out:
        raise SystemExit(f"{d}: no mujoco-<robot>/<robot>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def change(rec, k):
    n, o = (rec.get("native") or {}).get(k), (rec.get("omni") or {}).get(k)
    if n is None or o is None:
        return None
    return (o - n) if (k == "over_line_share" or n == 0) else (o - n) / abs(n)


def reproduced(recs, k):
    for arm in ("native", "omni"):
        v = [(r.get(arm) or {}).get(k) for r in recs]
        if any(x is None for x in v):
            return all(x is None for x in v)
        if not all(abs(x - v[0]) <= REPRO_REL * max(1.0, abs(v[0])) for x in v):
            return False
    return True


def verdict(recs, k, direction):
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
    return f"{c:+.3f}" if k == "over_line_share" else f"{100 * c:+.2f}%"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c"); ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = ["# Robot arms, MuJoCo Menagerie: the A/B/C three-run table (Omni v1)", "",
         "MuJoCo (Google DeepMind) integrates each arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the "
         "position servos it ships with as native. Omni sits on top of that servo on one knob, the speed override, inside the "
         "task's takt (`docs/ROBOTICS_PREREGISTRATION.md`). Energy is a declared model from MuJoCo's own torques and velocities, "
         "the same in both arms, with the standing draw charged for the whole takt. Three separate GitHub runs on the same frozen "
         "engine: MuJoCo is deterministic, so " + DETERMINISTIC_RULE + ", **STEADY, the same** under one part in a billion (nine decimal places), and **the runs differ** when they do not reproduce. A robot whose "
         "paired physics trial found a slower cycle no cheaper is listed as nothing for Omni to move. Every row is shown, LOSS "
         "included.", "",
         "| Run | GitHub run | Commit | Engine | Robots in the run |", "|---|---|---|---|---:|"]
    off = []; seen = []
    for tag, (run, recs) in zip("ABC", runs):
        sha, ver = engine(run)
        seen.append(ver.split(" ")[0])
        if not ver.startswith("omni-v"):                     # a fingerprinted engine (docs/OMNI_V2.md; v1 runs keep reading as v1)
            off.append(f"{tag} (run {run}: {ver})")
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {len(recs)} |")
    # the title names the engine the three runs carry (one engine, or it says they differ): never read across versions
    label = f"Omni {seen[0][5:]}" if len(set(seen)) == 1 and seen[0].startswith("omni-v") else "the runs' engines differ"
    L[0] = L[0].replace("(Omni v1)", f"({label})")
    if len({r for r, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if off:
        L[2:2] = [f"**Not one engine's three runs: {'; '.join(off)}.**", ""]
    robots = sorted(set().union(*(set(r) for _, r in runs)))
    tally = {}; idle = []; broken = []
    L += ["", "## Robots where Omni moved the override", ""]
    for rb in robots:
        recs = [r.get(rb) for _, r in runs]
        if any(x is None for x in recs) or any("error" in x for x in recs):
            errs = {str(x.get("error") if x else "missing from a run")[:160] for x in recs}
            broken.append((rb, "; ".join(sorted(errs)))); continue
        if not all(x.get("omni_moves") for x in recs):
            idle.append((rb, recs)); continue
        r0 = recs[0]
        L += [f"### {rb}: {r0['joints']} joints, planned {r0['planned_s']:.0f} s, takt {r0['line_s']:.0f} s, {r0['native']['cycles']} cycles per arm; "
              f"handed back every cycle: {'yes' if all(x['omni'].get('handed_back') for x in recs) else 'NO'}", "",
              "| Gauge | native (A) | omni (A) | A | B | C | Reading |", "|---|---:|---:|---:|---:|---:|---|"]
        for k, name, direction in GAUGES:
            v = verdict(recs, k, direction)
            if v == "no value":
                continue
            if direction != "shown":
                tally.setdefault(k, {}).setdefault(v, []).append(rb)
            L.append(f"| {name} | {r0['native'][k]:.4g} | {r0['omni'][k]:.4g} | {pct(change(recs[0], k), k)} | {pct(change(recs[1], k), k)} | "
                     f"{pct(change(recs[2], k), k)} | {v} |")
        L.append("")
    L += ["## Across the robots Omni moved", "", f"| Gauge | {ACROSS_HEAD} |", ACROSS_RULE]
    for k, name, direction in GAUGES:
        t = tally.get(k)
        if not t:
            continue
        L.append(f"| {name} | {across_cells(t, direction, k)} |")
    L += ["", "## Robots where the paired trial left the override native: nothing for Omni to move", "",
          "In native mode, before the counted cycles, one cycle at full speed and one at override 0.8 showed a slower cycle no "
          "cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so Omni left the override at 1.0 "
          "and both arms are the same. Reproduced over A, B, C is whether the three runs agree on every gauge.", "",
          "| Robot | Full-speed cycle (J, motion) | Override 0.8 cycle (J, motion) | Reproduced over A, B, C |", "|---|---:|---:|---|"]
    for rb, recs in idle:
        t0 = recs[0]["physics_trial"]; f, s = t0["full_speed"], [v for kk, v in t0.items() if kk.startswith("override_")][0]
        rep = all(reproduced(recs, k) for k, _, _ in GAUGES)
        L.append(f"| {rb} | {f['mechanical_j'] + f['copper_j']:.1f} | {s['mechanical_j'] + s['copper_j']:.1f} | {'yes' if rep else 'no'} |")
    L += ["", "## Robots the task could not be run on", "", "| Robot | The runner's reason |", "|---|---|"]
    for rb, e in broken:
        L.append(f"| {rb} | `{e}` |")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(with_own_runs(L))) + "\n")
    ng, nl, nv, nd = across_counts(tally, {k: d for k, _, d in GAUGES}.get)
    print(f"{out}: {len(robots) - len(idle) - len(broken)} robots moved ({ng} gauge-rows GAIN in all three of our runs, {nl} LOSS, {nv} power given, {nd} where the runs differ), "
          f"{len(idle)} nothing to move, {len(broken)} could not run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
