#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The heartbeat sweep (our own model, evidence class S; the founder's questions of 22 October: does a decision every 10
or 5 seconds do better than 15, is 20 different, what does a faster beat cost the engine, and what does a beat slower than
60 s do): the shipped controller of a checkout at a decision every 5, 10, 15, 20, 30, 60, 75, 90 and 120 s on one 5-second
plant, against native, in two settings.

  cloud    the cloud's plant (cloud_model below, the model gate's cloud model with the shipped actuator, cut into 5-second steps):
           the cloud's own autoscaler makes and deletes machines in every arm; the governor on top at the max with every
           muscle, as every cloud set runs it from 31 October (the founder's order of that day, no hard rule, struck the
           machines alone of 14 October; the records written before it read the governor on the machines alone).
  onsite   pilot/selfpilot.py's plant cut into 5-second steps: native is the pod autoscaler with the cluster autoscaler;
           with Omni-Compass the governor sizes the pool itself (nodepool mode, the max), as the live page's trace 5e.

The plant, the requests and the response time are this file's for every arm and every engine; the engine is imported from
the checkout under test. The governor's own cost is its own processor time around its decisions and checks, its reads of the
cluster and its writes; its fast check's rescues are the machines it added only after a pod waited (rescues below).

  python3 tools/heartbeat_sweep.py --cand CAND --base BASE --out OUT [--names omni-v17,omni-v16] [--seeds 1-8]
                                   [--periods 5,10,15,20,30,60,75,90,120] [--settings onsite,cloud] [--arms native,cand,base]
  python3 tools/heartbeat_sweep.py --one SETTING ARM SEED PERIOD DIR CAND   (one run, inside the checkout under test)

  python3 tools/heartbeat_sweep.py --table OUT/results.jsonl results/model_gate/HEARTBEAT_SWEEP.md   (the record)

The record of 22 October is results/model_gate/HEARTBEAT_SWEEP.md and its .json: native, omni-v16 (the engine that stands) and
omni-v15 (the engine before it), each row named by the engine it ran on.
"""
import argparse, json, math, os, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve()


SLO_MS = 200.0                       # the model service's line (tools/model_gate.py's)
SERVICE_MS = 20.0                    # the bare service time of one request
SAMPLES_PER_TICK = 20                # requests timed every 15 s
BLINK_EVERY, BLINK = 1440, (700, 708)  # the blink: two minutes (8 ticks of 15 s) out of service every six hours


def cloud_model(seed, days, fine=False, blink=False):
    """The cloud's plant and the cluster as its API shows it: (sim, kube, STEP_S). The model gate's cloud model as it stood on
    22 October with the shipped actuator (CloudSim below: a machine the governor parks is tainted idle and deleted by the cloud
    after ten minutes empty; an idle machine still takes pods), kept here whole so every engine the sweep reads runs on the
    same plant, whatever its own checkout's model gate holds."""
    from pilot.selfpilot import SimCluster, SimKube
    from fleet.harness import hpa_step
    from fleet.sim import ALLOC, _cluster_autoscaler
    IDLE = "omnicompass.io/idle"
    # the plant's step: the harness's 15 s, or 5 s in the fine plant (omni-v16's gate: a decision every 10 s, and every
    # period that divides the minute, falls on a step; the autoscaler and the cloud's autoscaler still sync every 15 s)
    SUB = 3 if fine else 1
    STEP_S = 15.0 / SUB

    class CloudSim(SimCluster):
        """The cloud as the governor meets it (scripts/kind_bench.sh, the cloud setting): the cloud's own autoscaler
        makes machines and deletes an unneeded one, in every arm; the governor only marks a machine that exists idle
        and wakes it, and never adds one. An idle machine is the shipped actuator's (scripts/kind_nodepool.sh, omni-v16's
        gate): marked PreferNoSchedule, Ready, powered and billed; no pod is moved off it; a pod that finds the open
        machines full lands on it at once; once it carries no work it stands empty for the cloud's scale-down time and
        is deleted. (Until omni-v16 the model took an idle machine's room away at once, as if drained, which the actuator
        never does: pods waited there that wait nowhere on a real cluster.)"""
        PARK_TICKS = 40 * SUB                                  # ten minutes: the autoscaler's scale-down-unneeded time

        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.c.pool.power_off = True                       # a machine the cloud scales down is deleted, not kept
            self.parked = []                                   # idle machines, carrying ones first: steps left once empty
            self.u = 0                                         # plant steps taken
            self.steps = self.steps * SUB
            self.acc = {}                                      # each workload's busy share over the autoscaler's 15 s

        def tick(self):
            c, p = self.c, self.c.pool
            t = self.u // SUB                                  # the harness's 15 s demand sample
            sync = (self.u + 1) % SUB == 0                     # this step closes a 15 s window: the autoscalers' sync
            if self.u % SUB == 0:                              # boots count in the harness's 15 s steps (BOOT_TICKS)
                p.booting = [b - 1 for b in p.booting]; p.nodes += sum(1 for b in p.booting if b <= 0)
                p.booting = [b for b in p.booting if b > 0]
            cap = p.cores * ALLOC
            alloc = (p.nodes + len(self.parked)) * cap         # every Ready machine: the idle ones take pods once the open are full
            reqs = sum(w.replicas * w.request for w in c.workloads)
            frac = min(1.0, alloc / reqs) if reqs > 0 else 1.0
            used = 0.0
            for w in c.workloads:
                capw = w.replicas * w.request * frac
                srv = min(w.demand[t] / SUB + w.backlog, capw / SUB)   # a step carries 1/SUB of the 15 s work
                w.backlog = w.demand[t] / SUB + w.backlog - srv; used += srv * SUB
                self.acc.setdefault(w.name, []).append(min(1.0, srv * SUB / max(w.replicas * w.request, 1e-9)))
            c.pending, c.reqs, c.alloc, c.used = max(0.0, reqs - alloc), reqs, alloc, used
            # the idle machines carrying pods (the requests past the open machines' room) stay in service, their clock
            # reset; the empty ones count down to the cloud's own scale-down
            carrying = min(len(self.parked), int(math.ceil(max(0.0, reqs - p.nodes * cap) / cap - 1e-9)))
            self.parked = [self.PARK_TICKS] * carrying + [x - 1 for x in self.parked[carrying:] if x > 1]
            util = min(1.0, used / max(alloc, 1e-9))
            kw = ((p.nodes + len(self.parked)) * (p.idle_kw + p.dyn_kw * util) + len(p.booting) * p.idle_kw) * self.scn.pue
            pending_pods = int(sum(max(0, w.replicas - int(w.replicas * frac)) for w in c.workloads))
            cur = sum(w.replicas for w in c.workloads)
            if sync:
                for w in c.workloads:
                    got = self.acc.pop(w.name, None) or [w.metric]
                    w.metric = sum(got) / len(got)             # the window the autoscaler reads
                    before = w.replicas; hpa_step(w, w.target); w.desired = w.replicas; w.current = before
                if self.autoscaler == "ca":
                    # the cloud's autoscaler: a pod that finds no room even on the idle machines starts one; an unneeded
                    # open machine leaves after its ten minutes (an idle one leaves by its own clock above)
                    c.alloc = p.nodes * cap
                    _cluster_autoscaler(c)
                    c.alloc = alloc
            self.rows.append(["", self.u * STEP_S, p.nodes + len(self.parked), p.nodes + len(self.parked) + len(p.booting),
                              int(alloc / ALLOC * 1000), int(reqs * 1000), int(used * 1000), pending_pods, len(c.workloads),
                              cur, sum(w.desired for w in c.workloads), kw * 1000])
            self.u += 1
            self.t = self.u // SUB

        def billed(self):
            p = self.c.pool
            return p.nodes + len(p.booting) + len(self.parked)

        def resize(self, n):
            p = self.c.pool; n = max(p.min_nodes, int(n))
            if n < p.nodes:
                k = p.nodes - n; p.nodes -= k; self.parked += [self.PARK_TICKS] * k
            elif n > p.nodes:
                # those still carrying work first: they are warm (scripts/kind_nodepool.sh)
                k = min(n - p.nodes, len(self.parked)); p.nodes += k; self.parked = self.parked[k:]

    sim = CloudSim(seed, days, autoscaler="ca")

    def placed():
        """Every running pod on its machine, as the API shows it: the open machines filled first, then the idle ones (a
        pod lands on an idle machine only when the open ones are full); the rest wait, with no machine."""
        c, p = sim.c, sim.c.pool
        frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
        cap = p.cores * ALLOC
        names = [f"n{i}" for i in range(p.nodes)] + [f"n{p.nodes + j}" for j in range(len(sim.parked))]
        room = [cap] * len(names); out_ = []; i = 0
        for w in c.workloads:
            run = int(w.replicas * frac)
            for _ in range(run):
                while i < len(names) - 1 and room[i] < w.request - 1e-9:
                    i += 1
                if names:
                    room[i] -= w.request
                out_.append((w, names[i] if names else None))
            out_ += [(w, None)] * (w.replicas - run)
        return out_, names, room

    class Kube(SimKube):
        def get(self, *args):
            if args[:2] == ("get", "nodes"):                    # in service, then idle-marked until the cloud deletes them
                p = self.sim.c.pool
                node = lambda i, taints: {"metadata": {"name": f"n{i}", "labels": {}},
                                          "spec": {"taints": taints}, "status": {"allocatable": {"cpu": str(p.cores)},
                                          "conditions": [{"type": "Ready", "status": "True"}]}}
                # the blink (omni-v11): four times a day every machine in service leaves service for two minutes in the
                # governor's reading, while the model cluster serves on, as the kind cluster of the CruiseKube test did on 18
                # October (run 39120444653, repetition 8)
                out_now = blink and BLINK[0] <= self.sim.t % BLINK_EVERY < BLINK[1]
                gone = [{"key": "node.kubernetes.io/unreachable", "effect": "NoSchedule"}] if out_now else []
                return {"items": [node(i, list(gone)) for i in range(p.nodes)]
                        + [node(p.nodes + j, [{"key": IDLE, "effect": "PreferNoSchedule"}]) for j in range(len(self.sim.parked))]}
            if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "name":
                c = self.sim.c
                frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
                pend = sum(w.replicas - int(w.replicas * frac) for w in c.workloads)
                return "\n".join(f"pod/p{i}" for i in range(pend))
            if args[:2] == ("get", "pods"):                     # every pod with its machine, as the API shows it
                cpu = lambda w: f"{int(w.request * 1000)}m"
                return {"items": [{"metadata": {"name": f"p{k}", "namespace": "default", "ownerReferences": [{"kind": "ReplicaSet"}]},
                                   "spec": {"nodeName": nm, "containers": [{"resources": {"requests": {"cpu": cpu(w)}}}]} if nm else
                                           {"containers": [{"resources": {"requests": {"cpu": cpu(w)}}}]},
                                   "status": {"phase": "Running" if nm else "Pending"}} for k, (w, nm) in enumerate(placed()[0])]}
            if args[:2] == ("top", "nodes"):                    # each machine's use, by the requests placed on it
                c, p = self.sim.c, self.sim.c.pool
                pods, names, room = placed()
                cap = p.cores * ALLOC
                load_ = {nm: cap - r for nm, r in zip(names, room)}
                tot = sum(load_.values()) or 1.0
                return "\n".join(f"{nm} {int(c.used * load_[nm] / tot * 1000)}m 1% 1Gi 1%" for nm in names if load_[nm] > 1e-9)
            if args[:2] == ("get", "hpa"):                      # the HPA as Kubernetes shows it: its range and target
                hp = super().get(*args)
                for h, w in zip(hp["items"], self.sim.c.workloads):
                    h["spec"].update({"minReplicas": int(w.min_rep), "maxReplicas": int(w.max_rep),
                                      "scaleTargetRef": {"kind": "Deployment", "name": w.name}})
                return hp
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

    return sim, Kube(sim, None), STEP_S


def onsite_model(seed, days, autoscaler):
    from pilot.selfpilot import SimCluster, SimKube
    from fleet.harness import hpa_step
    from fleet.sim import ALLOC, _cluster_autoscaler
    SUB = 3; STEP_S = 15.0 / SUB

    class Fine(SimCluster):
        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.u = 0; self.steps = self.steps * SUB; self.acc = {}; self.parked = []

        def tick(self):
            c, p = self.c, self.c.pool
            t = self.u // SUB
            sync = (self.u + 1) % SUB == 0
            if self.u % SUB == 0:
                p.booting = [b - 1 for b in p.booting]; p.nodes += sum(1 for b in p.booting if b <= 0)
                p.booting = [b for b in p.booting if b > 0]
            alloc = p.nodes * p.cores * ALLOC
            reqs = sum(w.replicas * w.request for w in c.workloads)
            frac = min(1.0, alloc / reqs) if reqs > 0 else 1.0
            used = 0.0
            for w in c.workloads:
                capw = w.replicas * w.request * frac
                srv = min(w.demand[t] / SUB + w.backlog, capw / SUB)
                w.backlog = w.demand[t] / SUB + w.backlog - srv; used += srv * SUB
                self.acc.setdefault(w.name, []).append(min(1.0, srv * SUB / max(w.replicas * w.request, 1e-9)))
            c.pending, c.reqs, c.alloc, c.used = max(0.0, reqs - alloc), reqs, alloc, used
            util = min(1.0, used / max(alloc, 1e-9))
            kw = (p.nodes * (p.idle_kw + p.dyn_kw * util) + len(p.booting) * p.idle_kw) * self.scn.pue
            pending_pods = int(sum(max(0, w.replicas - int(w.replicas * frac)) for w in c.workloads))
            cur = sum(w.replicas for w in c.workloads)
            if sync:
                for w in c.workloads:
                    got = self.acc.pop(w.name, None) or [w.metric]
                    w.metric = sum(got) / len(got)
                    before = w.replicas; hpa_step(w, w.target); w.desired = w.replicas; w.current = before
                if self.autoscaler == "ca":
                    _cluster_autoscaler(c)
            self.rows.append(["", self.u * STEP_S, p.nodes, p.nodes + len(p.booting), int(alloc / ALLOC * 1000), int(reqs * 1000),
                              int(used * 1000), pending_pods, len(c.workloads), cur, sum(w.desired for w in c.workloads), kw * 1000])
            self.u += 1
            self.t = self.u // SUB

        def billed(self):
            p = self.c.pool
            return p.nodes + len(p.booting)

    class Kube(SimKube):
        """pilot/selfpilot.py's SimKube with the fields Kubernetes shows that it leaves out: each HPA's range and target, each
        deployment, the pending pods by name (as tools/model_gate.py's cloud model shows them)."""
        def get(self, *args):
            import subprocess as sp
            if args[:2] == ("get", "hpa"):
                hp = super().get(*args)
                for h, w in zip(hp["items"], self.sim.c.workloads):
                    h["spec"].update({"minReplicas": int(w.min_rep), "maxReplicas": int(w.max_rep),
                                      "scaleTargetRef": {"kind": "Deployment", "name": w.name}})
                return hp
            if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "name":
                c = self.sim.c
                frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
                return "\n".join(f"pod/p{i}" for i in range(sum(w.replicas - int(w.replicas * frac) for w in c.workloads)))
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
                raise sp.CalledProcessError(1, ["kubectl", *args], stderr="not in the model cluster")

    sim = Fine(seed, days, autoscaler=autoscaler)
    return sim, Kube(sim, None), STEP_S


def one(setting, arm, seed, period, out, cand, days=1.0):
    import numpy as np
    from unittest import mock
    from pilot.score import blocks, load
    from fleet.sim import ALLOC
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    (out / "audit.jsonl").unlink(missing_ok=True)
    rng = np.random.default_rng(seed + 7)
    if setting == "cloud":
        sim, k, STEP_S = cloud_model(seed, days, fine=True)
    else:
        sim, k, STEP_S = onsite_model(seed, days, "ca" if arm == "native" else "none")
    SUB = int(round(15.0 / STEP_S))
    billed, lat_rows, minute_ms = [], [], {}
    lat_path = out / "latency.csv"
    reads = [0]

    def time_requests():
        c = sim.c
        frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
        cap = sum(w.replicas * w.request * frac for w in c.workloads)
        dem = sum(w.demand[min(sim.t, len(w.demand) - 1)] for w in c.workloads)
        backlog = sum(w.backlog for w in c.workloads)
        rho = min(0.98, dem / cap) if cap > 0 else 0.98
        mean = SERVICE_MS / (1.0 - rho) + (1000.0 * backlog / cap if cap > 0 else 1e4)
        t0 = sim.u * STEP_S
        kk = sim.u % SUB
        n = int(round((kk + 1) * SAMPLES_PER_TICK / SUB)) - int(round(kk * SAMPLES_PER_TICK / SUB))
        for i in range(n):
            ms = float(mean * rng.lognormal(0.0, 0.25))
            lat_rows.append((t0 + i * STEP_S / n, ms))
            minute_ms.setdefault(int(t0 // 60), []).append(ms)
        del lat_rows[:-60 * SAMPLES_PER_TICK]
        with open(lat_path, "w") as f:
            f.write("elapsed_seconds,latency_ms,ok\n")
            f.writelines(f"{t:.2f},{ms:.3f},1\n" for t, ms in lat_rows)

    def alloc_now():
        return (sim.c.pool.nodes + len(getattr(sim, "parked", []))) * sim.c.pool.cores * ALLOC

    decisions = 0
    gov_cpu = 0.0
    if arm != "native":
        from omni_controller.controller import Controller, parser
        common = ["--interval", str(period), "--floor-interval", str(STEP_S), "--latency-file", str(lat_path),
                  "--slo-ms", str(SLO_MS), "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "kill"),
                  "--node-scale-cmd", "SIMSCALE {n}", "--min-nodes", str(sim.c.pool.min_nodes),
                  "--max-nodes", str(sim.c.pool.max_nodes), "--headroom", "0.5"]
        if setting == "cloud":
            # the max with every muscle on top of the cloud's own autoscaler (the founder's order of 31 October: no hard rule; the
            # runs of 22 October in the record were at the tune-down on the machines alone, --dial save --sensed none/none
            # --give-back-only, the cloud's rule of 14 October, struck that day)
            argv = ["--mode", "nodepool", "--law", "compass", "--dial", "max", *common,
                    "--active-nodes-only", "--max-node-step", "1"]
        else:
            argv = ["--mode", "nodepool", *common]
        ctl = Controller(parser().parse_args(argv), kube=k)
        if setting == "onsite":
            ctl.k.audit = ctl.audit
        get0 = ctl.k.get

        def counted_get(*a, **kw):
            reads[0] += 1
            return get0(*a, **kw)
        ctl.k.get = counted_get
        real_run = subprocess.run

        def standin_run(cmd, *kw_a, **kw):
            if isinstance(cmd, list) and cmd and cmd[0] == "SIMSCALE":
                sim.resize(int(cmd[1])); return subprocess.CompletedProcess(cmd, 0)
            return real_run(cmd, *kw_a, **kw)
        every = max(1, int(round(period / STEP_S)))
        from omni_controller import controller as shipped
        fails = 0
        with mock.patch("omni_controller.controller.subprocess.run", side_effect=standin_run):
            while sim.u < sim.steps:
                sim.tick(); sim.c.alloc = alloc_now()
                time_requests(); billed.append(sim.billed())
                c0 = time.process_time()
                if sim.u % every == 0:
                    fails = shipped.safe_step(ctl, fails) if hasattr(shipped, "safe_step") else (ctl.step() or 0)
                    decisions += 1
                else:
                    try:
                        ctl.floor_step()
                    except Exception as e:
                        ctl.audit({"error": "floor check: " + repr(e)[:500]})
                gov_cpu += time.process_time() - c0
    else:
        while sim.u < sim.steps:
            sim.tick(); time_requests(); billed.append(sim.billed())
    cap = out / "capture.csv"; sim.write_capture(cap)
    rows = load(str(cap))
    day = blocks(rows, 86400 * days + 60, None, None)[0]
    allm = sorted(ms for v in minute_ms.values() for ms in v)
    alert = sum(1 for v in minute_ms.values() if sorted(v)[int(0.95 * len(v))] > SLO_MS)
    res = {"machine_hours": sum(billed) * STEP_S / 3600.0, "kwh_per_core_hour": day["kwh_per_core_hour"],
           "pending_pod_minutes_per_hour": day["pending_pod_minutes_per_hour"], "p95_ms": allm[int(0.95 * len(allm))],
           "p99_ms": allm[int(0.99 * len(allm))], "alert_minutes": float(alert), "decisions": float(decisions),
           "governor_cpu_s": gov_cpu, "cluster_reads": float(reads[0]), "writes": 0.0, "machines_parked": 0.0,
           "errors": 0.0}
    if arm != "native":
        recs = [json.loads(l) for l in open(out / "audit.jsonl")]
        res["writes"] = float(sum(1 for r in recs if "write" in r and not r.get("dry_run")))
        res["machines_parked"] = float(sum(1 for r in recs if r.get("write", [None])[0] == "SIMSCALE"))
        res["errors"] = float(sum(1 for r in recs if "error" in r))
        res["rescues"] = float(rescues(out / "audit.jsonl"))
    print(json.dumps(res))


def run_one(tree, cand, setting, arm, seed, period, d):
    env = {**os.environ, "PYTHONPATH": str(tree)}
    p = subprocess.run([sys.executable, str(HERE), "--one", setting, arm, str(seed), str(period), str(d), str(cand)],
                       cwd=tree, env=env, capture_output=True, text=True, timeout=7200)
    if p.returncode != 0:
        raise RuntimeError(f"{tree} {setting} {arm} {seed} {period}: {p.stderr[-3000:]}")
    return json.loads(p.stdout.strip().splitlines()[-1])


def rescues(audit):
    """The fast check's rescues in one run's audit: the pool commands written because a pod already waited for a place (the
    reason 'scheduling floor (pending pods)', omni_controller/controller.py floor_step), apart from the full decision's own,
    which size the pool ahead of the load. The count says why a slower beat waits more: the decision reads the load less often,
    the load outruns the pool between decisions, and the fast check adds the machine only after a pod waits."""
    n = 0
    with open(audit) as f:
        for line in f:
            r = json.loads(line)
            n += "write" in r and "scheduling floor" in str(r.get("why", ""))
    return n


GAUGES = {"machine_hours": ("lower", True), "kwh_per_core_hour": ("lower", True), "pending_pod_minutes_per_hour": ("lower", False),
          "p95_ms": ("lower", False), "p99_ms": ("lower", False), "alert_minutes": ("lower", False)}
NAMES = {"machine_hours": "Machine-hours", "kwh_per_core_hour": "Energy per used core-hour", "pending_pod_minutes_per_hour":
         "Pods waiting for a place", "p95_ms": "95th percentile response", "p99_ms": "99th percentile response",
         "alert_minutes": "Minutes over the line"}
SETTING = {"onsite": "On-site: native is the pod autoscaler with the cluster autoscaler; with Omni-Compass the governor sizes "
                     "the pool on top of the pod autoscaler (the max)",
           "cloud": "In the cloud: the cloud's own autoscaler makes and deletes machines in every arm; the governor on top (the "
                    "runs of 22 October in this record: on the machines alone, --give-back-only, the cloud's rule of 14 October; "
                    "from 31 October, the founder's order of that day, the max with every muscle, the bill judged)"}


def table(results, out_md):
    """The record: every beat of each engine against native and against the same engine at 60 s, paired by seed, read by the
    gate's own rule (tools/model_gate.py reading: the mean change, its 95% interval over the seeds, the word by the gauge's aim);
    with the engine's own cost a day."""
    import collections
    sys.path.insert(0, str(HERE.parents[1]))
    from tools.model_gate import reading
    from tools.legal import stamp
    rows = [json.loads(l) for l in open(results)]
    by = collections.defaultdict(dict)
    for r in rows:                       # every governed row names the engine it ran on (--names); native's is native
        eng = "native" if r["arm"] == "native" else r["engine"]
        by[(r["setting"], eng, r["period"])][r["seed"]] = r
    engines = sorted({e for (_, e, _) in by if e != "native"}, key=lambda e: [int(x) if x.isdigit() else x for x in e.replace("-", ".").split(".")], reverse=True)
    from tools.readings import by_word
    def pct(x):            # the number carries the word's sign, never the gauge's raw direction (the key, tools/readings.py)
        if x["word"].startswith("STEADY (identical)"):
            return "identical"
        return f"{by_word(100 * x['relative'], x['word'])} {x['word']}"
    beats = sorted({p for (_, e, p) in by if e != "native"})
    say = lambda ps: ", ".join(f"{p:g}" for p in ps[:-1]) + f" and {ps[-1]:g}" if len(ps) > 1 else f"{ps[0]:g}"
    rec, L = {}, [f"# The heartbeat sweep: a decision every {say(beats)} seconds", "",
                  "Our own model (evidence class S): what each beat of the governor does against native, in the cloud and on-site, "
                  "and what it costs the engine; never a benchmark result. The founder's questions of 22 October: does a decision "
                  "every 10 or 5 seconds do better than 15, is 20 different, what does a faster beat cost, and what a beat slower "
                  "than 60 seconds does (75, 90 and 120), to show whether, and why, it gains or loses. Run by "
                  "`tools/heartbeat_sweep.py` (the shipped controller of each checkout on one 5-second plant, eight seeds of a day "
                  "each, paired by seed; each row named by the engine it ran on: " + ", ".join(engines) + "). Each "
                  "reading is the gate's rule (`tools/model_gate.py`): the mean change over the seeds with its 95% interval, the word "
                  "by the gauge's aim (`tools/readings.py`). The engine's own cost is a mean a day: its decisions, its processor "
                  "time, its reads of the cluster and its writes; the fast check's rescues are the pool commands its 5-second check "
                  "wrote because a pod already waited for a place, apart from the full decision's own, which size the pool ahead "
                  "of the load (`rescues`). Run and scored by The Omni-Compass LLC's own code. No outside party has "
                  "reviewed or approved these results.", ""]
    for setting in ("onsite", "cloud"):
        nat = by.get((setting, "native", 15.0), {})
        if not nat:
            continue
        L += [f"## {SETTING[setting]}", ""]
        for eng in engines:
            periods = sorted(p for (st, e, p) in by if st == setting and e == eng)
            if not periods:
                continue
            L += [f"### {eng} against native", "",
                  "| Beat | " + " | ".join(NAMES[g] for g in GAUGES) + " | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day "
                  "| The fast check's rescues a day |", "|---|" + "---|" * (len(GAUGES) + 5)]
            for p in periods:
                cur = by[(setting, eng, p)]
                seeds = sorted(set(cur) & set(nat))
                if len(seeds) < 3:
                    continue
                words = {g: reading(g, [cur[s][g] - nat[s][g] for s in seeds], [nat[s][g] for s in seeds], GAUGES) for g in GAUGES}
                cost = {c: sum(cur[s][c] for s in seeds) / len(seeds) for c in ("decisions", "governor_cpu_s", "cluster_reads", "writes", "rescues")
                        if all(c in cur[s] for s in seeds)}
                def against(q):          # the same engine at the beat q, paired by seed; empty at q itself
                    rq = by.get((setting, eng, q), {})
                    sq = sorted(set(cur) & set(rq))
                    return ({g: reading(g, [cur[s][g] - rq[s][g] for s in sq], [rq[s][g] for s in sq], GAUGES) for g in GAUGES}
                            if p != q and len(sq) >= 3 else {})
                rec[f"{setting}|{eng}|{p:g}"] = {"seeds": seeds, "vs_native": words, "vs_15": against(15.0),
                                                        "vs_60": against(60.0), "cost": cost,
                                                        "mean": {g: sum(cur[s][g] for s in seeds) / len(seeds) for g in GAUGES}}
                L.append(f"| {p:g} s | " + " | ".join(pct(words[g]) for g in GAUGES) +
                         f" | {cost['decisions']:,.0f} | {cost['governor_cpu_s']:.1f} s | {cost['cluster_reads']:,.0f} | {cost['writes']:,.0f} | "
                         + (f"{cost['rescues']:.1f} |" if "rescues" in cost else "— |"))
            L.append("")
            for q in (15, 60):
                L += [f"#### {eng} at each beat against itself at {q} s" + (" (the factory's beat)" if q == 15 else ""), "",
                      "| Beat | " + " | ".join(NAMES[g] for g in GAUGES) + " |", "|---|" + "---|" * len(GAUGES)]
                for p in periods:
                    v = rec.get(f"{setting}|{eng}|{p:g}", {}).get(f"vs_{q}")
                    if v:
                        L.append(f"| {p:g} s | " + " | ".join(pct(v[g]) for g in GAUGES) + " |")
                L.append("")
        rec[f"{setting}|native"] = {g: sum(r[g] for r in nat.values()) / len(nat) for g in GAUGES}
        L += [f"Native's means over the seeds: " + "; ".join(f"{NAMES[g].lower()} {rec[f'{setting}|native'][g]:.3f}" for g in GAUGES) + ".", ""]
    Path(out_md).write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")   # the notice under the title and at the end
    Path(out_md).with_suffix(".json").write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print(f"{out_md}: {len(rec)} rows")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--table":
        return table(sys.argv[2], sys.argv[3])
    if len(sys.argv) > 1 and sys.argv[1] == "--one":
        setting, arm, seed, period, d, cand = sys.argv[2:8]
        return one(setting, arm, int(seed), float(period), d, cand)
    ap = argparse.ArgumentParser()
    ap.add_argument("--cand"); ap.add_argument("--base"); ap.add_argument("--out")
    ap.add_argument("--seeds", default="1-8"); ap.add_argument("--periods", default="5,10,15,20,30,60")
    ap.add_argument("--settings", default="cloud,onsite"); ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--arms", default="native,cand,base", help="which arms to run: native, cand (the candidate), base")
    ap.add_argument("--names", default="candidate,base", help="the engines' names, the candidate's then the base's, written "
                                                                 "into every row (the record names each row by its engine)")
    a = ap.parse_args()
    lo, _, hi = a.seeds.partition("-"); seeds = list(range(int(lo), int(hi or lo) + 1))
    periods = [float(x) for x in a.periods.split(",")]
    cand, base, out = Path(a.cand).resolve(), Path(a.base).resolve(), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    sts = a.settings.split(",")
    arms = a.arms.split(",")
    names = dict(zip(("cand", "base"), a.names.split(",")))
    jobs = [(cand, st, "native", s, 15.0) for st in sts for s in seeds] if "native" in arms else []
    for tree_name, tree in (("cand", cand), ("base", base)):          # the candidate first: it is the answer
        if tree_name not in arms:
            continue
        for st in sts:
            for p in sorted(periods):
                jobs += [(tree, st, tree_name, s, p) for s in seeds]
    from concurrent.futures import ThreadPoolExecutor
    res_path = out / "results.jsonl"
    done = set()
    if res_path.exists():
        for l in res_path.read_text().splitlines():
            r = json.loads(l); done.add((r["setting"], r["arm"], r["seed"], r["period"]))
    todo = [j for j in jobs if (j[1], j[2], j[3], j[4]) not in done]
    t0 = time.time()

    def go(j):
        tree, st, arm, s, p = j
        r = run_one(tree, cand, st, "native" if arm == "native" else "omni", s, p, out / st / f"{arm}-{p:g}-{s}")
        r.update(setting=st, arm=arm, seed=s, period=p, engine="native" if arm == "native" else names[arm])
        with open(res_path, "a") as f:
            f.write(json.dumps(r) + "\n")
        print(f"{time.time() - t0:7.0f}s {st:6s} {arm:6s} {p:4g}s seed {s}: machines {r['machine_hours']:.2f} h, pending "
              f"{r['pending_pod_minutes_per_hour']:.3f}, p95 {r['p95_ms']:.1f} ms, decisions {r['decisions']:.0f}, "
              f"cpu {r['governor_cpu_s']:.1f} s", flush=True)
        return r
    with ThreadPoolExecutor(a.jobs) as ex:
        list(ex.map(go, todo))


if __name__ == "__main__":
    main()
