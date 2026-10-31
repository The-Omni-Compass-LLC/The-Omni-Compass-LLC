# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.081 |
| node-hours | 2.512 | 2.127 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 244.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 424.9 | 395.7 |
| response time (ms), 95th percentile | 1871 | 1852 |
| response time (ms), 99th percentile | 2650 | 2568 |
| time over the response line (% of samples) | 15.71 | 15.06 |
| failed requests (%) | 0 | 0.0117 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.29 | 26.88 |
| utilisation (used / allocatable) | 0.0625 | 0.07258 |
| CPU used (cores), mean | 1.5 | 1.476 |
| Omni's own CPU (cores), mean | 0 | 0.01822 |
| CPU used with Omni's own (cores), mean | 1.5 | 1.495 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.2 | 402.7 |
| HPA replicas, mean | 1.99 | 2.044 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 45.38 | 46.11 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 837.7 | 840.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.296 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.075 | 1.233 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 4.1 |
| queue: job turnaround, submitted to done, mean (s) | 138 | 142.6 |
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
| worker nodes in service, mean | 6 | 5.081 | −15.3% | −1.5860 to −0.2527 | yes: GAIN |
| node-hours | 2.512 | 2.127 | −15.3% | −0.6614 to −0.1090 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 | −0.1% | −1.2679 to +0.7784 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 244.1 | −10.7% | −50.2748 to −7.9479 | yes: GAIN |
| response time (ms), mean | 424.9 | 395.7 | −6.9% | −71.3600 to +12.9153 | no |
| response time (ms), 95th percentile | 1871 | 1852 | −1.0% | −213.1910 to +175.3380 | no |
| response time (ms), 99th percentile | 2650 | 2568 | −3.1% | −331.3467 to +166.1155 | no |
| time over the response line (% of samples) | 15.71 | 15.06 | −4.1% | −2.9170 to +1.6214 | no |
| failed requests (%) | 0 | 0.0117 | +0.012 (native is 0) | −0.0148 to +0.0382 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 10.1 | +3.1% | −0.5294 to +1.1294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.8 | +30.800 (native is 0) | +20.7302 to +40.8698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.29 | 26.88 | +15.4% | −3.0250 to +10.2084 | no |
| utilisation (used / allocatable) | 0.0625 | 0.07258 | +16.1% | +0.0025 to +0.0176 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.5 | 1.476 | −1.6% | −0.0843 to +0.0371 | no |
| Omni's own CPU (cores), mean | 0 | 0.01822 | +0.018 (native is 0) | +0.0166 to +0.0198 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.5 | 1.495 | −0.4% | −0.0667 to +0.0559 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.2 | 402.7 | −9.7% | −76.0836 to −10.8112 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.99 | 2.044 | +2.7% | −0.0426 to +0.1514 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 45.38 | 46.11 | +1.6% | +0.2140 to +1.2469 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 837.7 | 840.5 | +0.3% | −7.3709 to +12.9709 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.296 | −28.4% | −2.7667 to −0.6405 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.075 | 1.233 | +14.7% | −0.1990 to +0.5157 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 4.1 | +64.0% | −0.2221 to +3.4221 | no |
| queue: job turnaround, submitted to done, mean (s) | 138 | 142.6 | +3.4% | −6.3684 to +15.6600 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*