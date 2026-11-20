# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Koordinator's best-effort queue replayed through the conveyance: the model of omni-v25's conveyed batch processor (class S).

On Koordinator's rigs the conveyance raised the web pods' processor limits into the processor Koordinator reclaims for its
best-effort jobs, and on the shared host its raise and its hand-back cycled (docs/LOSS_CAUSES_2026-11-07.md). This model replays
the native arm's own timelines of both Koordinator batch-stream tables (results/model_gate/KOORD_CONVEY_INPUTS.json: the host's
busy share from host_cpu.csv, each best-effort pod's machine and its times made, placed and done from pods.json, and the web
service's replicas from capture.csv; 60 repetitions of six runs; Koordinator's agent on every machine as the rig's pinned chart
installs it), open loop, through a checkout's own conveyance
(Muscles.convey) every 15 s, as the governor's fast check calls it, and reads what it writes to the web pods' limits:

  writes                 every limit written
  hand_backs             writes that lowered a limit
  turns                  a limit raised again after it was lowered (the cycle)
  held_while_waiting     processor-seconds of limit above the operator's while a best-effort pod waited for a place
  given                  processor-seconds of limit above the operator's in all
  largest_raise_m        the largest single raise of one pod's limit

Open loop: the conveyance's writes move neither the host's busy share nor the queue, so the model reads the rule alone. The
web service's and the queue's own gauges are read only by the benchmarks' runs.

  python3 tools/convey_owed_model.py --base CHECKOUT --cand CHECKOUT [--json OUT.json] [--md OUT.md]
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
INPUTS = ROOT / "results" / "model_gate" / "KOORD_CONVEY_INPUTS.json"
GAUGES = {"writes": ("lower", True), "hand_backs": ("lower", True), "turns": ("lower", False),
          "held_while_waiting": ("lower", False), "given": ("lower", True), "largest_raise_m": ("lower", True)}
CHECK_S, OPERATOR_M = 15.0, 500
WORKERS = ["omni-bench-worker"] + [f"omni-bench-worker{i}" for i in range(2, 7)]


def worker(index, out_dir):
    """One repetition's native timeline through the conveyance of the checkout on PYTHONPATH; prints the reading as JSON."""
    import bisect
    from types import SimpleNamespace
    import omni_controller.muscles as mmod
    from omni_controller.muscles import Muscles

    rep = json.loads(INPUTS.read_text())["reps"][index]
    busy_t = [b[0] for b in rep["busy"]]
    t = [0.0]
    limits, ann = {}, {}

    def busy_now():
        i = bisect.bisect_right(busy_t, t[0]) - 1
        return rep["busy"][max(0, i)][1]

    def replicas_now():
        n = 1
        for e, r in rep["web"]:
            if e > t[0]:
                break
            n = max(1, r)
        return n

    def pods_now():
        items = []
        for k in range(replicas_now()):
            name = f"php-apache-{k}"
            limits.setdefault(name, OPERATOR_M)
            items.append({"metadata": {"name": name, "namespace": "default", "labels": {"run": "php-apache"}},
                          "spec": {"nodeName": WORKERS[k % len(WORKERS)], "containers": [{"name": "php", "resources": {
                              "requests": {"cpu": "200m"}, "limits": {"cpu": f"{limits[name]}m"}}}]},
                          "status": {"phase": "Running", "conditions": [{"type": "Ready", "status": "True"}]}})
        # Koordinator's agent on every machine, as the pinned chart (koordinator-1.8.0.tgz, sha256 766011e7...) installs it: no CPU
        # requested, a 200m limit, so a pod with room of its own on every machine (the audit's "beside another workload's room")
        for n in WORKERS:
            items.append({"metadata": {"name": f"koordlet-{n}", "namespace": "koordinator-system", "labels": {"koord-app": "koordlet"},
                                       "ownerReferences": [{"kind": "DaemonSet", "name": "koordlet"}]},
                          "spec": {"nodeName": n, "containers": [{"name": "koordlet", "resources": {
                              "requests": {"cpu": "0"}, "limits": {"cpu": "200m"}}}]},
                          "status": {"phase": "Running"}})
        for j, (node, made, placed, done) in enumerate(rep["be"]):
            if made is None or made > t[0] or (done is not None and done <= t[0]):
                continue
            spec = {"containers": [{"name": "work", "resources": {
                "limits": {"kubernetes.io/batch-cpu": "1k", "kubernetes.io/batch-memory": "64Mi"},
                "requests": {"kubernetes.io/batch-cpu": "500", "kubernetes.io/batch-memory": "64Mi"}}}]}
            on = placed is not None and placed <= t[0]
            if on:
                spec["nodeName"] = node
            items.append({"metadata": {"name": f"omni-batch-{j}", "namespace": "default",
                                       "labels": {"app": "omni-batch-stream", "koordinator.sh/enable-colocation": "true"},
                                       "ownerReferences": [{"kind": "Job", "name": f"omni-batch-{j // 10:03d}"}]},
                          "spec": spec, "status": {"phase": "Running" if on else "Pending"}})
        return items

    writes = []

    class Kube:
        audit = None

        def get(self, *args):
            if args[:2] == ("get", "nodes"):
                return {"items": [{"metadata": {"name": n, "labels": {}}, "spec": {"providerID": f"kind://docker/omni-bench/{n}"},
                                   "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}
                                  for n in WORKERS]}
            if args[:2] == ("get", "pods"):
                return {"items": pods_now()}
            if args[:2] == ("get", "deployment"):
                return {"metadata": {"name": "php-apache", "namespace": "default", "annotations": dict(ann)},
                        "spec": {"selector": {"matchLabels": {"run": "php-apache"}}, "template": {"spec": {"containers": [
                            {"name": "php", "resources": {"requests": {"cpu": "200m"}, "limits": {"cpu": f"{OPERATOR_M}m"}}}]}}}}
            if args[:2] == ("get", "resourcequota"):
                return {"items": []}
            raise RuntimeError(f"not in the replay: {args}")

        def write(self, args, why):
            writes.append((t[0], list(args), why))
            if args[0] == "annotate":
                k, v = args[-1].split("=", 1)
                ann[k] = v
            elif args[0] == "patch":
                limits[args[2]] = int(round(mmod.milli(json.loads(args[-1])[0]["value"])))

    audit = []
    m = Muscles(Kube(), SimpleNamespace(cap_deployments="default/php-apache", cap_min_change_m=20, interval=10.0), audit.append)
    m._convey_engaged = lambda: True
    m.host_cpu = SimpleNamespace(sample=busy_now)
    m.served = lambda: [("default", {"run": "php-apache"})]
    held = given = 0.0
    lowered, turns, largest = set(), 0, 0
    while t[0] <= rep["window_s"]:
        before = dict(limits)
        m.convey()
        for name, lim in limits.items():
            was = before.get(name, OPERATOR_M)
            if lim < was:
                lowered.add(name)
            elif lim > was:
                largest = max(largest, lim - was)
                if name in lowered:
                    turns += 1
                    lowered.discard(name)
        live = {i["metadata"]["name"] for i in pods_now() if i["metadata"]["labels"].get("run") == "php-apache"}
        above = sum(max(0, limits[n] - OPERATOR_M) for n in live) / 1000.0 * CHECK_S
        given += above
        if any(i["status"]["phase"] == "Pending" for i in pods_now()):
            held += above
        t[0] += CHECK_S
    patches = [w for w in writes if w[1][0] == "patch"]
    lowers = 0
    seen = {}
    for _, args, _ in patches:
        v = int(round(mmod.milli(json.loads(args[-1])[0]["value"])))
        if v < seen.get(args[2], OPERATOR_M):
            lowers += 1
        seen[args[2]] = v
    print(json.dumps({"writes": len(patches), "hand_backs": lowers, "turns": turns, "held_while_waiting": round(held, 2),
                      "given": round(given, 2), "largest_raise_m": largest, "errors": sum(1 for r in audit if "error" in r),
                      "engine_tree": str(Path(mmod.__file__).resolve().parents[1])}))


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
    data = json.loads(INPUTS.read_text())
    n = len(data["reps"])
    work = Path(tempfile.mkdtemp(prefix="convey_owed_"))
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
              "errors": {arm: sum(r["errors"] for r in res[arm]) for arm in res}}
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=1) + "\n")
    if a.md:
        Path(a.md).write_text(render(report))
    print(json.dumps(report, indent=1))
    return 0


LABELS = {"writes": "limits written", "hand_backs": "limits lowered", "turns": "limits raised again after a lowering (the cycle)",
          "held_while_waiting": "processor-seconds above the operator's limit while a best-effort pod waited for a place",
          "given": "processor-seconds above the operator's limit in all", "largest_raise_m": "the largest single raise of one pod's limit"}
UNITS = {"writes": "writes", "hand_backs": "writes", "turns": "turns", "held_while_waiting": "core-s", "given": "core-s",
         "largest_raise_m": "m"}


def render(report):
    """The record of one replay, every gauge read by the key (tools/model_gate.reading: the paired change over the repetitions)."""
    sys.path.insert(0, str(ROOT))
    from tools.legal import stamp
    from tools.readings import by_word, interval_by_word
    lines = ["# Koordinator's best-effort queue through the conveyance: omni-v27 against omni-v26 (our own model, class S)",
             "", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "",
             "`tools/convey_owed_model.py` replays, open loop, the native arm's own timelines of both Koordinator batch-stream tables "
             "on omni-v25 (`" + report["inputs"] + "`: the host's busy share, each best-effort pod's machine and its times made, "
             "placed and done, and the web service's replicas; %d repetitions of runs 42173258848, 42173278954, 42185612749, "
             "41800261877, 41800269022 and 41802293120) through each engine's own conveyance every 15 s, as the governor's fast check "
             "calls it. The conveyance's writes move neither the host's busy share nor the queue, so the model reads the rule alone. "
             "The web service's and the queue's own gauges are read only by the benchmarks' runs (`docs/LOSS_CAUSES_2026-11-07.md`)."
             % report["repetitions"],
             "", "| Gauge | omni-v26, mean a repetition | omni-v27, mean a repetition | Reading | 95% interval of the paired change |",
             "|---|---|---|---|---|"]
    for g, v in report["rows"].items():
        lo, hi = v["ci95"]
        way = "down" if v["relative"] < 0 else "up"
        lines.append(f"| {LABELS[g]} | {v['base_mean']:.2f} | {v['cand_mean']:.2f} | {v['word']}, {way} "
                     f"{by_word(v['relative'] * 100.0, v['word'])}{'' if v['beyond_noise'] else ', inside the noise'} "
                     f"| {interval_by_word(lo, hi, v['word'], unit=' ' + UNITS[g], digits=2)} |")
    lines += ["", "Errors in the conveyance's audit: omni-v26 %d, omni-v27 %d." % (report["errors"]["base"], report["errors"]["cand"]), ""]
    return "\n".join(stamp(lines)) + "\n"


if __name__ == "__main__":
    sys.exit(main())
