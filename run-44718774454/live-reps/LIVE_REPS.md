# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.708 | 4.842 |
| node-hours | 2.516 | 2.517 | 1.975 | 2.028 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.7 | 272.7 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.7 | 232.1 | 236.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 328 | 297.2 | 318.6 | 288.1 |
| response time (ms), 95th percentile | 1144 | 1124 | 1283 | 1317 |
| response time (ms), 99th percentile | 1589 | 1697 | 1793 | 1882 |
| time over the response line (% of samples) | 12.29 | 9.263 | 13.67 | 9.515 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 7.2 | 9.1 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 117.6 | 89.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 31.25 | 41.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.595 | 12.04 | 12.71 | 14.51 |
| utilisation (used / allocatable) | 0.06019 | 0.05982 | 0.07718 | 0.07691 |
| CPU used (cores), mean | 1.445 | 1.436 | 1.437 | 1.453 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07412 | 0.07386 |
| CPU used with Omni's own (cores), mean | 1.445 | 1.436 | 1.511 | 1.527 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 462.5 | 387.3 | 390.4 |
| HPA replicas, mean | 1.948 | 2.028 | 2.182 | 2.285 |
| pods started | 0.1 | 0.4 | 1.2 | 1.2 |
| pod start wait, total (s) | 0.3 | 0.5 | 2.5 | 2.2 |
| pod start wait, mean (s) | 0.3 | 0.35 | 1.483 | 0.925 |
| host CPU busy, the real machine under kind (%) | 41.57 | 41.74 | 44.95 | 45.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 776.6 | 781 | 787.4 | 787.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.738 | 4.056 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.3292 | 0.1417 | 0.2458 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | 0.7 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 82.05 | 88.53 | 91.64 | 94.23 |
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
| worker nodes in service, mean | 6 | 4.842 | −19.3% | −1.9364 to −0.3789 | yes: GAIN |
| node-hours | 2.517 | 2.028 | −19.4% | −0.8137 to −0.1645 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.8 | +0.0% | −0.5487 to +0.7539 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 236.4 | −13.3% | −60.5723 to −11.9892 | yes: GAIN |
| response time (ms), mean | 297.2 | 288.1 | −3.1% | −36.3473 to +18.1248 | no |
| response time (ms), 95th percentile | 1124 | 1317 | +17.1% | −48.4326 to +433.2266 | no |
| response time (ms), 99th percentile | 1697 | 1882 | +10.9% | +36.0243 to +333.6113 | yes: LOSS |
| time over the response line (% of samples) | 9.263 | 9.515 | +2.7% | −0.5448 to +1.0487 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.9 | +9.7% | −0.1294 to +1.5294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +39.9456 to +139.2544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.04 | 14.51 | +20.5% | −0.9977 to +5.9343 | no |
| utilisation (used / allocatable) | 0.05982 | 0.07691 | +28.6% | +0.0051 to +0.0291 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 1.453 | +1.2% | −0.0034 to +0.0374 | no |
| Omni's own CPU (cores), mean | 0 | 0.07386 | +0.074 (native is 0) | +0.0676 to +0.0801 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.527 | +6.3% | +0.0714 to +0.1104 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.5 | 390.4 | −15.6% | −119.3110 to −24.9577 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.028 | 2.285 | +12.7% | −0.0210 to +0.5367 | no |
| pods started | 0.4 | 1.2 | +200.0% | −0.6226 to +2.2226 | no |
| pod start wait, total (s) | 0.5 | 2.2 | +340.0% | −0.8245 to +4.2245 | no |
| pod start wait, mean (s) | 0.35 | 0.925 | +164.3% | −0.4523 to +1.6023 | no |
| host CPU busy, the real machine under kind (%) | 41.74 | 45.02 | +7.8% | +2.8502 to +3.6969 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781 | 787.7 | +0.9% | −0.9823 to +14.3823 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.056 | −32.4% | −3.0247 to −0.8633 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3292 | 0.2458 | −25.3% | −0.6075 to +0.4409 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | −1.3871 to +1.5871 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.53 | 94.23 | +6.4% | −0.9977 to +12.3977 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.517 | +0.1% | −0.0071 to +0.0097 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.7 | +0.1% | −0.6389 to +0.9958 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.7 | +0.1% | −0.6389 to +0.9958 | no |
| response time (ms), mean | 328 | 297.2 | −9.4% | −65.6901 to +3.9802 | no |
| response time (ms), 95th percentile | 1144 | 1124 | −1.7% | −199.5581 to +160.7061 | no |
| response time (ms), 99th percentile | 1589 | 1697 | +6.8% | −102.0113 to +318.5727 | no |
| time over the response line (% of samples) | 12.29 | 9.263 | −24.6% | −5.9518 to −0.1058 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 7.2 | −14.3% | −2.6621 to +0.2621 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.595 | 12.04 | +25.5% | −0.4816 to +5.3783 | no |
| utilisation (used / allocatable) | 0.06019 | 0.05982 | −0.6% | −0.0011 to +0.0003 | no |
| CPU used (cores), mean | 1.445 | 1.436 | −0.6% | −0.0260 to +0.0083 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.445 | 1.436 | −0.6% | −0.0260 to +0.0083 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 462.5 | +0.9% | −2.7852 to +10.7361 | no |
| HPA replicas, mean | 1.948 | 2.028 | +4.1% | −0.0497 to +0.2079 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | −0.8556 to +1.2556 | no |
| pod start wait, mean (s) | 0.3 | 0.35 | +16.7% | −0.8171 to +0.9171 | no |
| host CPU busy, the real machine under kind (%) | 41.57 | 41.74 | +0.4% | −0.1803 to +0.5344 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.6 | 781 | +0.6% | −0.0249 to +8.8249 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.3292 | +338.9% | −0.3435 to +0.8518 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | +166.7% | −0.4685 to +1.4685 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.05 | 88.53 | +7.9% | +1.0974 to +11.8693 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.708 | −21.5% | −1.9927 to −0.5910 | yes: GAIN |
| node-hours | 2.516 | 1.975 | −21.5% | −0.8335 to −0.2491 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.7 | +0.0% | −0.6963 to +0.9288 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 232.1 | −14.9% | −62.6428 to −18.3205 | yes: GAIN |
| response time (ms), mean | 328 | 318.6 | −2.9% | −28.8282 to +10.0469 | no |
| response time (ms), 95th percentile | 1144 | 1283 | +12.2% | +3.5916 to +274.6124 | yes: LOSS |
| response time (ms), 99th percentile | 1589 | 1793 | +12.8% | −55.3077 to +463.1151 | no |
| time over the response line (% of samples) | 12.29 | 13.67 | +11.2% | −0.5079 to +3.2705 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.1 | +8.3% | +0.0214 to +1.3786 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.6 | +117.600 (native is 0) | +41.8163 to +193.3837 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.595 | 12.71 | +32.5% | +0.1133 to +6.1234 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06019 | 0.07718 | +28.2% | +0.0077 to +0.0263 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.437 | −0.5% | −0.0424 to +0.0278 | no |
| Omni's own CPU (cores), mean | 0 | 0.07412 | +0.074 (native is 0) | +0.0682 to +0.0801 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.511 | +4.6% | +0.0282 to +0.1055 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 387.3 | −15.5% | −107.9740 to −34.5575 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.182 | +12.0% | +0.1001 to +0.3672 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.5 | +733.3% | +0.5208 to +3.8792 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.483 | +394.4% | +0.5009 to +1.8658 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.57 | 44.95 | +8.1% | +2.8019 to +3.9638 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.6 | 787.4 | +1.4% | +2.1516 to +19.4484 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.738 | −37.7% | −3.2802 to −1.2448 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.1417 | +88.9% | −0.0653 to +0.1986 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | −0.5048 to +1.3048 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.05 | 91.64 | +11.7% | +1.4691 to +17.7143 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.708 | −21.5% | −1.9927 to −0.5910 | yes: GAIN |
| node-hours | 2.517 | 1.975 | −21.6% | −0.8365 to −0.2488 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.7 | −0.0% | −1.2133 to +1.0890 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 232.1 | −14.9% | −62.9527 to −18.3674 | yes: GAIN |
| response time (ms), mean | 297.2 | 318.6 | +7.2% | −17.5003 to +60.4289 | no |
| response time (ms), 95th percentile | 1124 | 1283 | +14.1% | +47.3064 to +269.7496 | yes: LOSS |
| response time (ms), 99th percentile | 1697 | 1793 | +5.6% | +34.3900 to +156.8560 | yes: LOSS |
| time over the response line (% of samples) | 9.263 | 13.67 | +47.6% | +1.5774 to +7.2428 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 9.1 | +26.4% | +0.3383 to +3.4617 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.6 | +117.600 (native is 0) | +41.8163 to +193.3837 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.04 | 12.71 | +5.6% | −1.0335 to +2.3735 | no |
| utilisation (used / allocatable) | 0.05982 | 0.07718 | +29.0% | +0.0077 to +0.0271 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 1.437 | +0.1% | −0.0228 to +0.0260 | no |
| Omni's own CPU (cores), mean | 0 | 0.07412 | +0.074 (native is 0) | +0.0682 to +0.0801 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.511 | +5.3% | +0.0469 to +0.1046 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.5 | 387.3 | −16.3% | −115.9412 to −34.5411 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.028 | 2.182 | +7.6% | −0.0291 to +0.3382 | no |
| pods started | 0.4 | 1.2 | +200.0% | −0.2556 to +1.8556 | no |
| pod start wait, total (s) | 0.5 | 2.5 | +400.0% | −0.1058 to +4.1058 | no |
| pod start wait, mean (s) | 0.35 | 1.483 | +323.8% | −0.0731 to +2.3397 | no |
| host CPU busy, the real machine under kind (%) | 41.74 | 44.95 | +7.7% | +2.7546 to +3.6570 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781 | 787.4 | +0.8% | −0.0351 to +12.8351 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.738 | −37.7% | −3.2802 to −1.2448 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3292 | 0.1417 | −57.0% | −0.6734 to +0.2984 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 | −12.5% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.53 | 91.64 | +3.5% | −1.6817 to +7.8984 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.842 | −19.3% | −1.9364 to −0.3789 | yes: GAIN |
| node-hours | 2.516 | 2.028 | −19.4% | −0.8086 to −0.1669 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.8 | +0.1% | −0.4520 to +1.0141 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 236.4 | −13.2% | −60.0786 to −12.1260 | yes: GAIN |
| response time (ms), mean | 328 | 288.1 | −12.2% | −60.4916 to −19.4409 | yes: GAIN |
| response time (ms), 95th percentile | 1144 | 1317 | +15.1% | −49.3334 to +395.2754 | no |
| response time (ms), 99th percentile | 1589 | 1882 | +18.4% | −34.3171 to +620.5141 | no |
| time over the response line (% of samples) | 12.29 | 9.515 | −22.6% | −6.2546 to +0.7009 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 7.9 | −6.0% | −1.7274 to +0.7274 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +39.9456 to +139.2544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.595 | 14.51 | +51.2% | +1.1932 to +8.6401 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06019 | 0.07691 | +27.8% | +0.0051 to +0.0283 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.453 | +0.6% | −0.0155 to +0.0318 | no |
| Omni's own CPU (cores), mean | 0 | 0.07386 | +0.074 (native is 0) | +0.0676 to +0.0801 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.527 | +5.7% | +0.0564 to +0.1076 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 390.4 | −14.9% | −111.2178 to −25.1001 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.285 | +17.3% | +0.0459 to +0.6281 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.2 | +633.3% | −0.2179 to +4.0179 | no |
| pod start wait, mean (s) | 0.3 | 0.925 | +208.3% | −0.2895 to +1.5395 | no |
| host CPU busy, the real machine under kind (%) | 41.57 | 45.02 | +8.3% | +2.8902 to +4.0109 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.6 | 787.7 | +1.4% | +1.4297 to +20.7703 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.056 | −32.4% | −3.0247 to −0.8633 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.2458 | +227.8% | −0.0791 to +0.4208 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.9 | +200.0% | −0.2396 to +1.4396 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.05 | 94.23 | +14.8% | +2.4389 to +21.9278 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*