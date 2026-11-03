# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.064 | 6 |
| node-hours | 2.516 | 2.521 | 2.123 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.9 | 272.5 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.9 | 243.1 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 331 | 133.3 | 318 | 109.1 |
| response time (ms), 95th percentile | 1179 | 230.1 | 1284 | 241.6 |
| response time (ms), 99th percentile | 1654 | 332.9 | 1846 | 352.5 |
| time over the response line (% of samples) | 14.03 | 0.1694 | 14.22 | 0.1572 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 0.1 | 9 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 142.3 | 93.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.913 | 1088 | 10.72 | 1204 |
| utilisation (used / allocatable) | 0.05958 | 0.06012 | 0.07262 | 0.05894 |
| CPU used (cores), mean | 1.43 | 1.443 | 1.433 | 1.415 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07263 | 0.06782 |
| CPU used with Omni's own (cores), mean | 1.43 | 1.443 | 1.506 | 1.482 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 450.8 | 406.8 | 458.5 |
| HPA replicas, mean | 2.025 | 1.952 | 2.469 | 2.067 |
| pods started | 0.1 | 0.1 | 1.4 | 0.5 |
| pod start wait, total (s) | 0.1 | 0.2 | 2.8 | 1 |
| pod start wait, mean (s) | 0.1 | 0.2 | 1.383 | 0.4 |
| host CPU busy, the real machine under kind (%) | 40.73 | 45.03 | 43.97 | 46.86 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 772 | 1455 | 780.7 | 1505 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.609 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 154.2 | 0.05417 | 198.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 748.1 | 0.3 | 787.6 |
| queue: job turnaround, submitted to done, mean (s) | 78.19 | 812.6 | 86.45 | 891 |
| queue: jobs unfinished at the window's end | 0 | 9 | 0 | 10.8 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.521 | 2.515 | −0.2% | −0.0158 to +0.0048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 271.7 | −0.4% | −2.7592 to +0.5254 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 271.7 | −0.4% | −2.7592 to +0.5254 | no |
| response time (ms), mean | 133.3 | 109.1 | −18.2% | −30.6104 to −17.8584 | yes: GAIN |
| response time (ms), 95th percentile | 230.1 | 241.6 | +5.0% | −4.1130 to +26.9360 | no |
| response time (ms), 99th percentile | 332.9 | 352.5 | +5.9% | −5.1956 to +44.3514 | no |
| time over the response line (% of samples) | 0.1694 | 0.1572 | −7.2% | −0.1763 to +0.1519 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93.8 | +93.800 (native is 0) | +84.6037 to +102.9963 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1088 | 1204 | +10.6% | +27.6844 to +203.6990 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06012 | 0.05894 | −2.0% | −0.0029 to +0.0005 | no |
| CPU used (cores), mean | 1.443 | 1.415 | −2.0% | −0.0688 to +0.0126 | no |
| Omni's own CPU (cores), mean | 0 | 0.06782 | +0.068 (native is 0) | +0.0602 to +0.0754 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.482 | +2.8% | +0.0011 to +0.0782 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 458.5 | +1.7% | −3.9524 to +19.3248 | no |
| HPA replicas, mean | 1.952 | 2.067 | +5.9% | −0.0561 to +0.2859 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0.2 | 1 | +400.0% | −0.5821 to +2.1821 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 45.03 | 46.86 | +4.1% | +0.8751 to +2.7793 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 1505 | +3.4% | −33.4265 to +132.6265 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 154.2 | 198.7 | +28.9% | −6.6523 to +95.6273 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 748.1 | 787.6 | +5.3% | −71.8708 to +150.8708 | no |
| queue: job turnaround, submitted to done, mean (s) | 812.6 | 891 | +9.6% | −16.1233 to +172.8900 | no |
| queue: jobs unfinished at the window's end | 9 | 10.8 | +20.0% | −0.9353 to +4.5353 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.521 | +0.2% | −0.0029 to +0.0129 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.9 | +0.2% | −1.9353 to +3.0388 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.9 | +0.2% | −1.9353 to +3.0388 | no |
| response time (ms), mean | 331 | 133.3 | −59.7% | −340.5893 to −54.8272 | yes: GAIN |
| response time (ms), 95th percentile | 1179 | 230.1 | −80.5% | −1657.9141 to −240.3259 | yes: GAIN |
| response time (ms), 99th percentile | 1654 | 332.9 | −79.9% | −2303.4937 to −338.7955 | yes: GAIN |
| time over the response line (% of samples) | 14.03 | 0.1694 | −98.8% | −24.6591 to −3.0533 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 0.1 | −98.9% | −12.8154 to −4.7846 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.913 | 1088 | +12104.7% | +837.8271 to +1320.0463 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05958 | 0.06012 | +0.9% | −0.0052 to +0.0063 | no |
| CPU used (cores), mean | 1.43 | 1.443 | +0.9% | −0.1255 to +0.1513 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.43 | 1.443 | +0.9% | −0.1255 to +0.1513 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 450.8 | −2.4% | −50.6532 to +28.1085 | no |
| HPA replicas, mean | 2.025 | 1.952 | −3.6% | −0.1796 to +0.0337 | no |
| pods started | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 40.73 | 45.03 | +10.6% | +1.3159 to +7.2899 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772 | 1455 | +88.5% | +605.9512 to +760.8488 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 154.2 | +231193.8% | +114.0411 to +194.2173 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 748.1 | +149520.0% | +597.5479 to +897.6521 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.19 | 812.6 | +939.3% | +628.6701 to +840.1633 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9 | +9.000 (native is 0) | +3.5838 to +14.4162 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.064 | −15.6% | −1.7307 to −0.1419 | yes: GAIN |
| node-hours | 2.516 | 2.123 | −15.6% | −0.7212 to −0.0648 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.5 | +0.1% | −0.6995 to +1.1352 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 243.1 | −10.7% | −54.0517 to −4.4375 | yes: GAIN |
| response time (ms), mean | 331 | 318 | −3.9% | −31.9359 to +5.9942 | no |
| response time (ms), 95th percentile | 1179 | 1284 | +8.9% | +36.6368 to +173.6902 | yes: LOSS |
| response time (ms), 99th percentile | 1654 | 1846 | +11.6% | +12.2810 to +370.7952 | yes: LOSS |
| time over the response line (% of samples) | 14.03 | 14.22 | +1.4% | −0.7171 to +1.1064 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9 | +1.1% | −0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.3 | +142.300 (native is 0) | +80.9084 to +203.6916 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.913 | 10.72 | +20.3% | −0.4293 to +4.0460 | no |
| utilisation (used / allocatable) | 0.05958 | 0.07262 | +21.9% | +0.0020 to +0.0241 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.43 | 1.433 | +0.2% | −0.0341 to +0.0401 | no |
| Omni's own CPU (cores), mean | 0 | 0.07263 | +0.073 (native is 0) | +0.0658 to +0.0795 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.506 | +5.3% | +0.0328 to +0.1185 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 406.8 | −12.0% | −96.3905 to −14.0959 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.469 | +22.0% | +0.1381 to +0.7510 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.4047 to +2.1953 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.8 | +2700.0% | +0.8515 to +4.5485 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.383 | +1283.3% | +0.4000 to +2.1667 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.73 | 43.97 | +8.0% | +2.6516 to +3.8356 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772 | 780.7 | +1.1% | −1.2919 to +18.6919 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.609 | −23.2% | −2.5333 to −0.2491 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 | −18.7% | −0.0524 to +0.0274 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.19 | 86.45 | +10.6% | +0.6507 to +15.8743 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.064 | −15.6% | −1.7307 to −0.1419 | yes: GAIN |
| node-hours | 2.521 | 2.123 | −15.8% | −0.7315 to −0.0645 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.5 | −0.1% | −3.0401 to +2.3723 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 243.1 | −10.9% | −56.1600 to −3.4327 | yes: GAIN |
| response time (ms), mean | 133.3 | 318 | +138.6% | +32.4712 to +337.0036 | yes: LOSS |
| response time (ms), 95th percentile | 230.1 | 1284 | +458.1% | +288.8437 to +1819.7233 | yes: LOSS |
| response time (ms), 99th percentile | 332.9 | 1846 | +454.3% | +400.0144 to +2625.3510 | yes: LOSS |
| time over the response line (% of samples) | 0.1694 | 14.22 | +8294.7% | +3.4881 to +24.6137 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 9 | +8900.0% | +4.7366 to +13.0634 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.3 | +142.300 (native is 0) | +80.9084 to +203.6916 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1088 | 10.72 | −99.0% | −1316.9870 to −837.2696 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06012 | 0.07262 | +20.8% | +0.0025 to +0.0225 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.433 | −0.7% | −0.1663 to +0.1465 | no |
| Omni's own CPU (cores), mean | 0 | 0.07263 | +0.073 (native is 0) | +0.0658 to +0.0795 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.506 | +4.3% | −0.0991 to +0.2246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 406.8 | −9.8% | −81.0091 to −6.9326 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.469 | +26.5% | +0.2686 to +0.7664 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.4047 to +2.1953 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | +0.6280 to +4.5720 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.383 | +591.7% | +0.1388 to +2.2279 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.03 | 43.97 | −2.4% | −4.3727 to +2.2541 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 780.7 | −46.4% | −754.3847 to −595.0153 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 154.2 | 0.05417 | −100.0% | −194.2480 to −114.0353 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 748.1 | 0.3 | −100.0% | −897.7982 to −597.8018 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 812.6 | 86.45 | −89.4% | −827.9214 to −624.3870 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9 | 0 | −100.0% | −14.4162 to −3.5838 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.515 | −0.0% | −0.0099 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.7 | −0.2% | −3.4076 to +2.2773 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.7 | −0.2% | −3.4076 to +2.2773 | no |
| response time (ms), mean | 331 | 109.1 | −67.1% | −367.1508 to −76.7345 | yes: GAIN |
| response time (ms), 95th percentile | 1179 | 241.6 | −79.5% | −1643.0139 to −232.4031 | yes: GAIN |
| response time (ms), 99th percentile | 1654 | 352.5 | −78.7% | −2289.7337 to −313.3997 | yes: GAIN |
| time over the response line (% of samples) | 14.03 | 0.1572 | −98.9% | −24.7335 to −3.0033 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 0.1 | −98.9% | −12.8295 to −4.7705 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93.8 | +93.800 (native is 0) | +84.6037 to +102.9963 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.913 | 1204 | +13402.7% | +992.1738 to +1397.0829 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05958 | 0.05894 | −1.1% | −0.0068 to +0.0055 | no |
| CPU used (cores), mean | 1.43 | 1.415 | −1.1% | −0.1634 to +0.1329 | no |
| Omni's own CPU (cores), mean | 0 | 0.06782 | +0.068 (native is 0) | +0.0602 to +0.0754 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.482 | +3.7% | −0.0885 to +0.1937 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 458.5 | −0.8% | −45.9329 to +38.7606 | no |
| HPA replicas, mean | 2.025 | 2.067 | +2.1% | −0.1442 to +0.2281 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0.1 | 1 | +900.0% | −0.6977 to +2.4977 | no |
| pod start wait, mean (s) | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 40.73 | 46.86 | +15.1% | +2.9485 to +9.3117 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772 | 1505 | +94.9% | +690.6563 to +775.3437 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 198.7 | +297925.0% | +143.4047 to +253.8286 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 787.6 | +157420.0% | +647.1898 to +927.0102 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.19 | 891 | +1039.6% | +726.5386 to +899.0614 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.8 | +10.800 (native is 0) | +5.3440 to +16.2560 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*