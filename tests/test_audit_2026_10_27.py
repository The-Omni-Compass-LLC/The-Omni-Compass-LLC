# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The faults the audit of 27 October 2026 found, each held by a test that fails on the code before it.

1. The repository's name was written in eleven tools; after the rename every API call and link they made named the old one.
   It is written once, in tools/repo.py.
2. The benefit sheet filed a table under every engine its text named, so the drone swarms' omni-v21 table, which names
   omni-v12 as the engine before whose runs its preregistration's amendment was written, read "omni-v12 and omni-v21".
3. The three-arm record the README's answer reads (results/orchestrator/V18_THREE_ARMS_ABC.json) had no tool: it was written
   by hand. tools/three_arms_abc.py builds it from the runs' own summaries by the one key.
4. The answer at the top of the README showed Omni-Compass by itself after the founder's order of 25 October (Omni-Compass is
   never by itself), and led with an older engine's record while the engine that stands had its own tables."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools import benefit_sheet, headline, repo, three_arms_abc  # noqa: E402


class RepositoryNameWrittenOnce(unittest.TestCase):
    OLD = re.compile(r"The-Omni-Compass-LLC/The-Omni-Compass(?!-LLC)")

    def test_no_tool_or_script_names_the_repository_itself(self):
        out = subprocess.run(["git", "grep", "-nI", "-e", "The-Omni-Compass-LLC/The-Omni-Compass", "--", "*.py", "*.sh"],
                             cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
        allowed = {"tools/repo.py", "scripts/dispatch_grid.py", "tests/test_audit_2026_10_27.py"}
        stray = [ln for ln in out if ln.split(":", 1)[0] not in allowed]
        self.assertEqual(stray, [], "the repository's name belongs in tools/repo.py alone")

    def test_the_name_is_the_new_one(self):
        self.assertIsNone(self.OLD.search(repo.HOME))
        self.assertTrue(repo.URL.endswith(repo.HOME))


class StatedEngine(unittest.TestCase):
    def test_a_table_is_filed_under_the_engine_its_run_table_states(self):
        with tempfile.TemporaryDirectory() as t:
            md = Path(t) / "V21_X.md"
            md.write_text("Amendment 2 was written before omni-v12's runs.\n\n| Run | GitHub run | Commit | Engine |\n"
                          "|---|---|---|---|\n| A | 1 | abc | omni-v21 (digest x) |\n| B | 2 | abc | omni-v21 (digest x) |\n")
            self.assertEqual(benefit_sheet.stated_engines(md), {21})

    def test_the_json_engine_field_when_no_run_table(self):
        with tempfile.TemporaryDirectory() as t:
            md = Path(t) / "V21_Y.md"
            md.write_text("A table that names omni-v12 in passing.\n")
            md.with_suffix(".json").write_text(json.dumps({"engine": "omni-v21 (digest b658f05d43c1e602, 63 files)"}))
            self.assertEqual(benefit_sheet.stated_engines(md), {21})

    def test_the_swarm_row_reads_one_engine(self):
        rows = json.loads((ROOT / "results" / "BENEFIT_SHEET.json").read_text())["rows"]
        swarm = [r for r in rows if r["file"].endswith("V21_SWARM.md")]
        self.assertTrue(swarm)
        self.assertEqual(swarm[0]["engine"], "omni-v21")


def summary(letter, rels):
    """A showing's summary.json with every pair and gauge moving by the given relative changes, intervals clear of zero."""
    readings = {}
    for pair in ("Omni on native against native", "Omni direct against native"):
        for g, rel in rels.items():
            lo, hi = (rel * 0.5, rel * 1.5) if rel > 0 else (rel * 1.5, rel * 0.5)
            readings[f"{pair}: {g}"] = {"mean": rel * 100, "lo": lo * 100, "hi": hi * 100, "rel": rel, "word": "x"}
    arm = {"answered": 100, "failed": 0, "wrong": 0, "p95_ms": 200.0, "machine_min": 45.0, "unit_min": 60.0}
    return {"summary": {"yardstick": arm, "omni_native": arm, "omni": arm}, "readings": readings}


class ThreeArms(unittest.TestCase):
    def build(self, rels_by_run):
        with tempfile.TemporaryDirectory() as t:
            dirs = []
            for letter, rels in rels_by_run.items():
                d = Path(t) / f"run-{letter}" / f"orchestrator-{letter}-busy-1{ord(letter)}"
                (d / "omni").mkdir(parents=True)
                (d / "summary.json").write_text(json.dumps(summary(letter, rels)))
                (d / "omni" / "meta.json").write_text(json.dumps({"steps": list(range(18)), "step_s": 25.0}))
                dirs.append(str(d.parent))
            with mock.patch.object(three_arms_abc, "commit_and_engine", return_value=("a" * 40, "omni-v21 (digest d, 63 files)")):
                return three_arms_abc.build(dirs)

    def test_every_run_the_same_way_reads_in_all_three(self):
        rec = self.build({k: {"requests": 0.06, "p95_ms": -0.09, "machines": -0.02, "units": 0.10} for k in "ABC"})
        row = {(r["pair"], r["gauge"]): r for r in rec["rows"]}
        self.assertEqual(row[("Omni on native against native", "requests")]["reading"], "GAIN in all three of our runs")
        self.assertEqual(row[("Omni on native against native", "p95_ms")]["reading"], "GAIN in all three of our runs")
        self.assertEqual(row[("Omni on native against native", "units")]["reading"], "power given in all three of our runs")
        self.assertIn("the full form: 18 steps of 25 s", rec["what"])

    def test_under_half_a_percent_reads_even(self):
        rec = self.build({k: {"requests": 0.001, "p95_ms": -0.002, "machines": 0.0, "units": 0.003} for k in "ABC"})
        words = {r["gauge"]: r["reading"] for r in rec["rows"] if r["pair"] == "Omni on native against native"}
        self.assertTrue(all(w.startswith("STEADY") for w in words.values()), words)

    def test_the_published_v18_record_is_the_tools(self):
        """The hand-written record, rebuilt from its own runs, byte for byte (tools/reproduce.py --table V18_THREE_ARMS_ABC
        against the raw branch); here, its every reading follows from its own per-run numbers by the one key."""
        rec = json.loads((ROOT / "results" / "orchestrator" / "V18_THREE_ARMS_ABC.json").read_text())
        from tools import readings as K
        for r in rec["rows"]:
            aim = three_arms_abc.GAUGES[r["gauge"]][1]
            paired = [{"native": 1.0, "diff": v["rel"], "ci95": [v["lo"], v["hi"]]} for v in r["runs"].values()]
            self.assertEqual(K.three_run_reading(paired, aim).replace("**", ""), r["reading"], (r["pair"], r["gauge"]))


class TheAnswer(unittest.TestCase):
    def setUp(self):
        self.m = headline.model()
        self.md = headline.markdown(self.m)

    def test_two_sides_only(self):
        self.assertNotIn("**Omni-Compass direct**", self.md)
        self.assertEqual([s["name"] for s in self.m["scen"]], ["Omni-Compass on top of native"])

    def test_it_leads_with_the_engine_that_stands(self):
        stands = headline.the_engine_that_stands()
        lead = self.md.split("\n")[4]
        self.assertIn(f"the engine that stands ({stands})", lead)

    def test_every_count_is_the_sheets(self):
        st = self.m["standing"]
        self.assertEqual(sum(n for _, n in st["words"]), st["on"])
        self.assertEqual(st["on"] + st["older"], st["bench"])


if __name__ == "__main__":
    unittest.main()
