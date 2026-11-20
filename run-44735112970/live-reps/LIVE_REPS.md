# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.005 | 5.991 |
| node-hours | 2.513 | 2.519 | 2.1 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 287.7 | 272.7 | 286.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 287.7 | 241.4 | 286.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 318.5 | 655.7 | 300.7 | 650.2 |
| response time (ms), 95th percentile | 1084 | 1360 | 1163 | 1338 |
| response time (ms), 99th percentile | 1526 | 1832 | 1585 | 1808 |
| time over the response line (% of samples) | 12.14 | 57.3 | 13.52 | 57.57 |
| failed requests (%) | 0 | 0 | 0 | 0.02685 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 24.5 | 8.9 | 24.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 138.8 | 44.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 2.173 | 11.58 | 2.515 |
| utilisation (used / allocatable) | 0.05967 | 0.09956 | 0.0736 | 0.09866 |
| CPU used (cores), mean | 1.432 | 2.39 | 1.433 | 2.365 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07063 | 0.04229 |
| CPU used with Omni's own (cores), mean | 1.432 | 2.39 | 1.504 | 2.407 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 287.7 | 404.5 | 289.8 |
| HPA replicas, mean | 1.942 | 2.083 | 2.273 | 2.511 |
| pods started | 0 | 0.2 | 1.3 | 1.5 |
| pod start wait, total (s) | 0 | 0.4 | 2.5 | 4 |
| pod start wait, mean (s) | 0 | 0.4 | 1.15 | 2.25 |
| host CPU busy, the real machine under kind (%) | 41.14 | 76.04 | 44.04 | 77.29 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 777.7 | 1479 | 783.6 | 1481 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.429 | 5.5 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 559.7 | 0.1417 | 626.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1179 | 0.9 | 1228 |
| queue: job turnaround, submitted to done, mean (s) | 82.06 | 932.6 | 88.36 | 966.6 |
| queue: jobs unfinished at the window's end | 0 | 13 | 0 | 14.2 |
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
| worker nodes in service, mean | 6 | 5.991 | −0.2% | −0.0296 to +0.0114 | no |
| node-hours | 2.519 | 2.51 | −0.4% | −0.0204 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 287.7 | 286.7 | −0.4% | −1.8993 to −0.1608 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.7 | 286.4 | −0.5% | −2.2898 to −0.3412 | yes: GAIN |
| response time (ms), mean | 655.7 | 650.2 | −0.8% | −57.0867 to +46.0482 | no |
| response time (ms), 95th percentile | 1360 | 1338 | −1.7% | −154.4285 to +108.6215 | no |
| response time (ms), 99th percentile | 1832 | 1808 | −1.3% | −194.5240 to +146.5548 | no |
| time over the response line (% of samples) | 57.3 | 57.57 | +0.5% | −4.1636 to +4.7062 | no |
| failed requests (%) | 0 | 0.02685 | +0.027 (native is 0) | −0.0339 to +0.0876 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.5 | 24.6 | +0.4% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 | +44.400 (native is 0) | +38.0270 to +50.7730 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.173 | 2.515 | +15.7% | −0.0893 to +0.7726 | no |
| utilisation (used / allocatable) | 0.09956 | 0.09866 | −0.9% | −0.0023 to +0.0004 | no |
| CPU used (cores), mean | 2.39 | 2.365 | −1.0% | −0.0516 to +0.0017 | no |
| Omni's own CPU (cores), mean | 0 | 0.04229 | +0.042 (native is 0) | +0.0376 to +0.0470 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.39 | 2.407 | +0.7% | −0.0067 to +0.0414 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.7 | 289.8 | +0.7% | −1.8412 to +5.9786 | no |
| HPA replicas, mean | 2.083 | 2.511 | +20.6% | +0.2555 to +0.6011 | yes: power given |
| pods started | 0.2 | 1.5 | +650.0% | +0.4047 to +2.1953 | yes: power given |
| pod start wait, total (s) | 0.4 | 4 | +900.0% | +1.3837 to +5.8163 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 2.25 | +462.5% | +0.6336 to +3.0664 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 76.04 | 77.29 | +1.6% | +0.7100 to +1.7866 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1479 | 1481 | +0.1% | −9.4247 to +11.8247 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 | −8.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 559.7 | 626.1 | +11.9% | −2.9159 to +135.6778 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1179 | 1228 | +4.1% | −6.6350 to +103.3698 | no |
| queue: job turnaround, submitted to done, mean (s) | 932.6 | 966.6 | +3.6% | +13.7843 to +54.1907 | yes: LOSS |
| queue: jobs unfinished at the window's end | 13 | 14.2 | +9.2% | −0.3379 to +2.7379 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.519 | +0.3% | −0.0021 to +0.0155 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 287.7 | +5.7% | +12.0000 to +19.2881 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 287.7 | +5.7% | +12.0000 to +19.2881 | yes: power given |
| response time (ms), mean | 318.5 | 655.7 | +105.8% | +237.7890 to +436.5175 | yes: LOSS |
| response time (ms), 95th percentile | 1084 | 1360 | +25.5% | −333.6588 to +887.1028 | no |
| response time (ms), 99th percentile | 1526 | 1832 | +20.0% | −611.4677 to +1222.3349 | no |
| time over the response line (% of samples) | 12.14 | 57.3 | +371.8% | +35.9467 to +54.3645 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 24.5 | +195.2% | +12.3583 to +20.0417 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 2.173 | −81.6% | −17.5261 to −1.7305 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05967 | 0.09956 | +66.9% | +0.0308 to +0.0490 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.432 | 2.39 | +66.9% | +0.7391 to +1.1757 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.432 | 2.39 | +66.9% | +0.7391 to +1.1757 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 287.7 | −38.0% | −227.0930 to −125.4349 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.083 | +7.3% | −0.0540 to +0.3373 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 41.14 | 76.04 | +84.9% | +30.2534 to +39.5581 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.7 | 1479 | +90.2% | +617.0153 to +786.3847 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 559.7 | +335711.7% | +343.1625 to +775.8765 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1179 | +147320.4% | +909.3557 to +1447.7705 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.06 | 932.6 | +1036.5% | +731.8113 to +969.3470 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13 | +13.000 (native is 0) | +8.2313 to +17.7687 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.005 | −16.6% | −1.8470 to −0.1429 | yes: GAIN |
| node-hours | 2.513 | 2.1 | −16.4% | −0.7687 to −0.0559 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.7 | +0.2% | +0.0447 to +1.1610 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 241.4 | −11.3% | −57.6113 to −3.7997 | yes: GAIN |
| response time (ms), mean | 318.5 | 300.7 | −5.6% | −41.4761 to +5.8599 | no |
| response time (ms), 95th percentile | 1084 | 1163 | +7.3% | −37.0661 to +195.0301 | no |
| response time (ms), 99th percentile | 1526 | 1585 | +3.8% | −130.4615 to +247.2451 | no |
| time over the response line (% of samples) | 12.14 | 13.52 | +11.3% | −1.9921 to +4.7447 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.9 | +7.2% | −0.4228 to +1.6228 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.8 | +138.800 (native is 0) | +49.6201 to +227.9799 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 11.58 | −1.9% | −1.7048 to +1.2648 | no |
| utilisation (used / allocatable) | 0.05967 | 0.0736 | +23.3% | +0.0017 to +0.0261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.432 | 1.433 | +0.1% | −0.0272 to +0.0292 | no |
| Omni's own CPU (cores), mean | 0 | 0.07063 | +0.071 (native is 0) | +0.0661 to +0.0751 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.504 | +5.0% | +0.0404 to +0.1029 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 404.5 | −12.8% | −108.7198 to −10.3538 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.273 | +17.1% | +0.1747 to +0.4889 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.3433 to +2.2567 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | +0.5851 to +4.4149 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.15 | +1.150 (native is 0) | +0.4141 to +1.8859 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.14 | 44.04 | +7.1% | +2.4056 to +3.4077 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.7 | 783.6 | +0.8% | −0.6857 to +12.4857 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.429 | −26.2% | −2.8007 to −0.3407 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 0.1417 | −15.0% | −0.1205 to +0.0705 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | −0.5263 to +0.7263 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.06 | 88.36 | +7.7% | −0.2501 to +12.8501 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.005 | −16.6% | −1.8470 to −0.1429 | yes: GAIN |
| node-hours | 2.519 | 2.1 | −16.6% | −0.7787 to −0.0591 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 287.7 | 272.7 | −5.2% | −18.7287 to −11.3538 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.7 | 241.4 | −16.1% | −75.3845 to −17.3146 | yes: GAIN |
| response time (ms), mean | 655.7 | 300.7 | −54.1% | −440.3183 to −269.6043 | yes: GAIN |
| response time (ms), 95th percentile | 1360 | 1163 | −14.5% | −791.1843 to +395.7043 | no |
| response time (ms), 99th percentile | 1832 | 1585 | −13.5% | −1083.1477 to +589.0641 | no |
| time over the response line (% of samples) | 57.3 | 13.52 | −76.4% | −51.4939 to −36.0648 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.5 | 8.9 | −63.7% | −19.3428 to −11.8572 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.8 | +138.800 (native is 0) | +49.6201 to +227.9799 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.173 | 11.58 | +432.9% | +1.8401 to +16.9765 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09956 | 0.0736 | −26.1% | −0.0382 to −0.0137 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.39 | 1.433 | −40.0% | −1.1905 to −0.7222 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07063 | +0.071 (native is 0) | +0.0661 to +0.0751 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.39 | 1.504 | −37.1% | −1.1233 to −0.6482 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.7 | 404.5 | +40.6% | +74.4491 to +159.0051 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.083 | 2.273 | +9.1% | −0.0458 to +0.4261 | no |
| pods started | 0.2 | 1.3 | +550.0% | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.5 | +525.0% | −0.1227 to +4.3227 | no |
| pod start wait, mean (s) | 0.4 | 1.15 | +187.5% | −0.4211 to +1.9211 | no |
| host CPU busy, the real machine under kind (%) | 76.04 | 44.04 | −42.1% | −36.7907 to −27.2074 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1479 | 783.6 | −47.0% | −781.1492 to −610.4508 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 559.7 | 0.1417 | −100.0% | −775.9057 to −343.1832 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1179 | 0.9 | −99.9% | −1447.5998 to −909.3265 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 932.6 | 88.36 | −90.5% | −959.7600 to −728.7983 | yes: GAIN |
| queue: jobs unfinished at the window's end | 13 | 0 | −100.0% | −17.7687 to −8.2313 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.991 | −0.2% | −0.0296 to +0.0114 | no |
| node-hours | 2.513 | 2.51 | −0.1% | −0.0122 to +0.0069 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 286.7 | +5.4% | +10.9137 to +18.3143 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 286.4 | +5.3% | +10.5253 to +18.1319 | yes: power given |
| response time (ms), mean | 318.5 | 650.2 | +104.1% | +214.9262 to +448.3417 | yes: LOSS |
| response time (ms), 95th percentile | 1084 | 1338 | +23.4% | −402.1350 to +909.7720 | no |
| response time (ms), 99th percentile | 1526 | 1808 | +18.4% | −704.3218 to +1267.2198 | no |
| time over the response line (% of samples) | 12.14 | 57.57 | +374.1% | +37.1967 to +53.6572 | yes: LOSS |
| failed requests (%) | 0 | 0.02685 | +0.027 (native is 0) | −0.0339 to +0.0876 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 24.6 | +196.4% | +12.3959 to +20.2041 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 | +44.400 (native is 0) | +38.0270 to +50.7730 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 2.515 | −78.7% | −17.3055 to −1.2679 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05967 | 0.09866 | +65.3% | +0.0297 to +0.0483 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.432 | 2.365 | +65.1% | +0.7090 to +1.1560 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04229 | +0.042 (native is 0) | +0.0376 to +0.0470 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 2.407 | +68.1% | +0.7552 to +1.1944 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 289.8 | −37.5% | −226.3107 to −122.0798 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.511 | +29.4% | +0.3125 to +0.8274 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.5921 to +2.4079 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +1.7633 to +6.2367 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.25 | +2.250 (native is 0) | +1.2490 to +3.2510 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.14 | 77.29 | +87.9% | +31.6972 to +40.6108 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.7 | 1481 | +90.4% | +624.2954 to +781.5046 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 | −8.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 626.1 | +375540.3% | +384.3432 to +867.4577 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1228 | +153366.3% | +946.2998 to +1507.5613 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.06 | 966.6 | +1077.9% | +776.6368 to +992.4965 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.2 | +14.200 (native is 0) | +9.2008 to +19.1992 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*