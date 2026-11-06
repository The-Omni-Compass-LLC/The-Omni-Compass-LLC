# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""KubeRay on the batch rig (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 7): the pinned chart and Ray image named the same
in the script and the preregistration; KubeRay's own autoscaling sample with only the operator's three settings; the same
stream as Ray jobs; and the stream's gauges read from each Ray job's own record, an unfinished job never reading quick."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.live_reps as LR

SCRIPT = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()
PREREG = (ROOT / "docs" / "BATCH_QUEUE_PREREGISTRATION.md").read_text()


def ts(epoch):
    import datetime as dt
    return dt.datetime.fromtimestamp(epoch, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class KubeRayRig(unittest.TestCase):
    def test_the_pins_are_the_preregistered_ones(self):
        chart = re.search(r'KUBERAY_SHA256="\$\{KUBERAY_SHA256:-([0-9a-f]{64})\}"', SCRIPT).group(1)
        digest = re.search(r'RAY_DIGEST="(sha256:[0-9a-f]{64})"', SCRIPT).group(1)
        self.assertIn(chart, PREREG)
        self.assertIn(digest, PREREG)
        self.assertIn('KUBERAY_VERSION="${KUBERAY_VERSION:-1.7.1}"', SCRIPT)
        self.assertIn('RAY_IMAGE="rayproject/ray:2.52.0"', SCRIPT)

    def test_the_cluster_is_the_sample_with_the_operators_three_settings(self):
        rc = yaml.safe_load((ROOT / "deploy" / "kind" / "kuberay-cluster.yaml").read_text())
        spec = rc["spec"]
        self.assertTrue(spec["enableInTreeAutoscaling"])
        self.assertEqual((spec["autoscalerOptions"]["upscalingMode"], spec["autoscalerOptions"]["idleTimeoutSeconds"]), ("Default", 60))
        head = spec["headGroupSpec"]
        self.assertEqual(head["rayStartParams"]["num-cpus"], "0")                                    # the head takes no task
        self.assertIn("node-role.kubernetes.io/control-plane", head["template"]["spec"]["nodeSelector"])
        w = spec["workerGroupSpecs"][0]
        self.assertEqual((w["minReplicas"], w["maxReplicas"]), (0, "MAX_WORKERS"))                    # sized live at install
        self.assertEqual(w["rayStartParams"]["num-cpus"], "1")
        res = w["template"]["spec"]["containers"][0]["resources"]
        job = yaml.safe_load(re.sub(r"\b[A-Z_]{5,}\b", "1", (ROOT / "deploy" / "kind" / "batch-stream-job.yaml").read_text()
                                    .replace("SCHEDULER_LINE", "x: 1").replace("POD_QUEUE_LABEL", "a: b").replace("QUEUE_LABEL", "a: b")))
        pod = job["spec"]["template"]["spec"]["containers"][0]["resources"]
        self.assertEqual((res["requests"]["cpu"], res["limits"]["cpu"]), (pod["requests"]["cpu"], pod["limits"]["cpu"]))
        for image in [head["template"]["spec"]["containers"][0]["image"], w["template"]["spec"]["containers"][0]["image"]]:
            self.assertEqual(image, "rayproject/ray:2.52.0")

    def test_the_worker_ceiling_is_bounded_by_the_machines_memory_as_well(self):
        # amendment 9: a kind node reports the whole machine's memory as its own; 48 workers of 1 GiB took the trial's runner down
        code = SCRIPT[SCRIPT.index("python3 -c '\nimport json, sys\ndef cpu(v)") + len("python3 -c '\n"):]
        code = code[:code.index("')")]
        self.assertIn('MemAvailable', code)
        self.assertEqual(res_limit := yaml.safe_load((ROOT / "deploy" / "kind" / "kuberay-cluster.yaml").read_text())
                         ["spec"]["workerGroupSpecs"][0]["template"]["spec"]["containers"][0]["resources"]["limits"]["memory"], "1Gi")
        nodes = json.dumps({"items": [{"status": {"allocatable": {"cpu": "4"}}} for _ in range(6)]})
        out = subprocess.run([sys.executable, "-c", code], input=nodes, capture_output=True, text=True, check=True).stdout
        free_gib = next(int(l.split()[1]) for l in open("/proc/meminfo") if l.startswith("MemAvailable:")) / 2 ** 20
        self.assertEqual(int(out), max(1, min(48, int(free_gib - 3))))          # 48 by the processors; the machine's free memory less 3 GiB

    def test_the_stream_is_the_same_work(self):
        rj = yaml.safe_load((ROOT / "deploy" / "kind" / "kuberay-job.yaml").read_text())
        self.assertEqual(rj["spec"]["submissionMode"], "HTTPMode")                                    # no submitter pod
        self.assertEqual(rj["spec"]["clusterSelector"], {"ray.io/cluster": "omni-ray"})
        for k in ("BATCH_COMPLETIONS", "BATCH_PARALLELISM", "BATCH_MB"):
            self.assertIn(k, rj["spec"]["entrypoint"])
        driver = (ROOT / "deploy" / "kind" / "kuberay_stream_job.py").read_text()
        self.assertIn('dd if=/dev/zero bs=1M count={mb} 2>/dev/null | sha256sum', driver)
        self.assertIn("dd if=/dev/zero bs=1M count=BATCH_MB 2>/dev/null | sha256sum",
                      (ROOT / "deploy" / "kind" / "batch-stream-job.yaml").read_text())
        self.assertIn("@ray.remote(num_cpus=1)", driver)
        self.assertIn('print("OMNI_TIMES "', driver)

    def test_each_ray_job_is_read_from_its_own_record(self):
        block = SCRIPT[SCRIPT.index('if [ "$Q" = kuberay ]; then\n    # every Ray job'):]
        code = block[block.index("<<'PY'\n") + 7:block.index("\nPY\n")]
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            (d / "rayjobs.json").write_text(json.dumps({"items": [
                {"metadata": {"name": "omni-ray-001", "creationTimestamp": ts(1000)},
                 "status": {"jobId": "omni-ray-001-x", "jobStatus": "SUCCEEDED", "endTime": ts(1100)}},
                {"metadata": {"name": "omni-ray-002", "creationTimestamp": ts(1030)},
                 "status": {"jobId": "omni-ray-002-y", "jobStatus": "RUNNING"}}]}))
            (d / "ray_job_logs.txt").write_text("== omni-ray-001-x\nsome line\nOMNI_TIMES {\"first\": 1012.0, \"last\": 1095.0, \"tasks\": 10}\n"
                                                "== omni-ray-002-y\nstill running\n")
            subprocess.run([sys.executable, "-c", code, str(d)], check=True)
            rows = json.loads((d / "ray_times.json").read_text())["items"]
            self.assertEqual(rows[0]["first_task"], 1012.0)
            self.assertIsNone(rows[1]["first_task"])
            (d / "window_end.txt").write_text("1200\n")
            g = LR.job_stream(d)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, mean (s)"], (12 + 170) / 2)  # unstarted: the window's end
        self.assertAlmostEqual(g["queue: job turnaround, submitted to done, mean (s)"], (100 + 170) / 2)
        self.assertEqual(g["queue: jobs unfinished at the window's end"], 1.0)

    def test_the_bench_takes_kuberay_and_its_namespace(self):
        bench = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertIn("|kuberay|", bench)
        self.assertIn('[ "$BATCH_QUEUE" = kuberay ] && qns=kuberay-system', bench)
        wf = (ROOT / ".github" / "workflows" / "kind-orchestrators.yml").read_text()
        self.assertIn("if: inputs.batch_queue == 'kuberay'", wf)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
