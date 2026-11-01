# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 521 | 520.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521 | 520.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 311.1 | 185.2 |
| response time (ms), 95th percentile | 821.7 | 424.7 |
| response time (ms), 99th percentile | 2886 | 2766 |
| time over the response line (% of samples) | 22.72 | 15.36 |
| failed requests (%) | 12.8 | 12.22 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 30.1 | 25.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7933 | 0.48 |
| utilisation (used / allocatable) | 0.1079 | 0.1072 |
| CPU used (cores), mean | 2.59 | 2.572 |
| Omni's own CPU (cores), mean | 0 | 0.01018 |
| CPU used with Omni's own (cores), mean | 2.59 | 2.582 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.2 | 290.9 |
| HPA replicas, mean | 9.49 | 10.42 |
| pods started | 5.2 | 7.9 |
| pod start wait, total (s) | 7.4 | 13.9 |
| pod start wait, mean (s) | 1.439 | 1.752 |
| host CPU busy, the real machine under kind (%) | 72.72 | 72.9 |
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
| node-hours | 4.513 | 4.512 | −0.0% | −0.0092 to +0.0068 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521 | 520.4 | −0.1% | −1.6433 to +0.5216 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521 | 520.4 | −0.1% | −1.6433 to +0.5216 | no |
| response time (ms), mean | 311.1 | 185.2 | −40.5% | −155.3412 to −96.4603 | yes: GAIN |
| response time (ms), 95th percentile | 821.7 | 424.7 | −48.3% | −514.8237 to −279.2363 | yes: GAIN |
| response time (ms), 99th percentile | 2886 | 2766 | −4.2% | −789.0549 to +549.0115 | no |
| time over the response line (% of samples) | 22.72 | 15.36 | −32.4% | −9.9589 to −4.7596 | yes: GAIN |
| failed requests (%) | 12.8 | 12.22 | −4.5% | −1.3774 to +0.2254 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 30.1 | 25.3 | −15.9% | −6.3379 to −3.2621 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 | +38.000 (native is 0) | +30.9028 to +45.0972 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7933 | 0.48 | −39.5% | −0.8695 to +0.2428 | no |
| utilisation (used / allocatable) | 0.1079 | 0.1072 | −0.7% | −0.0021 to +0.0006 | no |
| CPU used (cores), mean | 2.59 | 2.572 | −0.7% | −0.0509 to +0.0139 | no |
| Omni's own CPU (cores), mean | 0 | 0.01018 | +0.010 (native is 0) | +0.0088 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.59 | 2.582 | −0.3% | −0.0413 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.2 | 290.9 | +1.3% | −1.4050 to +8.9025 | no |
| HPA replicas, mean | 9.49 | 10.42 | +9.7% | +0.1715 to +1.6788 | yes: power given |
| pods started | 5.2 | 7.9 | +51.9% | +1.1529 to +4.2471 | yes: power given |
| pod start wait, total (s) | 7.4 | 13.9 | +87.8% | +3.7348 to +9.2652 | yes: LOSS |
| pod start wait, mean (s) | 1.439 | 1.752 | +21.8% | +0.0035 to +0.6239 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 72.72 | 72.9 | +0.2% | −0.7148 to +1.0700 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 18.0 |  |  | 10 |
| compass | 25.8 | +43.3% | +5.7 to +9.9 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*