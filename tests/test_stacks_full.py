# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The stacks with the card fully loaded (docs/GPU_PREREGISTRATION.md, amendment 16, 1 November): the founder's two bills
read the work done inside the same rented time, and at the usual load the card serves every request in both arms, so its
work cannot differ. The full load reaches the card inside the stacks alone, through a value the rented machine's
`env $ENVS` keeps as one word, and the card's workload carries it from its calibration into every arm."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "lambda-gpu.yml"
RUN = ROOT / "scripts" / "gpu_rented_run.sh"


def mode_line(mode: str) -> str:
    return next(ln for ln in WORKFLOW.read_text().splitlines() if ln.strip().startswith(f"1card:{mode})"))


class StacksFull(unittest.TestCase):
    def test_the_mode_is_the_stacks_with_the_card_loaded_and_nothing_else(self):
        full, usual = mode_line("stacks-full"), mode_line("stacks")
        envs = re.search(r'ENVS="([^"]*)"', full).group(1).split()
        self.assertIn("HIL_WORKLOAD_ARGS=--phases=1.3,1.3,1.3", envs)
        self.assertEqual(sorted(e for e in envs if not e.startswith("HIL_WORKLOAD_ARGS=")),
                         sorted(re.search(r'ENVS="([^"]*)"', usual).group(1).split()))   # the stacks' own skips, unchanged
        self.assertNotIn(" WORKLOAD_ARGS=", " " + " ".join(envs))                         # never the smoke's load
        self.assertEqual(re.search(r"BUDGET=([0-9.]+)", full).group(1), re.search(r"BUDGET=([0-9.]+)", usual).group(1))

    def test_every_value_survives_the_rented_machines_word_split(self):
        self.assertIn("env $ENVS bash $SCRIPT", WORKFLOW.read_text())
        for ln in WORKFLOW.read_text().splitlines():
            m = re.search(r'\bENVS="([^"$]*)"', ln)
            if m:
                with self.subTest(line=ln.strip()[:40]):
                    self.assertTrue(all("=" in w for w in m.group(1).split()), "a value with a space would split")

    def test_the_load_reaches_the_stacks_step_alone(self):
        text = RUN.read_text()
        lines = text.splitlines()
        uses = [i for i, ln in enumerate(lines) if "HIL_WORKLOAD_ARGS" in ln and not ln.lstrip().startswith("#")]
        start = next(i for i, ln in enumerate(lines) if 'if [ -z "${SKIP_HIL:-}" ]; then' in ln)   # the stacks step
        hil = next(i for i, ln in enumerate(lines) if "tools/run_hil.py --out" in ln)
        smoke = next(i for i, ln in enumerate(lines) if "PHASE=smoke" in ln)
        self.assertTrue(uses)
        self.assertTrue(all(start < i <= hil for i in uses), (uses, start, hil))
        self.assertLess(smoke, start)

    def test_the_workload_keeps_the_full_load_from_its_calibration(self):
        with tempfile.TemporaryDirectory() as d:
            subprocess.run([sys.executable, str(ROOT / "tools" / "gpu_workload.py"), "calibrate", "--out", d, "--device",
                            "cuda:0", "--sim", "--phases=1.3,1.3,1.3"], check=True, capture_output=True, timeout=120)
            self.assertEqual(json.loads((Path(d) / "calib.json").read_text())["phases"], "1.3,1.3,1.3")

    def test_the_preregistration_declares_it_before_any_run(self):
        text = (ROOT / "docs" / "GPU_PREREGISTRATION.md").read_text()
        self.assertIn("## Amendment 16 (2026-11-01, declared before any run of it)", text)
        self.assertIn("--phases=1.3,1.3,1.3", text)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
