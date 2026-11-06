# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Source: GitHub Actions workflow `aks-metered`, run 37534538088, commit `f162ce8` (Omni v1, `tools/omni_version.py --commit f162ce8`), 2026-10-06/07, job `aggregate` of attempt 2, artifact `live-reps-aks`; raw files under `results/live/raw/run-37534538088/` (`aks-1` to `aks-5`). The burst sized to the cluster: the load generator's replicas stepping 1 3 1 4 1 3 over a 1,800 s window, eastus, `Standard_D2s_v4` workers (1 to 4) under Azure's own cluster autoscaler, a fresh cluster per arm, deleted after it; arms native and omni (Omni-Compass on top of native), order rotated, **5 paired repetitions**: repetition 4 lost its native cluster to an Azure API error at cluster creation ("UnmarshalEntity encountered error: EOF") in the first attempt and was run again by itself (the same commit, the same design); the first attempt's four-pair table (bill +6.3%, interval across zero) stays in the history of this file. Evidence class L, the bill metered (Azure's own count of machines every 15 s, priced at list). A single run read by `tools/live_reps.py`'s own paired interval; runs B and C to follow.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.908 | 1.946 |
| node-hours | 0.9581 | 0.9779 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 186 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 184 |
| response time (ms), mean | 500.3 | 498.6 |
| response time (ms), 95th percentile | 1090 | 1254 |
| response time (ms), 99th percentile | 5975 | 3967 |
| time over the response line (% of samples) | 34.94 | 35 |
| failed requests (%) | 22.27 | 15.58 |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 |
| time pods had no machine to take them, pod-minutes | 3.67 | 2.22 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.733 | 3.357 |
| utilisation (used / allocatable) | 0.5854 | 0.5845 |
| CPU used (cores), mean | 2.122 | 2.16 |
| Omni's own CPU (cores), mean | 0 | 0.0099 |
| CPU used with Omni's own (cores), mean | 2.122 | 2.17 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 168.6 | 169.5 |
| HPA replicas, mean | 9.702 | 9.701 |
| pods started | 5.2 | 5.2 |
| pod start wait, total (s) | 257.4 | 165 |
| pod start wait, mean (s) | 50.85 | 31.13 |
| machines billed, machine-hours | 1.088 | 1.141 |
| compute bill at list price ($) | 0.1044 | 0.1096 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.908 | 1.946 | +2.0% | -0.03781 to +0.1138 | no |
| node-hours | 0.9581 | 0.9779 | +2.1% | -0.01685 to +0.05652 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 186 | +1.6% | -0.005012 to +5.762 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 184 | +2.4% | -0.8413 to +9.457 | no |
| response time (ms), mean | 500.3 | 498.6 | -0.3% | -85.06 to +81.63 | no |
| response time (ms), 95th percentile | 1090 | 1254 | +15.0% | -579.3 to +907.1 | no |
| response time (ms), 99th percentile | 5975 | 3967 | -33.6% | -3672 to -344.7 | yes: GAIN |
| time over the response line (% of samples) | 34.94 | 35 | +0.2% | -4.175 to +4.292 | no |
| failed requests (%) | 22.27 | 15.58 | -30.0% | -18.74 to +5.363 | no |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 | -30.8% | -3.491 to +1.891 | no |
| time pods had no machine to take them, pod-minutes | 3.67 | 2.22 | -39.5% | -5.351 to +2.451 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.733 | 3.357 | -41.5% | -7.642 to +2.889 | no |
| utilisation (used / allocatable) | 0.5854 | 0.5845 | -0.2% | -0.025 to +0.02319 | no |
| CPU used (cores), mean | 2.122 | 2.16 | +1.8% | -0.01065 to +0.08666 | no |
| Omni's own CPU (cores), mean | 0 | 0.0099 | +0.0099 (native is 0) | +0.007312 to +0.01249 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.122 | 2.17 | +2.3% | -0.002528 to +0.09834 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 168.6 | 169.5 | +0.5% | -3.593 to +5.315 | no |
| HPA replicas, mean | 9.702 | 9.701 | -0.0% | -0.09167 to +0.08921 | no |
| pods started | 5.2 | 5.2 | +0.0% | -0.8778 to +0.8778 | no |
| pod start wait, total (s) | 257.4 | 165 | -35.9% | -350.8 to +166 | no |
| pod start wait, mean (s) | 50.85 | 31.13 | -38.8% | -71.89 to +32.43 | no |
| machines billed, machine-hours | 1.088 | 1.141 | +5.0% | -0.03082 to +0.1387 | no |
| compute bill at list price ($) | 0.1044 | 0.1096 | +5.0% | -0.002959 to +0.01332 | no |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
