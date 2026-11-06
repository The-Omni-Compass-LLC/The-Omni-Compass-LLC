# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The add-on test's plug (scripts/kubectl_keda.py) against a stand-in cluster where KEDA owns the HPA and undoes any write
to it (tests/standin_keda/kubectl): the engine's own writes, in the order the controller makes them, land on the ScaledObject
and show on the HPA; the reset hands every setting back and leaves no record on either; a write the plug cannot carry
exactly is refused; reads pass through untouched; and the controller's own reset runs through it unchanged."""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUG = ROOT / "scripts" / "kubectl_keda.py"
STANDIN = ROOT / "tests" / "standin_keda" / "kubectl"
ANN = "omnicompass.io/original-target-utilization"
RNG = "omnicompass.io/original-replica-range"


def cluster(target=50, records=None):
    so = {"apiVersion": "keda.sh/v1alpha1", "kind": "ScaledObject",
          "metadata": {"name": "php-apache", "namespace": "default",
                       "annotations": {"kubectl.kubernetes.io/last-applied-configuration": "{}", **(records or {})}},
          "spec": {"minReplicaCount": 1, "maxReplicaCount": 10, "triggers": [
              {"type": "cpu", "metricType": "Utilization", "metadata": {"value": str(target)}},
              {"type": "external-push", "metadata": {"interceptorRoute": "php-apache", "scalerAddress": "s:9090"}}]}}
    hpa = {"apiVersion": "autoscaling/v2", "kind": "HorizontalPodAutoscaler",
           "metadata": {"name": "php-apache", "namespace": "default", "annotations": dict(so["metadata"]["annotations"]),
                        "ownerReferences": [{"apiVersion": "keda.sh/v1alpha1", "kind": "ScaledObject", "name": "php-apache"}]},
           "spec": {"minReplicas": 1, "maxReplicas": 10, "scaleTargetRef": {"kind": "Deployment", "name": "php-apache"},
                    "metrics": [{"type": "External", "external": {"metric": {"name": "s1-http"},
                                                                  "target": {"type": "AverageValue", "averageValue": "1"}}},
                                {"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization",
                                                                                            "averageUtilization": target}}}]},
           "status": {"currentReplicas": 1, "desiredReplicas": 1}}
    return {"so": so, "hpa": hpa}


class Plug(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); d = Path(self.tmp.name)
        self.state, self.log = d / "state.json", d / "plug.jsonl"
        self.state.write_text(json.dumps(cluster()))
        self.env = dict(os.environ, OMNI_KUBECTL=str(STANDIN), STANDIN_STATE=str(self.state), OMNI_PLUG_LOG=str(self.log),
                        OMNI_PLUG_WAIT_S="3")

    def tearDown(self):
        self.tmp.cleanup()

    def k(self, *args, code=0):
        r = subprocess.run([sys.executable, str(PLUG), *args], env=self.env, capture_output=True, text=True)
        self.assertEqual(r.returncode, code, (args, r.stdout, r.stderr))
        return r

    def now(self):
        s = json.loads(self.state.read_text())
        cpu = [m["resource"]["target"]["averageUtilization"] for m in s["hpa"]["spec"]["metrics"] if m["type"] == "Resource"]
        return s, cpu[0]

    def target(self, v):
        return ["patch", "hpa", "php-apache", "-n", "default", "--type=json", "-p",
                json.dumps([{"op": "replace", "path": "/spec/metrics/1/resource/target/averageUtilization", "value": v}])]

    def test_target_reaches_keda_and_the_reset_leaves_nothing(self):
        self.k("annotate", "hpa", "php-apache", "-n", "default", "--overwrite", f"{ANN}=50")
        self.k(*self.target(35))
        s, cpu = self.now()
        self.assertEqual(s["so"]["spec"]["triggers"][0]["metadata"]["value"], "35")
        self.assertEqual(cpu, 35)
        self.assertEqual(s["hpa"]["metadata"]["annotations"][ANN], "50")    # survives KEDA's rebuild: it is on the ScaledObject
        self.k(*self.target(50))
        self.k("annotate", "hpa", "php-apache", "-n", "default", f"{ANN}-")
        s, cpu = self.now()
        self.assertEqual((s["so"]["spec"]["triggers"][0]["metadata"]["value"], cpu), ("50", 50))
        self.assertNotIn(ANN, s["hpa"]["metadata"]["annotations"] or {})
        self.assertNotIn(ANN, s["so"]["metadata"]["annotations"] or {})
        recs = [json.loads(l) for l in self.log.read_text().splitlines()]
        self.assertTrue(recs and all(r["hpa_shows"] for r in recs))

    def test_replica_range(self):
        self.k("annotate", "hpa", "php-apache", "-n", "default", "--overwrite", f"{RNG}=1,10")
        self.k("patch", "hpa", "php-apache", "-n", "default", "--type=merge", "-p", json.dumps({"spec": {"minReplicas": 3}}))
        s, _ = self.now()
        self.assertEqual((s["so"]["spec"]["minReplicaCount"], s["hpa"]["spec"]["minReplicas"]), (3, 3))
        self.k("patch", "hpa", "php-apache", "-n", "default", "--type=merge",
               "-p", json.dumps({"spec": {"minReplicas": 1, "maxReplicas": 10}}))
        self.k("annotate", "hpa", "php-apache", "-n", "default", f"{RNG}-")
        s, _ = self.now()
        self.assertEqual((s["hpa"]["spec"]["minReplicas"], s["hpa"]["spec"]["maxReplicas"]), (1, 10))
        self.assertNotIn(RNG, s["hpa"]["metadata"]["annotations"] or {})

    def test_refuses_what_it_cannot_carry_exactly(self):
        r = self.k("patch", "hpa", "php-apache", "-n", "default", "--type=merge", "-p", json.dumps({"spec": {"behavior": {}}}), code=2)
        self.assertIn("refused", r.stderr)
        r = self.k("patch", "hpa", "php-apache", "-n", "default", "--type=json", "-p",
                   json.dumps([{"op": "replace", "path": "/spec/metrics/0/resource/target/averageUtilization", "value": 40}]), code=2)
        self.assertIn("not a resource metric", r.stderr)
        s, cpu = self.now()
        self.assertEqual(cpu, 50)

    def test_reads_pass_through(self):
        r = self.k("get", "hpa", "-A", "-o", "json")
        self.assertEqual(json.loads(r.stdout)["items"][0]["metadata"]["name"], "php-apache")

    def test_the_controllers_own_reset_through_the_plug(self):
        self.state.write_text(json.dumps(cluster(target=35, records={ANN: "50"})))
        d = Path(self.tmp.name)
        r = subprocess.run([sys.executable, "-m", "omni_controller.controller", "--restore-only", "--kubectl", str(PLUG),
                            "--no-api-proxy", "--mode", "nodepool", "--audit", str(d / "audit.jsonl"), "--kill-file", str(d / "kill")],
                           cwd=ROOT, env=dict(self.env, OMNI_REGISTRY=str(d / "registry")), capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        s, cpu = self.now()
        self.assertEqual((s["so"]["spec"]["triggers"][0]["metadata"]["value"], cpu), ("50", 50))
        self.assertFalse([k for k in (s["hpa"]["metadata"]["annotations"] or {}) if k.startswith("omnicompass.io/")])
        self.assertFalse([k for k in (s["so"]["metadata"]["annotations"] or {}) if k.startswith("omnicompass.io/")])


if __name__ == "__main__":
    unittest.main()
