#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The LOSS ledger: every row that reads LOSS across its three runs (in all three, or by their mean), in every benchmark's newest three-run table, on one page.

Built from the verdict audit's one selection (tools/verdict_audit.py: each benchmark's newest whole three-run table from omni-v8
on, tools/readings.py `landed`; the third arm, taken out on 25 October, never counted), never typed in; the live benchmark engine's
appraisal counts the same rows. Every row is placed by what its two arms are:

  against my own native     Omni-Compass on top of a native controller against that native alone (every plain table, and the
                            four ways' TOP and BARE): the readings "do no harm" is judged by (DISCLOSURES.md, section 3)
  in place of a controller  Omni-Compass on the organism alone against an orchestrator as shipped (the four ways' VS): shown,
                            a different question from do no harm
  without me, or compounded the orchestrator against the organism alone (ORCH: neither arm carries Omni-Compass) and
                            Omni-Compass on top of the orchestrator against the organism alone (BOTH: two changes at once)

A row against my own native carries its cause where one is written (CAUSES below names the page), the version that fixed
it where one did, and what decides it. A row with no cause written says so.

  python3 tools/loss_ledger.py            write docs/LOSS_LEDGER.md
  python3 tools/loss_ledger.py --check    exit 1 when docs/LOSS_LEDGER.md differs from what the tables give
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                       # noqa: E402
from tools.readings import classify, judged, landed, with_own_runs  # noqa: E402

OUT = ROOT / "docs" / "LOSS_LEDGER.md"
TABLE_DIRS = (ROOT / "results" / "live", ROOT / "results" / "orchestrator")

ARMS = {"BARE": "against my own native", "TOP": "against my own native", "VS": "in place of a controller",
        "ORCH": "without me, or compounded", "BOTH": "without me, or compounded"}
SECTIONS = ("against my own native", "in place of a controller", "without me, or compounded")

# (benchmark, gauge prefix) -> (cause, the page that states it, fixed in, what decides it). A prefix matches every gauge it
# begins; the benchmark is the table's name without its engine (V12_KUBERAY_4W_BARE -> KUBERAY_4W_BARE).
V13_FIX = ("on a shared host at its top, beside another workload's room, a CPU limit I raised was kept through a saturated batch "
           "queue, so the batch pods ran slower while the web served no faster", "docs/OMNI_V13.md", "omni-v13",
           "the benchmark's three runs on the engine that stands")
STORE_PAGE = "docs/STORE_ROOT_CAUSES_2026-10-30.md"
STORE_GATE = ("the verdict's gate: the allowance clamped every move, the wall's fail-up included, and the wall abandoned every "
              "spend trial, so in the seconds the service stood over its line the brain asked to go up and was kept from it")
STORE_NEXT = "the next version (its candidate on the branch v22-stores, the model gate first)"
STORE_DECIDES = "the benchmark's three runs at one setting on the next engine"
NO_WRITE = ("Omni-Compass wrote nothing in any repetition, so the two arms are one system and the difference is the rig's own "
            "noise between two native arms")
NO_WRITE_DECIDES = "no engine moves it: more repetitions a run, to shrink the rig's noise"
CAUSES_PAGE = "docs/LOSS_CAUSES_2026-10-31.md"
POD_SHIFT = ("the shared test machine: Omni-Compass's arm starts its pods while the one runner every kind node shares is busier, "
             "and starts more of them where its target moves, each start a wait native never paid because it never started the pod; "
             "a pod created on a host 70% to 100% busy waits longer at the kubelet than one created at 0% to 50%, a stratum a real "
             "cluster's own node never enters")
POD_DECIDES = "the benchmark's three runs on the engine that stands, the host's busy share read beside the row"
NEIGHBOUR_NEXT = ("no engine change: the price is flat in the lift (a limit at 2,000m costs the neighbour the same 6 ms of mean "
                  "response as one at 3,800m, so a cap buys nothing; read in the gate's two-app model, STEADY on every gauge) and "
                  "smaller than the governed app's gains in the same table, so on the organism conveyance beside a neighbour comes "
                  "out ahead")
CAUSES = {
    ("KUBERAY_4W_BARE", ""): V13_FIX,
    ("ARMADA_4W_BARE", ""): ("suspected: the conveyance fault fixed in omni-v13 (its shape fits: a batch gauge a few percent "
                             "slower on a shared host); not yet shown on this rig", "docs/LOSS_ROWS_UNDER_INVESTIGATION.md",
                             "omni-v13, if the suspicion holds", "the benchmark's three runs on the engine that stands"),
    ("BINPACK", "queue:"): ("suspected: the conveyance fault fixed in omni-v13; the omni-v13 model gate's batch model, set from the "
                            "KubeRay runs' own files, read the job turnaround back at native's", "docs/OMNI_V13.md",
                            "omni-v13, if the suspicion holds", "the benchmark's three runs on the engine that stands"),
    ("VANILLA", "queue:"): ("suspected: the conveyance fault fixed in omni-v13; the omni-v13 model gate's batch model read the job "
                            "turnaround back at native's", "docs/OMNI_V13.md", "omni-v13, if the suspicion holds",
                            "the benchmark's three runs on the engine that stands"),
    ("OCM_4W_TOP", "alert minutes"): ("under investigation: the third run's size is far from the first two",
                                      "docs/LOSS_ROWS_UNDER_INVESTIGATION.md", "", "the benchmark's three runs on the engine "
                                      "that stands, read repetition by repetition"),
    # the data stores on omni-v21, from their own files (docs/STORE_ROOT_CAUSES_2026-10-30.md, tools/store_causes.py)
    ("KAFKA", ""): (STORE_GATE + "; and the hand-back gave back a consumer the load still needed, each give-back and re-add a "
                    "rebalance of the whole group (a median 2.58 s and 1.24 s of every message waiting); run C ran at 20 s a notch, "
                    "A and B at 30 s, so the table is two settings", STORE_PAGE, STORE_NEXT, STORE_DECIDES),
    ("KAFKA_SERVICE", ""): (STORE_GATE + "; and the hand-back gave back a consumer the load still needed, each give-back and "
                            "re-add a rebalance of the whole group (a median 2.58 s and 1.24 s of every message waiting)",
                            STORE_PAGE, STORE_NEXT, STORE_DECIDES),
    ("REDIS", ""): (STORE_GATE + " (the cache held at 64 to 80 MB while the working set needs more; in our own model a ceiling the "
                    "working set fits under reads work inside the line GAIN, up 7.7% to 22.9%, and the 99th percentile GAIN or STEADY)",
                    STORE_PAGE, STORE_NEXT, STORE_DECIDES),
    ("REDIS_SERVICE", ""): (STORE_GATE + " (the cache held at 64 to 80 MB while the working set needs more)", STORE_PAGE, STORE_NEXT,
                            STORE_DECIDES),
    ("SYSBENCH_SHIPPED", "workload update_index"): (NO_WRITE + " (the pool at the shipped 128 MB in both arms)", STORE_PAGE, "",
                                                    NO_WRITE_DECIDES),
    ("SYSBENCH_SHIPPED", "workload "): ("one repetition of run B carries the mean of three (the burst's 95th percentile: run B up "
                                        "255.1%, its interval from 554% down to 1,065% up; runs A and C within 0.6%); on this rig a "
                                        "pool miss costs the statement nothing (the data files in the machine's page cache: 9% to 12% "
                                        "of page reads missing with the latency unmoved), so no move of the pool explains it",
                                        STORE_PAGE, "", "the benchmark's three runs, read repetition by repetition"),
    ("YCSB_SHIPPED", ""): (NO_WRITE + ": MongoDB's shipped cache (7,482 MB) is above the knob's cover, at its limit on native "
                           "(docs/YCSB_PREREGISTRATION.md, amendment 4)", STORE_PAGE, "", NO_WRITE_DECIDES),
    ("YCSB", ""): ("latencies of 0.3 to 0.6 ms that moved 0.2% to 5.4%, beyond the noise in no run: on this rig a cache miss costs "
                   "the read nothing (12% to 16% of pages missing with the read latency unmoved at 0.07 to 0.08 ms), so the cache's "
                   "few moves (2 to 12 an arm) bought and cost nothing; the rig's noise", STORE_PAGE, "", "the benchmark's three "
                   "runs at one setting on the next engine"),
    ("YCSB_SERVICE", ""): ("latencies of 0.3 to 0.6 ms that moved 0.2% to 1.7%, beyond the noise in no run: a cache miss costs the "
                           "read nothing on this rig, so the cache's few moves bought and cost nothing; the rig's noise", STORE_PAGE,
                           "", "the benchmark's three runs on the next engine"),
    # the 17 rows read from their own files on 31 October (docs/LOSS_CAUSES_2026-10-31.md): the pod start wait with
    # tools/pod_phases.py, the rest from the governor's audit
    ("ALL_FOUR", "pod start wait"): (POD_SHIFT + " (in the same stratum of host busy share its pods start 0.02 s faster; the "
                                     "whole rise is the shift to a busier host)", CAUSES_PAGE, "", POD_DECIDES),
    ("GOLDILOCKS", "pod start wait"): (POD_SHIFT + " (167 starts against native's 100, 125 of them while the host stood over 50% "
                                       "busy; in the same stratum 0.03 s slower, the shift 0.27 s of the 0.31 s)", CAUSES_PAGE, "",
                                       POD_DECIDES),
    ("KEDA_CPU_REQUESTS", "pod start wait"): (POD_SHIFT + " (in the same stratum 0.01 s faster; the rise is the count of starts "
                                              "and the shift)", CAUSES_PAGE, "", POD_DECIDES),
    ("ROBUST_KILL", "pod start wait"): (POD_SHIFT + " (194 starts against native's 163; the shift 0.16 s of the 0.25 s, the same "
                                        "stratum 0.09 s)", CAUSES_PAGE, "", POD_DECIDES),
    ("ROBUST_LONG", "pod start wait"): (POD_SHIFT + " (in the same stratum 0.07 s faster; the shift 0.38 s against a rise of 0.31 s)",
                                        CAUSES_PAGE, "", POD_DECIDES),
    ("TRACE_GOOGLE2011", "pod start wait"): (POD_SHIFT + " (in the same stratum 0.11 s faster; the shift 0.23 s against a rise of "
                                             "0.13 s)", CAUSES_PAGE, "", POD_DECIDES),
    ("BATCH", "pod start wait"): ("22 pods started inside the windows where native started none (the web service's target moved "
                                  "beside the queue): 17 on serving nodes at 1.29 s each and 5 on an empty node at 8.40 s each while "
                                  "the host stood 70% to 100% busy; native's zero is no start at all", CAUSES_PAGE, "", POD_DECIDES),
    ("BATCH", "failed requests"): ("one request of 965 in one repetition of ten timed out at 10 s, 20 s into the window, under the "
                                   "queue's load, before any replica, limit or machine had moved; no other request failed in the 30 "
                                   "arms", CAUSES_PAGE, "", "the benchmark's three runs on the engine that stands"),
    ("FAIRNESS", "pod start wait"): (POD_SHIFT + " (the shift 0.19 s of the 0.39 s; the other 0.19 s in the same stratum is the "
                                     "neighbour's pods, created on a worker whose idle CPU was conveyed to the governed app)",
                                     CAUSES_PAGE, NEIGHBOUR_NEXT, POD_DECIDES),
    ("FAIRNESS", "second app"): ("the neighbour's failures are its own surge's, in both arms: six load replicas saturate it and the "
                                 "shared host for 150 s at a time and its probe requests time out at 10 s (55% to 72% failed at 70% to "
                                 "100% host busy), with every conveyed limit already handed back and the same pods in both arms (19.2 on "
                                 "the two autoscalers); the row's half a request a repetition sits in that saturated band (59.2% against "
                                 "55.5% of the surge requests failed), the shared machine's noise at saturation. Conveyance's own price on "
                                 "the neighbour is in the quiet band: its mean response 3.7% longer (167.8 against 161.8 ms over 8,949 "
                                 "requests), its 95th percentile 2.0% shorter, failures 0.30% against 0.24%: the kernel's run queue under "
                                 "a serving pod's lifted quota", CAUSES_PAGE, NEIGHBOUR_NEXT,
                                 "the benchmark's three runs on the engine that stands, the neighbour's line read beside the governed app's"),
    ("CRUISEKUBE", ""): ("Omni-Compass wrote nothing in any of the 30 repetitions (the CPU limit is CruiseKube's alone, the machines "
                         "are kind's, fixed, and the service stayed inside its line, so the replica range had nothing to carry): the "
                         "two arms are one system and the rows are the rig's noise between two native arms", CAUSES_PAGE, "",
                         "no engine moves it: more repetitions a run, or a load that takes the service to its line"),
    ("CAPACITY", "3000:work"): ("at the 3-core cap the service is inside its line in both arms and the only moves are conveyances of "
                                "idle CPU to the serving pods; the completed count fell 0.6% by the mean with every run's interval "
                                "across zero (run A's own table reads the row STEADY): the rig's noise at the cap", CAUSES_PAGE, "",
                                "the benchmark's three runs on the engine that stands, and more pairs a cap"),
}


def newest_tables():
    """Each benchmark's newest whole table: (engine number, benchmark name, path)."""
    out = []
    for d in TABLE_DIRS:
        groups = defaultdict(list)
        for p in d.glob("V*_*.json"):
            m = re.fullmatch(r"V(\d+)_(.+)\.json", p.name)
            if m:
                groups[m.group(2)].append((int(m.group(1)), p))
        for name, found in groups.items():
            for n, p in sorted(found, reverse=True):
                if landed(p):
                    out.append((n, name, p))
                    break
    return sorted(out, key=lambda t: (t[1], t[0]))


def loss_rows(data):
    """(gauge, row) for every row that reads LOSS across its three runs, wherever the table keeps it (rows, or workloads' gauges)."""
    found = []

    def walk(o, path):
        if isinstance(o, dict):
            r = o.get("reading")
            if isinstance(r, str):
                try:
                    c = classify(r)
                except ValueError:
                    c = None
                if c == "loss" and judged(r):
                    found.append((" / ".join(path), o))
            for k, v in o.items():
                if k not in ("runs", "reading"):
                    walk(v, path + [str(k)])
    walk(data.get("rows") or {}, [])
    for wl, gauges in sorted((data.get("workloads") or {}).items()):
        if wl != "tuning":
            walk(gauges, [f"workload {wl}"])
    return found


def section(name):
    m = re.search(r"_4W_([A-Z]+)$", name)
    return ARMS.get(m.group(1), SECTIONS[0]) if m else SECTIONS[0]


def cause(name, gauge):
    for (bench, prefix), c in CAUSES.items():
        if bench == name and gauge.startswith(prefix):
            return c
    return None


def sizes(row):
    """Each run's change against the first arm, in percent of it, in the run's order; from one value to the other where the
    first arm stood at or near zero, so no percent is printed that a near-zero base inflates past meaning."""
    out = []
    for r in row.get("runs") or []:
        base, other = r.get("native"), r.get("omni")
        if not (isinstance(base, (int, float)) and isinstance(other, (int, float))):
            continue
        pct = abs(other - base) / abs(base) * 100 if base else None
        out.append(f"{pct:.1f}%" if pct is not None and pct < 1000 else f"{base:.4g} to {other:.4g}")
    return ", ".join(out) or "sizes in the table"


def build():
    """Every LOSS row of every standing table, from the verdict audit's one selection (tools/verdict_audit.py): the same tables,
    words and categories the live benchmark engine's appraisal counts, so the two can never differ."""
    from tools.verdict_audit import build as audit
    rec = audit()
    by_t = {t["stem"]: t for t in rec["tables"]}
    section_of = {"against its native": SECTIONS[0], "in place of a controller": SECTIONS[1],
                  "the orchestrator's own": SECTIONS[2], "two changes at once": SECTIONS[2]}
    rows = {s: [] for s in SECTIONS}
    engines = defaultdict(int)
    for r in rec["rows"]:
        t = by_t[r["table"]]
        if r["word"] != "LOSS" or t["status"] != "standing":
            continue
        n, name = int(t["engine"][len("omni-v"):]), t["stem"].split("_", 1)[1]
        where = (f"workload {r['section']} / " if t["stack"] == "Linux services" else f"{r['section']} / ") if r["section"] else ""
        rows[section_of[t["comparison"]]].append((n, name, ROOT / (t["json"] or t["file"]), where + r["gauge"], r, t["title"]))
        engines[n] += 1
    for s in SECTIONS:
        rows[s].sort(key=lambda x: (x[1], x[0]))
    return rows, engines


def render(built):
    rows, engines = built
    mine = rows[SECTIONS[0]]
    L = ["# The LOSS ledger: every row that reads LOSS across its three runs, in every benchmark's newest table", "",
         "Every row of every three-run table stands where its table stands, LOSS included; this page gathers the LOSS rows so "
         "none of them is found only by reading every table. A LOSS row is a gauge that moved away from its declared aim by 0.5% "
         "or more across the benchmark's three runs, A, B and C (the founder's order of 24 October 2026, `tools/readings.py`): in all "
         "three, every run's 95% interval clear of zero, or by the mean of the three, with the count of runs beyond the noise. Each benchmark "
         "is read from its newest whole table; an older engine's table stands only until the engine that stands has run that "
         "benchmark three times, and the engine each row ran on is printed beside it.", "",
         f"Rows that read LOSS across their three runs: **{sum(len(v) for v in rows.values())}**. Against my own native, the readings "
         f"do no harm is judged by: **{len(mine)}**. In place of a controller: **{len(rows[SECTIONS[1]])}**. Without me, or two "
         f"changes at once: **{len(rows[SECTIONS[2]])}**. By engine: "
         + (", ".join(f"omni-v{n}: {c}" for n, c in sorted(engines.items(), reverse=True)) or "none") + ".", ""]
    heads = {SECTIONS[0]: ("Against my own native",
                           "Omni-Compass on top of a native controller, against that native alone: the readings do no harm is "
                           "judged by (`DISCLOSURES.md`, section 3). Each row's cause stands beside it where it is written; a row "
                           "with none says so."),
             SECTIONS[1]: ("In place of a controller",
                           "Omni-Compass on the organism alone against an orchestrator as shipped (the four ways' VS): Omni-Compass "
                           "doing an orchestrator's work without it. Shown; a different question from do no harm, which is "
                           "judged against the native a governor sits on."),
             SECTIONS[2]: ("Without me, or two changes at once",
                           "The orchestrator as shipped against the organism alone (ORCH: neither arm carries Omni-Compass), and "
                           "Omni-Compass on top of the orchestrator against the organism alone (BOTH: the orchestrator and "
                           "Omni-Compass together, two changes at once). Shown because every row is shown.")}
    for s in SECTIONS:
        title, intro = heads[s]
        L += [f"## {title}", "", intro, ""]
        if not rows[s]:
            L += ["No row reads LOSS.", ""]
            continue
        if s == SECTIONS[0]:
            L += ["| Engine | Benchmark | Gauge | Each run's size | Cause | Fixed in | What decides it |", "|---|---|---|---|---|---|---|"]
            for n, name, p, gauge, row, title_ in rows[s]:
                c = cause(name, gauge)
                why, page, fixed, decides = c if c else ("not yet written", "", "", "the benchmark's three runs on the engine that stands")
                L.append(f"| omni-v{n} | `{p.relative_to(ROOT)}` | {gauge} | {sizes(row)} | {why}" + (f" (`{page}`)" if page else "")
                         + f" | {fixed or '—'} | {decides} |")
        else:
            L += ["| Engine | Benchmark | Gauge | Each run's size |", "|---|---|---|---|"]
            for n, name, p, gauge, row, title_ in rows[s]:
                L.append(f"| omni-v{n} | `{p.relative_to(ROOT)}` | {gauge} | {sizes(row)} |")
        L.append("")
    L += ["Each run's size is the change against the comparison's first arm, in percent of it, run by run; the direction is the "
          "gauge's, away from its aim in every run. The tables hold every number, its interval and its arms.", ""]
    return "\n".join(legal_stamp(with_own_runs(L))) + "\n"


def main(argv):
    md = render(build())
    if "--check" in argv:
        same = OUT.exists() and OUT.read_text() == md
        print("loss ledger: docs/LOSS_LEDGER.md " + ("matches the tables" if same else "differs from the tables: run python3 tools/loss_ledger.py"))
        return 0 if same else 1
    OUT.write_text(md)
    print(f"{OUT.relative_to(ROOT)} written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
