# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass live controller for a real Kubernetes cluster.

Modes
  observe   read the cluster every interval, run the fleet-mode governor in OBSERVE, log every decision; no writes (default)
  target    additionally patch each HPA's CPU averageUtilization to rho* (bounded, rate-limited); the Cluster Autoscaler and
            all node management remain unchanged
  nodepool  additionally size one node pool to the governor's recommendation through --node-scale-cmd, a command template
            such as "aws autoscaling set-desired-capacity --auto-scaling-group-name POOL --desired-capacity {n}"; the
            Cluster Autoscaler must not manage that pool
Laws (--law)
  governor  (default) the engine's allocation law sets the HPA target (rho*) and the closure law or the governor sizes the pool
  compass      the compass law (omnicompass/compass_law.py) holds the service in its band, read as the GPU compass reads it: the mean
            response time of the latency window between the bare service time (a tenth of --slo-ms) and --slo-ms. At the
            max (--dial max, the default) the balance point stands at --compass-center (0.3: well inside the line, so every
            rush finds its pods already there) and no machine the cluster had on its own is ever given back; at the
            tune-down (--dial save) it is held at the v5 edge (omnicompass/edge.py: the balance point moves with the
            service's own risk, 1 - (climb x reaction + 3.09 x wobble), never below 0.4 unless a breach while machines were
            given back has taught it otherwise) and the verdict below gives machines back; p95 at or past the SLO, a blind
            sense or pods waiting for a place read as past the wall. Its push and pull move two levers: each HPA's CPU target inside its cover (from 60% of the
            operator's target up to the operator's own, never tighter than native, so it only ever adds pods and gives them
            back) and the node pool (one machine back only while the force is clearly down, the position below the center
            and the nervous system's release gate open; past the 0.95 wall, one machine up at once). The verdict
            (omnicompass/verdict.py, stepwise) decides how many machines may be given back at all: while the service is
            calm, one more machine is given back on trial and the response time of the requests served without it is set
            against the requests served just before and against the cluster as it ran on its own at the start; at most
            --allow slower and that machine stays given back, slower than that and it is taken back and not tried again
            for --verdict-recheck decisions. Where no machine passes, the pool stays as the cluster runs it alone. The
            six-state engine still runs every decision: it grants the authority, feeds the release gate and the compass,
            and is audited
Safety
  every node action passes through the shield (bounds, step limit); the recommendation never falls below what the CPU
  requests of running and pending pods, or current usage, need, and capacity required by that floor is added in one step
  (the step limit applies only to the governor's own adjustments); --dry-run logs intended writes without executing them; creating the kill file (or
  setting OMNI_KILL=1) restores every HPA target this controller changed, runs --node-restore-cmd if given, and returns to
  observe; every decision and action
  is appended to the audit log.
Requires kubectl on PATH with access to the cluster (metrics-server for kubectl top).
"""
from __future__ import annotations

import argparse, csv, json, math, os, re, shlex, subprocess, sys, time
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass import master
from omnicompass.adapter import Governor, mode_law, OBSERVE, REF_PERIOD_S
from omnicompass.shield import enforce, ShieldLimits
from omni_controller.muscles import Muscles, add_args as add_muscle_args, run_operator_cmd, RESTORE_TRIES
from omni_controller.capacity import HostCpuSampler, bounded_replica_cap, kind_replica_ceiling, one_host

ANNOTATION = "omnicompass.io/original-target-utilization"
RELEASE_PERIOD_S = 60.0   # the pool gives back at most one machine a minute (v7: a rate in time, not in decisions)
ADD_PERIOD_S = 60.0       # omni-v16: and adds at most --max-node-step machines a minute past the scheduling floor
LAND_S = 60.0             # omni-v16: a command is given a minute to land before proprioception lets it go
COMPASS_UP, COMPASS_DOWN, COMPASS_RELEASE = 0.10, 0.02, -0.2   # the compass's gains, the same on every muscle (realms/compass_arm.py)
DEMAND_RISE = 0.05     # the demand moves: more than 5% between its least and its most over one HPA window
RANGE_ANN = "omnicompass.io/original-replica-range"
# the pod muscle of its own (Omni-Compass by itself, docs/SOLO_PREREGISTRATION.md): the operator names a workload no autoscaler
# governs (--own-replicas) and its target and range on the workload itself; the count it shipped is recorded at the first write
OWN_REPL_ANN = "omnicompass.io/original-own-replicas"
OWN_TARGET_ANN = "omnicompass.io/target-utilization"
OWN_RANGE_ANN = "omnicompass.io/replica-range"
# omni-v23 (the founder's order of 31 October: every muscle Omni-Compass cannot be stays; a knob left with no working controller
# fails the whole system): a write of the workload's own scale the cluster refuses this many times in a row hands the knob back
# to native's own pod autoscaler, made from the operator's own target and range recorded on the workload
OWN_REFUSALS = 3


def to_milli(v: str) -> float:
    v = str(v).strip()
    if v.endswith("m"):
        return float(v[:-1])
    if v.endswith("n"):
        return float(v[:-1]) / 1e6
    return float(v) * 1000.0


# the reads the controller makes, as API paths (group/version, plural, namespaced): through one `kubectl proxy` started
# once (the same identity as every kubectl call), a read costs a local HTTP request instead of a new kubectl process
REST = {"nodes": ("api/v1", "nodes", False), "node": ("api/v1", "nodes", False),
        "pods": ("api/v1", "pods", True), "pod": ("api/v1", "pods", True),
        "configmap": ("api/v1", "configmaps", True), "configmaps": ("api/v1", "configmaps", True),
        "resourcequota": ("api/v1", "resourcequotas", True),
        "deployment": ("apis/apps/v1", "deployments", True), "deployments": ("apis/apps/v1", "deployments", True),
        "statefulset": ("apis/apps/v1", "statefulsets", True),
        "jobs": ("apis/batch/v1", "jobs", True), "job": ("apis/batch/v1", "jobs", True),
        "hpa": ("apis/autoscaling/v2", "horizontalpodautoscalers", True)}


def milli_cpu(q):
    """A metrics-API CPU quantity (n, u, m or cores) as kubectl top prints it: millicores."""
    q = str(q)
    if q.endswith("n"):
        return f"{int(int(q[:-1]) / 1e6)}m"
    if q.endswith("u"):
        return f"{int(int(q[:-1]) / 1e3)}m"
    if q.endswith("m"):
        return q
    return f"{int(float(q) * 1000)}m"


class Kube:
    def __init__(self, kubectl: str = "kubectl", dry_run: bool = False, audit=None, proxy: bool = False):
        self.kubectl, self.dry_run, self.audit = kubectl, dry_run, audit
        self.base = None
        if proxy:
            self._start_proxy()

    def _start_proxy(self):
        import atexit
        p = subprocess.Popen([self.kubectl, "proxy", "--port=0"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        line = p.stdout.readline()                 # "Starting to serve on 127.0.0.1:PORT"
        if "serve on" not in line:
            p.kill()
            return                                 # no proxy: every read stays a kubectl call, as before
        self.base = "http://" + line.strip().split()[-1]
        self.proxy_proc = p
        atexit.register(p.terminate)

    def _rest(self, args):
        """The read through the proxy, in kubectl's own output shape, or None when it is not one the proxy serves."""
        import urllib.parse, urllib.request, urllib.error
        a = list(args)
        if not a:
            return None
        verb, rest = a[0], a[1:]
        if verb not in ("get", "top") or not rest:
            return None
        kind, rest = rest[0], rest[1:]
        ns, name, sel, fsel, out, allns = None, None, None, None, None, False
        i = 0
        while i < len(rest):
            t = rest[i]
            if t == "-A":
                allns = True
            elif t == "-n":
                ns = rest[i + 1]; i += 1
            elif t == "-l":
                sel = rest[i + 1]; i += 1
            elif t.startswith("--field-selector="):
                fsel = t.split("=", 1)[1]
            elif t == "-o":
                out = rest[i + 1]; i += 1
            elif t == "--no-headers":
                pass
            elif t.startswith("-"):
                return None                        # a flag the proxy path does not translate: use kubectl
            elif name is None:
                name = t
            else:
                return None
            i += 1
        if verb == "top":
            if kind not in ("nodes", "pods") or name:
                return None
            path = "apis/metrics.k8s.io/v1beta1/" + ("nodes" if kind == "nodes" else (f"namespaces/{ns}/pods" if ns else "pods"))
        else:
            if kind not in REST or out not in ("json", "name"):
                return None
            group, plural, namespaced = REST[kind]
            path = f"{group}/" + (f"namespaces/{ns or 'default'}/" if namespaced and not allns else "") + plural
            if name:
                path += "/" + name
        q = {k: v for k, v in (("labelSelector", sel), ("fieldSelector", fsel)) if v}
        url = f"{self.base}/{path}" + ("?" + urllib.parse.urlencode(q) if q else "")
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                body = json.loads(r.read())
        except urllib.error.HTTPError as e:
            raise subprocess.CalledProcessError(1, [self.kubectl, *args], stderr=f"API {e.code} for {path}")
        if verb == "top":
            if kind == "nodes":
                return "".join(f"{it['metadata']['name']} {milli_cpu(it['usage']['cpu'])} 0% 0Mi 0%\n" for it in body.get("items", []))
            return "".join(f"{it['metadata']['name']} {milli_cpu(sum(int(milli_cpu(c['usage']['cpu'])[:-1]) for c in it['containers']) / 1000)} 0Mi\n"
                           for it in body.get("items", []))
        if out == "name":
            single = REST[kind][1][:-1]
            return "".join(f"{single}/{it['metadata']['name']}\n" for it in body.get("items", [body] if name else []))
        return body

    def get(self, *args):
        if self.base:
            r = self._rest(args)
            if r is not None:
                return r
        out = subprocess.run([self.kubectl, *args], capture_output=True, text=True, check=True).stdout
        return json.loads(out) if "-o" in args and "json" in args else out

    def write(self, args, why):
        self.audit({"write": [self.kubectl, *args], "why": why, "dry_run": self.dry_run})
        if not self.dry_run:
            subprocess.run([self.kubectl, *args], capture_output=True, text=True, check=True)


IDLE_TAINT = "omnicompass.io/idle"   # PreferNoSchedule: new pods go elsewhere first, but land here at once if they must


def closed(n):
    """A machine I have closed to new work: marked idle (PreferNoSchedule) or cordoned."""
    spec = n.get("spec", {})
    return bool(spec.get("unschedulable")) or any(t.get("key") == IDLE_TAINT for t in spec.get("taints") or [])


def schedulable(n):
    """Open to new work: not closed by me, and not tainted NoSchedule (the control plane)."""
    spec = n.get("spec", {})
    return not closed(n) and not any(t.get("effect") == "NoSchedule" for t in spec.get("taints") or [])


CP_ROLES = ("node-role.kubernetes.io/control-plane", "node-role.kubernetes.io/master")


def is_ready(n):
    return any(c["type"] == "Ready" and c["status"] == "True" for c in n["status"].get("conditions", []))


def worker(n):
    """A machine the services' pods may run on: not the control plane (its role label, or its role's NoSchedule taint)."""
    labels = (n.get("metadata", {}) or {}).get("labels", {}) or {}
    if any(r in labels for r in CP_ROLES):
        return False
    return not any(t.get("key") in CP_ROLES and t.get("effect") == "NoSchedule" for t in (n.get("spec", {}) or {}).get("taints") or [])


UNBOUNDED = sys.maxsize   # no top but what the system itself refuses (the founder's rule of 13 October: from 1 up, unbounded)


# the muscles the operator can leave native, one by one (omni-v14; the founder's order of 20 October: "knobs on every monitor
# to turn off and on such a mechanism, a muscle"). A muscle named here is never written by the governor: it stays where native
# runs it, and every other muscle runs as before. The engine decides with the whole body in view either way.
MUSCLES = {"machines": "the node pool's size (the operator's node-scale command)",
           "replicas": "the pod autoscaler's target, the pod reflex's replica floor and the replica cap",
           "cpu": "the serving pods' CPU limits (the conveyance and the pod power cap)",
           "clock": "the processors' frequency ceiling", "gpu": "the GPU's power limit",
           "rollout": "the rollout guard (pause and undo)", "batch": "the batch admission and pacing",
           "rightsize": "the pods' rightsizing", "coldstart": "the cold-start reserve", "contain": "the namespaces' containment",
           "cooling": "the cooling setpoint"}


def native_muscles(text) -> frozenset:
    """The muscles left native, from --native (or OMNI_NATIVE): a comma list of MUSCLES' names; an unknown name is refused,
    never ignored, so a muscle the operator meant to leave native is never driven by a misspelling."""
    names = frozenset(x.strip() for x in str(text or "").split(",") if x.strip())
    bad = sorted(names - set(MUSCLES))
    if bad:
        raise SystemExit(f"--native: unknown muscle {', '.join(bad)} (the muscles: {', '.join(MUSCLES)})")
    return names


def autoscaler_room(k):
    """The machines the cluster's own autoscaler may still add, read live from its status (kube-system/
    cluster-autoscaler-status: per node group, its maxSize less the machines registered); None where no autoscaler reports
    (kind, a fixed pool, a pool Omni resizes with the operator's own command). The founder's rule of 13 October: a
    muscle's top is what the system itself can hold, read live."""
    try:
        text = str(((k.get("get", "configmap", "cluster-autoscaler-status", "-n", "kube-system", "-o", "json") or {})
                    .get("data", {}) or {}).get("status", ""))
    except Exception:
        return None
    if not text.strip():
        return None
    room = 0
    for line in text.splitlines():                                    # the plain format: one node group's health per line
        m = re.search(r"registered=(\d+).*?maxSize=(\d+)", line)
        if m:
            room += max(0, int(m.group(2)) - int(m.group(1)))
    if room == 0 and "maxSize:" in text:                              # the YAML format of newer autoscalers
        for block in re.split(r"\n\s*-\s*name:", text)[1:]:
            mx = re.search(r"maxSize:\s*(\d+)", block)
            reg = re.search(r"registered:\s*\n\s*total:\s*(\d+)", block)
            if mx and reg:
                room += max(0, int(mx.group(1)) - int(reg.group(1)))
    return room


def snapshot(k: Kube, active_only: bool = False):
    nodes = k.get("get", "nodes", "-o", "json")["items"]
    ready = [n for n in nodes if is_ready(n)]
    pool = sum(1 for n in ready if worker(n))                         # every ready worker, open or closed: the lever's pool
    pods = k.get("get", "pods", "-A", "-o", "json")["items"]
    if active_only:
        # in service: open to new work, or still carrying work (an idling worker keeps serving until its work is gone)
        carrying = {p["spec"].get("nodeName") for p in pods if p["status"].get("phase") in ("Running", "Pending")
                    and all(o.get("kind") != "DaemonSet" for o in p.get("metadata", {}).get("ownerReferences", []) or [])}
        ready = [n for n in ready if schedulable(n) or (closed(n) and n["metadata"]["name"] in carrying)]
    # open: the machines I keep open to new work. My machine orders are counted here; a machine I closed that still
    # carries work stays in service (in the energy count) until its work leaves on its own
    open_n = sum(1 for n in ready if schedulable(n))
    names = {n["metadata"]["name"] for n in ready}
    alloc = sum(to_milli(n["status"]["allocatable"]["cpu"]) for n in ready)
    req = sum(to_milli(c.get("resources", {}).get("requests", {}).get("cpu", "0")) for p in pods
              if p["status"].get("phase") in ("Running", "Pending")
              and (not active_only or p["status"].get("phase") == "Pending" or p["spec"].get("nodeName") in names)
              for c in p["spec"]["containers"])
    pending = sum(1 for p in pods if p["status"].get("phase") == "Pending")
    top = k.get("top", "nodes", "--no-headers")
    used = sum(to_milli(line.split()[1]) for line in top.strip().splitlines()
               if line.strip() and (not active_only or line.split()[0] in names))
    hpas = k.get("get", "hpa", "-A", "-o", "json")["items"]
    return {"nodes": len(ready), "open": open_n if active_only else len(ready), "alloc_m": alloc, "req_m": req, "used_m": used, "pending": pending, "hpas": hpas,
            "pool": pool}


def cpu_target(h):
    for i, m in enumerate(h["spec"].get("metrics", [])):
        if m.get("type") == "Resource" and m["resource"]["name"] == "cpu" and "averageUtilization" in m["resource"]["target"]:
            return i, int(m["resource"]["target"]["averageUtilization"])
    return None, None


class Controller:
    def __init__(self, a, kube: Kube | None = None):
        self.a = a
        a.native_muscles = native_muscles(getattr(a, "native", ""))        # omni-v14: the muscles left native
        if a.native_muscles:
            a.pod_reflex_writes = False if "replicas" in a.native_muscles else getattr(a, "pod_reflex_writes", False)
            a.strict_replicas = False if "replicas" in a.native_muscles else getattr(a, "strict_replicas", False)
            a.replica_ceiling = 0 if "replicas" in a.native_muscles else getattr(a, "replica_ceiling", -1)
        # v7: every rule of the governor counts in seconds; its count of decisions follows from the decision period, so
        # the period can change without changing any rule's time (at --interval 60 every count is the one v6 used)
        # --interval 0 is a model's or a test's loop that does not sleep: each call is one decision of the shipped minute
        period = float(a.interval) if float(a.interval) > 0 else 60.0
        per = lambda sec: max(1, int(round(float(sec) / period)))
        pick = lambda n, sec: int(n) if n is not None else per(sec)
        self.n_slo_clear = pick(getattr(a, "slo_clear", None), getattr(a, "slo_clear_s", 180.0))
        # cruise waits for work that waits decision after decision: two readings at least, at any beat (omni-v17: at 90 and
        # 120 s its 120 s rounded to one decision, and a single reading with a pod waiting put every machine in service)
        self.n_cruise_after = (int(a.cruise_after) if getattr(a, "cruise_after", None) is not None
                               else max(2, per(getattr(a, "cruise_after_s", 120.0)))) \
            if getattr(a, "cruise_after", None) != 0 else 0
        self.n_strict_window = pick(getattr(a, "strict_window", None), getattr(a, "strict_window_s", 300.0))
        self.n_verdict_every = pick(getattr(a, "verdict_every", None), getattr(a, "verdict_every_s", 600.0))
        self.n_verdict_recheck = pick(getattr(a, "verdict_recheck", None), getattr(a, "verdict_recheck_s", 7200.0))
        self.n_verdict_trial = per(getattr(a, "verdict_trial_s", 1200.0))
        self.step_scale = period / 60.0                # the compass's gains are per minute: a decision moves its share of one
        self.n_release = per(RELEASE_PERIOD_S)         # decisions between two machines given back (at most one a minute)
        # omni-v16: the rest of the governor's clocks in seconds as well, so the decision period changes only how often it
        # looks: the brain's minute, the compass's damping and smoothing, the edge, the additions, a command's time to
        # land, the host's busy share and the conveyance (at --interval 60 every value is the one omni-v15 used)
        self.pace = period / REF_PERIOD_S              # one decision's share of the brain's minute
        self.n_add = per(ADD_PERIOD_S)                 # decisions between two additions past the scheduling floor
        self.n_land = per(LAND_S)                      # decisions a command is watched for landing
        self.n_convey = max(1, int(round(float(getattr(a, "convey_every_s", 15.0)) / float(getattr(a, "floor_interval", 15.0) or 15.0))))
        # omni-v19: the pod muscle of its own keeps the pace of the controller it stands in for (the pod autoscaler syncs every
        # 15 s), whatever the decision period: a reconciliation every --own-every-s on the fast checks, its window of fewer pods
        # counted in those reconciliations (the strict window's seconds); the compass moves its target only in a decision
        self.n_own = max(1, int(round(float(getattr(a, "own_every_s", 15.0)) / float(getattr(a, "floor_interval", 15.0) or 15.0))))
        sw_s = float(a.strict_window) * period if getattr(a, "strict_window", None) is not None else float(getattr(a, "strict_window_s", 300.0))
        self.n_own_window = max(1, int(round(sw_s / max(1e-9, float(getattr(a, "own_every_s", 15.0))))))
        self.own_checks = 0                            # fast checks taken: the pod muscle of its own's clock between decisions
        self._own_last = None                          # (snapshot, observation, rho) of the last decision, for the checks between
        self.last_add = None                           # the decision at which the pool last added a machine
        self.cmd_at = {}                               # "nodes" or (ns, hpa) -> the decision its last command was written at
        self.checks = 0                                # checks taken, a fast check or a decision: the conveyance's clock
        self.decisions = 0                             # decisions taken, the governor's own clock for the rules above
        self.last_release = None                       # the decision at which the pool last gave a machine back
        self.log = open(a.audit, "a") if a.audit else None
        self.k = kube or Kube(a.kubectl, a.dry_run, self.audit, proxy=not getattr(a, "no_api_proxy", False))
        self.k.audit = self.audit
        # shared-host signal for kind (None means no scale-out proof), the busy share over the last minute (omni-v16)
        self.host_cpu = HostCpuSampler(span=per(60.0))
        self.g = Governor(law=mode_law("fleet"), period_s=period); self.g.set_mode(OBSERVE)
        # the machine organ's own engine view: fed with machine-attributable pressure only (pods waiting for a place)
        self.gn = Governor(law=mode_law("fleet"), period_s=period); self.gn.set_mode(OBSERVE)
        self.rec_n = None
        self.refused_at = None         # the first machine count the pool refused (its top, read live), if any
        self.changed = {}
        self.target_at = {}            # (ns, hpa) -> when I last set its target
        self.nodes_restored = False
        self.m = Muscles(self.k, a, self.audit)
        if a.native_muscles:
            self.audit({"native_muscles": sorted(a.native_muscles), "why": "left native by the operator (--native): never written"})
        self.cl = None
        if getattr(a, "closure", ""):
            from omnicompass.closure import ClosureLaw, ClosureNodes
            law = json.load(open(a.closure))
            law = law.get("setting", law).get("closure", law)
            law = {k: v for k, v in law.items() if k != "site"}
            # live decisions are 60 s apart, not simulator ticks: a rise the release band absorbs over the release horizon
            # does not veto a release (derived from the band itself, no new constant)
            from omnicompass.nervous_system import BAND
            law["rho_max"] = min(law.get("rho_max", 0.95), BAND[1])     # the living band: no machine filled past 95%
            law.setdefault("turn_rise", law.get("delta_rel", -1.0) if law.get("delta_rel", -1.0) >= 0 else law.get("delta", 0.05))
            self.cl = ClosureNodes(ClosureLaw(**law))
        self.lp_hist = []
        self.cmd_nodes = None          # efferent record: the node count last commanded (proprioception reads it back)
        self.cmd_hpa = {}              # efferent record: HPA targets last written
        self.pod_hold = {}             # (ns, hpa) -> (until, seconds): the pod target held at native's after a pod waited (omni-v19)
        self.waited = False            # a fast check saw a pod waiting for a place since the last decision (omni-v19)
        self.req_seen = []             # the requests on the machines at the last decisions, newest last (omni-v19)
        self.burst_m = 0.0             # the largest rise in requests seen inside two decisions: the immune memory (omni-v19)
        self.dem_seen = {}             # (ns, hpa) -> the service's demand at the last decisions, newest last (omni-v19)
        self.immune = {}               # (ns, hpa) -> its knob's self-knowledge (omnicompass/immune.py, omni-v21)
        self.dem_rise = {}             # (ns, hpa) -> the largest rise in its demand inside two decisions, as a ratio (omni-v19)
        self.hold_n = {}               # (ns, hpa) -> hand-backs in a row: each doubles the hold, up to two hours
        from omnicompass.compass import Compass
        gp = self.g.p                  # the compass reads the engine in the engine's own parameters
        self.compass = Compass(E_max=gp.E_max, alpha_s=gp.alpha_s, beta_s=gp.beta_s, delta=gp.delta)
        self.s_floor = None            # bare service time (ms): the fastest a request is served with no queue ahead of it
        self.reflex = {}               # (ns, name) -> replica floor the pod reflex holds while the queue says it is needed
        self.pod_cap = {}              # (ns, name) -> request / limit share: what the HPA's target means in queue terms
        self.compass_law = None
        self.edge = None
        self.dial = getattr(a, "dial", "max")
        if getattr(a, "law", "governor") == "compass":
            from omnicompass.compass_law import Band, CompassLaw
            # the max (the default dial): the service held well inside its line (the compass's balance point at
            # --compass-center, 0.3 at the max: more room than the line, so every rush finds pods already there), no
            # machine ever given back below what the cluster ran on its own; the tune-down (--dial save): the v5 edge
            # moves the balance point toward the line and the verdict gives machines back where the response time allows
            center = getattr(a, "compass_center", None)
            if center is None:
                center = 0.3 if self.dial == "max" else 0.4
            # one decision every --interval s; the service follows a target in about one HPA sync plus a pod start (tau).
            # The damping and the velocity's smoothing are set for a decision a minute and kept in time at any period
            # (omni-v16): kd is critical damping at the minute (compass_law.py's rule with dt = 60 s; the compass's moves
            # are per minute, step_scale), and the smoothing 0.3 a minute
            tau = getattr(a, "compass_tau", 60.0)
            self.compass_law = CompassLaw(Band(0.0, 1.0, center=center), dt=period, tau=tau, kp=1.0,
                                          kd=max(0.0, 2.0 * math.sqrt(1.0 * tau / REF_PERIOD_S) - 1.0) * REF_PERIOD_S,
                                          smooth=0.3 if self.pace == 1.0 else 0.3 ** self.pace)
            self.compass_law.kd *= 3.0                    # the same push as on every realm muscle (realms/compass_arm.py)
            # the v5 edge (the tune-down only): the knob's reaction is the time the service takes to follow it (one HPA
            # sync and a pod start, --compass-tau), in decisions; its window and rates per minute (omni-v16)
            from omnicompass.edge import Edge
            self.edge = Edge(react=tau / period, pace=self.pace) if self.dial == "save" else None
            self.edge_base = center
            from omnicompass.verdict import Verdict
            self.verdict = Verdict(tolerance=getattr(a, "allow", 0.02), min_samples=getattr(a, "verdict_samples", 200),
                                   probe_every=self.n_verdict_every, recheck=self.n_verdict_recheck,
                                   max_trial=self.n_verdict_trial, incremental=True)
            # immune maturity (omni-v19): no give-back trial before the governor has watched its organism for one recheck
            # period, so the immune memory has seen the organism's own rises before the first machine is given back
            self.verdict.last_probe = self.n_verdict_recheck - self.n_verdict_every
        self.n_native = None           # the machines the cluster ran on its own when Omni started (the verdict's step 0)
        self.cruise = False            # cruise (rule 7): work waiting for a place, so every machine in service until the line is empty
        self.cruise_hits = 0; self.cruise_clear = 0
        self.lat_t = None              # elapsed_seconds of the last request the verdict has seen
        self.compass_law_x = {}               # (ns, name) -> the compass's continuous HPA target, before rounding
        self.own = [tuple(x.split("/", 1)) if "/" in x else ("default", x) for x in filter(None, (getattr(a, "own_replicas", "") or "").split(","))]
        self.own_x = {}                # (ns, name) -> the compass's continuous target for a workload of its own, before rounding
        self._own_F = 0.0              # the compass's force of the last decision
        self.own_hist = {}             # (ns, name) -> the recommendations of the last window (fewer pods only to their highest)
        self.own_refused = {}          # (ns, name) -> writes of its scale the cluster refused in a row (omni-v23)
        self.own_handed = set()        # (ns, name) handed back to native's own autoscaler after OWN_REFUSALS refusals (omni-v23)
        self.demand = {}               # (ns, hpa) -> [(time, demand)]: the CPU its pods use, in units of one pod's request
        self.pinned = {}               # (ns, hpa) -> [time]: decisions at which the autoscaler stood at its replica cap

    def _sensed(self, h):
        """Whether the probe senses the service this HPA scales (--sensed ns/deployment,...; empty: every HPA, the
        single-service case). A muscle whose service I cannot sense stays at the operator's own target: the probe's
        response time says nothing about it, and more pods for it compete for the machines of the service I do sense."""
        sel = [t.strip() for t in getattr(self.a, "sensed", "").split(",") if t.strip()]
        ref = (h.get("spec", {}).get("scaleTargetRef", {}) or {}).get("name", "")
        return not sel or f'{h["metadata"]["namespace"]}/{ref}' in sel

    def _app_demand(self, h):
        """The demand on an HPA's service, read from the autoscaler's own status: its pods' mean CPU utilisation (of
        their request) times the pods running, i.e. the CPU used in units of one pod's request. None if not reported."""
        st = h.get("status", {}) or {}
        for m in st.get("currentMetrics", []) or []:
            if m.get("type") == "Resource" and (m.get("resource") or {}).get("name") == "cpu":
                u = (m["resource"].get("current") or {}).get("averageUtilization")
                if u is not None:
                    return float(u) / 100.0 * int(st.get("currentReplicas", 0) or 0)
        return None

    def _at_idle(self, h):
        """Whether an HPA's service stands at idle: at its least pods (spec.minReplicas), wanting no more, and running at
        no more than half its target utilisation. A served service is never at zero CPU (a health probe, a client's
        keep-alive), so idle is read from the autoscaler's own floor, not from a zero reading (amendment 9)."""
        lo = int((h.get("spec", {}) or {}).get("minReplicas", 1) or 1)
        st = h.get("status", {}) or {}
        cur, want = int(st.get("currentReplicas", 0) or 0), int(st.get("desiredReplicas", 0) or 0)
        _, target = cpu_target(h)
        u = None
        for m in st.get("currentMetrics", []) or []:
            if m.get("type") == "Resource" and (m.get("resource") or {}).get("name") == "cpu":
                u = (m["resource"].get("current") or {}).get("averageUtilization")
        return cur == lo and want <= lo and u is not None and target is not None and float(u) <= 0.5 * float(target)

    def _rising(self, key, win):
        """Whether the demand is still growing: now above (1 + DEMAND_RISE) times its least over the last window.
        While it grows, the pods a breach called are still owed to it; handing the operator's target back would remove
        them and start them again on the next rise."""
        now = time.time(); h = self.demand.get(key, []); past = [d for t, d in h if now - t <= win]
        return bool(past) and h[-1][1] > (1.0 + DEMAND_RISE) * min(past)

    def _steady(self, key, win):
        """Whether the demand has held still for one whole window: samples spanning it, its most within (1 +
        DEMAND_RISE) of its least. The autoscaler itself removes pods only after its scale-down window; a raise of the
        target (fewer, larger pods) waits for the same, so pods are never removed from a demand that is still moving
        and started again when it rises."""
        now = time.time(); h = [(t, d) for t, d in self.demand.get(key, []) if now - t <= win]
        # a pinned gauge is not a steady demand: while the autoscaler stands at its replica cap, every pod is as busy
        # as it can be and the reading cannot rise however much the load does; a window that touched the cap is not
        # steady (the wandering test: a target raised at the cap was taken back on the next climb, 1.5 pod starts a run)
        if any(now - t <= win for t in self.pinned.get(key, [])):
            return False
        return bool(h) and now - h[0][0] >= 0.9 * win and max(d for _, d in h) <= (1.0 + DEMAND_RISE) * min(d for _, d in h)

    def _machine_room(self, pool):
        """The machines the system can still add to a pool of `pool` ready workers, read live: up to the operator's own
        --max-nodes where given; else what the cluster's own autoscaler may add (its status); where Omni resizes the pool itself with the operator's command and no autoscaler
        reports, no top but the one the pool shows: one under the first count it refused (none refused: unbounded);
        otherwise none (a fixed pool)."""
        if (self.a.max_nodes or 0) > 0:
            return max(0, int(self.a.max_nodes) - pool)                  # the operator's own top
        room = autoscaler_room(self.k)
        if room is not None:
            return room
        if self.a.mode == "nodepool" and self.a.node_scale_cmd:
            return UNBOUNDED if self.refused_at is None else max(0, self.refused_at - 1 - pool)
        return 0

    def _max_nodes(self, s):
        """The machine lever's top, read live (the founder's rule of 13 October: from the floor up to what the system
        itself holds, never a number written in code): the operator's --max-nodes where given; else every ready worker
        the cluster has (the pool the lever opens and closes) plus the machines the system can still add."""
        if (self.a.max_nodes or 0) > 0:
            return int(self.a.max_nodes)
        if "_top" not in s:                                               # read once a snapshot
            pool = int(s.get("pool", s["nodes"]))
            s["_top"] = max(int(self.a.min_nodes), min(UNBOUNDED, pool + self._machine_room(pool)))
        return s["_top"]

    def _pool_command(self, n, n_now, why, **extra):
        """One node-pool command (the operator's own, --node-scale-cmd). A count the pool refuses is its top, read live:
        the lever stays one under it from then on, and the decision goes on (nothing else is held back by it)."""
        if "machines" in getattr(self.a, "native_muscles", ()):
            self.audit({"held": "machines", "why": f"{why}: the machines are left native (--native); {n} not written"})
            return False
        cmd = self.a.node_scale_cmd.format(n=n)
        self.audit({"write": shlex.split(cmd), "why": why, "dry_run": self.a.dry_run, **extra})
        if self.a.dry_run:
            return True
        try:
            subprocess.run(shlex.split(cmd), check=True)
            return True
        except subprocess.CalledProcessError as e:
            if n > n_now:
                self.refused_at = n if self.refused_at is None else min(self.refused_at, n)
            self.audit({"refused": {"nodes": n, "now": n_now, "code": e.returncode}, "why": why,
                        "pool_top": None if self.refused_at is None else self.refused_at - 1})
            return False

    def _pod_request_m(self, h):
        """One pod's CPU request (millicores) of the workload an HPA scales, read from its Deployment; None where unread."""
        ref = (h.get("spec") or {}).get("scaleTargetRef") or {}
        if ref.get("kind") != "Deployment" or not ref.get("name"):
            return None
        try:
            dep = self.k.get("get", "deployment", ref["name"], "-n", h["metadata"]["namespace"], "-o", "json")
        except Exception:
            return None
        tpl = dep["spec"]["template"]["spec"]
        req = sum(to_milli(c.get("resources", {}).get("requests", {}).get("cpu", "0")) for c in tpl.get("containers", []))
        return req if req > 0 else None

    def _cover(self):
        """The cover's floor as a share of the operator's target (--cover-floor, omni-v24; 0.6 the factory's), held inside
        [0.1, 1.0]; an unset or zero floor reads the factory's."""
        return min(1.0, max(0.1, float(getattr(self.a, "cover_floor", 0.6) or 0.6)))

    def _bounds(self, orig, g=1.0):
        """The compass's cover on an autoscaler's target, in the pods' own terms: (hi, lo) with hi the operator's target
        times the conveyed gain g (native's promise) and lo the cover's floor, never under 10%; a floor of 1.0 makes lo =
        hi, the pod count native's own target gives (omni-v24)."""
        hi = float(orig) * g
        return hi, min(hi, max(10.0, self._cover() * float(orig)) * g)

    def _placeable_target(self, h, s, lo_t, hi_t, rise=1.0):
        """The fail-up's target (omni-v19): the cover's floor lo_t where the machines in service can place the pods it asks
        for; else the lowest target whose pods they can place, ceil(100 dem / x) <= running + room, and the machines the rest
        need asked for now, so a pod is never asked for before there is a machine to run it. Unread (no demand, no request,
        not the node-pool mode): the cover's floor, as before. rise is the immune memory, the largest rise in the service's
        demand seen inside two decisions: the pods asked for leave room for that rise times themselves, so the next rise of
        that size finds a place, as native's fewer pods do."""
        dem, req = self._app_demand(h), self._pod_request_m(h)
        if dem is None or not req or dem <= 0:
            return lo_t
        cur = int((h.get("status") or {}).get("currentReplicas", 0) or 0)
        place = int((cur + max(0, int((s["alloc_m"] - s["req_m"]) // req))) / max(1.0, rise))
        if place <= 0:
            return hi_t
        fit = 100.0 * dem / place
        if fit <= lo_t:
            return lo_t
        short = int(math.ceil(100.0 * dem / lo_t - 1e-9)) - place
        if short > 0 and self.a.mode == "nodepool" and self.a.node_scale_cmd and "machines" not in getattr(self.a, "native_muscles", ()):
            n = max(1, s["open"]); per_node = s["alloc_m"] / max(1, s["nodes"])
            need = min(self._max_nodes(s), int(math.ceil((s["req_m"] + short * req) * (1.0 + self.a.headroom) / per_node)))
            if need > n and need > (self.rec_n or 0) and self._pool_command(need, n, "machines first: room for the pods the fail-up asks (omni-v19)",
                                                                            pods_short=short):
                self.rec_n = need
        self.audit({"placeable": {"hpa": f"{h['metadata']['namespace']}/{h['metadata']['name']}", "target": round(min(hi_t, fit), 1),
                                  "asked": round(lo_t, 1), "pods_placeable": place, "pods_short": max(0, short),
                                  "largest_rise": round(rise, 3)}})
        return min(hi_t, fit)

    def _live_ceiling(self, h):
        """The most replicas the machines can hold, one pod under it, read live: the allocatable CPU of every ready worker
        (closed ones included: the machine lever opens them) and of the machines the system can still add, less the CPU
        every other pod asks for, in units of one of this service's pods; where every node is a container on one machine
        (kind), that machine's CPU once. None where it cannot be read."""
        ref = (h.get("spec") or {}).get("scaleTargetRef") or {}
        ns = h["metadata"]["namespace"]
        if ref.get("kind") != "Deployment" or not ref.get("name"):
            return None
        try:
            dep = self.k.get("get", "deployment", ref["name"], "-n", ns, "-o", "json")
            nodes = [n for n in self.k.get("get", "nodes", "-o", "json")["items"] if is_ready(n) and worker(n)]
            pods = self.k.get("get", "pods", "-A", "-o", "json")["items"]
        except Exception:
            return None
        tpl = dep["spec"]["template"]["spec"]
        req = sum(to_milli(c.get("resources", {}).get("requests", {}).get("cpu", "0")) for c in tpl.get("containers", []))
        if req <= 0 or not nodes:
            return None
        shared_host = one_host(nodes)
        if shared_host:
            # kind nodes are containers on this machine: count its CPU once, then use /proc/stat busy share
            # so host-side load generators and processes outside Kubernetes consume the same capacity budget.
            alloc = max(to_milli(n["status"]["allocatable"]["cpu"]) for n in nodes)
        else:
            alloc = sum(to_milli(n["status"]["allocatable"]["cpu"]) for n in nodes)
            alloc += self._machine_room(len(nodes)) * alloc / len(nodes)
        sel = (dep["spec"].get("selector") or {}).get("matchLabels") or {}
        names = {n["metadata"]["name"] for n in nodes}
        mine = lambda p: p["metadata"].get("namespace") == ns and sel and all((p["metadata"].get("labels") or {}).get(k_) == v for k_, v in sel.items())
        other = sum(to_milli(c.get("resources", {}).get("requests", {}).get("cpu", "0")) for p in pods
                    if p["status"].get("phase") in ("Running", "Pending") and not mine(p)
                    and (p["spec"].get("nodeName") in names or p["status"].get("phase") == "Pending")
                    for c in p["spec"]["containers"])
        if shared_host:
            current = int((h.get("status") or {}).get("currentReplicas", 0) or 0)
            return kind_replica_ceiling(alloc, int(other), int(req), current, self.host_cpu.busy_share)
        return max(1, int((alloc - other) // req) - 1)

    def _replica_room(self, h, ns, name, win, obs, s):
        """The HPA's replica cap as a lever, up to what the machines can hold, one pod under it, read live (the
        founder's rule of 13 October; --replica-ceiling N sets a ceiling of the operator's own, 0 keeps the operator's cap
        unmoved). Only for a sensed service under the compass law. While the autoscaler
        stands at its cap and the compass is at or past its centre (or the line is breached), the cap is raised to the
        replicas the autoscaler's own arithmetic asks for, ceil(r x u / x), never past the ceiling; once the demand has
        held still for one window, the compass is under its centre, nothing breaches and that arithmetic fits the
        operator's own cap again, the cap returns to it. The operator's range is recorded before the first change, and
        the reset restores it."""
        given = int(getattr(self.a, "replica_ceiling", -1))
        if given == 0 or self.compass_law is None:
            return
        spec = h.get("spec", {}); st = h.get("status", {}) or {}
        ann = h["metadata"].get("annotations", {}) or {}
        lo0, hi0 = (int(x) for x in ann.get(RANGE_ANN, f"{spec.get('minReplicas', 1)},{spec.get('maxReplicas', 1)}").split(","))
        cap = int(spec.get("maxReplicas", hi0)); cur = int(st.get("currentReplicas", 0) or 0)
        _, tgt = cpu_target(h); dem = self._app_demand(h)
        if not tgt or dem is None:
            return
        need = int(math.ceil(100.0 * dem / float(tgt) - 1e-9))      # the replicas the autoscaler's arithmetic asks for
        pressed = self.compass_law.p >= self.compass_law.band.center or not obs["slo_clean"]
        ceil_ = given if given > 0 else None
        # Once Omni has raised the cap, refresh the shared-host ceiling every tick:
        # utilization can climb after the first decision. Keep the live replica count
        # runnable if the refreshed ceiling is below it.
        if ceil_ is None and ((cur >= cap and pressed and need > cap) or cap > hi0):
            ceil_ = self._live_ceiling(h)
        if cap > hi0:
            safe_cap = bounded_replica_cap(hi0, cap, cur, ceil_)
            if safe_cap < cap:
                self.k.write(["patch", "hpa", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"maxReplicas": safe_cap}})],
                             f"replica room: cap {cap} -> {safe_cap} (live ceiling {ceil_}; current replicas {cur})")
                return
        if cur >= cap and pressed and need > cap and ceil_ is not None and cap < ceil_:
            new = min(ceil_, need)
            if RANGE_ANN not in ann:
                self.k.write(["annotate", "hpa", name, "-n", ns, "--overwrite", f"{RANGE_ANN}={lo0},{hi0}"], "replica room: record the operator's range")
            self.k.write(["patch", "hpa", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"maxReplicas": new}})],
                         f"replica room: cap {cap} -> {new} (at the cap, {need} asked, ceiling {ceil_})")
        elif cap > hi0 and need <= hi0 and self.compass_law.p < self.compass_law.band.center and obs["slo_clean"] and self._steady((ns, name), win):
            self.k.write(["patch", "hpa", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"maxReplicas": hi0}})],
                         f"replica room: cap {cap} -> {hi0}, the operator's own (demand steady, {need} asked)")
            if int(spec.get("minReplicas", lo0)) == lo0:
                self.k.write(["annotate", "hpa", name, "-n", ns, f"{RANGE_ANN}-"], "replica room: operator's range back, record removed")

    def _new_latencies(self):
        """Response times (ms) of the requests served since the last decision (the probe's latency file)."""
        lf = getattr(self.a, "latency_file", "")
        if not lf:
            return []
        try:
            rows = list(csv.DictReader(open(lf)))
        except OSError:
            return []
        out, last = [], self.lat_t
        for row in rows:
            t, ms = row.get("elapsed_seconds"), row.get("latency_ms")
            if row.get("ok") != "1" or not t or not ms:
                continue
            t = float(t)
            if last is None or t > last:
                out.append(float(ms))
                self.lat_t = t if self.lat_t is None else max(self.lat_t, t)
        return [] if last is None else out

    def audit(self, rec):
        rec = {"time": time.time(), **rec}
        if self.log:
            self.log.write(json.dumps(rec) + "\n"); self.log.flush()
        return rec

    def killed(self):
        # this controller's own switch, or the master switch for the whole harness (omnicompass/master.py)
        return (os.environ.get("OMNI_KILL") == "1" or (self.a.kill_file and Path(self.a.kill_file).exists())
                or master.is_off())

    def _persist(self, what, fn):
        """One step of the hand-back, tried RESTORE_TRIES times against a transient failure of the cluster's API; every
        failed try is in the audit. Returns (the step's value, whether it landed)."""
        for attempt in range(1, RESTORE_TRIES + 1):
            try:
                return fn(), True
            except (subprocess.CalledProcessError, OSError) as e:
                self.audit({"error": f"restore: {what}: {e!r}"[:500], "stderr": str(getattr(e, "stderr", "") or "")[-300:],
                            "attempt": attempt, "of": RESTORE_TRIES})
                if attempt < RESTORE_TRIES:
                    time.sleep(min(4.0, 2.0 ** (attempt - 1)))
        return None, False

    def restore(self):
        """Every setting handed back to the operator's, from the records kept on the objects themselves. Each read and write
        is tried RESTORE_TRIES times, each muscle's hand-back on its own, and what did not land is raised at the end (the
        caller's audit records it; the master switch's watchdog runs the hand-back again)."""
        missed = []
        hpas, ok = self._persist("list the autoscalers", lambda: self.k.get("get", "hpa", "-A", "-o", "json")["items"])
        if not ok:
            missed.append("the autoscalers' replica ranges and targets (the list could not be read)")
        for h in hpas or []:
            ns, name = h["metadata"]["namespace"], h["metadata"]["name"]
            rng = h["metadata"].get("annotations", {}).get(RANGE_ANN)
            if rng:
                lo0, hi0 = (int(x) for x in rng.split(","))

                def put_range(ns=ns, name=name, lo0=lo0, hi0=hi0):
                    self.k.write(["patch", "hpa", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"minReplicas": lo0, "maxReplicas": hi0}})],
                                 "reset: restore the HPA's own replica range")
                    self.k.write(["annotate", "hpa", name, "-n", ns, f"{RANGE_ANN}-"], "reset: remove range record")
                if not self._persist(f"{ns}/{name}: the HPA's own replica range", put_range)[1]:
                    missed.append(f"{ns}/{name}: the replica range")
            orig = h["metadata"].get("annotations", {}).get(ANNOTATION)
            if orig is not None:
                idx, _ = cpu_target(h)

                def put_target(ns=ns, name=name, idx=idx, orig=orig):
                    if idx is not None:
                        self.k.write(["patch", "hpa", name, "-n", ns, "--type=json", "-p",
                                      json.dumps([{"op": "replace", "path": f"/spec/metrics/{idx}/resource/target/averageUtilization", "value": int(orig)}])],
                                     "reset: restore original HPA target")
                    self.k.write(["annotate", "hpa", name, "-n", ns, f"{ANNOTATION}-"], "reset: remove record")
                if not self._persist(f"{ns}/{name}: the operator's target", put_target)[1]:
                    missed.append(f"{ns}/{name}: the target")
        for ns, name in getattr(self, "own", []):
            dep, ok = self._persist(f"{ns}/{name}: read the workload", lambda ns=ns, name=name: self.k.get("get", "deployment", name, "-n", ns, "-o", "json"))
            if not ok:
                missed.append(f"{ns}/{name}: the operator's own count (the workload could not be read)")
                continue
            orig = (dep["metadata"].get("annotations", {}) or {}).get(OWN_REPL_ANN)
            if orig is None:
                continue

            def put_count(ns=ns, name=name, orig=orig):
                self.k.write(["scale", "deployment", name, "-n", ns, f"--replicas={int(orig)}"], "reset: restore the operator's own count")
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{OWN_REPL_ANN}-"], "reset: remove the count's record")
            if not self._persist(f"{ns}/{name}: the operator's own count", put_count)[1]:
                missed.append(f"{ns}/{name}: the operator's own count")
        self.changed.clear()
        try:
            missed += [f"the muscle's hand-back: {n}" for n in (self.m.restore() or [])]   # each lever tried on its own (muscles.py)
        except Exception as e:  # noqa: BLE001
            self.audit({"error": f"restore: the muscles' hand-back: {e!r}"[:500]})
            missed.append("the muscles' hand-back")
        cmd = getattr(self.a, "node_restore_cmd", "")
        if cmd and not self.nodes_restored:
            self.audit({"write": shlex.split(cmd), "why": "reset: restore node pool", "dry_run": self.a.dry_run})
            if self.a.dry_run or self._persist("the node pool", lambda: subprocess.run(shlex.split(cmd), check=True))[1]:
                self.nodes_restored = True
            else:
                missed.append("the node pool")
        if missed:
            raise RuntimeError("hand-back incomplete after %d tries each: %s" % (RESTORE_TRIES, "; ".join(missed)))

    def _gain(self, h):
        """The CPU each pod of the HPA's deployment is guaranteed, over the operator's limit (1 when nothing conveyed):
        g = min(mean conveyed limit, 0.95 A / ceil(maxReplicas / machines in service)) / L. The guaranteed share is the
        one each pod keeps with the autoscaler's largest count spread over the machines in service, so the target it
        sets moves only when a machine idles or wakes, never each time a pod starts or leaves."""
        from omnicompass.nervous_system import BAND
        ns = h["metadata"]["namespace"]; ref_ = h.get("spec", {}).get("scaleTargetRef", {}) or {}
        key = (ns, ref_.get("name", ""))
        g = self.m.gain.get(key, 1.0); base = self.m.base.get(key, 0.0); s = getattr(self, "_snap", None)
        if base > 0 and s and s.get("nodes"):
            ann = h["metadata"].get("annotations", {}) or {}
            hi0 = int(ann.get(RANGE_ANN, f"1,{h['spec'].get('maxReplicas', 1)}").split(",")[1])
            per_node = s["alloc_m"] / s["nodes"]
            g = min(g, BAND[1] * per_node / math.ceil(hi0 / s["nodes"]) / base)
        return max(1.0, g)

    def strict_step(self, s, obs):
        """Strict C: Omni-Compass decides each deployment's replica floor itself: replicas = ceil(current x measured
        utilisation / target utilisation), up at once, down only to the highest recommendation of the last
        --strict-window decisions; the HPA's minReplicas is set to that count, within its original range. Growth is never
        blocked: maxReplicas stays the operator's, so the HPA remains the fast up-reflex between Omni's decisions (the HPA
        reacts every 15 s; a count frozen for a 60 s decision would answer a load step up to 45 s late). The Unified
        Control Switch restores the original range."""
        hist = getattr(self, "_rec_hist", {}); self._rec_hist = hist
        for h in s["hpas"]:
            ns, name = h["metadata"]["namespace"], h["metadata"]["name"]
            ann = h["metadata"].get("annotations", {}) or {}
            lo0, hi0 = (int(x) for x in ann.get(RANGE_ANN, f"{h['spec'].get('minReplicas', 1)},{h['spec']['maxReplicas']}").split(","))
            idx, tgt = cpu_target(h)
            orig_t = int(ann.get(ANNOTATION, tgt or 50))
            cur = int(h.get("status", {}).get("currentReplicas", 0) or lo0)
            util = None
            for m in h.get("status", {}).get("currentMetrics", []) or []:
                if m.get("type") == "Resource" and m.get("resource", {}).get("name") == "cpu":
                    util = m["resource"].get("current", {}).get("averageUtilization")
            if util is None:
                continue
            rec = max(lo0, min(hi0, int(math.ceil(cur * float(util) / (orig_t * self._gain(h)) - 1e-9))))
            hh = (hist.get((ns, name), []) + [rec])[-self.n_strict_window:]; hist[(ns, name)] = hh
            want = rec if rec >= cur else max(hh)
            want = max(want, min(hi0, self.reflex.get((ns, name), 0)))   # the fast pod reflex's floor stands while held
            if obs.get("security_block", 0.0) > 0.5:
                want = min(want, cur)                     # shield I1: no expansion during a security hold
            if RANGE_ANN not in ann:
                self.k.write(["annotate", "hpa", name, "-n", ns, "--overwrite", f"{RANGE_ANN}={lo0},{hi0}"], "strict: record original replica range")
            if h["spec"].get("minReplicas") != want or h["spec"]["maxReplicas"] != hi0:
                self.k.write(["patch", "hpa", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"minReplicas": want, "maxReplicas": hi0}})],
                             f"strict: replica floor {cur} -> {want} decided by Omni-Compass (utilisation {util}%, target {orig_t}%); growth stays free up to {hi0}")

    def _own_pods(self, s, obs, rho, move=True):
        """The pod muscle of its own (omni-v19, the founder's order of 23 October: Omni-Compass by itself, running the muscles
        directly; docs/SOLO_PREREGISTRATION.md). For a workload the operator names (--own-replicas) and no autoscaler governs,
        Omni-Compass sets the replica count itself, through the workload's own scale, by strict C's rule: replicas =
        ceil(current x measured busy share / target), up at once, down only to the highest recommendation of the last
        --strict-window, inside the autoscaler's tolerance of a tenth. The target is the one the compass moves for an
        autoscaler (the decision above): the operator's own (the workload's target-utilization annotation, else
        --own-target), down to 60% of it, the most pods the cover allows past the wall. Never below the operator's own count
        at the max (the tune-down may go to the range's floor), never above the range's top, never below one pod. The count
        it shipped is recorded once on the workload and handed back by the reset (restore). With move False (a fast check
        between decisions) the target stays where the last decision set it and only the count is reconciled."""
        if "replicas" in self.a.native_muscles:
            return None                  # omni-v14: the replicas are left native; nothing written
        if move:
            self._own_last = (s, obs, rho)
        governed = {(h["metadata"]["namespace"], (h["spec"].get("scaleTargetRef") or {}).get("name")) for h in s["hpas"]}
        out = {}
        for ns, name in self.own:
            key = (ns, name)
            if key in self.own_handed:
                self.audit({"own_replicas": f"{ns}/{name}", "held": "handed back to native's own autoscaler: nothing written"})
                continue
            if key in governed:
                self.audit({"own_replicas": f"{ns}/{name}", "held": "an autoscaler governs it: its own muscle stands, nothing written"})
                continue
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            ann = dep["metadata"].get("annotations", {}) or {}
            cur = int(dep["spec"].get("replicas", 1) if dep["spec"].get("replicas") is not None else 1)
            orig = int(ann.get(OWN_REPL_ANN, cur))
            t_raw = ann.get(OWN_TARGET_ANN, getattr(self.a, "own_target", None))
            if t_raw is None:
                self.audit({"own_replicas": f"{ns}/{name}", "held": "no target named (the workload's annotation or --own-target): nothing written"})
                continue
            orig_t = float(t_raw)
            lo0, hi0 = (int(x) for x in str(ann.get(OWN_RANGE_ANN, f"1,{10 ** 6}")).split(","))
            c0 = dep["spec"]["template"]["spec"]["containers"][0]
            req = to_milli(c0.get("resources", {}).get("requests", {}).get("cpu", "0") or "0")
            sel = ",".join(f"{k_}={v_}" for k_, v_ in ((dep["spec"].get("selector") or {}).get("matchLabels") or {}).items())
            if req <= 0 or not sel:
                self.audit({"own_replicas": f"{ns}/{name}", "held": "no CPU request or no selector on the workload: nothing written"})
                continue
            top = self.k.get("top", "pods", "-n", ns, "-l", sel, "--no-headers")
            lines = [ln.split() for ln in str(top or "").strip().splitlines() if ln.strip()]
            if not lines:
                continue                 # no pod measured yet: nothing decided from it
            used = sum(to_milli(x[1]) for x in lines)
            util = 100.0 * used / (len(lines) * req)
            dem = used / req
            self.demand[key] = [(t_, v_) for t_, v_ in self.demand.get(key, []) if time.time() - t_ <= 600.0] + [(time.time(), dem)]
            # the target: the compass's push and pull inside its cover, as on an autoscaler's target (the decision above)
            hi_t, lo_t = self._bounds(orig_t)
            x = self.own_x.get(key, hi_t)
            if not move:
                pass                                                 # between decisions: the target the last decision set
            elif self.compass_law is None:
                x = min(hi_t, max(lo_t, 100.0 * rho))
            else:
                load = s["pending"] == 0 and not obs["slo_clean"]
                pos_ = self.compass_law.p if self.compass_law.p is not None else 0.0   # no reading yet: the operator's own target
                if pos_ >= self.compass_law.band.wall_high and load:
                    x = lo_t                                         # fail up: the most pods the cover allows, at once
                elif pos_ >= self.compass_law.band.wall_high:
                    x = hi_t                                         # past the wall, but not from load: the operator's own
                elif x < hi_t and pos_ < self.compass_law.band.center and obs["slo_clean"] and s["pending"] == 0 \
                        and not self._rising(key, 300.0):
                    x = hi_t
                else:
                    F_ = self._own_F                                  # the compass's force of this decision (above)
                    x = x - (COMPASS_UP if F_ > 0 else COMPASS_DOWN) * F_ * (hi_t - lo_t) * self.step_scale
            x = max(lo_t, min(hi_t, x)); self.own_x[key] = x
            ratio = util / x
            rec = cur if abs(ratio - 1.0) <= 0.1 else int(math.ceil(cur * ratio - 1e-9))
            floor_ = max(1, lo0, orig if self.dial == "max" else lo0)
            rec = max(floor_, min(hi0, rec))
            hh = (self.own_hist.get(key, []) + [rec])[-self.n_own_window:]; self.own_hist[key] = hh
            want = rec if rec >= cur else max(hh)
            if obs.get("security_block", 0.0) > 0.5:
                want = min(want, cur)                                # shield I1: no expansion during a security hold
            if want == cur:
                continue
            try:
                if OWN_REPL_ANN not in ann:
                    self.k.write(["annotate", "deployment", name, "-n", ns, "--overwrite", f"{OWN_REPL_ANN}={cur}"], "own pods: record the operator's count")
                self.k.write(["scale", "deployment", name, "-n", ns, f"--replicas={want}"],
                             f"own pods: {cur} -> {want} (busy {util:.0f}% of the request, target {x:.0f}%, the operator's {orig_t:.0f}%)")
            except subprocess.CalledProcessError as e:
                self._own_refused(key, orig_t, lo0, hi0, orig, e)       # omni-v23: the knob never left with no controller
                continue
            self.own_refused.pop(key, None)                              # a write that landed ends the run of refusals
            out[key] = want
        if out:
            self.audit({"own_replicas": {f"{k[0]}/{k[1]}": v for k, v in out.items()}})
        return out

    def _own_refused(self, key, orig_t, lo0, hi0, orig, e):
        """omni-v23 (the founder's order of 31 October: Omni direct keeps every muscle Omni-Compass cannot be; a knob left with no
        working controller fails the whole system and is never a result). A write of the workload's own scale that the cluster
        refuses (its permission, its admission, its API) is recorded, and the decision goes on: the cluster keeps the last count
        that landed. At OWN_REFUSALS refusals in a row Omni-Compass cannot be this knob's muscle, so the knob goes back to native's
        own pod autoscaler, made from the operator's own target and range recorded on the workload, and the muscle leaves the
        workload to it for the rest of the run (the snapshot's governed set holds it from the next decision on; the reset leaves
        native's autoscaler standing). Nothing is forced: the organism never runs with a knob nobody moves."""
        ns, name = key
        n = self.own_refused.get(key, 0) + 1
        self.own_refused[key] = n
        err = (getattr(e, "stderr", "") or str(e) or "")[-300:]
        self.audit({"own_replicas": f"{ns}/{name}", "refused": n, "error": err})
        if n < OWN_REFUSALS or key in self.own_handed:
            return
        self.own_handed.add(key)
        hi = hi0 if hi0 < 10 ** 6 else max(10, 10 * max(1, int(orig)))   # no range recorded: ten times the operator's count
        try:
            self.k.write(["autoscale", "deployment", name, "-n", ns, f"--cpu-percent={int(round(orig_t))}", f"--min={lo0}", f"--max={hi}"],
                         f"own pods: the cluster refused the muscle's write {n} times in a row: the knob handed back to native's "
                         f"own autoscaler at the operator's target {orig_t:.0f}% and range {lo0},{hi}")
            self.audit({"own_replicas": f"{ns}/{name}", "handed_back": "native's own pod autoscaler", "after_refusals": n,
                        "target": orig_t, "range": [lo0, hi]})
        except subprocess.CalledProcessError as e2:
            self.audit({"own_replicas": f"{ns}/{name}", "hand_back_refused": (getattr(e2, "stderr", "") or str(e2) or "")[-300:]})

    def pod_reflex(self):
        """The fast pod reflex (manuscript Section 5.3, preemptive coherence): the HPA's own staffing rule,
        replicas = current x busy / target, read from the live queue instead of CPU averages a minute old.

        Busy comes from queueing physics: a replica serving requests in processor sharing answers in R = S / (1 - u),
        so u = 1 - S / R, with S the bare service time (the fastest tenth of the window's requests, those with no queue
        ahead) and R the mean response of the same window. The operator's target is a share of the pod's CPU request; the queue runs on
        its limit, so the same promise in queue terms is target x request / limit. The reflex only raises the replica
        floor to what that rule needs now and hands it back the moment the queue no longer needs it: no padding, no new
        target, the operator's own promise met sooner. Zero cluster reads while the queue is calm."""
        lf = getattr(self.a, "latency_file", "")
        if not lf or self.killed() or self.a.mode not in ("target", "nodepool") or "replicas" in getattr(self.a, "native_muscles", ()):
            return None
        from omni_controller.muscles import latency_window
        w = latency_window(lf, getattr(self.a, "reflex_window_s", 30.0))
        if w["blind"] or len(w["ms"]) < 5:
            return None
        p10 = sorted(w["ms"])[len(w["ms"]) // 10]
        # S and R from the same window: the fastest tenth of the requests answered now, at the CPU the pods have now. An
        # all-time fastest would read every later change of a pod's CPU limit (convey) as a queue that is not there
        self.s_floor = p10
        R = sum(w["ms"]) / len(w["ms"])
        u = max(0.0, min(0.99, 1.0 - self.s_floor / R)) if R > 0 else 0.0
        if u <= 0.0 and not self.reflex:
            return None                          # calm and nothing held: no read, no write
        out = {}
        for h in self.k.get("get", "hpa", "-A", "-o", "json")["items"]:
            idx, tgt = cpu_target(h)
            if tgt is None:
                continue
            ns, name = h["metadata"]["namespace"], h["metadata"]["name"]
            ann = h["metadata"].get("annotations", {}) or {}
            lo0, hi0 = (int(x) for x in ann.get(RANGE_ANN, f"{h['spec'].get('minReplicas', 1)},{h['spec']['maxReplicas']}").split(","))
            orig_t = int(ann.get(ANNOTATION, tgt)) / 100.0
            key = (ns, name)
            if key not in self.pod_cap:
                ref = h["spec"]["scaleTargetRef"]
                c0 = self.k.get("get", ref["kind"].lower(), ref["name"], "-n", ns, "-o", "json")["spec"]["template"]["spec"]["containers"][0]
                req = to_milli(c0.get("resources", {}).get("requests", {}).get("cpu", "0") or "0")
                lim = to_milli(c0.get("resources", {}).get("limits", {}).get("cpu", "0") or "0")
                self.pod_cap[key] = (req / lim) if req > 0 and lim > 0 else 1.0
            u_star = max(0.05, orig_t * self.pod_cap[key])       # the operator's promise in queue terms
            cur = int(h.get("status", {}).get("currentReplicas", 0) or lo0)
            desired = int(h.get("status", {}).get("desiredReplicas", 0) or cur)
            need = min(hi0, int(math.ceil(cur * u / u_star - 1e-9)))
            held = self.reflex.get(key)
            if not getattr(self.a, "pod_reflex_writes", False):
                # the autoscaler is the muscle that makes and removes pods; I gauge what the queue needs and write
                # nothing, so no pod is started or stopped that the muscle itself would not start or stop
                if need > max(cur, desired):
                    self.audit({"pod_reflex_reading": {f"{ns}/{name}": need}, "replicas": cur, "busy": round(u, 3),
                                "promise": round(u_star, 3), "R_ms": round(R, 1), "S_ms": round(self.s_floor, 1)})
                continue
            if need > max(cur, desired, h["spec"].get("minReplicas", 1) or 1):
                if RANGE_ANN not in ann:
                    self.k.write(["annotate", "hpa", name, "-n", ns, "--overwrite", f"{RANGE_ANN}={lo0},{hi0}"], "pod reflex: record original replica range")
                self.k.write(["patch", "hpa", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"minReplicas": need}})],
                             f"pod reflex: floor {need} (queue busy {u:.2f} vs promise {u_star:.2f}, R {R:.0f} ms, S {self.s_floor:.0f} ms)")
                self.reflex[key] = need; out[key] = need
            elif held is not None and need <= max(desired, lo0):
                # the queue no longer needs the floor (or the HPA has caught up): hand it back. On top, the operator's
                # own minimum returns; in strict C the floor is Omni's own replica decision again (strict_step)
                del self.reflex[key]; out[key] = None
                if not getattr(self.a, "strict_replicas", False) and h["spec"].get("minReplicas") == held:
                    self.k.write(["patch", "hpa", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"minReplicas": lo0}})],
                                 f"pod reflex: release floor {held} -> {lo0} (queue busy {u:.2f})")
                    out[key] = lo0
        if out:
            self.audit({"pod_reflex": {f"{k[0]}/{k[1]}": v for k, v in out.items()}, "busy": round(u, 3), "R_ms": round(R, 1), "S_ms": round(self.s_floor, 1)})
        return out

    def _own_check(self):
        """Between decisions, the pod muscle of its own at the pod autoscaler's pace (omni-v19): every n-th fast check
        (--own-every-s, 15 s), the count reconciled to the busy share at the target the last decision set."""
        if not self.own or self._own_last is None:
            return None
        self.own_checks += 1
        if self.own_checks % self.n_own:
            return None
        s, obs, rho = self._own_last
        try:
            return self._own_pods(s, obs, rho, move=False)
        except Exception as e:
            self.audit({"error": "own pods check: " + repr(e)[:500]})
            return None

    def floor_step(self):
        """Fast path between governor decisions: add the nodes that pending and running pod requests need (nodepool mode)."""
        if self.killed() or self.a.mode != "nodepool":
            return None
        self._own_check()
        if not self.a.node_scale_cmd:
            return None
        due = self._convey_due()
        if getattr(self, "cruise", False):
            # cruise (rule 7, amendment 12): every machine is already in service, so a floor check can add nothing; and a
            # queue of other work starves the service's responses without any load on it, which the reflex would read as
            # a queue and answer with idle pods. Omni steps back: no reads, no reflex, no conveyance until cruise ends
            return None
        self.pod_reflex()
        # energy to where the work is: a new serving pod gets its machine's idle CPU within --convey-every-s (15 s), not a
        # decision
        if getattr(self.a, "latency_file", "") and due:
            self._convey()
        # one light read every check; the full snapshot (nodes, all pods, node metrics, HPAs) only when a pod waits. The
        # controller shares CPUs with the service it protects (on kind, one 4-core runner), so its reads cost latency
        if not str(self.k.get("get", "pods", "-A", "--field-selector=status.phase=Pending", "-o", "name")).strip():
            return None
        self.waited = True                       # time waited between decisions is harm the next decision's verdict reads
        s = snapshot(self.k, getattr(self.a, "active_nodes_only", False))
        if s["alloc_m"] <= 0:
            return None                          # no machine in service in the reading: blind, nothing to add from it
        if s["pending"] > 0:
            self._pods_wait_handback(s)
        n = max(1, s["open"]); per_node = s["alloc_m"] / max(1, s["nodes"])
        floor = max(int(math.ceil(s["req_m"] * (1.0 + self.a.headroom) / per_node)) if s["req_m"] > 0 else self.a.min_nodes, int(math.ceil(s["used_m"] / per_node)))
        floor = min(self._max_nodes(s), floor)
        if s["pending"] > 0 and floor > n and floor > (self.rec_n or 0):
            if self._pool_command(floor, n, "scheduling floor (pending pods)"):
                self.rec_n = floor
                return floor
        return None

    def _pods_wait_handback(self, s):
        """The immune hand-back (omni-v19, the founder's rule: where Omni-Compass cannot beat native, native stays). A pod waiting
        for a place is time waited, a LOSS: while one waits, every pod autoscaler whose target Omni-Compass holds below the
        operator's own (more pods than native would ask) gets the operator's target back at once, from this fast check, not the
        next decision, and keeps it for a hold of 10 minutes, doubled for each hand-back in a row up to two hours and halved back
        after a quiet hold. The machines the waiting pods need are still asked for by the scheduling floor below."""
        now = time.time()
        for h in s["hpas"]:
            ns, name = h["metadata"]["namespace"], h["metadata"]["name"]
            key = (ns, name)
            orig, cmd = self.changed.get(key), self.cmd_hpa.get(key)
            idx, cur = cpu_target(h)
            if idx is None or orig is None or cmd is None or cur is None:
                continue
            # native's target in the pods' own terms: the operator's, times the conveyed gain while a pod's limit is raised
            # (the same promise in queue terms the decision keeps), never over 100%
            back_to = min(100, int(round(float(orig) * self._gain(h))))
            if int(cur) >= back_to:
                continue
            until, length = self.pod_hold.get(key, (0.0, 0.0))
            if until > now:
                continue                         # already handed back and held
            n = self.hold_n.get(key, 0)
            hold = min(7200.0, 600.0 * (2 ** n))
            self.pod_hold[key], self.hold_n[key] = (now + hold, hold), n + 1
            if "replicas" in self.a.native_muscles:
                continue
            self.k.write(["patch", "hpa", name, "-n", ns, "--type=json", "-p",
                          json.dumps([{"op": "replace", "path": f"/spec/metrics/{idx}/resource/target/averageUtilization", "value": back_to}])],
                         f"immune hand-back: a pod waits, the HPA target back to native's {back_to}% for {int(hold)} s (omni-v19)")
            self.cmd_hpa[key] = back_to; self.target_at[key] = now
            self.compass_law_x[key] = float(back_to)
            self.audit({"immune": {"hpa": f"{ns}/{name}", "pending": s["pending"], "target_was": int(cur), "target_back_to": back_to,
                                   "hold_s": int(hold), "in_a_row": n + 1}})

    def _immune_native(self, h, ns, name, x, hi_t, lo_t, p95):
        """The immune system's self-knowledge for this service's autoscaler target (omni-v21; omnicompass/immune.py; the
        founder's order of 25 October): while the service's response time is over its line with Omni-Compass's target on it,
        and Omni-Compass's own pushing does not bring it back, the target goes to native when native's twin reads the moment
        lower, and stays where it is when native is not stronger. Native's twin is the same moment under the operator's target:
        the replicas native's own rule would ask for the measured demand, and the M/M/1 wait they would give, the response time
        scaled by (1 - rho_omni) / (1 - rho_native) with rho each pod's busy share of its request. True while native holds it."""
        from omnicompass.immune import Immune
        slo = float(getattr(self.a, "slo_ms", 0) or 0)
        key = (ns, name)
        im = self.immune.setdefault(key, Immune())
        dem = self._app_demand(h)
        cur = int((h.get("status") or {}).get("currentReplicas", 0) or 0)
        orig = int(h["metadata"].get("annotations", {}).get(ANNOTATION, cpu_target(h)[1] or 0) or 0)
        if not slo or p95 is None or dem is None or cur <= 0 or orig <= 0:
            return im.mode == "native"
        native_reps = max(1, int(math.ceil(100.0 * dem / orig - 1e-9)))
        rho_o, rho_n = min(0.98, dem / cur), min(0.98, dem / native_reps)
        p_omni = float(p95) / slo
        p_native = p_omni * (1.0 - rho_o) / (1.0 - rho_n)
        moved = abs(x - self.compass_law_x.get(key, hi_t)) > 0.5
        at_limit = x <= lo_t + 1e-9 or cur >= int(h["spec"].get("maxReplicas", 10 ** 9))
        mode, ev = im.tick(p_omni, p_native, moved, at_limit)
        if ev:
            self.audit({"immune": dict(ev, hpa=f"{ns}/{name}", native_replicas=native_reps, replicas=cur)})
        return mode == "native"

    def _held_native(self, key):
        """True while a pod autoscaler's target is held at the operator's after a pod waited (_pods_wait_handback); a hold that
        has passed with no new hand-back for another hold's length halves the next one."""
        until, length = self.pod_hold.get(key, (0.0, 0.0))
        now = time.time()
        if until > now:
            return True
        if length and now > until + length and self.hold_n.get(key, 0) > 0:
            self.hold_n[key] -= 1
            self.pod_hold[key] = (now, length / 2.0)
        return False

    def _convey_due(self):
        """The conveyance's clock (omni-v16): every check counts, a fast check or a decision, and the conveyance runs on
        every n-th, n = --convey-every-s / --floor-interval (15 s at the 5 s checks), whatever the decision period. Before
        omni-v16 it ran on every third fast check and a decision was never one, so at a decision every 5 s it never ran."""
        self.checks += 1
        return self.checks % self.n_convey == 0

    def _convey(self):
        try:
            self.m.convey()
        except Exception as e:  # a failed conveyance writes nothing more; the next one comes on time
            self.audit({"error": f"convey: {e}"})

    def step(self):
        self.decisions += 1
        convey_due = self._convey_due() if self.a.mode == "nodepool" and self.a.node_scale_cmd else False
        self.host_cpu.sample()              # two adjacent controller ticks provide a host CPU busy share
        if self.killed():
            self.restore()
            return self.audit({"decision": "killed", "mode": "observe"})
        s = snapshot(self.k, getattr(self.a, "active_nodes_only", False))
        if s["alloc_m"] <= 0:
            # a reading with no machine in service is blind, never an overload (omni-v11; 18 Oct, the CruiseKube test, run
            # 39120444653: every worker of the kind cluster left service for two minutes while the service answered every
            # probe, and omni-v10 read its load against no capacity, then divided by it). Nothing is decided from it and
            # nothing written; the last reading with machines stays the one the conveyance is bounded by
            return self.audit({"decision": "held: the cluster's reading shows no machine in service; nothing decided, nothing written",
                               "mode": "autopilot" if self.a.mode in ("target", "nodepool") else "observe"})
        self._snap = s
        # my orders are judged by the machines open to work; a machine's capacity by the machines in service
        n = max(1, s["open"]); per_node = s["alloc_m"] / max(1, s["nodes"])
        if self.rec_n is None:
            self.rec_n = n
        repl = sum(int(h.get("status", {}).get("currentReplicas", 0) or 0) for h in s["hpas"]) or n
        power_stress = 0.0; blind = {}
        if self.a.power_cmd and self.a.site_limit_w:
            try:
                power_stress = float(run_operator_cmd(self.a.power_cmd).stdout.strip()) / self.a.site_limit_w
                blind["power"] = False
            except ValueError:
                power_stress = 0.0; blind["power"] = True
        # proprioception (efferent -> afferent): did the last commands land? drift = |observed - commanded| / commanded
        drift = {}
        if self.cmd_nodes is not None:
            drift["nodes"] = abs(n - self.cmd_nodes) / max(1, self.cmd_nodes)
        for h in s["hpas"]:
            key = (h["metadata"]["namespace"], h["metadata"]["name"])
            if key in self.cmd_hpa:
                _, cur_t = cpu_target(h)
                if cur_t is not None:
                    drift["hpa " + "/".join(key)] = abs(cur_t - self.cmd_hpa[key]) / max(1, self.cmd_hpa[key])
        nodes_landed = drift.get("nodes", 0.0) == 0.0
        # a command is given LAND_S to land, however often the governor decides (omni-v16): every decision reads its drift
        # until it has landed or its minute has passed (at a decision a minute, the next decision only, as before)
        keep = lambda key, d_: d_ > 0.0 and self.decisions - self.cmd_at.get(key, self.decisions) < self.n_land
        if self.cmd_nodes is not None and not keep("nodes", drift.get("nodes", 0.0)):
            self.cmd_nodes = None
        self.cmd_hpa = {k_: v_ for k_, v_ in self.cmd_hpa.items() if keep(k_, drift.get("hpa " + "/".join(k_), 0.0))}
        obs = {"queue_ratio": min(2.0, s["pending"] / max(1, repl)), "load_ratio": min(2.0, s["used_m"] / max(1.0, self.rec_n * per_node)),
               "power_stress": power_stress, "thermal": 0.0, "network_stress": 0.0, "drift_ratio": max(drift.values(), default=0.0),
               "stale": 0.0, "security_block": 0.0}
        extra = self.m.sense(power_stress)
        lp = extra.pop("latency_pressure", 0.0); p95 = extra.pop("latency_p95_ms", None)
        if getattr(self.a, "latency_file", "") and getattr(self.a, "slo_ms", 0):
            blind["latency"] = bool(extra.pop("latency_blind", 0.0))
        age = extra.pop("latency_age_s", None)
        obs.update(extra)
        # afferent integrity: the share of declared senses that are blind enters the engine as its stale channel
        obs["stale"] = (sum(blind.values()) / len(blind)) if blind else 0.0
        obs["queue_ratio"] = min(2.0, max(obs["queue_ratio"], lp))
        # SLO reflex: while the response-time target is breached, and for --slo-clear decisions after, Omni-Compass may
        # not pack replicas tighter than the workload's own HPA target and may not cap power (no energy at service's cost)
        self.lp_hist.append(lp)
        guarded = bool(getattr(self.a, "latency_file", "")) and getattr(self.a, "slo_ms", 0)
        n_clear = self.n_slo_clear
        obs["slo_clean"] = (not guarded) or (not blind.get("latency", False) and len(self.lp_hist) >= n_clear
                                             and all(x == 0.0 for x in self.lp_hist[-n_clear:]))
        self.g.nodes = self.rec_n; self.g.current_cap = 1.0
        d = self.g.step(obs, 0)
        floor = max(int(math.ceil(s["req_m"] * (1.0 + self.a.headroom) / per_node)) if s["req_m"] > 0 else self.a.min_nodes, int(math.ceil(s["used_m"] / per_node)))
        rec_n = max(self.a.min_nodes, min(self._max_nodes(s), max(self.rec_n + int(d["node_delta"]), floor)))
        rho = max(0.5, min(0.95, float(d["demand"])))
        from omnicompass.nervous_system import from_governor, node_release_gate
        mode = "autopilot" if self.a.mode in ("target", "nodepool") else "observe"
        # an organ every governed knob of which the immune system handed to native has no authority of Omni-Compass's (omni-v21)
        held = [k for k, im in self.immune.items() if im.mode == "native"]
        auth = from_governor(self.g, obs, d, mode=mode, native_hold=("pods",) if held and len(held) == len(self.immune) else ())
        self.m.auth = auth
        breach_now = lp > 0.0 or blind.get("latency", False)
        # the machine organ's view: only pressure a machine release could cause (pods waiting for a place, a live
        # breach). Power and heat are relieved by a release, never worsened by it, so they cannot veto one
        obs_n = dict(obs, queue_ratio=min(2.0, s["pending"] / max(1, repl)), slo_clean=not breach_now,
                     power_stress=0.0, thermal=0.0)
        self.gn.nodes = self.rec_n; self.gn.current_cap = 1.0
        dn = self.gn.step(obs_n, 0)
        auth_n = from_governor(self.gn, obs_n, dn, mode=mode)
        if self.cl is not None:
            # the benchmarked law drives the machines: the closure law on requested cores (omnicompass/closure.py), the
            # scheduling floor stays underneath it
            self.cl.observe(s["req_m"] / 1000.0)
            # the machine organ's own pressure (as its release gate): pods waiting and live breaches, not modelled heat
            # or the whole body's latency push, which a machine release does not cause
            cl_n = self.cl.decide(n, per_node / 1000.0, self.gn.last_push, self.a.min_nodes, self._max_nodes(s))
            rec_n = max(self.a.min_nodes, min(self._max_nodes(s), max(cl_n, floor)))
        compass_rec = None
        if self.compass_law is not None:
            # the service position in its compass, read as the GPU compass reads it (omni_controller/gpu_compass.py): the mean
            # response time of the window between the bare service time (a tenth of the SLO) and the SLO; p95 at or
            # past the SLO, a blind sense, or a pod waiting for a place is past the wall
            slo = float(getattr(self.a, "slo_ms", 0) or 0)
            pos = 0.0
            if slo > 0 and getattr(self.a, "latency_file", ""):
                from omni_controller.muscles import latency_window
                w = latency_window(self.a.latency_file, getattr(self.a, "latency_window_s", 60.0))["ms"]
                bare = slo / 10.0
                mean = sum(w) / len(w) if w else (p95 or 0.0)
                pos = max(0.0, (mean - bare) / (slo - bare))
            if blind.get("latency", False) or s["pending"] > 0 or (p95 is not None and slo > 0 and p95 >= slo):
                pos = 1.0
            if self.edge is not None:
                # the v5 edge: a breach while machines are given back teaches the cushion a floor; then the balance point
                # and the wall move with the service's own climb and wobble (never behind the earlier law's own point
                # unless that lesson says so)
                if breach_now and self.n_native is not None and n < self.n_native:
                    self.edge.learn_fall(0.1 * self.pace)           # 0.1 a minute of breach (omni-v16)
                center = self.edge.update(pos)
                base = self.edge_base if self.edge.floor <= 0.0 else 0.0
                self.compass_law.band.center = min(0.995, max(0.0, max(base, center)))
                self.compass_law.band.cushion = min(0.05, max(0.005, self.edge.react_part))
            F = self.compass_law.force(pos)
            self._own_F = F            # the same force moves a workload's target of its own (_own_pods)
            # the verdict: the response times of the requests served since the last decision, at the machines the pool
            # stood at; then how many machines may be given back at all (or the count a trial needs)
            if self.n_native is None:
                self.n_native = n
            self.verdict.observe(self._new_latencies())
            # a pod that waited for a place since the last decision, seen by a fast check, is harm as much as one waiting now
            waited, self.waited = self.waited or s["pending"] > 0, False
            calm = self.compass_law.p < self.compass_law.band.wall_high and not waited and not breach_now
            if waited and self.verdict.allowed > 0:
                # the immune reaction (omni-v19; Omni direct's own, omni_orchestrator/control.py): work waited under an
                # allowed depth, so one step goes back toward native and is not tried again until the recheck has passed
                self.verdict.allowed -= 1
                self.verdict.refused_until[self.verdict.allowed + 1] = self.verdict.t + self.verdict.recheck
                self.audit({"verdict": {"verdict": "depth handed back: a pod waited for a place", "step": self.verdict.allowed + 1},
                            "machines_given_back_allowed": self.verdict.allowed, "machines_native": self.n_native})
            deepest, trial, ev = self.verdict.tick(calm)
            if self.dial == "max":
                deepest, trial = 0, False          # the max never gives back a machine the cluster had on its own
            if ev:
                self.audit({"verdict": ev, "state": self.verdict.state, "machines_given_back_allowed": self.verdict.allowed,
                            "machines_native": self.n_native})
            if self.compass_law.p >= self.compass_law.band.wall_high:
                rec_n = max(floor, n + 1)                                  # fail up: one machine more at once
            elif trial:
                rec_n = max(floor, self.n_native - deepest)                # the trial's count (one machine per decision below)
            elif F < COMPASS_RELEASE and self.compass_law.p < self.compass_law.band.center and self.n_native - (n - 1) <= deepest:
                rec_n = max(floor, n - 1)                                  # one back, if the verdict and the release gate agree
            else:
                rec_n = max(floor, n)
            rec_n = max(self.a.min_nodes, min(self._max_nodes(s), rec_n))
            compass_rec = {"position": round(self.compass_law.p, 4), "velocity": round(self.compass_law.v, 4), "force": round(F, 4),
                        "center": round(self.compass_law.band.center, 4), "wall": round(self.compass_law.band.wall_high, 4),
                        "verdict_state": self.verdict.state, "machines_given_back_allowed": self.verdict.allowed}
        scaling_up = any(int(h.get("status", {}).get("desiredReplicas", 0) or 0) > int(h.get("status", {}).get("currentReplicas", 0) or 0)
                         for h in s["hpas"])
        gate = node_release_gate(n, per_node, s["used_m"], s["pending"], scaling_up, breach_now, rho, auth_n,
                                 senses_live=not any(blind.values()), last_command_landed=nodes_landed)
        # the immune memory (omni-v19): the largest rise in requests seen inside two decisions, about the time a new machine
        # takes to boot; a machine is given back only when the machines left hold the requests and a reserve of the larger of
        # one machine and that rise, so the next rise of the same size lands on a machine already up, as it does on native's
        if s["req_m"] > 0:
            self.req_seen = (self.req_seen + [float(s["req_m"])])[-3:]
            self.burst_m = max(self.burst_m, float(s["req_m"]) - min(self.req_seen))
        reserve = max(per_node, self.burst_m)
        native_line = float(getattr(self.a, "native_release_util", 0.5) or 0.5)
        if rec_n < n and (s["req_m"] + reserve > (n - 1) * per_node or s["req_m"] > native_line * (n - 1) * per_node):
            self.audit({"immune_memory": {"kept": n, "requests_m": int(s["req_m"]), "reserve_m": int(reserve),
                                          "largest_rise_m": int(self.burst_m), "room_after_m": int((n - 1) * per_node),
                                          "native_line": native_line}})
            rec_n = n            # the machines left would not hold the requests and the reserve, or would stand thinner than
                                 # native's own autoscaler lets them: the machine stays
        if getattr(self, "verdict", None) is not None and self.verdict.allowed > 0 and rec_n <= n and s["req_m"] > 0:
            # while machines stand given back, the same rule every decision: when the machines in service no longer hold the
            # requests and the reserve, or stand thinner than native's own line (native's own autoscaler may have removed one
            # of its own meanwhile), one machine comes back now, before a pod waits for it
            need = max(int(math.ceil((s["req_m"] + reserve) / per_node - 1e-9)),
                       int(math.ceil(s["req_m"] / (native_line * per_node) - 1e-9)))
            if need > n:
                self.audit({"immune_memory": {"machine_back": n + 1, "requests_m": int(s["req_m"]), "reserve_m": int(reserve),
                                              "native_line": native_line, "machines_needed": need}})
                rec_n = min(self._max_nodes(s), n + 1)
        if rec_n < n and not gate["ok"]:
            rec_n = n            # nervous system: the machine organ may not give a machine back now (reason audited)
        elif rec_n < n and self.last_release is not None and self.decisions - self.last_release < self.n_release:
            rec_n = n            # at most one machine a minute, however often the governor decides (v7)
        elif rec_n < n:
            rec_n = n - 1        # one machine at a time: release is the slow, reversible direction
            self.last_release = self.decisions
        # cruise (rule 7): work waiting for a place, decision after decision, so every machine goes in service and stays
        # there, without second-guessing, until the line has been empty for as many decisions
        ca = self.n_cruise_after
        if ca > 0 and self.a.mode == "nodepool":
            self.cruise_hits = self.cruise_hits + 1 if s["pending"] > 0 else 0
            if not self.cruise and self.cruise_hits >= ca:
                self.cruise = True; self.cruise_clear = 0
                self.audit({"cruise": "on", "pending": s["pending"]})
            elif self.cruise:
                self.cruise_clear = self.cruise_clear + 1 if (s["pending"] == 0 and not scaling_up) else 0
                if self.cruise_clear >= ca:
                    self.cruise = False
                    self.audit({"cruise": "off", "pending": s["pending"]})
            if self.cruise:
                rec_n = min(self._max_nodes(s), n + max(1, int(self.a.max_node_step)))   # toward the top, a step a decision
        # idle (rule 8: one pedal, lifted all the way): nothing waiting, no breach, and the sensed services' demand at
        # zero: straight to the breathing floor in one move (the body idles, never at zero, and wakes straight to the
        # work when it comes). Every check of the release gate still holds except one machine per decision
        eb = float(getattr(self.a, "idle_demand", 0.05) or 0)
        if eb > 0 and self.a.mode == "nodepool" and not self.cruise and rec_n > self.a.min_nodes and s["pending"] == 0 \
                and not breach_now and not scaling_up:
            sensed = [h for h in s["hpas"] if self._sensed(h)]
            dem = [self._app_demand(h) for h in sensed]
            dem = [x for x in dem if x is not None]
            idle = bool(sensed) and all(self._at_idle(h) for h in sensed)
            g_ok = gate["ok"] or gate["reason"] == "release permitted"
            if dem and (max(dem) <= eb or idle) and g_ok and not any(blind.values()) and nodes_landed:
                low = max(self.a.min_nodes, floor)
                # the machines left must carry what runs now at or under the engine's utilisation target
                while low < rec_n and s["used_m"] / max(low * per_node, 1e-9) > rho:
                    low += 1
                if low < rec_n:
                    self.audit({"idle_floor": {"from": rec_n, "to": low, "demand": round(max(dem), 3), "at_idle": idle}})
                    rec_n = low
        out = self.audit({"authority": {"calm": round(auth["scalars"]["calm"], 3), "execute": auth["execute"],
                                        "contract": {o: v.get("contract") for o, v in auth["organs"].items()},
                                        "scalars": {k: round(v, 3) for k, v in auth["scalars"].items()},
                                        "node_view": {"calm": round(auth_n["scalars"]["calm"], 3),
                                                      "scalars": {k: round(v, 3) for k, v in auth_n["scalars"].items()}},
                                        "node_gate": {"ok": gate["ok"], "reason": gate["reason"], "util_after": round(gate["util_after"], 3)},
                                        "senses": {"blind": blind, "latency_age_s": None if age is None else round(age, 1), "stale": obs["stale"]},
                                        "proprioception": {k: round(v, 3) for k, v in drift.items()}}})
        # the compass: where the engine stands on the wheel, whether every level is inside Omega, whether the move at a
        # boundary points inward, and the ledger step
        fill = s["req_m"] / max(1.0, s["alloc_m"])
        levels = {"machine_fill": fill}
        moves = {"machine_fill": (1.0 if rec_n < n else -1.0 if rec_n > n else 0.0)}
        for o in ("cpufreq", "gpu", "power"):
            env = auth["organs"].get(o, {}).get("envelope")
            if env:
                levels[f"{o}_ceiling"] = env[1]
        forced = obs["queue_ratio"] > 0.0 or s["pending"] > 0
        self.audit({"compass": self.compass.read(d["state"]["E"], d["state"]["S"], levels, moves, forced, x=self.g.x, p=self.g.p)})
        out = self.audit({"decision": {"nodes_observed": n, "nodes_recommended": rec_n,
                                       "law": "compass" if self.compass_law is not None else "closure" if self.cl is not None else "governor",
                                       "compass_law": compass_rec, "hpa_target_recommended": round(rho, 3),
                                       "E": d["state"]["E"], "U": d["state"]["U"], "pending": s["pending"],
                                       "power_cap": round(float(d["power_cap"]), 3), "change_permitted": bool(d["change_permitted"]),
                                       "rollback_authorized": bool(d["rollback_authorized"]),
                                       "thermal": round(obs["thermal"], 3), "security_block": obs["security_block"],
                                       "power_stress": round(power_stress, 3), "latency_p95_ms": p95,
                                       "queue_ratio": round(obs["queue_ratio"], 3), "slo_clean": obs["slo_clean"]}, "mode": self.a.mode})
        if self.a.mode in ("target", "nodepool") and getattr(self.a, "strict_replicas", False):
            self.strict_step(s, obs)
            self.m.push(d, obs)
        elif self.a.mode in ("target", "nodepool"):
            for h in s["hpas"]:
                idx, cur = cpu_target(h)
                if cur is None:
                    continue
                ns, name = h["metadata"]["namespace"], h["metadata"]["name"]
                if not self._sensed(h):
                    continue     # a service the probe does not sense: its HPA stays at the operator's own target
                orig = int(h["metadata"].get("annotations", {}).get(ANNOTATION, cur))
                # the muscle's own clock: the autoscaler's scale-down window (300 s unless the operator set one)
                win = float(((h["spec"].get("behavior") or {}).get("scaleDown") or {}).get("stabilizationWindowSeconds", 300))
                dem = self._app_demand(h)
                if dem is not None:
                    self.demand[(ns, name)] = [(t, v) for t, v in self.demand.get((ns, name), []) if time.time() - t <= 2 * win] \
                        + [(time.time(), dem)]
                if int((h.get("status") or {}).get("currentReplicas", 0) or 0) >= int(h["spec"].get("maxReplicas", 10 ** 9)):
                    self.pinned[(ns, name)] = [t for t in self.pinned.get((ns, name), []) if time.time() - t <= 2 * win] + [time.time()]
                # more headroom is always allowed; less never: at a given load fewer pods always means a longer M/M/c wait
                # (no target above the operator's keeps the wait), so a raise only spends latency.
                # Omni on top earns its keep on machines, not by packing the operator's pods tighter
                # the same promise in queue terms: busy = target x request / limit. While convey() gives the pods a
                # limit g times the operator's, the target that keeps each pod exactly as busy is g times higher
                want = int(round(100 * min(rho, orig / 100.0) * self._gain(h)))
                back = False
                if self.compass_law is not None and getattr(self, "cruise", False):
                    # cruise (amendment 12): the service's own autoscaler runs it as it would alone (the operator's target);
                    # Omni only holds every machine in service while the queue drains
                    self.compass_law_x[(ns, name)] = orig * self._gain(h)
                    want = orig
                elif self.compass_law is not None:
                    # the compass's push and pull on the target, inside its cover [60% of the operator's, the operator's]
                    # (in queue terms, times the conveyed gain): a lower target is more pods, so the up force lowers it
                    g_ = self._gain(h); hi_t, lo_t = self._bounds(orig, g_)
                    x = self.compass_law_x.get((ns, name), hi_t)
                    load = not any(blind.values()) and s["pending"] == 0 and not obs["slo_clean"]
                    if self.compass_law.p >= self.compass_law.band.wall_high and load:
                        # fail up: the most pods the cover allows (placed below as far as the machines can hold them)
                        x = lo_t
                    elif self.compass_law.p >= self.compass_law.band.wall_high:
                        # past the wall, but not from load: a blind sense, or pods waiting for a machine that is gone.
                        # More pods answer neither, so fail up is native's own target, as on the card, where fail up is
                        # the card's own settings
                        x = hi_t; back = x != self.compass_law_x.get((ns, name), hi_t)
                    elif x < hi_t and self.compass_law.p < self.compass_law.band.center and obs["slo_clean"] and s["pending"] == 0:
                        # responses back inside the band, nothing waiting. If the demand that called the extra pods has
                        # stopped growing (a fault, a spike that passed), they were for it only: the operator's own
                        # target returns at once. While the demand still grows they stay, so the autoscaler does not
                        # remove them and start them again on the next rise
                        if not self._rising((ns, name), win):
                            x = hi_t; back = True
                    else:
                        F_ = compass_rec["force"]
                        x = x - (COMPASS_UP if F_ > 0 else COMPASS_DOWN) * F_ * (hi_t - lo_t) * self.step_scale
                    # the immune memory for pods (omni-v19): the largest rise in this service's demand seen inside two decisions
                    dem_now = self._app_demand(h)
                    if dem_now and dem_now > 0:
                        hist = (self.dem_seen.get((ns, name), []) + [dem_now])[-3:]
                        self.dem_seen[(ns, name)] = hist
                        self.dem_rise[(ns, name)] = max(self.dem_rise.get((ns, name), 1.0), dem_now / min(hist))
                    if self._held_native((ns, name)):
                        # a pod waited while the target stood below the operator's: native's target is held (omni-v19)
                        x = hi_t
                    if self._immune_native(h, ns, name, x, hi_t, lo_t, p95):
                        x = hi_t; back = x != self.compass_law_x.get((ns, name), hi_t)
                    x = max(lo_t, min(hi_t, x))
                    if x < hi_t and not back:
                        # every push for more pods, the fail-up's and the compass's alike, only as far as the machines in
                        # service can place them; the machines the rest need are asked for at once (omni-v19, Omni direct's
                        # rule: a unit never waits for a machine; a pod with no machine serves nothing, it only waits), and
                        # the pods follow as the room appears
                        x = max(x, self._placeable_target(h, s, x, hi_t, self.dem_rise.get((ns, name), 1.0)))
                    self.compass_law_x[(ns, name)] = x
                    self._replica_room(h, ns, name, win, obs, s)
                    want = int(round(x))
                want_h = want if obs["slo_clean"] else min(want, orig)
                if abs(cur - want_h) < self.a.min_target_change and not (not obs["slo_clean"] and cur > orig):
                    continue
                if cur == want_h:
                    continue
                if want_h > cur and not back and not self._steady((ns, name), win):
                    continue     # a raise (fewer pods) waits for a demand that has held still for one window
                if want_h > cur and self.a.coast_step > 0:
                    # coasting (rule 6): off the gas, the target eases toward fewer pods by at most coast_step points a
                    # window, never in one jump; a demand that comes back half way finds the pods still running and is
                    # met at once by the lower target, with no pod started again. More pods (a lower target) is never
                    # limited: the gas is always immediate
                    # (a raise comes at most once a window, below, so the step is per raise at any period: omni-v16)
                    want_h = min(want_h, cur + max(1, int(round(self.a.coast_step))))
                # the autoscaler takes its window to answer a target. A raise inside that window moves the muscle
                # mid-movement and removes pods it then starts again, so a raise is held for one window. A lower target
                # (more pods, the safe direction) is never held: on a step up the pods are asked for at once, before the
                # line is missed. A response-time breach returns the operator's target at once
                last = self.target_at.get((ns, name))
                # handing the operator's own target back is never held: it is where native stands
                if obs["slo_clean"] and last is not None and time.time() - last < win and not back and want_h > cur:
                    continue
                if "replicas" in self.a.native_muscles:
                    continue     # omni-v14: the replicas are left native; the decision is audited, nothing written
                self.target_at[(ns, name)] = time.time()
                self.changed.setdefault((ns, name), int(h["metadata"].get("annotations", {}).get(ANNOTATION, cur)))
                self.k.write(["annotate", "hpa", name, "-n", ns, "--overwrite", f"{ANNOTATION}={self.changed[(ns, name)]}"], "record original target")
                self.k.write(["patch", "hpa", name, "-n", ns, "--type=json", "-p",
                              json.dumps([{"op": "replace", "path": f"/spec/metrics/{idx}/resource/target/averageUtilization", "value": want_h}])],
                             f"HPA target to rho* = {want_h}%" + ("" if obs["slo_clean"] else " (SLO reflex: not tighter than native)"))
                self.cmd_hpa[(ns, name)] = want_h; self.cmd_at[(ns, name)] = self.decisions
            self.m.push(d, obs)
        if self.own and self.a.mode in ("target", "nodepool"):
            self._own_pods(s, obs, rho)
        if self.a.mode in ("target", "nodepool"):
            self.pod_reflex()
        want_n = rec_n
        if rec_n > n and self.last_add is not None and self.decisions - self.last_add < self.n_add:
            # machines past the scheduling floor are added at most --max-node-step a minute, however often the governor
            # decides (omni-v16; the pool gives back at most one a minute since v7); the floor's machines at once
            want_n = max(n, min(rec_n, floor))
        if self.a.mode == "nodepool" and self.a.node_scale_cmd and want_n != n:
            cfg = SimpleNamespace(minimum_nodes=self.a.min_nodes, maximum_nodes=self._max_nodes(s))
            if want_n > n:
                self.last_add = self.decisions
            acts, hits = enforce([{"action": "nodes", "target": want_n, "direction": 1 if want_n > n else -1}],
                                 {"actual_nodes": n, "power_cap": 1.0}, {"power_stress": power_stress, "security_block": obs["security_block"]}, cfg,
                                 ShieldLimits(power_limit=1e9, max_node_step=max(self.a.max_node_step, floor - n)))
            for act in acts:
                if self._pool_command(int(act["target"]), n, "node pool size", shield_interventions=hits) and not self.a.dry_run:
                    self.cmd_nodes = int(act["target"]); self.cmd_at["nodes"] = self.decisions
        if convey_due and getattr(self.a, "latency_file", "") and not self.cruise and not self.killed():
            self._convey()
        self.rec_n = rec_n
        return out


def parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["observe", "target", "nodepool"], default="observe")
    # the heartbeat, a dial (omni-v17, the founder's word of 22 October, afternoon): the main engine decides every 60 s, and any
    # beat can be set (5, 15, 30, 60, 75, 90, 120 s and every value between), each shown beside native; the fast checks run
    # every 5 s at every beat. Every rule counts seconds (omni-v16), so either can be turned alone
    ap.add_argument("--interval", type=float, default=60.0, help="seconds between governor decisions (the heartbeat, a dial; the main engine 60 s)")
    ap.add_argument("--floor-interval", type=float, default=5.0, help="seconds between the fast checks: the scheduling floor, the pod reflex, the conveyance's clock (nodepool mode)")
    ap.add_argument("--convey-every-s", type=float, default=15.0,
                    help="seconds between conveyance passes, counted on the checks (a fast check or a decision; omni-v16)")
    ap.add_argument("--iterations", type=int, default=0, help="0 = run until stopped")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--kubectl", default="kubectl")
    ap.add_argument("--audit", default="omni_audit.jsonl")
    ap.add_argument("--kill-file", default="/tmp/omni.kill")
    ap.add_argument("--no-api-proxy", action="store_true", help="read through a new kubectl process every time instead of one kubectl proxy (the controller's own cost is higher)")
    ap.add_argument("--restore-only", action="store_true", help="put every setting back from the records on the objects and exit (the watchdog's way back)")
    ap.add_argument("--node-scale-cmd", default="")
    ap.add_argument("--cruise-after", type=int, default=int(os.environ["CRUISE_AFTER"]) if os.environ.get("CRUISE_AFTER") else None,
                    help="decisions in a row with work waiting for a place before cruise puts every machine in service "
                         "(and decisions with the line empty before it ends); 0 turns cruise off; unset: --cruise-after-s")
    ap.add_argument("--cruise-after-s", type=float, default=120.0,
                    help="the same in seconds (v7: every rule of the governor counts in seconds, so its decision period can "
                         "change without changing any rule's time)")
    ap.add_argument("--idle-demand", "--brake-demand", dest="idle_demand", type=float,
                    default=float(os.environ.get("IDLE_DEMAND", os.environ.get("BRAKE_DEMAND", 0.05))),
                    help="the sensed services' demand (in pods' worth of CPU) at or under which the pool idles: the "
                         "machines go straight to the breathing floor (one pedal lifted all the way); 0 turns it off")
    ap.add_argument("--coast-step", type=int, default=int(os.environ.get("COAST_STEP", 25)),
                    help="the most the HPA target may ease toward fewer pods in one autoscaler window (points of "
                         "utilisation; 0: no limit). Adding pods is never limited")
    ap.add_argument("--min-nodes", type=int, default=int(os.environ.get("MIN_NODES", 2)),
                    help="machines always in service, ready for the next burst (the founder's floor: two)")
    ap.add_argument("--max-nodes", type=int, default=0,
                    help="the machine lever's top; 0, the default: read live, every ready worker plus what the cluster's "
                         "autoscaler may still add")
    ap.add_argument("--max-node-step", type=int, default=2)
    ap.add_argument("--min-target-change", type=int, default=3)
    ap.add_argument("--law", choices=["governor", "compass"], default="governor",
                    help="governor (default): the engine's allocation law; compass: the compass law at the v5 edge on the HPA "
                         "target and the node pool")
    ap.add_argument("--allow", type=float, default=0.02, help="the most a machine given back may add to the response time")
    ap.add_argument("--verdict-samples", type=int, default=200, help="requests measured before and after a machine is given back on trial")
    ap.add_argument("--verdict-every", type=int, default=None, help="decisions between trials (unset: --verdict-every-s)")
    ap.add_argument("--verdict-every-s", type=float, default=600.0, help="seconds between give-back trials")
    ap.add_argument("--verdict-recheck", type=int, default=None, help="decisions before a refused machine is tried again (unset: --verdict-recheck-s)")
    ap.add_argument("--verdict-recheck-s", type=float, default=7200.0, help="seconds before a refused machine is tried again")
    ap.add_argument("--verdict-trial-s", type=float, default=1200.0, help="seconds a give-back trial's phase may take before it is abandoned")
    ap.add_argument("--compass-tau", type=float, default=60.0, help="seconds the service takes to follow a lever (the compass's damping)")
    ap.add_argument("--compass-center", type=float, default=None,
                    help="where the compass holds the service (0 the bare service time, 1 the SLO); default 0.3 at the max, "
                         "0.4 at the tune-down")
    ap.add_argument("--cover-floor", type=float, default=0.6,
                    help="the lowest share of the operator's own autoscaler target the compass may set, its cover's floor "
                         "(omni-v24): 0.6, the factory's, asks for up to 1/0.6 of the pods native's target would; 1.0 "
                         "leaves the pod count native's. A knob, read in each declared setting by the tune study "
                         "(docs/THE_TUNE.md), never a rule")
    ap.add_argument("--dial", choices=["max", "save"], default=os.environ.get("OMNI_DIAL", "max"),
                    help="max (default): the most work, faster, never a machine given back below the cluster's own; save: "
                         "the tune-down (the v5 edge toward the line, machines given back where the response time allows)")
    ap.add_argument("--replica-ceiling", type=int, default=-1,
                    help="the most replicas Omni-Compass may raise a sensed HPA's cap to while it binds (compass law): "
                         "-1, the default, reads it live (what the machines can hold, one pod under); N, a ceiling of the "
                         "operator's own; 0 keeps the operator's cap unmoved")
    ap.add_argument("--sensed", default="",
                    help="ns/deployment,... whose response time the --latency-file measures; only their HPAs are moved "
                         "(empty: every HPA, the single-service case)")
    ap.add_argument("--closure", default="", help="JSON with the closure-law setting (e.g. tuning/GLOBAL_LEAGUE_PREREGISTRATION.json): the benchmarked law decides the node count")
    ap.add_argument("--strict-replicas", action="store_true", help="strict C: Omni-Compass sets replica counts; the HPA is pinned")
    ap.add_argument("--pod-reflex-writes", action="store_true",
                    help="let the pod reflex raise the HPA's replica floor itself (default: it gauges and writes nothing)")
    ap.add_argument("--reflex-window-s", type=float, default=30.0, help="window of probe samples the fast pod reflex reads")
    ap.add_argument("--strict-window", type=int, default=None, help="decisions a scale-down waits for (unset: --strict-window-s)")
    ap.add_argument("--strict-window-s", type=float, default=300.0, help="seconds a scale-down waits for (highest recent recommendation)")
    ap.add_argument("--headroom", type=float, default=0.5, help="spare capacity kept above pod requests (0.5 = 50%%, the default)")
    ap.add_argument("--native-release-util", type=float, default=float(os.environ.get("NATIVE_RELEASE_UTIL", 0.5)),
                    help="a machine is given back only while the machines left stay at or under this share of requests to allocatable: native's own line (the Cluster Autoscaler's scale-down utilization threshold, 0.5 by its documented default; set it to the cluster's own), so Omni-Compass never leaves the machines thinner than native's autoscaler would")
    ap.add_argument("--active-nodes-only", action="store_true",
                    help="count only nodes in service (schedulable, or cordoned but still carrying work) and the pods and usage on them")
    ap.add_argument("--node-restore-cmd", default="", help="command run once when the reset fires, returning the node pool to native")
    add_muscle_args(ap)
    ap.add_argument("--power-cmd", default="")
    ap.add_argument("--site-limit-w", type=float, default=0.0)
    ap.add_argument("--own-every-s", type=float, default=15.0,
                    help="seconds between two reconciliations of the pod muscle of its own on the fast checks (the pod autoscaler's sync)")
    ap.add_argument("--own-replicas", default=os.environ.get("OMNI_OWN_REPLICAS", ""),
                    help="ns/deployment,... no autoscaler governs, whose replica count Omni-Compass sets itself through the "
                         "workload's own scale (omni-v19, Omni-Compass by itself): its target from the workload's "
                         "omnicompass.io/target-utilization annotation (else --own-target), its range from omnicompass.io/replica-range")
    ap.add_argument("--own-target", type=float, default=None,
                    help="the busy share (percent of the CPU request) a workload of its own is held at when it names none")
    ap.add_argument("--native", default=os.environ.get("OMNI_NATIVE", ""),
                    help="muscles left native, never written (omni-v14): a comma list of " + ", ".join(MUSCLES))
    return ap


def safe_step(c, fails):
    """One decision. A failed decision is recorded and skipped: it writes nothing, so the cluster keeps the last settings
    that landed, and the next decision comes at the normal cadence. There is no automated fallback (manuscript Section
    5.8: the Unified Control Switch is mechanical, explicit, operator-controlled and 'does not rely on automated fallback
    inference'). Only a human flips the switch, for the whole harness at once: --kill-file present (or OMNI_KILL=1) turns
    Omni-Compass OFF and hands every setting back to native; removing it turns Omni-Compass back ON. Boundaries are never
    handled by switching anything off: the living band and the shield clamp every level inside its range."""
    try:
        c.step()
        return 0
    except Exception as e:
        fails += 1
        err = getattr(e, "stderr", "") or ""
        c.audit({"error": repr(e)[:500], "stderr": str(err)[-500:], "consecutive_failures": fails})
        print(f"decision failed ({fails} in a row): {e!r} {err}", file=sys.stderr, flush=True)
        return fails


def main(argv=None):
    a = parser().parse_args(argv)
    if a.restore_only:
        # the watchdog's way back for a controller that died: every setting back to the operator's, from the records
        # kept on the objects themselves (annotations), then exit
        c = Controller(a); c.restore(); c.audit({"decision": "restore only: every setting handed back"})
        return 0
    master.refuse_if_off("kubernetes controller")
    c = Controller(a); i = 0; fails = 0
    args = list(sys.argv[1:] if argv is None else argv)
    master.register("kubernetes controller", restore=[[sys.executable, "-m", "omni_controller.controller", *args, "--restore-only"]],
                    stale_s=max(120.0, 5 * a.interval))
    import signal

    def master_off(*_):
        # the master switch pulled from the command line (tools/omni_switch.py off): hand everything back now and exit
        try:
            c.restore()
        finally:
            c.audit({"decision": "master switch: OFF; every setting handed back; exiting"})
            sys.exit(0)
    signal.signal(signal.SIGTERM, master_off)
    import atexit, resource
    t0 = time.time()
    def overhead():   # the controller's own cost: CPU seconds of this process and every kubectl/script it ran
        me, kids = resource.getrusage(resource.RUSAGE_SELF), resource.getrusage(resource.RUSAGE_CHILDREN)
        cpu = me.ru_utime + me.ru_stime + kids.ru_utime + kids.ru_stime
        c.audit({"overhead": {"cpu_s": round(cpu, 2), "wall_s": round(time.time() - t0, 1),
                              "cores_mean": round(cpu / max(1e-9, time.time() - t0), 4)}})
    atexit.register(overhead)
    # the loop keeps its own schedule (omni-v16): a decision every --interval s and a fast check every --floor-interval s
    # between, each slept to its time from the schedule, never --interval after the last step ended, so the steps' own
    # time does not stretch every clock (before omni-v16 a decision of 60 s came every 62 to 67 s on kind, and one of 5 s
    # would have come every 7). A step that overruns its slot is followed at once by the next due one; missed slots are
    # skipped, never run in a burst, and the lateness is in the audit
    due = time.time()
    while a.iterations == 0 or i < a.iterations:
        master.heartbeat()
        t_dec = time.time()
        fails = safe_step(c, fails); i += 1
        c.audit({"decision_ms": round(1000 * (time.time() - t_dec), 1)})
        if a.iterations == 0 or i < a.iterations:
            nxt = due + a.interval
            if a.mode == "nodepool":
                k = 1
                while due + k * a.floor_interval < nxt - 1e-6:
                    slot = due + k * a.floor_interval
                    if time.time() > slot + a.floor_interval:                 # this slot is long gone: skip it
                        k += 1
                        continue
                    time.sleep(max(0.0, slot - time.time()))
                    try:
                        c.floor_step()
                    except Exception as e:
                        c.audit({"error": "floor check: " + repr(e)[:500], "stderr": str(getattr(e, "stderr", "") or "")[-500:]})
                    k += 1
            late = time.time() - nxt
            if a.interval > 0 and late > a.interval:
                c.audit({"behind_s": round(late, 1), "why": "a step outran its slot; the slots missed are skipped, not run at once"})
                nxt = time.time()
            time.sleep(max(0.0, nxt - time.time()))
            due = nxt


if __name__ == "__main__":
    main()
