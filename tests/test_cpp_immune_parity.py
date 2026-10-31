# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""C++ immune self-knowledge (cpp/src/immune.cpp) vs the Python (omnicompass/immune.py): the same scripts of readings through
both, every answer compared to the last bit, and the rule's own cases (the founder's order of 25 October): a knob redlining that
Omni-Compass cannot bring back goes to native when native's twin reads it lower, and stays when native is not stronger.

Usage: python tests/test_cpp_immune_parity.py OC_IMMUNE [scripts]"""
import random, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass.immune import Immune


def g(x):
    return repr(float(x))


def py_answers(lines):
    out, k = [], None
    for line in lines:
        f = line.split(",")
        if f[0] == "I":
            k = Immune(int(f[1]), float(f[2]), float(f[3]), int(f[4]), int(f[5])); out.append(["I"])
        else:
            m, ev = k.tick(float(f[1]), float(f[2]), f[3] == "1", f[4] == "1")
            row = ["T", m, str(k.left), str(k.hold_len), str(k.handbacks)]
            row += ["none"] if ev is None else [ev["immune"], g(ev["p_omni"]), g(ev["p_native"]),
                                               str(ev.get("redline_decisions", -1)), str(ev.get("hold", -1))]
            out.append(row)
    return out


def cpp_answers(exe, lines):
    with tempfile.TemporaryDirectory() as d:
        fin, fout = Path(d) / "in.csv", Path(d) / "out.csv"
        fin.write_text("\n".join(lines) + "\n")
        subprocess.run([str(exe), str(fin), str(fout)], check=True)
        rows = [r.split("|") if r.startswith("T|") else [r] for r in fout.read_text().splitlines() if r]
    return [[r[0]] if r[0] == "I" else r[:5] + (["none"] if r[5] == "none" else [r[5], g(float(r[6])), g(float(r[7])), r[8], r[9]])
            for r in rows]


def script(seed):
    """A knob through calm, a redline Omni-Compass cannot lift, native stronger or not, recoveries: readings drawn from a seed."""
    rng = random.Random(seed)
    lines = [f"I,{rng.choice([2, 3, 4])},{rng.choice([0.02, 0.05, 0.1])},{rng.choice([0.0, 0.05, 0.1])},{rng.choice([3, 5, 10])},{rng.choice([20, 40, 160])}"]
    p, pn = 0.8, 0.8
    for _ in range(rng.randint(80, 200)):
        phase = rng.random()
        p = max(0.1, p + rng.gauss(0, 0.08) + (0.15 if phase < 0.15 else -0.05 if phase > 0.85 else 0))
        pn = max(0.1, p * rng.choice([0.7, 0.9, 1.0, 1.1, 1.3]) + rng.gauss(0, 0.03))
        lines.append(f"T,{g(p)},{g(pn)},{int(rng.random() < 0.5)},{int(rng.random() < 0.2)}")
    return lines


class ImmuneRule(unittest.TestCase):
    def test_a_redline_omni_cannot_lift_goes_to_native_when_native_is_stronger(self):
        k = Immune(streak=3, relief=0.05, margin=0.05, hold=4)
        answers = [k.tick(1.3, 0.9, moved=True)[0] for _ in range(3)]
        self.assertEqual(answers, ["omni", "omni", "native"])         # three decisions over the line, not lifted: native
        self.assertEqual([k.tick(1.3, 0.9)[0] for _ in range(3)], ["native"] * 3)   # held

    def test_a_redline_native_cannot_beat_stays_with_omni(self):
        k = Immune(streak=3)
        out = [k.tick(1.2, 1.5) for _ in range(5)]
        self.assertTrue(all(m == "omni" for m, _ in out))
        self.assertEqual(out[-1][1]["immune"], "redlining, native not stronger: stays")

    def test_a_redline_omni_is_lifting_is_left_to_it(self):
        k = Immune(streak=3, relief=0.05)
        self.assertEqual([k.tick(p, 0.5)[0] for p in (1.4, 1.3, 1.2, 1.1)], ["omni"] * 4)   # falling: not stuck

    def test_back_to_omni_only_when_its_twin_is_stronger_and_clean(self):
        k = Immune(streak=1, hold=2)
        self.assertEqual(k.tick(1.5, 1.0)[0], "native")
        self.assertEqual(k.tick(0.9, 0.8)[0], "native")              # the hold
        self.assertEqual(k.tick(0.9, 0.8)[0], "native")              # native still stronger
        m, ev = k.tick(0.7, 0.9)
        self.assertEqual((m, ev["immune"]), ("omni", "returned to Omni-Compass"))

    def test_the_hold_doubles_in_a_row(self):
        k = Immune(streak=1, hold=2, hold_max=8)
        k.tick(1.5, 1.0); self.assertEqual(k.hold_len, 4)
        k.tick(0.5, 0.9); k.tick(0.5, 0.9)                          # the hold runs out; Omni-Compass's twin stronger: back
        k.tick(1.5, 1.0); self.assertEqual(k.hold_len, 8)


class Parity(unittest.TestCase):
    def test_python_and_cpp_answer_alike(self):
        exe = Path(sys.argv[1]) if len(sys.argv) > 1 and Path(sys.argv[1]).exists() else None
        for c in (ROOT / "cpp" / "build" / "oc_immune", Path("/root/cppb2/oc_immune")):
            exe = exe or (c if c.exists() else None)
        if exe is None:
            self.skipTest("oc_immune not built (cmake -S cpp -B cpp/build && make -C cpp/build oc_immune)")
        for seed in range(40):
            lines = script(seed)
            self.assertEqual(py_answers(lines), cpp_answers(exe, lines), seed)


if __name__ == "__main__":
    unittest.main(argv=sys.argv[:1])

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
