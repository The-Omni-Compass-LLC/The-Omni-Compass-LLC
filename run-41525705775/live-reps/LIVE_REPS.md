# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.17 | 11.25 |
| node-hours | 5.027 | 5.033 | 4.685 | 4.717 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527.1 | 528.1 | 526.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 527.1 | 502.1 | 502.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 748 | 894.6 | 852.9 | 1018 |
| response time (ms), 95th percentile | 2973 | 3855 | 3575 | 4321 |
| response time (ms), 99th percentile | 4060 | 5317 | 4909 | 6000 |
| time over the response line (% of samples) | 27.33 | 29.64 | 30.16 | 35.91 |
| failed requests (%) | 0 | 0.032 | 0.04796 | 0.1797 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 16.3 | 15.1 | 17.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 106.9 | 59.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 9.231 | 30 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.43 | 51.82 | 25.76 | 86.24 |
| utilisation (used / allocatable) | 0.03723 | 0.03582 | 0.04018 | 0.03731 |
| CPU used (cores), mean | 1.787 | 1.719 | 1.785 | 1.674 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05742 | 0.04686 |
| CPU used with Omni's own (cores), mean | 1.787 | 1.719 | 1.843 | 1.721 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.1 | 741.3 | 679.4 | 728.8 |
| HPA replicas, mean | 4 | 4.103 | 5.031 | 5.42 |
| pods started | 0.3 | 0.1 | 4.1 | 4.1 |
| pod start wait, total (s) | 0.7 | 0.1 | 9.9 | 10.7 |
| pod start wait, mean (s) | 0.45 | 0.1 | 2.128 | 2.525 |
| host CPU busy, the real machine under kind (%) | 54.48 | 60.95 | 60.33 | 67.34 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 924.5 | 1042 | 974.1 | 1110 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.53 | 10.57 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 8.804 | 0.1375 | 16.85 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 34.4 | 0.7 | 130.6 |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 350.7 | 272.8 | 417.2 |
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
| worker nodes in service, mean | 12 | 11.25 | −6.2% | −1.6838 to +0.1900 | no |
| node-hours | 5.033 | 4.717 | −6.3% | −0.6993 to +0.0675 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 526.4 | −0.1% | −3.8067 to +2.3907 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 502.9 | −4.6% | −52.4268 to +4.0274 | no |
| response time (ms), mean | 894.6 | 1018 | +13.8% | +46.2888 to +200.8960 | yes: LOSS |
| response time (ms), 95th percentile | 3855 | 4321 | +12.1% | −21.1110 to +951.6650 | no |
| response time (ms), 99th percentile | 5317 | 6000 | +12.9% | +123.3911 to +1243.2295 | yes: LOSS |
| time over the response line (% of samples) | 29.64 | 35.91 | +21.2% | +3.4402 to +9.1070 | yes: LOSS |
| failed requests (%) | 0.032 | 0.1797 | +461.6% | −0.0991 to +0.3945 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.3 | 17.8 | +9.2% | +1.1230 to +1.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.5 | +59.500 (native is 0) | +47.8813 to +71.1187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 51.82 | 86.24 | +66.4% | −22.9012 to +91.7479 | no |
| utilisation (used / allocatable) | 0.03582 | 0.03731 | +4.2% | −0.0036 to +0.0066 | no |
| CPU used (cores), mean | 1.719 | 1.674 | −2.6% | −0.2236 to +0.1332 | no |
| Omni's own CPU (cores), mean | 0 | 0.04686 | +0.047 (native is 0) | +0.0395 to +0.0543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.719 | 1.721 | +0.1% | −0.1743 to +0.1776 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.3 | 728.8 | −1.7% | −111.5306 to +86.4996 | no |
| HPA replicas, mean | 4.103 | 5.42 | +32.1% | +0.8341 to +1.8003 | yes: power given |
| pods started | 0.1 | 4.1 | +4000.0% | +2.7842 to +5.2158 | yes: power given |
| pod start wait, total (s) | 0.1 | 10.7 | +10600.0% | +6.8572 to +14.3428 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 2.525 | +2424.8% | +1.7276 to +3.1219 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.95 | 67.34 | +10.5% | +5.4640 to +7.3132 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1042 | 1110 | +6.5% | +51.7208 to +84.4792 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.57 | −11.9% | −2.9811 to +0.1309 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 8.804 | 16.85 | +91.3% | +0.0628 to +16.0205 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.4 | 130.6 | +279.7% | −12.8529 to +205.2529 | no |
| queue: job turnaround, submitted to done, mean (s) | 350.7 | 417.2 | +19.0% | +44.6919 to +88.2664 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.027 | 5.033 | +0.1% | −0.0116 to +0.0236 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527.1 | −0.1% | −2.5032 to +1.7281 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 527.1 | −0.1% | −2.5032 to +1.7281 | no |
| response time (ms), mean | 748 | 894.6 | +19.6% | +59.3570 to +233.6966 | yes: LOSS |
| response time (ms), 95th percentile | 2973 | 3855 | +29.7% | +331.3399 to +1432.6081 | yes: LOSS |
| response time (ms), 99th percentile | 4060 | 5317 | +30.9% | +730.6218 to +1782.1452 | yes: LOSS |
| time over the response line (% of samples) | 27.33 | 29.64 | +8.5% | −0.8620 to +5.4932 | no |
| failed requests (%) | 0 | 0.032 | +0.032 (native is 0) | −0.0079 to +0.0719 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 16.3 | +18.1% | +1.1407 to +3.8593 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.43 | 51.82 | +197.3% | +8.6393 to +60.1407 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03723 | 0.03582 | −3.8% | −0.0028 to +0.0000 | no |
| CPU used (cores), mean | 1.787 | 1.719 | −3.8% | −0.1362 to +0.0005 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.787 | 1.719 | −3.8% | −0.1362 to +0.0005 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.1 | 741.3 | +2.9% | −3.2878 to +45.7469 | no |
| HPA replicas, mean | 4 | 4.103 | +2.6% | −0.0304 to +0.2358 | no |
| pods started | 0.3 | 0.1 | −66.7% | −0.7642 to +0.3642 | no |
| pod start wait, total (s) | 0.7 | 0.1 | −85.7% | −1.8251 to +0.6251 | no |
| pod start wait, mean (s) | 0.45 | 0.1 | −77.8% | −1.1049 to +0.4049 | no |
| host CPU busy, the real machine under kind (%) | 54.48 | 60.95 | +11.9% | +4.9610 to +7.9804 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924.5 | 1042 | +12.7% | +69.7033 to +165.4967 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 8.804 | +6943.3% | +1.8509 to +15.5074 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 34.4 | +4814.3% | −39.5165 to +106.9165 | no |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 350.7 | +52.7% | +72.9812 to +169.2022 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.17 | −6.9% | −2.0217 to +0.3622 | no |
| node-hours | 5.027 | 4.685 | −6.8% | −0.8462 to +0.1639 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 528.1 | +0.1% | −1.7964 to +3.1753 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 502.1 | −4.8% | −63.6687 to +12.9185 | no |
| response time (ms), mean | 748 | 852.9 | +14.0% | +21.9260 to +187.6968 | yes: LOSS |
| response time (ms), 95th percentile | 2973 | 3575 | +20.2% | +224.3057 to +978.2873 | yes: LOSS |
| response time (ms), 99th percentile | 4060 | 4909 | +20.9% | +371.7357 to +1326.1545 | yes: LOSS |
| time over the response line (% of samples) | 27.33 | 30.16 | +10.4% | +1.2127 to +4.4577 | yes: LOSS |
| failed requests (%) | 0 | 0.04796 | +0.048 (native is 0) | −0.0440 to +0.1399 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 15.1 | +9.4% | −0.1326 to +2.7326 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.9 | +106.900 (native is 0) | +59.6916 to +154.1084 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.43 | 25.76 | +47.8% | −0.1304 to +16.7871 | no |
| utilisation (used / allocatable) | 0.03723 | 0.04018 | +7.9% | −0.0014 to +0.0073 | no |
| CPU used (cores), mean | 1.787 | 1.785 | −0.1% | −0.0673 to +0.0635 | no |
| Omni's own CPU (cores), mean | 0 | 0.05742 | +0.057 (native is 0) | +0.0532 to +0.0617 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.787 | 1.843 | +3.1% | −0.0115 to +0.1226 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.1 | 679.4 | −5.6% | −101.6456 to +20.3114 | no |
| HPA replicas, mean | 4 | 5.031 | +25.8% | +0.7098 to +1.3524 | yes: power given |
| pods started | 0.3 | 4.1 | +1266.7% | +2.3774 to +5.2226 | yes: power given |
| pod start wait, total (s) | 0.7 | 9.9 | +1314.3% | +5.1705 to +13.2295 | yes: LOSS |
| pod start wait, mean (s) | 0.45 | 2.128 | +373.0% | +0.8767 to +2.4800 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.48 | 60.33 | +10.7% | +4.2774 to +7.4293 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924.5 | 974.1 | +5.4% | +18.1532 to +81.0468 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.53 | −12.2% | −3.4014 to +0.4649 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.1375 | +10.0% | −0.0504 to +0.0754 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 272.8 | +18.8% | +17.5370 to +68.7880 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.17 | −6.9% | −2.0217 to +0.3622 | no |
| node-hours | 5.033 | 4.685 | −6.9% | −0.8434 to +0.1490 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 528.1 | +0.2% | −0.1321 to +2.2861 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 502.1 | −4.7% | −62.6673 to +12.6921 | no |
| response time (ms), mean | 894.6 | 852.9 | −4.7% | −92.7671 to +9.3362 | no |
| response time (ms), 95th percentile | 3855 | 3575 | −7.3% | −601.5153 to +40.1603 | no |
| response time (ms), 99th percentile | 5317 | 4909 | −7.7% | −1000.0897 to +185.2129 | no |
| time over the response line (% of samples) | 29.64 | 30.16 | +1.8% | −1.9935 to +3.0327 | no |
| failed requests (%) | 0.032 | 0.04796 | +49.9% | −0.0926 to +0.1245 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.3 | 15.1 | −7.4% | −1.5016 to −0.8984 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.9 | +106.900 (native is 0) | +59.6916 to +154.1084 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 51.82 | 25.76 | −50.3% | −44.8707 to −7.2526 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03582 | 0.04018 | +12.2% | +0.0005 to +0.0083 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.719 | 1.785 | +3.8% | −0.0199 to +0.1518 | no |
| Omni's own CPU (cores), mean | 0 | 0.05742 | +0.057 (native is 0) | +0.0532 to +0.0617 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.719 | 1.843 | +7.2% | +0.0342 to +0.2126 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.3 | 679.4 | −8.3% | −117.2406 to −6.5527 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.103 | 5.031 | +22.6% | +0.5757 to +1.2811 | yes: power given |
| pods started | 0.1 | 4.1 | +4000.0% | +2.4184 to +5.5816 | yes: power given |
| pod start wait, total (s) | 0.1 | 9.9 | +9800.0% | +5.6867 to +13.9133 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 2.128 | +2028.3% | +1.2346 to +2.8220 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.95 | 60.33 | −1.0% | −1.1099 to −0.1248 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1042 | 974.1 | −6.5% | −88.7508 to −47.2492 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.53 | −12.2% | −3.4014 to +0.4649 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 8.804 | 0.1375 | −98.4% | −15.4699 to −1.8634 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.4 | 0.7 | −98.0% | −106.9165 to +39.5165 | no |
| queue: job turnaround, submitted to done, mean (s) | 350.7 | 272.8 | −22.2% | −104.3554 to −51.5029 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.25 | −6.2% | −1.6838 to +0.1900 | no |
| node-hours | 5.027 | 4.717 | −6.2% | −0.7058 to +0.0861 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 526.4 | −0.2% | −4.2406 to +2.0496 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 502.9 | −4.7% | −53.7013 to +4.5268 | no |
| response time (ms), mean | 748 | 1018 | +36.1% | +146.7239 to +393.5145 | yes: LOSS |
| response time (ms), 95th percentile | 2973 | 4321 | +45.3% | +758.0124 to +1936.4896 | yes: LOSS |
| response time (ms), 99th percentile | 4060 | 6000 | +47.8% | +1211.5661 to +2667.8215 | yes: LOSS |
| time over the response line (% of samples) | 27.33 | 35.91 | +31.4% | +3.8961 to +13.2822 | yes: LOSS |
| failed requests (%) | 0 | 0.1797 | +0.180 (native is 0) | −0.0745 to +0.4340 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 17.8 | +29.0% | +2.6512 to +5.3488 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.5 | +59.500 (native is 0) | +47.8813 to +71.1187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.43 | 86.24 | +394.8% | +5.1841 to +132.4426 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03723 | 0.03731 | +0.2% | −0.0056 to +0.0058 | no |
| CPU used (cores), mean | 1.787 | 1.674 | −6.3% | −0.3012 to +0.0750 | no |
| Omni's own CPU (cores), mean | 0 | 0.04686 | +0.047 (native is 0) | +0.0395 to +0.0543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.787 | 1.721 | −3.7% | −0.2503 to +0.1179 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.1 | 728.8 | +1.2% | −99.6917 to +117.1199 | no |
| HPA replicas, mean | 4 | 5.42 | +35.5% | +1.0004 to +1.8395 | yes: power given |
| pods started | 0.3 | 4.1 | +1266.7% | +2.5474 to +5.0526 | yes: power given |
| pod start wait, total (s) | 0.7 | 10.7 | +1428.6% | +6.0966 to +13.9034 | yes: LOSS |
| pod start wait, mean (s) | 0.45 | 2.525 | +461.1% | +1.2811 to +2.8684 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.48 | 67.34 | +23.6% | +10.6728 to +15.0458 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924.5 | 1110 | +20.1% | +125.1917 to +246.2083 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.57 | −11.9% | −2.9811 to +0.1309 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 16.85 | +13376.7% | +4.8596 to +28.5820 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 130.6 | +18557.1% | +13.1218 to +246.6782 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 417.2 | +81.7% | +121.9587 to +253.1829 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*