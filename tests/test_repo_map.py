# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The map of the repository (tools/repo_map.py): every ID is kept for life and never given twice, a new file takes its
area's next number, a file that leaves keeps its ID among the retired, every file names its owner, and the LICENSE and
its copy for the scanners say the same."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import repo_map  # noqa: E402


class RepoMap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = json.loads(repo_map.REGISTER.read_text(encoding="utf-8"))

    def test_the_stored_map_is_whole_and_current(self):
        self.assertEqual(repo_map.main(["--check"]), 0)

    def test_every_id_is_well_formed_and_given_once(self):
        ids = [e["id"] for e in list(self.reg["files"].values()) + list(self.reg["retired"].values())]
        self.assertTrue(all(repo_map.ID_RE.match(i) for i in ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_file_names_its_owner(self):
        for path, e in self.reg["files"].items():
            self.assertTrue(e["owner"] == repo_map.OWNER or path.startswith(repo_map.THIRD_PARTY), path)

    def test_an_id_is_kept_a_new_file_takes_the_next_and_a_gone_file_is_retired(self):
        reg = copy.deepcopy(self.reg)
        paths = list(reg["files"])
        gone, kept = paths[0], paths[1]
        before = reg["files"][kept]["id"]
        area = "OC-" + repo_map.area_of("docs/NEW_PAGE_FOR_THE_TEST.md")
        top = max(int(e["id"].rsplit("-", 1)[1]) for e in list(reg["files"].values()) + list(reg["retired"].values())
                  if e["id"].startswith(area + "-"))
        live = [p for p in paths if p != gone] + ["docs/NEW_PAGE_FOR_THE_TEST.md"]
        orig_role, orig_carried = repo_map.role_of, repo_map.carried
        repo_map.role_of, repo_map.carried = (lambda p: ""), (lambda p, locked: (repo_map.OWNER, "test"))
        try:
            out = repo_map.assign(reg, live)
        finally:
            repo_map.role_of, repo_map.carried = orig_role, orig_carried
        self.assertEqual(out["files"][kept]["id"], before)
        self.assertEqual(out["files"]["docs/NEW_PAGE_FOR_THE_TEST.md"]["id"], f"{area}-{top + 1:05d}")
        self.assertIn(gone, out["retired"])
        self.assertNotIn(gone, out["files"])

    def test_the_license_and_its_copy_for_the_scanners_say_the_same(self):
        self.assertEqual((ROOT / "LICENSE").read_text(encoding="utf-8"),
                         (ROOT / "LICENSES" / "LicenseRef-OmniCompass-Evaluation-1.0.txt").read_text(encoding="utf-8"))

    def test_the_license_names_the_paid_pilot_and_every_owner_entity(self):
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("5.4 A pilot.", text)
        self.assertIn("Omni-Compass Entity", text)


if __name__ == "__main__":
    unittest.main()
