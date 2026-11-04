# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.24 | 11.51 |
| node-hours | 5.03 | 5.026 | 4.708 | 4.827 |
| energy, parked workers still on at idle power (Wh, declared model) | 528.5 | 528.6 | 527.9 | 527.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.5 | 528.6 | 504.2 | 512.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 868.3 | 1121 | 994.7 | 1211 |
| response time (ms), 95th percentile | 3593 | 5012 | 4258 | 5472 |
| response time (ms), 99th percentile | 4813 | 6650 | 5759 | 7177 |
| time over the response line (% of samples) | 31.78 | 33.37 | 34.29 | 38.95 |
| failed requests (%) | 0 | 0.06418 | 0.02303 | 0.3481 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 17.3 | 15.9 | 18.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 95.5 | 77.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 13.33 | 8.333 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.82 | 36.45 | 37.07 | 91.85 |
| utilisation (used / allocatable) | 0.03815 | 0.03905 | 0.04067 | 0.038 |
| CPU used (cores), mean | 1.831 | 1.875 | 1.829 | 1.743 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05986 | 0.05062 |
| CPU used with Omni's own (cores), mean | 1.831 | 1.875 | 1.889 | 1.794 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.4 | 693.4 | 666.2 | 710.8 |
| HPA replicas, mean | 4.145 | 4.079 | 4.92 | 5.902 |
| pods started | 0.1 | 0.1 | 4 | 5.5 |
| pod start wait, total (s) | 0.2 | 0.2 | 10.6 | 15.3 |
| pod start wait, mean (s) | 0.2 | 0.2 | 2.517 | 2.751 |
| host CPU busy, the real machine under kind (%) | 55.93 | 63.3 | 62.65 | 69.79 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 956.1 | 1100 | 1020 | 1163 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.7 | 11.24 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 7.446 | 0.1667 | 15.43 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 34.6 | 0.9 | 129.2 |
| queue: job turnaround, submitted to done, mean (s) | 260.7 | 400.6 | 317.7 | 468.9 |
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
| worker nodes in service, mean | 12 | 11.51 | −4.1% | −1.5819 to +0.6085 | no |
| node-hours | 5.026 | 4.827 | −4.0% | −0.6586 to +0.2612 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.6 | 527.4 | −0.2% | −4.5901 to +2.2169 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.6 | 512.2 | −3.1% | −50.3564 to +17.5249 | no |
| response time (ms), mean | 1121 | 1211 | +8.0% | −21.2499 to +201.2515 | no |
| response time (ms), 95th percentile | 5012 | 5472 | +9.2% | −312.0146 to +1233.0666 | no |
| response time (ms), 99th percentile | 6650 | 7177 | +7.9% | −136.0074 to +1189.4214 | no |
| time over the response line (% of samples) | 33.37 | 38.95 | +16.7% | +3.1344 to +8.0302 | yes: LOSS |
| failed requests (%) | 0.06418 | 0.3481 | +442.4% | −0.1241 to +0.6919 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.3 | 18.4 | +6.4% | +0.6940 to +1.5060 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 77.6 | +77.600 (native is 0) | +18.3947 to +136.8053 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 36.45 | 91.85 | +152.0% | −5.6196 to +116.4063 | no |
| utilisation (used / allocatable) | 0.03905 | 0.038 | −2.7% | −0.0073 to +0.0052 | no |
| CPU used (cores), mean | 1.875 | 1.743 | −7.0% | −0.3438 to +0.0811 | no |
| Omni's own CPU (cores), mean | 0 | 0.05062 | +0.051 (native is 0) | +0.0447 to +0.0566 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.875 | 1.794 | −4.3% | −0.2921 to +0.1308 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.4 | 710.8 | +2.5% | −96.3162 to +131.1732 | no |
| HPA replicas, mean | 4.079 | 5.902 | +44.7% | +0.7915 to +2.8540 | yes: power given |
| pods started | 0.1 | 5.5 | +5400.0% | +4.2715 to +6.5285 | yes: power given |
| pod start wait, total (s) | 0.2 | 15.3 | +7550.0% | +11.0473 to +19.1527 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.751 | +1275.6% | +1.9897 to +3.1125 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 63.3 | 69.79 | +10.2% | +5.8172 to +7.1519 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1100 | 1163 | +5.8% | +43.6177 to +82.9823 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.24 | −6.4% | −2.4758 to +0.9476 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.446 | 15.43 | +107.2% | +1.0947 to +14.8720 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.6 | 129.2 | +273.4% | −14.9073 to +204.1073 | no |
| queue: job turnaround, submitted to done, mean (s) | 400.6 | 468.9 | +17.0% | +49.9421 to +86.6579 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.03 | 5.026 | −0.1% | −0.0145 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.5 | 528.6 | +0.0% | −2.1312 to +2.4028 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.5 | 528.6 | +0.0% | −2.1312 to +2.4028 | no |
| response time (ms), mean | 868.3 | 1121 | +29.1% | +140.8912 to +364.5018 | yes: LOSS |
| response time (ms), 95th percentile | 3593 | 5012 | +39.5% | +891.5828 to +1946.3162 | yes: LOSS |
| response time (ms), 99th percentile | 4813 | 6650 | +38.2% | +1301.1971 to +2372.5849 | yes: LOSS |
| time over the response line (% of samples) | 31.78 | 33.37 | +5.0% | −1.3659 to +4.5528 | no |
| failed requests (%) | 0 | 0.06418 | +0.064 (native is 0) | +0.0055 to +0.1228 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 17.3 | +16.1% | +1.6311 to +3.1689 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.82 | 36.45 | +104.5% | −3.7688 to +41.0321 | no |
| utilisation (used / allocatable) | 0.03815 | 0.03905 | +2.4% | −0.0012 to +0.0030 | no |
| CPU used (cores), mean | 1.831 | 1.875 | +2.4% | −0.0553 to +0.1416 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.831 | 1.875 | +2.4% | −0.0553 to +0.1416 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.4 | 693.4 | −1.6% | −44.3981 to +22.4516 | no |
| HPA replicas, mean | 4.145 | 4.079 | −1.6% | −0.3030 to +0.1722 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 55.93 | 63.3 | +13.2% | +5.7902 to +8.9591 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 956.1 | 1100 | +15.0% | +98.2936 to +188.7064 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 7.446 | +4602.6% | +0.4311 to +14.1439 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 34.6 | +3744.4% | −39.2645 to +106.6645 | no |
| queue: job turnaround, submitted to done, mean (s) | 260.7 | 400.6 | +53.7% | +96.9095 to +182.9738 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.24 | −6.3% | −1.9815 to +0.4705 | no |
| node-hours | 5.03 | 4.708 | −6.4% | −0.8333 to +0.1877 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.5 | 527.9 | −0.1% | −1.8744 to +0.7315 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.5 | 504.2 | −4.6% | −62.5491 to +13.9896 | no |
| response time (ms), mean | 868.3 | 994.7 | +14.6% | +50.0529 to +202.7375 | yes: LOSS |
| response time (ms), 95th percentile | 3593 | 4258 | +18.5% | +259.9807 to +1069.4343 | yes: LOSS |
| response time (ms), 99th percentile | 4813 | 5759 | +19.7% | +383.1717 to +1509.2177 | yes: LOSS |
| time over the response line (% of samples) | 31.78 | 34.29 | +7.9% | +0.8551 to +4.1800 | yes: LOSS |
| failed requests (%) | 0 | 0.02303 | +0.023 (native is 0) | −0.0035 to +0.0496 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 15.9 | +6.7% | +0.5231 to +1.4769 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.5 | +95.500 (native is 0) | +40.8402 to +150.1598 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.82 | 37.07 | +108.0% | −1.0257 to +39.5290 | no |
| utilisation (used / allocatable) | 0.03815 | 0.04067 | +6.6% | −0.0015 to +0.0065 | no |
| CPU used (cores), mean | 1.831 | 1.829 | −0.1% | −0.0765 to +0.0714 | no |
| Omni's own CPU (cores), mean | 0 | 0.05986 | +0.060 (native is 0) | +0.0560 to +0.0637 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.831 | 1.889 | +3.1% | −0.0181 to +0.1328 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.4 | 666.2 | −5.4% | −103.1182 to +26.8551 | no |
| HPA replicas, mean | 4.145 | 4.92 | +18.7% | +0.4582 to +1.0920 | yes: power given |
| pods started | 0.1 | 4 | +3900.0% | +2.3023 to +5.4977 | yes: power given |
| pod start wait, total (s) | 0.2 | 10.6 | +5200.0% | +5.2728 to +15.5272 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.517 | +1158.7% | +1.6249 to +3.0098 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.93 | 62.65 | +12.0% | +5.5768 to +7.8658 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 956.1 | 1020 | +6.7% | +39.1430 to +88.6570 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.7 | −10.8% | −3.0708 to +0.4671 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.1667 | +5.3% | −0.0493 to +0.0659 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 260.7 | 317.7 | +21.9% | +35.6296 to +78.4704 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.24 | −6.3% | −1.9815 to +0.4705 | no |
| node-hours | 5.026 | 4.708 | −6.3% | −0.8295 to +0.1933 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.6 | 527.9 | −0.1% | −2.8571 to +1.4427 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.6 | 504.2 | −4.6% | −62.7014 to +13.8703 | no |
| response time (ms), mean | 1121 | 994.7 | −11.3% | −218.7900 to −33.8127 | yes: GAIN |
| response time (ms), 95th percentile | 5012 | 4258 | −15.0% | −1250.6161 to −257.8679 | yes: GAIN |
| response time (ms), 99th percentile | 6650 | 5759 | −13.4% | −1532.3519 to −249.0407 | yes: GAIN |
| time over the response line (% of samples) | 33.37 | 34.29 | +2.8% | −0.6697 to +2.5180 | no |
| failed requests (%) | 0.06418 | 0.02303 | −64.1% | −0.1075 to +0.0252 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.3 | 15.9 | −8.1% | −1.9001 to −0.8999 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.5 | +95.500 (native is 0) | +40.8402 to +150.1598 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 36.45 | 37.07 | +1.7% | −29.1468 to +30.3868 | no |
| utilisation (used / allocatable) | 0.03905 | 0.04067 | +4.1% | −0.0031 to +0.0064 | no |
| CPU used (cores), mean | 1.875 | 1.829 | −2.4% | −0.1665 to +0.0751 | no |
| Omni's own CPU (cores), mean | 0 | 0.05986 | +0.060 (native is 0) | +0.0560 to +0.0637 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.875 | 1.889 | +0.8% | −0.1075 to +0.1358 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.4 | 666.2 | −3.9% | −104.3542 to +50.0375 | no |
| HPA replicas, mean | 4.079 | 4.92 | +20.6% | +0.5513 to +1.1298 | yes: power given |
| pods started | 0.1 | 4 | +3900.0% | +2.3023 to +5.4977 | yes: power given |
| pod start wait, total (s) | 0.2 | 10.6 | +5200.0% | +5.2728 to +15.5272 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.517 | +1158.7% | +1.6249 to +3.0098 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 63.3 | 62.65 | −1.0% | −1.3402 to +0.0336 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1100 | 1020 | −7.2% | −103.8390 to −55.3610 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.7 | −10.8% | −3.0708 to +0.4671 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.446 | 0.1667 | −97.8% | −14.1356 to −0.4227 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.6 | 0.9 | −97.4% | −106.6645 to +39.2645 | no |
| queue: job turnaround, submitted to done, mean (s) | 400.6 | 317.7 | −20.7% | −107.8325 to −57.9508 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.51 | −4.1% | −1.5819 to +0.6085 | no |
| node-hours | 5.03 | 4.827 | −4.0% | −0.6629 to +0.2561 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.5 | 527.4 | −0.2% | −3.8649 to +1.7633 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.5 | 512.2 | −3.1% | −50.2315 to +17.6716 | no |
| response time (ms), mean | 868.3 | 1211 | +39.5% | +211.7710 to +473.6237 | yes: LOSS |
| response time (ms), 95th percentile | 3593 | 5472 | +52.3% | +1158.5101 to +2600.4409 | yes: LOSS |
| response time (ms), 99th percentile | 4813 | 7177 | +49.1% | +1558.6672 to +3168.5288 | yes: LOSS |
| time over the response line (% of samples) | 31.78 | 38.95 | +22.6% | +2.7337 to +11.6178 | yes: LOSS |
| failed requests (%) | 0 | 0.3481 | +0.348 (native is 0) | −0.0394 to +0.7356 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 18.4 | +23.5% | +2.5315 to +4.4685 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 77.6 | +77.600 (native is 0) | +18.3947 to +136.8053 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.82 | 91.85 | +415.4% | +18.5403 to +129.5097 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03815 | 0.038 | −0.4% | −0.0058 to +0.0055 | no |
| CPU used (cores), mean | 1.831 | 1.743 | −4.8% | −0.2706 to +0.0944 | no |
| Omni's own CPU (cores), mean | 0 | 0.05062 | +0.051 (native is 0) | +0.0447 to +0.0566 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.831 | 1.794 | −2.0% | −0.2190 to +0.1440 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.4 | 710.8 | +0.9% | −98.0689 to +110.9794 | no |
| HPA replicas, mean | 4.145 | 5.902 | +42.4% | +0.8126 to +2.7022 | yes: power given |
| pods started | 0.1 | 5.5 | +5400.0% | +4.1293 to +6.6707 | yes: power given |
| pod start wait, total (s) | 0.2 | 15.3 | +7550.0% | +10.8022 to +19.3978 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.751 | +1275.6% | +2.0210 to +3.0812 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.93 | 69.79 | +24.8% | +12.1134 to +15.6050 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 956.1 | 1163 | +21.6% | +147.7528 to +265.8472 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.24 | −6.4% | −2.4758 to +0.9476 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 15.43 | +9644.7% | +6.8336 to +23.7081 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 129.2 | +14255.6% | +11.9492 to +244.6508 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 260.7 | 468.9 | +79.9% | +150.0013 to +266.4820 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*