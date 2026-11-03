# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.27 | 11.91 |
| node-hours | 5.026 | 5.026 | 4.721 | 4.988 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527.3 | 528.9 | 526.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 527.3 | 506 | 524.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 867.2 | 1084 | 1016 | 1330 |
| response time (ms), 95th percentile | 3384 | 4635 | 4205 | 5423 |
| response time (ms), 99th percentile | 4455 | 6070 | 5494 | 7399 |
| time over the response line (% of samples) | 30.58 | 34.77 | 33.93 | 46.29 |
| failed requests (%) | 0 | 0.1063 | 0.02451 | 0.3021 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 18.3 | 16 | 20.56 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 98.3 | 56.56 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 9.091 | 18.52 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.73 | 61.41 | 30.98 | 129.1 |
| utilisation (used / allocatable) | 0.03735 | 0.03695 | 0.04157 | 0.03679 |
| CPU used (cores), mean | 1.793 | 1.773 | 1.861 | 1.753 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05826 | 0.05082 |
| CPU used with Omni's own (cores), mean | 1.793 | 1.773 | 1.92 | 1.804 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714 | 721 | 656.9 | 724.8 |
| HPA replicas, mean | 4.059 | 4.255 | 5.255 | 5.537 |
| pods started | 0.1 | 0 | 4.2 | 4.778 |
| pod start wait, total (s) | 0.3 | 0 | 12.1 | 12.78 |
| pod start wait, mean (s) | 0.3 | 0 | 2.339 | 2.756 |
| host CPU busy, the real machine under kind (%) | 56.7 | 63.77 | 63.09 | 72.52 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 967.8 | 1104 | 1027 | 1221 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.84 | 11.79 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 7.237 | 0.1417 | 21.52 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 33.6 | 0.8 | 212.7 |
| queue: job turnaround, submitted to done, mean (s) | 276.1 | 408.9 | 325.2 | 527.1 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.91 | −0.7% | −0.2647 to +0.0886 | no |
| node-hours | 5.029 | 4.988 | −0.8% | −0.1173 to +0.0355 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.2 | 526.9 | −0.2% | −4.0893 to +1.6384 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.2 | 524.2 | −0.8% | −9.6774 to +1.6987 | no |
| response time (ms), mean | 1184 | 1330 | +12.3% | +14.3165 to +277.1390 | yes: LOSS |
| response time (ms), 95th percentile | 5088 | 5423 | +6.6% | −224.3442 to +893.1097 | no |
| response time (ms), 99th percentile | 6647 | 7399 | +11.3% | +88.3667 to +1416.0173 | yes: LOSS |
| time over the response line (% of samples) | 37.92 | 46.29 | +22.1% | +5.2633 to +11.4757 | yes: LOSS |
| failed requests (%) | 0.1181 | 0.3021 | +155.7% | −0.0908 to +0.4588 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.11 | 20.56 | +7.6% | +0.8860 to +2.0029 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.56 | +56.556 (native is 0) | +45.6097 to +67.5014 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 67.58 | 129.1 | +91.1% | +1.7172 to +121.3458 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03771 | 0.03679 | −2.5% | −0.0062 to +0.0043 | no |
| CPU used (cores), mean | 1.81 | 1.753 | −3.2% | −0.3021 to +0.1876 | no |
| Omni's own CPU (cores), mean | 0 | 0.05082 | +0.051 (native is 0) | +0.0431 to +0.0586 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.81 | 1.804 | −0.4% | −0.2490 to +0.2361 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.9 | 724.8 | +2.8% | −66.5294 to +106.3401 | no |
| HPA replicas, mean | 4.321 | 5.537 | +28.2% | +0.7758 to +1.6578 | yes: power given |
| pods started | 0 | 4.778 | +4.778 (native is 0) | +3.0686 to +6.4870 | yes: power given |
| pod start wait, total (s) | 0 | 12.78 | +12.778 (native is 0) | +8.7878 to +16.7678 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.756 | +2.756 (native is 0) | +2.1477 to +3.3634 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 65.69 | 72.52 | +10.4% | +5.7627 to +7.9050 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1142 | 1221 | +6.9% | +61.5978 to +96.6244 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.79 | −1.8% | −0.6432 to +0.2134 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 8.019 | 21.52 | +168.4% | +2.0296 to +24.9797 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 37.22 | 212.7 | +471.3% | +47.3137 to +303.5752 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 445.3 | 527.1 | +18.4% | +60.9719 to +102.6485 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.026 | 5.026 | 0.0% | raw −0.0145 to +0.0145 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527.3 | −0.0% | −2.3401 to +1.9527 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 527.3 | −0.0% | −2.3401 to +1.9527 | no |
| response time (ms), mean | 867.2 | 1084 | +25.0% | +95.9541 to +337.4237 | yes: LOSS |
| response time (ms), 95th percentile | 3384 | 4635 | +37.0% | +573.3726 to +1928.9864 | yes: LOSS |
| response time (ms), 99th percentile | 4455 | 6070 | +36.2% | +968.9997 to +2259.8503 | yes: LOSS |
| time over the response line (% of samples) | 30.58 | 34.77 | +13.7% | +2.0023 to +6.3618 | yes: LOSS |
| failed requests (%) | 0 | 0.1063 | +0.106 (native is 0) | +0.0091 to +0.2035 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 18.3 | +18.8% | +1.8100 to +3.9900 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.73 | 61.41 | +82.1% | −8.1590 to +63.5157 | no |
| utilisation (used / allocatable) | 0.03735 | 0.03695 | −1.1% | −0.0026 to +0.0018 | no |
| CPU used (cores), mean | 1.793 | 1.773 | −1.1% | −0.1249 to +0.0861 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.793 | 1.773 | −1.1% | −0.1249 to +0.0861 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714 | 721 | +1.0% | −32.2980 to +46.1809 | no |
| HPA replicas, mean | 4.059 | 4.255 | +4.8% | −0.0712 to +0.4626 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 56.7 | 63.77 | +12.5% | +5.7494 to +8.3913 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 967.8 | 1104 | +14.1% | +94.6685 to +177.9315 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 7.237 | +4862.9% | +0.3498 to +13.8336 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 33.6 | +4700.0% | −38.2558 to +104.0558 | no |
| queue: job turnaround, submitted to done, mean (s) | 276.1 | 408.9 | +48.1% | +92.1835 to +173.4332 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.27 | −6.1% | −2.0166 to +0.5500 | no |
| node-hours | 5.026 | 4.721 | −6.1% | −0.8466 to +0.2368 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 528.9 | +0.3% | −1.0668 to +3.9160 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 506 | −4.1% | −62.8641 to +19.7299 | no |
| response time (ms), mean | 867.2 | 1016 | +17.1% | +22.4860 to +274.2342 | yes: LOSS |
| response time (ms), 95th percentile | 3384 | 4205 | +24.3% | +339.3228 to +1302.3792 | yes: LOSS |
| response time (ms), 99th percentile | 4455 | 5494 | +23.3% | +478.2055 to +1598.7165 | yes: LOSS |
| time over the response line (% of samples) | 30.58 | 33.93 | +10.9% | +0.6145 to +6.0742 | yes: LOSS |
| failed requests (%) | 0 | 0.02451 | +0.025 (native is 0) | −0.0038 to +0.0528 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 16 | +3.9% | −0.7146 to +1.9146 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 98.3 | +98.300 (native is 0) | +50.1631 to +146.4369 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.73 | 30.98 | −8.1% | −20.8020 to +15.3087 | no |
| utilisation (used / allocatable) | 0.03735 | 0.04157 | +11.3% | +0.0000 to +0.0084 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.793 | 1.861 | +3.8% | −0.0326 to +0.1695 | no |
| Omni's own CPU (cores), mean | 0 | 0.05826 | +0.058 (native is 0) | +0.0524 to +0.0641 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.793 | 1.92 | +7.1% | +0.0229 to +0.2306 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714 | 656.9 | −8.0% | −108.2288 to −6.0196 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.059 | 5.255 | +29.5% | +0.8165 to +1.5751 | yes: power given |
| pods started | 0.1 | 4.2 | +4100.0% | +2.1208 to +6.0792 | yes: power given |
| pod start wait, total (s) | 0.3 | 12.1 | +3933.3% | +5.4128 to +18.1872 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.339 | +679.5% | +0.8653 to +3.2119 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.7 | 63.09 | +11.3% | +4.4390 to +8.3413 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 967.8 | 1027 | +6.1% | +23.2197 to +94.9803 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.84 | −9.7% | −3.0577 to +0.7374 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 0.1417 | −2.9% | −0.0736 to +0.0653 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.8 | +14.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 276.1 | 325.2 | +17.8% | +14.4884 to +83.7616 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.27 | −6.1% | −2.0166 to +0.5500 | no |
| node-hours | 5.026 | 4.721 | −6.1% | −0.8394 to +0.2296 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.3 | 528.9 | +0.3% | −0.2923 to +3.5289 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.3 | 506 | −4.1% | −62.2580 to +19.5112 | no |
| response time (ms), mean | 1084 | 1016 | −6.3% | −183.4238 to +46.7661 | no |
| response time (ms), 95th percentile | 4635 | 4205 | −9.3% | −899.5044 to +38.8474 | no |
| response time (ms), 99th percentile | 6070 | 5494 | −9.5% | −1030.5225 to −121.4055 | yes: GAIN |
| time over the response line (% of samples) | 34.77 | 33.93 | −2.4% | −3.6391 to +1.9637 | no |
| failed requests (%) | 0.1063 | 0.02451 | −76.9% | −0.1612 to −0.0024 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.3 | 16 | −12.6% | −4.5380 to −0.0620 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 98.3 | +98.300 (native is 0) | +50.1631 to +146.4369 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 61.41 | 30.98 | −49.5% | −70.3912 to +9.5412 | no |
| utilisation (used / allocatable) | 0.03695 | 0.04157 | +12.5% | +0.0000 to +0.0092 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.773 | 1.861 | +5.0% | −0.0781 to +0.2539 | no |
| Omni's own CPU (cores), mean | 0 | 0.05826 | +0.058 (native is 0) | +0.0524 to +0.0641 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.773 | 1.92 | +8.2% | −0.0227 to +0.3151 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 721 | 656.9 | −8.9% | −122.3069 to −5.8244 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.255 | 5.255 | +23.5% | +0.6030 to +1.3972 | yes: power given |
| pods started | 0 | 4.2 | +4.200 (native is 0) | +2.1824 to +6.2176 | yes: power given |
| pod start wait, total (s) | 0 | 12.1 | +12.100 (native is 0) | +5.6450 to +18.5550 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.339 | +2.339 (native is 0) | +1.3246 to +3.3525 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 63.77 | 63.09 | −1.1% | −1.9201 to +0.5596 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1104 | 1027 | −7.0% | −103.8660 to −50.5340 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.84 | −9.7% | −3.0577 to +0.7374 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.237 | 0.1417 | −98.0% | −13.8542 to −0.3374 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33.6 | 0.8 | −97.6% | −103.9808 to +38.3808 | no |
| queue: job turnaround, submitted to done, mean (s) | 408.9 | 325.2 | −20.5% | −111.5014 to −55.8652 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.91 | −0.7% | −0.2647 to +0.0886 | no |
| node-hours | 5.026 | 4.988 | −0.8% | −0.1179 to +0.0419 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.2 | 526.9 | −0.2% | −4.5301 to +2.0853 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.2 | 524.2 | −0.8% | −9.7126 to +1.7400 | no |
| response time (ms), mean | 948 | 1330 | +40.3% | +244.1556 to +520.2802 | yes: LOSS |
| response time (ms), 95th percentile | 3716 | 5423 | +45.9% | +1073.6463 to +2339.9671 | yes: LOSS |
| response time (ms), 99th percentile | 4870 | 7399 | +51.9% | +2041.9591 to +3015.5876 | yes: LOSS |
| time over the response line (% of samples) | 33.67 | 46.29 | +37.5% | +9.8522 to +15.3839 | yes: LOSS |
| failed requests (%) | 0 | 0.3021 | +0.302 (native is 0) | −0.0097 to +0.6140 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.67 | 20.56 | +23.3% | +3.2880 to +4.4898 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.56 | +56.556 (native is 0) | +45.6097 to +67.5014 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 36.68 | 129.1 | +252.0% | +26.1116 to +158.7365 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03826 | 0.03679 | −3.8% | −0.0065 to +0.0035 | no |
| CPU used (cores), mean | 1.836 | 1.753 | −4.5% | −0.3150 to +0.1484 | no |
| Omni's own CPU (cores), mean | 0 | 0.05082 | +0.051 (native is 0) | +0.0431 to +0.0586 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.836 | 1.804 | −1.8% | −0.2606 to +0.1956 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.6 | 724.8 | +4.3% | −57.5274 to +117.9060 | no |
| HPA replicas, mean | 4.103 | 5.537 | +34.9% | +1.0356 to +1.8325 | yes: power given |
| pods started | 0.1111 | 4.778 | +4200.0% | +2.9479 to +6.3855 | yes: power given |
| pod start wait, total (s) | 0.3333 | 12.78 | +3733.3% | +8.2853 to +16.6036 | yes: LOSS |
| pod start wait, mean (s) | 0.3333 | 2.756 | +726.7% | +1.3238 to +3.5206 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.32 | 72.52 | +24.4% | +12.5968 to +15.8137 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 993.2 | 1221 | +23.0% | +189.8580 to +266.3642 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.79 | −1.8% | −0.6432 to +0.2134 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1528 | 21.52 | +13987.9% | +10.9046 to +31.8362 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 | 212.7 | +31800.0% | +91.1139 to +332.8861 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 301.3 | 527.1 | +75.0% | +184.2159 to +267.5526 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*