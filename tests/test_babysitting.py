# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The babysitting tax (the founder's order of 14 October): the receipt counts, in both arms, the alert minutes (whole
minutes whose 95th percentile, failed requests counted over, was over the line) and, from the governor's audit, the
settings commands it wrote on its own and the share of its additions decided while the service was still inside its
line (tools/live_reps.py, babysitting)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import live_reps  # noqa: E402


def arm(root, name, minutes, audit=None, t0=1000.0):
    """A repetition folder: one sample a second per minute, each minute's latencies given as (ms, ok) pairs."""
    d = root / name; d.mkdir()
    rows = ["elapsed_seconds,latency_ms,ok"]
    for m, samples in enumerate(minutes):
        for i, (ms, ok) in enumerate(samples):
            rows.append(f"{60 * m + i * 60.0 / len(samples):.2f},{ms},{1 if ok else 0}")
    (d / "latency.csv").write_text("\n".join(rows) + "\n")
    (d / "window_start.txt").write_text(f"{t0}\n")
    (d / "window_end.txt").write_text(f"{t0 + 60 * len(minutes)}\n")
    if audit is not None:
        (d / "audit.jsonl").write_text("".join(json.dumps(r) + "\n" for r in audit))
    return d


class Babysitting(unittest.TestCase):
    def test_alert_minutes_count_whole_minutes_whose_95th_percentile_is_over_the_line(self):
        calm = [(100.0, True)] * 100
        slow = [(100.0, True)] * 90 + [(900.0, True)] * 10            # p95 = 900 ms: over a 500 ms line
        failing = [(100.0, True)] * 94 + [(0.0, False)] * 6           # a failed request counts over: p95 over
        edge = [(100.0, True)] * 95 + [(900.0, True)] * 5             # p95 at rank 95 = 100 ms: inside
        with tempfile.TemporaryDirectory() as t:
            d = arm(Path(t), "bench-native-1", [calm, slow, failing, edge])
            g = live_reps.babysitting(d, 500.0)
            self.assertEqual(g[live_reps.ALERT], 2.0)
            self.assertEqual(g[live_reps.COMMANDS], 0.0)               # native runs no governor
            self.assertNotIn(live_reps.AHEAD, g)

    def test_the_governors_own_commands_and_its_additions_ahead_of_the_line(self):
        calm = [(100.0, True)] * 60
        audit = [{"time": 900.0, "write": ["kubectl", "annotate"], "why": "snapshot", "dry_run": False},   # before the window
                 {"time": 1001.0, "decision": {"nodes_observed": 2, "nodes_recommended": 2, "hpa_target_recommended": 0.5, "latency_p95_ms": 200.0}},
                 {"time": 1016.0, "decision": {"nodes_observed": 2, "nodes_recommended": 3, "hpa_target_recommended": 0.5, "latency_p95_ms": 300.0}},
                 {"time": 1017.0, "write": ["az", "aks", "nodepool", "scale"], "why": "compass", "dry_run": False},
                 {"time": 1031.0, "decision": {"nodes_observed": 3, "nodes_recommended": 3, "hpa_target_recommended": 0.4, "latency_p95_ms": 650.0}},
                 {"time": 1032.0, "write": ["kubectl", "patch", "hpa"], "why": "compass", "dry_run": False},
                 {"time": 1046.0, "decision": {"nodes_observed": 3, "nodes_recommended": 2, "hpa_target_recommended": 0.5, "latency_p95_ms": 100.0}},
                 {"time": 1047.0, "write": ["kubectl", "patch", "hpa"], "why": "compass", "dry_run": True}]          # a dry run is no command
        with tempfile.TemporaryDirectory() as t:
            d = arm(Path(t), "bench-compass-1", [calm], audit=audit)
            g = live_reps.babysitting(d, 500.0)
            self.assertEqual(g[live_reps.ALERT], 0.0)
            self.assertEqual(g[live_reps.COMMANDS], 2.0)
            self.assertEqual(g[live_reps.AHEAD], 50.0)                 # two additions, one decided inside the line

    def test_the_rows_stand_in_the_receipt_and_only_the_alert_minutes_are_judged(self):
        self.assertLess(live_reps.KEYS.index("failed requests (%)"), live_reps.KEYS.index(live_reps.ALERT))
        self.assertIn(live_reps.COMMANDS, live_reps.NEUTRAL)
        self.assertIn(live_reps.AHEAD, live_reps.NEUTRAL)
        self.assertNotIn(live_reps.ALERT, live_reps.NEUTRAL)
        self.assertEqual(live_reps.sig_word(live_reps.ALERT, -3.0), "yes: GAIN")


if __name__ == "__main__":
    unittest.main()
