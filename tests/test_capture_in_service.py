# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Which machines the recorder counts in service (fleet/capture/kube_capture.sh, ACTIVE_ONLY=1). On 18 and 19 October three
native repetitions of the CruiseKube test (runs 39171059299, repetitions 5 and 10; 39175670991, repetition 2) were refused
for "no machine in service" while the service answered every probe: CruiseKube had marked every worker
cruisekube.truefoundry.com/overloaded:NoSchedule, and the recorder took any NoSchedule mark for a machine out of service.
The recorder is run here on a cluster as those repetitions saw it, through a stand-in kubectl."""
import csv, json, os, shutil, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CP = {"key": "node-role.kubernetes.io/control-plane", "effect": "NoSchedule"}
OVER = {"key": "cruisekube.truefoundry.com/overloaded", "effect": "NoSchedule"}


def node(name, taints=(), ready=True, unschedulable=None, cp=False):
    labels = {"node-role.kubernetes.io/control-plane": ""} if cp else {}
    return {"metadata": {"name": name, "labels": labels}, "spec": {"taints": list(taints), "unschedulable": unschedulable},
            "status": {"allocatable": {"cpu": "2"},
                       "conditions": [{"type": "Ready", "status": "True" if ready else "Unknown"}]}}


def pod(on, owner="ReplicaSet", phase="Running"):
    return {"metadata": {"ownerReferences": [{"kind": owner}]}, "spec": {"nodeName": on, "containers": [
        {"resources": {"requests": {"cpu": "100m"}}}]}, "status": {"phase": phase}}


def capture(nodes, pods):
    """The recorder's first row on this cluster: (nodes ready, nodes counted in service)."""
    d = Path(tempfile.mkdtemp())
    (d / "nodes.json").write_text(json.dumps({"items": nodes}))
    (d / "pods.json").write_text(json.dumps({"items": pods}))
    k = d / "kubectl"
    k.write_text(f"""#!/usr/bin/env bash
case "$1 $2" in
  "get nodes") cat {d}/nodes.json ;;
  "get pods") cat {d}/pods.json ;;
  "get hpa") echo '{{"items":[]}}' ;;
  "top nodes") ;;
esac
""")
    k.chmod(0o755)
    env = dict(os.environ, PATH=f"{d}:{os.environ['PATH']}", OUT=str(d / "capture.csv"), INTERVAL="1", DURATION="0",
               ACTIVE_ONLY="1")
    subprocess.run(["bash", str(ROOT / "fleet" / "capture" / "kube_capture.sh")], env=env, check=True, timeout=60,
                   capture_output=True)
    row = next(csv.DictReader(open(d / "capture.csv")))
    shutil.rmtree(d)
    return int(row["nodes_ready"]), int(row["nodes_total"])


def test_workers_marked_overloaded_by_the_add_on_still_serve():
    # as the refused repetitions stood: every node marked by CruiseKube, the control plane with its own role mark too
    nodes = [node("cp", [CP, OVER], cp=True), node("w1", [OVER]), node("w2", [OVER])]
    pods = [pod("w1"), pod("w2"), pod("cp"), pod("w1", owner="DaemonSet")]
    assert capture(nodes, pods) == (2, 2)          # the two workers serve; before 19 October: (0, 0), the window refused


def test_what_still_takes_a_machine_out_of_service():
    nodes = [node("cp", [CP], cp=True),                                                      # the control plane
             node("gone", [{"key": "node.kubernetes.io/unreachable", "effect": "NoSchedule"}], ready=False),  # a lost machine
             node("press", [{"key": "node.kubernetes.io/memory-pressure", "effect": "NoSchedule"}]),           # Kubernetes' own mark
             node("evict", [{"key": "example.com/drain", "effect": "NoExecute"}]),           # an eviction mark
             node("idle", [OVER]),                                                           # marked and carrying nothing
             node("open")]                                                                   # open, carrying nothing
    pods = [pod("cp"), pod("gone"), pod("press"), pod("evict")]
    assert capture(nodes, pods) == (1, 1)          # only the open worker


def test_the_governors_own_marks_read_as_before():
    nodes = [node("cordoned", unschedulable=True), node("parked", [{"key": "omnicompass.io/idle", "effect": "PreferNoSchedule"}]),
             node("parked-empty", [{"key": "omnicompass.io/idle", "effect": "PreferNoSchedule"}]), node("open")]
    pods = [pod("cordoned"), pod("parked")]
    assert capture(nodes, pods) == (3, 3)          # closed but carrying counts; closed and empty does not
