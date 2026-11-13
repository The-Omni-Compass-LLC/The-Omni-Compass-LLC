# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.97 | 1.942 |
| node-hours | 1.424 | 1.405 |
| energy, parked workers still on at idle power (Wh, declared model) | 329.6 | 305.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.4 | 302.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 909.2 | 1053 |
| response time (ms), 95th percentile | 3539 | 4486 |
| response time (ms), 99th percentile | 6538 | 6545 |
| time over the response line (% of samples) | 81.23 | 86.62 |
| failed requests (%) | 66.07 | 75.85 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 43.2 | 43.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 31.02 |
| pods with no machine to take them (unschedulable) | 3.2 | 2.4 |
| time pods had no machine to take them, pod-minutes | 3.03 | 2.85 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.767 | 5.687 |
| utilisation (used / allocatable) | 0.78 | 0.7858 |
| CPU used (cores), mean | 2.919 | 2.899 |
| Omni's own CPU (cores), mean | 0 | 0.00408 |
| CPU used with Omni's own (cores), mean | 2.919 | 2.904 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 145.2 | 144.3 |
| HPA replicas, mean | 9.813 | 9.81 |
| pods started | 5.2 | 4.2 |
| pod start wait, total (s) | 225.2 | 205.8 |
| pod start wait, mean (s) | 43.36 | 41.48 |
| machines billed, machine-hours | 1.577 | 1.508 |
| compute bill at list price ($) | 0.1514 | 0.1448 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped) vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.97 | 1.942 | -1.4% | -0.1125 to +0.05718 | no |
| node-hours | 1.424 | 1.405 | -1.3% | -0.07781 to +0.0397 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 329.6 | 305.8 | -7.2% | -94.64 to +47.01 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.4 | 302.7 | -1.2% | -19.22 to +11.84 | no |
| response time (ms), mean | 909.2 | 1053 | +15.8% | -398.4 to +685.7 | no |
| response time (ms), 95th percentile | 3539 | 4486 | +26.8% | -2203 to +4097 | no |
| response time (ms), 99th percentile | 6538 | 6545 | +0.1% | -4180 to +4194 | no |
| time over the response line (% of samples) | 81.23 | 86.62 | +6.6% | -11.16 to +21.92 | no |
| failed requests (%) | 66.07 | 75.85 | +14.8% | -20.25 to +39.8 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 43.2 | 43.4 | +0.5% | -0.8387 to +1.239 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60 | +60 (native is 0) | +52.81 to +67.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 3.2 | 2.4 | -25.0% | -2.419 to +0.8187 | no |
| time pods had no machine to take them, pod-minutes | 3.03 | 2.85 | -5.9% | -2.953 to +2.593 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.767 | 5.687 | -16.0% | -2.929 to +0.7691 | no |
| utilisation (used / allocatable) | 0.78 | 0.7858 | +0.7% | -0.004901 to +0.01649 | no |
| CPU used (cores), mean | 2.919 | 2.899 | -0.7% | -0.1441 to +0.1057 | no |
| Omni's own CPU (cores), mean | 0 | 0.00408 | +0.00408 (native is 0) | +0.003522 to +0.004638 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.919 | 2.904 | -0.5% | -0.1399 to +0.1096 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 145.2 | 144.3 | -0.6% | -2.743 to +1.038 | no |
| HPA replicas, mean | 9.813 | 9.81 | -0.0% | -0.07688 to +0.07242 | no |
| pods started | 5.2 | 4.2 | -19.2% | -3.15 to +1.15 | no |
| pod start wait, total (s) | 225.2 | 205.8 | -8.6% | -201.4 to +162.6 | no |
| pod start wait, mean (s) | 43.36 | 41.48 | -4.3% | -38.1 to +34.34 | no |
| machines billed, machine-hours | 1.577 | 1.508 | -4.4% | -0.2455 to +0.1078 | no |
| compute bill at list price ($) | 0.1514 | 0.1448 | -4.4% | -0.02356 to +0.01035 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*