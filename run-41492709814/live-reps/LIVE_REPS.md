# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.97 |
| node-hours | 4.159 | 4.157 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.6 | 442.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 164.1 | 88.6 |
| response time (ms), 95th percentile | 328.5 | 117.8 |
| response time (ms), 99th percentile | 608.3 | 322.5 |
| time over the response line (% of samples) | 3.377 | 2.102 |
| failed requests (%) | 1.598 | 1.497 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2667 |
| utilisation (used / allocatable) | 0.04887 | 0.04813 |
| CPU used (cores), mean | 1.167 | 1.149 |
| Omni's own CPU (cores), mean | 0 | 0.03742 |
| CPU used with Omni's own (cores), mean | 1.167 | 1.187 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 579.3 | 583.2 |
| HPA replicas, mean | 8.366 | 8.89 |
| pods started | 8.1 | 10.9 |
| pod start wait, total (s) | 13.4 | 17.4 |
| pod start wait, mean (s) | 1.657 | 1.585 |
| host CPU busy, the real machine under kind (%) | 35.43 | 36.17 |
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
| worker nodes in service, mean | 5.969 | 5.97 | +0.0% | −0.0007 to +0.0030 | no |
| node-hours | 4.159 | 4.157 | −0.0% | −0.0108 to +0.0071 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.5 | −0.2% | −1.5858 to +0.1284 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.6 | 442.9 | −0.2% | −1.5527 to +0.2161 | no |
| response time (ms), mean | 164.1 | 88.6 | −46.0% | −98.8616 to −52.1691 | yes: GAIN |
| response time (ms), 95th percentile | 328.5 | 117.8 | −64.1% | −245.6450 to −175.8260 | yes: GAIN |
| response time (ms), 99th percentile | 608.3 | 322.5 | −47.0% | −418.0410 to −153.5456 | yes: GAIN |
| time over the response line (% of samples) | 3.377 | 2.102 | −37.8% | −1.9384 to −0.6123 | yes: GAIN |
| failed requests (%) | 1.598 | 1.497 | −6.3% | −0.2001 to −0.0011 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 7.1 | −25.3% | −3.7572 to −1.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.1 | +62.100 (native is 0) | +54.0604 to +70.1396 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2667 | +25.0% | −0.3156 to +0.4223 | no |
| utilisation (used / allocatable) | 0.04887 | 0.04813 | −1.5% | −0.0015 to +0.0001 | no |
| CPU used (cores), mean | 1.167 | 1.149 | −1.5% | −0.0368 to +0.0016 | no |
| Omni's own CPU (cores), mean | 0 | 0.03742 | +0.037 (native is 0) | +0.0319 to +0.0430 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.167 | 1.187 | +1.7% | +0.0040 to +0.0356 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 579.3 | 583.2 | +0.7% | −6.7254 to +14.4928 | no |
| HPA replicas, mean | 8.366 | 8.89 | +6.3% | −0.1151 to +1.1624 | no |
| pods started | 8.1 | 10.9 | +34.6% | +2.2358 to +3.3642 | yes: power given |
| pod start wait, total (s) | 13.4 | 17.4 | +29.9% | +1.0219 to +6.9781 | yes: LOSS |
| pod start wait, mean (s) | 1.657 | 1.585 | −4.4% | −0.3210 to +0.1762 | no |
| host CPU busy, the real machine under kind (%) | 35.43 | 36.17 | +2.1% | +0.3504 to +1.1259 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 75 | 4.1 |  |
| machine down | omni | 50 | 1.7 | -24 s (-32%) |
| spike | native | 256 | 67.6 |  |
| spike | omni | 244 | 65.6 | -12 s (-5%) |
| runaway pod started | native | 8 | 0.3 |  |
| runaway pod started | omni | 2 | 0.0 | -6 s (-75%) |
| probe blind | native | 71 | 1.3 |  |
| probe blind | omni | 48 | 0.0 | -23 s (-33%) |
| metrics down | native | 3 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-45%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*