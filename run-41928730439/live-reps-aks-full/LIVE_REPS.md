# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.847 | 3.529 |
| node-hours | 0.4826 | 0.5953 |
| energy, parked workers still on at idle power (Wh, declared model) | 67.4 | 105.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.45 | 87.14 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 573.8 | 746.5 |
| response time (ms), 95th percentile | 2113 | 3577 |
| response time (ms), 99th percentile | 3469 | 6849 |
| time over the response line (% of samples) | 48.94 | 44.03 |
| failed requests (%) | 33.43 | 26.95 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 9.524 |
| pods with no machine to take them (unschedulable) | 3 | 19 |
| time pods had no machine to take them, pod-minutes | 4.15 | 34.96 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.456 | 46.14 |
| utilisation (used / allocatable) | 0.5176 | 0.52 |
| CPU used (cores), mean | 2.799 | 3.488 |
| Omni's own CPU (cores), mean | 0 | 0.01923 |
| CPU used with Omni's own (cores), mean | 2.799 | 3.507 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 137.9 | 148 |
| HPA replicas, mean | 9.923 | 19.91 |
| pods started | 0 | 21.33 |
| pod start wait, total (s) | 0 | 2167 |
| pod start wait, mean (s) | 0 | 102.9 |
| machines billed, machine-hours | 0.3749 | 0.5627 |
| compute bill at list price ($) | 0.03599 | 0.05402 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.847 | 3.529 | +24.0% | −0.1350 to +1.4990 | no |
| node-hours | 0.4826 | 0.5953 | +23.3% | −0.0322 to +0.2576 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 67.4 | 105.8 | +56.9% | +22.8179 to +53.8982 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.45 | 87.14 | +33.1% | −3.5387 to +46.9215 | no |
| response time (ms), mean | 573.8 | 746.5 | +30.1% | −448.7090 to +794.0308 | no |
| response time (ms), 95th percentile | 2113 | 3577 | +69.3% | −4814.4728 to +7743.2795 | no |
| response time (ms), 99th percentile | 3469 | 6849 | +97.4% | −1304.9717 to +8064.9957 | no |
| time over the response line (% of samples) | 48.94 | 44.03 | −10.0% | −22.9382 to +13.1217 | no |
| failed requests (%) | 33.43 | 26.95 | −19.4% | −24.9317 to +11.9690 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21 | +21.000 (native is 0) | +5.4853 to +36.5147 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 3 | 19 | +533.3% | +11.6970 to +20.3030 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 4.15 | 34.96 | +742.3% | +23.3461 to +38.2650 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.456 | 46.14 | +518.9% | +34.1930 to +43.1737 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.5176 | 0.52 | +0.5% | −0.0182 to +0.0231 | no |
| CPU used (cores), mean | 2.799 | 3.488 | +24.6% | −0.2259 to +1.6026 | no |
| Omni's own CPU (cores), mean | 0 | 0.01923 | +0.019 (native is 0) | +0.0090 to +0.0294 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.799 | 3.507 | +25.3% | −0.1967 to +1.6118 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 137.9 | 148 | +7.3% | +6.6848 to +13.5677 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.923 | 19.91 | +100.6% | +4.9162 to +15.0559 | yes: power given |
| pods started | 0 | 21.33 | +21.333 (native is 0) | +15.0812 to +27.5854 | yes: power given |
| pod start wait, total (s) | 0 | 2167 | +2167.000 (native is 0) | +1899.2787 to +2434.7213 | yes: LOSS |
| pod start wait, mean (s) | 0 | 102.9 | +102.898 (native is 0) | +60.7579 to +145.0378 | yes: LOSS |
| machines billed, machine-hours | 0.3749 | 0.5627 | +50.1% | +0.1243 to +0.2513 | yes: power given |
| compute bill at list price ($) | 0.03599 | 0.05402 | +50.1% | +0.0119 to +0.0241 | yes: power given |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*