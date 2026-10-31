# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live benchmark engine's table of contents is its headings (the structure referee of 22 October: nineteen entries differed from the
headings they pointed at): every entry that points at a section or a part carries that section's heading or that part's title,
word for word, and every entry's target exists on the page."""
import html
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"


class LiveContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        page = PAGE.read_text(encoding="utf-8")
        cls.body = re.sub(r'<script type="application/json" id="[^"]+">.*?</script>', "", page, flags=re.S)
        a = cls.body.index('<nav class="toc" id="contents"'); b = cls.body.index("</nav>", a)
        cls.entries = re.findall(r'<a href="#([A-Za-z0-9-]+)"><span class="tn">([^<]*)</span><span class="tt">([^<]*)</span>', cls.body[a:b])

    def heading_of(self, sid):
        i = self.body.find(f'id="{sid}"')
        self.assertGreaterEqual(i, 0, f"the contents point at #{sid}, which is not on the page")
        if sid.startswith("p-"):
            m = re.search(r'<span class="pt">(.*?)</span>', self.body[i:i + 400])
            return html.unescape(m.group(1)) if m else None
        win = self.body[i:i + 2000]
        win = win[:win.find("<section", 1)] if win.find("<section", 1) > 0 else win   # its own element only, never the next section's heading
        m = re.search(r"<h2[^>]*>(.*?)</h2>", win, re.S)
        if not m:
            return None
        return html.unescape(re.sub(r"<[^>]+>", "", re.sub(r'<span class="sn">.*?</span>', "", m.group(1)))).strip()

    def test_every_entry_is_its_heading(self):
        self.assertGreater(len(self.entries), 30)
        for sid, tn, tt in self.entries:
            h = self.heading_of(sid)
            if h is None:                      # the front and back matter carry no numbered heading of their own
                continue
            self.assertEqual(html.unescape(tt), h, f"contents entry {tn} (#{sid})")


if __name__ == "__main__":
    unittest.main()
