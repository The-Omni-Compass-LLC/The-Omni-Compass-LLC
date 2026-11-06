# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live engine keeps itself current wherever it is shown (the founder's order of 1 November): the page is rebuilt on
GitHub every three hours and after every result, and every copy of it, the company's website's included, reads the newest
build's stamp from the repository when it opens and every 24 hours after, and loads the newer build in place
(docs/engine/build_live_engine.py self_update, write_version; docs/engine/LIVE_ENGINE_VERSION.json)."""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
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

    def test_the_newer_build_opens_in_a_document_of_its_own(self):
        # 1 November: written over the open page with document.write, the newer build's script met the open page's own
        # top-level declarations ("Identifier 'HBS_G' has already been declared") and every frame after it failed
        self.assertNotIn("document.write", ble.SELF_UPDATE)
        self.assertIn("URL.createObjectURL(new Blob([html]", ble.SELF_UPDATE)
        self.assertIn("location.replace(", ble.SELF_UPDATE)
        # 6 November, the software seat: a page cut short, or with a fault in its script, opened over a working copy and called
        # itself the newest build. It opens only with its stamp's byte count and sha256, its build the stamp's, every script
        # compiling; a build whose engine does not start sends the tab back; a failed check is asked again within the hour
        for s in ('crypto.subtle.digest("SHA-256"', "v.bytes", "v.sha256", "new Function(", "HOUR = 3600 * 1000", "function settle()"):
            self.assertIn(s, ble.SELF_UPDATE)
        self.assertNotIn("900000", ble.SELF_UPDATE)

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
        data = ble.PAGE.read_bytes()
        self.assertEqual((v["bytes"], v["sha256"]), (len(data), hashlib.sha256(data).hexdigest()))   # the page as it stands on disk
        self.assertTrue(v["page_url"].endswith("docs/engine/OMNI_COMPASS_LIVE_ENGINE.html"))

    def test_the_stamp_is_committed_with_every_rebuild(self):
        wf = (ROOT / ".github" / "workflows" / "live-engine.yml").read_text()
        self.assertIn("docs/engine/LIVE_ENGINE_VERSION.json", wf)
        self.assertRegex(wf, r'cron: "41 \*/3 \* \* \*"')                         # rebuilt every three hours on GitHub
        stamp = json.loads((ROOT / "docs" / "engine" / "LIVE_ENGINE_VERSION.json").read_text())
        self.assertEqual(stamp["built_at"], ble.embedded(PAGE, "build")["built_at"])

    def test_the_page_carries_its_identity_and_the_stamp_names_it(self):
        # 6 November, the software seat: four different pages carried one build time, so copies of three of them never loaded the newest.
        # The page carries its own identity (the sha256 of its bytes with the identity read as zeros), the stamp names it, and a copy
        # decides by it; zeros only until the build's stamp first writes it
        head = PAGE[:PAGE.index("</head>")]
        ids = re.findall(r'<meta name="omni-page-id" content="([0-9a-f]{64})">', head)
        self.assertEqual(len(ids), 1, "one identity tag, in the head")
        data = ble.PAGE.read_bytes()
        stamp = json.loads((ROOT / "docs" / "engine" / "LIVE_ENGINE_VERSION.json").read_text())
        if ids[0] != "0" * 64:
            self.assertEqual(ids[0], ble.page_id(data), "the page changed after its identity was written: run build_live_engine.py --stamp")
        if stamp.get("page_id"):
            self.assertEqual((stamp["page_id"], stamp["bytes"], stamp["sha256"]), (ids[0], len(data), hashlib.sha256(data).hexdigest()),
                             "the stamp names the page as committed: run docs/engine/build_live_engine.py --stamp after every writer of the page")
        for s in ("ownId()", "v.page_id", "idOf(html)", 'mem("opening", { sha: x.v.sha256', "homeLink(p.back)", "started()"):
            self.assertIn(s, ble.SELF_UPDATE)

    def test_the_identity_is_written_once_and_follows_every_byte(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "page.html"
            p.write_bytes(b'<html><head><meta name="omni-page-id" content="' + b"0" * 64 + b'"></head><body>one</body></html>')
            a = ble.stamp_page_id(p)
            once = p.read_bytes()
            self.assertRegex(a, r"^[0-9a-f]{64}$")
            self.assertIn(a.encode(), once)
            self.assertEqual((ble.stamp_page_id(p), p.read_bytes()), (a, once), "stamped again, nothing changes")
            p.write_bytes(once.replace(b"one", b"two"))
            self.assertNotEqual(ble.stamp_page_id(p), a, "one byte changed, another identity")
            self.assertEqual(len(p.read_bytes()), len(once), "the identity is written 64 characters for 64")

    def test_every_script_the_page_runs_compiles(self):
        # 6 November, the software seat: no check compiled the page's scripts, so a fault in one could be committed and stop the engine
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        i, n = 0, 0
        while True:
            a = PAGE.find("<script", i)
            if a < 0:
                break
            g = PAGE.index(">", a)
            z = PAGE.index("</script>", g)
            i = z + 9
            attrs = PAGE[a + 7:g]
            if "src=" in attrs or ("type=" in attrs and "javascript" not in attrs):
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
                f.write(PAGE[g + 1:z])
            r = subprocess.run([node, "--check", f.name], capture_output=True, text=True)
            os.unlink(f.name)
            n += 1
            self.assertEqual(r.returncode, 0, f"the script at character {a:,} does not compile: {r.stderr[:400]}")
        self.assertGreaterEqual(n, 4, "the self-update, the wallpaper, the first row and the engine")


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
