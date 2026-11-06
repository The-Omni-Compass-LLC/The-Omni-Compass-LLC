#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A batch queue's waiting pods replayed through the governor's own decision: the model of omni-v25's flipping target (class S).

On the batch rigs the cluster's waiting pods are a batch queue's, on and off, as its normal queueing. On omni-v25 the web
service's autoscaler target flipped between the cover's floor and native's with them (docs/LOSS_CAUSES_2026-11-06.md). This model
replays the native arm's own timelines of the KAI scheduler's four ways (results/model_gate/BATCH_FLIP_INPUTS.json: the cluster's
waiting pods from capture.csv and the web service's 95th percentile in 10 s windows from latency.csv, 30 repetitions of runs
41809041712, 41810759693 and 41812560443), open loop, through a checkout's own governor at the factory beat on site (a decision
every 10 s, a fast check every 5 s, on the replay's own clock), and reads what it writes to the web service's target:

  target_writes     every write of the target
  flips             writes that change the target after the first
  below_native_s    seconds the target stood below native's while another workload's pods waited (room held from them)
  holds             holds of native's target started (the immune hand-back's, from the fast check or the decision)

Open loop: the governor's writes move neither the replayed pods nor the response times, so the model reads the decision rule and
nothing else. The service's and the queue's own gauges are read only by the benchmarks' runs.

  python3 tools/batch_flip_model.py --base CHECKOUT --cand CHECKOUT [--json OUT.json] [--md OUT.md]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "results" / "model_gate" / "BATCH_FLIP_INPUTS.json"
GAUGES = {"target_writes": ("lower", True), "flips": ("lower", False), "below_native_s": ("lower", False),
          "holds": ("lower", True)}
BEAT_S, CHECK_S, NATIVE_TARGET, WEB_PODS, BATCH_RUNNING = 10.0, 5.0, 50, 3, 4


def worker(index, out_dir):
    """One repetition's native timeline through the governor of the checkout on PYTHONPATH; prints the reading as JSON."""
    import subprocess as sp
    from unittest import mock
    import omni_controller.controller as cmod
    from omni_controller.controller import Controller, parser

    data = json.loads(INPUTS.read_text())
    rep, slo = data["reps"][index], float(data["slo_ms"])
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "audit.jsonl").unlink(missing_ok=True)
    t0 = 1_800_000_000.0
    clock = [t0]
    st = {"target": NATIVE_TARGET, "hpa_ann": {}, "dep_ann": {}, "pending": 0}
    writes = []

    def pod(name, app, phase):
        return {"metadata": {"name": name, "namespace": "default", "labels": {"app": app}},
                "spec": {"nodeName": None if phase == "Pending" else "w0",
                         "containers": [{"resources": {"requests": {"cpu": "200m"}, "limits": {"cpu": "500m"}}}]},
                "status": {"phase": phase}}

    def pods():
        return ([pod(f"web-{i}", "web", "Running") for i in range(WEB_PODS)]
                + [pod(f"batch-run-{i}", "batch", "Running") for i in range(BATCH_RUNNING)]
                + [pod(f"batch-wait-{i}", "batch", "Pending") for i in range(st["pending"])])

    class Kube:
        audit = None

        def get(self, *args):
            if args[:2] == ("get", "nodes"):
                return {"items": [{"metadata": {"name": f"w{i}", "labels": {}}, "spec": {"providerID": f"kind://docker/kind/w{i}"},
                                   "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}
                                  for i in range(6)]}
            if args[:2] == ("get", "pods"):
                items = pods()
                if "-l" in args:
                    k, v = args[args.index("-l") + 1].split("=", 1)
                    items = [p for p in items if p["metadata"]["labels"].get(k) == v]
                for x in args:
                    if x.startswith("--field-selector=status.phase="):
                        items = [p for p in items if p["status"]["phase"] == x.split("=", 2)[2]]
                if "-o" in args and args[args.index("-o") + 1] == "name":
                    return "\n".join(f"pod/{p['metadata']['name']}" for p in items)
                return {"items": items}
            if args[:2] == ("top", "nodes"):
                return "\n".join(f"w{i} 1500m 37% 1Gi 5%" for i in range(6))
            if args[:2] == ("top", "pods"):
                return "\n".join(f"web-{i} 80m 50Mi" for i in range(WEB_PODS))
            if args[:2] == ("get", "hpa"):
                cpu = {"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": st["target"]}}}
                cur = [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": 40}}}]
                return {"items": [{"metadata": {"name": "web", "namespace": "default", "annotations": dict(st["hpa_ann"])},
                                   "spec": {"minReplicas": 1, "maxReplicas": 10, "metrics": [cpu],
                                            "scaleTargetRef": {"kind": "Deployment", "name": "web"}},
                                   "status": {"currentReplicas": WEB_PODS, "desiredReplicas": WEB_PODS, "currentMetrics": cur}}]}
            if args[:2] == ("get", "deployment"):
                return {"metadata": {"name": "web", "namespace": "default", "annotations": dict(st["dep_ann"])},
                        "spec": {"replicas": WEB_PODS, "selector": {"matchLabels": {"app": "web"}},
                                 "template": {"spec": {"containers": [{"name": "web", "resources": {
                                     "requests": {"cpu": "200m"}, "limits": {"cpu": "500m"}}}]}}},
                        "status": {"replicas": WEB_PODS, "readyReplicas": WEB_PODS}}
            raise sp.CalledProcessError(1, ["kubectl", *args], stderr="not in the replay")

        def write(self, args, why):
            writes.append((clock[0] - t0, list(args), why))
            if args[:2] == ["patch", "hpa"] and "--type=json" in args:
                st["target"] = int(json.loads(args[args.index("-p") + 1])[0]["value"])
            elif args[:2] == ["annotate", "hpa"]:
                k, _, v = args[-1].partition("=")
                st["hpa_ann"].pop(k[:-1], None) if args[-1].endswith("-") else st["hpa_ann"].__setitem__(k, v)
            elif args[:2] == ["annotate", "deployment"]:
                k, _, v = args[-1].partition("=")
                st["dep_ann"].pop(k[:-1], None) if args[-1].endswith("-") else st["dep_ann"].__setitem__(k, v)

    lat = out / "latency.csv"

    def probe(p95_ms):
        lat.write_text("elapsed_seconds,latency_ms,ok\n" + "".join(f"{i * 0.5:.1f},{p95_ms},1\n" for i in range(20)))
        os.utime(lat, (clock[0], clock[0]))

    a = parser().parse_args(["--mode", "nodepool", "--law", "compass", "--dial", "max", "--interval", str(BEAT_S),
                             "--floor-interval", str(CHECK_S), "--latency-file", str(lat), "--slo-ms", str(slo),
                             "--latency-window-s", "30", "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "kill"),
                             "--node-scale-cmd", "SIMSCALE {n}", "--min-nodes", "2", "--max-nodes", "6", "--max-node-step", "1"])
    real_run = sp.run

    def standin_run(cmd, *kw_a, **kw):
        if isinstance(cmd, list) and cmd and cmd[0] == "SIMSCALE":
            return sp.CompletedProcess(cmd, 0)
        return real_run(cmd, *kw_a, **kw)

    pend = rep["pending"]
    p95 = dict((int(t), ms) for t, ms in rep["p95_10s"])
    end = max(max(t for t, _ in pend), max(p95) + 10)
    below = 0.0
    fails = 0
    with mock.patch.object(cmod.time, "time", lambda: clock[0]), \
            mock.patch("omni_controller.controller.subprocess.run", side_effect=standin_run):
        ctl = Controller(a, kube=Kube())
        t = 0.0
        while t <= end:
            clock[0] = t0 + t
            st["pending"] = next((n for tt, n in reversed(pend) if tt <= t), 0)
            probe(p95.get(int(t // 10) * 10, 0.0) or 1.0)
            if t % BEAT_S == 0:
                fails = cmod.safe_step(ctl, fails)
            else:
                try:
                    ctl.floor_step()
                except Exception as error:
                    ctl.audit({"error": "floor check: " + repr(error)[:300]})
            if st["target"] < NATIVE_TARGET and st["pending"] > 0:
                below += CHECK_S
            t += CHECK_S
    values = [json.loads(w[1][w[1].index("-p") + 1])[0]["value"] for w in writes
              if w[1][:2] == ["patch", "hpa"] and "--type=json" in w[1]]
    audit = [json.loads(line) for line in (out / "audit.jsonl").read_text().splitlines() if line.strip()]
    holds = sum(1 for r in audit if isinstance(r.get("immune"), dict) and "hold_s" in r["immune"])
    print(json.dumps({"target_writes": len(values), "flips": sum(1 for x, y in zip(values, values[1:]) if x != y),
                      "below_native_s": below, "holds": holds, "errors": sum(1 for r in audit if "error" in r),
                      "values": values[:40], "engine_tree": str(Path(cmod.__file__).resolve().parents[1])}))


def run_one(tree, index, out_dir):
    env = {**os.environ, "PYTHONPATH": str(tree)}
    p = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--worker", str(index), "--dir", str(out_dir)],
                       cwd=tree, env=env, capture_output=True, text=True, timeout=1800)
    if p.returncode != 0:
        raise RuntimeError(f"{tree} {index}: {p.stderr[-2000:]}")
    r = json.loads(p.stdout.strip().splitlines()[-1])
    if Path(r.pop("engine_tree")).resolve() != Path(tree).resolve():
        raise RuntimeError(f"the engine was not imported from {tree}")
    return r


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base")
    ap.add_argument("--cand")
    ap.add_argument("--json", default="")
    ap.add_argument("--md", default="")
    ap.add_argument("--worker", type=int, help=argparse.SUPPRESS)
    ap.add_argument("--dir", help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    if a.worker is not None:
        return worker(a.worker, a.dir)
    sys.path.insert(0, str(ROOT))
    from tools.model_gate import reading
    n = len(json.loads(INPUTS.read_text())["reps"])
    work = Path(tempfile.mkdtemp(prefix="batch_flip_"))
    res = {"base": [], "cand": []}
    for i in range(n):
        for arm, tree in (("base", a.base), ("cand", a.cand)):
            res[arm].append(run_one(Path(tree).resolve(), i, work / f"{arm}-{i}"))
    rows = {}
    for g in GAUGES:
        b = [r[g] for r in res["base"]]; c = [r[g] for r in res["cand"]]
        rows[g] = {"base_mean": sum(b) / n, "cand_mean": sum(c) / n,
                   **reading(g, [y - x for x, y in zip(b, c)], b, GAUGES)}
    report = {"inputs": str(INPUTS.relative_to(ROOT)), "repetitions": n, "rows": rows,
              "errors": {arm: sum(r["errors"] for r in res[arm]) for arm in res},
              "example": {arm: res[arm][0]["values"] for arm in res}}
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=1) + "\n")
    if a.md:
        Path(a.md).write_text(render(report))
    print(json.dumps(report, indent=1))
    return 0


LABELS = {"target_writes": "writes of the web service's target", "flips": "changes of the target after the first",
          "below_native_s": "seconds below native's target while another workload's pods waited",
          "holds": "holds of native's target started"}
UNITS = {"target_writes": "writes", "flips": "changes", "below_native_s": "s", "holds": "holds"}


def render(report):
    """The record of one replay, every gauge read by the key (tools/model_gate.reading: the paired change over the repetitions)."""
    sys.path.insert(0, str(ROOT))
    from tools.legal import stamp
    from tools.readings import by_word, interval_by_word
    lines = ["# The batch queue's waiting pods through the governor's decision: omni-v26 against omni-v25 (our own model, class S)",
             "", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "",
             "`tools/batch_flip_model.py` replays, open loop, the native arm's own timelines of the KAI scheduler's four ways on the "
             "organism alone (`" + report["inputs"] + "`: the cluster's waiting pods from each repetition's capture and the web "
             "service's 95th percentile in 10 s windows, %d repetitions of runs 41809041712, 41810759693 and 41812560443) through "
             "each engine's own governor, a decision every 10 s and a fast check every 5 s on the replay's own clock. The governor's "
             "writes move neither the replayed pods nor the response times, so the model reads the decision rule alone. The service's "
             "and the queue's own gauges are read only by the benchmarks' runs (`docs/LOSS_CAUSES_2026-11-06.md`)." % report["repetitions"],
             "", "| Gauge | omni-v25, mean a repetition | omni-v26, mean a repetition | Reading | 95% interval of the paired change |",
             "|---|---|---|---|---|"]
    for g, v in report["rows"].items():
        lo, hi = v["ci95"]
        way = "down" if v["relative"] < 0 else "up"
        lines.append(f"| {LABELS[g]} | {v['base_mean']:.2f} | {v['cand_mean']:.2f} | {v['word']}, {way} "
                     f"{by_word(v['relative'] * 100.0, v['word'])}{'' if v['beyond_noise'] else ', inside the noise'} "
                     f"| {interval_by_word(lo, hi, v['word'], unit=' ' + UNITS[g], digits=2)} |")
    lines += ["", "Errors in the governor's audit: omni-v25 %d, omni-v26 %d." % (report["errors"]["base"], report["errors"]["cand"]),
              "", "A hold is the fix itself: native's target kept for ten minutes, doubled for each hold in a row, while another "
              "workload's pods wait for the room; its count rising is the mechanism working, power given by the key.", ""]
    return "\n".join(stamp(lines)) + "\n"


if __name__ == "__main__":
    sys.exit(main())
