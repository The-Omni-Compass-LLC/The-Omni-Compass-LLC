#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The three-run table for CPU power (docs/CPU_POWER_PREREGISTRATION.md): three separate runs of tools/run_cpu_power.py
(A, B, C; on one machine, or three machines of one kind) read by the three-run rule, every row shown, LOSS included.

  python3 tools/cpu_power_abc.py results/live/raw/<A> results/live/raw/<B> results/live/raw/<C> --out results/live/V3_CPU_POWER.md
"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.readings import with_own_runs, stack_reading, aim_of, Tally, STACK_RULE  # noqa: E402  (every table says whose runs these are)
from tools.run_cpu_power import GAUGES, SAME_REL, paired  # noqa: E402
from tools.knob_verdict import summarize  # noqa: E402


def load(d):
    """{workload: record} and the run's name, from a run folder (the files may be nested one level)."""
    out = {}
    for f in sorted(Path(d).rglob("cpu-power-*/*.json")):
        rec = json.loads(f.read_text())
        if "reps" in rec and rec.get("reps"):
            rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
            out[rec["workload"]] = rec
    if not out:
        raise SystemExit(f"{d}: no cpu-power-<workload>/<workload>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def engine(run_dir):
    """(commit, engine version) of the run, from its own run file, checked against the fingerprints."""
    for f in Path(run_dir).rglob("cpu-power-*/*.json"):
        e = json.loads(f.read_text()).get("engine") or {}
        sha = e.get("commit", "")
        if sha and sha != "?":
            r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT, capture_output=True, text=True)
            ver = r.stdout.strip().splitlines()[0] if r.stdout.strip() else "unknown"
            return sha[:12], ver
    return "", "unknown"


def verdict(rs, direction, key=None):
    """The three-run reading of one gauge, by rule, from its three within-run paired results: GAIN, LOSS, power given,
    STEADY or the runs disagree, by what the gauge is for (tools/readings.py)."""
    return stack_reading(rs, direction, SAME_REL, key)


def cell(r, key):
    """One run in separate fields (the referee's work order of 25 October): native's value → Omni-Compass's, the raw change with its
    true sign and its 95% interval (tools/confirm_abc.py cell, one format for every table)."""
    if r is None:
        return "n/a"
    from tools.confirm_abc import cell as fields
    return fields(r)

def fmt(v):
    return f"{v:.3g}" if abs(v) < 10 else f"{v:,.1f}" if abs(v) < 1000 else f"{v:,.0f}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dirs", nargs=3)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in a.dirs]
    eng = [engine(d) for d in a.dirs]
    L = ["# CPU power, the Linux kernel's own frequency governor under the processor's meter: the A/B/C three-run table", "",
         "The machine as it runs is native: the kernel's frequency governor as shipped under the operator's ceiling, the top clock. Omni is "
         "the compass law on the ceiling through the kernel's own interface inside [half the top, the top], holding the service's own request "
         "latency at 40% of the 20 ms line, every notch down allowed only by a paired trial on the machine itself under the declared objective "
         "(`docs/CPU_POWER_PREREGISTRATION.md`). " + STACK_RULE + " Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Energy is the processor's own meter (RAPL, class P, "
         "the processor's calibrated counter); the whole machine at the wall where a plug was fitted. The tuning workload is shown and not "
         "counted. Every row is shown, LOSS included.", "",
         "| Run | Run folder | Commit | Engine | Machine | Workloads |", "|---|---|---|---|---|---:|"]
    off = []
    for tag, (run, recs), (sha, ver) in zip("ABC", runs, eng):
        if not ver.startswith("omni-v"):
            off.append(f"{tag} (run {run}: {ver})")
        m = next(iter(recs.values())).get("machine", {})
        if m.get("modelled"):
            off.append(f"{tag} ran on a modelled machine (tests only): not a result")
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {m.get('model', '?')}, {m.get('cpus', '?')} CPUs, {', '.join(m.get('governors', []))} | {len(recs)} |")
    if len({r for r, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if len({v.split(' ')[0] for _, v in eng}) > 1:
        off.append("A, B and C are not all on the same engine")
    if off:
        L += ["", "> **Warning:** " + "; ".join(off) + "."]
    wls = sorted(set().union(*[set(r) for _, r in runs]), key=lambda w: (w != "tuning", w))
    tally = Tally()
    out = {"runs": [{"tag": t, "run": r, "commit": s, "engine": v} for t, (r, _), (s, v) in zip("ABC", runs, eng)], "workloads": {}}
    for wl in wls:
        recs = [r.get(wl) for _, r in runs]
        if any(x is None for x in recs):
            L += ["", f"## {wl}", "", "> not in every run: " + ", ".join(t for t, x in zip("ABC", recs) if x is None) + " lack it."]
            continue
        r0 = recs[0]; tuning = r0.get("tuning", False)
        L += ["", f"## {wl}: steps {r0['steps']} × {r0['step_s']} s; line {r0['line_ms']:.0f} ms, {len(r0['reps'])} paired repetitions a run"
              + (" (the tuning workload, shown and not counted)" if tuning else ""), "",
              f"{r0['unit_rps']:.1f} requests a second a step; the work unit {r0['work_unit_passes']} passes = {r0['service_ms_at_top']:.2f} ms at the top "
              f"clock; the cover {r0['cover_khz'][0] / 1000:.0f} to {r0['cover_khz'][1] / 1000:.0f} MHz by {r0['notch_khz'] / 1000:.0f} MHz; the verdict's "
              f"objective {r0.get('objective', 'resource')}; wall plug {'fitted' if r0.get('wall_meter') else 'none'}.", "",
              "| Gauge | native (A) | omni (A) | A | B | C | Reading |", "|---|---:|---:|---:|---:|---:|---|"]
        out["workloads"][wl] = {}
        for k, label, dr in GAUGES:
            rs = [r["paired"].get(k) for r in recs]
            v = verdict(rs, dr, k)
            if not tuning:
                tally.add(v, dr, k)
            nat = fmt(rs[0]["native"]) if rs[0] else "n/a"; om = fmt(rs[0]["omni"]) if rs[0] else "n/a"
            L.append(f"| {label} | {nat} | {om} | " + " | ".join(cell(r, k) for r in rs) + f" | {v} |")
            out["workloads"][wl][k] = {"reading": v.strip("*"), "aim": aim_of(dr, k), "runs": [None if r is None else {"native": r["native"], "omni": r["omni"], "diff": r["diff"], "ci95": r["ci95"]} for r in rs]}
        hb = all(all(x["omni"].get("handed_back") for x in r["reps"]) for r in recs)
        L += ["", f"The ceiling handed back to the operator's and read back at the end of every omni arm in every run: {'yes' if hb else '**NO**'}."]
        vr = {t: [x["omni"]["verdict"] for x in r["reps"] if x["omni"].get("verdict")] for t, r in zip("ABC", recs)}
        if any(vr.values()):
            objs = sorted({v["objective"] for vs in vr.values() for v in vs})
            L += ["", "The brain's own verdict on the ceiling in the omni arms, one trial at a time on the machine itself (the objective: " + ", ".join(objs) + "): "
                  + "; ".join(f"run {t}: {summarize(vs)}" for t, vs in vr.items() if vs) + "."]
            out.setdefault("verdicts", {})[wl] = {t: [{k: v.get(k) for k in ("objective", "state", "give_back_allowed_steps", "allowed_low", "allowed_high", "counts")} for v in vs] for t, vs in vr.items()}
    missing = {t: [w for w in wls if w not in r] for t, (_, r) in zip("ABC", runs)}
    if any(missing.values()):                           # 21 October: a table written from runs that failed said nothing at its foot
        L += ["", "> **Warning:** a run lacks a workload: " + "; ".join(f"run {t} lacks {', '.join(ws)}" for t, ws in missing.items() if ws)
              + ". A workload is read only where every run holds it; a table whose runs hold none carries no result and is not read by "
              "the index or the benefit sheet until its runs land (`tools/omni_index.newest`)."]
    n_wl = sum(1 for w in wls if all(w in r for _, r in runs) and not any((r.get(w) or {}).get("tuning") for _, r in runs))
    L += ["", tally.sentence(n_wl, "untouched workloads")]
    Path(a.out).write_text("\n".join(_legal_stamp(with_own_runs(L))) + "\n")
    Path(a.out).with_suffix(".json").write_text(json.dumps(out, indent=1))
    print(f"{a.out}: {n_wl} untouched workloads; {tally.counts()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
