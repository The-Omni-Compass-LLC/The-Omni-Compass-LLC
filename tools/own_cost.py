# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governor's own cost at 1, 10, 100 and 1,000 copies (docs/ROBUSTNESS_PREREGISTRATION.md, scenario 3), from runs
already archived: every omni arm's audit carries one "overhead" record (the CPU seconds of the governor's process and of
every command it ran, over the window, as a share of one core), written by the controller at exit. Nothing is rerun. Each
archived run is tabulated under the engine its commit carries (tools/omni_version.py), and nothing is read across engines.
Usage: python tools/own_cost.py results/live/raw/run-<id> [more run dirs] --out results/live/V3_OWN_COST.md"""
from __future__ import annotations

import argparse, csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.confirm_abc import ARMS, engine        # noqa: E402
from tools.legal import stamp as _legal_stamp     # noqa: E402

CELL = re.compile(r"^six-(?P<org>.+)-x(?P<copies>\d+)-(?P<rep>\d+)$")
ALIAS = {"organism_656": "tower", "stack_1226": "stack"}


def cells(run_dir: Path):
    """(organism, copies, repetition, overhead record, host cores) for every omni arm with an overhead record."""
    out = []
    for cell in sorted(run_dir.iterdir()):
        m = CELL.match(cell.name)
        if not m or not cell.is_dir():
            continue
        arm_dir = next((cell / f"bench-{a}-{m['rep']}" for a in ARMS if (cell / f"bench-{a}-{m['rep']}").exists()), None)
        if arm_dir is None or not (arm_dir / "audit.jsonl").exists():
            continue
        over = None
        for line in open(arm_dir / "audit.jsonl"):
            if '"overhead"' in line:
                over = json.loads(line)["overhead"]
        cores = None
        if (arm_dir / "host_cpu.csv").exists():
            rows = [r for r in csv.DictReader(open(arm_dir / "host_cpu.csv")) if r.get("cores")]
            cores = float(rows[-1]["cores"]) if rows else None
        if over:
            out.append((ALIAS.get(m["org"], m["org"]), int(m["copies"]), int(m["rep"]), over, cores))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", nargs="+"); ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    L = ["# The governor's own cost at 1, 10, 100 and 1,000 copies", "",
         "Omni-Compass's own CPU: the seconds its process and every command it ran spent on the CPU over the measured window, as a share of "
         "one core, from the `overhead` record every omni arm's audit carries (`omni_controller/controller.py`, written at exit), with the host's "
         "core count beside it. Native runs no governor: its cost is zero by construction. The organisms are the six with the real cluster inside "
         "(`tools/run_kil.py`); the governor's cost is the cost of governing the real cluster, which does not grow with the organism around it. Each "
         "run is shown under the engine its commit carries, and nothing is read across engines (`docs/ROBUSTNESS_PREREGISTRATION.md`, scenario 3). "
         "Shown, not judged.", ""]
    data = {}
    for d in a.runs:
        run = Path(d).resolve().name.replace("run-", "")
        rows = cells(Path(d))
        # the engine of the commit the arms actually ran (preflight.txt in every arm): a detached machine's files are
        # collected by a later GitHub run on a later commit, so the collecting run's commit is not the engine
        shas = set()
        for cell in Path(d).glob("six-*/bench-*/preflight.txt"):
            m = re.search(r"^git_commit=([0-9a-f]{40})", cell.read_text(), re.M)
            if m:
                shas.add(m.group(1))
        if len(shas) == 1:
            sha = shas.pop()
            import subprocess
            out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT, capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
            sha, ver = sha[:12], (out[0] if out else "unknown")
        else:
            sha, ver = engine(run)
        if not rows:
            L += [f"## Run {run} (`{sha}`, {ver}): no omni arm with an overhead record", ""]; continue
        L += [f"## Run {run} (`{sha}`, {ver})", "", "| Organism | Copies | Repetitions | Omni's own CPU (cores), mean | As a share of the host's cores | CPU seconds, mean | Window (s), mean |", "|---|---:|---:|---:|---:|---:|---:|"]
        by = {}
        for org, copies, rep, over, cores in rows:
            by.setdefault((org, copies), []).append((over, cores))
        for (org, copies), xs in sorted(by.items(), key=lambda kv: (kv[0][1], kv[0][0])):
            cm = sum(float(o.get("cores_mean", 0)) for o, _ in xs) / len(xs)
            cpu = sum(float(o.get("cpu_s", 0)) for o, _ in xs) / len(xs)
            wall = sum(float(o.get("wall_s", 0)) for o, _ in xs) / len(xs)
            cs = [c for _, c in xs if c]
            share = f"{100 * cm / (sum(cs) / len(cs)):.2f}% of {sum(cs) / len(cs):.0f}" if cs else "host cores not recorded"
            L.append(f"| {org} | {copies:,} | {len(xs)} | {cm:.4f} | {share} | {cpu:.1f} | {wall:.0f} |")
            data.setdefault(f"{run}", {})[f"{org} x{copies}"] = {"engine": ver, "cores_mean": cm, "cpu_s": cpu, "wall_s": wall, "repetitions": len(xs), "host_cores": (sum(cs) / len(cs) if cs else None)}
        L.append("")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(L)) + "\n"); out.with_suffix(".json").write_text(json.dumps(data, indent=1) + "\n")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
