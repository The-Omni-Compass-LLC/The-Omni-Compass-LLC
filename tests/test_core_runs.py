# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The core's Monte Carlo from the jump generator: every record reproduces its digest, and the live benchmark engine's port of the core gives the same."""
import json
import shutil
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import tools.core_runs as R  # noqa: E402
from omnicompass import core as C  # noqa: E402


class CoreRuns(unittest.TestCase):
    def test_the_draws_are_the_ranges(self):
        """Run k's state and parameters come from its own stream, inside the ranges benchmarks/core_evidence.py draws."""
        for k in range(20):
            seed, x0, p = R.draw(k, 20261024)
            self.assertEqual(seed, (20261024 + k * 0x9E3779B9) % 2 ** 32)
            for v, (lo, hi) in zip(x0.as_tuple(), R.STATE_RANGES):
                self.assertTrue(lo <= v <= hi)
            for name, (lo, hi) in C.PARAMETER_RANGES.items():
                self.assertTrue(lo <= getattr(p, name) <= hi, name)
        self.assertEqual(R.draw(3, 7)[1], R.draw(3, 7)[1])

    def test_a_run_is_the_core(self):
        """Each way of a run is omnicompass/core.simulate itself, its convey and cert steps as the core counts them."""
        r = R.one(0, 20261024)
        seed, x0, p = R.draw(0, 20261024)
        s = C.simulate(x0, p)
        self.assertEqual(r["controlled"]["U"], [float(u) for u in s.U_hist])
        self.assertEqual(r["controlled"]["convey"], s.convey_confirm if s.convey else 0)
        self.assertEqual(len(r["uncontrolled"]["U"]), C.MACRO_STEPS + 1)
        self.assertEqual(R.canonical([r]).count("\n") + 1, len(R.WAYS))

    def test_every_record_reproduces(self):
        """Every record, on the engine's own ranges or a system of its own (its ranges in the record), gives its digest and counts again."""
        recs = sorted((ROOT / "results" / "core_runs").glob("CORE_RUNS_*.json"))
        self.assertTrue(recs, "no record of the core's Monte Carlo")
        for f in recs:
            rec = json.loads(f.read_text(encoding="utf-8"))
            system = R.load_system(json.dumps({k: rec["system"][k] for k in ("name", "about", "state", "params")}) if "system" in rec else "")
            runs = [R.one(k, rec["base"], system) for k in range(rec["runs"])]
            self.assertEqual(R.digest(runs), rec["digest"], f.name)
            self.assertEqual(R.summary(runs), rec["summary"], f.name)

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_the_pages_port_is_the_pythons(self):
        page = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
        self.assertEqual(R.verify(page, 60, 1369407155), 0)
        self.assertEqual(R.verify(page, 60, 1369407155, R.load_system(str(ROOT / "systems" / "example_heavy_swing.json"))), 0)

    def test_a_system_is_numbers_only(self):
        """Your own system: ranges read and checked, unknown names and bad ranges refused, the rest the engine's own, the draws' order kept."""
        s = R.load_system('{"name": "my stack", "state": {"U": [-0.5, 0.5]}, "params": {"mu": 3, "E_max": [1, 2]}}')
        self.assertEqual(s["slug"], "my-stack")
        self.assertEqual(s["state"][1], [-0.5, 0.5])
        self.assertEqual(dict((n, [lo, hi]) for n, lo, hi in s["params"])["mu"], [3.0, 3.0])
        self.assertEqual([n for n, _, _ in s["params"]], list(C.PARAMETER_RANGES))
        self.assertEqual(R.load_system("")["state"], [list(r) for r in R.STATE_RANGES])
        for bad in ('{"name": "x", "params": {"bogus": 1}}', '{"name": "x", "state": {"U": [2, 1]}}', '{"name": "", "state": {}}',
                    '{"name": "x", "run": "rm -rf /"}', '{"name": "x", "params": {"mu": [1e9, 1e10]}}', '[1, 2]', '{"name": "x", "params": {"mu": "3"}}'):
            with self.assertRaises(ValueError, msg=bad):
                R.load_system(bad)
        seed, x0, p = R.draw(0, 7, s)
        self.assertTrue(-0.5 <= x0.U <= 0.5 and p.mu == 3.0 and 1 <= p.E_max <= 2)
        self.assertEqual(seed, R.draw(0, 7)[0])

    def test_every_system_file_reads(self):
        files = sorted((ROOT / "systems").glob("*.json"))
        self.assertTrue(files)
        for f in files:
            self.assertTrue(R.load_system(str(f))["slug"], f.name)

    @unittest.skipUnless((ROOT / "cpp" / "build" / "oc_core_runs").exists(), "the C++ harness is not built (cmake --build cpp/build --target oc_core_runs)")
    def test_the_cpp_twin_is_the_pythons(self):
        self.assertEqual(R.cpp_check(40, 1369407155, None, ROOT / "cpp" / "build" / "oc_core_runs"), 0)

    def test_the_record_carries_the_cpp(self):
        rec = json.loads((ROOT / "results" / "core_runs" / "CORE_RUNS_500_1369407155.json").read_text(encoding="utf-8"))
        self.assertTrue(rec["cpp"]["same"])
        self.assertEqual(rec["cpp"]["digest"], rec["digest"])


if __name__ == "__main__":
    unittest.main()
