# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The orchestra, the eighth organism (tools/run_orchestra.py): each governor the founder named is a body of its own made
of the catalog muscles that stand for its knobs (tools/governors_page.py, CATALOG), the orchestra holds every one of them
once, and the committed table was run on committed code with that same mapping."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.run_orchestra as O
from tools.governors_page import CATALOG, GOVERNORS

RESULT = ROOT / "results" / "orchestra"


def bodies():
    return O.bodies(O.R.catalog(str(ROOT / "realms" / "catalog_v5.csv")))


class Orchestra(unittest.TestCase):
    def test_every_governor_a_body_and_the_orchestra_every_muscle_once(self):
        g = bodies()
        self.assertEqual(list(g), [s for s, *_ in GOVERNORS] + [O.ORCHESTRA])
        for slug, (fid, muscles) in CATALOG.items():
            self.assertEqual([r["muscle"] for r in g[slug]], muscles)
            self.assertTrue(all(r["family_id"] == str(fid) for r in g[slug]))
        ids = [r["muscle_id"] for r in g[O.ORCHESTRA]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {r["muscle_id"] for slug in CATALOG for r in g[slug]})

    def test_the_committed_table_is_this_mapping_on_committed_code(self):
        d = json.loads((RESULT / "ORCHESTRA.json").read_text())
        self.assertEqual(d["run"]["bodies"], {b: [r["muscle_id"] for r in rs] for b, rs in bodies().items()})
        self.assertFalse(d["run"]["dirty"])
        self.assertEqual(d["run"]["seeds"], O.R.PREREG_SEEDS)
        self.assertEqual(set(d["bodies"]), set(O.R.ORGANISM_LOADS))
        for load in O.R.ORGANISM_LOADS:
            self.assertEqual(set(d["bodies"][load]), set(d["run"]["bodies"]))
            self.assertTrue(all(o["valid"] for o in d["bodies"][load].values()))

    def test_the_table_carries_the_notice_and_every_governor(self):
        text = (RESULT / "ORCHESTRA.md").read_text()
        self.assertIn("www.omni-compass.com", text.splitlines()[2])
        self.assertIn("www.omni-compass.com", text.rstrip().splitlines()[-1])
        for _, name, *_ in GOVERNORS:
            self.assertIn(name, text)


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
