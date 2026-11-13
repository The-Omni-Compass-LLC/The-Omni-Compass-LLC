# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.849 | 1.818 |
| node-hours | 0.4661 | 0.4581 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.35 | 85.88 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.5 | 82.44 |
| response time (ms), mean | 484.2 | 533.2 |
| response time (ms), 95th percentile | 1105 | 1408 |
| response time (ms), 99th percentile | 4180 | 5620 |
| time over the response line (% of samples) | 26.42 | 28.16 |
| failed requests (%) | 3.774 | 5.311 |
| pods with no machine to take them (unschedulable) | 2.2 | 3 |
| time pods had no machine to take them, pod-minutes | 2.96 | 3.96 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.257 | 6.953 |
| utilisation (used / allocatable) | 0.4743 | 0.5069 |
| CPU used (cores), mean | 1.661 | 1.75 |
| Omni's own CPU (cores), mean | 0 | 0.01154 |
| CPU used with Omni's own (cores), mean | 1.661 | 1.762 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 197.5 | 187.1 |
| HPA replicas, mean | 9.417 | 9.424 |
| pods started | 5.2 | 5.2 |
| pod start wait, total (s) | 216 | 288.6 |
| pod start wait, mean (s) | 41.9 | 55.59 |
| machines billed, machine-hours | 0.6066 | 0.5679 |
| compute bill at list price ($) | 0.05823 | 0.05452 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.849 | 1.818 | -1.7% | -0.1331 to +0.07146 | no |
| node-hours | 0.4661 | 0.4581 | -1.7% | -0.03482 to +0.01882 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.35 | 85.88 | +0.6% | -3.322 to +4.372 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.5 | 82.44 | -0.1% | -5.251 to +5.133 | no |
| response time (ms), mean | 484.2 | 533.2 | +10.1% | -53.51 to +151.6 | no |
| response time (ms), 95th percentile | 1105 | 1408 | +27.4% | -239.2 to +845.1 | no |
| response time (ms), 99th percentile | 4180 | 5620 | +34.5% | -1119 to +3999 | no |
| time over the response line (% of samples) | 26.42 | 28.16 | +6.6% | -1.668 to +5.136 | no |
| failed requests (%) | 3.774 | 5.311 | +40.7% | -1.296 to +4.37 | no |
| pods with no machine to take them (unschedulable) | 2.2 | 3 | +36.4% | -0.8187 to +2.419 | no |
| time pods had no machine to take them, pod-minutes | 2.96 | 3.96 | +33.8% | -0.9585 to +2.959 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.257 | 6.953 | +32.3% | -1.346 to +4.739 | no |
| utilisation (used / allocatable) | 0.4743 | 0.5069 | +6.9% | -0.0241 to +0.0892 | no |
| CPU used (cores), mean | 1.661 | 1.75 | +5.3% | -0.03848 to +0.2161 | no |
| Omni's own CPU (cores), mean | 0 | 0.01154 | +0.0115 (native is 0) | +0.008441 to +0.01464 | yes, more |
| CPU used with Omni's own (cores), mean | 1.661 | 1.762 | +6.0% | -0.02562 to +0.2264 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 197.5 | 187.1 | -5.3% | -33.37 to +12.59 | no |
| HPA replicas, mean | 9.417 | 9.424 | +0.1% | -0.166 to +0.1795 | no |
| pods started | 5.2 | 5.2 | +0.0% | +0 to +0 | no |
| pod start wait, total (s) | 216 | 288.6 | +33.6% | -71.83 to +217 | no |
| pod start wait, mean (s) | 41.9 | 55.59 | +32.7% | -14.71 to +42.08 | no |
| machines billed, machine-hours | 0.6066 | 0.5679 | -6.4% | -0.1768 to +0.09947 | no |
| compute bill at list price ($) | 0.05823 | 0.05452 | -6.4% | -0.01697 to +0.009549 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*