# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.529 | 3.079 |
| node-hours | 0.8505 | 1.033 |
| energy, parked workers still on at idle power (Wh, declared model) | 105.7 | 157.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 93.8 | 111.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 469.4 | 331.5 |
| response time (ms), 95th percentile | 1025 | 721.5 |
| response time (ms), 99th percentile | 2976 | 1027 |
| time over the response line (% of samples) | 28.74 | 15 |
| failed requests (%) | 3.147 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.64 | 18.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 10.2 |
| pods with no machine to take them (unschedulable) | 2.909 | 13.6 |
| time pods had no machine to take them, pod-minutes | 3.652 | 16.18 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.73 | 26.37 |
| utilisation (used / allocatable) | 0.3281 | 0.2594 |
| CPU used (cores), mean | 1.575 | 1.513 |
| Omni's own CPU (cores), mean | 0 | 0.01227 |
| CPU used with Omni's own (cores), mean | 1.575 | 1.525 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 177.2 | 219.8 |
| HPA replicas, mean | 7.411 | 12.99 |
| pods started | 8.182 | 28.7 |
| pod start wait, total (s) | 270.7 | 1150 |
| pod start wait, mean (s) | 33.16 | 39.05 |
| machines billed, machine-hours | 0.7533 | 0.9675 |
| compute bill at list price ($) | 0.07231 | 0.09288 |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.318 | 8.94 |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 9.178e+04 | 1.182e+05 |

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
| worker nodes in service, mean | 2.532 | 3.079 | +21.6% | +0.4197 to +0.6737 | yes: power given |
| node-hours | 0.8519 | 1.033 | +21.3% | +0.1395 to +0.2228 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 105.8 | 157.4 | +48.7% | +44.4130 to +58.7032 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 94.04 | 111.6 | +18.6% | +11.6461 to +23.4075 | yes: power given |
| response time (ms), mean | 467.3 | 331.5 | −29.1% | −172.8448 to −98.9347 | yes: GAIN |
| response time (ms), 95th percentile | 1033 | 721.5 | −30.2% | −414.7544 to −208.2426 | yes: GAIN |
| response time (ms), 99th percentile | 3067 | 1027 | −66.5% | −2944.5699 to −1136.6801 | yes: GAIN |
| time over the response line (% of samples) | 28.64 | 15 | −47.6% | −17.1017 to −10.1830 | yes: GAIN |
| failed requests (%) | 3.124 | 0 | −100.0% | −3.6178 to −2.6292 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.7 | 18.2 | −7.6% | −2.3430 to −0.6570 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | +33.200 (native is 0) | +29.2705 to +37.1295 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.9 | 13.6 | +369.0% | +6.5695 to +14.8305 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 3.627 | 16.18 | +346.0% | +7.6181 to +17.4786 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.668 | 26.37 | +295.4% | +13.5014 to +25.8986 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.3276 | 0.2594 | −20.8% | −0.0789 to −0.0574 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.574 | 1.513 | −3.9% | −0.0881 to −0.0352 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01227 | +0.012 (native is 0) | +0.0107 to +0.0138 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.574 | 1.525 | −3.1% | −0.0746 to −0.0241 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 177.6 | 219.8 | +23.8% | +32.1099 to +52.2786 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.41 | 12.99 | +75.3% | +4.1434 to +7.0220 | yes: power given |
| pods started | 8.2 | 28.7 | +250.0% | +16.9274 to +24.0726 | yes: power given |
| pod start wait, total (s) | 269.7 | 1150 | +326.6% | +536.4815 to +1225.1185 | yes: LOSS |
| pod start wait, mean (s) | 32.97 | 39.05 | +18.5% | −6.4637 to +18.6412 | no |
| machines billed, machine-hours | 0.753 | 0.9675 | +28.5% | +0.0869 to +0.3421 | yes: power given |
| compute bill at list price ($) | 0.07229 | 0.09288 | +28.5% | +0.0083 to +0.0328 | yes: power given |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.314 | 8.94 | +68.3% | +3.3286 to +3.9248 | yes: GAIN |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 9.184e+04 | 1.182e+05 | +28.8% | +9809.4195 to +43011.6260 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*