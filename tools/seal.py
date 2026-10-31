# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The seal: every law that exists in Python and in C++, locked together.

  python3 tools/seal.py            # build the C++, run every twin's parity test, and only if all pass write SEAL.json
  python3 tools/seal.py --check    # compare the files with SEAL.json (verify.py runs this)

SEAL.json (results/SEAL.json) records, for each twin, the SHA-256 of its Python file and of its C++ files, the parity
test that proved them equal, and when. A change to either side of a twin breaks the seal until its parity test passes
again and the seal is rewritten, so the Python and the C++ can never drift apart unnoticed. Mechanisms that exist in
Python only are listed too, so nobody takes them for twinned.
"""
from __future__ import annotations

import argparse, datetime, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
SEAL = ROOT / "results" / "SEAL.json"

TWINS = {
    "core engine (six-state equations)": {"python": ["omnicompass/core.py"],
        "cpp": ["cpp/src/core.cpp", "cpp/include/omnicompass/core.hpp"], "proof": "cpp/scripts/compare_results.py on fixtures/current_500_*.csv"},
    "governor (allocation laws)": {"python": ["omnicompass/adapter.py"],
        "cpp": ["cpp/src/governor.cpp", "cpp/include/omnicompass/governor.hpp"], "proof": "tests/test_cpp_governor_parity.py"},
    "safety shield": {"python": ["omnicompass/shield.py"],
        "cpp": ["cpp/src/shield.cpp", "cpp/include/omnicompass/shield.hpp"], "proof": "tests/test_cpp_shield_parity.py"},
    "HPA replica law": {"python": ["fleet/harness.py"],
        "cpp": ["cpp/src/hpa.cpp", "cpp/include/omnicompass/hpa.hpp"], "proof": "tests/test_cpp_hpa_parity.py"},
    "closure law (machines)": {"python": ["omnicompass/closure.py"],
        "cpp": ["cpp/src/closure.cpp", "cpp/include/omnicompass/closure.hpp"], "proof": "tests/test_cpp_closure_parity.py"},
    "conveyance law (the conserved budget)": {"python": ["omnicompass/conveyance.py"],
        "cpp": ["cpp/src/conveyance.cpp", "cpp/include/omnicompass/conveyance.hpp"], "proof": "tests/test_cpp_conveyance_parity.py"},
    "nervous system (authority per organ, living band)": {"python": ["omnicompass/nervous_system.py"],
        "cpp": ["cpp/src/nervous_system.cpp", "cpp/include/omnicompass/nervous_system.hpp"], "proof": "tests/test_cpp_twins_parity.py"},
    "compass and ledger (composite storage)": {"python": ["omnicompass/compass.py", "omnicompass/storage.py"],
        "cpp": ["cpp/src/compass.cpp", "cpp/include/omnicompass/compass.hpp"], "proof": "tests/test_cpp_twins_parity.py"},
    "GPU governor rules (shield limit, busy gate, speed lock, window, baseline)": {"python": ["omni_controller/gpu_governor.py"],
        "cpp": ["cpp/src/gpu_rules.cpp", "cpp/include/omnicompass/gpu_rules.hpp"], "proof": "tests/test_cpp_twins_parity.py"},
    "compass law and the two-way plug (every muscle's law, the tune-down and every live controller)": {
        "python": ["omnicompass/compass_law.py"], "cpp": ["cpp/src/compass_law.cpp", "cpp/include/omnicompass/compass_law.hpp"],
        "proof": "tests/test_cpp_compass_law_parity.py"},
    "verdict (the give-back trial, its interval reading and the steps it allows)": {
        "python": ["omnicompass/verdict.py"], "cpp": ["cpp/src/verdict.cpp", "cpp/include/omnicompass/verdict.hpp"],
        "proof": "tests/test_cpp_verdict_parity.py"},
    "Student's t (the exact two-sided 95% point every interval reads, CPython's own log-gamma)": {
        "python": ["omnicompass/student_t.py"], "cpp": ["cpp/src/student_t.cpp", "cpp/include/omnicompass/student_t.hpp"],
        "proof": "tests/test_cpp_student_t_parity.py"},
    "the edge (each muscle's balance point and wall, the cushion widened at once and narrowed slowly)": {
        "python": ["omnicompass/edge.py"], "cpp": ["cpp/src/edge.cpp", "cpp/include/omnicompass/edge.hpp"],
        "proof": "tests/test_cpp_edge_parity.py"},
    "the immune system's self-knowledge (a knob redlining that Omni-Compass cannot lift goes to native where native is stronger, "
    "stays where it is not)": {
        "python": ["omnicompass/immune.py"], "cpp": ["cpp/src/immune.cpp", "cpp/include/omnicompass/immune.hpp"],
        "proof": "tests/test_cpp_immune_parity.py"},
    "Omni direct's brain and room rule (the yardstick, the reflex, the compass, the twin, the verdict's depth, the conveyed walls, "
    "the machines, pack and spread)": {
        "python": ["omni_orchestrator/brain.py", "omni_orchestrator/scheduler.py"],
        "cpp": ["cpp/src/orchestrator_brain.cpp", "cpp/include/omnicompass/orchestrator_brain.hpp"],
        "proof": "tests/test_cpp_orchestrator_brain_parity.py"},
    "the engine's seeded runs (the Python's 500 from the jump generator, its draws the input, every twin above the mechanism)": {
        "python": ["tools/engine_runs.py"], "cpp": ["cpp/tools/engine_runs.cpp"],
        "proof": "tests/test_cpp_engine_runs_parity.py"},
    "the core's Monte Carlo (the Python's 500 RK4 runs from the jump generator, its draws the input, the core's twin the mechanism, four ways)": {
        "python": ["tools/core_runs.py"], "cpp": ["cpp/tools/core_runs.cpp"],
        "proof": "tests/test_cpp_core_runs_parity.py"},
}
PYTHON_ONLY = {
    "omni_controller/gpu_governor.py (device I/O)": "reading nvidia-smi and writing power limits; its decision rules are twinned above",
    "omni_controller/muscles.py": "Kubernetes and hardware muscles (convey, rightsize, coldstart, batch, contain, cooling, CPU/GPU connectors)",
    "omni_controller/controller.py": "Kubernetes controller (HPA target, pod reflex, machines, strict replicas)",
    "hardware/node_exchange.py": "CPU + GPU on one power budget (modelled harness; the law itself is twinned above)",
    "realms/compass_arm_v5.py": "the max, the default brain of every organism (max_apply, max_body_step, the Bone, the twins, the "
                                "heat debt); its tune-down runs the compass law, twinned above",
    "realms/harness.py, realms/plants.py": "the organisms' body and its plants (the modelled muscles the harness drives)",
    "omni_orchestrator/control.py, agent.py, cgroup.py, front.py": "Omni direct's control plane, hand, walls and front (I/O: "
                                "the machines' processes, cgroups and HTTP); its brain and room rule are twinned above",
}


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def prove():
    """Build the C++ and run every twin's parity test; raises on any failure."""
    import verify
    tmp = Path(tempfile.mkdtemp()); b = verify.build_cpp(tmp)
    subprocess.run([str(b / "oc_run_fixture"), str(ROOT / "fixtures/current_500_inputs.csv"), str(tmp / "cpp.csv")], check=True)
    subprocess.run([sys.executable, str(ROOT / "cpp/scripts/compare_results.py"), str(ROOT / "fixtures/current_500_expected.csv"),
                    str(tmp / "cpp.csv"), str(tmp / "cpp.json")], check=True, capture_output=True)
    assert json.loads((tmp / "cpp.json").read_text())["pass"], "core engine: C++ differs from the 500 fixtures"
    from tests import (test_cpp_governor_parity, test_cpp_shield_parity, test_cpp_hpa_parity, test_cpp_closure_parity,
                       test_cpp_conveyance_parity)
    for m in ("power_protect", "throughput", "fleet", "fleet_balanced", "fleet_wear"):
        test_cpp_governor_parity.main(str(b / "oc_governor"), 20, m)
    test_cpp_shield_parity.main(str(b / "oc_shield"), 8)
    test_cpp_hpa_parity.main(str(b / "oc_hpa"), (901,))
    test_cpp_closure_parity.main(str(b / "oc_closure"), 1)
    assert test_cpp_conveyance_parity.main(str(b / "oc_conveyance"), 200) < 1e-9
    from tests import test_cpp_twins_parity
    test_cpp_twins_parity.main(str(b / "oc_twins"), 2000)
    from tests import test_cpp_compass_law_parity
    test_cpp_compass_law_parity.main(str(b / "oc_compass_law"), 300)
    from tests import test_cpp_verdict_parity, test_cpp_engine_runs_parity, test_cpp_edge_parity
    test_cpp_verdict_parity.main(str(b / "oc_verdict"), 300)
    test_cpp_edge_parity.main(str(b / "oc_edge"), 400)
    from tests import test_cpp_student_t_parity
    test_cpp_student_t_parity.main(str(b / "oc_student_t"), 2000)
    from tests import test_cpp_orchestrator_brain_parity
    test_cpp_orchestrator_brain_parity.main(str(b / "oc_orchestrator_brain"), 300)
    from tests import test_cpp_immune_parity
    for seed in range(200):
        lines = test_cpp_immune_parity.script(seed)
        assert test_cpp_immune_parity.py_answers(lines) == test_cpp_immune_parity.cpp_answers(b / "oc_immune", lines), seed
    test_cpp_engine_runs_parity.main(str(b / "oc_engine_runs"), 100)
    from tests import test_cpp_core_runs_parity
    test_cpp_core_runs_parity.main(str(b / "oc_core_runs"), 100)


def check():
    """Returns a list of broken twins (empty when every sealed file is unchanged)."""
    if not SEAL.exists():
        return ["no seal: run python3 tools/seal.py"]
    seal = json.loads(SEAL.read_text()); broken = []
    for name, t in TWINS.items():
        rec = seal["twins"].get(name)
        if rec is None:
            broken.append(f"{name}: not in the seal"); continue
        for p in t["python"] + t["cpp"]:
            if rec["sha256"].get(p) != sha(p):
                broken.append(f"{name}: {p} changed since the seal ({t['proof']} must pass, then python3 tools/seal.py)")
    return broken


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        broken = check()
        print("\n".join(broken) if broken else f"seal intact: {len(TWINS)} Python/C++ twins")
        return 1 if broken else 0
    prove()
    out = {"sealed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "rule": "each twin's Python and C++ files were proven equal by its parity test before these hashes were written",
           "twins": {name: {"proof": t["proof"], "sha256": {p: sha(p) for p in t["python"] + t["cpp"]}} for name, t in TWINS.items()},
           "python_only": PYTHON_ONLY}
    SEAL.write_text(json.dumps(out, indent=1) + "\n")
    print(f"sealed {len(TWINS)} Python/C++ twins after every parity test passed; {len(PYTHON_ONLY)} mechanisms Python only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
