# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The compass law in the live Kubernetes controller (--law compass), against the standin kubectl (tests/standin_cluster/kubectl).

  calm      p95 far under the SLO: the compass pulls down, the HPA target never rises above the operator's (never tighter
            than native), and the node pool gives one machine back per decision through the release gate
  hot       p95 past the 0.95 wall: fail up, the HPA target goes to the bottom of its cover (60% of the operator's) at
            once and the node pool asks for one machine more
  blind     no live probe samples: read as past the wall, same as hot
  demand    calm again while the demand still grows: the extra pods stay; the operator's target returns once the
            demand has stopped growing for one autoscaler window (no remove-then-restart)
  steady    a raise of the target (fewer pods) waits for a demand steady for one autoscaler window
  room      the replica cap raised only while it binds and the line is threatened, up to the operator's ceiling;
            returned when calm and steady; the reset restores it
  sensed    two services, the probe measuring one: only its HPA moves; the neighbour's stays the operator's
  restore   the reset returns every HPA target to the operator's and removes every record
  engine    the six-state engine still runs every decision (E and U in the audit) and the decision names the compass law
"""
import json, os, sys, tempfile, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.controller import Controller, parser, ANNOTATION, UNBOUNDED
STANDIN = str(ROOT / "tests" / "standin_cluster" / "kubectl")


def cluster(tmp, target=50):
    nodes = [{"metadata": {"name": f"n{i}"}, "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}
             for i in range(6)]
    pods = [{"status": {"phase": "Running"}, "spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}}}]}} for _ in range(3)]
    cpu = {"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": target}}}
    cur = [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": 40}}}]
    hpas = [{"metadata": {"name": "web", "namespace": "default"}, "spec": {"minReplicas": 1, "maxReplicas": 10, "metrics": [cpu]},
             "status": {"currentReplicas": 3, "desiredReplicas": 3, "currentMetrics": cur}}]
    st = Path(tmp) / "state.json"; st.write_text(json.dumps({"nodes": nodes, "pods": pods, "hpas": hpas, "used_per_node": "300m"}))
    os.environ["STANDIN_KUBE_STATE"] = str(st); os.environ["STANDIN_KUBE_LOG"] = str(Path(tmp) / "writes.log")
    return st


def probe(tmp, ms, n=40):
    p = Path(tmp) / "latency.csv"
    rows = ["elapsed_seconds,latency_ms,ok"] + [f"{i * 0.5},{ms},1" for i in range(n)]
    p.write_text("\n".join(rows) + "\n"); os.utime(p, None)
    return p


def controller(tmp, lat, *extra):
    marker = Path(tmp) / "scaled"
    cmd = f"python3 -c \"open('{marker}', 'a').write('{{n}}\\\\n')\""
    a = parser().parse_args(["--kubectl", STANDIN, "--interval", "60", "--audit", str(Path(tmp) / "audit.jsonl"),
                             "--kill-file", str(Path(tmp) / "kill"), "--mode", "nodepool", "--law", "compass",
                             "--node-scale-cmd", cmd, "--max-node-step", "1", "--latency-file", str(lat), "--slo-ms", "500",
                             "--latency-window-s", "30", *extra])
    return Controller(a), marker


def target_now(st):
    return json.loads(st.read_text())["hpas"][0]["spec"]["metrics"][0]["resource"]["target"]["averageUtilization"]


def decisions(tmp):
    return [json.loads(l)["decision"] for l in (Path(tmp) / "audit.jsonl").read_text().splitlines() if '"decision"' in l
            and isinstance(json.loads(l).get("decision"), dict)]


def main():
    # calm: p95 = 50 ms on a 500 ms SLO (position 0.1)
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 50.0)
    c, marker = controller(t, lat)
    for _ in range(6):
        c.step()
    ns = [int(x) for x in marker.read_text().split()] if marker.exists() else []
    d = decisions(t)
    assert all(x["law"] == "compass" and x["compass_law"] is not None for x in d), "decision does not name the compass law"
    assert all("E" in x and "U" in x for x in d), "the engine did not run"
    assert target_now(st) <= 50, "the compass tightened the HPA past the operator's target"
    assert all(b - a in (-1, 0) for a, b in zip([6] + ns, ns)), f"more than one machine back per decision: {ns}"
    print(f"calm: target {target_now(st)} (operator 50, never higher), node commands {ns}, "
          f"force {d[-1]['compass_law']['force']}, position {d[-1]['compass_law']['position']}")

    # hot: p95 = 600 ms (position 1.2, past the wall): fail up at once
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 600.0)
    c, marker = controller(t, lat)
    c.step()
    ns = [int(x) for x in marker.read_text().split()] if marker.exists() else []
    assert target_now(st) == 30, f"fail up: target {target_now(st)}, expected the cover's bottom 30"
    assert ns and ns[-1] == 7 or c.a.max_nodes < 7, f"fail up: node commands {ns}"
    print(f"hot: target 50 -> {target_now(st)} at once (fail up), node command {ns}")

    # the fault is over: responses back inside the band, nothing waiting. The operator's own target returns at once,
    # inside the autoscaler's window, so the extra pods last only as long as the fault
    lat = probe(t, 50.0)
    for k in range(1, 4):
        c.step()
        if target_now(st) == 50:
            break
    assert target_now(st) == 50, f"fault over: target {target_now(st)}, expected the operator's 50 back at once"
    print(f"fault over: target back to 50 after {k} decision(s), inside the autoscaler's window")

    # demand still growing: a breach called the extra pods and the CPU the service uses keeps rising (the next load
    # step). Calm again, but the pods stay: handing the operator's target back now would remove them and start them
    # again on the next rise. Once the demand has stopped growing for one autoscaler window, the target returns
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 600.0)
    c, marker = controller(t, lat); c.step()
    assert target_now(st) == 30
    S = json.loads(st.read_text()); S["hpas"][0]["status"]["currentMetrics"][0]["resource"]["current"]["averageUtilization"] = 90
    st.write_text(json.dumps(S))
    lat = probe(t, 50.0)
    for _ in range(3):
        c.step()
    assert target_now(st) == 30, f"rising demand: target {target_now(st)}, expected the pods held at 30"
    k = ("default", "web"); c.demand[k] = [(tt - 400.0, u) for tt, u in c.demand[k]]   # one window (300 s) on, flat since
    c.pinned[k] = [tt - 400.0 for tt in c.pinned.get(k, [])]
    c.target_at = {k: v - 400.0 for k, v in c.target_at.items()}
    c.step()
    assert target_now(st) == 50, f"demand flat: target {target_now(st)}, expected the operator's 50 back"
    print("rising demand: pods held at 30 while the demand grew; back to 50 once it stopped growing for one window")

    # consolidation waits for a steady demand: a raise of the target (fewer, larger pods) only after the demand has held
    # still for one autoscaler window, as the autoscaler itself waits before removing pods
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 50.0)
    c, marker = controller(t, lat); now = time.time(); k = ("default", "web")
    c.demand[k] = [(now - 120 + 60 * i, 1.2) for i in range(3)]
    assert not c._steady(k, 300), "steady after 2 minutes of history"
    c.demand[k] = [(now - 295 + 59 * i, 1.2 + 0.01 * i) for i in range(6)]
    assert c._steady(k, 300), "not steady after a flat window"
    c.demand[k] = [(now - 295 + 59 * i, 1.2 + 0.2 * i) for i in range(6)]
    assert not c._steady(k, 300) and c._rising(k, 300), "a climbing demand read as steady"
    # a pinned gauge: the readings look flat because the autoscaler stood at its cap inside the window
    c.demand[k] = [(now - 295 + 59 * i, 1.2) for i in range(6)]; c.pinned[k] = [now - 100]
    assert not c._steady(k, 300.0), "flat readings at the replica cap are a pinned gauge, not a steady demand"
    c.pinned[k] = [now - 400]
    assert c._steady(k, 300.0), "flat readings a full window after the cap was last touched are steady"
    print("consolidation: a raise waits for one steady window; a climbing demand never consolidates")

    # the replica cap as a lever, up to the operator's ceiling: at the cap (10 of 10), the line breached, the autoscaler's
    # own arithmetic asking for 18 (10 pods at 90% of a 50% target), the cap is raised to 18 (ceiling 30); calm and
    # steady again, the operator's 10 returns; the reset restores the range and leaves no record. Without a
    # ceiling the cap is never touched
    def capped(ceiling, shape=None, more=()):
        t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 600.0)
        S = json.loads(st.read_text()); hh = S["hpas"][0]
        hh["status"].update({"currentReplicas": 10, "desiredReplicas": 10}); hh["status"]["currentMetrics"][0]["resource"]["current"]["averageUtilization"] = 90
        if shape:
            shape(S)
        st.write_text(json.dumps(S))
        extra = ("--replica-ceiling", str(ceiling)) if ceiling is not None else ()
        c, _ = controller(t, lat, *extra, *more); c.step()
        return t, st, c
    cap = lambda st: json.loads(st.read_text())["hpas"][0]["spec"]["maxReplicas"]
    t, st, c = capped(0)
    assert cap(st) == 10, "the operator kept the cap (--replica-ceiling 0), yet it moved"

    # the ceiling read live (the default, the founder's rule of 13 October): what the machines can hold of this service's
    # pods, one pod under it; the control plane never counts; the cluster autoscaler's own room counts
    def web(alloc="4", workers=6, other_m=0, room=None):
        def shape(S):
            S["nodes"] = [{"metadata": {"name": f"n{i}"}, "status": {"allocatable": {"cpu": alloc}, "conditions": [{"type": "Ready", "status": "True"}]}}
                          for i in range(workers)]
            S["nodes"].append({"metadata": {"name": "cp", "labels": {"node-role.kubernetes.io/control-plane": ""}},
                               "spec": {"taints": [{"key": "node-role.kubernetes.io/control-plane", "effect": "NoSchedule"}]},
                               "status": {"allocatable": {"cpu": "64"}, "conditions": [{"type": "Ready", "status": "True"}]}})
            S["hpas"][0]["spec"]["scaleTargetRef"] = {"kind": "Deployment", "name": "web"}
            S["deployments"] = [{"metadata": {"name": "web", "namespace": "default"},
                                 "spec": {"selector": {"matchLabels": {"app": "web"}}, "template": {"spec": {"containers": [
                                     {"resources": {"requests": {"cpu": "200m"}}}]}}}}]
            S["pods"] = [{"metadata": {"namespace": "default", "labels": {"app": "web"}}, "status": {"phase": "Running"},
                          "spec": {"nodeName": f"n{i % workers}", "containers": [{"resources": {"requests": {"cpu": "200m"}}}]}} for i in range(10)]
            if other_m:
                S["pods"].append({"metadata": {"namespace": "kube-system", "labels": {"app": "other"}}, "status": {"phase": "Running"},
                                  "spec": {"nodeName": "n0", "containers": [{"resources": {"requests": {"cpu": f"{other_m}m"}}}]}})
            if room is not None:
                S["configmaps"] = [{"metadata": {"name": "cluster-autoscaler-status"}, "data": {"status":
                    "Cluster-wide:\n  Health: Healthy (ready=%d unready=0 registered=%d)\nNodeGroups:\n  Name: pool\n"
                    "  Health: Healthy (ready=%d unready=0 registered=%d longUnregistered=0 cloudProviderTarget=%d (minSize=1, maxSize=%d))\n"
                    % (workers, workers, workers, workers, workers, workers + room)}}]
        return shape
    # a pool Omni resizes with the operator's own command and no autoscaler reporting: no top until the pool refuses a count
    t, st, c = capped(None, web())                                   # 24 cores, nothing else asks: the 18 asked for
    hpa = lambda: json.loads(st.read_text())["hpas"][0]
    assert cap(st) == 18, f"read live, no top: cap {cap(st)}, expected the 18 the autoscaler's arithmetic asks for"
    assert c._live_ceiling(hpa()) > 10 ** 12 and c._max_nodes({"pool": 6, "nodes": 7}) == UNBOUNDED, "no top but what the pool refuses"
    c.refused_at = 7                                                 # the pool refused a seventh machine: its top is six
    assert c._live_ceiling(hpa()) == 24000 // 200 - 1 and c._max_nodes({"pool": 6, "nodes": 7}) == 6
    c.a.node_scale_cmd = "python3 -c 'import sys; sys.exit(1)'"      # a refusal, read live from the command itself
    c.refused_at = None
    assert c._pool_command(9, 6, "test") is False and c.refused_at == 9 and c._max_nodes({"pool": 6, "nodes": 7}) == 8
    assert any("refused" in json.loads(l) for l in (Path(t) / "audit.jsonl").read_text().splitlines())
    t, st, c = capped(None, web(alloc="2", workers=2, other_m=1000), ("--max-nodes", "2"))   # the operator's pool of two:
    assert cap(st) == 14, f"read live, room for 15: cap {cap(st)}, expected 14 (one pod under what the machines hold)"  # 15 pods, 14
    # kind: every node a container on one machine, each reporting the whole host's CPU (4): the machine's 4 cores once,
    # less 1 asked by others, 15 pods, one under: 14, whatever the node count or the room the pool may still show
    def kind_nodes(S):
        web(alloc="4", workers=6, other_m=1000)(S)
        for n in S["nodes"]:
            n.setdefault("spec", {})["providerID"] = f"kind://docker/omni-bench/{n['metadata']['name']}"
    t, st, c = capped(None, kind_nodes)
    # A measured idle host leaves the request-based ceiling in force; no host sample holds at the current 10 replicas.
    c.host_cpu.busy_share = 0.0
    c.host_cpu.sample = lambda: 0.0
    c.step()
    assert c._live_ceiling(json.loads(st.read_text())["hpas"][0]) == (4000 - 1000) // 200 - 1 and cap(st) == 14, cap(st)
    t, st, c = capped(None, web(alloc="2", workers=2, other_m=1000, room=2))   # the autoscaler may add 2 more: 35, one under: 34
    assert cap(st) == 18, f"read live with the autoscaler's room: cap {cap(st)}, expected the 18 asked for"
    assert c._live_ceiling(json.loads(st.read_text())["hpas"][0]) == (8000 - 1000) // 200 - 1
    assert c._max_nodes({"pool": 2, "nodes": 3}) == 4, "the machine lever's top: 2 ready workers and 2 the autoscaler may add"
    print("replica room read live: no top until the pool refuses one (then 119), 14 of 15 (one pod under), kind's one host "
          "counted once, the autoscaler's room counted, the control plane never")
    t, st, c = capped(30)
    S = json.loads(st.read_text())
    assert cap(st) == 18, f"at the cap and breached: cap {cap(st)}, expected the 18 the autoscaler's arithmetic asks for"
    raised = cap(st)
    assert raised <= 30 and S["hpas"][0]["metadata"]["annotations"].get("omnicompass.io/original-replica-range") == "1,10"
    lat = probe(t, 50.0); S = json.loads(st.read_text()); hh = S["hpas"][0]
    hh["status"].update({"currentReplicas": 4, "desiredReplicas": 4}); hh["status"]["currentMetrics"][0]["resource"]["current"]["averageUtilization"] = 40
    st.write_text(json.dumps(S))
    for _ in range(4):
        c.step()
    k = ("default", "web"); now = time.time(); c.demand[k] = [(now - 280.0 + 56 * i, 1.6) for i in range(5)]   # a steady window
    c.pinned[k] = [tt - 400.0 for tt in c.pinned.get(k, [])]                                                  # the cap last touched before it
    for _ in range(4):
        c.step()
        if cap(st) == 10:
            break
    assert cap(st) == 10, f"calm and steady: cap {cap(st)}, expected the operator's 10 back"
    t, st, c = capped(30); (Path(t) / "kill").write_text("1"); c.step()
    S = json.loads(st.read_text())
    assert cap(st) == 10 and "omnicompass.io/original-replica-range" not in S["hpas"][0]["metadata"].get("annotations", {})
    print(f"replica room: at the cap and breached, 10 -> {raised} (ceiling 30); calm and steady, back to 10; kill restores 10; ceiling 0, never moved")

    # two services on the same machines, the probe measuring one (--sensed default/web): a breach moves only the HPA
    # of the service the probe measures; the neighbour's HPA stays at the operator's own target
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 600.0)
    S = json.loads(st.read_text()); S["hpas"][0]["spec"]["scaleTargetRef"] = {"kind": "Deployment", "name": "web"}
    nb = json.loads(json.dumps(S["hpas"][0])); nb["metadata"]["name"] = "noisy"; nb["spec"]["scaleTargetRef"]["name"] = "noisy"
    S["hpas"].append(nb); st.write_text(json.dumps(S))
    c, marker = controller(t, lat, "--sensed", "default/web")
    for _ in range(3):
        c.step()
    H = {h["metadata"]["name"]: h["spec"]["metrics"][0]["resource"]["target"]["averageUtilization"] for h in json.loads(st.read_text())["hpas"]}
    assert H == {"web": 30, "noisy": 50}, f"two services: targets {H}, expected web 30 (sensed), noisy 50 (the operator's)"
    print(f"two services: the sensed one failed up to {H['web']}, the neighbour stayed at the operator's {H['noisy']}")

    # blind: a probe file older than twice its window reads as past the wall: fail up, but more pods cannot answer a
    # blind sense, so the HPA target stays the operator's own (as on the card, fail up is native's own settings)
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 50.0)
    old = time.time() - 600; os.utime(lat, (old, old))
    c, marker = controller(t, lat)
    c.step()
    assert target_now(st) == 50, f"blind: target {target_now(st)}, expected the operator's own 50"
    assert decisions(t)[-1]["compass_law"]["position"] >= 0.95, "blind did not read as past the wall"
    print(f"blind: past the wall, target stays the operator's {target_now(st)} (more pods cannot answer a blind sense)")

    # restore: the reset hands the target back and removes the record (after a real breach moved it)
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 600.0)
    c, marker = controller(t, lat); c.step()
    assert target_now(st) == 30
    (Path(t) / "kill").write_text("1")
    c.step()
    S = json.loads(st.read_text())
    assert target_now(st) == 50 and ANNOTATION not in S["hpas"][0]["metadata"].get("annotations", {})
    print("reset: target back to 50, no record left")

    # cruise (amendment 12): a queue of other work waits for a place two decisions running, and the service's responses
    # are slow only because the machines are busy with it. Omni holds every machine and leaves the service's target at the
    # operator's own: no extra pods for a service nobody is loading
    t = tempfile.mkdtemp(); st = cluster(t); lat = probe(t, 600.0)
    S = json.loads(st.read_text())
    S["pods"] += [{"status": {"phase": "Pending"}, "spec": {"containers": [{"resources": {"requests": {"cpu": "500m"}}}]}}
                  for _ in range(20)]
    st.write_text(json.dumps(S))
    c, marker = controller(t, lat)
    c.step(); c.step()
    assert c.cruise, "cruise did not engage with work waiting two decisions running"
    assert target_now(st) == 50, f"cruise: target {target_now(st)}, expected the operator's own 50"
    print("cruise: every machine held, the service's target left at the operator's 50 (no pods for an unloaded service)")
    # and the five-second floor step stays still: every machine is in, so it reads nothing from the API server (the cost a
    # draining queue felt was these reads: all pods, nodes, metrics and HPAs every five seconds on a saturated machine)
    reads = []
    get0 = c.k.get
    c.k.get = lambda *a: (reads.append(a), get0(*a))[1]
    before = (Path(t) / "audit.jsonl").read_text()
    for _ in range(3):
        assert c.floor_step() is None, "the floor step acted during cruise"
    c.k.get = get0
    assert not reads and (Path(t) / "audit.jsonl").read_text() == before, f"the floor step read the cluster during cruise: {reads[:3]}"
    print("cruise: the floor step makes no API read and no write while the queue drains")
    print("PASS compass law in the live controller")


if __name__ == "__main__":
    main()
