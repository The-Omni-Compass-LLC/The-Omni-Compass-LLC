# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""tools/reproduce.py: a table rebuilt from its runs reads "same" only when every file is identical to the byte, a changed
table or an unopened run folder never reads "same", and a table of the engine that stands with no recipe is named."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import reproduce  # noqa: E402

TOOL = '''import sys
from pathlib import Path
args = sys.argv[1:]
out = Path(args[args.index("--out") + 1])
runs = [Path(a).name for a in args[:args.index("--out")]]
out.write_text("table of " + ",".join(runs) + "\\n")
out.with_suffix(".json").write_text("{}\\n")
'''


class Reproduce(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        root = Path(self.t.name)
        self.live, self.raw = root / "live", root / "live" / "raw"
        for r in ("run-1", "run-2", "run-3"):
            (self.raw / r).mkdir(parents=True)
        self.tool = root / "tool.py"
        self.tool.write_text(TOOL)
        self.recipe = {"tool": str(self.tool), "args": [], "runs": ["run-1", "run-2", "run-3"]}
        self.patch = mock.patch.multiple(reproduce, LIVE=self.live, RAW=self.raw, RECIPES=self.live / "RECIPES.json",
                                         STATE=self.live / "FRONT_PAGE_STATE.json")
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.t.cleanup()

    def rebuild(self):
        with tempfile.TemporaryDirectory() as s:
            return dict(reproduce.rebuild("V11_X", self.recipe, Path(s)))

    def test_an_identical_table_reads_same_and_a_changed_one_differs(self):
        (self.live / "V11_X.md").write_text("table of run-1,run-2,run-3\n")
        (self.live / "V11_X.json").write_text("{}\n")
        self.assertEqual(self.rebuild(), {"V11_X.json": "same", "V11_X.md": "same"})
        (self.live / "V11_X.md").write_text("table of run-1,run-2,run-3 \n")
        self.assertEqual(self.rebuild()["V11_X.md"], "differs")

    def test_a_run_folder_not_opened_is_never_same(self):
        (self.raw / "run-2").rmdir()
        res = self.rebuild()
        self.assertTrue(res["V11_X"].startswith("raw folder not opened: run-2"))

    def test_a_table_with_no_recipe_is_named(self):
        (self.live / "V11_X.md").write_text("x\n")
        (self.live / "V11_Y.md").write_text("y\n")
        (self.live / "V10_Z.md").write_text("z\n")
        (self.live / "RECIPES.json").write_text(json.dumps({"_about": "", "V11_X": self.recipe}))
        self.assertEqual(reproduce.check_recipes(11), ["V11_Y"])
        self.assertEqual(reproduce.patterns(["V11_X"]), ["/run-1/", "/run-2/", "/run-3/"])


if __name__ == "__main__":
    unittest.main()
