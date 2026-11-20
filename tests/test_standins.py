# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v27, the stand-ins (docs/OMNI_V27.md, section 4), against the standin kubectl (tests/standin_cluster/kubectl).

The founder's words of 15 November: "we don't want to make pods scale up when we can't give it to them"; "if it's scaling up,
it should be looking forward 3 steps". Through a cloud, a new machine is made by the cloud's own autoscaler, and only for a pod
that waits. The stand-ins are pods of the lowest priority that hold room and no work (deploy/kind/omni-headroom.yaml); the
governor sizes them for the demand looked ahead and the pods held back beyond the room the machines in service and the parked
ones have; the cloud makes their machine, and a real pod displaces a stand-in at once.

  rising      two machines of 2 cores, 2 cores asked, the requests rising 3 cores over the look-ahead, the cloud able to add 2:
              12 stand-ins of 250m, so 1 core's worth waits for the cloud's machine
  held back   nothing rising, 2.5 cores of pods held back until a machine can take them: 10 stand-ins
  parked      a third machine parked by the governor holds the rise: no stand-in (the floor opens the parked one first)
  room        the cloud's autoscaler at its pool's top: no stand-in (none could get a machine)
  flat        nothing rising, nothing held back: the stand-ins back to none
  on site     no node is a cloud's machine: nothing written, whatever is rising
  tune-down   the dial at save, or the cloud's give-back-only: none (the bill may not rise there)
  absent      the stand-ins not installed: nothing written, said once in the audit
  unseen      a stand-in is never a pod that waits, nor a request, in the governor's reading or its fast check
  reset       the reset sets the stand-ins back to none
"""
import json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.controller import Controller, parser, snapshot, standin, HEADROOM
STANDIN = str(ROOT / "tests" / "standin_cluster" / "kubectl")


def cluster(cloud=True, parked=0, room=2, installed=True, standin_pods=1, dial=None, give_back_only=False):
    t = tempfile.mkdtemp()
    nodes = [{"metadata": {"name": f"n{i}"}, "spec": {**({"providerID": f"azure:///subscriptions/x/vm/{i}"} if cloud else {}),
                                                      **({"unschedulable": True} if i >= 2 else {})},
              "status": {"allocatable": {"cpu": "2"}, "conditions": [{"type": "Ready", "status": "True"}]}} for i in range(2 + parked)]
    web = [{"metadata": {"name": f"web-{i}", "namespace": "default", "labels": {"app": "web"}}, "status": {"phase": "Running"},
            "spec": {"nodeName": f"n{i % 2}", "containers": [{"resources": {"requests": {"cpu": "200m"}}}]}} for i in range(10)]
    stand = [{"metadata": {"name": f"{HEADROOM}-{i}", "namespace": "default", "labels": {"app": HEADROOM}}, "status": {"phase": "Pending"},
              "spec": {"containers": [{"resources": {"requests": {"cpu": "250m"}}}]}} for i in range(standin_pods)]
    deps = [{"metadata": {"name": "web", "namespace": "default"}, "spec": {"selector": {"matchLabels": {"app": "web"}},
             "template": {"spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}}}]}}}}]
    if installed:
        deps.append({"metadata": {"name": HEADROOM, "namespace": "default"}, "spec": {"replicas": 0, "selector": {"matchLabels": {"app": HEADROOM}},
                     "template": {"spec": {"containers": [{"resources": {"requests": {"cpu": "250m"}}}]}}}})
    state = {"nodes": nodes, "pods": web + stand, "hpas": [], "used_per_node": "300m", "deployments": deps,
             "configmaps": [{"metadata": {"name": "cluster-autoscaler-status"}, "data": {"status":
                 "NodeGroups:\n  Name: pool\n  Health: Healthy (ready=%d unready=0 registered=%d longUnregistered=0 "
                 "cloudProviderTarget=%d (minSize=1, maxSize=%d))\n" % (2 + parked, 2 + parked, 2 + parked, 2 + parked + room)}}]}
    st = Path(t) / "state.json"; st.write_text(json.dumps(state))
    os.environ["STANDIN_KUBE_STATE"] = str(st); os.environ["STANDIN_KUBE_LOG"] = str(Path(t) / "writes.log")
    args = ["--kubectl", STANDIN, "--interval", "60", "--audit", str(Path(t) / "audit.jsonl"), "--kill-file", str(Path(t) / "kill"),
            "--mode", "nodepool", "--node-scale-cmd", "true"]
    if dial:
        args += ["--dial", dial]
    a = parser().parse_args(args)
    a.give_back_only = give_back_only
    c = Controller(a)
    s = snapshot(c.k, active_only=True)
    return c, s, st, Path(t)


def standins(st):
    return next(d for d in json.loads(st.read_text())["deployments"] if d["metadata"]["name"] == HEADROOM)["spec"]["replicas"]


def audits(t):
    f = t / "audit.jsonl"
    return [json.loads(l) for l in f.read_text().splitlines() if l.strip()] if f.exists() else []


def main():
    # unseen: the waiting stand-in is no pod waiting and no request; the reading is the ten web pods' 2 cores
    c, s, st, t = cluster()
    assert standin({"metadata": {"labels": {"app": HEADROOM}}}) and not standin({"metadata": {"labels": {"app": "web"}}})
    assert s["pending"] == 0 and s["req_m"] == 2000 and all(not standin(p) for p in s["pods"]), (s["pending"], s["req_m"])
    assert c.floor_step() is None, "the fast check read a waiting stand-in as a pod waiting"
    # rising: 4 cores in service, 2 free, 3 cores rising over the look-ahead, the cloud able to add 2 machines: 1 core short;
    # the stand-ins number the free room and the shortfall, (2000 + 1000) / 250 = 12, so 1 core's worth waits for the machine
    c.burst_m, c.held_back_m = 3000.0, 0.0
    c._headroom(s)
    assert standins(st) == 12, standins(st)
    h = [r["headroom"] for r in audits(t) if "headroom" in r]
    assert h and h[-1]["stand_ins"] == 12 and h[-1]["short_m"] == 1000 and h[-1]["free_m"] == 2000 and h[-1]["machine_room"] == 2, h
    # flat: nothing rising, nothing held back: back to none
    c.burst_m = 0.0
    S = json.loads(st.read_text()); next(d for d in S["deployments"] if d["metadata"]["name"] == HEADROOM)["spec"]["replicas"] = 12
    st.write_text(json.dumps(S)); c._headroom(s)
    assert standins(st) == 0, standins(st)
    # held back: nothing rising, 2.5 cores of pods held back until a machine can take them: (2000 + 500) / 250 = 10
    c.held_back_m = 2500.0; c._headroom(s)
    assert standins(st) == 10, standins(st)
    # reset: back to none
    c.restore()
    assert standins(st) == 0, standins(st)
    # parked: a third machine the governor parked holds the 3 cores' rise with the free room: no stand-in
    c, s, st, t = cluster(parked=1)
    assert s["pool"] == 3 and s["open"] == 2, (s["pool"], s["open"])
    c.burst_m = 3000.0; c._headroom(s)
    assert standins(st) == 0, standins(st)
    c.burst_m = 5000.0; c._headroom(s)                          # beyond the parked machine too: 1 core short, 20 stand-ins
    assert standins(st) == 20, standins(st)
    # room: the cloud's autoscaler at its pool's top: none could get a machine, none asked
    c, s, st, t = cluster(room=0)
    c.burst_m = 3000.0; c._headroom(s)
    assert standins(st) == 0, standins(st)
    # on site: nothing written, whatever is rising
    c, s, st, t = cluster(cloud=False)
    c.burst_m = 3000.0; c._headroom(s)
    assert standins(st) == 0 and not [r for r in audits(t) if "headroom" in r], audits(t)
    # tune-down and give-back-only: none
    for kw in ({"dial": "save"}, {"give_back_only": True}):
        c, s, st, t = cluster(**kw)
        c.burst_m = 3000.0; c._headroom(s)
        assert standins(st) == 0, (kw, standins(st))
    # absent: nothing written, said once
    c, s, st, t = cluster(installed=False)
    c.burst_m = 3000.0; c._headroom(s); c._headroom(s)
    said = [r["headroom"] for r in audits(t) if "headroom" in r]
    assert len(said) == 1 and said[0]["installed"] is False, said
    print("stand-ins: through a cloud, sized for the rise ahead and the pods held back beyond the free room and the parked "
          "machines (12, 10, 0 with a parked machine, 20 beyond it), none at the pool's top, on site, at the tune-down or on "
          "give-back-only; never read as a pod waiting or a request; said once where not installed; none after the reset")


if __name__ == "__main__":
    main()
