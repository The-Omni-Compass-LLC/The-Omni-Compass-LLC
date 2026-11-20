# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 3.839 |
| node-hours | 2.514 | 1.605 |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 268.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 200.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 185.2 | 173.5 |
| response time (ms), 95th percentile | 650.7 | 684.2 |
| response time (ms), 99th percentile | 874.5 | 1048 |
| time over the response line (% of samples) | 4.024 | 5.318 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 4.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 140.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.16 | 15.25 |
| utilisation (used / allocatable) | 0.05009 | 0.07932 |
| CPU used (cores), mean | 1.202 | 1.2 |
| Omni's own CPU (cores), mean | 0 | 0.06683 |
| CPU used with Omni's own (cores), mean | 1.202 | 1.267 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.8 | 403.3 |
| HPA replicas, mean | 1.95 | 2.088 |
| pods started | 0.3 | 0.7 |
| pod start wait, total (s) | 0.5 | 1.4 |
| pod start wait, mean (s) | 0.5 | 0.6 |
| host CPU busy, the real machine under kind (%) | 36.81 | 39.66 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 749.9 | 754.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 2.754 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.75 | 0.7208 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 55.99 | 61.24 |
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
| worker nodes in service, mean | 6 | 3.839 | −36.0% | −2.9031 to −1.4190 | yes: GAIN |
| node-hours | 2.514 | 1.605 | −36.2% | −1.2197 to −0.5991 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 268.7 | −0.1% | −2.0409 to +1.3215 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 200.8 | −25.3% | −91.4684 to −44.8593 | yes: GAIN |
| response time (ms), mean | 185.2 | 173.5 | −6.3% | −18.4295 to −5.0694 | yes: GAIN |
| response time (ms), 95th percentile | 650.7 | 684.2 | +5.1% | −61.0770 to +128.0280 | no |
| response time (ms), 99th percentile | 874.5 | 1048 | +19.8% | +21.2850 to +325.2040 | yes: LOSS |
| time over the response line (% of samples) | 4.024 | 5.318 | +32.2% | −0.1816 to +2.7691 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 4.5 | +40.6% | −0.6090 to +3.2090 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 140.3 | +140.300 (native is 0) | +76.1603 to +204.4397 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.16 | 15.25 | +0.6% | −1.8887 to +2.0587 | no |
| utilisation (used / allocatable) | 0.05009 | 0.07932 | +58.4% | +0.0183 to +0.0402 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.202 | 1.2 | −0.1% | −0.0588 to +0.0553 | no |
| Omni's own CPU (cores), mean | 0 | 0.06683 | +0.067 (native is 0) | +0.0583 to +0.0753 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.202 | 1.267 | +5.4% | +0.0052 to +0.1249 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.8 | 403.3 | −27.6% | −227.3279 to −79.6642 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.95 | 2.088 | +7.1% | −0.0853 to +0.3619 | no |
| pods started | 0.3 | 0.7 | +133.3% | −0.6228 to +1.4228 | no |
| pod start wait, total (s) | 0.5 | 1.4 | +180.0% | −1.0792 to +2.8792 | no |
| pod start wait, mean (s) | 0.5 | 0.6 | +20.0% | −0.7564 to +0.9564 | no |
| host CPU busy, the real machine under kind (%) | 36.81 | 39.66 | +7.7% | +2.3413 to +3.3636 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.9 | 754.9 | +0.7% | +0.0787 to +9.9213 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 2.754 | −54.1% | −4.0909 to −2.4003 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.75 | 0.7208 | −3.9% | −0.1476 to +0.0893 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 | +7.1% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.99 | 61.24 | +9.4% | +0.6122 to +9.8961 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*