# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.3 | 516.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.3 | 516.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 289.3 | 180.9 |
| response time (ms), 95th percentile | 799.3 | 406.4 |
| response time (ms), 99th percentile | 2976 | 2523 |
| time over the response line (% of samples) | 18.95 | 13.15 |
| failed requests (%) | 10.01 | 9.98 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.2 | 22.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 68.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7117 | 0.475 |
| utilisation (used / allocatable) | 0.1024 | 0.1008 |
| CPU used (cores), mean | 2.458 | 2.42 |
| Omni's own CPU (cores), mean | 0 | 0.04447 |
| CPU used with Omni's own (cores), mean | 2.458 | 2.465 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.6 | 305.9 |
| HPA replicas, mean | 9.43 | 10.76 |
| pods started | 5.7 | 10.6 |
| pod start wait, total (s) | 7.8 | 20.8 |
| pod start wait, mean (s) | 1.399 | 1.888 |
| host CPU busy, the real machine under kind (%) | 69.02 | 69.53 |
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
| node-hours | 4.513 | 4.518 | +0.1% | −0.0009 to +0.0109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.3 | 516.7 | −0.1% | −2.5553 to +1.5236 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.3 | 516.7 | −0.1% | −2.5553 to +1.5236 | no |
| response time (ms), mean | 289.3 | 180.9 | −37.5% | −126.0843 to −90.7819 | yes: GAIN |
| response time (ms), 95th percentile | 799.3 | 406.4 | −49.2% | −502.2599 to −283.5201 | yes: GAIN |
| response time (ms), 99th percentile | 2976 | 2523 | −15.2% | −978.8400 to +74.0312 | no |
| time over the response line (% of samples) | 18.95 | 13.15 | −30.6% | −7.3083 to −4.3035 | yes: GAIN |
| failed requests (%) | 10.01 | 9.98 | −0.3% | −0.5914 to +0.5273 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.2 | 22.2 | −21.3% | −8.7601 to −3.2399 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53 | +53.000 (native is 0) | +42.5088 to +63.4912 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7117 | 0.475 | −33.3% | −0.8210 to +0.3477 | no |
| utilisation (used / allocatable) | 0.1024 | 0.1008 | −1.6% | −0.0043 to +0.0011 | no |
| CPU used (cores), mean | 2.458 | 2.42 | −1.6% | −0.1029 to +0.0260 | no |
| Omni's own CPU (cores), mean | 0 | 0.04447 | +0.044 (native is 0) | +0.0376 to +0.0513 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.465 | +0.2% | −0.0635 to +0.0756 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.6 | 305.9 | +3.1% | −6.1389 to +24.8053 | no |
| HPA replicas, mean | 9.43 | 10.76 | +14.1% | −0.0608 to +2.7187 | no |
| pods started | 5.7 | 10.6 | +86.0% | +2.9208 to +6.8792 | yes: power given |
| pod start wait, total (s) | 7.8 | 20.8 | +166.7% | +2.5795 to +23.4205 | yes: LOSS |
| pod start wait, mean (s) | 1.399 | 1.888 | +35.0% | −0.3241 to +1.3031 | no |
| host CPU busy, the real machine under kind (%) | 69.02 | 69.53 | +0.7% | −1.3822 to +2.4076 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.2 |  |  | 10 |
| compass | 28.8 | +50.0% | +6.6 to +12.6 | 10 |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*