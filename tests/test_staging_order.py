# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The staging law's order, run through the real actuator (scripts/kind_nodepool.sh) against a stand-in kubectl:
on the way down the emptiest machine idles first (fewest serving pods, then fewest pods), on the way up the warmest
idle machine wakes first (most work still on it), two machines always stay in service (the floor), every machine is usable (an operator may hold some back), no pod is ever moved, and an
idled machine is marked prefer-not (PreferNoSchedule), never closed, so a pod that needs it lands at once."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STANDIN = r'''#!/usr/bin/env python3
import json, os, sys
p = os.environ["STAGE_STATE"]; st = json.load(open(p)); a = sys.argv[1:]
def save(): json.dump(st, open(p, "w"))
def opt(k):
    return a[a.index(k) + 1] if k in a else None
def node_of():
    for x in a:
        if x.startswith("spec.nodeName="): return x.split("=", 1)[1]
    fs = opt("--field-selector")
    return fs.split("=", 1)[1] if fs and fs.startswith("spec.nodeName=") else None
def pods():
    out = st["pods"]; n = node_of()
    if n: out = [q for q in out if q["spec"]["nodeName"] == n]
    if opt("-n"): out = [q for q in out if q["metadata"]["namespace"] == opt("-n")]
    if opt("-l"):
        k, v = opt("-l").split("=", 1); out = [q for q in out if q["metadata"]["labels"].get(k) == v]
    return out
if a[:2] == ["get", "nodes"]:
    print(json.dumps({"items": st["nodes"]}))
elif a[:2] == ["get", "pods"]:
    q = pods()
    if "--no-headers" in a: print("\n".join(x["metadata"]["name"] for x in q))
    elif opt("-o") == "name": print("\n".join("pod/" + x["metadata"]["name"] for x in q))
    elif opt("-o") and opt("-o").startswith("jsonpath"): print("\n".join(x["metadata"]["namespace"] + "/" + x["metadata"]["name"] for x in q))
    else: print(json.dumps({"items": q}))
elif a[:2] == ["get", "hpa"]:
    print(json.dumps({"items": [{"metadata": {"namespace": "default"}, "spec": {"scaleTargetRef": {"kind": "Deployment", "name": "web"}}}]}))
elif a[:2] == ["get", "deployment"]:
    print(json.dumps({"spec": {"selector": {"matchLabels": {"run": "web"}}}}))
elif a[:2] == ["taint", "node"]:
    n = next(x for x in st["nodes"] if x["metadata"]["name"] == a[2]); t = a[3]
    taints = n["spec"].setdefault("taints", [])
    if t.endswith("-"): n["spec"]["taints"] = [x for x in taints if x["key"] != t.split(":")[0].split("=")[0]]
    else:
        key = t.split(":")[0].split("=")[0]; n["spec"]["taints"] = [x for x in taints if x["key"] != key] + [{"key": key, "effect": t.split(":")[1]}]
    st["log"].append(["taint", a[2], t]); save()
elif a[:1] == ["uncordon"]:
    n = next(x for x in st["nodes"] if x["metadata"]["name"] == a[1]); n["spec"].pop("unschedulable", None)
    st["log"].append(["uncordon", a[1]]); save()
elif a[:1] == ["annotate"]:
    st["log"].append(["annotate"] + a[1:]); save()
elif a[:1] in (["delete"], ["drain"], ["evict"], ["cordon"]):
    st["log"].append(["FORBIDDEN"] + a); save()
'''


def node(name):
    return {"metadata": {"name": name}, "spec": {}, "status": {"conditions": [{"type": "Ready", "status": "True"}]}}


def pod(name, on, serving=True):
    return {"metadata": {"name": name, "namespace": "default", "labels": {"run": "web"} if serving else {"app": "other"}},
            "spec": {"nodeName": on}, "status": {"phase": "Running"}}


class StagingOrder(unittest.TestCase):
    def run_pool(self, d, want, floor=None, cushion=None):
        env = dict(os.environ, KUBECTL=str(d / "kubectl"), STAGE_STATE=str(d / "state.json"), WORKER_SEL="x")
        env.pop("MIN_NODES", None); env.pop("NODE_CUSHION", None)
        if floor is not None:
            env["MIN_NODES"] = str(floor)
        if cushion is not None:
            env["NODE_CUSHION"] = str(cushion)
        r = subprocess.run(["bash", str(ROOT / "scripts" / "kind_nodepool.sh"), str(want)], env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads((d / "state.json").read_text())

    def test_order_down_and_up(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            (d / "kubectl").write_text(STANDIN); (d / "kubectl").chmod(0o755)
            st = {"nodes": [node(n) for n in ("w1", "w2", "w3", "w4")],
                  "pods": [pod("a1", "w1"), pod("a2", "w1"), pod("a3", "w1"), pod("b1", "w2"), pod("d1", "w4"), pod("d2", "w4"),
                           pod("x1", "w4", serving=False)],
                  "log": []}
            (d / "state.json").write_text(json.dumps(st))
            idle = lambda s: [n["metadata"]["name"] for n in s["nodes"] if any(x["key"] == "omnicompass.io/idle" for x in n["spec"].get("taints", []))]
            # down 4 -> 2: the emptiest first (w3: no serving pod, then w2: one), the busiest stay
            s = self.run_pool(d, 2)
            self.assertEqual(sorted(idle(s)), ["w2", "w3"])
            self.assertTrue(all(x["effect"] == "PreferNoSchedule" for n in s["nodes"] for x in n["spec"].get("taints", [])))
            self.assertFalse([l for l in s["log"] if l[0] == "FORBIDDEN"], "no pod moved, no machine closed or deleted")
            # up 2 -> 3: the warmest idle machine wakes first (w2 still carries a pod; w3 carries none)
            s = self.run_pool(d, 3)
            self.assertEqual(idle(s), ["w3"])
            # down to 0 asked: two machines always stay in service (the floor), ready for a spike
            s = self.run_pool(d, 0)
            self.assertEqual(len(idle(s)), 2)
            # with the floor set to three by the operator, three stay
            s = self.run_pool(d, 0, floor=3)
            self.assertEqual(len(idle(s)), 1)
            # back up to 4: every machine usable, all 4 open, no boot
            s = self.run_pool(d, 4)
            self.assertEqual(idle(s), [])
            # an operator who holds one machine back (NODE_CUSHION=1): 3 open, 1 held
            s = self.run_pool(d, 4, cushion=1)
            self.assertEqual(len(idle(s)), 1)

    def test_foreign_cordon_left_alone(self):
        # a machine someone else cordoned (maintenance, an upgrade's drain) is never uncordoned, never counted, and the
        # governor's own idle mark on it comes off; waking every machine (the OFF switch's reset) leaves it cordoned
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            (d / "kubectl").write_text(STANDIN); (d / "kubectl").chmod(0o755)
            nodes = [node(n) for n in ("w1", "w2", "w3", "w4", "w5")]
            nodes[3]["spec"] = {"unschedulable": True}                                          # w4: cordoned, no mark
            nodes[4]["spec"] = {"unschedulable": True, "taints": [{"key": "omnicompass.io/idle", "effect": "PreferNoSchedule"}]}
            st = {"nodes": nodes, "pods": [pod("a1", "w1"), pod("b1", "w2"), pod("d1", "w4"), pod("e1", "w5")], "log": []}
            (d / "state.json").write_text(json.dumps(st))
            s = self.run_pool(d, 100000)
            by = {n["metadata"]["name"]: n["spec"] for n in s["nodes"]}
            self.assertTrue(by["w4"].get("unschedulable") and by["w5"].get("unschedulable"), "a foreign cordon stays")
            self.assertFalse([l for l in s["log"] if l[0] == "uncordon"], "never uncordons")
            self.assertFalse(any(x["key"] == "omnicompass.io/idle" for x in by["w5"].get("taints", [])), "own mark removed")
            # down to 2: only the three open machines count; the cordoned ones are neither in service nor idled
            s = self.run_pool(d, 2)
            idled = [n["metadata"]["name"] for n in s["nodes"] if any(x["key"] == "omnicompass.io/idle" for x in n["spec"].get("taints", []))]
            self.assertEqual(idled, ["w3"])
            self.assertFalse([l for l in s["log"] if l[0] in ("uncordon", "FORBIDDEN")])


def main():
    r = unittest.TextTestRunner(verbosity=0).run(unittest.defaultTestLoader.loadTestsFromTestCase(StagingOrder))
    if not r.wasSuccessful():
        raise SystemExit(1)
    print("PASS staging order: the emptiest idles first, the warmest wakes first, two always in service (the floor), every machine usable, no pod moved, a machine someone else cordoned left alone")


if __name__ == "__main__":
    main()
