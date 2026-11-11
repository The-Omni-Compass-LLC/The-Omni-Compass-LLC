# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The page of every Azure run (tools/azure_runs.py) is what its records give: every run once, linked to GitHub's own run page,
its engine and its standing named, and no run said to be counted by a table that does not name it."""
import json
import re
import unittest
from pathlib import Path

from tools.azure_runs import OUT, RECORDS, render

ROOT = Path(__file__).resolve().parents[1]


class AzureRuns(unittest.TestCase):
    def setUp(self):
        self.rec = json.loads(RECORDS.read_text(encoding="utf-8"))

    def test_page_is_its_records(self):
        self.assertEqual(OUT.read_text(encoding="utf-8"), render(self.rec))

    def test_every_run_once_with_its_link(self):
        ids = [r["id"] for r in self.rec["runs"]]
        self.assertEqual(len(ids), len(set(ids)))
        page = OUT.read_text(encoding="utf-8")
        for i in ids:
            self.assertEqual(page.count(f"[{i}](https://github.com/"), 1, i)

    def test_a_table_named_names_the_run(self):
        for r in self.rec["runs"]:
            for t in r["tables"]:
                text = "".join((ROOT / t).with_suffix(s).read_text(encoding="utf-8", errors="replace")
                               for s in (".md", ".json") if (ROOT / t).with_suffix(s).exists())
                self.assertTrue(re.search(rf"\b{r['id']}\b", text), (r["id"], t))


if __name__ == "__main__":
    unittest.main()
