# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1]))
from omnicompass.muscle_sdk import (
    AutomationMode, CapabilityContract, Evidence, FunctionalMuscle, MuscleRegistry,
    MuscleRuntime, MuscleSpec, Observation, SafetyContract, TimingContract,
)


def adapter(mode=AutomationMode.AUTOMATIC):
    state = {"v": 100.0}
    spec = MuscleSpec(
        muscle_id="test.gpu", plant_id="plant0", resource_type="gpu.power_limit", adapter_version="1",
        capability=CapabilityContract(50, 200, resolution=1, max_step=20, units="W"),
        timing=TimingContract(.2, 2, stale_after_s=5),
        safety=SafetyContract(60, 190, forbidden=("security_hold",)),
        automation=mode, evidence=Evidence.SIMULATION,
    )
    return state, FunctionalMuscle(
        spec, lambda: Observation(state["v"]), lambda v: state.__setitem__("v", v),
        lambda: state["v"], lambda: state["v"], lambda snap: state.__setitem__("v", snap),
    )


def test_bound_readback_receipt_restore():
    state, a = adapter()
    r = MuscleRuntime(a)
    x = r.command(180)
    assert x.permitted and x.bounded == 180 and x.realized == 180 and x.actuator_residual == 0
    y = r.command(250)  # max_step wins after hard capability clamp: 180 -> 200, then safety blocks >190
    assert not y.permitted and y.reason == "outside_hard_bounds"
    state["v"] = 170
    z = r.restore()
    assert z.restored and state["v"] == 100


def test_recommend_never_writes():
    state, a = adapter(AutomationMode.RECOMMEND)
    r = MuscleRuntime(a)
    x = r.command(80)
    assert not x.permitted and x.reason == "recommend" and state["v"] == 100


def test_forbidden_context_blocks():
    state, a = adapter()
    x = MuscleRuntime(a).command(90, context={"security_hold": True})
    assert not x.permitted and x.reason == "forbidden:security_hold" and state["v"] == 100


def test_registry_catalog_and_restore():
    state, a = adapter()
    reg = MuscleRegistry(); reg.register(MuscleRuntime(a))
    assert reg.catalog()[0]["resource_type"] == "gpu.power_limit"
    reg.command("test.gpu", 120)
    assert state["v"] == 120
    assert reg.restore_all()["test.gpu"].restored
    assert state["v"] == 100


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
