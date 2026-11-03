# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.785 |
| node-hours | 2.518 | 2.007 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 235.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 430.5 | 420.8 |
| response time (ms), 95th percentile | 1898 | 2039 |
| response time (ms), 99th percentile | 2534 | 2855 |
| time over the response line (% of samples) | 14.22 | 15.23 |
| failed requests (%) | 0 | 0.01149 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.38 | 31.48 |
| utilisation (used / allocatable) | 0.06231 | 0.08013 |
| CPU used (cores), mean | 1.495 | 1.505 |
| Omni's own CPU (cores), mean | 0 | 0.07874 |
| CPU used with Omni's own (cores), mean | 1.495 | 1.584 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.9 | 375.1 |
| HPA replicas, mean | 2.023 | 2.209 |
| pods started | 0.1 | 1 |
| pod start wait, total (s) | 0.2 | 1.7 |
| pod start wait, mean (s) | 0.2 | 0.725 |
| host CPU busy, the real machine under kind (%) | 45.17 | 48.59 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 840.8 | 853.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.962 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.05 | 1.221 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 3.4 |
| queue: job turnaround, submitted to done, mean (s) | 142.1 | 153.6 |
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
| worker nodes in service, mean | 6 | 4.785 | −20.3% | −2.0803 to −0.3498 | yes: GAIN |
| node-hours | 2.518 | 2.007 | −20.3% | −0.8758 to −0.1457 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 | +0.1% | −0.9421 to +1.2470 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 235.6 | −13.9% | −65.7120 to −10.3206 | yes: GAIN |
| response time (ms), mean | 430.5 | 420.8 | −2.3% | −33.9720 to +14.5806 | no |
| response time (ms), 95th percentile | 1898 | 2039 | +7.4% | −27.8054 to +309.6224 | no |
| response time (ms), 99th percentile | 2534 | 2855 | +12.7% | +118.4245 to +524.7509 | yes: LOSS |
| time over the response line (% of samples) | 14.22 | 15.23 | +7.1% | −0.0536 to +2.0747 | no |
| failed requests (%) | 0 | 0.01149 | +0.011 (native is 0) | −0.0145 to +0.0375 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 10.3 | +15.7% | −0.7905 to +3.5905 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.8 | +96.800 (native is 0) | +37.1045 to +156.4955 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.38 | 31.48 | +29.1% | +2.1548 to +12.0352 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06231 | 0.08013 | +28.6% | +0.0053 to +0.0303 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.495 | 1.505 | +0.7% | −0.0100 to +0.0295 | no |
| Omni's own CPU (cores), mean | 0 | 0.07874 | +0.079 (native is 0) | +0.0712 to +0.0862 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.495 | 1.584 | +5.9% | +0.0631 to +0.1140 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.9 | 375.1 | −16.4% | −125.2118 to −22.4759 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.209 | +9.2% | −0.0110 to +0.3824 | no |
| pods started | 0.1 | 1 | +900.0% | −0.2410 to +2.0410 | no |
| pod start wait, total (s) | 0.2 | 1.7 | +750.0% | −0.3850 to +3.3850 | no |
| pod start wait, mean (s) | 0.2 | 0.725 | +262.5% | −0.3925 to +1.4425 | no |
| host CPU busy, the real machine under kind (%) | 45.17 | 48.59 | +7.6% | +2.8275 to +4.0061 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 840.8 | 853.3 | +1.5% | +2.3602 to +22.6398 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.962 | −34.0% | −3.3212 to −0.7544 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.05 | 1.221 | +16.3% | +0.0020 to +0.3397 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 3.4 | +17.2% | −0.3430 to +1.3430 | no |
| queue: job turnaround, submitted to done, mean (s) | 142.1 | 153.6 | +8.1% | +4.0072 to +18.9762 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*