# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The verifier's last line reads every check: one failed check makes VERIFICATION: FAIL (verify.py all_passed).

Twice a local name inside main() stood in for the module's record of every check, and the last line read PASS over a
failed check. The verdict is read from the module's record through all_passed(), which no local name can shadow."""
import io, sys, contextlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import verify  # noqa: E402


def main():
    verify.ok = True
    with contextlib.redirect_stdout(io.StringIO()):
        verify.check("a check that passes", True)
    assert verify.all_passed()
    with contextlib.redirect_stdout(io.StringIO()):
        verify.check("a check that fails", False)
        verify.check("a later check that passes", True)
    assert not verify.all_passed(), "a failed check did not make the verdict FAIL"
    verify.ok = True
    print("PASS test_verify_verdict: one failed check makes the verdict FAIL, whatever passes after it")


if __name__ == "__main__":
    main()
