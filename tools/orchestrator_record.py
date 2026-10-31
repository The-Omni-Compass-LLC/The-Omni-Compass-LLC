#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""One showing of Omni direct's three arms, as a record the live benchmark engine page replays (docs/engine/build_live_engine.py).

  python3 tools/orchestrator_record.py <showing folder> results/orchestrator/<NAME>.json --commit <sha> [--where <words>]

The showing folder is what tools/orchestrator_show.py wrote (summary.json and one folder per arm). The record keeps, for each arm
(native, Omni on native, Omni direct), the per-step work, 95th percentile, machines and units read from the arm's own files by
the showing's own functions, the arm's summary, every pair's reading by the one key, the batch job and the drills, and the commit
and engine it ran on. Nothing is computed here that the showing did not compute; the record only gathers it.
"""
from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

ARMS = (("yardstick", "native"), ("omni_native", "Omni on native"), ("omni", "Omni direct"))


def build(folder: Path, commit: str, where: str) -> dict:
    from tools import orchestrator_show as S
    d = json.loads((folder / "summary.json").read_text())
    arms = {}
    meta0 = None
    for key, label in ARMS:
        if key not in d["summary"]:
            continue
        meta = json.loads((folder / key / "meta.json").read_text())
        spec = json.loads((folder / key / "spec.json").read_text())
        meta0 = meta0 or (meta, spec)
        ps = S.per_step(folder / key, meta)
        arms[key] = {"label": label, "brain": meta.get("brain", key), "room_rule": meta.get("room_rule"),
                     "summary": {k: (round(v, 3) if isinstance(v, float) else v) for k, v in d["summary"][key].items()},
                     "per_step": {g: [round(x, 2) for x in xs] for g, xs in ps.items()}}
    meta, spec = meta0
    svc = spec["services"][0]
    readings = []
    for name, r in d["readings"].items():
        pair, gauge = name.split(": ")
        readings.append({"pair": pair, "gauge": gauge, "word": r["word"], "rel": round(r["rel"], 4),
                         "mean": round(r["mean"], 3), "lo": round(r["lo"], 3), "hi": round(r["hi"], 3)})
    engine = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", commit], cwd=ROOT,
                            capture_output=True, text=True).stdout.strip()
    return {"what": "Omni direct's three arms on one host: native (Kubernetes' published autoscaling rule, written by us), "
                    "Omni on native, Omni direct", "class": "L", "runs": 1, "where": where,
            "commit": commit, "engine": engine, "written": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "steps": meta["steps"], "step_s": meta["step_s"], "line_ms": svc["line_ms"], "units_min": svc["min"],
            "units_max": svc["max"], "machines": len(spec["machines"]), "machine_cpu_m": spec["machines"][0]["cpu_m"],
            "unit_req_m": svc["req_m"], "arms": arms, "readings": readings,
            "batch": d["summary"].get("batch"), "drills": d["summary"].get("drills")}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("folder")
    ap.add_argument("out")
    ap.add_argument("--commit", required=True, help="the commit the showing ran on")
    ap.add_argument("--where", default="one host, four processors, the showing's quick form")
    a = ap.parse_args(argv)
    rec = build(Path(a.folder), a.commit, a.where)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
    print(f"{a.out}: {len(rec['arms'])} arms, {len(rec['readings'])} readings, {rec['engine']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
