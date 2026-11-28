#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The one benchmark: every scenario, one engine, every receipt (the founder's words of 15 November: "we need one full final
benchmark that shows everything with one mechanism wired in, producing all the receipts through one full engine instead of
pieces and parts of engines and pieces of parts of receipts").

  python3 tools/the_benchmark.py            write results/THE_BENCHMARK.md and .json
  python3 tools/the_benchmark.py --check    fail when the page differs from the records it is read from

Read from the repository's own records and nothing else: the engine that stands (its fingerprint, OMNI_V<n>.json, and the C++
twins sealed beside it, results/SEAL.json); every benchmark's newest three-run table and whether it stands on that engine, carries
to it, or runs again on it (tools/carry.py, followed import by import through the fingerprint), with its judged rows counted by
word; every paid scenario wired and waiting for the founder's word (each cloud's queue and its switch, the chip workflows); and our
own models (class S, never proof). A table on an older engine is its own engine's record and is never counted as the engine's
that stands: the page says, row by row, which receipts the one engine has given and which it has still to give.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.chips_board import TOP, END  # noqa: E402  (one notice)
from tools.readings import classify, judged as is_judged  # noqa: E402  (the one key)
from tools import carry  # noqa: E402
from tools.loss_ledger import section, SECTIONS  # noqa: E402  (which arms a table sets side by side, as the LOSS ledger reads it)

OUT_MD, OUT_JSON = ROOT / "results" / "THE_BENCHMARK.md", ROOT / "results" / "THE_BENCHMARK.json"
WORDS = ("GAIN", "LOSS", "power given", "the runs disagree", "STEADY")
STORES = ("PGBENCH", "SYSBENCH", "YCSB", "KAFKA", "REDIS")
GOVERNORS = ("KUEUE", "VOLCANO", "KAI", "KOORDINATOR", "BINPACK", "CRUISEKUBE", "GOLDILOCKS", "KEDA", "ARMADA", "KARMADA", "OCM",
             "GODEL", "KUBERAY", "CRANE")
PLANTS = ("CITYLEARN", "PANDAPOWER", "MUJOCO", "SWARM")
PLACES = ("the chip (class P: the card's own meter)", "through the cloud (class L: the cloud's own bill)", "Kubernetes (class L)",
          "the governors and orchestrators on Kubernetes (class L)", "Omni-Compass's own orchestrator (class L)",
          "the data stores (class L)", "the grid, the batteries and the robots (class L)")
CHIP_WORKFLOWS = (("aws-gpu.yml", "Amazon, one card (g5.xlarge): probe, then one card at 1, 10 and 100 copies"),
                  ("lambda-gpu.yml", "Lambda: the A10 and A100 cards, the organisms on the chip"),
                  ("gpu-bench.yml", "the card benchmark on a machine the founder attaches"))
MODELS = (("results/realms_v5", "the 1,107 muscles and the seven organisms, native, Omni-Compass on native and by itself"),
          ("results/orchestra", "the orchestra: every governor's and orchestrator's muscles"),
          ("results/orchestrator", "Omni-Compass's own orchestrator, the three arms"),
          ("results/RUNS_LEDGER.md", "the Python's runs and the core's Monte Carlo from the jump generator, with the C++ twin"),
          ("results/model_gate", "the model gate: each version against the one before"))


def place(row) -> str:
    name, table = row["benchmark"], row["table"]
    if table.startswith("results/gpu/"):
        return PLACES[0]
    if table.startswith("results/orchestrator/"):
        return PLACES[4]
    if name.startswith("AKS_"):
        return PLACES[1]
    if name.startswith(STORES):
        return PLACES[5]
    if name.startswith(PLANTS):
        return PLACES[6]
    if name.startswith(GOVERNORS) or "_4W_" in name:
        return PLACES[3]
    return PLACES[2]


KEY = {"gain": "GAIN", "loss": "LOSS", "given": "power given", "disagree": "the runs disagree", "same": "STEADY", "noise": "STEADY"}


def judged(table: str) -> dict:
    """Every reading the table holds, wherever it keeps it (rows, nested rows, the workloads' gauges; the tuning workload aside),
    counted by its word as the LOSS ledger walks them (tools/loss_ledger.py): GAIN, LOSS and power given only where judged (in
    all three runs, or by the mean of the three at 0.5% or more); STEADY and the runs disagree as they read; shown only, none."""
    p = ROOT / table
    if p.suffix != ".json":
        return {}
    try:
        d = json.loads(p.read_text())
    except (OSError, ValueError):
        return {}
    c = Counter()

    def walk(o):
        if isinstance(o, dict):
            r = o.get("reading")
            if isinstance(r, str):
                try:
                    k = classify(r)
                except ValueError:
                    k = None
                if k in ("gain", "loss", "given") and not is_judged(r):
                    k = "noise"
                if k in KEY:
                    c[KEY[k]] += 1
            for kk, v in o.items():
                if kk not in ("runs", "reading"):
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(d.get("rows") or {})
    for wl, gs in (d.get("workloads") or {}).items():
        if wl != "tuning":
            walk(gs)
    return dict(c)


def queues() -> list:
    out = []
    for q in sorted((ROOT / "scripts").glob("*_queue.txt")):
        lines = [x.strip() for x in q.read_text().splitlines() if x.strip() and not x.lstrip().startswith("#")]
        sw = next((x.split("=", 1)[1].strip() for x in lines if x.startswith("switch=")), "on")
        sets = [x.split("|", 1)[0].strip() for x in lines if "|" in x and not x.startswith(("switch=", "added="))]
        out.append({"cloud": q.name.replace("_queue.txt", ""), "queue": f"scripts/{q.name}", "switch": sw, "sets": sets})
    return out


def build() -> dict:
    rec = carry.build()
    stand = rec["engine_standing"]
    n = int(stand.split("v")[-1])
    fp = json.loads((ROOT / f"OMNI_V{n}.json").read_text())
    seal = json.loads((ROOT / "results" / "SEAL.json").read_text()) if (ROOT / "results" / "SEAL.json").exists() else {}
    rows = []
    for r in rec["rows"]:
        rows.append({**r, "place": place(r), "against": section(r["benchmark"]),
                     "judged": judged(r["table"]) if r["state"] == "on the engine that stands" else {}})
    by_place = {pl: [r for r in rows if r["place"] == pl] for pl in PLACES}
    on = {sec: Counter() for sec in SECTIONS}
    for r in rows:
        if r["state"] == "on the engine that stands":
            on[r["against"]].update(r["judged"])
    wf = ROOT / ".github" / "workflows"
    return {"engine": {"version": stand, "digest": str(fp.get("digest", ""))[:16], "files": len(fp.get("files") or {}),
                       "cpp_twins": len(seal.get("twins") or {})},
            "counts": rec["counts"], "judged_on_the_engine": {sec: dict(v) for sec, v in on.items()},
            "places": {pl: rs for pl, rs in by_place.items() if rs},
            "waiting": {"clouds": queues(),
                        "chips": [{"workflow": w, "what": what, "wired": (wf / w).exists()} for w, what in CHIP_WORKFLOWS]},
            "models": [{"record": r, "what": what, "present": (ROOT / r).exists()} for r, what in MODELS]}


def cnt(c: dict) -> str:
    return ", ".join(f"{w} {c[w]}" for w in WORDS if c.get(w)) or "none judged"


def render(b: dict) -> str:
    e, c = b["engine"], b["counts"]
    total = sum(c.values())
    L = [f"# The one benchmark: every scenario on {e['version']}", "", f"> {TOP}", "",
         "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "",
         "One engine. Every scenario. Every receipt. Nothing on this page asks to be believed: each line names the file it comes "
         "from, and `python3 tools/the_benchmark.py` writes the page again from those files. A receipt is the engine's own, carries "
         "to it (not one engine file its runner runs has moved), or runs again on it. A receipt on an older engine is that engine's, "
         "and is not counted here. Each one reads by the one key: GAIN, STEADY, LOSS, power given, with a 0.5% floor. The LOSS rows "
         "are printed in the same tables as the GAIN rows, because a record that hides its losses is not a record. Run it again. "
         "The numbers come out the same, or they do not. That is the whole argument.", "",
         "## 1. The one engine", "",
         f"**{e['version']}**, digest `{e['digest']}`, {e['files']} files under its fingerprint (`OMNI_V{e['version'].split('v')[-1]}.json`), "
         f"the same engine in Python and, for its {e['cpp_twins']} sealed mechanisms, in C++ held to the Python to the last bit "
         "(`results/SEAL.json`). The same governor runs on every place below; what differs per place is the wire to it.", "",
         "## 2. Every scenario on real machines", "",
         f"Of {total} scenarios with a three-run receipt: **{c['on the engine that stands']} on {e['version']}**, "
         f"{c['carries']} carry to it, **{c['runs again']} run again on it**. The rows on the engine's own receipts, by what each "
         "receipt sets side by side (as the LOSS ledger reads them, `docs/LOSS_LEDGER.md`):", "",
         "| Set side by side | Rows by word |", "|---|---|"]
    names = {SECTIONS[0]: "Omni-Compass on native against native alone", SECTIONS[1]: "Omni-Compass by itself, in place of a controller",
             SECTIONS[2]: "Omni-Compass on top of an orchestrator, against the orchestrator alone or compounded"}
    for sec, cc in b["judged_on_the_engine"].items():
        L.append(f"| {names.get(sec, sec)} | {cnt(cc)} |")
    L.append("")
    for pl, rs in b["places"].items():
        k = Counter(r["state"] for r in rs)
        L += [f"### {pl}", "",
              f"{len(rs)} scenarios: {k.get('on the engine that stands', 0)} on {e['version']}, {k.get('carries', 0)} carry, "
              f"{k.get('runs again', 0)} run again.", "",
              f"| Scenario | Its newest receipt | Its engine | On {e['version']} | Its rows by word (on the engine's own receipt) |", "|---|---|---|---|---|"]
        for r in rs:
            t = r["table"]
            L.append(f"| {r['benchmark']} | [{Path(t).name}]({t.replace('results/', '', 1)}) | {r['engine']} | **{r['state']}** | "
                     f"{cnt(r['judged']) if r['state'] == 'on the engine that stands' else '—'} |")
        L.append("")
    L += ["## 3. Wired, waiting for the founder's word", "",
          "Every paid scenario is built and wired as the free ones are (the same governor, the same harness, the same reading); none "
          "starts until its switch is on (the founder's order of 15 November: no chip and no cloud until the mechanism is right).", "",
          "| Cloud | Its queue | Switch | Its sets |", "|---|---|---|---|"]
    for q in b["waiting"]["clouds"]:
        L.append(f"| {q['cloud']} | `{q['queue']}` | **{q['switch']}** | {'; '.join(q['sets']) or 'none listed'} |")
    L += ["", "| Chip workflow | What it runs | Wired |", "|---|---|---|"]
    for ch in b["waiting"]["chips"]:
        L.append(f"| `{ch['workflow']}` | {ch['what']} | {'yes, started only by hand' if ch['wired'] else 'not in this repository'} |")
    L += ["", "## 4. Our own models (class S, never proof)", "",
          "Modelled beside the real runs, never counted as a receipt of a real machine: every organism three ways with the jump "
          "generator and the Monte Carlo, each version's model gate.", "", "| Record | What it holds |", "|---|---|"]
    for m in b["models"]:
        if m["present"]:
            L.append(f"| `{m['record']}` | {m['what']} |")
    L += ["", "---", "", f"*{END}*", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    b = build()
    md, js = render(b), json.dumps(b, indent=1, sort_keys=True) + "\n"
    if "--check" in argv:
        bad = [p.name for p, s in ((OUT_MD, md), (OUT_JSON, js)) if not p.exists() or p.read_text() != s]
        if bad:
            print("the one benchmark out of date (python3 tools/the_benchmark.py): " + ", ".join(bad)); return 1
        print(f"the one benchmark: {sum(b['counts'].values())} scenarios on {b['engine']['version']}, current"); return 0
    OUT_MD.write_text(md); OUT_JSON.write_text(js)
    c = b["counts"]
    print(f"wrote {OUT_MD.relative_to(ROOT)}: {sum(c.values())} scenarios, {c['on the engine that stands']} on "
          f"{b['engine']['version']}, {c['carries']} carry, {c['runs again']} run again")
    return 0


if __name__ == "__main__":
    sys.exit(main())
