# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Version after version, nothing left behind (the founder's order of 18 October): tools/land_engine.py moves every place that
names the engine that stands to the next version in one command, and --check names any place still on an older one."""
import json
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import land_engine  # noqa: E402


class LandEngine(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        n = land_engine.newest()
        files = {path for path, _ in land_engine.BOOKKEEPING + land_engine.WORDS}
        files |= {"tools/layout_check.py", "tools/release_manifest.py", f"OMNI_V{n}.json", f"docs/OMNI_V{n}.md",
                  f"results/grid_v{n}/DISPATCHED.json"}
        for f in files:
            (self.root / f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / f, self.root / f)
        self.n = n

    def tearDown(self):
        self.tmp.cleanup()

    def test_the_tree_as_it_stands_is_on_its_newest_engine(self):
        self.assertEqual(land_engine.check(ROOT), [])

    def test_a_landing_moves_every_bookkeeping_place_and_names_the_words_left(self):
        n, m = self.n, self.n + 1
        with redirect_stdout(StringIO()):
            land_engine.land(m, "2030-01-01T00:00:00Z", root=self.root, fingerprint=False)
        self.assertEqual(land_engine.newest(self.root), m)
        grid = (self.root / "scripts/dispatch_grid.py").read_text()
        self.assertIn(f'"grid_v{m}"', grid)
        self.assertIn(f'ENGINE = "omni-v{m}"', grid)
        self.assertEqual(grid.count('"2030-01-01T00:00:00Z"'), 3)          # the grid, the reruns and the clouds start again
        for wf in ("grid.yml", "six.yml", "six-kube.yml"):
            self.assertIn(f"results/grid_v{m}", (self.root / ".github/workflows" / wf).read_text())
        self.assertIn(f'version = "0.{m}.0"', (self.root / "pyproject.toml").read_text())
        meta = json.loads((self.root / "codemeta.json").read_text())
        self.assertEqual(meta["softwareVersion"], f"0.{m}.0 (engine omni-v{m})")
        self.assertEqual(json.loads((self.root / f"results/grid_v{m}/DISPATCHED.json").read_text())["engine"], f"omni-v{m}")
        self.assertIn(f'"OMNI_V{n}.json", "OMNI_V{m}.json"', (self.root / "tools/layout_check.py").read_text())
        self.assertIn(f'"engine_v{m}"', (self.root / "tools/release_manifest.py").read_text())
        self.assertTrue((self.root / f"results/grid_v{n}/DISPATCHED.json").exists())   # the older engine's record stays
        left = land_engine.check(self.root)
        # what is left is the person's: the version's page, its fingerprint, and the standing pages' words
        self.assertTrue(left)
        self.assertTrue(all(any(w in b for w in ("README.md", "CLAUDE.md", "MANUAL", "LIVE_ENGINE", f"OMNI_V{m}",
                                                 "FACTORY_PROFILE", "STATE_OF_PLAY", "APPRAISAL"))
                            for b in left), left)

    def test_the_check_names_a_page_left_on_an_older_engine(self):
        p = self.root / "README.md"
        p.write_text(p.read_text().replace(f"**Engine on main:** omni-v{self.n}", f"**Engine on main:** omni-v{self.n - 1}"))
        self.assertTrue(any(b.startswith("README.md: names omni-v") for b in land_engine.check(self.root)))

    def test_only_the_next_version_lands(self):
        with self.assertRaises(SystemExit):
            land_engine.land(self.n + 2, "2030-01-01T00:00:00Z", root=self.root, fingerprint=False)


if __name__ == "__main__":
    unittest.main()
