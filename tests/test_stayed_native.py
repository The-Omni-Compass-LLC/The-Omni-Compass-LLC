# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Staying native is the governor's own decision (the founder's order of 10 October): a window in which the governor
decided at every step and made no write counts as it ran, and the live table says in how many repetitions that was
(scripts/kind_bench.sh writes omni_stayed_native.txt; tools/live_reps.py counts it beside the paired table)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import live_reps  # noqa: E402

BENCH = Path(__file__).resolve().parents[1] / "scripts" / "kind_bench.sh"


class StayedNative(unittest.TestCase):
    def test_the_table_counts_the_windows_the_governor_stayed_native(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            for arm in ("native", "compass"):
                for rep in ("1", "2", "10"):
                    d = root / f"bench-{arm}-{rep}"; d.mkdir()
                    (d / "capture.csv").write_text("")
            (root / "bench-compass-2" / "omni_stayed_native.txt").write_text("Omni-Compass stayed native: 14 decisions recorded, no write\n")
            (root / "bench-compass-10" / "omni_stayed_native.txt").write_text("Omni-Compass stayed native: 14 decisions recorded, no write\n")
            gauges = lambda d: {k: (1.0 if "native" in d.name else 0.9) + 0.01 * int(d.name.rsplit("-", 1)[1]) for k in live_reps.KEYS}
            with mock.patch.object(live_reps, "arm_gauges", gauges), mock.patch("builtins.print"):
                live_reps.main(root)
            md = (root / "LIVE_REPS.md").read_text()
            self.assertIn("Omni-Compass stayed native in 2 of 3 repetitions (repetitions 2, 10)", md)
            out = json.loads((root / "LIVE_REPS.json").read_text())
            self.assertEqual(out["stayed_native"], {"compass": ["2", "10"]})
            self.assertNotIn("_stayed_native", out["paired"]["compass"])     # the paired table holds gauges only
            self.assertEqual(sorted(out["repetitions"]["compass"]), ["1", "10", "2"])  # every window counts as it ran

    def test_the_rig_keeps_a_decided_window_and_refuses_a_silent_governor(self):
        s = BENCH.read_text()
        self.assertIn('decisions=$(grep -c \'"decision"\' "$OUT_DIR/audit.jsonl" || true)', s)
        self.assertIn('the governor was not running"; exit 1; }', s)
        self.assertIn('tee "$OUT_DIR/omni_stayed_native.txt"', s)
        self.assertNotIn("Omni made no write, so the reset would prove nothing", s)

    def test_a_failed_decision_is_named_and_a_window_with_no_machine_is_refused_in_either_arm(self):
        s = BENCH.read_text()
        # failed decisions are counted apart and named by their error, never read as a governor that was not running
        self.assertIn('failed=$(grep -c \'"consecutive_failures"\' "$OUT_DIR/audit.jsonl" || true)', s)
        self.assertIn('more failed and wrote nothing, the last with', s)
        # the rule on readings with no machine in service stands after the arm's own checks, outside the omni-only block
        tail = s[s.rindex("\nfi\n"):]
        self.assertIn("awk -F, 'NR > 1 && $4 == 0' \"$OUT_DIR/capture.csv\"", tail)
        self.assertIn("INVALID RUN: the cluster showed no machine in service", tail)
        cap = (BENCH.parents[1] / "fleet" / "capture" / "kube_capture.sh").read_text()
        self.assertIn('no machine in service; the nodes as they stood:', cap)


if __name__ == "__main__":
    unittest.main()
