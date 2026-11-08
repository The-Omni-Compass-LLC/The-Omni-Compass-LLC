# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.452 | 4.396 |
| node-hours | 2.517 | 2.515 | 1.863 | 1.842 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | 271.5 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.6 | 222.8 | 220.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 270.8 | 280.2 | 293.8 | 297.6 |
| response time (ms), 95th percentile | 916.5 | 1021 | 1025 | 1100 |
| response time (ms), 99th percentile | 1355 | 1519 | 1445 | 1496 |
| time over the response line (% of samples) | 8.888 | 8.498 | 10.44 | 10.08 |
| failed requests (%) | 0 | 0 | 0 | 0.0122 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.5 | 8.6 | 8.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 18 | 19.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 48.57 | 77.08 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 12.36 | 13.11 | 15.78 |
| utilisation (used / allocatable) | 0.05862 | 0.05875 | 0.07986 | 0.07637 |
| CPU used (cores), mean | 1.407 | 1.41 | 1.39 | 1.348 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05802 | 0.06279 |
| CPU used with Omni's own (cores), mean | 1.407 | 1.41 | 1.448 | 1.41 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 468.8 | 385.2 | 396.9 |
| HPA replicas, mean | 2.094 | 2.133 | 2.384 | 2.16 |
| pods started | 0.1 | 0.2 | 1.4 | 0.4 |
| pod start wait, total (s) | 0.2 | 0.2 | 3.1 | 0.8 |
| pod start wait, mean (s) | 0.2 | 0.1 | 1.317 | 0.65 |
| host CPU busy, the real machine under kind (%) | 40.43 | 41.47 | 42.95 | 43.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 767.5 | 770.6 | 775.9 | 777 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.411 | 3.022 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.8083 | 0.325 | 0.4792 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | 1.2 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 71.98 | 77.81 | 78.88 | 82.86 |
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
| worker nodes in service, mean | 6 | 4.396 | −26.7% | −2.1898 to −1.0183 | yes: GAIN |
| node-hours | 2.515 | 1.842 | −26.7% | −0.9167 to −0.4283 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.2 | −0.2% | −1.8630 to +0.9451 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 220.8 | −18.7% | −69.6144 to −32.1035 | yes: GAIN |
| response time (ms), mean | 280.2 | 297.6 | +6.2% | +3.1814 to +31.5033 | yes: LOSS |
| response time (ms), 95th percentile | 1021 | 1100 | +7.8% | +3.8363 to +154.5487 | yes: LOSS |
| response time (ms), 99th percentile | 1519 | 1496 | −1.5% | −205.5072 to +159.3566 | no |
| time over the response line (% of samples) | 8.498 | 10.08 | +18.6% | +0.1913 to +2.9771 | yes: LOSS |
| failed requests (%) | 0 | 0.0122 | +0.012 (native is 0) | −0.0154 to +0.0398 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 8.4 | +12.0% | −0.2898 to +2.0898 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | +19.700 (native is 0) | +13.9079 to +25.4921 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.36 | 15.78 | +27.7% | +1.0144 to +5.8223 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05875 | 0.07637 | +30.0% | +0.0118 to +0.0234 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.41 | 1.348 | −4.4% | −0.1193 to −0.0054 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06279 | +0.063 (native is 0) | +0.0562 to +0.0694 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.41 | +0.0% | −0.0603 to +0.0612 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.8 | 396.9 | −15.3% | −97.1768 to −46.5722 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.133 | 2.16 | +1.3% | −0.1564 to +0.2104 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.5285 to +1.7285 | no |
| pod start wait, mean (s) | 0.1 | 0.65 | +550.0% | −0.3171 to +1.4171 | no |
| host CPU busy, the real machine under kind (%) | 41.47 | 43.75 | +5.5% | +1.9245 to +2.6466 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 770.6 | 777 | +0.8% | +1.8360 to +10.9640 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.022 | −49.6% | −3.9303 to −2.0261 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8083 | 0.4792 | −40.7% | −1.9592 to +1.3009 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.9 | −18.2% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.81 | 82.86 | +6.5% | +1.5042 to +8.5874 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.515 | −0.1% | −0.0105 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | −0.1% | −1.0425 to +0.5524 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.6 | −0.1% | −1.0425 to +0.5524 | no |
| response time (ms), mean | 270.8 | 280.2 | +3.5% | −5.6251 to +24.4337 | no |
| response time (ms), 95th percentile | 916.5 | 1021 | +11.4% | −44.0158 to +253.2758 | no |
| response time (ms), 99th percentile | 1355 | 1519 | +12.1% | −39.8417 to +366.5309 | no |
| time over the response line (% of samples) | 8.888 | 8.498 | −4.4% | −1.9082 to +1.1281 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.5 | −3.8% | −1.6924 to +1.0924 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 12.36 | +19.6% | −2.9688 to +7.0155 | no |
| utilisation (used / allocatable) | 0.05862 | 0.05875 | +0.2% | −0.0008 to +0.0011 | no |
| CPU used (cores), mean | 1.407 | 1.41 | +0.2% | −0.0194 to +0.0255 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.407 | 1.41 | +0.2% | −0.0194 to +0.0255 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 468.8 | −0.0% | −7.7271 to +7.3247 | no |
| HPA replicas, mean | 2.094 | 2.133 | +1.8% | −0.1530 to +0.2301 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 40.43 | 41.47 | +2.6% | +0.6808 to +1.4033 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.5 | 770.6 | +0.4% | −1.9854 to +8.1854 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.8083 | +1285.7% | −0.6956 to +2.1956 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | +175.0% | +0.3545 to +1.0455 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 71.98 | 77.81 | +8.1% | −0.3481 to +12.0148 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.452 | −25.8% | −2.3428 to −0.7526 | yes: GAIN |
| node-hours | 2.517 | 1.863 | −26.0% | −0.9832 to −0.3247 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.5 | −0.1% | −1.0758 to +0.3536 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 222.8 | −18.0% | −73.8128 to −24.2510 | yes: GAIN |
| response time (ms), mean | 270.8 | 293.8 | +8.5% | +6.8283 to +39.1069 | yes: LOSS |
| response time (ms), 95th percentile | 916.5 | 1025 | +11.8% | +42.2236 to +174.6764 | yes: LOSS |
| response time (ms), 99th percentile | 1355 | 1445 | +6.6% | +35.1539 to +144.4013 | yes: LOSS |
| time over the response line (% of samples) | 8.888 | 10.44 | +17.5% | +0.4303 to +2.6739 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.6 | +10.3% | −0.3081 to +1.9081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +13.1957 to +22.8043 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 13.11 | +26.8% | −2.5833 to +8.1333 | no |
| utilisation (used / allocatable) | 0.05862 | 0.07986 | +36.2% | +0.0100 to +0.0324 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.407 | 1.39 | −1.2% | −0.0559 to +0.0212 | no |
| Omni's own CPU (cores), mean | 0 | 0.05802 | +0.058 (native is 0) | +0.0517 to +0.0643 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.448 | +2.9% | −0.0010 to +0.0823 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 385.2 | −17.9% | −126.6384 to −40.9363 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.094 | 2.384 | +13.8% | +0.0083 to +0.5711 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.2310 to +2.3690 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.1 | +1450.0% | +0.5288 to +5.2712 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.317 | +558.3% | +0.0327 to +2.2007 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.43 | 42.95 | +6.2% | +1.8351 to +3.2031 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.5 | 775.9 | +1.1% | −1.2158 to +18.0158 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.411 | −43.2% | −3.6716 to −1.5067 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.325 | +457.1% | −0.0832 to +0.6166 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.2 | +200.0% | −0.3583 to +1.9583 | no |
| queue: job turnaround, submitted to done, mean (s) | 71.98 | 78.88 | +9.6% | −0.3011 to +14.1094 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.452 | −25.8% | −2.3428 to −0.7526 | yes: GAIN |
| node-hours | 2.515 | 1.863 | −25.9% | −0.9824 to −0.3205 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.5 | −0.0% | −0.9113 to +0.6792 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 222.8 | −18.0% | −73.6863 to −23.8875 | yes: GAIN |
| response time (ms), mean | 280.2 | 293.8 | +4.8% | +3.0962 to +24.0305 | yes: LOSS |
| response time (ms), 95th percentile | 1021 | 1025 | +0.4% | −99.1713 to +106.8113 | no |
| response time (ms), 99th percentile | 1519 | 1445 | −4.8% | −270.6616 to +123.5276 | no |
| time over the response line (% of samples) | 8.498 | 10.44 | +22.9% | +0.2593 to +3.6250 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 8.6 | +14.7% | −0.1818 to +2.3818 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +13.1957 to +22.8043 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.36 | 13.11 | +6.1% | +0.0061 to +1.4973 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05875 | 0.07986 | +35.9% | +0.0098 to +0.0324 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.41 | 1.39 | −1.5% | −0.0566 to +0.0157 | no |
| Omni's own CPU (cores), mean | 0 | 0.05802 | +0.058 (native is 0) | +0.0517 to +0.0643 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.448 | +2.7% | −0.0020 to +0.0772 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.8 | 385.2 | −17.8% | −127.4223 to −39.7499 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.133 | 2.384 | +11.8% | −0.0151 to +0.5173 | no |
| pods started | 0.2 | 1.4 | +600.0% | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.1 | +1450.0% | +0.8923 to +4.9077 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.317 | +1216.7% | +0.4378 to +1.9955 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.47 | 42.95 | +3.6% | +0.8641 to +2.0900 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 770.6 | 775.9 | +0.7% | −0.0000 to +10.6000 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.411 | −43.2% | −3.6716 to −1.5067 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8083 | 0.325 | −59.8% | −1.7546 to +0.7880 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.2 | +9.1% | −1.2254 to +1.4254 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.81 | 78.88 | +1.4% | −2.8890 to +5.0307 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.396 | −26.7% | −2.1898 to −1.0183 | yes: GAIN |
| node-hours | 2.517 | 1.842 | −26.8% | −0.9190 to −0.4310 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.2 | −0.3% | −1.8089 to +0.4009 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 220.8 | −18.8% | −69.9344 to −32.2736 | yes: GAIN |
| response time (ms), mean | 270.8 | 297.6 | +9.9% | +2.5050 to +50.9882 | yes: LOSS |
| response time (ms), 95th percentile | 916.5 | 1100 | +20.1% | +1.9669 to +365.6781 | yes: LOSS |
| response time (ms), 99th percentile | 1355 | 1496 | +10.3% | +30.8214 to +249.7172 | yes: LOSS |
| time over the response line (% of samples) | 8.888 | 10.08 | +13.4% | −0.6974 to +3.0857 | no |
| failed requests (%) | 0 | 0.0122 | +0.012 (native is 0) | −0.0154 to +0.0398 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.4 | +7.7% | −0.6251 to +1.8251 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | +19.700 (native is 0) | +13.9079 to +25.4921 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.34 | 15.78 | +52.6% | −1.4058 to +12.2891 | no |
| utilisation (used / allocatable) | 0.05862 | 0.07637 | +30.3% | +0.0123 to +0.0232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.407 | 1.348 | −4.2% | −0.1152 to −0.0033 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06279 | +0.063 (native is 0) | +0.0562 to +0.0694 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.41 | +0.3% | −0.0563 to +0.0633 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 396.9 | −15.4% | −95.1727 to −48.9787 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.094 | 2.16 | +3.1% | −0.1244 to +0.2556 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.5285 to +1.7285 | no |
| pod start wait, mean (s) | 0.2 | 0.65 | +225.0% | −0.5396 to +1.4396 | no |
| host CPU busy, the real machine under kind (%) | 40.43 | 43.75 | +8.2% | +2.8575 to +3.7978 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.5 | 777 | +1.2% | +0.3443 to +18.6557 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.022 | −49.6% | −3.9303 to −2.0261 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.4792 | +721.4% | −0.2727 to +1.1143 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | +125.0% | +0.1230 to +0.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 71.98 | 82.86 | +15.1% | +2.9026 to +18.8557 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*