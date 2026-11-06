# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Each arm of the model gate runs its own checkout's engine (18 October). From omni-v9's gate on, tools/model_gate.py put its own
tree ahead of the checkout under test, so both arms ran the candidate's code. The gate now appends its tree after the checkout,
every worker names the tree its engine came from, and run() refuses a reading taken on the wrong one."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import model_gate  # noqa: E402


class ModelGateTree(unittest.TestCase):
    def test_the_gate_never_puts_its_own_tree_ahead_of_the_checkout(self):
        s = (ROOT / "tools" / "model_gate.py").read_text()
        self.assertNotIn("sys.path.insert(0, str(ROOT))", s)
        self.assertIn("sys.path.append(str(ROOT))", s)

    def _run(self, tree, reported):
        done = subprocess.CompletedProcess([], 0, stdout=json.dumps({"engine_tree": reported, "p95_ms": 1.0}) + "\n", stderr="")
        with mock.patch.object(model_gate.subprocess, "run", return_value=done):
            return model_gate.run(tree, ["--worker", "omni"])

    def test_a_reading_from_the_checkout_under_test_is_kept(self):
        self.assertEqual(self._run(ROOT, str(ROOT)), {"p95_ms": 1.0})

    def test_a_reading_taken_on_another_tree_is_refused(self):
        with self.assertRaises(RuntimeError):
            self._run(ROOT, "/somewhere/else")


if __name__ == "__main__":
    unittest.main()
