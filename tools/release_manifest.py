# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The release's one identity: RELEASE_MANIFEST.json.

  python3 tools/release_manifest.py           # write the manifest, run verify.py --quick, record its receipt
  python3 tools/release_manifest.py --check   # compare the files with the manifest (verify.py runs this)

The manifest names the commit it was written at and fingerprints (SHA-256) everything that identifies the release: the
canonical engine and the reference engine, the C++ twins (through the seal), the GPU protocol, the live evidence
(execution commit, run id and raw-file digests of sets 20 and 21), the canonical engine declaration, and the receipt
of the verification run made when it was written. One object, so nobody has to reconstruct provenance from history.
"""
from __future__ import annotations

import argparse, datetime, hashlib, json, subprocess, sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # `python tools/release_manifest.py` imports tools.legal (the front-page bot)

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "RELEASE_MANIFEST.json"
RECEIPT = ROOT / "results" / "VERIFY_RECEIPT.txt"

GROUPS = {
    "benchmark_integrity": ["tools/bench_integrity.py", "tests/test_bench_integrity.py", "pilot/bench_report.py",
                            "scripts/kind_bench.sh", "scripts/kind_paired.sh", "scripts/aks_paired.sh",
                            ".github/workflows/six-kube.yml", "docs/REPAIR_20261029.md",
                            "tools/omni_switch.py", "scripts/kind_faults.sh", "tests/test_faults_extended.py",
                            "tests/test_switch_trust.py", "verify.py"],
    "engine_v8_citylearn": ["OMNI_V8.json", "tools/run_citylearn.py", "docs/OMNI_V8.md", "docs/CITYLEARN_PREREGISTRATION.md"],
    "engine_v23": ["OMNI_V23.json", "tools/omni_version.py", "docs/OMNI_V23.md", "omni_controller/controller.py",
                   "tests/test_own_replicas.py", "results/model_gate/V23_VS_V22.md", "results/model_gate/V23_VS_V22.json",
                   "deploy/kind/rbac-omni.yaml", "scripts/kind_bench.sh", "tests/test_kind_rig_rbac.py", "docs/SOLO_PREREGISTRATION.md"],
    "engine_v22": ["OMNI_V22.json", "tools/omni_version.py", "docs/OMNI_V22.md", "tools/store_brain.py", "tools/knob_verdict.py",
                   "tools/run_sysbench.py", "tools/run_ycsb.py", "tools/run_redis.py", "tools/run_kafka.py", "tools/run_pgbench.py",
                   "tools/store_gate.py", "tools/kafka_model.py", "tools/redis_model.py", "tests/test_store_brain.py", "tests/test_redis_twin.py",
                   "tests/test_kafka_twin.py", "results/model_gate/V22_STORE_GATE.md", "results/model_gate/V22_STORE_GATE.json",
                   "results/model_gate/V22_REDIS_MODEL.md", "results/model_gate/V22_KAFKA_MODEL.md", "results/model_gate/V22_KAFKA_MODEL_UNTOUCHED.md",
                   "results/model_gate/V22_KAFKA_MODEL_20S.md", "docs/STORE_ROOT_CAUSES_2026-10-30.md", "docs/MYSQL_PREREGISTRATION.md",
                   "docs/YCSB_PREREGISTRATION.md", "docs/POSTGRES_PREREGISTRATION.md", "docs/REDIS_PREREGISTRATION.md", "docs/KAFKA_PREREGISTRATION.md"],
    "engine_v21": ["OMNI_V21.json", "tools/omni_version.py", "docs/OMNI_V21.md"],   # extend with the files omni-v21 changed
    "engine_v20": ["OMNI_V20.json", "tools/omni_version.py", "docs/OMNI_V20.md", "tools/run_sysbench.py", "tools/run_kafka.py", "tools/run_ycsb.py", "tools/run_redis.py", "tools/run_pgbench.py", ".github/workflows/pgbench.yml", "tools/store_gate.py", "results/model_gate/STORE_GATE.md", "results/model_gate/STORE_GATE.json", "tests/test_store_wires.py", "tests/test_store_gate.py", "docs/STORE_LOSS_ROOT_CAUSES_2026-10-25.md"],
    "engine_v19": ["OMNI_V19.json", "tools/omni_version.py", "docs/OMNI_V19.md", "omni_controller/controller.py", "realms/harness.py",
                   "realms/plants.py", "tests/test_own_replicas.py", "results/model_gate/V19_VS_V18.md", "results/model_gate/V19_VS_V18.json",
                   "results/model_gate/SOLO_V19.md", "results/model_gate/SOLO_V19.json", "results/model_gate/SOLO_V19_VS_V18.md",
                   "results/model_gate/SOLO_V19_VS_V18.json", "docs/SOLO_PREREGISTRATION.md", "tools/solo_study.py", "scripts/kind_bench.sh",
                   "fleet/capture/kube_capture.sh", "tools/confirm_abc.py", "tools/live_reps.py", "tools/run_realms_v5.py"],
    "engine_v18": ["OMNI_V18.json", "tools/omni_version.py", "docs/OMNI_V18.md"],   # extend with the files omni-v18 changed
    "engine_v17": ["OMNI_V17.json", "tools/omni_version.py", "docs/OMNI_V17.md", "omni_controller/controller.py",
                   "tests/test_pace_clocks.py", "tests/test_time_correct.py", "tools/beat_ladder.py", "tests/test_beat_ladder.py",
                   "tools/model_gate.py", "results/model_gate/V17_VS_V16.md", "results/model_gate/V17_VS_V16.json",
                   "results/model_gate/V17_LADDER.md", "results/model_gate/V17_LADDER.json", "docs/PACE_PREREGISTRATION.md",
                   "docs/K8S_COMPASS_PREREGISTRATION.md", "scripts/kind_bench.sh", "scripts/kind_paired.sh", "scripts/kind_robust.sh",
                   "scripts/kind_levers.sh", "scripts/kind_full.sh", "scripts/kind_pilot.sh", "deploy/install/omni-compass.yaml",
                   "deploy/install/omni-compass-cloud.yaml", "deploy/controller.yaml", "tools/live_reps.py", "tools/confirm_abc.py",
                   "tools/omni_exporter.py", "tests/test_omni_exporter.py", "tools/omni_control.py", "tests/test_omni_control.py",
                   "deploy/prometheus/omni-compass-rules.yaml", "deploy/grafana/omni-compass.json", "docs/OBSERVABILITY.md",
                   "docs/engine/build_live_engine.py", "docs/CHANGE_CONTROL.md", "docs/THE_TUNE.md",
                   "tools/tune_study.py", "tests/test_tune_study.py", "DISCLOSURES.md"],
    "engine_v16": ["OMNI_V16.json", "tools/omni_version.py", "docs/OMNI_V16.md", "omnicompass/adapter.py", "omnicompass/edge.py",
                   "omni_controller/controller.py", "omni_controller/muscles.py", "omni_controller/capacity.py",
                   "cpp/include/omnicompass/governor.hpp", "cpp/src/governor.cpp", "cpp/tools/run_governor.cpp",
                   "tests/test_cpp_governor_parity.py", "tests/test_pace_clocks.py", "tests/test_loop_schedule.py", "tools/model_gate.py",
                   "results/model_gate/V16_VS_V15.md", "results/model_gate/V16_VS_V15.json", "results/model_gate/V16_PACE.md",
                   "results/model_gate/V16_PACE.json", "docs/PACE_PREREGISTRATION.md", "scripts/kind_paired.sh", "scripts/kind_bench.sh",
                   "tools/live_reps.py", "tools/confirm_abc.py", "docs/CHANGE_CONTROL.md", "results/SEAL.json",
                   "results/LOCK_AMENDMENTS.json"],
    "engine_v15": ["OMNI_V15.json", "tools/omni_version.py", "docs/OMNI_V15.md", "omnicompass/adapter.py",
                   "omni_controller/gpu_governor.py", "cpp/include/omnicompass/governor.hpp", "cpp/src/governor.cpp",
                   "cpp/tools/run_governor.cpp", "cpp/tools/engine_runs.cpp", "tests/test_cap_band.py",
                   "tests/fixtures/robust_long_39173420146_decisions.json", "tests/test_cpp_governor_parity.py", "tools/model_gate.py",
                   "results/model_gate/V15_VS_V14.md", "results/model_gate/V15_VS_V14.json", "tools/live_reps.py", "tests/test_robust.py",
                   "docs/ROBUSTNESS_PREREGISTRATION.md", "docs/CHANGE_CONTROL.md", "docs/MECHANISM_OF_ACTION.md", "results/SEAL.json"],
    "engine_v14": ["OMNI_V14.json", "tools/omni_version.py", "docs/OMNI_V14.md", "omni_controller/controller.py",
                   "omni_controller/muscles.py", "tools/wall_meter.py", "tools/omni_control.py", "tests/test_native_muscles.py",
                   "tests/test_operator_cmd.py", "results/model_gate/V14_VS_V13.md", "results/model_gate/V14_VS_V13.json",
                   "tools/model_gate.py"],
    "cpp_twin_compass_law": ["cpp/include/omnicompass/compass_law.hpp", "cpp/src/compass_law.cpp", "cpp/tools/run_compass_law.cpp",
                             "cpp/CMakeLists.txt", "tests/test_cpp_compass_law_parity.py", "docs/engine/export_cpp_twins.py",
                             "tools/seal.py", "results/SEAL.json"],
    "cpp_engine_runs": ["cpp/include/omnicompass/verdict.hpp", "cpp/src/verdict.cpp", "cpp/tools/run_verdict.cpp",
                        "cpp/tools/engine_runs.cpp", "cpp/include/omnicompass/governor.hpp", "cpp/src/governor.cpp",
                        "tests/test_cpp_verdict_parity.py", "tests/test_cpp_engine_runs_parity.py", "tools/engine_runs.py",
                        ".github/workflows/engine-runs.yml"],
    "engine_v13": ["OMNI_V13.json", "tools/omni_version.py", "docs/OMNI_V13.md", "omni_controller/muscles.py", "tests/test_convey_handback.py",
                   "results/model_gate/V13_VS_V12.md", "results/model_gate/V13_VS_V12.json"],
    "engine_v12_refused_raise": ["OMNI_V12.json", "omni_controller/muscles.py", "tools/omni_version.py", "docs/OMNI_V12.md",
                                 "tools/run_swarm.py", "tests/test_refused_raise.py", "results/model_gate/V12_VS_V11.md",
                                 "results/model_gate/V12_SWARM_REFLEX.md", "docs/SWARM_PREREGISTRATION.md", "tools/swarm_abc.py"],
    "engine_v11_blind_reading": ["OMNI_V11.json", "omni_controller/controller.py", "tools/omni_version.py", "docs/OMNI_V11.md",
                                 "docs/K8S_COMPASS_PREREGISTRATION.md", "tests/test_blind_reading.py", "results/model_gate/V11_VS_V10.md",
                                 "tools/model_gate.py", "tests/test_model_gate_tree.py", "tools/land_engine.py", "tests/test_land_engine.py"],
    "engine_v10_citylearn": ["OMNI_V10.json", "tools/run_citylearn.py", "tools/omni_version.py", "docs/OMNI_V10.md",
                             "docs/CITYLEARN_PREREGISTRATION.md", "results/model_gate/V10_VS_V9.md"],
    "engine_v9_citylearn": ["OMNI_V9.json", "tools/run_citylearn.py", "omnicompass/student_t.py", "realms/harness.py", "docs/OMNI_V9.md",
                            "docs/CITYLEARN_PREREGISTRATION.md", "results/model_gate/V9_VS_V8.md"],
    "quota_v7_candidate": ["OMNI_V7.json", "omni_controller/quota.py", "tests/test_quota_convey.py", "docs/OMNI_V7.md", "tools/mechanism_identity.py", "tests/standin_cluster/kubectl", "tools/layout_check.py"],
    "release_operations": ["tools/release_manifest.py", "scripts/aks_kubectl.py", "tests/test_manifest_refresh.py", "tests/test_aks_kubectl.py"],
    "engine_v6_campaign": ["OMNI_V6.json", "omni_controller/capacity.py", "omni_controller/controller.py",
                           "scripts/dispatch_grid.py", "scripts/reruns.txt", "scripts/benchmark_campaign.json",
                           "scripts/restart_aks.py", ".github/aks_restart_request.json",
                           "scripts/azure_capacity.py", "tests/test_azure_capacity.py", "docs/AZURE_REPAIR_2026-10-15.md",
                           "tools/artifact_legal.py", "tools/wire_artifact_legal.py", "tests/test_artifact_legal.py", "tests/test_robust_restart.py", "docs/REPAIR_STATUS_2026-10-15.md", "results/repair_20261015/STATUS.json",
                           "scripts/gpu_campaign_profiles.json", "docs/OMNI_V6.md", "tests/test_release_campaign.py",
                           "tools/run_realms_v5.py", "tools/run_scale.py", "tools/pool_scale.py", "tools/run_hil.py"],
    "benchmark_workflows": sorted(str(p.relative_to(ROOT)) for p in (ROOT / ".github" / "workflows").glob("*.yml")),
    "canonical_engine": ["omnicompass/core.py", "cpp/src/core.cpp", "docs/CANONICAL_ENGINE.md"],
    "reference_engine": ["reference/omni_compass_reference_engine.py", "reference/PROVENANCE.json"],
    "cpp_twins_seal": ["results/SEAL.json"],
    "gpu_protocol": ["docs/GPU_PREREGISTRATION.md", "scripts/gpu_paired.sh", "tools/gpu_workload.py", "tools/gpu_reps.py",
                     "omni_controller/gpu_governor.py", "omnicompass/adapter.py", "omni_controller/muscles.py"],
    "live_set_20": ["results/live/LIVE_REPS_20.md", "results/live/SET20_RAW_SHA256SUMS_ALL.txt"],
    "live_set_21": ["results/live/LIVE_REPS_21.md", "results/live/SET21_ARTIFACTS.json"],
    "live_set_22": ["results/live/LIVE_REPS_22.md", "results/live/SET22_ARTIFACTS.json",
                    "results/live/reaggregated/LIVE_REPS_36488547793.md"],
    "preregistration": ["results/PREREGISTRATION.json", "results/LOCK_AMENDMENTS.json"],
    "mechanism": ["results/MECHANISM_IDENTITY.json", "tools/mechanism_identity.py", "docs/TRACKING_THEOREM.md",
                  "tools/tracking_bounds.py", "results/TRACKING_BOUNDS.json", "docs/EVIDENCE_LEDGER.md", "results/OMNI_INDEX.md"],
    "live_set_23": ["results/live/LIVE_REPS_23.md"],
    "live_set_24": ["results/live/LIVE_REPS_24.md"],
    "live_set_25": ["results/live/LIVE_REPS_25.md"],
    "live_set_26": ["results/live/LIVE_REPS_26.md", "docs/K8S_COMPASS_PREREGISTRATION.md"],
    "live_set_27": ["results/live/LIVE_REPS_27.md"],
    "compass_law": ["omnicompass/disruption_budget.py", "omnicompass/muscle_sdk.py", "omnicompass/authority_contract.py", "omnicompass/ce_score.py", "tools/causal_evidence_gate.py", "tools/gpu_physical_preflight.py", "tools/gpu_dcgm_observer.sh", "tools/gpu_evidence_dashboard.py", "tools/validate_gpu_physical_evidence.py", "tools/gpu_actuator_watchdog.py", "tools/authority_matrix.py", "tests/test_disruption_budget.py", "tests/test_muscle_sdk.py", "tests/test_causal_evidence_gate.py", "tests/test_gpu_watchdog.py", "scripts/kind_faults.sh", "scripts/aks_paired.sh", ".github/workflows/aks-metered.yml", "tests/test_api_proxy.py", "tests/test_cost_to_match.py", "omnicompass/compass_law.py", "omnicompass/verdict.py", "tests/test_verdict.py", "omnicompass/master.py", "tools/omni_switch.py", "tests/test_master_switch.py", "realms/compass_arm.py", "omni_controller/gpu_compass.py", "tools/gpu_wire_check.py",
                 "realms/gpu_card.py", "results/sim/gpu_two_wire/RESULT.json"],
    "gpu_rented_run": ["scripts/gpu_rented_run.sh", "scripts/gpu_8card.sh", "tools/wall_meter.py", "tests/test_server_power.py", "scripts/gpu_fault_drill.sh", "scripts/gpu_vllm.sh", "tools/llm_workload.py", "tools/run_hil.py", "tests/standin_gpu/nvidia-smi", "tools/run_kil.py", "tools/omni_index.py", "tools/layout_check.py", "tests/test_staging_order.py", "tests/test_cruise_idle.py", "deploy/kind/batch-jobs.yaml", "tools/run_citylearn.py", "docs/CITYLEARN_PREREGISTRATION.md", ".github/workflows/citylearn.yml", "tools/run_pandapower.py", "docs/PANDAPOWER_PREREGISTRATION.md", "docs/REGISTER.md", ".github/workflows/pandapower.yml", "tools/six_kube_report.py", ".github/workflows/six-kube.yml", "tests/test_six_kube.py"],
    "kwok_scale": ["scripts/kwok_scale.sh", "deploy/kwok/kubectl_kwok.sh", "tools/kwok_report.py", ".github/workflows/kwok-scale.yml"],
    "six_organisms": ["tools/run_scale.py", "tools/pool_scale.py", "scripts/scale_ladder.sh", ".github/workflows/six.yml",
                      "results/scale/GRID.md", "tools/grid.py", "results/scale/receipts/v3-1x.md", "results/scale/v1/GRID.md", "results/scale/v1/receipts/round6-1x.md", "results/scale/v1/receipts/round6-10x.md", "docs/HOW_TO_READ_THE_RESULTS.md"],
    "license": ["LICENSE", "NOTICE", "DISCLOSURES.md", "LICENSING_FAQ.md", "THIRD_PARTY_NOTICES.md", "PATENTS.md",
                "TRADEMARKS.md"],
    "repository_standards": ["docs/REPOSITORY_STANDARDS.md", "codemeta.json", "sbom/omni-compass.cdx.json", ".github/SECURITY_CONTACTS",
                             ".snyk", "pyproject.toml"],
    "muscle_catalog": ["docs/MUSCLE_CATALOG.md", "tools/muscle_catalog.py"],
    "realms": ["realms/catalog.csv", "realms/plants.py", "realms/presets.py", "realms/harness.py",
               "tools/realms_catalog.py", "tools/run_realms.py", "docs/REALMS_PREREGISTRATION.md"],
}
# engine components checked identical to this release's at each execution commit (tools/mechanism_identity.py
# components F, C, h, G, dt, recomputed from the source at that commit); the Kubernetes actuator map and shield are as
# at the execution commit
SAME = ["F", "C", "h", "G", "dt"]
LIVE = {
    "set_20": {"run_id": 36366603505, "execution_commit": "18220d4", "repetitions": 10, "plant": "kind (GitHub Actions)",
               "engine_components_identical_to_release": SAME,
               "raw": "run-36366603505/ on the branch raw (its SHA256SUMS_ALL.txt, kept on main as results/live/SET20_RAW_SHA256SUMS_ALL.txt, covers every file)"},
    "set_21": {"run_id": 36466558583, "execution_commit": "9e64f7b", "repetitions": 10, "plant": "kind (GitHub Actions)",
               "engine_components_identical_to_release": SAME,
               "raw": "GitHub artifacts, digests in results/live/SET21_ARTIFACTS.json; recomputed by reaggregate run 36485672281"},
    "set_22": {"run_id": 36488547793, "execution_commit": "cfdc17c", "repetitions": 10, "plant": "kind (GitHub Actions)",
               "load": "open-loop, fixed rate (equal work)", "engine_components_identical_to_release": SAME,
               "raw": "GitHub artifacts, digests in results/live/SET22_ARTIFACTS.json; recomputed by the reaggregate workflow"},
}


GENERATED_REPORTS = {
    'results/OMNI_INDEX.md', 'results/OMNI_INDEX.json', 'docs/BENEFIT_SHEET.md',
    'results/BENEFIT_SHEET.json', 'docs/WIRING_VERDICTS.md', 'results/WIRING_VERDICTS.csv',
    'docs/DOSSIER.md',
}


def refresh_generated(baseline_reader=None):
    """Refresh derived reports or exact legal normalization, never engine/test/protocol changes.

    Validate the whole change set before writing. Existing verification receipts remain historical;
    this operation does not run verification and never declares that it passed.
    """
    manifest = json.loads(MANIFEST.read_text())
    def baseline(path):
        return subprocess.run(['git', 'show', f'HEAD:{path}'], cwd=ROOT, capture_output=True, check=True).stdout
    reader = baseline_reader or baseline
    updates = {}
    for files in manifest['files'].values():
        for name, expected in files.items():
            path = ROOT / name
            if not path.is_file():
                continue  # sparse checkout: absent historical evidence is not re-sealed
            data = path.read_bytes()
            actual = hashlib.sha256(data).hexdigest()
            if actual == expected or name in updates:
                continue
            old = reader(name)
            if hashlib.sha256(old).hexdigest() != expected:
                raise ValueError(f'{name}: baseline already differs from the manifest; explicit repair required')
            generated = name in GENERATED_REPORTS or bool(re.fullmatch(
                r'results/live/V\d+_(?:REDIS|KAFKA|PGBENCH|SYSBENCH|YCSB)(?:_SERVICE)?\.md', name))
            legal_only = False
            if name.endswith('.md') and name.startswith(('docs/', 'results/')):
                from tools.legal import normalize_markdown
                legal_only = normalize_markdown(old.decode('utf-8'))[0].encode('utf-8') == data
            if not (generated or legal_only):
                raise ValueError(f'{name}: automatic refresh cannot re-seal source, tests, protocols or edited evidence')
            updates[name] = actual
    for files in manifest['files'].values():
        for name in files.keys() & updates.keys():
            files[name] = updates[name]
    if updates:
        manifest['generated_refresh'] = {'files': sorted(updates), 'verification': 'not run by this refresh'}
        MANIFEST.write_text(json.dumps(manifest, indent=1) + '\n')
    return sorted(updates)


def sha_files(paths):
    h = hashlib.sha256()
    for p in paths:
        h.update(p.encode() + b"\0" + (ROOT / p).read_bytes())
    return h.hexdigest()


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def git_head():
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()


def check():
    """Returns a list of mismatches (empty when every fingerprinted file matches)."""
    if not MANIFEST.exists():
        return ["no RELEASE_MANIFEST.json: run python3 tools/release_manifest.py"]
    m = json.loads(MANIFEST.read_text()); bad = []
    for group, files in m["files"].items():
        for p, h in files.items():
            if not (ROOT / p).exists():
                bad.append(f"{group}: {p} is missing")
            elif sha(p) != h:
                bad.append(f"{group}: {p} changed since the manifest (python3 tools/release_manifest.py)")
    r = m.get("verification_receipt")
    if r and (not RECEIPT.exists() or sha(RECEIPT.relative_to(ROOT)) != r["sha256"]):
        bad.append("verification receipt: results/VERIFY_RECEIPT.txt differs from the manifest")
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument('--refresh-generated', action='store_true', help='update only derived-report/legal-normalization hashes; never declare verification passed')
    a = ap.parse_args(argv)
    if a.refresh_generated:
        print('Generated manifest hashes refreshed: ' + ', '.join(refresh_generated()))
        return 0
    if a.check:
        bad = check()
        print("\n".join(bad) if bad else "release manifest matches the files")
        return 1 if bad else 0
    mi = json.loads((ROOT / "results" / "MECHANISM_IDENTITY.json").read_text())
    canon = mi["configurations"][mi["canonical"]]
    tests = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "tests").glob("test_*.py")) + ["verify.py"]
    head = git_head()
    m = {"release": "Omni-Compass", "release_id": f"omni-compass-{head[:12]}", "written_at_commit": head,
         "written_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
         "canonical_engine": "symmetric_verified (docs/CANONICAL_ENGINE.md)",
         "mechanism_id": canon["mechanism_id"], "mechanism_configuration": mi["canonical"],
         "mechanism_components": canon["components"],
         "alternative_embodiments": {n: c["mechanism_id"] for n, c in mi["configurations"].items() if not c["canonical"]},
         "fingerprints": {"engine_sha256": sha("omnicompass/core.py"), "cpp_sha256": sha("cpp/src/core.cpp"),
                          "controller_sha256": sha("omni_controller/controller.py"),
                          "observation_map_sha256": canon["components"]["h"], "authority_map_sha256": canon["components"]["G"],
                          "actuator_map_sha256": canon["components"]["M_act"], "shield_sha256": sha("omnicompass/shield.py"),
                          "gpu_protocol_sha256": sha_files(GROUPS["gpu_protocol"]),
                          "preregistration_sha256": sha_files(GROUPS["preregistration"] + ["docs/GPU_PREREGISTRATION.md"]),
                          "test_suite_sha256": sha_files(tests)},
         "files": {g: {p: sha(p) for p in fs} for g, fs in GROUPS.items()},
         "live_evidence": LIVE,
         "physical_meter_results": ("NVIDIA A100 SXM4 40 GB on Lambda, 2026-10-24, omni-v18's card governor (commit e3b05dc), one run of "
                                    "10 paired repetitions (results/gpu/run-20261024T091235Z/GPU_REPS.md): every service gauge STEADY "
                                    "(work per energy up 0.2%, the 95th percentile up 0.2%, requests served the same), the temperature "
                                    "up 1.4% to 1.5% (power given); the governor wrote nothing, both knobs at their top on native (at its "
                                    "limit on native). The NVIDIA A10 run of 2026-10-02 (results/gpu/run-20261002T082232Z, the "
                                    "card controller of commit c908054, replaced since) stays as its own record")}
    MANIFEST.write_text(json.dumps(m, indent=1) + "\n")
    r = subprocess.run([sys.executable, str(ROOT / "verify.py"), "--quick"], capture_output=True, text=True, cwd=ROOT)
    RECEIPT.write_text(f"verify.py --quick at commit {m['written_at_commit']}, {m['written_at']}\n\n" + r.stdout)
    ok = r.returncode == 0 and "VERIFICATION: PASS" in r.stdout
    if not ok:
        # a run that stops part way keeps its reason: the exit code and the last lines it wrote to stderr
        err = "\n".join(r.stderr.strip().splitlines()[-40:])
        (ROOT / "results" / "VERIFY_FAILURE.txt").write_text(f"exit code {r.returncode}\n\n{err}\n")
        print(f"verify.py stopped (exit {r.returncode}); its last stderr lines are in results/VERIFY_FAILURE.txt")
    elif (ROOT / "results" / "VERIFY_FAILURE.txt").exists():
        (ROOT / "results" / "VERIFY_FAILURE.txt").unlink()
    m["verification_receipt"] = {"file": "results/VERIFY_RECEIPT.txt", "sha256": sha("results/VERIFY_RECEIPT.txt"), "passed": ok}
    MANIFEST.write_text(json.dumps(m, indent=1) + "\n")
    print(f"RELEASE_MANIFEST.json written at {m['written_at_commit'][:12]}; verification {'PASS' if ok else 'FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
