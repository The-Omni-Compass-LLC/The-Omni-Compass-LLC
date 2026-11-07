# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The batch stream under a queueing system (BATCH_QUEUE: Kueue or Volcano; docs/BATCH_QUEUE_PREREGISTRATION.md): every
job's wait runs from its submission to its first pod running, the same measure whether the queueing system holds the job
(Kueue) or its pods (Volcano); a job not started or not done by the window's end counts the window's end, never less; and
the stream's job template renders for every system (Kueue, Volcano, the KAI scheduler, Koordinator, and the Kubernetes
scheduler alone, as shipped and with the operator's bin-packing profile)."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.live_reps as LR

T0 = 1_760_000_000          # an epoch; times below are written as UTC stamps from it


def stamp(t):
    import datetime as dt
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def job(name, sub, done=None):
    st = {"completionTime": stamp(done)} if done is not None else {}
    return {"metadata": {"name": name, "creationTimestamp": stamp(sub)}, "status": st}


def pod(job_name, start):
    return {"metadata": {"labels": {"job-name": job_name}}, "status": {"startTime": stamp(start)}}


class JobStream(unittest.TestCase):
    def write(self, d, jobs, pods, end):
        (d / "window_end.txt").write_text(f"{end}\n")
        (d / "jobs.json").write_text(json.dumps({"items": jobs}))
        (d / "pods.json").write_text(json.dumps({"items": pods}))

    def test_wait_turnaround_and_unfinished(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            jobs = [job("a", T0, T0 + 100), job("b", T0 + 30, T0 + 200), job("c", T0 + 60)]
            pods = [pod("a", T0 + 10), pod("a", T0 + 50), pod("b", T0 + 90)]      # c never started
            self.write(d, jobs, pods, T0 + 300)
            g = LR.job_stream(d)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, mean (s)"], (10 + 60 + 240) / 3)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, 95th percentile (s)"], 240)
        self.assertAlmostEqual(g["queue: job turnaround, submitted to done, mean (s)"], (100 + 170 + 240) / 3)
        self.assertEqual(g["queue: jobs unfinished at the window's end"], 1.0)

    def test_absent_without_the_stream(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(LR.job_stream(Path(t)), {})

    def test_every_queue_gauge_reads_lower(self):
        for k in LR.QUEUE:
            self.assertIn(k, LR.KEYS)
            self.assertNotIn(k, LR.NEUTRAL)


class Template(unittest.TestCase):
    def render(self, label, sched, podlabel='omni-stream: "1"'):
        # in the order the script substitutes them: the pod's label first, whose placeholder holds the job's
        text = (ROOT / "deploy" / "kind" / "batch-stream-job.yaml").read_text()
        for a, b in (("JOB_NAME", "omni-batch-001"), ("BATCH_COMPLETIONS", "10"), ("BATCH_PARALLELISM", "5"), ("BATCH_MB", "3000"),
                     ("POD_QUEUE_LABEL", podlabel), ("QUEUE_LABEL", label), ("SCHEDULER_LINE", sched)):
            text = text.replace(a, b)
        return yaml.safe_load(text)

    def test_kueue_volcano_kai_and_koordinator(self):
        k = self.render("kueue.x-k8s.io/queue-name: omni-queue", "terminationGracePeriodSeconds: 30")
        self.assertEqual(k["metadata"]["labels"]["kueue.x-k8s.io/queue-name"], "omni-queue")
        self.assertNotIn("kueue.x-k8s.io/queue-name", k["spec"]["template"]["metadata"]["labels"])   # the job's, never a pod's
        self.assertNotIn("schedulerName", k["spec"]["template"]["spec"])
        v = self.render('omni-stream: "1"', "schedulerName: volcano")
        self.assertEqual(v["spec"]["template"]["spec"]["schedulerName"], "volcano")
        a = self.render("kai.scheduler/queue: default-queue", "schedulerName: kai-scheduler", "kai.scheduler/queue: default-queue")
        self.assertEqual(a["spec"]["template"]["spec"]["schedulerName"], "kai-scheduler")
        self.assertEqual(a["metadata"]["labels"]["kai.scheduler/queue"], "default-queue")
        self.assertEqual(a["spec"]["template"]["metadata"]["labels"]["kai.scheduler/queue"], "default-queue")
        c = self.render('koordinator.sh/enable-colocation: "true"', "terminationGracePeriodSeconds: 30",
                        'koordinator.sh/enable-colocation: "true"')                  # the colocation profile sets the rest
        self.assertEqual(c["metadata"]["labels"]["koordinator.sh/enable-colocation"], "true")
        self.assertEqual(c["spec"]["template"]["metadata"]["labels"]["koordinator.sh/enable-colocation"], "true")
        self.assertNotIn("schedulerName", c["spec"]["template"]["spec"])
        for j in (k, v, a, c):
            self.assertEqual((j["spec"]["completions"], j["spec"]["parallelism"]), (10, 5))
            self.assertEqual(j["spec"]["template"]["metadata"]["labels"]["app"], "omni-batch-stream")

    def test_the_scheduler_alone(self):
        v = self.render('omni-stream: "1"', "terminationGracePeriodSeconds: 30")       # as shipped: the default scheduler
        self.assertNotIn("schedulerName", v["spec"]["template"]["spec"])
        b = self.render('omni-stream: "1"', "schedulerName: binpack-scheduler")
        self.assertEqual(b["spec"]["template"]["spec"]["schedulerName"], "binpack-scheduler")
        text = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()
        self.assertIn('[ "$Q" = binpack ] && sched="schedulerName: binpack-scheduler"', text)
        self.assertRegex(text, r"vanilla\|binpack(\|[a-z]+)*\) NS=kube-system")   # the group's members read kube-system too

    def test_the_script_substitutes_the_pod_label_before_the_job_label(self):
        # QUEUE_LABEL is inside POD_QUEUE_LABEL: substituted the other way round, the pod's line would read POD_<label>
        text = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()
        self.assertLess(text.index('"s|POD_QUEUE_LABEL|'), text.index('"s|QUEUE_LABEL|'))

    def test_every_release_is_pinned(self):
        text = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()
        for name in ("KUEUE_SHA256", "VOLCANO_SHA256", "KAI_SHA256", "KOORD_SHA256"):
            self.assertRegex(text, name + r'="\$\{' + name + r':-[0-9a-f]{64}\}"')

    def test_the_script_parses(self):
        r = subprocess.run(["bash", "-n", str(ROOT / "scripts" / "kind_batch_queue.sh")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)


class KoordinatorFiles(unittest.TestCase):
    def test_values_and_profile(self):
        v = yaml.safe_load((ROOT / "deploy" / "kind" / "koordinator-values.yaml").read_text())
        self.assertEqual(v["imageRepositoryHost"], "ghcr.io")
        for part in ("manager", "scheduler", "descheduler"):
            self.assertEqual(v[part]["replicas"], 1)
            self.assertEqual(v[part]["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})
        p = yaml.safe_load((ROOT / "deploy" / "kind" / "koordinator-colocation.yaml").read_text())
        self.assertEqual((p["spec"]["qosClass"], p["spec"]["schedulerName"], p["spec"]["priorityClassName"]),
                         ("BE", "koord-scheduler", "koord-batch"))
        self.assertEqual(p["spec"]["selector"]["matchLabels"], {"koordinator.sh/enable-colocation": "true"})

    def test_the_bin_packing_profile(self):
        docs = list(yaml.safe_load_all((ROOT / "deploy" / "kind" / "binpack-scheduler.yaml").read_text()))
        kinds = {d["kind"]: d for d in docs}
        cfg = yaml.safe_load(kinds["ConfigMap"]["data"]["config.yaml"])
        self.assertEqual((cfg["apiVersion"], cfg["kind"]), ("kubescheduler.config.k8s.io/v1", "KubeSchedulerConfiguration"))
        self.assertFalse(cfg["leaderElection"]["leaderElect"])                       # one replica
        (prof,) = cfg["profiles"]
        self.assertEqual(prof["schedulerName"], "binpack-scheduler")
        (fit,) = prof["pluginConfig"]                                                  # every other plugin the release's default
        self.assertEqual(fit["name"], "NodeResourcesFit")
        self.assertEqual(fit["args"]["scoringStrategy"]["type"], "MostAllocated")
        self.assertEqual({r["name"]: r["weight"] for r in fit["args"]["scoringStrategy"]["resources"]}, {"cpu": 1, "memory": 1})
        spec = kinds["Deployment"]["spec"]
        self.assertEqual(spec["replicas"], 1)
        pod = spec["template"]["spec"]
        self.assertEqual(pod["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})
        self.assertEqual(pod["containers"][0]["image"], "KUBE_SCHEDULER_IMAGE")      # the control plane's own, read by the script
        roles = {d["roleRef"]["name"] for d in docs if d["kind"] in ("ClusterRoleBinding", "RoleBinding")}
        self.assertEqual(roles, {"system:kube-scheduler", "system:volume-scheduler", "extension-apiserver-authentication-reader"})

    def test_koordinators_cluster_is_the_rigs_with_the_cgroup_root_its_own_tests_use(self):
        full = yaml.safe_load((ROOT / "deploy" / "kind" / "cluster-full.yaml").read_text())
        koord = yaml.safe_load((ROOT / "deploy" / "kind" / "cluster-koordinator.yaml").read_text())
        self.assertEqual(koord["nodes"], full["nodes"])                               # one control plane, six workers
        patch = list(yaml.safe_load_all(koord["kubeadmConfigPatches"][0]))
        self.assertEqual({d["kind"]: d for d in patch}["KubeletConfiguration"]["cgroupRoot"], "/")
        self.assertNotIn("kubeadmConfigPatches", full)                               # every other set: kind's default
        paired = (ROOT / "scripts" / "kind_paired.sh").read_text()
        self.assertIn('[ "${BATCH_QUEUE:-}" = koordinator ] && cluster=deploy/kind/cluster-koordinator.yaml', paired)
        self.assertIn('--config "$cluster"', paired)

    def test_kai_values_place_every_component_on_the_control_plane(self):
        v = yaml.safe_load((ROOT / "deploy" / "kind" / "kai-values.yaml").read_text())
        self.assertEqual(v["global"]["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
