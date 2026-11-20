# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The every-chip board stands as the chip tables say (tools/chips_board.py): every table on a chip, every chip in the register,
a chip with no table listed as wired and not yet run, every LOSS row listed, never a chip number across engines."""
import json
import unittest
from pathlib import Path

from tools import chips_board as cb

ROOT = Path(__file__).resolve().parents[1]


class ChipsBoard(unittest.TestCase):
    def test_current(self):
        self.assertEqual(cb.main(["--check"]), 0)

    def test_every_table_on_a_known_chip_and_every_loss_listed(self):
        b = cb.build()
        self.assertEqual(len(b["tables"]), len(list((ROOT / "results" / "gpu").glob("*_ABC.json"))))
        for t in b["tables"]:
            self.assertNotEqual(t["chip"], "unknown", t["table"])
            losses = sum(c.get("LOSS", 0) for c in t["counts"].values())
            self.assertEqual(losses, sum(1 for x in t["listed"] if x["reading"].startswith("LOSS")), t["table"])
        for r in b["register"]:
            self.assertEqual(r["status"], "run" if r["tables"] else "wired, not yet run")

    def test_combined_never_across_engines(self):
        b = cb.build()
        for e, v in b["combined"].items():
            self.assertEqual(v["tables"], sum(1 for t in b["tables"] if t["engine"] == e))


if __name__ == "__main__":
    unittest.main()
