# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.511 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.4 | 511.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.4 | 511.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 251.7 | 135.6 |
| response time (ms), 95th percentile | 694.4 | 288.2 |
| response time (ms), 99th percentile | 1991 | 1168 |
| time over the response line (% of samples) | 16.94 | 10.49 |
| failed requests (%) | 9.425 | 8.522 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.7 | 18.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 60 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6883 | 0.4083 |
| utilisation (used / allocatable) | 0.09543 | 0.09349 |
| CPU used (cores), mean | 2.29 | 2.244 |
| Omni's own CPU (cores), mean | 0 | 0.00905 |
| CPU used with Omni's own (cores), mean | 2.29 | 2.253 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 328.7 | 338.1 |
| HPA replicas, mean | 9.329 | 9.173 |
| pods started | 5.7 | 6.3 |
| pod start wait, total (s) | 8.5 | 10.1 |
| pod start wait, mean (s) | 1.522 | 1.596 |
| host CPU busy, the real machine under kind (%) | 64.71 | 63.91 |
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
| node-hours | 4.511 | 4.513 | +0.0% | −0.0060 to +0.0083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.4 | 511.2 | −0.2% | −2.1585 to −0.1376 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.4 | 511.2 | −0.2% | −2.1585 to −0.1376 | yes: GAIN |
| response time (ms), mean | 251.7 | 135.6 | −46.1% | −158.4060 to −73.9185 | yes: GAIN |
| response time (ms), 95th percentile | 694.4 | 288.2 | −58.5% | −519.4517 to −292.8693 | yes: GAIN |
| response time (ms), 99th percentile | 1991 | 1168 | −41.3% | −1642.0093 to −2.7527 | yes: GAIN |
| time over the response line (% of samples) | 16.94 | 10.49 | −38.1% | −9.4626 to −3.4348 | yes: GAIN |
| failed requests (%) | 9.425 | 8.522 | −9.6% | −1.7869 to −0.0192 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.7 | 18.1 | −23.6% | −7.3586 to −3.8414 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +25.7297 to +41.8703 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6883 | 0.4083 | −40.7% | −0.7997 to +0.2397 | no |
| utilisation (used / allocatable) | 0.09543 | 0.09349 | −2.0% | −0.0030 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.29 | 2.244 | −2.0% | −0.0725 to −0.0207 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00905 | +0.009 (native is 0) | +0.0073 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.29 | 2.253 | −1.6% | −0.0642 to −0.0108 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 328.7 | 338.1 | +2.9% | +1.4939 to +17.3627 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.329 | 9.173 | −1.7% | −0.8462 to +0.5327 | no |
| pods started | 5.7 | 6.3 | +10.5% | −0.7985 to +1.9985 | no |
| pod start wait, total (s) | 8.5 | 10.1 | +18.8% | −2.5600 to +5.7600 | no |
| pod start wait, mean (s) | 1.522 | 1.596 | +4.8% | −0.2666 to +0.4133 | no |
| host CPU busy, the real machine under kind (%) | 64.71 | 63.91 | −1.2% | −1.5877 to +0.0006 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 24.0 |  |  | 10 |
| compass | 32.4 | +35.0% | +5.4 to +11.4 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*