# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The decision period (the founder's orders of 14 October, night: faster than every native controller, but only where it
hurts nothing). The fast checks run every 5 s, three times as fast as the HPA's own 15-second check. Under v6 the give-back
trial counted its phase in decisions, so at a period too short the phase ended before it had measured the response times it
needs and no machine was ever given back; v7 counts every rule in seconds (omni_controller/controller.py, --verdict-trial-s
and the other *-s settings), so a trial has its full time at any decision period."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NATIVE_CHECK_S = 15.0          # the HPA's own sync period on a managed cluster (fixed by the provider)
PROBE_MAX_PER_S = 1.0          # scripts/latency_probe.py: 5 requests, then a 5 s pause: at most one response time a second


def fast_checks_per_decision(interval, floor):
    """The controller's own spacing (omni_controller/controller.py, main): it sleeps in steps of the floor interval and runs
    a fast check after every step that ends before the next decision."""
    waited, n = 0.0, 0
    while waited + 1e-9 < interval:
        waited += min(floor, interval - waited)
        if waited + 1e-9 < interval:
            n += 1
    return n


def trial_phase_s(interval):
    """A give-back trial's phase in seconds at this decision period: v7 counts it in seconds (--verdict-trial-s), as
    whole decisions, so it is never shorter than its setting by more than one decision."""
    src = (ROOT / "omni_controller" / "controller.py").read_text()
    sec = float(re.search(r'"--verdict-trial-s", type=float, default=([0-9.]+)', src).group(1))
    return max(1, round(sec / interval)) * interval


def samples_needed():
    src = (ROOT / "omni_controller" / "controller.py").read_text()
    return int(re.search(r'getattr\(a, "verdict_samples", (\d+)\)', src).group(1))


def periods(env):
    """The periods a run hands the governor: the run's own, else the rig's defaults (scripts/kind_bench.sh)."""
    rig = (ROOT / "scripts" / "kind_bench.sh").read_text()
    m = re.search(r'OMNI_INTERVAL="\$\{OMNI_INTERVAL:-([0-9.]+)\}"', rig)
    if m:
        d_i = float(m.group(1))
    else:                    # omni-v24: the rig asks the engine its factory beat for the place; this run is a cloud's
        assert 'OMNI_INTERVAL="${OMNI_INTERVAL:-$(bash scripts/factory_beat.sh)}"' in rig
        sys.path.insert(0, str(ROOT))
        from omni_controller.controller import FACTORY_BEAT
        d_i = FACTORY_BEAT["through the cloud"]
    d_f = float(re.search(r'OMNI_FLOOR_INTERVAL="\$\{OMNI_FLOOR_INTERVAL:-([0-9.]+)\}"', rig).group(1))
    i = re.search(r"OMNI_INTERVAL: '([0-9.]+)'", env); f = re.search(r"OMNI_FLOOR_INTERVAL: '([0-9.]+)'", env)
    return (float(i.group(1)) if i else d_i), (float(f.group(1)) if f else d_f)


class DecisionPeriod(unittest.TestCase):
    def setUp(self):
        self.interval, self.floor = periods((ROOT / ".github" / "workflows" / "aks-metered.yml").read_text())

    def test_the_fast_checks_run_faster_than_native_and_between_every_decision(self):
        self.assertLess(self.floor, NATIVE_CHECK_S)
        self.assertGreaterEqual(fast_checks_per_decision(self.interval, self.floor), 1)

    def test_a_give_back_trial_has_time_to_measure_what_it_needs(self):
        need_s = samples_needed() / PROBE_MAX_PER_S
        self.assertGreaterEqual(trial_phase_s(self.interval), need_s)
        # the trap found before any run (14 October) is closed by v7: at 15 s or 5 s a phase still lasts its full time,
        # so a trial measures what it needs at any period; a 5 s decision with 5 s checks would still run no fast check
        for period in (60.0, 15.0, 5.0):
            self.assertGreaterEqual(trial_phase_s(period), need_s, period)
        self.assertEqual(fast_checks_per_decision(5.0, 5.0), 0)

    def test_the_rig_passes_both_periods_to_the_governor(self):
        s = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertIn('--interval "$OMNI_INTERVAL" --floor-interval "$OMNI_FLOOR_INTERVAL"', s)
        self.assertIn("want=$(( DURATION / 60 - 1 ))", s)          # a silent window still needs a decision a minute


if __name__ == "__main__":
    unittest.main()
