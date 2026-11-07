# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""tools/carry.py: a result carries to the engine that stands only when every engine file its runner imports is byte for byte its
own engine's (the founder's order of 7 November, evening: "we use the one that's got all that if it hasn't moved")."""
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import carry  # noqa: E402


class Carry(unittest.TestCase):
    def test_the_imports_are_followed_through_the_fingerprint(self):
        files = set(carry.fingerprints()[max(carry.fingerprints())])
        governor = carry.imports("omni_controller/controller.py", files)
        self.assertIn("omni_controller/muscles.py", governor)          # the governor runs the conveyance
        self.assertNotIn("omni_controller/controller.py", carry.imports("tools/run_mujoco.py", files))

    def test_a_result_carries_only_when_nothing_it_runs_has_moved(self):
        fps = {1: {"run.py": "a", "core.py": "b", "other.py": "c"}, 2: {"run.py": "a", "core.py": "b", "other.py": "CHANGED"}}
        table = (1, "STORE", ROOT / "results" / "live", ROOT / "results" / "live" / "V1_STORE.json")
        with mock.patch.object(carry, "fingerprints", return_value=fps), \
                mock.patch.object(carry, "newest_tables", return_value=[table]), \
                mock.patch.object(carry, "runner", return_value="run.py"):
            with mock.patch.object(carry, "imports", return_value={"run.py", "core.py"}):
                self.assertEqual(carry.build()["rows"][0]["state"], "carries")
            with mock.patch.object(carry, "imports", return_value={"run.py", "core.py", "other.py"}):
                row = carry.build()["rows"][0]
                self.assertEqual((row["state"], row["moved"]), ("runs again", ["other.py"]))

    def test_the_runner_of_each_kind(self):
        live, gpu = ROOT / "results" / "live", ROOT / "results" / "gpu"
        self.assertEqual(carry.runner(live, "PGBENCH_SERVICE"), "tools/run_pgbench.py")
        self.assertEqual(carry.runner(gpu, "A10_CAP_ABC"), carry.GPU_RUNNER)
        self.assertEqual(carry.runner(live, "KAI_4W_BARE"), carry.KUBERNETES_RUNNER)


if __name__ == "__main__":
    unittest.main()
