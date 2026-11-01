# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.969 |
| node-hours | 4.162 | 4.158 |
| energy, parked workers still on at idle power (Wh, declared model) | 446.9 | 445.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.2 | 444.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 165.8 | 91.46 |
| response time (ms), 95th percentile | 328.5 | 120.8 |
| response time (ms), 99th percentile | 618.1 | 208.1 |
| time over the response line (% of samples) | 3.257 | 1.932 |
| failed requests (%) | 1.761 | 1.573 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4317 | 0.27 |
| utilisation (used / allocatable) | 0.0509 | 0.04972 |
| CPU used (cores), mean | 1.215 | 1.187 |
| Omni's own CPU (cores), mean | 0 | 0.00889 |
| CPU used with Omni's own (cores), mean | 1.215 | 1.196 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 546.9 | 560.4 |
| HPA replicas, mean | 8.604 | 8.832 |
| pods started | 8.3 | 9.1 |
| pod start wait, total (s) | 11.9 | 15.8 |
| pod start wait, mean (s) | 1.428 | 1.702 |
| host CPU busy, the real machine under kind (%) | 36.83 | 36.17 |
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
| worker nodes in service, mean | 5.969 | 5.969 | +0.0% | −0.0036 to +0.0037 | no |
| node-hours | 4.162 | 4.158 | −0.1% | −0.0122 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 446.9 | 445.7 | −0.3% | −2.1883 to −0.1326 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.2 | 444.1 | −0.3% | −2.1467 to −0.1660 | yes: GAIN |
| response time (ms), mean | 165.8 | 91.46 | −44.8% | −93.9458 to −54.7392 | yes: GAIN |
| response time (ms), 95th percentile | 328.5 | 120.8 | −63.2% | −242.7335 to −172.5605 | yes: GAIN |
| response time (ms), 99th percentile | 618.1 | 208.1 | −66.3% | −554.7132 to −265.2650 | yes: GAIN |
| time over the response line (% of samples) | 3.257 | 1.932 | −40.7% | −1.7238 to −0.9267 | yes: GAIN |
| failed requests (%) | 1.761 | 1.573 | −10.7% | −0.3026 to −0.0729 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 7.1 | −27.6% | −3.9181 to −1.4819 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 | +47.100 (native is 0) | +39.6020 to +54.5980 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4317 | 0.27 | −37.5% | −0.4835 to +0.1602 | no |
| utilisation (used / allocatable) | 0.0509 | 0.04972 | −2.3% | −0.0017 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.215 | 1.187 | −2.3% | −0.0399 to −0.0168 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00889 | +0.009 (native is 0) | +0.0077 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.215 | 1.196 | −1.6% | −0.0310 to −0.0079 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 546.9 | 560.4 | +2.5% | +6.3312 to +20.6355 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.604 | 8.832 | +2.7% | −0.4368 to +0.8933 | no |
| pods started | 8.3 | 9.1 | +9.6% | −0.5821 to +2.1821 | no |
| pod start wait, total (s) | 11.9 | 15.8 | +32.8% | −0.6045 to +8.4045 | no |
| pod start wait, mean (s) | 1.428 | 1.702 | +19.2% | −0.0510 to +0.5982 | no |
| host CPU busy, the real machine under kind (%) | 36.83 | 36.17 | −1.8% | −0.8956 to −0.4093 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 65 | 3.5 |  |
| machine down | omni | 36 | 0.9 | -29 s (-44%) |
| spike | native | 268 | 70.5 |  |
| spike | omni | 252 | 69.6 | -17 s (-6%) |
| runaway pod started | native | 4 | 0.3 |  |
| runaway pod started | omni | 2 | 0.0 | -2 s (-45%) |
| probe blind | native | 64 | 0.8 |  |
| probe blind | omni | 60 | 0.0 | -4 s (-6%) |
| metrics down | native | 3 | 0.1 |  |
| metrics down | omni | 1 | 0.0 | -2 s (-70%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*