# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""More work at the end of the day (tools/work_today.py): every test's work row, from the records and nowhere else."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import work_today as wt  # noqa: E402


class WorkToday(unittest.TestCase):
    def test_the_page_is_what_the_records_give(self):
        self.assertEqual(wt.main(["--check"]), 0, "python3 tools/work_today.py")

    def test_every_test_is_read_once_and_a_fixed_load_is_never_counted_as_held_work(self):
        d = wt.build()
        names = [r["source"] + "|" + r["test"] for r in d["counted"] + d["blind"]]
        self.assertEqual(len(names), len(set(names)))
        self.assertFalse([r for r in d["counted"] if "fixed-rate work" in r["reading"]])
        self.assertEqual(sum(d["tally"].values()), len(d["counted"]))

    def test_a_word_is_the_records_own(self):
        for r in wt.build()["counted"]:
            self.assertTrue(r["reading"].startswith(r["word"]) or r["word"] in r["reading"], r)


if __name__ == "__main__":
    unittest.main()
