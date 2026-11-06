# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The group of clusters (docs/GROUP_PREREGISTRATION.md): the members' records merge into one arm the table tool reads (the
window from the stream's start to the first member's end, every job once with its submission and its last part done, the
machines summed at each moment, an unfinished part leaving its job unfinished); the stream goes to the orchestrator or to
the members in turn; Karmada's release is pinned; a member's bench opens its window with the others' and sends no stream."""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
import sys; sys.path.insert(0, str(ROOT))
import tools.merge_group as MG
import tools.live_reps as LR

T0 = 1_800_000_000


def iso(t):
    return MG.iso(t)


def member(d: Path, name: str, jobs, pods, nodes, shift=0):
    m = d / name; m.mkdir()
    (m / "window_start.txt").write_text(f"{T0 - 5 + shift}\n"); (m / "window_end.txt").write_text(f"{T0 + 600 + shift}\n")
    (m / "preflight.txt").write_text("batch: 24 jobs of 10 pods, 5 at a time, one every 30 s, 3000 MB hashed each, through group\n")
    (m / "jobs.json").write_text(json.dumps({"items": jobs}))
    (m / "pods.json").write_text(json.dumps({"items": pods}))
    with open(m / "capture.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "elapsed_seconds", "nodes_ready", "nodes_total", "alloc_cpu_m", "req_cpu_m", "used_cpu_m",
                    "pods_pending", "hpa_count", "hpa_current_replicas", "hpa_desired_replicas", "power_w"])
        for i, n in enumerate(nodes):
            w.writerow([iso(T0 + 15 * i + shift), 15 * i, n, 6, 24000, 1000, 500, 0, 1, 1, 1, 100.0 * n])
    (m / "latency.csv").write_text("elapsed_seconds,latency_ms,ok\n5,10,1\n10,12,1\n")
    return m


def job(name, created, done=None):
    j = {"metadata": {"name": name, "creationTimestamp": iso(created)}, "spec": {"completions": 10}, "status": {}}
    if done:
        j["status"]["completionTime"] = iso(done)
    return j


def pod(job_name, start):
    return {"metadata": {"name": f"{job_name}-x", "labels": {"job-name": job_name}}, "status": {"startTime": iso(start)}}


class GroupMerge(unittest.TestCase):
    def test_the_group_alone_reads_each_job_from_its_member(self):
        d = Path(tempfile.mkdtemp()) / "bench-nativebare-1"; d.mkdir(parents=True)
        (d / "stream_start.txt").write_text(f"{T0}\n"); (d / "batch_done.txt").write_text(f"{T0 + 300}\n")
        member(d, "m1", [job("omni-batch-001", T0 + 1, T0 + 100)], [pod("omni-batch-001", T0 + 4)], [6, 6, 5])
        member(d, "m2", [job("omni-batch-002", T0 + 31, None)], [pod("omni-batch-002", T0 + 40)], [6, 5, 5], shift=3)
        out = MG.main(d, 2, "none")
        self.assertIn("2 jobs (1 done)", out)
        with open(d / "capture.csv") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual([r["nodes_ready"] for r in rows], ["12", "11", "10"])            # summed at each moment
        self.assertEqual(rows[0]["power_w"], "1200.0")
        self.assertEqual(float((d / "window_start.txt").read_text()), T0)                   # the stream's start
        self.assertEqual(float((d / "window_end.txt").read_text()), T0 + 600)               # the first member's end
        g = LR.job_stream(d)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, mean (s)"], (3 + 9) / 2)
        self.assertEqual(g["queue: jobs unfinished at the window's end"], 1.0)
        self.assertIn("batch:", (d / "preflight.txt").read_text())

    def test_through_the_orchestrator_a_job_is_sent_when_it_reached_it_and_done_when_its_last_part_is(self):
        d = Path(tempfile.mkdtemp()) / "bench-native-1"; d.mkdir(parents=True)
        (d / "stream_start.txt").write_text(f"{T0}\n")
        (d / "orch_jobs.json").write_text(json.dumps({"items": [job("omni-batch-001", T0), job("omni-batch-002", T0 + 30)]}))
        member(d, "m1", [job("omni-batch-001", T0 + 2, T0 + 90), job("omni-batch-002", T0 + 32, T0 + 200)],
               [pod("omni-batch-001", T0 + 5), pod("omni-batch-002", T0 + 35)], [6, 6])
        member(d, "m2", [job("omni-batch-002", T0 + 32, None)], [pod("omni-batch-002", T0 + 33)], [6, 6])   # a part not done
        MG.main(d, 2, "karmada")
        jobs = {j["metadata"]["name"]: j for j in json.loads((d / "jobs.json").read_text())["items"]}
        self.assertEqual(jobs["omni-batch-001"]["metadata"]["creationTimestamp"], iso(T0))     # sent to the orchestrator
        self.assertEqual(jobs["omni-batch-001"]["status"]["completionTime"], iso(T0 + 90))
        self.assertNotIn("completionTime", jobs["omni-batch-002"]["status"])                  # its part on m2 never ended
        g = LR.job_stream(d)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, mean (s)"], (5 + 3) / 2)

    def test_a_member_without_a_valid_record_fails_the_arm(self):
        d = Path(tempfile.mkdtemp()) / "bench-native-1"; d.mkdir(parents=True)
        member(d, "m1", [], [], [6])
        with self.assertRaises(SystemExit):
            MG.main(d, 2, "none")


class GroupWiring(unittest.TestCase):
    ORCH = (ROOT / "scripts" / "kind_group_orch.sh").read_text()
    BENCH = (ROOT / "scripts" / "kind_bench.sh").read_text()
    QUEUE = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()

    def test_the_stream_goes_to_the_orchestrator_or_to_the_members_in_turn(self):
        self.assertIn('to="$D/kubeconfig-m$(( (i - 1) % N + 1 ))"', self.ORCH)
        self.assertIn('else to="$KC"; where="$ORCH"; fi', self.ORCH)
        self.assertIn('[ "$Q" = group ] && exit 0', self.QUEUE)                              # a member sends nothing

    def test_karmadas_release_is_pinned_and_its_credentials_stay_out_of_the_runs_files(self):
        self.assertRegex(self.ORCH, r'KARMADACTL_SHA256="\$\{KARMADACTL_SHA256:-[0-9a-f]{64}\}"')
        self.assertRegex(self.ORCH, r'KARMADA_CRDS_SHA256="\$\{KARMADA_CRDS_SHA256:-[0-9a-f]{64}\}"')
        self.assertIn('W="${RUNNER_TEMP:-/tmp}/omni-group-', self.ORCH)
        self.assertIn('rm -rf "$W"', self.ORCH)
        self.assertIn('rm -f "$D"/kubeconfig-*', (ROOT / "scripts" / "kind_group.sh").read_text())
        pol = yaml.safe_load((ROOT / "deploy" / "kind" / "karmada-propagation.yaml").read_text().replace("MEMBER_CLUSTERS", "[a, b]"))
        self.assertEqual(pol["spec"]["placement"]["replicaScheduling"],
                         {"replicaSchedulingType": "Divided", "replicaDivisionPreference": "Aggregated"})

    def test_a_member_opens_its_window_with_the_others(self):
        i = self.BENCH.index('if [ -n "${GROUP_BARRIER:-}" ]; then')
        self.assertLess(self.BENCH.index('sleep "$WARMUP"'), i)
        self.assertLess(i, self.BENCH.index('date -u +%s > "$OUT_DIR/window_start.txt"'))
        self.assertIn("|godel|group|vanilla|binpack)", self.BENCH)

    def test_ocm_is_pinned_and_places_every_job_by_a_placement_of_its_own(self):
        # amendment 1: clusteradm and its bundle pinned; a Placement per job (one cluster of the default set, OCM's default
        # prioritizers), the job as a ManifestWork where OCM decided; the token never in the run's files
        self.assertRegex(self.ORCH, r'CLUSTERADM_SHA256="\$\{CLUSTERADM_SHA256:-[0-9a-f]{64}\}"')
        self.assertIn('OCM_BUNDLE="${OCM_BUNDLE:-1.4.0}"', self.ORCH)
        self.assertIn('--bundle-version "$OCM_BUNDLE"', self.ORCH)
        place = self.ORCH[self.ORCH.index("ocm_place() {"):self.ORCH.index('case "${PHASE:?')]
        self.assertIn("kind: Placement", place)
        self.assertIn("numberOfClusters: 1", place)
        self.assertIn("clusterSets: [default]", place)
        self.assertNotIn("prioritizerPolicy", place)                                       # OCM's own default prioritizers
        self.assertIn('"kind": "ManifestWork"', place)
        self.assertIn('"namespace": sys.argv[3]', place)                                   # the member OCM decided
        self.assertIn('rm -f "$W/join.sh"', self.ORCH)
        self.assertIn('kind: ManagedClusterSetBinding', self.ORCH)
        group = (ROOT / "scripts" / "kind_group.sh").read_text()
        self.assertIn("karmada|ocm|armada) ;;", group)
        self.assertIn('agent_ns="open-cluster-management open-cluster-management-agent open-cluster-management-agent-addon"', group)
        self.assertIn("IN($qs[])", self.BENCH)                                              # several agent namespaces allowed
        self.assertIn('"orch=ocm"', (ROOT / "docs" / "GROUP_PREREGISTRATION.md").read_text().replace("`orch=ocm`", '"orch=ocm"'))

    def test_armada_is_pinned_and_takes_every_batch_as_a_job_set_of_its_pods(self):
        # amendment 2: armadactl and every image pinned (the images by digest); a batch is one job set of COMPLETIONS jobs,
        # each the stream's pod with its labels and requests equal to limits (Armada's rule); its control plane on the
        # runner's own network, not on a cluster; the members' kubeconfigs copied outside the run's files and removed
        self.assertRegex(self.ORCH, r'ARMADACTL_SHA256="\$\{ARMADACTL_SHA256:-[0-9a-f]{64}\}"')
        for var in ("ARMADA_BUNDLE", "ARMADA_LOOKOUT", "ARMADA_REDIS", "ARMADA_POSTGRES", "ARMADA_PULSAR"):
            self.assertRegex(self.ORCH, var + r'="[a-z/-]+@sha256:[0-9a-f]{64}"')
        sub = self.ORCH[self.ORCH.index("armada_submit() {"):self.ORCH.index("armada_done() {")]
        code = sub[sub.index("<<'PY'\n") + 7:sub.index("\nPY\n")]
        out = subprocess.run([sys.executable, "-c", code, "omni-batch-007", "10", "3000"], capture_output=True, text=True, check=True).stdout
        spec = yaml.safe_load(out)
        self.assertEqual((spec["queue"], spec["jobSetId"], len(spec["jobs"])), ("omni", "omni-batch-007", 10))
        job = spec["jobs"][0]
        self.assertEqual(job["labels"]["job-name"], "omni-batch-007")
        res = job["podSpecs"][0]["containers"][0]["resources"]
        self.assertEqual(res["requests"], res["limits"])
        self.assertIn("count=3000", job["podSpecs"][0]["containers"][0]["command"][2])
        self.assertNotIn("&id", out)                                                        # ten jobs written out, no aliases
        self.assertIn('--network host --cpuset-cpus "$cores"', self.ORCH)
        self.assertIn('cp "$D/kubeconfig-m$i" "$AR/kubeconfig-m$i"', self.ORCH)
        self.assertIn('AR="$W/armada"', self.ORCH)
        group = (ROOT / "scripts" / "kind_group.sh").read_text()
        self.assertIn("karmada|ocm|armada) ;;", group)
        self.assertIn("case \"$orch\" in none|armada) ;;", group)                              # no omni-host for Armada

    def test_a_batch_whose_jobs_are_pods_reads_its_end_from_the_orchestrators_record(self):
        # Armada runs pods, not Jobs: a member has no Job of the batch's name, so the merger takes the end Armada's record
        # carries (its tenth pod's end), and none where the record carries none
        d = Path(tempfile.mkdtemp()) / "bench-native-1"; d.mkdir(parents=True)
        (d / "stream_start.txt").write_text(f"{T0}\n")
        done = job("omni-batch-001", T0, T0 + 120); done["status"]["pods"] = 10
        (d / "orch_jobs.json").write_text(json.dumps({"items": [done, job("omni-batch-002", T0 + 30)]}))
        member(d, "m1", [], [pod("omni-batch-001", T0 + 4)], [6, 6])
        member(d, "m2", [], [pod("omni-batch-002", T0 + 35)], [6, 6])
        MG.main(d, 2, "armada")
        jobs = {j["metadata"]["name"]: j for j in json.loads((d / "jobs.json").read_text())["items"]}
        self.assertEqual(jobs["omni-batch-001"]["status"]["completionTime"], iso(T0 + 120))
        self.assertNotIn("completionTime", jobs["omni-batch-002"]["status"])
        g = LR.job_stream(d)
        self.assertEqual(g["queue: jobs unfinished at the window's end"], 1.0)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
