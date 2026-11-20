# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.59 | 10.93 |
| node-hours | 5.026 | 5.031 | 4.437 | 4.583 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 527.4 | 526.4 | 527.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 527.4 | 482.3 | 494.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 623.6 | 802.5 | 717 | 964 |
| response time (ms), 95th percentile | 2365 | 3359 | 2875 | 4236 |
| response time (ms), 99th percentile | 3248 | 4686 | 3920 | 5834 |
| time over the response line (% of samples) | 24.52 | 26.22 | 29.6 | 33.21 |
| failed requests (%) | 0 | 0.1119 | 0.03148 | 0.2238 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 15.8 | 14.5 | 17.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 118.3 | 47.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 34.67 | 31.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.38 | 31.68 | 27.95 | 53.27 |
| utilisation (used / allocatable) | 0.03548 | 0.0363 | 0.04042 | 0.04039 |
| CPU used (cores), mean | 1.703 | 1.742 | 1.708 | 1.753 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05501 | 0.04492 |
| CPU used with Omni's own (cores), mean | 1.703 | 1.742 | 1.763 | 1.798 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 735.8 | 679.2 | 677.2 |
| HPA replicas, mean | 3.935 | 4.026 | 4.604 | 5.049 |
| pods started | 0 | 0 | 3 | 3.6 |
| pod start wait, total (s) | 0 | 0 | 7.5 | 10.2 |
| pod start wait, mean (s) | 0 | 0 | 1.611 | 2.383 |
| host CPU busy, the real machine under kind (%) | 51.96 | 58.72 | 58.19 | 65.35 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 877.7 | 992.6 | 928 | 1074 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.136 | 9.636 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 5.908 | 0.125 | 12.22 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.9 | 0.7 | 104.3 |
| queue: job turnaround, submitted to done, mean (s) | 184.9 | 295.2 | 232.8 | 386.3 |
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
| worker nodes in service, mean | 12 | 10.93 | −8.9% | −2.1726 to +0.0286 | no |
| node-hours | 5.031 | 4.583 | −8.9% | −0.9117 to +0.0149 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 527.8 | +0.1% | −1.7213 to +2.5563 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 494.1 | −6.3% | −67.6338 to +1.1604 | no |
| response time (ms), mean | 802.5 | 964 | +20.1% | +96.8927 to +226.1761 | yes: LOSS |
| response time (ms), 95th percentile | 3359 | 4236 | +26.1% | +289.2597 to +1464.4513 | yes: LOSS |
| response time (ms), 99th percentile | 4686 | 5834 | +24.5% | +284.5846 to +2011.3302 | yes: LOSS |
| time over the response line (% of samples) | 26.22 | 33.21 | +26.6% | +4.0256 to +9.9461 | yes: LOSS |
| failed requests (%) | 0.1119 | 0.2238 | +100.0% | −0.1108 to +0.3346 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.8 | 17.5 | +10.8% | +0.8047 to +2.5953 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 | +47.700 (native is 0) | +30.6221 to +64.7779 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 31.68 | 53.27 | +68.1% | −5.7009 to +48.8676 | no |
| utilisation (used / allocatable) | 0.0363 | 0.04039 | +11.3% | −0.0010 to +0.0091 | no |
| CPU used (cores), mean | 1.742 | 1.753 | +0.6% | −0.0932 to +0.1139 | no |
| Omni's own CPU (cores), mean | 0 | 0.04492 | +0.045 (native is 0) | +0.0373 to +0.0525 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.742 | 1.798 | +3.2% | −0.0459 to +0.1565 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 735.8 | 677.2 | −8.0% | −134.7741 to +17.4364 | no |
| HPA replicas, mean | 4.026 | 5.049 | +25.4% | +0.5261 to +1.5184 | yes: power given |
| pods started | 0 | 3.6 | +3.600 (native is 0) | +1.6866 to +5.5134 | yes: power given |
| pod start wait, total (s) | 0 | 10.2 | +10.200 (native is 0) | +4.0578 to +16.3422 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.383 | +2.383 (native is 0) | +1.6274 to +3.1393 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.72 | 65.35 | +11.3% | +5.3750 to +7.8718 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 992.6 | 1074 | +8.2% | +54.6638 to +107.5362 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.636 | −19.7% | −4.4000 to −0.3273 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.908 | 12.22 | +106.8% | −3.4788 to +16.1038 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 104.3 | +5389.5% | −5.0799 to +209.8799 | no |
| queue: job turnaround, submitted to done, mean (s) | 295.2 | 386.3 | +30.9% | +64.6748 to +117.5086 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.026 | 5.031 | +0.1% | −0.0053 to +0.0159 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 527.4 | +0.2% | −0.3621 to +2.7501 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 527.4 | +0.2% | −0.3621 to +2.7501 | no |
| response time (ms), mean | 623.6 | 802.5 | +28.7% | +49.9513 to +307.8871 | yes: LOSS |
| response time (ms), 95th percentile | 2365 | 3359 | +42.0% | +367.8308 to +1620.9472 | yes: LOSS |
| response time (ms), 99th percentile | 3248 | 4686 | +44.3% | +909.5911 to +1965.9573 | yes: LOSS |
| time over the response line (% of samples) | 24.52 | 26.22 | +6.9% | −0.9465 to +4.3497 | no |
| failed requests (%) | 0 | 0.1119 | +0.112 (native is 0) | −0.0149 to +0.2387 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 15.8 | +17.9% | +1.5604 to +3.2396 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.38 | 31.68 | +120.3% | +0.4626 to +34.1374 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03548 | 0.0363 | +2.3% | −0.0009 to +0.0026 | no |
| CPU used (cores), mean | 1.703 | 1.742 | +2.3% | −0.0452 to +0.1232 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.703 | 1.742 | +2.3% | −0.0452 to +0.1232 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 735.8 | −2.8% | −52.0097 to +9.6729 | no |
| HPA replicas, mean | 3.935 | 4.026 | +2.3% | −0.0819 to +0.2642 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 51.96 | 58.72 | +13.0% | +5.3544 to +8.1659 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 877.7 | 992.6 | +13.1% | +69.0020 to +160.7980 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 5.908 | +5353.8% | +0.7214 to +10.8786 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.9 | +111.1% | +0.1079 to +1.8921 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 184.9 | 295.2 | +59.6% | +65.9716 to +154.5284 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.4967 to −0.3183 | yes: GAIN |
| node-hours | 5.026 | 4.437 | −11.7% | −1.0499 to −0.1279 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 526.4 | +0.0% | −1.7536 to +2.2162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 482.3 | −8.3% | −78.1472 to −9.5736 | yes: GAIN |
| response time (ms), mean | 623.6 | 717 | +15.0% | +28.3661 to +158.4856 | yes: LOSS |
| response time (ms), 95th percentile | 2365 | 2875 | +21.6% | +212.5469 to +807.4131 | yes: LOSS |
| response time (ms), 99th percentile | 3248 | 3920 | +20.7% | +263.4423 to +1079.9759 | yes: LOSS |
| time over the response line (% of samples) | 24.52 | 29.6 | +20.7% | +2.5176 to +7.6525 | yes: LOSS |
| failed requests (%) | 0 | 0.03148 | +0.031 (native is 0) | −0.0084 to +0.0713 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.5 | +8.2% | +0.4737 to +1.7263 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.3 | +118.300 (native is 0) | +52.9947 to +183.6053 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.38 | 27.95 | +94.3% | +0.1861 to +26.9439 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03548 | 0.04042 | +13.9% | +0.0003 to +0.0095 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.703 | 1.708 | +0.3% | −0.0486 to +0.0574 | no |
| Omni's own CPU (cores), mean | 0 | 0.05501 | +0.055 (native is 0) | +0.0497 to +0.0604 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.703 | 1.763 | +3.5% | +0.0097 to +0.1092 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 679.2 | −10.3% | −153.3449 to −2.3625 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.935 | 4.604 | +17.0% | +0.3224 to +1.0158 | yes: power given |
| pods started | 0 | 3 | +3.000 (native is 0) | +1.2479 to +4.7521 | yes: power given |
| pod start wait, total (s) | 0 | 7.5 | +7.500 (native is 0) | +1.9260 to +13.0740 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.611 | +1.611 (native is 0) | +0.6795 to +2.5420 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.96 | 58.19 | +12.0% | +5.2204 to +7.2390 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 877.7 | 928 | +5.7% | +26.0122 to +74.5878 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.136 | −23.9% | −4.7127 to −1.0161 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.125 | +15.4% | −0.0399 to +0.0732 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.7 | −22.2% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 184.9 | 232.8 | +25.9% | +26.1580 to +69.6836 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.4967 to −0.3183 | yes: GAIN |
| node-hours | 5.031 | 4.437 | −11.8% | −1.0554 to −0.1331 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 526.4 | −0.2% | −3.4373 to +1.5119 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 482.3 | −8.5% | −79.8060 to −10.3028 | yes: GAIN |
| response time (ms), mean | 802.5 | 717 | −10.7% | −195.6306 to +24.6439 | no |
| response time (ms), 95th percentile | 3359 | 2875 | −14.4% | −1032.4907 to +63.6727 | no |
| response time (ms), 99th percentile | 4686 | 3920 | −16.3% | −1325.0428 to −207.0874 | yes: GAIN |
| time over the response line (% of samples) | 26.22 | 29.6 | +12.9% | +0.2487 to +6.5181 | yes: LOSS |
| failed requests (%) | 0.1119 | 0.03148 | −71.9% | −0.1893 to +0.0284 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.8 | 14.5 | −8.2% | −2.0578 to −0.5422 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.3 | +118.300 (native is 0) | +52.9947 to +183.6053 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 31.68 | 27.95 | −11.8% | −22.0578 to +14.5878 | no |
| utilisation (used / allocatable) | 0.0363 | 0.04042 | +11.3% | −0.0003 to +0.0085 | no |
| CPU used (cores), mean | 1.742 | 1.708 | −2.0% | −0.1381 to +0.0689 | no |
| Omni's own CPU (cores), mean | 0 | 0.05501 | +0.055 (native is 0) | +0.0497 to +0.0604 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.742 | 1.763 | +1.2% | −0.0821 to +0.1229 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 735.8 | 679.2 | −7.7% | −118.7723 to +5.4016 | no |
| HPA replicas, mean | 4.026 | 4.604 | +14.4% | +0.1306 to +1.0253 | yes: power given |
| pods started | 0 | 3 | +3.000 (native is 0) | +1.2479 to +4.7521 | yes: power given |
| pod start wait, total (s) | 0 | 7.5 | +7.500 (native is 0) | +1.9260 to +13.0740 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.611 | +1.611 (native is 0) | +0.6795 to +2.5420 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.72 | 58.19 | −0.9% | −1.3360 to +0.2751 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 992.6 | 928 | −6.5% | −92.3759 to −36.8241 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.136 | −23.9% | −4.7127 to −1.0161 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.908 | 0.125 | −97.9% | −10.8455 to −0.7212 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.7 | −63.2% | −2.0121 to −0.3879 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 295.2 | 232.8 | −21.1% | −89.5056 to −35.1528 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.93 | −8.9% | −2.1726 to +0.0286 | no |
| node-hours | 5.026 | 4.583 | −8.8% | −0.9073 to +0.0212 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 527.8 | +0.3% | −1.0540 to +4.2769 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 494.1 | −6.1% | −66.2603 to +2.1749 | no |
| response time (ms), mean | 623.6 | 964 | +54.6% | +187.6248 to +493.2824 | yes: LOSS |
| response time (ms), 95th percentile | 2365 | 4236 | +79.1% | +1284.6021 to +2457.8869 | yes: LOSS |
| response time (ms), 99th percentile | 3248 | 5834 | +79.6% | +1757.2236 to +3414.2396 | yes: LOSS |
| time over the response line (% of samples) | 24.52 | 33.21 | +35.4% | +3.4726 to +13.9023 | yes: LOSS |
| failed requests (%) | 0 | 0.2238 | +0.224 (native is 0) | −0.0490 to +0.4966 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 17.5 | +30.6% | +2.6129 to +5.5871 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 | +47.700 (native is 0) | +30.6221 to +64.7779 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.38 | 53.27 | +270.3% | +2.0642 to +75.7025 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03548 | 0.04039 | +13.8% | −0.0011 to +0.0109 | no |
| CPU used (cores), mean | 1.703 | 1.753 | +2.9% | −0.1047 to +0.2035 | no |
| Omni's own CPU (cores), mean | 0 | 0.04492 | +0.045 (native is 0) | +0.0373 to +0.0525 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.703 | 1.798 | +5.5% | −0.0572 to +0.2458 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 677.2 | −10.5% | −178.6622 to +18.9877 | no |
| HPA replicas, mean | 3.935 | 5.049 | +28.3% | +0.6201 to +1.6066 | yes: power given |
| pods started | 0 | 3.6 | +3.600 (native is 0) | +1.6866 to +5.5134 | yes: power given |
| pod start wait, total (s) | 0 | 10.2 | +10.200 (native is 0) | +4.0578 to +16.3422 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.383 | +2.383 (native is 0) | +1.6274 to +3.1393 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.96 | 65.35 | +25.8% | +11.3179 to +15.4492 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 877.7 | 1074 | +22.3% | +137.0538 to +254.9462 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.636 | −19.7% | −4.4000 to −0.3273 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 12.22 | +11180.8% | −1.3708 to +25.5958 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 104.3 | +11488.9% | −4.7811 to +211.5811 | no |
| queue: job turnaround, submitted to done, mean (s) | 184.9 | 386.3 | +108.9% | +139.8677 to +262.8156 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*