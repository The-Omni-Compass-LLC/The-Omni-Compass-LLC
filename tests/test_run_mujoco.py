# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The robot runner (tools/run_mujoco.py) on a two-link arm written here (no download): the planned speed is set so the
arm's own servo tracks the task; the paired physics trial decides whether Omni moves; the standing draw is charged for
the whole takt in both arms; the override stays inside its guards and is handed back and read back every cycle; no cycle
crosses the takt; and the whole run is deterministic."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_mujoco as R

TWO_LINK = """<mujoco model="twolink">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>
  <worldbody>
    <body name="l1" pos="0 0 0.5">
      <joint name="j1" type="hinge" axis="0 1 0" range="-1.5 1.5"/>
      <geom type="capsule" fromto="0 0 0 0.3 0 0" size="0.03" mass="2"/>
      <body name="l2" pos="0.3 0 0">
        <joint name="j2" type="hinge" axis="0 1 0" range="-1.5 1.5"/>
        <geom type="capsule" fromto="0 0 0 0.25 0 0" size="0.025" mass="1"/>
      </body>
    </body>
  </worldbody>
  <actuator>
    <position name="a1" joint="j1" kp="300" kv="30" ctrlrange="-1.5 1.5" forcerange="-100 100"/>
    <position name="a2" joint="j2" kp="100" kv="10" ctrlrange="-1.5 1.5" forcerange="-50 50"/>
  </actuator>
  <keyframe><key name="home" qpos="0.2 -0.4" ctrl="0.2 -0.4"/></keyframe>
</mujoco>
"""


def main():
    with tempfile.TemporaryDirectory() as t:
        men = Path(t) / "menagerie"; (men / "twolink").mkdir(parents=True)
        (men / "twolink" / "scene.xml").write_text(TWO_LINK)
        out1, out2 = Path(t) / "o1", Path(t) / "o2"
        r1 = R.run_robot(men, "twolink", 3, out1)
        r2 = R.run_robot(men, "twolink", 3, out2)
        def result(r):                       # the wall-clock bookkeeping ("seconds") is not part of the result
            return json.dumps({k: ({kk: vv for kk, vv in v.items() if kk != "seconds"} if isinstance(v, dict) else v)
                               for k, v in r.items()}, sort_keys=True)
        assert result(r1) == result(r2), "the run is deterministic"
        n, o = r1["native"], r1["omni"]
        assert r1["native_tracking_at_planned_speed"] <= R.TRACK_OK, "the task is one the arm's own servo can track"
        assert abs(n["standing_j"] - r1["energy_model"]["idle_w"] * r1["line_s"]) < 1e-9 and n["standing_j"] == o["standing_j"], \
            "the standing draw is charged for the whole takt in both arms"
        assert o["handed_back"] and n["handed_back"], "the override is handed back and read back every cycle"
        assert n["over_line_share"] == 0.0 and o["over_line_share"] == 0.0, "no cycle crosses the takt"
        assert R.OVERRIDE_MIN <= o["override_mean"] <= R.OVERRIDE_MAX
        trial = r1["physics_trial"]
        assert trial["slower_is_cheaper"] == (trial["override_0.8"]["energy_j"] < trial["full_speed"]["energy_j"])
        if r1["omni_moves"]:
            assert o["cycle_s"] > n["cycle_s"] and o["cycle_s"] <= r1["line_s"], "omni slows inside the takt"
            assert o["mechanical_j"] + o["copper_j"] < n["mechanical_j"] + n["copper_j"], "and the motion energy is lower"
        else:
            assert o["cycle_s"] == n["cycle_s"] and o["energy_j"] == n["energy_j"], "left native: both arms identical"
        assert (out1 / "twolink.json").exists() and (out1 / "twolink_cycles.csv").exists() and (out1 / "MUJOCO.md").exists() is False
        R.report({"twolink": r1}, out1)
        assert (out1 / "MUJOCO.md").exists() and "declared model" in (out1 / "MUJOCO.md").read_text()
    print(f"PASS  robot runner: feasible speed set by the arm's own servo, the paired trial decides whether Omni moves ({'moved' if r1['omni_moves'] else 'left native'}), "
          "standing draw per takt in both arms, override inside its guards and handed back, no cycle over the takt, deterministic")


if __name__ == "__main__":
    main()
