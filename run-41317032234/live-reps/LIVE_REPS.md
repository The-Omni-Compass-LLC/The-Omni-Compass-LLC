# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.517 |
| node-hours | 2.519 | 2.316 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 276.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 261.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 514.7 | 479.7 |
| response time (ms), 95th percentile | 2385 | 2432 |
| response time (ms), 99th percentile | 3367 | 3479 |
| time over the response line (% of samples) | 20.35 | 19.5 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 12.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.07 | 16.39 |
| utilisation (used / allocatable) | 0.06848 | 0.07579 |
| CPU used (cores), mean | 1.644 | 1.656 |
| Omni's own CPU (cores), mean | 0 | 0.01735 |
| CPU used with Omni's own (cores), mean | 1.644 | 1.673 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 405.9 | 375.7 |
| HPA replicas, mean | 2.057 | 2.264 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 0.3 | 0.5 |
| pod start wait, mean (s) | 0.3 | 0.5 |
| host CPU busy, the real machine under kind (%) | 46.86 | 48.03 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 854.3 | 860.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.135 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.175 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 163.1 | 168.5 |
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
| worker nodes in service, mean | 6 | 5.517 | −8.1% | −1.1136 to +0.1473 | no |
| node-hours | 2.519 | 2.316 | −8.0% | −0.4692 to +0.0640 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 276.3 | +0.1% | −0.3273 to +0.8517 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 261.1 | −5.4% | −34.8636 to +4.9755 | no |
| response time (ms), mean | 514.7 | 479.7 | −6.8% | −54.8198 to −15.2746 | yes: GAIN |
| response time (ms), 95th percentile | 2385 | 2432 | +2.0% | −62.8143 to +157.6633 | no |
| response time (ms), 99th percentile | 3367 | 3479 | +3.3% | −48.4748 to +272.8164 | no |
| time over the response line (% of samples) | 20.35 | 19.5 | −4.2% | −1.8641 to +0.1501 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 12.2 | −0.8% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.7 | +27.700 (native is 0) | +13.7152 to +41.6848 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.07 | 16.39 | +2.0% | −2.5057 to +3.1357 | no |
| utilisation (used / allocatable) | 0.06848 | 0.07579 | +10.7% | −0.0021 to +0.0168 | no |
| CPU used (cores), mean | 1.644 | 1.656 | +0.8% | +0.0006 to +0.0246 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01735 | +0.017 (native is 0) | +0.0163 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.644 | 1.673 | +1.8% | +0.0184 to +0.0415 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 405.9 | 375.7 | −7.4% | −68.8812 to +8.5393 | no |
| HPA replicas, mean | 2.057 | 2.264 | +10.1% | +0.0032 to +0.4106 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | −0.4573 to +0.8573 | no |
| pod start wait, mean (s) | 0.3 | 0.5 | +66.7% | −0.4573 to +0.8573 | no |
| host CPU busy, the real machine under kind (%) | 46.86 | 48.03 | +2.5% | +0.6028 to +1.7271 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 854.3 | 860.4 | +0.7% | −0.6225 to +12.8225 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.135 | −14.4% | −1.8782 to +0.1483 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.175 | +44.8% | −0.0972 to +0.2055 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.9 | +80.0% | −0.2911 to +1.0911 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.1 | 168.5 | +3.3% | −1.9548 to +12.7714 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*