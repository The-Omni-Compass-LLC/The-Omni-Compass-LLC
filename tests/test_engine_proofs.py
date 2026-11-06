# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine's machine-checked proofs (tools/prove_engine.py, docs/ENGINE_PROOFS.md) are run on every push: every claim
must come back proved, none vacuous, and the stored record must be the one the proofs produce now."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import prove_engine  # noqa: E402
from omnicompass import core as C  # noqa: E402


class EngineProofs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stored = json.loads(prove_engine.OUT.read_text())
        cls.code = prove_engine.main(["--quiet"])
        cls.now = json.loads(prove_engine.OUT.read_text())

    def test_every_claim_is_proved(self):
        self.assertEqual(self.code, 0)
        items = {k: v for part in ("smt", "intervals") for k, v in self.now[part].items() if not k.startswith("_")}
        self.assertEqual(sorted(k for k, v in items.items() if v["result"] != "proved"), [])
        self.assertEqual(len(items), self.now["summary"]["of"])

    def test_the_stored_record_is_the_one_the_proofs_produce(self):
        self.assertEqual(self.stored, self.now)

    def test_the_tracking_bound_is_inside_the_basin_and_the_run(self):
        u = self.now["intervals"]
        self.assertLess(u["U3"]["r_star_upper"], C.BASIN_TOL)
        self.assertLessEqual(u["U5"]["micro_steps_max"], C.MACRO_STEPS * C.MICRO_STEPS)
        self.assertLess(u["U1"]["F_D_upper"], C.U_AUTHORITY)


if __name__ == "__main__":
    unittest.main()
