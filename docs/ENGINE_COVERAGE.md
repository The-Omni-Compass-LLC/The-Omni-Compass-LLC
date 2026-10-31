# How much of the engine the tests run

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Line coverage of every Python file in the engine that stands (omni-v23), under the whole test suite: the unittest suite and every file `tools/function_tests.py` runs. Measured with coverage.py by `python3 tools/engine_coverage.py --measure` on commit `2b1390a7dc02`; `tools/engine_coverage.py --check`, run by `verify.py`, fails a push where this page is not what `results/ENGINE_COVERAGE.json` records.

**71% of the engine's 11,424 statements run under the tests** (8,148 run, 3,276 not). Coverage counts lines a test executes, not what it asserts: the properties the tests check are in `tests/test_engine_properties.py`, and the proofs of the core in `docs/ENGINE_PROOFS.md`.

The 8 runners omni-v15 took into the fingerprint (the data stores', the swarm's, MuJoCo's and the CPU power runner, `tools/run_*.py`) hold 3,623 of these statements, 51% of them run under the tests: each is run whole by its own benchmark on GitHub, A, B and C, rather than by a unit test. The other 45 Python files, the engine as it stood before them, hold 7,801, 81% run. The whole figure fell when those runners came in; no test was lost.

| Engine file | Statements | Run by the tests | Coverage |
|---|---:|---:|---:|
| `tools/run_pgbench.py` | 657 | 146 | 22% |
| `tools/run_citylearn.py` | 166 | 41 | 25% |
| `omnicompass/stack_sim.py` | 210 | 55 | 26% |
| `omni_orchestrator/control.py` | 476 | 176 | 37% |
| `omnicompass/closure.py` | 151 | 61 | 40% |
| `omnicompass/speed.py` | 60 | 25 | 42% |
| `omnicompass/mathdrive.py` | 50 | 22 | 44% |
| `tools/run_redis.py` | 427 | 210 | 49% |
| `tools/run_kafka.py` | 579 | 285 | 49% |
| `omnicompass/shield.py` | 79 | 41 | 52% |
| `tools/run_swarm.py` | 257 | 134 | 52% |
| `tools/run_sysbench.py` | 433 | 226 | 52% |
| `tools/run_ycsb.py` | 511 | 267 | 52% |
| `tools/run_kil.py` | 132 | 94 | 71% |
| `realms/plants.py` | 645 | 461 | 71% |
| `omnicompass/master.py` | 77 | 58 | 75% |
| `omnicompass/adapter.py` | 207 | 157 | 76% |
| `omni_controller/gpu_compass.py` | 295 | 227 | 77% |
| `tools/run_cpu_power.py` | 554 | 427 | 77% |
| `tools/run_mujoco.py` | 205 | 165 | 80% |
| `realms/harness.py` | 425 | 359 | 84% |
| `omni_controller/quota.py` | 86 | 75 | 87% |
| `omnicompass/compass.py` | 82 | 75 | 91% |
| `omni_controller/controller.py` | 1,200 | 1,098 | 92% |
| `realms/compass_arm_v5.py` | 838 | 771 | 92% |
| `omnicompass/conveyance.py` | 52 | 48 | 92% |
| `omnicompass/muscle_sdk.py` | 215 | 199 | 93% |
| `omnicompass/edge.py` | 56 | 52 | 93% |
| `tools/store_brain.py` | 102 | 95 | 93% |
| `omnicompass/configurations.py` | 31 | 29 | 94% |
| `omni_controller/capacity.py` | 63 | 59 | 94% |
| `omnicompass/disruption_budget.py` | 16 | 15 | 94% |
| `omnicompass/storage.py` | 32 | 30 | 94% |
| `omni_controller/gpu_governor.py` | 354 | 332 | 94% |
| `omnicompass/student_t.py` | 52 | 49 | 94% |
| `omni_controller/muscles.py` | 621 | 586 | 94% |
| `omnicompass/compass_law.py` | 95 | 90 | 95% |
| `realms/compass_arm.py` | 107 | 102 | 95% |
| `omnicompass/authority_contract.py` | 26 | 25 | 96% |
| `omni_orchestrator/brain.py` | 58 | 56 | 97% |
| `omnicompass/core.py` | 159 | 154 | 97% |
| `realms/gpu_card.py` | 172 | 167 | 97% |
| `omnicompass/nervous_system.py` | 69 | 67 | 97% |
| `tools/knob_verdict.py` | 117 | 114 | 97% |
| `omnicompass/immune.py` | 47 | 46 | 98% |
| `omnicompass/verdict.py` | 109 | 108 | 99% |
| `omni_orchestrator/scheduler.py` | 21 | 21 | 100% |
| `omnicompass/ce_score.py` | 7 | 7 | 100% |
| `realms/presets.py` | 41 | 41 | 100% |

## Where the tests reach least

Files under 60%: `tools/run_pgbench.py`, `tools/run_citylearn.py`, `omnicompass/stack_sim.py`, `omni_orchestrator/control.py`, `omnicompass/closure.py`, `omnicompass/speed.py`, `omnicompass/mathdrive.py`, `tools/run_redis.py`, `tools/run_kafka.py`, `omnicompass/shield.py`, `tools/run_swarm.py`, `tools/run_sysbench.py`, `tools/run_ycsb.py`. The CityLearn runner and the runners of the data stores and the swarm are exercised by their own benchmarks on GitHub (`citylearn.yml`, `redis.yml` and the rest, three runs on every engine) rather than by a unit test; the stack simulator, the shield and the speed and mathdrive modules hold paths the live governors do not call. Raising each to the level of the rest is the next tests' work: no engine file changes for a test.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
