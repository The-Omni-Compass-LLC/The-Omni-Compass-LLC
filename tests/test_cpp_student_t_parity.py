# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""C++ Student's t (cpp/src/student_t.cpp) vs the Python (omnicompass/student_t.py): the log-gamma, the incomplete beta, the
coverage and the 95% point asked the same questions, every answer compared to the last bit, and t95 for every degree of
freedom from 1 to 1,000.

Usage: python tests/test_cpp_student_t_parity.py OC_STUDENT_T [questions]"""
import math, random, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass import student_t as S


def questions(rng, n):
    q = [f"T,{df}" for df in range(1, 1001)]
    for _ in range(n):
        k = rng.random()
        if k < 0.3:
            q.append(f"L,{rng.choice([rng.uniform(0.01, 5.0), rng.uniform(5.0, 600.0), rng.randint(1, 500) / 2.0])!r}")
        elif k < 0.6:
            q.append(f"B,{rng.uniform(0.5, 300.0)!r},{rng.choice([0.5, rng.uniform(0.2, 40.0)])!r},{rng.uniform(0.0, 1.0)!r}")
        else:
            q.append(f"C,{rng.uniform(0.0, 20.0)!r},{float(rng.randint(1, 400))!r}")
    return q


def py(line):
    f = line.split(",")
    if f[0] == "L":
        return math.lgamma(float(f[1]))
    if f[0] == "B":
        return S.ibeta(float(f[1]), float(f[2]), float(f[3]))
    if f[0] == "C":
        return S.coverage(float(f[1]), float(f[2]))
    return S.t95(int(f[1]))


def main(binary, n=3000):
    rng = random.Random(20261024)
    q = questions(rng, n)
    with tempfile.TemporaryDirectory() as t:
        inp, outp = Path(t) / "in.csv", Path(t) / "out.csv"
        inp.write_text("\n".join(q) + "\n")
        subprocess.run([binary, str(inp), str(outp)], check=True)
        got = outp.read_text().splitlines()
    assert len(got) == len(q), (len(got), len(q))
    for line, g in zip(q, got):
        want, have = py(line), float(g.split(",", 1)[1])
        assert have == want or (math.isnan(have) and math.isnan(want)), f"{line}: C++ {have!r} against Python {want!r}"
    print(f"PASS  C++ Student's t = Python to the last bit: t95 for 1 to 1,000 degrees of freedom and {n} more questions")
    return len(q)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3000)
