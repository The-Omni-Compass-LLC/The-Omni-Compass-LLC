# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Which results carry to the engine that stands: every benchmark's newest table, the engine files its runner imports, and
whether any of them has moved since the table's own engine (results/CARRY.md, results/CARRY.json).

The founder's order of 7 November, evening: "Don't go so far with a version that you can't carry my GPU and CPU and Kubernetes
and clouds. If you're not updating something that's ... doing anything, then we use the one that's got all that if it hasn't
moved." A benchmark's result carries to the engine that stands when every fingerprinted file its runner imports, followed import
by import through the fingerprint (`OMNI_V<n>.json`), has the same bytes on the table's engine and on the engine that stands; then
the engine that stands runs exactly the code that table ran, and its benchmark need not run again for the version number alone.
Where one of those files moved, the benchmark runs again on the engine that stands, and the files that moved are named. The
record is the table's own, under its own engine's name; carrying it says only that the code it measured has not changed.

  python3 tools/carry.py            write results/CARRY.md and results/CARRY.json
  python3 tools/carry.py --check    exit 1 when they differ from what the fingerprints and tables give
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
OUT_MD, OUT_JSON = ROOT / "results" / "CARRY.md", ROOT / "results" / "CARRY.json"
TABLE_DIRS = (ROOT / "results" / "live", ROOT / "results" / "orchestrator", ROOT / "results" / "gpu")
# the runner each kind of benchmark runs: the process whose imports are the engine code it measures
RUNNERS = [(re.compile(r"^(PGBENCH)"), "tools/run_pgbench.py"), (re.compile(r"^(SYSBENCH)"), "tools/run_sysbench.py"),
           (re.compile(r"^(REDIS)"), "tools/run_redis.py"), (re.compile(r"^(YCSB)"), "tools/run_ycsb.py"),
           (re.compile(r"^(KAFKA)"), "tools/run_kafka.py"), (re.compile(r"^(MUJOCO)"), "tools/run_mujoco.py"),
           (re.compile(r"^(SWARM)"), "tools/run_swarm.py"), (re.compile(r"^(CITYLEARN)"), "tools/run_citylearn.py"),
           (re.compile(r"^(PANDAPOWER|SIMBENCH)"), "tools/run_pandapower.py"), (re.compile(r"^(CPU_POWER)"), "tools/run_cpu_power.py"),
           (re.compile(r"^(THREE_ARMS)"), "omni_orchestrator/brain.py")]
GPU_RUNNER, KUBERNETES_RUNNER = "omni_controller/gpu_compass.py", "omni_controller/controller.py"


def fingerprints() -> dict:
    out = {}
    for p in ROOT.glob("OMNI_V*.json"):
        m = re.fullmatch(r"OMNI_V(\d+)\.json", p.name)
        if m:
            out[int(m.group(1))] = json.loads(p.read_text(encoding="utf-8")).get("files", {})
    return out


def runner(directory: Path, name: str) -> str:
    if directory.name == "gpu":
        return GPU_RUNNER
    for rx, path in RUNNERS:
        if rx.search(name):
            return path
    return KUBERNETES_RUNNER        # every other live table runs the Kubernetes governor: the cluster rigs, the governors, the clouds


def _module_file(module: str, files: set) -> str | None:
    p = Path(*module.split("."))
    for c in (str(p.with_suffix(".py")), str(p / "__init__.py")):
        if c in files:
            return c
    return None


def imports(entry: str, files: set) -> set:
    """Every fingerprinted file the entry imports, followed import by import (the entry included), read from the files as they
    stand in this checkout."""
    seen, todo = set(), [entry]
    while todo:
        f = todo.pop()
        if f in seen or f not in files:
            continue
        seen.add(f)
        try:
            tree = ast.parse((ROOT / f).read_text(encoding="utf-8"))
        except (OSError, SyntaxError):
            continue
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                names = [node.module] + [f"{node.module}.{a.name}" for a in node.names]
            for n in names:
                g = _module_file(n, files)
                if g:
                    todo.append(g)
    return seen


def newest_tables(fps: dict) -> list:
    """Each benchmark's newest three-run table on an engine with a fingerprint: (engine, name, directory, path)."""
    found = {}
    for d in TABLE_DIRS:
        # a table's record is its .json where it has one, else its page (the models' tables are written as pages only)
        for p in sorted(d.glob("V*_*.json")) + sorted(q for q in d.glob("V*_*.md") if not q.with_suffix(".json").exists()):
            m = re.fullmatch(r"V(\d+)_(.+)\.(json|md)", p.name)
            if not m or int(m.group(1)) not in fps:
                continue
            key = (d.name, m.group(2))
            if key not in found or int(m.group(1)) > found[key][0]:
                found[key] = (int(m.group(1)), m.group(2), d, p)
    return sorted(found.values(), key=lambda t: (t[2].name, t[1]))


def build() -> dict:
    fps = fingerprints()
    stand = max(fps)
    rows = []
    for n, name, d, path in newest_tables(fps):
        run = runner(d, name)
        files = set(fps[stand]) | set(fps[n])
        used = sorted(imports(run, files))
        moved = sorted(f for f in used if fps[n].get(f) != fps[stand].get(f))
        state = "on the engine that stands" if n == stand else ("carries" if not moved else "runs again")
        rows.append({"benchmark": name, "table": str(path.relative_to(ROOT)), "engine": f"omni-v{n}", "runner": run,
                     "files_run": len(used), "moved": moved, "state": state})
    counts = {s: sum(1 for r in rows if r["state"] == s) for s in ("on the engine that stands", "carries", "runs again")}
    return {"engine_standing": f"omni-v{stand}", "rows": rows, "counts": counts}


def render(rec: dict) -> str:
    from tools.legal import stamp
    s = rec["engine_standing"]
    c = rec["counts"]
    lines = [f"# Which results carry to the engine that stands ({s})", "",
             "Every benchmark's newest three-run table, the engine files its runner imports (followed import by import through the "
             "fingerprint), and whether any of them has moved since the table's own engine. A result **carries** when every one of "
             f"those files has the same bytes on its engine and on {s}: the engine that stands runs exactly the code the table "
             "measured, and the benchmark need not run again for the version number alone. A result **runs again** when one moved; "
             "the files that moved are named. A carried record stays its own engine's, under its own engine's name. Written by "
             "`python3 tools/carry.py` from the fingerprints (`OMNI_V<n>.json`) and the tables; `verify.py` fails a push where it "
             "differs (the founder's order of 7 November, evening).", "",
             f"On {s}: {c['on the engine that stands']} on the engine that stands, {c['carries']} carry, {c['runs again']} run again.", "",
             "| Benchmark | Its newest table | Its engine | The runner | Engine files it runs | Moved since its engine | On " + s + " |",
             "|---|---|---|---|---:|---|---|"]
    for r in rec["rows"]:
        lines.append(f"| {r['benchmark']} | `{r['table']}` | {r['engine']} | `{r['runner']}` | {r['files_run']} | "
                     f"{', '.join('`' + m + '`' for m in r['moved']) if r['moved'] else 'none'} | **{r['state']}** |")
    lines += ["", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    return "\n".join(stamp(lines)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    rec = build()
    md, js = render(rec), json.dumps(rec, indent=1) + "\n"
    if a.check:
        ok = OUT_MD.exists() and OUT_JSON.exists() and OUT_MD.read_text(encoding="utf-8") == md and OUT_JSON.read_text(encoding="utf-8") == js
        print("carry: results/CARRY.md is what the fingerprints and tables give" if ok else
              "carry: results/CARRY.md differs from the fingerprints and tables: python3 tools/carry.py")
        return 0 if ok else 1
    OUT_MD.write_text(md, encoding="utf-8")
    OUT_JSON.write_text(js, encoding="utf-8")
    c = rec["counts"]
    print(f"results/CARRY.md: on {rec['engine_standing']} {c['on the engine that stands']} stand, {c['carries']} carry, {c['runs again']} run again")
    return 0


if __name__ == "__main__":
    sys.exit(main())
