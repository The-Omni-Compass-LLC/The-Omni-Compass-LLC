# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.807 |
| node-hours | 2.517 | 2.017 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 236.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 397.7 | 360.6 |
| response time (ms), 95th percentile | 1637 | 1647 |
| response time (ms), 99th percentile | 2304 | 2366 |
| time over the response line (% of samples) | 14.03 | 13.62 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.84 | 18.73 |
| utilisation (used / allocatable) | 0.06356 | 0.08157 |
| CPU used (cores), mean | 1.525 | 1.53 |
| Omni's own CPU (cores), mean | 0 | 0.07077 |
| CPU used with Omni's own (cores), mean | 1.525 | 1.601 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.8 | 369.5 |
| HPA replicas, mean | 1.943 | 2.309 |
| pods started | 0 | 1.1 |
| pod start wait, total (s) | 0 | 2.2 |
| pod start wait, mean (s) | 0 | 0.7917 |
| host CPU busy, the real machine under kind (%) | 43.69 | 46.53 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 818.4 | 827.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.129 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2833 | 0.475 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 2.8 |
| queue: job turnaround, submitted to done, mean (s) | 125.2 | 135.1 |
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
| worker nodes in service, mean | 6 | 4.807 | −19.9% | −2.1179 to −0.2680 | yes: GAIN |
| node-hours | 2.517 | 2.017 | −19.9% | −0.8928 to −0.1082 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.3 | +0.1% | −0.7722 to +1.1343 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 236.8 | −13.6% | −66.8387 to −7.7242 | yes: GAIN |
| response time (ms), mean | 397.7 | 360.6 | −9.3% | −59.0198 to −15.1125 | yes: GAIN |
| response time (ms), 95th percentile | 1637 | 1647 | +0.6% | −79.2270 to +99.5210 | no |
| response time (ms), 99th percentile | 2304 | 2366 | +2.7% | −118.5632 to +241.7616 | no |
| time over the response line (% of samples) | 14.03 | 13.62 | −2.9% | −1.3717 to +0.5511 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.4 | +3.7% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.5 | +103.500 (native is 0) | +51.4650 to +155.5350 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.84 | 18.73 | +26.2% | +0.1829 to +7.5971 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06356 | 0.08157 | +28.3% | +0.0040 to +0.0320 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.525 | 1.53 | +0.3% | −0.0113 to +0.0213 | no |
| Omni's own CPU (cores), mean | 0 | 0.07077 | +0.071 (native is 0) | +0.0631 to +0.0784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.525 | 1.601 | +5.0% | +0.0531 to +0.0984 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.8 | 369.5 | −16.2% | −125.4680 to −17.1914 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.943 | 2.309 | +18.8% | +0.0576 to +0.6744 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | −0.0410 to +2.2410 | no |
| pod start wait, total (s) | 0 | 2.2 | +2.200 (native is 0) | −0.1556 to +4.5556 | no |
| pod start wait, mean (s) | 0 | 0.7917 | +0.792 (native is 0) | +0.0539 to +1.5294 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.69 | 46.53 | +6.5% | +2.1889 to +3.4968 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818.4 | 827.8 | +1.1% | +2.1978 to +16.6022 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.129 | −31.2% | −3.2053 to −0.5373 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2833 | 0.475 | +67.6% | −0.2782 to +0.6615 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 2.8 | +40.0% | −3.4626 to +5.0626 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.2 | 135.1 | +7.9% | +2.3135 to +17.4199 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*