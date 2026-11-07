# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 3 | 4.439 |
| node-hours | 1.003 | 1.496 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 291.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 277.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 709.9 | 1502 |
| response time (ms), 95th percentile | 2673 | 8661 |
| response time (ms), 99th percentile | 8142 | 9496 |
| time over the response line (% of samples) | 65.88 | 85.52 |
| failed requests (%) | 57.06 | 68.28 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20 | 20 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 23 |
| time pods had no machine to take them, pod-minutes | 0 | 106.9 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 117 |
| utilisation (used / allocatable) | 0.6519 | 0.7797 |
| CPU used (cores), mean | 3.716 | 6.577 |
| Omni's own CPU (cores), mean | 0 | 0.01 |
| CPU used with Omni's own (cores), mean | 3.716 | 6.587 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 127.2 | 125 |
| HPA replicas, mean | 9.929 | 28.42 |
| pods started | 0 | 27 |
| pod start wait, total (s) | 0 | 6560 |
| pod start wait, mean (s) | 0 | 243 |
| machines billed, machine-hours | 0.8533 | 1.218 |
| compute bill at list price ($) | 0.08192 | 0.1169 |
| work inside the response line (requests a second; the capacity test's own gauge) | 1.531 | 1.311 |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 2.273e+04 | 1.362e+04 |

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
| worker nodes in service, mean | 3 | 4.439 | +48.0% | ±nan to ±nan | no |
| node-hours | 1.003 | 1.496 | +49.1% | ±nan to ±nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 291.2 | +84.3% | ±nan to ±nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 277.1 | +75.3% | ±nan to ±nan | no |
| response time (ms), mean | 709.9 | 1502 | +111.5% | ±nan to ±nan | no |
| response time (ms), 95th percentile | 2673 | 8661 | +224.1% | ±nan to ±nan | no |
| response time (ms), 99th percentile | 8142 | 9496 | +16.6% | ±nan to ±nan | no |
| time over the response line (% of samples) | 65.88 | 85.52 | +29.8% | ±nan to ±nan | no |
| failed requests (%) | 57.06 | 68.28 | +19.7% | ±nan to ±nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20 | 20 | ±0.0% | ±nan to ±nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22 | +22.000 (native is 0) | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 23 | +23.000 (native is 0) | ±nan to ±nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 106.9 | +106.917 (native is 0) | ±nan to ±nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 117 | +117.033 (native is 0) | ±nan to ±nan | no |
| utilisation (used / allocatable) | 0.6519 | 0.7797 | +19.6% | ±nan to ±nan | no |
| CPU used (cores), mean | 3.716 | 6.577 | +77.0% | ±nan to ±nan | no |
| Omni's own CPU (cores), mean | 0 | 0.01 | +0.010 (native is 0) | ±nan to ±nan | no |
| CPU used with Omni's own (cores), mean | 3.716 | 6.587 | +77.3% | ±nan to ±nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 127.2 | 125 | −1.7% | ±nan to ±nan | no |
| HPA replicas, mean | 9.929 | 28.42 | +186.2% | ±nan to ±nan | no |
| pods started | 0 | 27 | +27.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, total (s) | 0 | 6560 | +6560.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, mean (s) | 0 | 243 | +242.963 (native is 0) | ±nan to ±nan | no |
| machines billed, machine-hours | 0.8533 | 1.218 | +42.7% | ±nan to ±nan | no |
| compute bill at list price ($) | 0.08192 | 0.1169 | +42.7% | ±nan to ±nan | no |
| work inside the response line (requests a second; the capacity test's own gauge) | 1.531 | 1.311 | −14.4% | ±nan to ±nan | no |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 2.273e+04 | 1.362e+04 | −40.1% | ±nan to ±nan | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*