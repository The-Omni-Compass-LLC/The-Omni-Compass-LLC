# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The mission-control wall (deploy/monitoring/, docs/MISSION_CONTROL.md): Prometheus, Grafana, node_exporter, Alertmanager, the
governor's exporter and the alert bridge in one stack, every image pinned, no password written, the two boards loaded, and the
alarms wired to the control panel's operator buttons only (tools/omni_alert_bridge.py), writing what they would press until told."""
import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import yaml

from tools import omni_alert_bridge as B

ROOT = Path(__file__).resolve().parents[1]
MON = ROOT / "deploy" / "monitoring"


class Stack(unittest.TestCase):
    def test_every_image_pinned_and_no_password_written(self):
        d = yaml.safe_load((MON / "docker-compose.yml").read_text())
        self.assertEqual(sorted(d["services"]), ["alertmanager", "grafana", "node-exporter", "omni-bridge", "omni-exporter", "prometheus"])
        for name, s in d["services"].items():
            with self.subTest(service=name):
                img = s["image"]
                self.assertRegex(img, r":v?\d+\.\d+\.\d+(-slim)?$")
                self.assertNotIn("latest", img)
        env = d["services"]["grafana"]["environment"]["GF_SECURITY_ADMIN_PASSWORD"]
        self.assertTrue(env.startswith("${GRAFANA_ADMIN_PASSWORD:?"), env)        # read from .env, refused when unset
        self.assertIn(".env", (MON / ".gitignore").read_text())
        self.assertIn("targets/bridge.token", (MON / ".gitignore").read_text())

    def test_prometheus_reads_the_governor_the_metal_the_panel_and_the_bridge(self):
        p = yaml.safe_load((MON / "prometheus.yml").read_text())
        jobs = {j["job_name"] for j in p["scrape_configs"]}
        self.assertTrue({"omni-exporter", "omni-control", "bare-metal", "omni-bridge"} <= jobs)
        self.assertEqual(p["rule_files"], ["/etc/prometheus/rules/omni-compass-rules.yaml"])
        self.assertEqual(p["alerting"]["alertmanagers"][0]["static_configs"][0]["targets"], ["alertmanager:9093"])
        for f in ("omni.yml", "nodes.yml", "control.yml"):
            yaml.safe_load((MON / "targets" / f).read_text())
        first = yaml.safe_load((MON / "targets" / "omni.yml").read_text())[0]
        self.assertEqual(first["labels"]["route"], "onsite")                         # the wall's knobs filter by route and provider

    def test_grafana_loads_the_boards_and_the_source_by_itself(self):
        ds = yaml.safe_load((MON / "grafana/provisioning/datasources/prometheus.yml").read_text())
        self.assertEqual(ds["datasources"][0]["url"], "http://prometheus:9090")
        dash = yaml.safe_load((MON / "grafana/provisioning/dashboards/omni.yml").read_text())
        self.assertEqual(dash["providers"][0]["options"]["path"], "/var/lib/grafana/dashboards/omni")
        for b in ("omni-compass-wall.json", "omni-compass.json"):
            self.assertTrue((ROOT / "deploy" / "grafana" / b).exists())
        am = yaml.safe_load((MON / "alertmanager.yml").read_text())
        self.assertEqual(am["receivers"][0]["webhook_configs"][0]["url"], "http://omni-bridge:9466/alerts")


class Bridge(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.presses = []
        presses = self.presses

        class Panel(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                presses.append((self.path, body, self.headers.get("Authorization")))
                out = json.dumps({"ok": True}).encode()
                self.send_response(200); self.send_header("Content-Length", str(len(out))); self.end_headers(); self.wfile.write(out)
        self.panel = ThreadingHTTPServer(("127.0.0.1", 0), Panel)
        threading.Thread(target=self.panel.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.panel.server_address[1]}"

    def tearDown(self):
        self.panel.shutdown()

    def alert(self, name, status="firing", fp="f1", start="2026-10-25T00:00:00Z"):
        return {"alerts": [{"status": status, "labels": {"alertname": name}, "fingerprint": fp, "startsAt": start}]}

    def test_the_shipped_list_names_only_operator_buttons(self):
        acts = B.load_actions(MON / "actions.json")
        self.assertTrue(acts)
        self.assertTrue(all(a["button"] in ("factory", "reset", "mode", "dial") for a in acts.values()))

    def test_a_list_naming_the_kill_switch_is_refused_whole(self):
        for b in ("kill", "arm"):
            p = self.d / f"{b}.json"; p.write_text(json.dumps({"actions": {"X": {"button": b}}}))
            with self.subTest(button=b), self.assertRaises(SystemExit):
                B.load_actions(p)

    def test_it_writes_and_never_presses_until_told(self):
        br = B.Bridge({"OmniGovernorStale": {"button": "reset", "body": {}}}, self.url, "tok", press=False, log=self.d / "b.jsonl")
        out = br.handle(self.alert("OmniGovernorStale"))
        self.assertEqual(out[0]["outcome"], "written, not pressed")
        self.assertEqual(self.presses, [])
        self.assertIn("written, not pressed", (self.d / "b.jsonl").read_text())

    def test_it_presses_once_a_firing_with_its_reason_and_never_on_a_resolve(self):
        br = B.Bridge({"OmniWriteErrors": {"button": "mode", "body": {"mode": "watch"}}}, self.url, "tok", press=True, log=None)
        self.assertEqual(br.handle(self.alert("OmniWriteErrors"))[0]["outcome"], "pressed")
        self.assertEqual(br.handle(self.alert("OmniWriteErrors"))[0]["outcome"], "no action")          # the same firing repeated
        self.assertEqual(br.handle(self.alert("OmniWriteErrors", status="resolved"))[0]["outcome"], "no action")
        self.assertEqual(br.handle(self.alert("OmniSenseBlind"))[0]["outcome"], "no action")            # no action listed
        self.assertEqual(len(self.presses), 1)
        path, body, auth = self.presses[0]
        self.assertEqual((path, body["mode"], auth), ("/v1/mode", "watch", "Bearer tok"))
        self.assertIn("alert OmniWriteErrors firing", body["reason"])
        self.assertIn('omni_bridge_decisions_total{outcome="pressed"} 1', br.metrics())


class WallKnobs(unittest.TestCase):
    """The monitor wall in Grafana carries knobs and buttons (the founder's order of 24 October): route, provider, machine,
    the rate window and the control panel; native orange and Omni-Compass blue; the signals' words; the panel's buttons a link."""

    def test_the_knobs_reach_every_series(self):
        d = json.loads((ROOT / "deploy/grafana/omni-compass-wall.json").read_text())
        self.assertEqual([v["name"] for v in d["templating"]["list"]], ["DS_PROMETHEUS", "route", "provider", "instance", "window", "control"])
        exprs = [t["expr"] for p in d["panels"] for t in p.get("targets", [])]
        omni = [e for e in exprs if "omni_" in e]
        self.assertTrue(omni)
        self.assertTrue(all('route=~"$route"' in e for e in omni))
        self.assertFalse(any("[5m]" in e for e in exprs))                    # every five-minute window is the window knob's

    def test_signals_colours_and_buttons(self):
        d = json.loads((ROOT / "deploy/grafana/omni-compass-wall.json").read_text())
        stats = [p for p in d["panels"] if p.get("id", 0) in range(901, 905)]
        self.assertEqual(len(stats), 4)
        words = {m["options"]["result"]["text"] for p in stats for m in p["fieldConfig"]["defaults"]["mappings"]}
        self.assertTrue({"redlining", "steady", "accelerating"} <= words)
        sides = [p for p in d["panels"] if p.get("targets") and p["fieldConfig"]["overrides"]]
        self.assertTrue(any(o["properties"][0]["value"]["fixedColor"] == "#ff8a1f" for p in sides for o in p["fieldConfig"]["overrides"]))
        self.assertTrue(any(l.get("url") == "${control}/" for l in d["links"]))


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
