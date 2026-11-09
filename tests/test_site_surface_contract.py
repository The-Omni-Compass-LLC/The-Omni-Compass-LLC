# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; see LICENSE, NOTICE and DISCLOSURES.md.
"""Check the website contract against exact source rows and proposed pricing."""
import json
from pathlib import Path
import unittest

from tools.site_surface_contract import ROOT, OUT, PUBLISHER, SURFACES, build_contract


class WebsiteSurfaceContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = build_contract()
        cls.published = json.loads(OUT.read_text(encoding="utf-8"))

    def test_published_contract_is_current(self):
        self.assertEqual(self.published, self.contract)
        self.assertEqual(self.published["publisher"], PUBLISHER)
        self.assertEqual(len(self.published["claims"]), 10)

    def test_every_page_and_spoken_reading_uses_receipt_only(self):
        ids = {row["id"] for row in self.published["claims"]}
        self.assertEqual(set(self.published["surfaces"]), set(SURFACES))
        for surface, keys in self.published["surfaces"].items():
            with self.subTest(surface=surface):
                self.assertTrue(set(keys) <= ids)
        self.assertIn("Where", self.published["virtual_guide_scripts"]["where_numbers_come_from"].title() or "Where")
        self.assertIn("not a whole-system bill reduction",
                      self.published["virtual_guide_scripts"]["where_numbers_come_from"])
        self.assertIn("adverse results", self.published["evidence_rule"])
        self.assertIn("could not be read", self.published["unavailable_message"])
        for row in self.published["claims"]:
            with self.subTest(claim=row["id"]):
                self.assertTrue(row["sentence"])
                self.assertIn(row["evidence_class"], ("L", "P"))
                self.assertTrue((ROOT / row["receipt"].split(" (")[0]).exists())

    def test_pricing_is_a_proposal_not_measurement(self):
        proposal = self.published["commercial_proposal"]
        self.assertEqual(proposal["status"], "proposed_not_executed")
        self.assertEqual(proposal["savings_participation_rate"], .25)
        self.assertEqual(proposal["hardware_embedding_royalty_rate"], .05)
        self.assertIn("defined by signed agreement", proposal["royalty_base"])
        for phrase in ("hardware", "bill", "cost"):
            self.assertNotIn("20% reduction in " + phrase,
                             self.published["product_definition"])


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
