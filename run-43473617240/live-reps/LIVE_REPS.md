# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.468 | 9.537 |
| node-hours | 5.031 | 5.03 | 3.966 | 3.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 525.3 | 524.8 | 525.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 525.3 | 445.4 | 448.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 477.7 | 613.1 | 564.8 | 706.3 |
| response time (ms), 95th percentile | 1777 | 2508 | 2219 | 2869 |
| response time (ms), 99th percentile | 2422 | 3601 | 3023 | 3996 |
| time over the response line (% of samples) | 17 | 20.55 | 21.25 | 23.66 |
| failed requests (%) | 0.01465 | 0.0247 | 0.02457 | 0.1788 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 13.5 | 11.6 | 14.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 110.9 | 53.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 27.3 | 32.05 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.65 | 35.66 | 19.54 | 44.85 |
| utilisation (used / allocatable) | 0.03332 | 0.03345 | 0.04268 | 0.04326 |
| CPU used (cores), mean | 1.599 | 1.606 | 1.585 | 1.61 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05305 | 0.0397 |
| CPU used with Omni's own (cores), mean | 1.599 | 1.606 | 1.638 | 1.649 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.4 | 789.2 | 675.5 | 668.5 |
| HPA replicas, mean | 4.009 | 4.054 | 4.376 | 4.253 |
| pods started | 0 | 0.1 | 2.1 | 1.4 |
| pod start wait, total (s) | 0 | 0.2 | 6.2 | 4 |
| pod start wait, mean (s) | 0 | 0.2 | 1.698 | 1.075 |
| host CPU busy, the real machine under kind (%) | 49.2 | 55.73 | 54.67 | 60.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 838.9 | 940.7 | 879.2 | 974.1 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 7.78 | 7.832 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 5.804 | 0.1042 | 7.421 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 33.9 | 0.4 | 66.9 |
| queue: job turnaround, submitted to done, mean (s) | 147 | 246 | 182.1 | 277.1 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan |

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
| worker nodes in service, mean | 12 | 9.537 | −20.5% | −4.1401 to −0.7861 | yes: GAIN |
| node-hours | 5.03 | 3.999 | −20.5% | −1.7350 to −0.3275 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 525.8 | +0.1% | −2.0969 to +3.2190 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 448.4 | −14.6% | −130.0406 to −23.6790 | yes: GAIN |
| response time (ms), mean | 613.1 | 706.3 | +15.2% | −62.3540 to +248.6902 | no |
| response time (ms), 95th percentile | 2508 | 2869 | +14.4% | −227.2226 to +950.6446 | no |
| response time (ms), 99th percentile | 3601 | 3996 | +11.0% | −288.9011 to +1079.0485 | no |
| time over the response line (% of samples) | 20.55 | 23.66 | +15.1% | −0.8713 to +7.0920 | no |
| failed requests (%) | 0.0247 | 0.1788 | +624.0% | −0.0398 to +0.3480 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 14.6 | +8.1% | −1.7303 to +3.9303 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.8 | +53.800 (native is 0) | +40.2330 to +67.3670 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.66 | 44.85 | +25.8% | −29.6992 to +48.0759 | no |
| utilisation (used / allocatable) | 0.03345 | 0.04326 | +29.3% | +0.0033 to +0.0164 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.606 | 1.61 | +0.2% | −0.1427 to +0.1507 | no |
| Omni's own CPU (cores), mean | 0 | 0.0397 | +0.040 (native is 0) | +0.0302 to +0.0492 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.606 | 1.649 | +2.7% | −0.1065 to +0.1939 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 789.2 | 668.5 | −15.3% | −211.8646 to −29.4480 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.054 | 4.253 | +4.9% | −0.1425 to +0.5409 | no |
| pods started | 0.1 | 1.4 | +1300.0% | −0.3189 to +2.9189 | no |
| pod start wait, total (s) | 0.2 | 4 | +1900.0% | −1.0725 to +8.6725 | no |
| pod start wait, mean (s) | 0.2 | 1.075 | +437.5% | −0.0456 to +1.7956 | no |
| host CPU busy, the real machine under kind (%) | 55.73 | 60.38 | +8.3% | +2.4275 to +6.8581 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 940.7 | 974.1 | +3.6% | −6.6191 to +73.4191 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 7.832 | −34.7% | −6.7821 to −1.5543 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.804 | 7.421 | +27.9% | −1.5377 to +4.7710 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33.9 | 66.9 | +97.3% | −39.3966 to +105.3966 | no |
| queue: job turnaround, submitted to done, mean (s) | 246 | 277.1 | +12.6% | −13.1796 to +75.3046 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.031 | 5.03 | −0.0% | −0.0228 to +0.0215 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 525.3 | +0.0% | −2.8539 to +3.2787 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 525.3 | +0.0% | −2.8539 to +3.2787 | no |
| response time (ms), mean | 477.7 | 613.1 | +28.3% | +46.5916 to +224.1592 | yes: LOSS |
| response time (ms), 95th percentile | 1777 | 2508 | +41.1% | +263.0031 to +1197.9559 | yes: LOSS |
| response time (ms), 99th percentile | 2422 | 3601 | +48.6% | +643.2134 to +1713.4846 | yes: LOSS |
| time over the response line (% of samples) | 17 | 20.55 | +20.9% | +0.2527 to +6.8487 | yes: LOSS |
| failed requests (%) | 0.01465 | 0.0247 | +68.6% | −0.0320 to +0.0521 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 13.5 | +35.0% | +0.9710 to +6.0290 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.65 | 35.66 | +182.0% | −1.1334 to +47.1634 | no |
| utilisation (used / allocatable) | 0.03332 | 0.03345 | +0.4% | −0.0019 to +0.0022 | no |
| CPU used (cores), mean | 1.599 | 1.606 | +0.4% | −0.0934 to +0.1060 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.599 | 1.606 | +0.4% | −0.0934 to +0.1060 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.4 | 789.2 | −2.0% | −58.8272 to +26.4244 | no |
| HPA replicas, mean | 4.009 | 4.054 | +1.1% | −0.2251 to +0.3154 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 49.2 | 55.73 | +13.3% | +4.9179 to +8.1561 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.9 | 940.7 | +12.1% | +53.8409 to +149.7591 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 5.804 | +8094.1% | −1.1916 to +12.6583 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 33.9 | +8375.0% | −39.7648 to +106.7648 | no |
| queue: job turnaround, submitted to done, mean (s) | 147 | 246 | +67.3% | +49.4168 to +148.6248 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.468 | −21.1% | −4.2904 to −0.7735 | yes: GAIN |
| node-hours | 5.031 | 3.966 | −21.2% | −1.8048 to −0.3238 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 524.8 | −0.0% | −1.8204 to +1.4075 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 445.4 | −15.2% | −135.2610 to −24.0978 | yes: GAIN |
| response time (ms), mean | 477.7 | 564.8 | +18.2% | −2.3584 to +176.5094 | no |
| response time (ms), 95th percentile | 1777 | 2219 | +24.8% | +123.2786 to +759.6534 | yes: LOSS |
| response time (ms), 99th percentile | 2422 | 3023 | +24.8% | +149.5048 to +1051.5344 | yes: LOSS |
| time over the response line (% of samples) | 17 | 21.25 | +25.0% | +2.1393 to +6.3641 | yes: LOSS |
| failed requests (%) | 0.01465 | 0.02457 | +67.7% | −0.0330 to +0.0528 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 11.6 | +16.0% | −0.0927 to +3.2927 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.9 | +110.900 (native is 0) | +52.0769 to +169.7231 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.65 | 19.54 | +54.4% | +1.3510 to +12.4223 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03332 | 0.04268 | +28.1% | +0.0028 to +0.0159 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.599 | 1.585 | −0.9% | −0.0654 to +0.0364 | no |
| Omni's own CPU (cores), mean | 0 | 0.05305 | +0.053 (native is 0) | +0.0477 to +0.0584 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.599 | 1.638 | +2.4% | −0.0137 to +0.0908 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.4 | 675.5 | −16.1% | −219.7977 to −40.0367 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.009 | 4.376 | +9.2% | −0.1361 to +0.8698 | no |
| pods started | 0 | 2.1 | +2.100 (native is 0) | +0.3989 to +3.8011 | yes: power given |
| pod start wait, total (s) | 0 | 6.2 | +6.200 (native is 0) | +0.7649 to +11.6351 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.698 | +1.698 (native is 0) | +0.6016 to +2.7936 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.2 | 54.67 | +11.1% | +4.2601 to +6.6964 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.9 | 879.2 | +4.8% | +11.4147 to +69.1853 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.78 | −35.2% | −6.9616 to −1.4783 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.1042 | +47.1% | −0.0225 to +0.0892 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 147 | 182.1 | +23.9% | +10.0837 to +60.0496 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.468 | −21.1% | −4.2904 to −0.7735 | yes: GAIN |
| node-hours | 5.03 | 3.966 | −21.1% | −1.8022 to −0.3251 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 524.8 | −0.1% | −3.3807 to +2.5431 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 445.4 | −15.2% | −136.2868 to −23.4967 | yes: GAIN |
| response time (ms), mean | 613.1 | 564.8 | −7.9% | −92.8261 to −3.7737 | yes: GAIN |
| response time (ms), 95th percentile | 2508 | 2219 | −11.5% | −593.6336 to +15.6066 | no |
| response time (ms), 99th percentile | 3601 | 3023 | −16.0% | −1022.9535 to −132.7053 | yes: GAIN |
| time over the response line (% of samples) | 20.55 | 21.25 | +3.4% | −3.6856 to +5.0877 | no |
| failed requests (%) | 0.0247 | 0.02457 | −0.5% | −0.0567 to +0.0564 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 11.6 | −14.1% | −3.6011 to −0.1989 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.9 | +110.900 (native is 0) | +52.0769 to +169.7231 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.66 | 19.54 | −45.2% | −35.4921 to +3.2354 | no |
| utilisation (used / allocatable) | 0.03345 | 0.04268 | +27.6% | +0.0037 to +0.0148 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.606 | 1.585 | −1.3% | −0.1507 to +0.1091 | no |
| Omni's own CPU (cores), mean | 0 | 0.05305 | +0.053 (native is 0) | +0.0477 to +0.0584 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.606 | 1.638 | +2.0% | −0.1018 to +0.1663 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 789.2 | 675.5 | −14.4% | −181.8167 to −45.6149 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.054 | 4.376 | +7.9% | −0.1608 to +0.8043 | no |
| pods started | 0.1 | 2.1 | +2000.0% | +0.4548 to +3.5452 | yes: power given |
| pod start wait, total (s) | 0.2 | 6.2 | +3000.0% | +0.8861 to +11.1139 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.698 | +748.8% | +0.4598 to +2.5355 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.73 | 54.67 | −1.9% | −2.2668 to +0.1493 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 940.7 | 879.2 | −6.5% | −87.4276 to −35.5724 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 7.78 | −35.2% | −6.9616 to −1.4783 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.804 | 0.1042 | −98.2% | −12.5884 to +1.1884 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33.9 | 0.4 | −98.8% | −106.7648 to +39.7648 | no |
| queue: job turnaround, submitted to done, mean (s) | 246 | 182.1 | −26.0% | −93.4754 to −34.4330 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.537 | −20.5% | −4.1401 to −0.7861 | yes: GAIN |
| node-hours | 5.031 | 3.999 | −20.5% | −1.7360 to −0.3279 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 525.8 | +0.1% | −1.1960 to +2.7428 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 448.4 | −14.6% | −128.7685 to −24.5263 | yes: GAIN |
| response time (ms), mean | 477.7 | 706.3 | +47.8% | +24.0537 to +433.0333 | yes: LOSS |
| response time (ms), 95th percentile | 1777 | 2869 | +61.5% | +313.2827 to +1871.0983 | yes: LOSS |
| response time (ms), 99th percentile | 2422 | 3996 | +65.0% | +745.4330 to +2401.4124 | yes: LOSS |
| time over the response line (% of samples) | 17 | 23.66 | +39.2% | +1.7741 to +11.5480 | yes: LOSS |
| failed requests (%) | 0.01465 | 0.1788 | +1120.4% | −0.0380 to +0.3663 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 14.6 | +46.0% | +1.8358 to +7.3642 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.8 | +53.800 (native is 0) | +40.2330 to +67.3670 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.65 | 44.85 | +254.6% | −19.6224 to +84.0290 | no |
| utilisation (used / allocatable) | 0.03332 | 0.04326 | +29.8% | +0.0021 to +0.0177 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.599 | 1.61 | +0.6% | −0.1140 to +0.1346 | no |
| Omni's own CPU (cores), mean | 0 | 0.0397 | +0.040 (native is 0) | +0.0302 to +0.0492 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.599 | 1.649 | +3.1% | −0.0715 to +0.1714 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.4 | 668.5 | −17.0% | −253.7892 to −19.9261 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.009 | 4.253 | +6.1% | −0.2164 to +0.7051 | no |
| pods started | 0 | 1.4 | +1.400 (native is 0) | −0.2927 to +3.0927 | no |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | −1.0128 to +9.0128 | no |
| pod start wait, mean (s) | 0 | 1.075 | +1.075 (native is 0) | +0.0632 to +2.0868 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.2 | 60.38 | +22.7% | +8.6085 to +13.7512 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.9 | 974.1 | +16.1% | +63.2194 to +207.1806 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.832 | −34.7% | −6.7821 to −1.5543 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 7.421 | +10376.5% | −1.1674 to +15.8674 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 66.9 | +16625.0% | −31.3466 to +164.3466 | no |
| queue: job turnaround, submitted to done, mean (s) | 147 | 277.1 | +88.5% | +53.8974 to +206.2693 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*