# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.516 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 156.8 | 160.2 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 156.8 | 160.2 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 176.5 | 93.28 | 74.54 |
| response time (ms), 95th percentile | 411 | 233 | 111 |
| response time (ms), 99th percentile | 558 | 462.5 | 227 |
| time over the response line (% of samples) | 3.061 | 0.994 | 0.2539 |
| failed requests (%) | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.5 | 1.3 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.3 | 4.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.08 | 0.05333 |
| utilisation (used / allocatable) | 0.02939 | 0.04138 | 0.0443 |
| CPU used (cores), mean | 0.7054 | 0.9931 | 1.063 |
| Omni's own CPU (cores), mean | 0 | 0.05596 | 0.00984 |
| CPU used with Omni's own (cores), mean | 0.7054 | 1.049 | 1.073 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 887.4 | 645.7 | 610.7 |
| HPA replicas, mean | 2.827 | 2.509 | 2.406 |
| pods started | 2.7 | 2.6 | 2.2 |
| pod start wait, total (s) | 3.5 | 3.3 | 3 |
| pod start wait, mean (s) | 1.283 | 1.283 | 1.367 |
| host CPU busy, the real machine under kind (%) | 23.29 | 33.33 | 33.42 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| node-hours | 1.51 | 1.516 | +0.4% | −0.0037 to +0.0164 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 156.8 | 160.2 | +2.2% | +2.2477 to +4.5969 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 156.8 | 160.2 | +2.2% | +2.2477 to +4.5969 | yes: power given |
| response time (ms), mean | 176.5 | 93.28 | −47.2% | −102.6007 to −63.8461 | yes: GAIN |
| response time (ms), 95th percentile | 411 | 233 | −43.3% | −208.0652 to −147.9788 | yes: GAIN |
| response time (ms), 99th percentile | 558 | 462.5 | −17.1% | −131.2346 to −59.7236 | yes: GAIN |
| time over the response line (% of samples) | 3.061 | 0.994 | −67.5% | −3.3634 to −0.7702 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.5 | 1.3 | −62.9% | −3.5403 to −0.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.3 | +78.300 (native is 0) | +58.8531 to +97.7469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.08 | −22.6% | −0.1322 to +0.0855 | no |
| utilisation (used / allocatable) | 0.02939 | 0.04138 | +40.8% | +0.0100 to +0.0140 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7054 | 0.9931 | +40.8% | +0.2401 to +0.3354 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05596 | +0.056 (native is 0) | +0.0460 to +0.0659 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7054 | 1.049 | +48.7% | +0.2873 to +0.4002 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 887.4 | 645.7 | −27.2% | −261.1600 to −222.2728 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.827 | 2.509 | −11.3% | −0.4484 to −0.1884 | yes: GAIN |
| pods started | 2.7 | 2.6 | −3.7% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 3.5 | 3.3 | −5.7% | −1.4972 to +1.0972 | no |
| pod start wait, mean (s) | 1.283 | 1.283 | 0.0% | raw −0.4243 to +0.4243 | STEADY, the same (to nine decimal places) |
| host CPU busy, the real machine under kind (%) | 23.29 | 33.33 | +43.1% | +8.1970 to +11.8706 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.515 | +0.3% | −0.0052 to +0.0152 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 156.8 | 160.7 | +2.5% | +2.5137 to +5.3421 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 156.8 | 160.7 | +2.5% | +2.5137 to +5.3421 | yes: power given |
| response time (ms), mean | 176.5 | 74.54 | −57.8% | −125.8055 to −78.1155 | yes: GAIN |
| response time (ms), 95th percentile | 411 | 111 | −73.0% | −346.7750 to −253.3630 | yes: GAIN |
| response time (ms), 99th percentile | 558 | 227 | −59.3% | −398.0702 to −264.0518 | yes: GAIN |
| time over the response line (% of samples) | 3.061 | 0.2539 | −91.7% | −4.7002 to −0.9137 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.5 | 0.2 | −94.3% | −5.5633 to −1.0367 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.8 | +4.800 (native is 0) | +3.2256 to +6.3744 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.05333 | −48.4% | −0.1673 to +0.0673 | no |
| utilisation (used / allocatable) | 0.02939 | 0.0443 | +50.7% | +0.0116 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7054 | 1.063 | +50.7% | +0.2779 to +0.4376 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00984 | +0.010 (native is 0) | +0.0082 to +0.0115 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7054 | 1.073 | +52.1% | +0.2863 to +0.4489 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 887.4 | 610.7 | −31.2% | −301.8515 to −251.5267 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.827 | 2.406 | −14.9% | −0.6492 to −0.1932 | yes: GAIN |
| pods started | 2.7 | 2.2 | −18.5% | −0.8770 to −0.1230 | yes: GAIN |
| pod start wait, total (s) | 3.5 | 3 | −14.3% | −1.4685 to +0.4685 | no |
| pod start wait, mean (s) | 1.283 | 1.367 | +6.5% | −0.2154 to +0.3820 | no |
| host CPU busy, the real machine under kind (%) | 23.29 | 33.42 | +43.5% | +7.7365 to +12.5072 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.515 | −0.1% | −0.0090 to +0.0063 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 160.7 | +0.3% | −0.4313 to +1.4424 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 160.7 | +0.3% | −0.4313 to +1.4424 | no |
| response time (ms), mean | 93.28 | 74.54 | −20.1% | −23.9178 to −13.5565 | yes: GAIN |
| response time (ms), 95th percentile | 233 | 111 | −52.4% | −163.5462 to −80.5478 | yes: GAIN |
| response time (ms), 99th percentile | 462.5 | 227 | −50.9% | −309.5662 to −161.5976 | yes: GAIN |
| time over the response line (% of samples) | 0.994 | 0.2539 | −74.5% | −1.3445 to −0.1358 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0.2 | −84.6% | −2.3367 to +0.1367 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 78.3 | 4.8 | −93.9% | −92.7388 to −54.2612 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.05333 | −33.3% | −0.1937 to +0.1404 | no |
| utilisation (used / allocatable) | 0.04138 | 0.0443 | +7.0% | +0.0013 to +0.0045 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9931 | 1.063 | +7.0% | +0.0313 to +0.1086 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.05596 | 0.00984 | −82.4% | −0.0544 to −0.0378 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.049 | 1.073 | +2.3% | −0.0088 to +0.0565 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 645.7 | 610.7 | −5.4% | −53.2839 to −16.6615 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.509 | 2.406 | −4.1% | −0.3654 to +0.1597 | no |
| pods started | 2.6 | 2.2 | −15.4% | −0.9001 to +0.1001 | no |
| pod start wait, total (s) | 3.3 | 3 | −9.1% | −1.1294 to +0.5294 | no |
| pod start wait, mean (s) | 1.283 | 1.367 | +6.5% | −0.1877 to +0.3543 | no |
| host CPU busy, the real machine under kind (%) | 33.33 | 33.42 | +0.3% | −0.8363 to +1.0125 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*