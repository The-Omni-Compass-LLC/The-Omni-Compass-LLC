# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every run that hands in files is archived with the code by itself (the founder's order of 19 October).

archive-run.yml takes, every hour, every finished run of the workflows it lists onto the branch raw. A workflow that
uploads files and is missing from that list would leave its runs in GitHub's artifact store, where they expire; so every
workflow that uploads files is either listed or named here as a report or a check that hands in no run of its own."""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
ARCHIVE = WORKFLOWS / "archive-run.yml"
# these upload files of their own making, never a benchmark run's: a report that reads another run's stored files, and
# the check run on a push of the AKS client
NOT_RUNS = {"pod-report.yml", "aks-client-check.yml"}


def listed():
    return set(yaml.safe_load(ARCHIVE.read_text())["env"]["ARCHIVE_WORKFLOWS"].split())


class ArchiveSweep(unittest.TestCase):
    def test_every_workflow_that_hands_in_files_is_archived(self):
        uploads = {p.name for p in WORKFLOWS.glob("*.yml") if "actions/upload-artifact" in p.read_text()}
        self.assertEqual(sorted(uploads - NOT_RUNS - listed()), [])

    def test_every_listed_workflow_exists_and_hands_in_files(self):
        for name in sorted(listed()):
            with self.subTest(workflow=name):
                p = WORKFLOWS / name
                self.assertTrue(p.exists())
                self.assertIn("actions/upload-artifact", p.read_text())

    def test_it_runs_by_itself_and_takes_failed_runs_too(self):
        d = yaml.safe_load(ARCHIVE.read_text())
        self.assertIn("schedule", d[True])                       # PyYAML reads the key `on` as True
        body = ARCHIVE.read_text()
        self.assertIn('select(.conclusion != "skipped")', body)       # a cancelled run with files is taken (24 October)
        self.assertNotIn('.conclusion != "cancelled"', body)
        self.assertRegex(body, r'ARCHIVE_SINCE: "2026-10-18T16:06:00Z"')

    def test_a_pass_frees_the_disk_after_each_run(self):
        body = ARCHIVE.read_text()
        save = body.index("raw_archive.sh save")
        self.assertRegex(body[save:], r'\n\s+rm -rf "\$d"\s+#')


if __name__ == "__main__":
    unittest.main()
