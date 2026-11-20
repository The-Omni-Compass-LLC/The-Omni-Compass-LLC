# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.915 |
| node-hours | 1.486 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 163 | 163.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.4 | 161.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 164 | 115.3 |
| response time (ms), 95th percentile | 342.4 | 166.6 |
| response time (ms), 99th percentile | 1018 | 523.8 |
| time over the response line (% of samples) | 5.745 | 4.314 |
| failed requests (%) | 3.156 | 2.923 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6267 | 0.3467 |
| utilisation (used / allocatable) | 0.06164 | 0.06165 |
| CPU used (cores), mean | 1.459 | 1.459 |
| Omni's own CPU (cores), mean | 0 | 0.03921 |
| CPU used with Omni's own (cores), mean | 1.459 | 1.498 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 450.8 |
| HPA replicas, mean | 8.312 | 9.751 |
| pods started | 5.8 | 9.8 |
| pod start wait, total (s) | 18.6 | 17.5 |
| pod start wait, mean (s) | 2.966 | 1.757 |
| host CPU busy, the real machine under kind (%) | 42.73 | 43.81 |
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
| worker nodes in service, mean | 5.915 | 5.915 | +0.0% | −0.0055 to +0.0059 | no |
| node-hours | 1.486 | 1.49 | +0.2% | +0.0007 to +0.0066 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 163 | 163.3 | +0.2% | +0.0753 to +0.6334 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.4 | 161.7 | +0.2% | +0.0478 to +0.6609 | yes: power given |
| response time (ms), mean | 164 | 115.3 | −29.7% | −72.7948 to −24.5933 | yes: GAIN |
| response time (ms), 95th percentile | 342.4 | 166.6 | −51.4% | −248.9745 to −102.7335 | yes: GAIN |
| response time (ms), 99th percentile | 1018 | 523.8 | −48.6% | −966.3296 to −23.0114 | yes: GAIN |
| time over the response line (% of samples) | 5.745 | 4.314 | −24.9% | −2.8638 to +0.0011 | no |
| failed requests (%) | 3.156 | 2.923 | −7.4% | −0.7439 to +0.2781 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 4.7 | −6.0% | −1.3144 to +0.7144 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.4 | +40.400 (native is 0) | +34.4324 to +46.3676 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6267 | 0.3467 | −44.7% | −0.8201 to +0.2601 | no |
| utilisation (used / allocatable) | 0.06164 | 0.06165 | +0.0% | −0.0012 to +0.0012 | no |
| CPU used (cores), mean | 1.459 | 1.459 | +0.0% | −0.0279 to +0.0284 | no |
| Omni's own CPU (cores), mean | 0 | 0.03921 | +0.039 (native is 0) | +0.0343 to +0.0442 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.459 | 1.498 | +2.7% | +0.0130 to +0.0659 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 450.8 | −0.5% | −9.5437 to +4.6546 | no |
| HPA replicas, mean | 8.312 | 9.751 | +17.3% | +0.6769 to +2.2017 | yes: power given |
| pods started | 5.8 | 9.8 | +69.0% | +2.2479 to +5.7521 | yes: power given |
| pod start wait, total (s) | 18.6 | 17.5 | −5.9% | −20.9989 to +18.7989 | no |
| pod start wait, mean (s) | 2.966 | 1.757 | −40.7% | −3.9602 to +1.5437 | no |
| host CPU busy, the real machine under kind (%) | 42.73 | 43.81 | +2.5% | +0.5495 to +1.6048 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 46 | 12.8 |  |
| machine down | omni | 31 | 9.3 | -15 s (-33%) |
| spike | native | 209 | 29.3 |  |
| spike | omni | 210 | 26.3 | +1 s (+0%) |
| runaway pod started | native | 56 | 3.9 |  |
| runaway pod started | omni | 37 | 2.7 | -19 s (-35%) |
| probe blind | native | 62 | 0.1 |  |
| probe blind | omni | 60 | 0.1 | -2 s (-3%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*