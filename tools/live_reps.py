# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Repeated live runs: aggregate native / watch (Omni runs, writes nothing) / omni (B) / strict (C) arms over repetitions of scripts/kind_bench.sh.
Per repetition the gauges come from pilot/bench_report.py (capture.csv, latency.csv); across repetitions this reports
means and, for each Omni arm against native, the paired mean difference with a t-based 95% interval (n repetitions).
Usage: python tools/live_reps.py DIR  (DIR holds bench-<arm>-<rep>/)  ->  DIR/LIVE_REPS.md, DIR/LIVE_REPS.json"""
import csv, json, math, re, sys

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from pilot.bench_report import gauges, latency, pod_starts
from tools.readings import word as gel_word, aim as gel_aim, receipt_key, WORK_PER  # noqa: E402  (the words every table uses)
from tools.readings import by_word, interval_by_word  # noqa: E402  (a number beside a word carries the word's sign)

SAME_REL = 1e-9          # "the same" only to nine decimal places of the value (tools/readings.py EXACT_REL; the referee's work order of 25 October)
from omnicompass.student_t import T95  # noqa: E402  (the two-sided 95% point of Student's t, any degrees of freedom)
KEYS = ["worker nodes in service, mean", "node-hours", "energy, parked workers still on at idle power (Wh)", "energy (Wh)", "response time (ms), mean", "response time (ms), 95th percentile",
        "response time (ms), 99th percentile", "time over the response line (% of samples)", "failed requests (%)", "pods with no machine to take them (unschedulable)", "time pods had no machine to take them, pod-minutes",
        "pending pods, pod-minutes", "utilisation (used / allocatable)",
        "CPU used (cores), mean", "Omni's own CPU (cores), mean", "CPU used with Omni's own (cores), mean",
        "energy per core-hour (Wh)", "HPA replicas, mean",
        "pods started", "pod start wait, total (s)", "pod start wait, mean (s)",
        "host CPU busy, the real machine under kind (%)", "host cores (the real machine under kind)",
        "batch: queue finished (s)", "batch: worker machines in service after the queue finished, mean",
        "machines billed, machine-hours", "compute bill at list price ($)",
        "work inside the response line (requests a second; the capacity test's own gauge)",
        "work per dollar of the bill (answers inside the line for each $; the cloud's judged number)",
        "second app: response time (ms), 95th percentile", "second app: response time (ms), 99th percentile",
        "second app: time over the response line (% of samples)", "second app: failed requests (%)"]
# the babysitting tax (the founder's order of 14 October): what a person on call would have had to do in each arm
ALERT = "alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line)"
COMMANDS = "settings commands the governor wrote on its own (no person touched either arm)"
AHEAD = "governor's additions decided while the service was still inside its line (% of its additions)"
KEYS[KEYS.index("failed requests (%)") + 1:KEYS.index("failed requests (%)") + 1] = [ALERT, COMMANDS, AHEAD]
BILL = {"machines billed, machine-hours", "compute bill at list price ($)"}   # a real cloud only (PLATFORM=aks)
# the work meter (LOADGEN=meter): the answers inside the line it counted, a second, and in a cloud for each dollar of the bill,
# the cloud's judged number (31 October: the bill may rise where the work rises more); both from the same run's files
WORK = "work inside the response line (requests a second; the capacity test's own gauge)"
WORK_DOLLAR = "work per dollar of the bill (answers inside the line for each $; the cloud's judged number)"
METERED_WORK = {WORK, WORK_DOLLAR}
SECOND = {k for k in KEYS if k.startswith("second app: ")}                     # the fairness test only (TWO_APP=1)
HOST = {"host CPU busy, the real machine under kind (%)", "host cores (the real machine under kind)"}   # kind only
BATCH = {"batch: queue finished (s)", "batch: worker machines in service after the queue finished, mean"}   # the batch test only
QUEUE = {"queue: job wait, submitted to its first pod running, mean (s)",
         "queue: job wait, submitted to its first pod running, 95th percentile (s)",
         "queue: job turnaround, submitted to done, mean (s)",
         "queue: jobs unfinished at the window's end"}   # the batch stream under a queueing system only (BATCH_QUEUE)
KEYS[KEYS.index("batch: worker machines in service after the queue finished, mean") + 1:KEYS.index("batch: worker machines in service after the queue finished, mean") + 1] = [
    "queue: job wait, submitted to its first pod running, mean (s)", "queue: job wait, submitted to its first pod running, 95th percentile (s)",
    "queue: job turnaround, submitted to done, mean (s)", "queue: jobs unfinished at the window's end"]
# the robustness test only (ROBUST=kill, scripts/kind_robust.sh): the same 300 s after the kill mark in both arms (120 s up to
# omni-v14; omni-v15 reads 300 s, declared in docs/ROBUSTNESS_PREREGISTRATION.md before its runs: the one tail rise of the
# omni-v11 kill test came 140 to 190 s after the kill, past the 120 s window)
ROBUST_AFTER_KILL_S = 300
ROBUST = {f"robust: time over the line in the {ROBUST_AFTER_KILL_S} s after the kill (% of samples)",
          f"robust: failed requests in the {ROBUST_AFTER_KILL_S} s after the kill (%)"}
KEYS += sorted(ROBUST)
# the machine's own meter (METER=rapl, scripts/kind_bench.sh; a machine with the processor's RAPL counters only) beside
# the declared model; and Kepler's readings of the same counters (KEPLER=1), shown beside it and never judged
METER = {"energy, the machine's own meter (Wh)"}
KEPLER = {"energy, Kepler's reading of the machine's meter (Wh)", "energy Kepler attributes to the service's pods (Wh)"}
KEYS[KEYS.index("energy (Wh)") + 1:KEYS.index("energy (Wh)") + 1] = sorted(METER) + sorted(KEPLER)
ROBUST_MEMORY_LIMIT = 1.25   # a governor whose resident memory in the last ten minutes is more than a quarter above the first ten has a leak (preregistered)
ROBUST_HANDBACK_S = 60.0     # every setting back at the operator's within this many seconds of the kill, or the repetition is marked (preregistered)


LABEL = {"energy, parked workers still on at idle power (Wh)": "energy, parked workers still on at idle power (Wh, declared model)",
         "energy (Wh)": "energy, parked workers at 25 W standby (Wh, declared model; kind never does this)",
         "energy per core-hour (Wh)": "energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged)",
         "pending pods, pod-minutes": "pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged)",
         "energy, the machine's own meter (Wh)": "energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P)",
         "energy, Kepler's reading of the machine's meter (Wh)": "energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged)",
         "energy Kepler attributes to the service's pods (Wh)": "energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged)"}
# the four ways (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6): the organism alone (nativebare), the orchestrator on it as
# shipped (native), Omni-Compass on the organism alone (compassbare) and Omni-Compass on top of the orchestrator (compass),
# all four in every repetition; each comparison is the first arm against the second, paired within the repetition
FOUR_WAYS = (("native", "nativebare", "the orchestrator as shipped vs the organism alone (what the orchestrator does on its own)"),
             ("compassbare", "nativebare", "omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator)"),
             ("compassbare", "native", "omni on the organism alone vs the orchestrator as shipped"),
             ("compass", "nativebare", "omni on top of the orchestrator vs the organism alone"))
NEUTRAL = {"CPU used (cores), mean", "utilisation (used / allocatable)", "Omni's own CPU (cores), mean",
           "CPU used with Omni's own (cores), mean", "energy per core-hour (Wh)", "pending pods, pod-minutes",
           COMMANDS, AHEAD} | HOST | KEPLER
# more or less is not judged by itself. Energy per core-hour is energy over CPU used, and CPU used is not judged, so the
# ratio is not either. A pod pending in the snapshot is waiting for a machine or is a pod the autoscaler just created and
# is starting; the judged gauge is the scheduler's own verdict that no machine would take it (amendment 10)
def sig_word(k, mean_diff):
    """The significance column's word for a difference clear of the noise: GAIN, LOSS or power given by what the gauge is
    for (tools/readings.py: every judged gauge here is time waited, missed or failed, or a resource spent); a gauge shown
    and never judged says only which way it went."""
    if k in NEUTRAL:
        return f"yes, {'up' if mean_diff > 0 else 'down'} (shown, not judged)"
    if k == WORK:
        return f"yes: {gel_word(mean_diff < 0, gel_aim('higher', k))}"
    if k == WORK_DOLLAR:
        return f"yes: {gel_word(mean_diff < 0, WORK_PER)}"
    return f"yes: {gel_word(mean_diff < 0, gel_aim('lower', k))}"


NOTE = ["**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first",
        "energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the",
        "declared standby power, which needs a node autoscaler that really removes the machine; this run has none.", ""]


def second_app(d):
    """The fairness test (TWO_APP=1): the noisy neighbour's own response time, from its own probe."""
    if not (d / "latency_noisy.csv").exists():
        return {}
    v = latency(str(d / "latency_noisy.csv"))
    return {f"second app: {k}": v[k] for k in ("response time (ms), 95th percentile", "response time (ms), 99th percentile",
                                               "time over the response line (% of samples)", "failed requests (%)") if k in v}


def bill(d):
    """The bill on a real cloud: every worker machine that exists is billed (scripts/kind_bench.sh, PLATFORM=aks),
    integrated over the measured window, priced at the cloud's list price per machine-hour (PRICE_PER_NODE_HOUR)."""
    g = {}
    if not (d / "billed_nodes.csv").exists():
        return g
    import os
    t0 = float((d / "window_start.txt").read_text().split()[0])
    t1 = float((d / "window_end.txt").read_text().split()[0]) if (d / "window_end.txt").exists() else float("inf")
    default_price = float(os.environ.get("PRICE_PER_NODE_HOUR", "0.096"))
    # a fleet of several machine families: each work pool at its own list price (POOL_PRICES="work0=0.096;work1=0.086"),
    # read from the pools column (pool=count;...) the bench writes beside the machine count; a pool without a price, or
    # a file without the column, is priced at the default
    prices = dict(kv.split("=") for kv in os.environ.get("POOL_PRICES", "").replace(",", ";").split(";") if "=" in kv)
    rows = [r for r in csv.DictReader(open(d / "billed_nodes.csv")) if r.get("machines")]
    b = [(float(r["epoch_s"]), float(r["machines"]), r.get("pools") or "") for r in rows]
    b = [x for x in b if t0 <= x[0] <= t1]
    if len(b) > 1:
        mh = sum((y[0] - x[0]) * x[1] for x, y in zip(b, b[1:])) / 3600.0
        g["machines billed, machine-hours"] = mh
        cost = 0.0
        for x, y in zip(b, b[1:]):
            dt = (y[0] - x[0]) / 3600.0
            pools = dict(kv.split("=") for kv in x[2].split(";") if "=" in kv)
            if pools:
                cost += sum(dt * float(n) * float(prices.get(p, default_price)) for p, n in pools.items())
            else:
                cost += dt * x[1] * default_price
        g["compute bill at list price ($)"] = cost
        work = meter_work(d)
        if work is not None and cost > 0:
            g[WORK_DOLLAR] = work / cost
    work = meter_work(d)
    if work is not None:
        try:
            span = (float((d / "window_end.txt").read_text().split()[0]) - t0)
            if span > 0:
                g[WORK] = work / span
        except (OSError, ValueError, IndexError):
            pass
    return g


def meter_work(d):
    """The answers inside the line the work meter counted over the window (its final count, work_meter.json; LOADGEN=meter),
    or None where the arm ran no meter."""
    f = d / "work_meter.json"
    if not f.exists():
        return None
    try:
        return float(json.loads(f.read_text().strip().splitlines()[-1])["total"]["in_time"])
    except (ValueError, KeyError, IndexError, TypeError):
        return None


def babysitting(d, slo):
    """The babysitting tax (the founder's order of 14 October): what a person on call would have had to do in each arm.
    Alert minutes: the whole minutes of the measured window whose 95th percentile response time (nearest rank, a failed
    request counted over the line) was over the line, the minutes an on-call page would be open; measured, judged (time
    missed: lower). From the governor's audit, shown and never judged: the settings commands it wrote on its own, and the
    share of its additions (a machine more, or a lower HPA target: more pods) decided while the 95th percentile it read
    was still inside the line, acting before the line was crossed. Native and the watching arm write nothing: 0 commands."""
    g = {}
    try:
        with open(d / "latency.csv") as f:
            rows = list(csv.DictReader(f))
    except OSError:
        rows = []
    mins = {}
    for r in rows:
        try:
            m = int(float(r["elapsed_seconds"]) // 60)
            v = float(r["latency_ms"]) if r.get("ok") == "1" and r.get("latency_ms") else float("inf")
        except (KeyError, ValueError):
            continue
        mins.setdefault(m, []).append(v)
    try:
        t0 = float((d / "window_start.txt").read_text().split()[0])
        t1 = float((d / "window_end.txt").read_text().split()[0])
        full = int((t1 - t0) // 60)
    except (OSError, ValueError, IndexError):
        t0, t1, full = None, None, (max(mins) if mins else 0)   # no recorded end: the last, partial minute is dropped
    if mins:
        def p95(v):
            v = sorted(v)
            return v[max(0, math.ceil(0.95 * len(v)) - 1)]
        g[ALERT] = float(sum(1 for m, v in mins.items() if m < full and p95(v) > slo))
    native = d.name.split("-")[1].startswith("native") if d.name.count("-") >= 2 else "-native-" in d.name
    audit = d / "audit.jsonl"
    if native or not audit.exists():
        g[COMMANDS] = 0.0 if native else float("nan")
        return g
    inside = (lambda t: True) if t0 is None else (lambda t: t0 <= t <= t1)
    cmds, adds, ahead, prev = 0, 0, 0, None
    recs = []
    with open(audit) as f:
        for line in f:
            try:
                recs.append(json.loads(line))
            except ValueError:
                continue                                  # a line cut off by a crash is no record
    for rec in recs:
        t = float(rec.get("time", 0.0))
        if "write" in rec and not rec.get("dry_run") and inside(t):
            cmds += 1
        dec = rec.get("decision")
        if isinstance(dec, dict):
            rho = dec.get("hpa_target_recommended")
            add = (dec.get("nodes_recommended") or 0) > (dec.get("nodes_observed") or 0) or (
                prev is not None and rho is not None and rho < prev - 1e-9)
            prev = rho if rho is not None else prev
            if add and inside(t) and dec.get("latency_p95_ms") is not None:
                adds += 1; ahead += float(dec["latency_p95_ms"]) <= slo
    g[COMMANDS] = float(cmds)
    if cmds and adds:
        g[AHEAD] = 100.0 * ahead / adds
    return g


def host_cpu(d):
    """The real machine under a kind cluster (host_cpu.csv, scripts/kind_bench.sh): its mean busy share over the measured
    window and its core count. kind's workers each report every host core as their own, so this, not "used /
    allocatable", says how full the machine doing the work was. Absent on a real cloud."""
    f = d / "host_cpu.csv"
    if not f.exists():
        return {}
    try:
        t0 = float((d / "window_start.txt").read_text().split()[0]); t1 = float((d / "window_end.txt").read_text().split()[0])
    except (OSError, ValueError, IndexError):
        return {}
    r = [x for x in csv.DictReader(open(f)) if x.get("busy") and t0 <= float(x["epoch_s"]) <= t1]
    if not r:
        return {}
    return {"host CPU busy, the real machine under kind (%)": 100.0 * sum(float(x["busy"]) for x in r) / len(r),
            "host cores (the real machine under kind)": float(r[-1]["cores"])}


def prom(path):
    """A Prometheus text file (Kepler's metrics as read at a window mark): (name, labels, value) for every sample line."""
    out = []
    with open(path) as f:
        lines = f.read().splitlines()
    for line in lines:
        m = re.match(r'^([a-zA-Z_:][a-zA-Z0-9_:]*)(?:\{(.*)\})?\s+(\S+)', line.strip())
        if not m or line.startswith("#"):
            continue
        try:
            out.append((m.group(1), dict(re.findall(r'(\w+)="((?:[^"\\]|\\.)*)"', m.group(2) or "")), float(m.group(3))))
        except ValueError:
            continue
    return out


def meter(d):
    """The machine's own meter over the measured window (rapl.csv, scripts/kind_bench.sh METER=rapl; tools/rapl.py): the
    processor's package and memory counters, sampled every 2 s from before the window opens to after it closes, read at
    the window's two marks. Kepler (KEPLER=1, scripts/kind_addons_kepler.sh): its node counter on the control plane
    (on kind every node reads the same machine) and its counters of the service's pods, from its reads at the two marks;
    a pod gone before the close takes its share with it, so the second is a floor. Absent without a meter."""
    from tools.rapl import window
    g = {}
    try:
        t0 = float((d / "window_start.txt").read_text().split()[0]); t1 = float((d / "window_end.txt").read_text().split()[0])
    except (OSError, ValueError, IndexError):
        return g
    if (d / "rapl.csv").exists():
        w = window(str(d / "rapl.csv"), t0, t1)
        if w.get("ok"):
            g["energy, the machine's own meter (Wh)"] = w["wh"]
    starts = {p.name[len("kepler_start_"):-len(".prom")]: p for p in d.glob("kepler_start_*.prom")}
    ends = {p.name[len("kepler_end_"):-len(".prom")]: p for p in d.glob("kepler_end_*.prom")}
    nodes = sorted(set(starts) & set(ends))
    if nodes:
        zones = ("package", "dram")
        node_j = lambda p: sum(v for n, l, v in prom(p) if n == "kepler_node_cpu_joules_total" and l.get("zone") in zones)
        cp = next((n for n in nodes if "control-plane" in n), nodes[0])
        g["energy, Kepler's reading of the machine's meter (Wh)"] = (node_j(ends[cp]) - node_j(starts[cp])) / 3600.0

        def pods_j(p):
            r = {}
            for n, l, v in prom(p):
                if (n == "kepler_pod_cpu_joules_total" and l.get("zone") in zones and l.get("pod_namespace") == "default"
                        and l.get("pod_name", "").startswith("php-apache-")):
                    r[(l.get("pod_id"), l.get("zone"))] = r.get((l.get("pod_id"), l.get("zone")), 0.0) + v
            return r
        tot = 0.0
        for n in nodes:
            a, b = pods_j(starts[n]), pods_j(ends[n])
            tot += sum(max(b[k] - a.get(k, 0.0), 0.0) for k in b)
        g["energy Kepler attributes to the service's pods (Wh)"] = tot / 3600.0
    return g


def batch(d):
    """The batch test (WORKLOAD=batch, scripts/kind_bench.sh): seconds from the window opening until the last job of the
    queue finished (batch_done.txt), and the worker machines in service, on average, from then to the end of the window
    (capture.csv): how fast the work was done, and what was held after it. A queue not finished in the window counts
    the whole window. Absent from every other test."""
    try:
        t0 = float((d / "window_start.txt").read_text().split()[0]); t1 = float((d / "window_end.txt").read_text().split()[0])
    except (OSError, ValueError, IndexError):
        return {}
    if not (d / "preflight.txt").exists() or "batch:" not in (d / "preflight.txt").read_text():
        return {}
    done = float((d / "batch_done.txt").read_text().split()[0]) if (d / "batch_done.txt").exists() else t1
    g = {"batch: queue finished (s)": done - t0}
    import datetime as _dt
    rows = [r for r in csv.DictReader(open(d / "capture.csv"))
            if _dt.datetime.strptime(r["timestamp"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc).timestamp() >= done]
    if rows:
        g["batch: worker machines in service after the queue finished, mean"] = sum(float(r["nodes_ready"]) for r in rows) / len(rows)
    return g


def job_stream(d):
    """The batch stream under a queueing system (BATCH_QUEUE, scripts/kind_batch_queue.sh): for every job, the seconds from
    its submission to its first pod running (the queueing system's admission and the scheduler's placement together, the
    same measure for Kueue, which holds the job, and Volcano, which holds its pods), and to its last pod done; a job not
    started or not done by the window's end counts the window's end, so an unfinished job never reads quick; and how many
    were unfinished. From jobs.json and pods.json; on KubeRay (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 7) the same
    measures of every Ray job, from ray_times.json: its submission, its first task begun (its own driver's record) and its
    end as KubeRay recorded it, a job that did not succeed counted unfinished. Absent from every other test."""
    import datetime as _dt
    ts = lambda s: _dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc).timestamp()
    try:
        t1 = float((d / "window_end.txt").read_text().split()[0])
        if (d / "ray_times.json").exists():
            rows = []   # (submitted, first started, done or None)
            for r in json.loads((d / "ray_times.json").read_text()).get("items", []):
                done = ts(r["end"]) if r.get("end") and r.get("status") == "SUCCEEDED" else None
                rows.append((ts(r["submitted"]), r["first_task"] if r.get("first_task") is not None else t1, done))
        else:
            jobs = json.loads((d / "jobs.json").read_text()).get("items", [])
            pods = json.loads((d / "pods.json").read_text()).get("items", [])
            first = {}
            for p in pods:
                job = (p.get("metadata", {}).get("labels", {}) or {}).get("job-name")
                start = (p.get("status") or {}).get("startTime")
                if job and start:
                    first[job] = min(first.get(job, float("inf")), ts(start))
            rows = []
            for j in jobs:
                st = j.get("status") or {}
                rows.append((ts(j["metadata"]["creationTimestamp"]), first.get(j["metadata"]["name"], t1),
                             ts(st["completionTime"]) if st.get("completionTime") else None))
    except (OSError, ValueError, IndexError, KeyError):
        return {}
    if not rows:
        return {}
    waits, turns, unfinished = [], [], 0
    for sub, started, done in rows:
        waits.append(min(started, t1) - sub)
        if done is not None and done <= t1:
            turns.append(done - sub)
        else:
            turns.append(t1 - sub); unfinished += 1
    waits.sort()
    p95 = waits[min(len(waits) - 1, int(math.ceil(0.95 * len(waits))) - 1)]
    return {"queue: job wait, submitted to its first pod running, mean (s)": sum(waits) / len(waits),
            "queue: job wait, submitted to its first pod running, 95th percentile (s)": p95,
            "queue: job turnaround, submitted to done, mean (s)": sum(turns) / len(turns),
            "queue: jobs unfinished at the window's end": float(unfinished)}


def robust_marks(d):
    """The robustness test's time marks (robust.log, scripts/kind_robust.sh): the kill mark (both arms), the seconds from the
    kill until every setting was back at the operator's (inf: never), whether the second governor started, the mode."""
    f = d / "robust.log"
    if not f.exists():
        return {}
    out = {}
    for line in f.read_text().splitlines():
        try:
            t, txt = line.split(" ", 1); t = float(t)
        except ValueError:
            continue
        if txt.startswith("kill"):
            out["kill_epoch"] = t
        elif txt.startswith("handed back:"):
            m = re.search(r"after (\d+) s", txt); out["handed_back_s"] = float(m.group(1)) if m else float("inf")
        elif txt.startswith("NOT handed back"):
            out["handed_back_s"] = float("inf")
        elif txt.startswith("second governor started"):
            out["second_governor"] = True
        elif txt.startswith("robust ") and len(txt.split()) > 1:
            out["mode"] = txt.split()[1].rstrip(":")
            w = re.search(r"window (\d+) s", txt)
            if w:
                out["window_s"] = float(w.group(1))
    return out


ROBUST_INTERVAL_S = 60.0       # the decision interval of the robustness runs that predate omni_interval.txt (scripts/kind_bench.sh, --interval 60); a run that
                               # carries the file (omni-v16 on) is read at its own, and its decision time from the governor's own decision_ms records,
                               # because its loop keeps its schedule and the gap between decisions no longer holds the step's time
ROBUST_DECISION_SHARE = 0.95   # fewer decisions than this share of the count the interval predicts reads INVALID (docs/ROBUSTNESS_PREREGISTRATION.md)
ROBUST_CYCLE_GROWTH = 1.5      # the governor's decision time, last hour over the first: more than half again is marked
ROBUST_LONG_MIN_S = 6840.0     # the decision-time ratio needs a span of at least 95% of the 7,200 s window, so the first and last hours do not overlap


def robust_decisions(d, window_s):
    """The long run's decision gauges from the governor's own audit (omni arm): decisions made against the count the configured
    interval predicts for the window; failed decisions (the audit's own failure records and the controller log's); the governor's
    decision time, read as the gap between consecutive decisions less the configured interval it sleeps between them, mean of the
    last hour over the first; and the reset check at the end (kill_switch.txt): every setting handed back, no record left."""
    f = d / "audit.jsonl"
    if not f.exists() or not window_s:
        return None
    try:
        interval = float((d / "omni_interval.txt").read_text().split()[0]); own = True
    except (OSError, ValueError, IndexError):
        interval, own = ROBUST_INTERVAL_S, False
    times, failed, reasons, step_ms = [], 0, [], []
    for line in open(f):
        if own and '"decision_ms"' in line:
            try:
                step_ms.append((len(times), float(json.loads(line)["decision_ms"])))
            except (ValueError, KeyError, TypeError):
                pass
        if '"decision"' in line:
            try:
                times.append(float(json.loads(line)["time"]))
            except (ValueError, KeyError, TypeError):
                pass
        if '"decision_failed"' in line:
            failed += 1
            try:
                reasons.append(str(json.loads(line)["decision_failed"])[:160])
            except (ValueError, KeyError, TypeError):
                reasons.append(line.strip()[:160])
    log = d / "controller.log"
    if log.exists():
        for l in open(log):
            if "decision failed" in l:
                failed += 1
                # "decision failed (n in a row): <exception> <the API's own words>": keep the API's words, not the command path
                r = l.split("):", 1)[-1].strip() if "):" in l else l.strip()
                r = re.sub(r"CalledProcessError\(\d+, \[.*?\]\)\s*", "", r)[:160]
                reasons.append(r)
    expected = window_s / interval
    out = {"decisions": len(times), "expected": expected, "interval_s": interval, "share": (len(times) / expected if expected else None), "failed": failed,
           "failed_reasons": sorted(set(reasons)), "decision_time_ratio": None}
    if len(times) >= 4 and times[-1] - times[0] >= ROBUST_LONG_MIN_S:
        gaps = [(b - a, a) for a, b in zip(times, times[1:])]
        t0, t1 = times[0], times[-1]
        first = [g for g, t in gaps if t <= t0 + 3600]; last = [g for g, t in gaps if t >= t1 - 3600]
        if own:
            # the step's own time, as the governor timed it: decisions whose time falls in the first and the last hour
            first = [ms / 1000.0 for i, ms in step_ms if i and times[i - 1] <= t0 + 3600]
            last = [ms / 1000.0 for i, ms in step_ms if i and times[i - 1] >= t1 - 3600]
        if first and last:
            a = max(sum(first) / len(first) - (0.0 if own else ROBUST_INTERVAL_S), 0.0)
            b = max(sum(last) / len(last) - (0.0 if own else ROBUST_INTERVAL_S), 0.0)
            out["decision_time_first_s"], out["decision_time_last_s"] = a, b
            out["decision_time_ratio"] = (b / a) if a >= 0.1 else None    # under a tenth of a second there is nothing to compare
    ks = d / "kill_switch.txt"
    if ks.exists():
        txt = ks.read_text()
        m = re.search(r"workers in service: (\d+) of (\d+)", txt)
        out["handed_back_end"] = ("restored target" in txt and bool(re.search(r"records left.*: none", txt)) and bool(m) and m.group(1) == m.group(2))
    else:
        out["handed_back_end"] = None
    return out


def robust_window(d, slo):
    """Both arms: in the ROBUST_AFTER_KILL_S after the kill mark, the share of response samples over the line or failed, and the share failed."""
    m = robust_marks(d)
    if "kill_epoch" not in m:
        return {}
    try:
        t0 = float((d / "window_start.txt").read_text().split()[0]); rows = list(csv.DictReader(open(d / "latency.csv")))
    except (OSError, ValueError, IndexError):
        return {}
    k = m["kill_epoch"]
    win = [r for r in rows if k <= t0 + float(r["elapsed_seconds"]) <= k + ROBUST_AFTER_KILL_S]
    if not win:
        return {}
    over = 100.0 * sum(1 for r in win if not (r.get("ok") == "1" and float(r["latency_ms"]) <= slo)) / len(win)
    failed = 100.0 * sum(1 for r in win if r.get("ok") != "1") / len(win)
    return {f"robust: time over the line in the {ROBUST_AFTER_KILL_S} s after the kill (% of samples)": over,
            f"robust: failed requests in the {ROBUST_AFTER_KILL_S} s after the kill (%)": failed}


def robust_memory(d):
    """The governor's resident memory (rss.csv, sampled from the process table every 15 s while a governor ran): the mean of
    the last ten minutes over the mean of the first ten."""
    f = d / "rss.csv"
    if not f.exists():
        return None
    rows = [r for r in csv.DictReader(open(f)) if r.get("rss_kb") and int(r.get("processes") or 0) > 0 and float(r["rss_kb"]) > 0]
    if len(rows) < 4:
        return None
    t = [float(r["epoch_s"]) for r in rows]; rss = [float(r["rss_kb"]) for r in rows]
    if t[-1] - t[0] < 1200:
        return None          # the first and last ten minutes must not overlap: the ratio is for the long run
    first = [v for tt, v in zip(t, rss) if tt <= t[0] + 600]; last = [v for tt, v in zip(t, rss) if tt >= t[-1] - 600]
    a, b = sum(first) / len(first), sum(last) / len(last)
    return {"first_kb": a, "last_kb": b, "ratio": b / max(a, 1.0)}


def robust_table(root, cols):
    """The robustness rows (omni arms only; native has no governor): seconds from the kill to the hand-back, whether within the
    preregistered allowance, the second governor, the watchdog's records, the governor's memory ratio, its decisions."""
    per = {}
    for d in sorted(root.glob("bench-*-*")):
        _, arm, rep = arm_rep(d)
        m = robust_marks(d)
        if not m or arm.startswith("native"):
            continue
        mem = robust_memory(d)
        decisions = sum(1 for l in open(d / "audit.jsonl") if '"decision"' in l) if (d / "audit.jsonl").exists() else None
        wd = sum(1 for l in open(d / "watchdog.log") if '"watchdog"' in l) if (d / "watchdog.log").exists() else 0
        dec = robust_decisions(d, m.get("window_s")) if m.get("mode") == "long" else None
        per.setdefault(arm, {})[rep] = {"mode": m.get("mode"), "handed_back_s": m.get("handed_back_s"), "second_governor": bool(m.get("second_governor", False)),
                                        "watchdog_records": wd, "memory": mem, "decisions": decisions, "long": dec}
    if not per:
        return [], {}
    L = ["## The robustness test: the governor killed outright, the lease, and the long run", "",
         f"In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back "
         f"from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker "
         f"and the records are at the operator's. Preregistered: within {ROBUST_HANDBACK_S:.0f} s, or the repetition is marked. A second governor "
         f"starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten "
         f"minutes over the first ten above {ROBUST_MEMORY_LIMIT} is marked a leak. The {ROBUST_AFTER_KILL_S} s after the kill mark are compared between the arms "
         "in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against "
         f"the count its {ROBUST_INTERVAL_S:.0f} s interval predicts for the window (under {ROBUST_DECISION_SHARE:.0%} reads INVALID), its failed decisions, "
         f"and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over {ROBUST_CYCLE_GROWTH} "
         "is marked); the reset check at the end says whether every setting was handed back.", "",
         "| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |",
         "|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|"]
    summary = {}
    for a, reps in per.items():
        hb = [r["handed_back_s"] for r in reps.values() if r.get("mode") == "kill"]
        hb_ok = [h is not None and h <= ROBUST_HANDBACK_S for h in hb]
        mems = [r["memory"]["ratio"] for r in reps.values() if r.get("memory")]
        finite = [h for h in hb if h is not None and h != float("inf")]
        longs = [r["long"] for r in reps.values() if r.get("long")]
        summary[a] = {"repetitions": len(reps), "kill_repetitions": len(hb), "handed_back_within_allowance_all": (all(hb_ok) if hb else None),
                      "handed_back_s_mean": (sum(finite) / len(finite) if finite else None), "handed_back_s_max": (max(hb) if hb else None),
                      "never_handed_back": sum(1 for h in hb if h == float("inf") or h is None),
                      "second_governor_all": (all(r["second_governor"] for r in reps.values() if r.get("mode") == "kill") if hb else None),
                      "memory_ratio_max": (max(mems) if mems else None), "allowance_s": ROBUST_HANDBACK_S, "memory_limit": ROBUST_MEMORY_LIMIT}
        if longs:
            shares = [x["share"] for x in longs if x.get("share") is not None]
            ratios = [x["decision_time_ratio"] for x in longs if x.get("decision_time_ratio") is not None]
            ends = [x["handed_back_end"] for x in longs if x.get("handed_back_end") is not None]
            summary[a].update({"long_repetitions": len(longs), "decisions_expected": longs[0]["expected"],
                               "decisions_share_min": (min(shares) if shares else None), "failed_decisions_total": sum(x["failed"] for x in longs),
                               "failed_reasons": sorted({r for x in longs for r in (x.get("failed_reasons") or [])}),
                               "decision_time_ratio_max": (max(ratios) if ratios else None),
                               "handed_back_end_all": (all(ends) if ends and len(ends) == len(longs) else None),
                               "decision_share_limit": ROBUST_DECISION_SHARE, "cycle_growth_limit": ROBUST_CYCLE_GROWTH})
        for rep in sorted(reps, key=lambda x: int(x) if x.isdigit() else x):
            r = reps[rep]; h = r["handed_back_s"]
            hs = "" if r.get("mode") != "kill" else ("never" if h is None or h == float("inf") else f"{h:.0f}")
            ok = "" if r.get("mode") != "kill" else ("**no**" if (h is None or h > ROBUST_HANDBACK_S) else "yes")
            sg = "" if r.get("mode") != "kill" else ("yes" if r["second_governor"] else "**no**")
            mr = "" if not r["memory"] else (f"{r['memory']['ratio']:.3f}" + ("" if r["memory"]["ratio"] <= ROBUST_MEMORY_LIMIT else " **(a leak)**"))
            lg = r.get("long") or {}
            share = "" if lg.get("share") is None else (f"{lg['share']:.1%}" + ("" if lg["share"] >= ROBUST_DECISION_SHARE else " **(INVALID)**"))
            fl = "" if not lg else (str(lg["failed"]) + ("" if lg["failed"] == 0 else " (shown: " + "; ".join(lg.get("failed_reasons") or ["no reason recorded"]) + ")"))
            dt = "" if lg.get("decision_time_ratio") is None else (f"{lg['decision_time_ratio']:.2f}" + ("" if lg["decision_time_ratio"] <= ROBUST_CYCLE_GROWTH else " **(grew past the limit)**"))
            hb_end = "" if lg.get("handed_back_end") is None else ("yes" if lg["handed_back_end"] else "**no**")
            L.append(f"| {dict(compass='omni').get(a, a)} | {rep} | {r.get('mode') or ''} | {hs} | {ok} | {sg} | {r['watchdog_records']} | {mr} | {r['decisions'] if r['decisions'] is not None else ''} | {share} | {fl} | {dt} | {hb_end} |")
    return L + [""], summary


def arm_gauges(d):
    import os
    rows = list(csv.DictReader(open(d / "capture.csv")))
    g = gauges(rows); g.update(latency(str(d / "latency.csv"))); g.update(pod_starts(d))
    g.update(host_cpu(d)); g.update(robust_window(d, float(os.environ.get("SLO_MS", 500))))
    g.update(babysitting(d, float(os.environ.get("SLO_MS", 500))))
    # the controller's own cost (its process and every command it ran; it runs beside the cluster, not in it), from its
    # audit: counted so a CPU saving in the cluster is never reported without what Omni itself spent. Native, and native
    # tuned by its operator (native40, native30, native20), run no Omni process: 0.
    own = 0.0
    native = d.name.split("-")[1].startswith("native") if d.name.count("-") >= 2 else "-native-" in d.name
    if not native and (d / "audit.jsonl").exists():
        for line in open(d / "audit.jsonl"):
            if '"overhead"' in line:
                own = float(json.loads(line)["overhead"].get("cores_mean", 0.0))
        if own == 0.0:
            own = float("nan")        # an Omni arm without its cost record: unknown, never zero
    elif not native:
        own = float("nan")
    g["Omni's own CPU (cores), mean"] = own
    g["CPU used with Omni's own (cores), mean"] = g.get("CPU used (cores), mean", float("nan")) + own
    g.update(bill(d)); g.update(second_app(d)); g.update(batch(d)); g.update(job_stream(d)); g.update(meter(d))
    return g


FAULTS = (("machine down", "machine back"), ("spike:", "spike over"), ("runaway pod started", "runaway pod removed"),
          ("probe blind", "probe back"), ("api frozen", "api back"), ("metrics down", "metrics back"))   # the last two: faults=2


def fault_windows(d, slo):
    """Per fault in this run (faults.log, scripts/kind_faults.sh): time to recover (until 30 s straight under the line,
    from the fault's start, at most 300 s) and the share of samples over the line or failed in the 300 s after it."""
    import os
    try:
        t0 = float(open(d / "window_start.txt").read().split()[0])
        rows = list(csv.DictReader(open(d / "latency.csv")))
        ev = [(float(l.split()[0]), l.split(" ", 1)[1].strip()) for l in open(d / "faults.log") if l.strip()]
    except (OSError, ValueError, IndexError):
        return {}
    smp = [(t0 + float(r["elapsed_seconds"]), r.get("ok") == "1" and float(r["latency_ms"]) <= slo) for r in rows]
    out = {}
    for start_key, _ in FAULTS:
        st = [t for t, txt in ev if txt.startswith(start_key)]
        if not st:
            continue
        s0 = st[0]
        win = [(t, good) for t, good in smp if s0 <= t <= s0 + 300]
        over = 100.0 * sum(1 for _, g in win if not g) / max(len(win), 1)
        rec, run_start = 300.0, None
        for t, g in win:
            if g:
                run_start = t if run_start is None else run_start
                if t - run_start >= 30:
                    rec = max(0.0, run_start - s0); break
            else:
                run_start = None
        out[start_key.rstrip(":")] = {"recover_s": rec, "over_pct": over}
    return out


def arm_rep(d):
    """(prefix, arm, repetition) of a bench-<arm>-<rep> folder; runs recorded before the rename name the compass arm 'bowl'."""
    pre, arm, rep = d.name.split("-", 2)
    return pre, {"bowl": "compass"}.get(arm, arm), rep


def fault_table(root, cols):
    import os
    slo = float(os.environ.get("SLO_MS", 500))
    per = {}
    for d in sorted(root.glob("bench-*-*")):
        _, arm, rep = arm_rep(d)
        w = fault_windows(d, slo)
        if w:
            per.setdefault(arm, {})[rep] = w
    if "native" not in per:
        return []
    L = ["## The fault test: the same faults at the same moments in every arm", "",
         "Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). "
         "Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired "
         "means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.", "",
         "| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |", "|---|---|---:|---:|---:|"]
    for f, _ in FAULTS:
        k = f.rstrip(":")
        for a in [c for c in cols if c in per]:
            reps = sorted(set(per[a]) & set(per["native"]))
            vals = [(per[a][r][k], per["native"][r][k]) for r in reps if k in per[a][r] and k in per["native"][r]]
            if not vals:
                continue
            rec = np.mean([v[0]["recover_s"] for v in vals]); ovr = np.mean([v[0]["over_pct"] for v in vals])
            base = np.mean([v[1]["recover_s"] for v in vals])
            ch = "" if a == "native" else (f"{(rec - base):+.0f} s" + (f" ({(rec - base) / base * 100:+.0f}%)" if base > 0 else ""))
            L.append(f"| {k} | {dict(compass='omni').get(a, a)} | {rec:.0f} | {ovr:.1f} | {ch} |")
    return L + [""]


def capacity(d, slo, over_max=5.0):
    """The capacity test (load_schedule.log rising in steps, open-loop load): for each load step, the share of response
    samples over the line or failed; the run's capacity is the highest step at which that share stays at or under
    over_max percent (and every lower step did too). Returns (capacity in load-generator replicas, per-step shares)."""
    import datetime as _dt
    try:
        t0 = float(open(d / "window_start.txt").read().split()[0])
        rows = list(csv.DictReader(open(d / "latency.csv")))
        steps = []
        day = _dt.datetime.fromtimestamp(t0, _dt.timezone.utc).date()
        for line in open(d / "load_schedule.log"):
            m = re.match(r"(\d\d):(\d\d):(\d\d) load-generator replicas -> (\d+)", line.strip())
            if m:
                t = _dt.datetime(day.year, day.month, day.day, int(m[1]), int(m[2]), int(m[3]), tzinfo=_dt.timezone.utc).timestamp()
                if t < t0 - 3600:
                    t += 86400                                  # the run crossed midnight (UTC)
                steps.append((t, int(m[4])))
    except (OSError, ValueError):
        return None, []
    rise = steps
    if steps:                                                  # a load that rises and then only falls: capacity is read
        top = max(r for _, r in steps)                         # on the way up, the fall is where machines are handed back
        k = next(i for i, (_, r) in enumerate(steps) if r == top)
        fall = steps[k:]
        if len(fall) > 1 and all(b[1] < a[1] for a, b in zip(fall, fall[1:])):
            rise, steps = steps[:k + 1], steps[:k + 2]
    if len(rise) < 3 or any(b[1] <= a[1] for a, b in zip(rise, rise[1:])):
        return None, []                                        # not a rising load: not a capacity run
    smp = [(t0 + float(r["elapsed_seconds"]), r.get("ok") == "1" and float(r["latency_ms"]) <= slo) for r in rows]
    shares, cap = [], 0
    for i, (ts, r) in enumerate(rise):
        te = steps[i + 1][0] if i + 1 < len(steps) else float("inf")
        w = [g for t, g in smp if ts + 30 <= t < te]            # 30 s for the step to settle
        sh = 100.0 * sum(1 for g in w if not g) / len(w) if w else float("nan")
        shares.append((r, sh))
    for r, sh in shares:
        if sh == sh and sh <= over_max:
            cap = r
        else:
            break
    return cap, shares


def capacity_table(root, cols):
    import os
    slo = float(os.environ.get("SLO_MS", 500)); rate = float(os.environ.get("LOAD_RATE", 6))
    per = {}
    for d in sorted(root.glob("bench-*-*")):
        _, arm, rep = arm_rep(d)
        c, sh = capacity(d, slo)
        if c is not None:
            per.setdefault(arm, {})[rep] = c
    if "native" not in per:
        return [], {}
    L = ["## The capacity test: the same machines, the load rising step by step", "",
         f"Each step adds one load generator ({rate:g} requests a second each). A run's capacity is the highest step at which "
         "no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s "
         "of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.", "",
         "| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |",
         "|---|---:|---:|---:|---:|"]
    out = {}
    nat = per["native"]
    for a in cols:
        if a not in per:
            continue
        reps = sorted(set(per[a]) & set(nat))
        if not reps:
            continue
        v = np.array([per[a][r] * rate for r in reps], float); n0 = np.array([nat[r] * rate for r in reps], float)
        m, mn = float(v.mean()), float(n0.mean())
        if a == "native":
            L.append(f"| native | {mn:.1f} |  |  | {len(reps)} |"); out[a] = {"capacity_rps": mn}; continue
        dd = v - n0; half = T95.get(len(dd) - 1, 1.96) * (dd.std(ddof=1) / math.sqrt(len(dd))) if len(dd) > 1 else float("nan")
        ch = (m - mn) / mn * 100 if mn > 0 else float("nan")
        L.append(f"| {a} | {m:.1f} | {by_word(ch, None)} | {interval_by_word(dd.mean() - half, dd.mean() + half, None, unit='')} | {len(reps)} |")
        out[a] = {"capacity_rps": m, "change_pct": ch, "ci95": [float(dd.mean() - half), float(dd.mean() + half)]}
    return L + [""], out


def engine_default_s():
    """The engine's own default decision period (omni_controller/controller.py, --interval: 60 s since omni-v17)."""
    from omni_controller.controller import parser
    return float(parser().get_default("interval"))


def main(root):
    root = Path(root); runs = {}; native_kept = {}; beats = {}
    machines_only = any((d / "machines_only.txt").exists() for d in root.glob("bench-*-*"))
    for d in sorted(root.glob("bench-*-*")):
        _, arm, rep = arm_rep(d)
        if (d / "capture.csv").exists() and not (d / "INVALID").exists():
            runs.setdefault(arm, {})[rep] = arm_gauges(d)
            try:                                              # the beat the arm ran at, as its run wrote it
                beats.setdefault(arm, set()).add(float((d / "omni_interval.txt").read_text().split()[0]))
            except (OSError, ValueError, IndexError):
                pass
            if (d / "omni_stayed_native.txt").exists():      # the governor decided at every step and wrote nothing
                native_kept.setdefault(arm, set()).add(rep)
    out = {"repetitions": {a: sorted(r) for a, r in runs.items()}, "means": {}, "paired": {}}
    out["beats"] = {a: sorted(v) for a, v in beats.items()}   # the beat each arm ran at (omni_interval.txt), for the tables
    for a, r in runs.items():
        out["means"][a] = {k: float(np.nanmean([g.get(k, np.nan) for g in r.values()])) for k in KEYS}
    cloud = any(not math.isnan(m.get("machines billed, machine-hours", float("nan"))) for m in out["means"].values())
    two = any(not math.isnan(m.get("second app: failed requests (%)", float("nan"))) for m in out["means"].values())
    host = any(not math.isnan(m.get("host cores (the real machine under kind)", float("nan"))) for m in out["means"].values())
    bat = any(not math.isnan(m.get("batch: queue finished (s)", float("nan"))) for m in out["means"].values())
    rob = any(not math.isnan(m.get(f"robust: failed requests in the {ROBUST_AFTER_KILL_S} s after the kill (%)", float("nan"))) for m in out["means"].values())
    que = any(not math.isnan(m.get("queue: jobs unfinished at the window's end", float("nan"))) for m in out["means"].values())
    keys = [k for k in KEYS if (k not in BILL or cloud) and (k not in SECOND or two) and (k not in HOST or host) and (k not in BATCH or bat) and (k not in ROBUST or rob)
            and (k not in QUEUE or que)]
    L = [f"# Repeated live runs on {'Azure Kubernetes Service (AKS), billed machines' if cloud else 'kind'} "
         "(native against omni: Omni-Compass on top of native)", "", *receipt_key(), ""]
    tuned = sorted((a for a in runs if re.fullmatch(r"native\d+", a)), key=lambda a: -int(a[6:]))
    # the decision pace: compass5 to compass120 (any compassN) are the compass arm deciding every N s; the compass arm itself
    # decides at the engine's default, its beat read from its own runs (omni_interval.txt), else from the engine
    paces = sorted((a for a in runs if re.fullmatch(r"compass\d+", a)), key=lambda a: -int(a[7:]))
    own = sorted(beats.get("compass", set()))
    beat = f"{own[0] if len(own) == 1 else engine_default_s():g}"
    cols = ([a for a in ("nativebare", "native") if a in runs] + tuned
            + [a for a in ("watch", "omni", "compassbare", "compass") if a in runs] + paces + [a for a in ("strict", "solo") if a in runs])
    names = {"native": "native", "watch": "omni, watching (writes nothing)", "omni": "omni (allocation law)", "compass": "omni", "strict": "omni alone (not on top: earlier sets only)",
             "nativebare": "the organism alone (no orchestrator)", "compassbare": "omni on the organism alone",
             "solo": "Omni-Compass by itself (no pod autoscaler; its own pod muscle)",
             **{a: f"Native tuned, HPA target {a[6:]}" for a in tuned},
             **{a: f"omni, a decision every {a[7:]} s" for a in paces}}
    L += ["## All columns, mean over repetitions", "", "| Gauge | " + " | ".join(names[a] for a in cols) + " |",
          "|---|" + "---:|" * len(cols)]
    L += [f"| {LABEL.get(k, k)} | " + " | ".join(f"{out['means'][a][k]:.4g}" for a in cols) + " |" for k in keys]
    L += [""] + (["**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;",
                  "Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the",
                  "measured window and priced at the list price per machine-hour. The energy rows remain the declared model.", ""]
                 if cloud else NOTE)
    L += ["**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert",
          "minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an",
          "on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with",
          "its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made",
          "before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.", ""]
    if any(not math.isnan(m.get("energy, the machine's own meter (Wh)", float("nan"))) for m in out["means"].values()):
        L += ["**This run carries the machine's own meter.** The processor's RAPL counters (its packages and its memory) were",
              "read every 2 s over the measured window: the energy the whole machine under the cluster drew, Omni-Compass's own",
              "process included (evidence class P). The declared-model rows stay beside it; Kepler's rows read the same counters.", ""]
    # every comparison: the arm, the arm it is read against, its key in the paired table, and its title; the four ways
    # (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6) add the organism alone, without and with Omni-Compass on top
    pairs = [(a, "native", a, None) for a in ("watch", "omni", "compass", "strict")] + [(a, b, f"{a}|{b}", t) for a, b, t in FOUR_WAYS]
    # each pace against native, and against the compass arm at its default beat, paired in the repetition
    pairs += [(a, "native", a, f"omni deciding every {a[7:]} s vs native") for a in paces]
    pairs += [(a, "compass", f"{a}|compass", f"omni deciding every {a[7:]} s vs omni at its default, every {beat} s") for a in paces]
    # Omni-Compass by itself (omni-v19, docs/SOLO_PREREGISTRATION.md): against native, and against Omni-Compass and native
    pairs += [("solo", "native", "solo", "Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native"),
              ("solo", "compass", "solo|compass", "Omni-Compass by itself vs Omni-Compass and native")]
    for a, base, key, four in pairs:
        if a not in runs or base not in runs:
            continue
        reps = sorted(set(runs[a]) & set(runs[base]))
        out["paired"][key] = {}
        title = four or {"watch": "omni, watching (dry run, writes nothing: the cost of being there)", "omni": "omni (allocation law, earlier sets)",
                 "compass": ("omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod "
                             "autoscaler moved, no processor conveyed, no power capped)") if machines_only else
                            "omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool",
                 "strict": "omni alone (not on top: earlier sets only)"}[a]
        kept = [] if four else sorted(native_kept.get(a, set()) & set(reps), key=lambda r: int(r) if str(r).isdigit() else 0)
        L += [f"## {title} vs native, {len(reps)} paired repetitions" if not four else f"## {title}, {len(reps)} paired repetitions", ""]
        if kept:
            out.setdefault("stayed_native", {})[a] = kept           # beside the paired table, never inside it
            L += [f"Omni-Compass stayed native in {len(kept)} of {len(reps)} repetitions (repetition{'s' if len(kept) > 1 else ''} "
                  f"{', '.join(str(r) for r in kept)}): its governor decided at every step, each decision in the audit with its "
                  "reasons, and made no write; those repetitions count as they ran.", ""]
        heads = (names.get(base, base), names.get(a, a)) if four else ("native", "omni")
        L += [f"| Gauge | {heads[0]} | {heads[1]} | Change | 95% interval of the difference | Significant |", "|---|---:|---:|---:|---:|---|"]
        for k in KEYS:
            d = np.array([runs[a][r].get(k, np.nan) - runs[base][r].get(k, np.nan) for r in reps], float)
            d = d[~np.isnan(d)]
            if len(d) == 0:
                continue
            nb = float(np.nanmean([runs[base][r].get(k, np.nan) for r in reps])); ob = nb + float(d.mean())
            half = T95.get(len(d) - 1, 1.96) * (d.std(ddof=1) / math.sqrt(len(d))) if len(d) > 1 else float("nan")
            sig = len(d) > 1 and (d.mean() - half > 0 or d.mean() + half < 0)
            # a change under one part in a billion of the value (nine decimal places) is rounding, not a difference: read "same" (SAME_REL)
            same = abs(d.mean()) <= SAME_REL * max(abs(nb), 1e-12)
            sig = sig and not same
            ch = (ob - nb) / abs(nb) * 100 if abs(nb) > 1e-12 else None
            out["paired"][key][k] = {"native": nb, "omni": ob, "diff": float(d.mean()), "ci95": [float(d.mean() - half), float(d.mean() + half)], "significant": bool(sig)}
            wd = 'STEADY, the same (to nine decimal places)' if same and d.mean() != 0 else sig_word(k, d.mean()) if sig else 'no'
            ch_s = by_word(ch, wd) if ch is not None else f"{by_word(ob - nb, wd, unit='', digits=3)} (native is 0)"
            L.append(f"| {LABEL.get(k, k)} | {nb:.4g} | {ob:.4g} | {ch_s} | {interval_by_word(d.mean() - half, d.mean() + half, wd, unit='', digits=4)} | "
                     f"{wd} |")
        L.append("")
    if tuned and "native" in runs and any(a in runs for a in ("omni", "compass")):
        # the cost to match: native tuned harder by its operator (a lower HPA target, more pods) against native with
        # Omni-Compass on top, at the same work; the cheapest native setting that reaches Omni-Compass's p95, and what
        # it costs over Omni-Compass
        P95, P99 = "response time (ms), 95th percentile", "response time (ms), 99th percentile"
        CPU, REP, NODES = "CPU used with Omni's own (cores), mean", "HPA replicas, mean", "worker nodes in service, mean"
        m = out["means"]
        L += ["## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top", "",
              "Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without "
              "Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the "
              "repetitions.", "",
              "| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |",
              "|---|---:|---:|---:|---:|---:|"]
        for a in cols:
            if a in ("watch", "strict"):
                continue
            L.append(f"| {names[a]} | {m[a][P95]:.4g} | {m[a][P99]:.4g} | {m[a][REP]:.4g} | {m[a][CPU]:.4g} | {m[a][NODES]:.4g} |")
        L.append("")
        out["cost_to_match"] = {}
        for o in ("compass", "omni"):
            if o not in runs:
                continue
            match = [a for a in ["native"] + tuned if m[a][P95] <= m[o][P95]]
            if not match:
                L.append(f"- {names[o]} (p95 {m[o][P95]:.4g} ms): no native setting tried reached it; the lowest native p95 "
                         f"is {min(m[a][P95] for a in ['native'] + tuned):.4g} ms ({names[min(['native'] + tuned, key=lambda a: m[a][P95])]}).")
                out["cost_to_match"][o] = None
                continue
            best = min(match, key=lambda a: m[a][CPU])
            extra = lambda k: (m[best][k] - m[o][k]) / m[o][k] * 100 if m[o][k] else float("nan")
            L.append(f"- To match {names[o]} (p95 {m[o][P95]:.4g} ms), the cheapest native setting is {names[best]} "
                     f"(p95 {m[best][P95]:.4g} ms): {by_word(extra(REP), None)} HPA replicas, {by_word(extra(CPU), None)} CPU including "
                     f"Omni-Compass's own, {extra(NODES):+.1f}% machines in service, against native with Omni-Compass on top.")
            out["cost_to_match"][o] = {"native_setting": best, "replicas_pct": extra(REP), "cpu_pct": extra(CPU), "machines_pct": extra(NODES)}
        L.append("")
    faults = fault_table(root, cols)
    if faults:
        L += faults
    cap_l, cap_o = capacity_table(root, cols)
    if cap_l:
        L += cap_l; out["capacity"] = cap_o
    rob_l, rob_o = robust_table(root, cols)
    if rob_l:
        L += rob_l; out["robust"] = rob_o
    (root / "LIVE_REPS.json").write_text(json.dumps(out, indent=1)); (root / "LIVE_REPS.md").write_text("\n".join(_legal_stamp(L)))
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1])
