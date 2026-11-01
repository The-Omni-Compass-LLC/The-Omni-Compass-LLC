# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.913 |
| node-hours | 1.492 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.7 | 165.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.1 | 163.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 216.9 | 118.4 |
| response time (ms), 95th percentile | 387.7 | 175.7 |
| response time (ms), 99th percentile | 1098 | 873.3 |
| time over the response line (% of samples) | 7.813 | 5.676 |
| failed requests (%) | 4.904 | 4.299 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 5.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8917 | 0.6383 |
| utilisation (used / allocatable) | 0.07142 | 0.06925 |
| CPU used (cores), mean | 1.69 | 1.638 |
| Omni's own CPU (cores), mean | 0 | 0.01166 |
| CPU used with Omni's own (cores), mean | 1.69 | 1.65 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 398.3 | 405.3 |
| HPA replicas, mean | 8.641 | 10.85 |
| pods started | 5.1 | 6.7 |
| pod start wait, total (s) | 22.6 | 12.5 |
| pod start wait, mean (s) | 4.208 | 1.809 |
| host CPU busy, the real machine under kind (%) | 48.63 | 47.73 |
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
| worker nodes in service, mean | 5.916 | 5.913 | −0.1% | −0.0084 to +0.0020 | no |
| node-hours | 1.492 | 1.493 | +0.1% | −0.0024 to +0.0048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.7 | 165.4 | −0.2% | −1.0165 to +0.4638 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.1 | 163.7 | −0.2% | −1.0540 to +0.3763 | no |
| response time (ms), mean | 216.9 | 118.4 | −45.4% | −142.2253 to −54.8996 | yes: GAIN |
| response time (ms), 95th percentile | 387.7 | 175.7 | −54.7% | −276.5148 to −147.5472 | yes: GAIN |
| response time (ms), 99th percentile | 1098 | 873.3 | −20.5% | −934.1591 to +483.9861 | no |
| time over the response line (% of samples) | 7.813 | 5.676 | −27.4% | −3.4119 to −0.8628 | yes: GAIN |
| failed requests (%) | 4.904 | 4.299 | −12.3% | −1.2179 to +0.0072 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 5.7 | −12.3% | −1.9583 to +0.3583 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.100 (native is 0) | +26.6477 to +37.5523 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8917 | 0.6383 | −28.4% | −0.6650 to +0.1584 | no |
| utilisation (used / allocatable) | 0.07142 | 0.06925 | −3.0% | −0.0045 to +0.0001 | no |
| CPU used (cores), mean | 1.69 | 1.638 | −3.1% | −0.1062 to +0.0020 | no |
| Omni's own CPU (cores), mean | 0 | 0.01166 | +0.012 (native is 0) | +0.0101 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.69 | 1.65 | −2.4% | −0.0938 to +0.0129 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 398.3 | 405.3 | +1.8% | −4.4260 to +18.4872 | no |
| HPA replicas, mean | 8.641 | 10.85 | +25.6% | +1.2108 to +3.2126 | yes: power given |
| pods started | 5.1 | 6.7 | +31.4% | +0.3749 to +2.8251 | yes: power given |
| pod start wait, total (s) | 22.6 | 12.5 | −44.7% | −29.3866 to +9.1866 | no |
| pod start wait, mean (s) | 4.208 | 1.809 | −57.0% | −5.9719 to +1.1738 | no |
| host CPU busy, the real machine under kind (%) | 48.63 | 47.73 | −1.9% | −2.0781 to +0.2751 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 58 | 13.7 |  |
| machine down | omni | 46 | 10.0 | -12 s (-21%) |
| spike | native | 261 | 64.7 |  |
| spike | omni | 262 | 51.9 | +2 s (+1%) |
| runaway pod started | native | 113 | 11.3 |  |
| runaway pod started | omni | 84 | 6.7 | -30 s (-26%) |
| probe blind | native | 73 | 0.7 |  |
| probe blind | omni | 60 | 0.0 | -13 s (-18%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*