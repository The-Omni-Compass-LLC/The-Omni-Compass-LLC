# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.263 |
| node-hours | 2.517 | 2.207 |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 251.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 500.8 | 465.4 |
| response time (ms), 95th percentile | 1971 | 1963 |
| response time (ms), 99th percentile | 2771 | 2849 |
| time over the response line (% of samples) | 23.71 | 23.18 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 13.57 |
| utilisation (used / allocatable) | 0.0663 | 0.07626 |
| CPU used (cores), mean | 1.591 | 1.589 |
| Omni's own CPU (cores), mean | 0 | 0.01743 |
| CPU used with Omni's own (cores), mean | 1.591 | 1.607 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.2 | 379.5 |
| HPA replicas, mean | 2.005 | 2.091 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.3 | 0.6 |
| pod start wait, mean (s) | 0.3 | 0.6 |
| host CPU busy, the real machine under kind (%) | 45.37 | 46.43 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 836.6 | 841.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.74 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.2458 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 142.8 | 147.4 |
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
| worker nodes in service, mean | 6 | 5.263 | −12.3% | −1.4772 to +0.0023 | no |
| node-hours | 2.517 | 2.207 | −12.3% | −0.6231 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.9 | −0.0% | −1.4381 to +1.2420 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 251.8 | −8.5% | −47.0504 to +0.5584 | no |
| response time (ms), mean | 500.8 | 465.4 | −7.1% | −51.6719 to −19.1777 | yes: GAIN |
| response time (ms), 95th percentile | 1971 | 1963 | −0.4% | −92.9755 to +75.9945 | no |
| response time (ms), 99th percentile | 2771 | 2849 | +2.8% | −72.7443 to +227.3745 | no |
| time over the response line (% of samples) | 23.71 | 23.18 | −2.2% | −1.4407 to +0.3831 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.2 | +1.8% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.300 (native is 0) | +11.9733 to +56.6267 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 13.58 | +1.1% | −1.5193 to +1.8193 | no |
| utilisation (used / allocatable) | 0.0663 | 0.07626 | +15.0% | +0.0000 to +0.0199 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.591 | 1.589 | −0.1% | −0.0281 to +0.0243 | no |
| Omni's own CPU (cores), mean | 0 | 0.01743 | +0.017 (native is 0) | +0.0159 to +0.0190 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.591 | 1.607 | +1.0% | −0.0119 to +0.0429 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.2 | 379.5 | −9.9% | −83.2476 to −0.0771 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.091 | +4.3% | −0.0859 to +0.2580 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | −0.7144 to +1.3144 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | −0.7144 to +1.3144 | no |
| host CPU busy, the real machine under kind (%) | 45.37 | 46.43 | +2.3% | +0.6623 to +1.4644 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836.6 | 841.7 | +0.6% | −0.6665 to +10.8665 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.74 | −21.0% | −2.3790 to −0.1405 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.2458 | +227.8% | −0.1270 to +0.4687 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.9 | +216.7% | −1.1790 to +3.7790 | no |
| queue: job turnaround, submitted to done, mean (s) | 142.8 | 147.4 | +3.3% | −0.7025 to +9.9859 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*