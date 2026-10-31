#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""How small an effect each three-run table can see: the minimum detectable effect of every judged row, from its own
measured intervals (docs/POWER.md).

A row reads STEADY when a run's 95% interval of the paired change includes zero. That says the change is smaller than the
test can resolve, not that it is zero. This tool states how small, for every row of the newest three-run table of each
benchmark:

  SE      the standard error of the paired change in one run: the interval's half-width over t(0.975, n - 1), the same
          Student t quantile the tables use (omnicompass/student_t.py)
  MDE 1   the smallest true change one run detects with 80% power at the two-sided 5% level: (t(0.975) + t(0.80)) SE
  MDE 3   the smallest true change all three runs detect together with 80% power, so the row reads GAIN or LOSS in all
          three of our runs: each run powered at 0.8^(1/3) = 92.8%, (t(0.975) + t(0.928)) SE
  n(5%)   the paired repetitions a run would need for MDE 3 to be 5% of native (the standard error falls as 1/sqrt(n))

Every figure is in percent of native's mean in that run, the largest of the three runs (the most conservative).

  python3 tools/power.py           write docs/POWER.md and results/POWER.json
  python3 tools/power.py --check   exit 1 if docs/POWER.md is not what the tables give now
"""
from __future__ import annotations

import argparse, json, math, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.student_t import coverage, t95  # noqa: E402
from tools.legal import stamp  # noqa: E402
from tools.readings import landed  # noqa: E402

LIVE = ROOT / "results" / "live"
PAGE = ROOT / "docs" / "POWER.md"
DATA = ROOT / "results" / "POWER.json"
TABLE = re.compile(r"^V(\d+)_([A-Z0-9_]+)\.json$")


def t_quantile(p: float, df: int) -> float:
    """The one-sided Student t quantile t(p, df) for p > 0.5, by bisection on the two-sided coverage."""
    target, lo, hi = 2.0 * p - 1.0, 0.0, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if coverage(mid, df) < target else (lo, mid)
    return 0.5 * (lo + hi)


def newest_tables(live: Path = LIVE):
    """{benchmark: (engine number, path)} for the newest three-run table of each benchmark that stores its rows."""
    best = {}
    for p in sorted(live.glob("V*_*.json")):
        m = TABLE.match(p.name)
        if not m:
            continue
        try:
            d = json.loads(p.read_text())
        except ValueError:
            continue
        if not isinstance(d.get("rows"), dict) or not isinstance(d.get("runs"), list) or len(d["runs"]) != 3 or not landed(p):
            continue
        v, name = int(m.group(1)), m.group(2)
        if name not in best or v > best[name][0]:
            best[name] = (v, p)
    return best


def row_power(row, n: int):
    """MDE 1, MDE 3 and n(5%) for one row, in percent of native; None when the row carries no paired interval."""
    runs = row.get("runs")
    if not isinstance(runs, list) or len(runs) != 3 or not all(isinstance(r, dict) and "ci95" in r and "native" in r for r in runs):
        return None
    df = max(n - 1, 1)
    t975, t80, t928 = t95(df), t_quantile(0.80, df), t_quantile(0.8 ** (1.0 / 3.0), df)
    worst = None
    for r in runs:
        lo, hi = r["ci95"]
        nat = abs(r["native"])
        if nat <= 0 or not all(map(math.isfinite, (lo, hi))):
            return None
        se = (hi - lo) / 2.0 / t975
        m1, m3 = 100.0 * (t975 + t80) * se / nat, 100.0 * (t975 + t928) * se / nat
        if worst is None or m3 > worst[1]:
            worst = (m1, m3)
    m1, m3 = worst
    need = math.ceil(n * (m3 / 5.0) ** 2) if m3 > 0 else n
    return {"mde_one_run_pct": round(m1, 2), "mde_three_runs_pct": round(m3, 2), "reps_for_5pct": need}


def build(live: Path = LIVE):
    out = {}
    for name, (v, p) in sorted(newest_tables(live).items()):
        d = json.loads(p.read_text())
        if not all(isinstance(r, dict) for r in d["runs"]):
            continue                                  # a table that does not record its repetitions (the capacity test)
        n = min(int(r.get("paired_repetitions") or 0) for r in d["runs"])
        if n < 2:
            continue
        rows = {}
        for key, row in d["rows"].items():
            pw = row_power(row, n)
            if pw is not None:
                rows[key] = {"reading": row.get("reading", ""), **pw}
        if rows:
            out[name] = {"table": p.name.replace(".json", ".md"), "engine": f"omni-v{v}", "paired_repetitions": n, "rows": rows}
    return out


def page(data) -> str:
    L = ["# How small an effect each test can see: the minimum detectable effect of every judged row", "",
         "Generated by `python3 tools/power.py` from the newest three-run table of each benchmark that stores its rows "
         "(`results/live/V*_*.json`); `tools/power.py --check`, run by `verify.py`, fails a push where this page is not what "
         "the tables give.", "",
         "A row reads **STEADY** when a run's 95% interval includes zero: the change is smaller than the test resolves, not "
         "zero. The columns say how small:", "",
         "- **MDE, one run**: the smallest true change one run detects with 80% power (two-sided 5%).",
         "- **MDE, all three runs**: the smallest true change that reads GAIN or LOSS in all three of our runs with 80% "
         "power (each run at 92.8%).",
         "- **Repetitions for 5%**: the paired repetitions a run would need for the three-run MDE to reach 5% of native.", "",
         "Each figure is in percent of native's mean in the least favourable of the three runs. Every number is computed "
         "from the table's own intervals with the Student t quantiles the tables use (`omnicompass/student_t.py`).", ""]
    for name, t in data.items():
        L += [f"## {name.replace('_', ' ').title()} ({t['engine']}, `{t['table']}`, {t['paired_repetitions']} paired repetitions a run)", "",
              "| Measure | Reading | MDE, one run | MDE, all three runs | Repetitions for 5% |", "|---|---|---:|---:|---:|"]
        for key, r in t["rows"].items():
            L.append(f"| {key} | {r['reading']} | {r['mde_one_run_pct']:.1f}% | {r['mde_three_runs_pct']:.1f}% | {r['reps_for_5pct']} |")
        L.append("")
    even = [(n, k, r) for n, t in data.items() for k, r in t["rows"].items() if r["reading"].startswith("STEADY")]
    wide = [(n, k, r) for n, k, r in even if r["mde_three_runs_pct"] > 10.0]
    L += ["## What the STEADY rows mean", "",
          f"{len(even)} rows read STEADY. In {len(wide)} of them the test could not resolve a change under 10% of native in "
          "all three runs, so STEADY there means \"no change larger than the MDE shown\", and nothing finer is claimed.", ""]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    data = build()
    text = "\n".join(stamp(page(data).split("\n"))) + "\n"
    if args.check:
        ok = PAGE.exists() and PAGE.read_text() == text
        print("power page: current" if ok else "power page: out of date (python3 tools/power.py)")
        return 0 if ok else 1
    PAGE.write_text(text)
    DATA.write_text(json.dumps(data, indent=1) + "\n")
    rows = sum(len(t["rows"]) for t in data.values())
    print(f"power: {rows} judged rows in {len(data)} tables -> {PAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
