# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 516.1 | 516 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.1 | 516 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 283.9 | 186 |
| response time (ms), 95th percentile | 773.4 | 422 |
| response time (ms), 99th percentile | 2930 | 2540 |
| time over the response line (% of samples) | 18.59 | 13.75 |
| failed requests (%) | 9.719 | 10.23 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.4 | 22.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 81.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.565 | 0.5 |
| utilisation (used / allocatable) | 0.1006 | 0.1004 |
| CPU used (cores), mean | 2.415 | 2.409 |
| Omni's own CPU (cores), mean | 0 | 0.04432 |
| CPU used with Omni's own (cores), mean | 2.415 | 2.454 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 306.5 | 310 |
| HPA replicas, mean | 9.432 | 10.54 |
| pods started | 5.7 | 10.3 |
| pod start wait, total (s) | 8.4 | 18.2 |
| pod start wait, mean (s) | 1.477 | 1.737 |
| host CPU busy, the real machine under kind (%) | 67.86 | 69.16 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.513 | 4.519 | +0.1% | −0.0048 to +0.0165 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516.1 | 516 | −0.0% | −2.0872 to +1.9383 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.1 | 516 | −0.0% | −2.0872 to +1.9383 | no |
| response time (ms), mean | 283.9 | 186 | −34.5% | −132.6168 to −63.2327 | yes: GAIN |
| response time (ms), 95th percentile | 773.4 | 422 | −45.4% | −445.0185 to −257.6635 | yes: GAIN |
| response time (ms), 99th percentile | 2930 | 2540 | −13.3% | −1419.6729 to +639.7445 | no |
| time over the response line (% of samples) | 18.59 | 13.75 | −26.0% | −6.5275 to −3.1566 | yes: GAIN |
| failed requests (%) | 9.719 | 10.23 | +5.3% | −0.0976 to +1.1240 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.4 | 22.5 | −14.8% | −5.6342 to −2.1658 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.8 | +53.800 (native is 0) | +42.6276 to +64.9724 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.565 | 0.5 | −11.5% | −0.3290 to +0.1990 | no |
| utilisation (used / allocatable) | 0.1006 | 0.1004 | −0.3% | −0.0015 to +0.0010 | no |
| CPU used (cores), mean | 2.415 | 2.409 | −0.3% | −0.0362 to +0.0241 | no |
| Omni's own CPU (cores), mean | 0 | 0.04432 | +0.044 (native is 0) | +0.0361 to +0.0526 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.454 | +1.6% | +0.0016 to +0.0750 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 306.5 | 310 | +1.1% | −3.1378 to +10.0783 | no |
| HPA replicas, mean | 9.432 | 10.54 | +11.7% | +0.1571 to +2.0503 | yes: power given |
| pods started | 5.7 | 10.3 | +80.7% | +2.6866 to +6.5134 | yes: power given |
| pod start wait, total (s) | 8.4 | 18.2 | +116.7% | +5.1301 to +14.4699 | yes: LOSS |
| pod start wait, mean (s) | 1.477 | 1.737 | +17.6% | −0.0121 to +0.5322 | no |
| host CPU busy, the real machine under kind (%) | 67.86 | 69.16 | +1.9% | +0.2739 to +2.3331 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 21.6 |  |  | 10 |
| compass | 28.2 | +30.6% | +5.2 to +8.0 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*