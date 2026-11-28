# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The compass loop's record (tools/compass_loop.py, results/model_gate/COMPASS_LOOP.md) is the one the engine's code
produces now, and in the proof's own case (M1, no damping) every row sits at or under the proved radius R*."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import compass_loop  # noqa: E402


class CompassLoopRecord(unittest.TestCase):
    def test_the_stored_record_is_current(self):
        self.assertEqual(compass_loop.main(["--check"]), 0)

    def test_the_proofs_case_never_passes_the_proved_radius(self):
        rows = [r for r in compass_loop.measure() if r["model"] == "M1, the proof's case"]
        self.assertTrue(rows)
        self.assertTrue(all(r["inside"] for r in rows))

    def test_every_row_is_kept_whichever_way_it_falls(self):
        rec = compass_loop.record()
        self.assertEqual(sum(s["rows"] for s in rec["summary"].values()), len(rec["rows"]))
        self.assertTrue(any(not r["inside"] for r in rec["rows"]))     # the rows beyond R* stay in the record


if __name__ == "__main__":
    unittest.main()
