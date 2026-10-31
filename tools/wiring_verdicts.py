#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Wire in, or watch: the verdict per knob, read from every result in the repository.

Omni-Compass is wired OUT of every muscle (it reads every reading) and IN to a knob only where the paired measurement
shows no gauge of the muscle read LOSS (or power given) against native. The engine already does this on the muscle itself (omnicompass/verdict.py: the paired
trial, "left native" where no step is allowed; the realms' watch arm, which reads and writes nothing). This tool applies
the same principle to every published result, one verdict per knob, so an operator can see which knobs earn a wire in
and which stay native with Omni only reading them. The founder's order of 9 October 2026: "where Omni cannot beat
native, the muscle stays native; we only wire out of it".

The rule, the same for every table (every judged gauge counts; "shown, not judged" rows never do):

  write               at least one gauge GAIN across our three runs and none LOSS or power given: Omni holds the knob
  watch               no GAIN across our three runs: the knob stays native and Omni only reads it. Where a gauge read LOSS
                      or power given across our three runs it is named and its cause given; where the runs disagree,
                      nothing is settled and the knob stays native until it is
  operator's choice   GAIN, and LOSS or power given, both judged across our three runs: a trade. Both readings of the Omni index are printed where the
                      test is in it (the resource reading, the preregistered headline; the service reading, work and
                      speed alone) and the side that pays is named. The operator who wants the gain and can pay the
                      cost wires in; every other operator watches

Nothing is typed in: every verdict is computed from the test's own result file. Modelled muscles (the 1,107 on their
plants, results/realms_v5) take their verdict from the realms' label by rule (a GAIN on work, speed or misses: write, the
energy the max took for it power given, never a trade; SAME AS NATIVE and AT ITS LIMIT ON NATIVE: watch).

Every word is decided by what the gauge is for, never by the sign of its number (tools/readings.py, the key): time waited,
missed or failed aims lower; work done aims higher; a resource spent or held (energy, machines, memory, connections,
consumers, processor time) is spent, so a fall is a cut, a GAIN, and a rise is power given.

  python3 tools/wiring_verdicts.py            ->  docs/WIRING_VERDICTS.md, results/WIRING_VERDICTS.csv
  python3 tools/wiring_verdicts.py --check    ->  exit 1 if the committed files differ from what the tables give
"""
from __future__ import annotations

import collections
import csv
import io
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                       # noqa: E402
from tools.readings import with_own_runs, receipt_key, row_gain, word as gel_word, aim as gel_aim, classify as gel_classify, labelled, LABEL_SHOWN  # noqa: E402
from tools import omni_index                                       # noqa: E402
from tools.grid_v5 import kube_verdict                             # noqa: E402  (a square's line in GAIN, STEADY and LOSS)

LIVE = ROOT / "results" / "live"
OUT_MD = ROOT / "docs" / "WIRING_VERDICTS.md"
OUT_CSV = ROOT / "results" / "WIRING_VERDICTS.csv"

WRITE, WATCH, CHOICE = "write", "watch", "operator's choice"
UNJUDGED = "shown, not judged"


# ------------------------------------------------------------------------------------------------------ the rule
CLASSES = ("gain", "loss", "given", "noise", "disagree", "same")


def classify(reading, aim=None):
    """A table's reading in one word for the scoring: gain, loss, given (power given), noise, disagree, same or unjudged
    (tools/readings.py reads every table's words; aim is the gauge's, needed for the direction words of 13 October)."""
    return gel_classify(reading, aim)


def empty():
    return {c: [] for c in CLASSES}


def verdict(gain, away):
    """The three words. gain: how many judged gauges read GAIN across our three runs; away: how many read LOSS or power
    given."""
    if gain and not away:
        return WRITE
    if gain and away:
        return CHOICE
    return WATCH


def away_of(j):
    """The judged gauges that read LOSS or power given."""
    return j["loss"] + j["given"]


def pct_range(runs):
    """The change omni against native over the runs, as 'lo to hi' in percent (one figure when they agree to a point)."""
    ps = []
    for r in runs:
        n, o = r.get("native"), r.get("omni")
        if n is None or o is None or not isinstance(n, (int, float)) or not isinstance(o, (int, float)):
            continue
        if abs(n) < 1e-12:
            ps.append(None if abs(o) < 1e-12 else math.inf)
        else:
            ps.append(100.0 * (o - n) / abs(n))
    ps = [p for p in ps if p is not None]
    if not ps:
        return ""
    if any(math.isinf(p) for p in ps):
        return "from zero"
    lo, hi = min(ps), max(ps)
    f = (lambda x: f"{x:+.0f}%") if max(abs(lo), abs(hi)) >= 10 else (lambda x: f"{x:+.1f}%")
    return f(lo) if f(lo) == f(hi) else f"{f(lo)} to {f(hi)}"


def first(runs, key):
    r = runs[0] if runs else {}
    v = r.get(key)
    return v


# ------------------------------------------------------------------------------------- the real stacks (three runs)
K8S_TESTS = [(name, f) for _, name, f, _, _ in omni_index.SOURCES]          # the seven Kubernetes tests, in the index's order
K8S_NAMES = {"V7_STEADY.json": "steady work", "V7_WANDERING.json": "demand that wanders", "V7_ALL_FOUR.json": "all four at once",
             "V7_FAIRNESS.json": "a noisy neighbour", "V7_FAULTS.json": "faults", "V7_BATCH.json": "a queue of jobs",
             "V7_TRACE_GOOGLE2011.json": "a public day of demand (Google 2011)"}
K8S_KNOB = "the autoscaler's replicas, the floor and the machines"
K8S_GAUGE = {"worker nodes in service, mean": "machines", "node-hours": "machine-hours", "energy (Wh)": "standby-model energy",
             "energy, parked workers still on at idle power (Wh)": "parked-worker energy", "response time (ms), mean": "mean response",
             "response time (ms), 95th percentile": "p95", "response time (ms), 99th percentile": "p99",
             "time over the response line (% of samples)": "time over the line", "failed requests (%)": "failed requests",
             "HPA replicas, mean": "replicas", "pods started": "pods started",
             omni_index.CAPACITY: "work inside the line", omni_index.CAPACITY_NOW: "work inside the line",
             "batch: worker machines in service after the queue finished, mean": "machines after the queue",
             "batch: queue finished (s)": "queue finished"}
WORKLOAD_STACKS = [
    # (category in the index, file, the knob in words, {gauge key: name}, the tuning workload's name, the declared cost note)
    ("Real database (PostgreSQL behind PgBouncer, GitHub)", "V7_PGBENCH.json", "the pooler's pool size (server connections)",
     {"work_inside_line_tps": "work inside the line", "tps": "throughput", "p95_ms": "p95", "p99_ms": "p99", "p50_ms": "median", "mean_ms": "mean",
      "servers_alive_mean": "connections held open", "servers_alive_max": "connections most at once", "cpu_busy_share": "host CPU busy",
      "cpu_seconds": "host CPU-seconds", "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
    ("Real messaging (Apache Kafka, GitHub)", "V7_KAFKA.json", "the consumer group's size",
     {"work_inside_line_mps": "work inside the line", "mps": "throughput", "p95_ms": "p95", "p99_ms": "p99", "p50_ms": "median", "mean_ms": "mean",
      "lag_max": "messages waiting, most", "lag_mean": "messages waiting, mean", "consumers_mean": "consumers running", "consumers_max": "consumers most at once",
      "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds", "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "lost": "lost"}),
    ("Real cache (Redis, GitHub)", "V7_REDIS.json", "the cache's memory ceiling",
     {"work_inside_line_rps": "work inside the line", "rps": "throughput", "hit_rate": "hit rate", "p95_ms": "p95", "p99_ms": "p99", "mean_ms": "mean",
      "maxmemory_mb_mean": "memory ceiling held", "used_mb_mean": "memory used", "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds",
      "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
    ("Real database cache (MongoDB under YCSB, GitHub)", "V7_YCSB.json", "the storage engine's cache size",
     {"work_inside_line_ops": "work inside the line", "ops": "throughput", "p95_ms": "p95", "p99_ms": "p99", "mean_ms": "mean",
      "cache_mb_mean": "cache size held", "cache_used_mb_mean": "cache in use", "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds",
      "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
    ("Real database buffer pool (MySQL under sysbench, GitHub)", "V7_SYSBENCH.json", "the buffer pool's size",
     {"work_inside_line_tps": "work inside the line", "tps": "throughput", "qps": "queries a second", "p95_ms": "p95", "p99_ms": "p99", "mean_ms": "mean",
      "pool_mb_mean": "pool held", "pool_used_mb_mean": "pages holding data", "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds",
      "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
]
STACK_SHORT = {"V7_PGBENCH.json": "PostgreSQL", "V7_KAFKA.json": "Kafka", "V7_REDIS.json": "Redis", "V7_YCSB.json": "MongoDB", "V7_SYSBENCH.json": "MySQL"}


def _stack_directions():
    """Every stack gauge's declared direction, from its runner (tools/run_*.py): the tables written before the gauges' aims
    were stored beside their readings are read by these."""
    out = {}
    for name in ("run_pgbench", "run_kafka", "run_redis", "run_ycsb", "run_sysbench", "run_cpu_power"):
        try:
            mod = __import__(f"tools.{name}", fromlist=["GAUGES"])
        except ImportError:
            continue
        for k, _, d in mod.GAUGES:
            out.setdefault(k, d)
    return out


STACK_DIRECTIONS = _stack_directions()

# Why each gauge that read LOSS or power given across our three runs did, read from the preregistration that carries the result (the file is named so a
# reader can check the words against the record). Keyed by (file, workload or test, gauge key); a key of "*" matches any case.
WHY = {
    ("V7_KAFKA.json", "*", "consumers_mean"): "the knob itself: Omni adds consumers while messages wait and the queue is kept short; the consumers running are the price, declared in advance as the gauge expected to rise: the power given (`docs/KAFKA_PREREGISTRATION.md`, the gauges)",
    ("V7_KAFKA.json", "*", "consumers_max"): "the same price at its peak: the group grown to the partition count while the burst is drained",
    ("V7_KAFKA.json", "*", "cpu_busy_share"): "more consumers polling cost the host CPU on the light workload, where the broker had slack; on the heavy and burst workloads the CPU is inside the noise",
    ("V7_KAFKA.json", "*", "cpu_seconds"): "the same CPU, counted over the run",
    ("V7_REDIS.json", "*", "maxmemory_mb_mean"): "the knob itself: the ceiling grows while the cache is full and misses, so a wide working set is held instead of evicted; the memory is the price of the hit rate, declared in advance as the gauge expected to rise: the power given (`docs/REDIS_PREREGISTRATION.md`, the gauges)",
    ("V7_REDIS.json", "*", "used_mb_mean"): "the memory actually used follows the ceiling: the working set the operator's 64 MB could not hold is held",
    ("V7_PGBENCH.json", "simple_update", "servers_alive_max"): "amendment 1's add rule (\"slow, clients waiting for a server: add\") fired 4 to 15 times an arm on this slow write workload and bought servers above the operator's 20, up to 36 at the peak; work, latency and CPU inside the noise, so nothing was bought for them (`docs/POSTGRES_PREREGISTRATION.md`, the second set). The rule stands as written and the verdict for this workload is to watch",
    ("V7_SYSBENCH.json", "read_write", "pool_used_mb_mean"): "memory bought on real misses: a written working set keeps the pool missing above one percent, so the growth gate lets the pool grow to 1.1 to 1.6 GB in the wide notches; the host's CPU was cut 4% to 6% for it, a GAIN across our three runs, and latency did not move (`docs/MYSQL_PREREGISTRATION.md`, the third set)",
}
DECLARED_COST = {"V7_KAFKA.json": "consumers", "V7_REDIS.json": "memory"}


def load_index():
    """The two index readings per test, keyed by (file, workload or None)."""
    out = {}
    for t in omni_index.tests():
        f = t["source"].rsplit("/", 1)[-1]
        m = re.search(r"`([a-z_]+)`", t["test"])
        out[(f, m.group(1) if m else None)] = (t.get("index_pct"), t.get("service_pct"))
    return out


def row_aim(k, v):
    """A row's aim: the table's own field where it carries one; else the generating tool's declared direction for the key
    (the stacks' runners), the capacity row's (work done: higher), or time waited for every other Kubernetes row; a resource
    spent or held is spent (tools/readings.py)."""
    if v.get("aim"):
        return gel_aim(v["aim"], k)
    if "work inside the response line" in k:
        return "higher"
    return gel_aim(STACK_DIRECTIONS.get(k, "lower"), k)


def judge_rows(rows, names, keys_order=None):
    """rows: {gauge key: {"reading", "runs"}}. Returns the classified lists with their ranges and each row's aim."""
    out = empty()
    for k in (keys_order or rows):
        v = rows[k]
        a = row_aim(k, v)
        c = classify(v["reading"], a)
        if c == "unjudged":
            continue
        out[c].append((k, names.get(k, k), pct_range(v["runs"]), v["runs"], a))
    return out


def real_stacks(index):
    cases = []
    # every test is read on the newest engine's table that holds it (omni_index.newest, as the index reads it); the names and
    # the notes stay keyed by the test's first file
    for name, f in K8S_TESTS:
        fn = omni_index.newest(f)
        p = LIVE / fn
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        j = judge_rows(d["rows"], K8S_GAUGE)
        v = verdict(len(j["gain"]), len(away_of(j)))
        res, svc = index.get((fn, None), (None, None))
        why = k8s_why(f, j, v)
        cases.append({"kind": "real knob", "domain": "Real Kubernetes (GitHub, kind)", "knob": K8S_KNOB, "case": K8S_NAMES.get(f, name),
                      "counted": True, "judged": j, "verdict": v, "resource_pct": res, "service_pct": svc, "why": why,
                      "source": f"results/live/{fn.replace('.json', '.md')}", "runs": [r["run"] for r in d["runs"]]})
    for cat, f, knob, names in WORKLOAD_STACKS:
        fn = omni_index.newest(f)
        p = LIVE / fn
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        for wl, gauges in d["workloads"].items():
            j = judge_rows(gauges, names)
            v = verdict(len(j["gain"]), len(away_of(j)))
            res, svc = index.get((fn, wl), (None, None))
            cases.append({"kind": "real knob", "domain": cat, "knob": knob, "case": wl + (" (tuning workload: shown, never counted)" if wl == "tuning" else ""),
                          "counted": wl != "tuning", "judged": j, "verdict": v, "resource_pct": res, "service_pct": svc,
                          "why": stack_why(f, wl, j, v, res, svc), "source": f"results/live/{fn.replace('.json', '.md')}",
                          "runs": [r["run"] for r in d["runs"]], "stack": STACK_SHORT[f], "workload": wl})
    return cases


def magnitude(rg):
    """'-65% to -66%' -> '65% to 66%': the size of a change without its sign (the sign is said in words instead)."""
    nums = re.findall(r"[-+]?\d+(?:\.\d+)?%", rg or "")
    if not nums:
        return (rg or "").lstrip("+-−")                     # a count's change (no percent): its size, the sign said in words
    mags = sorted(abs(float(x.rstrip("%"))) for x in nums)
    f = (lambda x: f"{x:.0f}%") if mags[-1] >= 10 else (lambda x: f"{x:.1f}%")
    return f(mags[0]) if f(mags[0]) == f(mags[-1]) else f"{f(mags[0])} to {f(mags[-1])}"


def verb(aim, rg):
    """Which way a change went, in the plain verb beside its word: a fall is a cut where less is the aim (time waited, a
    resource spent) and down where more is the aim (work done); a rise is up."""
    fell = (rg or "").strip().startswith(("-", "−"))
    if rg == "from zero":
        return "up from zero"
    if fell:
        return "down" if aim in ("higher", "never less") else "cut"
    return "up"


def words(name, aim, rg, tag=True):
    """'p95 cut 65% to 66%' or 'memory ceiling up 205% to 215%'."""
    v = verb(aim, rg); m = magnitude(rg)
    return f"{name} {v}" + (f" {m}" if m and v != "up from zero" else "")


def fmt_list(items, n=4, cls=None, tag=False):
    """'p95 cut 65% to 66%, p99 cut 68% to 72%, ...' from classified items (each carries its gauge's aim)."""
    s = [words(it[1], it[4] if len(it) > 4 else None, it[2], tag) for it in items[:n]]
    more = len(items) - n
    return ", ".join(s) + (f" and {more} more" if more > 0 else "")


def away_cell(j, n=12):
    """The LOSS and power-given gauges of a case, each named with its word."""
    parts = []
    if j["loss"]:
        parts.append("LOSS: " + fmt_list(j["loss"], n))
    if j["given"]:
        parts.append("power given: " + fmt_list(j["given"], n))
    return "; ".join(parts)


def k8s_why(f, j, v):
    if v == WRITE:
        return (f"{len(j['gain'])} gauges GAIN across our three runs ({fmt_list(j['gain'])}), none LOSS or power given"
                + (f"; {len(j['noise'])} gauges STEADY, inside the noise" if j["noise"] else "") + ". Omni holds the knob")
    if v == WATCH and not away_of(j):
        return (f"every judged gauge STEADY ({len(j['noise'])} inside the noise, {len(j['same'])} the same), the neighbour's "
                f"own rows included: beside a noisy neighbour no gauge moved, so under this demand the knob has nothing to move. "
                f"The same knob writes under the other six demands")
    return (f"GAIN across our three runs: {fmt_list(j['gain'])}"
            + (f"; LOSS across our three runs: {fmt_list(j['loss'])}" if j["loss"] else "")
            + (f"; power given across our three runs: {fmt_list(j['given'])}" if j["given"] else ""))


def stack_why(f, wl, j, v, res, svc):
    short = STACK_SHORT[f]
    parts = []
    if j["disagree"]:
        parts.append(f"the runs disagree on {', '.join(f'{nm} ({rg})' for _, nm, rg, *_ in j['disagree'][:3])}")
    if not j["gain"] and not away_of(j):
        parts.append(f"everything STEADY in all three of our runs ({len(j['noise'])} gauges inside the noise" + (f", {len(j['same'])} the same" if j["same"] else "") + ")")
    s = ("; ".join(parts) + ".") if parts else ""
    causes = []
    for k, nm, rg, _, a in away_of(j):
        w = WHY.get((f, wl, k)) or WHY.get((f, "*", k))
        if w:
            causes.append(f"{words(nm, a, rg)} ({gel_word(rg.startswith('-'), a)}), because {w}")
    if causes:
        s += " Why: " + "; ".join(causes) + "."
    s = s.strip()
    if v == CHOICE:
        cost = DECLARED_COST.get(f)
        if res is not None and svc is not None:
            if res > 0 and svc > 0:
                s += (f" The trade pays under both readings of the index (resource {res:+.1f}%, service {svc:+.1f}%): the operator who runs {short} "
                      f"for its service wires in and pays in {cost or 'the resource named'}; an operator who counts that resource above the service watches.")
            elif svc > 0:
                s += (f" The trade pays under the service reading ({svc:+.1f}%) and not under the resource reading ({res:+.1f}%, the preregistered "
                      f"headline): the operator who runs {short} for its speed and has the {cost or 'resource'} wires in; the operator who counts the "
                      f"{cost or 'resource'} as the cost watches.")
            else:
                s += (f" Under the index's own scoring the GAIN outweighs what was given by {res:+.1f}% (resource reading); the service reading is "
                      f"{svc:+.1f}%: a small trade, the operator's to take or leave.")
    if v == WATCH and j["disagree"] and not away_of(j):
        s += " Nothing is settled here, so the knob stays native until three runs agree."
    if v == WATCH and not j["gain"] and not away_of(j) and not j["disagree"]:
        s += " STEADY under this workload: the knob stays native and Omni reads it."
    if v == WRITE:
        s += " No LOSS and no power given: Omni holds the knob."
    return s


# ------------------------------------------------------------------------------- the modelled simulators (markdown)
SIMS = [
    ("V7_MUJOCO.md", "Robot arms (MuJoCo Menagerie, Google DeepMind)", "the servo's speed override inside the takt",
     {"Robots where Omni moved the override": "moved", "Robots where the paired trial left the override native": "left_native",
      "Robots the task could not be run on": "not_run"}),
    ("V7_PANDAPOWER.md", "The power grid (pandapower, SimBench grids)", "the substation's voltage setpoint, one tap at a time",
     {"ZIP loads (40% Z, 30% I, 30% P)": "moved:ZIP loads", "constant-power loads (SimBench as shipped)": "moved:constant-power loads"}),
    ("V7_CITYLEARN.md", "Buildings and batteries (CityLearn, UT Austin)", "the electric batteries' charge and discharge commands",
     {"Districts with electric batteries: omni against native, each run": "moved", "Districts with no electric battery: nothing for Omni to move": "no_knob",
      "Districts CityLearn cannot run with its own controller": "not_run"}),
    ("V7_SWARM.md", "Drone swarms (gym-pybullet-drones, University of Toronto)", "the autopilot's cruise override",
     {"Cells where Omni moved the cruise": "moved", "Cells where the paired trial left the cruise native": "left_native", "Void cells": "void"}),
]
SIM_SHORT = {
    "V7_PANDAPOWER.md": {"losses_up": "line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table)",
                         "taps_up": "taps: the declared cost on a grid that barely taps on its own (4 a year, doubled)",
                         "import_up": "import: follows the line heating, hundredths of a percent"},
    "V7_CITYLEARN.md": {"2023": "the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table)",
                        "monthly": "the monthly load factor moved by a tenth of a percent against a bill cut 8.6%"},
}
SIM_WHY = {
    "V7_PANDAPOWER.md": {
        "losses_up": ("the lower setpoint carries the grid's power at a lower voltage and therefore a higher current, and the energy dissipated "
                         "in the lines rises with the square of the current. The four grids where it rose are four of the five that export more "
                         "than they import (net import negative: rural 1 and 2, semiurb 1 and 2); on the importing grids the loads' own draw falls "
                         "with the voltage under ZIP loads and the line heating falls with it. Under constant-power loads the loads draw the same "
                         "at any voltage, so the setpoint saves nothing on the loads and the exporting grids give the line heating with nothing bought"),
        "taps_up": ("tap operations, declared in advance as Omni's expected cost (`docs/PANDAPOWER_PREREGISTRATION.md`): this grid barely taps on "
                       "its own (4 a year), so Omni's moves double a very small count"),
        "import_up": "the import follows the line heating: the same loads, more dissipated on the lines, so hundredths of a percent less exported or more imported upstream"},
    "V7_CITYLEARN.md": {
        "2023": ("the seven 2023 challenge districts are small (3 to 6 buildings) and short (720 to 2,208 hours), and in them the energy "
                 "not served and the comfort rows move, where in the county neighbourhoods they read the same: the compass steers the batteries from the district's "
                 "electricity reading alone (one wire, one muscle, `docs/CITYLEARN_PREREGISTRATION.md`), flattening the draw it sees, and in "
                 "these districts that leaves less in the batteries for the hours that count against the bill, the hour-to-hour ramping and "
                 "the energy not served. The bill, what the battery is bought to lower, is up 0.2% to 0.4% in all three of our runs here (power given), so "
                 "for the operator who pays the bill this is a watch. The cause is a reading of the tables, not yet tested on its own"),
        "monthly": "the monthly load factor moved by a tenth of a percent against a bill cut 8.6% and the electricity bought cut 14.7%"},
    "V7_MUJOCO.md": {
        "left_native": ("the engine's own verdict: one cycle at full speed and one at override 0.8, in native mode before the counted cycles, "
                        "showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so the "
                        "override was left at 1.0 and both arms are the same (`omnicompass/verdict.py`, left native)")},
}


def parse_sim(path):
    """The sections, subsections and tables of a simulator's A/B/C markdown table."""
    text = path.read_text()
    sections = []
    cur = None
    for ln in text.splitlines():
        if ln.startswith("## "):
            cur = {"title": ln[3:].strip(), "subs": [], "table": []}
            sections.append(cur)
        elif ln.startswith("### ") and cur is not None:
            cur["subs"].append({"title": ln[4:].strip(), "rows": []})
        elif ln.startswith("|") and cur is not None:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            (cur["subs"][-1]["rows"] if cur["subs"] else cur["table"]).append(cells)
    return sections


# the gauge names the simulators' tables used before the word LOSS became a reading (a physical term renamed, the same gauge)
OLD_LABELS = {"line and transformer losses (MWh)": "energy dissipated in lines and transformers (MWh)",
              "copper loss per cycle (J, declared model)": "copper heating per cycle (J, I²R, declared model)"}


def sim_aims(f):
    """{gauge label as the simulator's table writes it: its aim}, from the simulator's own gauge list (CityLearn's scores:
    tools/citylearn_abc.py's aims)."""
    try:
        if f == "V7_MUJOCO.md":
            from tools.run_mujoco import GAUGES
        elif f == "V7_PANDAPOWER.md":
            from tools.pandapower_abc import GAUGES
        elif f == "V7_SWARM.md":
            from tools.swarm_abc import GAUGES
        elif f == "V7_CITYLEARN.md":
            from tools.citylearn_abc import KPIS, KPI_NAMES, aim_of as kpi_aim
            return {f"{KPI_NAMES.get(k, k)} (`{k}`)": kpi_aim(k) for k in KPIS}
        else:
            return {}
    except ImportError:
        return {}
    aims = {name: gel_aim(d, k) for k, name, d in GAUGES}
    aims.update({old: aims[new] for old, new in OLD_LABELS.items() if new in aims})
    return aims


def sim_rows_judged(rows, aims=None):
    """Rows of a gauge table (header first) into classified items with the A/B/C range; aims: sim_aims() of the table."""
    j = empty()
    if not rows:
        return j
    head = rows[0]
    ridx = len(head) - 1
    abc = [i for i, h in enumerate(head) if h in ("A", "B", "C")]
    for r in rows[1:]:
        if len(r) != len(head):
            continue
        a = aims.get(r[0]) if aims else None
        c = classify(r[ridx], a)
        if c == "unjudged":
            continue
        vals = []
        for i in abc:
            s = r[i].replace("−", "-")
            if s.endswith("%"):
                try:
                    vals.append(float(s[:-1]))
                except ValueError:
                    pass
        if vals:
            lo, hi = min(vals), max(vals)
            f = (lambda x: f"{x:+.0f}%") if max(abs(lo), abs(hi)) >= 10 else (lambda x: f"{x:+.1f}%")
            rg = f(lo) if f(lo) == f(hi) else f"{f(lo)} to {f(hi)}"
        else:
            rg = r[abc[0]] if abc else ""
        name = re.sub(r"\s*\(`[^`]*`\)\s*$", "", r[0])          # CityLearn: drop the score's code name
        name = re.sub(r"\s*\([^()]*\)\s*$", "", name) or name     # the unit or the note in brackets: the table has it
        j[c].append((r[0], name, rg, None, a))
    return j


def sims():
    cases = []
    for f, domain, knob, modes in SIMS:
        p = LIVE / f
        if not p.exists():
            continue
        for sec in parse_sim(p):
            mode = next((m for t, m in modes.items() if sec["title"].startswith(t)), None)
            if mode is None:
                continue
            if mode.startswith("moved"):
                tag = mode.split(":", 1)[1] if ":" in mode else ""
                for sub in sec["subs"]:
                    name = sub["title"].split(":", 1)[0].strip()
                    j = sim_rows_judged(sub["rows"], sim_aims(f))
                    counted = not (f == "V7_SWARM.md" and name == "tuning")
                    v = verdict(len(j["gain"]), len(away_of(j)))
                    cases.append({"kind": "modelled simulator", "domain": domain, "knob": knob, "case": name + (f" ({tag})" if tag else "")
                                  + ("" if counted else " (the tuning swarm: shown, never counted)"),
                                  "counted": counted, "judged": j, "verdict": v, "resource_pct": None, "service_pct": None,
                                  "why": sim_why(f, name, j, v), "source": f"results/live/{f}", "runs": []})
            elif mode == "left_native":
                for r in sec["table"][1:]:
                    if not r or not r[0]:
                        continue
                    j = empty()
                    cases.append({"kind": "modelled simulator", "domain": domain, "knob": knob, "case": r[0], "counted": True, "judged": j,
                                  "verdict": WATCH, "resource_pct": None, "service_pct": None,
                                  "why": SIM_WHY[f]["left_native"][0].upper() + SIM_WHY[f]["left_native"][1:]
                                         + f". The trial's figures: {r[1]} J at full speed against {r[2]} J at the trial speed, reproduced over A, B, C: {r[3]}",
                                  "source": f"results/live/{f}", "runs": []})
            elif mode == "no_knob":
                for r in sec["table"][1:]:
                    if not r or not r[0]:
                        continue
                    cases.append({"kind": "modelled simulator", "domain": domain, "knob": knob, "case": r[0], "counted": False, "judged": None,
                                  "verdict": "no knob", "resource_pct": None, "service_pct": None,
                                  "why": f"no electric battery in the district ({r[1]} buildings, {r[2]} water tanks left native): there is nothing for Omni to hold, "
                                         f"so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation"
                                         + (f" (scores that differ in A: {r[3]}; reproduced: {r[4]})" if len(r) > 4 else ""),
                                  "source": f"results/live/{f}", "runs": []})
    return cases


def sim_why(f, name, j, v):
    parts = []
    if j["disagree"]:
        parts.append(f"the runs differ on {', '.join(f'{nm} ({rg})' for _, nm, rg, *_ in j['disagree'][:3])}")
    if not j["gain"] and not away_of(j):
        parts.append("everything STEADY in all three of our runs")
    s = ("; ".join(parts) + ".") if parts else ""
    why = SIM_SHORT.get(f, {})
    if f == "V7_PANDAPOWER.md" and away_of(j):
        keys = [it[0] for it in away_of(j)]
        causes = []
        if any("losses" in k or "dissipated" in k for k in keys):
            causes.append(why["losses_up"])
        if any("tap" in k for k in keys):
            causes.append(why["taps_up"])
        if any("import" in k for k in keys):
            causes.append(why["import_up"])
        s = (s + " Why: " + "; ".join(causes) + ".").strip()
        if v == CHOICE:
            s += " The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches."
    if f == "V7_CITYLEARN.md" and away_of(j):
        if "2023" in name:
            s = (s + " Why: " + why["2023"] + ".").strip()
        elif any("monthly" in it[0] for it in away_of(j)):
            s = (s + " Why: " + why["monthly"] + ".").strip()
        if v == CHOICE and "2023" in name:
            s += " By rule a trade; by what the battery is for (the bill), a watch."
    s = s.strip()
    if f == "V7_SWARM.md" and v == WRITE:
        s += " No LOSS: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved."
    if f == "V7_MUJOCO.md" and v == WRITE:
        s += " No LOSS: the same job inside the same takt, hit more accurately with less force; the cycle is slower inside the takt (shown, not judged)."
    if v == WRITE and f in ("V7_PANDAPOWER.md", "V7_CITYLEARN.md"):
        s += " No LOSS and no power given: Omni holds the knob."
    return s.strip()


# ------------------------------------------------------------------------------------- the 1,107 modelled muscles
LABEL_VERDICT = {"SUPERIOR WITHIN GUARDRAILS": WRITE, "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF": CHOICE,
                 "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF": CHOICE, "NONINFERIOR / INCONCLUSIVE": WATCH, "NOT ESTABLISHED": WATCH,
                 "AWAY FROM ITS AIM": WATCH, "INVALID": "invalid"}
REALM_NAMES = {"spine": "The spine, the muscles every stack runs on",
               "compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
               "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
               "stack": "The four stacked, every duplicate kept", "tower": "The whole tower, every muscle once"}
V5_DIR = ROOT / "results" / "realms_v5"
V5_LOADS = ("normal", "line")                    # every muscle alone runs its own load and work waiting in line
V5_ORGANISM_LOADS = ("normal", "climb", "line")
AT_LIMIT, SAME = "AT ITS LIMIT ON NATIVE", "SAME AS NATIVE"


def v5_verdict(label):
    """The v5 label's verdict by rule (the founder's orders of 13 October): a GAIN on work, speed or misses, alone or together,
    on every load the muscle ran, is write, and the energy the max took for it is power given, shown beside it, never a
    trade; SAME AS NATIVE is watch (nothing moved beyond the noise); AT ITS LIMIT ON NATIVE is watch by design (the knob
    already runs at the top of its range on native, read and left native)."""
    lab = (label or "").upper()
    if lab == "INVALID":
        return "invalid"
    if "MORE WORK" in lab or "FASTER" in lab or "FEWER MISSES" in lab:
        return WRITE
    return WATCH


def ffl(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def muscles():
    """One row per muscle of the 1,107 (results/realms_v5/MUSCLES_V5.csv, engine omni-v5 at the max): its label over every load it
    ran (label_all_loads), the verdict by rule (v5_verdict), and the figures of each load in words."""
    rows = list(csv.DictReader((V5_DIR / "MUSCLES_V5.csv").open()))
    by = collections.OrderedDict()
    for r in rows:
        by.setdefault(r["muscle_id"], collections.OrderedDict())[r["load"]] = r
    out = []
    for mid, loads in by.items():
        r = loads.get("normal") or next(iter(loads.values()))
        label = r["label_all_loads"]
        w = max((ffl(x["writes_per_run"]) or 0.0) for x in loads.values())
        parts = []
        for ld in V5_LOADS:
            x = loads.get(ld)
            if not x:
                continue
            bits = [labelled(x["label"])]
            if x["label"] not in (AT_LIMIT, SAME):
                viol, work, pg = ffl(x["viol_pp"]), ffl(x["work"]), ffl(x["power_given"])
                if viol is not None:
                    bits.append(f"misses {viol:+.2f} pp")
                if work is not None:
                    bits.append(f"work {100 * work:+.2f}%")
                if pg:
                    bits.append(f"power given {100 * pg:+.2f}%")
            parts.append(f"{ld}: " + ", ".join(bits))
        if label == AT_LIMIT:
            why = ("at its limit on native: the knob already runs at the top of its range on native (everything admitted, the full clock, the "
                   "full battery power), so there is nothing to push; read and left native. " + "; ".join(parts))
        elif label == SAME:
            why = ((f"wrote {w:.0f} times a run with no measurable change in work, speed or misses: the same as native. " if w else
                    "wrote nothing in any run: native held the reading and the law had nothing to push. ") + "; ".join(parts))
        else:
            why = "; ".join(parts) + (f"; wrote {w:.0f} times a run" if w else "")
        out.append({"kind": "modelled muscle", "domain": f"{REALM_NAMES.get(r['realm'], r['realm'])}: {r['family']}", "knob": r["knob"],
                    "case": r["muscle"], "counted": True, "judged": None, "verdict": v5_verdict(label), "resource_pct": None, "service_pct": None,
                    "why": why, "source": "results/realms_v5/MUSCLES_V5.csv", "runs": [], "muscle": r, "label": label, "writes": w, "loads": loads})
    return out


def organisms_modelled():
    """The seven organisms under the normal, climb and line loads (results/realms_v5/REALMS_V5.json): the whole, every muscle written at
    once by one brain; misses in percentage points, work, and the energy the max took as power given."""
    d = json.loads((V5_DIR / "REALMS_V5.json").read_text())
    out = []
    for load in V5_ORGANISM_LOADS:
        for name, o in d["organisms"].get(load, {}).items():
            sm = o["summary"]
            viol, work, pg = sm["viol_pp"], sm["work"], sm["energy"]
            out.append({"kind": "modelled organism", "domain": f"{REALM_NAMES.get(name, name)}, the {load} load", "knob": "every muscle of the organism, one brain",
                        "case": f"{o['n']} muscles", "counted": True, "judged": None, "verdict": v5_verdict(o["label"]), "resource_pct": None,
                        "service_pct": None, "why": f"{labelled(o['label'])}: misses {viol[0]:+.3f} pp ({viol[1]:+.3f} to {viol[2]:+.3f}), "
                        f"work {100 * work[0]:+.3f}%, power given {100 * pg[0]:+.3f}%; valid: {'yes' if o['valid'] else 'no'}",
                        "source": "results/realms_v5/REALMS_V5.md", "runs": [], "label": o["label"], "load": load})
    return out


# ------------------------------------------------------------------- the organisms with the real cluster inside
def organisms_cluster():
    out = []
    for f, title in (("V3_SIX_KUBE.json", "the six organisms with the real cluster inside (GitHub, 10 and 100 copies)"),
                     ("V3_BIG_ORGANISM.json", "the big organisms with the real cluster inside (a rented Azure machine, 1,000 copies)")):
        p = LIVE / f
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        for cell, c in d["organisms"].items():
            rows = c.get("rows") or {}
            if not rows or c.get("repetitions", 0) < 2:
                continue
            sure = lambda v: v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
            judged = {k: v for k, v in rows.items() if not v["neutral"] and not v["same"] and sure(v)}
            # the cluster's own gauges decide; the organism's modelled work and energy are judged muscle by muscle in the realms table
            gain = [k for k, v in judged.items() if not k.startswith("organism") and row_gain(v)]
            away = [k for k, v in judged.items() if not k.startswith("organism") and not row_gain(v)]
            modelled_away = [k for k, v in judged.items() if k.startswith("organism") and not row_gain(v)]
            v = verdict(len(gain), len(away))
            named = lambda ks: ", ".join("%s %+.1f%%" % (K8S_GAUGE.get(k, k), rows[k]["pct"]) for k in ks)
            given = [k for k in away if gel_aim("lower", k) == "spent"]
            lost = [k for k in away if k not in given]
            why = (f"each gauge's word: {kube_verdict(c)}. The cluster's gauges: {len(gain)} GAIN"
                   + (f" ({named(gain[:5])})" if gain else "")
                   + f", {len(lost)} LOSS" + (f" ({named(lost)})" if lost else "")
                   + f", {len(given)} power given" + (f" ({named(given)})" if given else "") + ".")
            if modelled_away:
                ow = rows.get("organism work")
                why += (f" The organism's modelled {', '.join(k.replace('organism ', '') for k in modelled_away)}"
                        + (f" {ow['pct']:+.4f}% ({abs(ow['pct']) * 1e4:.0f} parts in a million, rounding level)" if ow and "organism work" in modelled_away else "")
                        + " (LOSS or power given) is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's.")
            oe = rows.get("organism energy (J)")
            if oe:
                why += f" The organism's modelled energy {oe['pct']:+.1f}%."
            if c.get("off_the_clock_reps"):
                why += f" Off the clock in {len(c['off_the_clock_reps'])} of {c['repetitions']} repetitions."
            out.append({"kind": "organism with the cluster inside", "domain": title, "knob": K8S_KNOB + " under the organism's demand",
                        "case": cell.replace("@", " at ") + " copies" if "@" in cell else cell, "counted": True, "judged": None, "verdict": v,
                        "resource_pct": None, "service_pct": None, "why": why, "source": f"results/live/{f.replace('.json', '.md')}", "runs": []})
    return out


# ------------------------------------------------------------------------------------------------- the report
def pct_s(x):
    return "" if x is None else f"{x:+.1f}%"


def count(cases):
    c = collections.Counter(x["verdict"] for x in cases if x["counted"] and x["verdict"] in (WRITE, WATCH, CHOICE))
    return c[WRITE], c[CHOICE], c[WATCH]


def esc(s):
    return s.replace("|", "\\|")


def main(check=False):
    index = load_index()
    real = real_stacks(index)
    sim = sims()
    mus = muscles()
    org_m = organisms_modelled()
    org_c = organisms_cluster()
    all_cases = real + sim + mus + org_m + org_c

    rw, rc, rwa = count(real)
    sw, sc, swa = count([x for x in sim if x["verdict"] != "no knob"])
    mw, mc, mwa = count(mus)
    ow, oc, owa = count(org_c)

    L = ["# Wire in, or watch: the verdict per knob, from every result in the repository", "", *receipt_key(), "",
         "Omni-Compass is wired **out of** every muscle: it reads every reading. It is wired **into** a knob only where the paired "
         "measurement shows no gauge of the muscle read **LOSS** against native. Where the measurement shows nothing (**STEADY**), or shows "
         "a LOSS, the muscle stays "
         "native and Omni only watches it: one wire out, no wire in. This is not a new rule. It is what the engine does on the muscle "
         "itself before it moves anything (`omnicompass/verdict.py`: the paired trial, and the verdict **left native** where no step is "
         "allowed), and it is the watch arm of every realms run (`docs/REALMS_PREREGISTRATION.md`: the governor reads every period and "
         "writes nothing). This page applies the same principle to every published result, one verdict per knob, so that an operator "
         "can see which knobs earn a wire in and which stay native. The founder's order of 9 October 2026: where Omni cannot beat "
         "native, the muscle lives by itself; we only wire out of it.", "",
         "Every verdict here is computed by `tools/wiring_verdicts.py` from the test's own result file; nothing is typed in, and "
         "`verify.py` fails if this page differs from what the tables give. One row per knob and case: `results/WIRING_VERDICTS.csv` "
         f"({len(all_cases)} rows, the 1,107 modelled muscles included one by one, and the seven organisms under three loads).", "",
         "## The rule", "",
         "Every judged gauge of a table counts (rows marked \"shown, not judged\" never do). Every reading is **GAIN**, **STEADY** or "
         "**LOSS**, decided by what the gauge is for and never by the sign of its number (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): "
         "response times and failed requests are time waited, missed or failed, so a fall is GAIN; work done is GAIN when it rises; "
         "machines, energy, memory, connections, consumers and processor time are resources spent, so a fall is a cut, a GAIN, and a "
         "rise is **power given**, the price named beside what it bought. Each gauge's aim is its preregistration's; an operator whose "
         "aim differs reads the same numbers the other way. A knob reads:", "",
         "- **write**: at least one gauge GAIN across our three runs, and no LOSS and no power given. Omni holds the knob.",
         "- **watch**: no GAIN across our three runs. The knob stays native; Omni reads it and writes nothing. Where a gauge read "
         "LOSS or power given across our three runs, it is named and its cause given below. Where the runs disagree, nothing is "
         "settled and the knob stays native until it is.",
         "- **operator's choice**: GAIN, and LOSS or power given, both judged across our three runs: a trade. "
         "Both readings of the Omni index are shown where the test is in it (the resource reading, the preregistered headline, and "
         "the service reading, work and speed alone), and the side that pays is named. The operator who wants the gain and can pay "
         "the price wires in; every other operator watches.", "",
         "A modelled muscle (the 1,107 on their plants under its own load and work waiting in line, `results/realms_v5/MUSCLES_V5.csv`, "
         "engine omni-v5 at the max, the law omni-v6 carries unchanged) takes its verdict from its label by rule: a GAIN on work, speed or misses "
         "(MORE WORK, FASTER, FEWER MISSES, alone or together, on every load it ran) is write, and the energy the max took for it is power given, "
         "shown beside it and never a trade (the founder's order of 13 October); SAME AS NATIVE is watch, nothing moved beyond the noise; "
         "AT ITS LIMIT ON NATIVE is watch by design, the knob already at the top of its range on native, read and left native.", "",
         "## The count", "",
         "| Where | Knobs or cases | Write | Operator's choice | Watch |", "|---|---:|---:|---:|---:|",
         f"| Real stacks, three runs each (Kubernetes under seven demands; the pool, the consumer group, the memory ceiling, the storage-engine cache and the buffer pool, each under its untouched workloads) | {rw + rc + rwa} | {rw} | {rc} | {rwa} |",
         f"| Independent simulators, three runs each (robot arms, grids, districts, swarms; evidence class S) | {sw + sc + swa} | {sw} | {sc} | {swa} |",
         f"| The 1,107 modelled muscles, alone on their plants under two loads (evidence class S) | {mw + mc + mwa} | {mw} | {mc} | {mwa} |",
         f"| The organisms with the real cluster inside (GitHub at 10 and 100 copies; Azure at 1,000) | {ow + oc + owa} | {ow} | {oc} | {owa} |", ""]
    L += ["In words: on the real stacks Omni earns its wire in on " + f"{rw} of {rw + rc + rwa} knob-cases, trades on {rc} and watches on {rwa}. "
          f"Of the 1,107 modelled muscles, {mw} earn a wire in and {mwa} stay native: "
          f"{sum(1 for x in mus if x['label'] == AT_LIMIT)} of the {mwa} are at their limit on native (the knob already at the top of its range: "
          f"nothing to push, read and left native) and {sum(1 for x in mus if x['label'] == SAME)} read the same as native (nothing moved beyond "
          f"the noise). A knob left native costs nothing and earns nothing; it needs no wire in, and the page below says so muscle by muscle.", ""]

    # the real stacks
    L += ["## The real stacks (evidence class L: live software, three separate GitHub runs on the frozen engine)", "",
          "The reading of every judged gauge is in the test's own table (the Source column). The index columns are the two readings "
          "of `results/OMNI_INDEX.md` for that test, where it has one.", ""]
    L += ["### Real Kubernetes: one knob under seven demands", "",
          f"The knob: {K8S_KNOB}, on top of the Horizontal Pod Autoscaler (kind clusters on GitHub, ten pairs a run).", "",
          "| Demand | GAIN across our three runs | LOSS or power given across our three runs | Verdict | Index: resource | Index: service | Why | Source |", "|---|---|---|---|---:|---:|---|---|"]
    for x in [c for c in real if c["kind"] == "real knob" and "Kubernetes" in c["domain"]]:
        j = x["judged"]
        L.append(f"| {x['case']} | {esc(fmt_list(j['gain'], 12)) or 'none'} | {esc(away_cell(j)) or 'none'} | **{x['verdict']}** | "
                 f"{pct_s(x['resource_pct'])} | {pct_s(x['service_pct'])} | {esc(x['why'])} | `{x['source']}` |")
    L.append("")
    for cat, f, knob, names in WORKLOAD_STACKS:
        rows = [c for c in real if c.get("stack") == STACK_SHORT[f]]
        if not rows:
            continue
        L += [f"### {cat}", "", f"The knob: {knob}.", "",
              "| Workload | GAIN across our three runs | LOSS or power given across our three runs | Verdict | Index: resource | Index: service | Why | Source |", "|---|---|---|---|---:|---:|---|---|"]
        for x in rows:
            j = x["judged"]
            L.append(f"| {x['case']} | {esc(fmt_list(j['gain'], 12)) or 'none'} | {esc(away_cell(j)) or 'none'} | "
                     f"**{x['verdict']}**{'' if x['counted'] else ' (not counted)'} | {pct_s(x['resource_pct'])} | {pct_s(x['service_pct'])} | {esc(x['why'])} | `{x['source']}` |")
        L.append("")

    # every negative
    L += ["## Every LOSS and every power given across our three runs on a real stack, and why", "",
          "The founder's question was where the negatives are and why each is there. Every gauge that read LOSS or power given in all "
          "three of our runs on a real stack, with its cause read from the preregistration that carries the result:", ""]
    groups = collections.OrderedDict()
    for x in real:
        if not x["counted"]:
            continue
        f = x["source"].rsplit("/", 1)[-1].replace(".md", ".json")
        for cls in ("loss", "given"):
            for k, nm, rg, runs, a in x["judged"][cls]:
                w = WHY.get((f, x.get("workload", "*"), k)) or WHY.get((f, "*", k)) or "see the table"
                groups.setdefault((x.get("stack", "Kubernetes"), nm, w, cls, a), []).append((x.get("workload", x["case"]), rg, runs, x["verdict"]))
    for (stack, nm, w, cls, a), items in groups.items():
        cases = ", ".join(f"{wl} {verb(a, rg)} {magnitude(rg)}" for wl, rg, _, _ in items)
        figs = []
        for _, _, runs, _ in items:
            n0, o0 = first(runs, "native"), first(runs, "omni")
            if isinstance(n0, (int, float)) and isinstance(o0, (int, float)):
                figs.append((n0, o0))
        fig = ""
        if figs:
            ns = sorted({f"{n:.4g}" for n, _ in figs}); os_ = sorted(f"{o:.4g}" for _, o in figs)
            fig = f" ({' / '.join(ns)} → {os_[0]}{' to ' + os_[-1] if len(os_) > 1 and os_[0] != os_[-1] else ''} in run A)"
        vs = sorted({v for _, _, _, v in items})
        L.append(f"- **{stack}, {nm}: {cases}, {'LOSS' if cls == 'loss' else 'power given'}**{fig}. {w[0].upper() + w[1:]}. Verdict: **{' / '.join(vs)}**"
                 + (" on every workload named" if len(items) > 1 else "") + ".")
    if not groups:
        L.append("- none")
    losses = [nm for (_, nm, _, cls, _) in groups if cls == "loss"]
    L += ["", ("What these have in common: every one is power given, a resource spent to buy the service the knob exists for (consumers "
               "and the CPU they poll with, memory, pages, connections), each declared in advance in its preregistration as the gauge "
               "expected to rise, or found on the first counted set and disclosed. None is a LOSS: on no real stack did work inside the "
               "line, p95 or failed requests read LOSS across our three runs. " if not losses else
               f"{len(losses)} of these are a LOSS ({', '.join(sorted(set(losses)))}): each is named above with its cause, and each is a "
               "fault to find and fix, our own wiring first. The rest are power given, a resource spent to buy the service the knob exists "
               "for. ")
          + "Where the resource was given and nothing was bought (PostgreSQL's `simple_update`), the verdict is watch; where it bought "
          "service, the verdict is the operator's, and both index readings say what the trade is worth.", ""]

    # the simulators
    L += ["## The independent simulators (evidence class S: deterministic models with their own native controllers)", ""]
    for f, domain, knob, _ in SIMS:
        rows = [c for c in sim if c["domain"] == domain]
        if not rows:
            continue
        L += [f"### {domain}", "", f"The knob: {knob}.", "",
              "| Case | GAIN across our three runs | LOSS or power given across our three runs | Verdict | Why | Source |", "|---|---|---|---|---|---|"]
        for x in rows:
            j = x["judged"]
            b = esc(fmt_list(j["gain"], 12)) if j else ""
            w = esc(away_cell(j)) if j else ""
            L.append(f"| {x['case']} | {b or ('none' if j else '')} | {w or ('none' if j else '')} | **{x['verdict']}**"
                     f"{'' if x['counted'] or x['verdict'] == 'no knob' else ' (not counted)'} | {esc(x['why'])} | `{x['source']}` |")
        L.append("")
        if f == "V7_PANDAPOWER.md":
            L += ["**Why the line heating rose on four grids (power given).** " + SIM_WHY[f]["losses_up"][0].upper() + SIM_WHY[f]["losses_up"][1:] + ". "
                  + SIM_WHY[f]["taps_up"][0].upper() + SIM_WHY[f]["taps_up"][1:] + ". The verdict on those four grids is the operator's: the "
                  "loads' energy and the upstream import cut (GAIN) against the lines' heating up (power given); under constant-power loads on "
                  "1-MV-rural--1-sw, where nothing was bought, it is watch.", ""]
        if f == "V7_CITYLEARN.md":
            L += ["**Why the bill is up in the 2023 districts (power given), with the ramping and the energy not served (LOSS).** "
                  + SIM_WHY[f]["2023"][0].upper() + SIM_WHY[f]["2023"][1:] + ".", ""]

    # the 1,107 muscles
    by_label = collections.Counter(x["label"] for x in mus)
    L += ["## The 1,107 modelled muscles, alone on their plants (evidence class S)", "",
          "Every muscle's own row, with its verdict and the reason, is in `results/WIRING_VERDICTS.csv`; the labels and figures are the v5 "
          "realms table's (`results/realms_v5/REALMS_V5.md`, `results/realms_v5/MUSCLES_V5.csv`; engine omni-v5 at the max, every muscle its own "
          "card; seeds 3000 to 3009, ten paired seeds a muscle, under its own load and under work waiting in line). The label is the muscle's over "
          "every load it ran; the Why column gives each load's own.", "",
          "| Reading (the label over every load, its word first) | Muscles | Verdict |", "|---|---:|---|"]
    for lab, n in sorted(by_label.items(), key=lambda kv: -kv[1]):
        L.append(f"| {labelled(lab)} | {n} | **{v5_verdict(lab)}** |")
    L += ["", "### By knob", "", "| Knob | Muscles | Write | Watch: at its limit on native | Watch: the same as native | Of the watch, wrote nothing in any run |", "|---|---:|---:|---:|---:|---:|"]
    for knob in ("capacity", "setpoint", "power", "admission"):
        ms = [x for x in mus if x["knob"] == knob]
        c = collections.Counter(x["verdict"] for x in ms)
        lim = sum(1 for x in ms if x["label"] == AT_LIMIT); same = sum(1 for x in ms if x["label"] == SAME)
        z = sum(1 for x in ms if x["verdict"] == WATCH and x["writes"] == 0)
        L.append(f"| {knob} | {len(ms)} | {c[WRITE]} | {lim} | {same} | {z} |")
    L += ["", "### By family", "", "| Realm: family | Muscles | Write | Watch: at its limit on native | Watch: the same as native |", "|---|---:|---:|---:|---:|"]
    fams = collections.OrderedDict()
    for x in mus:
        fams.setdefault(x["domain"], []).append(x)
    for fam, ms in fams.items():
        c = collections.Counter(x["verdict"] for x in ms)
        lim = sum(1 for x in ms if x["label"] == AT_LIMIT); same = sum(1 for x in ms if x["label"] == SAME)
        L.append(f"| {fam} | {len(ms)} | {c[WRITE]} | {lim} | {same} |")
    limit = [x for x in mus if x["label"] == AT_LIMIT]
    same_as = [x for x in mus if x["label"] == SAME]
    same_wrote = [x for x in same_as if x["writes"] > 0]
    kc = collections.Counter(x["knob"] for x in limit)
    L += ["", "### Why the watch muscles are watch", "",
          f"- **{len(limit)} muscles are at their limit on native.** Native already runs the knob at the top of its range: every admission knob "
          f"lets everything in while change is permitted ({kc['admission']} admission knobs), a power knob runs the full clock or the full battery "
          f"power ({kc['power']} power knobs), and {kc['capacity'] + kc['setpoint']} capacity and setpoint knobs sit where native's own controller "
          "already has what the plant needs. There is nothing for the max to push; the knob is read and left native, STEADY by design, and no wire in "
          "is needed.",
          f"- **{len(same_as)} muscles read the same as native**: {len(same_wrote)} of them wrote and nothing moved beyond the noise on work, speed "
          f"or misses, {len(same_as) - len(same_wrote)} wrote nothing because native held the reading and the law had nothing to push. Watch, by rule; "
          "these are the room the next engine looks for a gain in, in the model gate first.", "",
          "### Power given, muscle by muscle", "",
          "The max buys work and speed; the energy it takes is **power given**, shown beside what it bought and never a trade or a loss (the "
          "founder's order of 13 October). The write muscles whose power given on their own load is the largest:", "",
          "| Muscle | Family | Knob | Reading | Misses (pp) | Work | Power given |", "|---|---|---|---|---:|---:|---:|"]
    given = []
    for x in mus:
        if x["verdict"] != WRITE:
            continue
        r = x["loads"].get("normal") or x["muscle"]
        pg = ffl(r["power_given"])
        if pg:
            given.append((pg, x, r))
    for pg, x, r in sorted(given, key=lambda t: -t[0])[:20]:
        L.append(f"| `{r['muscle']}` | {r['family']} | {r['knob']} | {labelled(r['label'])} | {ffl(r['viol_pp']):+.2f} | {100 * (ffl(r['work']) or 0):+.2f}% | {100 * pg:+.2f}% |")
    writes_total = sum(1 for x in mus if x["verdict"] == WRITE)
    L += ["", f"Of the {writes_total} write muscles, {len(given)} took power for their gain on their own load and {writes_total - len(given)} took none "
          "(the gain came from timing, not from more energy). Every muscle's figure, on both loads, is in the CSV.", ""]

    # the organisms
    L += ["## The organisms", "", "### The seven modelled organisms under three loads (every muscle written at once, one brain)", "",
          "| Organism and load | Muscles | Reading | Verdict | Figures |", "|---|---:|---|---|---|"]
    for x in org_m:
        L.append(f"| {x['domain']} | {x['case']} | {labelled(x['label'])} | **{x['verdict']}** | {esc(x['why'])} |")
    L += ["", "An organism's label is the whole's: every muscle written at once. The wiring an operator takes from this page is finer: the "
          "write muscles wired in, the watch muscles left native with one wire out. The organism result says the whole, "
          "written at once, read GAIN (fewer misses, and under the climb more work) in every organism under every load, the power given "
          "shown beside it; this page says which parts carried it.", "",
          "### The organisms with the real cluster inside", "",
          f"The knob is the cluster's ({K8S_KNOB}), under the organism's own demand, with the modelled muscles around it. The cluster's gauges "
          "decide the verdict; the organism's modelled work and energy are shown beside them and are judged muscle by muscle above.", "",
          "| Cell | Verdict | The table's reading, and the figures | Source |", "|---|---|---|---|"]
    for x in org_c:
        L.append(f"| {x['case']} ({'GitHub' if 'GitHub' in x['domain'] else 'Azure'}) | **{x['verdict']}** | {esc(x['why'])} | `{x['source']}` |")

    # not decided
    L += ["", "## Not decided here", "",
          "- **Azure's managed Kubernetes (the bill):** the two tables are on Omni v1 (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`) on a "
          "4-worker fleet, where every gauge read STEADY, no difference beyond the noise, but the burst's p99 in one run. A fleet too small to show one "
          "machine decides nothing; the fleet that can (`docs/K8S_COMPASS_PREREGISTRATION.md`, the fleet that can show one machine) decides this "
          "knob on v3 when it runs. Until then the verdict on Azure is watch, for want of a result rather than because of one.",
          "- **The card (NVIDIA, its own meter):** every earlier card result is obsolete; the current governor has not run on a real card. Nothing "
          "to decide yet.",
          "- **The 24-hour robustness machines:** running; they test the governor's own staying power, not a knob's value.", "",
          "## What this means for the wiring", "",
          "The two-way plug stays one wire in and one wire out (`docs/WIRING_GUIDE.md`). This page decides, per knob, whether the wire in is "
          "connected. A knob marked **write** is wired both ways. A knob marked **watch** is wired out only: Omni reads it, learns from it, "
          "and never writes it; the native controller lives by itself. A knob marked **operator's choice** is wired out, and in only by the "
          "operator who wants that trade. The engine's verdict (`omnicompass/verdict.py`) does the same on the muscle itself at run time, and a "
          "knob it has left native is a watch knob whatever this page says. Nothing on this page changes the engine, which stays Omni v3; it "
          "changes what an operator connects.", "",
          "## The same verdict, live: the brain decides on the knob before it writes", "",
          "This page judges after the fact, from published tables. The founder's order of 9 October is that the brain judge in real time, on "
          "the knob, before it writes, and that a knob which cannot prove it pays stay native. On the five live stacks (the pool, the consumer "
          "group, the memory ceiling, the storage-engine cache, the buffer pool) that is now built into the harnesses: `tools/knob_verdict.py` "
          "wraps the frozen engine's own verdict (`omnicompass/verdict.py`, unchanged) around every live knob. The knob starts in watch; a "
          "paired trial on the stack itself (the knob held at the deepest step already allowed, then one notch further, under the same traffic) "
          "allows one notch at a time under the declared objective, the resource reading of the index by default or the service reading at the "
          "operator's choice; a refused step is not taken and not retried for a minute; a trial holds the knob; a fail-up never spends beyond "
          "the allowance; the operator's setting is always free. The audit carries the cost sample and the verdict's state every second, the arm "
          "record sums it, and the three-run tables print the verdict per workload. It is declared as an amendment in each of the five "
          "preregistrations with the expectation written before the runs (Redis: left native under the resource objective; Kafka: allowed step by "
          "step while each consumer pays; PostgreSQL: the add above the operator's setting refused on `simple_update`; MySQL: the `read_write` "
          "chunks refused; MongoDB: the cache given back a notch a trial). The runs on it were dispatched on 10 October 2026 "
          "(`docs/RERUN_2026-10-10.md`); this page is then read again "
          "from their tables. Inside the modelled realms the organism still takes one directive for every muscle; the verdict per muscle there "
          "is the next engine, Omni v4, designed in `docs/OMNI_V4_PLAN.md` and not built.", "",
          "**Where the brain's verdict stands today, knob by knob.** Who decides, in real time, whether a knob pays before it is written, "
          "and in which directions (spend: more resource for service; give back: less resource where the service holds):", "",
          "| Where | The knob | Who decides it pays, and when | Directions tried | Engine |",
          "|---|---|---|---|---|",
          "| The five live stacks: Redis's memory ceiling, Kafka's consumers, PostgreSQL's pool, MySQL's buffer pool, MongoDB's cache | one knob each | "
          "`tools/knob_verdict.py` around the engine's verdict: the knob starts in watch; a paired trial on the stack itself before every notch, "
          "one notch a trial, under the declared objective | spend and give back, both tried; the operator's setting always free | outside the "
          "engine (Omni v3 unchanged); running since 10 October |",
          "| Kubernetes: the machines | nodes in service | the engine's verdict (`omnicompass/verdict.py`): a paired trial before a machine is taken | "
          "give back (a machine taken only when the trial shows the service holds); gas and brake on replicas and the floor by the compass law's "
          "band, no trial | Omni v3 |",
          "| The card: the clock ceiling | one 15 MHz step at a time | the engine's verdict: a paired trial per step while the service is calm; no step "
          "passing, the card runs as it does alone; the power lid stays at the operator's | give back (slower clock for the same service); the "
          "speed floor never under the card's own busy clock | Omni v3 (`omni_controller/gpu_compass.py`) |",
          "| Robot arms: the speed override; drones: the cruise | one knob each | the engine's verdict on the robot and the swarm; two of four robots "
          "left native by it | give back | Omni v3 |",
          "| Power grids: the tap; buildings: the batteries | one knob each | the compass law alone, no trial; the trades on four exporting grids and "
          "seven 2023 districts are read from the tables above as the operator's choice | the law's own push and pull | Omni v3 (a trial there is "
          "the next engine) |",
          "| The 1,107 modelled muscles | each muscle's knob | the max on every muscle, every muscle its own card; the knobs native already runs at the "
          "top of their range read and left native | the law's own push and pull | Omni v5 at the max (the law omni-v6 carries), `docs/OMNI_V5.md` |",
          "| The machine itself: the Linux kernel's frequency ceiling (`docs/CPU_POWER_PREREGISTRATION.md`) | one knob | `tools/knob_verdict.py` "
          "around the engine's verdict: every notch down tried on the machine first, under the index's reading for one machine (energy x "
          "latency / work) or energy per request inside the line | give back only (the ceiling cannot go above the top; the top always free) | "
          "outside the engine; built 10 October, waiting for a machine on the metal, no run yet |", ""]

    md = "\n".join(legal_stamp(with_own_runs(L))) + "\n"

    # the CSV
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["kind", "domain", "knob", "case", "counted", "gain_all_three", "loss_all_three", "power_given_all_three", "even_inside_the_noise",
                "runs_disagree", "verdict", "index_resource_pct", "index_service_pct", "why", "source"])
    for x in all_cases:
        j = x["judged"]
        w.writerow([x["kind"], x["domain"], x["knob"], x["case"], "yes" if x["counted"] else "no",
                    "; ".join(words(it[1], it[4], it[2]) for it in j["gain"]) if j else "",
                    "; ".join(words(it[1], it[4], it[2]) for it in j["loss"]) if j else "",
                    "; ".join(words(it[1], it[4], it[2]) for it in j["given"]) if j else "",
                    len(j["noise"]) if j else "", len(j["disagree"]) if j else "",
                    x["verdict"], "" if x["resource_pct"] is None else f"{x['resource_pct']:.2f}",
                    "" if x["service_pct"] is None else f"{x['service_pct']:.2f}", x["why"], x["source"]])
    csv_text = buf.getvalue()

    if check:
        bad = []
        if not OUT_MD.exists() or OUT_MD.read_text() != md:
            bad.append(str(OUT_MD.relative_to(ROOT)))
        if not OUT_CSV.exists() or OUT_CSV.read_text() != csv_text:
            bad.append(str(OUT_CSV.relative_to(ROOT)))
        if bad:
            print("wiring verdicts out of date (python3 tools/wiring_verdicts.py): " + ", ".join(bad))
            return 1
        print("wiring verdicts: in line with the tables")
        return 0
    OUT_MD.write_text(md)
    OUT_CSV.write_text(csv_text)
    print(f"{OUT_MD.relative_to(ROOT)}: real {rw}/{rc}/{rwa}, simulators {sw}/{sc}/{swa}, muscles {mw}/{mc}/{mwa}, cluster organisms {ow}/{oc}/{owa} "
          f"(write/operator's choice/watch); {OUT_CSV.relative_to(ROOT)}: {len(all_cases)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv[1:]))
