# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The jump generator's ledger (tools/runs_ledger.py): each proof it reads from a record fails on a record that breaks it, the
page's own digest is written into the set's record and its page, and the workflows that commit a set write the ledger with it."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import tools.engine_runs as E      # noqa: E402
import tools.runs_ledger as L      # noqa: E402


def small_set(base: int = 20261112, n: int = 10) -> dict:
    """A record of n runs as tools/engine_runs.py writes one, the C++ harness's part stated as agreeing."""
    rs = [E.one_run(k, base) for k in range(n)]
    dg = E.digest(rs)
    return {"engine": "omni-v26 (digest 75d3c22eed4473b9)", "runs": n, "base": base, "written": "2026-11-12T00:00:00Z", "digest": dg,
            "receipts": json.loads(json.dumps(rs)), "inputs_digest": "0" * 64,
            "cpp": {"digest": dg, "same": True, "largest_difference": 0.0, "agree": n},
            "ladder": [{"runs": m, "digest": E.digest(rs[:m]), "cpp_digest": E.digest(rs[:m]), "same": True} for m in E.LADDER if m <= n],
            "github": {"run_id": 1, "workflow": "engine-runs", "commit": "0" * 40, "ref": "main", "url": "https://example.invalid/1"}}


class Ledger(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.good = small_set()
        self._root = L.ROOT
        L.ROOT = self.dir            # the tool names a record by its path under the repository's root

    def tearDown(self):
        L.ROOT = self._root
        self.tmp.cleanup()

    def read(self, data: dict, md: bool = True) -> dict:
        p = self.dir / f"ENGINE_RUNS_{data['runs']}_{data['base']}.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        if md:
            p.with_suffix(".md").write_text("a record\n", encoding="utf-8")
        elif p.with_suffix(".md").exists():
            p.with_suffix(".md").unlink()
        return L.engine_set(p)

    def test_a_whole_record_passes_every_proof(self):
        r = self.read(self.good)
        self.assertEqual(r["failed"], [])
        self.assertEqual((r["engine"], r["run_id"], r["cpp"]), ("omni-v26", 1, self.good["digest"]))

    def test_a_changed_receipt_fails_the_digest(self):
        d = copy.deepcopy(self.good)
        key = next(k for k in E.KEYS if isinstance(d["receipts"][3].get(k), float))
        d["receipts"][3][key] += 1e-3
        self.assertTrue(any("receipts' digest" in f for f in self.read(d)["failed"]))

    def test_a_seed_that_is_not_the_jump_generators_fails(self):
        d = copy.deepcopy(self.good)
        d["receipts"][5]["seed"] = (d["receipts"][5]["seed"] + 1) % 2 ** 32
        self.assertTrue(any("seed" in f for f in self.read(d)["failed"]))

    def test_a_rung_that_is_not_its_receipts_digest_fails(self):
        d = copy.deepcopy(self.good)
        d["ladder"][0]["digest"] = "f" * 64
        self.assertTrue(any("rung of 1" in f for f in self.read(d)["failed"]))

    def test_a_cpp_digest_that_differs_fails_at_the_set_and_at_the_rung(self):
        d = copy.deepcopy(self.good)
        d["cpp"]["digest"] = "e" * 64
        self.assertTrue(any("C++ harness's digest" in f for f in self.read(d)["failed"]))
        d = copy.deepcopy(self.good)
        d["ladder"][1]["cpp_digest"] = "e" * 64
        self.assertTrue(any("C++ harness differs at the rung of 10" in f for f in self.read(d)["failed"]))

    def test_a_page_digest_that_differs_fails(self):
        d = copy.deepcopy(self.good)
        d["page"] = {"digest": "d" * 64, "same": False}
        self.assertTrue(any("page's digest" in f for f in self.read(d)["failed"]))
        d = copy.deepcopy(self.good)
        d["page"] = {"digest": d["digest"], "same": True}
        d["ladder"][0]["page_digest"] = "d" * 64
        self.assertTrue(any("page differs at the rung of 1" in f for f in self.read(d)["failed"]))

    def test_a_record_without_its_page_fails(self):
        self.assertTrue(any(".md" in f for f in self.read(self.good, md=False)["failed"]))

    def test_the_pages_digest_is_written_into_the_record_and_its_page(self):
        p = self.dir / "ENGINE_RUNS_10_20261112.json"
        p.write_text(json.dumps(self.good), encoding="utf-8")
        p.with_suffix(".md").write_text("# a set\n\n**The ladder** (the first runs)\n", encoding="utf-8")
        block = {"tool": "t", "page": "p", "page_sha256": "a" * 64, "digest": self.good["digest"], "same": None, "largest_difference": 0.0,
                 "agree": 10, "of": 10, "generator_bit_for_bit": True,
                 "ladder": [{"runs": g["runs"], "digest": g["digest"]} for g in self.good["ladder"]]}
        self.assertTrue(E.note_page(p, 10, 20261112, block))
        d = json.loads(p.read_text(encoding="utf-8"))
        self.assertTrue(d["page"]["same"])
        self.assertTrue(all(g["page_same"] and g["page_digest"] == g["digest"] for g in d["ladder"]))
        md = p.with_suffix(".md").read_text(encoding="utf-8")
        self.assertIn(E.PAGE_MARK, md)
        self.assertLess(md.index(E.PAGE_MARK), md.index("**The ladder**"))
        self.assertTrue(E.note_page(p, 10, 20261112, dict(block)))            # written again, the line is replaced, never doubled
        self.assertEqual(p.with_suffix(".md").read_text(encoding="utf-8").count(E.PAGE_MARK), 1)
        self.assertFalse(E.note_page(p, 10, 999, dict(block)))                # another set's record never takes it
        r = L.engine_set(p)
        self.assertEqual((r["failed"], r["page"], r["ladder_page"]), ([], self.good["digest"], True))

    def test_a_page_digest_that_differs_is_written_as_different(self):
        p = self.dir / "ENGINE_RUNS_10_20261112.json"
        p.write_text(json.dumps(self.good), encoding="utf-8")
        p.with_suffix(".md").write_text("# a set\n\n**The ladder**\n", encoding="utf-8")
        block = {"tool": "t", "page": "p", "page_sha256": "a" * 64, "digest": "c" * 64, "same": None, "largest_difference": 1.0,
                 "agree": 9, "of": 10, "generator_bit_for_bit": True, "ladder": [{"runs": 1, "digest": "c" * 64}]}
        E.note_page(p, 10, 20261112, block)
        self.assertIn("DIFFERENT", p.with_suffix(".md").read_text(encoding="utf-8"))
        self.assertTrue(L.engine_set(p)["failed"])


class Record(unittest.TestCase):
    """The repository's own records and the places that keep the ledger in step with them."""

    def test_every_recorded_set_passes_and_none_is_written_twice(self):
        d = L.build()
        self.assertTrue(d["engine_sets"] and d["core_sets"])
        self.assertEqual([r["file"] for r in d["engine_sets"] + d["core_sets"] if r["failed"]], [])
        self.assertEqual(d["cross"], [])

    def test_the_ledger_counts_nothing_it_did_not_read(self):
        d = L.build()
        t = L.tally(d)
        self.assertEqual(t["engine"], len(list((ROOT / "results" / "engine_runs").glob("ENGINE_RUNS_*.json"))))
        self.assertEqual(t["core"], len(list((ROOT / "results" / "core_runs").glob("CORE_RUNS_*.json"))))
        self.assertEqual(t["engine_runs"], sum(r["runs"] for r in d["engine_sets"]))
        self.assertEqual(sum(t["engines"].values()), t["engine"])

    def test_every_workflow_that_commits_a_set_writes_the_ledger_with_it(self):
        for wf in ("engine-runs.yml", "monte-carlo.yml"):
            s = (ROOT / ".github" / "workflows" / wf).read_text(encoding="utf-8")
            self.assertIn("python3 tools/runs_ledger.py > /dev/null", s, wf)
            self.assertIn("results/RUNS_LEDGER.json results/RUNS_LEDGER.md", s, wf)
            self.assertIn("python3 tools/runs_ledger.py --check", s, wf)
            self.assertLess(s.index("git pull -q --rebase"), s.index("python3 tools/runs_ledger.py > /dev/null"), wf)   # on the branch as it stands
        s = (ROOT / ".github" / "workflows" / "engine-runs.yml").read_text(encoding="utf-8")
        self.assertIn("--verify docs/engine/OMNI_COMPASS_LIVE_ENGINE.html --all", s)     # the step that writes the page's digest
        self.assertIn("runs_ledger.py", (ROOT / "verify.py").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
