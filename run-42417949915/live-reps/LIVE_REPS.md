# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.913 |
| node-hours | 1.489 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 165.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.5 | 163.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 222 | 110.1 |
| response time (ms), 95th percentile | 374.8 | 142.2 |
| response time (ms), 99th percentile | 1418 | 539 |
| time over the response line (% of samples) | 7.348 | 5.784 |
| failed requests (%) | 4.817 | 4.78 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.975 | 0.41 |
| utilisation (used / allocatable) | 0.07025 | 0.06949 |
| CPU used (cores), mean | 1.663 | 1.644 |
| Omni's own CPU (cores), mean | 0 | 0.04326 |
| CPU used with Omni's own (cores), mean | 1.663 | 1.687 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 399.7 | 402.9 |
| HPA replicas, mean | 8.605 | 11.16 |
| pods started | 5.3 | 9.3 |
| pod start wait, total (s) | 9 | 17.3 |
| pod start wait, mean (s) | 1.667 | 1.868 |
| host CPU busy, the real machine under kind (%) | 47.62 | 48.7 |
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
| worker nodes in service, mean | 5.916 | 5.913 | −0.1% | −0.0085 to +0.0023 | no |
| node-hours | 1.489 | 1.493 | +0.3% | +0.0010 to +0.0076 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 165.5 | +0.3% | −0.0583 to +0.9113 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.5 | 163.8 | +0.2% | −0.1360 to +0.8597 | no |
| response time (ms), mean | 222 | 110.1 | −50.4% | −164.2670 to −59.6643 | yes: GAIN |
| response time (ms), 95th percentile | 374.8 | 142.2 | −62.1% | −286.8519 to −178.2781 | yes: GAIN |
| response time (ms), 99th percentile | 1418 | 539 | −62.0% | −1553.4032 to −205.3104 | yes: GAIN |
| time over the response line (% of samples) | 7.348 | 5.784 | −21.3% | −2.2783 to −0.8500 | yes: GAIN |
| failed requests (%) | 4.817 | 4.78 | −0.8% | −0.6716 to +0.5987 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 5.8 | −13.4% | −1.7564 to −0.0436 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.8 | +44.800 (native is 0) | +39.6001 to +49.9999 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.975 | 0.41 | −57.9% | −1.1226 to −0.0074 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.07025 | 0.06949 | −1.1% | −0.0018 to +0.0002 | no |
| CPU used (cores), mean | 1.663 | 1.644 | −1.1% | −0.0431 to +0.0052 | no |
| Omni's own CPU (cores), mean | 0 | 0.04326 | +0.043 (native is 0) | +0.0380 to +0.0485 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.663 | 1.687 | +1.5% | +0.0005 to +0.0481 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 399.7 | 402.9 | +0.8% | −2.9235 to +9.3194 | no |
| HPA replicas, mean | 8.605 | 11.16 | +29.7% | +1.4419 to +3.6705 | yes: power given |
| pods started | 5.3 | 9.3 | +75.5% | +3.2460 to +4.7540 | yes: power given |
| pod start wait, total (s) | 9 | 17.3 | +92.2% | +5.1539 to +11.4461 | yes: LOSS |
| pod start wait, mean (s) | 1.667 | 1.868 | +12.0% | −0.1281 to +0.5292 | no |
| host CPU busy, the real machine under kind (%) | 47.62 | 48.7 | +2.3% | +0.4978 to +1.6652 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 56 | 13.9 |  |
| machine down | omni | 44 | 10.0 | -12 s (-21%) |
| spike | native | 251 | 56.3 |  |
| spike | omni | 248 | 52.9 | -2 s (-1%) |
| runaway pod started | native | 114 | 9.5 |  |
| runaway pod started | omni | 85 | 8.1 | -30 s (-26%) |
| probe blind | native | 68 | 0.4 |  |
| probe blind | omni | 60 | 0.0 | -8 s (-12%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*