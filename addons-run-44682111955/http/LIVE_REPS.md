# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 161.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 193.4 | 87.24 |
| response time (ms), 95th percentile | 465.1 | 143.9 |
| response time (ms), 99th percentile | 647.2 | 288.8 |
| time over the response line (% of samples) | 4.389 | 0.1341 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 189.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 |
| utilisation (used / allocatable) | 0.03029 | 0.04682 |
| CPU used (cores), mean | 0.7269 | 1.124 |
| Omni's own CPU (cores), mean | 0 | 0.07176 |
| CPU used with Omni's own (cores), mean | 0.7269 | 1.195 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.3 | 576.8 |
| HPA replicas, mean | 3.033 | 2.334 |
| pods started | 3 | 2.1 |
| pod start wait, total (s) | 3.5 | 3 |
| pod start wait, mean (s) | 1.167 | 1.483 |
| host CPU busy, the real machine under kind (%) | 23.55 | 36.74 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.518 | 1.516 | −0.1% | −0.0100 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 161.4 | +2.3% | +2.2624 to +5.0515 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 161.4 | +2.3% | +2.2624 to +5.0515 | yes: power given |
| response time (ms), mean | 193.4 | 87.24 | −54.9% | −127.9719 to −84.3011 | yes: GAIN |
| response time (ms), 95th percentile | 465.1 | 143.9 | −69.1% | −371.1496 to −271.3384 | yes: GAIN |
| response time (ms), 99th percentile | 647.2 | 288.8 | −55.4% | −422.2258 to −294.5138 | yes: GAIN |
| time over the response line (% of samples) | 4.389 | 0.1341 | −96.9% | −6.3097 to −2.2002 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 0.2 | −95.3% | −6.1358 to −2.0642 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 189.8 | +189.800 (native is 0) | +151.9273 to +227.6727 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | +33.3% | −0.1404 to +0.1937 | no |
| utilisation (used / allocatable) | 0.03029 | 0.04682 | +54.6% | +0.0135 to +0.0195 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7269 | 1.124 | +54.6% | +0.3251 to +0.4685 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07176 | +0.072 (native is 0) | +0.0580 to +0.0855 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7269 | 1.195 | +64.5% | +0.3846 to +0.5526 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.3 | 576.8 | −33.0% | −309.8558 to −257.1046 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.033 | 2.334 | −23.0% | −0.8989 to −0.4992 | yes: GAIN |
| pods started | 3 | 2.1 | −30.0% | −1.3060 to −0.4940 | yes: GAIN |
| pod start wait, total (s) | 3.5 | 3 | −14.3% | −1.2726 to +0.2726 | no |
| pod start wait, mean (s) | 1.167 | 1.483 | +27.1% | −0.1018 to +0.7352 | no |
| host CPU busy, the real machine under kind (%) | 23.55 | 36.74 | +56.0% | +10.8043 to +15.5737 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*