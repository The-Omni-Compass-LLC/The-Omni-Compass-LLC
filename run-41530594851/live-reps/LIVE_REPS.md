# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.31 | 11.16 |
| node-hours | 5.023 | 5.027 | 4.317 | 4.677 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 526 | 525.4 | 528.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 526 | 472.4 | 501.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 571.2 | 828.4 | 682.9 | 1082 |
| response time (ms), 95th percentile | 2130 | 2928 | 2702 | 4031 |
| response time (ms), 99th percentile | 2872 | 4097 | 3590 | 5535 |
| time over the response line (% of samples) | 22.76 | 32.49 | 27.23 | 39.05 |
| failed requests (%) | 0 | 0.06881 | 0.04329 | 0.1109 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 14 | 13.1 | 17.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 127.7 | 88.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 15 | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.12 | 29.83 | 27.64 | 51.23 |
| utilisation (used / allocatable) | 0.03464 | 0.03505 | 0.03996 | 0.04019 |
| CPU used (cores), mean | 1.663 | 1.683 | 1.642 | 1.781 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05235 | 0.0546 |
| CPU used with Omni's own (cores), mean | 1.663 | 1.683 | 1.694 | 1.836 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 761.5 | 694.1 | 674.4 |
| HPA replicas, mean | 4.043 | 3.956 | 4.777 | 5.078 |
| pods started | 0.4 | 0 | 3.3 | 4.1 |
| pod start wait, total (s) | 0.9 | 0 | 8.7 | 11.1 |
| pod start wait, mean (s) | 0.7 | 0 | 1.778 | 2.42 |
| host CPU busy, the real machine under kind (%) | 50.78 | 57.21 | 56.67 | 64.97 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 865.7 | 972.4 | 917.2 | 1069 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.937 | 10.33 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 11.9 | 0.125 | 12.94 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 89.1 | 0.7 | 75.1 |
| queue: job turnaround, submitted to done, mean (s) | 174.2 | 253.3 | 226.5 | 356.6 |
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
| worker nodes in service, mean | 12 | 11.16 | −7.0% | −2.0567 to +0.3672 | no |
| node-hours | 5.027 | 4.677 | −7.0% | −0.8533 to +0.1527 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526 | 528.1 | +0.4% | +0.0505 to +4.1078 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526 | 501.4 | −4.7% | −62.5767 to +13.4891 | no |
| response time (ms), mean | 828.4 | 1082 | +30.7% | +122.8451 to +385.2158 | yes: LOSS |
| response time (ms), 95th percentile | 2928 | 4031 | +37.6% | +625.7139 to +1578.6611 | yes: LOSS |
| response time (ms), 99th percentile | 4097 | 5535 | +35.1% | +716.1308 to +2160.6662 | yes: LOSS |
| time over the response line (% of samples) | 32.49 | 39.05 | +20.2% | +0.0585 to +13.0732 | yes: LOSS |
| failed requests (%) | 0.06881 | 0.1109 | +61.2% | −0.2027 to +0.2869 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 17.1 | +22.1% | −0.1771 to +6.3771 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 88.8 | +88.800 (native is 0) | +46.2236 to +131.3764 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 29.83 | 51.23 | +71.7% | +1.2078 to +41.5955 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03505 | 0.04019 | +14.7% | +0.0008 to +0.0095 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.683 | 1.781 | +5.9% | +0.0179 to +0.1799 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0546 | +0.055 (native is 0) | +0.0484 to +0.0608 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.683 | 1.836 | +9.1% | +0.0751 to +0.2319 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 674.4 | −11.4% | −156.3160 to −17.8610 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.956 | 5.078 | +28.3% | +0.4276 to +1.8152 | yes: power given |
| pods started | 0 | 4.1 | +4.100 (native is 0) | +2.7324 to +5.4676 | yes: power given |
| pod start wait, total (s) | 0 | 11.1 | +11.100 (native is 0) | +7.0193 to +15.1807 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.42 | +2.420 (native is 0) | +1.7387 to +3.1009 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.21 | 64.97 | +13.6% | +6.1496 to +9.3754 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 972.4 | 1069 | +10.0% | +62.2832 to +131.7168 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.33 | −14.0% | −3.4332 to +0.0842 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 11.9 | 12.94 | +8.7% | −10.8857 to +12.9607 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 89.1 | 75.1 | −15.7% | −67.2465 to +39.2465 | no |
| queue: job turnaround, submitted to done, mean (s) | 253.3 | 356.7 | +40.8% | +67.6281 to +139.1302 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.023 | 5.027 | +0.1% | −0.0136 to +0.0216 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 526 | +0.2% | −1.6740 to +3.3433 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 526 | +0.2% | −1.6740 to +3.3433 | no |
| response time (ms), mean | 571.2 | 828.4 | +45.0% | +110.4413 to +403.8260 | yes: LOSS |
| response time (ms), 95th percentile | 2130 | 2928 | +37.5% | +349.4450 to +1246.5020 | yes: LOSS |
| response time (ms), 99th percentile | 2872 | 4097 | +42.7% | +601.7657 to +1848.2815 | yes: LOSS |
| time over the response line (% of samples) | 22.76 | 32.49 | +42.8% | +5.8928 to +13.5667 | yes: LOSS |
| failed requests (%) | 0 | 0.06881 | +0.069 (native is 0) | −0.0231 to +0.1608 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 14 | +15.7% | +0.9198 to +2.8802 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.12 | 29.83 | +97.3% | −1.4992 to +30.9125 | no |
| utilisation (used / allocatable) | 0.03464 | 0.03505 | +1.2% | −0.0019 to +0.0027 | no |
| CPU used (cores), mean | 1.663 | 1.683 | +1.2% | −0.0920 to +0.1314 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.663 | 1.683 | +1.2% | −0.0920 to +0.1314 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 761.5 | −1.6% | −51.4534 to +25.9572 | no |
| HPA replicas, mean | 4.043 | 3.956 | −2.1% | −0.2409 to +0.0684 | no |
| pods started | 0.4 | 0 | −100.0% | −0.9001 to +0.1001 | no |
| pod start wait, total (s) | 0.9 | 0 | −100.0% | −1.9900 to +0.1900 | no |
| pod start wait, mean (s) | 0.7 | 0 | −100.0% | −1.5294 to +0.1294 | no |
| host CPU busy, the real machine under kind (%) | 50.78 | 57.21 | +12.7% | +4.6932 to +8.1603 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 865.7 | 972.4 | +12.3% | +53.2946 to +160.1054 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 11.9 | +10884.6% | −0.7796 to +24.3630 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 89.1 | +17720.0% | −3.3844 to +180.5844 | no |
| queue: job turnaround, submitted to done, mean (s) | 174.2 | 253.3 | +45.4% | +37.8839 to +120.2327 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.31 | −14.1% | −3.0621 to −0.3184 | yes: GAIN |
| node-hours | 5.023 | 4.317 | −14.1% | −1.2813 to −0.1312 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 525.4 | +0.1% | −2.2743 to +2.8009 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 472.4 | −10.1% | −96.0689 to −9.4961 | yes: GAIN |
| response time (ms), mean | 571.2 | 682.9 | +19.5% | +19.0309 to +204.2921 | yes: LOSS |
| response time (ms), 95th percentile | 2130 | 2702 | +26.8% | +201.1402 to +940.9368 | yes: LOSS |
| response time (ms), 99th percentile | 2872 | 3590 | +25.0% | +222.9264 to +1213.0530 | yes: LOSS |
| time over the response line (% of samples) | 22.76 | 27.23 | +19.7% | +2.6403 to +6.3043 | yes: LOSS |
| failed requests (%) | 0 | 0.04329 | +0.043 (native is 0) | −0.0546 to +0.1412 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 13.1 | +8.3% | +0.3256 to +1.6744 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.7 | +127.700 (native is 0) | +51.8429 to +203.5571 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.12 | 27.64 | +82.8% | −0.8233 to +25.8666 | no |
| utilisation (used / allocatable) | 0.03464 | 0.03996 | +15.4% | +0.0008 to +0.0098 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.663 | 1.642 | −1.3% | −0.0769 to +0.0350 | no |
| Omni's own CPU (cores), mean | 0 | 0.05235 | +0.052 (native is 0) | +0.0460 to +0.0587 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.663 | 1.694 | +1.9% | −0.0275 to +0.0903 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 694.1 | −10.4% | −146.0572 to −14.2970 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.043 | 4.777 | +18.2% | +0.3648 to +1.1042 | yes: power given |
| pods started | 0.4 | 3.3 | +725.0% | +0.8091 to +4.9909 | yes: power given |
| pod start wait, total (s) | 0.9 | 8.7 | +866.7% | +1.9420 to +13.6580 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 1.778 | +154.0% | −0.1949 to +2.3511 | no |
| host CPU busy, the real machine under kind (%) | 50.78 | 56.67 | +11.6% | +4.3906 to +7.3828 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 865.7 | 917.2 | +5.9% | +17.9690 to +85.0310 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.937 | −25.5% | −5.2715 to −0.8535 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.125 | +15.4% | −0.0495 to +0.0829 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 174.2 | 226.5 | +30.0% | +18.8889 to +85.7528 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.31 | −14.1% | −3.0621 to −0.3184 | yes: GAIN |
| node-hours | 5.027 | 4.317 | −14.1% | −1.2813 to −0.1392 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526 | 525.4 | −0.1% | −1.9499 to +0.8071 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526 | 472.4 | −10.2% | −96.8504 to −10.3840 | yes: GAIN |
| response time (ms), mean | 828.4 | 682.9 | −17.6% | −213.0808 to −77.8635 | yes: GAIN |
| response time (ms), 95th percentile | 2928 | 2702 | −7.7% | −482.6105 to +28.7405 | no |
| response time (ms), 99th percentile | 4097 | 3590 | −12.4% | −912.9985 to −101.0693 | yes: GAIN |
| time over the response line (% of samples) | 32.49 | 27.23 | −16.2% | −8.0086 to −2.5064 | yes: GAIN |
| failed requests (%) | 0.06881 | 0.04329 | −37.1% | −0.0850 to +0.0339 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 13.1 | −6.4% | −1.5263 to −0.2737 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.7 | +127.700 (native is 0) | +51.8429 to +203.5571 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 29.83 | 27.64 | −7.3% | −8.9493 to +4.5793 | no |
| utilisation (used / allocatable) | 0.03505 | 0.03996 | +14.0% | +0.0006 to +0.0092 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.683 | 1.642 | −2.4% | −0.1216 to +0.0402 | no |
| Omni's own CPU (cores), mean | 0 | 0.05235 | +0.052 (native is 0) | +0.0460 to +0.0587 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.683 | 1.694 | +0.7% | −0.0727 to +0.0960 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 694.1 | −8.9% | −129.3910 to −5.4669 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.956 | 4.777 | +20.7% | +0.4605 to +1.1811 | yes: power given |
| pods started | 0 | 3.3 | +3.300 (native is 0) | +1.2754 to +5.3246 | yes: power given |
| pod start wait, total (s) | 0 | 8.7 | +8.700 (native is 0) | +2.9870 to +14.4130 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.778 | +1.778 (native is 0) | +0.8803 to +2.6759 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.21 | 56.67 | −0.9% | −1.1929 to +0.1129 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 972.4 | 917.2 | −5.7% | −80.2931 to −30.1069 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.937 | −25.5% | −5.2715 to −0.8535 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 11.9 | 0.125 | −98.9% | −24.3643 to +0.8143 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 89.1 | 0.7 | −99.2% | −180.5894 to +3.7894 | no |
| queue: job turnaround, submitted to done, mean (s) | 253.3 | 226.5 | −10.6% | −50.9957 to −2.4793 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.16 | −7.0% | −2.0567 to +0.3672 | no |
| node-hours | 5.023 | 4.677 | −6.9% | −0.8485 to +0.1559 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 528.1 | +0.6% | +0.2293 to +5.5983 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 501.4 | −4.5% | −61.6568 to +14.2385 | no |
| response time (ms), mean | 571.2 | 1082 | +89.5% | +320.8002 to +701.5281 | yes: LOSS |
| response time (ms), 95th percentile | 2130 | 4031 | +89.2% | +1429.1719 to +2371.1501 | yes: LOSS |
| response time (ms), 99th percentile | 2872 | 5535 | +92.7% | +1910.0274 to +3416.8168 | yes: LOSS |
| time over the response line (% of samples) | 22.76 | 39.05 | +71.6% | +10.6876 to +21.9037 | yes: LOSS |
| failed requests (%) | 0 | 0.1109 | +0.111 (native is 0) | −0.1192 to +0.3410 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 17.1 | +41.3% | +2.1990 to +7.8010 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 88.8 | +88.800 (native is 0) | +46.2236 to +131.3764 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.12 | 51.23 | +238.8% | +1.9142 to +70.3025 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03464 | 0.04019 | +16.0% | +0.0003 to +0.0108 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.663 | 1.781 | +7.1% | −0.0477 to +0.2849 | no |
| Omni's own CPU (cores), mean | 0 | 0.0546 | +0.055 (native is 0) | +0.0484 to +0.0608 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.663 | 1.836 | +10.4% | +0.0097 to +0.3367 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 674.4 | −12.9% | −184.6615 to −15.0117 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.043 | 5.078 | +25.6% | +0.3382 to +1.7321 | yes: power given |
| pods started | 0.4 | 4.1 | +925.0% | +2.2283 to +5.1717 | yes: power given |
| pod start wait, total (s) | 0.9 | 11.1 | +1133.3% | +5.9508 to +14.4492 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.42 | +245.7% | +0.7521 to +2.6874 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.78 | 64.97 | +27.9% | +12.0874 to +16.2910 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 865.7 | 1069 | +23.5% | +146.4287 to +260.9713 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.33 | −14.0% | −3.4332 to +0.0842 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 12.94 | +11842.3% | −6.3903 to +32.0486 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 75.1 | +14920.0% | −19.5077 to +168.7077 | no |
| queue: job turnaround, submitted to done, mean (s) | 174.2 | 356.7 | +104.7% | +131.0904 to +233.7846 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*