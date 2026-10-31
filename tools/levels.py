#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every level on one page: Omni-Compass on top of the muscle, the organism, the cluster, the cluster with its add-ons, the
service, the physical plant, the organism with the cluster inside, the cloud and the group of clusters (the founder's order
of 17 October, evening: "on top of the muscle, on top of the stack, on top of the cluster, on top of the group of clusters,
all different levels and settings and gauges ... they will all be going in the same direction, and if they're not, we need
to talk to me").

Built from the result files as they stand (the realms result for the muscles and organisms, the three-run tables for
everything real), never typed in. For each level: the engine its tables ran on, the evidence class, how many judged gauges
read GAIN, STEADY, power given and LOSS, how many the runs disagree on, and every gauge that points the other way, named with
its table, so nothing that goes against the rest is hidden in a total. A level with no run yet says so.

  python3 tools/levels.py            write docs/LEVELS.md
  python3 tools/levels.py --check    exit 1 when docs/LEVELS.md differs from what the files give
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                       # noqa: E402
from tools.readings import receipt_key, with_own_runs, landed      # noqa: E402

OUT = ROOT / "docs" / "LEVELS.md"
LIVE = ROOT / "results" / "live"
REALMS = ROOT / "results" / "realms_v5"

# (level, evidence class, the tables' stems in results/live/, what native is at that level)
TABLE_LEVELS = [
    ("The cluster: real Kubernetes, native its own HPA and scheduler", "L",
     ["ALL_FOUR", "BATCH", "CAPACITY", "FAIRNESS", "FAULTS", "TRACE_GOOGLE2011", "ROBUST_KILL", "ROBUST_LONG"],
     "Kubernetes as shipped with the operator's HPA target"),
    ("The cluster with its add-ons native: KEDA, Goldilocks, CruiseKube", "L",
     ["KEDA_REQUESTS", "KEDA_CPU_REQUESTS", "GOLDILOCKS", "CRUISEKUBE"],
     "Kubernetes with the add-on as shipped and as used, its own recommendations applied"),
    ("A muscle inside a running service: database, broker, cache", "L",
     ["REDIS", "REDIS_SERVICE", "KAFKA", "KAFKA_SERVICE", "PGBENCH", "SYSBENCH", "YCSB"],
     "the server as shipped but for the one setting an operator sets (each table names it)"),
    ("A physical plant in an independent simulator: buildings, power grids, robot arms, drone swarms", "independent simulator",
     ["CITYLEARN", "PANDAPOWER", "MUJOCO", "SWARM"],
     "the simulator's own controller, unchanged"),
]
KIND = {"GAIN": "GAIN", "LOSS": "LOSS", "power given": "power given", "STEADY": "STEADY", "disagree": "the runs disagree"}


def kind_of(reading: str) -> str | None:
    r = reading.strip("* ").lower()
    if not r or r.startswith("shown") or r == "reading":
        return None
    if "disagree" in r or "different ways" in r:
        return "disagree"
    if r.startswith("gain") or "agree: gain" in r:
        return "GAIN"
    if r.startswith("loss") or "agree: loss" in r:
        return "LOSS"
    if r.startswith("power given") or "agree: power given" in r:
        return "power given"
    if r.startswith(("steady", "even")):
        return "STEADY"
    return None


def newest_table(stem: str) -> Path | None:
    """The table of this benchmark on the newest engine that has one with a reading (V8_ before V7_ ...; tools/readings.py,
    landed: a table whose runs share no workload leaves the older engine's table standing)."""
    found = [p for p in sorted(LIVE.glob(f"V[0-9]*_{stem}.md"), key=lambda p: int(re.match(r"V(\d+)_", p.name).group(1)), reverse=True)
             if re.fullmatch(rf"V\d+_{re.escape(stem)}\.md", p.name)]
    return next((p for p in found if landed(p)), found[0] if found else None)


def engine_of(text: str, name: str) -> str:
    m = re.search(r"\(Omni (v\d+)\)", text.split("\n", 1)[0])
    if m:
        return f"omni-{m.group(1)}"
    m = re.search(r"\b(omni-v\d+)\b", text)
    return m.group(1) if m else re.match(r"V(\d+)_", name).expand(r"omni-v\1")


def table_rows(path: Path):
    """(section, gauge, reading kind) for every judged row of a three-run table, read from its Markdown."""
    section, out = "", []
    for ln in path.read_text().splitlines():
        if ln.startswith("#"):
            section = ln.lstrip("# ").strip()
        if not ln.startswith("|") or ln.startswith("|---"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < 3:
            continue
        k = kind_of(cells[-1])
        if k:
            out.append((section, cells[0], k))
    return out


def realms_levels():
    """The muscle alone and the organisms (modelled, class S), from the realms result."""
    run = json.loads((REALMS / "REALMS_V5.json").read_text())
    eng = run["run"]["engine"]
    labels = [r["label_all_loads"] for r in csv.DictReader(open(REALMS / "MUSCLES_V5.csv")) if r["load"] == "normal"]
    c = Counter("STEADY" if lab in ("SAME AS NATIVE", "AT ITS LIMIT ON NATIVE") else
                "LOSS" if lab.startswith(("LESS WORK", "SLOWER", "MORE MISSES")) else
                "disagree" if "AND" in lab and "LOSS" in lab else "GAIN" for lab in labels)
    against = [f"{r['family']} / {r['muscle']} ({r['label_all_loads']})" for r in csv.DictReader(open(REALMS / "MUSCLES_V5.csv"))
               if r["load"] == "normal" and not (r["label_all_loads"] in ("SAME AS NATIVE", "AT ITS LIMIT ON NATIVE")
                                               or r["label_all_loads"].startswith(("MORE WORK", "FASTER", "FEWER MISSES")))]
    muscle = {"level": "The muscle, alone (1,107 muscles, each on its own native controller, under its own load)", "engine": eng,
              "evidence": "S (our model)", "tables": ["results/realms_v5/MUSCLES_V5.csv"], "native": "each muscle's native controller",
              "count": c, "against": against,
              "note": f"{labels.count('AT ITS LIMIT ON NATIVE')} of the STEADY are at their limit on native (nothing to push)"}
    oc, flagged = Counter(), []
    for load, orgs in run["organisms"].items():
        for name, o in orgs.items():
            lab = o["label"]
            oc["STEADY" if lab in ("SAME AS NATIVE", "AT ITS LIMIT ON NATIVE") else
               "LOSS" if lab.startswith(("LESS WORK", "SLOWER", "MORE MISSES")) else "GAIN"] += 1
            for p in o.get("plants_flagged") or []:
                flagged.append(f"{name}, {load} load: {p if isinstance(p, str) else p.get('plant', p)}")
    organism = {"level": "The organism, the stack: the seven organisms under three loads (own load, the climb, work waiting in line)",
                "engine": eng, "evidence": "S (our model)", "tables": ["results/realms_v5/REALMS_V5.md"],
                "native": "every muscle on its native controller, coupled in one body", "count": oc,
                "against": [], "inside": flagged,
                "note": ("the organism's own reading; " + (f"{len(flagged)} plants inside them did less work or missed their line more "
                         "often than native, listed below" if flagged else "inside them no plant did less work or missed its line more "
                         "often than native, under any load (the realms result's stricter look, plant by plant)"))}
    return [muscle, organism]


def table_level(level, evidence, stems, native):
    c, against, tables, engines, missing = Counter(), [], [], set(), []
    for stem in stems:
        p = newest_table(stem)
        if p is None:
            missing.append(stem)
            continue
        text = p.read_text()
        engines.add(engine_of(text, p.name))
        tables.append(str(p.relative_to(ROOT)))
        for section, gauge, k in table_rows(p):
            c[k] += 1
            if k in ("LOSS", "disagree"):
                against.append(f"{p.name}: {section}: {gauge} ({KIND[k]})")
    return {"level": level, "engine": ", ".join(sorted(engines)) or "none yet", "evidence": evidence, "tables": tables,
            "native": native, "count": c, "against": against, "missing": missing}


def build():
    levels = realms_levels()
    for level, ev, stems, native in TABLE_LEVELS:
        levels.append(table_level(level, ev, stems, native))
    six = [p for p in ("SIX_KUBE.md", "V3_SIX_KUBE.md", "V3_BIG_ORGANISM.md") if (LIVE / p).exists()]
    levels.append({"level": "The organism with the real cluster inside (the grid, at 1, 10, 100 and on GitHub's machines 1,000 copies)",
                   "engine": "older engines' tables; the grid runs again on the engine that stands", "evidence": "L, the cluster; S, the organism",
                   "tables": [f"results/live/{p}" for p in six], "native": "the organism's native controllers around Kubernetes with its HPA",
                   "count": None, "against": [],
                   "note": "no table on the engine that stands yet; the grid's runs (results/grid_v8/) are going"})
    levels.append({"level": "The cluster in a cloud: Azure Kubernetes Service, the bill", "engine": "single runs, omni-v5 to omni-v7",
                   "evidence": "L, the bill metered", "tables": ["results/live/AKS_BILL.md", "results/live/raw/run-38981149348/"],
                   "native": "Azure's own cluster autoscaler and the HPA", "count": None, "against": [],
                   "note": "no three-run table yet: eight single runs at the tune-down, machines billed −6.5% to +7.6%, every one STEADY; "
                           "the fleet (about 1.9 of 4 machines busy) leaves no whole machine to give back"})
    levels.append({"level": "A group of clusters", "engine": "not run", "evidence": "none yet", "tables": [],
                   "native": "each cluster's own autoscaler", "count": None, "against": [],
                   "note": "no run at this level yet, real or modelled, on the engine that stands (`k8s_fleet/` holds a model of an earlier engine)"})
    return levels


# A row an older engine's table read LOSS whose cause a later engine already repaired: said beside the row, never in its place.
REPAIRED = {("V7_CITYLEARN.md", "citylearn_challenge_2023"): "; repaired in omni-v8: a battery that carries its building "
            "through an outage stays native, so Omni-Compass reads native's own number there (`docs/OMNI_V8.md`); its three runs "
            "on the engine that stands are running"}


def repaired(row: str) -> str:
    return next((note for (table, part), note in REPAIRED.items() if row.startswith(table) and part in row), "")


def render(levels):
    L = ["# Every level: Omni-Compass on top of the muscle, the organism, the cluster, the service, the plant, the cloud", "",
         *receipt_key(), "",
         "The founder's order of 17 October: Omni-Compass is shown on top at every level, on every gauge, and every level's gauges "
         "should go the same way; where one does not, it is named here and taken to the founder. Each row is built from its result "
         "files by `tools/levels.py`; nothing is typed in. A count is of judged gauges (a table's rows that read a word), each "
         "under its own table's rule (the three runs, or the realms result's ten seeds); **power given** is a resource put in, "
         "shown and never called a loss. Every row names the engine its tables ran on, and no reading is carried from one engine "
         "to another.", "",
         "| Level | Engine | Evidence | GAIN | STEADY | power given | LOSS | runs disagree | Goes the other way? |",
         "|---|---|---|---:|---:|---:|---:|---:|---|"]
    for lv in levels:
        c = lv["count"]
        if c is None:
            L.append(f"| {lv['level']} | {lv['engine']} | {lv['evidence']} | – | – | – | – | – | {lv.get('note', '')} |")
            continue
        other = len(lv["against"]) + len(lv.get("inside") or [])
        word = "no: every judged gauge GAIN or STEADY" if not other and not c.get("power given") else \
               ("no LOSS; resources put in shown as power given" if not other else f"**yes: {other}, listed below**")
        L.append(f"| {lv['level']} | {lv['engine']} | {lv['evidence']} | {c.get('GAIN', 0)} | {c.get('STEADY', 0)} | "
                 f"{c.get('power given', 0)} | {c.get('LOSS', 0)} | {c.get('disagree', 0)} | {word} |")
    L += ["", "## Each level", ""]
    for lv in levels:
        L += [f"### {lv['level']}", "", f"Native at this level: {lv['native']}. Engine: {lv['engine']}. Evidence: {lv['evidence']}."]
        if lv.get("note"):
            L.append(f"{lv['note'][0].upper()}{lv['note'][1:]}.")
        if lv["tables"]:
            L.append("Tables: " + ", ".join(f"`{t}`" for t in lv["tables"]) + ".")
        if lv.get("missing"):
            L.append("No table yet for: " + ", ".join(lv["missing"]) + ".")
        if lv["against"]:
            L += ["", "Goes the other way:", ""] + [f"- {a}{repaired(a)}" for a in lv["against"]]
        if lv.get("inside"):
            L += ["", "Inside the organisms, the plants that did less work or missed their line more often than native:", ""]
            L += [f"- {a}" for a in lv["inside"]]
        L.append("")
    return "\n".join(legal_stamp(with_own_runs(L))) + "\n"


def main(argv):
    md = render(build())
    if "--check" in argv:
        same = OUT.exists() and OUT.read_text() == md
        print("levels: docs/LEVELS.md " + ("matches the files" if same else "differs from the files: run python3 tools/levels.py"))
        return 0 if same else 1
    OUT.write_text(md)
    print(f"{OUT.relative_to(ROOT)} written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
