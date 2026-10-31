#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C table for the YCSB on MongoDB benchmark (docs/OMNI_V1.md's readings, docs/YCSB_PREREGISTRATION.md): the untouched
workloads run three times as separate GitHub runs on the same frozen engine (tools/run_ycsb.py), each run holding three paired
repetitions of native and omni. Within a run the paired difference (omni minus native) over its repetitions gives a 95%
interval; across the three runs a gauge reads GAIN or LOSS in all three of our runs (by what it is for, never by its sign; a resource spent that rose reads power given) when all three move the same way with every
interval clear of zero, no difference beyond the noise when a run's interval includes zero (with the count of such runs), and
the runs disagree when runs clear of the noise point different ways. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. The
knob's moves are shown, never judged. The tuning workload is shown and not counted. Every row is reported, LOSS included; no
energy is claimed beyond the host's CPU seconds.
Usage: python tools/ycsb_abc.py A_DIR B_DIR C_DIR --out results/live/V3_YCSB.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding ycsb-<workload>/.../<workload>.json"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.readings import with_own_runs, stack_reading, aim_of, Tally  # noqa: E402  (every table says whose runs these are)
from tools.run_ycsb import GAUGES, OPTIONAL_GAUGES, SAME_REL, paired  # noqa: E402
from tools.knob_verdict import summarize  # noqa: E402


def load(d):
    """{workload: record} and the run id, from an archived run folder (the artifact may be nested one level)."""
    out = {}
    for f in sorted(Path(d).rglob("ycsb-*/*.json")):
        rec = json.loads(f.read_text())
        if "reps" in rec and rec.get("reps"):
            rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
            out[rec["workload"]] = rec
    if not out:
        raise SystemExit(f"{d}: no ycsb-<workload>/<workload>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def engine(run_dir):
    """(commit, engine version) of the run, from its own run file, checked against the fingerprints."""
    for f in Path(run_dir).rglob("ycsb-*/*.json"):
        e = json.loads(f.read_text()).get("engine") or {}
        sha = e.get("commit", "")
        if sha:
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
    L = ["# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table", "",
         (("MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the ") if all(rec.get("native") == "shipped" for _, recs in runs for rec in recs.values()) else "MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the ") + 
         "server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line"
         "(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache "
         "and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval "
         "within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) "
         "a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); "
         "clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is "
         "the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is "
         "claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.", "",
         "| Run | GitHub run | Commit | Engine | Workloads |", "|---|---|---|---|---:|"]
    off = []
    for tag, (run, recs), (sha, ver) in zip("ABC", runs, eng):
        if not ver.startswith("omni-v"):
            off.append(f"{tag} (run {run}: {ver})")
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {len(recs)} |")
    if len({r for r, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if len({v.split(" ")[0] for _, v in eng}) > 1:
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
        L += ["", f"## {wl}: YCSB {r0['ycsb_workload']}, {r0['base_records']:,} records × notch; line {r0['line_ms']:.0f} ms, {len(r0['reps'])} paired repetitions a run"
              + (" (the tuning workload, shown and not counted)" if tuning else ""), "",
              f"MongoDB {r0.get('mongodb_version', '?')}, YCSB {r0.get('ycsb_version', '?')}; {r0['rate_ops']:,} operations a second offered from {r0['threads']} threads; "
              f"steps {r0['steps']} × {r0['step_s']} s; " + (f"native's cache as shipped {r0['native_mb']} MB" if r0.get('native') == "shipped" else f"the operator's cache {r0['native_mb']} MB") + f", the cover {r0['cover_mb'][0]} to {r0['cover_mb'][1]} MB.", "",
              "| Gauge | native (A) | omni (A) | A | B | C | Reading |", "|---|---:|---:|---:|---:|---:|---|"]
        out["workloads"][wl] = {}
        for k, label, dr in GAUGES:
            rs = [r["paired"].get(k) for r in recs]
            if k in OPTIONAL_GAUGES and all(r is None for r in rs):
                continue                                       # a gauge the runs before 25 October did not record: no row, as before
            v = verdict(rs, dr, k)
            if not tuning:
                tally.add(v, dr, k)
            nat = fmt(rs[0]["native"]) if rs[0] else "n/a"; om = fmt(rs[0]["omni"]) if rs[0] else "n/a"
            L.append(f"| {label} | {nat} | {om} | " + " | ".join(cell(r, k) for r in rs) + f" | {v} |")
            out["workloads"][wl][k] = {"reading": v.strip("*"), "aim": aim_of(dr, k), "runs": [None if r is None else {"native": r["native"], "omni": r["omni"], "diff": r["diff"], "ci95": r["ci95"]} for r in rs]}
        hb = all(all(x["omni"].get("handed_back") for x in r["reps"]) for r in recs)
        L += ["", f"The cache size handed back to native's and read back at the end of every omni arm in every run: {'yes' if hb else '**NO**'}."]
        vr = {t: [x["omni"]["verdict"] for x in r["reps"] if x["omni"].get("verdict")] for t, r in zip("ABC", recs)}
        if any(vr.values()):                                   # the brain's own verdict on the knob, live in the omni arms (the amendment of 2026-10-09)
            objs = sorted({v["objective"] for vs in vr.values() for v in vs})
            L += ["", "The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: " + ", ".join(objs) + "): "
                  + "; ".join(f"run {t}: {summarize(vs)}" for t, vs in vr.items() if vs) + "."]
            out.setdefault("verdicts", {})[wl] = {t: [{k: v.get(k) for k in ("objective", "state", "dial", "spend_allowed_steps", "give_back_allowed_steps", "allowed_low", "allowed_high", "counts")} for v in vs] for t, vs in vr.items()}
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
