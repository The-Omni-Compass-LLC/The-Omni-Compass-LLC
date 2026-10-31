# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every cloud set runs the whole engine at the max (the founder's order of 31 October: no hard rule; the cloud's tune-down on
the machines alone of 14 October, OMNI_MACHINES_ONLY=1 and the governor's --give-back-only, is struck). The rig wires the same
muscles on every platform, no cloud workflow or queue sets the governor to the machines alone, the model gate's cloud setting
is the max, and the machine lever still asks the cloud for no machine: the cloud's own autoscaler is native's machine
controller and stays in every arm."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

WORKFLOWS = ("aks-metered.yml", "aks-metered-full.yml", "gke-metered.yml", "eks-metered.yml", "byoc-metered.yml")


class CloudAtTheMax(unittest.TestCase):
    def test_no_cloud_workflow_sets_the_governor_to_the_machines_alone(self):
        for w in WORKFLOWS:
            with self.subTest(workflow=w):
                y = (ROOT / ".github" / "workflows" / w).read_text()
                self.assertNotIn("OMNI_MACHINES_ONLY", y)
                self.assertNotIn("give-back-only", y)
                self.assertRegex(y, r"OMNI_DIAL: \$\{\{ github\.event\.inputs\.dial \|\| 'max' \}\}")
                self.assertNotRegex(y, r"github\.event\.inputs\.dial \|\| 'save'")

    def test_the_rig_wires_every_muscle_on_every_platform(self):
        s = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertNotIn("OMNI_MACHINES_ONLY", s)
        self.assertNotIn("$GIVE_BACK_ONLY", s)
        self.assertNotIn('"--give-back-only"', s)
        self.assertIn('OMNI_SENSED="default/php-apache"; OMNI_POWER_CMD="bash scripts/kind_power.sh"', s)
        self.assertIn('--sensed "$OMNI_SENSED"', s)
        self.assertIn('${OMNI_POWER_CMD:+--power-cmd "$OMNI_POWER_CMD"}', s)
        self.assertIn('CAP_ARGS="--cap-deployments default/php-apache"', s)
        p = (ROOT / "scripts" / "aks_paired.sh").read_text()
        self.assertNotIn("OMNI_MACHINES_ONLY", p)
        self.assertNotIn("--machines-only", p)

    def test_every_cloud_queue_runs_the_max_with_the_replica_room_read_live(self):
        queues = sorted((ROOT / "scripts").glob("*_queue.txt"))
        self.assertGreaterEqual(len(queues), 3)
        for q in queues:
            with self.subTest(queue=q.name):
                text = q.read_text()
                entries = [x for x in text.splitlines() if "|" in x and not x.startswith("#")]
                self.assertTrue(entries, q.name)
                for e in entries:
                    self.assertIn("dial=max", e)
                    self.assertNotIn("dial=save", e)
                    self.assertNotIn("replica_ceiling=0", e)   # the operator's cap is no longer pinned by rule

    def test_the_machine_lever_asks_the_cloud_for_no_machine(self):
        # the cloud's own autoscaler is native's machine controller: it stays in every arm and alone adds machines
        s = (ROOT / "scripts" / "kind_nodepool.sh").read_text()
        self.assertIn("(( want > total )) && want=$total", s)
        self.assertNotRegex(s, r"az aks (nodepool )?scale")

    def test_the_cloud_install_file_passes_the_max(self):
        y = (ROOT / "deploy" / "install" / "omni-compass-cloud.yaml").read_text()
        self.assertNotIn("--give-back-only", y)
        self.assertIn('"--dial", "max"', y)
        self.assertNotIn('"none/none"', y)

    def test_the_models_read_the_cloud_at_the_max(self):
        for f in ("tools/model_gate.py", "tools/orchestrators_arm.py", "tools/heartbeat_sweep.py"):
            with self.subTest(file=f):
                src = (ROOT / f).read_text()
                code = "\n".join(l for l in src.splitlines() if not l.lstrip().startswith("#"))
                self.assertNotRegex(code, r'argv\.append\("--give-back-only"\)|"--give-back-only"\]')
                self.assertNotIn('"--sensed", "none/none"', code)
                self.assertNotIn('"--dial", "save"', code)

    def test_the_struck_flag_left_the_governor_with_omni_v24(self):
        # the flag was an engine file's; it left with omni-v24 through the model gate, and the governor now refuses it
        import contextlib, io
        from omni_controller.controller import parser
        a = parser().parse_args(["--mode", "nodepool"])
        self.assertFalse(hasattr(a, "give_back_only"))
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            parser().parse_args(["--mode", "nodepool", "--give-back-only"])


if __name__ == "__main__":
    unittest.main()
