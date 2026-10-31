# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The drone swarms' A/B/C rule (tools/swarm_abc.py): a deterministic simulator, so the three runs must reproduce; a gauge
reads GAIN or LOSS in all three of our runs by what it is for when they do (energy is a resource spent: a rise reads power given),
STEADY under one part in a million, "the runs differ" when they do not; a late mission, a reserve breach or a near miss added is a
LOSS; a
cell the paired trial left native is nothing for Omni to move; a cell with a collision is void; the tuning cell is shown
and not counted."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import swarm_abc as M


def arm(**kw):
    base = {"energy_per_mission_j": 450.0, "fleet_energy_j": 9000.0, "missions_per_charge": 5.9, "late_share": 0.0, "reserve_breaches": 0,
            "near_miss_ticks": 0, "min_separation_m": 0.37, "tracking_rms_m": 0.07, "mission_s": 20.0, "airborne_s": 19.0, "override_mean": 1.0,
            "collisions": 0, "handed_back": True, "missions_flown": 20}
    base.update(kw); return base


def rec(cell="mixed", moves=True, void=False, tuning=False, **omni):
    o = arm(**omni)
    return {"cell": cell, "drones": 20, "missions_per_drone": 4, "distance_m": [3.0, 8.0], "tuning": tuning, "omni_moves": moves, "void": void,
            "physics_trial": {"planner_cruise": arm(), "override_1.25": arm(energy_per_mission_j=400.0), "faster_is_cheaper": moves},
            "native": arm(collisions=1 if void else 0), "omni": o}


def main():
    moved = rec(energy_per_mission_j=380.0, fleet_energy_j=7700.0, missions_per_charge=7.0, tracking_rms_m=0.14, min_separation_m=0.18, override_mean=1.5, mission_s=15.0)
    assert M.verdict([moved] * 3, "energy_per_mission_j", "lower") == "**GAIN in all three of our runs**", "energy cut is a GAIN"
    assert M.verdict([moved] * 3, "missions_per_charge", "higher") == "**GAIN in all three of our runs**", "more missions a charge is a GAIN"
    assert M.verdict([moved] * 3, "late_share", "never more") == "STEADY, the same"
    assert M.verdict([moved] * 3, "min_separation_m", "shown") == "shown, not judged"
    more = rec(late_share=0.05, reserve_breaches=1, near_miss_ticks=3, missions_per_charge=5.0)
    assert M.verdict([more] * 3, "late_share", "never more") == "**LOSS in all three of our runs**", "a late mission added is a LOSS"
    assert M.verdict([more] * 3, "reserve_breaches", "never more") == "**LOSS in all three of our runs**"
    assert M.verdict([more] * 3, "near_miss_ticks", "never more") == "**LOSS in all three of our runs**"
    assert M.verdict([more] * 3, "missions_per_charge", "higher") == "**LOSS in all three of our runs**", "fewer missions a charge is a LOSS"
    other = rec(energy_per_mission_j=381.0)
    assert M.verdict([moved, moved, other], "energy_per_mission_j", "lower") == "**the runs differ**"
    with tempfile.TemporaryDirectory() as t:
        dirs = []
        for i in (1, 2, 3):
            d = Path(t) / f"run-{i}"
            for name, r in (("mixed", moved), ("tuning", rec("tuning", tuning=True, energy_per_mission_j=390.0)),
                            ("short", rec("short", moves=False)), ("long", rec("long", void=True))):
                (d / f"swarm-{name}").mkdir(parents=True); (d / f"swarm-{name}" / f"swarm-{name}.json").write_text(json.dumps(r))
            dirs.append(str(d))
        out = Path(t) / "V3.md"
        assert M.main(dirs + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "### mixed" in txt and "### tuning" in txt and "GAIN in all three of our runs" in txt
        assert "| short | 450.0 | 400.0 | yes |" in txt, "the cell the trial left native is listed as nothing to move"
        assert "| long | a collision in an arm" in txt, "a collision voids the cell"
        across = txt[txt.index("## Across the untouched cells"):txt.index("## Cells where the paired trial")]
        assert "| energy per mission (J, declared model: motors and avionics over the fleet window) | 1 | 0 | 0 | 0 | 0 |" in across, "the tuning cell is not counted"
        assert "Not three runs on one frozen engine" in txt
        assert "collisions)" not in txt, "the tables before omni-v12 are rebuilt as they were scored, with no collision row"
    # amendment 2, from omni-v12's runs on: only a cell where native collides is void; a collision Omni-Compass adds is a judged LOSS
    from unittest import mock
    crash = rec(energy_per_mission_j=380.0, fleet_energy_j=7700.0, missions_per_charge=7.0, collisions=2)
    with tempfile.TemporaryDirectory() as t, mock.patch.object(M, "engine", return_value=("0123456789ab", "omni-v12 (digest d38b58fbe28939b8, 47 files)")):
        dirs = []
        for i in (1, 2, 3):
            d = Path(t) / f"run-{i}"
            for name, r in (("mixed", crash), ("long", rec("long", void=True))):
                (d / f"swarm-{name}").mkdir(parents=True); (d / f"swarm-{name}" / f"swarm-{name}.json").write_text(json.dumps(r))
            dirs.append(str(d))
        out = Path(t) / "V12.md"
        assert M.main(dirs + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "(Omni v12)" in txt and "amendment 2" in txt
        assert "| control ticks with two drones under two collision radii (collisions) | 0 | 2 | +2.000 | +2.000 | +2.000 | **LOSS in all three of our runs** |" in txt, \
            "a collision with Omni-Compass on top is a judged LOSS, not a void cell"
        assert "| long | native collided" in txt, "a cell where native itself collides is void"
    print("PASS  drone swarms A/B/C rule: reproduced runs read GAIN, STEADY or LOSS by what each gauge is for, a run that differs is a finding, a late mission, "
          "a reserve breach or a near miss added is a LOSS, a cell left native is nothing to move, a collision voids the cell, the tuning cell is not counted; "
          "from omni-v12 on a collision Omni-Compass adds is a judged LOSS and only native's own collision voids a cell")


if __name__ == "__main__":
    main()
