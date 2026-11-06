# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass's own orchestrator (omni_orchestrator/): the room rule, the brain, the yardstick and the ledger."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omni_orchestrator.brain import OmniBrain, Yardstick, conveyed_limits, machines_needed  # noqa: E402
from omni_orchestrator.control import Control  # noqa: E402
from omni_orchestrator.scheduler import place, room  # noqa: E402
from omni_orchestrator.workload import chain  # noqa: E402


def machines(*states):
    return {f"m{i}": {"name": f"m{i}", "cpu_m": 500, "state": s} for i, s in enumerate(states, 1)}


def unit(machine, service="web", req=250):
    return {"machine": machine, "service": service, "req_m": req}


class RoomRule(unittest.TestCase):
    def test_a_unit_goes_only_where_its_request_fits(self):
        ms = machines("awake", "awake")
        us = [unit("m1"), unit("m1"), unit("m2"), unit("m2")]
        self.assertIsNone(place(250, "web", ms, us))
        self.assertEqual(room(ms["m1"], us), 0)

    def test_no_unit_goes_to_a_machine_that_is_not_awake(self):
        ms = machines("parked", "booting", "draining", "awake")
        self.assertEqual(place(250, "web", ms, []), "m4")

    def test_pack_fills_the_fullest_machine_that_fits(self):
        ms = machines("awake", "awake", "awake")
        us = [unit("m1"), unit("m2", "other")]
        # the service stands on m1 alone: its next unit goes to another machine, the fullest that fits (m2)
        self.assertEqual(place(250, "web", ms, us, "pack"), "m2")
        us.append(unit("m2"))
        # on two machines now: the best fit wins, m1 (250 m left, the unit fills it)
        self.assertEqual(place(250, "web", ms, us, "pack"), "m1")

    def test_the_busy_rule_keeps_a_unit_off_a_machine_at_its_top(self):
        ms = machines("awake", "awake")
        ms["m1"]["busy_m"], ms["m2"]["busy_m"] = 380.0, 100.0       # m1 at 76% of its 500 m, m2 at 20%
        self.assertEqual(place(250, "web", ms, [], "pack", "requests"), "m1")   # by requests both fit; pack picks the fullest by name
        self.assertEqual(place(250, "web", ms, [], "pack", "busy"), "m2")       # under the busy rule m1 has no room
        ms["m2"]["busy_m"] = 300.0                                      # 60%: 75 m of room under 75%, less than a unit
        self.assertIsNone(place(250, "web", ms, [], "pack", "busy"))

    def test_spread_takes_the_machine_with_fewest_units_of_the_service(self):
        ms = machines("awake", "awake", "awake")
        us = [unit("m1"), unit("m2")]
        self.assertEqual(place(250, "web", ms, us, "spread"), "m3")


class Brain(unittest.TestCase):
    def test_the_yardstick_follows_kubernetes_published_rule(self):
        y = Yardstick(mn=2, mx=12)
        self.assertEqual(y.recommend(0.0, 4, 1.0), 8)            # twice the target: twice the units
        self.assertEqual(y.recommend(15.0, 8, 0.52), 8)          # inside the 10% tolerance
        self.assertEqual(y.recommend(30.0, 8, 0.1), 8)           # a fall only to the highest of the last 300 s
        self.assertEqual(y.recommend(400.0, 8, 0.1), 2)          # the window has passed

    def test_omni_never_holds_fewer_units_than_its_native_twin(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12)
        want, why = b.decide(0.0, 4, 1.5, 100.0, 0)              # calm response, but the units at three times target
        self.assertGreaterEqual(want, why["twin"])
        self.assertEqual(want, 8)                                # the rule's own limit: at most twice the units at once

    def test_past_the_wall_omni_adds_the_most_it_may_at_once(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12, max_step=3)
        want, why = b.decide(0.0, 4, 0.5, 790.0, 5)
        self.assertEqual(why["force"], 1.0)
        self.assertEqual(want, 7)

    def test_omni_gives_back_one_unit_only_after_the_force_held_down(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12, hold=3)
        b.twin.recommend(-400.0, 2, 0.5)
        got = [b.decide(t, 6, 0.2, 60.0, 0)[0] for t in (0.0, 5.0, 10.0)]
        self.assertEqual(got[:2], [6, 6])
        self.assertLessEqual(got[2], 6)

    def test_the_reflex_adds_a_unit_for_each_request_waiting_in_line(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12, max_step=3)
        self.assertEqual(b.decide(0.0, 4, 0.5, 100.0, 2)[0], 6)     # two waiting: two units now, the response still calm
        self.assertEqual(b.decide(5.0, 6, 0.5, 100.0, 5)[0], 9)     # five waiting: the step at most

    def test_the_verdicts_depth_lowers_the_floor_and_a_trial_walks_to_it_one_unit_a_beat(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12, hold=3)
        want, why = b.decide(0.0, 8, 0.5, 60.0, 0, depth=2, trial=True)
        self.assertEqual((why["twin"], why["floor"]), (8, 6))        # busy at target: the twin holds 8; two below it allowed
        self.assertEqual(want, 7)                                    # one unit a beat toward the step
        # the step is counted from the twin as the phase found it (anchor 8), so the floor does not follow the count down
        self.assertEqual(b.decide(5.0, 7, 0.5, 60.0, 0, depth=2, trial=True, anchor=8)[0], 6)
        self.assertEqual(b.decide(10.0, 6, 0.5, 60.0, 0, depth=2, trial=True, anchor=8)[0], 6)   # and stands there
        self.assertEqual(b.decide(15.0, 6, 0.5, 60.0, 1, depth=2, trial=True, anchor=8)[0], 7)   # work waits: the reflex

    def test_a_trials_floor_rises_with_a_twin_the_traffic_raised(self):
        # the phase began at a twin of 5; the traffic rose and the twin now says 6: one step below 6, never below 5 - 1
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12, hold=3)
        want, why = b.decide(0.0, 5, 0.5, 60.0, 0, depth=1, trial=True, twin=6, anchor=5)
        self.assertEqual((why["floor"], want), (5, 5))

    def test_a_trial_the_traffic_keeps_abandoning_waits_longer_each_time(self):
        d = tempfile.mkdtemp()
        spec = {"routes": str(Path(d) / "routes.json"), "front_stats": "http://127.0.0.1:1/_stats",
                "machines": [{"name": "m1", "url": "http://127.0.0.1:1", "cpu_m": 500}],
                "services": [{"name": "web", "replicas": 2, "min": 2, "max": 6, "req_m": 250, "limit_m": 250, "k": 10,
                              "line_ms": 800}]}
        c = Control(spec, d, "omni", 5.0)
        c.machine_brain = c.convey = lambda now: None        # the units' brain alone
        v = c.verdicts["web"]
        waits = []
        for _ in range(4):
            v.phase, v.trial = "ref", 1                       # a phase is on; the arrivals then move past 15%
            c.phase_rate["web"] = 10.0
            c.front_recent = lambda: {"p95_5s": 60.0, "line": 0, "hands": 1, "n_5s": 20.0, "recent": []}
            c.think(0.0)
            waits.append(c.trial_hold["web"] - v.t)
        self.assertEqual(waits, [6, 12, 24, 24])             # 6 beats, doubled, up to the recheck
        self.assertIsNone(v.phase)
        c.think(0.0)                                         # inside the hold no trial starts, however calm the service
        self.assertIsNone(v.phase)

    def test_conveyance_gives_a_unit_the_room_under_75_percent_of_its_machine(self):
        one, two = [{"id": "a", "req_m": 250}], [{"id": "a", "req_m": 250}, {"id": "b", "req_m": 250}]
        self.assertEqual(conveyed_limits(500, 100.0, one, 0.0), {"a": 370.0})     # alone: the room under 375 m, in 10 m steps
        self.assertEqual(conveyed_limits(500, 100.0, two, 0.0), {"a": 250.0, "b": 250.0})  # shared: never under the request
        self.assertEqual(conveyed_limits(500, 100.0, one, 100.0), {"a": 270.0})   # another workload's 100 m counted off
        self.assertIsNone(conveyed_limits(500, None, one, 0.0))                   # busy share unread: nothing moves
        self.assertIsNone(conveyed_limits(500, 360.0, one, 0.0))                  # 72%: between the lines, held
        self.assertIsNone(conveyed_limits(500, 380.0, one, 0.0))                  # 76%: no new raise, what stands stands
        self.assertEqual(conveyed_limits(500, 380.0, one, 0.0, others_room=True), {"a": 250.0})  # ...beside another's room: back
        self.assertEqual(conveyed_limits(500, 0.0, one, 0.0)["a"], 370.0)         # never over the machine, in any case
        self.assertEqual(conveyed_limits(2000, 0.0, one, 0.0)["a"], 1500.0)

    def test_machines_hold_room_for_the_next_step_and_never_fall_below_two(self):
        self.assertEqual(machines_needed(1, 250, 500, 2, 2), 2)
        self.assertEqual(machines_needed(8, 250, 500, 2, 2), 5)


class Ledger(unittest.TestCase):
    def test_a_control_plane_started_again_replays_the_same_ledger(self):
        d = tempfile.mkdtemp()
        spec = {"routes": str(Path(d) / "routes.json"), "front_stats": "http://127.0.0.1:1/_stats",
                "machines": [{"name": "m1", "url": "http://127.0.0.1:1", "cpu_m": 500}],
                "services": [{"name": "web", "replicas": 2, "min": 2, "max": 12, "req_m": 250, "limit_m": 250, "k": 10,
                              "line_ms": 800}]}
        c = Control(spec, d, "omni", 5.0)
        c.record({"ev": "desired", "service": "web", "n": 5})
        c.record({"ev": "unit", "u": {"id": "web-0", "seq": 0, "kind": "service", "service": "web", "machine": "m1",
                                      "port": 9100, "req_m": 250, "state": "placed", "born": 0.0}})
        c.record({"ev": "machine", "name": "m1", "state": "draining"})
        again = Control(spec, d, "omni", 5.0)
        self.assertEqual(again.desired["web"], 5)
        self.assertEqual(set(again.units), {"web-0"})
        self.assertEqual(again.machines["m1"]["state"], "draining")
        self.assertEqual(again.port, 9101)                      # no port is ever given twice

    def test_the_twins_busy_share_is_read_capped_at_the_request(self):
        d = tempfile.mkdtemp()
        spec = {"routes": str(Path(d) / "routes.json"), "front_stats": "http://127.0.0.1:1/_stats",
                "machines": [{"name": "m1", "url": "http://127.0.0.1:1", "cpu_m": 500}],
                "services": [{"name": "web", "replicas": 1, "min": 1, "max": 12, "req_m": 250, "limit_m": 250, "k": 10,
                              "line_ms": 800}]}
        c = Control(spec, d, "omni", 5.0)
        c.units["web-0"] = {"id": "web-0", "kind": "service", "service": "web", "machine": "m1", "req_m": 250,
                            "state": "placed", "cpu_s": 0.0}
        c.busy("web", 0.0)
        c.units["web-0"]["cpu_s"] = 1.6                          # 1.6 s of processor in 4 s: 400 m, over a 250 m request
        self.assertAlmostEqual(c.busy("web", 4.0), 1.0)         # what Kubernetes' pod, walled at its request, could use
        self.assertAlmostEqual(c.busy_raw["web"], 1.6)          # what the conveyed unit used, for the audit

    def test_the_three_arms_are_three_brains_of_one_control_plane(self):
        spec = {"routes": "r.json", "front_stats": "http://127.0.0.1:1/_stats",
                "machines": [{"name": "m1", "url": "http://127.0.0.1:1", "cpu_m": 500}],
                "services": [{"name": "web", "replicas": 1, "min": 1, "max": 12, "req_m": 250, "limit_m": 250, "k": 10,
                              "line_ms": 800}]}
        native = Control(spec, tempfile.mkdtemp(), "yardstick", 5.0)          # Kubernetes' rule alone: spread, no verdict
        on_native = Control(spec, tempfile.mkdtemp(), "omni_native", 5.0)    # Omni on top of it: packs, conveys, no verdict
        direct = Control(spec, tempfile.mkdtemp(), "omni", 5.0)              # Omni alone: packs, conveys, the verdict
        self.assertEqual((native.how, on_native.how, direct.how), ("spread", "pack", "pack"))
        self.assertEqual((set(native.verdicts), set(on_native.verdicts), set(direct.verdicts)), (set(), set(), {"web"}))

    def test_a_conveyed_wall_is_journaled_and_replayed(self):
        d = tempfile.mkdtemp()
        spec = {"routes": str(Path(d) / "routes.json"), "front_stats": "http://127.0.0.1:1/_stats",
                "machines": [{"name": "m1", "url": "http://127.0.0.1:1", "cpu_m": 500}],
                "services": [{"name": "web", "replicas": 1, "min": 1, "max": 12, "req_m": 250, "limit_m": 250, "k": 10,
                              "line_ms": 800}]}
        c = Control(spec, d, "omni", 5.0)
        c.record({"ev": "unit", "u": {"id": "web-0", "seq": 0, "kind": "service", "service": "web", "machine": "m1",
                                      "port": 9100, "req_m": 250, "state": "placed", "born": 0.0}})
        c.record({"ev": "limit", "id": "web-0", "limit_m": 370.0})
        self.assertEqual(Control(spec, d, "omni", 5.0).units["web-0"]["conveyed_m"], 370.0)


class Work(unittest.TestCase):
    def test_the_answer_is_fixed_by_its_seed(self):
        self.assertEqual(chain(7, 100), chain(7, 100))
        self.assertNotEqual(chain(7, 100), chain(8, 100))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
