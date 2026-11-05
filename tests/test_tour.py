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
        sections = re.findall(tour_script.SECTION, self.page)
        for sid in ("s-decision", "title-page", "s-disclose"):   # 5 November: the trio, the title page and the disclosures are stops too
            self.assertIn(sid, sections)
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

    def _tour_code(self):
        a, b = self.page.index("const TOUR = {"), self.page.index("function eqLive() {")
        return self.page[a:b]

    def test_the_opening_names_the_cards_own_buttons(self):
        """4 November: the opening told the reader to use Next and Back and that Play steps through on its own; the card had
        neither a Back button nor a Play that stepped on, and the reader was left asking what to click. Every control the
        opening names is a button the card draws, by the name it wears."""
        code = self._tour_code()
        for said, label in (("Play", "▶ Play"), ("Continue", "▶ Continue"), ("Pause", "⏸ Pause"), ("back ten seconds", "⏪ 10 s"),
                            ("forward ten seconds", "10 s ⏩"), ("Replay", "↺ Replay"), ("Stop", "■ Stop"), ("Back", "◀ Back"),
                            ("Skip", "Skip ▶"), ("question mark", 'id="tHelp"'), ("Step on by itself", "Step on by itself: "),
                            ("Close", "Close ✕")):
            with self.subTest(said=said):
                self.assertIn(said, tour_script.OPEN, f"the opening does not name {said}")
                self.assertIn(label, code, f"the card draws no {label!r} button")
        for gone in ("Use Next and Back", "Play steps through on its own", "Previous stop and Next stop", "blue button"):
            self.assertNotIn(gone, tour_script.OPEN)

    def test_the_reader_may_leave_and_hears_what_to_press(self):
        """5 November (the founder's words): the opening says this is the tour and that the reader may explore by hand; the blue
        tab sits by the dock's Tour button and bounces on the landing view; when a stop ends the voice says which button does what."""
        self.assertIn("leave it at any moment and explore the page by hand", tour_script.OPEN)
        nv = tour_script.nav()
        for said in ("green circle, Skip", "yellow diamond, Replay", "red stop sign, Back", "blue question mark"):
            self.assertIn(said, nv["text"])
        code = self._tour_code()
        self.assertIn("function tourNavSay(tok, go)", code)
        self.assertIn("function tourPlaceTab()", code)
        self.assertIn("body.tourInvite #tourTab{animation:tourBounce", self.page)

    def test_the_buttons_wear_the_signs_and_the_hand_moves_with_the_voice(self):
        """5 November (the founder's words): Back a red stop sign, Replay a yellow yield diamond, Play and Skip green, the
        question blue; a list of every stop showing the one being read; the whole voice loaded in one go; a hand that scrolls
        the page and points with the voice, and opens only what opening is all a press does."""
        code = self._tour_code()
        page = PAGE.read_text(encoding="utf-8")
        for cls, label in (("tsig tred", "◀ Back"), ("tsig tyel", "↺ Replay"), ("tsig tgrn", "Skip ▶"), ("tsig tblu", "?</button>")):
            self.assertRegex(code, re.escape(f'class="{cls}"') + r'[^`]*' + re.escape(label), f"{label} wears no {cls}")
        self.assertIn('id="tPause" class="tsig tgrn"', code, "Play is the green go button")
        self.assertIn("#tourCard .tsig.tred .tsh{clip-path:var(--oct)", page, "red only as a stop sign: Back's mark is an octagon")
        self.assertIn("#tourCard .tsig.tyel .tsh{clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%)", page, "Replay's mark is a diamond")
        self.assertIn("#tourCard .tsig.tgrn .tsh{border-radius:50%", page, "Skip's mark is a circle")
        self.assertIn('<select id="tJump"', code, "no list of every stop")
        self.assertIn('$("tJump").addEventListener("change", e => tourShow(+e.target.value, true));', code)
        self.assertIn("function tourPreload()", code)
        self.assertIn("tourShow(at, \"play\");   // the press that opened the tour is the press a browser waits for before it plays sound\n  tourPreload();", code)
        self.assertIn("if (pre && !usedPre) { usedPre = true; TOUR.tryBase = TOUR.base; src = pre; }", code, "a loaded clip is played from this browser")
        self.assertIn("function tourFollow(k)", code)
        self.assertIn("if (moved && TOUR.playing) tourFollow(k);", code, "the lit sentence moves the page")
        safe = re.search(r"const TOUR_SAFE = el => (.*?);   // opening, never a switch", code, re.S)
        self.assertIsNotNone(safe, "the hand has no rule for what it may open")
        for word in ("kill", "surge", "lose", "factory", "native", "stop"):
            self.assertIn(word, safe.group(1), f"the hand could press a {word} switch")

    def test_the_card_never_sits(self):
        """4 November: the tour read its opening and sat. A clip that failed to load, a browser voice that never started, or a
        browser that plays sound only after a press left no clock moving the card, and the refusal turned Step on by itself
        off. Now a reading clock moves the card from the first moment, every voice has a watchdog, and a refusal lights Play."""
        code = self._tour_code()
        self.assertIn("setInterval(tourTick, 250)", code, "no clock ticks the card")
        self.assertRegex(code, r"function tourFrom\(pos, byPress\) \{[^\n]*\n(?:[^\n]*\n){0,4}\s*tourReadOn\(pos\)",
                         "a stop must start its reading clock before any voice is tried")
        self.assertRegex(code, r"TOUR\.mode === \"read\" && TOUR\.playing && p >= d - 0\.05\) \{ tourAfter\(\)",
                         "the reading clock must end the stop on time")
        refusal = re.search(r'err\.name === "NotAllowedError"\) \{(.*?)\} \}\); \};', code, re.S)
        self.assertIsNotNone(refusal, "the recorded voice's refusal is not handled")
        self.assertIn("TOUR.need = true", refusal.group(1), "a refusal must light Play")
        self.assertNotIn("TOUR.auto = false", refusal.group(1), "a refusal must not stop the tour stepping on")
        self.assertIn("tneed", code)
        self.assertIn("No sound yet: this browser plays sound only after a press. Press the lit green ▶ Play", code)
        for dog in ("}, 5000);", "}, 4500);", "now - TOUR.lastTAt > 8000"):
            self.assertIn(dog, code, f"a voice without its watchdog: {dog}")
        # each address of the recorded voice is tried once: only the error event moves to the next one
        self.assertRegex(code, r"a\.onerror = \(\) => \{ if \(mine\(\) && !heard\) next\(\); \};")
        self.assertNotRegex(code, r"\.catch\(err => \{[^}]*else go\(\)", "a failed play may not try the next address a second time")
        # the browser's own voice reads one sentence at a time, each with its own watchdog
        self.assertIn("const say = k => {", code)
        self.assertIn("say(k + 1)", code)
        self.assertNotIn('aria-live="polite"></div>', self.page.split('id="tourCard"', 1)[1][:120],
                         "the whole card may not be a live region: a screen reader would read the clock four times a second")


if __name__ == "__main__":
    unittest.main()
