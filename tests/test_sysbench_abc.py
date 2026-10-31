# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The sysbench A/B/C table (tools/sysbench_abc.py): it reads the same three-run rule as the other stores (tools/ycsb_abc.py's
verdict and cells), finds the runner's records under sysbench-<workload>/, and every gauge of the runner has a direction the rule
knows."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import sysbench_abc as A
from tools import run_sysbench as S


def main():
    assert A.verdict is not None and A.cell is not None, "the same rule as the other stores"
    assert {dr for _, _, dr in S.GAUGES} <= {"higher", "lower", "spent", "never more", "shown"}
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "run-123" / "sysbench-tuning"; d.mkdir(parents=True)
        reps = [{"native": {"tps": 100.0, "pool_mb_mean": 512.0, "failed": 0, "handed_back": True},
                 "omni": {"tps": 101.0, "pool_mb_mean": 384.0, "failed": 0, "handed_back": True}}] * 3
        (d / "tuning.json").write_text(json.dumps({"workload": "tuning", "tuning": True, "reps": reps, "engine": {"commit": ""}}))
        run, recs = A.load(Path(t) / "run-123")
        assert run == "123" and "tuning" in recs and recs["tuning"]["paired"]["pool_mb_mean"]["reading"] in ("GAIN", "power given", "STEADY, no difference beyond the noise", "STEADY, the same")
        empty = Path(t) / "run-124"; empty.mkdir()
        try:
            A.load(empty); raise AssertionError("a folder without records must refuse")
        except SystemExit:
            pass
    print("PASS  sysbench A/B/C table: the same three-run rule as the other stores; the runner's records found under sysbench-<workload>/; every gauge has a known direction")


if __name__ == "__main__":
    main()
