# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The injection grid (tools/injection_grid.py, results/injection_grid): the Python's 500 injections through every organism and
every governor at 1, 10, 100 and 500 runs × 1, 10, 100 and 500 organisms stacked (the founder's order of 25 October).

The stacking wraps inside the one batch; every gauge is read per muscle, so two ways on the same muscles read what they read in
counts and a governor's way is read like for like; the shards deal out every body once; the readings carry their run count's
words; and the record, when one is written, re-hashes to its own digest, names a batch the Python ran (and the C++ engine ran the
same), and every cell's mean recomputes from its runs' means as the live benchmark engine's page recomputes it."""
import json
import math
import unittest
from pathlib import Path

import numpy as np

import tools.injection_grid as T
from tools.readings import HIGHER, LOWER

ROOT = Path(__file__).resolve().parents[1]


def page_series(rec, org, way):
    """The page's igSeries: every run's means of one way on one organism, per muscle, a governor's body joined muscle for muscle."""
    M, no = rec["means"], next(o["muscles"] for o in rec["organisms"] if o["key"] == org)
    omni = way == "on_native" or way.startswith("omni_gov:")
    base = np.array(M["org"][org]["on_native" if omni else "native"], dtype=np.float64)
    if way in ("native", "on_native"):
        base[:, 1:] /= no
        return base
    g = way.split(":")[1]
    gs = np.array(M["gov"][g]["on_native" if omni else "native"], dtype=np.float64)
    ng = next(x["muscles"] for x in rec["governors"] if x["key"] == g)
    out = (base + gs) / (no + ng)
    out[:, 0] = (no * base[:, 0] + ng * gs[:, 0]) / (no + ng)
    return out


def page_stack(a, m):
    """The page's igStack: run k the mean of the copies on injections k ... k + m − 1 (mod the batch)."""
    n = len(a)
    ext = np.concatenate([a] * (-(-(n + m - 1) // n)))[:n + m - 1]
    cs = np.concatenate([np.zeros((1, a.shape[1])), np.cumsum(ext, axis=0)])
    return (cs[m:m + n] - cs[:n]) / m


class Stacking(unittest.TestCase):
    def test_copies_wrap_inside_the_batch(self):
        rng = np.random.default_rng(3)
        a = rng.normal(size=(5, 3, 7))
        s = T.stacked(a, 7)                                # more copies than injections: the batch wraps
        for k in range(5):
            want = np.mean([a[(k + c) % 5] for c in range(7)], axis=0)
            np.testing.assert_allclose(s[k], want, rtol=1e-12, atol=1e-12)

    def test_one_copy_is_the_run_itself(self):
        a = np.random.default_rng(4).normal(size=(6, 3, 4))
        np.testing.assert_allclose(T.stacked(a, 1), a, atol=1e-12)


class PerMuscle(unittest.TestCase):
    def test_two_ways_on_the_same_muscles_read_the_same_per_muscle_as_in_counts(self):
        rng = np.random.default_rng(5)
        x = np.abs(rng.normal(10, 1, size=(4, 3, 240)))
        y = x * 1.07
        raw = T.run_changes(x, y)[0]
        pm = T.run_changes(T.per_muscle(x, 37), T.per_muscle(y, 37))[0]
        np.testing.assert_allclose(raw, pm, rtol=1e-9)

    def test_a_governor_joined_muscle_for_muscle(self):
        org = np.array([[[1.0], [6.0], [300.0]]])
        gov = np.array([[[2.0], [1.0], [20.0]]])
        j = T.joined(org, gov, 3, 1)                       # three organism muscles, one governor muscle
        np.testing.assert_allclose(j[0, :, 0], [(3 * 1.0 + 2.0) / 4, 7.0 / 4, 320.0 / 4])


class Shards(unittest.TestCase):
    def test_every_body_in_exactly_one_shard(self):
        T.setup()
        bodies = [("org", k) for k in T.ORG_ROWS] + [("gov", k) for k in T.GOV_ROWS]
        got = [b for i in range(1, 9) for b in T.shard_of(bodies, (i, 8))]
        self.assertEqual(sorted(got), sorted(bodies))
        self.assertEqual(len(got), len(set(got)))
        self.assertEqual(len(T.GOV_ROWS), 14)              # the fourteen governors and orchestrators the founder named


class Readings(unittest.TestCase):
    def test_the_words_carry_the_run_count(self):
        rel = np.array([0.02] * 10)
        text, word = T.cell_reading(rel, rel - 0.005, rel + 0.005, np.ones(10), rel, 10, HIGHER)
        self.assertEqual(word, "GAIN")
        self.assertIn("in all 10 of our runs", text)
        text, word = T.cell_reading(rel[:1], rel[:1] - 0.005, rel[:1] + 0.005, np.ones(1), rel[:1], 1, LOWER)
        self.assertIn("our one run", text)
        self.assertNotIn("three", text)


def newest_record():
    fs = [f for f in (ROOT / "results" / "injection_grid").glob("INJECTION_GRID_*.json") if "_look_" not in f.name]
    return max(fs, key=lambda f: f.name) if fs else None


@unittest.skipUnless(newest_record(), "no injection grid record written yet")
class Record(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rec = json.loads(newest_record().read_text(encoding="utf-8"))

    def test_the_record_rehashes_to_its_digest(self):
        self.assertEqual(T.digest_of(self.rec), self.rec["cells_digest"])

    def test_the_batch_is_one_the_python_and_the_cpp_ran(self):
        b = self.rec["batch"]
        er = json.loads((ROOT / b["file"]).read_text(encoding="utf-8"))
        self.assertEqual((er["base"], er["digest"]), (b["base"], b["python_digest"]))
        self.assertEqual(b["runs"], 500)
        if b["cpp_digest"]:
            self.assertEqual(b["cpp_digest"], b["python_digest"])

    def test_every_tier_and_every_way(self):
        r = self.rec
        self.assertEqual(r["tiers"], {"runs": [1, 10, 100, 500], "copies": [1, 10, 100, 500]})
        self.assertEqual(len(r["governors"]), 14)
        for o in r["organisms"]:
            cells = r["cells"][o["key"]]
            want = 1 if o["key"] == "orchestra" else 1 + 3 * 14
            self.assertEqual(len(cells), want, o["key"])
            for p, c in cells.items():
                self.assertEqual(len(c), 16, (o["key"], p))

    def test_every_cell_recomputes_from_its_runs_as_the_page_does(self):
        r, worst = self.rec, 0.0
        for org, pairs in r["cells"].items():
            for p, cells in pairs.items():
                a, b = p.split("|")
                x, y = page_series(r, org, b), page_series(r, org, a)
                for m in T.COPIES:
                    X, Y = page_stack(x, m), page_stack(y, m)
                    rel = (Y - X) / np.where(np.abs(X) > 1e-12, np.abs(X), 1.0)
                    for n in T.RUNS:
                        for gi, g in enumerate(("work", "over", "power")):
                            worst = max(worst, abs(rel[:n, gi].mean() - cells[f"{n}x{m}"][g]["mean"]))
        self.assertLess(worst, 1e-5)

    def test_no_number_without_its_word(self):
        words = {"GAIN", "STEADY", "LOSS", "power given", "the runs disagree"}
        for org, pairs in self.rec["cells"].items():
            for p, cells in pairs.items():
                for nm, c in cells.items():
                    for g in ("work", "over", "power"):
                        self.assertIn({"EVEN": "STEADY"}.get(c[g]["word"], c[g]["word"]), words)   # the grid's tool writes the old word; the key reads it as STEADY
                        self.assertTrue(math.isfinite(c[g]["mean"]))


if __name__ == "__main__":
    unittest.main()
