# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The health watch (tools/health_watch.py): a workflow that keeps failing, or starts itself over and over, raises an alarm;
a busy hour of healthy runs raises none. The conductor's hour of 24 October (one failed start every 15 seconds) is the case."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import health_watch as H  # noqa: E402


class HealthWatch(unittest.TestCase):
    def test_the_conductors_runaway_hour_raises_both_alarms(self):
        runs = [{"name": "grid", "conclusion": "failure"} for _ in range(240)]
        found = H.alarms(runs)
        self.assertIn(("grid", "failing", 240), found)
        self.assertIn(("grid", "runaway", 240), found)

    def test_a_busy_healthy_hour_raises_none(self):
        runs = ([{"name": "six", "conclusion": "success"} for _ in range(300)]
                + [{"name": "verify", "conclusion": "success"} for _ in range(20)]
                + [{"name": "verify", "conclusion": "failure"} for _ in range(H.FAIL_LIMIT - 1)])
        self.assertEqual(H.alarms(runs), [])

    def test_repeated_failures_alone_raise_the_failing_alarm(self):
        found = H.alarms([{"name": "aks-metered", "conclusion": "failure"} for _ in range(H.FAIL_LIMIT)])
        self.assertEqual(found, [("aks-metered", "failing", H.FAIL_LIMIT)])


if __name__ == "__main__":
    unittest.main()
