# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.918 |
| node-hours | 1.489 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.7 | 164.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.1 | 163 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 180.8 | 116.1 |
| response time (ms), 95th percentile | 346.1 | 139.8 |
| response time (ms), 99th percentile | 1008 | 499.4 |
| time over the response line (% of samples) | 6.77 | 5.423 |
| failed requests (%) | 4.396 | 4.424 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 5.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3617 | 0.61 |
| utilisation (used / allocatable) | 0.06825 | 0.0671 |
| CPU used (cores), mean | 1.614 | 1.588 |
| Omni's own CPU (cores), mean | 0 | 0.04074 |
| CPU used with Omni's own (cores), mean | 1.614 | 1.629 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.4 | 418.9 |
| HPA replicas, mean | 8.532 | 10.74 |
| pods started | 5.5 | 9.1 |
| pod start wait, total (s) | 8.6 | 16.3 |
| pod start wait, mean (s) | 1.53 | 1.797 |
| host CPU busy, the real machine under kind (%) | 46.04 | 47.08 |
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
| worker nodes in service, mean | 5.913 | 5.918 | +0.1% | −0.0003 to +0.0109 | no |
| node-hours | 1.489 | 1.49 | +0.1% | −0.0048 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.7 | 164.6 | −0.1% | −0.8556 to +0.5258 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.1 | 163 | −0.0% | −0.7159 to +0.5861 | no |
| response time (ms), mean | 180.8 | 116.1 | −35.8% | −97.3388 to −32.0546 | yes: GAIN |
| response time (ms), 95th percentile | 346.1 | 139.8 | −59.6% | −236.8700 to −175.9000 | yes: GAIN |
| response time (ms), 99th percentile | 1008 | 499.4 | −50.5% | −722.4232 to −295.5090 | yes: GAIN |
| time over the response line (% of samples) | 6.77 | 5.423 | −19.9% | −2.1671 to −0.5274 | yes: GAIN |
| failed requests (%) | 4.396 | 4.424 | +0.7% | −0.5087 to +0.5659 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 5.5 | −11.3% | −1.5953 to +0.1953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.6 | +40.600 (native is 0) | +35.3306 to +45.8694 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3617 | 0.61 | +68.7% | −0.1673 to +0.6640 | no |
| utilisation (used / allocatable) | 0.06825 | 0.0671 | −1.7% | −0.0026 to +0.0003 | no |
| CPU used (cores), mean | 1.614 | 1.588 | −1.6% | −0.0604 to +0.0089 | no |
| Omni's own CPU (cores), mean | 0 | 0.04074 | +0.041 (native is 0) | +0.0350 to +0.0465 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.614 | 1.629 | +0.9% | −0.0179 to +0.0478 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.4 | 418.9 | +1.3% | −1.6831 to +12.5742 | no |
| HPA replicas, mean | 8.532 | 10.74 | +25.9% | +1.1987 to +3.2188 | yes: power given |
| pods started | 5.5 | 9.1 | +65.5% | +2.1225 to +5.0775 | yes: power given |
| pod start wait, total (s) | 8.6 | 16.3 | +89.5% | +2.9188 to +12.4812 | yes: LOSS |
| pod start wait, mean (s) | 1.53 | 1.797 | +17.5% | −0.2253 to +0.7595 | no |
| host CPU busy, the real machine under kind (%) | 46.04 | 47.08 | +2.3% | +0.4345 to +1.6409 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 74 | 12.4 |  |
| machine down | omni | 50 | 9.9 | -24 s (-32%) |
| spike | native | 244 | 49.6 |  |
| spike | omni | 226 | 47.2 | -18 s (-8%) |
| runaway pod started | native | 82 | 8.3 |  |
| runaway pod started | omni | 82 | 6.7 | +0 s (+0%) |
| probe blind | native | 56 | 0.3 |  |
| probe blind | omni | 54 | 0.1 | -2 s (-3%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*