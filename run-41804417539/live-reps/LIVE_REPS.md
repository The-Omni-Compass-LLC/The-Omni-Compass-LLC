# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.905 |
| node-hours | 2.513 | 2.057 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 239.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 397.4 | 390.6 |
| response time (ms), 95th percentile | 1456 | 1636 |
| response time (ms), 99th percentile | 2019 | 2282 |
| time over the response line (% of samples) | 17.2 | 16.95 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.2 | 13.82 |
| utilisation (used / allocatable) | 0.06245 | 0.07764 |
| CPU used (cores), mean | 1.499 | 1.499 |
| Omni's own CPU (cores), mean | 0 | 0.07536 |
| CPU used with Omni's own (cores), mean | 1.499 | 1.574 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.8 | 384.7 |
| HPA replicas, mean | 2.009 | 2.303 |
| pods started | 0.2 | 1.1 |
| pod start wait, total (s) | 0.5 | 2.3 |
| pod start wait, mean (s) | 0.5 | 1.2 |
| host CPU busy, the real machine under kind (%) | 42.89 | 46.14 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 805.4 | 819 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.146 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.2875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 111.5 | 122.9 |
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
| worker nodes in service, mean | 6 | 4.905 | −18.3% | −1.8666 to −0.3237 | yes: GAIN |
| node-hours | 2.513 | 2.057 | −18.1% | −0.7787 to −0.1333 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.7 | +0.2% | −0.2414 to +1.2731 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 239.3 | −12.4% | −58.4462 to −9.3513 | yes: GAIN |
| response time (ms), mean | 397.4 | 390.6 | −1.7% | −27.6127 to +13.9257 | no |
| response time (ms), 95th percentile | 1456 | 1636 | +12.3% | −10.9738 to +370.5108 | no |
| response time (ms), 99th percentile | 2019 | 2282 | +13.0% | +23.6654 to +502.3378 | yes: LOSS |
| time over the response line (% of samples) | 17.2 | 16.95 | −1.4% | −0.7353 to +0.2428 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.7 | +2.4% | −1.0064 to +1.4064 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.3 | +134.300 (native is 0) | +62.6168 to +205.9832 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.2 | 13.82 | +13.4% | −1.1291 to +4.3858 | no |
| utilisation (used / allocatable) | 0.06245 | 0.07764 | +24.3% | +0.0039 to +0.0265 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.499 | 1.499 | +0.0% | −0.0246 to +0.0247 | no |
| Omni's own CPU (cores), mean | 0 | 0.07536 | +0.075 (native is 0) | +0.0679 to +0.0829 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.499 | 1.574 | +5.0% | +0.0448 to +0.1060 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.8 | 384.7 | −13.9% | −105.5297 to −18.6022 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.009 | 2.303 | +14.6% | +0.0342 to +0.5525 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | +0.0436 to +1.7564 | yes: power given |
| pod start wait, total (s) | 0.5 | 2.3 | +360.0% | −0.1015 to +3.7015 | no |
| pod start wait, mean (s) | 0.5 | 1.2 | +140.0% | −0.0661 to +1.4661 | no |
| host CPU busy, the real machine under kind (%) | 42.89 | 46.14 | +7.6% | +2.5826 to +3.9197 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.4 | 819 | +1.7% | +2.8402 to +24.3598 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.146 | −30.9% | −2.9326 to −0.7745 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.2875 | +187.5% | −0.1080 to +0.4830 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.9 | +171.4% | −0.5128 to +2.9128 | no |
| queue: job turnaround, submitted to done, mean (s) | 111.5 | 122.9 | +10.2% | +2.4155 to +20.4345 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*