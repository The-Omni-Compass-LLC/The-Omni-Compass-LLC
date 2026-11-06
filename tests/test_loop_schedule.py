# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v16: the Kubernetes governor's loop keeps its own schedule (omni_controller/controller.py, main): a decision every
--interval seconds and a fast check every --floor-interval seconds between, each on its time from the schedule however
long the steps take, a missed slot skipped and never run in a burst. Before omni-v16 each wait began when the step ended,
so a decision of 60 s came every 62 to 67 s on kind."""
import unittest
from types import SimpleNamespace
from unittest import mock

import omni_controller.controller as C


class Clock:
    def __init__(self):
        self.t = 1000.0

    def time(self):
        return self.t

    def sleep(self, s):
        self.t += max(0.0, s)


class StandinController:
    """Records when each decision and each fast check began; each takes the time it is given."""
    def __init__(self, clock, step_s, check_s):
        self.clock, self.step_s, self.check_s, self.events, self.audits = clock, step_s, check_s, [], []

    def step(self):
        self.events.append(("decision", self.clock.t - 1000.0)); self.clock.t += self.step_s

    def floor_step(self):
        self.events.append(("check", self.clock.t - 1000.0)); self.clock.t += self.check_s

    def audit(self, r):
        self.audits.append(r)

    def restore(self):
        pass


def run(interval, floor, iterations, step_s, check_s):
    clock = Clock()
    ctl = StandinController(clock, step_s, check_s)
    argv = ["--mode", "nodepool", "--interval", str(interval), "--floor-interval", str(floor), "--iterations", str(iterations),
            "--audit", ""]
    standin_time = SimpleNamespace(time=clock.time, sleep=clock.sleep)
    with mock.patch.object(C, "time", standin_time), mock.patch.object(C, "Controller", lambda a: ctl), \
            mock.patch.object(C.master, "refuse_if_off", lambda *a, **k: None), \
            mock.patch.object(C.master, "register", lambda *a, **k: None), \
            mock.patch.object(C.master, "heartbeat", lambda *a, **k: None), \
            mock.patch("atexit.register", lambda *a, **k: None):
        C.main(argv)
    return ctl


class Schedule(unittest.TestCase):
    def test_decisions_and_checks_keep_their_times(self):
        for interval, floor in ((60, 5), (15, 5), (10, 5), (5, 5)):
            ctl = run(interval, floor, 6, step_s=2.0, check_s=0.5)
            dec = [t for k, t in ctl.events if k == "decision"]
            self.assertEqual(dec, [interval * j for j in range(6)], interval)
            chk = [t for k, t in ctl.events if k == "check"]
            want = [interval * j + floor * m for j in range(5) for m in range(1, int(interval // floor)) if floor * m < interval]
            self.assertEqual(chk, [float(x) for x in want], interval)

    def test_a_step_longer_than_its_slot_skips_and_never_bursts(self):
        ctl = run(5, 5, 4, step_s=12.0, check_s=0.0)
        dec = [t for k, t in ctl.events if k == "decision"]
        self.assertTrue(all(b - a >= 5.0 for a, b in zip(dec, dec[1:])), dec)
        self.assertTrue(any("behind_s" in r for r in ctl.audits))


if __name__ == "__main__":
    unittest.main()
