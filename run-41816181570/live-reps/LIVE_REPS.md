# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.92 | 11.58 |
| node-hours | 5.026 | 5.025 | 4.571 | 4.857 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 526.6 | 526.2 | 527.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 526.6 | 492.4 | 514.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 756.3 | 1046 | 857.9 | 1247 |
| response time (ms), 95th percentile | 2938 | 3606 | 3443 | 4271 |
| response time (ms), 99th percentile | 3840 | 4689 | 4696 | 5732 |
| time over the response line (% of samples) | 24.57 | 36.32 | 28.59 | 43.09 |
| failed requests (%) | 0 | 0.01753 | 0 | 0.3404 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 15.6 | 14.4 | 18.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 145 | 101.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 15.42 | 15.83 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.07 | 49.57 | 41.28 | 69.4 |
| utilisation (used / allocatable) | 0.03642 | 0.03666 | 0.03952 | 0.03743 |
| CPU used (cores), mean | 1.748 | 1.759 | 1.721 | 1.733 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05921 | 0.06047 |
| CPU used with Omni's own (cores), mean | 1.748 | 1.759 | 1.78 | 1.794 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.8 | 735.2 | 691.6 | 726.7 |
| HPA replicas, mean | 4.063 | 4.031 | 5.446 | 5.612 |
| pods started | 0.3 | 0 | 2.7 | 4.1 |
| pod start wait, total (s) | 0.8 | 0 | 6.7 | 11.5 |
| pod start wait, mean (s) | 0.8 | 0 | 2.215 | 2.913 |
| host CPU busy, the real machine under kind (%) | 54.28 | 61.49 | 60.85 | 68.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 924.1 | 1052 | 978.4 | 1118 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.963 | 11.02 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 17.64 | 0.1792 | 25.17 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 118.3 | 0.6 | 137.3 |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 323.6 | 282.2 | 390.5 |
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
| worker nodes in service, mean | 12 | 11.58 | −3.5% | −0.9179 to +0.0706 | no |
| node-hours | 5.025 | 4.857 | −3.3% | −0.3715 to +0.0356 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.6 | 527.6 | +0.2% | −2.4672 to +4.5362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.6 | 514.3 | −2.3% | −26.8670 to +2.2984 | no |
| response time (ms), mean | 1046 | 1247 | +19.2% | +45.1960 to +355.7783 | yes: LOSS |
| response time (ms), 95th percentile | 3606 | 4271 | +18.5% | +134.2417 to +1196.5193 | yes: LOSS |
| response time (ms), 99th percentile | 4689 | 5732 | +22.3% | +377.2577 to +1709.6841 | yes: LOSS |
| time over the response line (% of samples) | 36.32 | 43.09 | +18.6% | +3.5014 to +10.0390 | yes: LOSS |
| failed requests (%) | 0.01753 | 0.3404 | +1841.9% | −0.2099 to +0.8557 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.6 | 18.4 | +17.9% | +0.3966 to +5.2034 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.5 | +101.500 (native is 0) | +57.6677 to +145.3323 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 49.57 | 69.4 | +40.0% | −44.2890 to +83.9590 | no |
| utilisation (used / allocatable) | 0.03666 | 0.03743 | +2.1% | −0.0053 to +0.0068 | no |
| CPU used (cores), mean | 1.759 | 1.733 | −1.5% | −0.2949 to +0.2424 | no |
| Omni's own CPU (cores), mean | 0 | 0.06047 | +0.060 (native is 0) | +0.0560 to +0.0650 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.759 | 1.794 | +1.9% | −0.2337 to +0.3021 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 735.2 | 726.7 | −1.2% | −124.3017 to +107.1790 | no |
| HPA replicas, mean | 4.031 | 5.612 | +39.2% | +0.6334 to +2.5280 | yes: power given |
| pods started | 0 | 4.1 | +4.100 (native is 0) | +2.5383 to +5.6617 | yes: power given |
| pod start wait, total (s) | 0 | 11.5 | +11.500 (native is 0) | +6.8490 to +16.1510 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.913 | +2.913 (native is 0) | +2.1716 to +3.6541 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.49 | 68.27 | +11.0% | +5.8720 to +7.6901 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1052 | 1118 | +6.3% | +40.8096 to +91.5904 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.02 | −8.2% | −2.1560 to +0.1886 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 17.64 | 25.17 | +42.7% | −7.6443 to +22.7026 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 118.3 | 137.3 | +16.1% | −66.2860 to +104.2860 | no |
| queue: job turnaround, submitted to done, mean (s) | 323.6 | 390.5 | +20.7% | +33.1670 to +100.6747 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.026 | 5.025 | −0.0% | −0.0201 to +0.0181 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 526.6 | −0.0% | −3.0029 to +2.5951 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 526.6 | −0.0% | −3.0029 to +2.5951 | no |
| response time (ms), mean | 756.3 | 1046 | +38.4% | +134.4045 to +445.9294 | yes: LOSS |
| response time (ms), 95th percentile | 2938 | 3606 | +22.7% | +272.3658 to +1062.6542 | yes: LOSS |
| response time (ms), 99th percentile | 3840 | 4689 | +22.1% | +320.6845 to +1376.9329 | yes: LOSS |
| time over the response line (% of samples) | 24.57 | 36.32 | +47.8% | +7.4019 to +16.0938 | yes: LOSS |
| failed requests (%) | 0 | 0.01753 | +0.018 (native is 0) | −0.0090 to +0.0441 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 15.6 | +26.8% | +1.2200 to +5.3800 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.07 | 49.57 | +135.3% | −14.4376 to +71.4342 | no |
| utilisation (used / allocatable) | 0.03642 | 0.03666 | +0.6% | −0.0033 to +0.0037 | no |
| CPU used (cores), mean | 1.748 | 1.759 | +0.6% | −0.1575 to +0.1797 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.748 | 1.759 | +0.6% | −0.1575 to +0.1797 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.8 | 735.2 | −1.3% | −76.1287 to +56.9109 | no |
| HPA replicas, mean | 4.063 | 4.031 | −0.8% | −0.2376 to +0.1741 | no |
| pods started | 0.3 | 0 | −100.0% | −0.6455 to +0.0455 | no |
| pod start wait, total (s) | 0.8 | 0 | −100.0% | −1.7417 to +0.1417 | no |
| pod start wait, mean (s) | 0.8 | 0 | −100.0% | −1.7417 to +0.1417 | no |
| host CPU busy, the real machine under kind (%) | 54.28 | 61.49 | +13.3% | +5.5533 to +8.8613 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924.1 | 1052 | +13.8% | +67.6567 to +187.7433 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 17.64 | +14496.6% | −0.0711 to +35.1044 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 118.3 | +16800.0% | +7.2791 to +227.9209 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 323.6 | +40.9% | +49.2358 to +138.7559 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.92 | −9.0% | −2.2599 to +0.1082 | no |
| node-hours | 5.026 | 4.571 | −9.1% | −0.9477 to +0.0377 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 526.2 | −0.1% | −2.5490 to +1.3750 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 492.4 | −6.5% | −70.7300 to +1.9060 | no |
| response time (ms), mean | 756.3 | 857.9 | +13.4% | −1.7172 to +204.8540 | no |
| response time (ms), 95th percentile | 2938 | 3443 | +17.2% | +137.5620 to +872.0390 | yes: LOSS |
| response time (ms), 99th percentile | 3840 | 4696 | +22.3% | +280.8882 to +1431.5912 | yes: LOSS |
| time over the response line (% of samples) | 24.57 | 28.59 | +16.4% | +2.4321 to +5.6117 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 14.4 | +17.1% | +0.0091 to +4.1909 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 145 | +145.000 (native is 0) | +64.0933 to +225.9067 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.07 | 41.28 | +95.9% | −1.4922 to +41.9222 | no |
| utilisation (used / allocatable) | 0.03642 | 0.03952 | +8.5% | −0.0022 to +0.0084 | no |
| CPU used (cores), mean | 1.748 | 1.721 | −1.6% | −0.1241 to +0.0698 | no |
| Omni's own CPU (cores), mean | 0 | 0.05921 | +0.059 (native is 0) | +0.0554 to +0.0630 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.748 | 1.78 | +1.8% | −0.0644 to +0.1285 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.8 | 691.6 | −7.1% | −143.7519 to +37.2700 | no |
| HPA replicas, mean | 4.063 | 5.446 | +34.0% | +0.3740 to +2.3921 | yes: power given |
| pods started | 0.3 | 2.7 | +800.0% | +1.0428 to +3.7572 | yes: power given |
| pod start wait, total (s) | 0.8 | 6.7 | +737.5% | +2.1232 to +9.6768 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 2.215 | +176.9% | +0.2044 to +2.6256 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.28 | 60.85 | +12.1% | +5.1532 to +7.9753 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924.1 | 978.4 | +5.9% | +20.2245 to +88.3755 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.963 | −17.0% | −4.0972 to +0.0228 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.1792 | +48.3% | −0.0226 to +0.1393 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 282.2 | +22.9% | +22.7151 to +82.5932 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.92 | −9.0% | −2.2599 to +0.1082 | no |
| node-hours | 5.025 | 4.571 | −9.0% | −0.9505 to +0.0425 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.6 | 526.2 | −0.1% | −2.6123 to +1.8462 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.6 | 492.4 | −6.5% | −71.6041 to +3.1879 | no |
| response time (ms), mean | 1046 | 857.9 | −18.0% | −292.8057 to −84.3914 | yes: GAIN |
| response time (ms), 95th percentile | 3606 | 3443 | −4.5% | −460.0500 to +134.6310 | no |
| response time (ms), 99th percentile | 4689 | 4696 | +0.2% | −436.5491 to +451.4111 | no |
| time over the response line (% of samples) | 36.32 | 28.59 | −21.3% | −10.7623 to −4.6897 | yes: GAIN |
| failed requests (%) | 0.01753 | 0 | −100.0% | −0.0441 to +0.0090 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.6 | 14.4 | −7.7% | −2.3583 to −0.0417 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 145 | +145.000 (native is 0) | +64.0933 to +225.9067 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 49.57 | 41.28 | −16.7% | −45.4431 to +28.8764 | no |
| utilisation (used / allocatable) | 0.03666 | 0.03952 | +7.8% | −0.0019 to +0.0076 | no |
| CPU used (cores), mean | 1.759 | 1.721 | −2.2% | −0.1682 to +0.0917 | no |
| Omni's own CPU (cores), mean | 0 | 0.05921 | +0.059 (native is 0) | +0.0554 to +0.0630 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.759 | 1.78 | +1.2% | −0.1106 to +0.1525 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 735.2 | 691.6 | −5.9% | −116.5262 to +29.2621 | no |
| HPA replicas, mean | 4.031 | 5.446 | +35.1% | +0.4100 to +2.4197 | yes: power given |
| pods started | 0 | 2.7 | +2.700 (native is 0) | +1.4819 to +3.9181 | yes: power given |
| pod start wait, total (s) | 0 | 6.7 | +6.700 (native is 0) | +3.3610 to +10.0390 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.215 | +2.215 (native is 0) | +1.5517 to +2.8783 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.49 | 60.85 | −1.0% | −1.6116 to +0.3256 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1052 | 978.4 | −7.0% | −104.3732 to −42.4268 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.963 | −17.0% | −4.0972 to +0.0228 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 17.64 | 0.1792 | −99.0% | −35.0105 to +0.0939 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 118.3 | 0.6 | −99.5% | −227.9605 to −7.4395 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 323.6 | 282.2 | −12.8% | −60.7411 to −21.9422 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.58 | −3.5% | −0.9179 to +0.0706 | no |
| node-hours | 5.026 | 4.857 | −3.4% | −0.3786 to +0.0408 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 527.6 | +0.2% | −3.2324 to +4.8935 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 514.3 | −2.4% | −27.6365 to +2.6601 | no |
| response time (ms), mean | 756.3 | 1247 | +64.9% | +254.7784 to +726.5298 | yes: LOSS |
| response time (ms), 95th percentile | 2938 | 4271 | +45.4% | +831.3389 to +1834.4421 | yes: LOSS |
| response time (ms), 99th percentile | 3840 | 5732 | +49.3% | +1287.9269 to +2496.6323 | yes: LOSS |
| time over the response line (% of samples) | 24.57 | 43.09 | +75.4% | +13.3074 to +23.7288 | yes: LOSS |
| failed requests (%) | 0 | 0.3404 | +0.340 (native is 0) | −0.1918 to +0.8727 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 18.4 | +49.6% | +3.6118 to +8.5882 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.5 | +101.500 (native is 0) | +57.6677 to +145.3323 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.07 | 69.4 | +229.4% | −3.3398 to +100.0065 | no |
| utilisation (used / allocatable) | 0.03642 | 0.03743 | +2.8% | −0.0047 to +0.0067 | no |
| CPU used (cores), mean | 1.748 | 1.733 | −0.9% | −0.2541 to +0.2238 | no |
| Omni's own CPU (cores), mean | 0 | 0.06047 | +0.060 (native is 0) | +0.0560 to +0.0650 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.748 | 1.794 | +2.6% | −0.1913 to +0.2820 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.8 | 726.7 | −2.4% | −131.3341 to +94.9936 | no |
| HPA replicas, mean | 4.063 | 5.612 | +38.1% | +0.6844 to +2.4134 | yes: power given |
| pods started | 0.3 | 4.1 | +1266.7% | +2.1208 to +5.4792 | yes: power given |
| pod start wait, total (s) | 0.8 | 11.5 | +1337.5% | +5.6415 to +15.7585 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 2.913 | +264.1% | +0.7048 to +3.5209 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.28 | 68.27 | +25.8% | +11.9128 to +16.0639 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924.1 | 1118 | +21.0% | +119.3047 to +268.4953 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.02 | −8.2% | −2.1560 to +0.1886 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 25.17 | +20727.6% | +1.5593 to +48.5324 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 137.3 | +19514.3% | +7.4897 to +265.7103 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 229.6 | 390.5 | +70.1% | +91.9537 to +229.8797 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*