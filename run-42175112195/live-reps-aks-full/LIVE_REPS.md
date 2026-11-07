# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 3.022 | 3.916 |
| node-hours | 0.5133 | 0.6606 |
| energy, parked workers still on at idle power (Wh, declared model) | 78.98 | 108.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 70.86 | 95.06 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 520.3 | 795 |
| response time (ms), 95th percentile | 918.2 | 4301 |
| response time (ms), 99th percentile | 4628 | 7697 |
| time over the response line (% of samples) | 48.14 | 38.36 |
| failed requests (%) | 35.74 | 11.48 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.33 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.67 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 6.667 |
| pods with no machine to take them (unschedulable) | 2 | 21.33 |
| time pods had no machine to take them, pod-minutes | 2.317 | 39.46 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.456 | 51.31 |
| utilisation (used / allocatable) | 0.4952 | 0.48 |
| CPU used (cores), mean | 2.823 | 3.572 |
| Omni's own CPU (cores), mean | 0 | 0.0139 |
| CPU used with Omni's own (cores), mean | 2.823 | 3.586 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 147.9 | 158 |
| HPA replicas, mean | 9.59 | 22.65 |
| pods started | 1 | 22.67 |
| pod start wait, total (s) | 2.333 | 2319 |
| pod start wait, mean (s) | 1.667 | 101 |
| machines billed, machine-hours | 0.4902 | 0.5717 |
| compute bill at list price ($) | 0.04706 | 0.05488 |
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
| worker nodes in service, mean | 3.022 | 3.916 | +29.6% | +0.1172 to +1.6704 | yes: power given |
| node-hours | 0.5133 | 0.6606 | +28.7% | +0.0364 to +0.2582 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 78.98 | 108.8 | +37.7% | −15.4089 to +74.9939 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 70.86 | 95.06 | +34.2% | +5.1509 to +43.2534 | yes: power given |
| response time (ms), mean | 520.3 | 795 | +52.8% | +31.0437 to +518.3924 | yes: LOSS |
| response time (ms), 95th percentile | 918.2 | 4301 | +368.4% | −2065.9639 to +8832.0739 | no |
| response time (ms), 99th percentile | 4628 | 7697 | +66.3% | −8490.4214 to +14628.8560 | no |
| time over the response line (% of samples) | 48.14 | 38.36 | −20.3% | −14.7761 to −4.7786 | yes: GAIN |
| failed requests (%) | 35.74 | 11.48 | −67.9% | −27.3569 to −21.1626 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.33 | 10 | −3.2% | −1.7677 to +1.1010 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.67 | +17.667 (native is 0) | +10.0769 to +25.2564 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2 | 21.33 | +966.7% | +8.9902 to +29.6765 | yes: LOSS |
| time pods had no machine to take them, pod-minutes | 2.317 | 39.46 | +1603.1% | +6.2610 to +68.0168 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.456 | 51.31 | +840.4% | +19.1385 to +72.5615 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.4952 | 0.48 | −3.1% | −0.1657 to +0.1353 | no |
| CPU used (cores), mean | 2.823 | 3.572 | +26.5% | +0.3000 to +1.1978 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0139 | +0.014 (native is 0) | +0.0070 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.823 | 3.586 | +27.0% | +0.3127 to +1.2128 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 147.9 | 158 | +6.9% | −44.2704 to +64.5438 | no |
| HPA replicas, mean | 9.59 | 22.65 | +136.2% | +9.9329 to +16.1873 | yes: power given |
| pods started | 1 | 22.67 | +2166.7% | +12.9420 to +30.3914 | yes: power given |
| pod start wait, total (s) | 2.333 | 2319 | +99285.7% | +627.8898 to +4005.4436 | yes: LOSS |
| pod start wait, mean (s) | 1.667 | 101 | +5960.7% | +50.5131 to +148.1784 | yes: LOSS |
| machines billed, machine-hours | 0.4902 | 0.5717 | +16.6% | −0.4072 to +0.5701 | no |
| compute bill at list price ($) | 0.04706 | 0.05488 | +16.6% | −0.0391 to +0.0547 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*