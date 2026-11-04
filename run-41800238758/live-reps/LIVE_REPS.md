# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.657 |
| node-hours | 2.515 | 1.954 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 230.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 355.4 | 343.8 |
| response time (ms), 95th percentile | 1443 | 1573 |
| response time (ms), 99th percentile | 2042 | 2360 |
| time over the response line (% of samples) | 11.88 | 12.44 |
| failed requests (%) | 0.01124 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.99 | 24.83 |
| utilisation (used / allocatable) | 0.06 | 0.07797 |
| CPU used (cores), mean | 1.44 | 1.429 |
| Omni's own CPU (cores), mean | 0 | 0.07905 |
| CPU used with Omni's own (cores), mean | 1.44 | 1.508 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.9 | 386.9 |
| HPA replicas, mean | 2.035 | 2.119 |
| pods started | 0.3 | 0.3 |
| pod start wait, total (s) | 0.3 | 0.4 |
| pod start wait, mean (s) | 0.2 | 0.25 |
| host CPU busy, the real machine under kind (%) | 43.12 | 46.55 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 807.9 | 823.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.809 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9417 | 0.925 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.6 | 2.3 |
| queue: job turnaround, submitted to done, mean (s) | 111.6 | 123.6 |
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
| worker nodes in service, mean | 6 | 4.657 | −22.4% | −2.2238 to −0.4618 | yes: GAIN |
| node-hours | 2.515 | 1.954 | −22.3% | −0.9309 to −0.1923 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.8 | +0.1% | −0.5730 to +1.3190 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 230.6 | −15.4% | −69.7997 to −14.0168 | yes: GAIN |
| response time (ms), mean | 355.4 | 343.8 | −3.3% | −51.8243 to +28.5196 | no |
| response time (ms), 95th percentile | 1443 | 1573 | +9.1% | −120.3670 to +381.5690 | no |
| response time (ms), 99th percentile | 2042 | 2360 | +15.6% | −75.8347 to +712.4539 | no |
| time over the response line (% of samples) | 11.88 | 12.44 | +4.7% | −1.0635 to +2.1853 | no |
| failed requests (%) | 0.01124 | 0 | −100.0% | −0.0367 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.5 | +6.2% | −0.4685 to +1.4685 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.6 | +110.600 (native is 0) | +59.0943 to +162.1057 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.99 | 24.83 | +18.3% | −0.5286 to +8.2119 | no |
| utilisation (used / allocatable) | 0.06 | 0.07797 | +29.9% | +0.0068 to +0.0292 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.44 | 1.429 | −0.8% | −0.0549 to +0.0318 | no |
| Omni's own CPU (cores), mean | 0 | 0.07905 | +0.079 (native is 0) | +0.0724 to +0.0857 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.44 | 1.508 | +4.7% | +0.0185 to +0.1166 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.9 | 386.9 | −16.6% | −125.2044 to −28.7826 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.035 | 2.119 | +4.1% | −0.1736 to +0.3422 | no |
| pods started | 0.3 | 0.3 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.7564 to +0.9564 | no |
| pod start wait, mean (s) | 0.2 | 0.25 | +25.0% | −0.3782 to +0.4782 | no |
| host CPU busy, the real machine under kind (%) | 43.12 | 46.55 | +8.0% | +2.7180 to +4.1433 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 807.9 | 823.6 | +1.9% | +3.3149 to +28.0851 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.809 | −36.5% | −3.4621 to −0.9194 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9417 | 0.925 | −1.8% | −0.2266 to +0.1932 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.6 | 2.3 | −11.5% | −1.8471 to +1.2471 | no |
| queue: job turnaround, submitted to done, mean (s) | 111.6 | 123.6 | +10.8% | +3.4450 to +20.5883 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*