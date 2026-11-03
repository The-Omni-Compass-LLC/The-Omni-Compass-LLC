# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.516 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 131.9 | 110.1 |
| response time (ms), 95th percentile | 234.6 | 246.4 |
| response time (ms), 99th percentile | 341.9 | 359.4 |
| time over the response line (% of samples) | 0.186 | 0.3557 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 108 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1190 | 1277 |
| utilisation (used / allocatable) | 0.05975 | 0.05825 |
| CPU used (cores), mean | 1.434 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0.0705 |
| CPU used with Omni's own (cores), mean | 1.434 | 1.468 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.9 | 463.4 |
| HPA replicas, mean | 1.978 | 2.156 |
| pods started | 0 | 0.7 |
| pod start wait, total (s) | 0 | 1.3 |
| pod start wait, mean (s) | 0 | 0.7 |
| host CPU busy, the real machine under kind (%) | 45.07 | 46.63 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1466 | 1487 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 179.2 | 219.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 839.1 | 869.1 |
| queue: job turnaround, submitted to done, mean (s) | 856.5 | 877.4 |
| queue: jobs unfinished at the window's end | 11.3 | 12.4 |
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
| node-hours | 2.516 | 2.515 | −0.1% | −0.0087 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.5 | −0.3% | −1.5277 to −0.1478 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.5 | −0.3% | −1.5277 to −0.1478 | yes: GAIN |
| response time (ms), mean | 131.9 | 110.1 | −16.5% | −26.9726 to −16.6183 | yes: GAIN |
| response time (ms), 95th percentile | 234.6 | 246.4 | +5.0% | −2.4040 to +25.9540 | no |
| response time (ms), 99th percentile | 341.9 | 359.4 | +5.1% | −9.3487 to +44.3399 | no |
| time over the response line (% of samples) | 0.186 | 0.3557 | +91.2% | −0.0250 to +0.3644 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 108 | +108.000 (native is 0) | +90.4333 to +125.5667 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1190 | 1277 | +7.3% | +12.0561 to +162.0939 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05975 | 0.05825 | −2.5% | −0.0026 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.434 | 1.398 | −2.5% | −0.0635 to −0.0090 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0705 | +0.071 (native is 0) | +0.0618 to +0.0792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.434 | 1.468 | +2.4% | +0.0068 to +0.0618 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.9 | 463.4 | +2.3% | +2.6086 to +18.4158 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.156 | +9.0% | −0.0219 to +0.3787 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | −0.2099 to +2.8099 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.07 | 46.63 | +3.4% | +0.8091 to +2.3000 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1466 | 1487 | +1.4% | −25.4040 to +66.4040 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 179.2 | 219.7 | +22.6% | −12.2772 to +93.3022 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 839.1 | 869.1 | +3.6% | −178.9149 to +238.9149 | no |
| queue: job turnaround, submitted to done, mean (s) | 856.5 | 877.4 | +2.4% | −50.1747 to +91.8747 | no |
| queue: jobs unfinished at the window's end | 11.3 | 12.4 | +9.7% | −1.2228 to +3.4228 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*