# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.013 |
| node-hours | 2.514 | 2.099 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 275 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 244 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 576.9 | 531.5 |
| response time (ms), 95th percentile | 3132 | 3179 |
| response time (ms), 99th percentile | 4155 | 4169 |
| time over the response line (% of samples) | 18.85 | 18.61 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 209.3 | 213.6 |
| utilisation (used / allocatable) | 0.0683 | 0.07939 |
| CPU used (cores), mean | 1.639 | 1.585 |
| Omni's own CPU (cores), mean | 0 | 0.08334 |
| CPU used with Omni's own (cores), mean | 1.639 | 1.668 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 406.3 | 368.9 |
| HPA replicas, mean | 2.097 | 2.367 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 47.22 | 49.6 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 645.6 | 662.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.319 |
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
| worker nodes in service, mean | 6 | 5.013 | −16.4% | −1.5274 to −0.4457 | yes: GAIN |
| node-hours | 2.514 | 2.099 | −16.5% | −0.6377 to −0.1914 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 275 | −0.2% | −1.7067 to +0.5628 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 244 | −11.5% | −48.1043 to −15.1229 | yes: GAIN |
| response time (ms), mean | 576.9 | 531.5 | −7.9% | −60.1745 to −30.6251 | yes: GAIN |
| response time (ms), 95th percentile | 3132 | 3179 | +1.5% | −68.7034 to +162.1944 | no |
| response time (ms), 99th percentile | 4155 | 4169 | +0.3% | −112.5106 to +141.3702 | no |
| time over the response line (% of samples) | 18.85 | 18.61 | −1.3% | −0.6304 to +0.1422 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.3 | +3.7% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.8 | +9.800 (native is 0) | +8.4179 to +11.1821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 209.3 | 213.6 | +2.0% | −0.3967 to +8.9233 | no |
| utilisation (used / allocatable) | 0.0683 | 0.07939 | +16.2% | +0.0040 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.639 | 1.585 | −3.3% | −0.1013 to −0.0069 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.08334 | +0.083 (native is 0) | +0.0737 to +0.0930 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.639 | 1.668 | +1.8% | −0.0183 to +0.0768 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 406.3 | 368.9 | −9.2% | −65.2736 to −9.4279 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.097 | 2.367 | +12.9% | −0.2564 to +0.7976 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 47.22 | 49.6 | +5.0% | +1.9142 to +2.8514 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 645.6 | 662.9 | +2.7% | +9.8812 to +24.7188 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.319 | −28.0% | −2.5281 to −0.8331 | yes: GAIN |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*