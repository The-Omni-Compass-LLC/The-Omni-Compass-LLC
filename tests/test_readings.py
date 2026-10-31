# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words rule (tools/readings.py): GAIN, STEADY and LOSS, set by what the gauge is for and never by its sign."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import readings as R  # noqa: E402


class Words(unittest.TestCase):
    def test_word_by_aim_not_sign(self):
        self.assertEqual(R.word(True, R.LOWER), R.GAIN)        # a response time that fell
        self.assertEqual(R.word(False, R.LOWER), R.LOSS)       # a response time that rose
        self.assertEqual(R.word(False, R.HIGHER), R.GAIN)      # work that rose
        self.assertEqual(R.word(True, R.HIGHER), R.LOSS)       # work that fell
        self.assertEqual(R.word(True, R.SPENT), R.GAIN)        # a resource cut
        self.assertEqual(R.word(False, R.SPENT), R.GIVEN)      # a resource that rose: power given, never a loss

    def test_aim_of_a_resource(self):
        self.assertEqual(R.aim("lower", "node-hours"), R.SPENT)
        self.assertEqual(R.aim("lower", "response time (ms), mean"), R.LOWER)
        self.assertIsNone(R.aim("shown"))

    def test_classify_new_and_old_words(self):
        self.assertEqual(R.classify("**GAIN in all three of our runs**", R.LOWER), "gain")
        self.assertEqual(R.classify("**power given in all three of our runs**", R.SPENT), "given")
        self.assertEqual(R.classify("**LOSS in all three of our runs**", R.HIGHER), "loss")
        self.assertEqual(R.classify("STEADY, no difference beyond the noise (all three runs)", R.LOWER), "noise")
        self.assertEqual(R.classify("**the runs disagree**", R.LOWER), "disagree")
        # older recorded tables read back the same way
        self.assertEqual(R.classify("**lower in all three of our runs**", R.LOWER), "gain")
        self.assertEqual(R.classify("**higher in all three of our runs**", R.SPENT), "given")
        self.assertEqual(R.classify("no difference beyond the noise (3 of 3 runs)", R.LOWER), "noise")

    def test_labels_word_first(self):
        self.assertEqual(R.labelled("SUPERIOR WITHIN GUARDRAILS"), "GAIN (within the guardrails)")
        self.assertTrue(R.labelled("AT ITS LIMIT ON NATIVE").startswith(R.STEADY))
        self.assertEqual(R.labelled("AWAY FROM ITS AIMS"), R.LOSS)

    def test_the_key(self):
        text = "\n".join(R.key_lines())
        for w in ("Growth", "Advantage", "Improvement", "Net-positive", "Stable", "True to baseline", "Equilibrium",
                  "At par", "Drift-free", "Yield held", "Leakage", "Off-track", "Setback", "Subpar", "power given", "Disclosure and disclaimer",
                  R.OWN_RUNS):
            self.assertIn(w, text)
        self.assertEqual(R.check_pages(), [], "a page lacks the key word for word: python3 tools/readings.py --fix")


class Landed(unittest.TestCase):
    """A newer engine's table takes its benchmark's place only once its three runs share a reading (20 October: the three
    omni-v12 YCSB runs each failed partway, their table held no workload in all three, and the benchmark fell off the
    benefit sheet and the Omni index instead of omni-v11's table standing)."""

    def test_a_table_whose_runs_share_no_workload_has_not_landed(self):
        import json, tempfile
        from tools import benefit_sheet, omni_index
        run = {"native": 1.0, "omni": 0.9, "diff": -0.1, "ci95": [-0.2, -0.05]}
        with tempfile.TemporaryDirectory() as td:
            live = Path(td)
            (live / "V11_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {"f": {"g": {"reading": "x", "runs": [run, run, run]}}}}))
            (live / "V12_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {}}))
            (live / "V12_DEMO.md").write_text("# demo\n")
            self.assertTrue(R.landed(live / "V11_DEMO.json"))
            self.assertFalse(R.landed(live / "V12_DEMO.json"))
            self.assertFalse(R.landed(live / "V12_DEMO.md"))          # read through its JSON twin
            keep = (benefit_sheet.LIVE, omni_index.LIVE)
            benefit_sheet.LIVE = omni_index.LIVE = live
            try:
                self.assertEqual(benefit_sheet.newest_table("V7_DEMO.json"), "V11_DEMO.json")
                self.assertEqual(omni_index.newest("V7_DEMO.json"), "V11_DEMO.json")
                (live / "V12_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {"tuning": {"g": {"runs": [run, run, run]}}}}))
                self.assertEqual(omni_index.newest("V7_DEMO.json"), "V11_DEMO.json")   # the tuning workload alone reads nothing
                (live / "V12_ORG.json").write_text(json.dumps({"organisms": {"spine": {}}}))
                self.assertTrue(R.landed(live / "V12_ORG.json"))                       # another table's shape: its writer decides
                (live / "V12_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {"f": {"g": {"runs": [run, run, run]}}}}))
                self.assertEqual(benefit_sheet.newest_table("V7_DEMO.json"), "V12_DEMO.json")
                self.assertEqual(omni_index.newest("V7_DEMO.json"), "V12_DEMO.json")
            finally:
                benefit_sheet.LIVE, omni_index.LIVE = keep


if __name__ == "__main__":
    unittest.main()
