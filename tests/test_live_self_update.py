# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live engine keeps itself current wherever it is shown (the founder's order of 1 November): the page is rebuilt on
GitHub every three hours and after every result, and every copy of it, the company's website's included, reads the newest
build's stamp from the repository when it opens and every 24 hours after, and loads the newer build in place
(docs/engine/build_live_engine.py self_update, write_version; docs/engine/LIVE_ENGINE_VERSION.json)."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.repo import HOME, RAW_MAIN  # noqa: E402

spec = importlib.util.spec_from_file_location("build_live_engine", ROOT / "docs" / "engine" / "build_live_engine.py")
ble = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ble)
PAGE = (ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html").read_text(encoding="utf-8")


class SelfUpdate(unittest.TestCase):
    def test_the_page_carries_its_link_and_script_once_in_its_head(self):
        self.assertEqual(ble.self_update(PAGE), PAGE, "the page is built with its self-update, exactly as written")
        head = PAGE[:PAGE.index("</head>")]
        self.assertEqual(head.count('<meta name="omni-live-source"'), 1)
        self.assertEqual(head.count('<script id="omniSelfUpdate">'), 1)
        self.assertIn(f'content="{RAW_MAIN}docs/engine/"', head)
        self.assertTrue(RAW_MAIN.startswith("https://raw.githubusercontent.com/") and HOME in RAW_MAIN)

    def test_the_script_reads_the_build_record_the_page_carries(self):
        build = ble.embedded(PAGE, "build")
        self.assertTrue(build and build.get("built_at"), "the page's build record holds the time it was built")
        self.assertIn('getElementById("build")', ble.SELF_UPDATE)
        self.assertIn("24 * 3600 * 1000", ble.SELF_UPDATE)                        # every 24 hours, and at every opening
        self.assertIn("LIVE_ENGINE_VERSION.json", ble.SELF_UPDATE)
        self.assertNotIn("POST", ble.SELF_UPDATE)                                  # it only reads

    def test_a_rebuild_keeps_one_copy_however_often_it_runs(self):
        once = ble.self_update(PAGE)
        self.assertEqual(ble.self_update(once), once)
        bare = once.replace(ble.SELF_UPDATE + "\n", "")
        self.assertEqual(ble.self_update(bare), once)

    def test_the_stamp_names_the_engine_the_time_and_the_page(self):
        with tempfile.TemporaryDirectory() as d:
            keep = ble.VERSION
            try:
                ble.VERSION = Path(d) / "LIVE_ENGINE_VERSION.json"
                ble.write_version({"engine": "omni-v23", "digest": "c96ea4105d8747db", "commit": "abc", "built_at": "2026-11-01 18:00 UTC"})
                v = json.loads(ble.VERSION.read_text())
            finally:
                ble.VERSION = keep
        self.assertEqual((v["engine"], v["built_at"]), ("omni-v23", "2026-11-01 18:00 UTC"))
        self.assertTrue(v["page_url"].endswith("docs/engine/OMNI_COMPASS_LIVE_ENGINE.html"))

    def test_the_stamp_is_committed_with_every_rebuild(self):
        wf = (ROOT / ".github" / "workflows" / "live-engine.yml").read_text()
        self.assertIn("docs/engine/LIVE_ENGINE_VERSION.json", wf)
        self.assertRegex(wf, r'cron: "41 \*/3 \* \* \*"')                         # rebuilt every three hours on GitHub
        stamp = json.loads((ROOT / "docs" / "engine" / "LIVE_ENGINE_VERSION.json").read_text())
        self.assertEqual(stamp["built_at"], ble.embedded(PAGE, "build")["built_at"])


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
