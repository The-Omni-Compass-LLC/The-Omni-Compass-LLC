# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.168 |
| node-hours | 2.516 | 2.166 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 247.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 412 | 373.3 |
| response time (ms), 95th percentile | 1737 | 1715 |
| response time (ms), 99th percentile | 2344 | 2321 |
| time over the response line (% of samples) | 14.86 | 14.22 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.96 | 27.76 |
| utilisation (used / allocatable) | 0.06253 | 0.0734 |
| CPU used (cores), mean | 1.501 | 1.499 |
| Omni's own CPU (cores), mean | 0 | 0.01678 |
| CPU used with Omni's own (cores), mean | 1.501 | 1.516 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.7 | 396.9 |
| HPA replicas, mean | 2.012 | 2.1 |
| pods started | 0.1 | 0.5 |
| pod start wait, total (s) | 0.1 | 0.9 |
| pod start wait, mean (s) | 0.1 | 0.5 |
| host CPU busy, the real machine under kind (%) | 45.48 | 46.3 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 834.6 | 837.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.551 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.046 | 1.221 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 4.1 |
| queue: job turnaround, submitted to done, mean (s) | 137.4 | 139.2 |
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
| worker nodes in service, mean | 6 | 5.168 | −13.9% | −1.5811 to −0.0834 | yes: GAIN |
| node-hours | 2.516 | 2.166 | −13.9% | −0.6648 to −0.0355 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.6 | −0.0% | −0.5494 to +0.4777 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 247.4 | −9.6% | −49.7828 to −2.6805 | yes: GAIN |
| response time (ms), mean | 412 | 373.3 | −9.4% | −70.1269 to −7.3395 | yes: GAIN |
| response time (ms), 95th percentile | 1737 | 1715 | −1.3% | −140.0202 to +96.2312 | no |
| response time (ms), 99th percentile | 2344 | 2321 | −1.0% | −147.0107 to +102.2179 | no |
| time over the response line (% of samples) | 14.86 | 14.22 | −4.3% | −2.6561 to +1.3909 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.7 | +1.9% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.9 | +31.900 (native is 0) | +16.5123 to +47.2877 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.96 | 27.76 | +7.0% | −1.0269 to +4.6369 | no |
| utilisation (used / allocatable) | 0.06253 | 0.0734 | +17.4% | +0.0008 to +0.0209 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.501 | 1.499 | −0.1% | −0.0225 to +0.0185 | no |
| Omni's own CPU (cores), mean | 0 | 0.01678 | +0.017 (native is 0) | +0.0156 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.501 | 1.516 | +1.0% | −0.0061 to +0.0357 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.7 | 396.9 | −10.9% | −92.7431 to −4.7945 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.012 | 2.1 | +4.3% | −0.0593 to +0.2338 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0.1 | 0.9 | +800.0% | −0.5403 to +2.1403 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 45.48 | 46.3 | +1.8% | +0.3687 to +1.2673 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 834.6 | 837.1 | +0.3% | −2.9398 to +7.9398 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.551 | −24.2% | −2.6804 to −0.2180 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.046 | 1.221 | +16.7% | −0.0457 to +0.3957 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 4.1 | +41.4% | −0.8176 to +3.2176 | no |
| queue: job turnaround, submitted to done, mean (s) | 137.4 | 139.2 | +1.3% | −3.6827 to +7.2077 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*