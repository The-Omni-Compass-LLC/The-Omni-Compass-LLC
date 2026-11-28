# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine's ladder stands as its records say (tools/engine_ladder.py): every fingerprinted version a step, in order, each
with its change-control row from omni-v5 on, and each table counted under its own engine only."""
import unittest

from tools import engine_ladder as el


class EngineLadder(unittest.TestCase):
    def test_current(self):
        self.assertEqual(el.main(["--check"]), 0)

    def test_every_version_in_order_and_tables_never_across_engines(self):
        b = el.build()
        ns = [int(s["version"].split("v")[-1]) for s in b["steps"]]
        self.assertEqual(ns, sorted(ns))
        self.assertEqual(len(ns), len(el.versions()))
        for s in b["steps"]:
            n = s["version"].split("v")[-1]
            for t in s["tables"]:
                self.assertTrue(t["table"].split("/")[-1].startswith(f"V{n}_"), (s["version"], t["table"]))
            if int(n) >= 5:
                self.assertTrue(s["change"], f"{s['version']} has no change-control row")


if __name__ == "__main__":
    unittest.main()
