# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.14 | 10.17 |
| node-hours | 5.031 | 5.025 | 4.25 | 4.254 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 525.5 | 525.4 | 524.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 525.5 | 466.9 | 467.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 584.6 | 712.9 | 654.7 | 827.9 |
| response time (ms), 95th percentile | 2229 | 3002 | 2614 | 3450 |
| response time (ms), 99th percentile | 2921 | 4117 | 3499 | 4699 |
| time over the response line (% of samples) | 19.7 | 23.92 | 24.15 | 27.61 |
| failed requests (%) | 0.02262 | 0.0987 | 0.03932 | 0.121 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 15.6 | 13.9 | 15.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 227.3 | 54.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 18.13 | 23.56 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.75 | 39.47 | 30.54 | 49.16 |
| utilisation (used / allocatable) | 0.03465 | 0.03459 | 0.04016 | 0.04072 |
| CPU used (cores), mean | 1.663 | 1.66 | 1.625 | 1.625 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05844 | 0.04354 |
| CPU used with Omni's own (cores), mean | 1.663 | 1.66 | 1.684 | 1.668 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.4 | 771.2 | 690.2 | 691.5 |
| HPA replicas, mean | 4.012 | 4.088 | 4.923 | 5.473 |
| pods started | 0.3 | 0.1 | 3.4 | 3.6 |
| pod start wait, total (s) | 0.5 | 0.2 | 9.6 | 10.9 |
| pod start wait, mean (s) | 0.35 | 0.2 | 2.435 | 2.072 |
| host CPU busy, the real machine under kind (%) | 51.5 | 57.42 | 57.26 | 62.57 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 873.9 | 969.8 | 913.7 | 1013 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.378 | 8.955 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 8.55 | 0.1208 | 14.93 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 64.7 | 0.6 | 127.2 |
| queue: job turnaround, submitted to done, mean (s) | 179.6 | 275.4 | 219.3 | 315.1 |
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
| worker nodes in service, mean | 12 | 10.17 | −15.2% | −3.4759 to −0.1824 | yes: GAIN |
| node-hours | 5.025 | 4.254 | −15.3% | −1.4603 to −0.0808 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 524.7 | −0.2% | −4.0737 to +2.4352 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 467.4 | −11.1% | −110.0803 to −6.1956 | yes: GAIN |
| response time (ms), mean | 712.9 | 827.9 | +16.1% | −6.0568 to +236.1585 | no |
| response time (ms), 95th percentile | 3002 | 3450 | +14.9% | −79.4237 to +975.0167 | no |
| response time (ms), 99th percentile | 4117 | 4699 | +14.1% | +14.0228 to +1149.9604 | yes: LOSS |
| time over the response line (% of samples) | 23.92 | 27.61 | +15.4% | +0.0158 to +7.3698 | yes: LOSS |
| failed requests (%) | 0.0987 | 0.121 | +22.6% | −0.2019 to +0.2465 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.6 | 15.7 | +0.6% | −1.5329 to +1.7329 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.8 | +54.800 (native is 0) | +35.1040 to +74.4960 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 39.47 | 49.15 | +24.5% | −25.2174 to +44.5840 | no |
| utilisation (used / allocatable) | 0.03459 | 0.04072 | +17.7% | −0.0005 to +0.0128 | no |
| CPU used (cores), mean | 1.66 | 1.625 | −2.1% | −0.1878 to +0.1168 | no |
| Omni's own CPU (cores), mean | 0 | 0.04354 | +0.044 (native is 0) | +0.0347 to +0.0523 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.66 | 1.668 | +0.5% | −0.1450 to +0.1611 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.2 | 691.5 | −10.3% | −173.2446 to +13.8258 | no |
| HPA replicas, mean | 4.088 | 5.473 | +33.9% | −0.0434 to +2.8137 | no |
| pods started | 0.1 | 3.6 | +3500.0% | +1.5556 to +5.4444 | yes: power given |
| pod start wait, total (s) | 0.2 | 10.9 | +5350.0% | +3.9640 to +17.4360 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.072 | +936.2% | +0.7115 to +3.0332 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.42 | 62.57 | +9.0% | +3.4039 to +6.9052 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 969.8 | 1013 | +4.4% | +8.5149 to +77.4851 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.955 | −25.4% | −5.6092 to −0.4804 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 8.55 | 14.93 | +74.7% | −2.3565 to +15.1232 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 64.7 | 127.2 | +96.6% | −31.3791 to +156.3791 | no |
| queue: job turnaround, submitted to done, mean (s) | 275.4 | 315.1 | +14.4% | +3.4185 to +76.0148 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.031 | 5.025 | −0.1% | −0.0171 to +0.0057 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 525.5 | −0.1% | −2.4697 to +1.5899 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 525.5 | −0.1% | −2.4697 to +1.5899 | no |
| response time (ms), mean | 584.6 | 712.9 | +21.9% | +56.4039 to +200.1645 | yes: LOSS |
| response time (ms), 95th percentile | 2229 | 3002 | +34.7% | +358.1821 to +1188.9369 | yes: LOSS |
| response time (ms), 99th percentile | 2921 | 4117 | +40.9% | +640.2462 to +1751.6462 | yes: LOSS |
| time over the response line (% of samples) | 19.7 | 23.92 | +21.5% | +1.7767 to +6.6733 | yes: LOSS |
| failed requests (%) | 0.02262 | 0.0987 | +336.4% | −0.0413 to +0.1934 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 15.6 | +45.8% | +2.4348 to +7.3652 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.75 | 39.47 | +135.7% | +0.7755 to +44.6678 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03465 | 0.03459 | −0.2% | −0.0013 to +0.0011 | no |
| CPU used (cores), mean | 1.663 | 1.66 | −0.2% | −0.0606 to +0.0549 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.663 | 1.66 | −0.2% | −0.0606 to +0.0549 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.4 | 771.2 | −0.8% | −30.4468 to +17.8870 | no |
| HPA replicas, mean | 4.012 | 4.088 | +1.9% | −0.2251 to +0.3757 | no |
| pods started | 0.3 | 0.1 | −66.7% | −0.7642 to +0.3642 | no |
| pod start wait, total (s) | 0.5 | 0.2 | −60.0% | −1.2567 to +0.6567 | no |
| pod start wait, mean (s) | 0.35 | 0.2 | −42.9% | −0.9049 to +0.6049 | no |
| host CPU busy, the real machine under kind (%) | 51.5 | 57.42 | +11.5% | +4.5881 to +7.2535 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 873.9 | 969.8 | +11.0% | +48.7760 to +143.0240 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 8.55 | +10700.0% | +0.3353 to +16.6064 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 64.7 | +12840.0% | −30.2072 to +158.6072 | no |
| queue: job turnaround, submitted to done, mean (s) | 179.6 | 275.4 | +53.3% | +53.2865 to +138.2969 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.14 | −15.5% | −3.0734 to −0.6451 | yes: GAIN |
| node-hours | 5.031 | 4.25 | −15.5% | −1.2842 to −0.2779 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 525.4 | −0.1% | −2.0332 to +0.9348 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 466.9 | −11.2% | −96.0179 to −21.9889 | yes: GAIN |
| response time (ms), mean | 584.6 | 654.7 | +12.0% | +5.1921 to +135.0137 | yes: LOSS |
| response time (ms), 95th percentile | 2229 | 2614 | +17.3% | +121.6584 to +648.1326 | yes: LOSS |
| response time (ms), 99th percentile | 2921 | 3499 | +19.8% | +123.6224 to +1033.5490 | yes: LOSS |
| time over the response line (% of samples) | 19.7 | 24.15 | +22.6% | +2.8581 to +6.0411 | yes: LOSS |
| failed requests (%) | 0.02262 | 0.03932 | +73.8% | −0.0522 to +0.0856 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 13.9 | +29.9% | +0.5492 to +5.8508 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 227.3 | +227.300 (native is 0) | +70.1602 to +384.4398 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.75 | 30.54 | +82.3% | −2.2827 to +29.8693 | no |
| utilisation (used / allocatable) | 0.03465 | 0.04016 | +15.9% | +0.0006 to +0.0105 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.663 | 1.625 | −2.3% | −0.0854 to +0.0093 | no |
| Omni's own CPU (cores), mean | 0 | 0.05844 | +0.058 (native is 0) | +0.0532 to +0.0636 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.663 | 1.684 | +1.2% | −0.0254 to +0.0662 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.4 | 690.2 | −11.2% | −163.7565 to −10.6462 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.012 | 4.923 | +22.7% | +0.6918 to +1.1290 | yes: power given |
| pods started | 0.3 | 3.4 | +1033.3% | +1.9102 to +4.2898 | yes: power given |
| pod start wait, total (s) | 0.5 | 9.6 | +1820.0% | +4.8823 to +13.3177 | yes: LOSS |
| pod start wait, mean (s) | 0.35 | 2.435 | +595.7% | +1.2556 to +2.9144 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.5 | 57.26 | +11.2% | +4.6192 to +6.9140 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 873.9 | 913.7 | +4.6% | +12.5937 to +67.0063 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.378 | −30.2% | −5.8007 to −1.4439 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.1208 | +52.6% | −0.0242 to +0.1076 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 | +20.0% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 179.6 | 219.3 | +22.1% | +16.6330 to +62.8003 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.14 | −15.5% | −3.0734 to −0.6451 | yes: GAIN |
| node-hours | 5.025 | 4.25 | −15.4% | −1.2830 to −0.2678 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 525.4 | −0.0% | −1.8127 to +1.5941 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 466.9 | −11.1% | −96.6966 to −20.4303 | yes: GAIN |
| response time (ms), mean | 712.9 | 654.7 | −8.2% | −83.2312 to −33.1314 | yes: GAIN |
| response time (ms), 95th percentile | 3002 | 2614 | −12.9% | −704.3825 to −72.9455 | yes: GAIN |
| response time (ms), 99th percentile | 4117 | 3499 | −15.0% | −1038.4898 to −196.2312 | yes: GAIN |
| time over the response line (% of samples) | 23.92 | 24.15 | +0.9% | −2.8219 to +3.2711 | no |
| failed requests (%) | 0.0987 | 0.03932 | −60.2% | −0.1868 to +0.0681 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.6 | 13.9 | −10.9% | −3.5174 to +0.1174 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 227.3 | +227.300 (native is 0) | +70.1602 to +384.4398 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 39.47 | 30.54 | −22.6% | −25.6326 to +7.7760 | no |
| utilisation (used / allocatable) | 0.03459 | 0.04016 | +16.1% | +0.0015 to +0.0097 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.66 | 1.625 | −2.1% | −0.0681 to −0.0023 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05844 | +0.058 (native is 0) | +0.0532 to +0.0636 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.66 | 1.684 | +1.4% | −0.0124 to +0.0589 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.2 | 690.2 | −10.5% | −141.7199 to −20.1230 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.088 | 4.923 | +20.4% | +0.4339 to +1.2363 | yes: power given |
| pods started | 0.1 | 3.4 | +3300.0% | +1.7901 to +4.8099 | yes: power given |
| pod start wait, total (s) | 0.2 | 9.6 | +4700.0% | +4.6648 to +14.1352 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.435 | +1117.5% | +1.3577 to +3.1123 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.42 | 57.26 | −0.3% | −0.8901 to +0.5817 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 969.8 | 913.7 | −5.8% | −80.0493 to −32.1507 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.378 | −30.2% | −5.8007 to −1.4439 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 8.55 | 0.1208 | −98.6% | −16.5600 to −0.2983 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 64.7 | 0.6 | −99.1% | −158.5455 to +30.3455 | no |
| queue: job turnaround, submitted to done, mean (s) | 275.4 | 219.3 | −20.4% | −79.7533 to −32.3967 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.17 | −15.2% | −3.4759 to −0.1824 | yes: GAIN |
| node-hours | 5.031 | 4.254 | −15.4% | −1.4640 to −0.0885 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 524.7 | −0.2% | −4.4038 to +1.8855 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 467.4 | −11.1% | −109.8468 to −7.3090 | yes: GAIN |
| response time (ms), mean | 584.6 | 827.9 | +41.6% | +70.1614 to +416.5087 | yes: LOSS |
| response time (ms), 95th percentile | 2229 | 3450 | +54.8% | +473.3799 to +1969.3321 | yes: LOSS |
| response time (ms), 99th percentile | 2921 | 4699 | +60.9% | +790.5045 to +2765.3711 | yes: LOSS |
| time over the response line (% of samples) | 19.7 | 27.61 | +40.2% | +4.5149 to +11.3208 | yes: LOSS |
| failed requests (%) | 0.02262 | 0.121 | +435.0% | −0.1045 to +0.3013 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 15.7 | +46.7% | +2.4099 to +7.5901 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.8 | +54.800 (native is 0) | +35.1040 to +74.4960 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.75 | 49.15 | +193.5% | −3.7594 to +68.5694 | no |
| utilisation (used / allocatable) | 0.03465 | 0.04072 | +17.5% | −0.0013 to +0.0134 | no |
| CPU used (cores), mean | 1.663 | 1.625 | −2.3% | −0.2032 to +0.1265 | no |
| Omni's own CPU (cores), mean | 0 | 0.04354 | +0.044 (native is 0) | +0.0347 to +0.0523 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.663 | 1.668 | +0.3% | −0.1580 to +0.1684 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.4 | 691.5 | −11.1% | −193.5050 to +21.5263 | no |
| HPA replicas, mean | 4.012 | 5.473 | +36.4% | −0.2071 to +3.1279 | no |
| pods started | 0.3 | 3.6 | +1100.0% | +1.0620 to +5.5380 | yes: power given |
| pod start wait, total (s) | 0.5 | 10.9 | +2080.0% | +3.3172 to +17.4828 | yes: LOSS |
| pod start wait, mean (s) | 0.35 | 2.072 | +492.1% | +0.4278 to +3.0170 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.5 | 62.57 | +21.5% | +8.2736 to +13.8771 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 873.9 | 1013 | +15.9% | +61.4796 to +216.3204 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.955 | −25.4% | −5.6092 to −0.4804 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 14.93 | +18763.2% | −0.5202 to +30.2286 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 127.2 | +25340.0% | +10.2886 to +243.1114 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 179.6 | 315.1 | +75.5% | +61.9571 to +209.0596 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*