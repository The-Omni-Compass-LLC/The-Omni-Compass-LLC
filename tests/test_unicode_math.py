# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Formulas in Unicode (tools/unicode_math.py): LaTeX becomes characters, code and prices are never touched, constants keep
their names, and a converted page reads back clean."""
import unittest

from tools.unicode_math import convert, fix_text, remaining


class UnicodeMath(unittest.TestCase):
    def test_formulas(self):
        self.assertEqual(convert(r"w \propto 1/\sqrt{n}"), "w ∝ 1/√n")
        self.assertEqual(convert(r"x_{i,k+1} = f_i(x_{i,k})"), "xᵢ,ₖ₊₁ = fᵢ(xᵢ,ₖ)")
        self.assertEqual(convert(r"\left\lceil \frac{R(1+h)}{r} \right\rceil"), "⌈R(1+h)/r⌉")
        self.assertEqual(convert(r"n_{ok} > 0"), "n[ok] > 0")
        self.assertEqual(convert(r"\frac{a+b}{2}"), "(a+b)/2")
        self.assertEqual(convert(r"\sum_{j} c_j \le 0.95 A_j"), "Σⱼ cⱼ ≤ 0.95 Aⱼ")

    def test_code_prices_and_constants_are_left_alone(self):
        text = ("It costs $5 to $15 a run. Set `x_{i}` and `$HOME`, keep U_AUTHORITY and max_ask.\n\n"
                "    f_U(x) = u_max\n\nThe bound $e^{-t}$ and N_i.\n")
        new, n = fix_text(text)
        self.assertIn("$5 to $15", new)
        self.assertIn("`x_{i}`", new)
        self.assertIn("U_AUTHORITY", new)
        self.assertIn("max_ask", new)
        self.assertIn("    f_U(x) = u_max", new)
        self.assertIn("e⁻ᵗ", new)
        self.assertIn("Nᵢ", new)
        self.assertEqual(n, 2)
        self.assertEqual(remaining(new), [])


if __name__ == "__main__":
    unittest.main()
