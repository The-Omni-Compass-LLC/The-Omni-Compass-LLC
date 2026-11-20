# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 171.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 444.4 | 433.4 |
| response time (ms), 95th percentile | 1737 | 1868 |
| response time (ms), 99th percentile | 4205 | 4356 |
| time over the response line (% of samples) | 21.42 | 21.36 |
| failed requests (%) | 2.009 | 1.273 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 450.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.453 | 1.393 |
| utilisation (used / allocatable) | 0.09265 | 0.09209 |
| CPU used (cores), mean | 2.224 | 2.21 |
| Omni's own CPU (cores), mean | 0 | 0.08001 |
| CPU used with Omni's own (cores), mean | 2.224 | 2.29 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.8 | 314.6 |
| HPA replicas, mean | 14.88 | 15.38 |
| pods started | 5.8 | 6.1 |
| pod start wait, total (s) | 9.4 | 10.8 |
| pod start wait, mean (s) | 1.63 | 1.783 |
| host CPU busy, the real machine under kind (%) | 63.56 | 66.39 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 243.9 | 297.5 |
| second app: response time (ms), 99th percentile | 2463 | 3437 |
| second app: time over the response line (% of samples) | 12.78 | 13.47 |
| second app: failed requests (%) | 10.45 | 10.81 |

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
| node-hours | 1.517 | 1.513 | −0.3% | −0.0130 to +0.0050 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.1 | −0.3% | −1.5133 to +0.3304 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 171.1 | −0.3% | −1.5133 to +0.3304 | no |
| response time (ms), mean | 444.4 | 433.4 | −2.5% | −44.4683 to +22.4647 | no |
| response time (ms), 95th percentile | 1737 | 1868 | +7.6% | −65.0567 to +327.8637 | no |
| response time (ms), 99th percentile | 4205 | 4356 | +3.6% | −1019.1808 to +1320.6834 | no |
| time over the response line (% of samples) | 21.42 | 21.36 | −0.3% | −1.1037 to +0.9785 | no |
| failed requests (%) | 2.009 | 1.273 | −36.6% | −1.6052 to +0.1344 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.7 | −3.7% | −1.3690 to +0.7690 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 450.9 | +450.900 (native is 0) | +402.9199 to +498.8801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.453 | 1.393 | −4.1% | −0.7083 to +0.5883 | no |
| utilisation (used / allocatable) | 0.09265 | 0.09209 | −0.6% | −0.0022 to +0.0011 | no |
| CPU used (cores), mean | 2.224 | 2.21 | −0.6% | −0.0526 to +0.0254 | no |
| Omni's own CPU (cores), mean | 0 | 0.08001 | +0.080 (native is 0) | +0.0695 to +0.0906 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.224 | 2.29 | +3.0% | +0.0341 to +0.0987 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.8 | 314.6 | −0.1% | −6.5998 to +6.0544 | no |
| HPA replicas, mean | 14.88 | 15.38 | +3.3% | −0.2079 to +1.1965 | no |
| pods started | 5.8 | 6.1 | +5.2% | −0.4578 to +1.0578 | no |
| pod start wait, total (s) | 9.4 | 10.8 | +14.9% | −0.5134 to +3.3134 | no |
| pod start wait, mean (s) | 1.63 | 1.783 | +9.4% | −0.3098 to +0.6165 | no |
| host CPU busy, the real machine under kind (%) | 63.56 | 66.39 | +4.5% | +2.1357 to +3.5261 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 243.9 | 297.5 | +22.0% | −19.8050 to +126.9680 | no |
| second app: response time (ms), 99th percentile | 2463 | 3437 | +39.6% | −82.7864 to +2031.2462 | no |
| second app: time over the response line (% of samples) | 12.78 | 13.47 | +5.4% | −0.4042 to +1.7897 | no |
| second app: failed requests (%) | 10.45 | 10.81 | +3.5% | −0.0936 to +0.8270 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*