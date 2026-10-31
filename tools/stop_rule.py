# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The preregistered stopping rule of a paid cloud set (docs/K8S_COMPASS_PREREGISTRATION.md, the amendment of 19 October): a set runs up
to its cap of repetitions (100, the founder's order of 12 October) and stops early at a look only when the answer is
already read, so no money is spent measuring what is known.

At each look (after 10, 20, 40 and 70 paired repetitions by default), on the repetitions 1 to that look only:
  the bill  the paired change of the machine-hours billed, with its 99% interval (Student's t; four looks at 1% each keep
            the whole rule's error under 5%, Bonferroni);
  decided   the interval clears zero (a cut: GAIN; a rise: power given), or it holds zero and its half-width is within
            the precision (2% of native's bill by default): STEADY, measured to that precision;
  harm      a set never stops while its 95th percentile or its failed requests read a LOSS at that look (their 99% interval
            wholly above zero): it runs on, so a LOSS is measured to the end, never cut short.
A look reads the first paired repetitions up to its count; one not reached (fewer paired repetitions finished than
the look) decides nothing. The rule
is stateless: repetition r runs unless a look at or before r - 1 decided, so every job reads the same answer from the
same files. The final table is read as every table is (tools/live_reps.py, its 95% intervals); the looks only stop it.

Usage: python3 tools/stop_rule.py DIR --rep R [--looks 10,20,40,70] [--precision 0.02]   prints run or stop, and why
       python3 tools/stop_rule.py DIR --report [--looks ...]                             every look, for the summary
Evidence class L (the real cloud's own count of machines); our own code, no outside party has reviewed it.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omnicompass.student_t import coverage  # noqa: E402  (P(|T| ≤ t), the same code every interval uses)

BILL = "machines billed, machine-hours"
HARM = ("response time (ms), 95th percentile", "failed requests (%)")
LEVEL = 0.99
LOOKS = (10, 20, 40, 70)
PRECISION = 0.02


def t_point(df: int, level: float = LEVEL) -> float:
    """The two-sided point of Student's t at this level, by bisection on the coverage (NaN below one degree of freedom)."""
    if df < 1:
        return float("nan")
    lo, hi = 0.0, 1000.0
    for _ in range(90):
        mid = (lo + hi) / 2.0
        lo, hi = (mid, hi) if coverage(mid, df) < level else (lo, mid)
    return (lo + hi) / 2.0


def interval(diffs: list[float], level: float = LEVEL) -> tuple[float, float, float]:
    """Mean of the paired differences and its interval at this level: (mean, low, high)."""
    n = len(diffs)
    m = sum(diffs) / n
    if n < 2:
        return m, float("nan"), float("nan")
    sd = math.sqrt(sum((d - m) ** 2 for d in diffs) / (n - 1))
    h = t_point(n - 1, level) * sd / math.sqrt(n)
    return m, m - h, m + h


def look(native: dict, omni: dict, n: int, precision: float = PRECISION) -> dict:
    """One look at repetitions 1..n (their keys sorted as numbers): the bill's reading and whether the set may stop."""
    reps = sorted(set(native) & set(omni), key=int)[:n]
    if len(reps) < n:
        return {"n": len(reps), "decided": False, "why": f"only {len(reps)} paired repetitions finished, the look needs {n}"}
    diffs = [omni[r][BILL] - native[r][BILL] for r in reps if not math.isnan(omni[r].get(BILL, float("nan")) - native[r].get(BILL, float("nan")))]
    if len(diffs) < n:
        return {"n": len(diffs), "decided": False, "why": "a repetition carries no bill"}
    base = sum(native[r][BILL] for r in reps) / n
    m, lo, hi = interval(diffs)
    out = {"n": n, "bill_pct": m / base * 100, "lo_pct": lo / base * 100, "hi_pct": hi / base * 100}
    harm = []
    for k in HARM:
        d = [omni[r][k] - native[r][k] for r in reps if k in omni[r] and k in native[r]]
        if len(d) >= 2:
            _, hl, _ = interval(d)
            if hl > 0:
                harm.append(k)
    if harm:
        out.update(decided=False, why="a LOSS reads at this look (" + ", ".join(harm) + "): the set runs on to measure it in full")
    elif lo > 0 or hi < 0:
        out.update(decided=True, word="GAIN, a cut" if hi < 0 else "power given", why="the bill's 99% interval clears zero")
    elif (hi - lo) / 2 <= precision * base:
        out.update(decided=True, word="STEADY", why=f"the bill's 99% interval holds zero within ±{precision * 100:g}% of native's bill")
    else:
        out.update(decided=False, why="the bill's 99% interval is wider than the precision and holds zero: not yet read")
    return out


def arms(root: Path) -> tuple[dict, dict]:
    """Every finished repetition's gauges, by arm, read by the repository's own scorer (tools/live_reps.py)."""
    from tools import live_reps as L
    runs: dict = {}
    for d in sorted(Path(root).glob("bench-*-*")):
        _, arm, rep = L.arm_rep(d)
        if (d / "capture.csv").exists() and not (d / "INVALID").exists():
            runs.setdefault(arm, {})[str(rep)] = L.arm_gauges(d)
    return runs.get("native", {}), runs.get("compass", runs.get("omni", {}))


def decide(native: dict, omni: dict, rep: int, looks=LOOKS, precision: float = PRECISION) -> tuple[bool, str]:
    """Whether repetition rep still runs: no look at or before rep - 1 decided."""
    for n in looks:
        if n > rep - 1:
            break
        r = look(native, omni, n, precision)
        if r.get("decided"):
            return False, f"stopped at the look after {n} repetitions: {r['word']} ({r['bill_pct']:+.2f}%, 99% interval {r['lo_pct']:+.2f}% to {r['hi_pct']:+.2f}%), {r['why']}"
    return True, "runs: no look so far has decided"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--rep", type=int)
    ap.add_argument("--looks", default=",".join(map(str, LOOKS)))
    ap.add_argument("--precision", type=float, default=PRECISION)
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args(argv)
    looks = tuple(int(x) for x in a.looks.split(",") if x.strip())
    native, omni = arms(Path(a.root))
    if a.report:
        print(f"Stopping rule: looks at {', '.join(map(str, looks))} paired repetitions, 99% intervals, precision ±{a.precision * 100:g}% of native's bill.")
        for n in looks:
            r = look(native, omni, n, a.precision)
            pct = f" bill {r['bill_pct']:+.2f}% (99% interval {r['lo_pct']:+.2f}% to {r['hi_pct']:+.2f}%)" if "bill_pct" in r else ""
            print(f"- look after {n}:{pct} {'decided: ' + r['word'] if r.get('decided') else 'not decided'}; {r['why']}")
            if r.get("decided"):
                break
        return 0
    if a.rep is None:
        ap.error("--rep or --report")
    go, why = decide(native, omni, a.rep, looks, a.precision)
    print(("run" if go else "stop") + ": " + why)
    gh = os.environ.get("GITHUB_OUTPUT")
    if gh:
        with open(gh, "a", encoding="utf-8") as f:
            f.write(f"run={'true' if go else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
