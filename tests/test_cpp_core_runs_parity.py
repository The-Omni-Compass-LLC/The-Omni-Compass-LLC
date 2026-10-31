# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The core's Monte Carlo through the C++ harness (cpp/tools/core_runs.cpp on the sealed cpp/src/core.cpp) against the Python's own
(tools/core_runs.py on omnicompass/core.py): the Python's draws from the jump generator are the input (tools/core_runs.py injection()),
the C++ twin of the core puts the mechanism on in the Python's own loop, four ways, and every U of every run must equal the Python's to
the last bit, with the same SHA-256 digest; on the engine's own ranges and on the example system (systems/example_heavy_swing.json).

Usage: python tests/test_cpp_core_runs_parity.py OC_CORE_RUNS [runs] [base]"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools import core_runs as CR


def main(exe, n=50, base=CR.DEFAULT_BASE):
    out = []
    for system in (CR.load_system(""), CR.load_system(str(ROOT / "systems" / "example_heavy_swing.json"))):
        runs = [CR.one(k, base, system) for k in range(n)]
        c = CR.cpp_runs(n, base, system, Path(exe))
        m = CR.cpp_compare(runs, c)
        assert c["digest"] == CR.digest(runs), f"digests differ ({system['name']}): C++ {c['digest']}, Python {CR.digest(runs)}"
        assert m["largest_difference"] == 0.0, f"largest difference {m['largest_difference']} ({m['of'] - m['agree']} of {m['of']} run-ways differ)"
        print(f"the core's Monte Carlo through the C++ twin ({system['name']}): {n} runs from base {base}, four ways, every U identical, "
              f"digest {c['digest'][:16]}… the same (the injection {c['inputs_digest'][:16]}…)")
        out.append(c["digest"])
    return out[0]


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 50, int(sys.argv[3]) if len(sys.argv) > 3 else CR.DEFAULT_BASE)
