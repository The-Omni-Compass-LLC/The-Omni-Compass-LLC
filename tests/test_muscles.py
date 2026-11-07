# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Live muscles against the standin kubectl and standin hardware commands: at the max (the default dial) the power cap is never
set under native (each capped pod gets its machine's idle CPU, one click under the machine; the frequency ceiling and the
GPU limit stay at their top, nothing written); on the tune-down the power cap scales the CPU limit, never under the pod's
own request nor its use plus headroom (nothing fixed), and the reset restores it; a security hold blocks any expansion;
rollouts pause when change is not permitted, resume when it is, and a stuck rollout is undone when rollback is
authorised; batch admits one held job only with headroom and never during a hold; the CPU-frequency and GPU power-limit
connectors follow the cap (never under the card's own minimum, read live) and are restored by the reset; the heat sense
follows the harness law and GPU temperature (one degree under the card's own slowdown temperature when it reports it);
observe mode writes nothing."""
import json, os, sys, tempfile
from pathlib import Path
from types import SimpleNamespace
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.controller import Controller, Kube, parser
from omni_controller.muscles import Muscles, CPU_ANN
STANDIN = str(ROOT / "tests" / "standin_cluster" / "kubectl")


def state(tmp, hold="false"):
    dep = lambda name: {"metadata": {"name": name, "namespace": "default", "annotations": {}},
                        "spec": {"selector": {"matchLabels": {"app": name}},
                                 "template": {"spec": {"containers": [{"resources": {"limits": {"cpu": "500m"}, "requests": {"cpu": "200m"}}}]}}},
                        "status": {"conditions": [{"type": "Progressing", "reason": "NewReplicaSetAvailable"}]}}
    job = lambda n, t: {"metadata": {"name": n, "namespace": "batch", "creationTimestamp": t}, "spec": {"suspend": True}}
    ready = [{"type": "Ready", "status": "True"}]
    st = {"nodes": [{"metadata": {"name": f"w{i}"}, "spec": {}, "status": {"allocatable": {"cpu": "4"}, "conditions": ready}} for i in range(3)],
          "pods": [{"metadata": {"name": f"web-{i}", "labels": {"app": "web"}}, "status": {"phase": "Running"},
                    "spec": {"nodeName": "w0", "containers": [{"resources": {"limits": {"cpu": "500m"}, "requests": {"cpu": "200m"}}}]}}
                   for i in range(2)], "hpas": [{"metadata": {"name": "web", "namespace": "default"}, "spec": {"metrics": [{"type": "Resource", "resource": {
              "name": "cpu", "target": {"type": "Utilization", "averageUtilization": 50}}}]}, "status": {"currentReplicas": 2}}],
          "used_per_node": "400m", "deployments": [dep("web"), dep("api")],
          "configmaps": [{"metadata": {"name": "omni-security"}, "data": {"hold": hold}}],
          "jobs": [job("j2", "2026-01-02"), job("j1", "2026-01-01")]}
    p = Path(tmp) / "state.json"; p.write_text(json.dumps(st))
    os.environ["STANDIN_KUBE_STATE"] = str(p); os.environ["STANDIN_KUBE_LOG"] = str(Path(tmp) / "writes.log")
    return p


def load(p): return json.loads(Path(p).read_text())
def cpu(p, name="web"):
    lims = {q["spec"]["containers"][0]["resources"]["limits"]["cpu"] for q in load(p)["pods"] if q["metadata"]["labels"]["app"] == name}
    tmpl = next(d for d in load(p)["deployments"] if d["metadata"]["name"] == name)["spec"]["template"]["spec"]["containers"][0]["resources"]["limits"]["cpu"]
    assert tmpl == "500m", "the deployment template must not change (no rollout)"
    assert len(lims) == 1, lims
    return lims.pop()


def args(tmp, **kw):
    a = parser().parse_args(["--kubectl", STANDIN, "--audit", str(Path(tmp) / "audit.jsonl"), "--kill-file", str(Path(tmp) / "kill"),
                             "--cap-deployments", "default/web", "--rollout-guard", "default/api", "--batch",
                             "--security-configmap", "default/omni-security", "--thermal-model"])
    for k, v in kw.items(): setattr(a, k, v)
    return a


def main():
    # the max (the default dial): a power cap under 1 from the governor sets nothing under native; each capped pod gets
    # its machine's idle CPU instead (w0: 4 CPU, two serving pods, 0.95 x 4000 / 2 = 1900m), and the reset hands it back
    t = tempfile.mkdtemp(); p = state(t); a = args(t); rec = []
    assert a.dial == "max" and a.cap_min == 0.0
    m = Muscles(Kube(STANDIN, audit=rec.append), a, rec.append)
    obs = {"load_ratio": 0.3, "power_stress": 0.5, "security_block": 0.0}
    m.push({"power_cap": 0.8, "change_permitted": True, "rollback_authorized": False}, obs)
    assert cpu(p) == "1900m", cpu(p)
    m.push({"power_cap": 0.3, "change_permitted": True, "rollback_authorized": False}, obs)
    assert cpu(p) == "1900m", "the max never sets the limit under native, whatever cap the governor proposes"
    m.restore(); assert cpu(p) == "500m"
    hw0 = Path(t) / "hw0.log"
    a0 = args(t, cpufreq_cmd=f"sh -c 'echo cpu {{khz}} >> {hw0}'", cpu_max_khz=3000000.0,
              gpu_power_cmd=f"sh -c 'echo gpu {{w}} >> {hw0}'", gpu_max_w=300.0, cap_deployments="", rollout_guard="", batch=False)
    m0 = Muscles(Kube(STANDIN, audit=lambda r: r), a0, lambda r: r)
    m0.push({"power_cap": 0.8, "change_permitted": True, "rollback_authorized": False}, obs); m0.restore()
    assert not hw0.exists(), "at the max the frequency ceiling and the GPU limit stay at their top: nothing written"

    # the tune-down (--dial save)
    t = tempfile.mkdtemp(); p = state(t); a = args(t, dial="save"); rec = []
    m = Muscles(Kube(STANDIN, audit=rec.append), a, rec.append)
    m.push({"power_cap": 0.8, "change_permitted": True, "rollback_authorized": False}, obs)
    assert cpu(p) == "400m", cpu(p)
    assert next(d for d in load(p)["deployments"] if d["metadata"]["name"] == "web")["metadata"]["annotations"][CPU_ANN] == "500m"
    assert [j["spec"]["suspend"] for j in load(p)["jobs"]] == [True, False], "oldest held job admitted first, one per decision"
    m.push({"power_cap": 0.8, "change_permitted": False, "rollback_authorized": False}, obs)
    api = lambda: next(d for d in load(p)["deployments"] if d["metadata"]["name"] == "api")
    assert api()["spec"]["paused"] is True
    m.push({"power_cap": 0.8, "change_permitted": True, "rollback_authorized": False}, obs)
    assert api()["spec"]["paused"] is False
    s = load(p); next(d for d in s["deployments"] if d["metadata"]["name"] == "api")["status"]["conditions"] = [
        {"type": "Progressing", "reason": "ProgressDeadlineExceeded"}]; Path(p).write_text(json.dumps(s))
    m.push({"power_cap": 0.8, "change_permitted": True, "rollback_authorized": True}, obs)
    assert any(r.get("why", "").startswith("rollout: undo") for r in rec)
    s = load(p); s["jobs"][0]["spec"]["suspend"] = True; Path(p).write_text(json.dumps(s))
    before = [j["spec"]["suspend"] for j in load(p)["jobs"]]
    hold = dict(obs, security_block=1.0)
    m.push({"power_cap": 1.0, "change_permitted": True, "rollback_authorized": False}, hold)
    assert cpu(p) == "400m", "no expansion of the power cap during a security hold"
    assert [j["spec"]["suspend"] for j in load(p)["jobs"]] == before, "no batch admission during a hold"
    m.push({"power_cap": 0.3, "change_permitted": True, "rollback_authorized": False}, obs)
    assert cpu(p) == "200m", "nothing fixed: the pod's own request (200m) is the floor"
    m.restore()
    assert cpu(p) == "500m" and CPU_ANN not in next(d for d in load(p)["deployments"] if d["metadata"]["name"] == "web")["metadata"]["annotations"]

    hw = Path(t) / "hw.log"
    a2 = args(t, cpufreq_cmd=f"sh -c 'echo cpu {{khz}} >> {hw}'", cpu_max_khz=3000000.0,
              gpu_power_cmd=f"sh -c 'echo gpu {{w}} >> {hw}'", gpu_max_w=300.0, gpu_query_cmd="echo 250,79",
              rapl_cmd="echo 120.5", cap_deployments="", rollout_guard="", batch=False, dial="save")
    m2 = Muscles(Kube(STANDIN, audit=lambda r: r), a2, lambda r: r)
    o = m2.sense(0.5)
    assert o["cpu_watts"] == 120.5 and o["gpu_watts"] == 250 and abs(o["thermal"] - 79 / 83) < 1e-9, o
    m2.push({"power_cap": 0.8, "change_permitted": True, "rollback_authorized": False}, obs)
    m2.restore()
    assert hw.read_text().split("\n")[:4] == ["cpu 2400000", "gpu 240", "cpu 3000000", "gpu 300"], hw.read_text()
    # the card's own figures, read live: its minimum limit floors the push (100 W, not 300 x 0.3 = 90 W), and one degree
    # under its own slowdown temperature (90 C) is heat 1.0
    hw2 = Path(t) / "hw2.log"
    a3 = args(t, gpu_power_cmd=f"sh -c 'echo gpu {{w}} >> {hw2}'", gpu_max_w=300.0, gpu_query_cmd="echo 250,79,100,90",
              cap_deployments="", rollout_guard="", batch=False, dial="save", thermal_model=False)
    m3 = Muscles(Kube(STANDIN, audit=lambda r: r), a3, lambda r: r)
    o3 = m3.sense(0.5)
    assert abs(o3["thermal"] - 79 / 89) < 1e-9 and m3.gpu_min_w == 100.0, o3
    m3.push({"power_cap": 0.3, "change_permitted": True, "rollback_authorized": False}, obs)
    assert hw2.read_text().split("\n")[0] == "gpu 100", hw2.read_text()
    th = Muscles(None, SimpleNamespace(thermal_model=True), None)
    x = th.sense(1.0)["thermal"]; assert abs(x - (0.86 * 0.32 + 0.14 * (0.34 + 0.62))) < 1e-12

    # reflex: the cap never goes below pod usage x 1.3 (usage 300m -> at least 390m, base 500m)
    s = load(p); s["pod_usage"] = "300m"; Path(p).write_text(json.dumps(s))
    m.push({"power_cap": 0.3, "change_permitted": True, "rollback_authorized": False}, obs)
    assert cpu(p) == "390m", cpu(p)
    m.restore(); assert cpu(p) == "500m"
    # latency afferent: p95 over the SLO becomes queue pressure
    from omni_controller.muscles import latency_p95
    lf = Path(t) / "lat.csv"; lf.write_text("elapsed_seconds,latency_ms,ok\n" + "".join(f"{i},{100 + i},1\n" for i in range(100)))
    assert latency_p95(str(lf), 60) == 196.0, latency_p95(str(lf), 60)
    a5 = args(t, latency_file=str(lf), slo_ms=100.0, latency_window_s=60.0, thermal_model=False, security_configmap="")
    o5 = Muscles(Kube(STANDIN, audit=lambda r: r), a5, lambda r: r).sense(0.5)
    assert abs(o5["latency_pressure"] - 0.96) < 1e-9, o5
    t3 = tempfile.mkdtemp(); p3 = state(t3)
    c = Controller(args(t3, mode="observe", interval=0))
    for _ in range(3): c.step()
    assert not (Path(t3) / "writes.log").exists(), "observe mode wrote"
    t4 = tempfile.mkdtemp(); p4 = state(t4, hold="true")
    c = Controller(args(t4, mode="target", interval=0))
    for _ in range(3): c.step()
    dec = [json.loads(l)["decision"] for l in (Path(t4) / "audit.jsonl").read_text().splitlines() if '"decision"' in l]
    assert all(d["security_block"] == 1.0 for d in dec) and all(0 <= d["thermal"] <= 1.35 for d in dec)
    assert [j["spec"]["suspend"] for j in load(p4)["jobs"]] == [True, True], "no batch admission during a live security hold"
    # SLO reflex through the controller: p95 over the SLO -> not slo_clean -> no tighter HPA target, never a CPU limit
    # below the operator's
    t5 = tempfile.mkdtemp(); p5 = state(t5)
    lf5 = Path(t5) / "lat.csv"; lf5.write_text("elapsed_seconds,latency_ms,ok\n" + "".join(f"{i},900,1\n" for i in range(60)))
    c = Controller(args(t5, mode="target", interval=0, latency_file=str(lf5), slo_ms=500.0, latency_window_s=60.0))
    for _ in range(3): c.step()
    dec = [json.loads(l)["decision"] for l in (Path(t5) / "audit.jsonl").read_text().splitlines() if '"decision"' in l]
    assert all(d["slo_clean"] is False for d in dec), dec
    assert next(h for h in load(p5)["hpas"])["spec"]["metrics"][0]["resource"]["target"]["averageUtilization"] <= 50, "densified during SLO breach"
    assert float(cpu(p5)[:-1]) >= 500, "capped during SLO breach"   # never below the operator's limit; idle CPU conveyed
    print("muscles: power cap, heat, security, rollout, batch, CPU frequency and GPU connectors; kill restores; observe writes nothing")
    print("PASS test_muscles")


if __name__ == "__main__":
    main()
