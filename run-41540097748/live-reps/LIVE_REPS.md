# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.516 | 1.518 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.8 | 157.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.8 | 157.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 118.7 | 64.61 | 67.56 |
| response time (ms), 95th percentile | 262.7 | 93.79 | 94.65 |
| response time (ms), 99th percentile | 460.9 | 125.7 | 129.9 |
| time over the response line (% of samples) | 1.511 | 0.01198 | 0.2043 |
| failed requests (%) | 0 | 0 | 0.03719 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | 34.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.08 | 0.1067 |
| utilisation (used / allocatable) | 0.03193 | 0.03081 | 0.03137 |
| CPU used (cores), mean | 0.7664 | 0.7394 | 0.7528 |
| Omni's own CPU (cores), mean | 0 | 0.03182 | 0.03297 |
| CPU used with Omni's own (cores), mean | 0.7664 | 0.7712 | 0.7858 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 891.7 | 906 | 889.6 |
| HPA replicas, mean | 7.722 | 7.917 | 8.741 |
| pods started | 5.4 | 5.1 | 11.7 |
| pod start wait, total (s) | 8.8 | 6.7 | 17.2 |
| pod start wait, mean (s) | 1.627 | 1.393 | 1.462 |
| host CPU busy, the real machine under kind (%) | 23.65 | 24.06 | 24.74 |
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
| node-hours | 1.516 | 1.518 | +0.1% | +0.0004 to +0.0036 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.8 | −0.0% | −0.3188 to +0.2676 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.8 | −0.0% | −0.3188 to +0.2676 | no |
| response time (ms), mean | 118.7 | 64.61 | −45.5% | −80.0206 to −28.0694 | yes: GAIN |
| response time (ms), 95th percentile | 262.7 | 93.79 | −64.3% | −233.4035 to −104.3555 | yes: GAIN |
| response time (ms), 99th percentile | 460.9 | 125.7 | −72.7% | −483.7056 to −186.7126 | yes: GAIN |
| time over the response line (% of samples) | 1.511 | 0.01198 | −99.2% | −2.7525 to −0.2464 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −2.9405 to −0.0595 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | +19.200 (native is 0) | +17.8179 to +20.5821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.08 | −40.0% | −0.2688 to +0.1621 | no |
| utilisation (used / allocatable) | 0.03193 | 0.03081 | −3.5% | −0.0023 to +0.0000 | no |
| CPU used (cores), mean | 0.7664 | 0.7394 | −3.5% | −0.0548 to +0.0007 | no |
| Omni's own CPU (cores), mean | 0 | 0.03182 | +0.032 (native is 0) | +0.0266 to +0.0371 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7664 | 0.7712 | +0.6% | −0.0188 to +0.0284 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 891.7 | 906 | +1.6% | −10.0713 to +38.6712 | no |
| HPA replicas, mean | 7.722 | 7.917 | +2.5% | −0.0895 to +0.4800 | no |
| pods started | 5.4 | 5.1 | −5.6% | −1.0578 to +0.4578 | no |
| pod start wait, total (s) | 8.8 | 6.7 | −23.9% | −4.1358 to −0.0642 | yes: GAIN |
| pod start wait, mean (s) | 1.627 | 1.393 | −14.3% | −0.5761 to +0.1094 | no |
| host CPU busy, the real machine under kind (%) | 23.65 | 24.06 | +1.8% | −0.2287 to +1.0602 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.512 | −0.3% | −0.0116 to +0.0039 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.3 | −0.3% | −1.2312 to +0.1854 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.3 | −0.3% | −1.2312 to +0.1854 | no |
| response time (ms), mean | 118.7 | 67.56 | −43.1% | −76.6804 to −25.5186 | yes: GAIN |
| response time (ms), 95th percentile | 262.7 | 94.65 | −64.0% | −232.6583 to −103.3847 | yes: GAIN |
| response time (ms), 99th percentile | 460.9 | 129.9 | −71.8% | −487.9846 to −174.0594 | yes: GAIN |
| time over the response line (% of samples) | 1.511 | 0.2043 | −86.5% | −2.5055 to −0.1088 | yes: GAIN |
| failed requests (%) | 0 | 0.03719 | +0.037 (native is 0) | −0.0227 to +0.0971 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0.3 | −80.0% | −2.4972 to +0.0972 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.300 (native is 0) | +25.8495 to +42.7505 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1067 | −20.0% | −0.2164 to +0.1630 | no |
| utilisation (used / allocatable) | 0.03193 | 0.03137 | −1.8% | −0.0016 to +0.0005 | no |
| CPU used (cores), mean | 0.7664 | 0.7528 | −1.8% | −0.0391 to +0.0119 | no |
| Omni's own CPU (cores), mean | 0 | 0.03297 | +0.033 (native is 0) | +0.0287 to +0.0373 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7664 | 0.7858 | +2.5% | −0.0037 to +0.0424 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 891.7 | 889.6 | −0.2% | −28.5419 to +24.3334 | no |
| HPA replicas, mean | 7.722 | 8.741 | +13.2% | +0.8396 to +1.1984 | yes: power given |
| pods started | 5.4 | 11.7 | +116.7% | +4.4826 to +8.1174 | yes: power given |
| pod start wait, total (s) | 8.8 | 17.2 | +95.5% | +4.2674 to +12.5326 | yes: LOSS |
| pod start wait, mean (s) | 1.627 | 1.462 | −10.1% | −0.4504 to +0.1211 | no |
| host CPU busy, the real machine under kind (%) | 23.65 | 24.74 | +4.6% | +0.4123 to +1.7740 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.518 | 1.512 | −0.4% | −0.0140 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.3 | −0.3% | −1.3474 to +0.3528 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.3 | −0.3% | −1.3474 to +0.3528 | no |
| response time (ms), mean | 64.61 | 67.56 | +4.6% | +1.4117 to +4.4792 | yes: LOSS |
| response time (ms), 95th percentile | 93.79 | 94.65 | +0.9% | −0.6257 to +2.3417 | no |
| response time (ms), 99th percentile | 125.7 | 129.9 | +3.3% | −7.1105 to +15.4847 | no |
| time over the response line (% of samples) | 0.01198 | 0.2043 | +1605.7% | +0.0692 to +0.3154 | yes: LOSS |
| failed requests (%) | 0 | 0.03719 | +0.037 (native is 0) | −0.0227 to +0.0971 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 34.3 | +78.6% | +6.0617 to +24.1383 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 52.5 | −41.7% | −80.7751 to +5.7751 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | +33.3% | −0.2018 to +0.2551 | no |
| utilisation (used / allocatable) | 0.03081 | 0.03137 | +1.8% | −0.0001 to +0.0012 | no |
| CPU used (cores), mean | 0.7394 | 0.7528 | +1.8% | −0.0015 to +0.0284 | no |
| Omni's own CPU (cores), mean | 0.03182 | 0.03297 | +3.6% | −0.0009 to +0.0032 | no |
| CPU used with Omni's own (cores), mean | 0.7712 | 0.7858 | +1.9% | −0.0011 to +0.0303 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 906 | 889.6 | −1.8% | −40.3543 to +7.5459 | no |
| HPA replicas, mean | 7.917 | 8.741 | +10.4% | +0.4234 to +1.2241 | yes: power given |
| pods started | 5.1 | 11.7 | +129.4% | +4.8414 to +8.3586 | yes: power given |
| pod start wait, total (s) | 6.7 | 17.2 | +156.7% | +6.6516 to +14.3484 | yes: LOSS |
| pod start wait, mean (s) | 1.393 | 1.462 | +4.9% | −0.2368 to +0.3741 | no |
| host CPU busy, the real machine under kind (%) | 24.06 | 24.74 | +2.8% | +0.0303 to +1.3245 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*