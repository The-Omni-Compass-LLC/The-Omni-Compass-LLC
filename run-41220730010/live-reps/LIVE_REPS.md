# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.823 |
| node-hours | 2.516 | 2.444 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 265.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 116.7 | 86.96 |
| response time (ms), 95th percentile | 205.3 | 194.7 |
| response time (ms), 99th percentile | 299.5 | 300.7 |
| time over the response line (% of samples) | 0.1767 | 0.2236 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 914.5 | 962.6 |
| utilisation (used / allocatable) | 0.05571 | 0.05763 |
| CPU used (cores), mean | 1.337 | 1.346 |
| Omni's own CPU (cores), mean | 0 | 0.01211 |
| CPU used with Omni's own (cores), mean | 1.337 | 1.358 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.8 | 473.2 |
| HPA replicas, mean | 2.007 | 2.015 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 0.2 | 0.4 |
| pod start wait, mean (s) | 0.2 | 0.2 |
| host CPU busy, the real machine under kind (%) | 41.59 | 42.35 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1319 | 1328 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.009 |
| queue: job wait, submitted to its first pod running, mean (s) | 152.2 | 146.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 651.9 | 651.6 |
| queue: job turnaround, submitted to done, mean (s) | 671.7 | 702.2 |
| queue: jobs unfinished at the window's end | 7.9 | 8.9 |

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
| worker nodes in service, mean | 6 | 5.823 | −3.0% | −0.4161 to +0.0612 | no |
| node-hours | 2.516 | 2.444 | −2.8% | −0.1719 to +0.0287 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 271 | +0.2% | −0.7664 to +1.7693 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 265.4 | −1.9% | −12.7192 to +2.5346 | no |
| response time (ms), mean | 116.7 | 86.96 | −25.5% | −37.6887 to −21.8103 | yes: GAIN |
| response time (ms), 95th percentile | 205.3 | 194.7 | −5.2% | −22.3843 to +1.1673 | no |
| response time (ms), 99th percentile | 299.5 | 300.7 | +0.4% | −16.7745 to +19.2121 | no |
| time over the response line (% of samples) | 0.1767 | 0.2236 | +26.6% | −0.1108 to +0.2047 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.5 | +13.500 (native is 0) | +11.4420 to +15.5580 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 914.5 | 962.6 | +5.3% | −23.8563 to +119.9996 | no |
| utilisation (used / allocatable) | 0.05571 | 0.05763 | +3.4% | −0.0001 to +0.0039 | no |
| CPU used (cores), mean | 1.337 | 1.346 | +0.6% | −0.0246 to +0.0416 | no |
| Omni's own CPU (cores), mean | 0 | 0.01211 | +0.012 (native is 0) | +0.0109 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.337 | 1.358 | +1.5% | −0.0127 to +0.0539 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.8 | 473.2 | −2.8% | −28.3258 to +1.1013 | no |
| HPA replicas, mean | 2.007 | 2.015 | +0.4% | −0.1659 to +0.1804 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.8556 to +1.2556 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 41.59 | 42.35 | +1.8% | +0.1053 to +1.3965 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1319 | 1328 | +0.7% | −55.5112 to +75.1112 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.009 | −16.5% | −2.2443 to +0.2632 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 152.2 | 146.8 | −3.5% | −53.6920 to +42.9754 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 651.9 | 651.6 | −0.0% | −185.3581 to +184.7581 | no |
| queue: job turnaround, submitted to done, mean (s) | 671.7 | 702.2 | +4.5% | −33.4509 to +94.3509 | no |
| queue: jobs unfinished at the window's end | 7.9 | 8.9 | +12.7% | −0.0663 to +2.0663 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*