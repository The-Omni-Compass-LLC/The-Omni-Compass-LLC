# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; commercial use requires a signed paid Enterprise License.
# See LICENSE, NOTICE and DISCLOSURES.md.
"""Fail closed when the public website feed misstates the repository's measured receipts.

Run: python3 -m unittest tests/test_public_benchmark_contract.py
This checks source-to-public-contract consistency; it does not certify the underlying
experiments, their independence, statistical power, or all GPU/CPU/cloud runs.
"""
import json
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class PublicBenchmarkContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = load("results/OMNI_INDEX.json")
        cls.feed = load("results/SITE_NUMBERS.json")
        cls.bills = load("results/TWO_BILLS.json")
        cls.rows = {row["id"]: row for row in cls.feed["show"]}

    def test_website_tour_and_commercial_contract_are_traceable(self):
        """Site-copy requirements must retain valid source, scope and proposal labels."""
        alignment = (ROOT / "docs/WEBSITE_GITHUB_ALIGNMENT_CONTRACT.md").read_text(encoding="utf-8")
        proposal = (ROOT / "docs/COMMERCIAL_TERMS_PROPOSAL.md").read_text(encoding="utf-8")
        front = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
        for name in ("Homepage hero", "Ticker / animated statistics",
                     "Virtual guide", "Whitepaper / mathematics",
                     "Investor / press", "results/SITE_NUMBERS.json",
                     "results/OMNI_INDEX.json", "results/TWO_BILLS.json"):
            self.assertIn(name, alignment, name)
        self.assertIn("25% of verified, attributable net savings", proposal)
        self.assertIn("5% royalty", proposal)
        self.assertIn("extra_goodput_pct", proposal)
        self.assertIn("not an executed license", proposal)
        for name in ("docs/WEBSITE_GITHUB_ALIGNMENT_CONTRACT.md",
                     "docs/COMMERCIAL_TERMS_PROPOSAL.md"):
            self.assertIn(name, front)
        self.assertIn("Dubra Software Inc. / The Omni-Compass LLC", alignment)
        self.assertIn("Dubra Software Inc. / The Omni-Compass LLC", proposal)

    def test_major_manuals_show_current_evidence_correction(self):
        """A current Markdown manual must expose the controlled receipt addendum."""
        addendum = ROOT / "docs/audits/MANUAL_EVIDENCE_CORRIGENDUM_2026-11-09.md"
        self.assertTrue(addendum.is_file(), "dated manual correction missing")
        correction = addendum.read_text(encoding="utf-8")
        for key in ("OMNI_V26.json", "results/OMNI_INDEX.json",
                    "results/TWO_BILLS.json", "docs/ENGINE_PROOFS.md",
                    "docs/LOSS_LEDGER.md"):
            self.assertIn(key, correction)
        for path in ("docs/OMNI_COMPASS_MANUAL.md",
                     "docs/OMNI_COMPASS_OWNERS_MANUAL.md",
                     "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md"):
            with self.subTest(manual=path):
                # Check front matter only: manual bodies are large and preserve history.
                front = (ROOT / path).read_text(encoding="utf-8")[:2000]
                self.assertIn("Evidence-currency notice (9 November 2026)", front)
                self.assertGreater(front.index("Evidence-currency notice"), front.index("SPDX-License-Identifier"),
                                   "legal notice must precede the editorial correction")
                self.assertIn(
                    "audits/MANUAL_EVIDENCE_CORRIGENDUM_2026-11-09.md", front)
                self.assertIn("does not certify", front)

    def test_machine_readable_editorial_summary_tracks_current_receipts(self):
        """The crawler-facing overview may not promote an obsolete index to current."""
        guide = (ROOT / "llms.txt").read_text(encoding="utf-8")
        index_value = round(self.index["headline_pct"], 1)
        service_value = round(self.index["service_headline_pct"], 1)
        measured_versions = {
            int(re.search(r"/V(\d+)_", test["source"]).group(1))
            for test in self.index["tests"]
        }
        self.assertEqual(len(measured_versions), 1,
                         "crawler-facing index combines different engine versions")
        measured_version = next(iter(measured_versions))
        current_sentence = f"published software-only index on omni-v{measured_version}"
        self.assertIn(current_sentence, guide,
                      "crawler guide must distinguish benchmark V25 from standing engine V26")
        self.assertIn(f"+{index_value:.1f}%", guide)
        self.assertIn(f"+{service_value:.1f}%", guide)
        self.assertIn("The old omni-v21 readings", guide)
        self.assertIn("historical, not the current headline", guide)
        self.assertIn("not raw throughput increases or cloud bill savings", guide)
        self.assertIn("not a physical whole-system measurement", guide)
        self.assertIn("results/OMNI_INDEX.json", guide)

    def test_index_geometric_aggregation_reproduces_record(self):
        """Recalculate from published per-test scores without importing the index generator.

        This is a source-integrity check, not independent validation of the
        experiments or of the selection/weighting policy.
        """
        def geomean(values):
            self.assertTrue(values, "missing scored evidence")
            for value in values:
                self.assertTrue(math.isfinite(value) and value > 0,
                                f"geometric mean requires finite positive ratios: {value}")
            return math.exp(sum(math.log(v) for v in values) / len(values))

        groups = {}
        for test in self.index["tests"]:
            groups.setdefault(test["category"], []).append(test)
        self.assertEqual(set(groups), set(self.index["categories"]))
        self.assertEqual(set(groups), set(self.index["service_categories"]))
        for category, tests in groups.items():
            with self.subTest(category=category):
                ratios = [1 + t["index_pct"] / 100 for t in tests
                          if t.get("index_pct") is not None]
                service = [1 + t["service_pct"] / 100 for t in tests
                           if t.get("service_pct") is not None]
                self.assertAlmostEqual(100 * (geomean(ratios) - 1),
                                       self.index["categories"][category], places=8)
                self.assertAlmostEqual(100 * (geomean(service) - 1),
                                       self.index["service_categories"][category], places=8)
        for field, key in (("headline_pct", "categories"),
                           ("service_headline_pct", "service_categories")):
            values = [1 + self.index[key][category] / 100 for category in groups]
            self.assertAlmostEqual(100 * (geomean(values) - 1),
                                   self.index[field], places=8,
                                   msg=f"{field} is inconsistent with category scores")

    def test_index_and_kubernetes_match_generated_feed(self):
        index = self.index
        self.assertTrue(math.isfinite(index["headline_pct"]))
        self.assertTrue(math.isfinite(index["service_headline_pct"]))
        self.assertAlmostEqual(self.rows["omni_index"]["value_pct"], round(index["headline_pct"], 1))
        self.assertAlmostEqual(self.rows["work_and_speed"]["value_pct"], round(index["service_headline_pct"], 1))
        k8 = {k: v for k, v in index["categories"].items() if k.startswith("Real Kubernetes")}
        self.assertEqual(len(k8), 1, "exactly one Kubernetes category expected")
        self.assertAlmostEqual(self.rows["kubernetes"]["value_pct"], round(next(iter(k8.values())), 1))
        for key in ("omni_index", "work_and_speed", "kubernetes"):
            row = self.rows[key]
            self.assertEqual(row["cls"], "L")
            self.assertEqual(row["receipt"], "results/OMNI_INDEX.md")
            self.assertRegex(row["engine"], r"omni-v[0-9]+", "engine version missing")
            self.assertEqual(row["direction"], "up" if row["value_pct"] > 0 else "down" if row["value_pct"] < 0 else "unchanged")
            self.assertIn(f'{abs(row["value_pct"]):.1f}%', row["sentence"])

    def test_no_missing_or_model_receipt_passes_as_measurement(self):
        self.assertEqual(len(self.rows), len(self.feed["show"]), "duplicate public row IDs")
        self.assertTrue(self.rows)
        for row in self.feed["show"]:
            with self.subTest(row=row["id"]):
                self.assertIn(row["cls"], ("L", "P"), "class S is a model, not measured evidence")
                receipt = row["receipt"].split(" (")[0]
                self.assertTrue((ROOT / receipt).is_file(), f"missing receipt {receipt}")
                self.assertTrue(row.get("sentence"))
                self.assertTrue(row.get("engine"))
                self.assertNotIn("ABC_TABLE", row["receipt"])
                value = row.get("value_pct")
                if value is not None:
                    self.assertTrue(math.isfinite(value))
        self.assertFalse((ROOT / "results/ABC_TABLE.json").exists(),
                         "archived class-S model must not be exposed as measured results")
        self.assertTrue((ROOT / "docs/history/model_tables/ABC_TABLE_MODEL.json").is_file())
        unsupported = " ".join(str(row["sentence"]) for row in self.feed["show"])
        for phrase in ("47.2%", "49.9%", "12.9% bare metal", "5.3% cloud"):
            self.assertNotIn(phrase, unsupported)

    def test_losses_are_not_silently_hidden_by_positive_index(self):
        k8tests = [t for t in self.index["tests"] if t.get("category", "").startswith("Real Kubernetes")]
        losses = [t for t in k8tests if t.get("index_pct") is not None and t["index_pct"] <= -0.5]
        published = self.rows["kubernetes"].get("losses", [])
        self.assertEqual({t["source"] for t in losses}, {x["source"] for x in published})
        for item in published:
            self.assertAlmostEqual(item["value_pct"],
                                   round(next(t["index_pct"] for t in losses if t["source"] == item["source"]), 1))
        if losses:
            self.assertIn("LOSS", self.rows["kubernetes"]["sentence"])
        for t in self.index["tests"]:
            with self.subTest(source=t.get("source")):
                self.assertTrue((ROOT / t["source"]).is_file(), "index entry has no underlying JSON")
                measured_version = re.search(r"omni-v(\d+)", self.rows["omni_index"]["engine"])
                self.assertIsNotNone(measured_version, "benchmark row must identify its engine")
                self.assertRegex(t["source"], rf"/V{measured_version.group(1)}_",
                                 "index must not mix different engine versions")

    def test_gpu_and_cloud_are_not_mislabeled_v25(self):
        arms = self.feed["four_arms"]
        self.assertEqual(set(arms), {"A", "B", "C", "D"})
        self.assertEqual(arms["A"]["engine"], arms["B"]["engine"])
        self.assertEqual(arms["C"]["engine"], arms["D"]["engine"])
        self.assertEqual(arms["A"]["class"], "P")
        self.assertEqual(arms["C"]["class"], "L")
        self.assertEqual(arms["A"]["engine"], self.bills["chip"]["engine"].split(" ")[0])
        self.assertEqual(arms["C"]["engine"], self.bills["cloud"]["engine"])
        self.assertEqual(len(arms["A"]["runs"]), len(arms["B"]["runs"]))
        self.assertEqual([r["run"] for r in arms["A"]["runs"]],
                         [r["run"] for r in arms["B"]["runs"]])
        self.assertEqual(arms["C"]["repetitions"], arms["D"]["repetitions"])
        for arm in arms.values():
            self.assertTrue((ROOT / arm["receipt"].split(" (")[0]).is_file())
        self.assertEqual(self.rows["chip_energy_per_request"]["engine"], arms["A"]["engine"])
        self.assertEqual(self.rows["cloud_bill"]["engine"], arms["C"]["engine"])
        self.assertIn("the runs disagree", self.rows["chip_work_for_the_bill"]["sentence"])
        self.assertIn("work was not counted", self.rows["cloud_bill"]["sentence"])
        for k in ("arm_b_vs_a", "arm_d_vs_c"):
            self.assertIn(k, self.rows)
        # The cloud receipt does not count completed work for a work-per-dollar claim.
        self.assertIn("arm_d_work_per_dollar",
                      {r["id"] for r in self.feed["not_for_the_site"]})

    def test_standing_engine_is_distinguished_from_benchmark_engine(self):
        """A current release does not redate the measurements in an earlier index."""
        versions = sorted(int(p.stem.removeprefix("OMNI_V")) for p in ROOT.glob("OMNI_V*.json")
                          if p.stem.removeprefix("OMNI_V").isdigit())
        self.assertTrue(versions, "no frozen engine manifest")
        current = versions[-1]
        manifest = load(f"OMNI_V{current}.json")
        self.assertEqual(manifest["version"], f"omni-v{current}")
        source_versions = {
            int(re.search(r"/V(\d+)_", t["source"]).group(1))
            for t in self.index["tests"]
        }
        self.assertEqual(len(source_versions), 1, "software index mixes engine versions")
        source = next(iter(source_versions))
        self.assertLessEqual(source, current)
        self.assertIn(f"omni-v{source}", self.rows["omni_index"]["engine"])
        if current != source:
            self.assertNotIn(f"omni-v{current}", self.rows["omni_index"]["sentence"],
                             "old measurements cannot be relabeled as current")
        self.assertTrue((ROOT / f"docs/OMNI_V{current}.md").is_file())

    def test_public_words_and_receipts_are_present(self):
        self.assertEqual(self.feed["source"], "tools/site_numbers.py")
        for path in ("LICENSE", "NOTICE", "DISCLOSURES.md",
                     "results/SITE_NUMBERS.md", "docs/WEBSITE_CLAIMS.md"):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertIn("LICENSE", self.feed["notice"])
        self.assertIn("DISCLOSURES.md", self.feed["notice"])
        self.assertIn("never added", self.feed["rule"])
        self.assertNotEqual(self.rows["chip_energy_per_request"]["engine"],
                            self.rows["omni_index"]["engine"],
                            "historical physical GPU receipt must retain its own version")


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
