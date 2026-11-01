# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.99 | 11.33 |
| node-hours | 5.031 | 5.03 | 4.603 | 4.744 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.4 | 527.4 | 526.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.4 | 495.5 | 505.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 708.7 | 1039 | 745.3 | 1077 |
| response time (ms), 95th percentile | 2837 | 3672 | 3176 | 3965 |
| response time (ms), 99th percentile | 3884 | 4829 | 4229 | 5128 |
| time over the response line (% of samples) | 24.87 | 36.43 | 26.62 | 38.64 |
| failed requests (%) | 0.006803 | 0.07855 | 0.01463 | 0.04452 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 15.4 | 13.4 | 17.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 58.6 | 42.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.82 | 44.69 | 24.03 | 69.45 |
| utilisation (used / allocatable) | 0.03617 | 0.03682 | 0.04043 | 0.03853 |
| CPU used (cores), mean | 1.736 | 1.767 | 1.767 | 1.745 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01312 | 0.01289 |
| CPU used with Omni's own (cores), mean | 1.736 | 1.767 | 1.78 | 1.758 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 742.9 | 734.8 | 678.7 | 705 |
| HPA replicas, mean | 3.947 | 4.151 | 4.362 | 4.379 |
| pods started | 0.1 | 0.1 | 1 | 1.3 |
| pod start wait, total (s) | 0.3 | 0.2 | 1.6 | 2.5 |
| pod start wait, mean (s) | 0.3 | 0.2 | 0.5833 | 1.4 |
| host CPU busy, the real machine under kind (%) | 53.45 | 60.56 | 55.63 | 63.52 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 910 | 1042 | 939.4 | 1080 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.34 | 10.76 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 18.48 | 0.1375 | 17.02 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 92.1 | 0.8 | 97.6 |
| queue: job turnaround, submitted to done, mean (s) | 218.1 | 316.1 | 239.3 | 367.5 |
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
| worker nodes in service, mean | 12 | 11.33 | −5.6% | −1.6444 to +0.2987 | no |
| node-hours | 5.03 | 4.744 | −5.7% | −0.6981 to +0.1259 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 526.9 | −0.1% | −4.0507 to +2.9622 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 505.8 | −4.1% | −52.3695 to +9.0644 | no |
| response time (ms), mean | 1039 | 1077 | +3.7% | −41.5943 to +118.2826 | no |
| response time (ms), 95th percentile | 3672 | 3965 | +8.0% | −134.3867 to +721.4647 | no |
| response time (ms), 99th percentile | 4829 | 5128 | +6.2% | −299.3043 to +899.1075 | no |
| time over the response line (% of samples) | 36.43 | 38.64 | +6.1% | −0.0807 to +4.5069 | no |
| failed requests (%) | 0.07855 | 0.04452 | −43.3% | −0.1151 to +0.0470 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 17.1 | +11.0% | +0.0811 to +3.3189 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.4 | +42.400 (native is 0) | +18.9187 to +65.8813 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 44.69 | 69.45 | +55.4% | −49.2531 to +98.7831 | no |
| utilisation (used / allocatable) | 0.03682 | 0.03853 | +4.6% | −0.0048 to +0.0082 | no |
| CPU used (cores), mean | 1.767 | 1.745 | −1.3% | −0.2863 to +0.2419 | no |
| Omni's own CPU (cores), mean | 0 | 0.01289 | +0.013 (native is 0) | +0.0118 to +0.0140 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.767 | 1.758 | −0.5% | −0.2733 to +0.2547 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 734.8 | 705 | −4.1% | −147.0056 to +87.3050 | no |
| HPA replicas, mean | 4.151 | 4.379 | +5.5% | −0.2052 to +0.6616 | no |
| pods started | 0.1 | 1.3 | +1200.0% | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.5 | +1150.0% | +0.5462 to +4.0538 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.4 | +600.0% | +0.3370 to +2.0630 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.56 | 63.52 | +4.9% | +2.1434 to +3.7713 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1042 | 1080 | +3.6% | +21.5940 to +53.2060 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.76 | −10.3% | −2.9457 to +0.4715 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 18.48 | 17.02 | −7.9% | −26.7568 to +23.8484 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 92.1 | 97.6 | +6.0% | −105.3274 to +116.3274 | no |
| queue: job turnaround, submitted to done, mean (s) | 316.1 | 367.5 | +16.3% | +16.5058 to +86.3776 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.031 | 5.03 | −0.0% | −0.0126 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.4 | +0.0% | −1.9433 to +2.2928 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.4 | +0.0% | −1.9433 to +2.2928 | no |
| response time (ms), mean | 708.7 | 1039 | +46.6% | +171.7449 to +488.5748 | yes: LOSS |
| response time (ms), 95th percentile | 2837 | 3672 | +29.4% | +473.9218 to +1194.9992 | yes: LOSS |
| response time (ms), 99th percentile | 3884 | 4829 | +24.3% | +471.1765 to +1418.5815 | yes: LOSS |
| time over the response line (% of samples) | 24.87 | 36.43 | +46.5% | +7.3100 to +15.8000 | yes: LOSS |
| failed requests (%) | 0.006803 | 0.07855 | +1054.7% | −0.0420 to +0.1855 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 15.4 | +21.3% | +1.7433 to +3.6567 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.82 | 44.69 | +125.5% | −12.8754 to +62.6087 | no |
| utilisation (used / allocatable) | 0.03617 | 0.03682 | +1.8% | −0.0021 to +0.0034 | no |
| CPU used (cores), mean | 1.736 | 1.767 | +1.8% | −0.1022 to +0.1645 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.736 | 1.767 | +1.8% | −0.1022 to +0.1645 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 742.9 | 734.8 | −1.1% | −59.9255 to +43.8800 | no |
| HPA replicas, mean | 3.947 | 4.151 | +5.2% | +0.0288 to +0.3786 | yes: power given |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 53.45 | 60.56 | +13.3% | +4.9423 to +9.2958 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 910 | 1042 | +14.5% | +75.1129 to +189.0871 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 18.48 | +16957.7% | −0.7470 to +37.4887 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 92.1 | +13057.1% | −5.3986 to +188.1986 | no |
| queue: job turnaround, submitted to done, mean (s) | 218.1 | 316.1 | +44.9% | +52.5814 to +143.4186 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.99 | −8.4% | −2.3891 to +0.3655 | no |
| node-hours | 5.031 | 4.603 | −8.5% | −1.0008 to +0.1441 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.4 | +0.0% | −1.7006 to +1.9933 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 495.5 | −6.0% | −74.7926 to +11.2853 | no |
| response time (ms), mean | 708.7 | 745.3 | +5.2% | −3.6644 to +76.9699 | no |
| response time (ms), 95th percentile | 2837 | 3176 | +11.9% | +17.8978 to +659.2882 | yes: LOSS |
| response time (ms), 99th percentile | 3884 | 4229 | +8.9% | −160.4044 to +850.3172 | no |
| time over the response line (% of samples) | 24.87 | 26.62 | +7.0% | +0.3134 to +3.1921 | yes: LOSS |
| failed requests (%) | 0.006803 | 0.01463 | +115.0% | −0.0211 to +0.0367 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 13.4 | +5.5% | +0.3545 to +1.0455 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.6 | +58.600 (native is 0) | +27.3891 to +89.8109 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.82 | 24.03 | +21.2% | −8.6938 to +17.1105 | no |
| utilisation (used / allocatable) | 0.03617 | 0.04043 | +11.8% | −0.0007 to +0.0092 | no |
| CPU used (cores), mean | 1.736 | 1.767 | +1.7% | −0.0560 to +0.1167 | no |
| Omni's own CPU (cores), mean | 0 | 0.01312 | +0.013 (native is 0) | +0.0123 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.736 | 1.78 | +2.5% | −0.0430 to +0.1299 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 742.9 | 678.7 | −8.6% | −138.5469 to +10.1724 | no |
| HPA replicas, mean | 3.947 | 4.362 | +10.5% | −0.0496 to +0.8790 | no |
| pods started | 0.1 | 1 | +900.0% | −0.5086 to +2.3086 | no |
| pod start wait, total (s) | 0.3 | 1.6 | +433.3% | −1.3347 to +3.9347 | no |
| pod start wait, mean (s) | 0.3 | 0.5833 | +94.4% | −0.7158 to +1.2824 | no |
| host CPU busy, the real machine under kind (%) | 53.45 | 55.63 | +4.1% | +1.1962 to +3.1694 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 910 | 939.4 | +3.2% | +14.8879 to +43.9121 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.34 | −13.8% | −3.8286 to +0.5156 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.1375 | +26.9% | −0.0054 to +0.0637 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.8 | +14.3% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 218.1 | 239.3 | +9.8% | +10.8728 to +31.6689 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.99 | −8.4% | −2.3891 to +0.3655 | no |
| node-hours | 5.03 | 4.603 | −8.5% | −1.0026 to +0.1486 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 527.4 | −0.0% | −3.3845 to +3.3277 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 495.5 | −6.1% | −75.1516 to +11.2948 | no |
| response time (ms), mean | 1039 | 745.3 | −28.3% | −422.7723 to −164.2420 | yes: GAIN |
| response time (ms), 95th percentile | 3672 | 3176 | −13.5% | −919.9331 to −71.8019 | yes: GAIN |
| response time (ms), 99th percentile | 4829 | 4229 | −12.4% | −1244.0579 to +44.2127 | no |
| time over the response line (% of samples) | 36.43 | 26.62 | −26.9% | −13.5145 to −6.0899 | yes: GAIN |
| failed requests (%) | 0.07855 | 0.01463 | −81.4% | −0.1646 to +0.0367 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 13.4 | −13.0% | −2.9537 to −1.0463 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.6 | +58.600 (native is 0) | +27.3891 to +89.8109 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 44.69 | 24.03 | −46.2% | −60.9948 to +19.6782 | no |
| utilisation (used / allocatable) | 0.03682 | 0.04043 | +9.8% | −0.0024 to +0.0096 | no |
| CPU used (cores), mean | 1.767 | 1.767 | −0.0% | −0.1827 to +0.1811 | no |
| Omni's own CPU (cores), mean | 0 | 0.01312 | +0.013 (native is 0) | +0.0123 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.767 | 1.78 | +0.7% | −0.1696 to +0.1943 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 734.8 | 678.7 | −7.6% | −149.7485 to +37.4195 | no |
| HPA replicas, mean | 4.151 | 4.362 | +5.1% | −0.2602 to +0.6823 | no |
| pods started | 0.1 | 1 | +900.0% | −0.5086 to +2.3086 | no |
| pod start wait, total (s) | 0.2 | 1.6 | +700.0% | −1.1503 to +3.9503 | no |
| pod start wait, mean (s) | 0.2 | 0.5833 | +191.7% | −0.4389 to +1.2056 | no |
| host CPU busy, the real machine under kind (%) | 60.56 | 55.63 | −8.2% | −6.2694 to −3.6031 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1042 | 939.4 | −9.9% | −146.0036 to −59.3964 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.34 | −13.8% | −3.8286 to +0.5156 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 18.48 | 0.1375 | −99.3% | −37.4635 to +0.7802 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 92.1 | 0.8 | −99.1% | −188.1519 to +5.5519 | no |
| queue: job turnaround, submitted to done, mean (s) | 316.1 | 239.3 | −24.3% | −115.1380 to −38.3203 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.33 | −5.6% | −1.6444 to +0.2987 | no |
| node-hours | 5.031 | 4.744 | −5.7% | −0.6967 to +0.1218 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.9 | −0.1% | −2.8689 to +2.1299 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 505.8 | −4.1% | −52.0639 to +9.1082 | no |
| response time (ms), mean | 708.7 | 1077 | +52.0% | +194.5704 to +542.4378 | yes: LOSS |
| response time (ms), 95th percentile | 2837 | 3965 | +39.8% | +638.9462 to +1617.0528 | yes: LOSS |
| response time (ms), 99th percentile | 3884 | 5128 | +32.1% | +603.4436 to +1886.1176 | yes: LOSS |
| time over the response line (% of samples) | 24.87 | 38.64 | +55.4% | +9.7956 to +17.7407 | yes: LOSS |
| failed requests (%) | 0.006803 | 0.04452 | +554.5% | −0.0283 to +0.1037 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 17.1 | +34.6% | +2.1330 to +6.6670 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.4 | +42.400 (native is 0) | +18.9187 to +65.8813 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.82 | 69.45 | +250.4% | −9.1729 to +108.4362 | no |
| utilisation (used / allocatable) | 0.03617 | 0.03853 | +6.5% | −0.0028 to +0.0075 | no |
| CPU used (cores), mean | 1.736 | 1.745 | +0.5% | −0.1772 to +0.1950 | no |
| Omni's own CPU (cores), mean | 0 | 0.01289 | +0.013 (native is 0) | +0.0118 to +0.0140 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.736 | 1.758 | +1.3% | −0.1642 to +0.2078 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 742.9 | 705 | −5.1% | −135.8125 to +60.0665 | no |
| HPA replicas, mean | 3.947 | 4.379 | +10.9% | +0.0281 to +0.8357 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.1997 to +2.2003 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.5 | +733.3% | +0.1268 to +4.2732 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.4 | +366.7% | −0.1251 to +2.3251 | no |
| host CPU busy, the real machine under kind (%) | 53.45 | 63.52 | +18.9% | +8.2295 to +11.9232 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 910 | 1080 | +18.6% | +110.3456 to +228.6544 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.76 | −10.3% | −2.9457 to +0.4715 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 17.03 | +15615.4% | −1.4836 to +35.3169 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 97.6 | +13842.9% | +3.6034 to +190.1966 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 218.1 | 367.5 | +68.5% | +91.3030 to +207.5803 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*