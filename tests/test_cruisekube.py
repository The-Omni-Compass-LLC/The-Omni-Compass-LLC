# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The CruiseKube test's wiring (docs/CRUISEKUBE_PREREGISTRATION.md): every download pinned, CruiseKube's usage reports off,
the set beside KEDA's HTTP add-on alone, the CPU limit left to CruiseKube, and a run without an applied change invalid."""
import hashlib
import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ADDON = ROOT / "scripts/kind_addons_cruisekube.sh"
BENCH = ROOT / "scripts/kind_bench.sh"


class Wiring(unittest.TestCase):
    def test_scripts_parse(self):
        for f in (ADDON, BENCH):
            subprocess.run(["bash", "-n", str(f)], check=True)

    def test_every_download_is_pinned(self):
        s = ADDON.read_text()
        fetched = re.findall(r'^\s*fetch "[^"]+" "[^"]+" "\$(\w+)"', s, re.M)
        self.assertEqual(len(fetched), 5)                          # kube-state-metrics' five standard files
        for var in fetched:
            self.assertRegex(s, rf'(?m)^{var}="\$\{{{var}:-[0-9a-f]{{64}}\}}"$')
        # the chart: a counted run needs its SHA-256; only a shakedown run may record one instead
        self.assertIn('CK_VERSION="${CK_VERSION:-0.3.4}"', s)
        self.assertIn('elif [ "${CRUISEKUBE_SHAKEDOWN:-}" != 1 ]; then', s)
        self.assertIn('[ "$got" = "$CK_CHART_SHA256" ] || {', s)

    def test_images_pinned_to_a_release(self):
        docs = [d for d in yaml.safe_load_all((ROOT / "deploy/kind/cruisekube-metrics.yaml").read_text()) if d]
        images = [c["image"] for d in docs if d.get("kind") in ("Deployment", "DaemonSet")
                  for c in d["spec"]["template"]["spec"]["containers"]]
        self.assertEqual(sorted(images), ["quay.io/prometheus/node-exporter:v1.12.0", "quay.io/prometheus/prometheus:v3.10.0"])
        prom = next(d for d in docs if d.get("kind") == "Deployment" and d["metadata"]["name"] == "prometheus")
        self.assertEqual(prom["spec"]["template"]["spec"]["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})

    def test_values_as_shipped_but_for_the_run(self):
        v = yaml.safe_load((ROOT / "deploy/kind/cruisekube-values.yaml").read_text())
        c = v["cruisekubeController"]
        self.assertIs(c["usageTelemetry"]["enabled"], False)       # no usage reports to its maker
        self.assertIs(c["admin"]["enabled"], False)
        self.assertIs(c["serviceMonitor"]["enabled"], False)
        self.assertIs(v["cruisekubeWebhook"]["serviceMonitor"]["enabled"], False)
        self.assertIs(v["cruisekubeFrontend"]["enabled"], False)
        self.assertEqual(c["env"], {"CRUISEKUBE_DEPENDENCIES_INCLUSTER_PROMETHEUSURL": "http://prometheus.cruisekube-metrics.svc:9090"})
        self.assertEqual(v["postgresql"]["primary"]["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})

    def test_beside_keda_http_alone_and_the_limit_left_to_cruisekube(self):
        s = BENCH.read_text()
        self.assertIn('[ -z "$CRUISEKUBE" ] || { [ "$ADDONS" = keda ] && [ "${ADDONS_PROFILE:-both}" = http ]; }', s)
        self.assertIn('CAP_ARGS="--cap-deployments default/php-apache"; [ -z "$CRUISEKUBE" ] || CAP_ARGS=""', s)
        self.assertNotIn("--cap-deployments default/php-apache --", s.replace('CAP_ARGS="--cap-deployments default/php-apache"', ""))
        self.assertIn("{.spec.template.spec.containers[0].resources.limits.cpu}", s)
        for phase in ("install", "learn", "end"):
            self.assertIn(f"PHASE={phase} ", s[s.index('if [ -n "$CRUISEKUBE" ]'):])

    def test_add_ons_on_the_control_plane(self):
        s = ADDON.read_text()
        self.assertIn('select($terminating or .metadata.deletionTimestamp == null)', s)   # a replaced pod may finish shutting down
        self.assertIn('(.metadata.labels["app.kubernetes.io/name"] // "") == "kube-state-metrics"', s)
        self.assertIn('[ -z "$off" ] || { echo "add-on pods on a measured worker: $off"; exit 1; }', s)
        self.assertEqual(s.count('api "/audit-events/$WORKLOAD_ID?minutes=600"'), 2)       # the whole run, not the last hour

    def test_no_change_applied_is_invalid(self):
        s = ADDON.read_text()
        self.assertIn('[ -n "$applied" ] || { echo "INVALID RUN: CruiseKube made no change', s)
        self.assertIn('test("RECOMMENDATION_APPLIED|WEBHOOK_MUTATION")', s)
        self.assertIn('LEARN="${CRUISEKUBE_LEARN:-4500}"', s)          # longer than CruiseKube's hour
        self.assertIn(">> \"$OUT_DIR/addons.txt\"", s)                  # KEDA's lines kept

    def test_workflow(self):
        w = yaml.safe_load((ROOT / ".github/workflows/kind-cruisekube.yml").read_text())
        step = next(s for s in w["jobs"]["run"]["steps"] if s.get("run") == "bash scripts/kind_paired.sh")
        env = step["env"]
        self.assertEqual((env["ADDONS"], env["ADDONS_PROFILE"], env["CRUISEKUBE"], env["ARMS"]),
                         ("keda", "http", "1", "native compass"))
        commit = next(s for s in w["jobs"]["aggregate"]["steps"] if "saved on the branch raw" in s.get("name", ""))
        self.assertIn("github.event.inputs.shakedown != 'yes'", commit["if"])   # a shakedown run is never counted


STANDIN = ROOT / "tests" / "standin_cruisekube"


def standin_env(t):
    """The stand-ins first on the path (tests/standin_cruisekube: kubectl, helm, curl, sleep), every pin matched to the
    stand-in downloads ("standin <name>"), a made-up powercap tree for the meter."""
    env = dict(os.environ, PATH=f"{STANDIN}:{os.environ['PATH']}", STANDIN_CALLS=str(t / "calls.jsonl"),
               STANDIN_STATE=str(t / "state.json"), RUNNER_TEMP=str(t),
               CK_CHART_SHA256=hashlib.sha256(b"a made-up chart\n").hexdigest())
    sha = lambda name, extra="": hashlib.sha256(f"standin {name}\n{extra}".encode()).hexdigest()
    for var, f in (("KSM_SHA256_CRB", "cluster-role-binding.yaml"), ("KSM_SHA256_CR", "cluster-role.yaml"),
                   ("KSM_SHA256_DEPLOY", "deployment.yaml"), ("KSM_SHA256_SA", "service-account.yaml"),
                   ("KSM_SHA256_SVC", "service.yaml"), ("KEPLER_SHA256_NAMESPACE", "namespace.yaml"),
                   ("KEPLER_SHA256_RBAC", "rbac.yaml"), ("KEPLER_SHA256_CONFIGMAP", "configmap.yaml"),
                   ("KEPLER_SHA256_SERVICE", "service.yaml")):
        env[var] = sha(f)
    env["KEPLER_SHA256_DAEMONSET"] = sha("daemonset.yaml", "        image: <KEPLER_IMAGE>\n        imagePullPolicy: Always\n")
    z = t / "powercap" / "intel-rapl:0"
    z.mkdir(parents=True)
    (z / "name").write_text("package-0\n"); (z / "energy_uj").write_text("12345\n"); (z / "max_energy_range_uj").write_text("262143328850\n")
    env["RAPL_ROOT"] = str(t / "powercap")
    return env


def calls(t):
    return [json.loads(x) for x in (t / "calls.jsonl").read_text().splitlines()]


class DryRun(unittest.TestCase):
    """Each add-on script run end to end against the stand-ins: every command line, every jq filter and every branch a
    real run takes, with no cluster and no network (both scripts' first GitHub trials stopped on lines a dry run catches)."""

    def phase(self, script, out, env, phase, **extra):
        r = subprocess.run(["bash", str(script)], cwd=ROOT, env=dict(env, OUT_DIR=str(out), PHASE=phase, **extra),
                           capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, f"PHASE={phase}\n{r.stdout}\n{r.stderr}")
        return r

    def test_cruisekube_install_learn_end(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t); out = t / "bench-compass-1"; out.mkdir()
            env = standin_env(t)
            self.phase(ADDON, out, env, "install")
            self.phase(ADDON, out, env, "learn", CRUISEKUBE_LEARN="0", LOAD_STEPS="1 2 3 1 2 1")
            self.phase(ADDON, out, env, "end")
            addons = (out / "addons.txt").read_text()
            for want in ("cruisekube=0.3.4", "cruise mode on for Deployment:default:php-apache", "applied a change to the service"):
                self.assertIn(want, addons)
            pins = (out / "cruisekube_pins.txt").read_text()
            self.assertIn("cruisekube_chart=0.3.4 sha256=" + env["CK_CHART_SHA256"], pins)
            self.assertIn("@sha256:", pins)                                     # every image with its digest
            c = calls(t)
            self.assertGreaterEqual(sum(1 for x in c if x[:4] == ["kubectl", "get", "pods", "-A"]), 3)   # waited for the replaced pods
            install = next(x for x in c if x[:2] == ["helm", "install"])
            self.assertIn("deploy/kind/cruisekube-values.yaml", install)
            post = next(x for x in c if x[0] == "curl" and any(a.endswith("/overrides") for a in x))
            self.assertEqual(json.loads(post[post.index("-d") + 1]), {"enabled": True})
            self.assertTrue(any(x[0] == "curl" and any("audit-events" in a and "minutes=600" in a for a in x) for x in c))
            for f in ("cruisekube_workloads.json", "cruisekube_audit_start.json", "cruisekube_resources_start.json",
                      "cruisekube_audit_end.json", "cruisekube_preflight.json", "cruisekube_settings.json"):
                json.loads((out / f).read_text())

    def test_a_pod_still_serving_on_a_worker_fails(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t); out = t / "bench-native-1"; out.mkdir()
            env = standin_env(t)
            # the replaced controller never finishes: the stand-in shows it on its worker in every list, not shutting down
            (t / "state.json").write_text(json.dumps({"lists": 0, "stuck": True}))
            script = (STANDIN / "kubectl").read_text()
            stuck = t / "standin"; stuck.mkdir()
            (stuck / "kubectl").write_text(script.replace('if st["lists"] == 1:', 'if st["lists"] == 1 or st.get("stuck"):')
                                           .replace('terminating=True),\n                  pod("cruisekube-system", "cruisekube-webhook-old"',
                                                    'terminating=False),\n                  pod("cruisekube-system", "cruisekube-webhook-old"'))
            (stuck / "kubectl").chmod(0o755)
            env["PATH"] = f"{stuck}:{env['PATH']}"
            r = subprocess.run(["bash", str(ADDON)], cwd=ROOT, env=dict(env, OUT_DIR=str(out), PHASE="install"),
                               capture_output=True, text=True, timeout=120)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("add-on pods on a measured worker: cruisekube-system/cruisekube-controller-old", r.stdout)

    def test_kepler_install_read_end(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t); out = t / "bench-native-1"; out.mkdir()
            env = standin_env(t)
            kepler = ROOT / "scripts/kind_addons_kepler.sh"
            self.phase(kepler, out, env, "install")
            self.phase(kepler, out, env, "read", TAG="start")
            self.phase(kepler, out, env, "read", TAG="end")
            self.phase(kepler, out, env, "end")
            self.assertIn("kepler=v0.11.4 image=quay.io/sustainable_computing_io/kepler:v0.11.4", (out / "addons.txt").read_text())
            for tag in ("start", "end"):
                p = out / f"kepler_{tag}_omni-bench-control-plane.prom"
                self.assertIn("kepler_node_cpu_joules_total", p.read_text())
                self.assertNotIn("go_goroutines", p.read_text())               # Kepler's own lines only
            (out / "window_start.txt").write_text("0\n"); (out / "window_end.txt").write_text("900\n")
            from tools import live_reps
            g = live_reps.meter(out)
            self.assertGreater(g["energy, Kepler's reading of the machine's meter (Wh)"], 0)

    def test_kepler_refuses_a_machine_without_a_meter(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t); out = t / "bench-native-1"; out.mkdir()
            env = dict(standin_env(t), RAPL_ROOT=str(t / "nothing"))
            r = subprocess.run(["bash", str(ROOT / "scripts/kind_addons_kepler.sh")], cwd=ROOT,
                               env=dict(env, OUT_DIR=str(out), PHASE="install"), capture_output=True, text=True, timeout=60)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("no processor meter on this machine", r.stdout)
            self.assertFalse(any(x[0] == "kubectl" for x in calls(t)) if (t / "calls.jsonl").exists() else False)


if __name__ == "__main__":
    unittest.main()
