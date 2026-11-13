# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.848 | 2.61 |
| node-hours | 0.31 | 0.4422 |
| energy, parked workers still on at idle power (Wh, declared model) | 65.5 | 104.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 63.59 | 87.16 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 793.1 | 848.9 |
| response time (ms), 95th percentile | 3385 | 4095 |
| response time (ms), 99th percentile | 7714 | 7198 |
| time over the response line (% of samples) | 52.73 | 50 |
| failed requests (%) | 40.91 | 36.67 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 3 | 24 |
| time pods had no machine to take them, pod-minutes | 1.95 | 48.9 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 3.733 | 51.37 |
| utilisation (used / allocatable) | 0.7141 | 0.6358 |
| CPU used (cores), mean | 2.507 | 3.153 |
| Omni's own CPU (cores), mean | 0 | 0.0157 |
| CPU used with Omni's own (cores), mean | 2.507 | 3.169 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 151.2 | 163.1 |
| HPA replicas, mean | 9.571 | 21.29 |
| pods started | 5 | 30 |
| pod start wait, total (s) | 157 | 3191 |
| pod start wait, mean (s) | 31.4 | 106.4 |
| machines billed, machine-hours | 0.3756 | 0.565 |
| compute bill at list price ($) | 0.03605 | 0.05424 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.848 | 2.61 | +41.2% | +nan to +nan | no |
| node-hours | 0.31 | 0.4422 | +42.7% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 65.5 | 104.8 | +60.0% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 63.59 | 87.16 | +37.1% | +nan to +nan | no |
| response time (ms), mean | 793.1 | 848.9 | +7.0% | +nan to +nan | no |
| response time (ms), 95th percentile | 3385 | 4095 | +21.0% | +nan to +nan | no |
| response time (ms), 99th percentile | 7714 | 7198 | -6.7% | +nan to +nan | no |
| time over the response line (% of samples) | 52.73 | 50 | -5.2% | +nan to +nan | no |
| failed requests (%) | 40.91 | 36.67 | -10.4% | +nan to +nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 | +0.0% | +nan to +nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21 | +21 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 3 | 24 | +700.0% | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 1.95 | 48.9 | +2407.7% | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 3.733 | 51.37 | +1275.9% | +nan to +nan | no |
| utilisation (used / allocatable) | 0.7141 | 0.6358 | -11.0% | +nan to +nan | no |
| CPU used (cores), mean | 2.507 | 3.153 | +25.8% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0157 | +0.0157 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 2.507 | 3.169 | +26.4% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 151.2 | 163.1 | +7.9% | +nan to +nan | no |
| HPA replicas, mean | 9.571 | 21.29 | +122.5% | +nan to +nan | no |
| pods started | 5 | 30 | +500.0% | +nan to +nan | no |
| pod start wait, total (s) | 157 | 3191 | +1932.5% | +nan to +nan | no |
| pod start wait, mean (s) | 31.4 | 106.4 | +238.7% | +nan to +nan | no |
| machines billed, machine-hours | 0.3756 | 0.565 | +50.4% | +nan to +nan | no |
| compute bill at list price ($) | 0.03605 | 0.05424 | +50.4% | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*