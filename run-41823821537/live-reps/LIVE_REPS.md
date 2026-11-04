# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.41 | 10.96 |
| node-hours | 5.033 | 5.028 | 4.775 | 4.597 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.6 | 526.4 | 528.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 526.6 | 507.7 | 495.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 698.4 | 851.2 | 786.2 | 974.1 |
| response time (ms), 95th percentile | 2746 | 3624 | 3269 | 4317 |
| response time (ms), 99th percentile | 3609 | 4963 | 4307 | 6020 |
| time over the response line (% of samples) | 25.55 | 28.55 | 29.77 | 34.6 |
| failed requests (%) | 0.007067 | 0.04997 | 0.01545 | 0.1297 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 17 | 15 | 18.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 112.9 | 71.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 13 | 33.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.92 | 38.81 | 28.07 | 51 |
| utilisation (used / allocatable) | 0.03605 | 0.0359 | 0.03797 | 0.04076 |
| CPU used (cores), mean | 1.73 | 1.723 | 1.729 | 1.771 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05556 | 0.04637 |
| CPU used with Omni's own (cores), mean | 1.73 | 1.723 | 1.785 | 1.817 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.5 | 741.7 | 711.1 | 670.4 |
| HPA replicas, mean | 4.028 | 4.22 | 5.181 | 5.1 |
| pods started | 0.1 | 0.1 | 3.9 | 4 |
| pod start wait, total (s) | 0.2 | 0.3 | 10 | 11.8 |
| pod start wait, mean (s) | 0.2 | 0.3 | 1.986 | 2.268 |
| host CPU busy, the real machine under kind (%) | 53.72 | 59.88 | 59.27 | 66.24 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 907.8 | 1018 | 950 | 1086 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.85 | 9.94 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 8.633 | 0.1625 | 17.99 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 65 | 0.7 | 159.4 |
| queue: job turnaround, submitted to done, mean (s) | 213.6 | 321.1 | 252.8 | 384.1 |
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
| worker nodes in service, mean | 12 | 10.96 | −8.7% | −2.2143 to +0.1379 | no |
| node-hours | 5.028 | 4.597 | −8.6% | −0.9235 to +0.0629 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.6 | 528.3 | +0.3% | +0.3325 to +3.0740 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.6 | 495.6 | −5.9% | −68.0232 to +6.0838 | no |
| response time (ms), mean | 851.2 | 974.1 | +14.4% | +46.6379 to +199.1525 | yes: LOSS |
| response time (ms), 95th percentile | 3624 | 4317 | +19.1% | +326.7032 to +1058.2028 | yes: LOSS |
| response time (ms), 99th percentile | 4963 | 6020 | +21.3% | +508.2374 to +1604.8526 | yes: LOSS |
| time over the response line (% of samples) | 28.55 | 34.6 | +21.2% | +3.4407 to +8.6701 | yes: LOSS |
| failed requests (%) | 0.04997 | 0.1297 | +159.5% | −0.0366 to +0.1960 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17 | 18.1 | +6.5% | +0.6940 to +1.5060 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.6 | +71.600 (native is 0) | +55.3367 to +87.8633 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 38.81 | 51 | +31.4% | −0.4535 to +24.8335 | no |
| utilisation (used / allocatable) | 0.0359 | 0.04076 | +13.5% | +0.0003 to +0.0094 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.723 | 1.771 | +2.8% | −0.0155 to +0.1114 | no |
| Omni's own CPU (cores), mean | 0 | 0.04637 | +0.046 (native is 0) | +0.0384 to +0.0543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.723 | 1.817 | +5.5% | +0.0322 to +0.1564 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.7 | 670.4 | −9.6% | −130.0055 to −12.6508 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.22 | 5.1 | +20.9% | +0.2410 to +1.5191 | yes: power given |
| pods started | 0.1 | 4 | +3900.0% | +1.5529 to +6.2471 | yes: power given |
| pod start wait, total (s) | 0.3 | 11.8 | +3833.3% | +4.1104 to +18.8896 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.268 | +656.1% | +0.5302 to +3.4062 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.88 | 66.24 | +10.6% | +5.3949 to +7.3402 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1018 | 1086 | +6.7% | +49.2013 to +86.7987 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.94 | −17.2% | −4.2058 to +0.0851 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 8.633 | 17.99 | +108.4% | −0.6685 to +19.3852 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 65 | 159.4 | +145.2% | −15.6805 to +204.4805 | no |
| queue: job turnaround, submitted to done, mean (s) | 321.1 | 384.1 | +19.6% | +43.1068 to +82.9932 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.033 | 5.028 | −0.1% | −0.0237 to +0.0137 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.6 | −0.1% | −3.9751 to +2.6040 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 526.6 | −0.1% | −3.9751 to +2.6040 | no |
| response time (ms), mean | 698.4 | 851.2 | +21.9% | +56.2770 to +249.4405 | yes: LOSS |
| response time (ms), 95th percentile | 2746 | 3624 | +32.0% | +332.0446 to +1424.4534 | yes: LOSS |
| response time (ms), 99th percentile | 3609 | 4963 | +37.5% | +798.6299 to +1909.6329 | yes: LOSS |
| time over the response line (% of samples) | 25.55 | 28.55 | +11.7% | −0.7267 to +6.7099 | no |
| failed requests (%) | 0.007067 | 0.04997 | +607.1% | −0.0268 to +0.1126 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 17 | +26.9% | +1.1405 to +6.0595 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.92 | 38.81 | +105.1% | −3.5777 to +43.3544 | no |
| utilisation (used / allocatable) | 0.03605 | 0.0359 | −0.4% | −0.0025 to +0.0022 | no |
| CPU used (cores), mean | 1.73 | 1.723 | −0.4% | −0.1207 to +0.1066 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.73 | 1.723 | −0.4% | −0.1207 to +0.1066 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.5 | 741.7 | +0.0% | −43.1250 to +43.4927 | no |
| HPA replicas, mean | 4.028 | 4.22 | +4.8% | −0.3685 to +0.7520 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.3 | +50.0% | −0.7564 to +0.9564 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | −0.7564 to +0.9564 | no |
| host CPU busy, the real machine under kind (%) | 53.72 | 59.88 | +11.5% | +4.8021 to +7.5048 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 907.8 | 1018 | +12.2% | +68.9023 to +151.8977 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 8.633 | +8908.7% | +0.3883 to +16.6867 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 65 | +10733.3% | −30.6699 to +159.4699 | no |
| queue: job turnaround, submitted to done, mean (s) | 213.6 | 321.1 | +50.3% | +70.5811 to +144.3522 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.41 | −4.9% | −1.4938 to +0.3072 | no |
| node-hours | 5.033 | 4.775 | −5.1% | −0.6233 to +0.1087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.4 | −0.2% | −3.2888 to +1.6960 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 507.7 | −3.7% | −46.7056 to +7.7127 | no |
| response time (ms), mean | 698.4 | 786.2 | +12.6% | +8.1958 to +167.5028 | yes: LOSS |
| response time (ms), 95th percentile | 2746 | 3269 | +19.0% | +157.6745 to +887.5985 | yes: LOSS |
| response time (ms), 99th percentile | 3609 | 4307 | +19.3% | +274.7587 to +1121.3015 | yes: LOSS |
| time over the response line (% of samples) | 25.55 | 29.77 | +16.5% | +1.5882 to +6.8388 | yes: LOSS |
| failed requests (%) | 0.007067 | 0.01545 | +118.7% | −0.0086 to +0.0254 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 15 | +11.9% | +0.2015 to +2.9985 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.9 | +112.900 (native is 0) | +76.8095 to +148.9905 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.92 | 28.07 | +48.3% | −0.4580 to +18.7513 | no |
| utilisation (used / allocatable) | 0.03605 | 0.03797 | +5.3% | −0.0011 to +0.0049 | no |
| CPU used (cores), mean | 1.73 | 1.729 | −0.0% | −0.0479 to +0.0463 | no |
| Omni's own CPU (cores), mean | 0 | 0.05556 | +0.056 (native is 0) | +0.0502 to +0.0609 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.73 | 1.785 | +3.2% | +0.0074 to +0.1021 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.5 | 711.1 | −4.1% | −74.0892 to +13.3175 | no |
| HPA replicas, mean | 4.028 | 5.181 | +28.6% | +0.6321 to +1.6737 | yes: power given |
| pods started | 0.1 | 3.9 | +3800.0% | +1.6199 to +5.9801 | yes: power given |
| pod start wait, total (s) | 0.2 | 10 | +4900.0% | +3.4395 to +16.1605 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.986 | +892.9% | +0.7915 to +2.7801 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.72 | 59.27 | +10.3% | +4.2786 to +6.8064 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 907.8 | 950 | +4.6% | +15.3301 to +69.0699 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.85 | −9.6% | −2.8525 to +0.5442 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 0.1625 | +69.6% | −0.0190 to +0.1524 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.7 | +16.7% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 213.6 | 252.8 | +18.3% | +14.8234 to +63.4933 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.41 | −4.9% | −1.4938 to +0.3072 | no |
| node-hours | 5.028 | 4.775 | −5.0% | −0.6265 to +0.1218 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.6 | 526.4 | −0.0% | −2.9985 to +2.7768 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.6 | 507.7 | −3.6% | −47.3929 to +9.7711 | no |
| response time (ms), mean | 851.2 | 786.2 | −7.6% | −156.7054 to +26.6865 | no |
| response time (ms), 95th percentile | 3624 | 3269 | −9.8% | −904.7902 to +193.5652 | no |
| response time (ms), 99th percentile | 4963 | 4307 | −13.2% | −1193.6553 to −118.5473 | yes: GAIN |
| time over the response line (% of samples) | 28.55 | 29.77 | +4.3% | −2.2280 to +4.6718 | no |
| failed requests (%) | 0.04997 | 0.01545 | −69.1% | −0.1049 to +0.0358 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17 | 15 | −11.8% | −3.5452 to −0.4548 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.9 | +112.900 (native is 0) | +76.8095 to +148.9905 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 38.81 | 28.07 | −27.7% | −33.3789 to +11.8956 | no |
| utilisation (used / allocatable) | 0.0359 | 0.03797 | +5.8% | −0.0015 to +0.0056 | no |
| CPU used (cores), mean | 1.723 | 1.729 | +0.4% | −0.1277 to +0.1402 | no |
| Omni's own CPU (cores), mean | 0 | 0.05556 | +0.056 (native is 0) | +0.0502 to +0.0609 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.723 | 1.785 | +3.6% | −0.0738 to +0.1974 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.7 | 711.1 | −4.1% | −83.7025 to +22.5632 | no |
| HPA replicas, mean | 4.22 | 5.181 | +22.8% | +0.2847 to +1.6375 | yes: power given |
| pods started | 0.1 | 3.9 | +3800.0% | +1.6727 to +5.9273 | yes: power given |
| pod start wait, total (s) | 0.3 | 10 | +3233.3% | +3.3552 to +16.0448 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.986 | +561.9% | +0.5710 to +2.8007 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.88 | 59.27 | −1.0% | −1.2611 to +0.0392 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1018 | 950 | −6.7% | −90.0811 to −46.3189 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.85 | −9.6% | −2.8525 to +0.5442 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 8.633 | 0.1625 | −98.1% | −16.5992 to −0.3425 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 65 | 0.7 | −98.9% | −159.4069 to +30.8069 | no |
| queue: job turnaround, submitted to done, mean (s) | 321.1 | 252.8 | −21.3% | −90.8693 to −45.7474 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.96 | −8.7% | −2.2143 to +0.1379 | no |
| node-hours | 5.033 | 4.597 | −8.6% | −0.9231 to +0.0524 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 528.3 | +0.2% | −2.0493 to +4.0847 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 495.6 | −6.0% | −67.7004 to +4.3900 | no |
| response time (ms), mean | 698.4 | 974.1 | +39.5% | +161.5085 to +389.9994 | yes: LOSS |
| response time (ms), 95th percentile | 2746 | 4317 | +57.2% | +1105.7300 to +2035.6740 | yes: LOSS |
| response time (ms), 99th percentile | 3609 | 6020 | +66.8% | +1905.8122 to +2915.5406 | yes: LOSS |
| time over the response line (% of samples) | 25.55 | 34.6 | +35.4% | +4.9237 to +13.1703 | yes: LOSS |
| failed requests (%) | 0.007067 | 0.1297 | +1735.2% | +0.0079 to +0.2374 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 18.1 | +35.1% | +2.3871 to +7.0129 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.6 | +71.600 (native is 0) | +55.3367 to +87.8633 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.92 | 51 | +169.5% | +2.2991 to +61.8576 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03605 | 0.04076 | +13.1% | −0.0008 to +0.0103 | no |
| CPU used (cores), mean | 1.73 | 1.771 | +2.4% | −0.0736 to +0.1555 | no |
| Omni's own CPU (cores), mean | 0 | 0.04637 | +0.046 (native is 0) | +0.0384 to +0.0543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.73 | 1.817 | +5.0% | −0.0243 to +0.1988 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.5 | 670.4 | −9.6% | −154.3448 to +12.0562 | no |
| HPA replicas, mean | 4.028 | 5.1 | +26.6% | +0.4925 to +1.6512 | yes: power given |
| pods started | 0.1 | 4 | +3900.0% | +1.7291 to +6.0709 | yes: power given |
| pod start wait, total (s) | 0.2 | 11.8 | +5800.0% | +4.6714 to +18.5286 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.268 | +1034.1% | +1.1520 to +2.9844 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.72 | 66.24 | +23.3% | +10.8825 to +14.1596 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 907.8 | 1086 | +19.7% | +128.7948 to +228.0052 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.94 | −17.2% | −4.2058 to +0.0851 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 17.99 | +18673.9% | +4.3530 to +31.4387 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 159.4 | +26466.7% | +39.9447 to +277.6553 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 213.6 | 384.1 | +79.8% | +121.5983 to +219.4350 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*