# Referee Checklist

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The standards a reviewer holds a performance or efficiency claim to, and where this repository meets each one. Where
it does not yet, the line says so. Sources of the standards: the ACM artifact review and badging criteria (available,
functional, reusable, results reproduced), the disclosure rules of industry benchmarks such as MLPerf and SPEC power
(fixed workload, full system description, every run reported, metering method stated), and common reproducibility
checklists for experimental computer science (code, data, seeds, environment, statistics, preregistration).

## 1. Availability

| Requirement | Where it is met | Status |
|---|---|---|
| Source code available to the reviewer | the repository (GitHub's Download ZIP gives the whole tree at any commit) | met (evaluation license) |
| License terms stated plainly, at entry and at exit | `LICENSE`, `NOTICE`, `REUSE.toml`; the notice at the start and end of every document and printed by every run command | met |
| A single starting point | `START_HERE.md` | met |

## 2. Functional: it runs and checks itself

| Requirement | Where it is met | Status |
|---|---|---|
| One command runs every test and integrity check | `python3 verify.py --quick`; its receipt `results/VERIFY_RECEIPT.txt` | met (0 failures) |
| The engine's two implementations agree | Python and C++ twins proven equal, value for value, and sealed (`results/SEAL.json`, `tools/seal.py`) | met |
| Every file of the release fingerprinted | `RELEASE_MANIFEST.json` | met |
| The environment can be rebuilt exactly | `requirements.txt` (ranges) and `requirements-lock.txt` (the exact versions the receipt passed with) | met |
| Safe to run on a real system | watch mode, the master switch (`tools/omni_switch.py`), the watchdog, the GPU fault drill, the Kubernetes fault test | met |

## 3. Reusable: a stranger can apply it

| Requirement | Where it is met | Status |
|---|---|---|
| How to wire it onto a stack, step by step | the manual, parts III and IV; `docs/GPU_RUN_GUIDE.md`; `docs/AZURE_SETUP.md` | met |
| How to plug in a new knob | `docs/specs/UNIVERSAL_MUSCLE_SDK.md`, `omnicompass/muscle_sdk.py` | met |
| How to read every result | the manual, chapter 11; `docs/HOW_TO_READ_THE_RESULTS.md` | met |

## 4. Experimental design

| Requirement | Where it is met | Status |
|---|---|---|
| The comparator is the real alternative | every arm is native alone against the same native with Omni-Compass on top (`DISCLOSURES.md`) | met |
| Equal work in every arm | fixed-rate (open-loop) load on Kubernetes; the same seeded request stream on the GPU | met |
| Paired runs, order rotated | `scripts/kind_paired.sh`, `scripts/gpu_paired.sh` | met |
| Written before the run | `docs/K8S_COMPASS_PREREGISTRATION.md`, `docs/GPU_PREREGISTRATION.md`, `docs/REALMS_PREREGISTRATION.md`, with every change and its reason | met |
| One rule decides the label, by code | `DISCLOSURES.md`, section 3; the label printed by `tools/live_reps.py`, `tools/gpu_reps.py` | met |
| Every run reported, including the ones that went wrong | earlier sets and the first GPU law kept in `results/`; the fault test's first two runs and their fixes recorded | met |
| A control arm that measures the cost of being there | the watch arm (Omni-Compass decides, writes nothing) on the GPU | met |
| The native comparator includes its own autoscaling of machines | the bill run on Azure with Azure's own autoscaler: no difference in the bill either way at this load (`results/live/AKS_BILL.md`) | **met: measured, no saving shown** |
| Behaviour under heavy load, not only light load | the capacity test: compass law +34.1% and, +51.9% after the first amendment; after the second, +41.4% (compass) and +44.8% (allocation law) with no LOSS clear of the noise (`results/live/CAPACITY.md`, `CAPACITY_2.md`, `AMENDMENT_2_RUNS.md`) | **met (compass law and allocation law)** |
| Many tenants on one cluster: one surging must not starve its neighbour | the fairness test: neighbour unharmed; compass failures higher, fixed by the amendment; after the second amendment the compass law has no LOSS for either application; the allocation law raises the neighbour's failures (`results/live/FAIRNESS.md`, `FAIRNESS_2.md`, `AMENDMENT_2_RUNS.md`) | **met (compass law); open (allocation law)** |
| Workloads beyond the synthetic one | real AI serving (vLLM) on the card; public data-center traces | vLLM in the card run; **traces open** |

## 5. Statistics

| Requirement | Where it is met | Status |
|---|---|---|
| Uncertainty on every number | paired differences with t-based 95% intervals (`tools/live_reps.py`, `tools/gpu_reps.py`, `realms/harness.py`) | met |
| Enough repetitions | 10 paired repetitions per Kubernetes set; 10 per GPU counted run; up to 1,000 runs per grid cell | met |
| Many measures compared at once | every measure is shown with its interval; labels use preregistered primary measures and guardrails, not the best of many | met; a family-wise correction is not applied and is disclosed here |
| The noise between identical arms measured | the watch arm on the GPU; repeated sets on Kubernetes | met |

## 6. Measurement

| Requirement | Where it is met | Status |
|---|---|---|
| The metering method stated for every energy number | evidence classes T, V, S, L, P in the manual, chapter 11; every receipt states measured or modelled | met |
| Device meter on hardware | the GPU's own power reading, sampled every 200 ms, and its energy counter | met (P class) |
| Whole-machine meter | the wall plug and the server's own BMC (Redfish, IPMI) readers (`tools/wall_meter.py`) | built; used where the host allows |
| A modelled number never presented as a meter | the kind energy rows carry "declared model" in their names | met |

## 7. Independence

| Requirement | Where it is met | Status |
|---|---|---|
| A second implementation of the native comparator | an independent HPA implementation (`tests/third_party/hpa_independent.py`) | met |
| Results reproduced by someone outside the company | the replication commands in `START_HERE.md` | **open** |
| Independent simulators built by others (buildings, energy grids) | BOPTEST and CityLearn with Omni-Compass on top of their own baseline controllers | **open** |

## 8. What this repository does not yet claim

Energy savings in watts on real hardware beyond the first card run; a lower bill on a real cloud (measured: no difference at
the load tested);
results reproduced by an outside party. Each has its test built and written down before it runs, and each result will
be published as it comes, whatever it says.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
