# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Negative controls for the paired SLO-goodput comparison."""
import unittest
from tools.paired_slo_goodput import evaluate


def record(completed=100, failed=0, p95_ms=100, energy_j=1000, cost_usd=10):
    return dict(workload_id="trace-A", hardware_id="GPU-A", offered_requests=110,
                completed=completed, failed=failed, p95_ms=p95_ms,
                energy_j=energy_j, cost_usd=cost_usd)


class PairedSLOTests(unittest.TestCase):
    def test_benefit_with_healthy_service(self):
        result = evaluate({"native": [record()], "omni": [record(energy_j=900, cost_usd=9)]})
        self.assertEqual(result["status"], "ADMISSIBLE")
        self.assertGreater(result["pairs"][0]["goodput_per_joule_delta_pct"], 0)

    def test_lower_energy_does_not_hide_latency_regression(self):
        result = evaluate({"native": [record()], "omni": [record(p95_ms=150, energy_j=800)]})
        self.assertEqual(result["status"], "GUARDRAIL_VIOLATION")

    def test_less_completed_work_fails(self):
        result = evaluate({"native": [record()], "omni": [record(completed=99, energy_j=800)]})
        self.assertEqual(result["status"], "GUARDRAIL_VIOLATION")

    def test_extra_failures_fail(self):
        result = evaluate({"native": [record()], "omni": [record(failed=1, energy_j=800)]})
        self.assertEqual(result["status"], "GUARDRAIL_VIOLATION")

    def test_mismatched_hardware_rejected(self):
        changed = record()
        changed["hardware_id"] = "GPU-B"
        with self.assertRaises(ValueError):
            evaluate({"native": [record()], "omni": [changed]})

    def test_nonfinite_input_rejected(self):
        with self.assertRaises(ValueError):
            evaluate({"native": [record()], "omni": [record(energy_j=float("nan"))]})

    def test_no_repetitions_rejected(self):
        with self.assertRaises(ValueError):
            evaluate({"native": [], "omni": []})


if __name__ == "__main__":
    unittest.main()
