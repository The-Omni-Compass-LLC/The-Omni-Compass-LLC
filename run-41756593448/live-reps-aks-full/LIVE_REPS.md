# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.705 | 3.023 |
| node-hours | 0.4533 | 0.5104 |
| energy, parked workers still on at idle power (Wh, declared model) | 66.05 | 101.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 62.34 | 76.09 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 682.4 | 779.1 |
| response time (ms), 95th percentile | 2208 | 2856 |
| response time (ms), 99th percentile | 5726 | 4635 |
| time over the response line (% of samples) | 60.07 | 62.85 |
| failed requests (%) | 45.13 | 46.33 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.33 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 21.67 |
| pods with no machine to take them (unschedulable) | 2.667 | 17 |
| time pods had no machine to take them, pod-minutes | 4.1 | 25.71 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.767 | 35.1 |
| utilisation (used / allocatable) | 0.5189 | 0.5613 |
| CPU used (cores), mean | 2.667 | 3.232 |
| Omni's own CPU (cores), mean | 0 | 0.01453 |
| CPU used with Omni's own (cores), mean | 2.667 | 3.247 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 139.5 | 139.4 |
| HPA replicas, mean | 9.168 | 15.32 |
| pods started | 5 | 21 |
| pod start wait, total (s) | 288 | 1790 |
| pod start wait, mean (s) | 57.6 | 85.28 |
| machines billed, machine-hours | 0.4276 | 0.5146 |
| compute bill at list price ($) | 0.04105 | 0.0494 |
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
| worker nodes in service, mean | 2.705 | 3.023 | +11.7% | −0.3912 to +1.0266 | no |
| node-hours | 0.4533 | 0.5104 | +12.6% | −0.0591 to +0.1732 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 66.05 | 101.1 | +53.1% | +19.1840 to +50.9994 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 62.34 | 76.09 | +22.0% | −11.3235 to +38.8125 | no |
| response time (ms), mean | 682.4 | 779.1 | +14.2% | −628.2413 to +821.6494 | no |
| response time (ms), 95th percentile | 2208 | 2856 | +29.3% | −4545.9312 to +5841.4178 | no |
| response time (ms), 99th percentile | 5726 | 4635 | −19.1% | −4477.4010 to +2294.7823 | no |
| time over the response line (% of samples) | 60.07 | 62.85 | +4.6% | −10.4168 to +15.9849 | no |
| failed requests (%) | 45.13 | 46.33 | +2.6% | −10.7713 to +13.1596 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.33 | +19.333 (native is 0) | +13.0812 to +25.5854 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.667 | 17 | +537.5% | +0.6507 to +28.0160 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 4.1 | 25.71 | +527.1% | +13.0781 to +30.1441 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.767 | 35.1 | +351.9% | +23.6041 to +31.0626 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.5189 | 0.5613 | +8.2% | −0.0181 to +0.1029 | no |
| CPU used (cores), mean | 2.667 | 3.232 | +21.2% | −0.5012 to +1.6318 | no |
| Omni's own CPU (cores), mean | 0 | 0.01453 | +0.015 (native is 0) | +0.0047 to +0.0243 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.667 | 3.247 | +21.7% | −0.4777 to +1.6374 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 139.5 | 139.4 | −0.0% | −5.1340 to +5.0530 | no |
| HPA replicas, mean | 9.168 | 15.32 | +67.1% | +2.0720 to +10.2352 | yes: power given |
| pods started | 5 | 21 | +320.0% | +11.6970 to +20.3030 | yes: power given |
| pod start wait, total (s) | 288 | 1790 | +521.6% | +880.8398 to +2123.8268 | yes: LOSS |
| pod start wait, mean (s) | 57.6 | 85.28 | +48.1% | −7.9787 to +63.3353 | no |
| machines billed, machine-hours | 0.4276 | 0.5146 | +20.4% | −0.0060 to +0.1801 | no |
| compute bill at list price ($) | 0.04105 | 0.0494 | +20.4% | −0.0006 to +0.0173 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*