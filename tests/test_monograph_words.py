# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""tools/monograph_words.py: every count the live engine's monograph quotes, written from its record and held there.

The referee's report of 7 November 2026 found the monograph's counts typed by hand and overtaken by the record within minutes;
these tests hold the generator that replaces them: it lists every block with a source that exists, writes every block into a
copy of the monograph, reads the copy back in step, names a block that falls out of step, refuses a broken marker pair and
an unknown name, and writes no word the claims checker would refuse.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import monograph_words as MW   # noqa: E402
from tools import claims_check as CC      # noqa: E402


def run(*argv) -> tuple:
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = MW.main(list(argv))
    return code, out.getvalue()


class TestMonographWords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        code, out = run("--list")
        cls.code, cls.blocks = code, json.loads(out)
        cls.tmp = Path(tempfile.mkdtemp(prefix="monograph_words_"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def copy_with_every_block(self, text_for=lambda b: "stale"):
        """A copy of the monograph with every block's markers in it: one-line blocks inside a sentence, the others on their
        own lines, each holding the text text_for gives."""
        src = MW.MONOGRAPH.read_text(encoding="utf-8") if MW.MONOGRAPH.exists() else "# The monograph\n"
        lines = [src, "", "## The blocks", ""]
        for b in self.blocks:
            body = text_for(b)
            if b["text"] and "\n" in b["text"]:
                lines += [MW.BEGIN.format(b["name"]), body, MW.END.format(b["name"]), ""]
            else:
                lines += [f"The record reads {MW.BEGIN.format(b['name'])}{body}{MW.END.format(b['name'])}, as written.", ""]
        p = self.tmp / "LIVE_ENGINE_MONOGRAPH.md"
        p.write_text("\n".join(lines), encoding="utf-8")
        return p

    def test_list_works(self):
        self.assertEqual(self.code, 0)
        names = [b["name"] for b in self.blocks]
        self.assertEqual(len(names), len(set(names)), "every block's name is its own")
        self.assertEqual(names, list(MW.BLOCKS), "--list names every registered block, in order")
        for b in self.blocks:
            self.assertEqual(set(b) - {"error"}, {"name", "text", "source"})
            self.assertIsNone(b.get("error"), f"{b['name']}: {b.get('error')}")
            self.assertTrue(b["text"], f"{b['name']} has no text")
            self.assertRegex(b["name"], r"^[a-z0-9_]+$")

    def test_the_blocks_the_referee_asked_for(self):
        names = {b["name"] for b in self.blocks}
        for need in ("validity", "loss_all", "loss_by_engine", "loss_causes", "flip_rows", "flip_tables", "audit_tables",
                     "index_headline", "index_categories", "index_interval", "index_leave_one_out", "oversight", "four_arms_table",
                     "engine_runs", "core_runs", "injection_grid", "appraisal_counts"):
            self.assertIn(need, names)

    def test_every_source_exists(self):
        for b in self.blocks:
            self.assertTrue(b["source"], f"{b['name']} names no source")
            for s in b["source"].split("; "):
                self.assertTrue((ROOT / s).exists(), f"{b['name']}: its source {s} does not exist")

    def test_one_line_blocks_sit_inside_a_sentence(self):
        for b in self.blocks:
            if "\n" not in b["text"]:
                bare = re.sub(r"\|R[₁₂₃₄]\|", "", b["text"])   # a set's size, |R₁|, is notation, not a cell's edge
                self.assertNotIn("|", bare, f"{b['name']} would break a table cell")
                self.assertEqual(b["text"], b["text"].strip(), f"{b['name']} carries a stray space")

    def test_check_passes_after_fix_on_a_copy(self):
        p = self.copy_with_every_block()
        code, out = run("--check", "--file", str(p))
        self.assertEqual(code, 1, "a copy of stale blocks reads out of step")
        for b in self.blocks:
            self.assertIn(f"{b['name']}: differs from its record", out)
        code, out = run("--fix", "--file", str(p))
        self.assertEqual(code, 0, out)
        code, out = run("--check", "--file", str(p))
        self.assertEqual(code, 0, out)
        text = p.read_text(encoding="utf-8")
        for b in self.blocks:
            self.assertIn(MW.BEGIN.format(b["name"]) + ("\n" + b["text"] + "\n" if "\n" in b["text"] else b["text"])
                          + MW.END.format(b["name"]), text)
        code, out = run("--fix", "--file", str(p))
        self.assertEqual((code, p.read_text(encoding="utf-8")), (0, text), "a second --fix changes nothing")

    def test_one_block_out_of_step_is_named(self):
        p = self.copy_with_every_block(lambda b: b["text"])
        self.assertEqual(run("--fix", "--file", str(p))[0], 0)
        self.assertEqual(run("--check", "--file", str(p))[0], 0)
        t = p.read_text(encoding="utf-8")
        name = "loss_against_native"
        good = MW.BEGIN.format(name) + next(b["text"] for b in self.blocks if b["name"] == name) + MW.END.format(name)
        at = t.rfind(good)
        p.write_text(t[:at] + MW.BEGIN.format(name) + "273" + MW.END.format(name) + t[at + len(good):], encoding="utf-8")
        code, out = run("--check", "--file", str(p))
        self.assertEqual(code, 1)
        named = [line for line in out.splitlines() if "differs from its record" in line]
        self.assertEqual(len(named), 1, out)
        self.assertIn(f"{name}: differs from its record", named[0])

    def test_broken_markers_and_unknown_names_fail(self):
        p = self.tmp / "broken.md"
        for text, word in ((f"a {MW.BEGIN.format('engine')} and no end", "has no end marker"),
                           (f"a stray {MW.END.format('engine')}", "with no block open"),
                           (f"{MW.BEGIN.format('engine')}x{MW.END.format('engine_name')}", "is closed as"),
                           (f"{MW.BEGIN.format('engine')}{MW.BEGIN.format('engine_name')}x{MW.END.format('engine_name')}",
                            "opens inside")):
            p.write_text(text, encoding="utf-8")
            for action in ("--check", "--fix"):
                code, out = run(action, "--file", str(p))
                self.assertEqual(code, 1, text)
                self.assertIn(word, out)
            self.assertEqual(p.read_text(encoding="utf-8"), text, "a broken file is never written")
        p.write_text(f"{MW.BEGIN.format('no_such_block')}x{MW.END.format('no_such_block')}", encoding="utf-8")
        code, out = run("--check", "--file", str(p))
        self.assertEqual(code, 1)
        self.assertIn("no_such_block: no such block", out)

    def test_a_file_with_no_block_passes(self):
        p = self.tmp / "plain.md"
        p.write_text("# Nothing marked yet\n", encoding="utf-8")
        self.assertEqual(run("--check", "--file", str(p))[0], 0)

    def test_every_word_reads_by_the_key(self):
        findings = []
        for b in self.blocks:
            CC.scan(b["name"], b["text"], findings)
        self.assertEqual(findings, [], "the claims checker refuses a block's words")
        for b in self.blocks:
            self.assertNotIn("confirmed", b["text"].lower(), b["name"])
            self.assertNotRegex(b["text"], r"\bsimulation\b", b["name"])

    def test_the_ledger_and_the_record_agree(self):
        """The counts come from the record the ledger reads: the stored audit's LOSS rows are the ledger's own."""
        rows, _ = MW.ledger()
        self.assertEqual(len(rows[MW.LL.SECTIONS[0]]), len(MW.native_losses()))
        head = next(line for line in MW.LEDGER.read_text(encoding="utf-8").splitlines() if line.startswith("Rows that read LOSS"))
        self.assertIn(f"**{len(MW.native_losses())}**", head)

    def test_the_index_and_its_runs(self):
        """The headline is tools/omni_index.py's, and its three runs' own indexes compose to it exactly."""
        rec = json.loads(MW.INDEX_JSON.read_text(encoding="utf-8"))
        self.assertAlmostEqual(100 * (MW.index_record()["head"] - 1), rec["headline_pct"], places=6)
        runs = MW.index_by_run()["head"]
        self.assertEqual(len(runs), 3)
        self.assertAlmostEqual(MW.OI.gmean(runs), MW.index_record()["head"], places=9)


    def test_the_rebuild_keeps_the_words_in_step(self):
        # the founder's order of 6 November: when a benchmark changes a number, the words that quote it follow by themselves; the
        # page's rebuild on GitHub writes every block again, checks them, and commits the monograph with the page
        wf = (ROOT / ".github" / "workflows" / "live-engine.yml").read_text(encoding="utf-8")
        self.assertIn("python tools/monograph_words.py --fix", wf)
        self.assertIn("python tools/monograph_words.py --check", wf)
        self.assertIn("docs/engine/LIVE_ENGINE_MONOGRAPH.md", wf.split("Legal notice checked, the page committed", 1)[1])
        self.assertIn("monograph_words.py", (ROOT / "verify.py").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
