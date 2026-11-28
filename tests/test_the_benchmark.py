# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The one benchmark stands as its records say (tools/the_benchmark.py): every scenario the carry record holds, each in one place,
on the engine that stands, with only that engine's own receipts counted, and the LOSS rows against native the LOSS ledger's."""
import unittest

from tools import the_benchmark as tb, carry


class TheBenchmark(unittest.TestCase):
    def test_current(self):
        self.assertEqual(tb.main(["--check"]), 0)

    def test_every_scenario_once_and_only_the_engines_own_receipts_counted(self):
        b = tb.build()
        rows = [r for rs in b["places"].values() for r in rs]
        self.assertEqual(sorted(r["benchmark"] + r["table"] for r in rows),
                         sorted(r["benchmark"] + r["table"] for r in carry.build()["rows"]))
        for r in rows:
            if r["state"] != "on the engine that stands":
                self.assertEqual(r["judged"], {}, r["benchmark"])
            else:
                self.assertTrue(r["table"].split("/")[-1].startswith(f"V{b['engine']['version'].split('v')[-1]}_"), r["table"])

    def test_every_paid_queue_is_listed_with_its_switch(self):
        b = tb.build()
        names = {q["cloud"] for q in b["waiting"]["clouds"]}
        self.assertTrue({"azure", "amazon", "google"} <= names, names)
        for q in b["waiting"]["clouds"]:
            self.assertIn(q["switch"], ("on", "off"), q)


if __name__ == "__main__":
    unittest.main()
