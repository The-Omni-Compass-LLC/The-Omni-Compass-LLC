# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live benchmark engine's glossary and index (tools/live_glossary.py, the founder's words of 24 October: "a glossary and index and
what that means ... all 1,000 muscles and every other thing that should be in this"): every catalog muscle once, every term
defined and sourced in words its source still carries, the counts the catalog's own, and a file that can sit inside the page's
<script> element."""
import csv
import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
JSON = ROOT / "docs" / "engine" / "glossary.json"
MD = ROOT / "docs" / "engine" / "GLOSSARY.md"
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
CATALOG = ROOT / "realms" / "catalog_v5.csv"
REALMS = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized"]
REQUIRED = ["GAIN", "STEADY", "LOSS", "power given", "the runs disagree", "do no harm", "native", "Omni-Compass on native",
            "the compass", "the compass law", "the band", "the cushion", "the centre",
            "the two antagonist forces", "k[p]", "k[d]", "A", "tanh", "the max", "the tune-down", "the dial", "one pedal",
            "lift-off", "cruise", "the lease", "the kill switch", "the snapshot", "the two-way plug", "the four pieces",
            "piece 1, the state and the basin", "piece 2, the basin's potential and flow",
            "piece 3, the bath", "piece 4, the governor's law", "ρ*", "κ", "h", "calm", "σ",
            "ν", "the organs and their grants", "the immune system", "the nervous system", "the heat debt", "the twin",
            "the bone", "the edge", "the verdict", "the give-back trial", "the model gate", "the fingerprint and its digest",
            "the seal", "evidence classes P, L, S", "three runs A, B and C", "the 95% interval on Student's t", "the 0.5% floor",
            "the heartbeat", "the fast checks", "the conveyance", "the organism", "muscle", "realm", "family", "template",
            "knob", "the spine", "the stack", "the tower", "the orchestra", "the grid", "protocol 4",
            "the conductor", "Omni index", "the benefit board", "the traffic signal", "REDLINING", "STEADY", "GAINING",
            "native's colour", "Omni-Compass's blue", "a changed tune's violet", "the cloud as the wire",
            "the three places Omni-Compass lives", "Monte Carlo", "RK4", "the jump generator", "the C++ twin",
            "Mechanism Knobs"]


class LiveGlossary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = JSON.read_text(encoding="utf-8")
        cls.d = json.loads(cls.raw)
        cls.rows = list(csv.DictReader(CATALOG.open(encoding="utf-8")))

    def test_the_json_can_sit_inside_a_script_element(self):
        self.assertNotIn("</", self.raw, "a '</' in docs/engine/glossary.json would close the page's <script> element")
        self.assertNotIn("<!--", self.raw)
        self.assertNotIn("\n", self.raw.rstrip("\n"), "the JSON is written compact, on one line")

    def test_every_catalog_muscle_is_present_exactly_once(self):
        ids = Counter(m["id"] for m in self.d["muscles"])
        self.assertEqual([k for k, n in ids.items() if n > 1], [], "a muscle written twice")
        self.assertEqual(set(ids), {r["muscle_id"] for r in self.rows}, "the glossary's muscles are not the catalog's")
        by = {r["muscle_id"]: r for r in self.rows}
        for m in self.d["muscles"]:
            r = by[m["id"]]
            self.assertEqual((m["name"], m["family"], m["template"], m["preset"], m["knob"], m["realms"]),
                             (r["muscle"], r["family_id"], r["template"], r["preset"], r["knob"], r["realms"].split(";")), m["id"])
            self.assertTrue(m["meaning"] and m["card"], m["id"])
            self.assertTrue(0 <= m["does"] < len(self.d["does"]), m["id"])
            for k in ("template", "preset", "knob", "family"):
                self.assertIn(m[k], self.d[{"template": "templates", "preset": "presets", "knob": "knobs", "family": "families"}[k]],
                              f"{m['id']}: its {k} has no entry in the glossary's tables")
        grouped = [mid for g in self.d["groups"] for f in g["families"] for mid in f["muscles"]]
        self.assertEqual(sorted(grouped), sorted(ids), "the muscles bulked by their realms are not every muscle once")

    def test_every_family_carries_its_native_controller(self):
        recipes = {r["family"]: r for r in csv.DictReader((ROOT / "docs" / "wiring_recipes.csv").open(encoding="utf-8"))}
        for fid, f in self.d["families"].items():
            self.assertEqual(f["native"], recipes[f["name"]]["native_controller"], fid)

    def test_the_counts_match_the_catalog(self):
        c, rows = self.d["counts"], self.rows
        self.assertEqual(c["muscles"], len(rows))
        self.assertEqual(c["catalog_rows"], len(rows))
        self.assertEqual(c["families"], len({r["family_id"] for r in rows}))
        self.assertEqual(c["terms"], len(self.d["terms"]))
        self.assertEqual(c["index"], len(self.d["index"]))
        self.assertEqual(c["scenarios"], c["organisms"] * c["arms"])
        orgs = {o["key"]: o for o in self.d["organisms"]}
        self.assertEqual(list(orgs), ["spine"] + REALMS + ["stack", "tower", "orchestra", "sixty", "whole"])
        realms_of = [r["realms"].split(";") for r in rows]
        self.assertEqual(orgs["spine"]["muscles"], sum(1 for rl in realms_of if set(REALMS) <= set(rl)))
        for k in REALMS:
            self.assertEqual(orgs[k]["muscles"], sum(1 for rl in realms_of if k in rl), k)
        self.assertEqual(orgs["stack"]["muscles"], sum(len(rl) for rl in realms_of))
        self.assertEqual(orgs["tower"]["muscles"], len(rows))
        self.assertEqual(orgs["sixty"]["muscles"], 60)
        self.assertEqual([len(p["muscles"]) for p in orgs["sixty"]["parts"]], [12] * 5)
        from tools.run_orchestra import bodies
        self.assertEqual(orgs["orchestra"]["muscles"], len(bodies(rows)["orchestra"]))
        self.assertIsNone(orgs["whole"]["muscles"])
        self.assertEqual([s["key"] for s in orgs["whole"]["sectors"]], ["software", "cloud", "hardware"])
        for o in self.d["organisms"]:
            if o["muscles"] is not None:
                self.assertEqual(sum(f["n"] for f in o["families"]), o["muscles"], o["key"])
        member = Counter(k for m in self.d["muscles"] for k in m["organisms"])
        for k in ["spine"] + REALMS + ["tower", "orchestra", "sixty"]:
            self.assertEqual(member[k], orgs[k]["muscles"], f"the muscles marked {k} are not the organism's count")
        self.assertEqual([a["key"] for a in self.d["arms"]], ["native", "omni"])
        self.assertEqual(len({s["key"] for s in self.d["scenarios"]}), len(self.d["scenarios"]))

    def test_every_term_has_a_definition_and_a_source_that_still_says_it(self):
        from tools.live_glossary import quote_found
        names = [t["term"] for t in self.d["terms"]]
        self.assertEqual([n for n, k in Counter(names).items() if k > 1], [], "a term written twice")
        self.assertEqual([t for t in REQUIRED if t not in names], [], "a term the live benchmark engine's reader meets is missing")
        for item in self.d["terms"] + self.d["organisms"] + self.d["arms"]:
            name = item.get("term") or item["name"]
            self.assertTrue((item.get("def") or item.get("meaning") or "").strip(), f"{name}: no definition")
            self.assertTrue(item["sources"], f"{name}: no source")
            for s in item["sources"]:
                self.assertTrue((ROOT / s["file"]).is_file(), f"{name}: {s['file']} does not exist")
                self.assertTrue(quote_found(s["file"], s["quote"]), f"{name}: {s['file']} no longer says {s['quote']!r}")

    def test_the_index_points_at_sections_the_page_has(self):
        page = PAGE.read_text(encoding="utf-8")
        ids = set(re.findall(r'<section\b[^>]*\bid="(s-[^"]+)"', page))
        listed = {s["id"] for s in self.d["sections"]}
        self.assertTrue(self.d["index"], "the index is empty")
        known = {t["term"] for t in self.d["terms"]} | {o["name"] for o in self.d["organisms"]} | {a["name"] for a in self.d["arms"]}
        for e in self.d["index"]:
            self.assertIn(e["term"], known)
            self.assertTrue(e["anchors"], e["term"])
            for a in e["anchors"]:
                self.assertTrue(a.startswith("s-"), a)
                self.assertIn(a, listed, f"{e['term']}: {a} is not among the glossary's sections")
                self.assertIn(a, ids, f"{e['term']}: the page has no section {a}")

    def test_the_readable_page_carries_the_notice_and_every_muscle(self):
        md = MD.read_text(encoding="utf-8")
        from tools.legal import CLOSE
        self.assertTrue(md.rstrip().endswith(CLOSE + "*"), "the notice closes the page")
        self.assertIn(CLOSE, md.split("\n## ", 1)[0], "the notice opens the page")
        self.assertIn(self.d["notice"], self.raw)
        muscles = md.split("\n## 5. ", 1)[1].split("\n## 6. ", 1)[0]
        rows_in_md = Counter(re.findall(r"^\| ([0-9A-Z][0-9A-Z-]*) \| ", muscles, re.M))
        self.assertEqual([k for k, n in rows_in_md.items() if n > 1], [], "GLOSSARY.md lists a muscle twice")
        self.assertEqual(set(rows_in_md), {r["muscle_id"] for r in self.rows}, "GLOSSARY.md does not list every muscle")

    def test_the_glossary_never_reads_itself_back_as_the_page(self):
        from tools.live_glossary import strip_glossary
        page = '<section class="stack" id="s-a"><h2>A</h2><p>the page</p></section>'
        embedded = (page + '<script type="application/json" id="glossary">' + self.raw.strip() + "</script>"
                    + '<section class="stack" id="s-glossary"><h2>Glossary</h2><section id="s-x">GAIN</section></section>')
        self.assertEqual(strip_glossary(embedded), page)

    def test_the_files_are_what_the_repository_gives_now(self):
        from tools.live_glossary import build_core
        core = build_core()
        for k in ("muscles", "terms", "organisms", "arms", "scenarios", "groups"):
            self.assertEqual(json.loads(json.dumps(core[k], ensure_ascii=False)), self.d[k],
                             f"docs/engine/glossary.json's {k} are stale: python3 tools/live_glossary.py")


if __name__ == "__main__":
    unittest.main()
