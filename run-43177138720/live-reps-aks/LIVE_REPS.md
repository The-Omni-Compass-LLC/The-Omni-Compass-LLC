# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.509 | 2.952 |
| node-hours | 0.8419 | 0.9908 |
| energy, parked workers still on at idle power (Wh, declared model) | 105.6 | 148.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 93.22 | 107.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 469.9 | 360.4 |
| response time (ms), 95th percentile | 1047 | 779 |
| response time (ms), 99th percentile | 3039 | 1266 |
| time over the response line (% of samples) | 27.53 | 17.77 |
| failed requests (%) | 2.784 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.3 | 18.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 9.693 |
| pods with no machine to take them (unschedulable) | 2.8 | 11.5 |
| time pods had no machine to take them, pod-minutes | 3.155 | 13.13 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.552 | 21.85 |
| utilisation (used / allocatable) | 0.3264 | 0.2725 |
| CPU used (cores), mean | 1.556 | 1.516 |
| Omni's own CPU (cores), mean | 0 | 0.01176 |
| CPU used with Omni's own (cores), mean | 1.556 | 1.528 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 178.5 | 211.1 |
| HPA replicas, mean | 7.444 | 11.85 |
| pods started | 8 | 26.6 |
| pod start wait, total (s) | 236.9 | 921.8 |
| pod start wait, mean (s) | 29.61 | 33.8 |
| machines billed, machine-hours | 0.7719 | 0.9104 |
| compute bill at list price ($) | 0.07411 | 0.0874 |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.441 | 8.651 |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 9.001e+04 | 1.208e+05 |

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
| worker nodes in service, mean | 2.509 | 2.952 | +17.7% | +0.2534 to +0.6323 | yes: power given |
| node-hours | 0.8419 | 0.9907 | +17.7% | +0.0839 to +0.2137 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 105.6 | 148.7 | +40.8% | +32.4900 to +53.7234 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 93.22 | 107.2 | +15.0% | +7.0862 to +20.8522 | yes: power given |
| response time (ms), mean | 469.9 | 360.4 | −23.3% | −150.3979 to −68.4447 | yes: GAIN |
| response time (ms), 95th percentile | 1047 | 779 | −25.6% | −384.1212 to −151.6638 | yes: GAIN |
| response time (ms), 99th percentile | 3039 | 1266 | −58.3% | −2808.8026 to −736.3846 | yes: GAIN |
| time over the response line (% of samples) | 27.53 | 17.77 | −35.5% | −12.9842 to −6.5418 | yes: GAIN |
| failed requests (%) | 2.784 | 0 | −100.0% | −3.3348 to −2.2339 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.3 | 18.4 | −4.7% | −2.5329 to +0.7329 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.4 | +34.400 (native is 0) | +31.5348 to +37.2652 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.8 | 11.5 | +310.7% | +5.0832 to +12.3168 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 3.155 | 13.13 | +316.1% | +5.6713 to +14.2720 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.552 | 21.85 | +233.6% | +10.3910 to +20.2123 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.3264 | 0.2725 | −16.5% | −0.0730 to −0.0349 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.556 | 1.516 | −2.6% | −0.0701 to −0.0100 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01176 | +0.012 (native is 0) | +0.0100 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.556 | 1.528 | −1.8% | −0.0592 to +0.0027 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 178.5 | 211.1 | +18.2% | +17.7554 to +47.3347 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.444 | 11.85 | +59.2% | +2.9289 to +5.8899 | yes: power given |
| pods started | 8 | 26.6 | +232.5% | +14.5368 to +22.6632 | yes: power given |
| pod start wait, total (s) | 236.9 | 921.8 | +289.1% | +400.0044 to +969.7956 | yes: LOSS |
| pod start wait, mean (s) | 29.61 | 33.8 | +14.2% | −4.8195 to +13.2005 | no |
| machines billed, machine-hours | 0.7719 | 0.9104 | +17.9% | +0.0462 to +0.2307 | yes: power given |
| compute bill at list price ($) | 0.07411 | 0.0874 | +17.9% | +0.0044 to +0.0221 | yes: power given |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.441 | 8.651 | +59.0% | +2.8472 to +3.5739 | yes: GAIN |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 9.001e+04 | 1.208e+05 | +34.2% | +21493.6225 to +40125.1070 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*