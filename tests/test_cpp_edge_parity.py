# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""C++ edge (cpp/src/edge.cpp) vs the Python (omnicompass/edge.py Edge): the same script of positions and falls through both,
every balance point, cushion, reaction part and floor compared to the last bit.

Each script draws an edge's settings (reaction 1 to 12 decisions, a window of 5 to 40, both estimators, with and without
memory, paces from a fifth to two) and walks a position that climbs, wobbles and falls past the line, with a fall learned now
and then, so the widening, the slow narrowing, the extrapolated climb and the floor's forgetting are all exercised.

Usage: python tests/test_cpp_edge_parity.py OC_EDGE [scripts]"""
import random, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass.edge import Edge


def script(rng):
    react = rng.choice([1.0, 1.5, 2.0, 2.5, 3.0, 5.0, 12.0])
    window = rng.randint(5, 40)
    est = rng.choice([1, 2, 2])
    memory = rng.choice([0.0, 0.0, 0.9, 0.99])
    pace = rng.choice([1.0, 1.0, 0.25, 0.2, 0.5, 2.0])
    lines = [f"E,{react!r},{rng.choice([3.09, 2.0])!r},{window},{rng.choice([0.05, 0.1])!r},{rng.uniform(0.2, 0.8)!r},"
             f"{memory!r},{rng.choice([0.9995, 0.99])!r},{est},{pace!r}"]
    p = rng.uniform(0.0, 0.6)
    for _ in range(rng.randint(10, 120)):
        p = max(0.0, p + rng.gauss(0.01 if rng.random() < 0.6 else -0.02, 0.04))
        if rng.random() < 0.03:
            p = rng.uniform(1.0, 1.4)                               # past the line
        lines.append(f"U,{p!r}")
        if rng.random() < 0.05:
            lines.append(f"F,{rng.uniform(0.01, 0.2)!r}")
    return lines


def py_answers(lines):
    out, e = [], None
    for line in lines:
        f = line.split(",")
        if f[0] == "E":
            e = Edge(float(f[1]), z=float(f[2]), window=int(f[3]), narrow=float(f[4]), start=float(f[5]), memory=float(f[6]),
                     fall_decay=float(f[7]), est=int(f[8]), pace=float(f[9]))
            out.append(["E"])
        elif f[0] == "U":
            b = e.update(float(f[1]))
            out.append(["U", b, e.cushion, e.react_part, e.floor])
        else:
            e.learn_fall(float(f[1]))
            out.append(["F", e.floor])
    return out


def main(binary, n=400):
    rng, worst, compared = random.Random(20261024), 0.0, 0
    with tempfile.TemporaryDirectory() as t:
        for k in range(n):
            lines = script(rng)
            inp, outp = Path(t) / f"in{k}.csv", Path(t) / f"out{k}.csv"
            inp.write_text("\n".join(lines) + "\n")
            subprocess.run([binary, str(inp), str(outp)], check=True)
            got = [r.split(",") for r in outp.read_text().splitlines()]
            want = py_answers(lines)
            assert len(got) == len(want), (k, len(got), len(want))
            for g, w in zip(got, want):
                assert g[0] == w[0], (k, g, w)
                for a, b in zip(g[1:], w[1:]):
                    compared += 1
                    if float(a) != b:
                        worst = max(worst, abs(float(a) - b))
                        raise AssertionError(f"script {k}: C++ {a} against Python {b!r} ({g} / {w})")
    print(f"PASS  C++ edge = Python edge to the last bit: {n} scripts, {compared} numbers compared, largest difference {worst}")
    return worst


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 400)
