# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Goldilocks test's operator rule and wiring (docs/GOLDILOCKS_PREREGISTRATION.md)."""
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.goldilocks_apply import apply_rule, milli, octets  # noqa: E402


class Quantities(unittest.TestCase):
    def test_cpu(self):
        self.assertEqual(milli("163m"), 163)
        self.assertEqual(milli("1"), 1000)
        self.assertEqual(milli("0.25"), 250)

    def test_memory(self):
        self.assertEqual(octets("262144k"), 262144000)
        self.assertEqual(octets("64Mi"), 64 * 2 ** 20)
        self.assertEqual(octets("104857600"), 104857600)
        with self.assertRaises(ValueError):
            octets("12 apples")


class OperatorRule(unittest.TestCase):
    def test_request_at_target_limit_in_proportion(self):
        out = apply_rule({"containerName": "php-apache", "target": {"cpu": "120m", "memory": "64Mi"}})
        self.assertEqual(out["cpu_request_m"], 120)
        self.assertEqual(out["cpu_limit_m"], 300)                  # 120 x 500 / 200
        self.assertEqual(out["memory_request_bytes"], 64 * 2 ** 20)

    def test_no_memory_target(self):
        self.assertIsNone(apply_rule({"target": {"cpu": "1"}})["memory_request_bytes"])

    def test_zero_cpu_refused(self):
        with self.assertRaises(ValueError):
            apply_rule({"target": {"cpu": "0m"}})


class Wiring(unittest.TestCase):
    def test_scripts_parse(self):
        for f in ("scripts/kind_addons_goldilocks.sh", "scripts/kind_bench.sh"):
            subprocess.run(["bash", "-n", str(ROOT / f)], check=True)

    def test_every_download_is_pinned(self):
        s = (ROOT / "scripts/kind_addons_goldilocks.sh").read_text()
        fetched = re.findall(r'^\s*fetch "[^"]+" "[^"]+" "\$(\w+)"', s, re.M)
        self.assertEqual(len(fetched), 7)
        for var in fetched:
            self.assertRegex(s, rf'{var}="\$\{{{var}:-[0-9a-f]{{64}}\}}"')

    def test_kind_bench_accepts_goldilocks_and_keeps_keda_apart(self):
        s = (ROOT / "scripts/kind_bench.sh").read_text()
        self.assertRegex(s, r'case "\$ADDONS" in ""\|keda\|goldilocks[|)]')   # Goldilocks among the add-ons (Crane after it)
        # every check that belongs to KEDA alone keys on KEDA, never on any add-on
        self.assertNotIn('[ -n "$ADDONS" ] && [ "${ADDONS_PROFILE', s)
        self.assertIn('test "$cpu_limit" = "$EXPECT_LIMIT"', s)
        self.assertNotIn('test "$cpu_limit" = "500m"', s)

    def test_workflow(self):
        w = (ROOT / ".github/workflows/kind-goldilocks.yml").read_text()
        self.assertIn("ADDONS: goldilocks", w)
        self.assertIn("ARMS: native compass", w)


if __name__ == "__main__":
    unittest.main()
