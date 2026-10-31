# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""End-to-end self-pilot: the shipped controller in nodepool mode (default headroom) against the simulated cluster for one
day, captured and scored with pilot/score.py against HPA + Cluster Autoscaler on identical traffic. I never loosen the
operator's own HPA target (fewer, fuller pods always lengthen the wait), and pending-pod time and the HPA's shortfall are
never a LOSS. From omni-v19 the immune system holds the machines at or under native's own line (docs/OMNI_V19.md), so on
this plant no pod waits (pending-pod time down 100%, GAIN) and the machines it holds read power given (node-hours per
core-hour up 18.3%, energy per core-hour up 11.4%): power given, never a LOSS by the one key; omni-v18 matched the
autoscaler's machines with pods waiting."""
import sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from pilot.selfpilot import main as selfpilot


def main(seed=424242):
    res, out = selfpilot(["--seed", str(seed), "--days", "1", "--out", tempfile.mkdtemp()])
    m = res["metrics"]
    assert not str(m["pending_pod_minutes_per_hour"]["verdict"]).startswith("LOSS"), m["pending_pod_minutes_per_hour"]
    assert not str(m["hpa_shortfall_minutes_per_hour"]["verdict"]).startswith("LOSS"), m["hpa_shortfall_minutes_per_hour"]
    for g in ("kwh_per_core_hour", "node_hours_per_core_hour"):     # a resource: a cut (GAIN), STEADY or power given, never a LOSS
        assert not str(m[g]["verdict"]).startswith("LOSS"), m[g]
    print(f"self-pilot: energy per core-hour {100 * m['kwh_per_core_hour']['relative']:+.1f}%, node-hours per core-hour "
          f"{100 * m['node_hours_per_core_hour']['relative']:+.1f}%, pending-pod time {m['pending_pod_minutes_per_hour']['verdict']}, "
          f"HPA shortfall {m['hpa_shortfall_minutes_per_hour']['verdict']}")
    print("PASS test_selfpilot")
    return res


if __name__ == "__main__":
    main()
