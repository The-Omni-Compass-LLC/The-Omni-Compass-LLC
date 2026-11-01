# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.508 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 513.1 | 512.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 513.1 | 512.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 262 | 142.7 |
| response time (ms), 95th percentile | 729.9 | 269 |
| response time (ms), 99th percentile | 2200 | 1506 |
| time over the response line (% of samples) | 16.27 | 9.436 |
| failed requests (%) | 8.451 | 7.531 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.9 | 18 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3533 | 0.355 |
| utilisation (used / allocatable) | 0.09718 | 0.09464 |
| CPU used (cores), mean | 2.332 | 2.271 |
| Omni's own CPU (cores), mean | 0 | 0.00886 |
| CPU used with Omni's own (cores), mean | 2.332 | 2.28 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.5 | 326.6 |
| HPA replicas, mean | 9.413 | 9.584 |
| pods started | 5.2 | 7.7 |
| pod start wait, total (s) | 7.9 | 11.8 |
| pod start wait, mean (s) | 1.515 | 1.481 |
| host CPU busy, the real machine under kind (%) | 65.44 | 64.34 |
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
| node-hours | 4.508 | 4.512 | +0.1% | −0.0019 to +0.0105 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 513.1 | 512.1 | −0.2% | −1.9994 to −0.1774 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 513.1 | 512.1 | −0.2% | −1.9994 to −0.1774 | yes: GAIN |
| response time (ms), mean | 262 | 142.7 | −45.5% | −148.7869 to −89.7373 | yes: GAIN |
| response time (ms), 95th percentile | 729.9 | 269 | −63.2% | −593.5287 to −328.3893 | yes: GAIN |
| response time (ms), 99th percentile | 2200 | 1506 | −31.5% | −1059.9492 to −327.7136 | yes: GAIN |
| time over the response line (% of samples) | 16.27 | 9.436 | −42.0% | −9.4056 to −4.2525 | yes: GAIN |
| failed requests (%) | 8.451 | 7.531 | −10.9% | −1.7357 to −0.1045 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.9 | 18 | −27.7% | −8.7299 to −5.0701 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.4 | +37.400 (native is 0) | +28.6186 to +46.1814 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3533 | 0.355 | +0.5% | −0.2828 to +0.2861 | no |
| utilisation (used / allocatable) | 0.09718 | 0.09464 | −2.6% | −0.0038 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.332 | 2.271 | −2.6% | −0.0922 to −0.0297 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00886 | +0.009 (native is 0) | +0.0074 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.28 | −2.2% | −0.0841 to −0.0201 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.5 | 326.6 | +3.5% | +0.7700 to +21.4395 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.413 | 9.584 | +1.8% | −0.4848 to +0.8258 | no |
| pods started | 5.2 | 7.7 | +48.1% | +0.6150 to +4.3850 | yes: power given |
| pod start wait, total (s) | 7.9 | 11.8 | +49.4% | −0.7043 to +8.5043 | no |
| pod start wait, mean (s) | 1.515 | 1.481 | −2.2% | −0.4448 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 65.44 | 64.34 | −1.7% | −1.9934 to −0.2127 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 22.8 |  |  | 10 |
| compass | 33.0 | +44.7% | +6.1 to +14.3 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*