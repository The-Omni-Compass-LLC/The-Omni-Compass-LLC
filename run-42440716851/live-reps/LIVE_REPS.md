# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.98 |
| node-hours | 2.514 | 2.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 271 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 127.4 | 104 |
| response time (ms), 95th percentile | 224.5 | 236.7 |
| response time (ms), 99th percentile | 340.3 | 366.9 |
| time over the response line (% of samples) | 0.1615 | 0.3919 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1152 | 1235 |
| utilisation (used / allocatable) | 0.05911 | 0.05808 |
| CPU used (cores), mean | 1.419 | 1.389 |
| Omni's own CPU (cores), mean | 0 | 0.07056 |
| CPU used with Omni's own (cores), mean | 1.419 | 1.46 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.5 | 465.2 |
| HPA replicas, mean | 2.028 | 2.257 |
| pods started | 0 | 1.4 |
| pod start wait, total (s) | 0 | 3.2 |
| pod start wait, mean (s) | 0 | 1.092 |
| host CPU busy, the real machine under kind (%) | 44.01 | 46.06 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1433 | 1457 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.392 |
| queue: job wait, submitted to its first pod running, mean (s) | 162.1 | 185.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 690.1 | 782.5 |
| queue: job turnaround, submitted to done, mean (s) | 832.5 | 847.6 |
| queue: jobs unfinished at the window's end | 11.1 | 11 |
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
| worker nodes in service, mean | 6 | 5.98 | −0.3% | −0.0517 to +0.0115 | no |
| node-hours | 2.514 | 2.509 | −0.2% | −0.0212 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.6 | +0.0% | −1.1952 to +1.3213 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 271 | −0.2% | −1.9872 to +0.8467 | no |
| response time (ms), mean | 127.4 | 104 | −18.4% | −29.1552 to −17.7368 | yes: GAIN |
| response time (ms), 95th percentile | 224.5 | 236.7 | +5.4% | −3.4040 to +27.7830 | no |
| response time (ms), 99th percentile | 340.3 | 366.9 | +7.8% | −4.6604 to +57.7998 | no |
| time over the response line (% of samples) | 0.1615 | 0.3919 | +142.7% | −0.0283 to +0.4890 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.7 | +111.700 (native is 0) | +94.0782 to +129.3218 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1152 | 1235 | +7.3% | +22.0897 to +144.9969 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05911 | 0.05808 | −1.7% | −0.0027 to +0.0007 | no |
| CPU used (cores), mean | 1.419 | 1.389 | −2.1% | −0.0668 to +0.0082 | no |
| Omni's own CPU (cores), mean | 0 | 0.07056 | +0.071 (native is 0) | +0.0615 to +0.0796 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.46 | +2.9% | +0.0081 to +0.0744 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.5 | 465.2 | +1.7% | −4.7279 to +20.1375 | no |
| HPA replicas, mean | 2.028 | 2.257 | +11.3% | −0.0633 to +0.5215 | no |
| pods started | 0 | 1.4 | +1.400 (native is 0) | +0.2715 to +2.5285 | yes: power given |
| pod start wait, total (s) | 0 | 3.2 | +3.200 (native is 0) | +0.3427 to +6.0573 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.092 | +1.092 (native is 0) | +0.1914 to +1.9919 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.01 | 46.06 | +4.7% | +1.5074 to +2.6006 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1433 | 1457 | +1.7% | −13.3970 to +61.7970 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.392 | −10.1% | −2.4083 to +1.1917 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 162.1 | 185.1 | +14.2% | −23.5130 to +69.6047 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 690.1 | 782.5 | +13.4% | −103.9015 to +288.7015 | no |
| queue: job turnaround, submitted to done, mean (s) | 832.5 | 847.6 | +1.8% | −12.5576 to +42.6326 | no |
| queue: jobs unfinished at the window's end | 11.1 | 11 | −0.9% | −2.9899 to +2.7899 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*