# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The monitor wall's stack (deploy/wall): every image pinned, every port on this machine only, Grafana's password required,
the jobs the governor's alert rules read collected, the rule file and the wall's dashboards the repository's own, every target
file a list, and every omni_ series the wall draws served by the governor's exporter or its control panel."""
import json
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WALL = ROOT / "deploy" / "wall"


class WallStack(unittest.TestCase):
    def setUp(self):
        self.compose = yaml.safe_load((WALL / "docker-compose.yml").read_text(encoding="utf-8"))
        self.prom = yaml.safe_load((WALL / "prometheus.yml").read_text(encoding="utf-8"))

    def test_images_pinned_and_ports_local(self):
        for name, svc in self.compose["services"].items():
            image = svc["image"]
            self.assertRegex(image, r":[0-9v][^:]*$", f"{name}: {image} is not pinned to a version")
            self.assertNotIn(":latest", image, name)
            for port in svc.get("ports", []):
                self.assertTrue(str(port).startswith("127.0.0.1:"), f"{name}: {port} is open beyond this machine")

    def test_grafana_password_required(self):
        env = "\n".join(self.compose["services"]["grafana"]["environment"])
        self.assertRegex(env, r"GF_SECURITY_ADMIN_PASSWORD=\$\{GRAFANA_ADMIN_PASSWORD:\?")
        self.assertNotRegex(env, r"GF_SECURITY_ADMIN_PASSWORD=admin")

    def test_alert_rule_jobs_collected(self):
        jobs = {j["job_name"] for j in self.prom["scrape_configs"]}
        rules = (ROOT / "deploy" / "prometheus" / "omni-compass-rules.yaml").read_text(encoding="utf-8")
        self.assertIn("omni-exporter", jobs)
        self.assertIn("omni-control", jobs)
        for job in re.findall(r"\(job ([a-z-]+)\)", rules):
            self.assertIn(job, jobs, f"the alert rules read job {job}, which the wall does not collect")
        self.assertEqual(self.prom["rule_files"], ["/etc/prometheus/rules/omni-compass-rules.yaml"])
        mounts = self.compose["services"]["prometheus"]["volumes"]
        self.assertIn("../prometheus:/etc/prometheus/rules:ro", mounts)

    def test_target_files_exist_and_are_lists(self):
        for job in self.prom["scrape_configs"]:
            for sd in job.get("file_sd_configs", []):
                for f in sd["files"]:
                    local = WALL / "targets" / Path(f).name
                    self.assertTrue(local.exists(), f"{job['job_name']}: {local} missing")
                    self.assertIsInstance(yaml.safe_load(local.read_text(encoding="utf-8")), list, local)

    def test_wall_dashboards_loaded(self):
        mounts = self.compose["services"]["grafana"]["volumes"]
        self.assertIn("../grafana:/var/lib/grafana/dashboards/omni:ro", mounts)
        for name in ("omni-compass-wall.json", "omni-compass.json"):
            self.assertTrue((ROOT / "deploy" / "grafana" / name).exists(), name)
        prov = yaml.safe_load((WALL / "grafana" / "provisioning" / "dashboards" / "omni.yml").read_text(encoding="utf-8"))
        self.assertEqual(prov["providers"][0]["options"]["path"], "/var/lib/grafana/dashboards/omni")

    def test_every_omni_series_on_the_wall_is_served(self):
        def panels(ps):
            for p in ps:
                yield p
                yield from panels(p.get("panels", []))
        board = json.loads((ROOT / "deploy" / "grafana" / "omni-compass-wall.json").read_text(encoding="utf-8"))
        exprs = " ".join(t.get("expr", "") for p in panels(board["panels"]) for t in p.get("targets", []))
        served = (ROOT / "tools" / "omni_exporter.py").read_text(encoding="utf-8") \
            + (ROOT / "tools" / "omni_control.py").read_text(encoding="utf-8")
        self.assertIn("omni_", exprs)
        for series in sorted(set(re.findall(r"\b(omni_[a-z_]+)", exprs))):
            base = re.sub(r"_(sum|count|bucket)$", "", series)
            self.assertIn(base, served, f"the wall draws {series}, which neither the exporter nor the panel serves")

    def test_exporter_mounted_read_only(self):
        vols = self.compose["services"]["omni-exporter"]["volumes"]
        self.assertTrue(all(v.endswith(":ro") for v in vols), vols)


if __name__ == "__main__":
    unittest.main()
