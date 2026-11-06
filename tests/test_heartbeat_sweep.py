# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The heartbeat sweep's record is the tool's own reading of its runs (the founder's order of 22 October: every beat from 5 to
120 s on the monitor, each with what it does against native and what it costs): the table and its JSON are written again from
the committed runs byte for byte, every governed row names the engine it ran on, and a rescue is counted only where the fast
check wrote a pool command for a pod already waiting."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import heartbeat_sweep as HS  # noqa: E402

RUNS = ROOT / "results" / "model_gate" / "HEARTBEAT_SWEEP_RUNS.jsonl"
MD = ROOT / "results" / "model_gate" / "HEARTBEAT_SWEEP.md"


class HeartbeatSweep(unittest.TestCase):
    def test_the_record_is_the_tool_reading_its_runs(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "HEARTBEAT_SWEEP.md"
            HS.table(str(RUNS), str(out))
            self.assertEqual(out.read_text(encoding="utf-8"), MD.read_text(encoding="utf-8"))
            self.assertEqual(out.with_suffix(".json").read_text(encoding="utf-8"),
                             MD.with_suffix(".json").read_text(encoding="utf-8"))

    def test_every_governed_row_names_its_engine(self):
        rows = [json.loads(line) for line in RUNS.read_text(encoding="utf-8").splitlines()]
        engines = {r["engine"] for r in rows}
        self.assertEqual(engines, {"native", "omni-v16", "omni-v15"})
        for r in rows:
            self.assertEqual(r["arm"] == "native", r["engine"] == "native", r)
            if r["engine"] != "native":
                self.assertIn("rescues", r)
        seen = {(r["setting"], r["engine"], r["period"], r["seed"]) for r in rows}
        self.assertEqual(len(seen), len(rows), "a run counted twice")

    def test_a_rescue_is_a_pool_command_for_a_waiting_pod(self):
        recs = [{"decision": {"why": "scheduling floor (pending pods)"}},                       # a decision record, no write
                {"write": ["SIMSCALE", "9"], "why": "node pool size"},                           # the decision's own command
                {"write": ["SIMSCALE", "10"], "why": "scheduling floor (pending pods)"},         # a rescue
                {"held": "machines", "why": "scheduling floor (pending pods): left native"},    # held, nothing written
                {"refused": {"nodes": 11}, "why": "scheduling floor (pending pods)"}]            # the pool's refusal
        with tempfile.TemporaryDirectory() as td:
            a = Path(td) / "audit.jsonl"
            a.write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
            self.assertEqual(HS.rescues(a), 1)


if __name__ == "__main__":
    unittest.main()
