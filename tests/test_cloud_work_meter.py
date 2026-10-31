# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The cloud judged by its work per dollar (the founder's words of 31 October, evening: "We're pushing 1% more bill, but we're
getting ~12% more work ... anybody will pay 1% more for 10% more product"). A cloud set reads the work and the bill from the same
run: the work meter's answers inside the line (LOADGEN=meter, deploy/kind/loadgen-meter.yaml) and the cloud's machines priced at
list, and their quotient, the work per dollar, read as work bought with each unit of a resource (a rise GAIN, a fall power
given). The meter runs on every cloud as on kind; every cloud workflow takes the load and the meter's rates as inputs and names
a meter set by its rates, so the conductor never reads it back as a steady or a burst set."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import tools.live_reps as LR  # noqa: E402
import tools.confirm_abc as CA  # noqa: E402
from tools.readings import WORK_PER, word  # noqa: E402


def conductor():
    spec = importlib.util.spec_from_file_location("dispatch_grid", ROOT / "scripts" / "dispatch_grid.py")
    g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
    return g


class CloudWorkMeter(unittest.TestCase):
    def test_the_rig_runs_the_meter_in_a_cloud(self):
        text = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertIn('{ [ "$PLATFORM" = kind ] || [ "$PLATFORM" = aks ]; }', text)
        self.assertNotIn('echo "LOADGEN=meter runs on kind, alone', text)

    def test_every_cloud_workflow_takes_the_load_and_the_rates(self):
        for wf in ("aks-metered.yml", "gke-metered.yml", "eks-metered.yml", "byoc-metered.yml"):
            y = (ROOT / ".github" / "workflows" / wf).read_text()
            self.assertIn("      loadgen: {", y, wf)
            self.assertIn("      rate_steps: {", y, wf)
            self.assertIn("LOADGEN: ${{ github.event.inputs.loadgen || 'open' }}", y, wf)
            self.assertIn("RATE_STEPS: ${{ github.event.inputs.rate_steps || '' }}", y, wf)
            self.assertIn("format('work meter {0}', github.event.inputs.rate_steps)", y, wf)

    def test_a_meter_set_is_named_by_its_rates(self):
        g = conductor()
        self.assertEqual(g.azure_title({"loadgen": "meter", "rate_steps": "10 20 40", "dial": "max"}),
                         "aks-metered work meter 10 20 40 dial max eastus Standard_D2s_v4")
        self.assertEqual(g.azure_title({"dial": "max"}), "aks-metered steady dial max eastus Standard_D2s_v4")

    def test_a_tuning_case_runs_once(self):
        # runs=A: the conductor starts its run A only, and never passes the key to the workflow as an input
        g = conductor()
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("switch=on\ntuning|loadgen=meter;rate_steps=10 20;reps=1;runs=A\nsteady|tier=standard;dial=max\n")
        q = g.azure_queue(f.name)
        self.assertEqual([(r, n) for r, n, _, _ in q], [("A", "tuning"), ("A", "steady"), ("B", "steady"), ("C", "steady")])
        self.assertTrue(all("runs" not in kv for _, _, _, kv in q))
        own = g.azure_queue(g.AZURE_QUEUE)                       # the repository's own queue: its tuning case first, once
        self.assertEqual(own[0][1], "work meter tuning case")
        self.assertEqual([n for r, n, _, _ in own].count("work meter tuning case"), 1)
        self.assertEqual(own[0][3].get("loadgen"), "meter")

    def test_the_receipt_reads_the_work_beside_the_bill(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t) / "bench-compass-1"; d.mkdir()
            (d / "window_start.txt").write_text("1000\n"); (d / "window_end.txt").write_text("1900\n")
            # two machines for the 900 s window at $0.096 an hour: $0.048
            (d / "billed_nodes.csv").write_text("epoch_s,machines\n1000,2\n1450,2\n1900,2\n")
            (d / "work_meter.json").write_text(json.dumps({"final": True, "total": {"sent": 9500, "in_time": 9000, "late": 400,
                                                                                    "failed": 100, "not_sent": 0}}) + "\n")
            g = LR.bill(d)
            self.assertAlmostEqual(g["compute bill at list price ($)"], 0.048, places=6)
            self.assertAlmostEqual(g[LR.WORK], 10.0, places=6)                 # 9,000 answers inside the line over 900 s
            self.assertAlmostEqual(g[LR.WORK_DOLLAR], 9000 / 0.048, places=3)

    def test_an_arm_without_the_meter_reads_no_work(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t) / "bench-native-1"; d.mkdir()
            (d / "window_start.txt").write_text("1000\n"); (d / "window_end.txt").write_text("1900\n")
            (d / "billed_nodes.csv").write_text("epoch_s,machines\n1000,2\n1900,2\n")
            g = LR.bill(d)
            self.assertNotIn(LR.WORK, g)
            self.assertNotIn(LR.WORK_DOLLAR, g)

    def test_work_per_dollar_reads_as_work_bought_with_a_resource(self):
        self.assertEqual(CA.aim_of_row(LR.WORK_DOLLAR), WORK_PER)
        self.assertEqual(word(False, WORK_PER), "GAIN")           # more work for each dollar
        self.assertEqual(word(True, WORK_PER), "power given")     # money spent for something other than work, never a LOSS
        self.assertIn(LR.WORK, CA.AIM_HIGHER)                     # the work itself aims higher, as in the capacity test
        self.assertTrue(LR.sig_word(LR.WORK_DOLLAR, 5.0).endswith("GAIN"))
        self.assertTrue(LR.sig_word(LR.WORK, -1.0).endswith("LOSS"))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
