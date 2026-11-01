# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The security scan's workflow fails when its check fails (31 October): the check ran through tee with no pipefail, so the
step read tee's exit and an unreviewed finding of medium severity (four stood on main) never failed it. Every step that
pipes a check into tee keeps the check's exit."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.security_scan import REVIEWED  # noqa: E402


class ScanFails(unittest.TestCase):
    def test_every_check_piped_into_tee_keeps_its_exit(self):
        text = (ROOT / ".github" / "workflows" / "security-scan.yml").read_text()
        steps = re.split(r"\n      - ", text)
        piped = [s for s in steps if re.search(r"--check\b.*\| tee|pip_audit.*\| tee", s)]
        self.assertEqual(len(piped), 2)                        # the static scan and the dependency audit
        for s in piped:
            with self.subTest(step=s.splitlines()[0]):
                self.assertIn("set -o pipefail", s)

    def test_the_check_reads_the_findings_never_the_counts_every_push_moves(self):
        from tools.security_scan import substance
        page = ("over every Python file that runs (`tools/`; 37,470 lines). **2 findings of high severity and 35 of medium "
                "severity, every one reviewed below; 350 of low severity, counted by kind.**\n"
                "| B310 (Audit url open) | `tools/a.py` | medium | 2 (46, 90) | the GitHub API |\n"
                "## Findings of low severity, by kind\n| B603 subprocess | 154 |\nThe low-severity kinds are ...\n")
        moved = page.replace("37,470", "38,001").replace("(46, 90)", "(51, 97)").replace("350 of low", "410 of low").replace("| 154 |", "| 160 |")
        self.assertEqual(substance(page), substance(moved))          # a push that shifts lines is not a finding
        added = page.replace("| medium | 2 (46, 90) |", "| medium | 3 (46, 90, 120) |")
        self.assertNotEqual(substance(page), substance(added))       # a new finding of medium severity is
        reviewed = page.replace("the GitHub API", "a new reason")
        self.assertNotEqual(substance(page), substance(reviewed))    # and so is a changed review

    def test_every_review_names_a_file_that_exists(self):
        for _check, path in REVIEWED:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).exists())


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
