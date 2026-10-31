# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every monitor of the live benchmark engine is registered, on the wall, knobbed and in the Grafana dashboard (the founder's order of 20
October: every monitor numbered, on the wall, with its own knobs and its open-source feed)."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
REG = ROOT / "docs" / "engine" / "monitors.json"


class LiveMonitors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        page = PAGE.read_text(encoding="utf-8")
        cls.body = re.sub(r'<script type="application/json" id="[^"]+">.*?</script>', "", page, flags=re.S)
        cls.canvases = [c for c in re.findall(r'<canvas id="([A-Za-z0-9_-]+)"', cls.body) if c != "wallCv"]
        cls.reg = json.loads(REG.read_text(encoding="utf-8"))

    def test_every_canvas_is_a_registered_monitor(self):
        ids = {m["id"] for m in self.reg["monitors"]}
        self.assertEqual(sorted(set(self.canvases) - ids), [], "a canvas on the page with no entry in docs/engine/monitors.json")
        self.assertEqual(sorted(ids - set(self.canvases)), [], "a registered monitor with no canvas on the page")

    def test_every_monitor_is_on_the_wall(self):
        wall = re.search(r"const WALL = \{.*?reg: \[(.*?)\]\]\};", self.body, re.S)
        self.assertIsNotNone(wall)
        on = set(re.findall(r'\["([A-Za-z0-9_-]+)",', wall.group(1)))
        self.assertEqual(sorted(set(self.canvases) - on), [], "a monitor missing from the wall")

    def test_every_knob_is_in_the_catalog(self):
        cat = set(self.reg["knobs"])
        for m in self.reg["monitors"]:
            self.assertTrue(set(m["knobs"]) <= cat, (m["id"], set(m["knobs"]) - cat))
            self.assertIn(m["layer"], self.reg["layers"], m["id"])

    def test_the_grafana_wall_has_a_panel_a_monitor(self):
        d = json.loads((ROOT / "deploy" / "grafana" / "omni-compass-wall.json").read_text(encoding="utf-8"))
        # 9000 and 9001: the legal notice at the wall's top and end; 899 to 904: the signals row (export_grafana.signals_row)
        mons = [p for p in d["panels"] if p["type"] != "row" and p.get("id", 0) < 9000 and not 899 <= p.get("id", 0) <= 904]
        self.assertEqual(len(mons), len(self.reg["monitors"]))
        notes = [p for p in d["panels"] if p.get("id", 0) >= 9000]
        self.assertEqual([p["id"] for p in notes], [9000, 9001])
        self.assertTrue(all("www.omni-compass.com" in p["options"]["content"] for p in notes))
        for p in mons:
            if p["type"] != "text":
                self.assertTrue(p["targets"] and all(t["expr"] for t in p["targets"]), p["title"])

    def test_every_grafana_panel_sits_under_its_section(self):
        """The founder's orders of 21 and 30 October: every panel numbered as the wall numbers its monitor, by importance, under the
        row of its block of the wall; its section named in its description."""
        sys.path.insert(0, str(ROOT / "docs" / "engine"))
        import export_grafana as XGF
        sec = XGF.page_sections()
        d = json.loads((ROOT / "deploy" / "grafana" / "omni-compass-wall.json").read_text(encoding="utf-8"))
        order = {c: i for i, c in enumerate(XGF.wall_order())}
        ids = [m["id"] for m in sorted(self.reg["monitors"], key=lambda m: order.get(m["id"], len(order)))]
        blocks = {i: (k, b["title"]) for k, b in enumerate(self.reg.get("blocks", []), 1) for i in b["ids"]}
        row, n = None, 0
        for p in d["panels"]:
            if p["type"] == "row":
                row = p["title"]
                continue
            if 899 <= p.get("id", 0) <= 904:  # the signals row, the governor's own state, under its own row before the sections
                continue
            if p.get("id", 0) >= 9000:      # the legal notice's two panels, at the wall's top and end
                continue
            n += 1
            cid = ids[n - 1]
            self.assertTrue(p["title"].startswith(f"{n} · "), p["title"])
            want = f"Block {blocks[cid][0]} · {blocks[cid][1]}" if cid in blocks else f"{sec[cid][0]} · {sec[cid][1]}"
            self.assertEqual(row, want, (cid, row))   # each panel under its block of the wall (the founder's order of 30 October)

    def test_every_monitor_is_in_a_numbered_section(self):
        sys.path.insert(0, str(ROOT / "docs" / "engine"))
        import export_grafana as XGF
        sec = XGF.page_sections()
        self.assertEqual([c for c in self.canvases if not sec.get(c, ("", ""))[0]], [], "a monitor outside every numbered section")

    def test_every_section_closes_what_it_opens(self):
        """A closing tag too many once ended section 4 early and left the scale-out grid and every section after it outside the
        page's frame (found 21 October): inside each section the divs open and close in balance, and none closes what it did not open."""
        body = re.sub(r"<!--.*?-->", "", re.sub(r"<script[^>]*>.*?</script>", "", PAGE.read_text(encoding="utf-8"), flags=re.S), flags=re.S)
        depth, opened = 0, []
        for t in re.finditer(r"<(/?)(div|section)\b[^>]*>", body):
            close, tag = t.group(1) == "/", t.group(2)
            if tag == "section":
                if close:
                    self.assertEqual(depth, opened.pop(), "a section closed with a div still open inside it")
                else:
                    opened.append(depth)
            else:
                depth += -1 if close else 1
                self.assertGreaterEqual(depth, opened[-1] if opened else 0, f"a closing div with no div open in its section, near offset {t.start()}")
        self.assertEqual((depth, opened), (0, []))

    def test_every_monitor_names_its_wiring(self):
        """The founder's order of 21 October: every monitor confirmed, its code to its Python to its C++, lined up. Each monitor names
        the page's own code (every function present in the page's script), the Python it ports or reads, the C++ twin or why there is
        none, the checks that hold them equal and how it moves; every file named is in the repository."""
        for m in self.reg["monitors"]:
            w = m.get("wire") or {}
            self.assertTrue(w.get("code") and w.get("moves"), m["id"])
            for fn in (f.strip() for f in w["code"].split(",")):
                self.assertRegex(self.body, rf"(function {fn}\(|const {fn} = )", (m["id"], fn))
            self.assertTrue(w.get("cpp") or w.get("cpp_none"), (m["id"], "a C++ twin, or why there is none"))
            for k in ("python", "cpp", "proof"):
                for p in w.get(k, []):
                    self.assertTrue((ROOT / p).exists(), (m["id"], k, p))

    def test_the_kill_switch_words(self):
        self.assertIn('class="onword">ON</span>', self.body)
        self.assertIn('class="offword">OFF</span>', self.body)
        self.assertIn('<h2 class="tocH">Contents</h2>', self.body)


if __name__ == "__main__":
    unittest.main()
