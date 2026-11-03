# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.19 | 6.179 |
| node-hours | 5.023 | 5.029 | 4.698 | 2.591 |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 504.9 | 529.1 | 505.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 504.9 | 503.7 | 322.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 765 | 130.4 | 965.6 | 75.84 |
| response time (ms), 95th percentile | 3083 | 180.6 | 4001 | 98.32 |
| response time (ms), 99th percentile | 4128 | 205.7 | 5217 | 133 |
| time over the response line (% of samples) | 28.89 | 0 | 32.96 | 0 |
| failed requests (%) | 0 | 0 | 0.02445 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 0 | 15.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 113.9 | 34.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 14.09 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.81 | 0.05167 | 36.45 | 0.08333 |
| utilisation (used / allocatable) | 0.03699 | 0.006286 | 0.04058 | 0.01019 |
| CPU used (cores), mean | 1.776 | 0.3017 | 1.813 | 0.252 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05815 | 0.03281 |
| CPU used with Omni's own (cores), mean | 1.776 | 0.3017 | 1.871 | 0.2849 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.3 | 4054 | 671.9 | 3108 |
| HPA replicas, mean | 4.064 | 4.287 | 5.11 | 4.631 |
| pods started | 0 | 0.4 | 3.3 | 1.8 |
| pod start wait, total (s) | 0 | 0.8 | 8.3 | 2.6 |
| pod start wait, mean (s) | 0 | 0.6 | 2.102 | 1.033 |
| host CPU busy, the real machine under kind (%) | 54.39 | 15.1 | 61.72 | 18.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 926.1 | 1507 | 1003 | 1509 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.51 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 1160 | 0.175 | 1162 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | 1 | 1478 |
| queue: job turnaround, submitted to done, mean (s) | 233 | 1160 | 304.3 | 1162 |
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
| worker nodes in service, mean | 12 | 6.179 | −48.5% | −5.8847 to −5.7578 | yes: GAIN |
| node-hours | 5.029 | 2.591 | −48.5% | −2.4710 to −2.4037 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.9 | 505.5 | +0.1% | −0.7314 to +1.9347 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.9 | 322.4 | −36.1% | −185.3239 to −179.6727 | yes: GAIN |
| response time (ms), mean | 130.4 | 75.84 | −41.8% | −61.7616 to −47.3245 | yes: GAIN |
| response time (ms), 95th percentile | 180.6 | 98.32 | −45.5% | −93.0295 to −71.4625 | yes: GAIN |
| response time (ms), 99th percentile | 205.7 | 133 | −35.3% | −83.5111 to −61.9041 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.100 (native is 0) | +31.8018 to +36.3982 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.08333 | +61.3% | −0.1396 to +0.2029 | no |
| utilisation (used / allocatable) | 0.006286 | 0.01019 | +62.1% | +0.0035 to +0.0043 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3017 | 0.252 | −16.5% | −0.0551 to −0.0443 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03281 | +0.033 (native is 0) | +0.0294 to +0.0362 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3017 | 0.2849 | −5.6% | −0.0220 to −0.0118 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4054 | 3108 | −23.3% | −1027.6221 to −864.1011 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.287 | 4.631 | +8.0% | +0.1532 to +0.5349 | yes: power given |
| pods started | 0.4 | 1.8 | +350.0% | +0.3231 to +2.4769 | yes: power given |
| pod start wait, total (s) | 0.8 | 2.6 | +225.0% | +0.1208 to +3.4792 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.033 | +72.2% | −0.4715 to +1.3381 | no |
| host CPU busy, the real machine under kind (%) | 15.1 | 18.06 | +19.6% | +2.5101 to +3.3987 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1509 | +0.1% | −0.9987 to +5.1987 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1162 | +0.2% | −1.1974 to +4.8640 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1478 | +0.1% | −1.2122 to +4.8122 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1162 | +0.2% | −1.1974 to +4.8640 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.023 | 5.029 | +0.1% | −0.0057 to +0.0170 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 504.9 | −4.2% | −25.3861 to −18.8052 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 504.9 | −4.2% | −25.3861 to −18.8052 | yes: GAIN |
| response time (ms), mean | 765 | 130.4 | −83.0% | −919.8085 to −349.4145 | yes: GAIN |
| response time (ms), 95th percentile | 3083 | 180.6 | −94.1% | −4225.2750 to −1579.6570 | yes: GAIN |
| response time (ms), 99th percentile | 4128 | 205.7 | −95.0% | −5710.7851 to −2134.1537 | yes: GAIN |
| time over the response line (% of samples) | 28.89 | 0 | −100.0% | −38.0980 to −19.6859 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 0 | −100.0% | −18.2771 to −10.5229 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.81 | 0.05167 | −99.8% | −30.4214 to −11.0953 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03699 | 0.006286 | −83.0% | −0.0342 to −0.0272 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.776 | 0.3017 | −83.0% | −1.6428 to −1.3050 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.776 | 0.3017 | −83.0% | −1.6428 to −1.3050 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.3 | 4054 | +458.9% | +2997.7956 to +3659.9273 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.064 | 4.287 | +5.5% | +0.1439 to +0.3026 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.2003 to +1.8003 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| host CPU busy, the real machine under kind (%) | 54.39 | 15.1 | −72.2% | −44.0820 to −34.4816 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 926.1 | 1507 | +62.7% | +479.7326 to +681.2674 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 1160 | +1265309.1% | +1158.1213 to +1161.6121 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1476 | +245916.7% | +1473.8056 to +1477.1944 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 233 | 1160 | +397.8% | +828.2012 to +1025.7238 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.19 | −6.7% | −2.0034 to +0.3923 | no |
| node-hours | 5.023 | 4.698 | −6.5% | −0.8258 to +0.1759 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 529.1 | +0.4% | +0.6835 to +3.5735 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 503.7 | −4.4% | −60.9718 to +14.4371 | no |
| response time (ms), mean | 765 | 965.6 | +26.2% | +58.9694 to +342.2405 | yes: LOSS |
| response time (ms), 95th percentile | 3083 | 4001 | +29.8% | +431.5352 to +1403.7808 | yes: LOSS |
| response time (ms), 99th percentile | 4128 | 5217 | +26.4% | +451.9022 to +1725.4074 | yes: LOSS |
| time over the response line (% of samples) | 28.89 | 32.96 | +14.1% | +1.6314 to +6.5032 | yes: LOSS |
| failed requests (%) | 0 | 0.02445 | +0.024 (native is 0) | −0.0038 to +0.0527 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 15.6 | +8.3% | +0.2583 to +2.1417 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.9 | +113.900 (native is 0) | +62.0004 to +165.7996 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.81 | 36.45 | +75.2% | −8.2446 to +39.5312 | no |
| utilisation (used / allocatable) | 0.03699 | 0.04058 | +9.7% | −0.0005 to +0.0077 | no |
| CPU used (cores), mean | 1.776 | 1.813 | +2.1% | −0.0454 to +0.1200 | no |
| Omni's own CPU (cores), mean | 0 | 0.05815 | +0.058 (native is 0) | +0.0530 to +0.0633 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.776 | 1.871 | +5.4% | +0.0120 to +0.1788 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.3 | 671.9 | −7.4% | −119.0215 to +12.1150 | no |
| HPA replicas, mean | 4.064 | 5.11 | +25.7% | +0.7672 to +1.3235 | yes: power given |
| pods started | 0 | 3.3 | +3.300 (native is 0) | +1.6811 to +4.9189 | yes: power given |
| pod start wait, total (s) | 0 | 8.3 | +8.300 (native is 0) | +3.2527 to +13.3473 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.102 | +2.102 (native is 0) | +1.2597 to +2.9451 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.39 | 61.72 | +13.5% | +5.1096 to +9.5581 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 926.1 | 1003 | +8.3% | +32.4213 to +121.9787 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.51 | −12.4% | −3.5894 to +0.6173 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.175 | +90.9% | −0.0317 to +0.1983 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1 | +66.7% | −0.2032 to +1.0032 | no |
| queue: job turnaround, submitted to done, mean (s) | 233 | 304.3 | +30.6% | +27.6316 to +114.9184 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.19 | −6.7% | −2.0034 to +0.3923 | no |
| node-hours | 5.029 | 4.698 | −6.6% | −0.8356 to +0.1743 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.9 | 529.1 | +4.8% | +20.8729 to +27.5753 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.9 | 503.7 | −0.2% | −41.3969 to +39.0535 | no |
| response time (ms), mean | 130.4 | 965.6 | +640.6% | +435.2545 to +1235.1784 | yes: LOSS |
| response time (ms), 95th percentile | 180.6 | 4001 | +2115.6% | +2094.4686 to +5545.7794 | yes: LOSS |
| response time (ms), 99th percentile | 205.7 | 5217 | +2436.0% | +2785.8608 to +7236.3876 | yes: LOSS |
| time over the response line (% of samples) | 0 | 32.96 | +32.959 (native is 0) | +22.8462 to +43.0722 | yes: LOSS |
| failed requests (%) | 0 | 0.02445 | +0.024 (native is 0) | −0.0038 to +0.0527 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 15.6 | +15.600 (native is 0) | +11.1623 to +20.0377 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.9 | +113.900 (native is 0) | +62.0004 to +165.7996 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 36.45 | +70454.8% | +3.9402 to +68.8631 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006286 | 0.04058 | +545.6% | +0.0311 to +0.0375 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3017 | 1.813 | +500.8% | +1.3009 to +1.7214 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05815 | +0.058 (native is 0) | +0.0530 to +0.0633 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3017 | 1.871 | +520.1% | +1.3553 to +1.7834 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4054 | 671.9 | −83.4% | −3771.2163 to −2993.4132 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.287 | 5.11 | +19.2% | +0.5852 to +1.0590 | yes: power given |
| pods started | 0.4 | 3.3 | +725.0% | +1.1014 to +4.6986 | yes: power given |
| pod start wait, total (s) | 0.8 | 8.3 | +937.5% | +2.2625 to +12.7375 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.102 | +250.4% | +0.3477 to +2.6571 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.1 | 61.72 | +308.6% | +40.0376 to +53.1938 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1003 | −33.4% | −640.5595 to −366.0405 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.175 | −100.0% | −1161.5919 to −1157.9748 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1 | −99.9% | −1477.0502 to −1473.1498 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 304.3 | −73.8% | −988.0529 to −723.3221 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.179 | −48.5% | −5.8847 to −5.7578 | yes: GAIN |
| node-hours | 5.023 | 2.591 | −48.4% | −2.4609 to −2.4024 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 505.5 | −4.1% | −23.7887 to −19.1993 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 322.4 | −38.8% | −206.6851 to −202.5028 | yes: GAIN |
| response time (ms), mean | 765 | 75.84 | −90.1% | −980.0433 to −398.2658 | yes: GAIN |
| response time (ms), 95th percentile | 3083 | 98.32 | −96.8% | −4311.9189 to −1657.5051 | yes: GAIN |
| response time (ms), 99th percentile | 4128 | 133 | −96.8% | −5784.1978 to −2206.1562 | yes: GAIN |
| time over the response line (% of samples) | 28.89 | 0 | −100.0% | −38.0980 to −19.6859 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 0 | −100.0% | −18.2771 to −10.5229 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.100 (native is 0) | +31.8018 to +36.3982 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.81 | 0.08333 | −99.6% | −30.3586 to −11.0947 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03699 | 0.01019 | −72.5% | −0.0300 to −0.0236 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.776 | 0.252 | −85.8% | −1.6945 to −1.3527 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03281 | +0.033 (native is 0) | +0.0294 to +0.0362 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.776 | 0.2849 | −84.0% | −1.6583 to −1.3232 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.3 | 3108 | +328.5% | +2108.2995 to +2657.7003 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.064 | 4.631 | +14.0% | +0.3964 to +0.7382 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.8583 to +2.7417 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +1.2854 to +3.9146 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.033 | +1.033 (native is 0) | +0.5037 to +1.5629 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.39 | 18.06 | −66.8% | −40.7547 to −31.9001 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 926.1 | 1509 | +62.9% | +483.8000 to +681.4000 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 1162 | +1267309.1% | +1159.8079 to +1163.5921 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1478 | +246216.7% | +1475.4515 to +1479.1485 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 233 | 1162 | +398.6% | +832.0207 to +1025.5710 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*