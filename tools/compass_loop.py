#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The compass loop measured where its proof stops (our own model, class S; docs/ENGINE_PROOFS.md, section 1b).

L1-L4 (tools/prove_engine.py) prove the loop without damping on the model M1, where the reading follows the lever within
the beat: the reading never passes the centre, the ball of radius R*(D) = (A / kp) artanh(D / (b A)) is never left, and
outside it every beat closes a fixed share of the distance. This tool runs the engine's own CompassLaw.force where the
proof does not reach and writes what it finds, every row, whichever way it falls:

  M1, kd = 0           the proof's own case: the tail must sit at or under R*
  M2, lagged muscle    the reading follows the lever with the muscle's response time tau (an exact first-order step),
                       the lever is the sum of the forces times its gain: kd = 0, the default damping for that tau, and
                       three times it (as realms/compass_arm.py sets it)
  M1, damping for a    the default damping for a response time tau the muscle does not have (it follows within the beat):
  lag not there        what a damping set from a wrong tau does

Each row is one gain set, one tau (in beats), one damping and one push of size D: outward (always away from the centre),
flip (its sign every beat), random (uniform in [-D, D], a fixed seed) or slow (its sign every seven beats or so). The
tail is the largest distance from the centre over the second half of 1,200 beats.

  python3 tools/compass_loop.py            write results/model_gate/COMPASS_LOOP.json and .md
  python3 tools/compass_loop.py --check    exit 1 if the stored record differs from what the code produces now
"""
from __future__ import annotations

import argparse, json, math, random, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402

OUT_JSON = ROOT / "results" / "model_gate" / "COMPASS_LOOP.json"
OUT_MD = ROOT / "results" / "model_gate" / "COMPASS_LOOP.md"
BEAT = 60.0
BEATS = 1200
GAINS = ({"kp": 1.0, "A": 1.0, "b": 0.4}, {"kp": 4.0, "A": 0.3, "b": 0.2})
TAUS = (0.25, 1.0, 2.0, 4.0)       # 2 beats: the response time the card governor and Omni direct declare
PUSHES = ("outward", "flip", "random", "slow")
DAMPING = ("none", "default", "three times")


def radius(kp, A, b, D):
    """R*(D): the smallest ball the proof keeps (L3), b A tanh(kp R / A) = D."""
    return (A / kp) * math.atanh(D / (b * A))


def run(kp, A, b, D, tau_beats, damping, push, lagged, seed=1):
    g = CompassLaw(Band(0.0, 1.0, center=0.5), dt=BEAT, tau=tau_beats * BEAT, kp=kp, authority=A,
                   kd=0.0 if damping == "none" else None)
    if damping == "three times":
        g.kd *= 3.0
    follow = 1.0 - math.exp(-1.0 / tau_beats) if lagged else 1.0
    rng = random.Random(seed)
    load, lever, p, tail = 0.5, 0.0, 0.5, 0.0
    for k in range(BEATS):
        f = g.force(p)
        lever += b * f
        e = p - 0.5
        d = {"outward": D if e >= 0 else -D, "flip": D if k % 2 else -D, "random": rng.uniform(-D, D),
             "slow": D * math.copysign(1.0, math.sin(k / 7.0))}[push]
        load += d
        p += follow * ((load - lever) - p)
        if not math.isfinite(p):
            return float("inf")
        if k >= BEATS // 2:
            tail = max(tail, abs(p - 0.5))
    return tail


def measure():
    rows = []
    for gs in GAINS:
        kp, A, b = gs["kp"], gs["A"], gs["b"]
        D = 0.5 * b * A * math.tanh(kp * 0.3 / A)        # half the pull at 0.3 from the centre
        R = radius(kp, A, b, D)
        cases = [("M1, the proof's case", False, 1.0, "none")]
        cases += [("M2, lagged muscle", True, t, dmp) for t in TAUS for dmp in DAMPING]
        cases += [("M1, damping for a lag not there", False, t, dmp) for t in TAUS for dmp in DAMPING[1:]]
        for model, lagged, t, dmp in cases:
            for push in PUSHES:
                tail = run(kp, A, b, D, t, dmp, push, lagged)
                rows.append({"kp": kp, "A": A, "b": b, "D": round(D, 6), "R_star": round(R, 6), "model": model,
                             "tau_beats": t, "damping": dmp, "push": push, "tail": round(tail, 6),
                             "tail_over_R_star": round(tail / R, 4),
                             "inside": bool(tail <= R * (1 + 1e-9))})
    return rows


def summary(rows):
    """Per model and per damping: the rows, how many sit at or under R*, the largest tail in R*."""
    out = {}
    for model in dict.fromkeys(r["model"] for r in rows):
        for damping in dict.fromkeys(r["damping"] for r in rows if r["model"] == model):
            rs = [r for r in rows if r["model"] == model and r["damping"] == damping]
            out[f"{model}; damping {damping}"] = {"rows": len(rs), "inside_R_star": sum(r["inside"] for r in rs),
                                                  "largest_tail_over_R_star": max(r["tail_over_R_star"] for r in rs)}
    return out


def record():
    rows = measure()
    return {"class": "S, our own model (never a benchmark result)", "beats": BEATS, "beat_s": BEAT,
            "gains": list(GAINS), "taus_in_beats": list(TAUS), "pushes": list(PUSHES), "damping": list(DAMPING),
            "summary": summary(rows), "rows": rows}


def page(rec):
    L = ["# The compass loop, measured where its proof stops", "",
         "Our own model (class S), never a benchmark result. Written by `tools/compass_loop.py` from the engine's own "
         "`CompassLaw.force` (`omnicompass/compass_law.py`); the proof it extends is `docs/ENGINE_PROOFS.md`, section 1b "
         "(L1 to L4, `tools/prove_engine.py`). Each row is one gain set, one response time tau (in beats), one damping and "
         "one push of size D (half the muscle's pull at 0.3 from the centre); the tail is the largest distance from the "
         "centre over the second half of %d beats; R* = (A / kp) artanh(D / (b A)) is the ball the proof keeps without "
         "damping. Every row is printed, whichever way it falls." % rec["beats"], "",
         "## What falls out", "", "| Model | Rows | At or under R* | Largest tail / R* |", "|---|---|---|---|"]
    for model, s in rec["summary"].items():
        L.append(f"| {model} | {s['rows']} | {s['inside_R_star']} | {s['largest_tail_over_R_star']:.3f} |")
    L += ["", "## Every row", "",
          "| kp | A | b | R* | Model | tau (beats) | Damping | Push | Tail | Tail / R* | At or under R* |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rec["rows"]:
        L.append(f"| {r['kp']:g} | {r['A']:g} | {r['b']:g} | {r['R_star']:.4f} | {r['model']} | {r['tau_beats']:g} | "
                 f"{r['damping']} | {r['push']} | {r['tail']:.4f} | {r['tail_over_R_star']:.3f} | "
                 f"{'yes' if r['inside'] else 'no'} |")
    from tools.legal import stamp
    return "\n".join(stamp(L)) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    rec = record()
    text = json.dumps(rec, indent=1) + "\n"
    if a.check:
        stored = json.loads(OUT_JSON.read_text()) if OUT_JSON.exists() else None
        ok = stored == json.loads(text) and OUT_MD.exists() and OUT_MD.read_text() == page(rec)
        print("compass loop record: " + ("current" if ok else "stale; run python3 tools/compass_loop.py"))
        return 0 if ok else 1
    OUT_JSON.write_text(text)
    OUT_MD.write_text(page(rec))
    for model, s in rec["summary"].items():
        print(f"{model}: {s['inside_R_star']} of {s['rows']} at or under R*, largest tail {s['largest_tail_over_R_star']:.3f} R*")
    return 0


if __name__ == "__main__":
    sys.exit(main())
