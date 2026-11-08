# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.512 | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.1 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.1 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 172.7 | 85.95 | 87.13 |
| response time (ms), 95th percentile | 390 | 128.1 | 128.7 |
| response time (ms), 99th percentile | 654.7 | 188.2 | 169.9 |
| time over the response line (% of samples) | 2.697 | 0 | 0.2321 |
| failed requests (%) | 0 | 0 | 0.1362 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | 24.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.1333 | 0.02667 |
| utilisation (used / allocatable) | 0.04199 | 0.03946 | 0.04066 |
| CPU used (cores), mean | 1.008 | 0.947 | 0.9759 |
| Omni's own CPU (cores), mean | 0 | 0.03881 | 0.03947 |
| CPU used with Omni's own (cores), mean | 1.008 | 0.9858 | 1.015 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 660.3 | 693.7 | 676.6 |
| HPA replicas, mean | 8.79 | 9.136 | 9.545 |
| pods started | 4.9 | 3.5 | 10 |
| pod start wait, total (s) | 8.4 | 5.8 | 17.9 |
| pod start wait, mean (s) | 1.563 | 1.418 | 1.842 |
| host CPU busy, the real machine under kind (%) | 30.62 | 30.56 | 31.45 |
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
| node-hours | 1.512 | 1.513 | +0.1% | −0.0007 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.1 | −0.3% | −0.7448 to −0.1685 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.1 | −0.3% | −0.7448 to −0.1685 | yes: GAIN |
| response time (ms), mean | 172.7 | 85.95 | −50.2% | −106.8755 to −66.5567 | yes: GAIN |
| response time (ms), 95th percentile | 390 | 128.1 | −67.2% | −314.4585 to −209.3915 | yes: GAIN |
| response time (ms), 99th percentile | 654.7 | 188.2 | −71.3% | −580.9954 to −351.9456 | yes: GAIN |
| time over the response line (% of samples) | 2.697 | 0 | −100.0% | −3.7868 to −1.6068 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0 | −100.0% | −4.8099 to −1.7901 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | +18.300 (native is 0) | +17.0361 to +19.5639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.1333 | −64.6% | −0.6830 to +0.1963 | no |
| utilisation (used / allocatable) | 0.04199 | 0.03946 | −6.0% | −0.0038 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.008 | 0.947 | −6.0% | −0.0913 to −0.0303 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03881 | +0.039 (native is 0) | +0.0341 to +0.0435 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.008 | 0.9858 | −2.2% | −0.0490 to +0.0051 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 660.3 | 693.7 | +5.1% | +20.7990 to +46.0109 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.79 | 9.136 | +3.9% | −0.1209 to +0.8113 | no |
| pods started | 4.9 | 3.5 | −28.6% | −2.4769 to −0.3231 | yes: GAIN |
| pod start wait, total (s) | 8.4 | 5.8 | −31.0% | −5.6009 to +0.4009 | no |
| pod start wait, mean (s) | 1.563 | 1.418 | −9.3% | −0.5302 to +0.2402 | no |
| host CPU busy, the real machine under kind (%) | 30.62 | 30.56 | −0.2% | −0.5102 to +0.3900 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0066 to +0.0096 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.5 | −0.1% | −0.8817 to +0.6912 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.5 | −0.1% | −0.8817 to +0.6912 | no |
| response time (ms), mean | 172.7 | 87.13 | −49.5% | −106.2526 to −64.8135 | yes: GAIN |
| response time (ms), 95th percentile | 390 | 128.7 | −67.0% | −313.7570 to −208.8050 | yes: GAIN |
| response time (ms), 99th percentile | 654.7 | 169.9 | −74.0% | −610.4996 to −359.0426 | yes: GAIN |
| time over the response line (% of samples) | 2.697 | 0.2321 | −91.4% | −3.5716 to −1.3578 | yes: GAIN |
| failed requests (%) | 0 | 0.1362 | +0.136 (native is 0) | +0.0582 to +0.2142 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0.3 | −90.9% | −4.6860 to −1.3140 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.8 | +24.800 (native is 0) | +16.2908 to +33.3092 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.02667 | −92.9% | −0.6919 to −0.0081 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04199 | 0.04066 | −3.2% | −0.0023 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.008 | 0.9759 | −3.2% | −0.0562 to −0.0075 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03947 | +0.039 (native is 0) | +0.0352 to +0.0437 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.008 | 1.015 | +0.8% | −0.0153 to +0.0305 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 660.3 | 676.6 | +2.5% | +4.1562 to +28.3136 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.79 | 9.545 | +8.6% | +0.4918 to +1.0167 | yes: power given |
| pods started | 4.9 | 10 | +104.1% | +3.2090 to +6.9910 | yes: power given |
| pod start wait, total (s) | 8.4 | 17.9 | +113.1% | +4.9105 to +14.0895 | yes: LOSS |
| pod start wait, mean (s) | 1.563 | 1.842 | +17.8% | −0.3849 to +0.9415 | no |
| host CPU busy, the real machine under kind (%) | 30.62 | 31.45 | +2.7% | +0.3694 to +1.2953 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.513 | +0.0% | −0.0071 to +0.0081 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.5 | +0.2% | −0.4979 to +1.2207 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.5 | +0.2% | −0.4979 to +1.2207 | no |
| response time (ms), mean | 85.95 | 87.13 | +1.4% | −0.5574 to +2.9236 | no |
| response time (ms), 95th percentile | 128.1 | 128.7 | +0.5% | −0.9891 to +2.2771 | no |
| response time (ms), 99th percentile | 188.2 | 169.9 | −9.7% | −33.6775 to −2.9237 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.2321 | +0.232 (native is 0) | +0.1555 to +0.3088 | yes: LOSS |
| failed requests (%) | 0 | 0.1362 | +0.136 (native is 0) | +0.0582 to +0.2142 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.3 | 24.8 | +35.5% | −2.2753 to +15.2753 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 40 | −60.0% | −127.9978 to +7.9978 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.02667 | −80.0% | −0.3642 to +0.1508 | no |
| utilisation (used / allocatable) | 0.03946 | 0.04066 | +3.1% | +0.0004 to +0.0020 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.947 | 0.9759 | +3.1% | +0.0104 to +0.0475 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03881 | 0.03947 | +1.7% | +0.0001 to +0.0013 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9858 | 1.015 | +3.0% | +0.0111 to +0.0480 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.7 | 676.6 | −2.5% | −27.2684 to −7.0717 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.136 | 9.545 | +4.5% | −0.1030 to +0.9211 | no |
| pods started | 3.5 | 10 | +185.7% | +4.5556 to +8.4444 | yes: power given |
| pod start wait, total (s) | 5.8 | 17.9 | +208.6% | +7.1048 to +17.0952 | yes: LOSS |
| pod start wait, mean (s) | 1.418 | 1.842 | +29.8% | −0.2948 to +1.1414 | no |
| host CPU busy, the real machine under kind (%) | 30.56 | 31.45 | +2.9% | +0.5313 to +1.2536 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*