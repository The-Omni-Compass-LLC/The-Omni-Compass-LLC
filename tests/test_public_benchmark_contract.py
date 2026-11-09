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
                self.assertRegex(t["source"], r"/V25_", "a V25 index cannot silently mix engine versions")

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
