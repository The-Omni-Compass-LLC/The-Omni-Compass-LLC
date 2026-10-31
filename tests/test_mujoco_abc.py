# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The robot arms' A/B/C rule (tools/mujoco_abc.py): a deterministic simulator, so the three runs must reproduce; a gauge
reads GAIN or LOSS in all three of our runs by what it is for when they do (energy and force are resources spent: a rise reads
power given), STEADY under one part in a million, "the runs differ" when they do not; any added tracking error or cycle over the
takt reads LOSS; a robot the paired trial left native is listed as nothing
for Omni to move; a robot the task could not run on is listed with the reason."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import mujoco_abc as M


def arm(**kw):
    base = {"cycle_s": 8.0, "energy_j": 1000.0, "mechanical_j": 200.0, "copper_j": 100.0, "standing_j": 700.0, "peak_torque_nm": 50.0,
            "mean_abs_torque_nm": 10.0, "tracking_rms_rad": 0.04, "waypoint_err_rad": 0.005, "override_mean": 1.0, "over_line_share": 0.0,
            "handed_back": True, "cycles": 10}
    base.update(kw); return base


def rec(moves=True, **omni):
    return {"robot": "x", "joints": 2, "planned_s": 8.0, "line_s": 12.0, "omni_moves": moves,
            "physics_trial": {"full_speed": arm(), "override_0.8": arm(mechanical_j=190.0, copper_j=95.0), "slower_is_cheaper": moves},
            "native": arm(), "omni": arm(**omni)}


def main():
    same = rec(energy_j=990.0, copper_j=90.0, tracking_rms_rad=0.03, peak_torque_nm=45.0, cycle_s=10.0, override_mean=0.78)
    assert M.verdict([same] * 3, "energy_j", "lower") == "**GAIN in all three of our runs**", "energy cut is a GAIN"
    assert M.verdict([same] * 3, "tracking_rms_rad", "never more") == "**GAIN in all three of our runs**"
    more = rec(tracking_rms_rad=0.05, over_line_share=0.1)
    assert M.verdict([more] * 3, "tracking_rms_rad", "never more") == "**LOSS in all three of our runs**", "more tracking error is a LOSS"
    assert M.verdict([more] * 3, "over_line_share", "never more") == "**LOSS in all three of our runs**", "a cycle over the takt is a LOSS"
    assert M.verdict([rec(copper_j=110.0)] * 3, "copper_j", "spent") == "**power given in all three of our runs**", "more copper heating is power given"
    assert M.verdict([same] * 3, "standing_j", "lower") == "STEADY, the same"
    assert M.verdict([same] * 3, "cycle_s", "shown") == "shown, not judged"
    other = rec(energy_j=991.0)
    assert M.verdict([same, same, other], "energy_j", "lower") == "**the runs differ**"
    with tempfile.TemporaryDirectory() as t:
        dirs = []
        for i in (1, 2, 3):
            d = Path(t) / f"run-{i}"
            for name, r in (("moved", same), ("idle", rec(moves=False)), ("broken", {"robot": "broken", "error": "RuntimeError: cannot track"})):
                (d / f"mujoco-{name}").mkdir(parents=True); (d / f"mujoco-{name}" / f"{name}.json").write_text(json.dumps(r))
            dirs.append(str(d))
        out = Path(t) / "V1.md"
        assert M.main(dirs + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "### moved" in txt and "GAIN in all three of our runs" in txt
        assert "| copper heating per cycle (J, I²R, declared model) | 1 | 0 | 0 | 0 | 0 |" in txt, "the count across the robots"
        assert "| idle | 300.0 | 285.0 | yes |" in txt, "the robot the trial left native is listed as nothing to move"
        assert "| broken | `RuntimeError: cannot track` |" in txt
        assert "Not one engine's three runs" in txt
    print("PASS  robot arms A/B/C rule: reproduced runs read GAIN, STEADY or LOSS by what each gauge is for, a run that differs is a finding, added tracking error or a "
          "cycle over the takt is a LOSS, a robot left native is nothing to move, a robot that cannot run is listed")


if __name__ == "__main__":
    main()
