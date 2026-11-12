# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.506 | 3.05 |
| node-hours | 0.8398 | 1.024 |
| energy, parked workers still on at idle power (Wh, declared model) | 105 | 153.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 92.6 | 111.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 459.5 | 331.3 |
| response time (ms), 95th percentile | 986.8 | 722.6 |
| response time (ms), 99th percentile | 2694 | 1083 |
| time over the response line (% of samples) | 28.13 | 15.32 |
| failed requests (%) | 3.201 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.45 | 17.64 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.45 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 13.96 |
| pods with no machine to take them (unschedulable) | 2.818 | 12.45 |
| time pods had no machine to take them, pod-minutes | 3.079 | 15.43 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.115 | 23.91 |
| utilisation (used / allocatable) | 0.3282 | 0.2662 |
| CPU used (cores), mean | 1.562 | 1.531 |
| Omni's own CPU (cores), mean | 0 | 0.01301 |
| CPU used with Omni's own (cores), mean | 1.562 | 1.544 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 176.9 | 216.4 |
| HPA replicas, mean | 7.467 | 12.78 |
| pods started | 8 | 28.64 |
| pod start wait, total (s) | 233.4 | 1075 |
| pod start wait, mean (s) | 29.17 | 36.39 |
| machines billed, machine-hours | 0.7602 | 0.9746 |
| compute bill at list price ($) | 0.07298 | 0.09356 |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.36 | 8.866 |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 8.978e+04 | 1.15e+05 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.505 | 3.031 | +21.0% | +0.3342 to +0.7179 | yes: power given |
| node-hours | 0.8395 | 1.018 | +21.3% | +0.1123 to +0.2450 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 105 | 152.6 | +45.4% | +37.8050 to +57.5077 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 92.56 | 110.6 | +19.5% | +11.8072 to +24.2763 | yes: power given |
| response time (ms), mean | 455.1 | 339.1 | −25.5% | −153.5133 to −78.5828 | yes: GAIN |
| response time (ms), 95th percentile | 985 | 736.3 | −25.2% | −348.1838 to −149.0572 | yes: GAIN |
| response time (ms), 99th percentile | 2581 | 1109 | −57.0% | −2003.5933 to −940.9465 | yes: GAIN |
| time over the response line (% of samples) | 27.9 | 16.01 | −42.6% | −15.9317 to −7.8414 | yes: GAIN |
| failed requests (%) | 3.241 | 0 | −100.0% | −3.4417 to −3.0411 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.4 | 17.8 | −8.2% | −2.7778 to −0.4222 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.7 | +35.700 (native is 0) | +32.5002 to +38.8998 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.8 | 12.2 | +335.7% | +5.8602 to +12.9398 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 3.082 | 15.16 | +391.9% | +6.8941 to +17.2592 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.015 | 23.78 | +295.3% | +12.4554 to +23.0746 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.3284 | 0.268 | −18.4% | −0.0797 to −0.0412 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.563 | 1.531 | −2.0% | −0.0642 to +0.0006 | no |
| Omni's own CPU (cores), mean | 0 | 0.01279 | +0.013 (native is 0) | +0.0109 to +0.0147 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.563 | 1.544 | −1.2% | −0.0520 to +0.0140 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 176.8 | 215.3 | +21.8% | +25.5874 to +51.4696 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.464 | 12.63 | +69.3% | +3.6319 to +6.7074 | yes: power given |
| pods started | 8 | 28.2 | +252.5% | +15.7164 to +24.6836 | yes: power given |
| pod start wait, total (s) | 233 | 1058 | +354.3% | +492.3888 to +1158.6112 | yes: LOSS |
| pod start wait, mean (s) | 29.12 | 36.29 | +24.6% | −2.9880 to +17.3106 | no |
| machines billed, machine-hours | 0.7592 | 0.969 | +27.6% | +0.1375 to +0.2822 | yes: power given |
| compute bill at list price ($) | 0.07288 | 0.09303 | +27.6% | +0.0132 to +0.0271 | yes: power given |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.348 | 8.823 | +65.0% | +3.1484 to +3.8017 | yes: GAIN |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 8.978e+04 | 1.152e+05 | +28.3% | +19647.2313 to +31214.5186 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*