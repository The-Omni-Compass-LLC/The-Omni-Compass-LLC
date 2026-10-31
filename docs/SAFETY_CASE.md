# The safety case: every hazard of a governor on top of native, its guard, and the evidence that the guard holds

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni-Compass writes settings that a native controller would otherwise own. A referee's first question is what happens
when it is wrong, is attacked, or dies. This page answers it hazard by hazard. Each row names the guard in the code that
stands against the hazard and the evidence that the guard holds: a test that runs on every push (`python3 verify.py`), or a
measured run (evidence class L). Where no evidence exists yet, the row says so. The page adds no mechanism; it maps the
mechanisms that are already there. Section 3 is the plug's interface, as the code defines it.

## 1. The claim this page supports

**Do no harm** (its meaning, `DISCLOSURES.md` section 3): the organism Omni-Compass governs is never left turning out less
than its native controllers make it turn out, nor less healthy (no muscle past its own limit, no service over its own line,
nothing made to fail). On the engine that stands, that means: Omni-Compass never leaves a setting other than native's after
it stops, never acts on a reading it cannot trust, never takes a step that a paired trial on the system itself showed
costs more, never exceeds a bound the system or its operator set, and can be switched off by one human action, everywhere
at once.

## 2. Hazards, guards and evidence

| # | Hazard | Guard (where it lives) | Evidence that it holds |
|---|---|---|---|
| H1 | The governor dies, hangs or loses its machine, leaving a setting changed | Before its first write, every governor records the exact commands that put every setting back, and renews a lease every decision. A watchdog finds any governor whose process is gone or whose lease is stale and runs those commands for it (`omnicompass/master.py`: `register`, `heartbeat`, `orphans`; `tools/omni_switch.py`: `watchdog`, `reclaim`) | `tests/test_master_switch.py`; the robustness kill test (the governor killed outright mid-run, every setting back within the allowance in every repetition; `docs/ROBUSTNESS_PREREGISTRATION.md`); `tests/test_robust.py`, `tests/test_robust_restart.py` |
| H2 | Someone takes over the governor, or it behaves in a way nobody intended | The kill switch: one file, one command. Every governor sees it at its next decision, writes back every setting it changed, reads each one back and exits. A governor that cannot read the switch treats that as OFF (`omnicompass/master.py`, `tools/omni_switch.py off`) | `tests/test_master_switch.py` |
| H3 | A write is refused or silently fails, so the governor's belief and the system differ | Every write goes through the plug, which reads the value back (`omnicompass/muscle_sdk.py`: `execute`, then `readback`, then a receipt). At the end of every run the reset is read back against the snapshot, and the run fails if any record is left (`scripts/kind_bench.sh`) | `tests/test_muscle_sdk.py`; every three-run table prints "handed back to native's and read back at the end of every omni arm in every run: yes" |
| H4 | It gives back too much, so service breaks when load returns | Floors read live: never below one replica, a pool never below two machines. A machine is given back only after its own trial shows the response time holds, and it wakes at once on a breach (`omni_controller/controller.py`) | `tests/test_node_release_gate.py`; the fault test (`results/live/V7_FAULTS.md`) |
| H5 | On a shared host, one tenant's raise starves the others | No CPU limit is raised while the host is 75% busy or its reading is missing; conveyance stays inside each namespace's CPU quota, and an unreadable quota means no known budget, so Kubernetes admission decides (`omni_controller/capacity.py`, `omni_controller/quota.py`) | `tests/test_capacity.py`, `tests/test_kind_capacity.py`, `tests/test_quota_convey.py`; the noisy-neighbour test (`results/live/V7_FAIRNESS.md`, STEADY) |
| H6 | It acts on a reading it cannot trust | A reading with no machine in service is blind: the decision holds, says why, and writes nothing (omni-v11, `omni_controller/controller.py`). A muscle whose reading is stale reports BLIND, and no command is executed (`omnicompass/muscle_sdk.py`: `MuscleStatus`) | `tests/test_blind_reading.py` (the fault reproduced on omni-v10, gone on omni-v11); `results/model_gate/V11_VS_V10.md`; the extended fault test, the API server frozen and the metrics server gone (queued, A, B and C: `docs/K8S_COMPASS_PREREGISTRATION.md`) |
| H7 | It keeps a step that hurts the system | One trial at a time, on the system itself: a reference phase at the deepest step already allowed, then one notch further. The step is refused if its median cost exceeds the reference's by more than 2%, or the cost first measured at the operator's setting. Refused steps wait 60 s; a trial is abandoned if the service swings (`tools/knob_verdict.py`) | `tests/test_knob_verdict.py`, `tests/test_verdict.py`, `tests/test_verdict_interval.py`; every database table prints each trial's count, allowance and refusal |
| H8 | It writes outside what the operator allows | A capability contract (minimum, maximum, resolution, step and rate limits) and a safety contract (hard bounds, forbidden contexts, fail closed) on every muscle (`omnicompass/muscle_sdk.py`: `CapabilityContract`, `SafetyContract`) | `tests/test_muscle_sdk.py` |
| H9 | It uses more privilege than its job needs | Least-privilege service account (`deploy/kind/rbac-omni.yaml`), and every arm records what it can and cannot do (`kubectl auth can-i`, `rbac_omni.txt` in each run's folder) | The receipts in every run folder on the branch `raw` |
| H10 | It expands while a security hold is on | The shield: no expansion during a security hold (invariant I1), with a C++ twin checked against the Python (`omnicompass/shield.py`, `cpp/`) | `tests/test_shield_properties.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_shield_adversarial.py` |
| H11 | In the cloud, it raises the bill for the same work | The bill is judged, never ruled (the founder's order of 31 October struck the machines-alone rule of 14 October): every cloud set reads the bill beside the work it bought by the one key, the cloud's judged number the work per dollar: a factory tune whose work per dollar falls against native (a bigger bill for the same work) is not admissible (`docs/THE_TUNE.md`) and is a fault of the tune, root-caused in the model first; the machine lever asks the cloud for no machine (`scripts/kind_nodepool.sh`); paid sets capped at 100 repetitions and 1, 10 and 100 copies | Azure: no difference in the bill on the engine of 13 October, at the tune-down on the machines alone (`results/live/AKS_BILL.md`); the sets at the max wait, held, for the load whose work grows with the speed (the work meter), so each reads the work per dollar. Google and Amazon: **undetermined**, not yet run. |
| H12 | A test machine's limit is reported as the governor's effect | Paired arms on the same runner, rotated order, the refusal rules for an unhealthy window, and the kind rig's image pre-puller (`docs/POD_START_WAIT.md`). `tools/confirm_abc.py` marks any table whose runs differ in engine or rig | `tests/test_confirm_abc.py`, `tests/test_pod_phases.py`, `tests/test_release_campaign.py` |
| H13 | The hand-back itself is turned against the system: a record another local user planted makes the watchdog run a command or stop a process, or a governor's pid given to another process gets that process stopped | The watchdog acts only on records of its own user that no other user can write, read without following a link; a pid counts as the governor's only while its process started before the governor registered (`tools/omni_switch.py`, 18 October). Every threat of misuse is set out in `docs/THREAT_MODEL.md` | `tests/test_switch_trust.py` (each fault reproduced on the tool as it stood, gone on the fix) |

## 3. The plug, as the code defines it

Every muscle is reached through one interface (`omnicompass/muscle_sdk.py`, `MuscleAdapter`). The sequence is fixed:
observe, bound, request, execute, read back, receipt, restore.

| Call | What it must do |
|---|---|
| `observe()` | Return the muscle's reading with its timestamp; a reading older than its timing contract makes the muscle BLIND |
| `snapshot_native()` | Capture native's setting once, before the first write; this is what every restore returns to |
| `execute(value)` | Write one value, already clamped by the capability contract and permitted by the safety contract |
| `readback()` | Read the value the system actually holds; a mismatch is recorded, never assumed away |
| `restore_native(snapshot)` | Put native's setting back, then read it back |

Each muscle carries three contracts: timing (observation and decision periods, actuation delay, the age after which a
reading is stale, the minimum hold and cool-down between writes), capability (range, resolution, step and rate limits,
reversible, read back) and safety (hard bounds, forbidden contexts, fail closed, a safe default). A muscle built on the SDK
cannot be declared without all three. It starts in recommend mode and writes only when set to automatic or approved from
outside; every command, written or refused, leaves a receipt with the reason, the reading's age, the value asked, the value
bounded, the value the system holds and the difference between the last two (`MuscleRuntime.command`).

## 4. What this case does not yet cover

- **No outside security review or penetration test.** H2, H9, H10 and H13 rest on our own tests; the threats still open are listed in `docs/THREAT_MODEL.md`, section 3.
- **No formal proof of the whole controller.** The theorems in `docs/TRACKING_THEOREM.md` hold for the compass law's
  channel; global stability of the full six-state system is open (`docs/FORMAL_STATUS.md`).
- **No production deployment.** Every hazard above is exercised on our own rigs (kind on GitHub runners, Azure's managed
  Kubernetes, the database servers in our workflows), not on a customer's system.
- **Physical plants.** The GPU's power and clock guards and every facility muscle are exercised only in our models or a
  stand-in card until the chip runs exist (undetermined).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
