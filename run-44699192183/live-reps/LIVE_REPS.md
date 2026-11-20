# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.968 |
| node-hours | 4.161 | 4.158 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.6 | 442.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 159.7 | 91.04 |
| response time (ms), 95th percentile | 320.5 | 115.6 |
| response time (ms), 99th percentile | 592.6 | 225.1 |
| time over the response line (% of samples) | 3.062 | 1.914 |
| failed requests (%) | 1.484 | 1.445 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.4983 |
| utilisation (used / allocatable) | 0.04828 | 0.04766 |
| CPU used (cores), mean | 1.153 | 1.138 |
| Omni's own CPU (cores), mean | 0 | 0.03844 |
| CPU used with Omni's own (cores), mean | 1.153 | 1.176 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 572.7 | 580.8 |
| HPA replicas, mean | 8.422 | 8.979 |
| pods started | 8.2 | 11.7 |
| pod start wait, total (s) | 13.6 | 19.7 |
| pod start wait, mean (s) | 1.654 | 1.683 |
| host CPU busy, the real machine under kind (%) | 35.35 | 36.19 |
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
| worker nodes in service, mean | 5.969 | 5.968 | −0.0% | −0.0048 to +0.0023 | no |
| node-hours | 4.161 | 4.158 | −0.1% | −0.0115 to +0.0047 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.5 | −0.2% | −1.6462 to +0.2646 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.6 | 442.9 | −0.2% | −1.7155 to +0.2005 | no |
| response time (ms), mean | 159.7 | 91.04 | −43.0% | −88.9169 to −48.4328 | yes: GAIN |
| response time (ms), 95th percentile | 320.5 | 115.6 | −63.9% | −243.0309 to −166.7531 | yes: GAIN |
| response time (ms), 99th percentile | 592.6 | 225.1 | −62.0% | −452.7946 to −282.1606 | yes: GAIN |
| time over the response line (% of samples) | 3.062 | 1.914 | −37.5% | −1.7610 to −0.5360 | yes: GAIN |
| failed requests (%) | 1.484 | 1.445 | −2.6% | −0.1422 to +0.0653 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 7.1 | −14.5% | −2.4064 to +0.0064 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.5 | +64.500 (native is 0) | +57.5138 to +71.4862 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.4983 | +367.2% | −0.0293 to +0.8126 | no |
| utilisation (used / allocatable) | 0.04828 | 0.04766 | −1.3% | −0.0010 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.153 | 1.138 | −1.3% | −0.0251 to −0.0053 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03844 | +0.038 (native is 0) | +0.0330 to +0.0439 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.153 | 1.176 | +2.0% | +0.0124 to +0.0340 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 572.7 | 580.8 | +1.4% | +1.9470 to +14.1172 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.422 | 8.979 | +6.6% | −0.0139 to +1.1290 | no |
| pods started | 8.2 | 11.7 | +42.7% | +2.0595 to +4.9405 | yes: power given |
| pod start wait, total (s) | 13.6 | 19.7 | +44.9% | +2.0333 to +10.1667 | yes: LOSS |
| pod start wait, mean (s) | 1.654 | 1.683 | +1.7% | −0.1979 to +0.2551 | no |
| host CPU busy, the real machine under kind (%) | 35.35 | 36.19 | +2.4% | +0.5174 to +1.1638 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 56 | 3.4 |  |
| machine down | omni | 42 | 1.3 | -14 s (-25%) |
| spike | native | 262 | 61.6 |  |
| spike | omni | 255 | 59.5 | -7 s (-3%) |
| runaway pod started | native | 3 | 0.2 |  |
| runaway pod started | omni | 3 | 0.0 | +0 s (+1%) |
| probe blind | native | 73 | 0.9 |  |
| probe blind | omni | 60 | 0.0 | -13 s (-18%) |
| metrics down | native | 5 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | -4 s (-71%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*