# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""C++ verdict (cpp/src/verdict.cpp) vs the Python (omnicompass/verdict.py Verdict): the same script of decisions and costs
through both, every answer compared to the last bit.

The script language is oc_verdict's (cpp/tools/run_verdict.cpp): V starts a verdict (both judges, stepwise or not), O hands
it the costs measured since the last decision (a cost of zero or below among them, which the interval judge leaves out), T is
one decision, calm or not. Each decision's answer is the step the knob stands at, whether it is a trial, the deepest step
allowed, the phase, how many costs each side holds, and the event for the audit with its medians, reading and intervals.
Each script gives its muscle a cost per step (from 3% cheaper to 8% dearer) and walks the costs through those steps on its own
(a script is written before it runs, so it cannot follow the verdict's answers), which brings trials allowed and refused alike.

Usage: python tests/test_cpp_verdict_parity.py OC_VERDICT [verdicts]"""
import math, random, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass.verdict import Verdict


def g(x):
    return repr(float(x))


def py_answers(lines):
    """The Python's answer to every line of an oc_verdict script, as oc_verdict writes it (numbers as floats)."""
    out, v = [], None
    for line in lines:
        f = line.split(",")
        if f[0] == "V":
            v = Verdict(tolerance=float(f[1]), min_samples=int(f[2]), probe_every=int(f[3]), recheck=int(f[4]),
                        max_steps=int(f[5]), max_trial=int(f[6]), incremental=f[7] == "1", judge=f[8])
            out.append(["V"])
        elif f[0] == "O":
            v.observe([float(x) for x in f[1].split(";") if x] if len(f) > 1 else [])
            out.append(["O"])
        elif f[0] == "T":
            step, is_trial, ev = v.tick(f[1] == "1")
            row = ["T", float(step), float(int(is_trial)), float(v.allowed), v.phase or "none", float(len(v.ref)), float(len(v.got))]
            if ev is None:
                row.append("none")
            else:
                ivs = ev.get("interval_ln", [])
                row += [ev["verdict"], float(ev["step"]), ev.get("cost_native", "none"), ev.get("cost_step", "none"),
                        ev.get("reading", "none"), float(len(ivs))] + [float(x) for iv in ivs for x in iv]
            out.append(row)
    return out


def cpp_answers(exe, lines, d):
    fin, fout = Path(d) / "verdict_in.csv", Path(d) / "verdict_out.csv"
    fin.write_text("\n".join(lines) + "\n")
    subprocess.run([str(exe), str(fin), str(fout)], check=True)

    def val(x):
        try:
            return float(x)
        except ValueError:
            return x
    return [[f[0]] + [val(x) for x in f[1:]] for f in (l.split(",") for l in fout.read_text().splitlines())]


def same(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return x == y
    x, y = float(x), float(y)
    return (math.isnan(x) and math.isnan(y)) or x == y


def differences(py, cpp):
    """(answers compared, the first answer that differs or None)."""
    if len(py) != len(cpp):
        return len(py), f"{len(py)} answers in Python, {len(cpp)} in C++"
    for i, (a, b) in enumerate(zip(py, cpp)):
        if len(a) != len(b) or not all(same(x, y) for x, y in zip(a, b)):
            return len(py), f"line {i + 1}: Python {a}, C++ {b}"
    return len(py), None


def script(rng):
    """A random verdict on a random muscle: every step its own cost (3% cheaper to 8% dearer), noisy work, calm mostly, a few
    costs of zero or below, a decision with no work, both judges, stepwise or not."""
    judge = rng.choice(["interval", "interval", "median"])
    lines = [f"V,{g(rng.choice([0.005, 0.01, 0.02, 0.03, 0.1]))},{rng.randint(1, 40)},{rng.randint(1, 12)},{rng.randint(1, 60)},"
             f"{rng.randint(1, 6)},{rng.randint(2, 80)},{int(rng.random() < 0.4)},{judge}"]
    cost = [1.0] + [1.0 + rng.choice([0.0, 0.0, 0.01, 0.02, 0.03, 0.05, 0.08, -0.03]) for _ in range(7)]
    sig = rng.choice([0.02, 0.1, 0.25, 0.4])
    step = 0
    for _ in range(rng.randint(30, 400)):
        calm = rng.random() < 0.93
        lines.append(f"T,{int(calm)}")
        n = rng.choice([0, 1, 2, 5, 10, 30])
        cs = []
        for _ in range(n):
            r = rng.random()
            cs.append(0.0 if r < 0.01 else -1.0 if r < 0.02 else math.exp(rng.gauss(0, sig)) * cost[min(step, 7)])
        lines.append("O," + ";".join(g(c) for c in cs))
        step = rng.randint(0, 7) if rng.random() < 0.05 else step + (1 if rng.random() < 0.1 else 0)
    return lines


def main(exe, verdicts=300):
    rng = random.Random(20261021)
    with tempfile.TemporaryDirectory() as d:
        lines = [l for _ in range(verdicts) for l in script(rng)]
        n, bad = differences(py_answers(lines), cpp_answers(exe, lines, d))
    assert bad is None, bad
    print(f"C++ verdict vs Python: {verdicts} verdicts, {n} answers, every one identical")
    return n


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 300)
