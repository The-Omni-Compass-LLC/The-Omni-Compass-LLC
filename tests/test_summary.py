# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The whole summary straight after a pull (tools/summary.py): the notice at the top and the end, the key, every headline
with its word, and no old verdict word."""
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Summary(unittest.TestCase):
    def run_it(self, *args):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "summary.py"), *args], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout

    def test_plain_and_markdown(self):
        for args in ((), ("--markdown",)):
            out = self.run_it(*args)
            lines = [l for l in out.splitlines() if l.strip()]
            self.assertIn("The Omni-Compass LLC", lines[0])
            self.assertTrue(lines[-1].rstrip("*").endswith("www.omni-compass.com"), lines[-1])
            for w in ("GAIN", "STEADY", "LOSS", "Growth", "The Omni index", "Run and scored by The Omni-Compass LLC's own code"):
                self.assertIn(w, out)
            self.assertIsNone(re.search(r"\b(better|worse)\b", out.replace("Better, same and worse are not used", "")))


if __name__ == "__main__":
    unittest.main()
