# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""C++ look-ahead and stand-ins (cpp/src/lookahead.cpp) vs the Python (omni_controller/controller.py: lookahead_slope,
lookahead_horizon, lookahead_delivered, standin_count; omni-v27): the same scripts through both, every answer compared to the
last bit, and the rule's own cases (the founder's words of 15 November: look forward three steps; never ask for pods that cannot
be given a machine).

Usage: python tests/test_cpp_lookahead_parity.py OC_LOOKAHEAD [scripts]"""
import random, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.controller import lookahead_slope, lookahead_horizon, lookahead_delivered, standin_count


def g(x):
    return repr(float(x))


def script(seed):
    rng = random.Random(seed); lines = []
    for _ in range(60):
        k = rng.random()
        if k < 0.4:
            beat = rng.choice([5.0, 10.0, 15.0, 30.0, 60.0, 90.0, 120.0, rng.uniform(1, 300)])
            d0 = rng.randint(0, 5000); n = rng.randint(0, 6); v = rng.uniform(0, 1e5); pts = []
            for i in range(n):
                v = max(0.0, v + rng.choice([0.0, rng.gauss(0, 500), rng.uniform(-5000, 5000)]))
                pts += [str(d0 + i), repr(v if rng.random() < 0.9 else float(int(v)))]
            lines.append(",".join(["S", repr(beat)] + pts))
        elif k < 0.55:
            lines.append(f"H,{rng.choice([5.0, 10.0, 60.0, rng.uniform(1, 300)])!r},{rng.uniform(0, 900)!r},{rng.randint(1, 5)}")
        elif k < 0.65:
            lines.append(f"D,{rng.uniform(1, 900)!r},{rng.uniform(1, 2000)!r}")
        else:
            nodes = rng.randint(0, 40); pool = nodes + rng.randint(-2, 5); opn = max(0, nodes - rng.randint(0, 2))
            alloc = rng.choice([0.0, nodes * rng.choice([1900.0, 3860.0, 7820.0, rng.uniform(500, 64000)])])
            req = rng.uniform(0, 1.3) * alloc; ahead = rng.choice([0.0, rng.uniform(0, 2.0) * max(alloc, 1.0)])
            room = rng.choice([-1, 0, rng.randint(0, 50)]); unit = rng.choice([250.0, 100.0, 1000.0, 0.0, rng.uniform(1, 2000)])
            lines.append(f"C,{alloc!r},{req!r},{nodes},{pool},{opn},{ahead!r},{room},{unit!r},{rng.choice(['0', '0', '0', '1'])}")
    return lines


def py_answers(lines):
    out = []
    for line in lines:
        f = line.split(",")
        if f[0] == "S":
            pts = [(float(f[i]), float(f[i + 1])) for i in range(2, len(f) - 1, 2)]
            out.append(["S", g(lookahead_slope(pts, float(f[1])))])
        elif f[0] == "H":
            out.append(["H", g(lookahead_horizon(float(f[1]), float(f[2]), int(f[3])))])
        elif f[0] == "D":
            out.append(["D", g(lookahead_delivered(float(f[1]), float(f[2])))])
        else:
            room = int(f[7])
            n, free, parked, short = standin_count(float(f[1]), float(f[2]), int(f[3]), int(f[4]), int(f[5]), float(f[6]),
                                                   None if room < 0 else room, float(f[8]), f[9] == "1")
            out.append(["C", str(n), g(free), g(parked), g(short)])
    return out


def cpp_answers(exe, lines):
    with tempfile.TemporaryDirectory() as t:
        i, o = Path(t) / "in.csv", Path(t) / "out.csv"
        i.write_text("\n".join(lines) + "\n")
        subprocess.run([str(exe), str(i), str(o)], check=True)
        return [[x if j == 0 or not _num(x) else g(float(x)) for j, x in enumerate(r.split("|"))] if r[0] != "C" else
                ["C", r.split("|")[1]] + [g(float(x)) for x in r.split("|")[2:]] for r in o.read_text().splitlines() if r]


def _num(x):
    try:
        float(x); return True
    except ValueError:
        return False


def cases():
    """The rule's own cases, read in the Python (the C++ is held to the Python above)."""
    assert lookahead_slope([(1, 10.0)], 60) == 0.0
    assert abs(lookahead_slope([(1, 10.0), (2, 12.0), (3, 14.0), (4, 16.0)], 60) - 2.0 / 60) < 1e-12
    assert lookahead_slope([(1, 10.0), (2, 10.0), (3, 10.0), (4, 40.0)], 60) == 0.0    # a single jump: no trend, none asked
    assert lookahead_horizon(60, 120.0) == 180.0 and lookahead_horizon(10, 120.0) == 120.0
    assert standin_count(4000, 2000, 2, 2, 2, 3000, 2, 250)[0] == 12       # 1 core short: 12 stand-ins, 4 of them wait
    assert standin_count(4000, 2000, 2, 3, 2, 3000, 2, 250)[0] == 0        # the parked machine holds it
    assert standin_count(4000, 2000, 2, 2, 2, 3000, 0, 250)[0] == 0        # the cloud at its top: none
    assert standin_count(4000, 2000, 2, 2, 2, 3000, 2, 250, off=True)[0] == 0


def main(exe, scripts=200):
    cases()
    for seed in range(scripts):
        lines = script(seed)
        py, cc = py_answers(lines), cpp_answers(exe, lines)
        assert py == cc, next((l, p, c) for l, p, c in zip(lines, py, cc) if p != c)
    print(f"C++ look-ahead and stand-ins equal the Python's on {scripts} scripts, every answer to the last bit")
    return scripts


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 200)
