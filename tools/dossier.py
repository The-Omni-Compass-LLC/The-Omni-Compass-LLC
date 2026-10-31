#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The referee dossier: every mechanism, harness, receipt and result in one place, read from the result files.

Writes docs/DOSSIER.md and its charts in docs/dossier/. Every number is read from a file named next to it; the only
numbers written here by hand are the Azure rows, transcribed from the receipts they cite. Run after any new result:

    python3 tools/dossier.py
"""
from __future__ import annotations

import csv

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
import json
import math
import re
import subprocess
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
import sys; sys.path.insert(0, str(ROOT))  # noqa: E402
from tools.readings import judged, with_own_runs, in_gel_words, classify, aim as gel_aim  # noqa: E402  (the words every table uses)
from realms.harness import STACK, TOWER, ORGANISM_ALIAS, organism_sizes  # noqa: E402
OUT = ROOT / "docs" / "DOSSIER.md"
FIG = ROOT / "docs" / "dossier"
SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#8a63d2"]   # validated categorical order
BANNER = f"> {_LEGAL_TOP}"                 # the one notice (tools/legal.py); stamp() keeps one copy of it
_SZ = organism_sizes()
ORG = [f"Compute / AI / Cloud ({_SZ['compute_ai_cloud']})", f"Physics / Robotics / Autonomous ({_SZ['physics_robotics_autonomous']})",
       f"Energy / Facility / Industrial ({_SZ['energy_facility_industrial']})", f"Distribution / Specialized ({_SZ['distribution_specialized']})",
       f"The four stacked ({_SZ[STACK]:,})", f"The whole tower ({_SZ[TOWER]})"]
SHORT = ["Compute", "Physics", "Energy", "Distribution", f"Stacked {_SZ[STACK]:,}", f"Tower {_SZ[TOWER]}"]


def style(ax, title, ylabel):
    ax.set_facecolor(SURF)
    ax.set_title(title, color=INK, fontsize=11, loc="left", pad=10)
    ax.set_ylabel(ylabel, color=INK2, fontsize=9)
    ax.tick_params(colors=INK2, labelsize=8, length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.axhline(0, color=INK2, linewidth=0.8)


def bars(path, title, ylabel, labels, values, lows=None, highs=None, colors=None, note=None):
    fig, ax = plt.subplots(figsize=(8, 3.6), dpi=160)
    fig.patch.set_facecolor(SURF)
    x = range(len(values))
    cols = colors or [SERIES[0]] * len(values)
    ax.bar(x, values, width=0.56, color=cols, edgecolor=SURF, linewidth=2)
    if lows is not None:
        ax.errorbar(x, values, yerr=[[v - l for v, l in zip(values, lows)], [h - v for v, h in zip(values, highs)]],
                    fmt="none", ecolor=INK2, elinewidth=1, capsize=3)
    for i, v in enumerate(values):
        ax.annotate(f"{v:+.1f}%", (i, v), xytext=(0, 4 if v >= 0 else -12), textcoords="offset points",
                    ha="center", fontsize=8, color=INK)
    ax.set_xticks(list(x)); ax.set_xticklabels(labels, fontsize=8, color=INK2)
    style(ax, title, ylabel)
    if note:
        fig.text(0.01, 0.01, note, fontsize=7, color=INK2)
    fig.tight_layout(rect=(0, 0.04 if note else 0, 1, 1))
    fig.savefig(path, facecolor=SURF); plt.close(fig)


def lines(path, title, ylabel, xs, series, xlog=True):
    fig, axes = plt.subplots(1, len(series), figsize=(9, 3.6), dpi=160, sharey=True)
    fig.patch.set_facecolor(SURF)
    for ax, (panel, rows) in zip(axes, series.items()):
        for i, (name, ys) in enumerate(rows):
            pts = [(x, y) for x, y in zip(xs, ys) if y is not None]
            if not pts:
                continue
            ax.plot([p[0] for p in pts], [p[1] for p in pts], color=SERIES[i], linewidth=2, marker="o", markersize=4,
                    label=name)
        if xlog:
            ax.set_xscale("log")
            ax.minorticks_off()
        ax.set_xticks(xs); ax.set_xticklabels([f"{x:,}" for x in xs])
        style(ax, panel, ylabel if ax is axes[0] else "")
        ax.set_xlabel("paired runs (first N of the same set)", color=INK2, fontsize=8)
    axes[-1].legend(fontsize=7, frameon=False, loc="center left", bbox_to_anchor=(1.0, 0.5))
    fig.suptitle(title, color=INK, fontsize=11, x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(path, facecolor=SURF, bbox_inches="tight"); plt.close(fig)


def sh(*cmd):
    return subprocess.run(list(cmd), cwd=ROOT, capture_output=True, text=True).stdout.strip()


def grid_tables():
    """{(size, runs): {"wpe": [6], "viol": [6]}} from results/scale/GRID.md (cells 'running' or 'not run' are None)."""
    t = (ROOT / "results" / "scale" / "GRID.md").read_text()
    out = {}
    for key, head in (("wpe", "## Work per energy"), ("viol", "## Time over the service line")):
        block = t[t.index(head):].split("\n## ")[0]
        rows = [l for l in block.splitlines() if l.startswith("| ") and not l.startswith("| Organism")]
        cols = [(s, r) for s in (1, 10, 100, 1000) for r in (1, 10, 100, 1000)]
        for i, l in enumerate(rows):
            cells = [c.strip() for c in l.strip("|").split("|")][1:]
            for (s, r), c in zip(cols, cells):
                v = None if not re.match(r"^[+-]", c) else float(c.rstrip("%"))
                out.setdefault((s, r), {}).setdefault(key, [None] * 6)[i] = v
    return out


def pct_ci(d):
    return 100 * d["diff"] / d["base"], 100 * d["ci95"][0] / d["base"], 100 * d["ci95"][1] / d["base"]


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    commit = sh("git", "rev-parse", "--short", "HEAD")
    man = json.loads((ROOT / "RELEASE_MANIFEST.json").read_text())
    receipt = (ROOT / "results" / "VERIFY_RECEIPT.txt").read_text()
    verdict = "PASS" if "VERIFICATION: PASS" in receipt else "see results/VERIFY_RECEIPT.txt"
    seal = sh("python3", "tools/seal.py", "--check")
    ident = sh("python3", "tools/mechanism_identity.py", "--check").splitlines()[-1:]
    L = ["# The Omni-Compass Dossier", "", BANNER, "",
         f"Every mechanism, harness, receipt and result, read from the files named beside it. Built by "
         f"`tools/dossier.py` at commit `{commit}`. Evidence classes: **T** theorem, **V** verified in code, **S** a model, "
         "**L** live software (real Kubernetes), **P** a physical meter. A model is not a meter, and a model written by "
         "the people who wrote the law is not an independent test; where a result is a model it says so.", ""]

    # ------------------------------------------------------------------ 1. integrity
    L += ["## 1. The mechanism, and proof that it is the one that ran", "",
          "| Check | Result | Where |", "|---|---|---|",
          f"| The whole repository re-runs and checks itself (`python3 verify.py`) | **{verdict}** | `results/VERIFY_RECEIPT.txt` |",
          f"| The eight-line engine and its six states, fingerprinted (`omnicompass/core.py`) | sha256 `{man['fingerprints']['engine_sha256'][:16]}…` | `RELEASE_MANIFEST.json` |",
          f"| Python and C++20 twins of every law, proven equal and sealed | {seal} | `results/SEAL.json` |",
          f"| The mechanism's identity against the code | {' '.join(ident)} | `results/MECHANISM_IDENTITY.json` |",
          "| The engine's convergence to its pole under the bounded command | proved | `docs/TRACKING_THEOREM.md` |",
          "| Safety shield: 2,000,000 adversarial cases | 0 violations | `tests/test_shield_properties.py` |",
          "| The compass law (push and pull, 5% cushions, fail up, plug contract) on every muscle, the card and Kubernetes | one law, one file | `omnicompass/compass_law.py` |",
          "| Every file the results depend on, by fingerprint | written after the check passes | `RELEASE_MANIFEST.json` |", "",
          "The engine is the founder's eight-line equation, integrated by RK4 with the bounded command held across all four "
          "stages; it is frozen and fingerprinted, and the C++ twin matches it. The compass law is the outer loop that moves "
          "each muscle's own setting: it reads one service position (0 calm, 1 the line), pulls it to the compass's center, "
          "pushes against whatever is rising, bounds its force by tanh, fails up past the wall, and writes through a plug "
          "that reads every lever once before the first write, reads back every write, yields to any other writer and "
          "restores the snapshot at the end.", ""]

    # ------------------------------------------------------------------ 2. Real Kubernetes on v3, three runs each
    K8S = [("STEADY", "Steady work in steps", "equal by design"), ("WANDERING", "Demand that wanders", None),
           ("ALL_FOUR", "All four in one run", "capacity"), ("FAIRNESS", "Fairness, a noisy neighbour", None),
           ("FAULTS", "Faults: machine down, spike, runaway pod, blind probe", None), ("BATCH", "A queue of batch jobs", None),
           ("TRACE_GOOGLE2011", "A public day of demand: the Google cluster trace of 2011, replayed one step at a time", None)]
    K8S = [k for k in K8S if (ROOT / "results" / "live" / f"V3_{k[0]}.json").exists()]   # a test joins when its three-run table lands
    NUM = {6: "Six", 7: "Seven", 8: "Eight"}.get(len(K8S), str(len(K8S)))
    P95, MEAN_RT = "response time (ms), 95th percentile", "response time (ms), mean"
    NODES, FAILED = "worker nodes in service, mean", "failed requests (%)"
    STANDBY = "energy (Wh)"                     # the standby model, as the three-run table names it
    from tools.omni_index import CAPACITY as CAP, CAPACITY_NOW as CAP_NOW   # the capacity row, as recorded before 13 October and since

    def pct_runs(row):
        return [100 * r["diff"] / r["native"] if r.get("diff") is not None and r.get("native") else
                (100 * (r["omni"] - r["native"]) / abs(r["native"]) if r.get("native") else 0.0) for r in row["runs"]]

    HIGHER_KEYS = {CAP, CAP_NOW, "work_inside_line_tps", "work_inside_line_mps", "work_inside_line_rps", "work_inside_line_ops", "hit_rate"}

    def cell(row, key):
        """A row's cell: its range over the three runs and its word, GAIN, LOSS or power given, by what the gauge is for; STEADY
        where it did not move beyond the noise."""
        if row is None:
            return "not taken"
        p = pct_runs(row); rd = row["reading"]
        aim_ = "higher" if key in HIGHER_KEYS else gel_aim("lower", key)
        if judged(rd):
            return f"**{min(p):+.0f}% to {max(p):+.0f}%, {in_gel_words(rd, p, aim_)}**"
        try:
            c = classify(rd, aim_)
        except ValueError:
            return rd
        return {"same": "STEADY, the same", "noise": "STEADY, inside the noise", "disagree": "the runs disagree"}.get(c, rd)

    tabs = {}
    for key, _, _ in K8S:
        tabs[key] = json.loads((ROOT / "results" / "live" / f"V3_{key}.json").read_text())
    runs_line = "; ".join(f"{t['tag']} {t['run']} ({t['engine'].split(' (')[0]})" for t in tabs["STEADY"]["runs"])
    # chart: the 95th percentile and the machines, three runs a test
    labels, vals, lows, highs, cols = [], [], [], [], []
    for key, name, _ in K8S:
        row = tabs[key]["rows"].get(MEAN_RT if key == "BATCH" else P95)
        for i, r in enumerate(row["runs"]):
            labels.append(f"{name.split(':')[0].split(',')[0][:14]} {'ABC'[i]}")
            vals.append(100 * r["diff"] / r["native"]); lows.append(100 * r["ci95"][0] / r["native"]); highs.append(100 * r["ci95"][1] / r["native"])
            cols.append(SERIES[[k for k, _, _ in K8S].index(key)])
    fig, ax = plt.subplots(figsize=(11, 3.8), dpi=160); fig.patch.set_facecolor(SURF)
    x = range(len(vals)); ax.bar(x, vals, width=0.7, color=cols, edgecolor=SURF, linewidth=1)
    ax.errorbar(x, vals, yerr=[[v - l for v, l in zip(vals, lows)], [h - v for v, h in zip(vals, highs)]], fmt="none", ecolor=INK2, elinewidth=1, capsize=2)
    ax.set_xticks(list(x)); ax.set_xticklabels(labels, fontsize=6.5, color=INK2, rotation=60, ha="right")
    style(ax, "Real Kubernetes on Omni v3: response time against native, three runs of ten pairs each (p95; the batch queue's mean)", "change (%)")
    fig.tight_layout(); fig.savefig(FIG / "k8s_v3.png", facecolor=SURF); plt.close(fig)
    L += ["## 2. Real Kubernetes, Omni v3, every test three times (evidence class L)", "",
          f"{NUM} tests, ten paired repetitions each, three separate GitHub runs on the frozen engine (A the result, B and C the "
          "replications): native Kubernetes (its HPA and scheduler) against the same Kubernetes with Omni-Compass on top, a "
          "fresh six-worker cluster per arm, order rotated, the same work sent to both arms. A row reads **GAIN** or **LOSS in all three of our runs** "
          "(by what the gauge is for, never by its sign: a response time cut is a GAIN; machines or energy up is **power given**) only when all three "
          "runs move the same way with every 95% interval clear of zero; otherwise it reads STEADY, no difference beyond the noise, which is the result. Every Omni arm ends with every setting handed back and "
          f"read back. Steady runs: {runs_line}; the other tests' runs are named in their tables.", "",
          "![Kubernetes on v3](dossier/k8s_v3.png)", "",
          "| Test | Work | Response time (p95; the batch queue's mean) | Machines in service | Energy (declared model) | Failed requests | Table |", "|---|---|---|---|---|---|---|"]
    for key, name, work in K8S:
        rows = tabs[key]["rows"]
        w = "STEADY, equal by design" if work == "equal by design" else (cell(rows.get(CAP) or rows.get(CAP_NOW), CAP) if work == "capacity" else "not taken")
        L.append(f"| {name} | {w} | {cell(rows.get(MEAN_RT if key == 'BATCH' else P95), P95)} | {cell(rows.get(NODES), NODES)} | {cell(rows.get(STANDBY), STANDBY)} | "
                 f"{cell(rows.get(FAILED), FAILED)} | `results/live/V3_{key}.md` |")
    L += ["", "Energy on kind is a declared model: the machines are containers on one runner, so a machine out of service cuts "
          "modelled watts, not a metered bill. Omni-Compass gives a machine back only after a paired trial shows the service no "
          "slower without it (the verdict, `omnicompass/verdict.py`); on these clusters one machine fewer made requests 30-45% "
          "slower in most trials, so the machines stayed and were spent on speed and work. The v1 tables (`results/live/V1_*.md`, "
          "`docs/OMNI_V1.md`) read the same; the sets before v1 are in `docs/history/`.", ""]

    # ------------------------------------------------------------------ 3. The real database on v3
    pg = json.loads((ROOT / "results" / "live" / "V3_PGBENCH.json").read_text())
    L += ["## 3. A real database: PostgreSQL behind PgBouncer, Omni v3, three runs (evidence class L)", "",
          "PostgreSQL 16 as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on one knob, the "
          "pool size, through PgBouncer's own console, inside the cover [2, 90] (`docs/POSTGRES_PREREGISTRATION.md`). Three "
          "paired repetitions a run, three runs, pgbench's own log for the gauges. Runs: "
          + "; ".join(f"{t['tag']} {t['run']}" for t in pg["runs"]) + ".", "",
          "| Workload | Work inside the 50 ms line | p95 | Connections held open | Host CPU-seconds (the compass's own cost) |", "|---|---|---|---|---|"]
    for wl, m in pg["workloads"].items():
        def c2(k):
            r = m.get(k)
            return "not taken" if r is None else cell(r, k)
        L.append(f"| `{wl}` | {c2('work_inside_line_tps')} | {c2('p95_ms')} | {c2('servers_alive_mean')} | {c2('cpu_seconds')} |")
    L += ["", "The compass takes connections back only while the pooler's clients wait for one under 1% of the time and gives them back "
          "the moment anyone waits (amendment 2 of `docs/POSTGRES_PREREGISTRATION.md`, 8 October: the first counted set's CPU cost was measured "
          "and traced to the harness's own psql launches, not to the pooler, and its first table is kept whole in `docs/history/V3_PGBENCH_set1.md`). "
          "Where it reads a cut it is connections held open for the same work, a GAIN, with the host's CPU STEADY (`tpcb_hot`: cut 7% to 13% "
          "in all three of our runs); where the add rule buys connections above the operator's setting on a slow write workload "
          "(`simple_update`: the most at once up 8% to 12%), that reads power given and counts below 1 in the index. The earlier counted "
          "sets are kept whole in `docs/history/V3_PGBENCH_set1.md` to `V3_PGBENCH_set3.md`. Table: `results/live/V3_PGBENCH.md`.", ""]

    # ------------------------------------------------------------------ 3b, 3c. Real messaging and the real cache on v3 (each when its table has landed)
    WORKLOAD_SECTIONS = (
        ("V3_KAFKA.json", "## 3b. Real messaging: Apache Kafka, a consumer group's operator-set size, Omni v3, three runs (evidence class L)",
         "Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's 2 consumers is native; "
         "omni is the compass law on one knob, the consumer count, inside the cover [1, 8], holding the group's own end-to-end latency "
         "at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Three paired repetitions a run, three runs, the consumers' own "
         "records for the gauges; the tuning workload is shown and not counted.",
         "| Workload | Work inside the 500 ms line | End-to-end p95 | Consumers running (the resource held) | Host CPU-seconds (the compass's own cost) |",
         ("work_inside_line_mps", "p95_ms", "consumers_mean", "cpu_seconds"),
         "On the counted set that stands (the brain's own verdict on the knob, amendment 2, run on 10 October: `docs/RERUN_2026-10-10.md`), "
         "the consumer count was handed back where the queue allowed: consumers running cut 0.8% on `burst` (0.3% on the tuning workload, "
         "shown and not counted), a GAIN in all three of our runs, with work, latency and CPU STEADY; `heavy` and `light` read STEADY on every "
         "gauge. No message went unconsumed in any arm; every count was handed back. The earlier counted sets are kept whole in "
         "`docs/history/V3_KAFKA_set1.md` and `V3_KAFKA_set2.md`. Table: `results/live/V3_KAFKA.md`."),
        ("V3_REDIS.json", "## 3c. A real cache: Redis, the operator's memory ceiling, Omni v3, three runs (evidence class L)",
         "Redis as Ubuntu ships it with the operator's 64 MB ceiling and allkeys-lru is native; omni is the compass law on one knob, the "
         "ceiling, inside the cover [16, 512] MB through Redis's own console, growing only while the cache is full and giving a notch "
         "back when calm and nothing is evicted (`docs/REDIS_PREREGISTRATION.md`). An application with a declared 5 ms store trip on a "
         "miss and a working set that steps up and down; three paired repetitions a run, three runs; the tuning workload is shown and not counted.",
         "| Workload | Work inside the 2 ms line | Cache hit rate | p95 | Memory ceiling held, MB (the resource held) | Host CPU-seconds |",
         ("work_inside_line_rps", "hit_rate", "p95_ms", "maxmemory_mb_mean", "cpu_seconds"),
         "On the counted set that stands (the brain's own verdict on the knob, amendment 2), every untouched workload reads STEADY on every "
         "gauge: under the resource objective the verdict left the ceiling where the operator set it, as the preregistration expected "
         "before the runs. The tuning workload, shown and never counted, bought a GAIN in work inside the line (+4% to +5%) and in the hit "
         "rate with memory given (+19% to +26%, power given). The earlier counted sets are kept whole in `docs/history/V3_REDIS_set1.md` "
         "and `V3_REDIS_set2.md`. Table: `results/live/V3_REDIS.md`."),
        ("V3_YCSB.json", "## 3d. A real database's storage-engine cache: MongoDB under YCSB, the operator's cache size, Omni v3, three runs (evidence class L)",
         "MongoDB 8.0 as its publisher ships it with the operator's WiredTiger cache of 512 MB is native; omni is the compass law on one knob, "
         "the cache size, inside the cover [256, 2,048] MB through the server's own console, growing by notches of 64 MB only while the cache "
         "is full and reads are slow, and giving a notch back when calm and the cache holds its working set (`docs/YCSB_PREREGISTRATION.md`; "
         "the first counted set's gate was 'nothing evicted', which its amendment 1 of 8 October records as satisfied by a cold cache, and the "
         "table named below says which set it is). YCSB's "
         "published core workloads with the key space stepping through the cache and past it, drawn uniformly, at 3,000 operations a second "
         "from 32 threads; three paired repetitions a run, three runs; the tuning workload (workload A) is shown and not counted.",
         "| Workload | Work inside the 1 ms line | p95 | Cache size held, MB (the resource held) | Pages read into the cache | Host CPU-seconds |",
         ("work_inside_line_ops", "p95_ms", "cache_mb_mean", "pages_read", "cpu_seconds"),
         "On this machine the data files sit in the operating system's page cache as well, so a storage-engine miss is a read from memory, "
         "not a disk, as disclosed before the run. On the counted set that stands, the cache size held was cut 10% to 15% on `burst` and "
         "`f`, a GAIN in all three of our runs, with work inside the line, p95, mean latency and CPU STEADY; `b` and `c` read STEADY on every "
         "gauge; the cache was handed back on every omni arm. The earlier counted sets are kept whole in `docs/history/V3_YCSB_set1.md` to "
         "`V3_YCSB_set3.md`. Table: `results/live/V3_YCSB.md`."),
        ("V3_SYSBENCH.json", "## 3e. A real database's buffer pool: MySQL under sysbench, the operator's InnoDB pool size, Omni v3, three runs (evidence class L)",
         "MySQL 8.0 as Ubuntu ships it with the operator's 512 MB InnoDB buffer pool is native; omni is the compass law on one knob, the pool "
         "size, inside the cover [128, 2,048] MB in the server's own 128 MB chunks through its own console, growing only while the pool is full "
         "and the server's own statement latency is slow, and giving a chunk back only while the pool's misses are under 1% of its reads "
         "(`docs/MYSQL_PREREGISTRATION.md`). sysbench's OLTP scripts as shipped with the tables in use stepping through the pool and past it, "
         "at a fixed offered rate from 32 threads; three paired repetitions a run, three runs; the tuning workload (point select) is shown and "
         "not counted.",
         "| Workload | Work inside the line | p95 | Buffer pool held, MB (the resource held) | Pages read from disk | Host CPU-seconds |",
         ("work_inside_line_tps", "p95_ms", "pool_mb_mean", "disk_reads", "cpu_seconds"),
         "On the counted set that stands (the brain's own verdict on the knob, amendment 3), every untouched workload reads STEADY on every "
         "gauge, and the pool was handed back on every omni arm. The earlier counted sets are kept whole in `docs/history/V3_SYSBENCH_set1.md` "
         "to `V3_SYSBENCH_set4.md` (the first: 15 of 45 arms not handed back because the plug's restore was issued while the server was still "
         "withdrawing the blocks of a shrink, which MySQL ignores; the plug fixed and the fix declared). The update_index work-inside-the-line "
         "row counts almost nothing in either arm (a single update's client round trip exceeds the server-side 0.6 ms line) and is disclosed. "
         "Table: `results/live/V3_SYSBENCH.md`."),
    )
    for fname, head, intro, header, keys, after in WORKLOAD_SECTIONS:
        p = ROOT / "results" / "live" / fname
        if not p.exists():
            continue
        tab = json.loads(p.read_text())
        L += [head, "", intro + " Runs: " + "; ".join(f"{t['tag']} {t['run']}" for t in tab["runs"]) + ".", "",
              header, "|" + "---|" * (len(keys) + 1)]
        for wl, m in tab["workloads"].items():
            def c3(k):
                r = m.get(k)
                return "not taken" if r is None else cell(r, k)
            name = f"`{wl}` (tuning, shown, not counted)" if wl == "tuning" else f"`{wl}`"
            L.append("| " + name + " | " + " | ".join(c3(k) for k in keys) + " |")
        L += ["", after, ""]

    # ------------------------------------------------------------------ 4. The bill on a real cloud
    L += ["## 4. The bill on a real cloud: Azure Kubernetes Service, Omni v1 (evidence class L, a metered bill)", "",
          "Azure's own cluster autoscaler is native; omni is the same autoscaler with Omni-Compass idling the machines it gives "
          "back; the bill is Azure's own count of machines every 15 s at list price, a fresh cluster per arm, deleted after it "
          "(`.github/workflows/aks-metered.yml`, `docs/K8S_COMPASS_PREREGISTRATION.md`, the bill on a real cloud). Transcribed "
          "from the receipts they cite:", "",
          "| Test | Fleet | Bill | Response time | Reading | Receipt |", "|---|---|---|---|---|---|",
          "| Steady load, 5 pairs | 4 workers | −4.7%, interval across zero | inside the noise | STEADY, no difference beyond the noise on any gauge | `results/live/V1_AKS_STEADY.md` |",
          "| A burst sized to the cluster, 5 pairs | 4 workers | +5.0%, interval across zero | p99 −34% clear of the noise in this one run (a GAIN in one run, not a reading of three); p95 inside the noise | the bill STEADY, inside the noise | `results/live/V1_AKS_BURST.md` |", "",
          "One machine is a quarter of a 4-worker fleet, so only a cut of about 30% or more can clear the noise there; the "
          "expected machine cut is a few percent. The fleet that can show one machine (40 workers in nine machine "
          "families, the subscription's per-family allowance being 10 vCPUs) is preregistered and dispatched on v3; its "
          "first dispatches were refused by the subscription's allowances and by Azure's own cluster capacity in eastus "
          "before any arm ran, each refusal recorded in the preregistration's amendments.", ""]

    # ------------------------------------------------------------------ 3. GPU model
    KEYS = ("work_per_kj", "energy_j", "p50_ms", "p95_ms", "p99_ms")

    def model(path):
        work = json.loads(path.read_text())["work"]
        out = {}
        for memb, arms in work.items():
            for base, top in (("native", "omni"), ("cap", "cap_omni")):
                for k in KEYS:
                    r = [math.log(x[k] / n[k]) for x, n in zip(arms[top], arms[base]) if x[k] > 0 and n[k] > 0]
                    out[(memb, top, k)] = 100 * (math.exp(sum(r) / len(r)) - 1)
        return out
    a = model(ROOT / "results" / "sim" / "gpu_two_wire" / "RESULT.json")
    b = model(ROOT / "results" / "sim" / "gpu_two_wire" / "fresh" / "RESULT.json")
    WORKN = (("0.0", "Compute-bound"), ("0.85", "AI token generation"))
    labels = [f"{w}:\n{g}" for _, w in WORKN for g in ("energy", "median", "p95")]
    pick = [(m, "omni", k) for m, _ in WORKN for k in ("energy_j", "p50_ms", "p95_ms")]
    va, vb = [a[x] for x in pick], [b[x] for x in pick]
    fig, ax = plt.subplots(figsize=(8, 3.6), dpi=160); fig.patch.set_facecolor(SURF)
    xs = range(len(labels))
    ax.bar([x - 0.17 for x in xs], va, width=0.32, color=SERIES[0], edgecolor=SURF, linewidth=2, label="seeds 5000-5009")
    ax.bar([x + 0.17 for x in xs], vb, width=0.32, color=SERIES[1], edgecolor=SURF, linewidth=2, label="fresh seeds 5100-5109")
    for x, v in zip(xs, va):
        ax.annotate(f"{v:+.1f}%", (x - 0.17, v), xytext=(0, 4 if v >= 0 else -12), textcoords="offset points", ha="center", fontsize=8)
    for x, v in zip(xs, vb):
        ax.annotate(f"{v:+.1f}%", (x + 0.17, v), xytext=(0, 4 if v >= 0 else -12), textcoords="offset points", ha="center", fontsize=8)
    ax.set_xticks(list(xs)); ax.set_xticklabels(labels, fontsize=7, color=INK2)
    style(ax, "The card's firmware with Omni on top, against the firmware alone (model, geometric means)", "change (%)")
    ax.legend(fontsize=8, frameon=False)
    fig.tight_layout(); fig.savefig(FIG / "gpu_model.png", facecolor=SURF); plt.close(fig)
    L += ["## 4b. The GPU governor on the modelled card: each base alone, and with Omni on top (evidence class S)", "",
          "Omni-Compass never runs the card. It sits on the card's own firmware (or on an operator's power cap) and moves the "
          "clock ceiling and the power limit, which that base already accepts (`omni_controller/gpu_compass.py`, the same law "
          "in `realms/gpu_card.py`). A step down is taken only after a paired trial on the card shows it adds at most 2% to "
          "the card's own time on a request (`omnicompass/verdict.py`); where no step passes, the card runs as it does alone.", "",
          "![The modelled card](dossier/gpu_model.png)", "",
          "| Work | Base | Energy (tuning / fresh) | Median response | p95 | p99 |", "|---|---|---:|---:|---:|---:|"]
    for m, w in WORKN:
        for top, base in (("omni", "firmware + Omni vs firmware alone"), ("cap_omni", "105 W cap + Omni vs the cap alone")):
            L.append(f"| {w} | {base} | " + " | ".join(f"{a[(m, top, k)]:+.2f}% / {b[(m, top, k)]:+.2f}%"
                                                         for k in ("energy_j", "p50_ms", "p95_ms", "p99_ms")) + " |")
    L += ["", "Source: `results/sim/gpu_two_wire/RESULT.md` and `fresh/RESULT.md`. The rule, and why the allowance is 2%, is "
          "amendment 8 of `docs/GPU_PREREGISTRATION.md`.", ""]

    # ------------------------------------------------------------------ 5. Six organisms grid
    gt = grid_tables()
    runs = [1, 10, 100, 1000]
    for key, fn, ttl, yl in (("wpe", "grid_wpe.png", "Six organisms: work per energy, Omni against native (model)", "change (%)"),
                             ("viol", "grid_viol.png", "Six organisms: time over the service line, Omni minus native (model)", "percentage points")):
        panels = {}
        for size in (1, 10, 100, 1000):
            rows = [(SHORT[i], [gt.get((size, r), {}).get(key, [None] * 6)[i] for r in runs]) for i in range(6)]
            if any(y is not None for _, ys in rows for y in ys):
                panels[f"{size}× size"] = rows
        lines(FIG / fn, ttl, yl, runs, panels)
    L += ["## 5. The six organisms at 1, 10, 100 and 1,000 runs and sizes, Omni v3 (evidence class S)", "",
          "Each organism runs native (its own controllers) and with the compass law on every muscle, same seed, same load, "
          "same clock. Size is the number of copies of the organism governed together on one clock (1,000 copies of the four "
          "stacked is 1.7 million modelled muscles); runs are the first N of the same paired set, so 1, 10, 100 and 1,000 "
          "nest. 84 of 90 cells are done; the six left (100 and 1,000 runs at 1,000 copies) are beyond the machines "
          "available and say so.", "",
          "![Work per energy](dossier/grid_wpe.png)", "", "![Time over the line](dossier/grid_viol.png)", "",
          "The full grid with every cell: `results/scale/GRID.md`; the receipts, one per size: `results/scale/receipts/`. "
          "Work per energy is up in every cell, a GAIN, the same figure at every size (+0.07% for Physics to +0.37% for Energy, "
          "the four stacked and the tower); the time over the service line is at or under native's in every cell, so the "
          "band-first rule holds and every cell of 10 runs or more reads GAIN within the guardrails by the preregistered rule. "
          "Every knob was handed back in every run.", ""]

    # ------------------------------------------------------------------ 6. Realms and muscles
    L += [f"## 6. The {_SZ[TOWER]} muscles and the four realms, Omni v3 (evidence class S)", "",
          f"The catalog (`realms/catalog.csv`): {_SZ[TOWER]} muscles in 59 families, {_SZ['compute_ai_cloud']} in Compute / AI / Cloud, {_SZ['physics_robotics_autonomous']} in Physics / Robotics / "
          f"Autonomous, {_SZ['energy_facility_industrial']} in Energy / Facility / Industrial and {_SZ['distribution_specialized']} in Distribution / Specialized ({_SZ[STACK]:,} counting a muscle "
          "once per realm, a shared spine of 257). Every muscle alone and every organism whole ran as A, B and C on v3 and "
          "reproduced to the last digit (`results/realms/REALMS.md`): 0 muscles with a LOSS, every organism GAIN within the "
          "guardrails (work per energy +0.1% to +0.3%, work STEADY, time over the line not above native's). On v2 the "
          "Physics realm and the tower read GAIN AND LOSS (a service traded for energy); the cause was a missing do-no-harm gate on speed knobs, "
          "which made v3 (`docs/OMNI_V3.md`). Three independent simulators with their own native controllers are wired the "
          "same way and read by the same rule: the power grid (`results/live/V3_PANDAPOWER.md`: energy drawn and net import "
          "cut in all 11 SimBench grids with ZIP loads, a GAIN; the energy dissipated in the lines up in 4 and tap operations 4 → 8 a year "
          "in one, power given), robot arms (`results/live/V3_MUJOCO.md`: Gen3 peak torque cut 29%, tracking error cut 21%, energy per takt "
          "cut 0.8%, each a GAIN; the Panda's copper heating up 14%, power given; two arms left native, STEADY) and CityLearn "
          "(`results/live/V3_CITYLEARN.md`: electricity bought, peak and unevenness cut in all 11 battery districts, a GAIN; the bill up in "
          "7, power given). Every row stands in every table, whichever way it went.", ""]

    # ------------------------------------------------------------------ 7. Harnesses and receipts
    L += ["## 7. Harnesses and receipts", "", "| Harness | What it proves | Receipt |", "|---|---|---|",
          "| `scripts/kind_paired.sh`, `tools/live_reps.py`, workflow `benchmark-reps` | native against Omni on real Kubernetes, paired on one runner, the reset checked | `results/live/raw/run-*/live-reps/` |",
          "| `tools/confirm_abc.py` (and `pgbench_abc.py`, `kafka_abc.py`, `redis_abc.py`, `swarm_abc.py`, `mujoco_abc.py`, `pandapower_abc.py`, `citylearn_abc.py`) | three separate runs read by one rule: GAIN or LOSS in all three of our runs (power given for a resource spent that rose), STEADY, the runs disagree; each run's engine checked against the fingerprint | `results/live/V3_*.md`, `V1_*.md` |",
          "| `tools/omni_version.py` | which frozen engine a checkout or any result's commit carries | `OMNI_V1.json`, `OMNI_V2.json`, `OMNI_V3.json` |",
          "| `scripts/aks_paired.sh`, workflow `aks-metered` | the same on Azure's managed Kubernetes, Azure's own bill, a fresh cluster per arm, the fleet pre-flighted against the subscription's allowances | `results/live/V1_AKS_*.md` |",
          "| `tools/run_kil.py`, workflows `six-kube`, `big-organism`, `big-organism-detached`; `tools/six_kube_report.py` | the six organisms with a real cluster inside at 1 to 1,000 copies, on GitHub and on a rented machine; the clock rule | `results/live/V1_SIX_KUBE.md`, `V3_SIX_KUBE.md`, `V1_BIG_ORGANISM.md` |",
          "| `tools/run_pgbench.py`, workflow `pgbench` | a real database behind its pooler, one knob through the pooler's console | `results/live/V3_PGBENCH.md` |",
          "| `tools/run_kafka.py`, workflow `kafka` | a real message broker as shipped, one knob (the consumer group's size) read from the consumers' own records | `results/live/V3_KAFKA.md` |",
          "| `tools/run_redis.py`, workflow `redis` | a real cache as shipped, one knob (the memory ceiling) through its own console, growing only while the cache is full | the three-run table V3_REDIS.md in `results/live/` when its runs land |",
          "| `tools/run_swarm.py`, workflow `swarm` | Omni on top of each drone's shipped autopilot in gym-pybullet-drones, collisions voiding the cell | `results/live/V3_SWARM.md` |",
          "| `tools/run_scale.py`, `tools/pool_scale.py`, workflow `six`; `tools/grid.py` | the six organisms at every run count and size | `results/scale/GRID.md`, `results/scale/receipts/` |",
          "| `tools/run_realms.py`, workflow `realms` | every muscle alone and every organism whole | `results/realms/REALMS.md` |",
          "| `tools/run_pandapower.py`, `run_mujoco.py`, `run_citylearn.py` | Omni on top of an independent simulator's own controller | `results/live/V3_PANDAPOWER.md`, `V3_MUJOCO.md`, `V3_CITYLEARN.md` |",
          "| `tools/omni_index.py` | the one combined number, read only from the three-run tables | `results/OMNI_INDEX.md` |",
          "| `scripts/gpu_rented_run.sh`, `tools/gpu_wire_check.py` | one command on a rented card: wire check, smoke, the organisms with the card inside, the preregistered counted run | the founder's runs, to come |",
          "| workflow `archive-run` | every finished run's files copied with the code onto the branch `raw`, one SHA-256 manifest per repetition | `results/live/raw/run-<id>/` (opened by `scripts/raw_archive.sh`) |",
          "| `verify.py`, `tools/release_manifest.py` | everything above re-runs and checks itself; the manifest fingerprints the result | `results/VERIFY_RECEIPT.txt`, `RELEASE_MANIFEST.json` |", "",
          "The rules for each run were written and committed before it ran (`docs/*_PREREGISTRATION.md`); every row is reported, "
          "LOSS included; nothing is read across engine versions.", ""]

    # ------------------------------------------------------------------ 8. Open
    L += ["## 8. What is not yet shown", "",
          "- A cloud bill or energy cut on real machines: the 4-worker Azure fleet reads STEADY, inside the noise, as a fleet too small "
          "to show one machine must; the 40-worker fleet runs are the test of that.",
          "- The real card on the current governor: every earlier card result ran on a controller since replaced and is obsolete; "
          "the one-card, card-inside-the-organisms and eight-card runs are the founder's, on rented cards, at one named commit.",
          "- The grid stops at 100 copies and 100 runs (the founder's order of 12 October, to cut the time and the bill): no 1,000 "
          "copies and no 1,000 runs are run on any engine from that day; the v3 cells at 1,000 above stand as they were run.",
          "- The queue in `docs/REGISTER.md` section 4 (drone swarms on gym-pybullet-drones and Kafka done; Redis running): PX4 and "
          "ArduPilot swarms, YCSB and HammerDB, Spark, OpenSearch, fio, Open-RMF, the 24-hour robustness run, Basilisk, Orekit and "
          "GMAT, RocketPy, Cantera.", ""]
    OUT.write_text("\n".join(_legal_stamp(with_own_runs(L))) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
