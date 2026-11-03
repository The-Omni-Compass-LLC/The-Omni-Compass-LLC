# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live engine's guided tour: one stop for every section, in the page's order, in the Live Engine Manual's words; the
notice at its opening and its close; a recorded clip only where it reads the stop's words today."""
import hashlib
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import tour_script  # noqa: E402
from legal import PLAIN  # noqa: E402

PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
VOICE = ROOT / "docs" / "engine" / "tour" / "TOUR_VOICE.json"


class Tour(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = PAGE.read_text(encoding="utf-8")
        cls.steps = tour_script.steps()

    def test_every_section_once_in_the_page_order(self):
        sections = re.findall(r'<section class="stack[^"]*" id="([a-z0-9-]+)"', self.page)
        ids = [s["id"] for s in self.steps]
        self.assertEqual(ids[0], "intro")
        self.assertEqual(ids[-1], "end")
        self.assertEqual(ids[1:-1], sections, "a section of the page has no stop, or the stops are out of the page's order")

    def test_the_notice_opens_and_closes_it(self):
        self.assertEqual(self.steps[0]["notice"], PLAIN)
        self.assertEqual(self.steps[-1]["notice"], PLAIN)
        for s in (self.steps[0], self.steps[-1]):
            self.assertIn("All rights reserved. Evaluation and Simulation use only.", s["say"])
            self.assertTrue(s["say"].rstrip().endswith("omni-compass dot com"))

    def test_each_stop_in_the_manuals_words(self):
        manual = (ROOT / "docs" / "OMNI_COMPASS_LIVE_ENGINE_MANUAL.md").read_text(encoding="utf-8")
        words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]+", re.sub(r"[_/.]", " ", manual))}   # a file's name said as words
        for s in self.steps[1:-1]:
            self.assertTrue(s["text"], s["id"])
            self.assertLessEqual(len(s["text"]), tour_script.CAP + 1, s["id"])
            new = {w for w in re.findall(r"[A-Za-z][A-Za-z'-]+", s["text"]) if w.lower() not in words}
            self.assertFalse(new, f"{s['id']}: words the manual does not print")

    def test_the_voice_reads_no_markup(self):
        for s in self.steps:
            for bad in ("`", "**", "#s-", ".py", ".json", "](", "<"):
                self.assertNotIn(bad, s["say"], f"{s['id']} would say {bad!r}")
            self.assertEqual(s["sha"], hashlib.sha256(s["say"].encode()).hexdigest())

    def test_spoken_units(self):
        self.assertEqual(tour_script.spoken("a decision every 60 s, the fast checks every 5 s"),
                         "a decision every 60 seconds, the fast checks every 5 seconds")
        self.assertEqual(tour_script.spoken("on omni-v24"), "on omni version 24")
        self.assertEqual(tour_script.spoken("G = (1 + ΔW) / (1 + ΔB) − 1"), "G equals (1 + delta W) over (1 + delta B) minus 1")

    def test_a_clip_is_kept_only_with_its_words(self):
        if not VOICE.exists():
            self.skipTest("no recorded voice yet: every stop is read by the browser's own voice")
        v = json.loads(VOICE.read_text(encoding="utf-8"))
        self.assertEqual(v["model_license"], "Apache-2.0")
        self.assertEqual(set(v["model_sha256"]), {"kokoro-v1.0.int8.onnx", "voices-v1.0.bin"})
        files = sorted(p.name for p in VOICE.parent.glob("*.mp3"))
        self.assertEqual(files, sorted(c["file"] for c in v["clips"].values()), "an MP3 without its record, or a record without its MP3")
        for sid, c in v["clips"].items():
            data = (VOICE.parent / c["file"]).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), c["mp3_sha256"], sid)
            self.assertEqual(len(data), c["bytes"], sid)
            self.assertRegex(c["sha"], r"^[0-9a-f]{64}$")

    def test_the_page_carries_the_tab_and_plays_a_clip_only_with_its_words(self):
        self.assertIn('id="tourTab"', self.page)
        self.assertIn('id="tourCard"', self.page)
        m = re.search(r'<script type="application/json" id="tour">(.*?)</script>', self.page, re.S)
        self.assertIsNotNone(m, "the page has no tour record")
        rec = json.loads(m.group(1))
        clips = json.loads(VOICE.read_text(encoding="utf-8"))["clips"] if VOICE.exists() else {}
        for s in rec["steps"]:
            if s["clip"]:
                self.assertEqual(clips[s["id"]]["sha"], s["sha"], f"{s['id']}: a clip that reads other words")


if __name__ == "__main__":
    unittest.main()
