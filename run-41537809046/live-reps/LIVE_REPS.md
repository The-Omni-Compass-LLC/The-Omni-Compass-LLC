# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.03 | 11.56 |
| node-hours | 5.029 | 5.02 | 4.621 | 4.841 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 526.8 | 528.2 | 526.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 526.8 | 497.6 | 512.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 754 | 1155 | 912 | 1321 |
| response time (ms), 95th percentile | 3081 | 4056 | 3814 | 4715 |
| response time (ms), 99th percentile | 4228 | 5319 | 5029 | 6063 |
| time over the response line (% of samples) | 27.76 | 39.62 | 31.94 | 44.08 |
| failed requests (%) | 0.01419 | 0.05307 | 0.04042 | 0.1273 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 16.8 | 15.5 | 17.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 107.9 | 91.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 26.67 | 20 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.08 | 39.95 | 22.62 | 88.17 |
| utilisation (used / allocatable) | 0.03625 | 0.03745 | 0.04086 | 0.03738 |
| CPU used (cores), mean | 1.74 | 1.798 | 1.808 | 1.733 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05712 | 0.05719 |
| CPU used with Omni's own (cores), mean | 1.74 | 1.798 | 1.865 | 1.79 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.1 | 722.6 | 667.3 | 726.7 |
| HPA replicas, mean | 4.056 | 4.084 | 4.949 | 5.393 |
| pods started | 0.1 | 0 | 3.7 | 4.3 |
| pod start wait, total (s) | 0.1 | 0 | 9.5 | 13.1 |
| pod start wait, mean (s) | 0.1 | 0 | 2.233 | 2.483 |
| host CPU busy, the real machine under kind (%) | 53.76 | 61.81 | 60.57 | 68.23 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 922.4 | 1068 | 990.1 | 1133 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.14 | 11.33 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 13.24 | 0.1167 | 9.938 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 79.7 | 0.8 | 62.8 |
| queue: job turnaround, submitted to done, mean (s) | 232.6 | 343.7 | 288.5 | 419.3 |
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
| worker nodes in service, mean | 12 | 11.56 | −3.7% | −1.3703 to +0.4906 | no |
| node-hours | 5.02 | 4.841 | −3.6% | −0.5698 to +0.2117 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 526.5 | −0.1% | −4.8238 to +4.1513 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 512.7 | −2.7% | −43.4036 to +15.1728 | no |
| response time (ms), mean | 1155 | 1321 | +14.4% | +30.0554 to +302.1926 | yes: LOSS |
| response time (ms), 95th percentile | 4056 | 4715 | +16.3% | +158.9613 to +1160.0167 | yes: LOSS |
| response time (ms), 99th percentile | 5319 | 6063 | +14.0% | +0.3704 to +1486.8806 | yes: LOSS |
| time over the response line (% of samples) | 39.62 | 44.08 | +11.3% | +2.1555 to +6.7759 | yes: LOSS |
| failed requests (%) | 0.05307 | 0.1273 | +140.0% | −0.0004 to +0.1489 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.8 | 17.9 | +6.5% | +0.5722 to +1.6278 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.1 | +91.100 (native is 0) | +36.9164 to +145.2836 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 39.95 | 88.17 | +120.7% | −18.8264 to +115.2630 | no |
| utilisation (used / allocatable) | 0.03745 | 0.03738 | −0.2% | −0.0066 to +0.0064 | no |
| CPU used (cores), mean | 1.798 | 1.733 | −3.6% | −0.3451 to +0.2163 | no |
| Omni's own CPU (cores), mean | 0 | 0.05719 | +0.057 (native is 0) | +0.0516 to +0.0627 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.798 | 1.79 | −0.4% | −0.2867 to +0.2722 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.6 | 726.7 | +0.6% | −128.0991 to +136.3162 | no |
| HPA replicas, mean | 4.084 | 5.393 | +32.0% | +0.6379 to +1.9791 | yes: power given |
| pods started | 0 | 4.3 | +4.300 (native is 0) | +2.4515 to +6.1485 | yes: power given |
| pod start wait, total (s) | 0 | 13.1 | +13.100 (native is 0) | +5.5115 to +20.6885 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.483 | +2.483 (native is 0) | +1.3868 to +3.5799 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.81 | 68.23 | +10.4% | +5.5187 to +7.3166 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1068 | 1133 | +6.1% | +39.0121 to +92.1879 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.33 | −5.6% | −2.0183 to +0.6794 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 13.24 | 9.938 | −24.9% | −16.6954 to +10.0954 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 79.7 | 62.8 | −21.2% | −111.8037 to +78.0037 | no |
| queue: job turnaround, submitted to done, mean (s) | 343.7 | 419.3 | +22.0% | +48.5351 to +102.8149 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.029 | 5.02 | −0.2% | −0.0193 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 526.8 | −0.0% | −1.4144 to +1.2867 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 526.8 | −0.0% | −1.4144 to +1.2867 | no |
| response time (ms), mean | 754 | 1155 | +53.1% | +220.5562 to +580.5934 | yes: LOSS |
| response time (ms), 95th percentile | 3081 | 4056 | +31.6% | +552.8632 to +1396.6048 | yes: LOSS |
| response time (ms), 99th percentile | 4228 | 5319 | +25.8% | +643.9474 to +1538.2422 | yes: LOSS |
| time over the response line (% of samples) | 27.76 | 39.62 | +42.7% | +8.0625 to +15.6578 | yes: LOSS |
| failed requests (%) | 0.01419 | 0.05307 | +274.0% | −0.0225 to +0.1003 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 16.8 | +17.5% | +1.4204 to +3.5796 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.08 | 39.95 | +121.0% | +2.8811 to +40.8655 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03625 | 0.03745 | +3.3% | −0.0008 to +0.0032 | no |
| CPU used (cores), mean | 1.74 | 1.798 | +3.3% | −0.0378 to +0.1534 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.74 | 1.798 | +3.3% | −0.0378 to +0.1534 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.1 | 722.6 | −3.7% | −62.4974 to +7.6244 | no |
| HPA replicas, mean | 4.056 | 4.084 | +0.7% | −0.1457 to +0.2031 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 53.76 | 61.81 | +15.0% | +6.1198 to +9.9842 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 922.4 | 1068 | +15.7% | +88.1099 to +202.2901 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 13.24 | +14340.9% | +0.7231 to +25.5686 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 79.7 | +15840.0% | −7.3786 to +165.7786 | no |
| queue: job turnaround, submitted to done, mean (s) | 232.6 | 343.7 | +47.8% | +64.5252 to +157.7081 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.03 | −8.1% | −2.1214 to +0.1757 | no |
| node-hours | 5.029 | 4.621 | −8.1% | −0.8874 to +0.0716 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 528.2 | +0.2% | −0.3442 to +2.9663 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 497.6 | −5.6% | −65.1072 to +6.4918 | no |
| response time (ms), mean | 754 | 912 | +21.0% | +53.6157 to +262.4362 | yes: LOSS |
| response time (ms), 95th percentile | 3081 | 3814 | +23.8% | +324.2039 to +1141.6651 | yes: LOSS |
| response time (ms), 99th percentile | 4228 | 5029 | +18.9% | +265.9775 to +1334.7697 | yes: LOSS |
| time over the response line (% of samples) | 27.76 | 31.94 | +15.1% | +2.7813 to +5.5913 | yes: LOSS |
| failed requests (%) | 0.01419 | 0.04042 | +184.9% | −0.0222 to +0.0746 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 15.5 | +8.4% | +0.3879 to +2.0121 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.9 | +107.900 (native is 0) | +56.8197 to +158.9803 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.08 | 22.62 | +25.1% | +0.2406 to +8.8494 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03625 | 0.04086 | +12.7% | +0.0008 to +0.0085 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.74 | 1.808 | +3.9% | +0.0220 to +0.1143 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05712 | +0.057 (native is 0) | +0.0526 to +0.0616 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.74 | 1.865 | +7.2% | +0.0775 to +0.1730 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.1 | 667.3 | −11.0% | −169.4839 to +3.9081 | no |
| HPA replicas, mean | 4.056 | 4.949 | +22.0% | +0.5063 to +1.2801 | yes: power given |
| pods started | 0.1 | 3.7 | +3600.0% | +2.0845 to +5.1155 | yes: power given |
| pod start wait, total (s) | 0.1 | 9.5 | +9400.0% | +4.7741 to +14.0259 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 2.233 | +2132.6% | +1.4872 to +2.7781 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.76 | 60.57 | +12.7% | +5.4834 to +8.1323 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 922.4 | 990.1 | +7.3% | +36.4166 to +98.9834 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.14 | −15.5% | −3.5799 to −0.1348 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.1167 | +27.3% | −0.0220 to +0.0720 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 232.6 | 288.5 | +24.0% | +28.4936 to +83.3564 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.03 | −8.1% | −2.1214 to +0.1757 | no |
| node-hours | 5.02 | 4.621 | −7.9% | −0.8796 to +0.0824 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 528.2 | +0.3% | −0.9038 to +3.6536 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 497.6 | −5.6% | −65.2839 to +6.7962 | no |
| response time (ms), mean | 1155 | 912 | −21.0% | −341.2517 to −143.8460 | yes: GAIN |
| response time (ms), 95th percentile | 4056 | 3814 | −6.0% | −493.7260 to +10.1270 | no |
| response time (ms), 99th percentile | 5319 | 5029 | −5.5% | −686.4177 to +104.9753 | no |
| time over the response line (% of samples) | 39.62 | 31.94 | −19.4% | −10.6171 to −4.7307 | yes: GAIN |
| failed requests (%) | 0.05307 | 0.04042 | −23.8% | −0.1139 to +0.0886 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.8 | 15.5 | −7.7% | −1.7828 to −0.8172 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.9 | +107.900 (native is 0) | +56.8197 to +158.9803 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 39.95 | 22.62 | −43.4% | −33.8180 to −0.8387 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03745 | 0.04086 | +9.1% | −0.0007 to +0.0075 | no |
| CPU used (cores), mean | 1.798 | 1.808 | +0.6% | −0.0954 to +0.1160 | no |
| Omni's own CPU (cores), mean | 0 | 0.05712 | +0.057 (native is 0) | +0.0526 to +0.0616 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.798 | 1.865 | +3.8% | −0.0403 to +0.1751 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.6 | 667.3 | −7.7% | −127.1244 to +16.4217 | no |
| HPA replicas, mean | 4.084 | 4.949 | +21.2% | +0.4748 to +1.2541 | yes: power given |
| pods started | 0 | 3.7 | +3.700 (native is 0) | +2.1166 to +5.2834 | yes: power given |
| pod start wait, total (s) | 0 | 9.5 | +9.500 (native is 0) | +4.7522 to +14.2478 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.233 | +2.233 (native is 0) | +1.5322 to +2.9331 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.81 | 60.57 | −2.0% | −2.1123 to −0.3760 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1068 | 990.1 | −7.3% | −108.0649 to −46.9351 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.14 | −15.5% | −3.5799 to −0.1348 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 13.24 | 0.1167 | −99.1% | −25.5653 to −0.6763 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 79.7 | 0.8 | −99.0% | −165.6319 to +7.8319 | no |
| queue: job turnaround, submitted to done, mean (s) | 343.7 | 288.5 | −16.1% | −84.7652 to −25.6181 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.56 | −3.7% | −1.3703 to +0.4906 | no |
| node-hours | 5.029 | 4.841 | −3.7% | −0.5792 to +0.2025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 526.5 | −0.1% | −4.3862 to +3.5860 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 512.7 | −2.7% | −43.4035 to +15.0450 | no |
| response time (ms), mean | 754 | 1321 | +75.2% | +341.3346 to +792.0631 | yes: LOSS |
| response time (ms), 95th percentile | 3081 | 4715 | +53.0% | +1031.8129 to +2236.6331 | yes: LOSS |
| response time (ms), 99th percentile | 4228 | 6063 | +43.4% | +1002.8996 to +2666.5410 | yes: LOSS |
| time over the response line (% of samples) | 27.76 | 44.08 | +58.8% | +11.6025 to +21.0493 | yes: LOSS |
| failed requests (%) | 0.01419 | 0.1273 | +797.5% | −0.0010 to +0.2273 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 17.9 | +25.2% | +2.4715 to +4.7285 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.1 | +91.100 (native is 0) | +36.9164 to +145.2836 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.08 | 88.17 | +387.7% | +7.8326 to +132.3507 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03625 | 0.03738 | +3.1% | −0.0042 to +0.0065 | no |
| CPU used (cores), mean | 1.74 | 1.733 | −0.4% | −0.2190 to +0.2058 | no |
| Omni's own CPU (cores), mean | 0 | 0.05719 | +0.057 (native is 0) | +0.0516 to +0.0627 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.74 | 1.79 | +2.9% | −0.1594 to +0.2606 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 750.1 | 726.7 | −3.1% | −151.5641 to +104.9082 | no |
| HPA replicas, mean | 4.056 | 5.393 | +33.0% | +0.7132 to +1.9612 | yes: power given |
| pods started | 0.1 | 4.3 | +4200.0% | +2.3904 to +6.0096 | yes: power given |
| pod start wait, total (s) | 0.1 | 13.1 | +13000.0% | +5.4827 to +20.5173 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 2.483 | +2383.3% | +1.3345 to +3.4322 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.76 | 68.23 | +26.9% | +12.7673 to +16.1720 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 922.4 | 1133 | +22.9% | +151.2075 to +270.3925 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.33 | −5.6% | −2.0183 to +0.6794 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 9.938 | +10740.9% | +1.4423 to +18.2494 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 62.8 | +12460.0% | +4.3351 to +120.2649 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 232.6 | 419.3 | +80.3% | +132.5811 to +241.0022 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*