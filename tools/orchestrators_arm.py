#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The orchestrators on the same organisms, with the same injection (the founder's order of 25 October: "all the orchestrators
to have the same injection ran through. Those orchestrators sit on the same organism. And there lies the third arm ... And of
course then OmniCompass on top of that same stack"). Our own models, evidence class S; docs/ORCHESTRATORS_PREREGISTRATION.md
was written before the first run.

Three arms on every organism, every repetition the same injection in all of them:

  native        Kubernetes alone on the organism: its default scheduler places every pod, the service's HPA, and in the
                cloud the Cluster Autoscaler
  orchestrator  the same organism and the same work, every pod of it sent to the orchestrator as its project documents
                for that kind of work, the orchestrator's shipped rule deciding what is admitted and where it goes
  omni          Omni-Compass on top of that orchestrator: the shipped Kubernetes governor of the engine that stands
                (omni_controller), its factory flags as the rig runs it, reading and writing only what it reads and writes
                on a real cluster (the service's autoscaler, the machines' idle mark, the service pods' CPU limit); it never
                writes an orchestrator's own objects

Every orchestrator's rule is written here from its own release and documentation (no orchestrator's code is in it):

  default      the Kubernetes 1.35 scheduler's default scoring: NodeResourcesFit LeastAllocated (weight 1), PodTopologySpread's
               default constraints (weight 2), TaintToleration (weight 3), each normalised to 0..100 over the feasible
               machines, ties broken at random, as the scheduler breaks them
  binpack      the same scheduler with the operator's bin-packing profile (deploy/kind/binpack-scheduler.yaml: NodeResourcesFit
               MostAllocated, every other plugin as shipped)
  volcano      Volcano v1.16.0's shipped scheduler configuration (installer/volcano-development.yaml): actions enqueue,
               allocate, backfill; a plain Job's or Deployment's pods each in a PodGroup of one; overcommit's enqueue gate at
               1.2 times the machines' room; jobs taken in DRF order (the least share first); nodeorder's leastrequested and
               binpack at weight 1 each, which on the processor cancel, so the best machines tie and one is taken at random
               (SelectBestNodeAndScore); its tainttoleration at weight 1
  kueue        Kueue v0.20.2 with the operator's one ClusterQueue (scripts/kind_batch_queue.sh): nominal quota the workers'
               allocatable processor read once at install, BestEffortFIFO; a Job admitted whole (parallelism times its pod's
               request), its quota given back as its pods finish (reclaimable pods); the service's pods each admitted as a
               workload of one (the pod integration); the admitted pods placed by the default scheduler
  kai          the KAI scheduler v0.18.6's defaults (pkg/apis/kai/v1/schedulingshard_types.go): placement strategy binpack for
               the processor, a plain Job's pods scheduled one by one (docs/batch: no min-member set), its default queue; no
               plugin of its default set scores a PreferNoSchedule taint
  koordinator  Koordinator 1.8.0 with the operator's colocation profile (deploy/kind/koordinator-colocation.yaml): the batch
               pods best effort (BE) on batch resources, the service latency-sensitive (LS) through koord-scheduler; batch
               allocatable = the machine's processor x 60% (CPUReclaimThresholdPercent) less the LS pods' use, refreshed when
               it moves 10% or every 300 s (pkg/util/sloconfig/colocation_config.go); the BE pods held to the machine x 65%
               (CPUSuppressThresholdPercent) less the LS use (nodeslo_config.go); koord-scheduler's LoadAwareScheduling
               filter at 65% busy (pkg/scheduler/apis/config/v1/defaults.go) and its least-allocated scoring

The organisms (one injection each, from the benchmark that carries it; ORGANISMS below), in two settings: on-site, the kind rig
(six workers that are containers on one runner: each reports the runner's 4 cores, the pods share its 3 cores left after the
governor's own; no cluster autoscaler) and the cloud (machines of 2 cores of their own, 1.9 allocatable, the Cluster Autoscaler
at its defaults, 2 to 9 machines, 90 s to boot). The service is the rig's php-apache (200m request, 500m limit, its HPA at 50%,
1 to 10 pods, 60 ms of processor a request, open-loop clients at 6 requests a second each); the batch stream is the rig's (24
jobs of 10 pods, 5 at a time, one every 30 s, 500m request and 1 core limit, 8.1 core-seconds of hashing a pod).

The injection: repetition k draws its seed from the jump generator of the engine's runs (seed_k = base + k·0x9E3779B9 mod 2³²,
tools/engine_runs.py) and every random number of the run (the clients' noise, every pod's work, every response time's spread)
is drawn before any arm runs, so all arms of repetition k meet the same numbers at the same moment whatever they decide.

  python3 tools/orchestrators_arm.py [--reps 8] [--base 20261025] [--out results/orchestrators] [--workers N]
  python3 tools/orchestrators_arm.py --one ORGANISM SETTING ORCH ARM K     one run, its gauges printed as JSON

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

DT = 5.0                                   # the plant's step and the governor's fast check (omni-v17 on: 5 s)
SAMPLES = 10                               # response times drawn every step
COST_S = 0.06                              # processor seconds a request (the model gate's calibration, tools/model_gate.py CAL)
RATE = 6.0                                 # requests a second a client sends (deploy/kind/loadgen-open.yaml, RATE)
TIMEOUT_S = 10.0                           # a request unanswered in 10 s fails (the client's wget -T 10)
SLO_MS = 500.0                             # the kind rig's line (scripts/kind_bench.sh, SLO_MS)
SVC = {"req": 200, "lim": 500, "target": 50, "min": 1, "max": 10}          # deploy/kind/demo.yaml
BATCH = {"jobs": 24, "every": 30, "completions": 10, "parallel": 5, "req": 500, "lim": 1000, "core_s": 8.1}
M32 = 0xFFFFFFFF

SETTINGS = {
    # the kind rig: six workers, each reporting the runner's 4 cores; the pods share the 3 cores the governor's own leaves
    "onsite": {"start": 6, "min": 2, "max": 6, "alloc": 4000, "host": 3000, "ca": False, "boot_s": 0,
               "idle_w": 30.0, "core_w": 15.0},
    # the cloud: machines of 2 cores (Standard_D2_v4), 1.9 allocatable, the Cluster Autoscaler at its defaults
    "cloud": {"start": 2, "min": 2, "max": 9, "alloc": 1900, "host": None, "ca": True, "boot_s": 90,
              "idle_w": 60.0, "core_w": 40.0, "cap": 2000},
}

# organism -> (the benchmark that carries it, its window in seconds, its clients over the window, two services?, the
# batch stream?, the fault drill?)
ORGANISMS = {
    "steady":       ("kubernetes steady", 900, [1, 2, 3, 1, 2, 1], False, False, False),
    "wandering":    ("kubernetes wandering", 2700, [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 4, 3, 2, 1, 2, 1], False, False, False),
    "all_four":     ("kubernetes all four", 2700, [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1], False, False, False),
    "google_2011":  ("kubernetes google 2011 trace", 2592, [2, 3, 3, 3, 3, 4, 4, 3, 2, 2, 2, 2, 2, 3, 2, 3, 4, 4, 3, 4, 5, 6, 5, 4], False, False, False),
    "climb":        ("the founder's traffic rule (1 2 3 2 3 4 ...)", 1800, [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8], False, False, False),
    "burst_1419":   ("the cloud's burst 1 4 1 6 1 9", 1800, [1, 4, 1, 6, 1, 9], False, False, False),
    "burst_1618":   ("the cloud's burst 1 6 1 8 1 6", 1800, [1, 6, 1, 8, 1, 6], False, False, False),
    "real_day":     ("the cloud's real day (Google 2011) on 1 to 9", 2592, [2, 3, 3, 4, 3, 4, 4, 3, 2, 2, 2, 2, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 5], False, False, False),
    "fairness":     ("kubernetes fairness (two services)", 900, [1, 2, 3, 1, 2, 1], True, False, False),
    "faults":       ("kubernetes faults", 900, [1, 2, 3, 1, 2, 1], False, False, True),
    "batch":        ("kubernetes batch (the stream; the service deployed, its clients at zero)", 1500, [0], False, True, False),
    "one_body":     ("the batch stream beside the service", 1800, [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8], False, True, False),
}

ORCHESTRATORS = {
    "default":     "the Kubernetes scheduler as shipped (the organism alone)",
    "binpack":     "the Kubernetes scheduler's bin-packing profile",
    "volcano":     "Volcano v1.16.0",
    "kueue":       "Kueue v0.20.2",
    "kai":         "the KAI scheduler v0.18.6",
    "koordinator": "Koordinator 1.8.0",
}

# each orchestrator's rule as the model writes it, and where it was read (the module's docstring has the whole of it)
RULES = {
    "default": "default scoring: least allocated (1), topology spread (2), taint toleration (3); ties at random (Kubernetes 1.35)",
    "binpack": "most allocated in place of least allocated, every other plugin as shipped (deploy/kind/binpack-scheduler.yaml)",
    "volcano": "enqueue gate at 1.2 times the room, jobs in DRF order, PodGroups of one; leastrequested and binpack cancel, "
               "the best machines tie, one taken at random (installer/volcano-development.yaml, v1.16.0)",
    "kueue": "one ClusterQueue, quota the workers' processor at install, BestEffortFIFO, a job admitted whole and its quota "
             "given back as pods finish, the service's pods admitted one by one; placed by the default scheduler (v0.20.2)",
    "kai": "bin-packing on the processor, a plain Job's pods one by one, its default queue (schedulingshard_types.go, v0.18.6)",
    "koordinator": "the batch pods best effort on batch resources (60% of the machine less the service's use), held to 65% "
                   "less the service's use, at the least processor weight; load-aware filter at 65% busy (1.8.0)",
}

# gauge -> (aim, a resource spent?) read by the one key (tools/readings.py): time waited, missed or failed that fell is a
# GAIN; work that rose is a GAIN; a resource spent that fell is a cut (GAIN) and one that rose is power given
GAUGES = {"p95_ms": ("lower", False), "alert_minutes": ("lower", False), "requests_failed": ("lower", False),
          "pending_pod_minutes": ("lower", False), "batch_turnaround_s": ("lower", False), "batch_makespan_s": ("lower", False),
          "batch_pods_done": ("higher", False), "requests_served": ("higher", False),
          "machine_hours": ("lower", True), "energy_kwh": ("lower", True)}


def seed_of(base: int, k: int) -> int:
    """The jump generator of the engine's runs (tools/engine_runs.py): seed_k = base + k·0x9E3779B9 mod 2³²."""
    return (base + k * 0x9E3779B9) & M32


def injection(organism: str, setting: str, k: int, base: int) -> dict:
    """Every random number of repetition k, drawn before any arm runs (the same injection in every arm)."""
    import numpy as np
    _, dur, steps, two, batch, _ = ORGANISMS[organism]
    n = int(dur / DT) * 3                                         # the window and a drain twice as long
    rng = np.random.default_rng([seed_of(base, k), sum(map(ord, organism)), sum(map(ord, setting))])
    return {"noise": (1.0 + 0.05 * rng.standard_normal((2, n))).clip(0.7, 1.3).tolist(),
            "spread": rng.lognormal(0.0, 0.25, (n, SAMPLES)).tolist(),
            "work": (BATCH["core_s"] * (1.0 + 0.05 * rng.standard_normal(BATCH["jobs"] * BATCH["completions"]))).clip(6.0, 11.0).tolist(),
            "ties": rng.random(n * 64).tolist()}


class Organism:
    """The cluster, its work and its native controllers, one step every DT seconds."""

    def __init__(self, organism, setting, orch, inj):
        self.name, self.setting, self.orch, self.inj = organism, SETTINGS[setting], orch, inj
        _, self.dur, self.steps, two, self.has_batch, self.faults = ORGANISMS[organism]
        s = self.setting
        self.t, self.ti = 0, 0                                     # step index; tie-breaker index
        self.nodes = [self._node(i) for i in range(s["start"])]
        self.booting = []                                          # cloud: (ready step,)
        self.pods, self.pid = [], 0
        self.svcs = [{"name": "php-apache", "target": SVC["target"], "min": SVC["min"], "max": SVC["max"], "desired": 1,
                      "recs": [], "backlog": 0.0, "metric": 0.0, "ann": {}, "dann": {}, "lim": SVC["lim"]}]
        if two:
            self.svcs.append(dict(self.svcs[0], name="web2", recs=[], ann={}, dann={}))
        for sv in self.svcs:
            self._new_pod("svc", sv["name"], ready_now=True)
        self.jobs = []                                             # {name, born, left, running, done_at, admitted}
        self.quota = sum(n["alloc"] for n in self.nodes) if orch == "kueue" else None
        if orch == "kueue" and s["ca"]:
            self.quota = s["max"] * s["alloc"]                     # the operator sizes the queue to the pool it may grow to
        self.batch_alloc = {}                                      # Koordinator: per node, its batch-cpu allocatable
        self.batch_seen = {}
        self.ca_under, self.ca_add_t = {}, -10 ** 9
        self.lat, self.minute, self.failed, self.served = [], {}, 0, 0.0
        self.pending_s, self.mach_s, self.energy_j = 0.0, 0.0, 0.0
        self.busy_hist = []
        self.down = None                                           # the fault drill's machine down

    # ---- the cluster's objects ---------------------------------------------------------------------------------------
    def _node(self, i):
        return {"name": f"w{i}", "alloc": self.setting["alloc"], "idle": False, "up": True, "born": self.t}

    def _new_pod(self, kind, owner, ready_now=False, job=None, work=0.0):
        self.pid += 1
        sv = next((x for x in self.svcs if x["name"] == owner), None)
        p = {"name": f"{owner}-{self.pid}", "kind": kind, "owner": owner, "job": job, "node": None, "born": self.t,
             "ready_at": None, "work": work, "req": SVC["req"] if kind == "svc" else BATCH["req"],
             "lim": (sv["lim"] if sv else SVC["lim"]) if kind == "svc" else BATCH["lim"], "cost": 0,
             "qos": "BE" if (kind == "batch" and self.orch == "koordinator") else "LS", "admitted": self.orch != "kueue" or kind == "batch"}
        if ready_now:
            p["node"], p["ready_at"], p["admitted"] = self.nodes[0]["name"], 0, True
        self.pods.append(p)
        return p

    def svc_pods(self, name):
        return [p for p in self.pods if p["kind"] == "svc" and p["owner"] == name]

    def node(self, name):
        return next((n for n in self.nodes if n["name"] == name), None)

    def live_nodes(self):
        return [n for n in self.nodes if n["up"]]

    def _tie(self):
        self.ti += 1
        return self.inj["ties"][self.ti % len(self.inj["ties"])]

    # ---- placement: each orchestrator's rule ---------------------------------------------------------------------------
    def requested(self, n, qos="LS"):
        return sum(p["req"] for p in self.pods if p["node"] == n["name"] and p["qos"] == qos)

    def used(self, n):
        return sum(p.get("use", 0.0) for p in self.pods if p["node"] == n["name"])

    def ls_used(self, n):
        return sum(p.get("use", 0.0) for p in self.pods if p["node"] == n["name"] and p["qos"] == "LS")

    def feasible(self, p, rule):
        out = []
        for n in self.live_nodes():
            if p["qos"] == "BE":                                   # Koordinator: batch-cpu, not the node's requests
                if sum(q["req"] for q in self.pods if q["node"] == n["name"] and q["qos"] == "BE") + p["req"] > self.batch_alloc.get(n["name"], 0):
                    continue
            elif self.requested(n) + p["req"] > n["alloc"]:
                continue
            if rule == "koordinator" and self.used(n) > 0.65 * self.report_cap(n):
                continue                                           # LoadAwareScheduling's filter at 65% busy
            out.append(n)
        return out

    def report_cap(self, n):
        """The processor a machine reports as its own: on kind every node reports the runner's cores; in the cloud its own."""
        return float(n["alloc"]) if self.setting["host"] else float(self.setting["cap"])

    @staticmethod
    def norm(vals):
        lo, hi = min(vals), max(vals)
        return [100.0 * (v - lo) / (hi - lo) if hi > lo else 100.0 for v in vals]

    def score(self, p, nodes, rule):
        """Each feasible machine's score by the orchestrator's shipped plugins, the best taken, ties at random."""
        if rule == "volcano":                                      # leastrequested + binpack cancel; tainttoleration x 1
            s = [0.0 if n["idle"] else 100.0 for n in nodes]
        elif rule == "kai":                                        # nodeplacement binpack on the processor
            s = [100.0 * (self.requested(n) + p["req"]) / n["alloc"] for n in nodes]
        else:
            if rule == "binpack":
                fit = [100.0 * (self.requested(n) + p["req"]) / n["alloc"] for n in nodes]
            elif rule == "koordinator":                            # koord-scheduler: least estimated use (85% of the request)
                fit = [100.0 * (1.0 - (self.used(n) + 0.85 * p["req"]) / self.report_cap(n)) for n in nodes]
            else:
                fit = [100.0 * (n["alloc"] - self.requested(n) - p["req"]) / n["alloc"] for n in nodes]
            same = [sum(1 for q in self.pods if q["node"] == n["name"] and q["owner"] == p["owner"]) for n in nodes]
            spread = self.norm([-c for c in same])                 # PodTopologySpread's default constraints: fewest first
            taint = [0.0 if n["idle"] else 100.0 for n in nodes]   # TaintToleration: a PreferNoSchedule taint scores 0
            s = [f + 2.0 * sp + 3.0 * ta for f, sp, ta in zip(self.norm(fit), spread, taint)]
        best = max(s)
        tops = [n for n, v in zip(nodes, s) if v >= best - 1e-9]
        return tops[int(self._tie() * len(tops)) % len(tops)]

    def rule_for(self, p):
        """Which scheduler places this pod: every pod of the organism goes to the orchestrator under test."""
        if self.orch in ("binpack", "volcano", "kai", "koordinator"):
            return self.orch
        return "default"

    def admit_kueue(self):
        """Kueue's BestEffortFIFO admission against the ClusterQueue's nominal quota (processor)."""
        def usage():
            u = sum(p["req"] for p in self.pods if p["kind"] == "svc" and p["admitted"])
            for j in self.jobs:
                if j["admitted"] and j["done_at"] is None:
                    u += min(BATCH["parallel"], j["left"] + j["running"]) * BATCH["req"]
            return u
        for j in sorted(self.jobs, key=lambda j: j["born"]):
            if not j["admitted"] and usage() + BATCH["parallel"] * BATCH["req"] <= self.quota:
                j["admitted"] = True
        for p in sorted((p for p in self.pods if not p["admitted"]), key=lambda p: p["born"]):
            if usage() + p["req"] <= self.quota:
                p["admitted"] = True

    def schedule(self):
        if self.orch == "kueue":
            self.admit_kueue()
        pend = [p for p in self.pods if p["node"] is None and p["admitted"]]
        if self.orch == "volcano":                                 # DRF: the job (or service) with the least share first
            share = {}
            for q in self.pods:
                if q["node"]:
                    share[q["owner"] if q["kind"] == "svc" else q["job"]] = share.get(q["owner"] if q["kind"] == "svc" else q["job"], 0) + q["req"]
            # overcommit's enqueue gate: a PodGroup of one goes in while the machines' room x 1.2 holds it
            room = 1.2 * sum(n["alloc"] for n in self.live_nodes()) - sum(q["req"] for q in self.pods if q["node"])
            pend = [p for p in pend if p["req"] <= room]
            pend.sort(key=lambda p: (share.get(p["owner"] if p["kind"] == "svc" else p["job"], 0), p["born"]))
        else:
            pend.sort(key=lambda p: p["born"])
        for p in pend:
            nodes = self.feasible(p, self.rule_for(p))
            if nodes:
                n = self.score(p, nodes, self.rule_for(p))
                p["node"], p["ready_at"] = n["name"], self.t + max(1, int(round(self.start_s() / DT)))

    def start_s(self):
        """A pod's start at the host's busy share (tools/model_gate.py start_time, from the v6 KEDA run's 151 starts)."""
        b = self.busy_hist[-1] if self.busy_hist else 0.3
        return 8.0 if b <= 0.5 else (8.0 + 6.0 * (b - 0.5) if b <= 0.75 else 9.5 + 11.6 * (min(b, 1.0) - 0.75))

    # ---- the native controllers ----------------------------------------------------------------------------------------
    def hpa(self):
        """Kubernetes' HPA every 15 s: the tolerance 0.1, scale-up by the larger of 100% and 4 pods, the 300 s window."""
        for sv in self.svcs:
            pods = self.svc_pods(sv["name"])
            ready = [p for p in pods if p["ready_at"] is not None and p["ready_at"] <= self.t]
            cur = max(1, len(pods))
            util = (sum(p.get("use", 0.0) for p in ready) / max(1, len(ready))) / SVC["req"] * 100.0 if ready else 0.0
            sv["metric"] = util
            ratio = util / max(1.0, sv["target"])
            rec = cur if abs(ratio - 1.0) <= 0.1 else int(math.ceil(len(ready) * ratio)) if ready else cur
            rec = max(sv["min"], min(sv["max"], rec))
            sv["recs"] = (sv["recs"] + [(self.t, rec)])[-int(300 / 15) - 1:]
            new = min(rec, cur + max(4, cur)) if rec > cur else max(r for _, r in sv["recs"])
            sv["desired"] = max(sv["min"], min(sv["max"], new))
            self.reconcile(sv)

    def reconcile(self, sv):
        """The Deployment's ReplicaSet: pods made or removed to the desired count; a pod on an idle machine, or carrying the
        lower deletion cost, goes first (kind_nodepool.sh marks the served pods on an idled machine), then the newest."""
        pods = self.svc_pods(sv["name"])
        while len(pods) < sv["desired"]:
            pods.append(self._new_pod("svc", sv["name"]))
        if len(pods) > sv["desired"]:
            def cost(p):
                n = self.node(p["node"]) if p["node"] else None
                return (p["node"] is not None, not (n and n["idle"]), p["ready_at"] is not None, -p["born"])
            for p in sorted(pods, key=cost)[:len(pods) - sv["desired"]]:
                self.pods.remove(p)

    def cluster_autoscaler(self):
        """The Cluster Autoscaler at its defaults: a machine for pods that cannot be placed (10 s scan, 90 s boot); a
        machine under 50% requested for 10 minutes whose pods fit elsewhere removed, 10 minutes after the last addition."""
        s = self.setting
        self.booting = [b for b in self.booting if not (b <= self.t and self.nodes.append(self._node(len(self.nodes) + self.pid)) is None)]
        live = self.live_nodes()
        pend = [p for p in self.pods if p["node"] is None and p["admitted"]]
        if pend and not self.booting and len(live) < s["max"]:
            need = sum(p["req"] for p in pend)
            add = min(s["max"] - len(live), max(1, int(math.ceil(need / s["alloc"]))))
            self.booting += [self.t + int(s["boot_s"] / DT)] * add
            self.ca_add_t = self.t
            return
        if self.t - self.ca_add_t < 600 / DT or len(live) <= s["min"]:
            return
        for n in live:
            if self.requested(n) < 0.5 * n["alloc"]:
                self.ca_under[n["name"]] = self.ca_under.get(n["name"], 0) + 1
            else:
                self.ca_under[n["name"]] = 0
        for n in sorted(live, key=lambda n: self.requested(n)):
            if self.ca_under.get(n["name"], 0) * DT * 2 >= 600 and len(self.live_nodes()) > s["min"]:
                moving = [p for p in self.pods if p["node"] == n["name"]]
                others = [m for m in self.live_nodes() if m is not n]
                room = sum(m["alloc"] - self.requested(m) for m in others)
                if sum(p["req"] for p in moving) <= room:
                    self.nodes.remove(n)
                    for p in moving:                               # moved: placed again from scratch
                        p["node"], p["ready_at"] = None, None
                        if p["kind"] == "batch":
                            p["work"] = p.get("work0", p["work"])
                    self.ca_under.pop(n["name"], None)
                    break

    def koordinator_batch(self):
        """koord-manager's batch allocatable, refreshed when it moves 10% or every 300 s."""
        for n in self.live_nodes():
            want = max(0.0, 0.60 * self.report_cap(n) - self.ls_used(n))
            old, seen = self.batch_alloc.get(n["name"]), self.batch_seen.get(n["name"], -10 ** 9)
            if old is None or abs(want - old) > 0.10 * max(old, 1.0) or (self.t - seen) * DT >= 300:
                self.batch_alloc[n["name"]], self.batch_seen[n["name"]] = want, self.t

    # ---- the work ---------------------------------------------------------------------------------------------------
    def clients(self):
        i = min(len(self.steps) - 1, int(self.t * DT / (self.dur / len(self.steps))))
        c = self.steps[i] if self.t * DT < self.dur else 0
        if self.faults and 0.35 * self.dur <= self.t * DT < 0.35 * self.dur + 120:
            c += 2.0 * self.steps[i]                               # the drill's spike: traffic x3 for two minutes
        return float(c)

    def submit(self):
        if not self.has_batch:
            return
        j = int(self.t * DT // BATCH["every"])
        if self.t * DT % BATCH["every"] < DT and j < BATCH["jobs"] and len(self.jobs) == j:
            self.jobs.append({"name": f"job-{j}", "born": self.t, "left": BATCH["completions"], "running": 0,
                              "done_at": None, "admitted": self.orch != "kueue", "k": j})
        for job in self.jobs:
            if job["done_at"] is None and job["admitted"]:
                while job["running"] < BATCH["parallel"] and job["left"] > 0:
                    idx = job["k"] * BATCH["completions"] + (BATCH["completions"] - job["left"])
                    p = self._new_pod("batch", "omni-batch-stream", job=job["name"], work=self.inj["work"][idx])
                    p["work0"] = p["work"]
                    job["left"] -= 1; job["running"] += 1

    def share_cpu(self):
        """The kernel's fair share between cgroups on each host (tools/model_gate.py water_fill): each running pod its
        want up to its limit, by the weight of its request, the BE pods held under Koordinator's suppression."""
        from tools.model_gate import water_fill
        hosts = {}
        for p in self.pods:
            if p["node"] and p["ready_at"] is not None and p["ready_at"] <= self.t and self.node(p["node"]):
                hosts.setdefault(None if self.setting["host"] else p["node"], []).append(p)
        cl = self.clients()
        load = [cl * self.inj["noise"][i][self.t % len(self.inj["noise"][i])] * RATE for i in range(len(self.svcs))]
        busy_tot, cap_tot = 0.0, 0.0
        for h, pods in hosts.items():
            cap = self.setting["host"] if h is None else self.setting["cap"]
            if self.runaway_on(h):
                cap = max(0.0, cap - 1000.0 * (1.0 if h is None else 0.5))
            wants = []
            for p in pods:
                if p["kind"] == "svc":
                    i = next(k for k, sv in enumerate(self.svcs) if sv["name"] == p["owner"])
                    n_ready = sum(1 for q in self.svc_pods(p["owner"]) if q["ready_at"] is not None and q["ready_at"] <= self.t and q["node"])
                    lam = load[i] / max(1, n_ready)
                    back = self.svcs[i]["backlog"] / max(1, n_ready)
                    wants.append(min(p["lim"], 1000.0 * COST_S * (lam + back / DT)))
                else:
                    wants.append(float(p["lim"]))
            if self.orch == "koordinator":                         # koordlet's BE suppression on each node: 65% of what
                for n in {p["node"] for p in pods}:                # the node reports, less its LS pods' use
                    on = [k for k, p in enumerate(pods) if p["node"] == n]
                    ls = sum(wants[k] for k in on if pods[k]["qos"] == "LS")
                    be = [k for k in on if pods[k]["qos"] == "BE"]
                    be_cap = max(0.0, 0.65 * self.report_cap(self.node(n)) - ls)
                    tot = sum(wants[k] for k in be)
                    for k in be:
                        wants[k] = wants[k] * min(1.0, be_cap / tot) if tot > 0 else 0.0
            # the cgroup weight is the processor request; a Koordinator BE pod asks batch-cpu, not cpu, so the kubelet puts it in
            # the best-effort cgroup at the least weight (cpu.shares 2)
            weights = [2.0 if p["qos"] == "BE" else max(1.0, p["req"]) for p in pods]
            got = water_fill(cap, wants, weights)
            # what a serving pod could get if it asked its whole limit, the others asking what they ask: its speed
            full = water_fill(cap, [float(p["lim"]) if p["kind"] == "svc" else w for p, w in zip(pods, wants)], weights)
            for p, g, f in zip(pods, got, full):
                p["use"], p["capm"] = g, f
            busy_tot += sum(got) + (1000.0 if self.runaway_on(h) else 0.0)
            cap_tot += self.setting["host"] if h is None else self.setting["cap"]
        for p in self.pods:
            if not (p["node"] and p["ready_at"] is not None and p["ready_at"] <= self.t):
                p["use"], p["capm"] = 0.0, 0.0
        self.busy_hist.append(min(1.0, busy_tot / cap_tot) if cap_tot else 0.0)
        return load

    def runaway_on(self, h):
        """The drill's runaway pod (a busy loop, no request): one core on the host, or on the first worker, for two minutes."""
        if not self.faults or not (0.55 * self.dur <= self.t * DT < 0.55 * self.dur + 120):
            return False
        return h is None or h == self.live_nodes()[0]["name"]

    def serve(self, load):
        for i, sv in enumerate(self.svcs):
            ready = [p for p in self.svc_pods(sv["name"]) if p["ready_at"] is not None and p["ready_at"] <= self.t and p["node"]]
            cap_rps = sum(p.get("capm", 0.0) for p in ready) / (1000.0 * COST_S)
            arrive = load[i] * DT
            done = min(arrive + sv["backlog"], cap_rps * DT)
            sv["backlog"] = arrive + sv["backlog"] - done
            lost = 0.0
            if cap_rps > 0 and sv["backlog"] / cap_rps > TIMEOUT_S:   # the clients give up after 10 s
                lost = sv["backlog"] - TIMEOUT_S * cap_rps
            elif cap_rps <= 0:
                lost = sv["backlog"]
            sv["backlog"] -= lost
            self.failed += lost
            self.served += done
            if arrive <= 0:
                continue
            # the kernel shares the processor without leaving any idle (work-conserving): a request alone runs at its pod's
            # limit (or what the host leaves, one core at most: a request runs on one thread), and the queue is the whole service's, C_s the processor all its pods can
            # get together, however many pods it is split into (amendment 1): T = S/r1 + (S/C_s)·ρ/(1 − ρ) + backlog
            c_s = sum(p.get("capm", 0.0) for p in ready) / 1000.0
            r1 = min(max((p["lim"] for p in ready), default=0) / 1000.0, c_s, 1.0)   # one request, one thread: a core at most
            rho = min(0.98, (load[i] * COST_S) / max(1e-9, c_s)) if ready else 0.98
            base = (COST_S / max(1e-3, r1) + (COST_S / max(1e-3, c_s)) * rho / (1.0 - rho)
                    + (sv["backlog"] / cap_rps if cap_rps > 0 else TIMEOUT_S))
            row = self.inj["spread"][self.t % len(self.inj["spread"])]
            for z in row:
                ms = min(TIMEOUT_S, base * z) * 1000.0
                self.lat.append(ms)
                self.minute.setdefault(int(self.t * DT // 60), []).append(ms)

    def progress(self):
        for p in list(self.pods):
            if p["kind"] == "batch" and p["node"] and p["ready_at"] is not None and p["ready_at"] <= self.t:
                p["work"] -= p["use"] / 1000.0 * DT
                if p["work"] <= 0:
                    self.pods.remove(p)
                    job = next(j for j in self.jobs if j["name"] == p["job"])
                    job["running"] -= 1
                    if job["left"] == 0 and job["running"] == 0:
                        job["done_at"] = self.t

    def fault_machine(self):
        """The drill's machine down: the last worker leaves service for two minutes at 15% of the window, its pods lost."""
        if not self.faults:
            return
        t0 = int(0.15 * self.dur / DT)
        if self.t == t0 and len(self.live_nodes()) > 1:
            n = self.live_nodes()[-1]; n["up"] = False; self.down = n
            for p in self.pods:
                if p["node"] == n["name"]:
                    p["node"], p["ready_at"] = None, None
        if self.down and self.t == t0 + int(120 / DT):
            self.down["up"] = True; self.down = None

    def step(self):
        self.fault_machine()
        self.submit()
        if self.t % 3 == 0:                                        # the HPA every 15 s, its new pods placed in this step
            self.hpa()
        if self.orch == "koordinator":
            self.koordinator_batch()
        self.schedule()
        # a pod waiting for a place: one the scheduler could not place (no machine with room), counted after its pass
        self.pending_s += sum(1 for p in self.pods if p["node"] is None) * DT
        if self.setting["ca"] and self.t % 2 == 0:                 # the Cluster Autoscaler acts on pods the scheduler could
            self.cluster_autoscaler()                              # not place, never on pods not yet tried (amendment 2)
        load = self.share_cpu()
        self.serve(load)
        self.progress()
        live = self.live_nodes()
        in_service = len(live) + len(self.booting) if self.setting["ca"] else sum(1 for n in live if not n["idle"])
        self.mach_s += in_service * DT
        busy = self.busy_hist[-1] if self.busy_hist else 0.0
        if self.setting["host"]:
            self.energy_j += (self.setting["idle_w"] + self.setting["core_w"] * busy * self.setting["host"] / 1000.0) * DT
        else:
            self.energy_j += sum(self.setting["idle_w"] + self.setting["core_w"] * busy * 2.0 for _ in range(in_service)) * DT
        self.t += 1

    def finished(self):
        if self.t * DT < self.dur:
            return False
        if self.has_batch and any(j["done_at"] is None for j in self.jobs):
            return self.t * DT >= 3 * self.dur - DT
        return True

    def gauges(self):
        lat = sorted(self.lat)
        alert = sum(1 for v in self.minute.values() if sorted(v)[int(0.95 * len(v))] > SLO_MS)
        out = {"p95_ms": lat[int(0.95 * len(lat))] if lat else 0.0, "alert_minutes": float(alert),
               "requests_failed": self.failed, "requests_served": self.served,
               "pending_pod_minutes": self.pending_s / 60.0, "machine_hours": self.mach_s / 3600.0,
               "energy_kwh": self.energy_j / 3.6e6}
        if self.has_batch:
            done = [j for j in self.jobs if j["done_at"] is not None]
            out["batch_turnaround_s"] = sum((j["done_at"] - j["born"]) * DT for j in done) / max(1, len(done)) if done else 3 * self.dur
            out["batch_makespan_s"] = (max(j["done_at"] for j in done) * DT) if len(done) == BATCH["jobs"] else 3 * self.dur
            out["batch_pods_done"] = float(sum(BATCH["completions"] - j["left"] - j["running"] for j in self.jobs))
        if not self.lat:                                           # no client sent a request (the batch stream alone)
            for g in ("p95_ms", "alert_minutes", "requests_failed", "requests_served"):
                out.pop(g)
        return out


class Kube:
    """Answers the shipped governor's reads from the organism, as a real cluster answers them, and applies its writes."""

    def __init__(self, org, audit_path):
        self.o, self.audit, self.dry_run, self.unknown = org, None, False, []

    def _node_json(self, n):
        o = self.o
        taints = [{"key": "omnicompass.io/idle", "value": "true", "effect": "PreferNoSchedule"}] if n["idle"] else []
        prov = f"kind://docker/omni-bench/{n['name']}" if o.setting["host"] else f"azure:///{n['name']}"
        return {"metadata": {"name": n["name"], "labels": {}}, "spec": {"taints": taints, "providerID": prov},
                "status": {"allocatable": {"cpu": f"{n['alloc']}m"}, "conditions": [{"type": "Ready", "status": "True"}]}}

    def _pod_json(self, p):
        ready = p["ready_at"] is not None and p["ready_at"] <= self.o.t and p["node"] is not None
        labels = {"run": p["owner"], "app": p["owner"]} if p["kind"] == "svc" else {"app": "omni-batch-stream"}
        ann = {"controller.kubernetes.io/pod-deletion-cost": "-100"} if p.get("cost") else {}
        res = {"requests": {"cpu": f"{p['req']}m"}, "limits": {"cpu": f"{int(p['lim'])}m"}}
        return {"metadata": {"name": p["name"], "namespace": "default", "labels": labels, "annotations": ann,
                             "ownerReferences": [{"kind": "ReplicaSet" if p["kind"] == "svc" else "Job", "name": p["owner"]}]},
                "spec": {"nodeName": p["node"], "containers": [{"name": "app", "resources": res}]},
                "status": {"phase": "Running" if ready else "Pending",
                           "conditions": [{"type": "Ready", "status": "True" if ready else "False"}]}}

    def _hpa_json(self, sv):
        n = len(self.o.svc_pods(sv["name"]))
        return {"metadata": {"name": sv["name"], "namespace": "default", "annotations": dict(sv["ann"])},
                "spec": {"scaleTargetRef": {"kind": "Deployment", "name": sv["name"]}, "minReplicas": sv["min"],
                         "maxReplicas": sv["max"], "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {
                             "type": "Utilization", "averageUtilization": int(sv["target"])}}}]},
                "status": {"currentReplicas": n, "desiredReplicas": sv["desired"], "currentMetrics": [{"type": "Resource",
                           "resource": {"name": "cpu", "current": {"averageUtilization": int(round(sv["metric"]))}}}]}}

    def get(self, *args):
        o = self.o
        if args[:2] == ("get", "nodes"):
            return {"items": [self._node_json(n) for n in o.live_nodes()]}
        if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "name":
            return "\n".join(f"pod/{p['name']}" for p in o.pods if p["node"] is None)
        if args[:2] == ("get", "pods"):
            sel = args[args.index("-l") + 1] if "-l" in args else ""
            pods = o.pods
            if sel:
                k, _, v = sel.partition("=")
                pods = [p for p in pods if self._pod_json(p)["metadata"]["labels"].get(k) == v]
            return {"items": [self._pod_json(p) for p in pods]}
        if args[:2] == ("get", "hpa"):
            return {"items": [self._hpa_json(sv) for sv in o.svcs]}
        if args[:2] == ("get", "deployment"):
            sv = next((x for x in o.svcs if x["name"] == args[2]), None)
            if sv is None:
                raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="not found")
            n = len(o.svc_pods(sv["name"]))
            res = {"requests": {"cpu": f"{SVC['req']}m"}, "limits": {"cpu": f"{SVC['lim']}m"}}
            return {"metadata": {"name": sv["name"], "namespace": "default", "annotations": dict(sv["dann"])},
                    "spec": {"replicas": n, "selector": {"matchLabels": {"run": sv["name"]}},
                             "template": {"metadata": {"labels": {"run": sv["name"]}}, "spec": {"containers": [{"name": "app", "resources": res}]}}},
                    "status": {"replicas": n, "readyReplicas": sum(1 for p in o.svc_pods(sv["name"]) if p["ready_at"] is not None and p["ready_at"] <= o.t)}}
        if args[:2] == ("top", "pods"):
            sel = args[args.index("-l") + 1] if "-l" in args else ""
            k, _, v = sel.partition("=")
            return "\n".join(f"{p['name']} {int(p.get('use', 0))}m 10Mi" for p in o.pods
                             if p["node"] and self._pod_json(p)["metadata"]["labels"].get(k) == v)
        if args[:2] == ("top", "nodes"):
            return "\n".join(f"{n['name']} {int(o.used(n))}m {int(100 * o.used(n) / n['alloc'])}% 1Gi 10%" for n in o.live_nodes())
        if args[:2] == ("get", "jobs"):
            return {"items": []}                                   # no job of the stream carries the pausable label
        self.unknown.append(" ".join(args[:3]))
        raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="forbidden in the model cluster")

    def write(self, args, why):
        o = self.o
        if self.audit:                                             # every write recorded, as the shipped client records it
            self.audit({"write": list(args), "why": why, "dry_run": False})
        if args[:2] == ["patch", "hpa"]:
            sv = next(x for x in o.svcs if x["name"] == args[2])
            body = json.loads(args[args.index("-p") + 1])
            if isinstance(body, list):
                sv["target"] = float(body[0]["value"])
            else:
                sp = body.get("spec", {})
                sv["min"] = int(sp.get("minReplicas", sv["min"])); sv["max"] = int(sp.get("maxReplicas", sv["max"]))
        elif args[:2] == ["annotate", "hpa"]:
            sv = next(x for x in o.svcs if x["name"] == args[2]); kv = args[-1]
            sv["ann"].pop(kv[:-1], None) if kv.endswith("-") else sv["ann"].__setitem__(*kv.split("=", 1))
        elif args[:2] == ["annotate", "deployment"]:
            sv = next((x for x in o.svcs if x["name"] == args[2]), None)
            if sv is not None:
                kv = args[-1]
                sv["dann"].pop(kv[:-1], None) if kv.endswith("-") else sv["dann"].__setitem__(*kv.split("=", 1))
        elif args[:2] == ["patch", "pod"] and "resize" in args:
            val = json.loads(args[args.index("-p") + 1])[0]["value"]
            for p in o.pods:
                if p["name"] == args[2]:
                    p["lim"] = int(str(val).rstrip("m")) if not str(val).endswith("m") or True else p["lim"]
        else:
            self.unknown.append("write " + " ".join(args[:3]))


class HostSampler:
    """The governor's host busy share (omni_controller/capacity.py HostCpuSampler), read from the organism's host."""

    def __init__(self, org):
        self.o, self.busy_share, self._n = org, None, 0

    def sample(self):
        h = self.o.busy_hist[self._n:] if self.o.busy_hist else []
        self._n = len(self.o.busy_hist)
        self.busy_share = sum(h) / len(h) if h else None
        return self.busy_share


def park(org, want):
    """scripts/kind_nodepool.sh N: machines in service brought to N (2 at least), an idled machine marked PreferNoSchedule and
    its served pods given the lower deletion cost; woken, the mark taken off."""
    s = org.setting
    live = org.live_nodes()
    active = [n for n in live if not n["idle"]]
    idle = [n for n in live if n["idle"]]
    want = max(s["min"], min(len(live), int(want)))
    if want > len(active):
        for n in sorted(idle, key=lambda n: -sum(1 for p in org.pods if p["node"] == n["name"]))[:want - len(active)]:
            n["idle"] = False
            for p in org.pods:
                if p["node"] == n["name"]:
                    p["cost"] = 0
    elif want < len(active):
        served = lambda n: sum(1 for p in org.pods if p["node"] == n["name"] and p["kind"] == "svc")
        work = lambda n: sum(1 for p in org.pods if p["node"] == n["name"])
        for n in sorted(active, key=lambda n: (served(n), work(n)))[:len(active) - want]:
            n["idle"] = True
            for p in org.pods:
                if p["node"] == n["name"] and p["kind"] == "svc":
                    p["cost"] = 1


def run_one(organism, setting, orch, arm, k, base=20261025, keep=None):
    """One run: the organism under the orchestrator, native or with Omni-Compass on top; its gauges (keep: a folder that
    keeps the governor's audit and the probe's file)."""
    inj = injection(organism, setting, k, base)
    org = Organism(organism, setting, "default" if arm == "native" else orch, inj)
    ctl, kube = None, None
    tmp = None if keep else tempfile.TemporaryDirectory()
    out = Path(keep) if keep else Path(tmp.name)
    out.mkdir(parents=True, exist_ok=True)
    (out / "audit.jsonl").unlink(missing_ok=True)
    if arm == "omni":
        from omni_controller import controller as shipped
        from omni_controller.controller import Controller, parser
        lat_path = out / "latency.csv"
        s = SETTINGS[setting]
        # the compass law at the max with every muscle in both settings (the founder's order of 31 October: no hard rule; the
        # cloud's tune-down on the machines alone of 14 October, --dial save --sensed none/none --give-back-only, is struck)
        law = ["--law", "compass", "--cap-deployments", "default/php-apache", "--sensed", "default/php-apache"]
        argv = ["--mode", "nodepool", "--active-nodes-only", "--interval", "60", "--floor-interval", str(DT),
                "--reflex-window-s", "15", "--min-nodes", str(s["min"]), "--max-nodes", str(s["max"]), "--max-node-step", "1",
                "--node-scale-cmd", "SIMSCALE {n}", "--latency-file", str(lat_path), "--slo-ms", str(SLO_MS),
                "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "kill"), "--no-api-proxy", *law]
        p = parser()
        known = {o for a in p._actions for o in a.option_strings}
        argv = [x for i, x in enumerate(argv) if not (x.startswith("--") and x not in known)
                and not (i > 0 and argv[i - 1].startswith("--") and argv[i - 1] not in known and not x.startswith("--"))]
        a = p.parse_args(argv)
        kube = Kube(org, None)
        ctl = Controller(a, kube=kube)
        kube.audit = ctl.audit
        ctl.host_cpu = HostSampler(org)
        ctl.m.host_cpu = HostSampler(org)
        real_run = subprocess.run

        def standin_run(cmd, *ka, **kw):
            if isinstance(cmd, list) and cmd and cmd[0] == "SIMSCALE":
                park(org, int(cmd[1])); return subprocess.CompletedProcess(cmd, 0)
            if isinstance(cmd, str) and cmd.startswith("SIMSCALE"):
                park(org, int(cmd.split()[1])); return subprocess.CompletedProcess(cmd, 0)
            return real_run(cmd, *ka, **kw)
        every = int(60 / DT)
        fails = 0
        with mock.patch("omni_controller.controller.subprocess.run", side_effect=standin_run), \
                mock.patch("omni_controller.muscles.subprocess.run", side_effect=standin_run):
            while not org.finished():
                org.step()
                write_latency(lat_path, org)
                if org.t % every == 0:
                    fails = shipped.safe_step(ctl, fails)
                else:
                    try:
                        ctl.floor_step()
                    except Exception as e:  # noqa: BLE001  the shipped loop records a failed check and goes on
                        ctl.audit({"error": "floor check: " + repr(e)[:300]})
    else:
        while not org.finished():
            org.step()
    g = org.gauges()
    if arm == "omni":
        recs = [json.loads(line) for line in open(out / "audit.jsonl")] if (out / "audit.jsonl").exists() else []
        g["_writes"] = sum(1 for r in recs if "write" in r)
        kinds = {}
        for r in recs:
            if "write" in r:
                w = r["write"]
                key = " ".join(str(x) for x in w[:2]) + (" " + str(r.get("why", ""))[:40] if w[:1] != ["SIMSCALE"] else "")
                kinds[key] = kinds.get(key, 0) + 1
        g["_write_kinds"] = kinds
        g["_errors"] = sum(1 for r in recs if "error" in r)
        g["_unknown"] = sorted(set(kube.unknown))[:12]
    if tmp:
        tmp.cleanup()
    return g


def write_latency(path, org):
    """The probe's file the governor reads (elapsed_seconds, latency_ms, ok), its last 15 minutes."""
    rows = org.lat[-int(900 / DT) * SAMPLES:]
    t1 = org.t * DT
    n = len(rows)
    with open(path, "w") as f:
        f.write("elapsed_seconds,latency_ms,ok\n")
        f.writelines(f"{t1 - (n - i) * DT / SAMPLES:.2f},{ms:.3f},1\n" for i, ms in enumerate(rows))


def _job(args):
    organism, setting, orch, arm, k, base = args
    try:
        return args, run_one(organism, setting, orch, arm, k, base)
    except Exception as e:  # noqa: BLE001  a run that fails is recorded with its error, never dropped silently
        return args, {"_failed": repr(e)[:400]}


def read(pairs, aim, resource):
    """The one key on paired differences (tools/readings.py): the mean change in percent of the reference, its 95% interval
    (Student's t), and the word by the gauge's aim; under 0.5% STEADY."""
    from omnicompass.student_t import T95
    base = [a for a, _ in pairs]
    d = [(b - a) for a, b in pairs]
    ref = sum(base) / len(base)
    if not d:
        return None
    mean = sum(d) / len(d)
    sd = math.sqrt(sum((x - mean) ** 2 for x in d) / (len(d) - 1)) if len(d) > 1 else 0.0
    half = T95.get(len(d) - 1, 2.0) * sd / math.sqrt(len(d)) if len(d) > 1 else 0.0
    if abs(ref) < 1e-9:
        pct = 0.0 if abs(mean) < 1e-9 else math.copysign(100.0, mean)
        lo = hi = pct
    else:
        pct, lo, hi = 100.0 * mean / abs(ref), 100.0 * (mean - half) / abs(ref), 100.0 * (mean + half) / abs(ref)
    if abs(pct) < 0.5:
        word = "STEADY"
    else:
        good = pct < 0 if aim == "lower" else pct > 0
        word = "GAIN" if good else ("power given" if resource else "LOSS")
    clear = lo > 0 or hi < 0
    return {"pct": round(pct, 2), "lo": round(lo, 2), "hi": round(hi, 2), "word": word, "beyond_noise": clear,
            "ref": round(ref, 4)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--reps", type=int, default=8)
    ap.add_argument("--base", type=int, default=20261025)
    ap.add_argument("--out", default=str(ROOT / "results" / "orchestrators"))
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--organisms", default=",".join(ORGANISMS))
    ap.add_argument("--settings", default="onsite,cloud")
    ap.add_argument("--orchs", default=",".join(ORCHESTRATORS))
    ap.add_argument("--one", nargs=5, metavar=("ORGANISM", "SETTING", "ORCH", "ARM", "K"))
    a = ap.parse_args(argv)
    if a.one:
        o, s, orch, arm, k = a.one
        print(json.dumps(run_one(o, s, orch, arm, int(k), a.base), sort_keys=True))
        return 0
    orgs, sets, orchs = a.organisms.split(","), a.settings.split(","), a.orchs.split(",")
    jobs = []
    for o in orgs:
        for s in sets:
            for k in range(a.reps):
                jobs.append((o, s, "default", "native", k, a.base))
                for orch in orchs:
                    if orch != "default":
                        jobs.append((o, s, orch, "orch", k, a.base))
                    jobs.append((o, s, orch, "omni", k, a.base))
    runs = {}
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        for i, (key, g) in enumerate(ex.map(_job, jobs, chunksize=1)):
            runs[key] = g
            if (i + 1) % 50 == 0:
                print(f"{i + 1}/{len(jobs)} runs", flush=True)
    from tools.orchestrators_report import write_report
    write_report(runs, a, Path(a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
