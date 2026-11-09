# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; see LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Independent source-to-index provenance test.

Checks the 26 indexed test entries against raw JSON table records: source file,
three GitHub run IDs, engine version, workload identity, reading, first-pair
measurements and geometric-mean ratios. It does not rerun experimental hardware,
certify run authenticity or prove comparative benefit; the index generator is
deliberately not imported.
"""
import json
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def geomean(values):
    if not values or any(v is None or not math.isfinite(v) or v <= 0 for v in values):
        raise ValueError("geometric means need a non-empty set of finite positive ratios")
    return math.exp(sum(math.log(v) for v in values) / len(values))


def is_scored(reading):
    # Mirror only the *published selection predicate*, independently of its
    # implementation. The metric aim itself is checked separately.
    key = (reading or "").strip().strip("*").strip().lower()
    return (
        key.startswith("confirmed")
        or "in all three of our runs" in key
        or "by the mean of our three runs" in key
        or key.startswith("higher in at least one of our runs")
        or key.startswith("never more")
    )


class IndexRawProvenance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "results/OMNI_INDEX.json").read_text(encoding="utf-8"))
        cls.cache = {}

    @classmethod
    def source(cls, path):
        if path not in cls.cache:
            cls.cache[path] = json.loads((ROOT / path).read_text(encoding="utf-8"))
        return cls.cache[path]

    def test_every_index_entry_tracks_its_original_three_runs(self):
        self.assertTrue(self.index["tests"], "the index has no tests")
        for test in self.index["tests"]:
            with self.subTest(test=test["test"], source=test["source"]):
                path = test["source"]
                self.assertRegex(path, r"^results/live/V[0-9]+_[A-Z0-9_]+\.json$")
                data = self.source(path)
                runs = data["runs"]
                self.assertEqual(len(runs), 3, "require A/B/C source table runs")
                self.assertEqual([str(run["run"]) for run in runs],
                                 [str(run) for run in test["runs"]])
                self.assertEqual([run["tag"] for run in runs], ["A", "B", "C"])
                version = int(re.search(r"/V(\d+)_", path).group(1))
                for run in runs:
                    self.assertIn(f"omni-v{version}", run["engine"],
                                  "an index source mixes engine versions")
                    self.assertTrue(run["commit"], "source record lacks execution commit")

    def test_each_index_measure_reproduces_source_table(self):
        for test in self.index["tests"]:
            workload = re.search(r"`([^`]+)`", test["test"])
            data = self.source(test["source"])
            table = data["workloads"][workload.group(1)] if workload else data["rows"]
            self.assertTrue(table, "empty source table")
            for metric, indexed in test["measures"].items():
                with self.subTest(test=test["test"], metric=metric):
                    if indexed["reading"] == "the same fixed-rate work sent to both arms":
                        self.assertEqual(metric, "work")
                        self.assertEqual((indexed["native"], indexed["omni"],
                                          indexed["ratio"]), (1.0, 1.0, 1.0))
                        continue

                    matching = []
                    for raw in table.values():
                        pairs = raw.get("runs") or []
                        if len(pairs) != 3 or raw.get("reading") != indexed["reading"]:
                            continue
                        a = pairs[0]
                        if any(a.get(k) is None for k in ("native", "omni")):
                            continue
                        if (math.isclose(a["native"], indexed["native"], rel_tol=1e-8, abs_tol=1e-8)
                                and math.isclose(a["omni"], indexed["omni"], rel_tol=1e-8, abs_tol=1e-8)):
                            matching.append(raw)
                    self.assertTrue(matching, "indexed reading/values absent from source table")
                    candidates = []
                    for raw in matching:
                        pairs = raw["runs"]
                        ratios = [
                            (row["omni"] / row["native"] if metric == "work"
                             else row["native"] / row["omni"])
                            if row["native"] and row["omni"] else None
                            for row in pairs
                        ]
                        ratio = (geomean(ratios) if is_scored(raw["reading"])
                                 and all(v is not None for v in ratios) else 1.0)
                        candidates.append(ratio)
                    self.assertTrue(
                        any(math.isclose(v, indexed["ratio"], rel_tol=1e-9, abs_tol=1e-9)
                            for v in candidates),
                        f"index ratio {indexed['ratio']} contradicts the original A/B/C rows"
                    )


class PhysicalAndCloudBillProvenance(unittest.TestCase):
    """Keep P-class chip, L-class Azure and computed work-per-dollar separate."""

    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "results/TWO_BILLS.json").read_text(encoding="utf-8"))

    def test_gpu_work_per_dollar_uses_each_paired_rental_window(self):
        chip = self.data["chip"]
        self.assertIn("omni-v23", chip["engine"])
        self.assertEqual(len(chip["per_run"]), 3)
        self.assertEqual(len(chip["runs"]), 3)
        diffs = []
        for pair in chip["per_run"]:
            with self.subTest(pair=pair):
                for arm in ("native", "omni"):
                    record = pair[arm]
                    self.assertGreater(record["bill"], 0)
                    self.assertGreater(record["work"], 0)
                    self.assertAlmostEqual(
                        record["work"] / record["bill"],
                        record["per_dollar"], places=7)
                diffs.append(
                    pair["omni"]["per_dollar"] / pair["native"]["per_dollar"] - 1)
        self.assertGreater(diffs[0], 0)
        self.assertGreater(diffs[1], 0)
        self.assertLess(diffs[2], 0,
                        "historical adverse work-per-dollar run must remain visible")
        self.assertIn("the runs disagree",
                      chip["rows"]["work per dollar (requests served per $)"]["reading"])

    def test_azure_bill_has_no_completed_work_claim(self):
        cloud = self.data["cloud"]
        self.assertEqual(cloud["engine"], "omni-v18")
        self.assertEqual(cloud["repetitions"], 97)
        self.assertIsNone(cloud["work_key"],
                          "unmeasured work cannot be used to infer cloud work/$")
        self.assertFalse(cloud["work"],
                         "unmeasured work cannot become a measured cloud benefit")
        bill = cloud["bill"]
        self.assertAlmostEqual(
            bill["omni"] - bill["native"], bill["diff"], places=10)
        self.assertLess(bill["ci95"][0], 0)
        self.assertGreater(bill["ci95"][1], 0,
                           "historical interval crosses zero; bill effect unresolved")


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
