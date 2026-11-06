# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The undefined-name check finds a name nothing defines, and only that."""
import tempfile
import textwrap
import unittest
from pathlib import Path

from tools.lint_names import undefined


def names(src):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(textwrap.dedent(src))
    try:
        return [n for _, n in undefined(Path(f.name))]
    finally:
        Path(f.name).unlink()


class LintNames(unittest.TestCase):
    def test_finds_a_misspelt_name(self):
        self.assertEqual(names("""
            import math
            def area(r):
                return math.pi * r * rr
        """), ["rr"])

    def test_finds_a_removed_import_at_module_level(self):
        self.assertEqual(names("x = json.dumps({})\n"), ["json"])

    def test_clean_code_reads_clean(self):
        self.assertEqual(names("""
            import os
            from pathlib import Path
            K = 3
            def f(a, *args, b=2, **kw):
                def g(y):
                    return y + a + K
                total = sum(args) + b + len(kw)
                return [g(i) for i in range(total)], os.sep, Path(".")
            class C:
                z = K
                def m(self):
                    return self.z, __name__, print
            try:
                import yaml
            except ImportError:
                yaml = None
            for i in range(2):
                last = i
            print(last, yaml)
        """), [])

    def test_a_late_global_is_defined(self):
        self.assertEqual(names("""
            def f():
                return LATER
            LATER = 1
        """), [])


if __name__ == "__main__":
    unittest.main()
