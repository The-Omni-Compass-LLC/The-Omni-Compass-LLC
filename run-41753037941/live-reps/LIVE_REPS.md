# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.328 |
| energy, parked workers still on at idle power (Wh, declared model) | 473.9 | 472.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 473.9 | 472.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 208.5 | 107.2 |
| response time (ms), 95th percentile | 532 | 217.6 |
| response time (ms), 99th percentile | 983.9 | 530 |
| time over the response line (% of samples) | 8.172 | 1.998 |
| failed requests (%) | 0.6181 | 0.5551 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 46.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.575 | 0.67 |
| utilisation (used / allocatable) | 0.0671 | 0.06528 |
| CPU used (cores), mean | 1.61 | 1.567 |
| Omni's own CPU (cores), mean | 0 | 0.03892 |
| CPU used with Omni's own (cores), mean | 1.61 | 1.606 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.5 | 464.8 |
| HPA replicas, mean | 9.534 | 10.76 |
| pods started | 7.6 | 15.7 |
| pod start wait, total (s) | 10.6 | 25.3 |
| pod start wait, mean (s) | 1.454 | 1.613 |
| host CPU busy, the real machine under kind (%) | 46.88 | 47.29 |
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
| node-hours | 4.334 | 4.328 | −0.1% | −0.0131 to +0.0008 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 473.9 | 472.1 | −0.4% | −2.5752 to −1.0435 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 473.9 | 472.1 | −0.4% | −2.5752 to −1.0435 | yes: GAIN |
| response time (ms), mean | 208.5 | 107.2 | −48.6% | −145.6507 to −56.8630 | yes: GAIN |
| response time (ms), 95th percentile | 532 | 217.6 | −59.1% | −426.6900 to −202.2460 | yes: GAIN |
| response time (ms), 99th percentile | 983.9 | 530 | −46.1% | −601.2213 to −306.5649 | yes: GAIN |
| time over the response line (% of samples) | 8.172 | 1.998 | −75.5% | −10.7250 to −1.6220 | yes: GAIN |
| failed requests (%) | 0.6181 | 0.5551 | −10.2% | −0.1533 to +0.0272 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15 | 5.6 | −62.7% | −15.1344 to −3.6656 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.6 | +65.600 (native is 0) | +46.2317 to +84.9683 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.575 | 0.67 | +16.5% | −0.2111 to +0.4011 | no |
| utilisation (used / allocatable) | 0.0671 | 0.06528 | −2.7% | −0.0027 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.567 | −2.7% | −0.0652 to −0.0221 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03892 | +0.039 (native is 0) | +0.0311 to +0.0468 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.606 | −0.3% | −0.0238 to +0.0143 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.5 | 464.8 | +2.3% | +6.2177 to +14.2842 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.534 | 10.76 | +12.9% | −0.6065 to +3.0610 | no |
| pods started | 7.6 | 15.7 | +106.6% | +3.3259 to +12.8741 | yes: power given |
| pod start wait, total (s) | 10.6 | 25.3 | +138.7% | +7.0697 to +22.3303 | yes: LOSS |
| pod start wait, mean (s) | 1.454 | 1.613 | +11.0% | −0.0842 to +0.4027 | no |
| host CPU busy, the real machine under kind (%) | 46.88 | 47.29 | +0.9% | −0.1679 to +0.9830 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*