# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The front page's plan: archived runs grouped by what they are, the three newest complete runs of a kind as A, B and C, a
table rebuilt only when its runs changed, two runs never a set, the service objective its own table, the README's latest
block kept newest first and bounded."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import front_page as fp  # noqa: E402


def standin_run(raw: Path, rid: int, product: str, workloads, objective="resource", engine="omni-v3", report=True):
    d = raw / f"run-{rid}"
    if report:
        (d / f"{product}-report").mkdir(parents=True, exist_ok=True)
        (d / f"{product}-report" / f"{product.upper()}.md").write_text("table\n")
    for wl in workloads:
        w = d / f"{product}-{wl}" / f"{product}-{wl}"
        w.mkdir(parents=True, exist_ok=True)
        (w / f"{wl}.json").write_text(json.dumps({"workload": wl, "objective": objective, "engine": {"version": engine, "digest": "x"},
                                                  "tuning": wl == "tuning"}))
    return d


class TestFrontPage(unittest.TestCase):
    def test_plan_groups_the_three_newest_complete_runs_of_a_kind(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            raw = root / "results" / "live" / "raw"
            for rid in (101, 102, 103, 104):                       # four resource runs: the newest three are the set
                standin_run(raw, rid, "redis", ["tuning", "small", "large", "burst"])
            standin_run(raw, 201, "redis", ["tuning", "small", "large", "burst"], objective="service")   # one service run: no set
            standin_run(raw, 202, "redis", ["tuning", "small", "large", "burst"], objective="service")   # two: still no set
            standin_run(raw, 301, "kafka", ["light"], report=False)   # no report directory: not complete, not counted
            standin_run(raw, 401, "ycsb", ["a", "b"]); standin_run(raw, 402, "ycsb", ["a", "b"]); standin_run(raw, 403, "ycsb", ["a", "b"])
            standin_run(raw, 404, "ycsb", ["a", "b"], engine="omni-v4")                                  # another engine: another kind
            items = fp.plan(root)
            by = {it["table"]: it for it in items}
            self.assertEqual(sorted(by), ["V3_REDIS", "V3_YCSB"])
            self.assertEqual(by["V3_REDIS"]["runs"], [102, 103, 104])
            self.assertEqual(by["V3_REDIS"]["workloads"], ["burst", "large", "small", "tuning"])
            self.assertEqual(by["V3_YCSB"]["runs"], [401, 402, 403])
            self.assertEqual(by["V3_REDIS"]["tool"], "tools/redis_abc.py")

    def test_a_database_run_keeps_its_objective_in_the_repetitions_and_its_engine_in_the_summary(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            raw = root / "results" / "live" / "raw"
            for rid in (501, 502, 503):
                d = raw / f"run-{rid}"
                (d / "pgbench-report").mkdir(parents=True)
                (d / "pgbench-report" / "PGBENCH.md").write_text("table\n")
                for wl in ("select", "tpcb_hot"):
                    w = d / f"pgbench-{wl}" / f"pgbench-{wl}"
                    (w / "rep-1" / "omni").mkdir(parents=True)
                    (w / f"{wl}.json").write_text(json.dumps({"engine": {"version": "omni-v3", "digest": "x"}, "reps": []}))
                    (w / "rep-1" / "omni" / "arm.json").write_text(json.dumps({"verdict": {"objective": "service", "state": "acting"}}))
            self.assertEqual(fp.describe(raw / "run-501"), ("pgbench", "service", "omni-v3", ("select", "tpcb_hot"), "operator"))
            items = fp.plan(root)
            self.assertEqual([(it["table"], it["runs"]) for it in items], [("V3_PGBENCH_SERVICE", [501, 502, 503])])

    def test_native_as_shipped_and_the_operators_setting_are_never_one_table(self):
        # 19 October: the omni-v11 Redis runs were the operator's setting and native as shipped, A, B and C of each, both on
        # the resource objective; the three newest of the six are two of one and one of the other, never one benchmark
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            raw = root / "results" / "live" / "raw"
            for rid, native in ((601, "operator"), (602, "shipped"), (603, "operator"), (604, "shipped"), (605, "operator"),
                                (606, "shipped")):
                d = raw / f"run-{rid}"
                (d / "redis-report").mkdir(parents=True)
                for wl in ("small", "large"):
                    w = d / f"redis-{wl}" / f"redis-{wl}"
                    w.mkdir(parents=True)
                    (w / f"{wl}.json").write_text(json.dumps({"engine": "omni-v11 (digest x, 47 files)", "objective": "resource",
                                                               "native": native}))
            self.assertEqual(fp.describe(raw / "run-602")[4], "shipped")
            items = sorted((it["table"], it["runs"]) for it in fp.plan(root))
            self.assertEqual(items, [("V11_REDIS", [601, 603, 605]), ("V11_REDIS_SHIPPED", [602, 604, 606])])

    def test_a_table_built_from_its_newest_runs_is_not_rebuilt(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            raw = root / "results" / "live" / "raw"
            for rid in (11, 12, 13):
                standin_run(raw, rid, "kafka", ["tuning", "light", "heavy", "burst"])
            live = root / "results" / "live"
            (live / "V3_KAFKA.md").write_text("built\n")
            (live / "FRONT_PAGE_STATE.json").write_text(json.dumps({"V3_KAFKA": {"runs": [11, 12, 13]}}))
            self.assertEqual(fp.plan(root), [])
            standin_run(raw, 14, "kafka", ["tuning", "light", "heavy", "burst"])    # a fourth run: the set moves and the table is stale
            items = fp.plan(root)
            self.assertEqual([it["runs"] for it in items], [[12, 13, 14]])
            self.assertEqual(items[0]["previous"], [11, 12, 13])

    def test_table_names_follow_the_engine_and_the_objective(self):
        self.assertEqual(fp.table_name("redis", "resource", "omni-v3"), "V3_REDIS")
        self.assertEqual(fp.table_name("redis", "service", "omni-v3"), "V3_REDIS_SERVICE")
        self.assertEqual(fp.table_name("redis", "resource", "omni-v11", "shipped"), "V11_REDIS_SHIPPED")
        self.assertEqual(fp.table_name("pgbench", "per-work", "omni-v4"), "V4_PGBENCH_PER_WORK")
        # the records carry the whole version line; only the version counts, and a record on no declared version never joins
        self.assertEqual(fp.table_name("kafka", "resource", "omni-v3 (digest b53d05449ee04c4b, 40 files)"), "V3_KAFKA")
        self.assertEqual(fp.engine_version("omni-v3 (digest b53d05449ee04c4b, 40 files)"), "omni-v3")
        self.assertEqual(fp.engine_version("differs from v2: realms/catalog_v1.csv"), "unversioned")
        self.assertEqual(fp.table_name("ycsb", "resource", "differs from v2: realms/catalog_v1.csv"), "V0_YCSB")

    def test_readme_block_is_newest_first_and_bounded(self):
        with tempfile.TemporaryDirectory() as t:
            r = Path(t) / "README.md"
            r.write_text("# title\n\n## Latest\n\n" + fp.BEGIN + "\n- old line\n" + fp.END + "\n\n## rest\n")
            self.assertTrue(fp.write_readme(["- new A", "- new B"], r, keep=2))
            s = r.read_text()
            self.assertIn(fp.BEGIN + "\n- new B\n- new A\n" + fp.END, s)
            self.assertNotIn("- old line", s)           # bounded at two
            self.assertIn("## rest", s)
            r.write_text("# no markers\n")
            self.assertFalse(fp.write_readme(["- x"], r))
            self.assertEqual(r.read_text(), "# no markers\n")


if __name__ == "__main__":
    unittest.main()
