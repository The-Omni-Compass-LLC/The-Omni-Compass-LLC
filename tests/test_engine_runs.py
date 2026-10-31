# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Python's seeded runs and the live benchmark engine's: the record reproduces, and the page's own loop computes the same runs."""
import json
import shutil
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import tools.engine_runs as E  # noqa: E402


class EngineRuns(unittest.TestCase):
    def test_the_generator_is_the_pages(self):
        g = E.mulberry32(12345)
        self.assertEqual([round(g(), 12) for _ in range(3)], [round(x, 12) for x in (0.9797282677609473, 0.3067522644996643, 0.484205421525985)])

    def test_the_record_reproduces(self):
        recs = sorted((ROOT / "results" / "engine_runs").glob("ENGINE_RUNS_*.json"),
                      key=lambda f: (json.loads(f.read_text(encoding="utf-8")).get("written", ""), f.name))   # the newest written, as the page reads it
        self.assertTrue(recs, "no record of the engine's runs")
        rec = json.loads(recs[-1].read_text(encoding="utf-8"))
        runs = [E.one_run(k, rec["base"]) for k in range(25)]
        for a, b in zip(runs, rec["receipts"][:25]):
            for k in E.KEYS:
                va, vb = a[k], b[k]
                if isinstance(va, list):
                    self.assertTrue(all(abs(x - y) < 1e-12 for x, y in zip(va, vb)), (a["k"], k))
                else:
                    self.assertLess(abs(float(va) - float(vb)), 1e-12, (a["k"], k))
        self.assertEqual(len(rec["receipts"]), rec["runs"])
        self.assertEqual(E.digest(rec["receipts"]), rec["digest"])

    def test_the_draws_are_the_runs_input(self):
        """The injection carries every draw: the Python run on the draws is the run, and the text round-trips every number."""
        dr = E.draws(3, 20261020)
        self.assertEqual(E.run_draws(dr), E.one_run(3, 20261020))
        lines = E.injection([dr]).splitlines()
        self.assertEqual(lines[0], f"OCRUNS 1 1 {E.DECISIONS} {E.LAW_STEPS}")
        self.assertEqual(sum(1 for x in lines if x.startswith("O ")), E.DECISIONS)
        self.assertEqual([float(x) for x in lines[-2].split()[3:]], dr["inc"])

    @unittest.skipUnless((ROOT / "cpp" / "build" / "oc_engine_runs").exists(), "the C++ harness is not built (cmake -S cpp -B cpp/build)")
    def test_the_cpp_harness_computes_the_same_runs(self):
        self.assertEqual(E.cpp_check(12, 20261020, ROOT / "cpp" / "build" / "oc_engine_runs"), 0)

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_the_page_computes_the_same_runs(self):
        self.assertEqual(E.verify(ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html", 12), 0)


if __name__ == "__main__":
    unittest.main()
