# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.89 | 6.461 |
| node-hours | 5.019 | 5.027 | 4.558 | 2.71 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 504.6 | 527.3 | 505.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 504.6 | 492.4 | 331.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 675.6 | 123.9 | 800.8 | 73.86 |
| response time (ms), 95th percentile | 2641 | 171.1 | 3381 | 98.51 |
| response time (ms), 99th percentile | 3541 | 194 | 4375 | 129.3 |
| time over the response line (% of samples) | 24.73 | 0 | 28.25 | 0.003623 |
| failed requests (%) | 0 | 0 | 0.007246 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 0 | 14.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 99.2 | 34.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 10 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.8 | 0 | 20.5 | 0.16 |
| utilisation (used / allocatable) | 0.03581 | 0.006054 | 0.04086 | 0.009638 |
| CPU used (cores), mean | 1.719 | 0.2906 | 1.784 | 0.2481 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05637 | 0.03204 |
| CPU used with Omni's own (cores), mean | 1.719 | 0.2906 | 1.84 | 0.2801 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.4 | 4244 | 671.4 | 3270 |
| HPA replicas, mean | 4.06 | 4.146 | 4.849 | 4.74 |
| pods started | 0.3 | 0.1 | 3.9 | 2.2 |
| pod start wait, total (s) | 0.8 | 0.2 | 10.6 | 3.3 |
| pod start wait, mean (s) | 0.5 | 0.2 | 2.448 | 0.98 |
| host CPU busy, the real machine under kind (%) | 52.48 | 14.73 | 58.67 | 17.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 894.2 | 1506 | 948.6 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.941 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 1159 | 0.1208 | 1161 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1476 | 0.7 | 1477 |
| queue: job turnaround, submitted to done, mean (s) | 201.7 | 1159 | 249.2 | 1161 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |
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
| worker nodes in service, mean | 12 | 6.461 | −46.2% | −6.2003 to −4.8771 | yes: GAIN |
| node-hours | 5.027 | 2.71 | −46.1% | −2.5977 to −2.0365 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 505.3 | +0.1% | −0.5764 to +2.0167 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 331.1 | −34.4% | −194.6547 to −152.2717 | yes: GAIN |
| response time (ms), mean | 123.9 | 73.86 | −40.4% | −58.3589 to −41.6765 | yes: GAIN |
| response time (ms), 95th percentile | 171.1 | 98.51 | −42.4% | −83.8074 to −61.3026 | yes: GAIN |
| response time (ms), 99th percentile | 194 | 129.3 | −33.3% | −74.9123 to −54.3893 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.003623 | +0.004 (native is 0) | −0.0046 to +0.0118 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.200 (native is 0) | +31.2837 to +37.1163 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.16 | +0.160 (native is 0) | −0.0975 to +0.4175 | no |
| utilisation (used / allocatable) | 0.006054 | 0.009638 | +59.2% | +0.0029 to +0.0042 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2906 | 0.2481 | −14.6% | −0.0506 to −0.0344 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03204 | +0.032 (native is 0) | +0.0281 to +0.0360 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2906 | 0.2801 | −3.6% | −0.0200 to −0.0010 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4244 | 3270 | −22.9% | −1112.8302 to −834.6094 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.146 | 4.74 | +14.3% | +0.3727 to +0.8153 | yes: power given |
| pods started | 0.1 | 2.2 | +2100.0% | +0.6914 to +3.5086 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.3 | +1550.0% | +0.8519 to +5.3481 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.98 | +390.0% | +0.2481 to +1.3119 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.73 | 17.75 | +20.5% | +2.5080 to +3.5185 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1507 | +0.1% | −2.6333 to +5.6333 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1161 | +0.1% | −2.9845 to +5.6678 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1477 | +0.1% | −2.9991 to +5.7991 | no |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1161 | +0.1% | −2.9845 to +5.6678 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.019 | 5.027 | +0.2% | −0.0072 to +0.0226 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 504.6 | −4.0% | −24.5703 to −17.7207 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 504.6 | −4.0% | −24.5703 to −17.7207 | yes: GAIN |
| response time (ms), mean | 675.6 | 123.9 | −81.7% | −862.8995 to −240.5063 | yes: GAIN |
| response time (ms), 95th percentile | 2641 | 171.1 | −93.5% | −3887.0355 to −1052.0635 | yes: GAIN |
| response time (ms), 99th percentile | 3541 | 194 | −94.5% | −5228.9091 to −1465.8721 | yes: GAIN |
| time over the response line (% of samples) | 24.73 | 0 | −100.0% | −35.8353 to −13.6254 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 0 | −100.0% | −17.6958 to −7.9042 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.8 | 0 | −100.0% | −23.7357 to −9.8643 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03581 | 0.006054 | −83.1% | −0.0335 to −0.0261 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.719 | 0.2906 | −83.1% | −1.6060 to −1.2504 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.719 | 0.2906 | −83.1% | −1.6060 to −1.2504 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.4 | 4244 | +465.5% | +3029.3635 to +3957.0241 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.06 | 4.146 | +2.1% | −0.1507 to +0.3216 | no |
| pods started | 0.3 | 0.1 | −66.7% | −0.7642 to +0.3642 | no |
| pod start wait, total (s) | 0.8 | 0.2 | −75.0% | −2.1155 to +0.9155 | no |
| pod start wait, mean (s) | 0.5 | 0.2 | −60.0% | −1.2567 to +0.6567 | no |
| host CPU busy, the real machine under kind (%) | 52.48 | 14.73 | −71.9% | −43.1393 to −32.3510 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 894.2 | 1506 | +68.4% | +503.0905 to +720.3095 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 1159 | +897529.0% | +1157.1013 to +1161.5154 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1476 | +184350.0% | +1472.5940 to +1477.0060 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 201.7 | 1159 | +474.8% | +850.9638 to +1064.4779 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | −9.3% | −2.2489 to +0.0263 | no |
| node-hours | 5.019 | 4.558 | −9.2% | −0.9374 to +0.0154 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 527.3 | +0.3% | −0.8135 to +3.9290 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 492.4 | −6.3% | −69.4388 to +2.8086 | no |
| response time (ms), mean | 675.6 | 800.8 | +18.5% | +33.1938 to +217.3149 | yes: LOSS |
| response time (ms), 95th percentile | 2641 | 3381 | +28.0% | +336.4042 to +1144.6088 | yes: LOSS |
| response time (ms), 99th percentile | 3541 | 4375 | +23.6% | +402.4711 to +1265.6419 | yes: LOSS |
| time over the response line (% of samples) | 24.73 | 28.25 | +14.2% | +2.0108 to +5.0287 | yes: LOSS |
| failed requests (%) | 0 | 0.007246 | +0.007 (native is 0) | −0.0091 to +0.0236 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 14.3 | +11.7% | −0.1944 to +3.1944 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.2 | +99.200 (native is 0) | +29.4921 to +168.9079 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.8 | 20.5 | +22.0% | −0.4684 to +7.8751 | no |
| utilisation (used / allocatable) | 0.03581 | 0.04086 | +14.1% | +0.0015 to +0.0086 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.719 | 1.784 | +3.8% | +0.0087 to +0.1210 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05637 | +0.056 (native is 0) | +0.0512 to +0.0615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.719 | 1.84 | +7.1% | +0.0616 to +0.1808 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.4 | 671.4 | −10.5% | −138.1621 to −19.9448 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.06 | 4.849 | +19.4% | +0.4525 to +1.1255 | yes: power given |
| pods started | 0.3 | 3.9 | +1200.0% | +2.0845 to +5.1155 | yes: power given |
| pod start wait, total (s) | 0.8 | 10.6 | +1225.0% | +5.8850 to +13.7150 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 2.448 | +389.7% | +0.7755 to +3.1212 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.48 | 58.67 | +11.8% | +4.8135 to +7.5723 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 894.2 | 948.6 | +6.1% | +23.7127 to +85.0873 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.941 | −17.2% | −3.9644 to −0.1528 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 0.1208 | −6.5% | −0.0676 to +0.0509 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 | −12.5% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 201.7 | 249.2 | +23.6% | +22.2698 to +72.7636 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | −9.3% | −2.2489 to +0.0263 | no |
| node-hours | 5.027 | 4.558 | −9.3% | −0.9472 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 527.3 | +4.5% | +18.8997 to +26.5069 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 492.4 | −2.4% | −50.9677 to +26.6284 | no |
| response time (ms), mean | 123.9 | 800.8 | +546.5% | +280.3962 to +1073.5183 | yes: LOSS |
| response time (ms), 95th percentile | 171.1 | 3381 | +1876.5% | +1399.2713 to +5020.8407 | yes: LOSS |
| response time (ms), 99th percentile | 194 | 4375 | +2155.7% | +1891.8033 to +6471.0909 | yes: LOSS |
| time over the response line (% of samples) | 0 | 28.25 | +28.250 (native is 0) | +16.8837 to +39.6165 | yes: LOSS |
| failed requests (%) | 0 | 0.007246 | +0.007 (native is 0) | −0.0091 to +0.0236 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14.3 | +14.300 (native is 0) | +9.9158 to +18.6842 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.2 | +99.200 (native is 0) | +29.4921 to +168.9079 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 20.5 | +20.503 (native is 0) | +10.1274 to +30.8793 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006054 | 0.04086 | +574.9% | +0.0320 to +0.0376 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2906 | 1.784 | +513.8% | +1.2690 to +1.7171 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05637 | +0.056 (native is 0) | +0.0512 to +0.0615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2906 | 1.84 | +533.2% | +1.3208 to +1.7780 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4244 | 671.4 | −84.2% | −4093.8560 to −3050.6384 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.146 | 4.849 | +17.0% | +0.3735 to +1.0335 | yes: power given |
| pods started | 0.1 | 3.9 | +3800.0% | +2.3379 to +5.2621 | yes: power given |
| pod start wait, total (s) | 0.2 | 10.6 | +5200.0% | +6.2128 to +14.5872 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.448 | +1124.2% | +1.4478 to +3.0489 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.73 | 58.67 | +298.2% | +37.2595 to +50.6168 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 948.6 | −37.0% | −695.4940 to −419.1060 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.1208 | −100.0% | −1161.5501 to −1157.0832 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.7 | −100.0% | −1477.2471 to −1472.5529 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 249.2 | −78.5% | −1040.4552 to −779.9531 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.461 | −46.2% | −6.2003 to −4.8771 | yes: GAIN |
| node-hours | 5.019 | 2.71 | −46.0% | −2.5920 to −2.0268 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 505.3 | −3.9% | −23.5767 to −17.2741 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 331.1 | −37.0% | −215.6130 to −173.6044 | yes: GAIN |
| response time (ms), mean | 675.6 | 73.86 | −89.1% | −919.3887 to −284.0524 | yes: GAIN |
| response time (ms), 95th percentile | 2641 | 98.51 | −96.3% | −3964.0883 to −1120.1207 | yes: GAIN |
| response time (ms), 99th percentile | 3541 | 129.3 | −96.3% | −5293.9066 to −1530.1762 | yes: GAIN |
| time over the response line (% of samples) | 24.73 | 0.003623 | −100.0% | −35.8292 to −13.6243 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 0 | −100.0% | −17.6958 to −7.9042 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.200 (native is 0) | +31.2837 to +37.1163 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.8 | 0.16 | −99.0% | −23.4878 to −9.7922 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03581 | 0.009638 | −73.1% | −0.0296 to −0.0228 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.719 | 0.2481 | −85.6% | −1.6487 to −1.2927 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03204 | +0.032 (native is 0) | +0.0281 to +0.0360 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.719 | 0.2801 | −83.7% | −1.6132 to −1.2642 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.4 | 3270 | +335.7% | +2156.9340 to +2882.0139 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.06 | 4.74 | +16.7% | +0.4119 to +0.9469 | yes: power given |
| pods started | 0.3 | 2.2 | +633.3% | +0.1014 to +3.6986 | yes: power given |
| pod start wait, total (s) | 0.8 | 3.3 | +312.5% | −0.8253 to +5.8253 | no |
| pod start wait, mean (s) | 0.5 | 0.98 | +96.0% | −0.7111 to +1.6711 | no |
| host CPU busy, the real machine under kind (%) | 52.48 | 17.75 | −66.2% | −39.6863 to −29.7776 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 894.2 | 1507 | +68.6% | +506.7055 to +719.6945 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 1161 | +898567.7% | +1158.0255 to +1163.2745 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1477 | +184525.0% | +1473.4031 to +1478.9969 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 201.7 | 1161 | +475.5% | +854.5786 to +1063.5464 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*