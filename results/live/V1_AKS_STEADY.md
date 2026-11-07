# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Source: GitHub Actions workflow `aks-metered`, run 37385657374, commit `f162ce8` (Omni v1, `tools/omni_version.py --commit f162ce8`), 2026-10-05/06, job `aggregate` (112491175079), artifact `live-reps-aks`; raw files under `results/live/raw/run-37385657374/` (`aks-1` to `aks-5`, each with both arms' capture, response-time and audit files). Steady load (the load generator's replica count fixed), eastus, `Standard_D2s_v4` workers under Azure's own cluster autoscaler, a fresh cluster per arm, deleted after it; arms native and omni (Omni-Compass on top of native), order rotated, 5 paired repetitions; repetitions 3 to 5 were re-run after the first attempt lost them to the regional vCPU quota while the big-organism machine was up. Evidence class L, the bill metered (Azure's own count of machines every 15 s, priced at list). A single run read by `tools/live_reps.py`'s own paired interval; the three-run A/B/C reading waits for runs B and C.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.849 | 1.902 |
| node-hours | 0.4648 | 0.4831 |
| energy, parked workers still on at idle power (Wh, declared model) | 94.1 | 93.73 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.75 | 84.24 |
| response time (ms), mean | 503.6 | 507.2 |
| response time (ms), 95th percentile | 1079 | 1056 |
| response time (ms), 99th percentile | 4918 | 4634 |
| time over the response line (% of samples) | 27.21 | 28.09 |
| failed requests (%) | 5.144 | 3.485 |
| pods with no machine to take them (unschedulable) | 2.8 | 3 |
| time pods had no machine to take them, pod-minutes | 3.21 | 3.69 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.337 | 6.55 |
| utilisation (used / allocatable) | 0.4831 | 0.4675 |
| CPU used (cores), mean | 1.682 | 1.681 |
| Omni's own CPU (cores), mean | 0 | 0.01446 |
| CPU used with Omni's own (cores), mean | 1.682 | 1.696 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 198 | 197.3 |
| HPA replicas, mean | 9.294 | 9.564 |
| pods started | 5.2 | 5 |
| pod start wait, total (s) | 231.2 | 263 |
| pod start wait, mean (s) | 44.95 | 52.6 |
| machines billed, machine-hours | 0.6622 | 0.6312 |
| compute bill at list price ($) | 0.06357 | 0.06059 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.849 | 1.902 | +2.8% | -0.3088 to +0.414 | no |
| node-hours | 0.4648 | 0.4831 | +3.9% | -0.07144 to +0.1079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 94.1 | 93.73 | -0.4% | -38.87 to +38.12 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.75 | 84.24 | +0.6% | -11.42 to +12.41 | no |
| response time (ms), mean | 503.6 | 507.2 | +0.7% | -110.3 to +117.4 | no |
| response time (ms), 95th percentile | 1079 | 1056 | -2.1% | -405.6 to +360.1 | no |
| response time (ms), 99th percentile | 4918 | 4634 | -5.8% | -4823 to +4256 | no |
| time over the response line (% of samples) | 27.21 | 28.09 | +3.3% | -3.523 to +5.298 | no |
| failed requests (%) | 5.144 | 3.485 | -32.3% | -4.266 to +0.948 | no |
| pods with no machine to take them (unschedulable) | 2.8 | 3 | +7.1% | -0.3552 to +0.7552 | no |
| time pods had no machine to take them, pod-minutes | 3.21 | 3.69 | +15.0% | -1.091 to +2.051 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.337 | 6.55 | +3.4% | -1.521 to +1.947 | no |
| utilisation (used / allocatable) | 0.4831 | 0.4675 | -3.2% | -0.107 to +0.07583 | no |
| CPU used (cores), mean | 1.682 | 1.681 | -0.0% | -0.03797 to +0.03726 | no |
| Omni's own CPU (cores), mean | 0 | 0.01446 | +0.0145 (native is 0) | +0.01296 to +0.01596 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.682 | 1.696 | +0.8% | -0.02439 to +0.05261 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 198 | 197.3 | -0.3% | -31.62 to +30.36 | no |
| HPA replicas, mean | 9.294 | 9.564 | +2.9% | -0.1062 to +0.6459 | no |
| pods started | 5.2 | 5 | -3.8% | -0.7552 to +0.3552 | no |
| pod start wait, total (s) | 231.2 | 263 | +13.8% | -58.05 to +121.7 | no |
| pod start wait, mean (s) | 44.95 | 52.6 | +17.0% | -11.6 to +26.9 | no |
| machines billed, machine-hours | 0.6622 | 0.6312 | -4.7% | -0.2911 to +0.2291 | no |
| compute bill at list price ($) | 0.06357 | 0.06059 | -4.7% | -0.02794 to +0.02199 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
