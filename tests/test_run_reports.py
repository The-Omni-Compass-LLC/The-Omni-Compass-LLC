# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The run-set reports (tools/run_reports.py): every reader gets every form, each form carries the owners' notice at its top
and its end, every number is the set's own record's, every interval is what its formula gives, and the workflow that writes a
set writes its reports beside it without ever costing the set its record (the founder's order of 16 November)."""
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import tools.run_reports as R      # noqa: E402
from tools.legal import NOTICE      # noqa: E402


class Reports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name)
        cls.runs, cls.base = R.newest()
        R.write(cls.runs, cls.base, cls.out)
        cls.e, cls.c = R.load(cls.runs, cls.base)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_every_reader_gets_every_form(self):
        for a in R.AUDIENCES:
            for ext in (".md", ".txt", ".pdf", ".docx"):
                self.assertTrue((self.out / f"{a}{ext}").stat().st_size > 1000, f"{a}{ext}")
        for name in R.DATA + ("README.md",):
            self.assertTrue((self.out / name).exists(), name)
        self.assertTrue((self.out / "ENGINEER.pdf").read_bytes().startswith(b"%PDF"))
        self.assertTrue(zipfile.is_zipfile(self.out / "BOARD.docx"))

    def test_the_notice_stands_at_the_top_and_the_end_of_every_form(self):
        plain = R.plain(NOTICE)
        for a in R.AUDIENCES:
            md = (self.out / f"{a}.md").read_text(encoding="utf-8")
            self.assertIn(NOTICE.split(" Every copy")[0][:60], md.split("\n")[2])
            self.assertTrue(md.rstrip().endswith(f"*{NOTICE}*"))
            txt = (self.out / f"{a}.txt").read_text(encoding="utf-8").strip().split("\n")
            self.assertEqual((txt[0], txt[-1]), (plain, plain))
            paras = [x for x in R.docx_text(self.out / f"{a}.docx") if x]
            self.assertEqual((R.plain(paras[0]), R.plain(paras[-1])), (plain, plain))

    def test_every_number_is_the_records(self):
        s = json.loads((self.out / "SET_SUMMARY.json").read_text(encoding="utf-8"))
        self.assertEqual((s["engine_digest"], s["core_digest"]), (self.e["digest"], self.c["digest"]))
        for way, v in self.c["summary"].items():
            self.assertEqual((s["ways"][way]["conveyed"], s["ways"][way]["certified"]), (v["conveyed"], v["certified"]))
        self.assertEqual(s["allowed"], sum(1 for r in self.e["receipts"] if r["allowed"]))
        rows = (self.out / "SET_ENGINE_RUNS.csv").read_text(encoding="utf-8").strip().split("\n")
        self.assertEqual(len(rows), 1 + self.runs)
        board = (self.out / "BOARD.md").read_text(encoding="utf-8")
        self.assertIn(f"{self.c['summary']['controlled']['conveyed']} of {self.runs}", board)
        self.assertIn(f"{self.c['summary']['uncontrolled']['conveyed']} of {self.runs}", board)

    def test_the_intervals_and_the_words(self):
        lo, hi = R.wilson(500, 500)
        self.assertAlmostEqual(hi, 1.0)
        self.assertAlmostEqual(lo, 500 / (500 + R.Z95 ** 2), places=12)   # Wilson at p = 1: n / (n + z²)
        lo, hi = R.newcombe(500, 500, 474, 500)
        self.assertTrue(0 < lo < 0.052 < hi)
        self.assertEqual(R.reading(5.5, "higher"), "GAIN")          # more runs brought home
        self.assertEqual(R.reading(-43.3, "lower"), "GAIN")         # fewer steps taken
        self.assertEqual(R.reading(-5.5, "higher"), "LOSS")
        self.assertTrue(R.reading(0.2, "higher").startswith("STEADY"))

    def test_the_same_records_give_the_same_bytes(self):
        with tempfile.TemporaryDirectory() as t:
            R.write(self.runs, self.base, Path(t))
            for p in self.out.iterdir():
                self.assertEqual(p.read_bytes(), (Path(t) / p.name).read_bytes(), p.name)

    def test_each_set_on_github_writes_its_reports_and_never_loses_its_record_to_them(self):
        s = (ROOT / ".github" / "workflows" / "engine-runs.yml").read_text(encoding="utf-8")
        self.assertIn('python3 tools/run_reports.py > /dev/null || echo "::warning::', s)
        self.assertIn("git add -A results/run_reports/latest/ 2>/dev/null || true", s)
        self.assertLess(s.index("git pull -q --rebase"), s.index("python3 tools/run_reports.py > /dev/null"))
        # the Word form needs no package beyond Python's own: the lock file's pinned supply chain is unchanged
        self.assertNotIn("docx", (ROOT / "requirements-lock.txt").read_text(encoding="utf-8"))
        self.assertNotIn("import docx", (ROOT / "tools" / "run_reports.py").read_text(encoding="utf-8"))
        self.assertIn("run_reports.py", (ROOT / "verify.py").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
