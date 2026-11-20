# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.335 | 6 |
| node-hours | 2.518 | 2.514 | 2.239 | 2.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 272.2 | 273.8 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 272.2 | 252.9 | 271.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 419 | 148.2 | 402.7 | 151.8 |
| response time (ms), 95th percentile | 1559 | 258.6 | 1676 | 269.8 |
| response time (ms), 99th percentile | 2267 | 379.9 | 2460 | 392.2 |
| time over the response line (% of samples) | 18.4 | 0.2996 | 18.64 | 0.3788 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.44 | 0.1111 | 11.44 | 0.1111 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 113 | 25.78 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.82 | 1245 | 11.02 | 1324 |
| utilisation (used / allocatable) | 0.06246 | 0.05997 | 0.07058 | 0.05796 |
| CPU used (cores), mean | 1.499 | 1.439 | 1.504 | 1.391 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07741 | 0.0698 |
| CPU used with Omni's own (cores), mean | 1.499 | 1.439 | 1.581 | 1.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.6 | 451.4 | 405.7 | 466.1 |
| HPA replicas, mean | 1.942 | 2.017 | 2.309 | 2.241 |
| pods started | 0 | 0.2222 | 1.111 | 1 |
| pod start wait, total (s) | 0 | 0.5556 | 2.556 | 2.556 |
| pod start wait, mean (s) | 0 | 0.2778 | 1.667 | 0.8519 |
| host CPU busy, the real machine under kind (%) | 43.15 | 45.92 | 46.3 | 47.01 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 796.7 | 1504 | 807.8 | 1511 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.707 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 154.6 | 0.05556 | 199.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 654.2 | 0.3333 | 828.4 |
| queue: job turnaround, submitted to done, mean (s) | 101.7 | 902 | 113 | 927.8 |
| queue: jobs unfinished at the window's end | 0 | 11.56 | 0 | 15.11 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.518 | +0.2% | −0.0043 to +0.0121 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.9 | −0.1% | −1.2786 to +0.7663 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.9 | −0.1% | −1.2786 to +0.7663 | no |
| response time (ms), mean | 148.2 | 151.8 | +2.4% | +0.3802 to +6.7447 | yes: LOSS |
| response time (ms), 95th percentile | 258.6 | 269.8 | +4.3% | +2.6955 to +19.5989 | yes: LOSS |
| response time (ms), 99th percentile | 379.9 | 392.2 | +3.2% | −17.9937 to +42.5115 | no |
| time over the response line (% of samples) | 0.2996 | 0.3788 | +26.5% | −0.1268 to +0.2853 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1111 | 0.1111 | ±0.0% | −0.3843 to +0.3843 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.78 | +25.778 (native is 0) | +21.5715 to +29.9840 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1245 | 1324 | +6.4% | +21.9877 to +136.6049 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05997 | 0.05796 | −3.3% | −0.0039 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.391 | −3.3% | −0.0933 to −0.0030 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0698 | +0.070 (native is 0) | +0.0631 to +0.0765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.461 | +1.5% | −0.0260 to +0.0693 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.4 | 466.1 | +3.2% | +1.2187 to +28.1164 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.017 | 2.241 | +11.1% | −0.0266 to +0.4740 | no |
| pods started | 0.2222 | 1 | +350.0% | −0.5961 to +2.1516 | no |
| pod start wait, total (s) | 0.5556 | 2.556 | +360.0% | −1.5014 to +5.5014 | no |
| pod start wait, mean (s) | 0.2778 | 0.8519 | +206.7% | −0.7279 to +1.8760 | no |
| host CPU busy, the real machine under kind (%) | 45.92 | 47.01 | +2.4% | +0.1459 to +2.0381 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1504 | 1511 | +0.5% | −8.8239 to +24.1572 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 154.6 | 199.5 | +29.0% | +7.1976 to +82.5246 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 654.2 | 828.4 | +26.6% | +50.0750 to +298.3695 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 902 | 927.8 | +2.9% | −43.2163 to +94.6978 | no |
| queue: jobs unfinished at the window's end | 11.56 | 15.11 | +30.8% | −0.2707 to +7.3818 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.514 | −0.1% | −0.0153 to +0.0083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 272.2 | −0.5% | −5.0469 to +2.1192 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 272.2 | −0.5% | −5.0469 to +2.1192 | no |
| response time (ms), mean | 419 | 148.2 | −64.6% | −439.3945 to −102.1778 | yes: GAIN |
| response time (ms), 95th percentile | 1559 | 258.6 | −83.4% | −2120.4749 to −480.2762 | yes: GAIN |
| response time (ms), 99th percentile | 2267 | 379.9 | −83.2% | −3083.7265 to −691.0773 | yes: GAIN |
| time over the response line (% of samples) | 18.4 | 0.2996 | −98.4% | −29.6959 to −6.5097 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.44 | 0.1111 | −98.9% | −14.0990 to −6.5677 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.82 | 1245 | +11406.4% | +979.7129 to +1487.8760 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06246 | 0.05997 | −4.0% | −0.0099 to +0.0049 | no |
| CPU used (cores), mean | 1.499 | 1.439 | −4.0% | −0.2380 to +0.1183 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.499 | 1.439 | −4.0% | −0.2380 to +0.1183 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.6 | 451.4 | +1.8% | −42.4669 to +58.1628 | no |
| HPA replicas, mean | 1.942 | 2.017 | +3.9% | −0.0617 to +0.2124 | no |
| pods started | 0 | 0.2222 | +0.222 (native is 0) | −0.2902 to +0.7347 | no |
| pod start wait, total (s) | 0 | 0.5556 | +0.556 (native is 0) | −0.7256 to +1.8367 | no |
| pod start wait, mean (s) | 0 | 0.2778 | +0.278 (native is 0) | −0.3628 to +0.9183 | no |
| host CPU busy, the real machine under kind (%) | 43.15 | 45.92 | +6.4% | −1.1135 to +6.6451 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.7 | 1504 | +88.7% | +656.1125 to +757.8875 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 154.6 | +417362.5% | +113.8534 to +195.3040 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 654.2 | +196166.7% | +489.2392 to +818.5386 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 101.7 | 902 | +787.2% | +717.1451 to +883.5586 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.56 | +11.556 (native is 0) | +4.7007 to +18.4104 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.335 | −11.1% | −1.2072 to −0.1230 | yes: GAIN |
| node-hours | 2.518 | 2.239 | −11.1% | −0.5028 to −0.0559 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 | +0.1% | −0.5184 to +0.9398 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 252.9 | −7.6% | −37.5308 to −3.9460 | yes: GAIN |
| response time (ms), mean | 419 | 402.7 | −3.9% | −36.8853 to +4.2671 | no |
| response time (ms), 95th percentile | 1559 | 1676 | +7.5% | +23.8079 to +210.2365 | yes: LOSS |
| response time (ms), 99th percentile | 2267 | 2460 | +8.5% | −33.7265 to +419.4159 | no |
| time over the response line (% of samples) | 18.4 | 18.64 | +1.3% | −0.2842 to +0.7594 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.44 | 11.44 | +9.6% | −0.2154 to +2.2154 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 | +113.000 (native is 0) | +38.2850 to +187.7150 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.82 | 11.02 | +1.8% | −1.8249 to +2.2249 | no |
| utilisation (used / allocatable) | 0.06246 | 0.07058 | +13.0% | +0.0023 to +0.0139 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.499 | 1.504 | +0.3% | −0.0211 to +0.0306 | no |
| Omni's own CPU (cores), mean | 0 | 0.07741 | +0.077 (native is 0) | +0.0726 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.499 | 1.581 | +5.5% | +0.0544 to +0.1100 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.6 | 405.7 | −8.5% | −65.5324 to −10.1387 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.309 | +18.9% | +0.0756 to +0.6595 | yes: power given |
| pods started | 0 | 1.111 | +1.111 (native is 0) | +0.3978 to +1.8244 | yes: power given |
| pod start wait, total (s) | 0 | 2.556 | +2.556 (native is 0) | +0.4466 to +4.6645 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.667 | +1.667 (native is 0) | +0.8073 to +2.5261 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.15 | 46.3 | +7.3% | +2.7134 to +3.5883 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.7 | 807.8 | +1.4% | +3.0911 to +19.1311 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.707 | −21.6% | −2.3138 to −0.2729 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 0.05556 | +50.0% | −0.0271 to +0.0641 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 0.3333 | ±0.0% | −0.5435 to +0.5435 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.7 | 113 | +11.2% | +3.2694 to +19.4806 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.335 | −11.1% | −1.2072 to −0.1230 | yes: GAIN |
| node-hours | 2.514 | 2.239 | −11.0% | −0.5047 to −0.0469 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 273.8 | +0.6% | −1.8818 to +5.2308 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 252.9 | −7.1% | −38.7841 to +0.2351 | no |
| response time (ms), mean | 148.2 | 402.7 | +171.7% | +73.8454 to +435.1086 | yes: LOSS |
| response time (ms), 95th percentile | 258.6 | 1676 | +548.1% | +528.9063 to +2305.8892 | yes: LOSS |
| response time (ms), 99th percentile | 379.9 | 2460 | +547.6% | +759.5995 to +3400.8936 | yes: LOSS |
| time over the response line (% of samples) | 0.2996 | 18.64 | +6122.6% | +6.8490 to +29.8317 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1111 | 11.44 | +10200.0% | +7.8743 to +14.7923 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 | +113.000 (native is 0) | +38.2850 to +187.7150 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1245 | 11.02 | −99.1% | −1486.7659 to −980.4230 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05997 | 0.07058 | +17.7% | +0.0048 to +0.0164 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.504 | +4.5% | −0.1259 to +0.2550 | no |
| Omni's own CPU (cores), mean | 0 | 0.07741 | +0.077 (native is 0) | +0.0726 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.581 | +9.9% | −0.0525 to +0.3365 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.4 | 405.7 | −10.1% | −77.8549 to −13.5121 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.017 | 2.309 | +14.5% | −0.0185 to +0.6029 | no |
| pods started | 0.2222 | 1.111 | +400.0% | −0.1597 to +1.9375 | no |
| pod start wait, total (s) | 0.5556 | 2.556 | +360.0% | −0.8243 to +4.8243 | no |
| pod start wait, mean (s) | 0.2778 | 1.667 | +500.0% | +0.0606 to +2.7172 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.92 | 46.3 | +0.8% | −3.7786 to +4.5487 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1504 | 807.8 | −46.3% | −753.5215 to −638.2563 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.5 | −58.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 154.6 | 0.05556 | −100.0% | −195.2618 to −113.8586 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 654.2 | 0.3333 | −99.9% | −818.4471 to −489.3307 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 902 | 113 | −87.5% | −866.3735 to −711.5802 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.56 | 0 | −100.0% | −18.4104 to −4.7007 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.518 | +0.0% | −0.0099 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 271.9 | −0.6% | −4.9499 to +1.5099 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 271.9 | −0.6% | −4.9499 to +1.5099 | no |
| response time (ms), mean | 419 | 151.8 | −63.8% | −434.2701 to −100.1773 | yes: GAIN |
| response time (ms), 95th percentile | 1559 | 269.8 | −82.7% | −2103.9630 to −474.4936 | yes: GAIN |
| response time (ms), 99th percentile | 2267 | 392.2 | −82.7% | −3061.4321 to −688.8539 | yes: GAIN |
| time over the response line (% of samples) | 18.4 | 0.3788 | −97.9% | −29.5701 to −6.4770 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.44 | 0.1111 | −98.9% | −14.0794 to −6.5873 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.78 | +25.778 (native is 0) | +21.5715 to +29.9840 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.82 | 1324 | +12139.5% | +1104.1039 to +1522.0775 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06246 | 0.05796 | −7.2% | −0.0116 to +0.0026 | no |
| CPU used (cores), mean | 1.499 | 1.391 | −7.2% | −0.2776 to +0.0616 | no |
| Omni's own CPU (cores), mean | 0 | 0.0698 | +0.070 (native is 0) | +0.0631 to +0.0765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.499 | 1.461 | −2.5% | −0.2015 to +0.1251 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.6 | 466.1 | +5.1% | −25.6041 to +70.6351 | no |
| HPA replicas, mean | 1.942 | 2.241 | +15.4% | +0.0517 to +0.5463 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | −0.1530 to +2.1530 | no |
| pod start wait, total (s) | 0 | 2.556 | +2.556 (native is 0) | −0.3993 to +5.5105 | no |
| pod start wait, mean (s) | 0 | 0.8519 | +0.852 (native is 0) | −0.1331 to +1.8368 | no |
| host CPU busy, the real machine under kind (%) | 43.15 | 47.01 | +8.9% | +0.0196 to +7.6959 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.7 | 1511 | +89.7% | +659.9481 to +769.3853 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 199.5 | +538487.5% | +147.0491 to +251.8306 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 828.4 | +248433.3% | +639.2534 to +1016.9688 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 101.7 | 927.8 | +812.5% | +771.7017 to +880.4834 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.11 | +15.111 (native is 0) | +10.2733 to +19.9489 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*