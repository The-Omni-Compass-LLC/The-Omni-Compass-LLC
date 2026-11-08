# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.915 |
| node-hours | 1.491 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 164.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.3 | 162.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 183.1 | 114.5 |
| response time (ms), 95th percentile | 391.4 | 179.5 |
| response time (ms), 99th percentile | 1073 | 744.4 |
| time over the response line (% of samples) | 7.333 | 5.462 |
| failed requests (%) | 4.362 | 3.905 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 70 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.87 | 0.5917 |
| utilisation (used / allocatable) | 0.06838 | 0.06731 |
| CPU used (cores), mean | 1.618 | 1.592 |
| Omni's own CPU (cores), mean | 0 | 0.04317 |
| CPU used with Omni's own (cores), mean | 1.618 | 1.636 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.6 | 419.5 |
| HPA replicas, mean | 8.542 | 11.12 |
| pods started | 5.4 | 10.5 |
| pod start wait, total (s) | 17.5 | 29.2 |
| pod start wait, mean (s) | 2.87 | 2.735 |
| host CPU busy, the real machine under kind (%) | 46.57 | 47.81 |
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
| worker nodes in service, mean | 5.915 | 5.915 | +0.0% | −0.0055 to +0.0056 | no |
| node-hours | 1.491 | 1.489 | −0.1% | −0.0101 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 164.5 | −0.2% | −1.5677 to +0.8629 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.3 | 162.9 | −0.2% | −1.5498 to +0.8491 | no |
| response time (ms), mean | 183.1 | 114.5 | −37.5% | −82.1762 to −55.1788 | yes: GAIN |
| response time (ms), 95th percentile | 391.4 | 179.5 | −54.1% | −243.0555 to −180.6365 | yes: GAIN |
| response time (ms), 99th percentile | 1073 | 744.4 | −30.6% | −664.3575 to +7.5333 | no |
| time over the response line (% of samples) | 7.333 | 5.462 | −25.5% | −2.6703 to −1.0715 | yes: GAIN |
| failed requests (%) | 4.362 | 3.905 | −10.5% | −0.9776 to +0.0622 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.3 | −13.1% | −1.4573 to −0.1427 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.7 | +46.700 (native is 0) | +41.0269 to +52.3731 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.87 | 0.5917 | −32.0% | −0.9263 to +0.3696 | no |
| utilisation (used / allocatable) | 0.06838 | 0.06731 | −1.6% | −0.0028 to +0.0006 | no |
| CPU used (cores), mean | 1.618 | 1.592 | −1.6% | −0.0649 to +0.0143 | no |
| Omni's own CPU (cores), mean | 0 | 0.04317 | +0.043 (native is 0) | +0.0369 to +0.0495 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.618 | 1.636 | +1.1% | −0.0195 to +0.0553 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.6 | 419.5 | +0.9% | −5.8767 to +13.5999 | no |
| HPA replicas, mean | 8.542 | 11.12 | +30.2% | +1.3711 to +3.7812 | yes: power given |
| pods started | 5.4 | 10.5 | +94.4% | +4.3128 to +5.8872 | yes: power given |
| pod start wait, total (s) | 17.5 | 29.2 | +66.9% | −17.1715 to +40.5715 | no |
| pod start wait, mean (s) | 2.87 | 2.735 | −4.7% | −3.5412 to +3.2693 | no |
| host CPU busy, the real machine under kind (%) | 46.57 | 47.81 | +2.7% | +0.5037 to +1.9908 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 52 | 14.3 |  |
| machine down | omni | 31 | 8.5 | -21 s (-40%) |
| spike | native | 241 | 56.0 |  |
| spike | omni | 240 | 53.5 | -1 s (-0%) |
| runaway pod started | native | 83 | 8.8 |  |
| runaway pod started | omni | 80 | 8.0 | -3 s (-4%) |
| probe blind | native | 60 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | -0 s (-0%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*