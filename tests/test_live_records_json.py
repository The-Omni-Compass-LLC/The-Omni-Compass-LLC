# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every record the live engine page carries is JSON a browser reads (4 November: one Azure run of a single repetition put NaN
in the ledger, JSON.parse refused the whole build record and the page stopped starting up), and the full rebuild writes every
record the check reads (the tour, the bills and the law's wires had been written once by hand and never rebuilt)."""
import json
import math
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "docs" / "engine"))
import build_live_engine as B  # noqa: E402

PAGES = (ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html",)   # the website's copy packs these same records, compressed


def _strict(text):
    def refuse(c):
        raise ValueError(f"{c} is not JSON")
    return json.loads(text, parse_constant=refuse)


class Records(unittest.TestCase):
    def test_every_record_is_json_a_browser_reads(self):
        for page in PAGES:
            s = page.read_text(encoding="utf-8")
            found = re.findall(r'<script type="application/json" id="([a-z]+)">(.*?)</script>', s, re.S)
            self.assertGreater(len(found), 20, page.name)
            for key, text in found:
                with self.subTest(page=page.name, record=key):
                    _strict(text)

    def test_a_number_that_is_not_finite_is_written_null(self):
        page = '<script type="application/json" id="harness">{}</script>'
        out = B.inject(page, "build", {"ci95": [math.nan, math.inf], "x": [1.5, -math.inf], "n": 2})
        rec = _strict(out.split('id="build">', 1)[1].split("</script>", 1)[0])
        self.assertEqual(rec, {"ci95": [None, None], "x": [1.5, None], "n": 2})

    def test_the_rebuild_writes_every_record_it_checks(self):
        src = (ROOT / "docs" / "engine" / "build_live_engine.py").read_text(encoding="utf-8")
        self.assertIn("    for k in rec:", src, "the rebuild must write every record, not a list that can leave one out")
        self.assertIn('bad = [k for k in rec if k != "build"', src, "the check must read every record")


if __name__ == "__main__":
    unittest.main()
