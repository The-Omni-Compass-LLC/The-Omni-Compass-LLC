# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.342 |
| node-hours | 2.514 | 1.822 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 220.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 452.7 | 412 |
| response time (ms), 95th percentile | 2667 | 2649 |
| response time (ms), 99th percentile | 3616 | 3756 |
| time over the response line (% of samples) | 16.25 | 16.48 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 181.4 | 193.4 |
| utilisation (used / allocatable) | 0.05997 | 0.0814 |
| CPU used (cores), mean | 1.439 | 1.413 |
| Omni's own CPU (cores), mean | 0 | 0.07608 |
| CPU used with Omni's own (cores), mean | 1.439 | 1.489 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.7 | 373.8 |
| HPA replicas, mean | 2.034 | 2.514 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 0.7 | 1.6 |
| pod start wait, mean (s) | 0.7 | 0.8 |
| host CPU busy, the real machine under kind (%) | 41.67 | 44.18 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 561.1 | 578.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.311 |
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
| worker nodes in service, mean | 6 | 4.342 | −27.6% | −1.9368 to −1.3795 | yes: GAIN |
| node-hours | 2.514 | 1.822 | −27.5% | −0.8091 to −0.5753 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.4 | −0.0% | −1.5099 to +1.4143 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 220.3 | −19.2% | −60.8657 to −43.5841 | yes: GAIN |
| response time (ms), mean | 452.7 | 412 | −9.0% | −59.2471 to −22.0243 | yes: GAIN |
| response time (ms), 95th percentile | 2667 | 2649 | −0.7% | −121.8180 to +85.4230 | no |
| response time (ms), 99th percentile | 3616 | 3756 | +3.9% | −68.8808 to +348.3592 | no |
| time over the response line (% of samples) | 16.25 | 16.48 | +1.4% | −0.4460 to +0.8965 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | +1.0% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 | +11.500 (native is 0) | +10.2726 to +12.7274 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 181.4 | 193.4 | +6.6% | +4.3867 to +19.6533 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05997 | 0.0814 | +35.7% | +0.0164 to +0.0264 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.413 | −1.9% | −0.0826 to +0.0291 | no |
| Omni's own CPU (cores), mean | 0 | 0.07608 | +0.076 (native is 0) | +0.0689 to +0.0832 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.489 | +3.4% | −0.0032 to +0.1018 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.7 | 373.8 | −18.1% | −105.6882 to −59.9740 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.034 | 2.514 | +23.6% | −0.0783 to +1.0402 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.7 | 1.6 | +128.6% | −3.2084 to +5.0084 | no |
| pod start wait, mean (s) | 0.7 | 0.8 | +14.3% | −2.4335 to +2.6335 | no |
| host CPU busy, the real machine under kind (%) | 41.67 | 44.18 | +6.0% | +1.8858 to +3.1433 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 561.1 | 578.5 | +3.1% | +5.8208 to +28.9792 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.311 | −44.8% | −3.0450 to −2.3323 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*