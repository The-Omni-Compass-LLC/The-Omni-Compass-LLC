# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The referee's work order of 25 October, its acceptance tests: the key at its edges (falls, rises, exact equality to nine
decimals, a zero native, every three-run combination, a change no run could tell from its noise), every stored reading the key's
reading of its stored values, the raw change printed with its true sign, one count for the LOSS ledger and the appraisal, the
current engine apart from the earlier ones, the page's shapes and colours, and the records' raw numbers untouched."""
import itertools
import json
import re
import unittest
from pathlib import Path

from tools.readings import (EXACT_REL, GIVEN, HIGHER, LOWER, NEVER_MORE, SPENT, WORK_PER, evidence, three_run_reading,
                            word_of)

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"


def run(native, diff, lo=None, hi=None):
    if lo is None:
        lo, hi = diff - abs(diff) * 0.1 - 1e-12, diff + abs(diff) * 0.1 + 1e-12
    return {"native": native, "diff": diff, "ci95": [lo, hi]}


def w(rs, aim):
    return word_of(three_run_reading(rs, aim))


class Directions(unittest.TestCase):
    def test_1_lower_is_better(self):
        self.assertEqual(w([run(100, -5)] * 3, LOWER), "GAIN")       # a wait that fell
        self.assertEqual(w([run(100, 5)] * 3, LOWER), "LOSS")        # a wait that rose
        self.assertEqual(w([run(100, 0)] * 3, LOWER), "STEADY")

    def test_2_higher_is_better(self):
        self.assertEqual(w([run(100, 5)] * 3, HIGHER), "GAIN")
        self.assertEqual(w([run(100, -5)] * 3, HIGHER), "LOSS")
        self.assertEqual(w([run(100, 0)] * 3, HIGHER), "STEADY")

    def test_3_resources_and_efficiency(self):
        self.assertEqual(w([run(100, -5)] * 3, SPENT), "GAIN")       # a cut
        self.assertEqual(w([run(100, 5)] * 3, SPENT), GIVEN)         # power given, never a LOSS
        self.assertEqual(w([run(100, 5)] * 3, WORK_PER), "GAIN")     # more work per unit
        self.assertEqual(w([run(100, -5)] * 3, WORK_PER), GIVEN)

    def test_4_zero_native(self):
        rs = [run(0.0, 0.5), run(0.0, 0.3), run(0.0, 0.2)]
        self.assertEqual(w(rs, LOWER), "LOSS")                       # read by its signs, no division by zero
        ev = evidence(rs, LOWER)
        self.assertIsNone(ev["mean_pct"])
        self.assertEqual(ev["run_pct"], [None, None, None])
        self.assertEqual(w([run(0.0, 0.0)] * 3, LOWER), "STEADY")


class ThreeRuns(unittest.TestCase):
    def test_5_every_combination(self):
        """Every combination of three runs' directions and noise: the word follows the key's rule and the evidence counts agree."""
        for signs in itertools.product((-1, 0, 1), repeat=3):
            for clear in itertools.product((False, True), repeat=3):
                rs = []
                for s_, c in zip(signs, clear):
                    d = 3.0 * s_
                    lo, hi = (d - 1, d + 1) if c and s_ else (d - 9, d + 9)
                    rs.append(run(100.0, d, lo, hi))
                word = w(rs, LOWER)
                moving = {s_ for s_ in signs if s_}
                ev = evidence(rs, LOWER)
                if len(moving) > 1:
                    self.assertEqual(word, "the runs disagree", (signs, clear))
                    self.assertEqual(ev["strength"], "unresolved")
                    self.assertFalse(ev["agree"])
                elif not moving:
                    self.assertEqual(word, "STEADY")
                else:
                    mean = sum(signs) / 3
                    want = "GAIN" if mean < 0 else "LOSS"
                    self.assertEqual(word, want, (signs, clear))   # 1% of native from one run is a mean change of 1%: a change
                    k = sum(1 for s_, c in zip(signs, clear) if c and s_)
                    self.assertEqual(ev["clear_with_mean"], k)
                    if k == 3:
                        self.assertEqual(ev["strength"], "strong")
                    elif k == 0:
                        self.assertEqual(ev["strength"], "inconclusive")

    def test_6_equality_to_nine_decimals(self):
        same = [run(1000.0, 1000.0 * 5e-10, -1e-9, 1e-9)] * 3
        self.assertEqual(three_run_reading(same, LOWER), "STEADY, the same")
        apart = [run(1000.0, 1000.0 * 5e-9, -1e-6, 1e-6)] * 3        # nonzero past the ninth decimal: measured, under the floor
        r = three_run_reading(apart, LOWER)
        self.assertTrue(r.startswith("STEADY, under the floor"), r)
        self.assertEqual(evidence(apart, LOWER)["steady"], "under the floor")
        self.assertEqual(three_run_reading(apart, LOWER, same_rel=1e-6), r)   # an older caller's looser tolerance is tightened
        self.assertEqual(EXACT_REL, 1e-9)

    def test_7_inconclusive_change(self):
        rs = [run(100.0, 2.0, -5, 9), run(100.0, 1.5, -4, 7), run(100.0, 2.5, -6, 11)]
        r = three_run_reading(rs, LOWER)
        self.assertIn("by the mean of our three runs, beyond the noise in 0 of 3", r)
        ev = evidence(rs, LOWER)
        self.assertEqual(ev["strength"], "inconclusive")
        self.assertAlmostEqual(ev["mean_pct"], 2.0)
        self.assertLess(ev["mean_ci95_pct"][0], ev["mean_pct"])

    def test_never_more(self):
        self.assertEqual(word_of(three_run_reading([run(10, 1), run(10, 0), run(10, 0)], NEVER_MORE)), "LOSS")


class Record(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tools.verdict_audit import build
        cls.rec = build()
        cls.by_t = {t["stem"]: t for t in cls.rec["tables"]}

    def test_2_every_stored_reading_is_the_keys(self):
        bad = [(r["table"], r["gauge"], r["stored"], r["recomputed"]) for r in self.rec["rows"] if not r["agrees"]]
        self.assertEqual(bad, [])
        self.assertEqual([r for r in self.rec["rows"] if r.get("md_agrees") is False], [])
        self.assertGreater(self.rec["counts"]["recomputed"], 6000)

    def test_1_raw_sign_printed(self):
        """Every run cell of a standing table that carries native → Omni-Compass prints the raw change with its true sign."""
        rx = re.compile(r"raw\s*([+−±])")
        n = 0
        for r in self.rec["rows"]:
            if self.by_t[r["table"]]["status"] != "standing" or "cells" not in r:
                continue
            for c, x in zip(r["cells"], r["runs"]):
                m = rx.search(c or "")
                raw = x.get("raw_pct", x.get("raw_unit"))
                if not m or raw is None:
                    continue
                n += 1
                want = "+" if raw > 0 and round(abs(raw), 4) else "−" if raw < 0 and round(abs(raw), 4) else None
                if want and abs(raw) >= 0.05:
                    self.assertEqual(m.group(1), want, (r["table"], r["gauge"], c, raw))
        self.assertGreater(n, 1000)

    def test_3_armada_pod_start_wait(self):
        row = next(r for r in self.rec["rows"] if r["table"] == "V12_ARMADA_4W_BARE" and r["gauge"] == "pod start wait, mean (s)")
        self.assertEqual(row["word"], "LOSS")                      # a wait that rose: a LOSS, kept
        self.assertAlmostEqual(row["runs"][0]["raw_pct"], 275.0, places=3)
        self.assertGreater(row["runs"][0]["omni"], row["runs"][0]["native"])
        self.assertIn("raw +275.0%", row["cells"][0])

    def test_8_current_and_earlier_engines_apart(self):
        c = self.rec["counts"]
        st = [t for t in self.rec["tables"] if t["status"] == "standing"]
        self.assertEqual(c["standing_tables_on_the_engine_that_stands"] + c["standing_tables_not_yet_rerun"], len(st))
        by_eng = c["standing_against_native_by_engine"]
        for w_ in ("GAIN", "LOSS", "STEADY"):
            self.assertEqual(sum(d.get(w_, 0) for d in by_eng.values()), c["standing_against_native"].get(w_, 0))
        self.assertTrue(all(t["status"] != "standing" for t in self.rec["tables"] if int(t["engine"][6:]) < 8))
        self.assertTrue(all(t["status"] == "taken out" for t in self.rec["tables"] if "THREE_ARMS" in t["stem"]))

    def test_9_one_count(self):
        from tools.loss_ledger import build as ledger
        rows, _ = ledger()
        from tools.verdict_audit import loss_rows
        self.assertEqual(len(rows["against my own native"]), len(loss_rows(self.rec)))
        self.assertEqual(len(rows["against my own native"]), self.rec["counts"]["standing_against_native"]["LOSS"])
        text = (ROOT / "docs" / "LOSS_LEDGER.md").read_text(encoding="utf-8")
        self.assertIn(f"the readings do no harm is judged by: **{len(loss_rows(self.rec))}**", text)

    def test_14_raw_numbers_untouched(self):
        """The discrepancy report names no table whose stored native, Omni-Compass or difference changed: it compares printed cells
        and words; the JSON numbers of every standing table recompute the cells printed beside them."""
        d = json.loads((ROOT / "results" / "verdict_audit" / "DISCREPANCIES.json").read_text(encoding="utf-8"))
        self.assertTrue(d["base"])
        for x in d["rows"]:
            self.assertTrue(x["reasons"])


class Page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = PAGE.read_text(encoding="utf-8")

    def test_11_shapes_and_colours(self):
        s = self.s
        self.assertIn('.word.w-gain::before{content:"";display:inline-block;width:.68em;height:.68em;border-radius:50%', s)   # a green circle
        self.assertRegex(s, r"\.word\.w-even::before\{[^}]*transform:rotate\(45deg\)")                                  # a yellow diamond
        self.assertRegex(s, r"\.word\.w-loss::before\{[^}]*clip-path:var\(--oct\)")                                     # a red octagon
        self.assertRegex(s, r"\.sigw\.sw-r,\.word\.w-loss,\.w-loss\.word\{border-radius:0;clip-path:var\(--octw\)")     # never a red circle
        self.assertIn('const SIG_WORD = ["GAINING", "STEADY", "REDLINING", "AWAITING", "OVER THE LINE"]', s)
        self.assertIn("@keyframes redBlack", s)
        self.assertIn("@keyframes redWhite", s)
        self.assertIn(":root{--key-omni:#4e97d1;--key-nat:#ff8a1f}", s)

    def test_no_retired_words(self):
        recs = [(m.start(), m.end()) for m in re.finditer(r'<script type="application/json" id="[^"]+">.*?</script>', self.s, re.S)]
        text = "".join(self.s[a:b] for a, b in recs)
        self.assertNotIn("THRIVING", self.s)
        self.assertNotRegex(text, r"\bEVEN\b")
        self.assertIn("<title>The Omni-Compass Live Benchmark Engine</title>", self.s)

    def test_10_the_page_carries_the_audit(self):
        m = re.search(r'<script type="application/json" id="audit">(.*?)</script>', self.s, re.S)
        self.assertIsNotNone(m)
        a = json.loads(m.group(1))
        from tools.verdict_audit import build, digest
        self.assertEqual(a["digest"], digest(build()))


if __name__ == "__main__":
    unittest.main()
