# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v14: a muscle the operator leaves native (--native, or OMNI_NATIVE) is never written, and every other muscle runs
as before (the founder's order of 20 October: a knob on every monitor to turn a muscle on and off). With nothing left
native the governor is omni-v13's, write for write."""
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from omni_controller.controller import MUSCLES, native_muscles
from tests.test_convey_shared_host import Cluster, Stat, muscles, node, pod
from tests.test_omni_controller import cluster, run, writes


class TheList(unittest.TestCase):
    def test_names(self):
        self.assertEqual(native_muscles(""), frozenset())
        self.assertEqual(native_muscles(" machines , cpu "), frozenset({"machines", "cpu"}))

    def test_an_unknown_muscle_is_refused_never_ignored(self):
        with self.assertRaises(SystemExit):
            native_muscles("machines,cpus")

    def test_every_muscle_is_described(self):
        self.assertTrue(all(isinstance(v, str) and v for v in MUSCLES.values()))


class Cpu(unittest.TestCase):
    def test_conveyance_left_native_writes_nothing(self):
        c = Cluster([node("w1", kind=False)], [pod("web-1", "w1")])
        m, events = muscles(c, None)
        m.a.native_muscles = frozenset({"cpu"})
        self.assertIsNone(m.convey())
        self.assertEqual([w for w in c.writes if w[0][0] == "patch"], [])

    def test_conveyance_runs_when_another_muscle_is_left_native(self):
        c = Cluster([node("w1", kind=False)], [pod("web-1", "w1")])
        m, events = muscles(c, None)
        m.a.native_muscles = frozenset({"machines", "replicas"})
        self.assertEqual(m.convey(), {"default/web-1": 3800})


class Push(unittest.TestCase):
    def test_hardware_left_native(self):
        calls = []
        a = SimpleNamespace(dial="save", cap_min=0.5, cpufreq_cmd="setfreq {khz}", cpu_max_khz=3_000_000, gpu_power_cmd="setgpu {w}",
                            gpu_max_w=300, dry_run=True, native_muscles=frozenset({"clock", "gpu"}))
        from omni_controller.muscles import Muscles
        m = Muscles(None, a, calls.append)
        m._hardware(0.7, {"slo_clean": True})
        self.assertEqual([c for c in calls if "write" in c], [])
        a.native_muscles = frozenset({"gpu"})
        m._last_cap = 1.0
        m._hardware(0.7, {"slo_clean": True})
        self.assertEqual([c["write"][0] for c in calls if "write" in c], ["setfreq"])


class Governor(unittest.TestCase):
    def test_replicas_left_native_patch_no_target(self):
        t = tempfile.mkdtemp(); st = cluster(t)
        run(t, "--mode", "target", "--native", "replicas")
        self.assertEqual([w for w in writes(t) if w[0] in ("patch", "annotate")], [])
        aud = [json.loads(l) for l in (Path(t) / "audit.jsonl").read_text().splitlines()]
        self.assertTrue(any(r.get("native_muscles") == ["replicas"] for r in aud))
        self.assertTrue(any("decision" in r for r in aud))       # it still decides, with the whole body in view

    def test_the_targets_move_when_nothing_is_left_native(self):
        t = tempfile.mkdtemp(); st = cluster(t)
        run(t, "--mode", "target")
        self.assertTrue(any(w[0] == "patch" for w in writes(t)))

    def test_machines_left_native_run_no_pool_command(self):
        t = tempfile.mkdtemp(); st = cluster(t)
        marker = Path(t) / "scaled"
        cmd = f"python3 -c \"open('{marker}', 'a').write('{{n}}\\\\n')\""
        run(t, "--mode", "nodepool", "--node-scale-cmd", cmd, "--max-node-step", "2", "--native", "machines", iterations=8)
        self.assertFalse(marker.exists())
        aud = [json.loads(l) for l in (Path(t) / "audit.jsonl").read_text().splitlines()]
        self.assertTrue(any(r.get("held") == "machines" for r in aud) or not any(r.get("why") == "node pool size" for r in aud))

    def test_the_pool_moves_when_nothing_is_left_native(self):
        t = tempfile.mkdtemp(); st = cluster(t)
        marker = Path(t) / "scaled"
        cmd = f"python3 -c \"open('{marker}', 'a').write('{{n}}\\\\n')\""
        run(t, "--mode", "nodepool", "--node-scale-cmd", cmd, "--max-node-step", "2", iterations=8)
        self.assertTrue(marker.exists())


if __name__ == "__main__":
    unittest.main()
