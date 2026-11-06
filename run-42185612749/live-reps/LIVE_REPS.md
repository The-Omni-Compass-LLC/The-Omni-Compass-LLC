# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.973 |
| node-hours | 2.516 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 124.6 | 106 |
| response time (ms), 95th percentile | 219.3 | 233.3 |
| response time (ms), 99th percentile | 324.7 | 356 |
| time over the response line (% of samples) | 0.2152 | 0.2709 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1111 | 1220 |
| utilisation (used / allocatable) | 0.06005 | 0.0582 |
| CPU used (cores), mean | 1.441 | 1.391 |
| Omni's own CPU (cores), mean | 0 | 0.06945 |
| CPU used with Omni's own (cores), mean | 1.441 | 1.46 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.6 | 464.6 |
| HPA replicas, mean | 1.984 | 2.107 |
| pods started | 0.2 | 0.6 |
| pod start wait, total (s) | 0.6 | 1.5 |
| pod start wait, mean (s) | 0.6 | 0.7 |
| host CPU busy, the real machine under kind (%) | 44.84 | 46.28 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1443 | 1480 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.684 |
| queue: job wait, submitted to its first pod running, mean (s) | 133.8 | 183.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 612 | 738.4 |
| queue: job turnaround, submitted to done, mean (s) | 811.9 | 877.1 |
| queue: jobs unfinished at the window's end | 9.9 | 12.2 |
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
| worker nodes in service, mean | 6 | 5.973 | −0.4% | −0.0876 to +0.0339 | no |
| node-hours | 2.516 | 2.508 | −0.3% | −0.0343 to +0.0179 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | −0.2% | −1.8006 to +0.8902 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.1 | −0.5% | −3.2552 to +0.6615 | no |
| response time (ms), mean | 124.6 | 106 | −14.9% | −22.4566 to −14.6830 | yes: GAIN |
| response time (ms), 95th percentile | 219.3 | 233.3 | +6.4% | +1.2315 to +26.8545 | yes: LOSS |
| response time (ms), 99th percentile | 324.7 | 356 | +9.6% | +13.7336 to +48.7764 | yes: LOSS |
| time over the response line (% of samples) | 0.2152 | 0.2709 | +25.9% | −0.0658 to +0.1773 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.1 | +100.100 (native is 0) | +84.2788 to +115.9212 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1111 | 1220 | +9.8% | +56.2298 to +162.6002 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06005 | 0.0582 | −3.1% | −0.0043 to +0.0006 | no |
| CPU used (cores), mean | 1.441 | 1.391 | −3.5% | −0.1035 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0 | 0.06945 | +0.069 (native is 0) | +0.0613 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.441 | 1.46 | +1.3% | −0.0313 to +0.0693 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.6 | 464.6 | +2.9% | −4.0800 to +29.9782 | no |
| HPA replicas, mean | 1.984 | 2.107 | +6.2% | −0.1257 to +0.3702 | no |
| pods started | 0.2 | 0.6 | +200.0% | −0.3689 to +1.1689 | no |
| pod start wait, total (s) | 0.6 | 1.5 | +150.0% | −1.3227 to +3.1227 | no |
| pod start wait, mean (s) | 0.6 | 0.7 | +16.7% | −1.0410 to +1.2410 | no |
| host CPU busy, the real machine under kind (%) | 44.84 | 46.28 | +3.2% | +0.3072 to +2.5712 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1443 | 1480 | +2.5% | −13.1197 to +86.3197 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.684 | −21.9% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 133.8 | 183.7 | +37.3% | +5.2005 to +94.6828 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 612 | 738.4 | +20.7% | −20.8785 to +273.6785 | no |
| queue: job turnaround, submitted to done, mean (s) | 811.9 | 877.1 | +8.0% | +0.5968 to +129.8449 | yes: LOSS |
| queue: jobs unfinished at the window's end | 9.9 | 12.2 | +23.2% | −0.5222 to +5.1222 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*