# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Heaviest hitters first (the founder's order of 1 November, night): every list of the catalog's 1,107 muscles, in full or
condensed, is ordered by one declared rule (tools/heavy_hitters.py), heaviest hitter first down to the last, in the four
realms the muscles live in, each muscle once under its home realm: the catalog page, the organism page and the live engine's
glossary."""
import csv
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import heavy_hitters as HH  # noqa: E402

ROWS = list(csv.DictReader(open(ROOT / "realms" / "catalog_v5.csv", encoding="utf-8")))


def entry(label, vn=0, vm=0, steps=7200, line=None, work=0.0):
    loads = {"normal": {"viol_native": vn, "viol_max": vm, "steps": steps, "summary": {"work": [work, work, work]}},
             "line": {"viol_native": 0, "viol_max": 0, "steps": steps, "summary": {"work": [work, work, work]},
                      "line": line}}
    return {"label": label, "loads": loads}


class TheRule(unittest.TestCase):
    def test_the_tiers_come_in_the_declared_order(self):
        misses = HH.hit_of(entry("FEWER MISSES", vn=100, vm=10))
        line = HH.hit_of(entry("FASTER", line=[40.0, 10.0, 0, 0]))
        work = HH.hit_of(entry("MORE WORK", work=0.02))
        same = HH.hit_of(entry("SAME AS NATIVE"))
        limit = HH.hit_of(entry("AT ITS LIMIT ON NATIVE", vn=5, vm=0))
        self.assertEqual([x.tier for x in (misses, line, work, same, limit)], [1, 2, 3, 4, 5])
        self.assertAlmostEqual(misses.value, 100.0 * 90 / 14400)          # of all its decisions, both loads
        self.assertAlmostEqual(line.value, 75.0)                           # the line cleared 75% sooner
        self.assertAlmostEqual(work.value, 2.0)
        self.assertEqual((same.value, limit.value), (0.0, 0.0))            # no hit: Omni-Compass wrote nothing, or nothing moved

    def test_a_bigger_share_of_the_muscles_life_hits_harder(self):
        small = HH.hit_of(entry("FEWER MISSES", vn=8, vm=0, steps=7200))   # every miss gone, but eight of them
        big = HH.hit_of(entry("FEWER MISSES", vn=2000, vm=1100))          # 900 decisions taken back
        rows = [{"muscle_id": "1"}, {"muscle_id": "2"}]
        got = HH.order(rows, {"1": small, "2": big})
        self.assertEqual([r["muscle_id"] for r in got], ["2", "1"])

    def test_the_order_is_total_and_holds_every_muscle_once(self):
        by = HH.by_realm(ROWS)
        self.assertEqual(list(by), list(HH.REALMS))
        ids = [r["muscle_id"] for rs in by.values() for r in rs]
        self.assertEqual(len(ids), 1107)
        self.assertEqual(len(set(ids)), 1107)
        for k, rs in by.items():
            keys = [HH.key(r) for r in rs]
            self.assertEqual(keys, sorted(keys), k)
            self.assertTrue(all(r["realm"] == k for r in rs), k)

    def test_the_record_it_reads_names_its_engine(self):
        run = HH.record_run()
        self.assertTrue(run["engine"].startswith("omni-v") and run["started"] and run["seeds"] > 0)
        self.assertIn(run["engine"], HH.rule_words())


class ThePages(unittest.TestCase):
    def test_the_catalog_page(self):
        self.assertEqual(HH.check(ROOT / "docs" / "MUSCLE_CATALOG.md", ROWS), [])

    def test_the_organism_page(self):
        text = (ROOT / "docs" / "REALM_MUSCLES.md").read_text(encoding="utf-8")
        name = {r["muscle_id"]: r["muscle"] for r in ROWS}
        for k, rs in HH.by_realm(ROWS).items():
            block = text.split(f"### {HH.REALMS[k]}: {len(rs)} muscles, heaviest hitter first", 1)[1].split("\n\n", 2)[1]
            got = [re.sub(r"^\d+ ", "", item).split(" [")[0] for item in block.rstrip(".").split("; ")]
            self.assertEqual(got, [name[r["muscle_id"]] for r in rs], k)

    def test_the_live_engines_glossary(self):
        g = json.loads((ROOT / "docs" / "engine" / "glossary.json").read_text())
        want = {k: [r["muscle_id"] for r in rs] for k, rs in HH.by_realm(ROWS).items()}
        self.assertEqual([x["key"] for x in g["groups"]], list(HH.REALMS))
        for x in g["groups"]:
            self.assertEqual(x["ranked"], want[x["key"]], x["key"])
            flat = [m for f in x["families"] for m in f["muscles"]]
            self.assertEqual(sorted(flat), sorted(x["ranked"]), x["key"])
            first = [next(i for i, m in enumerate(x["ranked"]) if m in f["muscles"]) for f in x["families"]]
            self.assertEqual(first, sorted(first), f"{x['key']}: a family stands where its heaviest hitter stands")
            for f in x["families"]:
                pos = [x["ranked"].index(m) for m in f["muscles"]]
                self.assertEqual(pos, sorted(pos), f"{x['key']} {f['name']}: its muscles heaviest hitter first")


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
