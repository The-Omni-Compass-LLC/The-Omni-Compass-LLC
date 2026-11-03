# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.575 | 4.686 |
| node-hours | 2.514 | 2.518 | 1.915 | 1.964 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 273.2 | 272.2 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 273.2 | 227.4 | 231.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 340.7 | 384.5 | 335.7 | 375.6 |
| response time (ms), 95th percentile | 1242 | 1645 | 1393 | 1753 |
| response time (ms), 99th percentile | 1761 | 2200 | 1982 | 2344 |
| time over the response line (% of samples) | 13.99 | 11.97 | 13.92 | 12.23 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.3 | 7.3 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 180.4 | 113.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.882 | 24.57 | 11.13 | 32.76 |
| utilisation (used / allocatable) | 0.06007 | 0.06092 | 0.07955 | 0.07798 |
| CPU used (cores), mean | 1.442 | 1.462 | 1.432 | 1.452 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07136 | 0.0785 |
| CPU used with Omni's own (cores), mean | 1.442 | 1.462 | 1.503 | 1.531 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.5 | 458.8 | 381.7 | 383.6 |
| HPA replicas, mean | 2.005 | 2.024 | 2.501 | 2.259 |
| pods started | 0 | 0 | 1.7 | 0.7 |
| pod start wait, total (s) | 0 | 0 | 4.1 | 1.4 |
| pod start wait, mean (s) | 0 | 0 | 1.808 | 0.6333 |
| host CPU busy, the real machine under kind (%) | 40.78 | 43.78 | 44.38 | 47.51 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 788.9 | 827.4 | 799.2 | 838.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.727 | 3.679 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1.129 | 0.1583 | 1.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 3.3 | 0.4 | 3.6 |
| queue: job turnaround, submitted to done, mean (s) | 95 | 125.9 | 103.9 | 137.1 |
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
| worker nodes in service, mean | 6 | 4.686 | −21.9% | −2.0942 to −0.5338 | yes: GAIN |
| node-hours | 2.518 | 1.964 | −22.0% | −0.8782 to −0.2301 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 | −0.1% | −0.8495 to +0.3836 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 231.7 | −15.2% | −65.7929 to −17.2980 | yes: GAIN |
| response time (ms), mean | 384.5 | 375.6 | −2.3% | −24.9570 to +7.1238 | no |
| response time (ms), 95th percentile | 1645 | 1753 | +6.5% | +12.3179 to +202.6231 | yes: LOSS |
| response time (ms), 99th percentile | 2200 | 2344 | +6.5% | +19.7284 to +267.9064 | yes: LOSS |
| time over the response line (% of samples) | 11.97 | 12.23 | +2.2% | −0.6135 to +1.1286 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.8 | +6.8% | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.5 | +113.500 (native is 0) | +56.1075 to +170.8925 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.57 | 32.76 | +33.3% | +1.5633 to +14.8033 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06092 | 0.07798 | +28.0% | +0.0069 to +0.0272 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.462 | 1.452 | −0.7% | −0.0485 to +0.0292 | no |
| Omni's own CPU (cores), mean | 0 | 0.0785 | +0.078 (native is 0) | +0.0710 to +0.0860 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.462 | 1.531 | +4.7% | +0.0259 to +0.1118 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.8 | 383.6 | −16.4% | −121.2451 to −29.0825 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.024 | 2.259 | +11.6% | +0.0143 to +0.4566 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | −0.2242 to +3.0242 | no |
| pod start wait, mean (s) | 0 | 0.6333 | +0.633 (native is 0) | −0.1307 to +1.3973 | no |
| host CPU busy, the real machine under kind (%) | 43.78 | 47.51 | +8.5% | +3.1099 to +4.3477 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 827.4 | 838.4 | +1.3% | +1.4924 to +20.5076 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.679 | −38.7% | −3.5934 to −1.0484 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.129 | 1.2 | +6.3% | −0.2154 to +0.3571 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 3.6 | +9.1% | −1.8072 to +2.4072 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.9 | 137.1 | +8.9% | +3.0054 to +19.3696 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.518 | +0.2% | −0.0004 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 273.2 | +0.3% | +0.3463 to +1.5118 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 273.2 | +0.3% | +0.3463 to +1.5118 | yes: power given |
| response time (ms), mean | 340.7 | 384.5 | +12.9% | −1.8103 to +89.5178 | no |
| response time (ms), 95th percentile | 1242 | 1645 | +32.5% | +12.4146 to +793.8574 | yes: LOSS |
| response time (ms), 99th percentile | 1761 | 2200 | +25.0% | −10.8696 to +889.7964 | no |
| time over the response line (% of samples) | 13.99 | 11.97 | −14.4% | −3.9394 to −0.1027 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.3 | +7.4% | −0.1079 to +1.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.882 | 24.57 | +148.7% | +6.0633 to +23.3200 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06007 | 0.06092 | +1.4% | −0.0005 to +0.0022 | no |
| CPU used (cores), mean | 1.442 | 1.462 | +1.4% | −0.0128 to +0.0536 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.442 | 1.462 | +1.4% | −0.0128 to +0.0536 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.5 | 458.8 | −1.0% | −17.0059 to +7.6036 | no |
| HPA replicas, mean | 2.005 | 2.024 | +0.9% | −0.1476 to +0.1856 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.78 | 43.78 | +7.4% | +2.0558 to +3.9451 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.9 | 827.4 | +4.9% | +8.5324 to +68.4676 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1.129 | +1190.5% | +0.6299 to +1.4535 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 3.3 | +1000.0% | +0.7888 to +5.2112 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 95 | 125.9 | +32.5% | +6.1350 to +55.6234 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.575 | −23.8% | −2.2875 to −0.5629 | yes: GAIN |
| node-hours | 2.514 | 1.915 | −23.8% | −0.9569 to −0.2406 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.2 | −0.0% | −0.4003 to +0.2281 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 227.4 | −16.5% | −72.1616 to −17.6231 | yes: GAIN |
| response time (ms), mean | 340.7 | 335.7 | −1.5% | −15.4425 to +5.4954 | no |
| response time (ms), 95th percentile | 1242 | 1393 | +12.1% | +15.2189 to +286.4841 | yes: LOSS |
| response time (ms), 99th percentile | 1761 | 1982 | +12.6% | −7.5081 to +450.4443 | no |
| time over the response line (% of samples) | 13.99 | 13.92 | −0.6% | −0.7460 to +0.5895 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.3 | +7.4% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 180.4 | +180.400 (native is 0) | +90.3854 to +270.4146 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.882 | 11.13 | +12.6% | +0.1348 to +2.3586 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06007 | 0.07955 | +32.4% | +0.0081 to +0.0308 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.442 | 1.432 | −0.7% | −0.0531 to +0.0335 | no |
| Omni's own CPU (cores), mean | 0 | 0.07136 | +0.071 (native is 0) | +0.0637 to +0.0790 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.442 | 1.503 | +4.3% | +0.0139 to +0.1093 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.5 | 381.7 | −17.7% | −127.3822 to −36.3000 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.501 | +24.8% | +0.1818 to +0.8113 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.6856 to +2.7144 | yes: power given |
| pod start wait, total (s) | 0 | 4.1 | +4.100 (native is 0) | +1.8267 to +6.3733 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.808 | +1.808 (native is 0) | +0.8228 to +2.7939 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.78 | 44.38 | +8.9% | +3.0784 to +4.1390 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.9 | 799.2 | +1.3% | +1.1083 to +19.4917 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.727 | −37.9% | −3.4960 to −1.0498 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.1583 | +81.0% | −0.0640 to +0.2056 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 95 | 103.9 | +9.4% | +1.5529 to +16.2804 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.575 | −23.8% | −2.2875 to −0.5629 | yes: GAIN |
| node-hours | 2.518 | 1.915 | −24.0% | −0.9605 to −0.2457 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.2 | −0.4% | −1.4304 to −0.5998 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 227.4 | −16.8% | −72.7239 to −18.9188 | yes: GAIN |
| response time (ms), mean | 384.5 | 335.7 | −12.7% | −89.2037 to −8.4510 | yes: GAIN |
| response time (ms), 95th percentile | 1645 | 1393 | −15.3% | −559.3569 to +54.7879 | no |
| response time (ms), 99th percentile | 2200 | 1982 | −9.9% | −496.4183 to +60.4277 | no |
| time over the response line (% of samples) | 11.97 | 13.92 | +16.2% | +0.6243 to +3.2612 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.3 | ±0.0% | −0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 180.4 | +180.400 (native is 0) | +90.3854 to +270.4146 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.57 | 11.13 | −54.7% | −21.6045 to −5.2855 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06092 | 0.07955 | +30.6% | +0.0067 to +0.0306 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.462 | 1.432 | −2.1% | −0.0614 to +0.0010 | no |
| Omni's own CPU (cores), mean | 0 | 0.07136 | +0.071 (native is 0) | +0.0637 to +0.0790 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.462 | 1.503 | +2.8% | +0.0056 to +0.0767 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.8 | 381.7 | −16.8% | −125.9174 to −28.3625 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.024 | 2.501 | +23.6% | +0.1552 to +0.7999 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.6856 to +2.7144 | yes: power given |
| pod start wait, total (s) | 0 | 4.1 | +4.100 (native is 0) | +1.8267 to +6.3733 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.808 | +1.808 (native is 0) | +0.8228 to +2.7939 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.78 | 44.38 | +1.4% | −0.2103 to +1.4268 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 827.4 | 799.2 | −3.4% | −49.3464 to −7.0536 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.727 | −37.9% | −3.4960 to −1.0498 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.129 | 0.1583 | −86.0% | −1.2741 to −0.6675 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 0.4 | −87.9% | −5.0970 to −0.7030 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 125.9 | 103.9 | −17.4% | −39.4148 to −4.5102 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.686 | −21.9% | −2.0942 to −0.5338 | yes: GAIN |
| node-hours | 2.514 | 1.964 | −21.9% | −0.8759 to −0.2238 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 273 | +0.3% | +0.0457 to +1.3466 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 231.7 | −14.9% | −65.2939 to −15.9388 | yes: GAIN |
| response time (ms), mean | 340.7 | 375.6 | +10.3% | −17.6210 to +87.4953 | no |
| response time (ms), 95th percentile | 1242 | 1753 | +41.1% | +33.0628 to +988.1502 | yes: LOSS |
| response time (ms), 99th percentile | 1761 | 2344 | +33.1% | +62.2305 to +1104.3311 | yes: LOSS |
| time over the response line (% of samples) | 13.99 | 12.23 | −12.6% | −4.2359 to +0.7089 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.8 | +14.7% | +0.3256 to +1.6744 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.5 | +113.500 (native is 0) | +56.1075 to +170.8925 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.882 | 32.76 | +231.5% | +7.8684 to +37.8816 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06007 | 0.07798 | +29.8% | +0.0082 to +0.0276 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.442 | 1.452 | +0.7% | −0.0218 to +0.0434 | no |
| Omni's own CPU (cores), mean | 0 | 0.0785 | +0.078 (native is 0) | +0.0710 to +0.0860 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.442 | 1.531 | +6.2% | +0.0505 to +0.1281 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.5 | 383.6 | −17.2% | −123.5129 to −36.2171 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.259 | +12.7% | −0.0249 to +0.5338 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | −0.2242 to +3.0242 | no |
| pod start wait, mean (s) | 0 | 0.6333 | +0.633 (native is 0) | −0.1307 to +1.3973 | no |
| host CPU busy, the real machine under kind (%) | 40.78 | 47.51 | +16.5% | +5.5287 to +7.9298 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.9 | 838.4 | +6.3% | +10.5681 to +88.4319 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.679 | −38.7% | −3.5934 to −1.0484 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1.2 | +1271.4% | +0.6358 to +1.5892 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 3.6 | +1100.0% | +0.9871 to +5.6129 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 95 | 137.1 | +44.3% | +9.7673 to +74.3660 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*