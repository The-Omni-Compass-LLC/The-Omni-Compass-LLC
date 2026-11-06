# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Cruise and idle, the one pedal lifted all the way (rules 7 and 8), through the live controller against the standin kubectl: work waiting
for a place two decisions in a row puts every machine in service, and they stay until the line has been empty two
decisions; with nothing waiting and the sensed service's demand at zero the machines go straight to the floor (two) in
one move, never below it."""
import json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.controller import Controller, parser
STANDIN = str(ROOT / "tests" / "standin_cluster" / "kubectl")


def cluster(tmp, pending, util, replicas, used="200m"):
    ready = [{"type": "Ready", "status": "True"}]
    nodes = [{"metadata": {"name": f"w{i}"}, "spec": {}, "status": {"allocatable": {"cpu": "4"}, "conditions": ready}} for i in range(6)]
    pod = lambda where, phase="Running": {"metadata": {"name": f"p-{where}", "namespace": "default", "labels": {"run": "php-apache"},
                                                       "ownerReferences": [{"kind": "ReplicaSet"}]},
                                          "status": {"phase": phase}, "spec": {"nodeName": where, "containers": [{"resources": {"requests": {"cpu": "200m"}}}]}}
    pods = [pod(f"w{i}") for i in range(6)] + [{"metadata": {"name": f"wait-{j}", "namespace": "default"}, "status": {"phase": "Pending"},
                                                 "spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}}}]}} for j in range(pending)]
    cpu = {"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": 50}}}
    hpas = [{"metadata": {"name": "php-apache", "namespace": "default"},
             "spec": {"minReplicas": 1, "maxReplicas": 10, "scaleTargetRef": {"kind": "Deployment", "name": "php-apache"}, "metrics": [cpu]},
             "status": {"currentReplicas": replicas, "desiredReplicas": replicas,
                        "currentMetrics": [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": util}}}]}}]
    st = Path(tmp) / "state.json"
    st.write_text(json.dumps({"nodes": nodes, "pods": pods, "hpas": hpas, "used_per_node": used, "deployments": [], "configmaps": [], "jobs": []}))
    os.environ["STANDIN_KUBE_STATE"] = str(st); os.environ["STANDIN_KUBE_LOG"] = str(Path(tmp) / "writes.log")


def main():
    t = tempfile.mkdtemp(); sized = Path(t) / "sized"
    a = parser().parse_args(["--kubectl", STANDIN, "--mode", "nodepool", "--interval", "0", "--min-nodes", "2", "--max-nodes", "6",
                             "--audit", str(Path(t) / "audit.jsonl"), "--kill-file", str(Path(t) / "kill"),
                             "--sensed", "default/php-apache", "--node-scale-cmd", f"sh -c 'echo {{n}} >> {sized}'"])
    c = Controller(a)
    sizes = lambda: [int(x) for x in sized.read_text().split()] if sized.exists() else []
    events = lambda key: [json.loads(l)[key] for l in (Path(t) / "audit.jsonl").read_text().splitlines() if key in json.loads(l)]

    # cruise: work waiting for a place, two decisions in a row
    cluster(t, pending=4, util=95, replicas=6, used="3500m")
    c.step(); assert "on" not in events("cruise"), "one decision with work waiting is not yet cruise"
    c.step(); assert events("cruise")[-1:] == ["on"], events("cruise")
    assert c.cruise
    # cruise steps back (amendment 12): the floor step reads nothing and writes nothing while cruising
    n_audit = len((Path(t) / "audit.jsonl").read_text().splitlines())
    assert c.floor_step() is None and len((Path(t) / "audit.jsonl").read_text().splitlines()) == n_audit, \
        "the floor step acted during cruise"
    # the line empties: cruise holds one decision more, then ends
    cluster(t, pending=0, util=60, replicas=6, used="2500m")
    c.step(); assert c.cruise, "cruise ends only after the line has been empty two decisions"
    c.step(); assert not c.cruise and events("cruise")[-1] == "off", events("cruise")

    # idle: nothing waiting, the service's demand at zero: straight to the breathing floor, never below it
    cluster(t, pending=0, util=0, replicas=1, used="50m")
    for _ in range(40):
        c.step()
        if events("idle_floor"):
            break
    eb = events("idle_floor")
    assert eb, "the pool never went to its idle floor at zero demand"
    assert eb[0]["to"] == 2 and eb[0]["from"] > 2, eb
    assert all(n >= 2 for n in sizes()), sizes()
    # idle as a served service really stands (amendment 9): one pod, its floor, a probe keeping it at 10% of a 50% target
    def idles(util, replicas):
        t2 = tempfile.mkdtemp()
        a2 = parser().parse_args(["--kubectl", STANDIN, "--mode", "nodepool", "--interval", "0", "--min-nodes", "2", "--max-nodes", "6",
                                  "--audit", str(Path(t2) / "audit.jsonl"), "--kill-file", str(Path(t2) / "kill"),
                                  "--sensed", "default/php-apache", "--node-scale-cmd", "true"])
        c2 = Controller(a2)
        cluster(t2, pending=0, util=util, replicas=replicas, used="200m")
        for _ in range(40):
            c2.step()
        return [json.loads(l)["idle_floor"] for l in (Path(t2) / "audit.jsonl").read_text().splitlines()
                if "idle_floor" in json.loads(l)]
    idle = idles(10, 1)
    assert idle and idle[0]["to"] == 2 and idle[0]["at_idle"], "the pool did not idle with the service idle at its floor"
    assert not idles(10, 3), "the pool idled with the service above its floor"
    assert not idles(40, 1), "the pool idled with the service busy at its floor (40% of a 50% target)"
    print(f"cruise: on after two decisions with work waiting, off after two with the line empty; idle: "
          f"{eb[0]['from']} -> {eb[0]['to']} machines in one move at zero demand, never below the floor")
    print("PASS test_cruise_idle")


if __name__ == "__main__":
    main()
