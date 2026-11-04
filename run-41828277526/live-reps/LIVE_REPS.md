# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.92 | 6.336 |
| node-hours | 5.032 | 5.025 | 4.571 | 2.656 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 504.5 | 527 | 505.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 504.5 | 492.9 | 327.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 760.4 | 127.8 | 857.7 | 74.78 |
| response time (ms), 95th percentile | 3024 | 175 | 3616 | 98.8 |
| response time (ms), 99th percentile | 4046 | 208.4 | 4772 | 133.4 |
| time over the response line (% of samples) | 27.13 | 0 | 29.93 | 0.00361 |
| failed requests (%) | 0 | 0 | 0.02242 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 0 | 14.8 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 120.6 | 34.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 27.5 | 95 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.77 | 0.02667 | 33.58 | 0 |
| utilisation (used / allocatable) | 0.03654 | 0.006277 | 0.04041 | 0.009949 |
| CPU used (cores), mean | 1.754 | 0.3013 | 1.768 | 0.2527 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05939 | 0.03287 |
| CPU used with Omni's own (cores), mean | 1.754 | 0.3013 | 1.827 | 0.2855 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.2 | 4083 | 679.1 | 3157 |
| HPA replicas, mean | 3.97 | 4.152 | 4.703 | 4.668 |
| pods started | 0.2 | 0.2 | 2.3 | 2.7 |
| pod start wait, total (s) | 0.5 | 0.3 | 5.3 | 4.3 |
| pod start wait, mean (s) | 0.5 | 0.3 | 1.592 | 1.465 |
| host CPU busy, the real machine under kind (%) | 54.39 | 15.56 | 60.52 | 18.49 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 929.4 | 1505 | 981.1 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.01 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 1158 | 0.125 | 1160 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | 0.8 | 1477 |
| queue: job turnaround, submitted to done, mean (s) | 238.8 | 1158 | 276.1 | 1160 |
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
| worker nodes in service, mean | 12 | 6.336 | −47.2% | −5.9411 to −5.3868 | yes: GAIN |
| node-hours | 5.025 | 2.656 | −47.2% | −2.4898 to −2.2495 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 505.1 | +0.1% | −0.5250 to +1.7693 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 327.1 | −35.2% | −186.5663 to −168.2811 | yes: GAIN |
| response time (ms), mean | 127.8 | 74.78 | −41.5% | −64.0420 to −41.9784 | yes: GAIN |
| response time (ms), 95th percentile | 175 | 98.8 | −43.5% | −91.4391 to −60.8719 | yes: GAIN |
| response time (ms), 99th percentile | 208.4 | 133.4 | −36.0% | −90.9259 to −59.1531 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.00361 | +0.004 (native is 0) | −0.0046 to +0.0118 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.300 (native is 0) | +32.1134 to +36.4866 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0 | −100.0% | −0.0870 to +0.0337 | no |
| utilisation (used / allocatable) | 0.006277 | 0.009949 | +58.5% | +0.0033 to +0.0040 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3013 | 0.2527 | −16.1% | −0.0583 to −0.0389 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03287 | +0.033 (native is 0) | +0.0294 to +0.0363 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3013 | 0.2855 | −5.2% | −0.0245 to −0.0070 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4083 | 3157 | −22.7% | −1063.3282 to −788.8389 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.152 | 4.668 | +12.4% | +0.2278 to +0.8043 | yes: power given |
| pods started | 0.2 | 2.7 | +1250.0% | +1.0995 to +3.9005 | yes: power given |
| pod start wait, total (s) | 0.3 | 4.3 | +1333.3% | +1.3024 to +6.6976 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.465 | +388.3% | +0.3079 to +2.0221 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.56 | 18.49 | +18.8% | +2.5607 to +3.2955 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 1507 | +0.1% | −2.8622 to +6.6622 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 1160 | +0.2% | −2.8768 to +6.8018 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1477 | +0.1% | −2.9443 to +6.9443 | no |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 1160 | +0.2% | −2.8768 to +6.8018 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.032 | 5.025 | −0.1% | −0.0220 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 504.5 | −4.4% | −26.9165 to −19.0752 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 504.5 | −4.4% | −26.9165 to −19.0752 | yes: GAIN |
| response time (ms), mean | 760.4 | 127.8 | −83.2% | −935.1640 to −329.9663 | yes: GAIN |
| response time (ms), 95th percentile | 3024 | 175 | −94.2% | −4227.6173 to −1470.7837 | yes: GAIN |
| response time (ms), 99th percentile | 4046 | 208.4 | −94.8% | −5670.1148 to −2005.3852 | yes: GAIN |
| time over the response line (% of samples) | 27.13 | 0 | −100.0% | −38.6033 to −15.6501 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 0 | −100.0% | −17.9516 to −8.8484 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.77 | 0.02667 | −99.9% | −29.9495 to −11.5272 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03654 | 0.006277 | −82.8% | −0.0342 to −0.0263 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.754 | 0.3013 | −82.8% | −1.6432 to −1.2624 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.754 | 0.3013 | −82.8% | −1.6432 to −1.2624 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.2 | 4083 | +451.6% | +2958.0895 to +3727.1757 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.97 | 4.152 | +4.6% | −0.0225 to +0.3851 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.5 | 0.3 | −40.0% | −1.2003 to +0.8003 | no |
| pod start wait, mean (s) | 0.5 | 0.3 | −40.0% | −1.2003 to +0.8003 | no |
| host CPU busy, the real machine under kind (%) | 54.39 | 15.56 | −71.4% | −44.1739 to −33.4740 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 929.4 | 1505 | +61.9% | +470.1233 to +681.2767 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 1158 | +1263695.5% | +1155.4053 to +1161.3697 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | +245683.3% | +1471.1134 to +1477.0866 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 238.8 | 1158 | +385.1% | +814.4796 to +1024.8871 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.92 | −9.0% | −2.3335 to +0.1692 | no |
| node-hours | 5.032 | 4.571 | −9.2% | −0.9772 to +0.0538 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527 | −0.1% | −2.2962 to +1.3156 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 492.9 | −6.5% | −73.1274 to +4.0427 | no |
| response time (ms), mean | 760.4 | 857.7 | +12.8% | −7.7331 to +202.3420 | no |
| response time (ms), 95th percentile | 3024 | 3616 | +19.6% | +13.5263 to +1169.4707 | yes: LOSS |
| response time (ms), 99th percentile | 4046 | 4772 | +17.9% | +49.3697 to +1402.2751 | yes: LOSS |
| time over the response line (% of samples) | 27.13 | 29.93 | +10.3% | +0.8387 to +4.7618 | yes: LOSS |
| failed requests (%) | 0 | 0.02242 | +0.022 (native is 0) | −0.0132 to +0.0581 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.8 | +10.4% | +0.5604 to +2.2396 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 120.6 | +120.600 (native is 0) | +66.6048 to +174.5952 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.77 | 33.58 | +61.7% | −11.6892 to +37.3125 | no |
| utilisation (used / allocatable) | 0.03654 | 0.04041 | +10.6% | −0.0008 to +0.0085 | no |
| CPU used (cores), mean | 1.754 | 1.768 | +0.8% | −0.1206 to +0.1481 | no |
| Omni's own CPU (cores), mean | 0 | 0.05939 | +0.059 (native is 0) | +0.0545 to +0.0643 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.754 | 1.827 | +4.2% | −0.0614 to +0.2077 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.2 | 679.1 | −8.3% | −146.5919 to +24.3297 | no |
| HPA replicas, mean | 3.97 | 4.703 | +18.5% | +0.3951 to +1.0712 | yes: power given |
| pods started | 0.2 | 2.3 | +1050.0% | +1.0634 to +3.1366 | yes: power given |
| pod start wait, total (s) | 0.5 | 5.3 | +960.0% | +2.2364 to +7.3636 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.592 | +218.3% | +0.2327 to +1.9506 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.39 | 60.52 | +11.3% | +4.7786 to +7.4957 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 929.4 | 981.1 | +5.6% | +20.1218 to +83.2782 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.01 | −16.6% | −3.9902 to +0.0145 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.125 | +36.4% | −0.0292 to +0.0959 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 238.8 | 276.1 | +15.6% | +10.4957 to +64.0876 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.92 | −9.0% | −2.3335 to +0.1692 | no |
| node-hours | 5.025 | 4.571 | −9.0% | −0.9758 to +0.0664 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 527 | +4.5% | +18.8021 to +26.2090 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 492.9 | −2.3% | −53.5841 to +30.4910 | no |
| response time (ms), mean | 127.8 | 857.7 | +571.2% | +360.4983 to +1099.2407 | yes: LOSS |
| response time (ms), 95th percentile | 175 | 3616 | +1966.6% | +1734.7736 to +5146.6244 | yes: LOSS |
| response time (ms), 99th percentile | 208.4 | 4772 | +2189.4% | +2379.8167 to +6747.3281 | yes: LOSS |
| time over the response line (% of samples) | 0 | 29.93 | +29.927 (native is 0) | +18.3072 to +41.5466 | yes: LOSS |
| failed requests (%) | 0 | 0.02242 | +0.022 (native is 0) | −0.0132 to +0.0581 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14.8 | +14.800 (native is 0) | +10.2285 to +19.3715 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 120.6 | +120.600 (native is 0) | +66.6048 to +174.5952 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 33.58 | +125812.5% | +7.3866 to +59.7134 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006277 | 0.04041 | +543.7% | +0.0314 to +0.0369 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3013 | 1.768 | +486.8% | +1.2325 to +1.7006 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05939 | +0.059 (native is 0) | +0.0545 to +0.0643 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3013 | 1.827 | +506.5% | +1.2895 to +1.7625 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4083 | 679.1 | −83.4% | −3847.3731 to −2960.1544 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.152 | 4.703 | +13.3% | +0.2653 to +0.8385 | yes: power given |
| pods started | 0.2 | 2.3 | +1050.0% | +0.8182 to +3.3818 | yes: power given |
| pod start wait, total (s) | 0.3 | 5.3 | +1666.7% | +1.9280 to +8.0720 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.592 | +430.6% | +0.2882 to +2.2951 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.56 | 60.52 | +288.9% | +38.4851 to +51.4371 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 981.1 | −34.8% | −656.2190 to −391.7810 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 0.125 | −100.0% | −1161.3562 to −1155.3522 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.8 | −99.9% | −1476.9987 to −1470.8013 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 276.1 | −76.2% | −1007.0267 to −757.7566 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.336 | −47.2% | −5.9411 to −5.3868 | yes: GAIN |
| node-hours | 5.032 | 2.656 | −47.2% | −2.4888 to −2.2644 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 505.1 | −4.2% | −25.7439 to −19.0035 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 327.1 | −38.0% | −208.1896 to −192.6495 | yes: GAIN |
| response time (ms), mean | 760.4 | 74.78 | −90.2% | −998.3265 to −372.8241 | yes: GAIN |
| response time (ms), 95th percentile | 3024 | 98.8 | −96.7% | −4315.3904 to −1535.3216 | yes: GAIN |
| response time (ms), 99th percentile | 4046 | 133.4 | −96.7% | −5755.1834 to −2070.3956 | yes: GAIN |
| time over the response line (% of samples) | 27.13 | 0.00361 | −100.0% | −38.5981 to −15.6481 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 0 | −100.0% | −17.9516 to −8.8484 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.300 (native is 0) | +32.1134 to +36.4866 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.77 | 0 | −100.0% | −29.9528 to −11.5772 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03654 | 0.009949 | −72.8% | −0.0303 to −0.0229 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.754 | 0.2527 | −85.6% | −1.6942 to −1.3087 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03287 | +0.033 (native is 0) | +0.0294 to +0.0363 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.754 | 0.2855 | −83.7% | −1.6584 to −1.2788 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.2 | 3157 | +326.5% | +2154.2705 to +2678.8277 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.97 | 4.668 | +17.6% | +0.4596 to +0.9350 | yes: power given |
| pods started | 0.2 | 2.7 | +1250.0% | +1.2726 to +3.7274 | yes: power given |
| pod start wait, total (s) | 0.5 | 4.3 | +760.0% | +1.4204 to +6.1796 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.465 | +193.0% | +0.0288 to +1.9012 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.39 | 18.49 | −66.0% | −41.1168 to −30.6749 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 929.4 | 1507 | +62.1% | +474.0792 to +681.1208 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 1160 | +1265836.4% | +1157.6299 to +1163.0701 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1477 | +246016.7% | +1473.4353 to +1478.7647 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 238.8 | 1160 | +386.0% | +818.5201 to +1024.7715 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*