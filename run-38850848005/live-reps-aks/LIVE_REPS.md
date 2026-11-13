# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.876 | 1.913 |
| node-hours | 0.9429 | 0.9598 |
| energy, parked workers still on at idle power (Wh, declared model) | 215.2 | 215.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 210.6 | 212.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 425.2 | 404.3 |
| response time (ms), 95th percentile | 741.6 | 672.9 |
| response time (ms), 99th percentile | 3869 | 4330 |
| time over the response line (% of samples) | 49.19 | 49.09 |
| failed requests (%) | 40.16 | 42.62 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 28.45 |
| pods with no machine to take them (unschedulable) | 2.2 | 1.8 |
| time pods had no machine to take them, pod-minutes | 16.98 | 2.083 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.737 | 4.737 |
| utilisation (used / allocatable) | 0.8196 | 0.812 |
| CPU used (cores), mean | 2.921 | 2.951 |
| Omni's own CPU (cores), mean | 0 | 0.00392 |
| CPU used with Omni's own (cores), mean | 2.921 | 2.955 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 143.5 | 143.4 |
| HPA replicas, mean | 9.558 | 9.645 |
| pods started | 5.2 | 4.4 |
| pod start wait, total (s) | 1052 | 159.4 |
| pod start wait, mean (s) | 205.4 | 35.71 |
| machines billed, machine-hours | 1.124 | 1.079 |
| compute bill at list price ($) | 0.1079 | 0.1036 |

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
| worker nodes in service, mean | 1.876 | 1.913 | +2.0% | -0.02829 to +0.1018 | no |
| node-hours | 0.9429 | 0.9598 | +1.8% | -0.01719 to +0.05108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 215.2 | 215.6 | +0.1% | -1.52 to +2.142 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 210.6 | 212.3 | +0.8% | -1.409 to +4.806 | no |
| response time (ms), mean | 425.2 | 404.3 | -4.9% | -111.6 to +69.91 | no |
| response time (ms), 95th percentile | 741.6 | 672.9 | -9.3% | -142.9 to +5.51 | no |
| response time (ms), 99th percentile | 3869 | 4330 | +11.9% | -2620 to +3542 | no |
| time over the response line (% of samples) | 49.19 | 49.09 | -0.2% | -5.462 to +5.271 | no |
| failed requests (%) | 40.16 | 42.62 | +6.1% | -3.082 to +7.997 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29 | -2.0% | -2.015 to +0.8155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35 | +35 (native is 0) | +31.38 to +38.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.2 | 1.8 | -18.2% | -2.477 to +1.677 | no |
| time pods had no machine to take them, pod-minutes | 16.98 | 2.083 | -87.7% | -56.54 to +26.75 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.737 | 4.737 | -17.4% | -3.371 to +1.371 | no |
| utilisation (used / allocatable) | 0.8196 | 0.812 | -0.9% | -0.03284 to +0.01763 | no |
| CPU used (cores), mean | 2.921 | 2.951 | +1.1% | -0.03483 to +0.09639 | no |
| Omni's own CPU (cores), mean | 0 | 0.00392 | +0.00392 (native is 0) | +0.003183 to +0.004657 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.921 | 2.955 | +1.2% | -0.03145 to +0.1009 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 143.5 | 143.4 | -0.1% | -1.52 to +1.285 | no |
| HPA replicas, mean | 9.558 | 9.645 | +0.9% | -0.2251 to +0.3989 | no |
| pods started | 5.2 | 4.4 | -15.4% | -3.764 to +2.164 | no |
| pod start wait, total (s) | 1052 | 159.4 | -84.8% | -3394 to +1610 | no |
| pod start wait, mean (s) | 205.4 | 35.71 | -82.6% | -675.3 to +335.8 | no |
| machines billed, machine-hours | 1.124 | 1.079 | -4.0% | -0.1198 to +0.03007 | no |
| compute bill at list price ($) | 0.1079 | 0.1036 | -4.0% | -0.01151 to +0.002887 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*