# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.15 |
| node-hours | 2.515 | 2.154 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 246.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 459.9 | 464.3 |
| response time (ms), 95th percentile | 1996 | 2179 |
| response time (ms), 99th percentile | 2763 | 2980 |
| time over the response line (% of samples) | 16.67 | 16.94 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 27.77 | 37.42 |
| utilisation (used / allocatable) | 0.06396 | 0.07507 |
| CPU used (cores), mean | 1.535 | 1.527 |
| Omni's own CPU (cores), mean | 0 | 0.08312 |
| CPU used with Omni's own (cores), mean | 1.535 | 1.611 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.3 | 390.6 |
| HPA replicas, mean | 2.081 | 2.278 |
| pods started | 0 | 0.9 |
| pod start wait, total (s) | 0 | 1.6 |
| pod start wait, mean (s) | 0 | 0.9333 |
| host CPU busy, the real machine under kind (%) | 46.47 | 50.34 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 855.1 | 871.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.519 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.083 | 1.417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 4.4 |
| queue: job turnaround, submitted to done, mean (s) | 154.8 | 167.7 |
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
| worker nodes in service, mean | 6 | 5.15 | −14.2% | −1.6221 to −0.0785 | yes: GAIN |
| node-hours | 2.515 | 2.154 | −14.3% | −0.6850 to −0.0359 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.5 | −0.2% | −1.1575 to +0.2291 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 246.8 | −9.9% | −51.7308 to −2.5684 | yes: GAIN |
| response time (ms), mean | 459.9 | 464.3 | +0.9% | −30.0761 to +38.8101 | no |
| response time (ms), 95th percentile | 1996 | 2179 | +9.1% | +37.7924 to +327.1576 | yes: LOSS |
| response time (ms), 99th percentile | 2763 | 2980 | +7.9% | +21.4801 to +412.7729 | yes: LOSS |
| time over the response line (% of samples) | 16.67 | 16.94 | +1.6% | −1.4033 to +1.9395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.5 | +5.0% | −0.3430 to +1.3430 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.8 | +80.800 (native is 0) | +40.6056 to +120.9944 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 27.77 | 37.42 | +34.8% | +1.4241 to +17.8825 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06396 | 0.07507 | +17.4% | +0.0010 to +0.0212 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.535 | 1.527 | −0.5% | −0.0412 to +0.0259 | no |
| Omni's own CPU (cores), mean | 0 | 0.08312 | +0.083 (native is 0) | +0.0751 to +0.0911 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.535 | 1.611 | +4.9% | +0.0385 to +0.1124 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.3 | 390.6 | −10.7% | −90.4312 to −2.8934 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.081 | 2.278 | +9.5% | −0.0430 to +0.4374 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | +0.1128 to +1.6872 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | +0.2854 to +2.9146 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9333 | +0.933 (native is 0) | +0.2154 to +1.6513 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.47 | 50.34 | +8.3% | +3.2349 to +4.5044 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 855.1 | 871.6 | +1.9% | +4.9697 to +28.0303 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.519 | −24.7% | −2.5913 to −0.3711 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.083 | 1.417 | +30.8% | −0.1479 to +0.8145 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 4.4 | +51.7% | −0.7932 to +3.7932 | no |
| queue: job turnaround, submitted to done, mean (s) | 154.8 | 167.7 | +8.3% | +2.6917 to +23.0416 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*