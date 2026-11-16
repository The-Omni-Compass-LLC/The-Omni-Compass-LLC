# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v27, the place-before-asking rule (docs/OMNI_V27.md), against the standin kubectl (tests/standin_cluster/kubectl).

The founder's order of 14 November: pods waiting for a machine with Omni-Compass on top may never be worse than native; where
Omni-Compass's push makes them wait, the push goes back to native. On omni-v26 the replica room raised the autoscaler's cap to
pods sized for machines the cloud had not yet made and raised it again while pods already waited (the Azure work meter's own
audits, runs 43005182097, 43177138720, 43364393684: 10 -> 11 -> 16 -> 19 -> 22 -> 25 -> 31 -> 35, 47 asked).

  back      a cap Omni-Compass raised above the operator's, while pods of the service wait for a machine: set back to the pods
            already placed, never below the operator's own cap, and said in the audit (R2); omni-v26 kept it
  floor     the same with fewer pods placed than the operator's cap: back to the operator's cap, never below it
  no raise  the cap at the operator's, the line breached, pods waiting: no raise (R1); omni-v26 raised it to 18
  in service  the cap at the operator's, the line breached, nothing waiting, the cluster autoscaler able to add machines: the
            raise goes only to the pods the machines in service hold (14), never to machines still to come (omni-v26: 18)
  ahead     the scale-up looks forward (the founder's words of 15 November): the rate the demand has risen at every one of the
            last three beats, projected three beats ahead and never nearer than a machine's delivery (measured live from the order
            to the node ready); nothing projected while the demand is flat or falling, nor for a single jump already taken, where
            omni-v19's memory held the largest rise ever seen
"""
import json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.controller import Controller, parser, RANGE_ANN, ANNOTATION, LOOK_AHEAD_BEATS, DELIVERY_S
STANDIN = str(ROOT / "tests" / "standin_cluster" / "kubectl")


def rig(cap, cur, placed, waiting, operator=10, alloc="4", workers=6, other_m=0, room=None, target=50, orig=None, util=90):
    """A cluster whose web service stands at `cur` replicas under a cap of `cap` (the operator's own `operator`), `placed` of its
    pods on a machine and `waiting` with none, the line breached (a probe at 600 ms against a 500 ms line), the utilization 90%
    against a 50% target."""
    t = tempfile.mkdtemp()
    nodes = [{"metadata": {"name": f"n{i}"}, "status": {"allocatable": {"cpu": alloc}, "conditions": [{"type": "Ready", "status": "True"}]}}
             for i in range(workers)]
    pod = lambda i, on: {"metadata": {"name": f"web-{i}", "namespace": "default", "labels": {"app": "web"}},
                         "status": {"phase": "Running" if on else "Pending"},
                         "spec": {**({"nodeName": f"n{i % workers}"} if on else {}), "containers": [{"resources": {"requests": {"cpu": "200m"}}}]}}
    pods = [pod(i, True) for i in range(placed)] + [pod(placed + i, False) for i in range(waiting)]
    if other_m:
        pods.append({"metadata": {"name": "other", "namespace": "kube-system", "labels": {"app": "other"}}, "status": {"phase": "Running"},
                     "spec": {"nodeName": "n0", "containers": [{"resources": {"requests": {"cpu": f"{other_m}m"}}}]}})
    cpu = {"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": target}}}
    ann = {RANGE_ANN: f"1,{operator}"} if cap != operator else {}
    if orig is not None:
        ann[ANNOTATION] = str(orig)
    hpa = {"metadata": {"name": "web", "namespace": "default", "annotations": ann},
           "spec": {"minReplicas": 1, "maxReplicas": cap, "metrics": [cpu], "scaleTargetRef": {"kind": "Deployment", "name": "web"}},
           "status": {"currentReplicas": cur, "desiredReplicas": cur,
                      "currentMetrics": [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": util}}}]}}
    state = {"nodes": nodes, "pods": pods, "hpas": [hpa], "used_per_node": "300m",
             "deployments": [{"metadata": {"name": "web", "namespace": "default"},
                              "spec": {"selector": {"matchLabels": {"app": "web"}},
                                       "template": {"spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}}}]}}}}]}
    if room is not None:
        state["configmaps"] = [{"metadata": {"name": "cluster-autoscaler-status"}, "data": {"status":
            "Cluster-wide:\n  Health: Healthy (ready=%d unready=0 registered=%d)\nNodeGroups:\n  Name: pool\n"
            "  Health: Healthy (ready=%d unready=0 registered=%d longUnregistered=0 cloudProviderTarget=%d (minSize=1, maxSize=%d))\n"
            % (workers, workers, workers, workers, workers, workers + room)}}]
    st = Path(t) / "state.json"; st.write_text(json.dumps(state))
    os.environ["STANDIN_KUBE_STATE"] = str(st); os.environ["STANDIN_KUBE_LOG"] = str(Path(t) / "writes.log")
    lat = Path(t) / "latency.csv"
    lat.write_text("elapsed_seconds,latency_ms,ok\n" + "".join(f"{i * 0.5},600.0,1\n" for i in range(40)))
    marker = Path(t) / "scaled"
    cmd = f"python3 -c \"open('{marker}', 'a').write('{{n}}\\\\n')\""
    a = parser().parse_args(["--kubectl", STANDIN, "--interval", "60", "--audit", str(Path(t) / "audit.jsonl"),
                             "--kill-file", str(Path(t) / "kill"), "--mode", "nodepool", "--law", "compass",
                             "--node-scale-cmd", cmd, "--max-node-step", "1", "--latency-file", str(lat), "--slo-ms", "500",
                             "--latency-window-s", "30"])
    c = Controller(a); c.step()
    cap_now = json.loads(st.read_text())["hpas"][0]["spec"]["maxReplicas"]
    audit = [json.loads(l) for l in (Path(t) / "audit.jsonl").read_text().splitlines() if l.strip()]
    ann_now = json.loads(st.read_text())["hpas"][0]["metadata"].get("annotations", {})
    c.ann_now = ann_now
    return cap_now, audit, c, st


def main():
    # back: Omni-Compass had raised the cap to 18; 14 pods placed, 4 waiting for a machine: back to the 14 placed
    cap, audit, _, _ = rig(cap=18, cur=18, placed=14, waiting=4)
    assert cap == 14, f"a raised cap kept while 4 pods wait: cap {cap}, expected 14 (the pods already placed)"
    back = [r["immune"] for r in audit if (r.get("immune") or {}).get("replica_room") == "back while pods wait"]
    assert back and back[0]["cap_was"] == 18 and back[0]["cap"] == 14 and back[0]["waiting"] == 4 and back[0]["placed"] == 14, back
    # floor: 6 placed, 6 waiting under a raised cap of 12: back to the operator's 10, never below it
    cap, _, _, _ = rig(cap=12, cur=12, placed=6, waiting=6)
    assert cap == 10, f"back below the operator's own cap: {cap}, expected 10"
    # no raise: the cap at the operator's 10, the line breached, 2 pods waiting: the cap stays (omni-v26 raised it to 18)
    cap, _, _, _ = rig(cap=10, cur=10, placed=8, waiting=2)
    assert cap == 10, f"raised while pods wait for a machine: cap {cap}, expected the operator's 10"
    # in service: two machines of 2 cores, 1 core asked by another workload, the cluster autoscaler able to add 2 more: the
    # machines in service hold (4000 - 1000) // 200 - 1 = 14; omni-v26 asked 18 on machines still to come
    cap, _, c, st = rig(cap=10, cur=10, placed=10, waiting=0, alloc="2", workers=2, other_m=1000, room=2)
    assert cap == 14, f"raised onto machines not yet made: cap {cap}, expected 14 (the machines in service)"
    h = json.loads(st.read_text())["hpas"][0]
    assert c._live_ceiling(h) == (8000 - 1000) // 200 - 1 and c._live_ceiling(h, in_service=True) == (4000 - 1000) // 200 - 1
    assert c._own_pod_counts(h) == (10, 0)
    # ... and the 4 pods the machines still to come would hold are held back, counted for the stand-ins to ask the cloud for
    # their machine (tests/test_standins.py), never asked for by a real pod left waiting
    assert c.held_back_m == 4 * 200, c.held_back_m
    # native's count (R3): the target at 30% where native's is 50%, 18 pods asked at a demand of 5.4 pods' requests (native's
    # own count 11), 14 placed and 4 waiting: the cap goes from the operator's 20 to 14, the pods placed (never below native's
    # 11), the operator's range recorded first; omni-v26 kept 20 and the 4 waited for a machine
    cap, audit, c3, _ = rig(cap=20, cur=18, placed=14, waiting=4, operator=20, target=30, orig=50, util=30)
    assert cap == 14, f"Omni-Compass's own pods kept while they wait: cap {cap}, expected 14"
    assert c3.ann_now.get(RANGE_ANN) == "1,20", c3.ann_now
    r3 = [r["immune"] for r in audit if (r.get("immune") or {}).get("replica_room") == "back while pods wait"]
    assert r3 and r3[0]["native_count"] == 11 and r3[0]["target_below_native"] is True, r3
    # ... and where native's own count is above the pods placed, native's count stands: 8 placed, 10 waiting, native's 11
    cap, _, _, _ = rig(cap=20, cur=18, placed=8, waiting=10, operator=20, target=30, orig=50, util=30)
    assert cap == 11, f"below native's own count: cap {cap}, expected native's 11"
    # ... and the fast check withdraws them too, at once, not at the next decision: the cap stands at the operator's 20 again
    # with the 4 still waiting, and one fast check sets it back to the 14 placed
    cap, _, c5, st5 = rig(cap=20, cur=18, placed=14, waiting=4, operator=20, target=30, orig=50, util=30)
    S5 = json.loads(st5.read_text()); S5["hpas"][0]["spec"]["maxReplicas"] = 20; st5.write_text(json.dumps(S5))
    c5.floor_step()
    assert json.loads(st5.read_text())["hpas"][0]["spec"]["maxReplicas"] == 14, "the fast check left Omni-Compass's pods waiting"
    # the release: nothing waits, the machines in service hold 119 pods: back to the operator's 20, the record removed
    cap, _, c4, _ = rig(cap=14, cur=14, placed=14, waiting=0, operator=20, target=30, orig=50, util=30)
    assert cap == 20 and RANGE_ANN not in c4.ann_now, (cap, c4.ann_now)
    # ahead: the look-ahead is three beats, never nearer than a machine's delivery
    assert LOOK_AHEAD_BEATS == 3 and DELIVERY_S == 120.0
    for beat, horizon in ((60, 180.0), (15, 120.0), (10, 120.0), (120, 360.0)):
        c.a.interval = beat; c.delivery_s = DELIVERY_S
        assert c._horizon_s() == horizon, (beat, c._horizon_s())
    c.a.interval = 60
    assert c._slope([(1, 10.0)]) == 0.0                                    # one reading: no rate yet
    assert c._slope([(1, 10.0), (2, 10.0), (3, 10.0), (4, 10.0)]) == 0.0   # flat: nothing projected
    assert c._slope([(1, 16.0), (2, 14.0), (3, 12.0), (4, 10.0)]) < 0      # falling: nothing projected (the rise is its positive part)
    v = c._slope([(1, 10.0), (2, 12.0), (3, 14.0), (4, 16.0)])             # 2 pods' worth a beat of 60 s
    assert abs(v - 2.0 / 60.0) < 1e-12, v
    assert abs(max(0.0, v) * c._horizon_s() - 6.0) < 1e-9                  # three beats ahead: 6 pods' worth more
    assert c._slope([(1, 10.0), (2, 10.0), (3, 10.0), (4, 10.0), (5, 10.0), (6, 30.0)]) == 0  # a single jump is no trend
    assert c._slope([(1, 50.0), (2, 10.0), (3, 12.0), (4, 13.0), (5, 15.0)]) == 1.0 / 60.0  # only the last three beats count:
    assert c._slope([(1, 10.0), (2, 11.0), (3, 30.0), (4, 30.5)]) == 0.5 / 60.0              # the rise held at every one of them
    # the delivery measured live: a machine ordered at decision 10 is open at decision 12, at a 60 s beat 120 s; the look-ahead
    # takes half the last measure and half the new, and is never nearer than three beats
    c.order = (10, 7); c.decisions = 12; c.delivery_s = 120.0
    c._delivered({"open": 6}); assert c.order == (10, 7)                    # not landed yet
    c.decisions = 14; c._delivered({"open": 7})                             # landed after 240 s
    assert c.order is None and c.delivery_s == 180.0 and c._horizon_s() == 180.0
    print("place before asking: a raised cap goes back to the pods placed while pods wait (18 -> 14), never below the "
          "operator's (12 -> 10); no raise while pods wait; a raise only onto the machines in service (14, not 18); "
          "Omni-Compass's own pods beyond native's count withdrawn while they wait (20 -> 14, never below native's 11) and "
          "given back as the machines place them; the scale-up looks three beats ahead, never nearer than a machine's delivery, "
          "measured live")


if __name__ == "__main__":
    main()
