# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""C++ compass law and plug (cpp/src/compass_law.cpp) vs the Python (omnicompass/compass_law.py Band, CompassLaw, Plug):
the same script of readings and plug commands through both, every answer compared to the last bit.

The script language is oc_compass_law's (cpp/tools/run_compass_law.cpp): L starts a law, F feeds it one reading (and the
band's center, cushion and kd where the caller moves them between readings, as the organisms' tune-down does), P starts a
plug on a device with its own resolution, A attaches, W writes, M is another writer moving the lever, S restores.
py_answers() is the Python side; the live engine page's C++ twin panel (docs/engine/export_cpp_twins.py) feeds both sides
the organisms' and the live controllers' own readings through the same two functions.

Usage: python tests/test_cpp_compass_law_parity.py OC_COMPASS_LAW [laws]"""
import math, random, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw, ForeignWriter, Plug


def g(x):
    return repr(float(x)) if x is not None else "nan"


def num(s):
    return None if s == "nan" else float(s)


class _Device(Plug):
    """The script's device: a lever that takes a value to its own resolution (res > 0: floor(v / res + 0.5) x res)."""

    def __init__(self, lo, hi, tol, lever, res):
        super().__init__(lo, hi, tol)
        self.value, self.res = lever, res

    def _read_service(self):
        return 0.0

    def _read_lever(self):
        return self.value

    def _send(self, v):
        self.value = math.floor(v / self.res + 0.5) * self.res if self.res > 0 else v


def py_answers(lines):
    """The Python's answer to every line of an oc_compass_law script, as floats where the C++ prints numbers."""
    out, law, plug = [], None, None
    for line in lines:
        f = line.split(",")
        c = f[0]
        if c == "L":
            kd = num(f[8])
            law = CompassLaw(Band(float(f[1]), float(f[2]), center=float(f[3]), cushion=float(f[4])), dt=float(f[5]),
                             tau=float(f[6]), kp=float(f[7]), kd=kd, authority=float(f[9]), smooth=float(f[10]))
            out.append(["L", law.kd])
        elif c == "F":
            center, cushion, kd = num(f[2]), num(f[3]), num(f[4])
            if center is not None:
                law.band.center = center
            if cushion is not None:
                law.band.cushion = cushion
            if kd is not None:
                law.kd = kd
            force = law.force(float(f[1]))
            out.append(["F", force, law.p, law.v])
        elif c == "P":
            plug = _Device(float(f[1]), float(f[2]), float(f[3]), float(f[4]), float(f[5]))
            out.append(["P"])
        elif c == "A":
            out.append(["A", plug.attach()])
        elif c == "W":
            try:
                w = plug.write(float(f[1]))
                out.append(["W", "none" if w is None else w, int(plug.owned), plug.writes, plug.clipped, plug.value])
            except ForeignWriter:
                out.append(["X", int(plug.owned), plug.value])
        elif c == "M":
            plug.value = float(f[1])
            out.append(["M"])
        elif c == "S":
            at = plug.restore()
            out.append(["S", int(at), plug.value])
    return out


def cpp_answers(exe, lines, d):
    fin, fout = Path(d) / "law_in.csv", Path(d) / "law_out.csv"
    fin.write_text("\n".join(lines) + "\n")
    subprocess.run([str(exe), str(fin), str(fout)], check=True)
    rows = []
    for l in fout.read_text().splitlines():
        f = l.split(",")
        rows.append([f[0]] + [x if x == "none" else float(x) for x in f[1:]])
    return rows


def differences(py, cpp):
    """(answers compared, largest absolute difference, the first line that differs in kind or None)."""
    if len(py) != len(cpp):
        return len(py), math.inf, f"{len(py)} answers in Python, {len(cpp)} in C++"
    worst = 0.0
    for i, (a, b) in enumerate(zip(py, cpp)):
        if a[0] != b[0] or len(a) != len(b):
            return len(py), math.inf, f"line {i + 1}: Python {a}, C++ {b}"
        for x, y in zip(a[1:], b[1:]):
            if x == "none" or y == "none":
                if x != y:
                    return len(py), math.inf, f"line {i + 1}: Python {a}, C++ {b}"
                continue
            worst = max(worst, abs(float(x) - float(y)))
    return len(py), worst, None


def law_line(band, dt, tau, kp=1.0, kd=None, authority=1.0, smooth=0.5):
    return f"L,{g(band.lo)},{g(band.hi)},{g(band.center)},{g(band.cushion)},{g(dt)},{g(tau)},{g(kp)},{g(kd)},{g(authority)},{g(smooth)}"


def script(rng):
    """A random law and plug: readings that climb past the wall, fall below calm and swing; the band moved between readings
    as the organisms' tune-down moves it; a plug written in and out of its cover, moved by another writer, restored."""
    lo = rng.uniform(-5, 5); hi = lo + rng.uniform(0.01, 50)
    band = Band(lo, hi, center=rng.uniform(0.1, 0.9), cushion=rng.uniform(0.005, 0.2))
    dt, tau = rng.uniform(0.1, 60), rng.uniform(0.1, 300)
    kd = None if rng.random() < 0.5 else rng.uniform(0, 5)
    lines = [law_line(band, dt, tau, rng.uniform(0.1, 3), kd, rng.uniform(0.1, 2), rng.uniform(0, 0.95))]
    x = rng.uniform(lo, hi)
    for _ in range(rng.randint(20, 120)):
        x += rng.gauss(0, (hi - lo) * 0.15)
        moved = rng.random() < 0.15
        lines.append(f"F,{g(x)},{g(rng.uniform(0, 0.995)) if moved else 'nan'},{g(rng.uniform(0.005, 0.3)) if moved else 'nan'},"
                     f"{g(rng.uniform(0, 4)) if rng.random() < 0.05 else 'nan'}")
    plo = rng.uniform(-100, 100); phi = plo + rng.uniform(1, 1000)
    res = 0.0 if rng.random() < 0.5 else (phi - plo) / rng.choice([10, 100, 1000])
    lines += [f"P,{g(plo)},{g(phi)},{g(1e-6)},{g(rng.uniform(plo, phi))},{g(res)}", "A"]
    for _ in range(rng.randint(5, 40)):
        r = rng.random()
        if r < 0.75:
            lines.append(f"W,{g(rng.uniform(plo - 0.2 * (phi - plo), phi + 0.2 * (phi - plo)))}")
        elif r < 0.85:
            lines.append(f"M,{g(rng.uniform(plo, phi))}")
        else:
            lines.append("S")
    lines.append("S")
    return lines


def climb(rng):
    """A law whose damping gain takes either sign (the Python answers for any real gain, so the twin must too) fed readings
    that climb above the center: with a negative kd the pull goes negative while the reading climbs, and the law's "never
    take back while it climbs above the center" line decides the answer. script() never reaches that line (its gains are
    never negative), so without these laws a C++ law missing it would pass."""
    lo = rng.uniform(-5, 5); hi = lo + rng.uniform(0.01, 50)
    band = Band(lo, hi, center=rng.uniform(0.1, 0.9), cushion=rng.uniform(0.005, 0.2))
    lines = [law_line(band, rng.uniform(0.1, 2), rng.uniform(0.1, 300), rng.uniform(0.1, 1), rng.uniform(-5, 1),
                      rng.uniform(0.1, 2), rng.uniform(0, 0.95))]
    x = rng.uniform(lo, lo + band.center * (hi - lo))
    for _ in range(rng.randint(10, 60)):
        x += abs(rng.gauss(0, (hi - lo) * 0.05)) if rng.random() < 0.85 else -abs(rng.gauss(0, (hi - lo) * 0.05))
        lines.append(f"F,{g(x)},nan,nan,{g(rng.uniform(-5, 4)) if rng.random() < 0.05 else 'nan'}")
    return lines


def main(exe, laws=300):
    rng, rng_climb = random.Random(20261021), random.Random(20261022)
    worst, n = 0.0, 0
    with tempfile.TemporaryDirectory() as d:
        lines = [l for _ in range(laws) for l in script(rng)] + [l for _ in range(laws // 3 + 1) for l in climb(rng_climb)]
        n, worst, bad = differences(py_answers(lines), cpp_answers(exe, lines, d))
    assert bad is None, bad
    assert worst == 0.0, f"largest difference {worst}"
    print(f"C++ compass law and plug vs Python: {laws} laws and plugs and {laws // 3 + 1} climbing laws, {n} answers, every one identical")
    return n


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 300)
