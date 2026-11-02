# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 486.7 | 485.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 486.7 | 485.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 315.2 | 159.2 |
| response time (ms), 95th percentile | 803.6 | 341.7 |
| response time (ms), 99th percentile | 1512 | 848.4 |
| time over the response line (% of samples) | 15.63 | 3.873 |
| failed requests (%) | 1.413 | 1.259 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.7 | 11.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 18 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4033 | 0.7417 |
| utilisation (used / allocatable) | 0.08681 | 0.08435 |
| CPU used (cores), mean | 2.083 | 2.024 |
| Omni's own CPU (cores), mean | 0 | 0.04758 |
| CPU used with Omni's own (cores), mean | 2.083 | 2.072 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 331.7 | 340.5 |
| HPA replicas, mean | 9.869 | 12.89 |
| pods started | 5.1 | 17.3 |
| pod start wait, total (s) | 8 | 33.4 |
| pod start wait, mean (s) | 1.629 | 1.941 |
| host CPU busy, the real machine under kind (%) | 59.98 | 60.25 |
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
| node-hours | 4.334 | 4.338 | +0.1% | −0.0041 to +0.0121 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 486.7 | 485.5 | −0.2% | −2.2363 to −0.0522 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 486.7 | 485.5 | −0.2% | −2.2363 to −0.0522 | yes: GAIN |
| response time (ms), mean | 315.2 | 159.2 | −49.5% | −188.8141 to −123.3029 | yes: GAIN |
| response time (ms), 95th percentile | 803.6 | 341.7 | −57.5% | −542.5656 to −381.1104 | yes: GAIN |
| response time (ms), 99th percentile | 1512 | 848.4 | −43.9% | −806.8696 to −519.6568 | yes: GAIN |
| time over the response line (% of samples) | 15.63 | 3.873 | −75.2% | −15.7600 to −7.7508 | yes: GAIN |
| failed requests (%) | 1.413 | 1.259 | −10.9% | −0.2817 to −0.0256 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.7 | 11.1 | −58.4% | −20.2748 to −10.9252 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.7 | +79.700 (native is 0) | +73.1784 to +86.2216 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4033 | 0.7417 | +83.9% | +0.0188 to +0.6578 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08681 | 0.08435 | −2.8% | −0.0031 to −0.0019 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.083 | 2.024 | −2.8% | −0.0733 to −0.0449 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04758 | +0.048 (native is 0) | +0.0429 to +0.0523 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.083 | 2.072 | −0.6% | −0.0262 to +0.0031 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 331.7 | 340.5 | +2.6% | +6.2153 to +11.2668 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.869 | 12.89 | +30.6% | +1.5699 to +4.4684 | yes: power given |
| pods started | 5.1 | 17.3 | +239.2% | +9.5066 to +14.8934 | yes: power given |
| pod start wait, total (s) | 8 | 33.4 | +317.5% | +19.8881 to +30.9119 | yes: LOSS |
| pod start wait, mean (s) | 1.629 | 1.941 | +19.1% | +0.1713 to +0.4522 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.98 | 60.25 | +0.4% | −0.0908 to +0.6188 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*