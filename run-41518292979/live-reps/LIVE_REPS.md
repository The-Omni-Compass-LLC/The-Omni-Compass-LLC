# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.772 | 4.525 |
| node-hours | 2.515 | 2.515 | 2 | 1.895 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.6 | 272.2 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.6 | 233.7 | 226 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 357.9 | 371.5 | 350.7 | 368.3 |
| response time (ms), 95th percentile | 1309 | 1355 | 1444 | 1495 |
| response time (ms), 99th percentile | 1812 | 1906 | 2015 | 2056 |
| time over the response line (% of samples) | 15.37 | 16.18 | 16.04 | 16.43 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8 | 8 | 8.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 136.8 | 134.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 77.78 | 31.25 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.75 | 11.33 | 12.94 | 14.44 |
| utilisation (used / allocatable) | 0.06044 | 0.06012 | 0.07662 | 0.08012 |
| CPU used (cores), mean | 1.451 | 1.443 | 1.429 | 1.429 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07264 | 0.07611 |
| CPU used with Omni's own (cores), mean | 1.451 | 1.443 | 1.502 | 1.505 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.5 | 468.2 | 396 | 384.1 |
| HPA replicas, mean | 1.968 | 2.09 | 2.298 | 2.366 |
| pods started | 0.2 | 0.3 | 0.8 | 1.4 |
| pod start wait, total (s) | 0.4 | 0.7 | 1.7 | 3.8 |
| pod start wait, mean (s) | 0.2 | 0.2333 | 0.85 | 1.667 |
| host CPU busy, the real machine under kind (%) | 41.14 | 41.72 | 44.34 | 45.32 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 793.4 | 799.8 | 802.8 | 810.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.18 | 3.611 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.7083 | 0.2125 | 1.371 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 5.4 | 1.1 | 7 |
| queue: job turnaround, submitted to done, mean (s) | 98.81 | 105.7 | 107.9 | 115.3 |
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
| worker nodes in service, mean | 6 | 4.525 | −24.6% | −2.3302 to −0.6203 | yes: GAIN |
| node-hours | 2.515 | 1.895 | −24.7% | −0.9803 to −0.2599 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.3 | −0.1% | −1.6676 to +1.0377 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 226 | −17.1% | −73.9256 to −19.3168 | yes: GAIN |
| response time (ms), mean | 371.5 | 368.3 | −0.9% | −18.8970 to +12.5340 | no |
| response time (ms), 95th percentile | 1355 | 1495 | +10.3% | +3.3939 to +275.8891 | yes: LOSS |
| response time (ms), 99th percentile | 1906 | 2056 | +7.9% | −39.3419 to +338.7697 | no |
| time over the response line (% of samples) | 16.18 | 16.43 | +1.6% | −0.3970 to +0.8989 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.5 | +6.2% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.1 | +134.100 (native is 0) | +60.4651 to +207.7349 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.33 | 14.44 | +27.5% | −0.7753 to +7.0019 | no |
| utilisation (used / allocatable) | 0.06012 | 0.08012 | +33.3% | +0.0075 to +0.0325 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.429 | −1.0% | −0.0516 to +0.0241 | no |
| Omni's own CPU (cores), mean | 0 | 0.07611 | +0.076 (native is 0) | +0.0669 to +0.0854 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.505 | +4.3% | +0.0198 to +0.1048 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.2 | 384.1 | −18.0% | −135.8917 to −32.3509 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.09 | 2.366 | +13.2% | −0.0956 to +0.6480 | no |
| pods started | 0.3 | 1.4 | +366.7% | −0.3484 to +2.5484 | no |
| pod start wait, total (s) | 0.7 | 3.8 | +442.9% | −0.6466 to +6.8466 | no |
| pod start wait, mean (s) | 0.2333 | 1.667 | +614.3% | +0.0439 to +2.8227 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.72 | 45.32 | +8.6% | +3.2094 to +3.9841 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 799.8 | 810.7 | +1.4% | +2.6579 to +19.1421 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.611 | −39.8% | −3.5117 to −1.2659 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7083 | 1.371 | +93.5% | −0.2441 to +1.5691 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 5.4 | 7 | +29.6% | −0.2835 to +3.4835 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.7 | 115.3 | +9.1% | +1.7361 to +17.5389 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.515 | 0.0% | raw −0.0048 to +0.0048 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.6 | −0.0% | −0.4982 to +0.3986 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.6 | −0.0% | −0.4982 to +0.3986 | no |
| response time (ms), mean | 357.9 | 371.5 | +3.8% | −5.6365 to +32.7824 | no |
| response time (ms), 95th percentile | 1309 | 1355 | +3.5% | −73.4980 to +166.4260 | no |
| response time (ms), 99th percentile | 1812 | 1906 | +5.2% | −87.0115 to +275.3851 | no |
| time over the response line (% of samples) | 15.37 | 16.18 | +5.2% | −0.3368 to +1.9481 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8 | +2.6% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.75 | 11.33 | −3.6% | −1.9835 to +1.1435 | no |
| utilisation (used / allocatable) | 0.06044 | 0.06012 | −0.5% | −0.0010 to +0.0004 | no |
| CPU used (cores), mean | 1.451 | 1.443 | −0.5% | −0.0239 to +0.0086 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.451 | 1.443 | −0.5% | −0.0239 to +0.0086 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.5 | 468.2 | +0.8% | −1.9859 to +9.2715 | no |
| HPA replicas, mean | 1.968 | 2.09 | +6.2% | −0.0401 to +0.2840 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.4 | 0.7 | +75.0% | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0.2 | 0.2333 | +16.7% | −0.0421 to +0.1087 | no |
| host CPU busy, the real machine under kind (%) | 41.14 | 41.72 | +1.4% | +0.1940 to +0.9824 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.4 | 799.8 | +0.8% | +0.2633 to +12.5367 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.7083 | +286.4% | −0.3333 to +1.3833 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 5.4 | +350.0% | −4.3025 to +12.7025 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.81 | 105.7 | +7.0% | −0.0443 to +13.7943 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.772 | −20.5% | −2.1833 to −0.2725 | yes: GAIN |
| node-hours | 2.515 | 2 | −20.5% | −0.9196 to −0.1112 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.2 | −0.2% | −1.6673 to +0.7421 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 233.7 | −14.3% | −69.6065 to −8.2813 | yes: GAIN |
| response time (ms), mean | 357.9 | 350.7 | −2.0% | −22.6529 to +8.3199 | no |
| response time (ms), 95th percentile | 1309 | 1444 | +10.3% | +33.6434 to +237.0116 | yes: LOSS |
| response time (ms), 99th percentile | 1812 | 2015 | +11.2% | +6.9937 to +398.7941 | yes: LOSS |
| time over the response line (% of samples) | 15.37 | 16.04 | +4.3% | −1.0268 to +2.3564 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8 | +2.6% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.8 | +136.800 (native is 0) | +65.7351 to +207.8649 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.75 | 12.94 | +10.2% | −2.4325 to +4.8259 | no |
| utilisation (used / allocatable) | 0.06044 | 0.07662 | +26.8% | +0.0028 to +0.0296 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.451 | 1.429 | −1.5% | −0.0628 to +0.0202 | no |
| Omni's own CPU (cores), mean | 0 | 0.07264 | +0.073 (native is 0) | +0.0632 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.451 | 1.502 | +3.5% | +0.0049 to +0.0977 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.5 | 396 | −14.8% | −122.6654 to −14.4982 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.968 | 2.298 | +16.8% | +0.0978 to +0.5625 | yes: power given |
| pods started | 0.2 | 0.8 | +300.0% | −0.4228 to +1.6228 | no |
| pod start wait, total (s) | 0.4 | 1.7 | +325.0% | −0.8340 to +3.4340 | no |
| pod start wait, mean (s) | 0.2 | 0.85 | +325.0% | −0.3623 to +1.6623 | no |
| host CPU busy, the real machine under kind (%) | 41.14 | 44.34 | +7.8% | +2.6999 to +3.6978 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.4 | 802.8 | +1.2% | +2.4714 to +16.3286 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.18 | −30.3% | −3.2161 to −0.4230 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.2125 | +15.9% | −0.0175 to +0.0759 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.1 | −8.3% | −0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.81 | 107.9 | +9.2% | +1.9538 to +16.1712 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.772 | −20.5% | −2.1833 to −0.2725 | yes: GAIN |
| node-hours | 2.515 | 2 | −20.5% | −0.9193 to −0.1115 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.2 | −0.2% | −1.6427 to +0.8170 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 233.7 | −14.3% | −69.5572 to −8.2310 | yes: GAIN |
| response time (ms), mean | 371.5 | 350.7 | −5.6% | −28.9392 to −12.5397 | yes: GAIN |
| response time (ms), 95th percentile | 1355 | 1444 | +6.6% | +16.3822 to +161.3448 | yes: LOSS |
| response time (ms), 99th percentile | 1906 | 2015 | +5.7% | +23.7687 to +193.6455 | yes: LOSS |
| time over the response line (% of samples) | 16.18 | 16.04 | −0.9% | −0.8656 to +0.5838 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.8 | +136.800 (native is 0) | +65.7351 to +207.8649 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.33 | 12.94 | +14.3% | −2.7605 to +5.9938 | no |
| utilisation (used / allocatable) | 0.06012 | 0.07662 | +27.4% | +0.0029 to +0.0301 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.429 | −1.0% | −0.0498 to +0.0224 | no |
| Omni's own CPU (cores), mean | 0 | 0.07264 | +0.073 (native is 0) | +0.0632 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.502 | +4.1% | +0.0185 to +0.0994 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.2 | 396 | −15.4% | −129.2192 to −15.2300 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.09 | 2.298 | +10.0% | −0.0943 to +0.5108 | no |
| pods started | 0.3 | 0.8 | +166.7% | −0.6802 to +1.6802 | no |
| pod start wait, total (s) | 0.7 | 1.7 | +142.9% | −1.6119 to +3.6119 | no |
| pod start wait, mean (s) | 0.2333 | 0.85 | +264.3% | −0.4468 to +1.6801 | no |
| host CPU busy, the real machine under kind (%) | 41.72 | 44.34 | +6.3% | +2.2280 to +2.9933 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 799.8 | 802.8 | +0.4% | +0.5684 to +5.4316 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.18 | −30.3% | −3.2161 to −0.4230 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7083 | 0.2125 | −70.0% | −1.3599 to +0.3683 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 5.4 | 1.1 | −79.6% | −13.2853 to +4.6853 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.7 | 107.9 | +2.1% | −1.1922 to +5.5672 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.525 | −24.6% | −2.3302 to −0.6203 | yes: GAIN |
| node-hours | 2.515 | 1.895 | −24.7% | −0.9802 to −0.2600 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.3 | −0.1% | −1.5116 to +0.7821 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 226 | −17.1% | −73.9443 to −19.3977 | yes: GAIN |
| response time (ms), mean | 357.9 | 368.3 | +2.9% | −9.7784 to +30.5612 | no |
| response time (ms), 95th percentile | 1309 | 1495 | +14.2% | +70.6969 to +301.5141 | yes: LOSS |
| response time (ms), 99th percentile | 1812 | 2056 | +13.5% | +87.0713 to +400.7301 | yes: LOSS |
| time over the response line (% of samples) | 15.37 | 16.43 | +6.9% | −0.6064 to +2.7196 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.5 | +9.0% | +0.0214 to +1.3786 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.1 | +134.100 (native is 0) | +60.4651 to +207.7349 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.75 | 14.44 | +22.9% | −1.2550 to +6.6417 | no |
| utilisation (used / allocatable) | 0.06044 | 0.08012 | +32.6% | +0.0073 to +0.0320 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.451 | 1.429 | −1.5% | −0.0655 to +0.0227 | no |
| Omni's own CPU (cores), mean | 0 | 0.07611 | +0.076 (native is 0) | +0.0669 to +0.0854 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.451 | 1.505 | +3.8% | +0.0052 to +0.1042 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.5 | 384.1 | −17.3% | −129.6041 to −31.3529 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.968 | 2.366 | +20.2% | +0.0917 to +0.7046 | yes: power given |
| pods started | 0.2 | 1.4 | +600.0% | −0.0972 to +2.4972 | no |
| pod start wait, total (s) | 0.4 | 3.8 | +850.0% | +0.0756 to +6.7244 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.667 | +733.3% | +0.1275 to +2.8058 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.14 | 45.32 | +10.2% | +3.7708 to +4.5992 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.4 | 810.7 | +2.2% | +4.5619 to +30.0381 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.611 | −39.8% | −3.5117 to −1.2659 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 1.371 | +647.7% | −0.4281 to +2.8031 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 7 | +483.3% | −3.9017 to +15.5017 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.81 | 115.3 | +16.7% | +4.4172 to +28.6078 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*