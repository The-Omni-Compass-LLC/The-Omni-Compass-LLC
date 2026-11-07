# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""C++ Omni direct brain and room rule (cpp/src/orchestrator_brain.cpp) vs the Python (omni_orchestrator/brain.py and
scheduler.py): the same scripts of beats, each brain's count fed back as the next beat's units (a closed loop, as the
orchestrator runs it), trials and their anchors, the yardstick alone, the conveyed walls, the machines, and where each unit
goes (pack and spread, by requests and by the busy rule); every answer compared to the last bit.

Usage: python tests/test_cpp_orchestrator_brain_parity.py OC_ORCHESTRATOR_BRAIN [scripts]"""
import math, random, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_orchestrator import brain as B, scheduler as S


def num(x):
    return "-" if x is None else repr(x)


def script(rng):
    """One brain's life: a line, a beat and bounds, then beats whose units follow the brain's own count."""
    line, beat = rng.choice([150.0, 250.0, 400.0, rng.uniform(50.0, 900.0)]), rng.choice([5.0, 15.0, 60.0, rng.uniform(5.0, 120.0)])
    mn, mx = rng.choice([1, 2, 2, 3]), rng.choice([8, 12, 24, 40])
    step, hold = rng.choice([1, 2, 3, 3, 5]), rng.choice([1, 2, 3, 3, 4])
    q = [f"B,{line!r},{beat!r},{mn},{mx},{step},{hold}"]
    brain, units, now = B.OmniBrain(line, beat, mn, mx, max_step=step, hold=hold), rng.randint(mn, mx), 0.0
    load = rng.uniform(0.2, 1.4)
    for _ in range(rng.randint(20, 160)):
        now += beat
        load = max(0.0, load + rng.gauss(0.0, 0.08))
        busy = None if rng.random() < 0.05 else min(1.0, load * rng.uniform(0.7, 1.3) * 4.0 / max(units, 1))
        p95 = line * rng.choice([rng.uniform(0.0, 0.6), rng.uniform(0.6, 1.0), rng.uniform(1.0, 2.5), 0.5, 1.0])
        waiting = rng.choice([0, 0, 0, 0, 1, 2, rng.randint(0, 9)])
        depth = rng.choice([0, 0, 1, 2, rng.randint(0, 4)])
        trial = rng.random() < 0.25
        twin = rng.randint(mn, mx) if rng.random() < 0.3 else None
        anchor = rng.randint(mn, mx) if trial and rng.random() < 0.6 else None
        q.append(f"D,{now!r},{units},{num(busy)},{p95!r},{waiting},{depth},{int(trial)},{num(twin)},{num(anchor)}")
        units, _ = brain.decide(now, units, busy, p95, waiting, depth=depth, trial=trial, twin=twin, anchor=anchor)
    return q


def yard_script(rng):
    mn, mx = rng.choice([1, 2]), rng.choice([10, 30, 100])
    q, units, now = [f"Y,{mn},{mx}"], rng.randint(mn, mx), 0.0
    y = B.Yardstick(mn, mx)
    for _ in range(rng.randint(10, 120)):
        now += rng.choice([15.0, 15.0, 5.0, 60.0])
        busy = None if rng.random() < 0.05 else rng.choice([0.5, 0.55, 0.45, rng.uniform(0.0, 1.0)])
        q.append(f"R,{now!r},{units},{num(busy)}")
        units = y.recommend(now, units, busy)
    return q


def other_lines(rng, n):
    q = []
    for _ in range(n):
        cpu = rng.choice([1000.0, 2000.0, 4000.0, 8000.0, rng.uniform(500.0, 16000.0)])
        busy = None if rng.random() < 0.1 else cpu * rng.choice([0.70, 0.75, rng.uniform(0.0, 1.0)])
        ours = [(f"u{k}", rng.choice([100.0, 250.0, 500.0, rng.uniform(50.0, 2000.0)])) for k in range(rng.randint(0, 6))]
        q.append(f"C,{cpu!r},{num(busy)},{rng.uniform(0.0, cpu)!r},{int(rng.random() < 0.5)}"
                 + "".join(f",{i},{r!r}" for i, r in ours))
        q.append(f"M,{rng.randint(0, 60)},{rng.uniform(50.0, 2000.0)!r},{rng.uniform(500.0, 16000.0)!r},{rng.randint(0, 5)},"
                 f"{rng.choice([1, 2, 3])},{rng.choice([0.0, rng.uniform(0.0, 4000.0)])!r}")
    return q


def place_lines(rng, n):
    """Clusters of machines in every state, units of several services on them, a unit to place."""
    q = []
    for _ in range(n):
        ms = []
        for k in range(rng.randint(0, 7)):
            cpu = rng.choice([1000.0, 2000.0, 4000.0, rng.uniform(500.0, 8000.0)])
            busy = None if rng.random() < 0.3 else cpu * rng.uniform(0.0, 1.0)
            ms.append((f"m{rng.randint(0, 9)}{k}", cpu, busy, rng.choice(["awake", "awake", "awake", "booting", "draining", "parked"])))
        us = [(rng.choice(ms)[0] if ms and rng.random() < 0.9 else "gone", rng.choice([100.0, 250.0, 500.0, rng.uniform(50.0, 1500.0)]),
               rng.choice(["web", "web", "batch", None])) for _ in range(rng.randint(0, 14))]
        q.append(f"P,{rng.choice([100.0, 250.0, 500.0, rng.uniform(50.0, 2000.0)])!r},{rng.choice(['web', 'batch'])},"
                 f"{rng.choice(['pack', 'spread'])},{rng.choice(['requests', 'busy'])},{len(ms)}"
                 + "".join(f",{a},{b!r},{num(c)},{d}" for a, b, c, d in ms)
                 + "".join(f",{a},{b!r},{'-' if c is None else c}" for a, b, c in us))
    return q


def python_answers(q):
    out, brain, yard = [], None, None
    for line in q:
        f = line.split(",")
        opt = lambda s, t=float: None if s == "-" else t(s)
        if f[0] == "B":
            brain = B.OmniBrain(float(f[1]), float(f[2]), int(f[3]), int(f[4]), max_step=int(f[5]), hold=int(f[6])); out.append("B")
        elif f[0] == "D":
            want, i = brain.decide(float(f[1]), int(f[2]), opt(f[3]), float(f[4]), int(f[5]), depth=int(f[6]), trial=f[7] == "1",
                                   twin=opt(f[8], int), anchor=opt(f[9], int))
            out.append((want, i["force"], i["position"], i["twin"], i["floor"], i["depth"], int(i["trial"]), i["p95_ms"], i["busy"],
                        i["waiting"], brain.calm))
        elif f[0] == "Y":
            yard = B.Yardstick(int(f[1]), int(f[2])); out.append("Y")
        elif f[0] == "R":
            out.append(yard.recommend(float(f[1]), int(f[2]), opt(f[3])))
        elif f[0] == "C":
            ours = [{"id": f[k], "req_m": float(f[k + 1])} for k in range(5, len(f) - 1, 2)]
            out.append(B.conveyed_limits(float(f[1]), opt(f[2]), ours, float(f[3]), others_room=f[4] == "1"))
        elif f[0] == "M":
            out.append(B.machines_needed(int(f[1]), float(f[2]), float(f[3]), int(f[4]), int(f[5]), float(f[6])))
        elif f[0] == "P":
            n = int(f[5])
            machines = {f[6 + 4 * k]: {"name": f[6 + 4 * k], "cpu_m": float(f[7 + 4 * k]), "busy_m": opt(f[8 + 4 * k]),
                                       "state": f[9 + 4 * k]} for k in range(n)}
            units = []
            for k in range(6 + 4 * n, len(f) - 2, 3):
                u = {"machine": f[k], "req_m": float(f[k + 1])}
                if f[k + 2] != "-":
                    u["service"] = f[k + 2]
                units.append(u)
            out.append(S.place(float(f[1]), f[2], machines, units, how=f[3], rule=f[4]))
    return out


def same(want, have_line, line):
    h = have_line.split(",")
    if line[0] in "BY":
        return h == [want]
    if line[0] == "D":
        parsed = (int(h[1]), float(h[2]), float(h[3]), int(h[4]), int(h[5]), int(h[6]), int(h[7]), float(h[8]),
                  None if h[9] == "-" else float(h[9]), int(h[10]), int(h[11]))
        return parsed == want
    if line[0] == "P":
        return h[1:] == ["-" if want is None else want]
    if line[0] in "RM":
        return int(h[1]) == want
    if line[0] == "C":
        if want is None:
            return h[1:] == ["-"]
        return dict(zip(h[1::2], map(float, h[2::2]))) == want and len(h[1:]) == 2 * len(want)
    return False


def main(binary, n=300):
    rng = random.Random(20261024)
    q = []
    for _ in range(n):
        q += script(rng)
    for _ in range(n // 3):
        q += yard_script(rng)
    q += other_lines(rng, 4 * n)
    q += place_lines(rng, 10 * n)
    want = python_answers(q)
    with tempfile.TemporaryDirectory() as t:
        inp, outp = Path(t) / "in.csv", Path(t) / "out.csv"
        inp.write_text("\n".join(q) + "\n")
        subprocess.run([binary, str(inp), str(outp)], check=True)
        got = outp.read_text().splitlines()
    assert len(got) == len(q), (len(got), len(q))
    beats = 0
    for line, w, g in zip(q, want, got):
        assert same(w, g, line), f"{line}\n  C++    {g}\n  Python {w}"
        beats += line[0] == "D"
    print(f"PASS  C++ Omni direct brain = Python to the last bit: {n} brains, {beats} beats in a closed loop, the yardstick, "
          f"{4 * n} conveyed walls, {4 * n} machine counts and {10 * n} placements")
    return len(q)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 300)
