# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""What the brain's six-state equations change in the governor's decisions: the same input, the equations on and off.

The governor (omnicompass/adapter.py, Governor) senses, assimilates, evolves its six states (E, U, I_U, S, B, Ḃ) one macro
step of equations (1) to (7), and allocates. Its own switch, Governor.evolve, leaves the equations out and keeps every
other part. This records the observations the fleet model (fleet/sim_slo.py, the omni_fleet arm) feeds the governor,
then replays that same stream twice, the equations on and off, and counts the decisions that come out the same: the
machines added or taken away, the power cap, the change permission and the rollback authority, and the demand target.
Class S, our own model; it writes nothing.

  python3 docs/engine/brain_off.py [--seeds 101 102] [--vessel web]
"""
from __future__ import annotations

import argparse
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from omnicompass import adapter as A  # noqa: E402
from fleet import sim_slo  # noqa: E402
from fleet.harness import make_scenario  # noqa: E402


def record(vessel: str, seed: int) -> list:
    """The observations the fleet model hands the governor, decision by decision, with the equations on (as shipped)."""
    seen, step = [], A.Governor.step

    def spy(self, obs, conflicts):
        seen.append((dict(obs), conflicts))
        return step(self, obs, conflicts)

    A.Governor.step = spy
    try:
        sim_slo.run(make_scenario(vessel, seed), "omni_fleet")
    finally:
        A.Governor.step = step
    return seen


def replay(stream: list, evolve: bool) -> list:
    g = A.Governor(law=A.mode_law("fleet"))
    g.set_mode(A.AUTOPILOT)
    g.evolve = evolve
    out = []
    for obs, c in stream:
        d = g.step(obs, c)
        out.append((d["node_delta"], round(d["power_cap"], 6), d["change_permitted"], d["rollback_authorized"], float(d["demand"])))
    return out


def compare(vessel: str = "web", seeds=(101, 102)) -> dict:
    """The counts over every decision of every seed: how many come out the same with the equations off."""
    tot = {"vessel": vessel, "seeds": list(seeds), "decisions": 0, "machines": 0, "cap": 0, "permission": 0, "rollback": 0, "per_seed": []}
    diffs = []
    for seed in seeds:
        s = record(vessel, seed)
        on, off = replay(s, True), replay(s, False)
        same = [sum(1 for x, y in zip(on, off) if x[i] == y[i]) for i in range(4)]
        tot["decisions"] += len(on)
        for k, v in zip(("machines", "cap", "permission", "rollback"), same):
            tot[k] += v
        tot["per_seed"].append({"seed": seed, "decisions": len(on), "machines": same[0], "cap": same[1], "permission": same[2], "rollback": same[3]})
        diffs += [abs(x[4] - y[4]) for x, y in zip(on, off)]
    tot["demand_moved_mean"] = round(statistics.mean(diffs), 6) if diffs else None
    tot["demand_moved_max"] = round(max(diffs), 6) if diffs else None
    return tot


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seeds", type=int, nargs="+", default=[101, 102])
    ap.add_argument("--vessel", default="web")
    a = ap.parse_args()
    t = compare(a.vessel, a.seeds)
    for s in t["per_seed"]:
        print(f"{a.vessel} seed {s['seed']}: {s['decisions']} decisions; the same with the equations off: machines {s['machines']}, "
              f"power cap {s['cap']}, change permission {s['permission']}, rollback authority {s['rollback']}")
    print(f"over {t['decisions']} decisions the equations off leave the machines the same on {t['machines']}, the power cap on {t['cap']}, "
          f"the change permission on {t['permission']} and the rollback authority on {t['rollback']}; the demand target moves by "
          f"{t['demand_moved_mean']:.4f} on average (largest {t['demand_moved_max']:.4f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
