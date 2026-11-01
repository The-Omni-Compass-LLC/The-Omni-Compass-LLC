# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.56 | 5.975 |
| node-hours | 2.512 | 2.51 | 2.328 | 2.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 285.8 | 273.4 | 287.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 285.8 | 259.6 | 286.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 401 | 707.8 | 377.8 | 699.9 |
| response time (ms), 95th percentile | 1447 | 1445 | 1540 | 1431 |
| response time (ms), 99th percentile | 2098 | 1903 | 2218 | 1939 |
| time over the response line (% of samples) | 17.99 | 64.76 | 17.97 | 63.31 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 24.3 | 10.2 | 24.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 32.3 | 18.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.07 | 2.238 | 11.67 | 2.298 |
| utilisation (used / allocatable) | 0.06331 | 0.09697 | 0.06835 | 0.09833 |
| CPU used (cores), mean | 1.519 | 2.327 | 1.515 | 2.352 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01619 | 0.00944 |
| CPU used with Omni's own (cores), mean | 1.519 | 2.327 | 1.531 | 2.361 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 294.9 | 414.2 | 291.2 |
| HPA replicas, mean | 1.965 | 2.056 | 2.078 | 2.836 |
| pods started | 0 | 0.2 | 0.2 | 1 |
| pod start wait, total (s) | 0 | 0.2 | 0.4 | 3.2 |
| pod start wait, mean (s) | 0 | 0.1 | 0.4 | 2.5 |
| host CPU busy, the real machine under kind (%) | 43.1 | 75.48 | 44.14 | 75.73 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 799.3 | 1464 | 807.3 | 1470 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.22 | 5.111 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 688.6 | 0.0375 | 642.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1254 | 0.3 | 1240 |
| queue: job turnaround, submitted to done, mean (s) | 106 | 964.4 | 110.9 | 959.4 |
| queue: jobs unfinished at the window's end | 0 | 15.7 | 0 | 14.8 |
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
| worker nodes in service, mean | 6 | 5.975 | −0.4% | −0.0803 to +0.0311 | no |
| node-hours | 2.51 | 2.512 | +0.1% | −0.0195 to +0.0241 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 287.5 | +0.6% | +0.9943 to +2.5206 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 286.8 | +0.3% | −0.6789 to +2.6396 | no |
| response time (ms), mean | 707.8 | 699.9 | −1.1% | −48.9857 to +33.1641 | no |
| response time (ms), 95th percentile | 1445 | 1431 | −1.0% | −122.0313 to +93.8323 | no |
| response time (ms), 99th percentile | 1903 | 1939 | +1.9% | −133.3368 to +205.8404 | no |
| time over the response line (% of samples) | 64.76 | 63.31 | −2.2% | −5.1377 to +2.2449 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.3 | 24.3 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 | +18.900 (native is 0) | +13.9162 to +23.8838 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.238 | 2.298 | +2.7% | −0.5615 to +0.6815 | no |
| utilisation (used / allocatable) | 0.09697 | 0.09833 | +1.4% | +0.0001 to +0.0026 | yes, up (shown, not judged) |
| CPU used (cores), mean | 2.327 | 2.352 | +1.1% | +0.0012 to +0.0481 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00944 | +0.009 (native is 0) | +0.0086 to +0.0103 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.327 | 2.361 | +1.5% | +0.0110 to +0.0571 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294.9 | 291.2 | −1.3% | −7.2402 to −0.2086 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.056 | 2.836 | +37.9% | +0.5145 to +1.0440 | yes: power given |
| pods started | 0.2 | 1 | +400.0% | +0.1427 to +1.4573 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.2 | +1500.0% | +0.9768 to +5.0232 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 2.5 | +2400.0% | +1.1866 to +3.6134 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 75.48 | 75.73 | +0.3% | +0.1739 to +0.3335 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1464 | 1470 | +0.4% | +3.2091 to +9.7909 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.111 | −14.8% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 688.6 | 642.8 | −6.7% | −123.4432 to +31.7365 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1254 | 1240 | −1.1% | −69.0075 to +40.6377 | no |
| queue: job turnaround, submitted to done, mean (s) | 964.4 | 959.4 | −0.5% | −40.8213 to +30.8047 | no |
| queue: jobs unfinished at the window's end | 15.7 | 14.8 | −5.7% | −2.6986 to +0.8986 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.51 | −0.1% | −0.0058 to +0.0025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 285.8 | +4.6% | +9.9740 to +14.9904 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 285.8 | +4.6% | +9.9740 to +14.9904 | yes: power given |
| response time (ms), mean | 401 | 707.8 | +76.5% | +216.5516 to +397.0946 | yes: LOSS |
| response time (ms), 95th percentile | 1447 | 1445 | −0.1% | −645.3234 to +641.1324 | no |
| response time (ms), 99th percentile | 2098 | 1903 | −9.3% | −1180.9627 to +790.9131 | no |
| time over the response line (% of samples) | 17.99 | 64.76 | +259.9% | +39.2835 to +54.2458 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 24.3 | +150.5% | +10.8270 to +18.3730 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.07 | 2.238 | −79.8% | −10.6070 to −7.0663 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06331 | 0.09697 | +53.2% | +0.0266 to +0.0407 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.519 | 2.327 | +53.2% | +0.6377 to +0.9780 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.519 | 2.327 | +53.2% | +0.6377 to +0.9780 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 294.9 | −32.7% | −183.5612 to −102.5110 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.965 | 2.056 | +4.7% | −0.0728 to +0.2561 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 43.1 | 75.48 | +75.1% | +28.3021 to +36.4581 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 799.3 | 1464 | +83.1% | +570.0409 to +758.5591 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 688.6 | +972104.3% | +454.9458 to +922.2019 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1254 | +250641.5% | +948.1940 to +1558.2207 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 106 | 964.4 | +809.5% | +724.6153 to +992.0930 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.7 | +15.700 (native is 0) | +10.7666 to +20.6334 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.56 | −7.3% | −0.9724 to +0.0930 | no |
| node-hours | 2.512 | 2.328 | −7.3% | −0.4063 to +0.0397 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.4 | +0.0% | −0.4515 to +0.6278 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 259.6 | −5.0% | −30.6649 to +3.2246 | no |
| response time (ms), mean | 401 | 377.8 | −5.8% | −46.3764 to −0.0014 | yes: GAIN |
| response time (ms), 95th percentile | 1447 | 1540 | +6.4% | −53.9304 to +238.4894 | no |
| response time (ms), 99th percentile | 2098 | 2218 | +5.8% | −138.8426 to +380.1116 | no |
| time over the response line (% of samples) | 17.99 | 17.97 | −0.1% | −0.6567 to +0.6197 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.2 | +5.2% | −0.8593 to +1.8593 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 | +32.300 (native is 0) | +14.9022 to +49.6978 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.07 | 11.67 | +5.4% | −1.6670 to +2.8604 | no |
| utilisation (used / allocatable) | 0.06331 | 0.06835 | +8.0% | −0.0011 to +0.0112 | no |
| CPU used (cores), mean | 1.519 | 1.515 | −0.3% | −0.0275 to +0.0184 | no |
| Omni's own CPU (cores), mean | 0 | 0.01619 | +0.016 (native is 0) | +0.0149 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.519 | 1.531 | +0.8% | −0.0120 to +0.0354 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 414.2 | −5.4% | −52.0346 to +4.5050 | no |
| HPA replicas, mean | 1.965 | 2.078 | +5.8% | −0.0734 to +0.3000 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 43.1 | 44.14 | +2.4% | +0.8627 to +1.2328 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 799.3 | 807.3 | +1.0% | +3.0442 to +12.9558 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.22 | −13.0% | −1.6465 to +0.0861 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0375 | −47.1% | −0.0773 to +0.0106 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 106 | 110.9 | +4.6% | −0.9201 to +10.6284 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.56 | −7.3% | −0.9724 to +0.0930 | no |
| node-hours | 2.51 | 2.328 | −7.2% | −0.4033 to +0.0401 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 273.4 | −4.3% | −14.9240 to −9.8640 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 259.6 | −9.2% | −43.3672 to −9.0375 | yes: GAIN |
| response time (ms), mean | 707.8 | 377.8 | −46.6% | −426.5902 to −233.4338 | yes: GAIN |
| response time (ms), 95th percentile | 1445 | 1540 | +6.5% | −592.2598 to +781.0098 | no |
| response time (ms), 99th percentile | 1903 | 2218 | +16.6% | −724.8883 to +1356.2069 | no |
| time over the response line (% of samples) | 64.76 | 17.97 | −72.2% | −54.0300 to −39.5363 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.3 | 10.2 | −58.0% | −17.6277 to −10.5723 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 | +32.300 (native is 0) | +14.9022 to +49.6978 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.238 | 11.67 | +421.4% | +6.1828 to +12.6839 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09697 | 0.06835 | −29.5% | −0.0380 to −0.0192 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.327 | 1.515 | −34.9% | −0.9891 to −0.6356 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01619 | +0.016 (native is 0) | +0.0149 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.327 | 1.531 | −34.2% | −0.9732 to −0.6191 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294.9 | 414.2 | +40.4% | +82.1801 to +156.3626 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.056 | 2.078 | +1.1% | −0.1869 to +0.2302 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.6121 to +1.0121 | no |
| pod start wait, mean (s) | 0.1 | 0.4 | +300.0% | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 75.48 | 44.14 | −41.5% | −35.4458 to −27.2188 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1464 | 807.3 | −44.8% | −751.0056 to −561.5944 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 688.6 | 0.0375 | −100.0% | −922.2617 to −454.9526 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1254 | 0.3 | −100.0% | −1558.5093 to −948.3054 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 964.4 | 110.9 | −88.5% | −985.7006 to −721.2994 | yes: GAIN |
| queue: jobs unfinished at the window's end | 15.7 | 0 | −100.0% | −20.6334 to −10.7666 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.975 | −0.4% | −0.0803 to +0.0311 | no |
| node-hours | 2.512 | 2.512 | +0.0% | −0.0225 to +0.0238 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 287.5 | +5.2% | +11.6601 to +16.8191 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 286.8 | +4.9% | +10.1631 to +16.7619 | yes: power given |
| response time (ms), mean | 401 | 699.9 | +74.5% | +221.2962 to +376.5284 | yes: LOSS |
| response time (ms), 95th percentile | 1447 | 1431 | −1.1% | −628.2620 to +595.8720 | no |
| response time (ms), 99th percentile | 2098 | 1939 | −7.6% | −1087.3205 to +769.7745 | no |
| time over the response line (% of samples) | 17.99 | 63.31 | +251.9% | +38.3708 to +52.2657 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 24.3 | +150.5% | +10.8270 to +18.3730 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 | +18.900 (native is 0) | +13.9162 to +23.8838 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.07 | 2.298 | −79.2% | −10.6983 to −6.8550 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06331 | 0.09833 | +55.3% | +0.0276 to +0.0425 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.519 | 2.352 | +54.8% | +0.6515 to +1.0134 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00944 | +0.009 (native is 0) | +0.0086 to +0.0103 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.519 | 2.361 | +55.4% | +0.6615 to +1.0222 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 291.2 | −33.5% | −189.1566 to −104.3644 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.965 | 2.836 | +44.3% | +0.6780 to +1.0637 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.5231 to +1.4769 | yes: power given |
| pod start wait, total (s) | 0 | 3.2 | +3.200 (native is 0) | +1.2985 to +5.1015 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.5 | +2.500 (native is 0) | +1.3319 to +3.6681 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.1 | 75.73 | +75.7% | +28.6116 to +36.6559 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 799.3 | 1470 | +83.9% | +577.7931 to +763.8069 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.111 | −14.8% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 642.8 | +907370.1% | +432.8059 to +852.6351 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1240 | +247804.5% | +952.7799 to +1525.2650 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 106 | 959.4 | +804.8% | +724.7033 to +981.9883 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.8 | +14.800 (native is 0) | +10.1179 to +19.4821 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*