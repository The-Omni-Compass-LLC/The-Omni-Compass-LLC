# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.22 | 9.884 |
| node-hours | 5.023 | 5.036 | 3.856 | 4.145 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 524.2 | 522.3 | 524.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 524.2 | 435 | 458 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 275.8 | 312.2 | 278.7 | 394.7 |
| response time (ms), 95th percentile | 890.4 | 1141 | 1037 | 1930 |
| response time (ms), 99th percentile | 1233 | 2115 | 1450 | 3207 |
| time over the response line (% of samples) | 15.62 | 13.42 | 17.85 | 16.68 |
| failed requests (%) | 0 | 0.005391 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.9 | 9.9 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 129.4 | 69.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 40.07 | 62.17 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.707 | 10.86 | 9.633 | 17.65 |
| utilisation (used / allocatable) | 0.03082 | 0.03117 | 0.04036 | 0.03935 |
| CPU used (cores), mean | 1.479 | 1.496 | 1.462 | 1.531 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04897 | 0.0352 |
| CPU used with Omni's own (cores), mean | 1.479 | 1.496 | 1.511 | 1.566 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.2 | 851.2 | 712 | 714.6 |
| HPA replicas, mean | 3.953 | 4.054 | 4.327 | 4.485 |
| pods started | 0 | 0.1 | 1.5 | 1.7 |
| pod start wait, total (s) | 0 | 0.2 | 3.7 | 3.8 |
| pod start wait, mean (s) | 0 | 0.2 | 0.9167 | 1.8 |
| host CPU busy, the real machine under kind (%) | 45.05 | 49.31 | 49.24 | 54.73 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 763.3 | 819 | 778.2 | 872 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 7.165 | 8.231 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.3083 | 0.06667 | 0.475 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | 0.7 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 75.95 | 128.4 | 89.36 | 177.4 |
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
| worker nodes in service, mean | 12 | 9.884 | −17.6% | −3.6716 to −0.5594 | yes: GAIN |
| node-hours | 5.036 | 4.145 | −17.7% | −1.5431 to −0.2400 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 524.5 | +0.1% | −1.4262 to +2.0938 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 458 | −12.6% | −115.4473 to −16.9142 | yes: GAIN |
| response time (ms), mean | 312.2 | 394.7 | +26.5% | +21.1095 to +144.0525 | yes: LOSS |
| response time (ms), 95th percentile | 1141 | 1930 | +69.1% | +301.9629 to +1275.4051 | yes: LOSS |
| response time (ms), 99th percentile | 2115 | 3207 | +51.6% | +395.1116 to +1788.9398 | yes: LOSS |
| time over the response line (% of samples) | 13.42 | 16.68 | +24.3% | +1.0153 to +5.5010 | yes: LOSS |
| failed requests (%) | 0.005391 | 0 | −100.0% | −0.0176 to +0.0068 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 11 | +11.1% | +0.4737 to +1.7263 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 69.6 | +69.600 (native is 0) | +25.1355 to +114.0645 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.86 | 17.65 | +62.5% | +1.0121 to +12.5645 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03117 | 0.03935 | +26.3% | +0.0032 to +0.0132 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.496 | 1.531 | +2.3% | −0.0255 to +0.0955 | no |
| Omni's own CPU (cores), mean | 0 | 0.0352 | +0.035 (native is 0) | +0.0302 to +0.0402 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.496 | 1.566 | +4.7% | +0.0068 to +0.1336 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851.2 | 714.6 | −16.1% | −224.9213 to −48.4011 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.054 | 4.485 | +10.6% | +0.0329 to +0.8290 | yes: power given |
| pods started | 0.1 | 1.7 | +1600.0% | +0.6952 to +2.5048 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.8 | +1800.0% | +1.4095 to +5.7905 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.8 | +800.0% | +0.8414 to +2.3586 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.31 | 54.73 | +11.0% | +4.1080 to +6.7424 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 819 | 872 | +6.5% | +24.3123 to +81.6877 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.231 | −31.4% | −5.9061 to −1.6318 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3083 | 0.475 | +54.1% | +0.0634 to +0.2699 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.3 | +18.2% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 128.4 | 177.4 | +38.2% | +20.1694 to +77.9639 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.023 | 5.036 | +0.3% | −0.0087 to +0.0354 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 524.2 | +0.3% | −0.8639 to +4.5046 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 524.2 | +0.3% | −0.8639 to +4.5046 | no |
| response time (ms), mean | 275.8 | 312.2 | +13.2% | +10.1035 to +62.6628 | yes: LOSS |
| response time (ms), 95th percentile | 890.4 | 1141 | +28.1% | +62.5809 to +438.2841 | yes: LOSS |
| response time (ms), 99th percentile | 1233 | 2115 | +71.5% | +354.7460 to +1407.8908 | yes: LOSS |
| time over the response line (% of samples) | 15.62 | 13.42 | −14.1% | −3.9160 to −0.4945 | yes: GAIN |
| failed requests (%) | 0 | 0.005391 | +0.005 (native is 0) | −0.0068 to +0.0176 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.9 | +2.1% | −1.4450 to +1.8450 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.707 | 10.86 | +40.9% | +0.6401 to +5.6666 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03082 | 0.03117 | +1.1% | −0.0005 to +0.0012 | no |
| CPU used (cores), mean | 1.479 | 1.496 | +1.1% | −0.0226 to +0.0562 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.479 | 1.496 | +1.1% | −0.0226 to +0.0562 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.2 | 851.2 | −0.3% | −30.8257 to +24.8663 | no |
| HPA replicas, mean | 3.953 | 4.054 | +2.5% | −0.0804 to +0.2819 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 45.05 | 49.31 | +9.4% | +3.0516 to +5.4581 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 819 | +7.3% | +28.5119 to +82.8881 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.3083 | +640.0% | +0.1253 to +0.4080 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | +266.7% | +0.3476 to +1.2524 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 75.95 | 128.4 | +69.0% | +24.9569 to +79.8598 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.22 | −23.2% | −4.2135 to −1.3469 | yes: GAIN |
| node-hours | 5.023 | 3.856 | −23.2% | −1.7691 to −0.5644 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 522.3 | −0.0% | −1.8325 to +1.6813 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 435 | −16.7% | −132.6824 to −41.9771 | yes: GAIN |
| response time (ms), mean | 275.8 | 278.7 | +1.1% | −14.0798 to +19.9607 | no |
| response time (ms), 95th percentile | 890.4 | 1037 | +16.5% | +51.7170 to +241.4690 | yes: LOSS |
| response time (ms), 99th percentile | 1233 | 1450 | +17.6% | +60.1699 to +372.7931 | yes: LOSS |
| time over the response line (% of samples) | 15.62 | 17.85 | +14.3% | +0.1131 to +4.3490 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.9 | +2.1% | −1.0526 to +1.4526 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 129.4 | +129.400 (native is 0) | +72.0571 to +186.7429 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.707 | 9.633 | +25.0% | −0.5007 to +4.3540 | no |
| utilisation (used / allocatable) | 0.03082 | 0.04036 | +31.0% | +0.0046 to +0.0145 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.479 | 1.462 | −1.2% | −0.0546 to +0.0196 | no |
| Omni's own CPU (cores), mean | 0 | 0.04897 | +0.049 (native is 0) | +0.0467 to +0.0512 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.511 | +2.1% | −0.0069 to +0.0698 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.2 | 712 | −16.6% | −216.6179 to −67.7376 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.953 | 4.327 | +9.4% | −0.0764 to +0.8234 | no |
| pods started | 0 | 1.5 | +1.500 (native is 0) | −0.0544 to +3.0544 | no |
| pod start wait, total (s) | 0 | 3.7 | +3.700 (native is 0) | −0.4988 to +7.8988 | no |
| pod start wait, mean (s) | 0 | 0.9167 | +0.917 (native is 0) | +0.0383 to +1.7950 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.05 | 49.24 | +9.3% | +3.5009 to +4.8656 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 778.2 | +2.0% | +6.4266 to +23.3734 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.165 | −40.3% | −6.7573 to −2.9136 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.06667 | +60.0% | −0.0199 to +0.0699 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | −0.1001 to +0.9001 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.95 | 89.36 | +17.7% | +3.6833 to +23.1334 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.22 | −23.2% | −4.2135 to −1.3469 | yes: GAIN |
| node-hours | 5.036 | 3.856 | −23.4% | −1.7755 to −0.5846 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 522.3 | −0.4% | −3.3435 to −0.4484 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 435 | −17.0% | −133.4387 to −44.8614 | yes: GAIN |
| response time (ms), mean | 312.2 | 278.7 | −10.7% | −46.5859 to −20.2996 | yes: GAIN |
| response time (ms), 95th percentile | 1141 | 1037 | −9.1% | −228.8535 to +21.1745 | no |
| response time (ms), 99th percentile | 2115 | 1450 | −31.4% | −1122.5722 to −207.1016 | yes: GAIN |
| time over the response line (% of samples) | 13.42 | 17.85 | +33.1% | +2.5408 to +6.3317 | yes: LOSS |
| failed requests (%) | 0.005391 | 0 | −100.0% | −0.0176 to +0.0068 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.9 | ±0.0% | −1.0116 to +1.0116 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 129.4 | +129.400 (native is 0) | +72.0571 to +186.7429 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.86 | 9.633 | −11.3% | −3.3936 to +0.9402 | no |
| utilisation (used / allocatable) | 0.03117 | 0.04036 | +29.5% | +0.0037 to +0.0147 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.496 | 1.462 | −2.3% | −0.0660 to −0.0025 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04897 | +0.049 (native is 0) | +0.0467 to +0.0512 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.496 | 1.511 | +1.0% | −0.0182 to +0.0476 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851.2 | 712 | −16.4% | −234.5606 to −43.8354 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.054 | 4.327 | +6.7% | −0.1474 to +0.6929 | no |
| pods started | 0.1 | 1.5 | +1400.0% | −0.2242 to +3.0242 | no |
| pod start wait, total (s) | 0.2 | 3.7 | +1750.0% | −0.8215 to +7.8215 | no |
| pod start wait, mean (s) | 0.2 | 0.9167 | +358.3% | −0.3717 to +1.8050 | no |
| host CPU busy, the real machine under kind (%) | 49.31 | 49.24 | −0.1% | −0.8471 to +0.7040 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 819 | 778.2 | −5.0% | −61.6541 to −19.9459 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 7.165 | −40.3% | −6.7573 to −2.9136 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3083 | 0.06667 | −78.4% | −0.3882 to −0.0951 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.7 | −36.4% | −0.9001 to +0.1001 | no |
| queue: job turnaround, submitted to done, mean (s) | 128.4 | 89.36 | −30.4% | −58.9174 to −19.0826 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.884 | −17.6% | −3.6716 to −0.5594 | yes: GAIN |
| node-hours | 5.023 | 4.145 | −17.5% | −1.5354 to −0.2210 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 524.5 | +0.4% | +0.1059 to +4.2024 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 458 | −12.3% | −114.6582 to −14.0628 | yes: GAIN |
| response time (ms), mean | 275.8 | 394.7 | +43.1% | +40.0332 to +197.8951 | yes: LOSS |
| response time (ms), 95th percentile | 890.4 | 1930 | +116.7% | +433.4919 to +1644.7411 | yes: LOSS |
| response time (ms), 99th percentile | 1233 | 3207 | +160.0% | +935.7101 to +3010.9781 | yes: LOSS |
| time over the response line (% of samples) | 15.62 | 16.68 | +6.7% | −1.8397 to +3.9456 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 11 | +13.4% | −0.7525 to +3.3525 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 69.6 | +69.600 (native is 0) | +25.1355 to +114.0645 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.707 | 17.65 | +129.0% | +2.6344 to +17.2489 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03082 | 0.03935 | +27.7% | +0.0042 to +0.0129 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.479 | 1.531 | +3.5% | −0.0349 to +0.1384 | no |
| Omni's own CPU (cores), mean | 0 | 0.0352 | +0.035 (native is 0) | +0.0302 to +0.0402 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.566 | +5.9% | −0.0028 to +0.1768 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.2 | 714.6 | −16.3% | −206.8442 to −72.4376 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.953 | 4.485 | +13.4% | +0.1824 to +0.8809 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.8706 to +2.5294 | yes: power given |
| pod start wait, total (s) | 0 | 3.8 | +3.800 (native is 0) | +1.6996 to +5.9004 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.8 | +1.800 (native is 0) | +0.9977 to +2.6023 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.05 | 54.73 | +21.5% | +7.5555 to +11.8046 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 872 | +14.2% | +54.5073 to +162.8927 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.231 | −31.4% | −5.9061 to −1.6318 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.475 | +1040.0% | +0.2555 to +0.6112 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.3 | +333.3% | +0.5231 to +1.4769 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 75.95 | 177.4 | +133.6% | +48.4917 to +154.4583 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*