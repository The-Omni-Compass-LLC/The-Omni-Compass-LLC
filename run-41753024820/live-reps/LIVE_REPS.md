# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.919 | 5.914 |
| node-hours | 1.492 | 1.496 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 165.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 163.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 201 | 133.7 |
| response time (ms), 95th percentile | 422.4 | 248.8 |
| response time (ms), 99th percentile | 983.4 | 854.7 |
| time over the response line (% of samples) | 8.004 | 6.259 |
| failed requests (%) | 4.532 | 4.143 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 70 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9467 | 0.915 |
| utilisation (used / allocatable) | 0.06846 | 0.067 |
| CPU used (cores), mean | 1.621 | 1.585 |
| Omni's own CPU (cores), mean | 0 | 0.04418 |
| CPU used with Omni's own (cores), mean | 1.621 | 1.629 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422 | 423.3 |
| HPA replicas, mean | 8.358 | 10.94 |
| pods started | 5.7 | 11.6 |
| pod start wait, total (s) | 16.2 | 32.4 |
| pod start wait, mean (s) | 2.995 | 2.911 |
| host CPU busy, the real machine under kind (%) | 46.81 | 47.22 |
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
| worker nodes in service, mean | 5.919 | 5.914 | −0.1% | −0.0109 to +0.0014 | no |
| node-hours | 1.492 | 1.496 | +0.3% | +0.0013 to +0.0075 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 165.2 | +0.2% | −0.1843 to +0.7777 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 163.6 | +0.1% | −0.2450 to +0.6468 | no |
| response time (ms), mean | 201 | 133.7 | −33.5% | −122.6995 to −11.9118 | yes: GAIN |
| response time (ms), 95th percentile | 422.4 | 248.8 | −41.1% | −276.4201 to −70.6889 | yes: GAIN |
| response time (ms), 99th percentile | 983.4 | 854.7 | −13.1% | −479.0558 to +221.7292 | no |
| time over the response line (% of samples) | 8.004 | 6.259 | −21.8% | −2.9476 to −0.5426 | yes: GAIN |
| failed requests (%) | 4.532 | 4.143 | −8.6% | −0.8749 to +0.0971 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.6 | −12.5% | −1.6793 to +0.0793 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 | +50.900 (native is 0) | +45.7149 to +56.0851 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9467 | 0.915 | −3.3% | −0.8120 to +0.7487 | no |
| utilisation (used / allocatable) | 0.06846 | 0.067 | −2.1% | −0.0038 to +0.0008 | no |
| CPU used (cores), mean | 1.621 | 1.585 | −2.2% | −0.0898 to +0.0182 | no |
| Omni's own CPU (cores), mean | 0 | 0.04418 | +0.044 (native is 0) | +0.0373 to +0.0511 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.621 | 1.629 | +0.5% | −0.0401 to +0.0569 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422 | 423.3 | +0.3% | −14.8327 to +17.4743 | no |
| HPA replicas, mean | 8.358 | 10.94 | +30.9% | +1.6698 to +3.4998 | yes: power given |
| pods started | 5.7 | 11.6 | +103.5% | +3.7554 to +8.0446 | yes: power given |
| pod start wait, total (s) | 16.2 | 32.4 | +100.0% | −10.3678 to +42.7678 | no |
| pod start wait, mean (s) | 2.995 | 2.911 | −2.8% | −3.9499 to +3.7828 | no |
| host CPU busy, the real machine under kind (%) | 46.81 | 47.22 | +0.9% | −0.3759 to +1.2062 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 65 | 14.6 |  |
| machine down | omni | 37 | 10.2 | -28 s (-44%) |
| spike | native | 248 | 69.5 |  |
| spike | omni | 246 | 61.1 | -2 s (-1%) |
| runaway pod started | native | 113 | 11.5 |  |
| runaway pod started | omni | 88 | 7.9 | -24 s (-22%) |
| probe blind | native | 56 | 0.5 |  |
| probe blind | omni | 60 | 0.1 | +4 s (+7%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*