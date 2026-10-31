#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The model gate: every change to the engine or a live controller runs here first, in our own models (evidence class S),
against the engine that stands, on the same seeds, before any real run is started (the founder's order of 15 October,
night). A change goes on to real runs only where it reads no LOSS here and shows promise; a LOSS here is root-caused and
fixed in the model, never carried into a real run. A reading here is a model's, never a benchmark's result.

  python3 tools/model_gate.py --base <checkout> --cand <checkout> [--seeds 1-8] [--days 1] [--models cluster,cluster15,cluster_blink,verdict]

Each checkout is a working tree: one on the engine that stands, one on the candidate. Each runs in its own process with
its own code, so the two never share a module.

  cluster    the shipped Kubernetes controller in the cloud's setting (node-pool mode, the compass law at the max, every
             muscle: the service sensed and its pod target moved, the pool parked and woken on top of the cloud's own
             autoscaler, which makes and deletes machines in every arm; the founder's order of 31 October, no hard rule,
             struck the tune-down on the machines alone of 14 October) on the model cluster of
             pilot/selfpilot.py: the fleet harness's web workload, the HPA at its target, a node's boot delay, power;
             a decision every 60 s and the fast check every 15 s. Response times come from a queue on the running pods
             (an M/M/1 delay on each pod's share, log-normal spread, the backlog's wait added). Native is the HPA with
             the Cluster Autoscaler on the same demand.
  cluster15  the same with a decision every 15 s: each rule's time at a shorter period.
  cluster_shipped  the same with each checkout at its own default decision period, as an install file that sets none
             runs it (omni-v16: 15 s, the founder's word of 22 October; every engine before it: 60 s).
  cluster_blink  the cluster model with every machine out of service in the governor's reading for two minutes every six
             hours while the cluster serves on (the kind cluster of the CruiseKube test, 18 October): a decision or a
             check that fails is recorded and skipped, as the shipped loop does.
  verdict   the do-no-harm trigger (omnicompass/verdict.py) on noisy work: how often a give-back step that truly costs
             0 to 5% more is allowed against a 2% allowance, the candidate's verdict against the standing one, at 20 and at
             200 pieces of work a decision (slow work, and work fast enough to read a 2% step in a trial's time).
  card, card_floor  the checkout's own GPU governor (omni_controller/gpu_governor.py, cap mode, its defaults) on the
             modelled card of tools/gpu_physics_sim.py, written into this file so both engines meet one model: the card
             whose voltage falls with its clock (gamma 3) and the card near its voltage floor (gamma 1.5), under Poisson
             work at 30 to 80% of capacity for 600 s; native is the card's own firmware at its start limit (omni-v15).

Gauges per seed (a day each): machine-hours, energy per used core-hour, pending-pod minutes an hour, HPA shortfall
minutes an hour, the 95th-percentile response time, alert minutes (minutes whose 95th percentile is over the line), and
the brain's request for the power cap: its moves, its reversals and its travel over the day (omni-v15; never written in
the cloud setting). The card models read the requests served and not served, the 95th and 99th percentiles, the card's
energy and peak temperature, and the power limit's writes, moves, reversals and travel in watts.
The candidate is read against the standing engine paired by seed: the mean change, its 95% interval over the seeds
(Student's t), and the word by the gauge's aim (tools/readings.py): a fall in time waited, missed or over the line is a
GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is power given; a mean change under 0.5% is STEADY, and
from 0.5% up every change reads by its aim, with whether it stands beyond the seeds' noise beside it (24 October 2026).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLO_MS = 200.0                       # the model service's line
SERVICE_MS = 20.0                    # the bare service time of one request
SAMPLES_PER_TICK = 20                # requests timed every 15 s
FINE_S, FINE_SUB = 5.0, 3            # omni-v16's pace models: a plant that moves every 5 s, three steps to one 15 s step
BLINK_EVERY, BLINK = 1440, (700, 708)  # the blink model: two minutes (8 ticks of 15 s) out of service every six hours
# after the checkout under test (a worker's PYTHONPATH), never before it: placed first, the gate's own tree shadowed the
# checkout and both arms ran the gate tree's engine (18 October; from omni-v9's gate of 17 October on). Every worker now
# names the tree its engine was imported from, and run() refuses a reading taken on the wrong one
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
try:   # the size beside a word, no sign, the raw change apart (tools/readings.py by_word); only the gate's own process formats a reading,
    from tools.readings import by_word  # noqa: E402  so a worker run against an older checkout's tools never needs it
except ImportError:
    by_word = None
try:   # the readings' table, keyed by degrees of freedom (the table it replaced was keyed by seeds and read one row early);
    from omnicompass.student_t import T95  # noqa: E402
except ImportError:   # a worker on a checkout from before omni-v9 has none, and needs none: only the parent reads
    T95 = None
# gauge -> (aim, a resource spent?)
GAUGES = {"machine_hours": ("lower", True), "kwh_per_core_hour": ("lower", True),
          "pending_pod_minutes_per_hour": ("lower", False), "hpa_shortfall_minutes_per_hour": ("lower", False),
          "p95_ms": ("lower", False), "alert_minutes": ("lower", False),
          # the brain's request for the power cap over the day (omni-v15): how often it moved, how often it turned back the
          # other way, and how far it travelled in all; wear on the part that would obey it, a resource held (a fall is a
          # cut, a rise is power given). In the cloud setting the request is never written; native asks for none
          "power_cap_moves": ("lower", True), "power_cap_reversals": ("lower", True), "power_cap_travel": ("lower", True)}


# the pace study's gauges (omni-v16): the cluster model's, and the governor's own cost: its processor time and its reads of
# the cluster an hour (resources it spends: a fall is a cut, a rise is power given)
PACE_GAUGES = {**GAUGES, "governor_cpu_s_per_hour": ("lower", True), "reads_per_hour": ("lower", True)}


def cap_wear(caps):
    """A request's wear over a run: moves (a change from one decision to the next), reversals (a move the other way from
    the move before it) and travel (the sizes of the moves, summed)."""
    moves = [b - a for a, b in zip(caps, caps[1:]) if b != a]
    return {"power_cap_moves": float(len(moves)), "power_cap_travel": float(sum(abs(m) for m in moves)),
            "power_cap_reversals": float(sum(1 for a, b in zip(moves, moves[1:]) if (a > 0) != (b > 0)))}


# ---- the worker: one arm, one seed, run inside one checkout --------------------------------------------------------
def worker(arm, seed, days, period, out, blink=False, fine=False, setting="cloud", ctl=""):
    import csv
    from unittest import mock
    import numpy as np
    from pilot.selfpilot import SimCluster, SimKube
    from pilot.score import blocks, load
    from fleet.sim import ALLOC
    import fleet.sim as fleet_sim
    from fleet.harness import BOOT_TICKS, hpa_step
    tick_s = FINE_S if fine else 15.0                          # the plant's step (omni-v16: 5 s for the pace models)
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    # a fresh audit every run: the governor appends to its audit, so a folder left by an earlier, interrupted gate would
    # carry that run's records into this one's counts (21 October: a container restart left half-written audits, and the
    # next gate appended to them)
    (out / "audit.jsonl").unlink(missing_ok=True)
    rng = np.random.default_rng(seed + 7)
    IDLE = "omnicompass.io/idle"

    class CloudSim(SimCluster):
        """The cloud as the governor meets it (scripts/kind_bench.sh, the cloud setting): the cloud's own autoscaler,
        native's machine controller, makes machines and deletes an unneeded one, in every arm. Omni-Compass on top runs at
        the max with every muscle (the founder's order of 31 October: no hard rule; the tune-down on the machines alone of
        14 October is struck); its machine lever parks a machine that exists (marked idle and drained), which the cloud
        deletes once it has stood empty for its scale-down time, and wakes a parked machine at once while it still exists.
        It asks the cloud for no machine itself: a pool the cloud's autoscaler owns refuses a count set by hand, so a
        machine is added by that autoscaler, for the pods the governor's target asks for (scripts/kind_nodepool.sh)."""
        PARK_TICKS = 40                                        # ten minutes: the autoscaler's scale-down-unneeded time

        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.c.pool.power_off = True                       # a machine the cloud scales down is deleted, not kept
            self.parked = []

        def tick(self):
            self.parked = [x - 1 for x in self.parked if x > 1]
            super().tick()

        def billed(self):
            p = self.c.pool
            return p.nodes + len(p.booting) + len(self.parked)

        def resize(self, n):
            p = self.c.pool; n = max(p.min_nodes, int(n))
            if n < p.nodes:
                k = p.nodes - n; p.nodes -= k; self.parked += [self.PARK_TICKS] * k
            elif n > p.nodes:
                k = min(n - p.nodes, len(self.parked)); p.nodes += k; self.parked = self.parked[k:]

    class FineSim(CloudSim):
        """The same cloud on a plant that moves every 5 s (omni-v16), so a decision every 10 or 5 s can be read at all: the
        day's demand held for its 15 s step, the work served and the backlog kept in the 15 s plant's units, a node's boot
        (90 s) and the autoscaler's scale-down wait (ten minutes) in time, and the HPA and the Cluster Autoscaler every
        15 s as on the 15 s plant (the HPA reads the mean of its 15 s)."""
        PARK_TICKS = CloudSim.PARK_TICKS * FINE_SUB

        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.steps *= FINE_SUB

        def tick(self):
            self.parked = [x - 1 for x in self.parked if x > 1]
            c, p, t, f = self.c, self.c.pool, self.t, 1.0 / FINE_SUB
            p.booting = [b - 1 for b in p.booting]; p.nodes += sum(1 for b in p.booting if b <= 0); p.booting = [b for b in p.booting if b > 0]
            alloc = p.nodes * p.cores * ALLOC; reqs = sum(w.replicas * w.request for w in c.workloads)
            frac = min(1.0, alloc / reqs) if reqs > 0 else 1.0; used = 0.0
            for w in c.workloads:
                capw = w.replicas * w.request * frac; dem = w.demand[min(t // FINE_SUB, len(w.demand) - 1)]
                srv = min(dem * f + w.backlog, capw * f)
                w.backlog = dem * f + w.backlog - srv; used += srv / f
                w.mhist = (getattr(w, "mhist", []) + [min(1.0, (srv / f) / max(w.replicas * w.request, 1e-9))])[-FINE_SUB:]
            c.pending, c.reqs, c.alloc, c.used = max(0.0, reqs - alloc), reqs, alloc, used
            util = min(1.0, used / max(alloc, 1e-9))
            kw = (p.nodes * (p.idle_kw + p.dyn_kw * util) + len(p.booting) * p.idle_kw) * self.scn.pue
            pending_pods = int(sum(max(0, w.replicas - int(w.replicas * frac)) for w in c.workloads))
            for w in c.workloads:
                w.current = w.replicas
            if (t + 1) % FINE_SUB == 0:
                for w in c.workloads:
                    w.metric = sum(w.mhist) / len(w.mhist)
                    hpa_step(w, w.target); w.desired = w.replicas
                if self.autoscaler == "ca":                    # a plant with fixed machines has none (StaticFineSim)
                    fleet_sim._cluster_autoscaler(c)
            self.rows.append(["", t * FINE_S, p.nodes, p.nodes + len(p.booting), int(alloc / ALLOC * 1000), int(reqs * 1000),
                              int(used * 1000), pending_pods, len(c.workloads), sum(w.current for w in c.workloads),
                              sum(w.desired for w in c.workloads), kw * 1000])
            self.t += 1

    if fine:
        fleet_sim.BOOT_TICKS = BOOT_TICKS * FINE_SUB           # a node boots in 90 s on the 5 s plant, as on the 15 s one
    class StaticSim(CloudSim):
        """The machines as the kind rig has them (scripts/kind_bench.sh: every worker made at the start, no cluster autoscaler):
        the pool stays at its starting size in every arm; the governor may park a machine (marked idle and drained, kept) and
        wake it, never add one past the pool. The arms then differ in the pods alone, as on the real rig."""

        def resize(self, n):
            p = self.c.pool; total = p.nodes + len(self.parked); n = max(p.min_nodes, min(total, int(n)))
            if n < p.nodes:
                k = p.nodes - n; p.nodes -= k; self.parked += [10 ** 9] * k      # parked and kept: never deleted
            elif n > p.nodes:
                k = min(n - p.nodes, len(self.parked)); p.nodes += k; self.parked = self.parked[k:]

    class StaticFineSim(FineSim):
        """On site, the kind rig's own machines on the 5 s plant (docs/PACE_PREREGISTRATION.md, amendment 5): every worker made at
        the start and already paid for, no cluster autoscaler, the pool at its starting size in every arm. The governor may park a
        machine (marked idle and kept, drawing its standby share of idle power, fleet/harness.py park_frac, as on the kind rig) and
        wake it, never add one past the pool. The arms then differ in the software end alone: the pods and their processor."""

        def resize(self, n):
            p = self.c.pool; total = p.nodes + len(self.parked); n = max(p.min_nodes, min(total, int(n)))
            if n < p.nodes:
                k = p.nodes - n; p.nodes -= k; self.parked += [10 ** 9] * k      # parked and kept: never deleted
            elif n > p.nodes:
                k = min(n - p.nodes, len(self.parked)); p.nodes += k; self.parked = self.parked[k:]

        def tick(self):
            super().tick()
            p = self.c.pool
            self.rows[-1][-1] += len(self.parked) * p.idle_kw * p.park_frac * self.scn.pue * 1000   # a kept machine's standby draw

    static = setting == "static"
    sim = (StaticFineSim if static and fine else StaticSim if static else FineSim if fine else CloudSim)(
        seed, days, autoscaler="none" if static else "ca")
    billed = []
    lat_path = out / "latency.csv"
    lat_rows, minute_ms, p95s = [], {}, []

    def time_requests():
        """The requests of this 15 s (of this 5 s on the 5 s plant: 7, 7 and 6 of the 15 s's 20), timed on the pods
        running now (the same queue in every arm)."""
        c = sim.c
        frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
        cap = sum(w.replicas * w.request * frac for w in c.workloads)
        ti = sim.t // FINE_SUB if fine else sim.t
        dem = sum(w.demand[min(ti, len(w.demand) - 1)] for w in c.workloads)
        backlog = sum(w.backlog for w in c.workloads)
        rho = min(0.98, dem / cap) if cap > 0 else 0.98
        mean = SERVICE_MS / (1.0 - rho) + (1000.0 * backlog / cap if cap > 0 else 1e4)
        t0 = sim.t * tick_s
        n = (7 if sim.t % FINE_SUB < 2 else 6) if fine else SAMPLES_PER_TICK
        for i in range(n):
            ms = float(mean * rng.lognormal(0.0, 0.25))
            lat_rows.append((t0 + i * tick_s / n, ms))
            minute_ms.setdefault(int(t0 // 60), []).append(ms)
        del lat_rows[:-60 * SAMPLES_PER_TICK]                  # the probe file keeps the last 15 minutes
        with open(lat_path, "w") as f:
            f.write("elapsed_seconds,latency_ms,ok\n")
            f.writelines(f"{t:.2f},{ms:.3f},1\n" for t, ms in lat_rows)

    class Kube(SimKube):
        reads = 0                                              # every read the governor made (its own cost, omni-v16)

        def get(self, *args):
            Kube.reads += 1
            if args[:2] == ("get", "nodes"):                    # in service, then parked (marked idle) until deleted
                p = self.sim.c.pool
                node = lambda i, taints: {"metadata": {"name": f"n{i}", "labels": {}},
                                          # a node's allocatable as the scheduler places pods on it (the plant's ALLOC of its
                                          # cores, fleet/sim.py), as a real cluster reports it (24 October: the model said all of
                                          # its cores, so the governor's floor counted room the plant did not place pods in)
                                          "spec": {"taints": taints}, "status": {"allocatable": {"cpu": f"{int(round(p.cores * ALLOC * 1000))}m"},
                                          "conditions": [{"type": "Ready", "status": "True"}]}}
                # the blink (omni-v11): four times a day every machine in service leaves service for two minutes in the
                # governor's reading, while the model cluster serves on, as the kind cluster of the CruiseKube test did on 18
                # October (run 39120444653, repetition 8)
                out_now = blink and BLINK[0] <= self.sim.t % BLINK_EVERY < BLINK[1]
                gone = [{"key": "node.kubernetes.io/unreachable", "effect": "NoSchedule"}] if out_now else []
                return {"items": [node(i, list(gone)) for i in range(p.nodes)]
                        + [node(p.nodes + j, [{"key": IDLE, "effect": "PreferNoSchedule"}]) for j in range(len(self.sim.parked))]}
            if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "json":
                # every running pod on a machine in service, by name, as a real cluster lists it (24 October: the model's pods
                # carried no node, so the governor's count of what the machines in service hold, which reads a running pod by
                # its node, came out 0 and every rule that reads the room saw an empty fleet)
                got = super().get(*args)
                n = max(1, self.sim.c.pool.nodes)
                for i, pod in enumerate(x for x in got["items"] if x["status"].get("phase") == "Running"):
                    pod["spec"]["nodeName"] = f"n{i % n}"
                return got
            if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "name":
                c = self.sim.c
                frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
                pend = sum(w.replicas - int(w.replicas * frac) for w in c.workloads)
                return "\n".join(f"pod/p{i}" for i in range(pend))
            if args[:2] == ("get", "hpa"):                      # the HPA as Kubernetes shows it: its range and target
                hp = super().get(*args)
                for h, w in zip(hp["items"], self.sim.c.workloads):
                    h["spec"].update({"minReplicas": int(w.min_rep), "maxReplicas": int(w.max_rep),
                                      "scaleTargetRef": {"kind": "Deployment", "name": w.name}})
                    # the pods' mean CPU over their request, as the autoscaler's status reports it (24 October: the model
                    # reported none, so every rule of the governor that reads the service's demand from it was silent)
                    h.setdefault("status", {})["currentMetrics"] = [{"type": "Resource", "resource": {
                        "name": "cpu", "current": {"averageUtilization": int(round(100 * getattr(w, "metric", 0.0)))}}}]
                return hp
            if args[:2] == ("top", "pods"):                     # the pods' own usage, as metrics-server reports it
                sel = args[args.index("-l") + 1] if "-l" in args else ""
                w = next(x for x in self.sim.c.workloads if sel == f"app={x.name}")
                c = self.sim.c; frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0; run = int(w.replicas * frac)
                per = w.metric * w.request * 1000.0 * (w.replicas / max(1, run)) if run else 0.0
                return "\n".join(f"{w.name}-{i} {int(per)}m 10Mi" for i in range(run))
            if args[:2] == ("get", "deployment"):
                w = next(x for x in self.sim.c.workloads if x.name == args[2])
                cpu = f"{int(w.request * 1000)}m"
                return {"metadata": {"name": w.name, "namespace": "default", "annotations": {}},
                        "spec": {"replicas": int(w.replicas), "selector": {"matchLabels": {"app": w.name}},
                                 "template": {"metadata": {"labels": {"app": w.name}}, "spec": {"containers": [
                                     {"name": "app", "resources": {"requests": {"cpu": cpu}, "limits": {"cpu": cpu}}}]}}},
                        "status": {"replicas": int(w.replicas), "readyReplicas": int(w.replicas)}}
            try:
                return super().get(*args)
            except ValueError:
                raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="not in the model cluster")

    if arm != "native":
        from omni_controller.controller import Controller, parser
        # the compass law at the max, every HPA sensed, in both settings: the kind benchmark's (omni-v16's pace models, as
        # ARM=compass runs it in benchmark-reps.yml) and the cloud's (the founder's order of 31 October: no hard rule; the
        # cloud's tune-down on the machines alone of 14 October, --dial save --sensed none/none --give-back-only, is struck).
        # The plants differ (CloudSim, StaticSim); the law does not
        law = ["--law", "compass", "--dial", "max"]
        p0 = parser()
        # a period of 0 is the checkout's own default (the shipped model); the fast checks come once a plant step, as
        # every model has run them (15 s on the cluster's plant, 5 s on the fine one)
        argv = ["--mode", "nodepool", *law, *(["--interval", str(period)] if period > 0 else []),
                "--floor-interval", str(tick_s), "--latency-file", str(lat_path), "--slo-ms", str(SLO_MS),
                "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "kill"), "--node-scale-cmd", "SIMSCALE {n}",
                "--min-nodes", str(sim.c.pool.min_nodes), "--max-nodes", str(sim.c.pool.nodes if static else sim.c.pool.max_nodes), "--headroom", "0.5",
                "--active-nodes-only", "--max-node-step", "1", *shlex.split(ctl)]
        p = parser()
        a = p.parse_args(argv)
        period = period if period > 0 else float(a.interval)
        k = Kube(sim, None)
        ctl = Controller(a, kube=k)
        real_run = subprocess.run

        def standin_run(cmd, *kw_a, **kw):
            if isinstance(cmd, list) and cmd and cmd[0] == "SIMSCALE":
                sim.resize(int(cmd[1])); return subprocess.CompletedProcess(cmd, 0)
            return real_run(cmd, *kw_a, **kw)
        every = max(1, int(round(period / tick_s)))
        from omni_controller import controller as shipped
        fails = 0
        import time as _time
        gov_cpu = 0.0
        with mock.patch("omni_controller.controller.subprocess.run", side_effect=standin_run):
            while sim.t < sim.steps:
                sim.tick(); sim.c.alloc = sim.c.pool.nodes * sim.c.pool.cores * ALLOC
                time_requests(); billed.append(sim.billed())
                # the shipped loop's own handling (omni_controller.controller.main): a failed decision is recorded and
                # skipped, a failed floor check recorded, and the next one comes on time
                c0 = _time.process_time()
                if sim.t % every == 0:
                    fails = shipped.safe_step(ctl, fails)
                else:
                    try:
                        ctl.floor_step()
                    except Exception as e:
                        ctl.audit({"error": "floor check: " + repr(e)[:500], "stderr": ""})
                gov_cpu += _time.process_time() - c0
    else:
        while sim.t < sim.steps:
            sim.tick(); time_requests(); billed.append(sim.billed())
    cap = out / "capture.csv"; sim.write_capture(cap)
    rows = load(str(cap))
    day = blocks(rows, 86400 * days + 60, None, None)[0]                # one block: the whole run
    hours = sum(billed) * tick_s / 3600.0                               # the bill: every machine that exists
    allm = sorted(ms for v in minute_ms.values() for ms in v)
    alert = sum(1 for v in minute_ms.values() if sorted(v)[int(0.95 * len(v))] > SLO_MS)
    res = {"machine_hours": hours, "kwh_per_core_hour": day["kwh_per_core_hour"],
           "pending_pod_minutes_per_hour": day["pending_pod_minutes_per_hour"],
           "hpa_shortfall_minutes_per_hour": day["hpa_shortfall_minutes_per_hour"],
           "p95_ms": allm[int(0.95 * len(allm))], "alert_minutes": alert,
           "power_cap_moves": 0.0, "power_cap_reversals": 0.0, "power_cap_travel": 0.0}
    if arm != "native":
        recs = [json.loads(l) for l in open(out / "audit.jsonl")]
        res.update(cap_wear([float(r["decision"]["power_cap"]) for r in recs
                             if isinstance(r.get("decision"), dict) and "power_cap" in r["decision"]]))
        ev = [r["verdict"].get("verdict", "") for r in recs if isinstance(r.get("verdict"), dict)]
        res["steps_allowed"] = sum(1 for v in ev if v == "step allowed")
        res["steps_refused"] = sum(1 for v in ev if v.startswith("step refused"))
        res["trials_abandoned"] = sum(1 for v in ev if v.startswith("trial abandoned"))
        res["machines_parked"] = sum(1 for r in recs if r.get("write", [None])[0] == "SIMSCALE")
        res["errors"] = sum(1 for r in recs if "error" in r)
        res["readings_held"] = sum(1 for r in recs if str(r.get("decision", "")).startswith("held"))
        res["decisions"] = sum(1 for r in recs if isinstance(r.get("decision"), dict))
        res["governor_cpu_s_per_hour"] = gov_cpu / (sim.steps * tick_s / 3600.0)
        res["reads_per_hour"] = Kube.reads / (sim.steps * tick_s / 3600.0)
        res["engine_tree"] = engine_tree("omni_controller.controller")
    print(json.dumps(res))


# ---- the conveyance model: one kind host, the checkout's own conveyance code ------------------------------------------
# the model host's calibration, set so the native arm sits where the v6 KEDA run's native arm did (results/live/raw/addons-run-
# 38725705826: host busy mean 0.27 and p95 0.42, response p50 91 ms and p95 248 ms, the HPA's replicas), see docs/OMNI_V7.md
CAL = {"cost_s": 0.06, "clients": 1.0, "think_s": 0.05, "other_cores": 0.55, "loadgen_s": 0.004}
CAL.update(json.loads(os.environ.get("MODEL_CAL", "{}")))        # a heavier or lighter load for one run, without a code change
CONVEY_GAUGES = {"requests_served": ("higher", False), "start_wait_s": ("lower", False), "start_wait_p95_s": ("lower", False), "p95_ms": ("lower", False),
                 "alert_minutes": ("lower", False), "host_busy": ("lower", True), "limit_given_m": ("lower", True),
                 "pod_seconds": ("lower", True), "writes": ("lower", True)}
# the batch muscle beside the serving one (omni-v13's gate, 20 October): the stream of KubeRay's rig with the organism
# alone (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 7): 24 jobs, one every 30 s, each ten pods run five at a time,
# every pod requesting 500m with a 1-core limit and hashing a fixed amount of work. BATCH_POD_CORE_S is set so the native
# arm's queue finishes where the saturated runners' did (the 16 KubeRay repetitions whose native queue ran past 760 s:
# mean 834 s, the host at its top through the stream). BATCH_INTERFERENCE is the batch pods' loss of work per processor
# second while a serving pod's quota is lifted above its operator's on a host at its top, read from those repetitions'
# own pods (hashing time 59.2 s native, 63.1 s with the quota lifted: +7.64%, so 1 - 1/1.0764 = 0.071); with the host
# not at its top the same pods read +0.30%, and the model takes none
BATCH = {"jobs": 24, "every_s": 30, "completions": 10, "parallel": 5, "req_m": 500, "lim_m": 1000, "pod_core_s": 8.1,
         "interference": 0.071, "start_lag_s": 3, "kind_cores": 3.0, "gov_cores": 0.017}
# the batch rig's host as it ran (amendment 5): the kind nodes on 3 of its 4 cores, the governor alone on the fourth (its
# own processor 0.017 cores, the table's "Omni's own CPU"); a batch pod running 2.66 s after it was made (the saturated
# repetitions' mean, rounded up to whole seconds); and the governor's reading as its sampler takes it (capacity.py): the
# host's busy share over the whole time since its previous reading, none at the first
BATCH.update(json.loads(os.environ.get("MODEL_BATCH", "{}")))
CONVEY_BATCH_GAUGES = {**CONVEY_GAUGES, "batch_queue_s": ("lower", False), "batch_turnaround_s": ("lower", False),
                       "batch_work_core_s": ("higher", False)}
# the noisy neighbour beside the serving app (omni-v23's gate, 31 October): the fairness rig's second app (deploy/kind/noisy.yaml,
# scripts/kind_bench.sh TWO_APP=1) on the same workers, 200m requested and 500m limited a pod, its own autoscaler at 50% from 1 to
# 10 pods, its own load: a probe about 0.87 requests a second throughout, and six load generators for 150 s in two of the six
# 150 s phases, which saturate it (its probe requests time out at 10 s in both arms of every repetition). Set from the three
# omni-v21 fairness runs' own files (docs/LOSS_CAUSES_2026-10-31.md, section 4): while a serving pod on the neighbour's node
# stands above the operator's limit, the neighbour's mean response is 3.7% longer at the same host busy share and the same
# phase (167.8 against 161.8 ms over 8,949 requests in the quiet band): the kernel's run queue under a lifted quota.
NEIGHBOUR = {"req_m": 200, "lim_m": 500, "target": 0.5, "min": 1, "max": 10, "cost_s": 0.03, "probe_rps": 0.87, "surge_rps": 60.0,
             "steps": (0, 0, 1, 0, 1, 0), "interference": 0.037, "timeout_ms": 10000.0}
NEIGHBOUR.update(json.loads(os.environ.get("MODEL_NEIGHBOUR", "{}")))
CONVEY_NEIGHBOUR_GAUGES = {**CONVEY_GAUGES, "neighbour_mean_ms": ("lower", False), "neighbour_p95_ms": ("lower", False),
                           "neighbour_failed_pct": ("lower", False), "neighbour_served": ("higher", False)}


def water_fill(avail, wants, weights):
    """The kernel's fair share between cgroups under contention: each gets min(its want, weight x level), the level set
    so the shares sum to what is available; with room for every want, each gets its want."""
    if sum(wants) <= avail:
        return list(wants)
    lo, hi = 0.0, max((w / max(g, 1e-9) for w, g in zip(wants, weights)), default=0.0)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if sum(min(w, g * mid) for w, g in zip(wants, weights)) > avail:
            hi = mid
        else:
            lo = mid
    return [min(w, g * lo) for w, g in zip(wants, weights)]


def start_time(busy):
    """Seconds a pod takes to start on the host at this busy share, fitted to the v6 KEDA table's own 151 pod starts
    (results/live/V6_KEDA_REQUESTS.md): about 8 s to half busy, 9.5 s at three quarters, 12.4 s near the top."""
    if busy <= 0.5:
        return 8.0
    if busy <= 0.75:
        return 8.0 + 6.0 * (busy - 0.5)
    return 9.5 + 11.6 * (min(busy, 1.0) - 0.75)


def worker_convey(arm, seed, out, quota="none", batch=False, neighbour=False):
    """A 4-core host carrying three kind nodes (each reports the host's 4 cores as its own); php-apache (200m request,
    500m limit) under an HPA at 50%, minimum 1, maximum 10, five minutes' scale-down window; load generators stepping
    1 2 3 1 2 1 every 150 s, each two closed-loop clients (a client sends its next request when the last one is answered,
    after half a second), 30 ms of CPU a request, so faster answers bring more requests, as on kind, and the HPA sits at
    one to three pods as the v6 KEDA run did (three serving pods at its peak); a starting pod uses 300m and starts at the
    pace the host's busy share allows. Native keeps the operator's limit; the omni arms call the checkout's own
    Muscles.convey every 15 s, as the governor's fast check does.

    With batch, the batch muscle of KubeRay's rig runs beside it (BATCH above): its pods are placed where the nodes'
    requests leave room, and the host's processor is shared as the kernel shares it between cgroups, each pod its want
    up to its own limit, by the weight of its request, when the wants exceed the host (water_fill); a serving pod's
    limit lifted above its operator's on a host at its top costs the batch pods BATCH_INTERFERENCE of their work.

    With neighbour, the fairness rig's second app runs beside it (NEIGHBOUR above): its pods placed where the fewest pods are,
    the host's processor shared as the kernel shares it (water_fill, by the weight of each pod's request), its own autoscaler
    and its own load (a probe throughout, and a surge that saturates it in two phases of six); while a serving pod on a
    neighbour pod's node stands above the operator's limit, the neighbour's service time is NEIGHBOUR['interference'] longer."""
    import random
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed * 101 + 3)
    HOST, REQ_M, LIM_M, COST = 4.0, 200, 500, CAL["cost_s"]
    nodes = ["w0", "w1", "w2"]
    pods, ann, nid, busy = [], {}, [0], 0.3
    bpods, jobs, bid, win = [], [], [0], []                            # the batch muscle and the busy since the last reading (batch only)
    writes = [0]                                                       # every settings command the governor sent, refused ones included
    npods, nnid, nlat, n_desired_hist, n_starts, use_now = [], [0], [], [], [], {}   # the neighbour (neighbour only)
    nbacklog, nr_prev, n_served, n_pod_s = 0.0, 0.15, 0.0, 0.0

    def new_pod():
        counts = {n: sum(1 for p in pods if p["node"] == n) + sum(1 for p in npods if p["node"] == n) for n in nodes}
        nid[0] += 1
        pods.append({"name": f"php-{nid[0]}", "node": min(nodes, key=lambda n: counts[n]), "limit": LIM_M,
                     "progress": 0.0, "ready": False, "born": t})

    def new_npod():
        counts = {n: sum(1 for p in pods if p["node"] == n) + sum(1 for p in npods if p["node"] == n) for n in nodes}
        nnid[0] += 1
        npods.append({"name": f"php-noisy-{nnid[0]}", "node": min(nodes, key=lambda n: counts[n]), "limit": NEIGHBOUR["lim_m"],
                      "progress": 0.0, "ready": False, "born": t})

    class Kube:
        audit = None

        def get(self, *args):
            if args[:2] == ("get", "nodes"):
                return {"items": [{"metadata": {"name": n, "labels": {}}, "spec": {"providerID": f"kind://docker/kind/{n}"},
                                   "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}
                                  for n in nodes]}
            if args[:2] == ("get", "pods"):
                items = [{"metadata": {"name": p["name"], "namespace": "default", "labels": {"run": "php-apache"}},
                          "spec": {"nodeName": p["node"], "containers": [{"name": "php", "resources": {
                              "requests": {"cpu": f"{REQ_M}m"}, "limits": {"cpu": f"{p['limit']}m"}}}]},
                          "status": {"phase": "Running", "conditions": [{"type": "Ready", "status": "True" if p["ready"] else "False"}]}}
                         for p in pods]
                items += [{"metadata": {"name": f"sys-{n}", "namespace": "kube-system", "labels": {}},
                           "spec": {"nodeName": n, "containers": [{"name": "s", "resources": {"requests": {"cpu": "100m"}}}]},
                           "status": {"phase": "Running", "conditions": [{"type": "Ready", "status": "True"}]}} for n in nodes]
                # a batch pod is Pending, not ready, until its container runs (start_lag_s, the rig's own pod start), as the
                # cluster lists it; the model listed it Running from its creation until 21 October
                items += [{"metadata": {"name": b["name"], "namespace": "default", "labels": {"app": "omni-batch-stream"}},
                           "spec": {"nodeName": b["node"], "containers": [{"name": "work", "resources": {
                               "requests": {"cpu": f"{BATCH['req_m']}m"}, "limits": {"cpu": f"{BATCH['lim_m']}m"}}}]},
                           "status": {"phase": "Running" if b["runs"] <= t else "Pending", "conditions": [
                               {"type": "Ready", "status": "True" if b["runs"] <= t else "False"}]}} for b in bpods]
                items += [{"metadata": {"name": p["name"], "namespace": "default", "labels": {"run": "php-noisy"}},
                           "spec": {"nodeName": p["node"], "containers": [{"name": "php", "resources": {
                               "requests": {"cpu": f"{NEIGHBOUR['req_m']}m"}, "limits": {"cpu": f"{NEIGHBOUR['lim_m']}m"}}}]},
                           "status": {"phase": "Running", "conditions": [{"type": "Ready", "status": "True" if p["ready"] else "False"}]}}
                          for p in npods]
                return {"items": items}
            if args[:2] == ("top", "pods"):                            # metrics-server's reading of every pod, as kubectl top prints it
                return "\n".join(f"default {n} {u}m 10Mi" for n, u in use_now.items())
            if args[:2] == ("get", "deployment"):
                return {"metadata": {"name": "php-apache", "namespace": "default", "annotations": dict(ann)},
                        "spec": {"replicas": len(pods), "selector": {"matchLabels": {"run": "php-apache"}},
                                 "template": {"spec": {"containers": [{"name": "php", "resources": {
                                     "requests": {"cpu": f"{REQ_M}m"}, "limits": {"cpu": f"{LIM_M}m"}}}]}}}}
            if args[:2] == ("get", "resourcequota"):
                if quota in ("unreadable", "refused"):               # the governor's role cannot list quotas (every kind test)
                    raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="resourcequotas is forbidden")
                return {"items": []}
            raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="not in the model host")

        def write(self, args, why):
            writes[0] += 1
            if quota == "refused" and args[0] == "patch" and "resize" in args \
                    and int(str(json.loads(args[args.index("-p") + 1])[0]["value"]).rstrip("m")) > LIM_M:
                # the capacity test's namespace: a quota at the operator's limits, which the governor cannot read; admission
                # refuses every raise above it (exceeded quota: omni-cap), as on the omni-v11 capacity runs
                raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="pods is forbidden: exceeded quota: omni-cap")
            if args[0] == "annotate":
                k, _, v = args[-1].partition("="); ann[k] = v
            elif args[0] == "patch" and "resize" in args:
                val = json.loads(args[args.index("-p") + 1])[0]["value"]
                for p in pods:
                    if p["name"] == args[2]:
                        p["limit"] = int(str(val).rstrip("m"))

    m = None
    if arm != "native":
        from omni_controller.controller import parser
        from omni_controller.muscles import Muscles
        a = parser().parse_args(["--cap-deployments", "default/php-apache", "--audit", "", "--mode", "nodepool"])
        held = []
        m = Muscles(Kube(), a, lambda r: held.append(r) or r)

        class Sampler:
            def sample(self):
                if not batch:
                    return busy
                if not hasattr(self, "seen"):           # the governor's sampler: two readings make one share
                    self.seen = True; win.clear(); return None
                share = sum(win) / len(win) if win else None
                win.clear()
                return share
        m.host_cpu = Sampler()
    t = 0
    new_pod(); pods[0]["ready"] = True; pods[0]["progress"] = 1.0
    if neighbour:
        new_npod(); npods[0]["ready"] = True; npods[0]["progress"] = 1.0
    desired_hist, starts, lat, minute_ms, backlog = [], [], [], {}, 0.0
    busy_sum, limit_sum, pod_s, served, r_prev, busy_hist = 0.0, 0.0, 0.0, 0.0, 0.15, []
    steps = [1, 2, 3, 1, 2, 1] * 4
    for t in range(len(steps) * 150):
        # each load generator: 20 requests in a row, then 0 to 2 s of sleep (deploy/kind/loadgen.yaml), one request at a time
        lam = steps[t // 150] * CAL["clients"] / (min(r_prev, 5.0) + CAL["think_s"]) * (1.0 + 0.03 * rng.gauss(0, 1))
        demand = lam * COST                                            # cores the requests ask for
        ready = [p for p in pods if p["ready"]]; boot = [p for p in pods if not p["ready"]]
        other = CAL["other_cores"] + lam * CAL["loadgen_s"]            # control plane, KEDA, system pods, governor; the load generators
        start_use = 0.3 * len(boot)
        if batch:
            # the stream: a job every 30 s; its pods placed on the node whose requests leave the most room, five at a time
            if t % BATCH["every_s"] == 0 and len(jobs) < BATCH["jobs"]:
                jobs.append({"arrive": t, "made": 0, "done": 0, "end": None})
            req_on = {n: 100 + REQ_M * sum(1 for p in pods if p["node"] == n)
                      + BATCH["req_m"] * sum(1 for b in bpods if b["node"] == n) for n in nodes}
            for j in jobs:
                while j["end"] is None and j["made"] < BATCH["completions"] \
                        and sum(1 for b in bpods if b["job"] is j) < BATCH["parallel"]:
                    n = min(nodes, key=lambda x: req_on[x])
                    if 4000 - req_on[n] < BATCH["req_m"]:
                        break
                    bid[0] += 1; j["made"] += 1; req_on[n] += BATCH["req_m"]
                    bpods.append({"name": f"batch-{bid[0]}", "node": n, "left": BATCH["pod_core_s"], "job": j,
                                  "runs": t + BATCH["start_lag_s"]})
            run_b = [b for b in bpods if b["runs"] <= t]
            avail = max(0.05, BATCH["kind_cores"] - other - start_use)
            weights = [REQ_M / 1000.0] * len(ready) + [BATCH["req_m"] / 1000.0] * len(run_b)
            blim = [BATCH["lim_m"] / 1000.0] * len(run_b)
            # what each serving pod could have at this level (its whole limit wanted), and what it takes of its demand
            caps = water_fill(avail, [p["limit"] / 1000.0 for p in ready] + blim, weights)[:len(ready)]
            give = water_fill(avail, [min(c, demand / max(1, len(ready))) for c in caps] + blim, weights)
            used = sum(give[:len(ready)])
            busy = min(1.0, (other + start_use + used + sum(give[len(ready):]) + (BATCH["gov_cores"] if m else 0.0)) / HOST)
            win.append(busy)
            eff = 1.0 - (BATCH["interference"] if busy >= 0.75 and any(p["limit"] > LIM_M for p in ready) else 0.0)
            for b, g in zip(run_b, give[len(ready):]):
                b["left"] -= g * eff
                if b["left"] <= 0:
                    bpods.remove(b); b["job"]["done"] += 1
                    if b["job"]["done"] >= BATCH["completions"]:
                        b["job"]["end"] = t + 1
            cap_total = max(1e-6, sum(caps))
        elif neighbour:
            # the neighbour's pods, its load (the probe, and the surge in its phases), and the host shared by the kernel's rule
            n_ready = [p for p in npods if p["ready"]]; n_boot = [p for p in npods if not p["ready"]]
            start_use += 0.3 * len(n_boot)
            lam_n = NEIGHBOUR["probe_rps"] + (NEIGHBOUR["surge_rps"] if NEIGHBOUR["steps"][(t // 150) % len(NEIGHBOUR["steps"])] else 0.0)
            lam_n *= 1.0 + 0.03 * rng.gauss(0, 1)
            demand_n = lam_n * NEIGHBOUR["cost_s"]
            avail = max(0.05, HOST - other - start_use)
            weights = [REQ_M / 1000.0] * len(ready) + [NEIGHBOUR["req_m"] / 1000.0] * len(n_ready)
            want_php = [min(p["limit"] / 1000.0, demand / max(1, len(ready))) for p in ready]
            want_n = [min(p["limit"] / 1000.0, demand_n / max(1, len(n_ready))) for p in n_ready]
            give = water_fill(avail, want_php + want_n, weights)
            used = sum(give[:len(ready)]); used_n = sum(give[len(ready):])
            busy = min(1.0, (other + start_use + used + used_n + (BATCH["gov_cores"] if m else 0.0)) / HOST)
            # each app's capacity: what its pods could have, up to their limits, beside the other app's actual wants
            caps = water_fill(avail, [p["limit"] / 1000.0 for p in ready] + want_n, weights)[:len(ready)]
            cap_total = max(1e-6, sum(caps))
            cap_n = max(1e-6, sum(water_fill(avail, want_php + [p["limit"] / 1000.0 for p in n_ready], weights)[len(ready):]))
            # while a serving pod on the neighbour pod's node stands above the operator's limit, its service time is longer
            lifted = {p["node"] for p in ready if p["limit"] > LIM_M}
            infl = [1.0 + NEIGHBOUR["interference"] if p["node"] in lifted else 1.0 for p in n_ready]
            svc_n = NEIGHBOUR["cost_s"] / max(1e-6, min(1.0, cap_n / max(1, len(n_ready)))) * (sum(infl) / len(infl) if infl else 1.0)
            rho_n = demand_n / cap_n
            nbacklog = max(0.0, nbacklog + (demand_n - cap_n))
            mean_ms_n = 1000.0 * (svc_n / (1.0 - min(0.98, rho_n)) + nbacklog / cap_n)
            nr_prev = mean_ms_n / 1000.0; n_served += lam_n
            for _ in range(5):
                nlat.append(mean_ms_n * rng.lognormvariate(0.0, 0.3))
            use_now = {p["name"]: int(1000.0 * g) for p, g in zip(ready + n_ready, give)}
            for p in n_boot:
                p["progress"] += 8.0 / start_time(busy) / 8.0
                if p["progress"] >= 1.0:
                    p["ready"] = True; n_starts.append(t - p["born"] + 1)
            if t % 15 == 0:                                             # the neighbour's own autoscaler, on its ready pods' CPU
                util_n = (used_n / max(1, len(n_ready))) / (NEIGHBOUR["req_m"] / 1000.0) if n_ready else 0.0
                d_n = max(NEIGHBOUR["min"], min(NEIGHBOUR["max"], math.ceil(len(n_ready) * util_n / NEIGHBOUR["target"]))) if n_ready else len(npods)
                n_desired_hist = [x for x in n_desired_hist if x[0] > t - 300] + [(t, d_n)]
                target_n = max(x[1] for x in n_desired_hist) if d_n < len(npods) else d_n
                while len(npods) < target_n:
                    new_npod()
                while len(npods) > target_n and len(npods) > NEIGHBOUR["min"]:
                    npods.remove(max(npods, key=lambda p: p["born"]))
            n_pod_s += len(npods)
        else:
            want = [min(p["limit"] / 1000.0, demand / max(1, len(ready))) for p in ready]
            avail = max(0.05, HOST - other - start_use)
            scale = min(1.0, avail / sum(want)) if want and sum(want) > 0 else 1.0
            caps = [min(p["limit"] / 1000.0, avail / max(1, len(ready))) if scale < 1.0 else p["limit"] / 1000.0 for p in ready]
            used = sum(w * scale for w in want)
            busy = min(1.0, (other + start_use + used) / HOST)
            cap_total = max(1e-6, sum(min(c, avail) for c in caps))
        rho = demand / cap_total
        backlog = max(0.0, backlog + (demand - cap_total))
        svc = COST / max(1e-6, min(1.0, cap_total / max(1, len(ready))))
        mean_ms = 1000.0 * (svc / (1.0 - min(0.98, rho)) + backlog / cap_total)
        r_prev = mean_ms / 1000.0; served += lam
        for _ in range(5):
            ms = mean_ms * rng.lognormvariate(0.0, 0.3)
            lat.append(ms); minute_ms.setdefault(t // 60, []).append(ms)
        for p in boot:                                                  # starts advance at the host's pace
            p["progress"] += 8.0 / start_time(busy) / 8.0
            if p["progress"] >= 1.0:
                p["ready"] = True; starts.append(t - p["born"] + 1)
        if t % 15 == 0:                                                 # the HPA, every 15 s, on the ready pods' CPU
            util = (used / max(1, len(ready))) / (REQ_M / 1000.0) if ready else 0.0
            d = max(1, min(10, math.ceil(len(ready) * util / 0.5))) if ready else len(pods)
            desired_hist = [x for x in desired_hist if x[0] > t - 300] + [(t, d)]
            target = max(x[1] for x in desired_hist) if d < len(pods) else d
            while len(pods) < target:
                new_pod()
            while len(pods) > target and len(pods) > 1:
                pods.remove(max(pods, key=lambda p: p["born"]))
            if m is not None:
                m.convey()
        busy_sum += busy; limit_sum += sum(p["limit"] for p in pods); pod_s += len(pods); busy_hist.append(busy)
    lat.sort(); st = sorted(starts)
    res = {"start_wait_s": sum(st) / len(st) if st else 0.0, "start_wait_p95_s": st[int(0.95 * len(st))] if st else 0.0,
           "p95_ms": lat[int(0.95 * len(lat))], "alert_minutes": sum(1 for v in minute_ms.values() if sorted(v)[int(0.95 * len(v))] > 500.0),
           "host_busy": busy_sum / (t + 1), "limit_given_m": limit_sum / (t + 1), "pod_seconds": pod_s,
           "requests_served": served, "starts": len(st), "busy_p95": sorted(busy_hist)[int(0.95 * len(busy_hist))],
           "pods_mean": pod_s / (t + 1), "writes": writes[0],
           "starts_past_75": sum(1 for b in busy_hist if b >= 0.75)}
    if batch:
        ends = [j["end"] if j["end"] is not None else t + 1 for j in jobs]
        res["batch_queue_s"] = float(max(ends)) if ends else 0.0
        res["batch_turnaround_s"] = sum(e - j["arrive"] for j, e in zip(jobs, ends)) / len(jobs) if jobs else 0.0
        res["batch_work_core_s"] = BATCH["pod_core_s"] * sum(j["done"] for j in jobs)
    if neighbour:
        nl = sorted(nlat)
        res["neighbour_mean_ms"] = sum(nl) / len(nl) if nl else 0.0
        res["neighbour_p95_ms"] = nl[int(0.95 * len(nl))] if nl else 0.0
        res["neighbour_failed_pct"] = 100.0 * sum(1 for v in nl if v > NEIGHBOUR["timeout_ms"]) / len(nl) if nl else 0.0
        res["neighbour_served"] = n_served
        res["neighbour_pods_mean"] = n_pod_s / (t + 1)
        res["neighbour_starts"] = len(n_starts)
    if arm != "native":
        res["engine_tree"] = engine_tree("omni_controller.muscles")
    print(json.dumps(res))


# ---- the verdict model: the trigger alone on noisy work, in one checkout ---------------------------------------------
# ---- the card model: the checkout's own GPU governor on a modelled card -----------------------------------------------
# the card of tools/gpu_physics_sim.py, written here so both engines meet one model: idle draw 40 W; busy draw
# 80 + 220 s^gamma W at speed s (1 = full clock, 300 W, the start limit); a power limit under 300 W slows the card to the
# speed whose draw is the limit, as real cards do by lowering their clocks; heat first order toward 30 C + 0.12 C/W x draw
# with a 20 s time constant. gamma 3: voltage falls with the clock (capping cheap in speed); gamma 1.5: the card near its
# voltage floor (capping dear). The work: Poisson arrivals at 30, 60, 80, 30, 60, 30% of full-speed capacity, 100 s each,
# one server first come first served, 50 ms a request at full speed, 600 s and a 30 s drain, the response line ten service
# times (500 ms). The governor is omni_controller/gpu_governor.py at its command-line defaults (cap mode, a decision every
# 2 s), reading the modelled card as it reads nvidia-smi and the response-time file as on hardware; native is the card's own
# firmware at the start limit. A reading here is a model's (class S): the hardware answer is scripts/gpu_paired.sh
CARD = {"start_w": 300.0, "min_w": 100.0, "idle_w": 40.0, "static_w": 80.0, "demand_w": 300.0, "service_ms": 50.0, "slo_ms": 500.0,
        "phases": (0.3, 0.6, 0.8, 0.3, 0.6, 0.3), "duration_s": 600, "drain_s": 30}
CARD_GAUGES = {"requests_served": ("higher", False), "requests_not_served": ("lower", False), "p95_ms": ("lower", False),
               "p99_ms": ("lower", False), "gpu_energy_j": ("lower", True), "peak_temp_c": ("lower", True),
               "limit_writes": ("lower", True), "limit_moves": ("lower", True), "limit_reversals": ("lower", True),
               "limit_travel_w": ("lower", True)}
CARD_SMI = '''#!/usr/bin/env python3
import json, os, sys
p = os.environ["PHYS_STATE"]; st = json.load(open(p)); a = sys.argv[1:]
if "-pl" in a:
    st["limit"] = float(a[a.index("-pl") + 1]); json.dump(st, open(p, "w")); print("ok"); sys.exit(0)
f = [x for x in a if x.startswith("--query-gpu=")][0].split("=", 1)[1].split(",")
if any("reasons" in x for x in f): sys.exit(2)
v = {"index": 0, "power.draw": st["draw"], "temperature.gpu": st["temp"], "utilization.gpu": round(100 * st["util"]),
     "power.limit": st["limit"], "power.min_limit": %s, "clocks.sm": round(1800 * st["speed"]),
     "enforced.power.limit": st["limit"], "power.management": "Enabled", "persistence_mode": "Enabled",
     "power.default_limit": 300, "power.max_limit": 300}
print(", ".join(str(v[x]) for x in f))
''' % CARD["min_w"]


def worker_card(arm, seed, gamma, out):
    """One arm of the card model on one seed: native (the start limit throughout) or the checkout's governor in cap mode."""
    import random
    import statistics
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    (out / "audit.jsonl").unlink(missing_ok=True)
    C = CARD
    speed_at = lambda limit: 1.0 if limit >= C["demand_w"] else max(0.05, (limit - C["static_w"]) / (C["demand_w"] - C["static_w"])) ** (1.0 / gamma)
    busy_power = lambda s: C["static_w"] + (C["demand_w"] - C["static_w"]) * s ** gamma
    rng = random.Random(seed); arr = []; per = C["duration_s"] / len(C["phases"])
    for i, share in enumerate(C["phases"]):
        rate = share / (C["service_ms"] / 1000.0); t = i * per
        while True:
            t += rng.expovariate(rate)
            if t >= (i + 1) * per:
                break
            arr.append(t)
    smi, state, lat = out / "smi.py", out / "state.json", out / "latency.csv"
    smi.write_text(CARD_SMI); smi.chmod(0o755)
    state.write_text(json.dumps({"limit": C["start_w"], "draw": C["idle_w"], "temp": 35.0, "util": 0.0, "speed": 1.0}))
    lat.write_text("elapsed_seconds,latency_ms,ok\n")
    os.environ["PHYS_STATE"] = str(state)
    gov = None
    if arm != "native":
        from omni_controller.gpu_governor import GpuGovernor, parser as gov_parser
        a = gov_parser().parse_args(["--mode", "cap", "--smi", str(smi), "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "no-kill"),
                                     "--latency-file", str(lat), "--slo-ms", str(C["slo_ms"])])
        gov = GpuGovernor(a); every = max(1, int(round(a.interval)))
    ai = 0; queue = []; energy = 0.0; temp = 35.0; lats = []; limits = []; peak = 0.0
    for sec in range(C["duration_s"] + C["drain_s"]):
        st = json.loads(state.read_text()); limit = st["limit"]; limits.append(limit)
        s = speed_at(limit); pb = busy_power(s)
        t, end, busy, rows = float(sec), sec + 1.0, 0.0, []
        while t < end:
            while ai < len(arr) and arr[ai] <= t:
                queue.append([arr[ai], C["service_ms"] / 1000.0]); ai += 1
            nxt = arr[ai] if ai < len(arr) else math.inf
            if not queue:
                t = min(end, nxt); continue
            job = queue[0]
            step = min(job[1] / s, end - t, nxt - t)
            job[1] -= step * s; busy += step; t += step
            if job[1] <= 1e-12:
                queue.pop(0); ms = (t - job[0]) * 1000.0; lats.append(ms); rows.append(f"{t:.3f},{ms:.2f},1\n")
        draw = busy * pb + (1 - busy) * C["idle_w"]
        energy += draw; temp += (30 + 0.12 * draw - temp) / 20.0; peak = max(peak, temp)
        with open(lat, "a") as f:
            f.writelines(rows)
        st.update(draw=round(draw, 2), temp=round(temp, 1), util=busy, speed=s); state.write_text(json.dumps(st))
        if gov and sec < C["duration_s"] and sec % every == every - 1:
            gov.step()
    if gov:
        gov.restore()
    lats.sort()
    held = limits[:C["duration_s"]]
    wear = cap_wear(held)
    res = {"requests_served": float(len(lats)), "requests_not_served": float(len(arr) - len(lats)),
           "p95_ms": lats[int(0.95 * len(lats))], "p99_ms": lats[int(0.99 * len(lats))], "gpu_energy_j": energy, "peak_temp_c": peak,
           "limit_writes": float(gov.writes if gov else 0), "limit_moves": wear["power_cap_moves"],
           "limit_reversals": wear["power_cap_reversals"], "limit_travel_w": wear["power_cap_travel"]}
    if gov:
        res["engine_tree"] = engine_tree("omni_controller.gpu_governor")
        if engine_tree("omnicompass.adapter") != res["engine_tree"]:
            raise RuntimeError("the card governor and the brain were imported from two trees")
    print(json.dumps(res))


VERDICT_RATES = (20, 200)


def worker_verdict(seeds):
    import random
    from omnicompass.verdict import Verdict
    out = {}
    for rate in VERDICT_RATES:                     # pieces of work a decision: slow work, and work fast enough to read a 2% step
        out[str(rate)] = {}
        for rise in (0.0, 0.01, 0.02, 0.03, 0.05):
            allowed = 0
            for s in range(seeds):
                rng = random.Random(s)
                v = Verdict(tolerance=0.02, min_samples=60, probe_every=1, recheck=10 ** 6, max_trial=40)
                step = 0
                for _ in range(120):
                    base = 10.0 * (1.0 + rise * step)
                    v.observe([base * rng.lognormvariate(0.0, 0.25) for _ in range(rate)])
                    step, _, ev = v.tick(True)
                    if ev and str(ev.get("verdict", "")).startswith(("step", "trial not started")):
                        allowed += ev["verdict"] == "step allowed"
                        break
            out[str(rate)][f"{rise:.2f}"] = allowed / seeds
    out["engine_tree"] = engine_tree("omnicompass.verdict")
    print(json.dumps(out))


def verdict_rates(r):
    """The verdict model's readings by pieces of work a decision; a checkout whose model ran one rate (20) is read as that rate."""
    return r if all(isinstance(v, dict) for v in r.values()) else {"20": r}


# ---- the parent: both checkouts, every seed, the readings -----------------------------------------------------------
def engine_tree(module):
    """The checkout a worker's engine module was imported from (the root above its package)."""
    return str(Path(sys.modules[module].__file__).resolve().parents[1])


def run(tree, args):
    # a worker's reading is kept in its own folder, so a study stopped part way (22 October: the machine restarted an hour into
    # the pace study) starts again from the jobs it has not finished; a kept reading is reused only for the same checkout and
    # the same arguments
    keep = Path(args[args.index("--dir") + 1]) / "reading.json" if "--dir" in args else None
    if keep is not None and keep.exists():
        k = json.loads(keep.read_text())
        if k.get("tree") == str(Path(tree).resolve()) and k.get("args") == list(args):
            return k["reading"]
    env = {**os.environ, "PYTHONPATH": str(tree)}
    p = subprocess.run([sys.executable, str(Path(__file__).resolve()), *args], cwd=tree, env=env, capture_output=True,
                       text=True, timeout=7200)
    if p.returncode != 0:
        raise RuntimeError(f"{tree} {args}: {p.stderr[-2000:]}")
    r = json.loads(p.stdout.strip().splitlines()[-1])
    got = r.pop("engine_tree", None) if isinstance(r, dict) else None
    if got is not None and Path(got).resolve() != Path(tree).resolve():
        raise RuntimeError(f"{args[:2]}: the engine was imported from {got}, not from the checkout under test {tree}")
    if keep is not None and keep.parent.is_dir():
        keep.write_text(json.dumps({"tree": str(Path(tree).resolve()), "args": list(args), "reading": r}))
    return r


def reading(gauge, diffs, base_vals, gauges=None):
    aim, spent = (gauges or GAUGES)[gauge]
    n = len(diffs); m = sum(diffs) / n
    sd = math.sqrt(sum((d - m) ** 2 for d in diffs) / (n - 1)) if n > 1 else float("inf")
    t = T95.get(n - 1, 2.0); lo, hi = m - t * sd / math.sqrt(n), m + t * sd / math.sqrt(n)
    if sd == 0.0:
        lo = hi = m
    b = sum(base_vals) / n
    rel = m / b if b else float("nan")
    # the founder's order of 24 October 2026: a change of 0.5% or more (the seeds' mean) is a change, read by the gauge's aim;
    # STEADY is kept for a change under 0.5%; whether the change stands beyond the seeds' noise is kept beside the word
    if lo == hi == 0.0:
        word = "STEADY (identical)"
    elif (b and abs(rel) < 0.005) or m == 0.0:
        word = "STEADY"
    elif (m < 0) == (aim == "lower"):
        word = "GAIN"
    else:
        word = "power given" if spent else "LOSS"
    return {"mean_change": m, "ci95": [lo, hi], "relative": rel, "word": word, "beyond_noise": not (lo <= 0.0 <= hi)}


def render(report_path, out_md):
    """MODEL_GATE.json -> a page with the notice: the models, their gauges, the readings, the counts (class S, never a benchmark)."""
    return render_report(json.loads(Path(report_path).read_text()), out_md)


def render_report(r, out_md):
    """The page of a report already in memory (tools/model_reread.py reads a record again and renders it from here)."""
    from tools.legal import stamp

    def engine(tree):
        """The engine a tree declares (tools/omni_version.py), or the tree's name where it cannot be read."""
        try:
            out = subprocess.run([sys.executable, "tools/omni_version.py"], cwd=tree, env={**os.environ, "PYTHONPATH": tree},
                                 capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
            differs = [ln.split(": ", 1)[1] for ln in out if ln.startswith("differs from ")]
            if differs:                    # every engine file the tree changes, not only the last one printed
                return f"{out[0].split(': ', 1)[0]}: {', '.join(differs)}"
            return out[-1].split(" (")[0] if out else Path(tree).name
        except (OSError, subprocess.SubprocessError):
            return Path(tree).name
    # the engines as the page first named them, where the record keeps them (its trees are gone once the gate has run)
    base_e = r.get("base_engine") or (engine(r["base"]) if Path(r["base"]).exists() else r["base"])
    cand_e = r.get("cand_engine") or (engine(r["cand"]) if Path(r["cand"]).exists() else r["cand"])
    lines = ["# The model gate: the candidate against the engine that stands, in our own models", "",
             f"Seeds {r['seeds'][0]} to {r['seeds'][-1]}, {r['days']} day each where a day is run; the standing engine "
             f"{base_e}, the candidate {cand_e}. Evidence class S, our own models: a reading here says "
             "whether a change shows promise before a real run, never what a benchmark found. Each candidate reading is paired by seed "
             "with the standing engine's (the mean change, its 95% interval over the seeds, the word by the gauge's aim: "
             "tools/readings.py).", ""]
    if r.get("note"):
        lines += [r["note"], ""]
    for model, t in r["models"].items():
        period = (f" (a decision every {t['period_s']:.0f} s)" if t["period_s"] else " (each checkout at its own default decision period)") \
            if "period_s" in t else ""
        lines += [f"## {model}{period}", ""]
        if model.startswith("pace_"):
            # the pace study (omni-v16): the candidate alone at each decision period on the 5 s plant, each pace against the
            # candidate at the reference period and against native, paired by seed
            cellp = lambda d: "" if d is None else (f"{by_word(100 * d['relative'], d['word'], digits=2)} {d['word']}" if d["relative"] == d["relative"]
                                                     else d["word"])
            lines += [f"The {t['setting']} setting on the plant that moves every 5 s; the candidate decides every "
                      f"{', '.join(f'{p:g}' for p in t['periods'])} s, each faster pace read against a decision every "
                      f"{t['reference']} s and against native.", "",
                      f"A decision every {t['reference']} s against native:", "",
                      "| Gauge | Native | Every " + t["reference"] + " s | Against native |", "|---|---:|---:|---|"]
            for g, x in t["reference_rows"].items():
                lines.append(f"| {g} | {x['native']:.3f} | {x['ref']:.3f} | {cellp(x['ref_vs_native'])} |")
            lines.append("")
            for per, rows in t["against_reference"].items():
                lines += [f"A decision every {per} s:", "",
                          f"| Gauge | Native | Every {t['reference']} s | Every {per} s | Against every {t['reference']} s | Against native |",
                          "|---|---:|---:|---:|---|---|"]
                for g, x in rows.items():
                    lines.append(f"| {g} | {x['native']:.3f} | {x['ref']:.3f} | {x['pace']:.3f} | {cellp(x['pace_vs_ref'])} | "
                                 f"{cellp(x['pace_vs_native'])} |")
                lines.append("")
            lines += ["Counts over all seeds, by decision period: " + ", ".join(f"{k} {v}" for k, v in t["counts"].items()), ""]
            continue
        if model == "verdict":
            for rate, b in verdict_rates(t["base"]).items():
                c = verdict_rates(t["cand"]).get(rate, {})
                lines += [f"{rate} pieces of work a decision, their log spread 0.25:", "",
                          "| True extra cost of a give-back step | Allowed, standing | Allowed, candidate |", "|---|---|---|"]
                lines += [f"| +{100 * float(k):.0f}% | {100 * b[k]:.0f}% | "
                          f"{(f'{100 * c[k]:.0f}%') if k in c else 'not run'} |" for k in b]
                lines.append("")
            continue
        lines += ["| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |",
                  "|---|---:|---:|---:|---|---|---|"]
        cell = lambda d: f"{by_word(100 * d['relative'], d['word'], digits=2)} {d['word']}" if d["relative"] == d["relative"] else d["word"]
        for g, x in t["gauges"].items():
            lines.append(f"| {g} | {x['native']:.3f} | {x['base']:.3f} | {x['cand']:.3f} | {cell(x['cand_vs_base'])} | "
                         f"{cell(x['base_vs_native'])} | {cell(x['cand_vs_native'])} |")
        lines += ["", "Counts over all seeds: " + ", ".join(f"{k} {v}" for k, v in t["counts"].items()), ""]
        first = t.get("candidate_as_first_pushed")
        if first:                                   # the reading that caught a fault, kept beside the corrected candidate's
            lines += [f"The candidate as first pushed (digest {first['digest']}), the reading that caught the fault:", "",
                      "| Gauge | Native | Standing | Candidate as first pushed | Against standing | Against native |", "|---|---:|---:|---:|---|---|"]
            for g, x in first["gauges"].items():
                lines.append(f"| {g} | {x['native']:.3f} | {x['base']:.3f} | {x['cand']:.3f} | {cell(x['cand_vs_base'])} | {cell(x['cand_vs_native'])} |")
            lines.append("")
    lines += ["Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    if r.get("afterword"):                 # a dated correction written under the record after it ran (kept by tools/model_reread.py)
        lines += [r["afterword"], ""]
    Path(out_md).write_text("\n".join(stamp(lines)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--render", nargs=2, metavar=("MODEL_GATE.json", "MODEL_GATE.md"), help="write the page from a report")
    ap.add_argument("--base", help="checkout of the engine that stands")
    ap.add_argument("--cand", help="checkout of the candidate")
    ap.add_argument("--seeds", default="1-8")
    ap.add_argument("--days", type=float, default=1.0)
    ap.add_argument("--models", default="cluster,cluster15,cluster_blink,cluster_shipped,convey,convey_unreadable_quota,convey_refused,convey_batch,card,card_floor,verdict")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--out", default="")
    ap.add_argument("--worker", help=argparse.SUPPRESS)
    ap.add_argument("--seed", type=int, help=argparse.SUPPRESS)
    ap.add_argument("--period", type=float, default=60.0, help=argparse.SUPPRESS)
    ap.add_argument("--dir", help=argparse.SUPPRESS)
    ap.add_argument("--blink", action="store_true", help=argparse.SUPPRESS)  # the cluster model with its machines out of service a while
    ap.add_argument("--fine", action="store_true", help=argparse.SUPPRESS)   # the cluster model on the 5 s plant (omni-v16)
    ap.add_argument("--setting", default="cloud", help=argparse.SUPPRESS)   # cloud (the cloud's plant) or kind (the kind rig's, ARM=omni); the max on both
    ap.add_argument("--pace-periods", default="60,15,10,5", help="the pace study's decision periods, seconds (omni-v16)")
    ap.add_argument("--quota", default="none", help=argparse.SUPPRESS)      # the convey model's quota: none (readable, empty), unreadable, or refused (unreadable, every raise refused)
    ap.add_argument("--batch", action="store_true", help=argparse.SUPPRESS)  # the convey model with the batch muscle beside the serving one
    ap.add_argument("--neighbour", action="store_true", help=argparse.SUPPRESS)  # the convey model with the fairness rig's second app beside the serving one
    ap.add_argument("--gamma", type=float, default=3.0, help=argparse.SUPPRESS)  # the card model's clock-cost exponent
    ap.add_argument("--ctl", default="", help=argparse.SUPPRESS)   # more of the governor's own arguments, one tune of its knobs (tools/tune_study.py)
    a = ap.parse_args(argv)
    if a.render:
        return render(*a.render)
    if a.worker == "verdict":
        return worker_verdict(a.seed)
    if a.worker in ("convey-native", "convey-omni"):
        return worker_convey(a.worker.split("-")[1], a.seed, a.dir, a.quota, a.batch, a.neighbour)
    if a.worker in ("card-native", "card-omni"):
        return worker_card(a.worker.split("-")[1], a.seed, a.gamma, a.dir)
    if a.worker:
        return worker(a.worker, a.seed, a.days, a.period, a.dir, a.blink, a.fine, a.setting, a.ctl)
    lo_s, _, hi_s = a.seeds.partition("-")
    seeds = list(range(int(lo_s), int(hi_s or lo_s) + 1))
    base, cand = Path(a.base).resolve(), Path(a.cand).resolve()
    work = Path(a.out or tempfile.mkdtemp(prefix="model_gate_"))
    from concurrent.futures import ThreadPoolExecutor
    report = {"seeds": seeds, "days": a.days, "base": str(base), "cand": str(cand), "models": {}}
    models = a.models.split(",")
    for model, period in (("cluster", 60.0), ("cluster15", 15.0), ("cluster_blink", 60.0), ("cluster_shipped", 0.0)):
        if model not in models:
            continue
        jobs = [(arm, tree, s) for s in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        blink = ["--blink"] if model == "cluster_blink" else []
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(j[1], ["--worker", "native" if j[0] == "native" else "omni", "--seed", str(j[2]),
                                                    "--days", str(a.days), "--period", str(period), *blink,
                                                    "--dir", str(work / model / f"{j[0]}-{j[2]}")]), jobs))
        res = {}
        for (arm, _, s), r in zip(jobs, got):
            res.setdefault(arm, {})[s] = r
        rows = {}
        for g in GAUGES:
            bv = [res["base"][s][g] for s in seeds]; cv = [res["cand"][s][g] for s in seeds]
            nv = [res["native"][s][g] for s in seeds]
            rows[g] = {"native": sum(nv) / len(nv), "base": sum(bv) / len(bv), "cand": sum(cv) / len(cv),
                       "cand_vs_base": reading(g, [c - b for c, b in zip(cv, bv)], bv),
                       "base_vs_native": reading(g, [b - n for b, n in zip(bv, nv)], nv),
                       "cand_vs_native": reading(g, [c - n for c, n in zip(cv, nv)], nv)}
        extra = {k: {arm: sum(res[arm][s].get(k, 0) for s in seeds) for arm in ("base", "cand")}
                 for k in ("steps_allowed", "steps_refused", "trials_abandoned", "machines_parked", "errors", "readings_held")}
        report["models"][model] = {"period_s": period, "gauges": rows, "counts": extra, "per_seed": res}
    # the convey model twice: the namespace's quota readable and empty, and unreadable (the governor's role cannot list
    # quotas on every kind test, and on any stack whose role withholds it; the first v7 trial read that as a zero budget)
    # and a third time with every raise refused by a quota the governor cannot read (the capacity test, v12); and a
    # fourth with the batch muscle of KubeRay's rig beside the serving one (omni-v13)
    for model, quota, bat, nb in (("convey", "none", False, False), ("convey_unreadable_quota", "unreadable", False, False),
                                ("convey_refused", "refused", False, False), ("convey_batch", "none", True, False),
                                ("convey_neighbour", "none", False, True)):
        if model not in models:
            continue
        gauges = CONVEY_BATCH_GAUGES if bat else (CONVEY_NEIGHBOUR_GAUGES if nb else CONVEY_GAUGES)
        jobs = [(arm, tree, s) for s in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(j[1], ["--worker", "convey-native" if j[0] == "native" else "convey-omni",
                                                    "--seed", str(j[2]), "--quota", quota, *(["--batch"] if bat else []),
                                                    *(["--neighbour"] if nb else []),
                                                    "--dir", str(work / model / f"{j[0]}-{j[2]}")]), jobs))
        res = {}
        for (arm, _, s), r in zip(jobs, got):
            res.setdefault(arm, {})[s] = r
        rows = {}
        for g in gauges:
            bv = [res["base"][s][g] for s in seeds]; cv = [res["cand"][s][g] for s in seeds]
            nv = [res["native"][s][g] for s in seeds]
            rows[g] = {"native": sum(nv) / len(nv), "base": sum(bv) / len(bv), "cand": sum(cv) / len(cv),
                       "cand_vs_base": reading(g, [c - b for c, b in zip(cv, bv)], bv, gauges),
                       "base_vs_native": reading(g, [b - n for b, n in zip(bv, nv)], nv, gauges),
                       "cand_vs_native": reading(g, [c - n for c, n in zip(cv, nv)], nv, gauges)}
        report["models"][model] = {"gauges": rows, "counts": {k: {arm: sum(res[arm][s][k] for s in seeds) for arm in ("native", "base", "cand")}
                                                          for k in ("starts", "starts_past_75")}, "per_seed": res}
    # the card models (omni-v15): the GPU governor of each checkout on the modelled card, native the card's own firmware at its
    # start limit; the card whose voltage falls with its clock (gamma 3) and the card near its voltage floor (gamma 1.5)
    for model, gamma in (("card", 3.0), ("card_floor", 1.5)):
        if model not in models:
            continue
        jobs = [(arm, tree, s) for s in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(j[1], ["--worker", "card-native" if j[0] == "native" else "card-omni",
                                                    "--seed", str(j[2]), "--gamma", str(gamma),
                                                    "--dir", str(work / model / f"{j[0]}-{j[2]}")]), jobs))
        res = {}
        for (arm, _, s), r in zip(jobs, got):
            res.setdefault(arm, {})[s] = r
        rows = {}
        for g in CARD_GAUGES:
            bv = [res["base"][s][g] for s in seeds]; cv = [res["cand"][s][g] for s in seeds]
            nv = [res["native"][s][g] for s in seeds]
            rows[g] = {"native": sum(nv) / len(nv), "base": sum(bv) / len(bv), "cand": sum(cv) / len(cv),
                       "cand_vs_base": reading(g, [c - b for c, b in zip(cv, bv)], bv, CARD_GAUGES),
                       "base_vs_native": reading(g, [b - n for b, n in zip(bv, nv)], nv, CARD_GAUGES),
                       "cand_vs_native": reading(g, [c - n for c, n in zip(cv, nv)], nv, CARD_GAUGES)}
        report["models"][model] = {"gauges": rows, "counts": {k: {arm: sum(res[arm][s][k] for s in seeds) for arm in ("native", "base", "cand")}
                                                          for k in ("limit_writes", "limit_moves", "limit_reversals")}, "per_seed": res}
    # the pace study (omni-v16): the candidate alone on the 5 s plant at each decision period, in the cloud's setting and in
    # the kind benchmark's, each pace read against the candidate at 60 s and against native, paired by seed
    periods = [float(x) for x in a.pace_periods.split(",")]
    # pace_onsite (31 October, amendment 5): on site, the kind rig's own fixed machines, no cluster autoscaler
    for model, setting in (("pace_cloud", "cloud"), ("pace_kind", "kind"), ("pace_onsite", "static")):
        if model not in models:
            continue
        jobs = [("native", None, s_) for s_ in seeds] + [("omni", per, s_) for per in periods for s_ in seeds]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(cand, ["--worker", j[0], "--seed", str(j[2]), "--days", str(a.days), "--fine",
                                                    "--setting", setting, "--period", str(j[1] or 60.0),
                                                    "--dir", str(work / model / f"{j[0]}-{j[1] or 0:g}-{j[2]}")]), jobs))
        res = {}
        for (arm, per, s_), r in zip(jobs, got):
            res.setdefault("native" if arm == "native" else f"{per:g}", {})[s_] = r
        ref = f"{periods[0]:g}"
        table = {}
        for per in periods[1:]:
            key = f"{per:g}"
            rows = {}
            for g in PACE_GAUGES:
                rv = [res[ref][s_][g] for s_ in seeds]; pv = [res[key][s_][g] for s_ in seeds]
                nv = [res["native"][s_].get(g, 0.0) for s_ in seeds]
                rows[g] = {"native": sum(nv) / len(nv), "ref": sum(rv) / len(rv), "pace": sum(pv) / len(pv),
                           "pace_vs_ref": reading(g, [p_ - r_ for p_, r_ in zip(pv, rv)], rv, PACE_GAUGES),
                           "pace_vs_native": reading(g, [p_ - n_ for p_, n_ in zip(pv, nv)], nv, PACE_GAUGES)
                           if g in GAUGES else None}
            table[key] = rows
        ref_rows = {g: {"native": sum(res["native"][s_].get(g, 0.0) for s_ in seeds) / len(seeds),
                        "ref": sum(res[ref][s_][g] for s_ in seeds) / len(seeds),
                        "ref_vs_native": reading(g, [res[ref][s_][g] - res["native"][s_].get(g, 0.0) for s_ in seeds],
                                                 [res["native"][s_].get(g, 0.0) for s_ in seeds], PACE_GAUGES)
                        if g in GAUGES else None} for g in PACE_GAUGES}
        report["models"][model] = {"setting": setting, "periods": periods, "reference": ref, "reference_rows": ref_rows,
                               "against_reference": table,
                               "counts": {k: {per: sum(res[per][s_].get(k, 0) for s_ in seeds) for per in res if per != "native"}
                                          for k in ("decisions", "machines_parked", "errors", "steps_allowed", "steps_refused",
                                                    "trials_abandoned")},
                               "per_seed": res}
    if "verdict" in models:
        report["models"]["verdict"] = {"base": run(base, ["--worker", "verdict", "--seed", "300"]),
                                     "cand": run(cand, ["--worker", "verdict", "--seed", "300"])}
    (work / "MODEL_GATE.json").write_text(json.dumps(report, indent=1))
    for model, r in report["models"].items():
        if model.startswith("pace_"):
            print(f"\n== {model} ({r['setting']} setting, the 5 s plant; each pace against a decision every {r['reference']} s)")
            for per, rows in r["against_reference"].items():
                print(f" a decision every {per} s:")
                for g, x in rows.items():
                    d = x["pace_vs_ref"]; n = x["pace_vs_native"]
                    print(f"  {g:32s} {x['ref']:10.3f} -> {x['pace']:10.3f}  {by_word(100 * d['relative'], d['word'], digits=2):>9s} {d['word']:12s}"
                          + (f"  against native {by_word(100 * n['relative'], n['word'], digits=2):>9s} {n['word']}" if n else ""))
            print("counts over all seeds:", json.dumps(r["counts"]))
            continue
        print(f"\n== {model}" + (f" (a decision every {r['period_s']:.0f} s)" if "period_s" in r else ""))
        if model == "verdict":
            print("share of give-back steps allowed, by the step's true extra cost (2% allowance, noisy work):")
            for rate, b in verdict_rates(r["base"]).items():
                c = verdict_rates(r["cand"]).get(rate, {})
                print(f" {rate} pieces of work a decision:")
                for k in b:
                    print(f"  +{100 * float(k):.0f}%: standing {100 * b[k]:.0f}%  candidate "
                          f"{(f'{100 * c[k]:.0f}%') if k in c else 'not run'}")
            continue
        print(f"{'gauge':32s} {'native':>10s} {'standing':>10s} {'candidate':>10s}  candidate vs standing         standing vs native   candidate vs native")
        for g, x in r["gauges"].items():
            cb, bn, cn = x["cand_vs_base"], x["base_vs_native"], x["cand_vs_native"]
            print(f"{g:32s} {x['native']:10.3f} {x['base']:10.3f} {x['cand']:10.3f}  {by_word(100 * cb['relative'], cb['word'], digits=2):>9s} {cb['word']:18s}"
                  f"  {by_word(100 * bn['relative'], bn['word'], digits=2):>9s} {bn['word']:10s}  {by_word(100 * cn['relative'], cn['word'], digits=2):>9s} {cn['word']}")
        print("counts over all seeds:", json.dumps(r["counts"]))
    print(f"\n(our own models, evidence class S; {work / 'MODEL_GATE.json'})")
    return report


if __name__ == "__main__":
    main()
