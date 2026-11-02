# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.845 |
| node-hours | 1.518 | 1.472 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.7 | 158.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 78.4 | 79.99 |
| response time (ms), 95th percentile | 118.1 | 118.8 |
| response time (ms), 99th percentile | 134.1 | 137.4 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.05333 |
| utilisation (used / allocatable) | 0.04765 | 0.04966 |
| CPU used (cores), mean | 1.144 | 1.151 |
| Omni's own CPU (cores), mean | 0 | 0.05046 |
| CPU used with Omni's own (cores), mean | 1.144 | 1.202 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 567.5 | 553.2 |
| HPA replicas, mean | 2.753 | 2.785 |
| pods started | 1.7 | 1.5 |
| pod start wait, total (s) | 2.6 | 2 |
| pod start wait, mean (s) | 1.55 | 1.25 |
| host CPU busy, the real machine under kind (%) | 35.79 | 38.03 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.845 | −2.6% | −0.5059 to +0.1957 | no |
| node-hours | 1.518 | 1.472 | −3.0% | −0.1311 to +0.0396 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.2 | −0.3% | −1.5097 to +0.5141 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.7 | 158.2 | −2.1% | −9.5501 to +2.6421 | no |
| response time (ms), mean | 78.4 | 79.99 | +2.0% | +0.3178 to +2.8537 | yes: LOSS |
| response time (ms), 95th percentile | 118.1 | 118.8 | +0.6% | −2.0279 to +3.4199 | no |
| response time (ms), 99th percentile | 134.1 | 137.4 | +2.5% | −6.4116 to +13.0508 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.2 | +4.200 (native is 0) | +3.7476 to +4.6524 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.05333 | −50.8% | −0.2068 to +0.0968 | no |
| utilisation (used / allocatable) | 0.04765 | 0.04966 | +4.2% | −0.0016 to +0.0056 | no |
| CPU used (cores), mean | 1.144 | 1.151 | +0.7% | −0.0174 to +0.0327 | no |
| Omni's own CPU (cores), mean | 0 | 0.05046 | +0.050 (native is 0) | +0.0433 to +0.0577 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.144 | 1.202 | +5.1% | +0.0344 to +0.0819 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 567.5 | 553.2 | −2.5% | −36.0929 to +7.4735 | no |
| HPA replicas, mean | 2.753 | 2.785 | +1.1% | −0.1259 to +0.1889 | no |
| pods started | 1.7 | 1.5 | −11.8% | −0.7642 to +0.3642 | no |
| pod start wait, total (s) | 2.6 | 2 | −23.1% | −1.6769 to +0.4769 | no |
| pod start wait, mean (s) | 1.55 | 1.25 | −19.4% | −0.8385 to +0.2385 | no |
| host CPU busy, the real machine under kind (%) | 35.79 | 38.03 | +6.3% | +1.5465 to +2.9332 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*