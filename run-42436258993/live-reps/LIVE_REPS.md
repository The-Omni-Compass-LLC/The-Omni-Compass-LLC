# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.972 |
| node-hours | 4.159 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 446.1 | 445.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.5 | 443.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 162.5 | 93.49 |
| response time (ms), 95th percentile | 320 | 114.9 |
| response time (ms), 99th percentile | 525.2 | 178.7 |
| time over the response line (% of samples) | 2.939 | 1.914 |
| failed requests (%) | 1.674 | 1.604 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 81.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1567 | 0.2967 |
| utilisation (used / allocatable) | 0.04988 | 0.0488 |
| CPU used (cores), mean | 1.191 | 1.166 |
| Omni's own CPU (cores), mean | 0 | 0.03766 |
| CPU used with Omni's own (cores), mean | 1.191 | 1.203 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 545.3 | 555.6 |
| HPA replicas, mean | 8.604 | 9.507 |
| pods started | 8.8 | 12.3 |
| pod start wait, total (s) | 13.4 | 20 |
| pod start wait, mean (s) | 1.538 | 1.641 |
| host CPU busy, the real machine under kind (%) | 35.98 | 36.64 |
| host cores (the real machine under kind) | 4 | 4 |
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
| worker nodes in service, mean | 5.969 | 5.972 | +0.1% | −0.0008 to +0.0068 | no |
| node-hours | 4.159 | 4.159 | −0.0% | −0.0100 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 446.1 | 445.1 | −0.2% | −1.8374 to −0.1187 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.5 | 443.6 | −0.2% | −1.8135 to +0.1739 | no |
| response time (ms), mean | 162.5 | 93.49 | −42.5% | −84.7937 to −53.2029 | yes: GAIN |
| response time (ms), 95th percentile | 320 | 114.9 | −64.1% | −233.4214 to −176.8246 | yes: GAIN |
| response time (ms), 99th percentile | 525.2 | 178.7 | −66.0% | −405.0469 to −288.0337 | yes: GAIN |
| time over the response line (% of samples) | 2.939 | 1.914 | −34.9% | −1.5674 to −0.4831 | yes: GAIN |
| failed requests (%) | 1.674 | 1.604 | −4.2% | −0.2042 to +0.0644 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 7.4 | −16.9% | −2.4079 to −0.5921 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.7 | +67.700 (native is 0) | +60.5307 to +74.8693 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1567 | 0.2967 | +89.4% | −0.1356 to +0.4156 | no |
| utilisation (used / allocatable) | 0.04988 | 0.0488 | −2.2% | −0.0015 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.191 | 1.166 | −2.1% | −0.0360 to −0.0143 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03766 | +0.038 (native is 0) | +0.0336 to +0.0418 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.191 | 1.203 | +1.1% | +0.0033 to +0.0217 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 545.3 | 555.6 | +1.9% | +6.0459 to +14.5972 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.604 | 9.507 | +10.5% | +0.1146 to +1.6915 | yes: power given |
| pods started | 8.8 | 12.3 | +39.8% | +2.0995 to +4.9005 | yes: power given |
| pod start wait, total (s) | 13.4 | 20 | +49.3% | +3.0925 to +10.1075 | yes: LOSS |
| pod start wait, mean (s) | 1.538 | 1.641 | +6.7% | −0.2020 to +0.4072 | no |
| host CPU busy, the real machine under kind (%) | 35.98 | 36.64 | +1.8% | +0.4188 to +0.9086 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 67 | 3.8 |  |
| machine down | omni | 49 | 1.7 | -18 s (-27%) |
| spike | native | 264 | 62.8 |  |
| spike | omni | 263 | 59.8 | -1 s (-1%) |
| runaway pod started | native | 6 | 0.4 |  |
| runaway pod started | omni | 3 | 0.0 | -3 s (-49%) |
| probe blind | native | 62 | 0.9 |  |
| probe blind | omni | 60 | 0.1 | -2 s (-3%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+23%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*