# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The spine, the seventh organism (the founder's order of 16 October): the muscles every stack runs on, every one in all
four realms, run native and with Omni-Compass on top like the other six, named the same in every runner and in the grid
conductor, and in no engine file (the organisms are groupings of catalog rows made in the runners)."""
import csv
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from realms.harness import catalog, STACK, TOWER  # noqa: E402
from tools import run_realms_v5, run_scale, run_hil  # noqa: E402

CATALOG = str(ROOT / "realms" / "catalog_v5.csv")


def load(path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, ROOT / path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


class Spine(unittest.TestCase):
    def setUp(self):
        self.rows = catalog(CATALOG)
        self.spine = run_realms_v5.spine_rows(self.rows)

    def test_the_spine_is_every_muscle_in_all_four_realms(self):
        realms = set(run_realms_v5.REALMS)
        self.assertEqual({r["muscle_id"] for r in self.spine},
                         {r["muscle_id"] for r in self.rows if realms <= set(r["realms"].split(";"))})
        self.assertEqual(len(self.spine), 267)
        self.assertEqual(len({r["family"] for r in self.spine}), 13)
        for r in self.rows:                                   # no fifth realm name anywhere, so "all four" is well defined
            self.assertTrue(set(r["realms"].split(";")) <= realms, r["muscle_id"])

    def test_every_runner_names_the_seven_organisms_the_same(self):
        seven = [run_realms_v5.SPINE] + run_realms_v5.REALMS + [STACK, TOWER]
        self.assertEqual(run_realms_v5.ORGANISMS, seven)
        self.assertEqual(sorted(run_realms_v5.NAMES), sorted(seven))
        self.assertEqual(sorted(run_hil.NAMES), sorted(seven))
        self.assertEqual(sorted(v[0] for v in run_scale.ORGS.values()), sorted(seven))
        self.assertEqual(run_scale.ORGS["7"][0], run_realms_v5.SPINE)
        g = load("scripts/dispatch_grid.py")
        self.assertEqual(g.ORGS, ["1", "2", "3", "4", "5", "6", "7"])
        self.assertEqual(g.KUBE[-1], "spine")
        self.assertEqual(dict(zip(g.ORGS, g.KUBE))["7"], "spine")
        for table in (g.SEC, g.CAL, g.MEM):
            for size in g.SIZES:
                self.assertIn("7", table[size], (table, size))

    def test_the_runners_cut_the_same_spine(self):
        ids = sorted(r["muscle_id"] for r in self.spine)
        self.assertEqual(sorted(r["muscle_id"] for r in run_scale.rows_for("spine", 1, CATALOG)), ids)
        self.assertEqual(sorted(r["muscle_id"] for r in run_hil.groups(1)["spine"]), ids)
        self.assertEqual(len(run_scale.rows_for("spine", 3, CATALOG)), 3 * len(ids))   # copies on one clock, as every organism

    def test_the_spine_is_in_every_realm_and_touches_no_engine_file(self):
        for realm in run_realms_v5.REALMS:
            in_realm = {r["muscle_id"] for r in run_scale.rows_for(realm, 1, CATALOG)}
            self.assertTrue({r["muscle_id"] for r in self.spine} <= in_realm, realm)
        fingerprinted = (ROOT / "realms" / "harness.py").read_text().lower()
        self.assertNotIn("spine", fingerprinted)          # the fingerprinted harness names no seventh organism: the runners do

    def test_the_catalog_page_lists_the_spine_first(self):
        realm_muscles = load("tools/realm_muscles.py")
        L, n = realm_muscles.build(list(csv.DictReader(open(CATALOG, encoding="utf-8"))))
        self.assertEqual(n, 267)
        text = "\n".join(L)
        self.assertIn("## The seven organisms", text)
        self.assertLess(text.index("| The spine | `spine` (7) | 267 |"), text.index("| Compute / AI / Cloud | `compute_ai_cloud` (1) |"))
        self.assertIn("## Organism 7: the spine, 267 muscles", text)


if __name__ == "__main__":
    unittest.main()
