# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The wiring verdicts (tools/wiring_verdicts.py): one of three words per knob, by one rule, from the tables themselves.
write where a gauge read GAIN in all three of our runs and none LOSS or power given; watch where nothing read GAIN; the
operator's choice where both did. Every word is decided by what the gauge is for, never by its sign; the older tables' words
(lower and higher, better and worse) are still read. Rows shown and not judged never count."""
import sys
import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import wiring_verdicts as wv  # noqa: E402


class TheRule(unittest.TestCase):
    def test_the_three_words(self):
        self.assertEqual(wv.verdict(3, 0), wv.WRITE)
        self.assertEqual(wv.verdict(0, 0), wv.WATCH)
        self.assertEqual(wv.verdict(0, 2), wv.WATCH)            # LOSS or power given with no GAIN: native, Omni reads
        self.assertEqual(wv.verdict(2, 1), wv.CHOICE)           # a trade is the operator's

    def test_every_reading_the_tables_use_is_classified(self):
        # the words every table uses now
        self.assertEqual(wv.classify("**GAIN in all three of our runs**"), "gain")
        self.assertEqual(wv.classify("LOSS in all three of our runs"), "loss")
        self.assertEqual(wv.classify("**power given in all three of our runs**"), "given")
        self.assertEqual(wv.classify("**LOSS in at least one of our runs**"), "loss")
        self.assertEqual(wv.classify("**GAIN or STEADY in all three of our runs**"), "gain")
        self.assertEqual(wv.classify("STEADY, no difference beyond the noise (2 of 3 runs)"), "noise")
        self.assertEqual(wv.classify("STEADY, the same"), "same")
        # the direction words of 13 October: the gauge's aim gives the word (a resource spent that rose is power given)
        self.assertEqual(wv.classify("**lower in all three of our runs**", "lower"), "gain")
        self.assertEqual(wv.classify("higher in all three of our runs", "lower"), "loss")
        self.assertEqual(wv.classify("higher in all three of our runs", "higher"), "gain")
        self.assertEqual(wv.classify("higher in all three of our runs", "spent"), "given")
        self.assertEqual(wv.classify("lower in all three of our runs", "spent"), "gain")
        self.assertEqual(wv.classify("**higher in at least one of our runs**", "never more"), "loss")
        self.assertEqual(wv.classify("lower or the same in all three of our runs", "never more"), "gain")
        with self.assertRaises(ValueError):
            wv.classify("lower in all three of our runs")             # a direction needs its gauge's aim
        # the older tables' own words, kept as written, are still read
        self.assertEqual(wv.classify("better in all three of our runs"), "gain")
        self.assertEqual(wv.classify("**WORSE in all three of our runs**"), "loss")
        self.assertEqual(wv.classify("**WORSE in all three of our runs**", "spent"), "given")
        self.assertEqual(wv.classify("no difference beyond the noise (2 of 3 runs)"), "noise")
        self.assertEqual(wv.classify("no difference beyond the noise in 1 of 3 runs"), "noise")
        self.assertEqual(wv.classify("the runs disagree"), "disagree")
        self.assertEqual(wv.classify("**the runs differ**"), "disagree")
        self.assertEqual(wv.classify("same"), "same")
        self.assertEqual(wv.classify("same (under one part in a million)"), "same")
        self.assertEqual(wv.classify("shown, not judged"), "unjudged")
        with self.assertRaises(ValueError):
            wv.classify("a reading nobody declared")

    def test_unjudged_rows_never_count(self):
        rows = {"a": {"reading": "shown, not judged", "runs": [{"native": 1.0, "omni": 2.0}]},
                "b": {"reading": "lower in all three of our runs", "aim": "lower", "runs": [{"native": 100.0, "omni": 50.0}, {"native": 100.0, "omni": 48.0}]}}
        j = wv.judge_rows(rows, {"b": "p95"})
        self.assertEqual([x[1] for x in j["gain"]], ["p95"])
        self.assertEqual(j["gain"][0][2], "-52% to -50%")
        self.assertEqual(wv.verdict(len(j["gain"]), len(wv.away_of(j))), wv.WRITE)
        self.assertEqual(wv.words("p95", "lower", "-52% to -50%"), "p95 cut 50% to 52%")
        self.assertEqual(wv.words("work", "higher", "-5%"), "work down 5.0%")
        self.assertEqual(wv.words("memory", "spent", "+215%"), "memory up 215%")

    def test_the_range_reads_one_figure_when_the_runs_agree(self):
        self.assertEqual(wv.pct_range([{"native": 2, "omni": 8}, {"native": 2, "omni": 8}]), "+300%")
        self.assertEqual(wv.pct_range([{"native": 64, "omni": 65}, {"native": 64, "omni": 66}]), "+1.6% to +3.1%")
        self.assertEqual(wv.pct_range([{"native": 0, "omni": 0}]), "")
        self.assertEqual(wv.pct_range([{"native": 0, "omni": 3}]), "from zero")

    def test_a_simulator_table_is_read_by_its_reading_column(self):
        rows = [["Gauge", "native (A)", "omni (A)", "A", "B", "C", "Reading"],
                ["energy (J)", "482.3", "478.3", "-0.82%", "-0.82%", "-0.82%", "**lower in all three of our runs**"],
                ["cycle time (s)", "8.01", "10.21", "+27.47%", "+27.47%", "+27.47%", "shown, not judged"],
                ["line heating (MWh)", "730", "736", "+0.76%", "+0.76%", "+0.80%", "**power given in all three of our runs**"],
                ["bus-steps", "0", "0", "+0.0e+00", "+0.0e+00", "+0.0e+00", "STEADY, the same"]]
        j = wv.sim_rows_judged(rows, {"energy (J)": "spent", "line heating (MWh)": "spent", "bus-steps": "never more"})
        self.assertEqual([x[1] for x in j["gain"]], ["energy"])
        self.assertEqual(j["gain"][0][2], "-0.8%")
        self.assertEqual([x[2] for x in j["given"]], ["+0.8%"])
        self.assertEqual(len(j["same"]), 1)
        self.assertEqual(wv.verdict(len(j["gain"]), len(wv.away_of(j))), wv.CHOICE)
        self.assertTrue(wv.sim_aims("V7_SWARM.md"))                    # every simulator's own gauge list gives the aims

    def test_the_labels_map_to_the_three_words(self):
        self.assertEqual(wv.LABEL_VERDICT["SUPERIOR WITHIN GUARDRAILS"], wv.WRITE)
        self.assertEqual(wv.LABEL_VERDICT["ENERGY IMPROVEMENT WITH SERVICE TRADEOFF"], wv.CHOICE)
        self.assertEqual(wv.LABEL_VERDICT["SERVICE IMPROVEMENT WITH ENERGY TRADEOFF"], wv.CHOICE)
        for lab in ("NONINFERIOR / INCONCLUSIVE", "NOT ESTABLISHED"):
            self.assertEqual(wv.LABEL_VERDICT[lab], wv.WATCH)


class TheRepository(unittest.TestCase):
    def test_the_published_page_is_what_the_tables_give(self):
        self.assertEqual(wv.main(check=True), 0)

    def test_every_counted_case_has_one_of_the_three_words_and_the_counts_add_up(self):
        index = wv.load_index()
        real = wv.real_stacks(index)
        self.assertTrue(real)
        for x in real:
            self.assertIn(x["verdict"], (wv.WRITE, wv.WATCH, wv.CHOICE))
            self.assertEqual(x["verdict"], wv.verdict(len(x["judged"]["gain"]), len(wv.away_of(x["judged"]))))
        w, c, wa = wv.count(real)
        self.assertEqual(w + c + wa, sum(1 for x in real if x["counted"]))
        mus = wv.muscles()
        n = sum(1 for _ in csv.DictReader((wv.ROOT / "realms" / "catalog_v5.csv").open()))   # every muscle of the catalog that stands
        self.assertEqual(len(mus), n)
        self.assertEqual(sum(wv.count(mus)), n)
        for x in mus:
            self.assertEqual(x["verdict"], wv.v5_verdict(x["label"]))      # the verdict by rule, from the label over every load
            if x["label"] == wv.SAME and x["writes"] == 0:
                self.assertIn("wrote nothing", x["why"])


if __name__ == "__main__":
    unittest.main()
