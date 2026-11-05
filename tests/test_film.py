# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The film (tools/film.py): the screenplay parses as a screenplay, every shot speaks the screenplay's words and every line
has a shot, every number the audience hears or reads is declared and every receipt says what its record says, each prompt
stands alone, and every output is what its sources give."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import film as F  # noqa: E402


class Film(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.P = json.loads(F.PROD.read_text(encoding="utf-8"))
        cls.title, cls.els = F.parse(F.SRC.read_text(encoding="utf-8"))

    def test_the_screenplay_parses_as_a_screenplay(self):
        kinds = [k for k, _ in self.els]
        self.assertEqual(kinds.count("character"), kinds.count("dialogue"))
        heads = [F.plain(t) for k, t in self.els if k == "scene"]
        for sc in self.P["scenes"]:
            self.assertIn(sc["heading"], heads)
        self.assertIn("www.omni-compass.com", " ".join(self.title["copyright"]))
        self.assertEqual(F.plain(" ".join(self.title["title"])), "YIELD LIMIT LINE")

    def test_every_shot_speaks_the_screenplay_and_every_number_is_declared(self):
        self.assertEqual(F.problems(self.P, self.title, self.els), [])

    def test_a_number_without_a_declaration_is_refused(self):
        els = self.els + [("action", "The slide reads 47% faster and forty-nine point nine percent cheaper.")]
        bad = F.number_problems(els, self.P)
        self.assertTrue(any("'4'" in b or "47" in b for b in bad), bad)
        self.assertTrue(any("percent" in b for b in bad), bad)

    def test_a_receipt_that_does_not_match_its_record_is_refused(self):
        R = F.receipts()
        self.assertIsNone(F.check_receipt({"text": "thirteen point eight", "check": "pages_native"}, R))
        self.assertIsNotNone(F.check_receipt({"text": "thirteen point nine", "check": "pages_native"}, R))
        self.assertIsNotNone(F.check_receipt({"text": "47.2%", "check": "pages_change"}, R))
        self.assertIsNotNone(F.check_receipt({"text": "omni-v25", "check": "pages_engine"}, R))

    def test_a_line_without_a_shot_is_found(self):
        els = self.els + [("character", "DEL"), ("dialogue", "A line no shot speaks.")]
        self.assertTrue(any("has no shot" in b for b in F.problems(self.P, self.title, els)))

    def test_each_prompt_stands_alone(self):
        pack = F.prompt_pack(self.P)
        self.assertEqual(len(pack["shots"]), len(self.P["shots"]))
        for s, x in zip(self.P["shots"], pack["shots"]):
            with self.subTest(shot=s["id"]):
                self.assertIn(self.P["locations"][s["at"]]["look"], x["prompt"])
                for w in s.get("who", []):
                    c = self.P["characters"][w]
                    if c["look"] != "unseen" and not F.offscreen(s, w):
                        self.assertIn(c["look"], x["prompt"])
                self.assertIn("no legible text", x["prompt"])
                for ln in s.get("say", []):
                    self.assertIn(ln["line"], x["prompt"])
                for tool, sec in x["generate_seconds"].items():
                    self.assertTrue(sec.split("+")[0].isdigit())

    def test_every_card_and_overlay_carries_the_notice(self):
        B = F.build()
        svgs = [t for p, t in B["text"].items() if p.suffix == ".svg"]
        self.assertGreater(len(svgs), 4)
        for t in svgs:
            lines = t.rstrip("\n").split("\n")
            self.assertTrue(lines[1].startswith("<!-- ©") and lines[1].endswith("www.omni-compass.com -->"))
            self.assertTrue(lines[-1].startswith("<!-- ©") and lines[-1].endswith("www.omni-compass.com -->"))

    def test_the_outputs_are_what_the_sources_give(self):
        self.assertEqual(F.main(["--check"]), 0)

    def test_the_open_source_parser_reads_it_the_same_way(self):
        try:
            from screenplain.parsers import fountain  # the industry's open-source Fountain parser, when installed
        except Exception:
            self.skipTest("screenplain is not installed here")
        with open(F.SRC, encoding="utf-8") as fh:
            screen = fountain.parse(fh)
        from screenplain.types import Dialog, Slug
        theirs_dialog = sum(1 for p in screen.paragraphs if isinstance(p, Dialog))
        theirs_slugs = sum(1 for p in screen.paragraphs if isinstance(p, Slug))
        ours = [k for k, _ in self.els]
        self.assertEqual(theirs_dialog, ours.count("character"))
        self.assertEqual(theirs_slugs, ours.count("scene"))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
