# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.532 | 2.769 |
| node-hours | 0.8525 | 0.9322 |
| energy, parked workers still on at idle power (Wh, declared model) | 107.4 | 158 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 95.58 | 101.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 374.5 | 347.4 |
| response time (ms), 95th percentile | 827.8 | 820.4 |
| response time (ms), 99th percentile | 2863 | 1344 |
| time over the response line (% of samples) | 22.05 | 20.67 |
| failed requests (%) | 3.288 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19 | 20 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 5 |
| pods with no machine to take them (unschedulable) | 1 | 5 |
| time pods had no machine to take them, pod-minutes | 1.217 | 7.9 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 3.733 | 16.1 |
| utilisation (used / allocatable) | 0.3174 | 0.2967 |
| CPU used (cores), mean | 1.527 | 1.561 |
| Omni's own CPU (cores), mean | 0 | 0.0152 |
| CPU used with Omni's own (cores), mean | 1.527 | 1.576 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 185.9 | 193.4 |
| HPA replicas, mean | 7.35 | 10.18 |
| pods started | 8 | 20 |
| pod start wait, total (s) | 115 | 568 |
| pod start wait, mean (s) | 14.38 | 28.4 |
| machines billed, machine-hours | 0.8606 | 0.8472 |
| compute bill at list price ($) | 0.08261 | 0.08133 |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.476 | 8.35 |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 8.18e+04 | 1.244e+05 |

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
| worker nodes in service, mean | 2.532 | 2.769 | +9.4% | ±nan to ±nan | no |
| node-hours | 0.8525 | 0.9322 | +9.4% | ±nan to ±nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 107.4 | 158 | +47.1% | ±nan to ±nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 95.58 | 101.7 | +6.4% | ±nan to ±nan | no |
| response time (ms), mean | 374.5 | 347.4 | −7.2% | ±nan to ±nan | no |
| response time (ms), 95th percentile | 827.8 | 820.4 | −0.9% | ±nan to ±nan | no |
| response time (ms), 99th percentile | 2863 | 1344 | −53.0% | ±nan to ±nan | no |
| time over the response line (% of samples) | 22.05 | 20.67 | −6.3% | ±nan to ±nan | no |
| failed requests (%) | 3.288 | 0 | −100.0% | ±nan to ±nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19 | 20 | +5.3% | ±nan to ±nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34 | +34.000 (native is 0) | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 1 | 5 | +400.0% | ±nan to ±nan | no |
| time pods had no machine to take them, pod-minutes | 1.217 | 7.9 | +549.3% | ±nan to ±nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 3.733 | 16.1 | +331.2% | ±nan to ±nan | no |
| utilisation (used / allocatable) | 0.3174 | 0.2967 | −6.5% | ±nan to ±nan | no |
| CPU used (cores), mean | 1.527 | 1.561 | +2.2% | ±nan to ±nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0152 | +0.015 (native is 0) | ±nan to ±nan | no |
| CPU used with Omni's own (cores), mean | 1.527 | 1.576 | +3.2% | ±nan to ±nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 185.9 | 193.4 | +4.0% | ±nan to ±nan | no |
| HPA replicas, mean | 7.35 | 10.18 | +38.6% | ±nan to ±nan | no |
| pods started | 8 | 20 | +150.0% | ±nan to ±nan | no |
| pod start wait, total (s) | 115 | 568 | +393.9% | ±nan to ±nan | no |
| pod start wait, mean (s) | 14.38 | 28.4 | +97.6% | ±nan to ±nan | no |
| machines billed, machine-hours | 0.8606 | 0.8472 | −1.5% | ±nan to ±nan | no |
| compute bill at list price ($) | 0.08261 | 0.08133 | −1.5% | ±nan to ±nan | no |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.476 | 8.35 | +52.5% | ±nan to ±nan | no |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 8.18e+04 | 1.244e+05 | +52.1% | ±nan to ±nan | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*