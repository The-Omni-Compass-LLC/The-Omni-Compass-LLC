# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The census (tools/census.py) is what its records give, its counts add up, and every gap it finds is on the archive's
request list: a run whose files GitHub still holds and a run a table names that raw does not hold."""
import json
import re
import unittest
from pathlib import Path

from tools.census import OUT, RECORDS, REQUEST, render

ROOT = Path(__file__).resolve().parents[1]


class Census(unittest.TestCase):
    def setUp(self):
        self.rec = json.loads(RECORDS.read_text(encoding="utf-8"))

    def test_page_is_its_records(self):
        self.assertEqual(OUT.read_text(encoding="utf-8"), render(self.rec))

    def test_counts_add_up(self):
        for wf, v in self.rec["workflows"].items():
            with self.subTest(wf=wf):
                self.assertEqual(sum(v["by_outcome"].values()), v["runs"])
                self.assertEqual(v["finished"], v["by_outcome"].get("success", 0) + v["by_outcome"].get("failure", 0))
                self.assertEqual(v["archived"] + v["with_files"] + v["no_files"] + v["unread"], v["finished"])
        raw = self.rec["raw"]
        self.assertLessEqual(raw["signed"], raw["checksums"])
        self.assertLessEqual(raw["checksums"], raw["folders"])

    def test_every_gap_is_requested(self):
        asked = set(re.findall(r"\b\d{9,12}\b", REQUEST.read_text(encoding="utf-8")))
        gaps = {str(x[1]) for x in self.rec["unarchived_with_files"]} | {i for _, i in self.rec["tables"]["not_on_raw"]}
        self.assertEqual(sorted(gaps - asked), [])


if __name__ == "__main__":
    unittest.main()
