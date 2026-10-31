# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The database benchmark's A/B/C rule (tools/pgbench_abc.py, docs/OMNI_V1.md): GAIN or LOSS in all three of our runs (by what the gauge is for) only when all
three runs move the same way with every interval clear of zero; a run whose interval includes zero reads no difference
beyond the noise with the count; clear runs pointing different ways read as a disagreement; any added failed transaction
in any run is marked; the pool size is shown, never judged."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import pgbench_abc as P


def r(diff, lo, hi, nat=100.0):
    return {"native": nat, "omni": nat + diff, "diff": diff, "ci95": [lo, hi], "significant": lo > 0 or hi < 0}


def main():
    assert P.verdict([r(10, 5, 15)] * 3, "higher") == "**GAIN in all three of our runs**", "more work is a GAIN"
    assert P.verdict([r(10, 5, 15)] * 3, "lower") == "**LOSS in all three of our runs**", "a longer wait is a LOSS: the word is the gauge's aim, never the sign"
    assert P.verdict([r(-10, -15, -5)] * 3, "lower") == "**GAIN in all three of our runs**", "a shorter wait is a GAIN (a minus that reads GAIN)"
    assert P.verdict([r(10, 5, 15)] * 3, "spent") == "**power given in all three of our runs**", "a resource spent that rose is power given, never a LOSS"
    assert P.verdict([r(10, 5, 15)] * 3, "lower", "cpu_seconds") == "**power given in all three of our runs**", "a resource declared lower before the word spent"
    assert P.verdict([r(-10, -15, -5)] * 3, "spent") == "**GAIN in all three of our runs**", "a cut is a GAIN"
    assert P.verdict([r(10, 5, 15), r(10, -2, 22), r(10, 5, 15)], "higher") == "**GAIN by the mean of our three runs, beyond the noise in 2 of 3**"
    assert P.verdict([r(10, 5, 15), r(-10, -15, -5), r(10, 5, 15)], "higher") == "**the runs disagree**"
    assert P.verdict([r(0.0, -1e-9, 1e-9)] * 3, "higher") == "STEADY, the same"
    assert P.verdict([r(0, 0, 0, nat=0), r(1, 1, 1, nat=0), r(0, 0, 0, nat=0)], "never more") == "**LOSS in at least one of our runs**", "one more failed transaction in one run is marked"
    assert P.verdict([r(0, 0, 0, nat=0)] * 3, "never more") == "STEADY, the same"
    assert P.verdict([r(-5, -8, -2)] * 3, "shown") == "shown, not judged"
    assert P.verdict([r(1, 0, 2), None, r(1, 0, 2)], "higher") == "no value"
    print("PASS  database A/B/C rule: GAIN or LOSS in all three of our runs (by what the gauge is for; a resource spent that rose is power given) only with the same sign and every interval clear of zero in all three runs; an interval "
          "over zero reads STEADY, no difference beyond the noise, with its count; clear runs pointing different ways read as a disagreement; "
          "any added failed transaction is marked; the pool size is shown, never judged")


if __name__ == "__main__":
    main()
