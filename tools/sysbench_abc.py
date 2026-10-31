#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C table for the sysbench on MySQL benchmark (docs/OMNI_V1.md's readings, docs/MYSQL_PREREGISTRATION.md): the untouched
workloads run three times as separate GitHub runs on the same frozen engine (tools/run_sysbench.py), each run holding three
paired repetitions of native and omni. Within a run the paired difference (omni minus native) over its repetitions gives a 95%
interval; across the three runs a gauge reads by the one key (tools/readings.py, the founder's order of 24 October 2026): a change of 0.5% or more, the mean of the three runs, reads GAIN, LOSS or power given by the gauge's aim, in all three of our runs when every run is clear of zero the same way and otherwise by the mean of our three runs with the count beyond the noise; under 0.5% STEADY, under the floor; runs that moved 0.5% or more in opposite ways disagree. Errors: any rise in any run reads **LOSS in at least one of our runs**. The knob's moves
are shown, never judged. The tuning workload is shown and not counted. Every row is reported, LOSS included; no energy is
claimed beyond the host's CPU seconds.
Usage: python tools/sysbench_abc.py A_DIR B_DIR C_DIR --out results/live/V3_SYSBENCH.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding sysbench-<workload>/.../<workload>.json"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.readings import with_own_runs, aim_of, Tally, STACK_RULE  # noqa: E402  (every table says whose runs these are)
from tools.run_sysbench import GAUGES, SAME_REL, paired, resizing  # noqa: E402
from tools.knob_verdict import summarize  # noqa: E402
from tools.ycsb_abc import cell, fmt, verdict  # noqa: E402  (the same three-run rule and cells as the other stores)


def load(d):
    """{workload: record} and the run id, from an archived run folder (the artifact may be nested one level)."""
    out = {}
    for f in sorted(Path(d).rglob("sysbench-*/*.json")):
        rec = json.loads(f.read_text())
        if "reps" in rec and rec.get("reps"):
            rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
            out[rec["workload"]] = rec
    if not out:
        raise SystemExit(f"{d}: no sysbench-<workload>/<workload>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def engine(run_dir):
    """(commit, engine version) of the run, from its own run file, checked against the fingerprints."""
    for f in Path(run_dir).rglob("sysbench-*/*.json"):
        e = json.loads(f.read_text()).get("engine") or {}
        sha = e.get("commit", "")
        if sha:
            r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT, capture_output=True, text=True)
            ver = r.stdout.strip().splitlines()[0] if r.stdout.strip() else "unknown"
            return sha[:12], ver
    return "", "unknown"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dirs", nargs=3)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in a.dirs]
    eng = [engine(d) for d in a.dirs]
    r00 = next(iter(runs[0][1].values()))
    L = ["# sysbench on MySQL, a database's " + ("buffer pool as shipped" if r00.get("native") == "shipped" else "operator-set buffer pool") + ": the A/B/C three-run table", "",
         (f"MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default ({r00['native_mb']} MB), is native (`docs/MYSQL_PREREGISTRATION.md`, amendment 5); omni is the compass law on the pool size through " if r00.get("native") == "shipped" else f"MySQL as Ubuntu ships it with the operator's InnoDB buffer pool ({r00['native_mb']} MB) is native; omni is the compass law on the pool size through ")
         + f"the server's own console inside [{r00['cover_mb'][0]}, {r00['cover_mb'][1]:,}] MB in chunks of {r00['chunk_mb']} MB, holding the server's own mean "
         f"statement latency at 40% of the {r00['line_stmt_ms']:g} ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads "
         "ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. " + STACK_RULE + " Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the "
         "host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning "
         "workload is shown and not counted. Every row is shown, LOSS included.", "",
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
        L += ["", f"## {wl}: sysbench {r0['script']}, {r0['statements']} statements a transaction, {r0['rate_tps']} a second offered; the transaction line "
              f"{r0['line_ms']:g} ms, {len(r0['reps'])} paired repetitions a run" + (" (the tuning workload, shown and not counted)" if tuning else ""), "",
              f"MySQL {r0.get('mysql_version', '?')}, {r0.get('sysbench_version', '?')}; {r0['threads']} client threads; {r0['tables']} tables of {r0['table_rows']:,} rows, "
              f"steps {r0['steps']} × {r0['step_s']} s; " + (f"native's pool as shipped {r0['native_mb']} MB" if r0.get('native') == "shipped" else f"the operator's pool {r0['native_mb']} MB") + f", the cover {r0['cover_mb'][0]} to {r0['cover_mb'][1]:,} MB.", "",
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
        arms = [x["omni"] for r in recs for x in r["reps"]]
        not_hb = [x for x in arms if not x.get("handed_back")]
        receipts = any("restore" in x for x in arms)
        in_flight = sum(1 for x in not_hb if resizing((x.get("restore") or {}).get("resize_in_flight_at_end", "")))
        if not not_hb:
            line = "The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes."
        else:
            line = (f"The buffer pool handed back to native's and read back at the end of every omni arm in every run: **NO** "
                    f"({len(not_hb)} of {len(arms)} omni arms not handed back"
                    + (f"; in {in_flight} of them the server was still carrying out a resize when the restore was issued" if receipts else "") + ").")
        L += ["", line]
        out.setdefault("handed_back", {})[wl] = {"omni_arms": len(arms), "not_handed_back": len(not_hb), "resize_in_flight": in_flight if receipts else None}
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
