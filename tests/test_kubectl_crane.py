# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Crane test's plug (scripts/kubectl_crane.py) against a stand-in cluster where Crane owns the HPA and undoes any write
to it (tests/standin_crane/kubectl): the engine's own writes land on the EHPA and show on the HPA; the reset hands every
setting back and leaves no record on either; a write the plug cannot carry exactly is refused; reads pass through
untouched; and the controller's own reset runs through it unchanged."""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUG = ROOT / "scripts" / "kubectl_crane.py"
STANDIN = ROOT / "tests" / "standin_crane" / "kubectl"
ANN = "omnicompass.io/original-target-utilization"
RNG = "omnicompass.io/original-replica-range"


def cluster(target=50, records=None):
    ehpa = {"apiVersion": "autoscaling.crane.io/v1alpha1", "kind": "EffectiveHorizontalPodAutoscaler",
            "metadata": {"name": "php-apache", "namespace": "default", "annotations": dict(records or {})},
            "spec": {"minReplicas": 1, "maxReplicas": 10, "scaleStrategy": "Auto",
                     "scaleTargetRef": {"apiVersion": "apps/v1", "kind": "Deployment", "name": "php-apache"},
                     "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization",
                                                                                             "averageUtilization": target}}}]}}
    hpa = {"apiVersion": "autoscaling/v2", "kind": "HorizontalPodAutoscaler",
           "metadata": {"name": "ehpa-php-apache", "namespace": "default", "annotations": dict(records or {}) or None,
                        "ownerReferences": [{"apiVersion": "autoscaling.crane.io/v1alpha1",
                                             "kind": "EffectiveHorizontalPodAutoscaler", "name": "php-apache"}]},
           "spec": {"minReplicas": 1, "maxReplicas": 10, "scaleTargetRef": {"kind": "Deployment", "name": "php-apache"},
                    "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization",
                                                                                            "averageUtilization": target}}},
                                {"type": "External", "external": {"metric": {"name": "crane_pod_cpu_usage"},
                                                                  "target": {"type": "AverageValue", "averageValue": "250m"}}}]},
           "status": {"currentReplicas": 1, "desiredReplicas": 1}}
    return {"ehpa": ehpa, "hpa": hpa}


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
        return ["patch", "hpa", "ehpa-php-apache", "-n", "default", "--type=json", "-p",
                json.dumps([{"op": "replace", "path": "/spec/metrics/0/resource/target/averageUtilization", "value": v}])]

    def test_target_reaches_crane_and_the_reset_leaves_nothing(self):
        self.k("annotate", "hpa", "ehpa-php-apache", "-n", "default", "--overwrite", f"{ANN}=50")
        self.k(*self.target(35))
        s, cpu = self.now()
        self.assertEqual(s["ehpa"]["spec"]["metrics"][0]["resource"]["target"]["averageUtilization"], 35)
        self.assertEqual(cpu, 35)
        self.assertEqual(s["hpa"]["metadata"]["annotations"][ANN], "50")    # survives Crane's rebuild: it is on the EHPA
        self.k(*self.target(50))
        self.k("annotate", "hpa", "ehpa-php-apache", "-n", "default", f"{ANN}-")
        s, cpu = self.now()
        self.assertEqual((s["ehpa"]["spec"]["metrics"][0]["resource"]["target"]["averageUtilization"], cpu), (50, 50))
        self.assertNotIn(ANN, s["hpa"]["metadata"]["annotations"] or {})
        self.assertNotIn(ANN, s["ehpa"]["metadata"]["annotations"] or {})
        recs = [json.loads(l) for l in self.log.read_text().splitlines()]
        self.assertTrue(recs and all(r["hpa_shows"] for r in recs))

    def test_replica_range(self):
        self.k("annotate", "hpa", "ehpa-php-apache", "-n", "default", "--overwrite", f"{RNG}=1,10")
        self.k("patch", "hpa", "ehpa-php-apache", "-n", "default", "--type=merge", "-p", json.dumps({"spec": {"minReplicas": 3}}))
        s, _ = self.now()
        self.assertEqual((s["ehpa"]["spec"]["minReplicas"], s["hpa"]["spec"]["minReplicas"]), (3, 3))
        self.k("patch", "hpa", "ehpa-php-apache", "-n", "default", "--type=merge",
               "-p", json.dumps({"spec": {"minReplicas": 1, "maxReplicas": 10}}))
        self.k("annotate", "hpa", "ehpa-php-apache", "-n", "default", f"{RNG}-")
        s, _ = self.now()
        self.assertEqual((s["hpa"]["spec"]["minReplicas"], s["hpa"]["spec"]["maxReplicas"]), (1, 10))
        self.assertNotIn(RNG, s["hpa"]["metadata"]["annotations"] or {})

    def test_refuses_what_it_cannot_carry_exactly(self):
        r = self.k("patch", "hpa", "ehpa-php-apache", "-n", "default", "--type=merge", "-p", json.dumps({"spec": {"behavior": {}}}), code=2)
        self.assertIn("refused", r.stderr)
        r = self.k("patch", "hpa", "ehpa-php-apache", "-n", "default", "--type=json", "-p",
                   json.dumps([{"op": "replace", "path": "/spec/metrics/1/resource/target/averageUtilization", "value": 40}]), code=2)
        self.assertIn("not a resource metric", r.stderr)                    # Crane's forecast metric is not the engine's
        s, cpu = self.now()
        self.assertEqual(cpu, 50)

    def test_reads_pass_through(self):
        r = self.k("get", "hpa", "-A", "-o", "json")
        self.assertEqual(json.loads(r.stdout)["items"][0]["metadata"]["name"], "ehpa-php-apache")

    def test_the_controllers_own_reset_through_the_plug(self):
        self.state.write_text(json.dumps(cluster(target=35, records={ANN: "50"})))
        d = Path(self.tmp.name)
        r = subprocess.run([sys.executable, "-m", "omni_controller.controller", "--restore-only", "--kubectl", str(PLUG),
                            "--no-api-proxy", "--mode", "nodepool", "--audit", str(d / "audit.jsonl"), "--kill-file", str(d / "kill")],
                           cwd=ROOT, env=dict(self.env, OMNI_REGISTRY=str(d / "registry")), capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        s, cpu = self.now()
        self.assertEqual((s["ehpa"]["spec"]["metrics"][0]["resource"]["target"]["averageUtilization"], cpu), (50, 50))
        self.assertFalse([k for k in (s["hpa"]["metadata"]["annotations"] or {}) if k.startswith("omnicompass.io/")])
        self.assertFalse([k for k in (s["ehpa"]["metadata"]["annotations"] or {}) if k.startswith("omnicompass.io/")])


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
