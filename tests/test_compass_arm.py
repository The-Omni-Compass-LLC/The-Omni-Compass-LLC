# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The compass on a realm muscle keeps its state from one decision to the next (realms/compass_arm.py).

Each muscle's compass is made once, on its first decision, and then carries its position, its velocity and the knob's
continuous value forward. A compass made fresh every decision would forget the knob between decisions, so the knob could
never travel more than one step from native. A renamed attribute did exactly that (2026-10-05); this test keeps it from
coming back."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from realms.compass_arm import compass_apply  # noqa: E402
from realms.presets import PRESETS  # noqa: E402


class Axis:
    """A stand-in reaction wheel (its own preset's physics, where an effort cap pays): calm (no queue, light load), so the
    compass gives effort back step by step."""
    template = "motion_axis"
    P = PRESETS["reaction_wheel"]
    vhist = []

    def observe(self):
        return {"queue_ratio": 0.0, "load_ratio": 0.2, "power_stress": 0.0}


def main():
    p = Axis()
    compass_apply(p, "power")
    law = p._compass_law
    xs = [p._compass_law_x]
    for _ in range(40):
        compass_apply(p, "power")
        assert p._compass_law is law, "the compass was made again: its state would be lost between decisions"
        xs.append(p._compass_law_x)
    assert xs[-1] < xs[1] < 1.0, f"the knob did not travel from native across decisions: {xs[:3]} ... {xs[-1]}"
    assert all(b <= a + 1e-12 for a, b in zip(xs, xs[1:])), "a calm muscle's knob only goes down"
    assert xs[-1] >= 0.4 - 1e-12, "never under the cover"
    print(f"compass arm: one compass per muscle, kept across decisions; a calm axis eased from 1.00 to {xs[-1]:.2f} "
          f"over 40 decisions, never under its cover (0.40)")

    # Omni v3: the speed knob is offered only where the axis has slack (duty at full speed at most one half)
    from realms.compass_arm import lever, speed_slack
    class Busy(Axis):
        P = PRESETS["rail_traction"]                            # a train at its timetable's capacity: duty about 0.8
    class Light(Axis):
        P = PRESETS["flight_axis"]                              # a flight axis: duty about 0.34
    assert not speed_slack(Busy()) and lever(Busy(), "capacity") is None, "a loaded axis's speed knob stays native"
    assert speed_slack(Light()) and lever(Light(), "capacity") is not None, "an axis with slack offers its speed knob"
    for name, P in PRESETS.items():
        if "task_rate" in P:
            class Any(Axis):
                pass
            Any.P = P
            print(f"  speed knob on {name}: {'offered' if speed_slack(Any()) else 'left native (no slack)'}")
    print("PASS test_compass_arm")


if __name__ == "__main__":
    main()
