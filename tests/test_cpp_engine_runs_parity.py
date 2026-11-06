# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Python's runs through the C++ harness (cpp/tools/engine_runs.cpp) against the Python's own (tools/engine_runs.py): the
Python's draws from the jump generator are the input (tools/engine_runs.py injection()), the C++ twins of the engine put the
mechanism on (the governor's RK4 state equations, the nervous system's authority per organ, the compass law, the verdict), and
every receipt must equal the Python's to the last bit, with the same SHA-256 digest.

compare() is what the live engine's C++ twin panel (docs/engine/export_cpp_twins.py) shows run by run.

Usage: python tests/test_cpp_engine_runs_parity.py OC_ENGINE_RUNS [runs] [base]"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools import engine_runs as ER


def compare(py, cpp):
    """Per run, the largest absolute difference over every number of its receipt (inf where a count, a seed or the number of
    runs differs)."""
    out = []
    for a, b in zip(py, cpp):
        w = 0.0 if (a["k"], a["seed"]) == (b["k"], b["seed"]) else float("inf")
        for k in ER.KEYS:
            xs, ys = (a[k], b[k]) if isinstance(a[k], list) else ([a[k]], [b[k]])
            for x, y in zip(xs, ys):
                w = max(w, abs(float(x) - float(y)) if k not in ER.INT_KEYS else (0.0 if int(x) == int(y) else float("inf")))
        out.append(w)
    return out + [float("inf")] * abs(len(py) - len(cpp))


def main(exe, n=50, base=ER.DEFAULT_BASE):
    sets = [ER.draws(k, base) for k in range(n)]
    py = [ER.run_draws(dr) for dr in sets]
    c = ER.cpp_runs(sets, Path(exe))
    per = compare(py, c["runs"])
    worst, same = max(per), sum(1 for w in per if w == 0.0)
    assert c["digest"] == ER.digest(py), f"digests differ: C++ {c['digest']}, Python {ER.digest(py)}"
    assert worst == 0.0, f"largest difference {worst} ({n - same} of {n} runs differ)"
    print(f"the Python's runs through the C++ harness: {n} runs from base {base}, every receipt identical, digest {c['digest'][:16]}… "
          f"the same (the injection {c['inputs_digest'][:16]}…)")
    return c["digest"]


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 50, int(sys.argv[3]) if len(sys.argv) > 3 else ER.DEFAULT_BASE)
