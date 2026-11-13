# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.506 | 1.513 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 160.1 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 160.1 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 114.8 | 85.7 | 75.51 |
| response time (ms), 95th percentile | 240.6 | 158 | 117.4 |
| response time (ms), 99th percentile | 357.8 | 271 | 159.4 |
| time over the response line (% of samples) | 0.3984 | 0.2235 | 0.02396 |
| failed requests (%) | 0 | 0.01258 | 0.01176 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 388.1 | 33.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.32 | 0.08 |
| utilisation (used / allocatable) | 0.03578 | 0.04347 | 0.04516 |
| CPU used (cores), mean | 0.8587 | 1.043 | 1.084 |
| Omni's own CPU (cores), mean | 0 | 0.1048 | 0.01607 |
| CPU used with Omni's own (cores), mean | 0.8587 | 1.148 | 1.1 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733 | 620.2 | 599 |
| HPA replicas, mean | 8.825 | 10.46 | 9.459 |
| pods started | 5.1 | 7.4 | 6.2 |
| pod start wait, total (s) | 7.2 | 11.4 | 10.2 |
| pod start wait, mean (s) | 1.423 | 1.485 | 1.621 |
| host CPU busy, the real machine under kind (%) | 27.17 | 36.14 | 34.35 |
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
| node-hours | 1.506 | 1.513 | +0.5% | −0.0001 to +0.0148 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 160.1 | +1.6% | +1.4445 to +3.5700 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 160.1 | +1.6% | +1.4445 to +3.5700 | yes: power given |
| response time (ms), mean | 114.8 | 85.7 | −25.3% | −39.2789 to −18.8489 | yes: GAIN |
| response time (ms), 95th percentile | 240.6 | 158 | −34.3% | −97.8091 to −67.3929 | yes: GAIN |
| response time (ms), 99th percentile | 357.8 | 271 | −24.3% | −107.4628 to −66.0984 | yes: GAIN |
| time over the response line (% of samples) | 0.3984 | 0.2235 | −43.9% | −0.3560 to +0.0060 | no |
| failed requests (%) | 0 | 0.01258 | +0.013 (native is 0) | −0.0159 to +0.0410 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 388.1 | +388.100 (native is 0) | +256.0430 to +520.1570 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.32 | +50.0% | −0.2499 to +0.4633 | no |
| utilisation (used / allocatable) | 0.03578 | 0.04347 | +21.5% | +0.0043 to +0.0110 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8587 | 1.043 | +21.5% | +0.1041 to +0.2651 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.1048 | +0.105 (native is 0) | +0.0707 to +0.1389 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8587 | 1.148 | +33.7% | +0.1760 to +0.4028 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733 | 620.2 | −15.4% | −151.6153 to −74.0840 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.825 | 10.46 | +18.6% | +0.5102 to +2.7642 | yes: power given |
| pods started | 5.1 | 7.4 | +45.1% | +0.3910 to +4.2090 | yes: power given |
| pod start wait, total (s) | 7.2 | 11.4 | +58.3% | +0.5558 to +7.8442 | yes: LOSS |
| pod start wait, mean (s) | 1.423 | 1.485 | +4.3% | −0.2067 to +0.3305 | no |
| host CPU busy, the real machine under kind (%) | 27.17 | 36.14 | +33.0% | +5.5148 to +12.4227 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.506 | 1.518 | +0.8% | +0.0033 to +0.0207 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 161 | +2.2% | +2.0262 to +4.8077 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 161 | +2.2% | +2.0262 to +4.8077 | yes: power given |
| response time (ms), mean | 114.8 | 75.51 | −34.2% | −54.5915 to −23.9070 | yes: GAIN |
| response time (ms), 95th percentile | 240.6 | 117.4 | −51.2% | −152.9513 to −93.3137 | yes: GAIN |
| response time (ms), 99th percentile | 357.8 | 159.4 | −55.4% | −238.6923 to −158.1159 | yes: GAIN |
| time over the response line (% of samples) | 0.3984 | 0.02396 | −94.0% | −0.6904 to −0.0585 | yes: GAIN |
| failed requests (%) | 0 | 0.01176 | +0.012 (native is 0) | −0.0148 to +0.0384 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.6 | +33.600 (native is 0) | +18.2391 to +48.9609 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.08 | −62.5% | −0.3581 to +0.0915 | no |
| utilisation (used / allocatable) | 0.03578 | 0.04516 | +26.2% | +0.0057 to +0.0130 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8587 | 1.084 | +26.2% | +0.1372 to +0.3131 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01607 | +0.016 (native is 0) | +0.0114 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8587 | 1.1 | +28.1% | +0.1493 to +0.3331 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733 | 599 | −18.3% | −171.9442 to −96.1409 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.825 | 9.459 | +7.2% | −0.3949 to +1.6617 | no |
| pods started | 5.1 | 6.2 | +21.6% | −0.3871 to +2.5871 | no |
| pod start wait, total (s) | 7.2 | 10.2 | +41.7% | −0.4388 to +6.4388 | no |
| pod start wait, mean (s) | 1.423 | 1.621 | +13.9% | −0.1605 to +0.5553 | no |
| host CPU busy, the real machine under kind (%) | 27.17 | 34.35 | +26.4% | +4.7214 to +9.6323 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.518 | +0.3% | −0.0039 to +0.0132 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 161 | +0.6% | −0.0784 to +1.8976 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 161 | +0.6% | −0.0784 to +1.8976 | no |
| response time (ms), mean | 85.7 | 75.51 | −11.9% | −16.2401 to −4.1306 | yes: GAIN |
| response time (ms), 95th percentile | 158 | 117.4 | −25.7% | −64.2092 to −16.8538 | yes: GAIN |
| response time (ms), 99th percentile | 271 | 159.4 | −41.2% | −158.2417 to −65.0053 | yes: GAIN |
| time over the response line (% of samples) | 0.2235 | 0.02396 | −89.3% | −0.3917 to −0.0073 | yes: GAIN |
| failed requests (%) | 0.01258 | 0.01176 | −6.5% | −0.0419 to +0.0402 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 388.1 | 33.6 | −91.3% | −475.9578 to −233.0422 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.08 | −75.0% | −0.6252 to +0.1452 | no |
| utilisation (used / allocatable) | 0.04347 | 0.04516 | +3.9% | +0.0005 to +0.0029 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.043 | 1.084 | +3.9% | +0.0118 to +0.0693 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.1048 | 0.01607 | −84.7% | −0.1189 to −0.0586 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.148 | 1.1 | −4.2% | −0.0840 to −0.0124 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 620.2 | 599 | −3.4% | −38.1519 to −4.2338 | yes, down (shown, not judged) |
| HPA replicas, mean | 10.46 | 9.459 | −9.6% | −2.0924 to +0.0849 | no |
| pods started | 7.4 | 6.2 | −16.2% | −2.9779 to +0.5779 | no |
| pod start wait, total (s) | 11.4 | 10.2 | −10.5% | −4.4131 to +2.0131 | no |
| pod start wait, mean (s) | 1.485 | 1.621 | +9.1% | −0.1330 to +0.4039 | no |
| host CPU busy, the real machine under kind (%) | 36.14 | 34.35 | −5.0% | −3.1444 to −0.4394 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*