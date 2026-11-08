# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.875 |
| node-hours | 2.514 | 2.047 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 238.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 434.7 | 422.9 |
| response time (ms), 95th percentile | 1625 | 1801 |
| response time (ms), 99th percentile | 2273 | 2553 |
| time over the response line (% of samples) | 20.17 | 20.88 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 13.5 |
| utilisation (used / allocatable) | 0.06425 | 0.07962 |
| CPU used (cores), mean | 1.542 | 1.523 |
| Omni's own CPU (cores), mean | 0 | 0.07471 |
| CPU used with Omni's own (cores), mean | 1.542 | 1.598 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.2 | 374.5 |
| HPA replicas, mean | 1.997 | 2.318 |
| pods started | 0 | 1.9 |
| pod start wait, total (s) | 0 | 4.2 |
| pod start wait, mean (s) | 0 | 1.675 |
| host CPU busy, the real machine under kind (%) | 43.83 | 46.91 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 810.4 | 820.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.066 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 116.7 | 126.4 |
| queue: jobs unfinished at the window's end | 0 | 0 |
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
| worker nodes in service, mean | 6 | 4.875 | −18.8% | −1.9290 to −0.3216 | yes: GAIN |
| node-hours | 2.514 | 2.047 | −18.6% | −0.8057 to −0.1290 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.2 | +0.1% | −0.5877 to +1.2962 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 238.9 | −12.8% | −60.8083 to −9.1916 | yes: GAIN |
| response time (ms), mean | 434.7 | 422.9 | −2.7% | −28.1525 to +4.4559 | no |
| response time (ms), 95th percentile | 1625 | 1801 | +10.8% | +85.1483 to +266.1387 | yes: LOSS |
| response time (ms), 99th percentile | 2273 | 2553 | +12.3% | +147.2936 to +412.0230 | yes: LOSS |
| time over the response line (% of samples) | 20.17 | 20.88 | +3.5% | −1.4191 to +2.8370 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.9 | +1.9% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.3 | +111.300 (native is 0) | +25.8581 to +196.7419 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 13.51 | +19.6% | −0.4700 to +4.8933 | no |
| utilisation (used / allocatable) | 0.06425 | 0.07962 | +23.9% | +0.0039 to +0.0269 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.542 | 1.523 | −1.2% | −0.0475 to +0.0091 | no |
| Omni's own CPU (cores), mean | 0 | 0.07471 | +0.075 (native is 0) | +0.0686 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.542 | 1.598 | +3.6% | +0.0220 to +0.0891 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.2 | 374.5 | −13.4% | −100.2776 to −15.1703 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.318 | +16.1% | +0.1410 to +0.5024 | yes: power given |
| pods started | 0 | 1.9 | +1.900 (native is 0) | +0.8634 to +2.9366 | yes: power given |
| pod start wait, total (s) | 0 | 4.2 | +4.200 (native is 0) | +1.4647 to +6.9353 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.675 | +1.675 (native is 0) | +0.9208 to +2.4292 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.83 | 46.91 | +7.0% | +2.3645 to +3.7886 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.4 | 820.6 | +1.3% | +2.6842 to +17.7158 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.066 | −32.2% | −3.1097 to −0.7586 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1125 | +145.5% | −0.0774 to +0.2108 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | +125.0% | −0.4685 to +1.4685 | no |
| queue: job turnaround, submitted to done, mean (s) | 116.7 | 126.4 | +8.3% | +2.2063 to +17.2270 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*