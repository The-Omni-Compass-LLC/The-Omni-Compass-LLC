# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The swarm runner (tools/run_swarm.py) without the simulator: the task keeps every path clear of the other depot columns
and depots apart; a drone flown perfectly along its carrot finishes every mission inside its deadline; the override stays
inside its guards, rises only with slack and falls to the planner's cruise at the wall or near another drone, and is handed
back; the energy model is the declared one and the same in both arms; the whole mission plan is deterministic."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omnicompass.compass_law import Band, CompassLaw
from tools import run_swarm as S


def fly_perfect(drone, lag=0.0, nearest=float("inf")):
    """Feed the drone its own carrot back as its position (a perfect autopilot, optionally lagging by `lag` metres)."""
    pos = tuple(drone.home); t = 0.0
    while drone.phase != "finished" and t < 10_000:
        tp, _ = drone.step(pos, (14468.0,) * 4, nearest)
        cx, cy, cz = tp
        pos = (cx - lag, cy, cz)
        t += S.CTRL_DT
    return drone


def main():
    # the task: paths clear of the other spots of the depot, depots far apart, the same plan twice
    ms1 = S.missions(20, 4, (3.0, 8.0), 12); ms2 = S.missions(20, 4, (3.0, 8.0), 12)
    assert ms1 == ms2, "the mission plan is fixed by the seed"
    for i, ms in enumerate(ms1):
        x0, y0, _ = S.depot(i)
        for tx, ty, d in ms:
            assert 3.0 - 1e-9 <= d <= 8.0 + 1e-9 and abs(math.dist((x0, y0), (tx, ty)) - d) < 1e-9
            for j in range(20):
                if j != i and j // 5 == i // 5:
                    ox, oy, _ = S.depot(j)
                    assert S._seg_dist(ox, oy, x0, y0, tx, ty) >= S.KEEPOUT, "a path keeps clear of the other columns of its depot"
    assert S.depot(5)[0] - S.depot(4)[0] >= S.DEPOT_GAP - S.DEPOT_PITCH * 4 and S.DEPOT_GAP >= 2 * 8.0 + 1.0, "depots never share airspace"
    assert len(set(S.ALT[:5])) == 5 and min(b - a for a, b in zip(S.ALT, S.ALT[1:])) >= 0.3 - 1e-9, "one altitude per spot, 0.3 m apart"
    # native: a perfect autopilot finishes every mission inside its deadline, no late mission, the override untouched
    d = fly_perfect(S.Drone(0, ms1[0], None))
    assert len(d.done) == 4 and not any(r["late"] for r in d.done) and all(r["mission_s"] <= r["line_s"] for r in d.done)
    assert all(abs(o - 1.0) < 1e-12 for o in d.ov), "native never moves the override"
    # omni with no tracking error: the compass spends the slack as speed, inside the guards, faster missions, handed back
    law = CompassLaw(Band(0.0, S.E_LINE), dt=S.CTRL_DT, tau=S.TAU, kp=S.KP, smooth=S.SMOOTH)
    o = fly_perfect(S.Drone(0, ms1[0], law))
    assert len(o.done) == 4 and not any(r["late"] for r in o.done)
    assert all(S.O_MIN - 1e-12 <= v <= S.O_MAX + 1e-12 for v in o.ov), "the override stays inside its guards"
    assert max(o.ov) > 1.2 and sum(r["mission_s"] for r in o.done) < sum(r["mission_s"] for r in d.done), "slack is spent as speed: shorter missions"
    assert all(abs(o.ov[k + 1] - o.ov[k]) <= S.SLEW + 1e-12 or o.ov[k + 1] == S.O_MIN for k in range(len(o.ov) - 1)), \
        "one slew step a tick, except the hand-back to the planner's cruise at each landing"
    assert abs(o.override - 1.0) < 1e-12, "handed back to the planner's cruise after the last mission"
    # omni at the wall: a lag at the safe error, or another drone too close, holds the planner's cruise
    law2 = CompassLaw(Band(0.0, S.E_LINE), dt=S.CTRL_DT, tau=S.TAU, kp=S.KP, smooth=S.SMOOTH)
    w = fly_perfect(S.Drone(1, ms1[1], law2), lag=S.E_LINE)
    assert max(w.ov) <= S.O_MIN + S.SLEW + 1e-9, "at the wall the cruise is the planner's"
    law3 = CompassLaw(Band(0.0, S.E_LINE), dt=S.CTRL_DT, tau=S.TAU, kp=S.KP, smooth=S.SMOOTH)
    c = fly_perfect(S.Drone(2, ms1[2], law3), nearest=S.SEP_WALL / 2)
    assert max(c.ov) <= S.O_MIN + S.SLEW + 1e-9, "another drone inside the separation wall holds the planner's cruise"
    # the energy model: the declared formula, the same for both arms, grows with rpm
    e = S.Drone(0, ms1[0], None); e.motor_energy((10_000.0,) * 4, 7.94e-12, 1.0)
    want = 4 * 7.94e-12 * 1e8 * (2 * math.pi * 1e4 / 60) / S.MOTOR_EFF
    assert abs(e.energy - want) < 1e-9, "torque KM rpm^2 times angular speed, over the motor efficiency"
    e2 = S.Drone(0, ms1[0], None); e2.motor_energy((20_000.0,) * 4, 7.94e-12, 1.0)
    assert e2.energy > 7 * e.energy, "power rises as the cube of rpm"
    assert S.planned_time(8.0, 2.0) == 2 * 1.9 / S.VZ + 16.0 / S.V_PLAN + S.HOVER_S + S.SETTLE_S
    print("PASS  swarm runner: paths clear of the depot columns and depots apart, every mission inside its deadline under a perfect autopilot, "
          "the override inside its guards (slack spent as speed, the planner's cruise at the wall and near another drone) and handed back, "
          "the declared energy model, deterministic plan")


if __name__ == "__main__":
    main()
