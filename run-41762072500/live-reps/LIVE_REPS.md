# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.847 |
| node-hours | 2.516 | 2.031 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 237.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 348.5 | 346.1 |
| response time (ms), 95th percentile | 1424 | 1589 |
| response time (ms), 99th percentile | 2182 | 2355 |
| time over the response line (% of samples) | 13.12 | 13.42 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.59 | 22.59 |
| utilisation (used / allocatable) | 0.06175 | 0.0783 |
| CPU used (cores), mean | 1.482 | 1.499 |
| Omni's own CPU (cores), mean | 0 | 0.07372 |
| CPU used with Omni's own (cores), mean | 1.482 | 1.573 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 382.6 |
| HPA replicas, mean | 2.014 | 2.26 |
| pods started | 0 | 1 |
| pod start wait, total (s) | 0 | 2.2 |
| pod start wait, mean (s) | 0 | 0.8667 |
| host CPU busy, the real machine under kind (%) | 43.22 | 46.64 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 824.9 | 833.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.216 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8917 | 1.05 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 3.5 |
| queue: job turnaround, submitted to done, mean (s) | 134.6 | 142.8 |
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
| worker nodes in service, mean | 6 | 4.847 | −19.2% | −2.0853 to −0.2202 | yes: GAIN |
| node-hours | 2.516 | 2.031 | −19.3% | −0.8750 to −0.0941 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.5 | +0.1% | −0.6323 to +1.4002 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 237.3 | −13.1% | −65.1382 to −6.5522 | yes: GAIN |
| response time (ms), mean | 348.5 | 346.1 | −0.7% | −24.8826 to +20.0282 | no |
| response time (ms), 95th percentile | 1424 | 1589 | +11.6% | −27.0503 to +357.1863 | no |
| response time (ms), 99th percentile | 2182 | 2355 | +7.9% | −22.4708 to +368.7924 | no |
| time over the response line (% of samples) | 13.12 | 13.42 | +2.3% | −0.6828 to +1.2919 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.8 | +1.3% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.1 | +118.100 (native is 0) | +41.9240 to +194.2760 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.59 | 22.59 | +15.3% | +0.3071 to +5.6796 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06175 | 0.0783 | +26.8% | +0.0035 to +0.0296 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.482 | 1.499 | +1.2% | −0.0299 to +0.0647 | no |
| Omni's own CPU (cores), mean | 0 | 0.07372 | +0.074 (native is 0) | +0.0660 to +0.0814 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.482 | 1.573 | +6.1% | +0.0393 to +0.1429 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 382.6 | −16.7% | −135.2043 to −17.7936 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.26 | +12.2% | −0.0003 to +0.4934 | no |
| pods started | 0 | 1 | +1.000 (native is 0) | −0.0116 to +2.0116 | no |
| pod start wait, total (s) | 0 | 2.2 | +2.200 (native is 0) | −0.1556 to +4.5556 | no |
| pod start wait, mean (s) | 0 | 0.8667 | +0.867 (native is 0) | +0.0316 to +1.7018 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.22 | 46.64 | +7.9% | +2.8103 to +4.0293 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 824.9 | 833.9 | +1.1% | +2.8652 to +15.1348 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.216 | −29.7% | −3.1482 to −0.4188 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8917 | 1.05 | +17.8% | +0.0180 to +0.2987 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 3.5 | +66.7% | +0.1749 to +2.6251 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 134.6 | 142.8 | +6.1% | +1.3223 to +15.2194 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*