# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Azure record (tools/azure_record.py): each run read by the one key on its own receipt, a tuning case never counted,
failed requests by the never-more rule, and the record in step with the receipts where the branch raw is fetched."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import azure_record as AR  # noqa: E402
import readings as K  # noqa: E402


class AzureRecord(unittest.TestCase):
    def test_a_tuning_case_is_never_counted(self):
        s, c = AR.kind("aks-metered work meter 2 4 6 8 10 12 16 20 dial max eastus Standard_D2s_v4")
        self.assertIn("2 4 6 8 10 12 16 20", s)
        self.assertTrue(c.startswith("tuning case"))
        self.assertEqual(AR.kind("aks-metered burst 1 4 1 6 1 9 replica room 0 dial save eastus Standard_D2_v4"), ("the burst 1 4 1 6 1 9", "counted set"))
        self.assertTrue(AR.kind("aks-metered burst 2 3 3 4 3 4 4 3 2 2 2 2 2 3 2 3 4 5 4 5 6 7 6 5 replica room 0 dial save")[0].startswith("the real day"))
        self.assertEqual(AR.kind("aks-metered steady replica room 0 to the cap, stopping rule dial save")[0], "the steady set under the stopping rule")

    def test_the_counted_work_meter_set_is_counted(self):
        """13 November: run A of the counted work meter set (43005182097) was read as a tuning case with rates "?"."""
        s, c = AR.kind("aks-metered work meter 2 4 6 8 10 12 16 20 to the cap, stopping rule dial max eastus Standard_D2s_v4")
        self.assertEqual((s, c), ("the work meter at rates 2 4 6 8 10 12 16 20 a second under the stopping rule", "counted set"))
        s, c = AR.kind("aks-metered work meter 10 20 40 60 80 100 120 140 dial max eastus Standard_D2s_v4")
        self.assertEqual((s, c), ("the work meter at rates 10 20 40 60 80 100 120 140 a second", "tuning case: sets the counted rates, never counted"))

    def test_each_word_by_what_the_gauge_is_for(self):
        bill = AR.reading({"native": 1.0, "omni": 1.012, "diff": 0.012, "ci95": [-0.001, 0.02], "significant": False}, K.SPENT, 97)
        self.assertEqual(bill["word"], K.GIVEN)
        self.assertIn("inside the noise", bill["text"])
        p99 = AR.reading({"native": 4744, "omni": 4222, "diff": -522, "ci95": [-1009, -34], "significant": True}, K.LOWER, 97)
        self.assertEqual(p99["word"], K.GAIN)
        self.assertTrue(p99["text"].startswith("GAIN, down 11.0%"))
        work = AR.reading({"native": 5.3, "omni": 9.0, "diff": 3.7, "ci95": [float("nan")] * 2, "significant": False}, K.HIGHER, 1)
        self.assertEqual(work["word"], K.GAIN)
        self.assertIn("one repetition", work["text"])
        under = AR.reading({"native": 100.0, "omni": 100.3, "diff": 0.3, "significant": False}, K.LOWER, 5)
        self.assertEqual(under["word"], K.STEADY)

    def test_failed_requests_never_more(self):
        up = AR.reading({"native": 4.4, "omni": 4.43, "diff": 0.03, "significant": False}, K.NEVER_MORE, 97)
        self.assertEqual(up["word"], K.LOSS)        # any rise, with no floor
        down = AR.reading({"native": 4.4, "omni": 3.9, "diff": -0.5, "significant": False}, K.NEVER_MORE, 97)
        self.assertEqual(down["word"], f"{K.GAIN} or {K.STEADY}")
        same = AR.reading({"native": 4.4, "omni": 4.4, "diff": 0.0, "significant": False}, K.NEVER_MORE, 97)
        self.assertEqual(same["word"], K.STEADY)

    def test_the_record_is_in_step_with_the_receipts(self):
        d = AR.build(check=True)
        if not d["runs"]:
            self.skipTest("the branch raw is not fetched here")
        kept = json.loads(AR.OUT_JSON.read_text(encoding="utf-8"))
        self.assertEqual([x["id"] for x in kept["runs"]], [x["id"] for x in d["runs"]])
        for x in kept["runs"]:
            self.assertTrue(x["receipt"].startswith(f"raw:run-{x['id']}/"))
            self.assertIn(x["counts"], ("counted set", "tuning case: sets the counted rates, never counted"))


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
