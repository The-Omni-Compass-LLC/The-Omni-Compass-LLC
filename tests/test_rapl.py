# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The machine's own meter (tools/rapl.py): which zones are counted, a wrapped counter, and a window read between
samples, on a made-up powercap tree."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import rapl  # noqa: E402


def zone(root, name, label, uj, rng=262143328850):
    d = Path(root) / name
    d.mkdir(parents=True)
    (d / "name").write_text(label + "\n")
    (d / "energy_uj").write_text(f"{uj}\n")
    (d / "max_energy_range_uj").write_text(f"{rng}\n")
    return d


class Zones(unittest.TestCase):
    def test_packages_and_memory_counted_parts_never_twice(self):
        with tempfile.TemporaryDirectory() as t:
            zone(t, "intel-rapl:0", "package-0", 1000)
            zone(t, "intel-rapl:0:0", "core", 400)          # a part of package 0
            zone(t, "intel-rapl:0:1", "dram", 200)
            zone(t, "intel-rapl:1", "package-1", 900)
            zone(t, "intel-rapl:2", "psys", 5000)           # the platform: recorded, never added
            zs = {z["zone"]: z for z in rapl.zones(t)}
            self.assertEqual(sorted(k for k, z in zs.items() if z["counted"]),
                             ["intel-rapl:0", "intel-rapl:0:1", "intel-rapl:1"])
            self.assertEqual(zs["intel-rapl:0:0"]["kind"], "core")
            self.assertEqual(zs["intel-rapl:2"]["kind"], "psys")
            p = rapl.probe(t)
            self.assertTrue(p["meter"])
            self.assertEqual(p["counted"], ["intel-rapl:0", "intel-rapl:0:1", "intel-rapl:1"])

    def test_no_zones_no_meter(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertFalse(rapl.probe(t)["meter"])
            self.assertEqual(rapl.main(["probe", "--root", t]), 2)
            with self.assertRaises(SystemExit):
                rapl.sample(str(Path(t) / "x.csv"), root=t, count=1)


class Counting(unittest.TestCase):
    def test_a_wrapped_counter_counts_once(self):
        zs = [{"zone": "intel-rapl:0", "max_range_uj": 1_000_000}]
        acc = rapl.Accumulator(zs)
        acc.add({"intel-rapl:0": 900_000})
        self.assertAlmostEqual(acc.add({"intel-rapl:0": 950_000})["intel-rapl:0"], 0.05)
        self.assertAlmostEqual(acc.add({"intel-rapl:0": 50_000})["intel-rapl:0"], 0.15)   # wrapped: +0.10 J

    def test_sampling_and_the_window(self):
        with tempfile.TemporaryDirectory() as t:
            pkg = zone(t, "intel-rapl:0", "package-0", 0, rng=10_000_000)
            ticks = iter([100.0, 110.0, 120.0, 130.0])
            values = iter([2_000_000, 6_000_000, 1_000_000])    # +2 J, +4 J, then a wrap: +5 J
            def sleep(_):
                (pkg / "energy_uj").write_text(f"{next(values)}\n")
            out = Path(t) / "rapl.csv"
            rapl.sample(str(out), interval=10, root=t, count=4, clock=lambda: next(ticks), sleep=sleep)
            rows = out.read_text().splitlines()
            self.assertEqual(rows[0].split(",")[:2], ["epoch_s", "machine_j"])
            self.assertEqual([float(r.split(",")[1]) for r in rows[1:]], [0.0, 2.0, 6.0, 11.0])
            w = rapl.window(str(out), 105.0, 125.0)               # 1 J of the first step, all of the second, half the third
            self.assertTrue(w["ok"])
            self.assertAlmostEqual(w["joules"], 1.0 + 4.0 + 2.5)
            self.assertAlmostEqual(w["mean_w"], 7.5 / 20.0)
            self.assertFalse(rapl.window(str(out), 90.0, 125.0)["ok"])   # the samples must cover the window
            self.assertEqual(rapl.main(["window", str(out), "105", "125"]), 0)


class TheTable(unittest.TestCase):
    def test_meter_and_kepler_rows(self):
        from tools import live_reps
        with tempfile.TemporaryDirectory() as t:
            d = Path(t) / "bench-compass-1"
            d.mkdir()
            (d / "window_start.txt").write_text("1000\n")
            (d / "window_end.txt").write_text("1900\n")
            # 200 W for the whole window, sampled every 2 s from 997 s to 1903 s, the last line cut short
            lines = ["epoch_s,machine_j,intel-rapl:0:package-0_j"] + [f"{t0},{(t0 - 997) * 200.0},{(t0 - 997) * 200.0}"
                                                                        for t0 in range(997, 1905, 2)]
            (d / "rapl.csv").write_text("\n".join(lines) + "\n1905,18")
            node = 'kepler_node_cpu_joules_total{node_name="omni-bench-control-plane",path="/host/sys",zone="%s"} %s\n'
            pod = 'kepler_pod_cpu_joules_total{node_name="%s",pod_id="%s",pod_name="%s",pod_namespace="%s",state="running",zone="package"} %s\n'
            (d / "kepler_start_omni-bench-control-plane.prom").write_text(node % ("package", 5000) + node % ("dram", 500) + node % ("core", 4000))
            (d / "kepler_end_omni-bench-control-plane.prom").write_text(node % ("package", 5000 + 171000) + node % ("dram", 500 + 9000) + node % ("core", 9e9))
            (d / "kepler_start_omni-bench-worker.prom").write_text(pod % ("omni-bench-worker", "a", "php-apache-7d-x1", "default", 100))
            (d / "kepler_end_omni-bench-worker.prom").write_text(pod % ("omni-bench-worker", "a", "php-apache-7d-x1", "default", 3700)
                                                                 + pod % ("omni-bench-worker", "b", "php-apache-7d-x2", "default", 3600)
                                                                 + pod % ("omni-bench-worker", "c", "load-generator-1", "default", 9999))
            g = live_reps.meter(d)
            self.assertAlmostEqual(g["energy, the machine's own meter (Wh)"], 200.0 * 900 / 3600)       # 50 Wh
            self.assertAlmostEqual(g["energy, Kepler's reading of the machine's meter (Wh)"], 180000 / 3600)
            self.assertAlmostEqual(g["energy Kepler attributes to the service's pods (Wh)"], 7200 / 3600)
            self.assertIn("energy, the machine's own meter (Wh)", live_reps.METER)
            self.assertTrue(live_reps.KEPLER <= live_reps.NEUTRAL)                 # shown, never judged
            self.assertEqual(live_reps.meter(Path(t)), {})                          # no window marks: nothing


if __name__ == "__main__":
    unittest.main()
