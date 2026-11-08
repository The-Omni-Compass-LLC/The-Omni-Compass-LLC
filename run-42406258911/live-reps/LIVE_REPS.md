# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 518 | 517.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518 | 517.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 288 | 188.8 |
| response time (ms), 95th percentile | 801.2 | 464.2 |
| response time (ms), 99th percentile | 2358 | 2458 |
| time over the response line (% of samples) | 19.76 | 13.9 |
| failed requests (%) | 10.45 | 10.25 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.6 | 23.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 71.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5233 | 0.3483 |
| utilisation (used / allocatable) | 0.1032 | 0.1022 |
| CPU used (cores), mean | 2.476 | 2.452 |
| Omni's own CPU (cores), mean | 0 | 0.04548 |
| CPU used with Omni's own (cores), mean | 2.476 | 2.497 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294.8 | 299.8 |
| HPA replicas, mean | 9.469 | 10.92 |
| pods started | 5.4 | 10.1 |
| pod start wait, total (s) | 7.6 | 17.8 |
| pod start wait, mean (s) | 1.406 | 1.76 |
| host CPU busy, the real machine under kind (%) | 69.77 | 70.74 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.515 | 4.515 | +0.0% | −0.0088 to +0.0095 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 518 | 517.5 | −0.1% | −2.1107 to +1.0775 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518 | 517.5 | −0.1% | −2.1107 to +1.0775 | no |
| response time (ms), mean | 288 | 188.8 | −34.5% | −124.5414 to −73.9062 | yes: GAIN |
| response time (ms), 95th percentile | 801.2 | 464.2 | −42.1% | −443.2822 to −230.7278 | yes: GAIN |
| response time (ms), 99th percentile | 2358 | 2458 | +4.3% | −736.8681 to +937.3965 | no |
| time over the response line (% of samples) | 19.76 | 13.9 | −29.7% | −7.6056 to −4.1138 | yes: GAIN |
| failed requests (%) | 10.45 | 10.25 | −1.9% | −0.9428 to +0.5414 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.6 | 23.1 | −19.2% | −7.3546 to −3.6454 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.1 | +53.100 (native is 0) | +43.8627 to +62.3373 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5233 | 0.3483 | −33.4% | −0.5204 to +0.1704 | no |
| utilisation (used / allocatable) | 0.1032 | 0.1022 | −1.0% | −0.0024 to +0.0003 | no |
| CPU used (cores), mean | 2.476 | 2.452 | −1.0% | −0.0566 to +0.0072 | no |
| Omni's own CPU (cores), mean | 0 | 0.04548 | +0.045 (native is 0) | +0.0386 to +0.0524 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.476 | 2.497 | +0.8% | −0.0165 to +0.0581 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294.8 | 299.8 | +1.7% | −0.3878 to +10.2758 | no |
| HPA replicas, mean | 9.469 | 10.92 | +15.3% | +0.3938 to +2.5075 | yes: power given |
| pods started | 5.4 | 10.1 | +87.0% | +2.5660 to +6.8340 | yes: power given |
| pod start wait, total (s) | 7.6 | 17.8 | +134.2% | +6.1006 to +14.2994 | yes: LOSS |
| pod start wait, mean (s) | 1.406 | 1.76 | +25.2% | +0.1031 to +0.6051 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 69.77 | 70.74 | +1.4% | −0.0148 to +1.9535 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.2 |  |  | 10 |
| compass | 27.6 | +43.8% | +6.2 to +10.6 | 10 |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*