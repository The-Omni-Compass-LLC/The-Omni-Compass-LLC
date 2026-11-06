# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The index reads each test from its newest whole table: a newer table written from runs that failed (no workload beside
the tuning one, no gauge row) is passed over, so no test leaves the index or the benefit sheet for a failed run (20 October:
the omni-v12 MongoDB table, whose runs B and C had no workload, had taken MongoDB off both)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import omni_index  # noqa: E402


class NewestWholeTable(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = omni_index.LIVE
        omni_index.LIVE = self.tmp

    def tearDown(self):
        omni_index.LIVE = self.saved

    def write(self, name, data):
        (self.tmp / name).write_text(json.dumps(data))

    def test_an_empty_newer_table_is_passed_over(self):
        self.write("V11_YCSB.json", {"runs": [{"run": "1"}] * 3, "workloads": {"tuning": {}, "b": {"x": 1}}, "verdicts": {"b": "GAIN"}})
        self.write("V12_YCSB.json", {"runs": [{"run": "2"}] * 3, "workloads": {}})
        self.assertEqual(omni_index.newest("V7_YCSB.json"), "V11_YCSB.json")
        self.assertFalse(omni_index.whole(self.tmp / "V12_YCSB.json"))
        self.assertTrue(omni_index.whole(self.tmp / "V11_YCSB.json"))

    def test_the_tuning_workload_alone_is_not_whole(self):
        self.write("V11_YCSB.json", {"runs": [], "workloads": {"b": {"x": 1}}})
        self.write("V12_YCSB.json", {"runs": [], "workloads": {"tuning": {"x": 1}}})
        self.assertEqual(omni_index.newest("V7_YCSB.json"), "V11_YCSB.json")

    def test_a_whole_newer_table_takes_the_place(self):
        self.write("V11_YCSB.json", {"runs": [], "workloads": {"b": {"x": 1}}})
        self.write("V12_YCSB.json", {"runs": [], "workloads": {"b": {"x": 2}, "c": {"x": 3}}})
        self.assertEqual(omni_index.newest("V7_YCSB.json"), "V12_YCSB.json")

    def test_a_kubernetes_table_is_whole_by_its_rows(self):
        self.write("V12_GOLDILOCKS.json", {"runs": [], "rows": {"p95": {"runs": []}}})
        self.write("V13_GOLDILOCKS.json", {"runs": [], "rows": {}})
        self.assertEqual(omni_index.newest("V7_GOLDILOCKS.json"), "V12_GOLDILOCKS.json")

    def test_no_whole_table_falls_back_to_the_newest(self):
        self.write("V12_X.json", {"runs": [], "workloads": {}})
        self.write("V13_X.json", {"runs": [], "workloads": {}})
        self.assertEqual(omni_index.newest("V7_X.json"), "V13_X.json")
        self.assertEqual(omni_index.newest("V7_NONE.json"), "V7_NONE.json")


if __name__ == "__main__":
    unittest.main()
