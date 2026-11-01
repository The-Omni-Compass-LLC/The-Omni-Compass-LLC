# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.9 | 511.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.9 | 511.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 276.1 | 143.1 |
| response time (ms), 95th percentile | 728.4 | 289.9 |
| response time (ms), 99th percentile | 2620 | 1364 |
| time over the response line (% of samples) | 16.07 | 8.855 |
| failed requests (%) | 7.56 | 6.636 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.4 | 17.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3967 | 0.4933 |
| utilisation (used / allocatable) | 0.09557 | 0.09373 |
| CPU used (cores), mean | 2.294 | 2.249 |
| Omni's own CPU (cores), mean | 0 | 0.00948 |
| CPU used with Omni's own (cores), mean | 2.294 | 2.259 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 319.4 | 324 |
| HPA replicas, mean | 9.538 | 10.91 |
| pods started | 5.7 | 8.6 |
| pod start wait, total (s) | 7.5 | 13.4 |
| pod start wait, mean (s) | 1.31 | 1.589 |
| host CPU busy, the real machine under kind (%) | 64.69 | 63.99 |
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
| node-hours | 4.515 | 4.514 | −0.0% | −0.0091 to +0.0074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.9 | 511.7 | −0.2% | −2.1822 to −0.2526 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.9 | 511.7 | −0.2% | −2.1822 to −0.2526 | yes: GAIN |
| response time (ms), mean | 276.1 | 143.1 | −48.2% | −173.3460 to −92.6226 | yes: GAIN |
| response time (ms), 95th percentile | 728.4 | 289.9 | −60.2% | −535.4340 to −341.4270 | yes: GAIN |
| response time (ms), 99th percentile | 2620 | 1364 | −47.9% | −2288.1491 to −222.9421 | yes: GAIN |
| time over the response line (% of samples) | 16.07 | 8.855 | −44.9% | −9.8267 to −4.6091 | yes: GAIN |
| failed requests (%) | 7.56 | 6.636 | −12.2% | −1.5491 to −0.3003 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.4 | 17.5 | −31.1% | −10.0709 to −5.7291 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.9 | +44.900 (native is 0) | +35.3123 to +54.4877 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3967 | 0.4933 | +24.4% | −0.1569 to +0.3502 | no |
| utilisation (used / allocatable) | 0.09557 | 0.09373 | −1.9% | −0.0028 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.294 | 2.249 | −1.9% | −0.0672 to −0.0212 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00948 | +0.009 (native is 0) | +0.0082 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.294 | 2.259 | −1.5% | −0.0570 to −0.0124 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 319.4 | 324 | +1.4% | +0.9839 to +8.1478 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.538 | 10.91 | +14.4% | +0.1983 to +2.5516 | yes: power given |
| pods started | 5.7 | 8.6 | +50.9% | +0.6519 to +5.1481 | yes: power given |
| pod start wait, total (s) | 7.5 | 13.4 | +78.7% | +2.1232 to +9.6768 | yes: LOSS |
| pod start wait, mean (s) | 1.31 | 1.589 | +21.3% | −0.0733 to +0.6309 | no |
| host CPU busy, the real machine under kind (%) | 64.69 | 63.99 | −1.1% | −1.3060 to −0.0991 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*