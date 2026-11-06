# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1]))
from omnicompass.disruption_budget import allowed_downs, apply_node_delta
from omnicompass.ce_score import all_sweeps


def test_allowed_downs():
    assert allowed_downs(10, 10.0) == 1
    assert allowed_downs(10, 10.0, abs_cap=1) == 1
    assert allowed_downs(3, 10.0) == 1


def test_apply_clips_to_budget():
    d, used, blocked = apply_node_delta(-5, 0, 2)
    assert d == -2 and used == 2 and blocked is False
    d, used, blocked = apply_node_delta(-1, 2, 2)
    assert d == 0 and blocked is True


def test_ce_sweeps_present():
    row = dict(replica_change_units=10, evictions=1, node_starts=2, node_stops=2,
               request_changes=0, replica_reversals=1, power_cap_travel=0)
    s = all_sweeps(row)
    assert "balanced" in s and s["node_heavy"] >= s["balanced"]


def main():
    """Run every test in this file (it also runs under pytest)."""
    import inspect, pathlib, tempfile
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            args = [pathlib.Path(tempfile.mkdtemp()) for p in inspect.signature(fn).parameters if p == "tmp_path"]
            fn(*args); n += 1
    print(f"PASS {pathlib.Path(__file__).stem}: {n} tests")


if __name__ == "__main__":
    main()
