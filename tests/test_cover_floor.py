# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The compass's cover on an autoscaler's target is a knob (omni-v24, --cover-floor): the lowest share of the operator's own
target the compass may set. 0.6 is the factory's, the cover every engine before omni-v24 had written in; 1.0 leaves the pod
count where native's own target puts it. Read in each declared setting by the tune study (docs/THE_TUNE.md), never a rule.
The floor is never above the operator's target, so the compass never asks for fewer pods than native would (do no harm)."""
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omni_controller.controller import Controller, parser  # noqa: E402


def controller(*extra):
    return Controller(parser().parse_args(["--audit", "", "--mode", "nodepool", "--law", "compass", *extra]), kube=Mock())


class CoverFloor(unittest.TestCase):
    def test_the_factory_cover_is_the_one_every_earlier_engine_wrote(self):
        c = controller()
        self.assertEqual(c.a.cover_floor, 0.6)
        self.assertEqual(c._bounds(50), (50.0, 30.0))             # 60% of the operator's 50%: up to 1/0.6 of native's pods
        self.assertEqual(c._bounds(50, 1.5), (75.0, 45.0))        # in the pods' own terms while a limit is conveyed

    def test_a_floor_of_one_leaves_the_pod_count_natives(self):
        c = controller("--cover-floor", "1.0")
        hi, lo = c._bounds(50)
        self.assertEqual(hi, lo)                                  # the compass can set nothing but native's own target

    def test_the_floor_is_held_inside_its_range(self):
        self.assertEqual(controller("--cover-floor", "0.05")._cover(), 0.1)
        self.assertEqual(controller("--cover-floor", "2")._cover(), 1.0)
        self.assertEqual(controller("--cover-floor", "0")._cover(), 0.6)   # unset reads the factory's

    def test_the_floor_is_never_above_the_operators_target(self):
        # an operator's target under 10%: the cover's 10% bound once put the floor above it (fewer pods than native); never now
        for cover in ("0.6", "1.0"):
            hi, lo = controller("--cover-floor", cover)._bounds(8)
            self.assertLessEqual(lo, hi)
            self.assertEqual(hi, 8.0)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
