# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 513.9 | 513.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 513.9 | 513.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 271.5 | 164.2 |
| response time (ms), 95th percentile | 749.5 | 359.5 |
| response time (ms), 99th percentile | 2273 | 2001 |
| time over the response line (% of samples) | 16.45 | 10.74 |
| failed requests (%) | 7.779 | 7.956 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.6 | 19.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.4283 |
| utilisation (used / allocatable) | 0.09708 | 0.09631 |
| CPU used (cores), mean | 2.33 | 2.311 |
| Omni's own CPU (cores), mean | 0 | 0.04327 |
| CPU used with Omni's own (cores), mean | 2.33 | 2.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.1 | 318.8 |
| HPA replicas, mean | 9.549 | 12.16 |
| pods started | 5.8 | 9.4 |
| pod start wait, total (s) | 8.7 | 15.8 |
| pod start wait, mean (s) | 1.502 | 1.669 |
| host CPU busy, the real machine under kind (%) | 65.52 | 66.68 |
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
| node-hours | 4.514 | 4.513 | −0.0% | −0.0085 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 513.9 | 513.2 | −0.1% | −2.0553 to +0.7161 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 513.9 | 513.2 | −0.1% | −2.0553 to +0.7161 | no |
| response time (ms), mean | 271.5 | 164.2 | −39.5% | −147.7245 to −66.8786 | yes: GAIN |
| response time (ms), 95th percentile | 749.5 | 359.5 | −52.0% | −534.1855 to −245.8195 | yes: GAIN |
| response time (ms), 99th percentile | 2273 | 2001 | −11.9% | −1731.5322 to +1189.4304 | no |
| time over the response line (% of samples) | 16.45 | 10.74 | −34.7% | −7.7181 to −3.7014 | yes: GAIN |
| failed requests (%) | 7.779 | 7.956 | +2.3% | −0.4194 to +0.7747 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.6 | 19.3 | −24.6% | −7.9537 to −4.6463 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.100 (native is 0) | +40.0718 to +60.1282 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.4283 | +24.2% | −0.3246 to +0.4913 | no |
| utilisation (used / allocatable) | 0.09708 | 0.09631 | −0.8% | −0.0023 to +0.0008 | no |
| CPU used (cores), mean | 2.33 | 2.311 | −0.8% | −0.0552 to +0.0182 | no |
| Omni's own CPU (cores), mean | 0 | 0.04327 | +0.043 (native is 0) | +0.0361 to +0.0504 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.33 | 2.355 | +1.1% | −0.0168 to +0.0663 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.1 | 318.8 | +1.5% | −3.9924 to +13.4060 | no |
| HPA replicas, mean | 9.549 | 12.16 | +27.3% | +1.2262 to +3.9963 | yes: power given |
| pods started | 5.8 | 9.4 | +62.1% | +1.9073 to +5.2927 | yes: power given |
| pod start wait, total (s) | 8.7 | 15.8 | +81.6% | +2.3979 to +11.8021 | yes: LOSS |
| pod start wait, mean (s) | 1.502 | 1.669 | +11.1% | −0.1875 to +0.5212 | no |
| host CPU busy, the real machine under kind (%) | 65.52 | 66.68 | +1.8% | −0.0773 to +2.3802 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*