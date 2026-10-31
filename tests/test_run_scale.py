# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The grid's organism runs (tools/run_scale.py, tools/pool_scale.py): a shard cut short hands in every run it finished,
the four stacked joined from the four realms' runs on the same seed equals the four stacked run whole, and a pooled block
short of a run says so."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_scale, pool_scale  # noqa: E402
from tools.run_scale import REALMS, SEED0, joined  # noqa: E402
from realms.harness import STACK  # noqa: E402

KEYS = ("primary", "work", "energy", "viol_pp", "wear", "energy_native_j", "energy_omni_j", "misses_native", "misses_omni",
        "decisions")


class RunScale(unittest.TestCase):
    def test_four_stacked_joined_equals_run_whole(self):
        cat = run_scale.CATALOGS["v5"]
        args = lambda k: (k, 1, SEED0, "v5", cat, "realms", "line")
        _, _, whole = run_scale.job(args(STACK))
        parts = [run_scale.job(args(r))[2] for r in REALMS]
        j = joined(parts)
        for q in KEYS:
            self.assertAlmostEqual(j[q], whole[q], delta=1e-9 * max(1.0, abs(whole[q])), msg=q)
        self.assertEqual(j["restore_ok"], whole["restore_ok"])
        self.assertEqual(j["sums"]["plants"], whole["sums"]["plants"])

    def test_cut_short_hands_in_what_finished(self):
        with tempfile.TemporaryDirectory() as t:
            run_scale.main(["--runs", "3", "--scale", "1", "--organisms", "3", "--out", t, "--workers", "1", "--arm", "v5",
                            "--deadline-min", "0.001"])
            d = json.loads((Path(t) / "SCALE.json").read_text())
            self.assertFalse(d["complete"])
            self.assertEqual(d["runs_done"], 1)                 # the first run always starts; none after the deadline
            from tools.omni_version import engine_files, version_of
            self.assertEqual(d["engine"], version_of(engine_files()))
            run = d["per_run"]["energy_facility_industrial"][str(SEED0)]
            self.assertGreater(run["wall_s"], 0.0)
            self.assertIn("sums", run)
            self.assertIn("finished before the deadline", (Path(t) / "SCALE.md").read_text())


def _run(work, viol_omni):
    """A synthetic run record with its plant sums (two plants, native work 1 each)."""
    s = {"w_sum": 2.0 * work, "w_n": 2, "e_omni": 10.0, "e_native": 10.0, "v_omni": viol_omni, "s_omni": 100.0,
         "v_native": 1.0, "s_native": 100.0, "wear_sum": 0.0, "wear_n": 0, "plants": 2}
    c = run_scale.contrast(s, True)
    c["sums"] = s
    return c


class TheStackCutDown(unittest.TestCase):
    """The ladder of copies (the founder's order of 25 October): the stack of 500 copies cut down to its first 100, 10 and 1 is
    the first part of the same stack, copy for copy, and a run's cut reads exactly those copies' plants."""

    def test_every_size_is_the_first_part_of_the_500_stack(self):
        for key in ("spine", "compute_ai_cloud"):
            stack = run_scale.rows_for(key, 500)
            n = len(run_scale.rows_for(key, 1))
            for m in (1, 10, 100):
                with self.subTest(organism=key, copies=m):
                    self.assertEqual(run_scale.rows_for(key, m), stack[:n * m])   # the same copies, the same muscles, in order

    def test_a_cut_reads_the_first_copies_of_every_body(self):
        n = [len(run_scale.rows_for(r, 1)) for r in REALMS]
        idx = run_scale.cut_plants(STACK, 10, None, "realms", 2)
        offs = [sum(x * 10 for x in n[:i]) for i in range(len(n))]
        self.assertEqual(idx, [o + j for o, nb in zip(offs, n) for j in range(nb * 2)])   # each realm's own first 2 copies
        self.assertEqual(run_scale.cut_plants("spine", 500, None, "body", 100), list(range(len(run_scale.rows_for("spine", 1)) * 100)))


class PoolScale(unittest.TestCase):
    def test_joined_stack_and_short_block(self):
        with tempfile.TemporaryDirectory() as t:
            per = {r: {str(SEED0 + i): _run(1.0, 0.5) for i in range(10)} for r in REALMS}
            del per[REALMS[0]][str(SEED0 + 4)]                # a run missing from one realm: that seed cannot be joined
            d = {"runs": 10, "first": 0, "scale": 1, "commit": "0" * 40, "engine": "omni-v5", "arm": "v5", "load": "line",
                 "catalog": "realms/catalog_v5.csv", "stack": "realms", "complete": False, "summary": {}, "per_run": per}
            (Path(t) / "a").mkdir()
            (Path(t) / "a" / "SCALE.json").write_text(json.dumps(d))
            out = Path(t) / "SIX.md"
            pool_scale.main(str(out), str(Path(t) / "*" / "SCALE.json"))
            pooled = json.loads(out.with_suffix(".json").read_text())
            self.assertEqual(pooled["joined_stack_runs"], 9)
            ten = pooled["summary"]["10"]
            self.assertEqual((ten[STACK]["runs"], ten[STACK]["of"], ten[STACK]["joined"]), (9, 10, 9))
            self.assertEqual(ten[REALMS[0]]["runs"], 9)
            self.assertAlmostEqual(ten[STACK]["viol_pp"][0], -0.5)
            self.assertIn("9 of 10", out.read_text())

    def test_engines_never_pooled_across(self):
        with tempfile.TemporaryDirectory() as t:
            for i, eng in enumerate(("omni-v5", "omni-v3")):
                d = {"runs": 1, "scale": 1, "commit": "0" * 40, "engine": eng, "arm": "v5", "load": "line",
                     "catalog": "realms/catalog_v5.csv", "stack": "realms", "summary": {},
                     "per_run": {REALMS[0]: {str(SEED0 + i): _run(1.0, 1.0)}}}
                (Path(t) / str(i)).mkdir()
                (Path(t) / str(i) / "SCALE.json").write_text(json.dumps(d))
            with self.assertRaises(AssertionError):
                pool_scale.main(str(Path(t) / "SIX.md"), str(Path(t) / "*" / "SCALE.json"))

    def test_later_seed_shard_and_complete_join(self):
        with tempfile.TemporaryDirectory() as t:
            def shard(name, first, runs):
                d = {"runs": runs, "first": first, "scale": 1, "commit": "0" * 40,
                     "engine": "omni-v6", "arm": "v5", "load": "line",
                     "catalog": "realms/catalog_v5.csv", "stack": "realms",
                     "per_run": {REALMS[0]: {str(SEED0 + i): _run(1.0, 2.0)
                                            for i in range(first, first + runs)}}}
                p = Path(t) / name
                p.write_text(json.dumps(d))
                return str(p)
            late = shard("late.json", 10, 90)
            out = Path(t) / "SIX.md"
            pool_scale.main(str(out), late)
            d = json.loads(out.with_suffix(".json").read_text())
            self.assertEqual(d["summary"]["1"][REALMS[0]]["label"], "NO RUNS")
            hundred = d["summary"]["100"][REALMS[0]]
            self.assertEqual(hundred["runs"], 90)
            self.assertEqual(hundred["missing_seeds"], list(range(SEED0, SEED0 + 10)))
            self.assertFalse(hundred["complete"])
            self.assertEqual(hundred["band_first"], "NOT held")
            self.assertIn("90 of 100", out.read_text())
            early = shard("early.json", 0, 10)
            pool_scale.main(str(out), late, early, late)
            d = json.loads(out.with_suffix(".json").read_text())
            self.assertTrue(d["summary"]["100"][REALMS[0]]["complete"])
            self.assertEqual(d["available_runs"][REALMS[0]], 100)
            # An overlapping shard cannot quietly replace an earlier observation.
            bad = json.loads(Path(early).read_text())
            bad["per_run"][REALMS[0]][str(SEED0)] = _run(2.0, 2.0)
            conflict = Path(t) / "conflict.json"
            conflict.write_text(json.dumps(bad))
            with self.assertRaisesRegex(ValueError, "conflicting duplicate"):
                pool_scale.main(str(out), early, str(conflict))


class Conductor(unittest.TestCase):
    """scripts/dispatch_grid.py: every supported free square planned once to 500 runs at 1/10/100/500 copies, nothing started twice, every shard inside a runner's six hours and memory, and the started runs
    read back from their own names."""

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
        import dispatch_grid
        cls.g = dispatch_grid

    def test_every_square_once_to_100(self):
        g = self.g
        self.assertEqual((g.SIZES, g.RUNS), ((1, 10, 100, 500), 500))
        plan = g.next_dispatches({})
        seen = {}
        for d in plan:
            if d["grid"] == "six":
                k, r = ("six", d["size"], d["orgs"][0]), range(d["first"], d["first"] + d["runs"])
                keys = [k]
            else:
                r = range(d["rep_first"], d["rep_first"] + d["reps"])
                keys = [("kube", d["size"], o) for o in d["orgs"]]
            self.assertLessEqual(d["jobs"], g.MAX_JOBS)
            for k in keys:
                s = seen.setdefault(k, set())
                self.assertFalse(s & set(r), f"{k} planned twice")
                s.update(r)
        for size in g.SIZES:
            for o, k in zip(g.ORGS, g.KUBE):
                expected = set(range(g.RUNS)) if g.shape(size, o) else None
                self.assertEqual(seen.get(("six", size, o)), expected, (size, o))
                expected = set(range(1, g.RUNS + 1)) if g.kube_fits(size, k) else None
                self.assertEqual(seen.get(("kube", size, k)), expected, (size, k))
        self.assertTrue([d for d in plan if d["size"] == 500])
        self.assertTrue(g.free_runner_refusals())

    def test_shards_fit_a_runner(self):
        g = self.g
        for size in g.SIZES:
            for o in g.ORGS:
                if g.shape(size, o) is None:
                    continue
                per, w = g.shape(size, o)
                self.assertLessEqual(w * g.MEM[size][o], g.RUNNER_GB)
                runs_per_worker = -(-per // w)
                self.assertLess(g.CAL[size][o] + runs_per_worker * g.SEC[size][o], g.DEADLINE_MIN * 60, (size, o))
        for size in g.SIZES:
            for k in g.KUBE:
                if g.kube_fits(size, k):
                    self.assertLess(g.kube_minutes(size, k, size >= g.SIZES[-1]), 330, (size, k))

    def test_azure_and_reports_go_before_the_grid(self):
        g = self.g
        q, run, done = {"status": "queued"}, {"status": "in_progress"}, {"status": "completed"}
        aks = ".github/workflows/aks-metered.yml"
        self.assertTrue(g.waits_for_a_runner(aks, [done, done, q, q]))          # the next repetition waits for a runner
        self.assertFalse(g.waits_for_a_runner(aks, [done, run, q, q]))          # one at a time: waits for its own matrix
        self.assertTrue(g.waits_for_a_runner(".github/workflows/six-kube.yml",
                                             [dict(done, name="run (tower, 100, 1)"), dict(q, name="report")]))
        self.assertFalse(g.waits_for_a_runner(".github/workflows/six-kube.yml", [dict(q, name="run (tower, 100, 2)")]))
        self.assertFalse(g.waits_for_a_runner(".github/workflows/benchmark-reps.yml", [q]))
        self.assertIn("verify.yml", g.FIRST)
        self.assertIn("archive-run.yml", g.FIRST)

    def test_reruns_released_a_then_b_then_c_never_twice(self):
        g = self.g
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("# a comment\nx one|w1.yml|a=1;b=two words\nx two|w2.yml|\nx three|w1.yml|a=3\n")
        q = g.rerun_queue(f.name)
        self.assertEqual([(r, n) for r, n, _, _ in q[:3]], [("A", "x one"), ("A", "x two"), ("A", "x three")])
        self.assertEqual(len(q), 9)
        self.assertEqual(q[0][3], {"a": "1", "b": "two words"})
        left = g.reruns_to_start(q, {"w1.yml": 3, "w2.yml": 1})      # w1: A one, A three, B one started; w2: A two
        self.assertEqual([(r, n) for r, n, _, _ in left], [("B", "x two"), ("B", "x three"), ("C", "x one"), ("C", "x two"),
                                                           ("C", "x three")])
        self.assertEqual(g.reruns_to_start(q, {"w1.yml": 6, "w2.yml": 3}), [])
        self.assertTrue(g.rerun_queue(g.RERUNS))                      # the repository's own queue reads

    def test_an_entry_added_under_way_keeps_every_started_run_in_its_place(self):
        # 18 October: w1's two entries had all started (A, B and C); an entry put between them would have been read as
        # started in their place, one entry's C run twice and the new entry's A never. In a block of its own it comes after.
        g = self.g
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("x one|w1.yml|a=1\nx two|w2.yml|\nx three|w1.yml|a=3\n# added\nadded=2026-10-18T22:45:00Z\nx new|w1.yml|a=2\n")
        self.assertEqual([[n for n, _, _ in b] for b in g.rerun_blocks(f.name)], [["x one", "x two", "x three"], ["x new"]])
        q = g.rerun_queue(f.name)
        self.assertEqual(len(q), 12)
        self.assertEqual([(r, n) for r, n, _, _ in q[9:]], [("A", "x new"), ("B", "x new"), ("C", "x new")])
        left = g.reruns_to_start(q, {"w1.yml": 6, "w2.yml": 3})
        self.assertEqual([(r, n) for r, n, _, _ in left], [("A", "x new"), ("B", "x new"), ("C", "x new")])
        self.assertEqual(left[0][3], {"a": "2"})

    def test_azure_sets_one_a_queue_a_then_b_then_c_never_twice(self):
        g = self.g
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("# a comment\nsteady|tier=standard\nburst x|load_steps=1 6 1 8 1 6;vm_size=Standard_D2_v4\n"
                    "burst y|load_steps=1 4 1 6 1 9;vm_size=Standard_D2_v4\n")
        q = g.azure_queue(f.name)
        self.assertEqual(len(q), 9)
        # a set with no dial reads the workflow's own default, the max since 31 October, as the workflow titles it
        self.assertEqual(q[0][2], "aks-metered steady dial max eastus Standard_D2s_v4")
        self.assertEqual(q[1][2], "aks-metered burst 1 6 1 8 1 6 dial max eastus Standard_D2_v4")
        steady, x, y = q[0][2], q[1][2], q[2][2]
        # one region is one line at GitHub whatever the machine size (17 October: two sizes treated as two lines cancelled
        # each other's waiting runs): the line busy, nothing starts
        self.assertEqual(g.azure_group(steady), "eastus")
        self.assertEqual(g.azure_group("aks-metered burst 1 6 1 8 1 6 dial save eastus Standard_D2_v4"), "eastus")
        self.assertEqual(g.azure_to_start(q, {steady: 1, x: 1}, {"eastus"}), [])
        # the line free: only its next set, A of every line before any B, one at a time
        self.assertEqual([(r, n) for r, n, _, _ in g.azure_to_start(q, {steady: 1, x: 1}, set())], [("A", "burst y")])
        # every set started: nothing more, ever
        self.assertEqual(g.azure_to_start(q, {steady: 3, x: 3, y: 3}, set()), [])
        self.assertEqual(g.azure_title({"dial": "max", "replica_ceiling": "0"}), "aks-metered steady replica room 0 dial max eastus Standard_D2s_v4")
        own = g.azure_queue(g.AZURE_QUEUE)                                 # the repository's own queue reads: the four sets at the
        self.assertEqual(len(own), 12)                                     # max (the founder's order of 31 October), A, B, C of each
        self.assertEqual([n for r, n, _, _ in own if r == "A"], ["steady", "burst 1 4 1 6 1 9", "burst 1 6 1 8 1 6", "the real day on 1 to 9"])
        for _, _, title, kv in own:
            self.assertTrue(title.startswith("aks-metered ") and " dial max " in title, title)
            # the replica room read live, as on kind: the operator's cap no longer pinned by the struck rule of 14 October
            self.assertEqual((kv.get("dial"), kv.get("replica_ceiling")), ("max", None))
            # a set at the max is never read back as one of the tune-down's started sets
            self.assertNotIn(" dial save ", title)

    def test_one_cloud_one_line_queue_sets_then_its_reruns_and_cancelled_runs_not_counted(self):
        g = self.g
        self.assertEqual(g.cloud_of("aks-metered.yml"), "Azure")
        self.assertEqual(g.cloud_of("aks-metered-full.yml"), "Azure")
        self.assertEqual(g.cloud_of("big-organism.yml"), "Azure")
        self.assertEqual(g.cloud_of("gke-metered.yml"), "Google Cloud")
        self.assertIsNone(g.cloud_of("redis.yml"))
        queue = [("A", "steady", "t-steady", {"s": "1"}), ("A", "burst", "t-burst", {"b": "1"}),
                 ("B", "steady", "t-steady", {"s": "1"}), ("B", "burst", "t-burst", {"b": "1"})]
        reruns = [("A", "full burst", "aks-metered-full.yml", {"f": "1"}), ("B", "full burst", "aks-metered-full.yml", {"f": "1"})]
        # A of the queue's sets first, then A of the cloud's reruns, then B
        self.assertEqual(g.cloud_next(queue, {}, reruns)[1:3], ("A", "steady"))
        self.assertEqual(g.cloud_next(queue, {"t-steady": 1, "t-burst": 1}, reruns), ("aks-metered-full.yml", "A", "full burst", {"f": "1"}))
        self.assertEqual(g.cloud_next(queue, {"t-steady": 1, "t-burst": 1}, reruns[1:])[1:3], ("B", "steady"))
        self.assertIsNone(g.cloud_next(queue, {"t-steady": 2, "t-burst": 2}, []))
        # a run GitHub cancelled before it began is not a run: it is released again
        calls = []
        def standin_api(path, method="GET", data=None):
            calls.append(path)
            return {"workflow_runs": [{"conclusion": "cancelled"}, {"conclusion": "success"}, {"conclusion": None}]}
        real, g.api = g.api, standin_api
        try:
            self.assertEqual(g.reruns_started([("A", "x", "w.yml", {})]), {"w.yml": 2})
        finally:
            g.api = real

    def test_started_runs_read_back_and_not_started_again(self):
        g = self.g
        first = g.next_dispatches({})[:12]
        runs = [{"display_title": d["title"], "conclusion": None} for d in first]
        runs.append({"display_title": g.six_title(100, "1", 500, 50), "conclusion": "cancelled"})   # a cancelled run counts for nothing
        cov = g.coverage(runs, {"dispatches": []})
        again = {d["title"] for d in g.next_dispatches(cov)}
        for d in first:
            self.assertNotIn(d["title"], again)
        self.assertNotIn(500, cov.get(("six", 100, "1"), set()))

    def test_protocol_one_runs_counted_in_no_square(self):
        """Runs with the cluster inside from before the amendment of 12 Oct (no protocol in their names) count in no
        square; the modelled runs are untouched by it."""
        g = self.g
        old = "six-kube x1 orgs stack reps 1+10 arms native compass split no window 960"
        runs = [{"id": 1, "display_title": old, "conclusion": "success"},
                {"id": 2, "display_title": g.six_title(1, "5", 0, 10), "conclusion": "success"}]
        cov = g.coverage(runs, {"dispatches": [{"grid": "six-kube", "size": 1, "rep_first": 1, "reps": 10, "status": "kept"}]})
        self.assertFalse(cov.get(("kube", 1, "stack")))
        self.assertEqual(cov[("six", 1, "5")], set(range(10)))
        runs.append({"id": 3, "display_title": g.kube_title(1, ["stack"], 1, 10, False, 960), "conclusion": None})
        self.assertEqual(g.coverage(runs, {"dispatches": []})[("kube", 1, "stack")], set(range(1, 11)))

    def test_protocol_three_runs_counted_in_no_square_and_both_workflows_name_four(self):
        """18 Oct: the served image pulled onto every kind worker before each arm makes protocol 4 (docs/POD_START_WAIT.md); a
        protocol-3 run fills no square, and both workflows that start runs with the cluster inside name the conductor's
        protocol in their run's name."""
        g = self.g
        self.assertEqual(g.KUBE_PROTOCOL, "4")
        old = "six-kube x1 orgs stack reps 1+10 arms native compass split no window 960 protocol 3"
        cov = g.coverage([{"id": 1, "display_title": old, "conclusion": "success"}], {"dispatches": []})
        self.assertFalse(cov.get(("kube", 1, "stack")))
        wf = Path(__file__).resolve().parents[1] / ".github" / "workflows"
        self.assertIn(f"window {{6}} protocol {g.KUBE_PROTOCOL}'", (wf / "six-kube.yml").read_text())
        self.assertIn(f"' protocol {g.KUBE_PROTOCOL}'", (wf / "big-organism-detached.yml").read_text())

    def test_failed_repetition_started_again_then_listed(self):
        """A repetition whose job failed is started again, alone; after MAX_TRIES failures it is started no more and
        listed for the report."""
        g = self.g
        title = g.kube_title(1, list(g.KUBE), 1, 10, False, 960)
        runs = [{"id": 10, "display_title": title, "conclusion": "failure"}]
        failed = {10: {("stack", 7)}}
        cov = g.coverage(runs, {"dispatches": []}, failed)
        self.assertNotIn(7, cov[("kube", 1, "stack")])
        self.assertEqual(cov[("kube", 1, "tower")], set(range(1, 11)))
        again = [d for d in g.next_dispatches(cov) if d["grid"] == "six-kube" and d["size"] == 1 and d["rep_first"] <= 7]
        self.assertEqual([(d["orgs"], d["rep_first"], d["reps"]) for d in again], [(["stack"], 7, 1)])
        self.assertTrue(g.KUBE_NAME.match(again[0]["title"]))
        for i in range(1, g.MAX_TRIES):                       # it fails again, each time in a run of its own
            runs.append({"id": 10 + i, "display_title": g.kube_title(1, ["stack"], 7, 1, False, 960), "conclusion": "failure"})
            failed[10 + i] = {("stack", 7)}
        cov = g.coverage(runs, {"dispatches": []}, failed)
        self.assertEqual(g.give_up(cov, runs, failed), {(1, "stack", 7): g.MAX_TRIES})
        self.assertIn(7, cov[("kube", 1, "stack")])
        self.assertFalse([d for d in g.next_dispatches(cov) if d["grid"] == "six-kube" and d["size"] == 1
                          and d["rep_first"] <= 7 < d["rep_first"] + d["reps"]])

    def test_job_names_read_back(self):
        g = self.g
        m = g.JOB_NAME.match("run (stack, 1, 56, 960, native compass)")
        self.assertEqual((m.group(1), int(m.group(2)), int(m.group(3))), ("stack", 1, 56))
        m = g.JOB_NAME.match("run (compute_ai_cloud, 500, 7, 7200, compass, -compass)")
        self.assertEqual((m.group(1), int(m.group(2)), int(m.group(3))), ("compute_ai_cloud", 500, 7))
        self.assertIsNone(g.JOB_NAME.match("report"))

    def test_matrix_cuts_the_runs_asked(self):
        g = self.g
        m = g.matrix(100, ["1", "6"], 10, 90)["include"]
        for o in ("1", "6"):
            got = sorted(x for s in m if s["org"] == o for x in range(s["first"], s["first"] + s["n"]))
            self.assertEqual(got, list(range(10, 100)))
        cells = g.kube_matrix([100], ["compute_ai_cloud"], 1, 2, [7200], True)       # split by hand still works
        self.assertEqual([(c["rep"], c["arms"]) for c in cells], [(1, "native"), (1, "compass"), (2, "native"), (2, "compass")])
        self.assertEqual(len({f"{c['rep']}{c['tag']}" for c in cells}), 4)        # one artifact name per arm


if __name__ == "__main__":
    unittest.main()
