# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The pages a person would have been sent (tools/pages.py): the bad minute is the oversight line's alert minute exactly, the
page rule is the one written before the first count, every run read reproduces its own table, and the page is its record's."""
import json
import math
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import pages as P  # noqa: E402

REC = ROOT / "results" / "OVERSIGHT_PAGES.json"


def csv(rows):
    return "elapsed_seconds,latency_ms,ok\n" + "\n".join(f"{t},{ms},{ok}" for t, ms, ok in rows) + "\n"


class Rule(unittest.TestCase):
    def test_a_bad_minute_is_the_alert_minute(self):
        # minute 0: 19 fast and 1 slow (the 95th percentile by nearest rank is the 19th of 20: fast); minute 1: 2 slow in 20
        # (the 19th is slow: bad); minute 2: a failed request counts over the line; minute 3 past the window's end is dropped
        rows = [(i * 0.1, 100, 1) for i in range(19)] + [(1.9, 900, 1)]
        rows += [(60 + i * 0.1, 100, 1) for i in range(18)] + [(61.8, 900, 1), (61.9, 900, 1)]
        rows += [(120.0, 100, 1), (120.5, "", 0)]
        rows += [(180.0, 900, 1)]
        self.assertEqual(P.bad_minutes(csv(rows), "1000", "1180"), [False, True, True])

    def test_a_minute_without_a_sample_is_clean(self):
        self.assertEqual(P.bad_minutes(csv([(0.5, 900, 1), (130, 900, 1)]), "0", "180"), [True, False, True])

    def test_the_page_rule(self):
        B, G = True, False
        self.assertEqual(P.pages([G, B, B, G, G, G, G, B], 1, 5), 1)        # a gap of 4 clean minutes keeps one page open
        self.assertEqual(P.pages([B, G, G, G, G, G, B], 1, 5), 2)           # 5 clean minutes close it; the next bad opens another
        self.assertEqual(P.pages([B, G, B, G, B], 2, 5), 0)                 # FOR 2: no two bad minutes in a row, no page
        self.assertEqual(P.pages([B, B, G, G, G, G, G, B, B], 2, 5), 2)
        self.assertEqual(P.pages([B] * 30, 1, 5), 1)
        self.assertEqual(P.pages([], 1, 5), 0)

    def test_the_rule_is_the_preregistered_one(self):
        text = (ROOT / P.PREREG).read_text(encoding="utf-8")
        self.assertEqual(P.PRIMARY, (1, 5))
        self.assertIn("`FOR` = 1 minute", text)
        self.assertIn("`RESET` = 5 minutes", text)
        self.assertEqual(set(P.RULES), {(h, r) for h in (1, 2, 5) for r in (5, 15)})
        self.assertEqual(P.RULES[0], P.PRIMARY)

    def test_paired_interval_on_the_student_t(self):
        p = P.paired([3, 4, 5, 4], [2, 3, 3, 3])
        self.assertAlmostEqual(p["diff"], -1.25)
        sd = math.sqrt(sum((x + 1.25) ** 2 for x in (-1, -1, -2, -1)) / 3)
        h = P.t95(3) * sd / 2
        self.assertAlmostEqual(p["ci95"][0], -1.25 - h)
        self.assertAlmostEqual(p["ci95"][1], -1.25 + h)


@unittest.skipUnless(REC.exists(), "no pages record yet")
class Record(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rec = json.loads(REC.read_text(encoding="utf-8"))

    def test_every_run_read_reproduces_its_table(self):
        n = 0
        for t in self.rec["tests"]:
            d = json.loads((ROOT / t["file"]).read_text(encoding="utf-8"))
            R = d["rows"]
            printed = R[next(k for k in R if k.startswith(P.oversight.ALERT))]["runs"]
            for k, r in enumerate(t["runs"]):
                if not r["reps"]:
                    self.assertIn("left out", r["check"])
                    continue
                a = P.paired([x["native"]["alert_minutes"] for x in r["reps"]], [x["omni"]["alert_minutes"] for x in r["reps"]])
                self.assertAlmostEqual(a["native"], printed[k]["native"], delta=0.05 + 1e-9, msg=f"{t['file']} run {k}")
                self.assertAlmostEqual(a["omni"], printed[k]["omni"], delta=0.05 + 1e-9, msg=f"{t['file']} run {k}")
                for x, y in zip(a["ci95"], printed[k]["ci95"]):
                    self.assertAlmostEqual(x, y, delta=1e-6)
                n += 1
        self.assertGreater(n, 0)

    def test_a_page_never_without_a_bad_minute(self):
        for t in self.rec["tests"]:
            for r in t["runs"]:
                for x in r["reps"]:
                    for arm in ("native", "omni"):
                        g = x[arm]
                        for key, n in g["pages"].items():
                            self.assertLessEqual(n, g["alert_minutes"], key)
                            if g["alert_minutes"]:
                                self.assertGreaterEqual(g["pages"]["1,5"], 1)

    def test_the_page_is_its_records(self):
        self.assertEqual(P.main(["--check"]), 0)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
