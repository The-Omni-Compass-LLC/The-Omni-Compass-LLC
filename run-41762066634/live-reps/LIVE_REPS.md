# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.548 |
| node-hours | 2.515 | 2.324 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 275.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 261.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 580.7 | 565.9 |
| response time (ms), 95th percentile | 2256 | 2395 |
| response time (ms), 99th percentile | 3152 | 3412 |
| time over the response line (% of samples) | 27.38 | 27.03 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.1 | 13.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.93 | 19.09 |
| utilisation (used / allocatable) | 0.06898 | 0.07538 |
| CPU used (cores), mean | 1.655 | 1.672 |
| Omni's own CPU (cores), mean | 0 | 0.08156 |
| CPU used with Omni's own (cores), mean | 1.655 | 1.754 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.6 | 377.6 |
| HPA replicas, mean | 2.007 | 2.303 |
| pods started | 0.1 | 0.8 |
| pod start wait, total (s) | 0.3 | 2.4 |
| pod start wait, mean (s) | 0.3 | 1.067 |
| host CPU busy, the real machine under kind (%) | 47.86 | 51.39 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 862.8 | 878.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.949 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6292 | 1.258 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.8 | 7 |
| queue: job turnaround, submitted to done, mean (s) | 167.1 | 181.9 |
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
| worker nodes in service, mean | 6 | 5.548 | −7.5% | −0.7110 to −0.1932 | yes: GAIN |
| node-hours | 2.515 | 2.324 | −7.6% | −0.2992 to −0.0822 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 275.9 | +0.0% | −0.5450 to +0.7344 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 261.7 | −5.1% | −22.2231 to −5.9458 | yes: GAIN |
| response time (ms), mean | 580.7 | 565.9 | −2.6% | −34.3706 to +4.6815 | no |
| response time (ms), 95th percentile | 2256 | 2395 | +6.1% | +52.8974 to +223.6666 | yes: LOSS |
| response time (ms), 99th percentile | 3152 | 3412 | +8.2% | +67.6319 to +451.6197 | yes: LOSS |
| time over the response line (% of samples) | 27.38 | 27.03 | −1.3% | −0.8168 to +0.1101 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.1 | 13.4 | +2.3% | −0.4578 to +1.0578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.5 | +65.500 (native is 0) | +22.3421 to +108.6579 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.93 | 19.09 | +19.9% | −0.2811 to +6.6111 | no |
| utilisation (used / allocatable) | 0.06898 | 0.07538 | +9.3% | +0.0032 to +0.0096 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.655 | 1.672 | +1.0% | −0.0019 to +0.0352 | no |
| Omni's own CPU (cores), mean | 0 | 0.08156 | +0.082 (native is 0) | +0.0769 to +0.0862 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.655 | 1.754 | +5.9% | +0.0787 to +0.1177 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.6 | 377.6 | −6.2% | −38.8363 to −11.1109 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.007 | 2.303 | +14.7% | +0.0734 to +0.5186 | yes: power given |
| pods started | 0.1 | 0.8 | +700.0% | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0.3 | 2.4 | +700.0% | −0.5217 to +4.7217 | no |
| pod start wait, mean (s) | 0.3 | 1.067 | +255.6% | −0.1741 to +1.7074 | no |
| host CPU busy, the real machine under kind (%) | 47.86 | 51.39 | +7.4% | +3.1830 to +3.8781 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 862.8 | 878.5 | +1.8% | +9.1959 to +22.2041 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.949 | −17.5% | −1.5982 to −0.5045 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6292 | 1.258 | +100.0% | +0.0068 to +1.2516 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.8 | 7 | +84.2% | −1.5663 to +7.9663 | no |
| queue: job turnaround, submitted to done, mean (s) | 167.1 | 181.9 | +8.9% | +7.5855 to +22.0479 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*