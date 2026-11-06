# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The orchestra, the eighth organism (the founder's word of 19 October, night: "governors and orchestrators in their own
category or catalog group organism ... benchmark them on the organism native, and then Omni on top of them on top of the
organism"): every catalog muscle that stands for a knob of a governor or orchestrator he named (tools/governors_page.py,
CATALOG), run like the seven organisms of tools/run_realms_v5.py: each governor's muscles as a body of its own ("in their
own field") and all of them together as one body, the orchestra; native, then Omni-Compass on top at the max
(realms/compass_arm_v5.py), under the organism loads (its own load, the climb, work waiting in line), on the realms'
preregistered seeds (3000-3009). Evidence class S (modelled), deterministic: the same commit gives the same table. A
grouping of catalog rows made here, as the seven are made in their runner; no engine file names it.
Usage: python3 tools/run_orchestra.py [--out results/orchestra] [--workers N]"""
from __future__ import annotations

import argparse, hashlib, json, os, subprocess, sys, time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.readings import labelled, receipt_key  # noqa: E402
from tools.governors_page import CATALOG, GOVERNORS  # noqa: E402
import tools.run_realms_v5 as R  # noqa: E402

ORCHESTRA = "orchestra"
OUT = ROOT / "results" / "orchestra"


def bodies(rows):
    """{body: rows}: each governor's muscles as a body of its own, in the founder's order of naming, then the orchestra,
    every muscle once."""
    by_name = {r["muscle"]: r for r in rows}
    out = {}
    for slug, *_ in GOVERNORS:
        fid, muscles = CATALOG[slug]
        out[slug] = [by_name[m] for m in muscles if by_name.get(m) and by_name[m]["family_id"] == str(fid)]
    seen, every = set(), []
    for rs in out.values():
        for r in rs:
            if r["muscle_id"] not in seen:
                seen.add(r["muscle_id"]); every.append(r)
    out[ORCHESTRA] = every
    return out


def aggregate(runs):
    valid = all(o["restore_ok"] for o in runs)
    per = [o["max"] for o in runs]
    agg = defaultdict(lambda: [0.0, 0, 0])
    for o in runs:
        for mid, dw, dv in o["harms"]:
            agg[mid][0] += dw / len(runs); agg[mid][1] += dv; agg[mid][2] += 1
    return {"valid": valid, "label": R.label_max(per, valid), "summary": R.summarize(per), "per_seed": per,
            "plants_flagged": {mid: v for mid, v in agg.items() if v[0] < -1e-9 or v[1] > 0},
            "wear": sum(o["wear"] for o in runs) / len(runs),
            "totals": {"viol_native": sum(o["viol_native"] for o in runs), "viol_max": sum(o["viol_max"] for o in runs),
                       "steps": sum(o["steps"] for o in runs)}}


def write_md(out, groups, orgs, run):
    names = {slug: name for slug, name, *_ in GOVERNORS}
    names[ORCHESTRA] = "**The orchestra, every governor's muscle once**"
    L = ["# The orchestra, the eighth organism: the governors' muscles, native and with Omni-Compass on top (modelled)", ""]
    L += receipt_key() + [""]
    L += [f"The founder's word of 19 October, night: the governors and orchestrators in a catalog group, an organism of their "
          f"own, benchmarked native and then with Omni-Compass on top of them. Every catalog muscle that stands for a knob of a "
          f"governor or orchestrator he named (the mapping on the governors page, `tools/governors_page.py`) runs in the "
          f"modelled organisms as the seven do (`tools/run_realms_v5.py`): each governor's muscles as a body of its own, and "
          f"all of them together as one body, the orchestra ({len(groups[ORCHESTRA])} muscles). Native is each muscle's own "
          f"native controller in the catalog, the governor's rule as modelled; omni is Omni-Compass on top at the max, on "
          f"{run['engine']} (digest {run['engine_digest']}), commit `{run['commit'][:12]}`, seeds {run['seeds'][0]}-"
          f"{run['seeds'][-1]} ({len(run['seeds'])} paired seeds per body and load).", "",
          "These are models (evidence class S): a model's energy is not a meter's, and a plant written by the people who "
          "wrote the law is not an independent test. The governors' live results, each on a real Kubernetes cluster with the "
          "governor as shipped and Omni-Compass on top (class L), stand on the governors page (`results/live/GOVERNORS.md`).",
          ""]
    for load in run["loads"]:
        L += [f"## {R.LOADS[load][0].upper() + R.LOADS[load][1:]}", "",
              "Work: the mean over the body's plants of each plant's work against native's. Misses: the plants' decisions "
              "over their own line, native → omni. Power given: the body's energy against native's. Wear: shown, never "
              "judged. 95% intervals over seeds.", "",
              "| Body | Muscles | Reading | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Valid |",
              "|---|---:|---|---:|---|---:|---:|---:|---|"]
        for body in list(groups):
            if body not in orgs[load]:
                continue
            o = orgs[load][body]; s = o["summary"]
            L.append(f"| {names[body]} | {len(groups[body])} | **{labelled(o['label'])}** | {R.fmt(s['work'], 100.0)} | "
                     f"{R.misses_line(o['totals'])} | {R.fmt(s['viol_pp'], 1.0, '')} | {R.fmt(s['energy'])} | "
                     f"{o['wear'] * 100:+.2f}% | {'yes' if o['valid'] else 'NO'} |")
        L.append("")
    L += ["## Inside every body: each plant that did less work than native or missed its line more often", "",
          "| Load | Body | Plants | Plants with less work or more misses | The plants (work change, extra decisions over the line, all seeds) |",
          "|---|---|---:|---:|---|"]
    for load in run["loads"]:
        for body in list(groups):
            o = orgs[load].get(body)
            if not o:
                continue
            h = o["plants_flagged"]
            lst = "; ".join(f"{mid} ({v[0] * 100:+.3f}%, {v[1]:+d})" for mid, v in sorted(h.items(), key=lambda kv: kv[1][0])) or "none"
            L.append(f"| {load} | {names[body]} | {len(groups[body])} | {len(h)} | {lst} |")
    L += ["", "## The muscles", "", "| Body | Muscles (catalog family) |", "|---|---|"]
    for body, rs in groups.items():
        L.append(f"| {names[body]} | " + ", ".join(f"`{r['muscle']}` ({r['family_id']})" for r in rs) + " |")
    L += ["", "Raw per-seed contrasts: `ORCHESTRA.json`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`."]
    (out / "ORCHESTRA.md").write_text("\n".join(stamp(L)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows = R.catalog(str(ROOT / "realms" / "catalog_v5.csv"))
    groups = bodies(rows)
    from tools.omni_version import engine_files, version_of, digest
    snap = engine_files()
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + R.FROZEN + ["tools/run_orchestra.py", "tools/governors_page.py"],
                           cwd=ROOT, capture_output=True, text=True).stdout.strip()
    run = {"started": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "commit": commit, "dirty": bool(dirty),
           "seeds": R.PREREG_SEEDS, "loads": R.ORGANISM_LOADS, "engine": version_of(snap) or "undeclared",
           "engine_digest": digest(snap), "dial": "max", "bodies": {b: [r["muscle_id"] for r in rs] for b, rs in groups.items()}}
    t0 = time.time()
    jobs = [(name, rs, s, load) for load in R.ORGANISM_LOADS for name, rs in groups.items() if rs for s in R.PREREG_SEEDS]
    raw = defaultdict(lambda: defaultdict(dict))
    with ProcessPoolExecutor(a.workers) as ex:
        for name, seed, load, o in ex.map(R.organism_job, jobs):
            raw[load][name][seed] = o
    orgs = {load: {name: aggregate([by_seed[s] for s in R.PREREG_SEEDS]) for name, by_seed in by_name.items()}
            for load, by_name in raw.items()}
    run["elapsed_s"] = round(time.time() - t0)
    (out / "ORCHESTRA.json").write_text(json.dumps({"run": run, "bodies": orgs}, indent=1) + "\n")
    (out / "RUN.json").write_text(json.dumps(run, indent=1) + "\n")
    write_md(out, groups, orgs, run)
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt")
    (out / "SHA256SUMS.txt").write_text("".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in files))
    print(f"orchestra -> {out}/ORCHESTRA.md ({run['elapsed_s']} s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
