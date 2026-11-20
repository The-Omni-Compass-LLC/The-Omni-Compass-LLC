# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.619 | 4.75 |
| node-hours | 2.514 | 2.514 | 1.933 | 1.99 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 | 271.7 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271.7 | 228.3 | 232.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 279 | 280.5 | 296.8 | 294.5 |
| response time (ms), 95th percentile | 941.9 | 1006 | 1043 | 1077 |
| response time (ms), 99th percentile | 1351 | 1451 | 1513 | 1528 |
| time over the response line (% of samples) | 9.177 | 8.684 | 10.97 | 9.943 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.4 | 9.3 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 21.5 | 15 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 40 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.86 | 13.81 | 13.14 | 14.38 |
| utilisation (used / allocatable) | 0.05906 | 0.05885 | 0.07688 | 0.07343 |
| CPU used (cores), mean | 1.417 | 1.412 | 1.404 | 1.394 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06018 | 0.06347 |
| CPU used with Omni's own (cores), mean | 1.417 | 1.412 | 1.464 | 1.458 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.3 | 468.5 | 391 | 403.2 |
| HPA replicas, mean | 2.062 | 1.969 | 2.229 | 2.241 |
| pods started | 0 | 0.1 | 0.5 | 0.8 |
| pod start wait, total (s) | 0 | 0.2 | 1.3 | 1.4 |
| pod start wait, mean (s) | 0 | 0.2 | 0.95 | 0.7167 |
| host CPU busy, the real machine under kind (%) | 40.85 | 41.66 | 43.14 | 44.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 770.3 | 774.1 | 774.7 | 781.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.556 | 3.589 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 0.5042 | 0.175 | 1.146 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.8 | 1.2 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 74.63 | 78.88 | 79.25 | 84.19 |
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
| worker nodes in service, mean | 6 | 4.75 | −20.8% | −1.8744 to −0.6254 | yes: GAIN |
| node-hours | 2.514 | 1.99 | −20.8% | −0.7818 to −0.2660 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.5 | −0.1% | −1.5153 to +1.1848 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 232.2 | −14.5% | −59.1926 to −19.8046 | yes: GAIN |
| response time (ms), mean | 280.5 | 294.5 | +5.0% | −7.9177 to +35.7564 | no |
| response time (ms), 95th percentile | 1006 | 1077 | +7.0% | −46.6380 to +187.4180 | no |
| response time (ms), 99th percentile | 1451 | 1528 | +5.3% | −159.0446 to +312.8708 | no |
| time over the response line (% of samples) | 8.684 | 9.943 | +14.5% | −0.3658 to +2.8833 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 7.7 | +4.1% | −1.2099 to +1.8099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 | +15.000 (native is 0) | +10.3276 to +19.6724 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.81 | 14.38 | +4.1% | −3.3547 to +4.4981 | no |
| utilisation (used / allocatable) | 0.05885 | 0.07343 | +24.8% | +0.0079 to +0.0213 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.412 | 1.394 | −1.3% | −0.0716 to +0.0351 | no |
| Omni's own CPU (cores), mean | 0 | 0.06347 | +0.063 (native is 0) | +0.0567 to +0.0702 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.412 | 1.458 | +3.2% | −0.0106 to +0.1010 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 403.2 | −13.9% | −96.0661 to −34.5224 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.241 | +13.8% | +0.0090 to +0.5358 | yes: power given |
| pods started | 0.1 | 0.8 | +700.0% | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 0.2 | 1.4 | +600.0% | −0.2226 to +2.6226 | no |
| pod start wait, mean (s) | 0.2 | 0.7167 | +258.3% | −0.0846 to +1.1179 | no |
| host CPU busy, the real machine under kind (%) | 41.66 | 44.11 | +5.9% | +1.9491 to +2.9619 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 774.1 | 781.4 | +0.9% | +1.1186 to +13.4814 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.589 | −40.2% | −3.5290 to −1.2936 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5042 | 1.146 | +127.3% | −0.6743 to +1.9576 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.2 | +50.0% | −0.2911 to +1.0911 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.88 | 84.19 | +6.7% | +0.1161 to +10.5006 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.514 | +0.0% | −0.0074 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 | −0.0% | −0.7681 to +0.6467 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271.7 | −0.0% | −0.7681 to +0.6467 | no |
| response time (ms), mean | 279 | 280.5 | +0.5% | −10.1753 to +13.1708 | no |
| response time (ms), 95th percentile | 941.9 | 1006 | +6.8% | −40.2584 to +169.0374 | no |
| response time (ms), 99th percentile | 1351 | 1451 | +7.4% | −85.9627 to +285.6137 | no |
| time over the response line (% of samples) | 9.177 | 8.684 | −5.4% | −1.6803 to +0.6947 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.4 | −3.9% | −1.9537 to +1.3537 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.86 | 13.81 | +16.4% | −0.8253 to +4.7253 | no |
| utilisation (used / allocatable) | 0.05906 | 0.05885 | −0.3% | −0.0013 to +0.0009 | no |
| CPU used (cores), mean | 1.417 | 1.412 | −0.3% | −0.0322 to +0.0224 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.417 | 1.412 | −0.3% | −0.0322 to +0.0224 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.3 | 468.5 | +0.5% | −6.6403 to +10.9360 | no |
| HPA replicas, mean | 2.062 | 1.969 | −4.5% | −0.2505 to +0.0630 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.85 | 41.66 | +2.0% | +0.5802 to +1.0401 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 770.3 | 774.1 | +0.5% | −0.7466 to +8.3466 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 0.5042 | +95.2% | −0.3298 to +0.8214 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.8 | −46.7% | −3.5622 to +2.1622 | no |
| queue: job turnaround, submitted to done, mean (s) | 74.63 | 78.88 | +5.7% | −0.5659 to +9.0742 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.619 | −23.0% | −2.0434 to −0.7183 | yes: GAIN |
| node-hours | 2.514 | 1.933 | −23.1% | −0.8573 to −0.3036 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 | −0.0% | −0.7073 to +0.5926 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 228.3 | −16.0% | −64.2318 to −22.5996 | yes: GAIN |
| response time (ms), mean | 279 | 296.8 | +6.4% | +7.2469 to +28.2496 | yes: LOSS |
| response time (ms), 95th percentile | 941.9 | 1043 | +10.7% | +35.0560 to +167.1590 | yes: LOSS |
| response time (ms), 99th percentile | 1351 | 1513 | +12.0% | +25.6127 to +298.2955 | yes: LOSS |
| time over the response line (% of samples) | 9.177 | 10.97 | +19.6% | −0.0394 to +3.6340 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 9.3 | +20.8% | −0.1586 to +3.3586 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.5 | +21.500 (native is 0) | +16.1551 to +26.8449 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.86 | 13.14 | +10.8% | −1.8966 to +4.4566 | no |
| utilisation (used / allocatable) | 0.05906 | 0.07688 | +30.2% | +0.0085 to +0.0271 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.417 | 1.404 | −0.9% | −0.0479 to +0.0210 | no |
| Omni's own CPU (cores), mean | 0 | 0.06018 | +0.060 (native is 0) | +0.0545 to +0.0658 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.417 | 1.464 | +3.3% | +0.0139 to +0.0796 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.3 | 391 | −16.1% | −113.3153 to −37.2788 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.062 | 2.229 | +8.1% | −0.0330 to +0.3670 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | −0.3877 to +2.9877 | no |
| pod start wait, mean (s) | 0 | 0.95 | +0.950 (native is 0) | −0.1485 to +2.0485 | no |
| host CPU busy, the real machine under kind (%) | 40.85 | 43.14 | +5.6% | +2.0100 to +2.5760 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 770.3 | 774.7 | +0.6% | −0.7933 to +9.5933 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.556 | −40.7% | −3.4545 to −1.4326 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 0.175 | −32.3% | −0.3064 to +0.1397 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.2 | −20.0% | −2.7560 to +2.1560 | no |
| queue: job turnaround, submitted to done, mean (s) | 74.63 | 79.25 | +6.2% | +0.5126 to +8.7374 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.619 | −23.0% | −2.0434 to −0.7183 | yes: GAIN |
| node-hours | 2.514 | 1.933 | −23.1% | −0.8560 to −0.3062 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 | +0.0% | −0.7802 to +0.7870 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 228.3 | −16.0% | −63.8268 to −22.8831 | yes: GAIN |
| response time (ms), mean | 280.5 | 296.8 | +5.8% | +5.6782 to +26.8228 | yes: LOSS |
| response time (ms), 95th percentile | 1006 | 1043 | +3.6% | −29.4597 to +102.8957 | no |
| response time (ms), 99th percentile | 1451 | 1513 | +4.3% | −24.3933 to +148.6505 | no |
| time over the response line (% of samples) | 8.684 | 10.97 | +26.4% | +0.4976 to +4.0827 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 9.3 | +25.7% | +0.8634 to +2.9366 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.5 | +21.500 (native is 0) | +16.1551 to +26.8449 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.81 | 13.14 | −4.9% | −3.2948 to +1.9548 | no |
| utilisation (used / allocatable) | 0.05885 | 0.07688 | +30.6% | +0.0084 to +0.0277 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.412 | 1.404 | −0.6% | −0.0262 to +0.0091 | no |
| Omni's own CPU (cores), mean | 0 | 0.06018 | +0.060 (native is 0) | +0.0545 to +0.0658 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.412 | 1.464 | +3.7% | +0.0329 to +0.0703 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 391 | −16.5% | −118.4819 to −36.4078 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.229 | +13.2% | +0.0635 to +0.4580 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | −0.4617 to +2.6617 | no |
| pod start wait, mean (s) | 0.2 | 0.95 | +375.0% | −0.0972 to +1.5972 | no |
| host CPU busy, the real machine under kind (%) | 41.66 | 43.14 | +3.6% | +1.1773 to +1.7884 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 774.1 | 774.7 | +0.1% | −1.1586 to +2.3586 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.556 | −40.7% | −3.4545 to −1.4326 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5042 | 0.175 | −65.3% | −0.8770 to +0.2187 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.2 | +50.0% | −1.0385 to +1.8385 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.88 | 79.25 | +0.5% | −3.6878 to +4.4295 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.75 | −20.8% | −1.8744 to −0.6254 | yes: GAIN |
| node-hours | 2.514 | 1.99 | −20.8% | −0.7821 to −0.2644 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.5 | −0.1% | −1.7986 to +1.3467 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 232.2 | −14.6% | −59.5422 to −19.5764 | yes: GAIN |
| response time (ms), mean | 279 | 294.5 | +5.5% | −0.2519 to +31.0860 | no |
| response time (ms), 95th percentile | 941.9 | 1077 | +14.3% | −14.8409 to +284.3999 | no |
| response time (ms), 99th percentile | 1351 | 1528 | +13.1% | −2.0860 to +355.5632 | no |
| time over the response line (% of samples) | 9.177 | 9.943 | +8.3% | −1.1059 to +2.6378 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.7 | ±0.0% | −1.6519 to +1.6519 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 | +15.000 (native is 0) | +10.3276 to +19.6724 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.86 | 14.38 | +21.3% | −3.3218 to +8.3651 | no |
| utilisation (used / allocatable) | 0.05906 | 0.07343 | +24.3% | +0.0082 to +0.0205 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.417 | 1.394 | −1.6% | −0.0875 to +0.0412 | no |
| Omni's own CPU (cores), mean | 0 | 0.06347 | +0.063 (native is 0) | +0.0567 to +0.0702 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.417 | 1.458 | +2.8% | −0.0254 to +0.1061 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.3 | 403.2 | −13.5% | −89.8001 to −36.4926 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.062 | 2.241 | +8.7% | −0.0921 to +0.4495 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | +0.0015 to +2.7985 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.7167 | +0.717 (native is 0) | +0.0469 to +1.3865 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.85 | 44.11 | +8.0% | +2.8141 to +3.7172 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 770.3 | 781.4 | +1.4% | +1.6798 to +20.5202 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.589 | −40.2% | −3.5290 to −1.2936 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 1.146 | +343.5% | −0.3169 to +2.0919 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.2 | −20.0% | −3.2980 to +2.6980 | no |
| queue: job turnaround, submitted to done, mean (s) | 74.63 | 84.19 | +12.8% | +2.8050 to +16.3200 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*