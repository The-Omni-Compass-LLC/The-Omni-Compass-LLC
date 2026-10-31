# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The YCSB A/B/C rule (tools/ycsb_abc.py): GAIN or LOSS in all three of our runs (by what the gauge is for) only with the same sign and every interval clear of zero in all three
runs; an interval over zero reads STEADY, no difference beyond the noise, with the count of such runs; clear runs pointing different
ways read as a disagreement; a failed operation added in any run is marked; the resource held reads power given when it grows."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import ycsb_abc as A


def r(diff, lo, hi, native=100.0):
    return {"native": native, "omni": native + diff, "diff": diff, "ci95": [lo, hi], "n": 3, "significant": lo > 0 or hi < 0}


def main():
    assert A.verdict([r(5, 2, 8), r(6, 3, 9), r(4, 1, 7)], "higher") == "**GAIN in all three of our runs**"
    assert A.verdict([r(5, 2, 8), r(6, 3, 9), r(4, 1, 7)], "spent") == "**power given in all three of our runs**", "a resource that grows is power given"
    assert A.verdict([r(5, 2, 8), r(6, 3, 9), r(4, 1, 7)], "lower", "cache_mb_mean") == "**power given in all three of our runs**", "the cache size is a resource"
    assert A.verdict([r(5, 2, 8), r(6, 3, 9), r(4, 1, 7)], "lower") == "**LOSS in all three of our runs**", "a longer wait is a LOSS"
    assert A.verdict([r(5, 2, 8), r(1, -2, 4), r(4, 1, 7)], "higher") == "**GAIN by the mean of our three runs, beyond the noise in 2 of 3**"
    assert A.verdict([r(5, 2, 8), r(-6, -9, -3), r(4, 1, 7)], "higher") == "**the runs disagree**"
    assert A.verdict([r(0, -1, 1), r(0, -1, 1), r(0, -1, 1)], "higher") == "STEADY, the same"
    assert A.verdict([r(0, 0, 0), r(1, 1, 1), r(0, 0, 0)], "never more") == "**LOSS in at least one of our runs**", "one failed operation more in any run is marked"
    assert A.verdict([r(0, 0, 0), r(0, 0, 0), r(0, 0, 0)], "never more") == "STEADY, the same"
    assert A.verdict([r(1, 0, 2), None, r(1, 0, 2)], "higher") == "no value"
    assert A.verdict([r(9, 1, 2)], "shown") == "shown, not judged"
    # native → Omni-Compass and the raw change with its true sign (the referee's work order of 25 October); a native at zero in
    # the gauge's own unit, never a percentage made up
    assert A.cell(r(5, 2, 8), "ops") == "100 → 105; raw +5.0% (95%: +2.0% to +8.0%)"
    assert A.cell(r(2, 1, 3, native=0.0), "failed") == "0 → 2; raw +2.0000 in the gauge's unit (95%: +1.0000 to +3.0000)"
    print("PASS  YCSB A/B/C rule: GAIN or LOSS in all three of our runs (by what the gauge is for) only with the same sign and every interval clear of zero in all three runs; an interval over zero reads STEADY, no "
          "difference beyond the noise, with the count; clear runs pointing different ways read as a disagreement; a failed operation added is marked")


if __name__ == "__main__":
    main()
