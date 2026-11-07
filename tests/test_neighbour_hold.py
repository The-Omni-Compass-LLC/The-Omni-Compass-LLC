# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v26: another workload's waiting pods hold native's target, so the fail-up does not flip with a batch queue.

On omni-v25 the web service's target flipped between the cover's floor (30%) and native's (50%) every one or two decisions
while a batch queue's pods waited on and off beside it (the KAI scheduler's four ways: 304 flips over 30 repetitions;
docs/LOSS_CAUSES_2026-11-06.md): the decision returned native's target when a pod waited but did not start the immune
hand-back's hold, and the fast check that starts it skips a target already at native's. Here the decision starts the hold
when the waiting pods are another workload's, and the fail-up is not taken again while it runs. Where only the service's own
new pods wait (a machine still coming), the decision keeps omni-v25's rule.
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omni_controller.controller import Controller, parser  # noqa: E402

STANDIN = str(ROOT / "tests" / "standin_cluster" / "kubectl")


def pod(name, app, phase="Running"):
    return {"metadata": {"name": name, "namespace": "default", "labels": {"app": app}}, "status": {"phase": phase},
            "spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}, "limits": {"cpu": "500m"}}}]}}


def cluster(tmp):
    nodes = [{"metadata": {"name": f"n{i}"}, "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}
             for i in range(6)]
    pods = [pod(f"web-{i}", "web") for i in range(3)] + [pod(f"batch-{i}", "batch") for i in range(4)]
    cpu = {"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": 50}}}
    cur = [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": 40}}}]
    hpas = [{"metadata": {"name": "web", "namespace": "default"},
             "spec": {"minReplicas": 1, "maxReplicas": 10, "metrics": [cpu], "scaleTargetRef": {"kind": "Deployment", "name": "web"}},
             "status": {"currentReplicas": 3, "desiredReplicas": 3, "currentMetrics": cur}}]
    deployments = [{"metadata": {"name": "web", "namespace": "default", "annotations": {}},
                    "spec": {"replicas": 3, "selector": {"matchLabels": {"app": "web"}},
                             "template": {"spec": {"containers": [{"name": "web", "resources": {
                                 "requests": {"cpu": "200m"}, "limits": {"cpu": "500m"}}}]}}}}]
    st = Path(tmp) / "state.json"
    st.write_text(json.dumps({"nodes": nodes, "pods": pods, "hpas": hpas, "deployments": deployments, "used_per_node": "300m"}))
    os.environ["STANDIN_KUBE_STATE"] = str(st)
    os.environ["STANDIN_KUBE_LOG"] = str(Path(tmp) / "writes.log")
    return st


def waiting(st, app, n):
    """n of the app's pods Pending, the rest Running."""
    state = json.loads(st.read_text())
    k = 0
    for p in state["pods"]:
        if p["metadata"]["labels"]["app"] == app:
            p["status"]["phase"] = "Pending" if k < n else "Running"
            k += 1
    st.write_text(json.dumps(state))


def hot_probe(tmp):
    p = Path(tmp) / "latency.csv"                       # 600 ms on a 500 ms line: the compass law past its wall
    p.write_text("elapsed_seconds,latency_ms,ok\n" + "".join(f"{i * 0.5},600,1\n" for i in range(40)))
    return p


def controller(tmp):
    marker = Path(tmp) / "scaled"
    cmd = f"python3 -c \"open('{marker}', 'a').write('{{n}}\\\\n')\""
    a = parser().parse_args(["--kubectl", STANDIN, "--interval", "60", "--audit", str(Path(tmp) / "audit.jsonl"),
                             "--kill-file", str(Path(tmp) / "kill"), "--mode", "nodepool", "--law", "compass",
                             "--node-scale-cmd", cmd, "--max-node-step", "1", "--latency-file", str(hot_probe(tmp)),
                             "--slo-ms", "500", "--latency-window-s", "30"])
    return Controller(a)


def target_writes(tmp):
    out = []
    for line in (Path(tmp) / "writes.log").read_text().splitlines():
        a = json.loads(line)
        if a[:2] == ["patch", "hpa"] and "--type=json" in a:
            out.append(json.loads(a[a.index("-p") + 1])[0]["value"])
    return out


class NeighbourHold(unittest.TestCase):
    def test_a_batch_queues_waiting_pods_hold_native_target_instead_of_flipping_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            st = cluster(tmp)
            c = controller(tmp)
            for batch_waiting in (0, 2, 0, 2, 0, 0):       # the queue's pods wait on and off, as on the batch rigs
                waiting(st, "batch", batch_waiting)
                c.step()
            # omni-v25 wrote 30, 50, 30, 50, 30: the target followed the queue's waiting
            self.assertEqual(target_writes(tmp), [30, 50])
            held = [json.loads(l)["immune"] for l in (Path(tmp) / "audit.jsonl").read_text().splitlines()
                    if '"others_waiting"' in l]
            self.assertEqual(len(held), 1)
            self.assertEqual((held[0]["others_waiting"], held[0]["hold_s"]), (2, 600))

    def test_a_new_machines_daemonset_pods_never_start_the_hold(self):
        # a machine joining the pool: its DaemonSet's pod waits for that machine, not for another workload's room
        with tempfile.TemporaryDirectory() as tmp:
            st = cluster(tmp)
            state = json.loads(st.read_text())
            node_pod = pod("kube-proxy-new", "kube-proxy", "Pending")
            node_pod["metadata"].update({"namespace": "kube-system", "ownerReferences": [{"kind": "DaemonSet", "name": "kube-proxy"}]})
            state["pods"].append(node_pod)
            st.write_text(json.dumps(state))
            c = controller(tmp)
            c.step()                                        # the node's pod waits: no fail-up from load, native's target stays
            state = json.loads(st.read_text())
            state["pods"] = [p for p in state["pods"] if p["metadata"]["name"] != "kube-proxy-new"]
            st.write_text(json.dumps(state))
            c.step()                                        # nothing waits: fail up
            self.assertNotIn('"others_waiting"', (Path(tmp) / "audit.jsonl").read_text())
            self.assertEqual(target_writes(tmp)[-1], 30)

    def test_another_governed_services_waiting_pods_keep_the_rule_of_omni_v25(self):
        # a second service with its own autoscaler, its new pods waiting for a machine: its waits are its own autoscaler's and
        # the fast check's hand-back's (omni-v19), not a queue's; the decision starts no hold for them (the cloud models of the
        # gate: one service's pods waiting for a machine had started the hold for another, the 95th percentile up 2.7% at 15 s)
        with tempfile.TemporaryDirectory() as tmp:
            st = cluster(tmp)
            state = json.loads(st.read_text())
            state["pods"] += [pod(f"api-{i}", "api", "Running") for i in range(2)]
            api = json.loads(json.dumps(state["hpas"][0]))
            api["metadata"]["name"] = "api"; api["spec"]["scaleTargetRef"]["name"] = "api"
            state["hpas"].append(api)
            dep = json.loads(json.dumps(state["deployments"][0]))
            dep["metadata"]["name"] = "api"; dep["spec"]["selector"]["matchLabels"] = {"app": "api"}
            state["deployments"].append(dep)
            st.write_text(json.dumps(state))
            c = controller(tmp)
            for api_waiting in (0, 2, 0):
                waiting(st, "api", api_waiting)
                c.step()
            self.assertNotIn('"others_waiting"', (Path(tmp) / "audit.jsonl").read_text())

    def test_only_the_services_own_waiting_pods_keep_the_rule_of_omni_v25(self):
        # the service's own new pod waits (a machine still coming) and nothing else does: no hold is started from the decision
        with tempfile.TemporaryDirectory() as tmp:
            st = cluster(tmp)
            c = controller(tmp)
            for web_waiting in (0, 1, 0):
                waiting(st, "web", web_waiting)
                c.step()
            self.assertEqual(target_writes(tmp), [30, 50, 30])
            self.assertNotIn('"others_waiting"', (Path(tmp) / "audit.jsonl").read_text())


if __name__ == "__main__":
    unittest.main()
