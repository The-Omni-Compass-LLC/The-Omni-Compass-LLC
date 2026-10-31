# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Live muscles for the Kubernetes controller beyond HPA and nodes.

Each muscle pulls (afferent) and pushes (efferent) through kubectl, records what it changed so the reset can hand
the muscle back, and tags every write with its muscle name in the audit log.

  power_cap   push: at the max (the default dial) the cap is never set under native: each machine's idle CPU is conveyed
              to the capped deployments' running pods (convey: one click under the machine, its last 5% never handed out,
              never under the operator's limit), and the frequency ceiling and the GPU limit stay at their top. The
              tune-down (--dial save): CPU limit of each running pod = base limit x the governor's power cap, never under
              the pod's own request nor its use plus headroom (nothing fixed), resized in place (no restart; Linux CFS
              quota throttles the containers for real); pull: power from --power-cmd
  heat        pull: thermal state from the harness heat law driven by live power stress (modelled: kind has no thermometer)
  security    pull: ConfigMap key "hold" == "true" means a security hold; the shield then blocks every expansion
  rollout     push: pause a deployment's rollout while the governor does not permit change; resume it when it does;
              undo a rollout that has exceeded its progress deadline when the governor authorises rollback
  batch       push: admit (unsuspend) held batch Jobs, one a minute, only when change is permitted and load and power
              stress are under the compass's wall less one cushion (0.95 - 0.05: one click under, the nervous system's
              own admit gate); running Jobs are never suspended
  latency     pull: 95th-percentile response time over the last --latency-window-s from --latency-file (CSV written by
              scripts/latency_probe.py); pressure max(0, p95 / --slo-ms - 1) enters the engine as queue pressure
  cpu_pstate  hardware connector. pull: --rapl-cmd prints package watts (e.g. from /sys/class/powercap/intel-rapl);
              push: --cpufreq-cmd with {khz}, the frequency ceiling = max frequency x power cap (e.g. writing
              scaling_max_freq with scripts/cpufreq_ceiling.sh {khz}, see hardware/SCHEDUTIL.md, or `cpupower frequency-set -u {khz}kHz`); kill runs it with the maximum frequency
  gpu         hardware connector. pull: --gpu-query-cmd prints "watts,celsius[,min_watts[,slowdown_celsius]]" (e.g.
              `nvidia-smi --query-gpu=power.draw,temperature.gpu,power.min_limit --format=csv,noheader,nounits` plus the
              card's slowdown temperature): the card's own figures, read live. One degree under its own slowdown
              temperature reads as heat 1.0 (--gpu-temp-limit only for a card that does not report it); push:
              --gpu-power-cmd with {w}, the power limit = max limit x power cap, never under the card's own minimum
              (e.g. `nvidia-smi -pl {w}`); kill restores the maximum limit
  rightsize   push: each running pod's CPU *request* follows its measured use x (1 + headroom), resized in place through the
              pods/resize subresource (no restart); never above the limit, never below --rightsize-min-m; no decrease while
              the SLO is breached, no increase during a security hold; kill restores every original request
  coldstart   push: a deployment with no work waiting (ConfigMap key "queue" == 0, the queue a KEDA scaler would read) for
              --coldstart-idle-s seconds is scaled to zero; it is scaled back to its recorded replica count the moment
              work is waiting; kill restores the recorded count
  batch_pace  push: while power stress or heat is high, one running Job labelled omnicompass.io/pausable=true is suspended
              a minute (checkpointed training pauses instead of the site going over its limit); it is resumed when
              stress and heat are back down; kill resumes every Job Omni paused
  contain     push: an agent namespace whose measured CPU use exceeds --contain-cpu-m, or any namespace during a security
              hold, gets a ResourceQuota (limits.cpu = budget) and its running pods' CPU limits are scaled in place so the
              total fits the budget; lifted when use is back under budget; kill deletes the quota and restores the limits
  cooling     facility connector. push: --cooling-cmd with {c}, the supply-air setpoint moved between --cooling-min-c and
              --cooling-max-c by the heat state (warm setpoint while cool, saving chiller energy; cold setpoint as heat
              rises); kill runs it with --cooling-restore-c
  Hardware connectors are off unless their commands are given (not available on CI runners); the mechanism is the same.
"""
from __future__ import annotations

import csv, json, math, shlex, subprocess, time
import re

# omni-v22 (30 October): a hand-back step is tried this many times against a transient failure of the cluster's API (a 500 from
# the server, a dropped connection), 1 s apart doubling to 4 s, about 10 s in all, inside the rig's 60 s wait for the governor
# to exit and the master switch's stale time. Before, the first failed read ended the whole hand-back: six-kube run
# 41044680505, repetition 346, one 500 on the autoscaler list left every conveyed limit and the replica range behind, and the
# arm was marked invalid. Each muscle's hand-back is tried on its own, and what did not land is raised at the end, never silent.
RESTORE_TRIES = 5

CPU_ANN = "omnicompass.io/original-cpu-limit"
PAUSE_ANN = "omnicompass.io/paused-by-omni"
BATCH_LABEL = "omnicompass.io/batch=true"
PAUSABLE_LABEL = "omnicompass.io/pausable=true"
REQ_ANN = "omnicompass.io/original-cpu-request"
REPL_ANN = "omnicompass.io/original-replicas"
PACE_ANN = "omnicompass.io/paced-by-omni"
QUOTA = "omni-containment"
LIM_ANN = "omnicompass.io/original-limits"
# a raise the cluster's admission refused is not written again until the pod's limit changes or this wait passes, doubled at
# each refusal up to the last (v12): the refusal is the authority's answer, and asking again every fast check is hammering
REFUSED_WAIT_S = (300.0, 3600.0)


def milli(v):
    v = str(v)
    return float(v[:-1]) if v.endswith("m") else float(v) * 1000.0


def claim_m(container):
    """The CPU (milli) a container may use: its own limit where it has one, else its request (omni-v13). A limit is the
    container's own room up to which the kernel lets it burst; that room is its muscle's, never idle for another."""
    res = container.get("resources", {}) or {}
    req = milli((res.get("requests", {}) or {}).get("cpu", "0") or "0")
    lim = (res.get("limits", {}) or {}).get("cpu")
    return max(req, milli(lim)) if lim else req


def has_room(pod):
    """A pod with room of its own: a container whose limit is above its request, the CPU between them the pod's to burst
    into (omni-v13). Conveyed to another muscle on a host with no idle CPU, that room is a trade the engine never makes."""
    for c in pod["spec"]["containers"]:
        res = c.get("resources", {}) or {}
        if claim_m(c) > milli((res.get("requests", {}) or {}).get("cpu", "0") or "0"):
            return True
    return False


def ref(s):
    ns, name = s.split("/", 1)
    return ns, name


# what only a shell reads in a command: a pipe, a list, a redirect, a subshell, a variable or a substitution, a glob, a
# home directory, a comment, a line break (quotes are read by shlex.split as a shell reads them, and need no shell)
SHELL_ONLY = set("|&;<>()$`*?[]{}~#\n")


def run_operator_cmd(cmd, timeout=None):
    """The operator's own configured command (a site power reading, a muscle's read command, a wall meter's `cmd:`),
    with the governor's own rights, never text read from the cluster or the network. omni-v14: a command that holds nothing
    only a shell reads is split into its words and run directly, without a shell; one that does (a pipe, a redirect, a
    variable, VAR=value before the command) runs through the shell as before, so no operator's wiring changes. The
    static scan's three high findings were these calls (docs/SECURITY_SCAN.md)."""
    words = shlex.split(cmd) if not (set(cmd) & SHELL_ONLY) else None
    if words and "=" not in words[0]:
        return subprocess.run(words, capture_output=True, text=True, timeout=timeout)
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)


class Muscles:
    def __init__(self, k, a, audit):
        self.k, self.a, self.audit = k, a, audit
        self.gain = {}       # (ns, deployment) -> mean conveyed CPU limit / operator's limit
        self.refused = {}    # "ns/pod" -> (limit when refused, the raise refused, retry at (s), wait (s)), v12
        self.base = {}       # (ns, deployment) -> operator's CPU limit (millicores)
        self.thermal = 0.32  # harness initial thermal state
        self.gpu_min_w = 0.0     # the card's own minimum power limit, read live (0 until the card reports it)
        self.gpu_heat_c = 0.0    # one degree under the card's own slowdown temperature, read live (0: not reported)
        # omni-v16: the governor's decision period, so every muscle rule written per decision keeps its time at any period
        # (--interval 0 is a model's loop: each call one decision of the minute)
        self.period = float(getattr(a, "interval", 60.0) or 0.0) or 60.0
        self.pace = self.period / 60.0
        self.pushes = 0          # decisions this side has acted on: the clock of the rules below

    def _per(self, sec):
        """Decisions in sec seconds at this decision period (never fewer than one)."""
        return max(1, int(round(float(sec) / self.period)))

    def native(self, muscle):
        """omni-v14: a muscle the operator left native (--native) is never written; every other runs as before."""
        return muscle in getattr(self.a, "native_muscles", ())

    def at_max(self):
        """The max (the default dial): no level is ever set under what native runs."""
        return getattr(self.a, "dial", "max") == "max"

    # ---- afferent ---------------------------------------------------------------------------------------------------
    def sense(self, power_stress):
        o = {}
        if getattr(self.a, "thermal_model", False):
            # the heat law's step is a minute (0.86 of the heat kept a minute, omni-v16 at any decision period)
            keep, take = (0.86, 0.14) if self.pace == 1.0 else (0.86 ** self.pace, 1.0 - 0.86 ** self.pace)
            self.thermal = min(1.35, max(0.0, keep * self.thermal + take * (0.34 + 0.62 * min(1.35, power_stress))))
            o["thermal"] = self.thermal
        if getattr(self.a, "rapl_cmd", ""):
            o["cpu_watts"] = self._read(self.a.rapl_cmd)
        if getattr(self.a, "gpu_query_cmd", ""):
            out = self._run_out(self.a.gpu_query_cmd)
            try:
                vals = [float(x) for x in out.split(",")]
                w, t = vals[:2]
                o["gpu_watts"], o["gpu_celsius"] = w, t
                if len(vals) > 2 and vals[2] > 0:
                    self.gpu_min_w = vals[2]                    # the card's own floor
                if len(vals) > 3 and vals[3] > 1:
                    self.gpu_heat_c = vals[3] - 1.0             # one degree under the card's own slowdown
                limit = self.gpu_heat_c or self.a.gpu_temp_limit
                o["thermal"] = max(o.get("thermal", 0.0), min(1.35, t / max(1.0, limit)))
            except ValueError:
                pass
        lf = getattr(self.a, "latency_file", "")
        if lf and getattr(self.a, "slo_ms", 0):
            ls = latency_sense(lf, self.a.latency_window_s)
            o["latency_blind"] = 1.0 if ls["blind"] else 0.0
            o["latency_age_s"] = ls["age_s"]
            if not ls["blind"]:
                o["latency_p95_ms"] = ls["p95"]
                o["latency_pressure"] = max(0.0, ls["p95"] / self.a.slo_ms - 1.0)
                if ls["fail"]:        # failed requests in a live window are real service failures: full pressure share
                    o["latency_pressure"] = max(o["latency_pressure"], ls["fail"] / (ls["ok"] + ls["fail"]))
        cm = getattr(self.a, "security_configmap", "")
        if cm:
            ns, name = ref(cm)
            try:
                data = self.k.get("get", "configmap", name, "-n", ns, "-o", "json").get("data", {}) or {}
                o["security_block"] = 1.0 if str(data.get("hold", "")).lower() == "true" else 0.0
            except Exception:
                o["security_block"] = 0.0
        return o

    def _run_out(self, cmd):
        return run_operator_cmd(cmd).stdout.strip()

    def _read(self, cmd):
        try:
            return float(self._run_out(cmd).split()[0])
        except (ValueError, IndexError):
            return float("nan")

    def _hw(self, template, value, why):
        cmd = template.format(khz=int(value), w=int(value), v=value)
        self.audit({"write": shlex.split(cmd), "why": why, "dry_run": self.a.dry_run})
        if not self.a.dry_run:
            subprocess.run(shlex.split(cmd), check=True)

    # ---- efferent ---------------------------------------------------------------------------------------------------
    def push(self, d, obs, killed=False):
        if killed:
            return
        self.pushes += 1
        cap = 1.0 if self.at_max() else float(d["power_cap"])     # the max: never under native
        if not self.native("cpu"):
            self._power_cap(cap, obs)
        self._hardware(cap, obs)
        if not self.native("rollout"):
            self._rollout(bool(d["change_permitted"]), bool(d["rollback_authorized"]))
        if not self.native("batch"):
            self._batch(bool(d["change_permitted"]), obs)
        for name, muscle, fn in (("rightsize", "rightsize", lambda: self._rightsize(obs)), ("coldstart", "coldstart", self._coldstart),
                                 ("batch_pace", "batch", lambda: self._batch_pace(obs)), ("contain", "contain", lambda: self._contain(obs)),
                                 ("cooling", "cooling", lambda: self._cooling(obs))):
            if not self.native(muscle):
                self._guard(name, fn)

    def _may(self, organ, what):
        """Nervous-system authority for an organ ("expand", "contract", "admit", "pause"); without it, everything allowed."""
        a = getattr(self, "auth", None)
        if not a:
            return True
        return bool(a.get("organs", {}).get(organ, {}).get(what, False))

    def _envelope(self, organ, default):
        a = getattr(self, "auth", None)
        return (a or {}).get("organs", {}).get(organ, {}).get("envelope", default)

    def _guard(self, name, fn):
        """One lever failing is logged and never stops the others (nor the reset)."""
        try:
            fn()
        except Exception as e:  # noqa: BLE001
            err = getattr(e, "stderr", "") or str(e)
            self.audit({"error": f"{name}: {type(e).__name__}: {str(err).strip()[:400]}"})

    def _guard_restore(self, name, fn):
        """A lever's hand-back, tried RESTORE_TRIES times against a transient failure of the cluster's API (omni-v22: the
        hand-back must land; a 500 from the server on one read had left the conveyed limits behind), every failed try in the
        audit; one lever failing never stops the others. A fault that is not the API's weather is reported at once, not
        retried. Returns whether it landed."""
        for attempt in range(1, RESTORE_TRIES + 1):
            try:
                fn()
                return True
            except Exception as e:  # noqa: BLE001
                err = getattr(e, "stderr", "") or str(e)
                self.audit({"error": f"{name}: {type(e).__name__}: {str(err).strip()[:400]}", "attempt": attempt, "of": RESTORE_TRIES})
                if not isinstance(e, (subprocess.CalledProcessError, OSError)):
                    return False
                if attempt < RESTORE_TRIES:
                    time.sleep(min(4.0, 2.0 ** (attempt - 1)))
        return False

    # ---- new levers ---------------------------------------------------------------------------------------------------
    def _named_usage(self, ns, sel=None):
        args = ["top", "pods", "-n", ns, "--no-headers"] + (["-l", sel] if sel else [])
        try:
            out = self.k.get(*args)
        except Exception:
            return {}
        return {line.split()[0]: milli(line.split()[1]) for line in str(out).strip().splitlines() if line.strip()}

    def _rightsize(self, obs):
        for target in filter(None, getattr(self.a, "rightsize_deployments", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            ann = dep["metadata"].get("annotations", {}) or {}
            c0 = dep["spec"]["template"]["spec"]["containers"][0].get("resources", {})
            base = c0.get("requests", {}).get("cpu")
            if base is None:
                continue
            if REQ_ANN not in ann:
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{REQ_ANN}={int(milli(base))}m"], "rightsize: record original CPU request")
            sel = ",".join(f"{k}={v}" for k, v in dep["spec"]["selector"]["matchLabels"].items())
            use = self._named_usage(ns, sel)
            for pod in self._pods(dep, ns):
                pn = pod["metadata"]["name"]
                if pn not in use:
                    continue
                res = pod["spec"]["containers"][0].get("resources", {})
                cur = milli(res.get("requests", {}).get("cpu", base))
                lim = milli(res.get("limits", {}).get("cpu", "1000000m"))
                want = int(min(lim, max(self.a.rightsize_min_m, math.ceil(use[pn] * (1.0 + self.a.rightsize_headroom) / 10.0) * 10)))
                if want < cur and (not obs.get("slo_clean", True) or not self._may("pods", "contract")):
                    continue  # SLO reflex / nervous system: no shrinking without contraction authority
                if want > cur and obs.get("security_block", 0.0) > 0.5:
                    continue  # shield I1: no expansion during a security hold
                if abs(want - cur) < self.a.cap_min_change_m:
                    continue
                self.k.write(["patch", "pod", pn, "-n", ns, "--subresource", "resize", "--type=json", "-p",
                              json.dumps([{"op": "replace", "path": "/spec/containers/0/resources/requests/cpu", "value": f"{want}m"}])],
                             f"rightsize: CPU request {int(cur)}m -> {want}m in place (use {int(use[pn])}m)")

    def _coldstart(self):
        sig = getattr(self.a, "coldstart_signal", "")
        if not sig:
            return
        sns, sname = ref(sig)
        try:
            q = float((self.k.get("get", "configmap", sname, "-n", sns, "-o", "json").get("data") or {}).get("queue", "0"))
        except Exception:
            return
        self._idle = getattr(self, "_idle", 0) + 1 if q <= 0 else 0
        n_idle = int(self.a.coldstart_idle) if getattr(self.a, "coldstart_idle", None) is not None \
            else self._per(getattr(self.a, "coldstart_idle_s", 180.0))           # the idle time in seconds (omni-v16)
        for target in filter(None, getattr(self.a, "coldstart_deployments", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            ann = dep["metadata"].get("annotations", {}) or {}
            rep = int(dep["spec"].get("replicas", 1))
            if q > 0 and rep == 0 and REPL_ANN in ann:
                self.k.write(["scale", "deployment", name, "-n", ns, f"--replicas={ann[REPL_ANN]}"], f"coldstart: wake to {ann[REPL_ANN]} (queue {q:g})")
            elif self._idle >= n_idle and rep > 0 and self._may("pods", "contract"):
                self.k.write(["annotate", "deployment", name, "-n", ns, "--overwrite", f"{REPL_ANN}={rep}"], "coldstart: record replicas")
                self.k.write(["scale", "deployment", name, "-n", ns, "--replicas=0"], f"coldstart: scale to zero (idle {self._idle} decisions)")

    def _batch_pace(self, obs):
        if not getattr(self.a, "batch_pace", False):
            return
        hot = obs.get("power_stress", 0.0) >= self.a.pace_high or obs.get("thermal", 0.0) >= self.a.pace_heat \
            or (getattr(self, "auth", None) is not None and self._may("batch", "pause"))
        calm = obs.get("power_stress", 1.0) <= self.a.pace_low and obs.get("thermal", 1.0) < self.a.pace_heat - 0.06
        if self.pushes - getattr(self, "_paced_at", -10 ** 9) < self._per(60.0):
            return               # one job paused or resumed a minute, however often the governor decides (omni-v16)
        jobs = self.k.get("get", "jobs", "-A", "-l", PAUSABLE_LABEL, "-o", "json")["items"]
        if hot:
            run = [j for j in jobs if not j["spec"].get("suspend")]
            if run:
                j = run[0]; ns, name = j["metadata"]["namespace"], j["metadata"]["name"]
                self.k.write(["annotate", "job", name, "-n", ns, "--overwrite", f"{PACE_ANN}=true"], "batch_pace: record pause")
                self.k.write(["patch", "job", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"suspend": True}})],
                             f"batch_pace: pause job (power stress {obs.get('power_stress', 0.0):.2f}, heat {obs.get('thermal', 0.0):.2f})")
                self._paced_at = self.pushes
        elif calm:
            paced = [j for j in jobs if j["spec"].get("suspend") and (j["metadata"].get("annotations") or {}).get(PACE_ANN) == "true"]
            if paced:
                self._resume_job(paced[0], "batch_pace: resume job (stress and heat back down)")
                self._paced_at = self.pushes

    def _resume_job(self, j, why):
        ns, name = j["metadata"]["namespace"], j["metadata"]["name"]
        self.k.write(["patch", "job", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"suspend": False}})], why)
        self.k.write(["annotate", "job", name, "-n", ns, f"{PACE_ANN}-"], "batch_pace: clear pause record")

    def _quota(self, ns):
        try:
            return self.k.get("get", "resourcequota", QUOTA, "-n", ns, "-o", "json")
        except Exception:
            return None

    def _contain(self, obs):
        """Contain on over-budget use or a security hold; while contained each running pod gets an equal share of the
        budget as its CPU limit (in place); lift only when use is under 80% of the budget (release band) and no hold."""
        for ns in filter(None, getattr(self.a, "contain_namespaces", "").split(",")):
            total = sum(self._named_usage(ns).values())
            budget = float(self.a.contain_cpu_m)
            hold = obs.get("security_block", 0.0) > 0.5
            q = self._quota(ns)
            if q is None and (total > budget or hold):
                self.k.write(["create", "quota", QUOTA, "-n", ns, f"--hard=limits.cpu={int(budget)}m"],
                             f"contain: quota limits.cpu={int(budget)}m (use {int(total)}m)")
                q = {"metadata": {"annotations": {}}}
            elif q is not None and total < 0.8 * budget and not hold:
                self._release(ns, q, "contain: use back under budget, lift containment")
                continue
            if q is None:
                continue
            held = json.loads((q["metadata"].get("annotations") or {}).get(LIM_ANN, "{}"))
            run = [p for p in self.k.get("get", "pods", "-n", ns, "-o", "json")["items"] if p["status"].get("phase") == "Running"
                   and p["spec"]["containers"][0].get("resources", {}).get("limits", {}).get("cpu") is not None]
            share = max(10, int(budget / max(1, len(run)) / 10) * 10)
            changed = False
            for p in run:
                pn = p["metadata"]["name"]; lim = p["spec"]["containers"][0]["resources"]["limits"]["cpu"]
                if pn not in held:
                    held[pn] = lim; changed = True
                want = min(share, int(milli(held[pn])))
                if int(milli(lim)) != want:
                    self.k.write(["patch", "pod", pn, "-n", ns, "--subresource", "resize", "--type=json", "-p",
                                  json.dumps([{"op": "replace", "path": "/spec/containers/0/resources/limits/cpu", "value": f"{want}m"}])],
                                 f"contain: pod CPU limit {lim} -> {want}m in place (budget share)")
            if changed:
                # the original limits live on the quota object, so a reset in any process can restore them
                self.k.write(["annotate", "resourcequota", QUOTA, "-n", ns, "--overwrite", f"{LIM_ANN}={json.dumps(held, sort_keys=True)}"],
                             "contain: record original pod CPU limits")

    def _release(self, ns, q, why):
        # the quota goes first: while it stands, Kubernetes refuses to raise a pod's limit back above the budget share
        held = json.loads((q["metadata"].get("annotations") or {}).get(LIM_ANN, "{}"))
        self.k.write(["delete", "resourcequota", QUOTA, "-n", ns], f"{why}: delete quota")
        for pn, lim in held.items():
            self._guard(f"{why} {pn}", lambda pn=pn, lim=lim: self.k.write(
                ["patch", "pod", pn, "-n", ns, "--subresource", "resize", "--type=json", "-p",
                 json.dumps([{"op": "replace", "path": "/spec/containers/0/resources/limits/cpu", "value": lim}])],
                f"{why}: restore pod CPU limit {lim}"))

    def _cooling(self, obs):
        cmd = getattr(self.a, "cooling_cmd", "")
        if not cmd:
            return
        th = obs.get("thermal", 0.5)
        x = min(1.0, max(0.0, (th - 0.5) / 0.5))
        c = round(self.a.cooling_max_c - (self.a.cooling_max_c - self.a.cooling_min_c) * x, 1)
        c = round(min(c, max(self.a.cooling_min_c, self._envelope("cooling", [0, 99])[1])), 1)   # nervous-system envelope
        if abs(c - getattr(self, "_setpoint", -99.0)) >= 0.5:
            self._hw(cmd.replace("{c}", "{v}"), c, f"cooling: supply-air setpoint {c} C (heat {th:.2f})")
            self._setpoint = c

    def _pods(self, dep, ns):
        sel = ",".join(f"{k}={v}" for k, v in dep["spec"]["selector"]["matchLabels"].items())
        return [p for p in self.k.get("get", "pods", "-n", ns, "-l", sel, "-o", "json")["items"]
                if p["status"].get("phase") == "Running"]

    def _pod_usage(self, dep, ns):
        sel = ",".join(f"{k}={v}" for k, v in dep["spec"]["selector"]["matchLabels"].items())
        try:
            out = self.k.get("top", "pods", "-n", ns, "-l", sel, "--no-headers")
        except Exception:
            return []
        return [milli(line.split()[1]) for line in str(out).strip().splitlines() if line.strip()]

    def _resize(self, pod, ns, value, why):
        self.k.write(["patch", "pod", pod["metadata"]["name"], "-n", ns, "--subresource", "resize", "--type=json", "-p",
                      json.dumps([{"op": "replace", "path": "/spec/containers/0/resources/limits/cpu", "value": value}])], why)

    def _power_cap(self, cap, obs):
        """In-place pod resize (no restart): each running pod's CPU limit = base limit x cap; the kernel's CFS quota
        enforces it. The deployment template is not changed, so no rollout is triggered."""
        if not obs.get("slo_clean", True):
            cap = 1.0  # SLO reflex: no power capping while service is (or was just) over its response-time target
        if getattr(self.a, "latency_file", "") or self.at_max():
            # a request-served workload: its work is set by arrivals, not by the cap, so throttling it saves no energy
            # (the same CPU-seconds run later) and only adds wait. The energy goes where the work is: convey(). And at
            # the max every capped pod gets its machine's idle CPU, never less than its operator gave it
            return self.convey(obs)
        for target in filter(None, getattr(self.a, "cap_deployments", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            ann = dep["metadata"].get("annotations", {}) or {}
            c0 = dep["spec"]["template"]["spec"]["containers"][0]
            tmpl = c0.get("resources", {}).get("limits", {}).get("cpu")
            if tmpl is None:
                continue
            base = milli(ann.get(CPU_ANN, tmpl))
            req = milli(c0.get("resources", {}).get("requests", {}).get("cpu", "0"))
            want = int(max(req, round(base * max(self.a.cap_min, min(1.0, cap)) / 10.0) * 10))
            # reflex: never cap a pod below what it is using plus headroom (as the node muscle never goes below requests)
            use = self._pod_usage(dep, ns)
            if use:
                want = int(min(base, max(want, math.ceil(max(use) * (1.0 + self.a.cap_headroom) / 10.0) * 10)))
            if CPU_ANN not in ann:
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{CPU_ANN}={int(base)}m"], "power_cap: record original CPU limit")
            for pod in self._pods(dep, ns):
                cur = milli(pod["spec"]["containers"][0].get("resources", {}).get("limits", {}).get("cpu", tmpl))
                if obs.get("security_block", 0.0) > 0.5 and want > cur:
                    continue  # shield I1: no expansion during a security hold
                if abs(want - cur) < self.a.cap_min_change_m:
                    continue
                self._resize(pod, ns, f"{want}m", f"power_cap: pod CPU limit to {want}m in place (cap {cap:.3f})")

    def convey(self, obs=None):
        """Energy to where the work is (omnicompass/conveyance.py, on one machine's CPU).

        A serving pod's CPU limit is a quota: a request that needs more CPU than one quota period allows waits for the
        next period, while the machine it runs on sits idle. That wait is energy withheld from the work, not saved: the
        request uses the same CPU-seconds either way. So each machine's idle CPU is conveyed to the serving pods on it:

            c_i = min( max(L_i, (0.95 A_j - Q_j) / |P_j|), 0.95 A_j )

        A_j the machine's allocatable CPU, Q_j what every other pod on it may use (its own limit, or its request where it
        has no limit: omni-v13; the requests alone before), P_j the serving pods on it, L_i the operator's own limit. The
        machine's last five percent is never handed out (the living band), a pod never gets
        less than its operator gave it, and the requests (what the scheduler and the autoscaler read) are untouched.
        Resized in place through pods/resize: no pod restarts. No expansion during a security hold. The reset
        returns every pod to L_i.

        On kind every node is a container on one machine and reports that machine's whole CPU as its own, so the limits
        the nodes hand out sum to more than the machine: a ceiling, not a use, and the kernel's fair scheduler arbitrates
        when the serving pods ask for more than the machine, as it does for native's pods. v7 adds one guard, the same
        as the replica room's (capacity.py): on such a shared host no limit is raised while the machine's measured busy
        share is at or over 75% or cannot be read; limits already given stay, and lowering is never held back. Each hold
        is written to the audit ("convey": "held"). omni-v13 adds the hand-back: while another workload on the shared
        host has room of its own (a pod, not one of the serving pods, whose limit is above its request) and the host is
        at its top (busy at or over 75%), there is no idle CPU to convey, so every limit given goes back to the
        operator's; it is conveyed again only once the host's busy share is under 70% (the band's 5% cushion below the
        top), so the hand-back and the raise never chase each other. On KubeRay's rig the limits given in the queue's
        first half minute stayed through the saturated queue: the batch pods hashed 7.6% slower, the queue finished
        0.7% later and the web served no faster (20 October, docs/OMNI_V13.md). A host with no such workload keeps the
        v7 rule: what the serving pods use there at the top is the host's own idle, and no other muscle's room.
        Two other designs were tried in the model gate (tools/model_gate.py,
        docs/OMNI_V7.md) and refused by it: the host's CPU counted once and shared by every serving pod (at the v6 KEDA
        runs' nine replicas, 3,500m / 9 is under the operator's 500m, so nothing is ever conveyed and the +64% work and
        -53% response time of conveyance are lost whole), and a hold while a pod starts on the host (a start wait 1%
        shorter for a LOSS on work and speed). The slower pod start of the v6 KEDA runs (+12.5% mean, EVEN on the
        three-run rule) is the busier host serving more requests: the price of the work, not a fault to hold against.
        The namespace's CPU quota, where the governor's role can read it, bounds every raise (omni_controller/quota.py);
        where it cannot be read, no budget is known and the raise proceeds as on v6, Kubernetes' own admission the
        authority: the first v7 trial read an unreadable quota as zero and conveyed nothing (docs/OMNI_V7.md, section 1).

        Conveyance is on by default. It moves no work: the same requests run with less waiting. (The +26% CPU seen on
        kind is more requests served, because that load is closed-loop, not waste.) Optionally, --convey-on (a share
        of --slo-ms) engages it only once the 95th-percentile response time reaches convey-on x SLO and releases it
        below convey-off x SLO, returning every serving pod to L_i; a blind latency sense engages it (service first)."""
        from omnicompass.nervous_system import BAND
        obs = obs or {}
        targets = [ref(t) for t in filter(None, getattr(self.a, "cap_deployments", "").split(","))]
        if not targets or self.native("cpu"):
            return None
        engaged = self._convey_engaged()
        from omni_controller.capacity import HostCpuSampler, KIND_SCALE_OUT_BUSY_LIMIT, one_host
        node_items = self.k.get("get", "nodes", "-o", "json")["items"]
        alloc = {n["metadata"]["name"]: milli(n["status"]["allocatable"]["cpu"]) for n in node_items}
        pods = [p for p in self.k.get("get", "pods", "-A", "-o", "json")["items"]
                if p["status"].get("phase") in ("Running", "Pending") and p["spec"].get("nodeName")]
        shared = one_host(node_items)
        if not hasattr(self, "host_cpu"):
            self.host_cpu = HostCpuSampler()
        busy = self.host_cpu.sample() if shared else None
        # the shared host near its top, or unread: no limit is raised anywhere on it (v7); elsewhere nothing is held
        busy_hold = shared and (busy is None or busy >= KIND_SCALE_OUT_BUSY_LIMIT)
        from omni_controller.quota import CpuLimitBudget
        budget = CpuLimitBudget(self.k, self.audit)
        out = {}
        held = set()
        handed = False
        for ns, name in targets:
            self.gain[(ns, name)] = 1.0
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            ann = dep["metadata"].get("annotations", {}) or {}
            c0 = dep["spec"]["template"]["spec"]["containers"][0]
            tmpl = c0.get("resources", {}).get("limits", {}).get("cpu")
            if tmpl is None:
                continue
            base = milli(ann.get(CPU_ANN, tmpl))
            sel = dep["spec"]["selector"]["matchLabels"]
            mine = lambda p: p["metadata"].get("namespace", "default") == ns and all(
                (p["metadata"].get("labels", {}) or {}).get(k) == v for k, v in sel.items())
            serving, other = {}, {}
            for p in pods:
                node = p["spec"]["nodeName"]
                if mine(p) and p["status"].get("phase") == "Running":
                    serving.setdefault(node, []).append(p)
                elif not mine(p):
                    # every other pod by what it may use: its own limit where it has one, its request where it has none
                    # (omni-v13). Counted by requests (omni-v12 and before), a batch pod's room between its request and
                    # its limit read as idle and was conveyed to the serving pod: the queue finished later and its tail
                    # rose on KubeRay's rig (20 October, docs/OMNI_V13.md), a trade between muscles the engine never makes
                    other[node] = other.get(node, 0.0) + sum(claim_m(c) for c in p["spec"]["containers"])
            if CPU_ANN not in ann and serving:
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{CPU_ANN}={int(base)}m"], "convey: record original CPU limit")
            # omni-v13: on a shared host, another workload with room of its own (a limit above its request) and the host
            # at its top: there is no idle CPU, every limit given goes back to the operator's; under the top but within
            # the band's cushion of it, nothing is raised again, so the hand-back and the raise never chase each other
            contended = shared and busy is not None and any(not mine(p) and has_room(p) for p in pods)
            give_back = contended and busy >= KIND_SCALE_OUT_BUSY_LIMIT
            cushion = contended and busy >= KIND_SCALE_OUT_BUSY_LIMIT - BAND[0]
            handed = handed or give_back
            got = []
            for node, ps in serving.items():
                a_j = alloc.get(node, 0.0)
                share = (BAND[1] * a_j - other.get(node, 0.0)) / len(ps)
                want = int(min(max(base, math.floor(share / 10.0) * 10), BAND[1] * a_j)) if engaged and not give_back else int(base)
                for p in ps:
                    cur = milli(p["spec"]["containers"][0].get("resources", {}).get("limits", {}).get("cpu", tmpl))
                    if obs.get("security_block", 0.0) > 0.5 and want > cur:
                        got.append(cur); continue  # shield I1: no expansion during a security hold
                    if (busy_hold or cushion) and want > cur:
                        held.add(node); got.append(cur); continue  # the shared host near its top, or unread
                    permitted, reservations = budget.limit(ns, p, cur, want)
                    if abs(permitted - cur) < self.a.cap_min_change_m:
                        got.append(cur); continue
                    key = f"{ns}/{p['metadata']['name']}"
                    r = self.refused.get(key)
                    if r is not None and (cur != r[0] or permitted < r[1]):
                        self.refused.pop(key); r = None             # the pod or the raise changed: the refusal is spent
                    if r is not None and permitted > cur and time.time() < r[2]:
                        got.append(cur); continue                   # held: admission refused this raise and nothing changed
                    try:
                        self._resize(p, ns, f"{permitted}m", (
                            f"convey: the shared host at its top (busy {busy:.2f}) beside another workload's room, operator's limit {permitted}m in place"
                            if give_back else f"convey: {node} idle CPU to its {len(ps)} serving pod(s), limit {permitted}m in place"
                            if engaged else f"convey: response time calm, operator's limit {permitted}m in place"))
                    except Exception as error:
                        # Admission can race another writer. Never advertise a rejected increase to the HPA.
                        wait = REFUSED_WAIT_S[0] if r is None else min(REFUSED_WAIT_S[1], 2.0 * r[3])
                        if permitted > cur:
                            self.refused[key] = (cur, permitted, time.time() + wait, wait)
                        self.audit({"error": f"convey resize rejected: {type(error).__name__}: {str(getattr(error, 'stderr', '') or error).strip()[:400]}",
                                    "pod": key, "accepted_limit_m": cur,
                                    "held_s": wait if permitted > cur else 0.0})
                        got.append(cur)
                        # Do not reuse uncertain headroom for other pods in this decision.
                        budget.reserve(reservations, cur, permitted)
                        continue
                    budget.reserve(reservations, cur, permitted)
                    self.refused.pop(key, None)
                    out[key] = permitted; got.append(permitted)
            # the gain g = mean conveyed limit / operator's limit: the replica organ reads it to keep the operator's
            # promise in queue terms (target x request / limit) while the limit is larger
            self.gain[(ns, name)] = (sum(got) / len(got) / base) if got and base > 0 else 1.0
            self.base[(ns, name)] = base
        if held or handed:
            self.audit({"convey": "handed back" if handed else "held", "machines": sorted(held),
                        "host_busy": None if busy is None else round(busy, 3), "shared_host": shared})
        return out

    def _convey_engaged(self):
        """Hysteresis on the response time: on at convey-on x SLO, off below convey-off x SLO; blind engages."""
        on, off = getattr(self.a, "convey_on", 0.0), getattr(self.a, "convey_off", 0.0)
        lf, slo = getattr(self.a, "latency_file", ""), getattr(self.a, "slo_ms", 0.0)
        if not on or not lf or not slo:
            return True
        ls = latency_sense(lf, self.a.latency_window_s)
        was = getattr(self, "_conveying", False)
        now = True if ls["blind"] else (ls["p95"] >= on * slo or (was and ls["p95"] >= off * slo))
        if now != was:
            self.audit({"convey": "engaged" if now else "released", "p95_ms": None if ls["blind"] else round(ls["p95"], 1),
                        "slo_ms": slo, "blind": ls["blind"]})
        self._conveying = now
        return now

    def _hardware(self, cap, obs):
        cap = 1.0 if not obs.get("slo_clean", True) else max(self.a.cap_min, min(1.0, cap))
        if obs.get("security_block", 0.0) > 0.5:
            cap = min(cap, getattr(self, "_last_cap", 1.0))  # shield I1: no expansion during a security hold
        if abs(cap - getattr(self, "_last_cap", 1.0)) < 0.02:
            return
        if getattr(self.a, "cpufreq_policy_root", "") and not self.native("clock"):
            self._cpufreq_sysfs(cap, obs)
        if getattr(self.a, "cpufreq_cmd", "") and self.a.cpu_max_khz and not self.native("clock"):
            lo, hi = self._envelope("cpufreq", [0.0, 1.0]); cap = min(max(cap, lo), hi)
            self._hw(self.a.cpufreq_cmd, self.a.cpu_max_khz * cap, f"cpu_pstate: frequency ceiling {int(self.a.cpu_max_khz * cap)} kHz (cap {cap:.3f})")
        if getattr(self.a, "gpu_power_cmd", "") and self.a.gpu_max_w and not self.native("gpu"):
            w = max(self.gpu_min_w, self.a.gpu_max_w * cap)               # never under the card's own minimum
            self._hw(self.a.gpu_power_cmd, w, f"gpu: power limit {int(w)} W (cap {cap:.3f})")
        self._last_cap = cap

    def _cpufreq_sysfs(self, cap, obs):
        """CPU frequency ceiling through the kernel's own policy files (hardware/cpufreq.py).
        ceiling = min(max(cap, envelope floor, schedutil request), envelope ceiling), where the schedutil request is
        min(1, 1.25 u) at the current CPU utilisation u: the ceiling never cuts below the frequency schedutil itself
        would ask for, so it only removes headroom the scheduler is not using. The envelope ceiling (heat) wins last.
        The first write snapshots every policy; the reset restores those exact values."""
        from hardware.cpufreq import CpuFreqPolicies, schedutil_frequency_invariant
        if getattr(self, "_cf", None) is None:
            self._cf = CpuFreqPolicies(self.a.cpufreq_policy_root)
            snap = self._cf.capture_original()
            if getattr(self.a, "cpufreq_require_schedutil", False):
                self._cf.assert_schedutil()
            self.audit({"cpu_pstate_snapshot": [r.as_dict() for r in snap]})
        lo, hi = self._envelope("cpufreq", [0.0, 1.0])
        u = float(obs.get("cpu_util", obs.get("load_ratio", 1.0)))
        c = min(max(cap, lo, schedutil_frequency_invariant(u)), hi)
        w = self._cf.apply_cap(c, dry_run=self.a.dry_run)
        self.audit({"cpu_pstate_write": w, "why": f"cpu_pstate: ceiling {c:.3f} (cap {cap:.3f}, envelope [{lo:.3f}, {hi:.3f}], "
                                                  f"schedutil request {schedutil_frequency_invariant(u):.3f} at u {u:.3f})"})

    def _rollout(self, permitted, rollback):
        for target in filter(None, getattr(self.a, "rollout_guard", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            ann = dep["metadata"].get("annotations", {}) or {}
            paused = bool(dep["spec"].get("paused"))
            conds = {c["type"]: c for c in dep.get("status", {}).get("conditions", [])}
            stuck = conds.get("Progressing", {}).get("reason") == "ProgressDeadlineExceeded"
            if rollback and stuck:
                self.k.write(["rollout", "undo", f"deployment/{name}", "-n", ns], "rollout: undo stuck rollout (rollback authorised)")
                continue
            if not permitted and not paused:
                self.k.write(["annotate", "deployment", name, "-n", ns, "--overwrite", f"{PAUSE_ANN}=true"], "rollout: record pause")
                self.k.write(["rollout", "pause", f"deployment/{name}", "-n", ns], "rollout: pause (change not permitted)")
            elif permitted and paused and ann.get(PAUSE_ANN) == "true":
                self.k.write(["rollout", "resume", f"deployment/{name}", "-n", ns], "rollout: resume (change permitted)")
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{PAUSE_ANN}-"], "rollout: clear pause record")

    def _batch(self, permitted, obs):
        if not getattr(self.a, "batch", False):
            return
        if not permitted or obs.get("security_block", 0.0) > 0.5:
            return
        if obs.get("load_ratio", 1.0) >= self.a.batch_load_max or obs.get("power_stress", 1.0) >= self.a.batch_power_max:
            return
        if not self._may("batch", "admit"):
            return
        if self.pushes - getattr(self, "_admitted_at", -10 ** 9) < self._per(60.0):
            return               # one held job admitted a minute, however often the governor decides (omni-v16)
        jobs = self.k.get("get", "jobs", "-A", "-l", BATCH_LABEL, "-o", "json")["items"]
        held = sorted((j for j in jobs if j["spec"].get("suspend")), key=lambda j: j["metadata"].get("creationTimestamp", ""))
        if held:
            j = held[0]; ns, name = j["metadata"]["namespace"], j["metadata"]["name"]
            self.k.write(["patch", "job", name, "-n", ns, "--type=merge", "-p", json.dumps({"spec": {"suspend": False}})],
                         "batch: admit held job (headroom)")
            self._admitted_at = self.pushes

    # ---- kill -------------------------------------------------------------------------------------------------------
    def restore(self):
        """Every lever handed back, each tried RESTORE_TRIES times on its own; returns the names of the levers that did not land."""
        missed = []
        for name, fn in (("kill cooling", self._restore_cooling), ("kill contain", self._restore_contain),
                         ("kill batch_pace", self._restore_pace), ("kill coldstart", self._restore_coldstart),
                         ("kill rightsize", self._restore_rightsize), ("kill hardware and power cap", self._restore_core)):
            if not self._guard_restore(name, fn):
                missed.append(name)
        return missed

    def _restore_cooling(self):
        if getattr(self.a, "cooling_cmd", ""):
            self._hw(self.a.cooling_cmd.replace("{c}", "{v}"), self.a.cooling_restore_c, "reset: restore cooling setpoint")
            self._setpoint = None

    def _restore_contain(self):
        for ns in filter(None, getattr(self.a, "contain_namespaces", "").split(",")):
            q = self._quota(ns)
            if q is not None:
                self._release(ns, q, "reset")

    def _restore_pace(self):
        if getattr(self.a, "batch_pace", False):
            for j in self.k.get("get", "jobs", "-A", "-l", PAUSABLE_LABEL, "-o", "json")["items"]:
                if j["spec"].get("suspend") and (j["metadata"].get("annotations") or {}).get(PACE_ANN) == "true":
                    self._resume_job(j, "reset: resume paced job")

    def _restore_coldstart(self):
        for target in filter(None, getattr(self.a, "coldstart_deployments", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            ann = dep["metadata"].get("annotations", {}) or {}
            if REPL_ANN in ann:
                if int(dep["spec"].get("replicas", 1)) == 0:
                    self.k.write(["scale", "deployment", name, "-n", ns, f"--replicas={ann[REPL_ANN]}"], "reset: restore replicas")
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{REPL_ANN}-"], "reset: clear replica record")

    def _restore_rightsize(self):
        for target in filter(None, getattr(self.a, "rightsize_deployments", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            orig = (dep["metadata"].get("annotations", {}) or {}).get(REQ_ANN)
            if orig:
                for pod in self._pods(dep, ns):
                    if pod["spec"]["containers"][0].get("resources", {}).get("requests", {}).get("cpu") != orig:
                        self.k.write(["patch", "pod", pod["metadata"]["name"], "-n", ns, "--subresource", "resize", "--type=json", "-p",
                                      json.dumps([{"op": "replace", "path": "/spec/containers/0/resources/requests/cpu", "value": orig}])],
                                     "reset: restore original CPU request in place")
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{REQ_ANN}-"], "reset: remove request record")

    def _restore_core(self):
        if getattr(self, "_cf", None) is not None:
            self.audit({"cpu_pstate_restore": self._cf.restore(dry_run=self.a.dry_run), "why": "reset: exact pre-Omni CPU ceilings"})
        if getattr(self.a, "cpufreq_cmd", "") and self.a.cpu_max_khz and getattr(self, "_last_cap", 1.0) != 1.0:
            self._hw(self.a.cpufreq_cmd, self.a.cpu_max_khz, "reset: restore maximum CPU frequency")
        if getattr(self.a, "gpu_power_cmd", "") and self.a.gpu_max_w and getattr(self, "_last_cap", 1.0) != 1.0:
            self._hw(self.a.gpu_power_cmd, self.a.gpu_max_w, "reset: restore maximum GPU power limit")
        self._last_cap = 1.0
        for target in filter(None, getattr(self.a, "cap_deployments", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            orig = (dep["metadata"].get("annotations", {}) or {}).get(CPU_ANN)
            if orig:
                for pod in self._pods(dep, ns):
                    if pod["spec"]["containers"][0].get("resources", {}).get("limits", {}).get("cpu") != orig:
                        self._resize(pod, ns, orig, "reset: restore original pod CPU limit in place")
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{CPU_ANN}-"], "reset: remove CPU record")
        for target in filter(None, getattr(self.a, "rollout_guard", "").split(",")):
            ns, name = ref(target)
            dep = self.k.get("get", "deployment", name, "-n", ns, "-o", "json")
            if (dep["metadata"].get("annotations", {}) or {}).get(PAUSE_ANN) == "true":
                self.k.write(["rollout", "resume", f"deployment/{name}", "-n", ns], "reset: resume rollout")
                self.k.write(["annotate", "deployment", name, "-n", ns, f"{PAUSE_ANN}-"], "reset: clear pause record")


def latency_sense(path, window_s, now=None):
    """The latency afferent with its integrity (manuscript Appendix J: the nervous system owns delay and dropout
    handling). Returns p95 of successful requests in the last window, the ok and failed counts in it, and the age of
    the newest sample against the wall clock. The sense is blind when its newest sample is older than two windows, or
    when the window holds no successful request: a hung probe stops writing, and its last clean window must not be read
    as the present."""
    import os, time
    try:
        age = (now if now is not None else time.time()) - os.path.getmtime(path)
        rows = list(csv.DictReader(open(path)))
    except OSError:
        return {"p95": float("nan"), "ok": 0, "fail": 0, "age_s": float("inf"), "blind": True}
    if not rows:
        return {"p95": float("nan"), "ok": 0, "fail": 0, "age_s": age, "blind": True}
    t_end = float(rows[-1]["elapsed_seconds"])
    win = [r for r in rows if float(r["elapsed_seconds"]) >= t_end - window_s]
    ms = sorted(float(r["latency_ms"]) for r in win if r.get("ok") == "1")
    fails = sum(1 for r in win if r.get("ok") != "1")
    p95 = ms[min(len(ms) - 1, int(0.95 * len(ms)))] if ms else float("nan")
    return {"p95": p95, "ok": len(ms), "fail": fails, "age_s": age, "blind": age > 2.0 * window_s or not ms}


def latency_window(path, window_s, now=None):
    """The last window_s seconds of successful probe samples (ms), with the same integrity rule as latency_sense."""
    import os, time
    try:
        age = (now if now is not None else time.time()) - os.path.getmtime(path)
        rows = list(csv.DictReader(open(path)))
    except OSError:
        return {"ms": [], "blind": True}
    if not rows:
        return {"ms": [], "blind": True}
    t_end = float(rows[-1]["elapsed_seconds"])
    ms = [float(r["latency_ms"]) for r in rows if r.get("ok") == "1" and float(r["elapsed_seconds"]) >= t_end - window_s]
    return {"ms": ms, "blind": age > 2.0 * window_s or not ms}


def latency_p95(path, window_s):
    """95th-percentile response time (ms) of successful requests in the last window_s seconds of the probe CSV."""
    try:
        rows = list(csv.DictReader(open(path)))
    except OSError:
        return float("nan")
    if not rows:
        return float("nan")
    t_end = float(rows[-1]["elapsed_seconds"])
    ms = sorted(float(r["latency_ms"]) for r in rows if r.get("ok") == "1" and float(r["elapsed_seconds"]) >= t_end - window_s)
    fails = sum(1 for r in rows if r.get("ok") != "1" and float(r["elapsed_seconds"]) >= t_end - window_s)
    if fails and not ms:
        return 1e9
    return ms[min(len(ms) - 1, int(0.95 * len(ms)))] if ms else float("nan")


def add_args(ap):
    ap.add_argument("--cap-deployments", default="", help="ns/name[,ns/name]: power_cap muscle scales their CPU limit")
    ap.add_argument("--cap-min", type=float, default=0.0,
                    help="lowest power cap the tune-down applies, a share of the operator's limit; 0 (the default): nothing "
                         "fixed, the pod's own request and its use plus headroom are the floor")
    ap.add_argument("--cap-min-change-m", type=int, default=20, help="smallest CPU-limit change written, millicores")
    ap.add_argument("--cap-headroom", type=float, default=0.3, help="power cap never below pod CPU usage x (1 + headroom)")
    ap.add_argument("--latency-file", default="", help="probe CSV (elapsed_seconds,latency_ms,ok) for the latency afferent")
    ap.add_argument("--slo-ms", type=float, default=0.0, help="95th-percentile response-time target, ms")
    ap.add_argument("--latency-window-s", type=float, default=60.0)
    ap.add_argument("--convey-on", type=float, default=0.0,
                    help="0 (default): convey idle CPU always; > 0: only once p95 reaches this share of --slo-ms")
    ap.add_argument("--convey-off", type=float, default=0.25, help="return pods to the operator's limit once p95 is below this share")
    ap.add_argument("--slo-clear", type=int, default=None, help="decisions the SLO must stay met before densifying or capping again (unset: --slo-clear-s)")
    ap.add_argument("--slo-clear-s", type=float, default=180.0, help="seconds the SLO must stay met before densifying or capping again")
    ap.add_argument("--thermal-model", action="store_true", help="heat muscle: thermal state from the harness heat law")
    ap.add_argument("--security-configmap", default="", help="ns/name of a ConfigMap whose key 'hold' signals a security hold")
    ap.add_argument("--rollout-guard", default="", help="ns/name[,ns/name]: rollout muscle pauses, resumes, undoes")
    ap.add_argument("--batch", action="store_true", help="batch muscle: admit held Jobs labelled " + BATCH_LABEL)
    ap.add_argument("--batch-load-max", type=float, default=0.9,
                    help="admit held work only under this load: the compass's wall less one cushion (0.95 - 0.05)")
    ap.add_argument("--batch-power-max", type=float, default=0.9,
                    help="admit held work only under this power stress: the wall less one cushion, as the nervous system")
    ap.add_argument("--rapl-cmd", default="", help="cpu_pstate pull: prints CPU package watts")
    ap.add_argument("--cpufreq-cmd", default="", help="cpu_pstate push: command template with {khz}")
    ap.add_argument("--cpufreq-policy-root", default="", help="cpu_pstate push through sysfs policies (e.g. /sys/devices/system/cpu/cpufreq); exact restore on kill")
    ap.add_argument("--cpufreq-require-schedutil", action="store_true", help="refuse to act unless every policy runs schedutil")
    ap.add_argument("--cpu-max-khz", type=float, default=0.0)
    ap.add_argument("--gpu-query-cmd", default="", help="gpu pull: prints 'watts,celsius'")
    ap.add_argument("--gpu-power-cmd", default="", help="gpu push: command template with {w}")
    ap.add_argument("--gpu-max-w", type=float, default=0.0)
    ap.add_argument("--gpu-temp-limit", type=float, default=83.0,
                    help="GPU temperature read as heat 1.0 when the card does not report its own slowdown temperature "
                         "(--gpu-query-cmd's fourth field; then one degree under it)")
    ap.add_argument("--rightsize-deployments", default="", help="ns/name[,ns/name]: rightsize muscle sets pod CPU requests from use")
    ap.add_argument("--rightsize-headroom", type=float, default=0.3)
    ap.add_argument("--rightsize-min-m", type=int, default=50)
    ap.add_argument("--coldstart-deployments", default="", help="ns/name[,ns/name]: scaled to zero when idle, woken on work")
    ap.add_argument("--coldstart-signal", default="", help="ns/name of a ConfigMap whose key 'queue' is the waiting work")
    ap.add_argument("--coldstart-idle", type=int, default=None, help="idle decisions before scaling to zero (unset: --coldstart-idle-s)")
    ap.add_argument("--coldstart-idle-s", type=float, default=180.0, help="idle seconds before scaling to zero (omni-v16)")
    ap.add_argument("--batch-pace", action="store_true", help="batch_pace muscle: pause Jobs labelled " + PAUSABLE_LABEL + " under stress")
    ap.add_argument("--pace-high", type=float, default=0.95, help="power stress that pauses a job")
    ap.add_argument("--pace-low", type=float, default=0.8, help="power stress under which a paused job resumes")
    ap.add_argument("--pace-heat", type=float, default=0.96, help="heat state that pauses a job")
    ap.add_argument("--contain-namespaces", default="", help="ns[,ns]: agent namespaces held to --contain-cpu-m")
    ap.add_argument("--contain-cpu-m", type=float, default=1000.0)
    ap.add_argument("--cooling-cmd", default="", help="cooling push: command template with {c} (supply-air setpoint, C)")
    ap.add_argument("--cooling-min-c", type=float, default=18.0)
    ap.add_argument("--cooling-max-c", type=float, default=27.0)
    ap.add_argument("--cooling-restore-c", type=float, default=22.0)
