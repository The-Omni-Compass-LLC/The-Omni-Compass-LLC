# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The numbers a website may show (tools/site_numbers.py): every one with a receipt that exists, never our own model as a
result, the model's columns and the figures no receipt carries listed as not for the site, and the four arms A, B, C and D."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import site_numbers as S  # noqa: E402


class SiteNumbers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = S.build()

    def test_every_number_shown_has_a_receipt_and_is_never_the_model(self):
        self.assertTrue(self.d["show"])
        for n in self.d["show"]:
            with self.subTest(n=n["id"]):
                self.assertIn(n["cls"], ("L", "P"), "our own model (class S) is never shown as a result")
                path = n["receipt"].split(" (")[0]
                self.assertTrue((ROOT / path).exists(), f"{n['id']}: no receipt at {path}")
                self.assertTrue(n["sentence"])
                self.assertNotIn("ABC_TABLE", n["receipt"])

    def test_the_models_columns_and_the_unbacked_figures_are_not_for_the_site(self):
        no = {n["id"]: n for n in self.d["not_for_the_site"]}
        # 4 November: the model table left results/, where the website had read it and printed 47.2% and 49.9% as results
        self.assertFalse((ROOT / "results" / "ABC_TABLE.json").exists(), "a model table under results/ is read as a result")
        abc = json.loads((ROOT / "docs" / "history" / "model_tables" / "ABC_TABLE_MODEL.json").read_text(encoding="utf-8"))
        self.assertIn("web", abc)
        # 4 November, the founder: those two figures are garbage and live nowhere, not even as a figure on the remove list
        for k in ("abc_web_speed", "abc_multi_speed", "abc_gpu_energy"):
            self.assertIsNone(no[k]["value_pct"], k)
        for f in ("SITE_NUMBERS.json", "SITE_NUMBERS.md"):
            text = (ROOT / "results" / f).read_text(encoding="utf-8")
            for figure in ("47.2", "49.9"):
                self.assertNotIn(figure, text, f"{figure} in results/{f}")
        for k in ("abc_web_speed", "abc_multi_speed", "abc_gpu_energy", "drain_20_percent", "sixteen_million", "free_work_33",
                  "thirteen_point_one", "arm_d_work_per_dollar"):
            self.assertIn(k, no)
        # arm D is shown from its receipt; only its work per dollar waits (the founder's words of 4 November: four arms, A, B, C, D)
        self.assertFalse(any("nothing for D" in n["why"] for n in no.values()))
        shown = " ".join(n["sentence"] for n in self.d["show"])
        for figure in ("47.2", "49.9", "20%", "$16"):
            self.assertNotIn(figure, shown, f"{figure} has no receipt and is shown")

    def test_four_arms_each_from_its_receipt(self):
        arms = self.d["four_arms"]
        self.assertEqual(sorted(arms), ["A", "B", "C", "D"])
        for k, x in arms.items():
            with self.subTest(arm=k):
                self.assertTrue((ROOT / x["receipt"].split(" (")[0]).exists())
        self.assertEqual(len(arms["A"]["runs"]), len(arms["B"]["runs"]))
        self.assertIn("the bill", arms["D"]["values"])
        self.assertTrue(any(s["id"] == "arm_d_vs_c" for s in self.d["show"]))

    def test_the_page_is_its_records(self):
        self.assertEqual(S.main(["--check"]), 0)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
