#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The plug between Omni-Compass and an autoscaler that Crane owns (the Crane test, ADDONS=crane in scripts/kind_bench.sh;
docs/CRANE_PREREGISTRATION.md).

Crane builds the service's HPA (ehpa-<name>) from its EffectiveHorizontalPodAutoscaler and writes the HPA's settings, labels
and annotations back whenever they differ from the ones it builds, so a move written to the HPA itself would be undone at
Crane's next pass, and two writers on one knob is what the one-writer rule forbids. This wrapper stands where kubectl
stands (the controller's --kubectl), exactly as the KEDA plug does (scripts/kubectl_keda.py, whose parsing, waiting and
record it shares). Every read and every other write passes through unchanged, as the Omni-Compass service account. A write
to the settings of an HPA that a Crane EHPA owns is carried to that EHPA, the one place Crane reads them from:

  HPA minReplicas / maxReplicas         ->  EHPA minReplicas / maxReplicas
  HPA CPU (or memory) target            ->  the target of the EHPA's own cpu (or memory) resource metric
  an Omni-Compass record (annotation)   ->  on the EHPA (Crane propagates the omnicompass.io/ annotations onto the HPA it
                                            builds, its operator's setting --ehpa-propagation-annotation-prefixes) and on
                                            the HPA, where the engine reads it

The engine is not changed: the same decisions reach the cluster through Crane. Anything the plug cannot carry exactly is
refused with the reason (exit 2), never approximated; every carried write is one JSON line in OMNI_PLUG_LOG."""
from __future__ import annotations

import json, os, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kubectl_keda as K  # noqa: E402  (the shared parsing, patch splitting, waiting and record)

EHPA_KIND = "effectivehorizontalpodautoscalers.autoscaling.crane.io"


def owner(hpa):
    """The name of the Crane EHPA that owns this HPA, or None."""
    for o in (hpa.get("metadata", {}) or {}).get("ownerReferences") or []:
        if o.get("kind") == "EffectiveHorizontalPodAutoscaler" and str(o.get("apiVersion", "")).startswith("autoscaling.crane.io/"):
            return o.get("name")
    return None


def metric_index(ehpa, resource):
    """Index of the EHPA's own resource metric for this resource (cpu or memory)."""
    found = [j for j, m in enumerate(ehpa["spec"].get("metrics") or [])
             if m.get("type") == "Resource" and (m.get("resource") or {}).get("name") == resource]
    if len(found) != 1:
        raise K.Refused(f"the EHPA has {len(found)} {resource} resource metrics (one is needed to carry the target)")
    return found[0]


def carry(hpa, ehpa, typ, payload):
    """The EHPA patch that carries an HPA patch exactly, and what the HPA must show once Crane rebuilt it."""
    expect = {}
    if typ == "json":
        ops = []
        for op in payload:
            path, kind = op.get("path", ""), op.get("op")
            if kind not in ("replace", "add"):
                raise K.Refused(f"json patch op {kind} on {path}")
            m = K.METRIC_PATH.match(path)
            if path in K.RANGE_PATHS:
                ops.append({"op": kind, "path": path, "value": int(op["value"])})   # the EHPA names them as the HPA does
                expect[path.rsplit("/", 1)[1]] = int(op["value"])
            elif m:
                metrics = hpa["spec"].get("metrics") or []
                i = int(m.group(1))
                if i >= len(metrics) or metrics[i].get("type") != "Resource":
                    raise K.Refused(f"{path}: the HPA's metric {i} is not a resource metric")
                res = metrics[i]["resource"]["name"]
                j = metric_index(ehpa, res)
                ops.append({"op": "replace", "path": f"/spec/metrics/{j}/resource/target/averageUtilization", "value": int(op["value"])})
                expect["target:" + res] = int(op["value"])
            else:
                raise K.Refused(f"json patch path {path}")
        return "json", ops, expect
    if typ in ("merge", "strategic"):
        spec = payload.get("spec") or {}
        if set(payload) - {"spec"} or set(spec) - set(K.RANGE_KEYS) or not spec:
            raise K.Refused(f"merge patch {json.dumps(payload)}")
        new = {k: int(v) for k, v in spec.items()}
        expect.update(new)
        return "merge", {"spec": new}, expect
    raise K.Refused(f"patch type {typ}")


def do_patch(args, name, ns, out, hpa, ehpa_name):
    typ, payload, rest = K.split_patch(out)
    ehpa = K.get(EHPA_KIND, ehpa_name, ns)
    typ2, payload2, expect = carry(hpa, ehpa, typ, payload)
    cmd = ["patch", EHPA_KIND, ehpa_name, "-n", ns, f"--type={typ2}", "-p", json.dumps(payload2), *rest]
    K.kubectl(cmd)
    after = K.wait_for(lambda: K.shows(K.get("hpa", name, ns), expect))
    K.log({"in": args, "out": [cmd], "hpa_shows": after is not None, "after_s": after})
    if after is None:
        print(f"kubectl_crane: Crane did not show {expect} on hpa/{name} within {K.WAIT_S:.0f} s", file=sys.stderr)


def do_annotate(args, name, ns, out, ehpa_name):
    toks = [t for t in out if not t.startswith("-")]
    flags = [t for t in out if t.startswith("-")]
    sets = dict(t.split("=", 1) for t in toks if "=" in t)
    drops = [t[:-1] for t in toks if t.endswith("-") and "=" not in t]
    if not sets and not drops:
        raise K.Refused(f"annotate with nothing to write: {out}")
    cmds = [["annotate", EHPA_KIND, ehpa_name, "-n", ns, *flags, *toks], list(args)]
    for c in cmds:
        K.kubectl(c)

    def settled():
        ann = (K.get("hpa", name, ns).get("metadata", {}) or {}).get("annotations") or {}
        return all(ann.get(k) == v for k, v in sets.items()) and not any(k in ann for k in drops)

    # a pass Crane began before the EHPA changed can land after the HPA write: the HPA must hold the record three reads in a
    # row (half a second apart), and the write to the HPA is made again if a pass undid it
    t0, ok, held = time.time(), False, 0
    while time.time() - t0 < K.WAIT_S:
        if settled():
            held += 1
            if held >= 3:
                ok = True; break
        else:
            held = 0
            K.kubectl(list(args), check=False)
        time.sleep(0.5)
    K.log({"in": args, "out": cmds, "hpa_shows": ok, "after_s": round(time.time() - t0, 2)})
    if not ok:
        print(f"kubectl_crane: hpa/{name} does not hold the record {out} after {K.WAIT_S:.0f} s", file=sys.stderr)


def main(argv):
    if argv and argv[0] in ("patch", "annotate") and len(argv) > 1:
        verb, kind, name, ns, out = K.parse(argv)
        if kind in K.HPA_KINDS and name:
            hpa = K.get("hpa", name, ns)
            ehpa_name = owner(hpa)
            if ehpa_name:
                try:
                    if verb == "patch":
                        do_patch(argv, name, ns, out, hpa, ehpa_name)
                    else:
                        do_annotate(argv, name, ns, out, ehpa_name)
                except K.Refused as e:
                    K.log({"in": argv, "refused": str(e)})
                    print(f"kubectl_crane: refused, the plug cannot carry this exactly: {e}", file=sys.stderr)
                    return 2
                except subprocess.CalledProcessError as e:
                    sys.stderr.write(e.stderr or "")
                    return e.returncode or 1
                return 0
    os.execvp(K.BASE, [K.BASE, *argv])   # everything else: kubectl itself, as the Omni-Compass service account


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
