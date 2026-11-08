# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.564 |
| node-hours | 2.515 | 2.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 261.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 489.4 | 460.3 |
| response time (ms), 95th percentile | 2154 | 2350 |
| response time (ms), 99th percentile | 3139 | 3222 |
| time over the response line (% of samples) | 19.17 | 18.11 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.51 | 15.67 |
| utilisation (used / allocatable) | 0.06674 | 0.07209 |
| CPU used (cores), mean | 1.602 | 1.602 |
| Omni's own CPU (cores), mean | 0 | 0.07646 |
| CPU used with Omni's own (cores), mean | 1.602 | 1.678 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.7 | 394.7 |
| HPA replicas, mean | 2.064 | 2.408 |
| pods started | 0.1 | 1.5 |
| pod start wait, total (s) | 0.2 | 3 |
| pod start wait, mean (s) | 0.2 | 1.417 |
| host CPU busy, the real machine under kind (%) | 45.95 | 49.23 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 841.9 | 853.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.283 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.2333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 149.3 | 162.3 |
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
| worker nodes in service, mean | 6 | 5.564 | −7.3% | −1.0861 to +0.2134 | no |
| node-hours | 2.515 | 2.334 | −7.2% | −0.4539 to +0.0915 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275.3 | +0.1% | −0.8631 to +1.4889 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 261.5 | −4.9% | −34.4592 to +7.5516 | no |
| response time (ms), mean | 489.4 | 460.3 | −5.9% | −43.6233 to −14.4607 | yes: GAIN |
| response time (ms), 95th percentile | 2154 | 2350 | +9.1% | +56.7303 to +333.7427 | yes: LOSS |
| response time (ms), 99th percentile | 3139 | 3222 | +2.7% | −15.7119 to +182.5645 | no |
| time over the response line (% of samples) | 19.17 | 18.11 | −5.5% | −2.2479 to +0.1270 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12.3 | +3.4% | −0.8707 to +1.6707 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.4 | +53.400 (native is 0) | +13.1556 to +93.6444 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.51 | 15.66 | +7.9% | −1.0136 to +3.3203 | no |
| utilisation (used / allocatable) | 0.06674 | 0.07209 | +8.0% | −0.0009 to +0.0117 | no |
| CPU used (cores), mean | 1.602 | 1.602 | +0.0% | −0.0511 to +0.0517 | no |
| Omni's own CPU (cores), mean | 0 | 0.07646 | +0.076 (native is 0) | +0.0715 to +0.0814 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.602 | 1.678 | +4.8% | +0.0216 to +0.1319 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.7 | 394.7 | −5.7% | −51.4236 to +3.5272 | no |
| HPA replicas, mean | 2.064 | 2.408 | +16.7% | +0.0086 to +0.6799 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.3772 to +2.4228 | yes: power given |
| pod start wait, total (s) | 0.2 | 3 | +1400.0% | +0.8396 to +4.7604 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.417 | +608.3% | +0.5329 to +1.9005 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.95 | 49.23 | +7.1% | +3.0181 to +3.5521 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841.9 | 853.1 | +1.3% | +5.5194 to +16.8806 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.283 | −12.0% | −1.6290 to +0.1940 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.2333 | +133.3% | −0.0292 to +0.2959 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.1 | +83.3% | −0.7274 to +1.7274 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.3 | 162.3 | +8.7% | +7.1544 to +18.7873 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*