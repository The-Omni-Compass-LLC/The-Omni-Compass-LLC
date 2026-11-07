# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""How steadily the governor steered (tools/steering.py): each omni arm's gauges per hour of its own audit, a run's arms
averaged, only the omni arms read."""
import json, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.steering as ST


def audit(path, hpa_values, writes=0, step=60.0):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for i, v in enumerate(hpa_values):
        t = i * step
        lines.append({"time": t, "decision": {"nodes_observed": 6, "nodes_recommended": 6, "hpa_target_recommended": v,
                                              "power_cap": 1.0, "compass_law": {"position": 0.5, "force": 0.0}}})
        lines.append({"time": t + 1, "decision_ms": 500.0})
    for j in range(writes):
        lines.append({"time": j * step + 2, "write": ["kubectl"], "why": "convey: a pod's limit", "dry_run": False})
    path.write_text("\n".join(json.dumps(x) for x in lines) + "\n")


class Steering(unittest.TestCase):
    def test_an_arm_per_hour_of_its_own_audit(self):
        d = Path(tempfile.mkdtemp())
        audit(d / "bench-compass-1" / "audit.jsonl", [0.5, 0.6, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6], writes=5)
        g = ST.arm(d / "bench-compass-1" / "audit.jsonl")
        hours = (10 * 60 + 1) / 3600.0                           # from the first record to the last decision's time
        self.assertAlmostEqual(g["decisions_h"], 11 / hours)
        self.assertAlmostEqual(g["writes_h"], 5 / hours)
        self.assertAlmostEqual(g["moves_h_hpa_target"], 3 / hours)
        self.assertAlmostEqual(g["reversals_h_hpa_target"], 2 / hours)
        self.assertAlmostEqual(g["decision_s_mean"], 0.5)

    def test_a_run_averages_its_omni_arms_and_never_reads_native(self):
        d = Path(tempfile.mkdtemp())
        audit(d / "paired-1" / "bench-compass-1" / "audit.jsonl", [0.5] * 11, writes=0)
        audit(d / "paired-2" / "bench-compass-2" / "audit.jsonl", [0.5] * 11, writes=10)
        audit(d / "paired-1" / "bench-native-1" / "audit.jsonl", [0.5] * 11, writes=1000)
        r = ST.run(d)
        self.assertEqual(r["repetitions"], 2)
        one = ST.arm(d / "paired-2" / "bench-compass-2" / "audit.jsonl")["writes_h"]
        self.assertAlmostEqual(r["writes_h"], one / 2)

    def test_a_run_with_no_omni_audit_reads_nothing(self):
        self.assertIsNone(ST.run(Path(tempfile.mkdtemp())))


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
