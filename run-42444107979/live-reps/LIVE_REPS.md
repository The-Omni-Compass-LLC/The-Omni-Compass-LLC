# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.424 | 5.98 |
| node-hours | 2.513 | 2.519 | 1.853 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 272.3 | 271.1 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 272.3 | 221.6 | 270.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 271.5 | 124 | 262.9 | 100.8 |
| response time (ms), 95th percentile | 918.5 | 213.2 | 1057 | 223.8 |
| response time (ms), 99th percentile | 1352 | 310.5 | 1497 | 331.7 |
| time over the response line (% of samples) | 10.42 | 0.1607 | 10.8 | 0.1644 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 0 | 7.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 166.6 | 95.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 5 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.285 | 985.9 | 8.535 | 1110 |
| utilisation (used / allocatable) | 0.05709 | 0.05963 | 0.07802 | 0.05774 |
| CPU used (cores), mean | 1.37 | 1.431 | 1.35 | 1.381 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07031 | 0.06697 |
| CPU used with Omni's own (cores), mean | 1.37 | 1.431 | 1.42 | 1.448 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.6 | 453.6 | 394 | 467.6 |
| HPA replicas, mean | 2.011 | 1.976 | 2.151 | 2.046 |
| pods started | 0 | 0.1 | 0.7 | 0.3 |
| pod start wait, total (s) | 0 | 0.3 | 1.5 | 0.6 |
| pod start wait, mean (s) | 0 | 0.3 | 0.6333 | 0.4 |
| host CPU busy, the real machine under kind (%) | 38.98 | 44.17 | 41.67 | 45.72 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 758.7 | 1454 | 766.8 | 1457 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.433 | 5.611 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.004167 | 155.6 | 0.05417 | 161.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 715.4 | 0.3 | 672.1 |
| queue: job turnaround, submitted to done, mean (s) | 64.19 | 768.1 | 72.18 | 797 |
| queue: jobs unfinished at the window's end | 0 | 5.9 | 0 | 9.3 |
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
| worker nodes in service, mean | 6 | 5.98 | −0.3% | −0.0566 to +0.0161 | no |
| node-hours | 2.519 | 2.508 | −0.4% | −0.0285 to +0.0062 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.3 | −0.4% | −2.2329 to +0.2175 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 270.7 | −0.6% | −3.2706 to −0.0198 | yes: GAIN |
| response time (ms), mean | 124 | 100.8 | −18.7% | −28.0801 to −18.3000 | yes: GAIN |
| response time (ms), 95th percentile | 213.2 | 223.8 | +5.0% | +0.3705 to +20.7955 | yes: LOSS |
| response time (ms), 99th percentile | 310.5 | 331.7 | +6.8% | +6.2397 to +36.0873 | yes: LOSS |
| time over the response line (% of samples) | 0.1607 | 0.1644 | +2.3% | −0.1672 to +0.1747 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.9 | +95.900 (native is 0) | +80.4092 to +111.3908 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 985.9 | 1110 | +12.6% | +5.9880 to +241.5387 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05963 | 0.05774 | −3.2% | −0.0034 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.381 | −3.5% | −0.0863 to −0.0135 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06697 | +0.067 (native is 0) | +0.0590 to +0.0750 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.448 | +1.2% | −0.0229 to +0.0571 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.6 | 467.6 | +3.1% | +3.1719 to +24.8101 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.046 | +3.5% | −0.0740 to +0.2133 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | −0.9639 to +1.5639 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.8802 to +1.0802 | no |
| host CPU busy, the real machine under kind (%) | 44.17 | 45.72 | +3.5% | +0.3443 to +2.7417 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1454 | 1457 | +0.2% | −83.6075 to +89.4075 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.559 | −7.4% | −6.0468 to +5.1644 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 155.6 | 161.3 | +3.7% | −12.3661 to +23.7911 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 715.4 | 672.1 | −6.1% | −174.1572 to +87.5572 | no |
| queue: job turnaround, submitted to done, mean (s) | 768.1 | 797 | +3.8% | −64.9505 to +122.7255 | no |
| queue: jobs unfinished at the window's end | 5.9 | 9.3 | +57.6% | −0.4624 to +7.2624 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.519 | +0.2% | −0.0015 to +0.0129 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 272.3 | +0.4% | −1.0245 to +3.2634 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 272.3 | +0.4% | −1.0245 to +3.2634 | no |
| response time (ms), mean | 271.5 | 124 | −54.3% | −276.7575 to −18.3509 | yes: GAIN |
| response time (ms), 95th percentile | 918.5 | 213.2 | −76.8% | −1338.3344 to −72.1356 | yes: GAIN |
| response time (ms), 99th percentile | 1352 | 310.5 | −77.0% | −1957.4592 to −124.9186 | yes: GAIN |
| time over the response line (% of samples) | 10.42 | 0.1607 | −98.5% | −20.4335 to −0.0917 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 0 | −100.0% | −10.7150 to −2.2850 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.285 | 985.9 | +10518.0% | +728.5965 to +1224.5968 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05709 | 0.05963 | +4.4% | −0.0038 to +0.0089 | no |
| CPU used (cores), mean | 1.37 | 1.431 | +4.4% | −0.0921 to +0.2138 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.37 | 1.431 | +4.4% | −0.0921 to +0.2138 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.6 | 453.6 | −5.6% | −71.7068 to +17.5689 | no |
| HPA replicas, mean | 2.011 | 1.976 | −1.7% | −0.1999 to +0.1306 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 38.98 | 44.17 | +13.3% | +1.7178 to +8.6727 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.7 | 1454 | +91.6% | +614.5394 to +775.6606 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.004167 | 155.6 | +3734800.0% | +105.3674 to +205.8659 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 715.4 | +715.400 (native is 0) | +559.9746 to +870.8254 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 64.19 | 768.1 | +1096.6% | +588.0266 to +819.7901 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 5.9 | +5.900 (native is 0) | −0.5989 to +12.3989 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.424 | −26.3% | −2.3280 to −0.8230 | yes: GAIN |
| node-hours | 2.513 | 1.853 | −26.3% | −0.9748 to −0.3455 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.1 | −0.1% | −1.3242 to +1.0168 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 221.6 | −18.3% | −73.6606 to −25.5426 | yes: GAIN |
| response time (ms), mean | 271.5 | 262.9 | −3.2% | −25.7848 to +8.5452 | no |
| response time (ms), 95th percentile | 918.5 | 1057 | +15.1% | +7.3947 to +269.2473 | yes: LOSS |
| response time (ms), 99th percentile | 1352 | 1497 | +10.8% | +9.0635 to +282.1193 | yes: LOSS |
| time over the response line (% of samples) | 10.42 | 10.8 | +3.7% | +0.1108 to +0.6505 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 7.1 | +9.2% | −0.0032 to +1.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 166.6 | +166.600 (native is 0) | +91.5308 to +241.6692 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.285 | 8.535 | −8.1% | −2.3855 to +0.8855 | no |
| utilisation (used / allocatable) | 0.05709 | 0.07802 | +36.7% | +0.0101 to +0.0317 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.37 | 1.35 | −1.5% | −0.0570 to +0.0168 | no |
| Omni's own CPU (cores), mean | 0 | 0.07031 | +0.070 (native is 0) | +0.0624 to +0.0782 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.37 | 1.42 | +3.7% | +0.0074 to +0.0931 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.6 | 394 | −18.0% | −126.9669 to −46.3717 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.151 | +7.0% | −0.0660 to +0.3461 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.1953 to +1.5953 | no |
| pod start wait, total (s) | 0 | 1.5 | +1.500 (native is 0) | −0.4444 to +3.4444 | no |
| pod start wait, mean (s) | 0 | 0.6333 | +0.633 (native is 0) | −0.0990 to +1.3657 | no |
| host CPU busy, the real machine under kind (%) | 38.98 | 41.67 | +6.9% | +1.7615 to +3.6228 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.7 | 766.8 | +1.1% | −0.7668 to +16.9668 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.433 | −42.8% | −3.4727 to −1.6621 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.004167 | 0.05417 | +1200.0% | +0.0060 to +0.0940 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 64.19 | 72.18 | +12.4% | −1.7258 to +17.7091 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.424 | −26.3% | −2.3280 to −0.8230 | yes: GAIN |
| node-hours | 2.519 | 1.853 | −26.4% | −0.9813 to −0.3503 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.1 | −0.5% | −4.0017 to +1.4554 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 221.6 | −18.6% | −76.4387 to −25.0034 | yes: GAIN |
| response time (ms), mean | 124 | 262.9 | +112.1% | −6.4722 to +284.3410 | no |
| response time (ms), 95th percentile | 213.2 | 1057 | +395.6% | +100.9447 to +1586.1673 | yes: LOSS |
| response time (ms), 99th percentile | 310.5 | 1497 | +382.2% | +138.5155 to +2235.0451 | yes: LOSS |
| time over the response line (% of samples) | 0.1607 | 10.8 | +6624.4% | +0.5353 to +20.7512 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 7.1 | +7.100 (native is 0) | +2.6208 to +11.5792 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 166.6 | +166.600 (native is 0) | +91.5308 to +241.6692 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 985.9 | 8.535 | −99.1% | −1225.5533 to −729.1400 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05963 | 0.07802 | +30.9% | +0.0096 to +0.0272 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.35 | −5.7% | −0.2608 to +0.0989 | no |
| Omni's own CPU (cores), mean | 0 | 0.07031 | +0.070 (native is 0) | +0.0624 to +0.0782 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.42 | −0.7% | −0.1960 to +0.1748 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.6 | 394 | −13.1% | −90.6699 to −28.5308 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.151 | +8.8% | −0.0566 to +0.4061 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.3656 to +1.5656 | no |
| pod start wait, total (s) | 0.3 | 1.5 | +400.0% | −0.9801 to +3.3801 | no |
| pod start wait, mean (s) | 0.3 | 0.6333 | +111.1% | −0.7680 to +1.4346 | no |
| host CPU busy, the real machine under kind (%) | 44.17 | 41.67 | −5.7% | −6.5451 to +1.5389 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1454 | 766.8 | −47.3% | −769.1161 to −604.8839 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 155.6 | 0.05417 | −100.0% | −205.8066 to −105.3267 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 715.4 | 0.3 | −100.0% | −870.4011 to −559.7989 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 768.1 | 72.18 | −90.6% | −805.6774 to −586.1560 | yes: GAIN |
| queue: jobs unfinished at the window's end | 5.9 | 0 | −100.0% | −12.3989 to +0.5989 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.98 | −0.3% | −0.0566 to +0.0161 | no |
| node-hours | 2.513 | 2.508 | −0.2% | −0.0240 to +0.0130 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.3 | +0.0% | −1.7835 to +2.0070 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 270.7 | −0.2% | −2.5058 to +1.4543 | no |
| response time (ms), mean | 271.5 | 100.8 | −62.9% | −300.5448 to −40.9437 | yes: GAIN |
| response time (ms), 95th percentile | 918.5 | 223.8 | −75.6% | −1325.4578 to −63.8462 | yes: GAIN |
| response time (ms), 99th percentile | 1352 | 331.7 | −75.5% | −1943.4900 to −96.5608 | yes: GAIN |
| time over the response line (% of samples) | 10.42 | 0.1644 | −98.4% | −20.4836 to −0.0341 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 0.1 | −98.5% | −10.5188 to −2.2812 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.9 | +95.900 (native is 0) | +80.4092 to +111.3908 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.285 | 1110 | +11850.9% | +848.9522 to +1351.7678 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05709 | 0.05774 | +1.1% | −0.0050 to +0.0063 | no |
| CPU used (cores), mean | 1.37 | 1.381 | +0.8% | −0.1218 to +0.1438 | no |
| Omni's own CPU (cores), mean | 0 | 0.06697 | +0.067 (native is 0) | +0.0590 to +0.0750 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.37 | 1.448 | +5.7% | −0.0475 to +0.2034 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.6 | 467.6 | −2.7% | −52.5574 to +26.4015 | no |
| HPA replicas, mean | 2.011 | 2.046 | +1.7% | −0.1734 to +0.2433 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 38.98 | 45.72 | +17.3% | +3.9579 to +9.5187 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.7 | 1457 | +92.0% | +624.9172 to +771.0828 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.611 | −6.5% | −1.5078 to +0.7291 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.004167 | 161.3 | +3871900.0% | +109.6592 to +212.9992 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 672.1 | +672.100 (native is 0) | +455.6499 to +888.5501 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 64.19 | 797 | +1141.6% | +621.6143 to +843.9774 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.3 | +9.300 (native is 0) | +4.0215 to +14.5785 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*