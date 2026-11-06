# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""No script stops reading a pipe early under pipefail. `cmd | grep -q x` quits at its first match; the writer then dies of a
broken pipe, and with `set -o pipefail` the pipeline reads as failed though the match was found (the Kepler meter read as
"no node energy" on 17 October, and a permission check written `! cmd | grep -q x` could pass when it should stop). Every
such test reads the whole stream: `cmd | grep x >/dev/null`."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Pipes(unittest.TestCase):
    def test_no_early_exit_grep_in_a_pipe(self):
        bad = [f"{p.relative_to(ROOT)}:{i}" for p in sorted((ROOT / "scripts").glob("*.sh"))
               for i, line in enumerate(p.read_text().splitlines(), 1) if re.search(r"\|\s*grep\s+-q\b", line)]
        self.assertEqual(bad, [], "grep -q at the end of a pipe: " + ", ".join(bad))


if __name__ == "__main__":
    unittest.main()
