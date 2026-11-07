# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""tools/claims_check.py catches each fault it names and passes the founder's own wording (the order of 6 November)."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("claims_check", ROOT / "tools" / "claims_check.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


def keys(text):
    out = []
    cc.scan("x.md", text, out)
    return sorted({k for _, _, k, _ in out})


class ClaimsCheck(unittest.TestCase):
    def test_each_fault_is_caught(self):
        self.assertEqual(keys("the pods waiting read EVEN"), ["even"])
        self.assertEqual(keys("energy -14.09% GAIN"), ["sign"])
        self.assertEqual(keys("GAIN +4.8% of decisions"), ["sign"])
        self.assertEqual(keys("machines +3.2% fewer"), ["direction"])
        self.assertEqual(keys("more work, faster, on fewer machines, as measured"), ["fewer"])
        self.assertEqual(keys("Omni-Compass on top of the governor governs both bodies"), ["repeat"])
        self.assertEqual(keys("the Omni index, GAIN 5.0%"), ["stale"])

    def test_the_rule_words_pass(self):
        for ok in ("GAIN, down 4.8%: less waiting, so it helps the system",
                   "power given, up 77.7% (raw +77.7%)",
                   "the aim: more work, faster, on fewer machines",
                   "Omni-Compass, supervisory on top of that product, steers both bodies",
                   "STEADY, under the 0.5% floor"):
            self.assertEqual(keys(ok), [], ok)


if __name__ == "__main__":
    unittest.main()
# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
