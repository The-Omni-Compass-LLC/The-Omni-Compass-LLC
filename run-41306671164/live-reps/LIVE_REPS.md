# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.765 |
| node-hours | 2.515 | 1.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 233.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 375.3 | 341.3 |
| response time (ms), 95th percentile | 1587 | 1630 |
| response time (ms), 99th percentile | 2144 | 2174 |
| time over the response line (% of samples) | 11.45 | 11.53 |
| failed requests (%) | 0 | 0.01075 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.83 | 24.01 |
| utilisation (used / allocatable) | 0.06028 | 0.07465 |
| CPU used (cores), mean | 1.447 | 1.409 |
| Omni's own CPU (cores), mean | 0 | 0.01713 |
| CPU used with Omni's own (cores), mean | 1.447 | 1.426 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 399.8 |
| HPA replicas, mean | 2.013 | 2.109 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 43.4 | 44.28 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 822 | 823.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.947 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.062 | 1.054 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.4 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 122.7 | 124.9 |
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
| worker nodes in service, mean | 6 | 4.765 | −20.6% | −2.0924 to −0.3776 | yes: GAIN |
| node-hours | 2.515 | 1.998 | −20.5% | −0.8707 to −0.1618 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.5 | −0.1% | −0.8099 to +0.3924 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 233.6 | −14.3% | −65.9260 to −12.2249 | yes: GAIN |
| response time (ms), mean | 375.3 | 341.3 | −9.1% | −47.6855 to −20.2632 | yes: GAIN |
| response time (ms), 95th percentile | 1587 | 1630 | +2.7% | −18.3128 to +105.1278 | no |
| response time (ms), 99th percentile | 2144 | 2174 | +1.4% | −130.8843 to +191.0527 | no |
| time over the response line (% of samples) | 11.45 | 11.53 | +0.7% | −0.9062 to +1.0731 | no |
| failed requests (%) | 0 | 0.01075 | +0.011 (native is 0) | −0.0136 to +0.0351 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.5 | +8.7% | −0.0032 to +1.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.5 | +34.500 (native is 0) | +18.3276 to +50.6724 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.83 | 24.01 | +5.1% | −1.9392 to +4.2825 | no |
| utilisation (used / allocatable) | 0.06028 | 0.07465 | +23.8% | +0.0045 to +0.0242 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.447 | 1.409 | −2.6% | −0.0800 to +0.0047 | no |
| Omni's own CPU (cores), mean | 0 | 0.01713 | +0.017 (native is 0) | +0.0149 to +0.0194 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.447 | 1.426 | −1.4% | −0.0641 to +0.0230 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 399.8 | −13.7% | −106.4337 to −20.2486 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.013 | 2.109 | +4.8% | −0.0895 to +0.2808 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 43.4 | 44.28 | +2.0% | +0.5763 to +1.1946 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822 | 823.9 | +0.2% | −2.3177 to +6.1177 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.947 | −34.2% | −3.3775 to −0.7286 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.062 | 1.054 | −0.8% | −0.1385 to +0.1218 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.4 | 2.5 | −26.5% | −3.2228 to +1.4228 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.7 | 124.9 | +1.8% | −2.6115 to +6.9198 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*