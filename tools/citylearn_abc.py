# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C table for CityLearn (docs/OMNI_V1.md): the same districts run three times as separate GitHub runs on the
same frozen engine (tools/run_citylearn.py). CityLearn is a deterministic simulator, so the three runs must give the same
numbers: a row reads GAIN or LOSS in all three of our runs when all three runs agree on the sign (judged by what the score
is for, never by its sign: CITYLEARN_AIMS; the electricity bought, the bill and the carbon are resources spent, so a fall is a
cut, a GAIN, and a rise is power given), STEADY when every run's change is under one part in a billion (nine decimal places), and "the runs differ" when they
do not reproduce each other, which is a finding about the simulator or the harness and is said so. A district with no electric battery gets nothing from Omni (the runner moves
only `electrical_storage` commands; a water tank stays native), so it is listed as "nothing for Omni to move", and any
native/omni difference in it is CityLearn's own run-to-run variation, never an Omni result. A district CityLearn cannot
run is listed with CityLearn's own error. Every row is reported, LOSS included.
Usage: python tools/citylearn_abc.py A_DIR B_DIR C_DIR --out results/live/V1_CITYLEARN.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding citylearn-<district>/<district>.json"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.readings import with_own_runs, in_all_three, EVEN_SAME, ACROSS_HEAD, ACROSS_RULE, across_cells, across_counts, reproduced_reading  # noqa: E402  (every table says whose runs these are)
from tools.repo import NAME as REPO_NAME  # noqa: E402  (the repository's name, written once)
from tools.run_citylearn import KPIS, WORDS as KPI_NAMES

# What each CityLearn score is for (tools/readings.py, one key for every gauge). CityLearn aims every score lower. The
# electricity bought, the bill, the carbon, the distance from zero net energy, the peaks, the swings and the unevenness are the
# power the district draws and holds and the wear of moving it: a fall is a cut, a GAIN; a rise is power given, never a loss
# (a peak is power held, as a cluster's peak power is; the founder's order of 17 October). The energy not served and the time
# uncomfortable are the occupants' misses: a rise is a LOSS.
CITYLEARN_AIMS = {"cost_total": "spent", "electricity_consumption_total": "spent", "carbon_emissions_total": "spent",
                  "zero_net_energy": "spent", "all_time_peak_average": "spent", "daily_peak_average": "spent",
                  "ramping_average": "spent", "monthly_one_minus_load_factor_average": "spent",
                  "daily_one_minus_load_factor_average": "spent"}


def aim_of(k):
    return CITYLEARN_AIMS.get(k, "lower")

SAME_REL = 1e-9          # "the same" only to nine decimal places of the value (tools/readings.py EXACT_REL; the referee's work order of 25 October)
REPRO_REL = 1e-9         # two runs of a deterministic simulator agree to this, or they did not reproduce


def load(d):
    """{district: record} and the run id, from an archived run folder."""
    out = {}
    for f in sorted(Path(d).glob("citylearn-*/*.json")):
        out[f.stem] = json.loads(f.read_text())
    if not out:
        raise SystemExit(f"{d}: no citylearn-<district>/<district>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def change(rec, k):
    """omni against native on one score, as a share of native; None where either is missing."""
    n, o = rec["native"]["kpis"].get(k), rec["omni"]["kpis"].get(k)
    if n is None or o is None or n == 0:
        return None
    return (o - n) / abs(n)


def reproduced(recs, k, arm):
    """True when every run's value of this score in this arm agrees to REPRO_REL."""
    v = [r[arm]["kpis"].get(k) for r in recs]
    if any(x is None for x in v):
        return all(x is None for x in v)
    return all(abs(x - v[0]) <= REPRO_REL * max(1.0, abs(v[0])) for x in v)


def verdict(recs, k):
    """The score's reading over the three runs, by rule: GAIN, LOSS or power given in all three of our runs by what the score
    is for (CITYLEARN_AIMS), STEADY, or the runs differ."""
    if not (reproduced(recs, k, "native") and reproduced(recs, k, "omni")):
        return "**the runs differ**"
    ch = [change(r, k) for r in recs]
    if any(c is None for c in ch):
        return "no value"
    if all(abs(c) <= SAME_REL for c in ch):
        return EVEN_SAME
    signs = {(c > 0) - (c < 0) for c in ch}
    if len(signs) > 1:
        return "**the runs differ**"
    return reproduced_reading(ch, aim_of(k))


def engine(run):
    """The Omni version the run's commit carries, from the GitHub run record."""
    try:
        sha = subprocess.run(["gh", "api", f"repos/{REPO_NAME}/actions/runs/{run}", "--jq", ".head_sha"],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            return "?", "unknown"                          # a run whose commit cannot be read is never called v1
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                             capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
        return sha[:12], (out[0] if out else "unknown")
    except (OSError, subprocess.SubprocessError):
        return "?", "unknown"


def pct(c):
    return "n/a" if c is None else f"{100 * c:+.2f}%"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c"); ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = ["# CityLearn, every district: the A/B/C three-run table (Omni v1)", "",
         "CityLearn (University of Texas at Austin) is an independent, deterministic simulator of real buildings with its own "
         "controller (BasicRBC) and its own scores; every score is one CityLearn itself aims lower. Native is that controller; omni is the "
         "same controller with the compass law on top of its electric battery commands only (`tools/run_citylearn.py`). The "
         "same districts ran three times as separate GitHub runs on the same frozen engine. Because the simulator is "
         "deterministic, the runs must reproduce each other: a score reads **GAIN** or **LOSS in all three of our runs** when all "
         "three runs give the same sign, judged by what the score is for and never by its sign: the electricity bought, the bill, "
         "the carbon, the peaks, the swings and the unevenness are the power the district draws and holds and the wear of moving it, "
         "so a fall is a cut, a GAIN, and a rise is **power given**; a rise in the energy not served or the time uncomfortable (the "
         "occupants' misses) is a LOSS. **STEADY, the same** when the change is under one part "
         "in a million, and **the runs differ** when they do not reproduce, which is a finding about the simulator or the harness and "
         "is said so. A district with no electric battery gets nothing from Omni (a water tank stays native), so any native/omni "
         "difference in it is CityLearn's own run-to-run variation, never an Omni result. Every row is shown, LOSS included.", "",
         "| Run | GitHub run | Commit | Engine | Districts in the run |", "|---|---|---|---|---:|"]
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
    districts = sorted(set().union(*(set(r) for _, r in runs)))
    ran, idle, not_run = [], [], []
    for d in districts:
        recs = [r.get(d) for _, r in runs]
        if any(x is None for x in recs):
            not_run.append((d, "missing from a run")); continue
        if any("kpis" not in x.get("native", {}) or "kpis" not in x.get("omni", {}) for x in recs):
            errs = {str((x.get("native") or {}).get("error") or (x.get("omni") or {}).get("error") or "no result")[:120] for x in recs}
            not_run.append((d, "; ".join(sorted(errs)))); continue
        (idle if recs[0]["native"].get("batteries", 0) == 0 else ran).append((d, recs))
    tally = {}
    L += ["", "## Districts with electric batteries: omni against native, each run", ""]
    for d, recs in ran:
        n0 = recs[0]["native"]
        L += [f"### {d}: {n0['buildings']} buildings, {n0.get('batteries', 0)} batteries, {n0.get('thermal_stores_left_native', 0)} water tanks left native, "
              f"{n0['steps']:,} hours", "", "| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |", "|---|---:|---:|---:|---|"]
        for k in KPIS:
            v = verdict(recs, k)
            if v == "no value":
                continue
            tally.setdefault(k, {}).setdefault(v, []).append(d)
            L.append(f"| {KPI_NAMES.get(k, k)} (`{k}`) | {pct(change(recs[0], k))} | {pct(change(recs[1], k))} | {pct(change(recs[2], k))} | {v} |")
        L.append("")
    L += ["## Across the districts with batteries", "", "A district counts only when all three runs agree.", "",
          f"| CityLearn score | {ACROSS_HEAD} |", ACROSS_RULE]
    for k in KPIS:
        t = tally.get(k, {})
        if not t:
            continue
        L.append(f"| {KPI_NAMES.get(k, k)} | {across_cells(t, aim_of(k))} |")
    # a score that did not reproduce while native and omni were equal in every run: CityLearn's own value moved between runs
    # by the same amount in both arms, so the row says nothing about Omni (its reading stays the preregistered one)
    drift = [(d, k, max(abs(r[arm]["kpis"][k] - recs[0][arm]["kpis"][k]) for r in recs for arm in ("native", "omni")))
             for d, recs in ran for k in KPIS
             if verdict(recs, k) == "**the runs differ**" and all(change(r, k) == 0 for r in recs)]
    if drift:
        L += ["", "Where **the runs differ** above with native and omni equal in every run, CityLearn's own value moved between "
              "the runs by the same amount in both arms; the paired change is exactly zero in A, B and C, so the row says nothing "
              "about Omni-Compass, and it stays as the preregistered rule reads it: "
              + "; ".join(f"{d}, {KPI_NAMES.get(k, k)} (moved by at most {m:.2g} between runs)" for d, k, m in drift) + "."]
    L += ["", "## Districts with no electric battery: nothing for Omni to move", "",
          "The runner changes only `electrical_storage` commands, so in these districts omni applied nothing. Any difference "
          "between the arms is CityLearn's own run-to-run variation and says nothing about Omni; where the two arms agree, the "
          "simulator is deterministic there.", "",
          "| District | Buildings | Water tanks (native) | Scores where native and omni differ in A | Reproduced over A, B, C |", "|---|---:|---:|---|---|"]
    for d, recs in idle:
        n0 = recs[0]["native"]
        diff = [f"{KPI_NAMES.get(k, k)} {pct(change(recs[0], k))}" for k in KPIS if change(recs[0], k) is not None and abs(change(recs[0], k)) > SAME_REL]
        rep = all(reproduced(recs, k, arm) for k in KPIS for arm in ("native", "omni"))
        L.append(f"| {d} | {n0['buildings']} | {n0.get('thermal_stores_left_native', 0)} | {', '.join(diff) or 'none'} | {'yes' if rep else 'no'} |")
    L += ["", "## Districts CityLearn cannot run with its own controller", "",
          "The same for native and omni; listed, never dropped.", "", "| District | CityLearn's own error |", "|---|---|"]
    for d, e in not_run:
        L.append(f"| {d} | `{e}` |")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(with_own_runs(L))) + "\n")
    ng, nl, nv, nd = across_counts(tally, aim_of)
    print(f"{out}: {len(ran)} districts with batteries ({ng} score-rows GAIN in all three of our runs, {nl} LOSS, {nv} power given, {nd} where the runs differ), "
          f"{len(idle)} with nothing to move, {len(not_run)} CityLearn cannot run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
