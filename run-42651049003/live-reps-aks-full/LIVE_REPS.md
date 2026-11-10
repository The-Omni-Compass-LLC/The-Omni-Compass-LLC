# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.779 | 3.851 |
| node-hours | 0.4706 | 0.6508 |
| energy, parked workers still on at idle power (Wh, declared model) | 67.28 | 109.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 64.47 | 95.01 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 501.2 | 752.9 |
| response time (ms), 95th percentile | 1542 | 3729 |
| response time (ms), 99th percentile | 4233 | 8091 |
| time over the response line (% of samples) | 46.3 | 34.39 |
| failed requests (%) | 36.89 | 14.6 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.33 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.67 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.19 |
| pods with no machine to take them (unschedulable) | 2.667 | 22.33 |
| time pods had no machine to take them, pod-minutes | 2.794 | 44.82 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.833 | 51.96 |
| utilisation (used / allocatable) | 0.5226 | 0.4975 |
| CPU used (cores), mean | 2.761 | 3.634 |
| Omni's own CPU (cores), mean | 0 | 0.01307 |
| CPU used with Omni's own (cores), mean | 2.761 | 3.647 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 138.2 | 155.2 |
| HPA replicas, mean | 9.576 | 22.58 |
| pods started | 1.333 | 24.33 |
| pod start wait, total (s) | 87 | 2667 |
| pod start wait, mean (s) | 29.67 | 109.3 |
| machines billed, machine-hours | 0.412 | 0.5588 |
| compute bill at list price ($) | 0.03956 | 0.05364 |
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
| worker nodes in service, mean | 2.779 | 3.851 | +38.6% | +0.4709 to +1.6737 | yes: power given |
| node-hours | 0.4706 | 0.6508 | +38.3% | +0.0630 to +0.2975 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 67.28 | 109.6 | +62.8% | +32.8487 to +51.7064 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 64.47 | 95.01 | +47.4% | +15.6587 to +45.4102 | yes: power given |
| response time (ms), mean | 501.2 | 752.9 | +50.2% | −523.8364 to +1027.1662 | no |
| response time (ms), 95th percentile | 1542 | 3729 | +141.8% | −5871.3579 to +10244.5213 | no |
| response time (ms), 99th percentile | 4233 | 8091 | +91.1% | −3308.3675 to +11024.8675 | no |
| time over the response line (% of samples) | 46.3 | 34.39 | −25.7% | −29.5177 to +5.7126 | no |
| failed requests (%) | 36.89 | 14.6 | −60.4% | −37.6138 to −6.9645 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.33 | 10 | −3.2% | −1.7677 to +1.1010 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.67 | +20.667 (native is 0) | +16.8718 to +24.4616 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.667 | 22.33 | +737.5% | +15.8718 to +23.4616 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 2.794 | 44.82 | +1504.0% | +21.7593 to +62.2963 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.833 | 51.96 | +975.1% | +29.5218 to +64.7338 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.5226 | 0.4975 | −4.8% | −0.1398 to +0.0896 | no |
| CPU used (cores), mean | 2.761 | 3.634 | +31.6% | +0.2066 to +1.5382 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01307 | +0.013 (native is 0) | +0.0074 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.761 | 3.647 | +32.1% | +0.2145 to +1.5564 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 138.2 | 155.2 | +12.3% | −3.0419 to +37.0752 | no |
| HPA replicas, mean | 9.576 | 22.58 | +135.8% | +9.9132 to +16.0907 | yes: power given |
| pods started | 1.333 | 24.33 | +1725.0% | +20.5157 to +25.4843 | yes: power given |
| pod start wait, total (s) | 87 | 2667 | +2965.1% | +1631.5658 to +3527.7675 | yes: LOSS |
| pod start wait, mean (s) | 29.67 | 109.3 | +268.5% | −2.8656 to +162.1923 | no |
| machines billed, machine-hours | 0.412 | 0.5588 | +35.6% | +0.0820 to +0.2115 | yes: power given |
| compute bill at list price ($) | 0.03956 | 0.05364 | +35.6% | +0.0079 to +0.0203 | yes: power given |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*