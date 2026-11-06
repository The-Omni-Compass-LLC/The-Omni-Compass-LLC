# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Gödel scheduler on the batch rig (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 8): the pinned commit, node image and
metrics-server named the same in the scripts, the workflow and the preregistration; the image built from that commit and
checked before it is loaded; the stream's pods sent to Gödel with its guide's three annotations while every other system's
job file stays as it was; and the bench takes Gödel, its namespace and its metrics-server line."""
import re
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
QUEUE = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()
BENCH = (ROOT / "scripts" / "kind_bench.sh").read_text()
BUILD = (ROOT / "scripts" / "kind_godel_build.sh").read_text()
PREREG = (ROOT / "docs" / "BATCH_QUEUE_PREREGISTRATION.md").read_text()
WF = yaml.safe_load((ROOT / ".github" / "workflows" / "kind-godel.yml").read_text())
COMMIT = re.search(r'GODEL_COMMIT="\$\{GODEL_COMMIT:-([0-9a-f]{40})\}"', QUEUE).group(1)


def job(queue_vars: str) -> dict:
    """The stream's job file as the submit phase writes it, for the given queue variables (the script's own sed line)."""
    sed = QUEUE[QUEUE.index('    sed -e "s/JOB_NAME/omni-batch-'):QUEUE.index('deploy/kind/batch-stream-job.yaml > "$OUT_DIR/job.yaml"')]
    script = (f'COMPLETIONS=10 PARALLELISM=5 MB=3000 i=1; label=""; podlabel=""; sched=""; podann=""; {queue_vars}\n'
              + sed.replace("\\\n", " ") + " deploy/kind/batch-stream-job.yaml")
    out = subprocess.run(["bash", "-c", script], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return yaml.safe_load(out)


class GodelRig(unittest.TestCase):
    def test_the_pins_are_the_preregistered_ones(self):
        self.assertIn(COMMIT, PREREG)
        env = next(s for s in WF["jobs"]["run"]["steps"] if "kind_paired.sh" in str(s.get("run", "")))["env"]
        self.assertEqual(env["BATCH_QUEUE"], "godel")
        for k in ("KIND_NODE_IMAGE", "METRICS_SERVER_SHA256"):
            self.assertIn(env[k].split("@")[-1].replace("sha256:", ""), PREREG)
        self.assertTrue(env["KIND_NODE_IMAGE"].startswith("kindest/node:v1.24."))
        self.assertEqual(env["METRICS_SERVER_VERSION"], "v0.5.2")
        kind = next(s for s in WF["jobs"]["run"]["steps"] if str(s.get("uses", "")).startswith("helm/kind-action"))
        self.assertEqual((kind["with"]["version"], kind["with"]["kubectl_version"]), ("v0.22.0", "v1.24.17"))

    def test_the_image_is_built_from_the_pinned_commit_and_checked_before_it_is_loaded(self):
        steps = [str(s.get("run", "")) for s in WF["jobs"]["run"]["steps"]]
        self.assertLess(steps.index("bash scripts/kind_godel_build.sh"), next(i for i, s in enumerate(steps) if "kind_paired.sh" in s))
        got = subprocess.run(["bash", "-c", BUILD[BUILD.index('GODEL_COMMIT="'):BUILD.index("\n", BUILD.index('GODEL_COMMIT="'))]
                              + '\necho "$GODEL_COMMIT"'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        self.assertEqual(got, COMMIT)                                           # one pin, read from the queue script
        self.assertIn('docker build -q -t godel-local:latest -f docker/godel-local.Dockerfile .', BUILD)
        self.assertIn('IMAGE_ID', BUILD)
        install = QUEUE[QUEUE.index('elif [ "$Q" = godel ]; then'):]
        self.assertLess(install.index('rev-parse HEAD'), install.index('kind load docker-image godel-local:latest'))
        self.assertLess(install.index('IMAGE_ID'), install.index('kind load docker-image godel-local:latest'))
        self.assertIn('kubectl apply --server-side -k "$GODEL_SRC/manifests/base"', install)

    def test_the_stream_goes_to_godel_with_its_annotations_and_no_other_job_changes(self):
        g = job('sched="schedulerName: godel-scheduler"; podann=", annotations: {godel.bytedance.com/pod-state: pending, '
                'godel.bytedance.com/pod-resource-type: guaranteed, godel.bytedance.com/pod-launcher: kubelet}"')
        pod = g["spec"]["template"]
        self.assertEqual(pod["spec"]["schedulerName"], "godel-scheduler")
        self.assertEqual(pod["metadata"]["annotations"], {"godel.bytedance.com/pod-state": "pending",
                                                          "godel.bytedance.com/pod-resource-type": "guaranteed",
                                                          "godel.bytedance.com/pod-launcher": "kubelet"})
        self.assertIn('[ "$Q" = godel ] && { sched="schedulerName: godel-scheduler"', QUEUE)
        k = job('label="kai.scheduler/queue: default-queue"; podlabel="$label"; sched="schedulerName: kai-scheduler"')
        self.assertNotIn("annotations", k["spec"]["template"]["metadata"])     # every other system's pods as before
        self.assertEqual(k["spec"]["template"]["metadata"]["labels"]["kai.scheduler/queue"], "default-queue")

    def test_the_bench_takes_godel_its_namespace_and_its_metrics_server(self):
        self.assertRegex(BENCH, r'case "\$BATCH_QUEUE" in ""\|[a-z|]*\|godel\|[a-z|]*binpack\)')   # Gödel among the queues
        self.assertIn('[ "$BATCH_QUEUE" = godel ] && qns=godel-system', BENCH)
        self.assertIn("v0.5.*) ms_floor=8 ;;", BENCH)
        self.assertIn("godel) NS=godel-system ;;", QUEUE)

    def test_metrics_server_is_applied_once_with_the_rigs_settings_and_by_the_registry_that_serves_it(self):
        # amendment 9: one rollout (two left the first pod terminating past the wait on 1.24); k8s.gcr.io only redirects
        self.assertNotIn("patch deployment metrics-server", BENCH)
        code = BENCH[BENCH.index("<<'EOF'\nimport sys, yaml") + len("<<'EOF'\n"):BENCH.index("\nEOF\nkubectl apply -f \"$OUT_DIR/metrics-server-rig.yaml\"")]
        manifest = ("apiVersion: v1\nkind: ServiceAccount\nmetadata: {name: metrics-server, namespace: kube-system}\n---\n"
                    "apiVersion: apps/v1\nkind: Deployment\nmetadata: {name: metrics-server, namespace: kube-system}\n"
                    "spec:\n  template:\n    spec:\n      containers:\n      - name: metrics-server\n"
                    "        image: k8s.gcr.io/metrics-server/metrics-server:v0.5.2\n        args: [--cert-dir=/tmp]\n")
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
            f.write(manifest)
        out = subprocess.run(["python3", "-", f.name], input=code, capture_output=True, text=True, check=True).stdout
        docs = list(yaml.safe_load_all(out))
        dep = next(d for d in docs if d["kind"] == "Deployment")["spec"]["template"]["spec"]
        self.assertEqual(dep["containers"][0]["image"], "registry.k8s.io/metrics-server/metrics-server:v0.5.2")
        self.assertEqual(dep["containers"][0]["args"], ["--cert-dir=/tmp", "--kubelet-insecure-tls"])
        self.assertEqual(dep["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})
        # amendment 10: kubeadm 1.24 taints the control plane twice (control-plane and master); a pod tolerating only the first
        # stays Pending and the rollout never finishes (runs 39438395275, 39438412522, 39438430198: every arm invalid)
        self.assertEqual({t["key"] for t in dep["tolerations"]},
                         {"node-role.kubernetes.io/control-plane", "node-role.kubernetes.io/master"})
        self.assertTrue(all(t["operator"] == "Exists" and t["effect"] == "NoSchedule" for t in dep["tolerations"]))
        self.assertEqual(len(docs), 2)                                          # every other document untouched

    def test_every_pod_pinned_to_the_control_plane_tolerates_both_taints_of_1_24(self):
        # amendment 10, second finding (run 39479725812): the load generator stayed Pending behind the master taint
        import glob
        for f in sorted(glob.glob(str(ROOT / "deploy" / "kind" / "*.yaml"))) + [str(ROOT / "scripts" / "kind_batch_queue.sh"), str(ROOT / "scripts" / "kind_bench.sh")]:
            text = Path(f).read_text()
            for pat in ("{key: node-role.kubernetes.io/control-plane, operator: Exists",       # a toleration in a manifest or chart values
                        '"key": "node-role.kubernetes.io/control-plane", "operator": "Exists"',  # the bench's patch (Python)
                        '"key":"node-role.kubernetes.io/control-plane","operator":"Exists"'):   # the batch rig's patch (JSON)
                at = 0
                while (i := text.find(pat, at)) >= 0:
                    self.assertIn("node-role.kubernetes.io/master", text[i:i + 400],
                                  f"{f}: a control-plane toleration without the master taint beside it")
                    at = i + len(pat)
        for f in ("loadgen.yaml", "loadgen-open.yaml", "noisy.yaml"):
            text = (ROOT / "deploy" / "kind" / f).read_text()
            self.assertIn("node-role.kubernetes.io/master, operator: Exists, effect: NoSchedule", text, f)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
