# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The CPU power harness (tools/run_cpu_power.py) on a modelled machine: the decision rule (a slow service raises the ceiling
by notches, calm gives one back after the dwell, the wall puts the top on at once, the cover holds), the grid of notches, the
plug on the kernel's files (the snapshot once, write and read back, another writer stops Omni, restore), the energy counter's
wrap-around, the probe, the hand-back from a snapshot file, and one short paired run end to end: the same requests in both
arms, the brain's verdict allowing notches one trial at a time, energy lower on the modelled machine, the ceiling handed
back and read back."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_cpu_power as R  # noqa: E402

TOP, FLOOR, NOTCH = 2_800_000, 1_400_000, 140_000


class Rules(unittest.TestCase):
    def test_decide(self):
        self.assertEqual(R.decide(0.96, 0.0, 2_000_000, TOP, FLOOR, NOTCH, 10)[0], TOP, "past the wall: the top at once")
        self.assertIn("fail up", R.decide(0.96, 0.0, 2_000_000, TOP, FLOOR, NOTCH, 10)[1])
        self.assertEqual(R.decide(0.5, 0.35, 2_000_000, TOP, FLOOR, NOTCH, 10)[0], 2_000_000 + 4 * NOTCH, "slow: ceil(force / 0.1) notches up")
        self.assertEqual(R.decide(0.5, 1.0, 2_700_000, TOP, FLOOR, NOTCH, 10)[0], TOP, "the cover holds on the way up")
        self.assertEqual(R.decide(0.2, -0.5, 2_000_000, TOP, FLOOR, NOTCH, 10)[0], 2_000_000 - NOTCH, "calm: a notch given back")
        self.assertEqual(R.decide(0.2, -0.5, 2_000_000, TOP, FLOOR, NOTCH, 2)[0], 2_000_000, "not within the dwell")
        self.assertEqual(R.decide(0.2, -0.5, FLOOR, TOP, FLOOR, NOTCH, 10)[0], FLOOR, "never under the floor")
        self.assertEqual(R.decide(0.4, 0.02, 2_000_000, TOP, FLOOR, NOTCH, 10)[0], 2_000_000, "inside the cushion nothing moves")

    def test_grid(self):
        self.assertEqual(R.grid(2_800_000, 800_000), (140_000, 1_400_000))
        notch, floor = R.grid(3_000_000, 2_000_000)
        self.assertEqual(notch, 150_000)
        self.assertEqual(floor, 2_100_000, "the floor sits on the notch grid and never under the processor's own minimum")

    def test_cost_objectives(self):
        from tools.knob_verdict import sample_cost
        self.assertAlmostEqual(sample_cost("resource", 100.0, 0.005, 30.0, None), 30.0 * 0.005 / 100.0)
        self.assertAlmostEqual(sample_cost("per-work", 100.0, 0.005, 30.0, None), 30.0 / 100.0)
        self.assertAlmostEqual(sample_cost("service", 100.0, 0.005, 30.0, None), 0.005 / 100.0)
        self.assertIsNone(sample_cost("resource", 0, 0.005, 30.0, None))


class PlantFiles(unittest.TestCase):
    def test_snapshot_write_restore_foreign(self):
        d = tempfile.mkdtemp(); p = R.SimPlant(d)
        self.assertEqual(p.attach(), TOP)
        self.assertEqual(p.write(2_660_000), 2_660_000)
        self.assertEqual(p.lever(), 2_660_000)
        self.assertEqual(p.ceiling_actual(), 2_660_000)
        (Path(d) / "sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq").write_text("2000000\n")   # someone else moved one core's ceiling
        with self.assertRaises(RuntimeError):
            p.lever()
        self.assertTrue(p.restore())
        self.assertEqual(p.ceiling_actual(), TOP, "restored to the snapshot and read back")
        p.write(2_000_000); p.attach()
        self.assertEqual(p.snapshot["cpu0"]["max_khz"], TOP, "the snapshot is taken once, as found")
        self.assertTrue(p.restore())

    def test_energy_wrap(self):
        d = tempfile.mkdtemp(); p = R.SimPlant(d); pk = p.packages[0]
        self.assertEqual(p.energy_j(), 0.0)
        (pk / "energy_uj").write_text("5000000\n")
        self.assertAlmostEqual(p.energy_j(), 5.0)
        rng = 262143328850
        (pk / "energy_uj").write_text("1000000\n")                        # the counter wrapped
        self.assertAlmostEqual(p.energy_j(), 5.0 + (1_000_000 - 5_000_000 + rng + 1) / 1e6, places=3)

    def test_probe(self):
        out = []
        self.assertEqual(R.probe(R.SimPlant(tempfile.mkdtemp()), None, out.append), 0)
        self.assertTrue(any("can run" in s for s in out))
        out = []
        self.assertEqual(R.probe(R.Plant(tempfile.mkdtemp()), None, out.append), 2, "a machine without cpufreq or the meter cannot run it")
        self.assertTrue(any("CANNOT RUN HERE" in s for s in out))

    def test_restore_from_file(self):
        d = tempfile.mkdtemp(); p = R.SimPlant(d); p.attach(); p.write(2_000_000)
        snap = Path(d) / "snapshot.json"; snap.write_text(json.dumps({"root": d, "snapshot": p.snapshot}))
        self.assertEqual(R.restore_from(str(snap)), 0)
        self.assertEqual(R.Plant(d).ceiling_actual(), TOP, "the watchdog's hand-back puts every CPU's ceiling back")


class PairedRun(unittest.TestCase):
    def test_short_paired_run(self):
        from tools import cpu_power_model as M
        from tools.cpu_power_model import ModelClock, ModelOmni, ModelSampler, ModelService   # the modelled machine's service as the model's own queue, on the model's own clock (30 October 2026)
        R.VERDICT_KW = dict(min_samples=3, probe_every=4, recheck=10, max_trial=12, settle_s=1.0)   # short trials for the test
        R.Service.JITTER = (0.9, 1.1)
        real = (R.Service, R.Omni, R.Sampler, R.time, R.cpu_times)
        R.Service, R.Omni, R.Sampler = ModelService, ModelOmni, ModelSampler   # the harness's threads, joined on the model's clock
        clock = ModelClock()
        R.time = M.time = clock; M.CURRENT["clock"] = clock      # the service, the governor, the sampler and the arms' own thread keep modelled time: the same run on a loaded machine as on a quiet one
        R.cpu_times = M.model_cpu_times                            # and the machine's busy share is the model's, never the runner's /proc/stat
        try:
            sim = tempfile.mkdtemp(); out = Path(tempfile.mkdtemp()) / "out"
            rc = R.main(["--plant", "sim", "--sim-dir", sim, "--workloads", "tuning", "--reps", "1", "--step-s", "4", "--out", str(out)])
        finally:
            R.VERDICT_KW = {}; R.Service, R.Omni, R.Sampler, R.time, R.cpu_times = real; R.Service.JITTER = (0.5, 1.5); M.time = R.time
            M.CURRENT["clock"] = M.CURRENT["service"] = None
        self.assertEqual(rc, 0)
        rec = json.loads((out / "cpu-power-tuning" / "tuning.json").read_text())
        self.assertTrue(rec["machine"]["modelled"])
        r = rec["reps"][0]; nat, om = r["native"], r["omni"]
        self.assertEqual(nat["issued"], om["issued"], "the same requests offered in both arms")
        self.assertEqual(nat["failed"], 0); self.assertEqual(om["failed"], 0)
        self.assertTrue(om["handed_back"]); self.assertFalse(om["foreign_writer"]); self.assertFalse(om["switched_off"])
        self.assertEqual(R.Plant(sim).ceiling_actual(), R.SimPlant.TOP_KHZ, "the ceiling handed back on the machine")
        self.assertEqual(om["verdict"]["objective"], "resource")
        self.assertGreaterEqual(om["verdict"]["counts"]["allowed"], 1, "at least one notch allowed by its trial")
        self.assertLess(om["ceiling_mhz_mean"], nat["ceiling_mhz_mean"], "notches given back")
        self.assertLess(om["energy_j"], nat["energy_j"], "on the modelled machine the notches pay")
        self.assertLessEqual(om["p95_ms"], R.LINE_MS, "the service stays inside the line")
        lines = [json.loads(x) for x in (out / "cpu-power-tuning" / "rep-1" / "omni" / "audit.jsonl").read_text().splitlines()]
        self.assertIn("snapshot", lines[0])
        self.assertTrue(all("cost" in x and "verdict_phase" in x and "allowed_low" in x for x in lines[1:] if "error" not in x))
        self.assertTrue((out / "CPU_POWER.md").exists())
        self.assertIn("reading", rec["paired"]["energy_j"])
        # the three-run table on three copies of this run: it is made, and it flags the modelled machine as not a result
        import shutil
        from tools import cpu_power_abc as T
        dirs = []
        for tag in "ABC":
            d = out.parent / f"run-{tag}"; shutil.copytree(out, d); dirs.append(str(d))
        table = out.parent / "CPU_POWER_ABC.md"
        self.assertEqual(T.main(dirs + ["--out", str(table)]), 0)
        text = table.read_text()
        self.assertIn("modelled machine", text)
        self.assertIn("| energy, CPU package", text)
        self.assertTrue(table.with_suffix(".json").exists())


if __name__ == "__main__":
    unittest.main()
