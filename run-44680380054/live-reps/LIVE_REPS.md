# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.916 |
| node-hours | 1.488 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 163.2 | 163.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.6 | 161.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 166.8 | 106 |
| response time (ms), 95th percentile | 344.2 | 165.2 |
| response time (ms), 99th percentile | 930.4 | 626.4 |
| time over the response line (% of samples) | 5.632 | 3.928 |
| failed requests (%) | 3.172 | 2.88 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 4.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4133 | 0.4317 |
| utilisation (used / allocatable) | 0.06132 | 0.06026 |
| CPU used (cores), mean | 1.45 | 1.426 |
| Omni's own CPU (cores), mean | 0 | 0.03694 |
| CPU used with Omni's own (cores), mean | 1.45 | 1.463 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 466.9 |
| HPA replicas, mean | 8.228 | 9.521 |
| pods started | 5.9 | 9.6 |
| pod start wait, total (s) | 8.8 | 15.8 |
| pod start wait, mean (s) | 1.473 | 1.61 |
| host CPU busy, the real machine under kind (%) | 41.83 | 42.59 |
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
| worker nodes in service, mean | 5.914 | 5.916 | +0.0% | −0.0020 to +0.0055 | no |
| node-hours | 1.488 | 1.49 | +0.1% | −0.0041 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 163.2 | 163.1 | −0.1% | −0.9352 to +0.7431 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.6 | 161.5 | −0.0% | −0.8446 to +0.7150 | no |
| response time (ms), mean | 166.8 | 106 | −36.5% | −81.8824 to −39.7528 | yes: GAIN |
| response time (ms), 95th percentile | 344.2 | 165.2 | −52.0% | −227.7177 to −130.2753 | yes: GAIN |
| response time (ms), 99th percentile | 930.4 | 626.4 | −32.7% | −752.8002 to +144.6520 | no |
| time over the response line (% of samples) | 5.632 | 3.928 | −30.3% | −2.4720 to −0.9371 | yes: GAIN |
| failed requests (%) | 3.172 | 2.88 | −9.2% | −0.6039 to +0.0205 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 4.3 | −17.3% | −1.5263 to −0.2737 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.7 | +39.700 (native is 0) | +33.7625 to +45.6375 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4133 | 0.4317 | +4.4% | −0.3809 to +0.4176 | no |
| utilisation (used / allocatable) | 0.06132 | 0.06026 | −1.7% | −0.0025 to +0.0003 | no |
| CPU used (cores), mean | 1.45 | 1.426 | −1.7% | −0.0579 to +0.0083 | no |
| Omni's own CPU (cores), mean | 0 | 0.03694 | +0.037 (native is 0) | +0.0305 to +0.0434 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.463 | +0.8% | −0.0224 to +0.0467 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 466.9 | +1.9% | −5.4360 to +22.9832 | no |
| HPA replicas, mean | 8.228 | 9.521 | +15.7% | +0.7783 to +1.8064 | yes: power given |
| pods started | 5.9 | 9.6 | +62.7% | +2.2283 to +5.1717 | yes: power given |
| pod start wait, total (s) | 8.8 | 15.8 | +79.5% | +1.5733 to +12.4267 | yes: LOSS |
| pod start wait, mean (s) | 1.473 | 1.61 | +9.3% | −0.3769 to +0.6497 | no |
| host CPU busy, the real machine under kind (%) | 41.83 | 42.59 | +1.8% | +0.0688 to +1.4684 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 49 | 12.4 |  |
| machine down | omni | 27 | 7.6 | -23 s (-46%) |
| spike | native | 209 | 32.9 |  |
| spike | omni | 193 | 30.3 | -16 s (-8%) |
| runaway pod started | native | 45 | 3.9 |  |
| runaway pod started | omni | 45 | 3.7 | +0 s (+1%) |
| probe blind | native | 48 | 0.0 |  |
| probe blind | omni | 60 | 0.1 | +12 s (+25%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*