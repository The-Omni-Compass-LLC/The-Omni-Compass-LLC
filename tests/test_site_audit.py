# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The graded audit of every page (the founder's order of 1 November, tools/site_audit.py): the rules read a page to the
letter (a heading's anchor as GitHub writes it, a link to a file that is not there, an outside link that is not secure), and
every page of the repository reads A."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import site_audit as SA  # noqa: E402


class TheRules(unittest.TestCase):
    def test_a_headings_anchor_is_githubs(self):
        self.assertEqual(SA.slug("The engine that stands: omni-v26 (another workload's waiting pods hold native's target)"),
                         "the-engine-that-stands-omni-v26-another-workloads-waiting-pods-hold-natives-target")
        self.assertEqual(SA.slug("**Bold** and `code` · 10 s"), "bold-and-code--10-s")
        text = "# Title\n\n## Same\n\n## Same\n\n```\n## not a heading\n```\n<a id=\"kept\"></a>\n"
        self.assertEqual(SA.anchors_md(text), {"title", "same", "same-1", "kept"})

    def test_the_grade_is_the_worst_finding(self):
        self.assertEqual(max(("C", "B"), key=SA.ORDER.index), "C")
        self.assertEqual([SA.GRADES[k] for k in ("outside", "anchor", "link", "notice", "engine")], ["B", "C", "D", "F", "F"])

    def test_a_script_is_code_not_a_link(self):
        page = '<a href="#top">x</a><script>const u = "href=\\"missing.html\\"";</script><img src="a.png">'
        self.assertEqual(SA.links_of("x.html", page), ["#top", "a.png"])


class EveryPage(unittest.TestCase):
    def test_every_page_reads_a(self):
        low = {p: v for p, v in SA.audit().items() if v["grade"] != "A"}
        self.assertEqual(low, {}, "pages below A (python3 tools/site_audit.py writes each finding with its fix)")


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
