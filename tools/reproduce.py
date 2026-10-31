#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every three-run table of the engine that stands, rebuilt from its raw receipts and compared byte for byte.

A table in results/live/ is written by its own tool from three archived runs (the branch raw, opened at
results/live/raw/). This reads how each table of the engine that stands was built (its recipe), rebuilds it into a scratch
folder with the same tool from the same runs, and compares the rebuilt files with the committed ones. Every tool is
deterministic, so a reproduced table is identical to the byte; any difference is printed and fails the run.

Recipes: results/live/RECIPES.json for the tables written by hand (the Kubernetes, capacity and outside-simulator tables),
and results/live/FRONT_PAGE_STATE.json for the tables the front page builds itself (the five data stores).

  python3 tools/reproduce.py                   rebuild every table of the engine that stands and compare; exit 1 on a difference
  python3 tools/reproduce.py --table V11_X     one table
  python3 tools/reproduce.py --patterns        the raw folders the rebuild reads (for scripts/raw_archive.sh open)
  python3 tools/reproduce.py --check-recipes   exit 1 when a table of the engine that stands has no recipe (verify.py)
"""
from __future__ import annotations

import argparse, json, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
LIVE = ROOT / "results" / "live"
ORCH = ROOT / "results" / "orchestrator"     # the orchestrator's three-arm tables (tools/three_arms_abc.py)
RAW = LIVE / "raw"
RECIPES = LIVE / "RECIPES.json"
STATE = LIVE / "FRONT_PAGE_STATE.json"
TABLE = re.compile(r"^V(\d+)_([A-Z0-9_]+)\.md$")


def engine_number() -> int:
    from tools import omni_version as ov
    m = re.search(r"omni-v(\d+)", ov.version_of(ov.engine_files()) or "")
    return int(m.group(1)) if m else 0


def recipes() -> dict:
    """{table: {"tool", "args", "runs"}} for every table with a recipe: RECIPES.json, then the front page's own builds."""
    from tools import front_page as fp
    out = {}
    if RECIPES.exists():
        out.update({k: v for k, v in json.loads(RECIPES.read_text()).items() if not k.startswith("_")})
    if STATE.exists():
        for name, s in json.loads(STATE.read_text()).items():
            base = re.sub(r"^V\d+_", "", name).split("_")[0]
            tool = next((t for p, (b, t) in fp.PRODUCTS.items() if b == base), None)
            if tool and s.get("runs") and name not in out:
                out[name] = {"tool": tool, "args": [], "runs": [f"run-{r}" for r in s["runs"]]}
    return out


def tables_of(v: int) -> list:
    return sorted(p.stem for d in (LIVE, ORCH) for p in d.glob(f"V{v}_*.md") if TABLE.match(p.name))


def check_recipes(v: int) -> list:
    """The tables of engine v that have no recipe."""
    have = recipes()
    return [t for t in tables_of(v) if t not in have]


def patterns(names) -> list:
    """The raw folders the named tables read, as patterns for scripts/raw_archive.sh open."""
    rs = recipes()
    return sorted({"/" + r.split("/")[0] + "/" for n in names for r in rs[n]["runs"]})


def rebuild(name: str, r: dict, scratch: Path):
    """Rebuild one table into scratch; returns [(file, 'same' | 'differs' | 'missing')]."""
    dirs = [str(RAW / run) for run in r["runs"]]
    missing = [d for d in dirs if not Path(d).is_dir()]
    if missing:
        return [(name, "raw folder not opened: " + ", ".join(Path(m).relative_to(RAW).as_posix() for m in missing))]
    out = scratch / f"{name}.md"
    p = subprocess.run([sys.executable, str(ROOT / r["tool"]), *r.get("args", []), *dirs, "--out", str(out)],
                       capture_output=True, text=True, cwd=ROOT)
    if p.returncode != 0:
        return [(name, f"{r['tool']} failed: {(p.stdout + p.stderr).strip()[-300:]}")]
    built_json = scratch / f"{name}.json"
    if built_json.exists() and not isinstance(json.loads(built_json.read_text()).get("rows"), list):
        from tools.reread import reread_pair   # every published table stands read again by the rule that stands (verify.py)
        reread_pair(built_json)
    res = []
    for built in sorted(scratch.glob(f"{name}.*")):
        mine = (ORCH if name.endswith("_THREE_ARMS_ABC") else LIVE) / built.name
        res.append((built.name, "missing in results/live" if not mine.exists() else
                    "same" if mine.read_bytes() == built.read_bytes() else "differs"))
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--table", action="append")
    ap.add_argument("--patterns", action="store_true")
    ap.add_argument("--check-recipes", action="store_true")
    a = ap.parse_args(argv)
    v = engine_number()
    if a.check_recipes:
        miss = check_recipes(v)
        print(f"reproduce: every omni-v{v} table has a recipe" if not miss else
              f"reproduce: omni-v{v} tables with no recipe (results/live/RECIPES.json): {', '.join(miss)}")
        return 1 if miss else 0
    names = a.table or [t for t in tables_of(v) if t in recipes()]
    if a.patterns:
        print(" ".join(patterns(names)))
        return 0
    rs, bad = recipes(), 0
    with tempfile.TemporaryDirectory() as t:
        for n in names:
            for f, res in rebuild(n, rs[n], Path(t)):
                ok = res == "same"
                bad += not ok
                print(f"{'same   ' if ok else 'DIFFERS'} {f}" + ("" if ok else f": {res}"))
    engines = sorted({int(m.group(1)) for n in names for m in [re.match(r"V(\d+)_", n)] if m}) or [v]
    print(f"reproduce: {len(names)} {' and '.join(f'omni-v{e}' for e in engines)} tables rebuilt from their raw receipts, "
          + ("every file identical to the byte" if not bad else f"{bad} files not identical"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
