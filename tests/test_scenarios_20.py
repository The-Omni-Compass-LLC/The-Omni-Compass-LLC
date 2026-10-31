# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The twenty scenarios (tools/scenarios_20.py, results/scenarios/SCENARIOS_20.json): ten organisms in the founder's order, each
native and with Omni-Compass on native, and no third way (the founder's order of 25 October: Omni-Compass is never by
itself); every judged cell carries a word of the key; the record was run on committed code; and a small organism run twice
gives the same record, its recording changing nothing in the harness's own run."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.scenarios_20 as S  # noqa: E402
from tools.readings import GAIN, STEADY, LOSS, GIVEN, DISAGREE, SHOWN, SHOWN_AIM, HIGHER, LOWER, SPENT, OWN_RUNS, classify, aim  # noqa: E402

RESULT = ROOT / "results" / "scenarios"
WORDS = {GAIN, STEADY, LOSS, GIVEN, DISAGREE}


def record():
    return json.loads((RESULT / "SCENARIOS_20.json").read_text(encoding="utf-8"))


class Shape(unittest.TestCase):
    def test_ten_organisms_two_arms_in_the_founders_order(self):
        d = record()
        self.assertEqual([o["key"] for o in d["organisms"]], [k for k, *_ in S.ORGANISMS])
        self.assertEqual([o["no"] for o in d["organisms"]], list(range(1, 11)))
        self.assertEqual(S.ARMS, ("native", "on_native"))
        self.assertEqual(len(d["organisms"]) * len(S.ARMS), 20)
        self.assertNotIn("direct", json.dumps(d["arms"]) + json.dumps(d["pairs"]))
        for o in d["organisms"]:
            self.assertEqual(set(o["arms"]), set(S.ARMS), o["key"])
            self.assertEqual(set(o["readings"]), set(S.PAIR_KEY.values()), o["key"])
            self.assertTrue(o["class"].startswith("S"), o["key"])

    def test_every_judged_cell_has_a_word_of_the_key(self):
        for o in record()["organisms"][:9]:
            for arm in S.ARMS:
                self.assertEqual(set(o["arms"][arm]["runs"]), set(S.RUNS), (o["key"], arm))
                for x in S.RUNS:
                    self.assertEqual(set(o["arms"][arm]["runs"][x]["gauges"]), set(S.GAUGES))
            for pk, rd in o["readings"].items():
                self.assertEqual(set(rd["gauges"]), set(S.GAUGES))
                for key, g in rd["gauges"].items():
                    if g["aim"] == SHOWN_AIM:
                        self.assertEqual(g["word"], SHOWN, (o["key"], pk, key))
                        continue
                    self.assertIn(g["word"], WORDS, (o["key"], pk, key))
                    self.assertIn(classify(g["reading"], aim(g["aim"])), {"gain", "loss", "given", "noise", "same", "disagree"})
                    self.assertEqual(set(g["runs"]), set(S.RUNS))
                    for x in S.RUNS:                    # each run's change and interval, as the key prints them: the size beside its
                        # word with no sign, the raw interval apart with its true signs (tools/readings.py by_word, interval_by_word;
                        # the referee's work order of 25 October)
                        self.assertRegex(g["runs"][x]["cell"], r"^\d+\.\d+% \(raw [+−±]\d+\.\d+% to [+−±]\d+\.\d+%\)$")
                self.assertIn(rd["runner"]["labelled"].split(" ")[0].strip(","), {GAIN, STEADY, LOSS, "INVALID"}, (o["key"], pk))

    def test_the_whole_organism_is_the_composition_of_the_real_tables(self):
        w = record()["organisms"][9]
        self.assertEqual(w["key"], S.WHOLE)
        self.assertEqual(set(w["arms"]), set(S.ARMS))
        comp = w["readings"]["on_native_vs_native"]["composition"]
        self.assertEqual(comp["state"], "composed")
        for sc in comp["scopes"].values():
            for rd in ("index", "carried"):
                for g in sc[rd]["whole"]["gauges"].values():
                    self.assertIn(g["word"], {GAIN, STEADY, LOSS, GIVEN})

    def test_run_on_committed_code_with_the_harness_records_seeds(self):
        run = record()["run"]
        self.assertEqual(run["seeds"], [3000, 3001, 3002])
        self.assertEqual(run["runs"], {"A": 3000, "B": 3001, "C": 3002})
        self.assertEqual(run["steps"], 240)
        self.assertEqual(run["load"], "climb")
        self.assertRegex(run["commit"], r"^[0-9a-f]{40}$")
        self.assertFalse(run["dirty"])
        self.assertTrue(run["engine"].startswith("omni-v"))
        live = record()["organisms"][8]
        self.assertTrue(live["export_check"])          # the harness export's own run and the run here agree decision by decision

    def test_the_page_carries_the_notice_and_every_organism(self):
        text = (RESULT / "SCENARIOS_20.md").read_text(encoding="utf-8")
        lines = text.rstrip().splitlines()
        self.assertIn("www.omni-compass.com", lines[2])
        self.assertIn("www.omni-compass.com", lines[-1])
        self.assertIn(OWN_RUNS, text)
        for _, name, _ in S.ORGANISMS:
            self.assertIn(name, text)
        self.assertNotRegex(text, r"Omni-Compass direct|by itself, the|SOLO")


class Reading(unittest.TestCase):
    def runs(self, *changes, base=100.0, half=1.0):
        return [{"base": base, "diff": c, "lo": c - half, "hi": c + half} for c in changes]

    def test_the_key_reads_by_the_gauges_aim(self):
        self.assertTrue(S.three_run(self.runs(5, 6, 7), HIGHER).strip("*").startswith("GAIN in all three"))
        self.assertTrue(S.three_run(self.runs(-5, -6, -7), HIGHER).strip("*").startswith("LOSS in all three"))
        self.assertTrue(S.three_run(self.runs(-5, -6, -7), LOWER).strip("*").startswith("GAIN in all three"))
        self.assertTrue(S.three_run(self.runs(5, 6, 7), SPENT).strip("*").startswith("power given in all three"))
        # a change of 0.5% or more shows its word, with how many runs were clear of the noise (the founder's order of 24 October)
        self.assertEqual(S.three_run(self.runs(5, 0.5, 7), HIGHER), "**GAIN by the mean of our three runs, beyond the noise in 2 of 3**")
        self.assertTrue(S.three_run(self.runs(0.3, 0.2, 0.4, half=0.1), HIGHER).startswith("STEADY, under the floor"))
        self.assertEqual(S.three_run(self.runs(5, -6, 7), HIGHER).strip("*"), DISAGREE)
        self.assertTrue(S.three_run(self.runs(0, 0, 0, half=0), HIGHER).startswith("STEADY, the same"))
        self.assertEqual(S.three_run(self.runs(5, 6, 7), SHOWN_AIM), SHOWN)


class Tiny(unittest.TestCase):
    def test_a_small_organism_reproduces_and_its_recording_changes_nothing(self):
        rows = S.organism_rows(S.R.catalog(str(ROOT / "realms" / "catalog_v5.csv")))[S.ORCHESTRA]
        a = S.organism_job((S.ORCHESTRA, rows, 3000))
        b = S.organism_job((S.ORCHESTRA, rows, 3000))
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))
        for arm in S.ARMS:
            rec, out = S.recorded_run(S.ORCHESTRA, rows, 3000, S.HARNESS_ARM[arm])
            plain = S.R.organism_run(S.ORCHESTRA, rows, 3000, S.HARNESS_ARM[arm], S.LOAD)
            self.assertEqual(out["plants"], plain["plants"], arm)
            self.assertEqual(out["writes"], plain["writes"], arm)
            self.assertEqual(len(rec["power_kw"]), S.ORGANISM_STEPS)


if __name__ == "__main__":
    unittest.main()
