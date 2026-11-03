# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.23 | 11.19 |
| node-hours | 5.033 | 5.028 | 4.704 | 4.687 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.2 | 526.6 | 526.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 526.2 | 502.5 | 501.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 724.4 | 971.1 | 834.9 | 1185 |
| response time (ms), 95th percentile | 2807 | 3407 | 3439 | 4193 |
| response time (ms), 99th percentile | 3680 | 4478 | 4562 | 5463 |
| time over the response line (% of samples) | 24.53 | 35.14 | 28.53 | 44.88 |
| failed requests (%) | 0.008264 | 0 | 0.04087 | 0.261 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 15.7 | 15.1 | 18.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 134.8 | 84.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 5.526 | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.8 | 55.09 | 30.46 | 83.78 |
| utilisation (used / allocatable) | 0.03608 | 0.03542 | 0.0386 | 0.03875 |
| CPU used (cores), mean | 1.732 | 1.7 | 1.741 | 1.731 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05875 | 0.05789 |
| CPU used with Omni's own (cores), mean | 1.732 | 1.7 | 1.8 | 1.789 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.4 | 759.2 | 703.5 | 706.8 |
| HPA replicas, mean | 4.095 | 4.153 | 5.12 | 5.036 |
| pods started | 0.2 | 0.1 | 4 | 3.6 |
| pod start wait, total (s) | 0.5 | 0.3 | 11 | 10.6 |
| pod start wait, mean (s) | 0.5 | 0.3 | 2.466 | 2.697 |
| host CPU busy, the real machine under kind (%) | 53.75 | 60.57 | 60.23 | 67.71 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 915.2 | 1032 | 971.7 | 1109 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.56 | 10.19 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 14.94 | 0.1583 | 24.13 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 79.5 | 0.7 | 123.7 |
| queue: job turnaround, submitted to done, mean (s) | 224.6 | 308.2 | 276.6 | 391.9 |
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
| worker nodes in service, mean | 12 | 11.19 | −6.8% | −1.6448 to +0.0228 | no |
| node-hours | 5.028 | 4.687 | −6.8% | −0.6862 to +0.0044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 526.9 | +0.1% | −3.5450 to +4.9667 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 501.4 | −4.7% | −50.2726 to +0.6568 | no |
| response time (ms), mean | 971.1 | 1185 | +22.0% | +101.8720 to +325.9590 | yes: LOSS |
| response time (ms), 95th percentile | 3407 | 4193 | +23.1% | +196.7880 to +1375.5410 | yes: LOSS |
| response time (ms), 99th percentile | 4478 | 5463 | +22.0% | +264.1764 to +1705.8918 | yes: LOSS |
| time over the response line (% of samples) | 35.14 | 44.88 | +27.7% | +3.7334 to +15.7495 | yes: LOSS |
| failed requests (%) | 0 | 0.261 | +0.261 (native is 0) | −0.1517 to +0.6738 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.7 | 18.8 | +19.7% | +1.0642 to +5.1358 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.4 | +84.400 (native is 0) | +61.1939 to +107.6061 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 55.09 | 83.78 | +52.1% | −64.2649 to +121.6482 | no |
| utilisation (used / allocatable) | 0.03542 | 0.03875 | +9.4% | −0.0038 to +0.0104 | no |
| CPU used (cores), mean | 1.7 | 1.731 | +1.8% | −0.2638 to +0.3262 | no |
| Omni's own CPU (cores), mean | 0 | 0.05789 | +0.058 (native is 0) | +0.0523 to +0.0635 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.7 | 1.789 | +5.2% | −0.2057 to +0.3838 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 759.2 | 706.8 | −6.9% | −192.4698 to +87.7276 | no |
| HPA replicas, mean | 4.153 | 5.036 | +21.3% | +0.5640 to +1.2022 | yes: power given |
| pods started | 0.1 | 3.6 | +3500.0% | +2.0995 to +4.9005 | yes: power given |
| pod start wait, total (s) | 0.3 | 10.6 | +3433.3% | +6.1695 to +14.4305 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.697 | +798.9% | +1.4614 to +3.3320 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.57 | 67.71 | +11.8% | +5.8308 to +8.4528 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1032 | 1109 | +7.5% | +48.7734 to +106.0266 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.19 | −15.1% | −3.6271 to +0.0125 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 14.94 | 24.13 | +61.5% | −18.1713 to +36.5463 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 79.5 | 123.7 | +55.6% | −100.2676 to +188.6676 | no |
| queue: job turnaround, submitted to done, mean (s) | 308.2 | 391.9 | +27.1% | +43.5388 to +123.7279 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.033 | 5.028 | −0.1% | −0.0208 to +0.0108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.2 | −0.2% | −3.2703 to +1.2527 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 526.2 | −0.2% | −3.2703 to +1.2527 | no |
| response time (ms), mean | 724.4 | 971.1 | +34.1% | +106.9691 to +386.4236 | yes: LOSS |
| response time (ms), 95th percentile | 2807 | 3407 | +21.4% | +172.1962 to +1028.3278 | yes: LOSS |
| response time (ms), 99th percentile | 3680 | 4478 | +21.7% | +278.4481 to +1318.6617 | yes: LOSS |
| time over the response line (% of samples) | 24.53 | 35.14 | +43.3% | +7.1248 to +14.1106 | yes: LOSS |
| failed requests (%) | 0.008264 | 0 | −100.0% | −0.0270 to +0.0104 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 15.7 | +30.8% | +2.4361 to +4.9639 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.8 | 55.09 | +152.7% | −5.7642 to +72.3476 | no |
| utilisation (used / allocatable) | 0.03608 | 0.03542 | −1.8% | −0.0034 to +0.0021 | no |
| CPU used (cores), mean | 1.732 | 1.7 | −1.8% | −0.1641 to +0.1001 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.732 | 1.7 | −1.8% | −0.1641 to +0.1001 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.4 | 759.2 | +1.8% | −47.7074 to +75.1712 | no |
| HPA replicas, mean | 4.095 | 4.153 | +1.4% | −0.3011 to +0.4179 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.5 | 0.3 | −40.0% | −1.3081 to +0.9081 | no |
| pod start wait, mean (s) | 0.5 | 0.3 | −40.0% | −1.3081 to +0.9081 | no |
| host CPU busy, the real machine under kind (%) | 53.75 | 60.57 | +12.7% | +4.6379 to +8.9984 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 915.2 | 1032 | +12.7% | +54.8252 to +178.3748 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 14.94 | +9591.9% | −3.7219 to +33.2969 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 79.5 | +9837.5% | −20.8063 to +178.2063 | no |
| queue: job turnaround, submitted to done, mean (s) | 224.6 | 308.2 | +37.2% | +32.7121 to +134.4545 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.23 | −6.4% | −1.6403 to +0.1046 | no |
| node-hours | 5.033 | 4.704 | −6.5% | −0.7023 to +0.0435 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.6 | −0.1% | −3.1706 to +2.0544 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 502.5 | −4.7% | −53.1589 to +3.8802 | no |
| response time (ms), mean | 724.4 | 834.9 | +15.3% | −13.3750 to +234.3437 | no |
| response time (ms), 95th percentile | 2807 | 3439 | +22.5% | +71.9374 to +1192.6616 | yes: LOSS |
| response time (ms), 99th percentile | 3680 | 4562 | +24.0% | +181.1850 to +1583.1726 | yes: LOSS |
| time over the response line (% of samples) | 24.53 | 28.53 | +16.3% | +1.5560 to +6.4486 | yes: LOSS |
| failed requests (%) | 0.008264 | 0.04087 | +394.5% | −0.0321 to +0.0973 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 15.1 | +25.8% | +0.5001 to +5.6999 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.8 | +134.800 (native is 0) | +65.2791 to +204.3209 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.8 | 30.46 | +39.7% | −3.0614 to +20.3814 | no |
| utilisation (used / allocatable) | 0.03608 | 0.0386 | +7.0% | −0.0004 to +0.0054 | no |
| CPU used (cores), mean | 1.732 | 1.741 | +0.5% | −0.0929 to +0.1115 | no |
| Omni's own CPU (cores), mean | 0 | 0.05875 | +0.059 (native is 0) | +0.0535 to +0.0640 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.732 | 1.8 | +3.9% | −0.0355 to +0.1715 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.4 | 703.5 | −5.6% | −87.5700 to +3.7944 | no |
| HPA replicas, mean | 4.095 | 5.12 | +25.0% | +0.6354 to +1.4151 | yes: power given |
| pods started | 0.2 | 4 | +1900.0% | +1.9904 to +5.6096 | yes: power given |
| pod start wait, total (s) | 0.5 | 11 | +2100.0% | +4.4656 to +16.5344 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 2.466 | +393.1% | +1.0552 to +2.8759 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.75 | 60.23 | +12.1% | +4.8021 to +8.1722 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 915.2 | 971.7 | +6.2% | +15.5581 to +97.4419 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.56 | −12.0% | −3.0552 to +0.1708 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.1583 | +2.7% | −0.0562 to +0.0645 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 | −12.5% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 224.6 | 276.6 | +23.1% | +15.7638 to +88.1029 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.23 | −6.4% | −1.6403 to +0.1046 | no |
| node-hours | 5.028 | 4.704 | −6.5% | −0.6894 to +0.0405 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 526.6 | +0.1% | −3.2503 to +4.1517 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 502.5 | −4.5% | −52.0648 to +4.8037 | no |
| response time (ms), mean | 971.1 | 834.9 | −14.0% | −224.7682 to −47.6557 | yes: GAIN |
| response time (ms), 95th percentile | 3407 | 3439 | +0.9% | −443.8387 to +507.9137 | no |
| response time (ms), 99th percentile | 4478 | 4562 | +1.9% | −453.6824 to +620.9302 | no |
| time over the response line (% of samples) | 35.14 | 28.53 | −18.8% | −10.6428 to −2.5881 | yes: GAIN |
| failed requests (%) | 0 | 0.04087 | +0.041 (native is 0) | −0.0179 to +0.0996 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.7 | 15.1 | −3.8% | −2.1526 to +0.9526 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.8 | +134.800 (native is 0) | +65.2791 to +204.3209 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 55.09 | 30.46 | −44.7% | −68.7644 to +19.5011 | no |
| utilisation (used / allocatable) | 0.03542 | 0.0386 | +9.0% | −0.0011 to +0.0075 | no |
| CPU used (cores), mean | 1.7 | 1.741 | +2.4% | −0.1688 to +0.2513 | no |
| Omni's own CPU (cores), mean | 0 | 0.05875 | +0.059 (native is 0) | +0.0535 to +0.0640 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.7 | 1.8 | +5.9% | −0.1120 to +0.3120 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 759.2 | 703.5 | −7.3% | −133.8718 to +22.6324 | no |
| HPA replicas, mean | 4.153 | 5.12 | +23.3% | +0.4625 to +1.4713 | yes: power given |
| pods started | 0.1 | 4 | +3900.0% | +1.9498 to +5.8502 | yes: power given |
| pod start wait, total (s) | 0.3 | 11 | +3566.7% | +4.2839 to +17.1161 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.466 | +721.9% | +1.0093 to +3.3218 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.57 | 60.23 | −0.5% | −1.4328 to +0.7707 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1032 | 971.7 | −5.8% | −87.4868 to −32.7132 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.56 | −12.0% | −3.0552 to +0.1708 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 14.94 | 0.1583 | −98.9% | −33.2875 to +3.7208 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 79.5 | 0.7 | −99.1% | −178.2616 to +20.6616 | no |
| queue: job turnaround, submitted to done, mean (s) | 308.2 | 276.6 | −10.3% | −52.4589 to −10.8411 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.19 | −6.8% | −1.6448 to +0.0228 | no |
| node-hours | 5.033 | 4.687 | −6.9% | −0.6958 to +0.0040 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.9 | −0.1% | −4.2523 to +3.6564 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 501.4 | −4.9% | −51.1214 to −0.5120 | yes: GAIN |
| response time (ms), mean | 724.4 | 1185 | +63.6% | +251.0433 to +670.1803 | yes: LOSS |
| response time (ms), 95th percentile | 2807 | 4193 | +49.4% | +548.2401 to +2224.6129 | yes: LOSS |
| response time (ms), 99th percentile | 3680 | 5463 | +48.5% | +733.2527 to +2833.9253 | yes: LOSS |
| time over the response line (% of samples) | 24.53 | 44.88 | +83.0% | +16.2809 to +24.4374 | yes: LOSS |
| failed requests (%) | 0.008264 | 0.261 | +3058.7% | −0.1634 to +0.6689 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 18.8 | +56.7% | +3.8258 to +9.7742 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.4 | +84.400 (native is 0) | +61.1939 to +107.6061 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.8 | 83.78 | +284.4% | −13.8720 to +137.8387 | no |
| utilisation (used / allocatable) | 0.03608 | 0.03875 | +7.4% | −0.0041 to +0.0094 | no |
| CPU used (cores), mean | 1.732 | 1.731 | −0.0% | −0.2546 to +0.2530 | no |
| Omni's own CPU (cores), mean | 0 | 0.05789 | +0.058 (native is 0) | +0.0523 to +0.0635 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.732 | 1.789 | +3.3% | −0.1952 to +0.3094 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.4 | 706.8 | −5.2% | −172.1998 to +94.9214 | no |
| HPA replicas, mean | 4.095 | 5.036 | +23.0% | +0.5712 to +1.3118 | yes: power given |
| pods started | 0.2 | 3.6 | +1700.0% | +1.8845 to +4.9155 | yes: power given |
| pod start wait, total (s) | 0.5 | 10.6 | +2020.0% | +5.6208 to +14.5792 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 2.697 | +439.3% | +1.1635 to +3.2298 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.75 | 67.71 | +26.0% | +11.9743 to +15.9457 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 915.2 | 1109 | +21.2% | +130.5250 to +257.4750 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.19 | −15.1% | −3.6271 to +0.0125 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 24.13 | +15551.4% | −0.5888 to +48.5388 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 123.7 | +15362.5% | +4.7145 to +241.0855 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 224.6 | 391.9 | +74.4% | +123.1957 to +211.2376 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*