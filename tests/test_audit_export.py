# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The scoring contract's export (tools/audit_export.py, the solid-A directive's phase 4): the files are what the record gives
now; the independent classifier reads no row otherwise than the key; every raw change carries the true sign of Omni-Compass
minus native; the counts of the standing tables against native are the verdict audit's; a resource spent that rose is never a
LOSS; and no row is called exactly the same unless its values agree to nine decimals."""
import csv
import json
import unittest
from pathlib import Path

from tools import audit_export as AE

ROOT = Path(__file__).resolve().parents[1]


class AuditExport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a, cls.rows = AE.build()

    def test_files_current(self):
        self.assertEqual(AE.main(["--check"]), 0, "python3 tools/audit_export.py")

    def test_no_row_read_otherwise(self):
        bad = [(r["table"], r["gauge"], r["classification"], r["independent_classification"])
               for r in self.rows if r["independent_agrees"] == "NO"]
        self.assertEqual(bad, [])

    def test_raw_sign_is_omni_minus_native(self):
        n = 0
        for r in self.rows:
            nat = [x for x in r["native_runs"].split("; ")]
            om = [x for x in r["omni_runs"].split("; ")]
            raws = r["raw_delta_runs"].split("; ")
            for a, b, d in zip(nat, om, raws):
                if not a or not b or not d or d.startswith("absolute"):
                    continue
                diff = float(b) - float(a)
                if abs(diff) < 1e-12 * max(abs(float(a)), 1.0):
                    continue
                n += 1
                self.assertEqual(d[0], "+" if diff > 0 else "−", (r["table"], r["gauge"], a, b, d))
        self.assertGreater(n, 15000)

    def test_counts_are_the_verdict_audits(self):
        c = self.a["counts"]["standing_against_native"]
        st = [r for r in self.rows if r["status"] == "standing" and r["comparison"] == "against its native"]
        got = {AE.C_GAIN: 0, AE.C_LOSS: 0, AE.C_GIVEN: 0, AE.C_DISAGREE: 0}
        for r in st:
            if r["classification"] in got:
                got[r["classification"]] += 1
        self.assertEqual(got[AE.C_GAIN], c.get("GAIN", 0))
        self.assertEqual(got[AE.C_LOSS], c.get("LOSS", 0))
        self.assertEqual(got[AE.C_GIVEN], c.get("power given", 0))
        self.assertEqual(got[AE.C_DISAGREE], c.get("the runs disagree", 0))

    def test_resource_spent_never_a_loss(self):
        self.assertEqual([r["gauge"] for r in self.rows if r["metric_direction"].startswith("spent:")
                          and r["classification"] == AE.C_LOSS], [])

    def test_exact_means_nine_decimals(self):
        """The independent classifier calls a row exact only where every run's values agree to 1e-9 of the value."""
        row = {"aim": "lower", "runs": [{"native": 1000.0, "omni": 1000.0 + 5e-6}] * 3, "word": "STEADY"}
        self.assertEqual(AE.independent(row)[0], AE.C_FLOOR)
        row = {"aim": "lower", "runs": [{"native": 1000.0, "omni": 1000.0 + 5e-7}] * 3, "word": "STEADY"}
        self.assertEqual(AE.independent(row)[0], AE.C_EXACT)

    def test_zero_native_makes_no_percentage(self):
        row = {"aim": "lower", "runs": [{"native": 0.0, "omni": 0.4}, {"native": 0.0, "omni": 0.2}, {"native": 0.0, "omni": 0.1}]}
        self.assertEqual(AE.independent(row)[0], AE.C_LOSS)
        vals = AE.run_values(row)
        self.assertTrue(all(v["rel"] is None for v in vals))

    def test_csv_columns(self):
        with open(AE.CSV_OUT, encoding="utf-8") as f:
            head = next(csv.reader(f))
        for col in ("benchmark", "engine", "native_runs", "omni_runs", "raw_delta_runs", "metric_direction",
                    "performance_effect", "verdict", "confidence", "evidence_class", "source"):
            self.assertIn(col, head)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
