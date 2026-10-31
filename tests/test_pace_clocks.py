# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v16: every clock of the Kubernetes governor counts seconds, so its decision period (--interval) changes only how
often it looks. At 60 s every value is the one omni-v15 used; at 15, 10 or 5 s each rule keeps its time: the brain's
minute, the compass's damping and smoothing, the edge's window and rates, the additions past the scheduling floor, a
command's minute to land, the host's busy share over a minute, the heat law's minute, one batch job a minute, the coast
per raise, and the conveyance every 15 s whichever check falls due."""
import math
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

from omnicompass.adapter import ASSIMILATION, Governor, mode_law
from omnicompass.edge import Edge
from omni_controller.capacity import HostCpuSampler
from omni_controller.controller import Controller, parser
from omni_controller.muscles import Muscles

ROOT = Path(__file__).resolve().parents[1]

OBS = {"queue_ratio": 0.3, "load_ratio": 0.9, "power_stress": 0.4, "thermal": 0.2, "network_stress": 0.1,
       "drift_ratio": 0.0, "stale": 0.0, "security_block": 0.0, "slo_clean": True}


def controller(*extra):
    return Controller(parser().parse_args(["--audit", "", *extra]), kube=Mock())


class Brain(unittest.TestCase):
    def test_the_brain_keeps_its_minute(self):
        """Four steps of 15 s on a held observation move the brain as one step of 60 s: the observation's weight is the
        same exactly, and the engine's evolution agrees to the integration's own error."""
        one, four = Governor(law=mode_law("fleet")), Governor(law=mode_law("fleet"), period_s=15.0)
        one.step(dict(OBS), 0)
        for _ in range(4):
            four.step(dict(OBS), 0)
        self.assertAlmostEqual(four.t, one.t, places=12)
        a = 1.0 - (1.0 - ASSIMILATION) ** 0.25
        self.assertAlmostEqual(1.0 - (1.0 - a) ** 4, ASSIMILATION, places=12)
        for k in ("E", "U", "I_U", "S", "B"):
            self.assertAlmostEqual(getattr(four.x, k), getattr(one.x, k), delta=0.02, msg=k)

    def test_at_60_s_nothing_moves(self):
        a, b = Governor(law=mode_law("fleet")), Governor(law=mode_law("fleet"), period_s=60.0)
        for _ in range(20):
            self.assertEqual(a.step(dict(OBS), 0), b.step(dict(OBS), 0))
        self.assertIsNone(b.recent)

    def test_contraction_waits_for_the_brains_own_minute(self):
        """The pods' contraction authority (calm >= 0.5, omnicompass/nervous_system.py) comes after the brain's first minute
        on an idle reading, whatever the period: the first decision at 60 s, the fourth at 15 s, and not within three
        decisions of 5 s (the levers rig's old phases, which failed rightsize and coldstart on omni-v16, 22 October)."""
        from omnicompass.nervous_system import from_governor
        idle = dict(OBS, queue_ratio=0.0, load_ratio=0.2, power_stress=0.0, thermal=0.0, network_stress=0.0)
        first = {}
        for period, n in ((60.0, 3), (15.0, 12), (5.0, 3)):
            g = Governor(law=mode_law("fleet"), period_s=period)
            for i in range(n):
                d = g.step(dict(idle), 0)
                if from_governor(g, idle, d)["organs"]["pods"]["contract"]:
                    first[period] = (i + 1) * period
                    break
        self.assertEqual(first, {60.0: 60.0, 15.0: 60.0})

    def test_additions_stay_within_the_minute(self):
        """A need far above the machines asks for up_max a step at 60 s; at 15, 10 or 5 s the same law adds no more than
        up_max over any minute's steps, and as much as at 60 s over whole minutes."""
        need = dict(OBS, queue_ratio=1.5, load_ratio=1.8)
        total = {}
        for period in (60.0, 15.0, 10.0, 5.0):
            g = Governor(law=mode_law("fleet"), period_s=period); g.nodes = 10
            m = int(round(60.0 / period))
            adds = [max(0, g.step(dict(need), 0)["node_delta"]) for _ in range(4 * m)]
            for i in range(len(adds) - m + 1):
                self.assertLessEqual(sum(adds[i:i + m]), g.law.up_max, (period, i))
            total[period] = sum(adds)
        self.assertEqual(len(set(total.values())), 1, total)


class EdgePace(unittest.TestCase):
    def test_counts_and_rates_per_minute(self):
        e1, e4 = Edge(react=1.0), Edge(react=4.0, pace=0.25)
        self.assertEqual((e1.window, e1.narrow, e1.fall_decay, e1.lag), (20, 0.05, 0.9995, 1))
        self.assertEqual((e4.window, e4.lag), (80, 4))
        self.assertAlmostEqual((1.0 - e4.narrow) ** 4, 1.0 - e1.narrow, places=12)
        self.assertAlmostEqual(e4.fall_decay ** 4, e1.fall_decay, places=12)

    def test_a_climb_reads_the_same_cushion_at_either_pace(self):
        """A position that climbs steadily, read once a minute or every 15 s: the cushion's reaction part is the rise
        over the knob's reaction time either way."""
        e1, e4 = Edge(react=1.0), Edge(react=4.0, pace=0.25)
        for i in range(30):
            e1.update(0.01 * i)
        for i in range(120):
            e4.update(0.0025 * i)
        self.assertAlmostEqual(e4.react_part, e1.react_part, places=9)


class ControllerClocks(unittest.TestCase):
    def test_the_heartbeat_is_20_s(self):
        """The founder's order of 31 October, evening ("lock this base engine at 20 ... a whole minute to double check itself
        ... that's way too long"): the main engine decides every 20 s by default from omni-v24 (60 s from omni-v17, the word of
        22 October), the beat a dial any value can be set on, the fast checks every 5 s at every beat, in the governor and in
        every place that starts it (the rigs, the install files and the alert rules' staleness bound)."""
        a = parser().parse_args(["--audit", ""])
        self.assertEqual((a.interval, a.floor_interval), (20.0, 5.0))
        self.assertIn('OMNI_INTERVAL="${OMNI_INTERVAL:-20}"', (ROOT / "scripts" / "kind_bench.sh").read_text())
        for f in ("deploy/install/omni-compass.yaml", "deploy/install/omni-compass-cloud.yaml", "deploy/controller.yaml"):
            self.assertIn('"--interval", "20"', (ROOT / f).read_text(), f)
        # the staleness bound follows the beat: three of the beats the exporter measures, at any setting of the dial
        self.assertIn("omni_last_decision_timestamp_seconds > 3 * clamp_min(omni_heartbeat_seconds, 5)",
                      (ROOT / "deploy/prometheus/omni-compass-rules.yaml").read_text())
        for beat in ("5", "15", "30", "75", "90", "120"):         # every setting of the dial runs, each keeping its rules' time
            c = controller("--interval", beat, "--law", "compass", "--floor-interval", "5")
            self.assertEqual(c.g.period_s, float(beat))
            self.assertEqual(c.n_convey, 3)

    def test_the_levers_rig_runs_the_brains_minutes(self):
        """The levers rig runs at the default heartbeat and gives each phase the 3, 2 and 3 minutes its checks were written
        for (three, two and three decisions of a brain minute before omni-v16), the idle time before cold start in seconds."""
        text = (ROOT / "scripts" / "kind_levers.sh").read_text()
        self.assertIn('IV="${OMNI_INTERVAL:-20}"', text)
        self.assertIn('--interval "$IV" --iterations "$n"', text)
        self.assertIn("--coldstart-idle-s 120", text)
        self.assertNotIn("--interval 5 ", text)
        for phase in ("run 180 --pace-high 0 --contain-cpu-m 200", "run 120 --pace-high 5 --pace-low 5 --contain-cpu-m 100000",
                      'touch "$OUT_DIR/kill"; run 0 --contain-cpu-m 200'):
            self.assertIn(phase, text)

    def test_at_60_s_every_value_is_omni_v15s(self):
        c = controller("--interval", "60", "--law", "compass", "--floor-interval", "5")
        self.assertEqual((c.pace, c.n_add, c.n_land, c.n_convey, c.host_cpu.span), (1.0, 1, 1, 3, 1))
        self.assertEqual(c.compass_law.kd, 180.0)
        self.assertEqual(c.compass_law.smooth, 0.3)
        self.assertEqual(c.g.period_s, 60.0)

    def test_each_clock_keeps_its_time(self):
        for period in (15, 10, 5):
            c = controller("--interval", str(period), "--law", "compass", "--dial", "save", "--floor-interval", "5")
            self.assertEqual(c.n_add * period, 60)
            self.assertEqual(c.n_land * period, 60)
            self.assertEqual(c.host_cpu.span * period, 60)
            self.assertEqual(c.n_convey, 3)                       # 15 s at the 5 s checks, whatever the decision period
            self.assertEqual(c.compass_law.kd, 180.0)             # the damping set at the minute
            self.assertAlmostEqual(c.compass_law.smooth ** (60 / period), 0.3, places=12)
            self.assertEqual(c.g.period_s, float(period))
            self.assertEqual(c.edge.window * period, 20 * 60)

    def test_cruise_waits_for_two_readings_at_any_beat(self):
        """Cruise puts every machine in service when work waits for a place decision after decision: its 120 s is 2, 8 and 24
        decisions at 60, 15 and 5 s, as before, and never fewer than two readings at a slow beat (omni-v17: at 90 and 120 s
        it had rounded to one, and one reading with a pod waiting set every machine in service). A count set by hand stands."""
        for beat, n in ((5, 24), (15, 8), (30, 4), (60, 2), (75, 2), (90, 2), (120, 2)):
            self.assertEqual(controller("--interval", str(beat), "--floor-interval", "5").n_cruise_after, n, beat)
        self.assertEqual(controller("--interval", "120", "--cruise-after", "1").n_cruise_after, 1)
        self.assertEqual(controller("--interval", "120", "--cruise-after", "0").n_cruise_after, 0)

    def test_the_conveyance_runs_every_15_s_at_any_decision_period(self):
        """Every check counts, a decision as well as a fast check: at a decision every 5 s (no fast check between) the
        conveyance still comes every third check (before omni-v16 it never ran there)."""
        for period in (60, 15, 10, 5):
            c = controller("--interval", str(period), "--floor-interval", "5")
            due = [c._convey_due() for _ in range(12)]
            self.assertEqual(sum(due), 4, period)


class Sampler(unittest.TestCase):
    def test_the_busy_share_over_the_span(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "stat"
            s1, s4 = HostCpuSampler(p), HostCpuSampler(p, span=4)
            total = idle = 0
            for busy in (0.2, 0.9, 0.9, 0.9, 0.1):                # five readings, four intervals of 100 ticks
                total += 100; idle += int(round(100 * (1 - busy)))
                p.write_text(f"cpu  {total - idle} 0 0 {idle} 0 0 0 0\n")
                s1.sample(); s4.sample()
            self.assertAlmostEqual(s1.busy_share, 0.1)            # the last interval only, as before
            self.assertAlmostEqual(s4.busy_share, (0.9 * 3 + 0.1) / 4)


class MuscleClocks(unittest.TestCase):
    def test_the_heat_law_keeps_its_minute(self):
        a1 = SimpleNamespace(thermal_model=True, interval=60.0)
        a4 = SimpleNamespace(thermal_model=True, interval=15.0)
        m1, m4 = Muscles(None, a1, lambda r: r), Muscles(None, a4, lambda r: r)
        x1 = m1.sense(1.0)["thermal"]
        for _ in range(4):
            x4 = m4.sense(1.0)["thermal"]
        self.assertAlmostEqual(x4, x1, places=12)
        self.assertEqual(x1, min(1.35, 0.86 * 0.32 + 0.14 * (0.34 + 0.62)))

    def test_one_batch_job_a_minute(self):
        for period, per_min in ((60.0, 1), (15.0, 4)):
            m = Muscles(None, SimpleNamespace(interval=period), lambda r: r)
            self.assertEqual(m._per(60.0), per_min)


class PaceArms(unittest.TestCase):
    """The real runs (docs/PACE_PREREGISTRATION.md): an arm named compassN (compass5 to compass120) is the compass arm deciding
    every N s (scripts/kind_paired.sh), and the receipt pairs each beat against native and against the compass arm at its
    default within the repetition, the default read from the arm's own runs or else from the engine (tools/live_reps.py)."""
    def test_the_runner_sets_the_pace_from_the_arm(self):
        text = (ROOT / "scripts" / "kind_paired.sh").read_text()
        self.assertIn('if [[ "$base" =~ ^compass([0-9]+)$ ]]; then pace="${BASH_REMATCH[1]}"; base=compass; fi', text)
        self.assertIn('OMNI_INTERVAL="${pace:-${OMNI_INTERVAL:-20}}" ARM="$base"', text)

    def test_the_receipt_pairs_each_pace(self):
        import json
        import tools.live_reps as LR
        p95 = "response time (ms), 95th percentile"
        level = {"native": 300.0, "compass": 200.0, "compass15": 190.0, "compass10": 185.0, "compass5": 188.0}

        def standin(d):
            arm, rep = d.name.split("-")[1], int(d.name.split("-")[2])
            g = {k: 0.0 for k in LR.KEYS}
            g[p95] = level[arm] + rep
            return g
        t = Path(tempfile.mkdtemp())
        for arm in level:
            for r in (1, 2, 3):
                d = t / f"bench-{arm}-{r}"; d.mkdir(); (d / "capture.csv").write_text("x\n")
        old = LR.arm_gauges
        try:
            LR.arm_gauges = standin
            LR.main(str(t))
        finally:
            LR.arm_gauges = old
        out = json.loads((t / "LIVE_REPS.json").read_text())
        for pace in (15, 10, 5):
            self.assertAlmostEqual(out["paired"][f"compass{pace}"][p95]["diff"], level[f"compass{pace}"] - 300.0, places=6)
            self.assertAlmostEqual(out["paired"][f"compass{pace}|compass"][p95]["diff"], level[f"compass{pace}"] - 200.0, places=6)
        md = (t / "LIVE_REPS.md").read_text()
        self.assertIn("omni deciding every 15 s vs omni at its default, every 20 s", md)   # no beat written: the engine's default
        self.assertIn("omni, a decision every 5 s", md)
        for r in (1, 2, 3):                                   # the compass arm's own beat, as its runs wrote it, names its default
            (t / f"bench-compass-{r}" / "omni_interval.txt").write_text("90\n")
        try:
            LR.arm_gauges = standin
            LR.main(str(t))
        finally:
            LR.arm_gauges = old
        self.assertIn("omni deciding every 15 s vs omni at its default, every 90 s", (t / "LIVE_REPS.md").read_text())


if __name__ == "__main__":
    unittest.main()
