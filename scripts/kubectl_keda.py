#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The plug between Omni-Compass and an autoscaler that KEDA owns (the add-on test, ADDONS=keda in scripts/kind_bench.sh).

KEDA builds the service's HPA from its ScaledObject and writes the HPA back whenever the two differ, so a move written to
the HPA itself would be undone within a second, and two writers on one knob is what the one-writer rule forbids. This
wrapper stands where kubectl stands (the controller's --kubectl). Every read and every other write passes through
unchanged, as the Omni-Compass service account (scripts/kubectl_omni.sh, or OMNI_KUBECTL). A write to the settings of an
HPA that a KEDA ScaledObject owns is carried to that ScaledObject, the one place KEDA reads them from:

  HPA minReplicas / maxReplicas         ->  ScaledObject minReplicaCount / maxReplicaCount
  HPA CPU (or memory) target            ->  the value of the ScaledObject's cpu (or memory) trigger
  an Omni-Compass record (annotation)   ->  on the ScaledObject (KEDA copies its annotations onto every HPA it rebuilds)
                                            and on the HPA, where the engine reads it

The engine is not changed: it reads the HPA as it always does, and the same decisions reach the cluster through KEDA. A
carried setting is written once to the ScaledObject; the plug then waits (up to OMNI_PLUG_WAIT_S, 20 s) for KEDA to show it
on the HPA, as a write to the HPA itself would show at once. Anything the plug cannot carry exactly is refused with the
reason (exit 2), never approximated. Every carried write is one JSON line in OMNI_PLUG_LOG: what came in, what went out,
whether the HPA showed it and after how long.
"""
from __future__ import annotations

import json, os, re, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = os.environ.get("OMNI_KUBECTL") or str(HERE / "kubectl_omni.sh")
HPA_KINDS = {"hpa", "hpas", "horizontalpodautoscaler", "horizontalpodautoscalers", "hpa.autoscaling",
             "horizontalpodautoscalers.autoscaling"}
SO_KIND = "scaledobjects.keda.sh"
WAIT_S = float(os.environ.get("OMNI_PLUG_WAIT_S", "20"))
METRIC_PATH = re.compile(r"^/spec/metrics/(\d+)/resource/target/averageUtilization$")
RANGE_PATHS = {"/spec/minReplicas": "/spec/minReplicaCount", "/spec/maxReplicas": "/spec/maxReplicaCount"}
RANGE_KEYS = {"minReplicas": "minReplicaCount", "maxReplicas": "maxReplicaCount"}


class Refused(Exception):
    """A write the plug cannot carry exactly."""


def kubectl(args, check=True):
    return subprocess.run([BASE, *args], capture_output=True, text=True, check=check)


def get(kind, name, ns):
    return json.loads(kubectl(["get", kind, name, "-n", ns, "-o", "json"]).stdout)


def log(rec):
    path = os.environ.get("OMNI_PLUG_LOG")
    if path:
        with open(path, "a") as f:
            f.write(json.dumps({"time": round(time.time(), 3), **rec}) + "\n")


def parse(args):
    """(verb, kind, name, namespace, the remaining tokens) of a kubectl command line as the engine writes it."""
    verb, rest = args[0], list(args[1:])
    kind = rest.pop(0) if rest else ""
    name = None
    if "/" in kind:
        kind, name = kind.split("/", 1)
    ns, out, i = "default", [], 0
    while i < len(rest):
        t = rest[i]
        if t in ("-n", "--namespace") and i + 1 < len(rest):
            ns = rest[i + 1]; i += 2; continue
        if t.startswith("--namespace="):
            ns = t.split("=", 1)[1]; i += 1; continue
        if name is None and not t.startswith("-"):
            name = t; i += 1; continue
        out.append(t); i += 1
    return verb, kind.lower(), name, ns, out


def owner(hpa):
    """The name of the KEDA ScaledObject that owns this HPA, or None."""
    for o in (hpa.get("metadata", {}) or {}).get("ownerReferences") or []:
        if o.get("kind") == "ScaledObject" and str(o.get("apiVersion", "")).startswith("keda.sh/"):
            return o.get("name")
    return None


def split_patch(out):
    """(patch type, payload, other tokens) of a kubectl patch command's remaining tokens."""
    typ, payload, rest, i = "strategic", None, [], 0
    while i < len(out):
        t = out[i]
        if t.startswith("--type="):
            typ = t.split("=", 1)[1]
        elif t == "--type" and i + 1 < len(out):
            typ = out[i + 1]; i += 1
        elif t in ("-p", "--patch") and i + 1 < len(out):
            payload = out[i + 1]; i += 1
        elif t.startswith(("--patch=", "-p=")):
            payload = t.split("=", 1)[1]
        else:
            rest.append(t)
        i += 1
    if payload is None:
        raise Refused("a patch with no payload")
    return typ, json.loads(payload), rest


def trigger_index(so, resource):
    """Index of the ScaledObject's trigger that sets the HPA's target for this resource (cpu or memory)."""
    found = [j for j, t in enumerate(so["spec"].get("triggers") or []) if t.get("type") == resource]
    if len(found) != 1:
        raise Refused(f"the ScaledObject has {len(found)} {resource} triggers (one is needed to carry the target)")
    return found[0]


def carry(hpa, so, typ, payload):
    """The ScaledObject patch that carries an HPA patch exactly, and what the HPA must show once KEDA rebuilt it."""
    expect = {}
    if typ == "json":
        ops = []
        for op in payload:
            path, kind = op.get("path", ""), op.get("op")
            if kind not in ("replace", "add"):
                raise Refused(f"json patch op {kind} on {path}")
            m = METRIC_PATH.match(path)
            if path in RANGE_PATHS:
                ops.append({"op": kind, "path": RANGE_PATHS[path], "value": int(op["value"])})
                expect[path.rsplit("/", 1)[1]] = int(op["value"])
            elif m:
                metrics = hpa["spec"].get("metrics") or []
                i = int(m.group(1))
                if i >= len(metrics) or metrics[i].get("type") != "Resource":
                    raise Refused(f"{path}: the HPA's metric {i} is not a resource metric")
                res = metrics[i]["resource"]["name"]
                j = trigger_index(so, res)
                ops.append({"op": "replace", "path": f"/spec/triggers/{j}/metadata/value", "value": str(int(op["value"]))})
                expect["target:" + res] = int(op["value"])
            else:
                raise Refused(f"json patch path {path}")
        return "json", ops, expect
    if typ in ("merge", "strategic"):
        spec = payload.get("spec") or {}
        if set(payload) - {"spec"} or set(spec) - set(RANGE_KEYS) or not spec:
            raise Refused(f"merge patch {json.dumps(payload)}")
        new = {RANGE_KEYS[k]: int(v) for k, v in spec.items()}
        expect.update({k: int(v) for k, v in spec.items()})
        return "merge", {"spec": new}, expect
    raise Refused(f"patch type {typ}")


def shows(hpa, expect):
    spec = hpa.get("spec", {}) or {}
    for k, v in expect.items():
        if k.startswith("target:"):
            res = k.split(":", 1)[1]
            got = [m["resource"]["target"].get("averageUtilization") for m in spec.get("metrics") or []
                   if m.get("type") == "Resource" and m["resource"]["name"] == res]
            if got != [v]:
                return False
        elif spec.get(k) != v:
            return False
    return True


def wait_for(check):
    """Seconds until check() held (None if it never did within WAIT_S)."""
    t0 = time.time()
    while True:
        if check():
            return round(time.time() - t0, 2)
        if time.time() - t0 >= WAIT_S:
            return None
        time.sleep(0.25)


def do_patch(args, name, ns, out, hpa, so_name):
    typ, payload, rest = split_patch(out)
    so = get(SO_KIND, so_name, ns)
    typ2, payload2, expect = carry(hpa, so, typ, payload)
    cmd = ["patch", SO_KIND, so_name, "-n", ns, f"--type={typ2}", "-p", json.dumps(payload2), *rest]
    kubectl(cmd)
    after = wait_for(lambda: shows(get("hpa", name, ns), expect))
    log({"in": args, "out": [cmd], "hpa_shows": after is not None, "after_s": after})
    if after is None:
        print(f"kubectl_keda: KEDA did not show {expect} on hpa/{name} within {WAIT_S:.0f} s", file=sys.stderr)


def do_annotate(args, name, ns, out, so_name):
    toks = [t for t in out if not t.startswith("-")]
    flags = [t for t in out if t.startswith("-")]
    sets = dict(t.split("=", 1) for t in toks if "=" in t)
    drops = [t[:-1] for t in toks if t.endswith("-") and "=" not in t]
    if not sets and not drops:
        raise Refused(f"annotate with nothing to write: {out}")
    cmds = [["annotate", SO_KIND, so_name, "-n", ns, *flags, *toks], list(args)]
    for c in cmds:
        kubectl(c)

    def settled():
        ann = (get("hpa", name, ns).get("metadata", {}) or {}).get("annotations") or {}
        return all(ann.get(k) == v for k, v in sets.items()) and not any(k in ann for k in drops)

    # a rebuild KEDA began before the ScaledObject changed can land after the HPA write: the HPA must hold the record as
    # asked three reads in a row (half a second apart), and the write to the HPA is made again if a rebuild undid it
    t0, ok, held = time.time(), False, 0
    while time.time() - t0 < WAIT_S:
        if settled():
            held += 1
            if held >= 3:
                ok = True; break
        else:
            held = 0
            kubectl(list(args), check=False)
        time.sleep(0.5)
    log({"in": args, "out": cmds, "hpa_shows": ok, "after_s": round(time.time() - t0, 2)})
    if not ok:
        print(f"kubectl_keda: hpa/{name} does not hold the record {out} after {WAIT_S:.0f} s", file=sys.stderr)


def main(argv):
    if argv and argv[0] in ("patch", "annotate") and len(argv) > 1:
        verb, kind, name, ns, out = parse(argv)
        if kind in HPA_KINDS and name:
            hpa = get("hpa", name, ns)
            so_name = owner(hpa)
            if so_name:
                try:
                    if verb == "patch":
                        do_patch(argv, name, ns, out, hpa, so_name)
                    else:
                        do_annotate(argv, name, ns, out, so_name)
                except Refused as e:
                    log({"in": argv, "refused": str(e)})
                    print(f"kubectl_keda: refused, the plug cannot carry this exactly: {e}", file=sys.stderr)
                    return 2
                except subprocess.CalledProcessError as e:
                    sys.stderr.write(e.stderr or "")
                    return e.returncode or 1
                return 0
    os.execvp(BASE, [BASE, *argv])   # everything else: kubectl itself, as the Omni-Compass service account


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
