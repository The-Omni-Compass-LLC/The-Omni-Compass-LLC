# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine coverage (tools/engine_coverage.py) traces every file tools/function_tests.py runs: each one is started as
`coverage run --append`, never as `coverage --append`, which coverage refuses, leaving the file untraced and the page
short of the tests it names (found on 19 October: 51% read where the suite runs 81%)."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.engine_coverage as EC


class FunctionTestsTraced(unittest.TestCase):
    def test_every_function_test_runs_under_coverage_run_append(self):
        calls = []

        def standin(cmd, *a, **kw):
            calls.append(list(cmd))
            if "--list" in cmd:
                return subprocess.CompletedProcess(cmd, 0, "main      tests/test_one.py\nfunctions tests/test_two.py\n", "")
            if "json" in cmd:
                Path(cmd[cmd.index("-o") + 1]).write_text(json.dumps({"files": {}}))
            return subprocess.CompletedProcess(cmd, 0, "", "")

        with mock.patch.object(EC, "engine_manifest", return_value=("omni-v12", ["omnicompass/core.py"])), \
                mock.patch.object(EC.subprocess, "run", side_effect=standin):
            rec = EC.measure()
        ones = [c for c in calls if "--one" in c]
        self.assertEqual([c[c.index("--one") + 1] for c in ones], ["tests/test_one.py", "tests/test_two.py"])
        for c in ones:
            self.assertEqual(c[:5], [sys.executable, "-m", "coverage", "run", "--append"], c)
        self.assertEqual(rec["engine"], "omni-v12")

    def test_a_refused_command_stops_the_measurement(self):
        def standin(cmd, *a, **kw):
            if "--list" in cmd:
                return subprocess.CompletedProcess(cmd, 0, "main      tests/test_one.py\n", "")
            if "--one" in cmd:
                return subprocess.CompletedProcess(cmd, 2, "", "no such option: --append")
            return subprocess.CompletedProcess(cmd, 0, "", "")

        with mock.patch.object(EC, "engine_manifest", return_value=("omni-v12", ["omnicompass/core.py"])), \
                mock.patch.object(EC.subprocess, "run", side_effect=standin):
            with self.assertRaises(SystemExit):
                EC.measure()


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
