# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Checks that the live benchmark engine page's three records are the repository's own runs, not a drawing of them.

  harness     docs/engine/export_harness_trace.py against realms/harness.py itself: the organism (run_organism_arm,
              native and the max, the climb) and every muscle alone (run_muscle_arm, the line), decisions over the line
              and work, plant by plant
  controller  docs/engine/export_controller_trace.py against tools/model_gate.py's own worker (the cloud's setting: the
              machine-hours, the verdict's steps allowed and refused, the machines parked) and against
              pilot/selfpilot.py run_day (the machines and the pods waiting, tick by tick, and the writes)
  stacks      docs/engine/export_scenarios.py against realms/gpu_card.run (the GPU card, every arm and both kinds of work:
              the run's own result, and the energy and requests of every second adding up to it) and against
              tools/model_gate.py worker_convey (the Linux host: its own result line, the requests and the host's busy share)

pilot/selfpilot.py's omni day builds the controller's own kubectl reader, which starts a kubectl proxy; where no kubectl
is installed the proxy is stubbed for that one call (the simulated cluster answers every read either way).
Usage: python3 docs/engine/check_records.py [--seed 3000 3001 3002]. Exit 0 when every comparison is identical (every seed
named; by default the three seeds of runs A, B and C).
"""
from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(HERE))

import export_controller_trace as XC                  # noqa: E402
import export_harness_trace as XH                     # noqa: E402
import export_scenarios as XS                         # noqa: E402
from realms import harness as H                       # noqa: E402


def harness(seed):
    rs, bad = XH.rows(), []
    for arm, harm in (("native", "native"), ("omni", "v5")):
        mine, ref = XH.run(rs, seed, arm), H.run_organism_arm(rs, seed, harm, load="climb")
        if sum(sum(x) for x in mine["over"]) != sum(p["viol"] for p in ref["plants"]):
            bad.append(f"organism {arm}: decisions over the line")
        for i, p in enumerate(ref["plants"]):
            if abs(sum(mine["work"][k][i] for k in range(len(mine["work"]))) - p["work"]) > 1e-9 * max(1.0, abs(p["work"])):
                bad.append(f"organism {arm}: work of {rs[i]['muscle']}")
    for r in rs:
        for arm, harm in (("native", "native"), ("omni", "v5")):
            rec, _, _ = XH.run_alone(r, seed, arm)
            ref = H.run_muscle_arm(r, seed, harm, "line")
            if sum(rec["over"]) != ref["viol"] or abs(sum(rec["work"]) - ref["work"]) > 1e-9 * max(1.0, abs(ref["work"])):
                bad.append(f"alone {arm}: {r['muscle']}")
    return bad


def controller(seed):
    bad = []
    tg = ROOT / "tools" / "model_gate.py"
    for arm in ("native", "omni"):
        d = tempfile.mkdtemp()
        out = subprocess.run([sys.executable, str(tg), "--worker", arm, "--seed", str(seed), "--days", str(XC.DAYS), "--period", "60",
                              "--dir", d], capture_output=True, text=True, cwd=ROOT,
                             env=dict(__import__("os").environ, PYTHONPATH=str(ROOT)))
        if not out.stdout.strip():
            bad.append(f"cloud {arm}: tools/model_gate.py gave no result: {out.stderr[-300:]}"); continue
        res = json.loads(out.stdout.strip().splitlines()[-1])
        ticks, dec = XC.run("cloud", seed, arm)
        mh = sum(t["nodes"] + t["boot"] + t["parked"] for t in ticks) * 15 / 3600
        if abs(mh - res["machine_hours"]) > 1e-9:
            bad.append(f"cloud {arm}: machine-hours {mh} against {res['machine_hours']}")
        if arm == "omni":
            got = {"steps_allowed": sum(1 for x in dec if x.get("verdict") == "step allowed"),
                   "steps_refused": sum(1 for x in dec if str(x.get("verdict", "")).startswith("step refused"))}
            for k, v in got.items():
                if v != res[k]:
                    bad.append(f"cloud omni: {k} {v} against {res[k]}")
    from pilot.selfpilot import run_day
    import omni_controller.controller as C
    for omni in (False, True):
        d = Path(tempfile.mkdtemp())
        if shutil.which("kubectl"):
            path = run_day(seed, omni, d, XC.DAYS)
        else:
            with mock.patch.object(C.Kube, "_start_proxy", lambda self: None):
                path = run_day(seed, omni, d, XC.DAYS)
        rows = list(csv.DictReader(open(path)))
        ticks, dec = XC.run("selfpilot", seed, "omni" if omni else "native")
        if [int(r["nodes_ready"]) for r in rows] != [t["nodes"] for t in ticks]:
            bad.append(f"selfpilot {'omni' if omni else 'native'}: machines")
        if [int(r["pods_pending"]) for r in rows] != [t["pending"] for t in ticks]:
            bad.append(f"selfpilot {'omni' if omni else 'native'}: pods waiting")
        if omni and sum(1 for l in open(d / "audit.jsonl") if '"write"' in l) != sum(x["writes"] for x in dec):
            bad.append("selfpilot omni: writes")
    return bad


def stacks(seed):
    """Section 3: the GPU card's record against realms/gpu_card.run untouched (seed 5100 for 3000, 5101 for 3001, ...),
    and the Linux host's against tools/model_gate.py worker_convey untouched."""
    import contextlib
    import io
    import realms.gpu_card as G
    from tools import model_gate as TG
    bad, gs = [], 5100 + seed - 3000
    for memb in (0.85, 0.0):
        for arm in ("native", "omni", "cap", "cap_omni"):
            rec, ref = XS.gpu_run(gs, arm, memb), G.run(gs, arm, 600.0, memb)
            if any(rec["summary"][k] != ref[k] for k in rec["summary"]):
                bad.append(f"gpu {arm} memb {memb}: the recorded run differs from realms/gpu_card.run")
            n = len(rec["power"])                              # the record keeps W to 0.01 and requests to 0.001 each second
            if abs(sum(rec["power"]) - ref["energy_j"]) > 0.005 * n + 1e-6 * ref["energy_j"] or abs(sum(rec["served"]) - ref["served"]) > 0.0005 * n:
                bad.append(f"gpu {arm} memb {memb}: energy or requests per second do not add up to the run's")
    for arm in ("native", "omni"):
        rec = XS.linux_run(seed, arm)
        buf = io.StringIO()
        with tempfile.TemporaryDirectory() as td, contextlib.redirect_stdout(buf):
            TG.worker_convey(arm, seed, td)
        ref = json.loads(buf.getvalue().strip().splitlines()[-1])
        got = ref.pop("engine_tree", None)          # the checkout the engine came from: this one (a path, never part of the record)
        if got is not None and Path(got).resolve() != ROOT.resolve():
            bad.append(f"linux {arm}: the engine was imported from {got}, not from this checkout")
        if rec["summary"] != ref:
            bad.append(f"linux {arm}: the recorded run differs from tools/model_gate.py worker_convey")
        if abs(sum(rec["lam"]) - ref["requests_served"]) > 0.0005 * len(rec["lam"]):            # kept to 0.001 each second
            bad.append(f"linux {arm}: requests a second do not add up to the run's")
        if abs(sum(rec["busy"]) / len(rec["busy"]) - ref["host_busy"]) > 1e-3:
            bad.append(f"linux {arm}: host busy")
    return bad


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--seed", type=int, nargs="+", default=[3000, 3001, 3002]); a = ap.parse_args()
    bad = []
    for sd in a.seed:
        b = [f"seed {sd}: {x}" for x in harness(sd) + controller(sd) + stacks(sd)]
        print("\n".join(b) if b else f"seed {sd}: every record identical to the repository's own run")
        bad += b
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
