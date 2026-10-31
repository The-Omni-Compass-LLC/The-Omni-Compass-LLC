# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.067 |
| node-hours | 2.52 | 2.124 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 273.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 244.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 407.9 | 381 |
| response time (ms), 95th percentile | 1859 | 1900 |
| response time (ms), 99th percentile | 2697 | 2714 |
| time over the response line (% of samples) | 14.76 | 14.93 |
| failed requests (%) | 0.01124 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.09 | 13.55 |
| utilisation (used / allocatable) | 0.06276 | 0.07498 |
| CPU used (cores), mean | 1.506 | 1.504 |
| Omni's own CPU (cores), mean | 0 | 0.01627 |
| CPU used with Omni's own (cores), mean | 1.506 | 1.521 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.1 | 391 |
| HPA replicas, mean | 2.054 | 2.07 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.1 | 0.5 |
| pod start wait, mean (s) | 0.1 | 0.35 |
| host CPU busy, the real machine under kind (%) | 43.11 | 44.01 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 820.4 | 822.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.471 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 0.1583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 128.8 | 130.7 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.067 | −15.5% | −1.7856 to −0.0796 | yes: GAIN |
| node-hours | 2.52 | 2.124 | −15.7% | −0.7526 to −0.0405 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 273.6 | −0.2% | −1.1097 to +0.0749 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 244.3 | −10.9% | −56.4911 to −3.1729 | yes: GAIN |
| response time (ms), mean | 407.9 | 381 | −6.6% | −48.7790 to −5.1570 | yes: GAIN |
| response time (ms), 95th percentile | 1859 | 1900 | +2.2% | −42.4957 to +124.0217 | no |
| response time (ms), 99th percentile | 2697 | 2714 | +0.6% | −224.0106 to +256.7132 | no |
| time over the response line (% of samples) | 14.76 | 14.93 | +1.1% | −0.6048 to +0.9382 | no |
| failed requests (%) | 0.01124 | 0 | −100.0% | −0.0367 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.2 | +28.200 (native is 0) | +17.9456 to +38.4544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.09 | 13.54 | −3.9% | −2.3062 to +1.2162 | no |
| utilisation (used / allocatable) | 0.06276 | 0.07498 | +19.5% | +0.0009 to +0.0236 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 1.504 | −0.1% | −0.0209 to +0.0176 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.016 (native is 0) | +0.0145 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 1.521 | +1.0% | −0.0049 to +0.0341 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.1 | 391 | −13.3% | −117.5798 to −2.5607 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.054 | 2.07 | +0.8% | −0.1234 to +0.1562 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.3689 to +1.1689 | no |
| pod start wait, mean (s) | 0.1 | 0.35 | +250.0% | −0.2628 to +0.7628 | no |
| host CPU busy, the real machine under kind (%) | 43.11 | 44.01 | +2.1% | +0.5293 to +1.2702 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.4 | 822.8 | +0.3% | −3.7181 to +8.5181 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.471 | −25.5% | −2.8516 to −0.2060 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 0.1583 | −5.0% | −0.1362 to +0.1195 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.7 | −50.0% | −2.3877 to +0.9877 | no |
| queue: job turnaround, submitted to done, mean (s) | 128.8 | 130.7 | +1.4% | −3.9208 to +7.6374 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*