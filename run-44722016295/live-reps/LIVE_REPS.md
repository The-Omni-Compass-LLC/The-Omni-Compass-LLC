# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.476 | 4.203 |
| node-hours | 2.514 | 2.519 | 1.878 | 1.762 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.8 | 271 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 271.8 | 223 | 214.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 245.5 | 206.8 | 224.5 | 209 |
| response time (ms), 95th percentile | 792.6 | 678.3 | 838.3 | 816.2 |
| response time (ms), 99th percentile | 1104 | 1027 | 1148 | 1264 |
| time over the response line (% of samples) | 7.93 | 4.835 | 8.982 | 6.617 |
| failed requests (%) | 0 | 0 | 0.02145 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 3.1 | 6.5 | 4.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 159.8 | 127.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 20.2 | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.8 | 12.94 | 8.717 | 15.28 |
| utilisation (used / allocatable) | 0.05603 | 0.05693 | 0.07497 | 0.07889 |
| CPU used (cores), mean | 1.345 | 1.366 | 1.316 | 1.32 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06937 | 0.07369 |
| CPU used with Omni's own (cores), mean | 1.345 | 1.366 | 1.386 | 1.393 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492 | 484.3 | 407.8 | 395.2 |
| HPA replicas, mean | 1.964 | 1.98 | 2.237 | 2.172 |
| pods started | 0 | 0.2 | 1.7 | 1.1 |
| pod start wait, total (s) | 0 | 0.5 | 4.1 | 2.7 |
| pod start wait, mean (s) | 0 | 0.25 | 1.91 | 1.2 |
| host CPU busy, the real machine under kind (%) | 38.87 | 39.71 | 41.66 | 43.12 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 755.2 | 762.4 | 759.3 | 775.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.702 | 3.122 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.6667 | 0.2583 | 0.8042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.2 | 1.1 | 1.8 |
| queue: job turnaround, submitted to done, mean (s) | 60.85 | 70.74 | 65.6 | 86.35 |
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
| worker nodes in service, mean | 6 | 4.203 | −29.9% | −2.5597 to −1.0334 | yes: GAIN |
| node-hours | 2.519 | 1.762 | −30.1% | −1.0766 to −0.4378 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 270.6 | −0.4% | −2.3522 to +0.1228 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 214.2 | −21.2% | −82.2769 to −32.8067 | yes: GAIN |
| response time (ms), mean | 206.8 | 209 | +1.1% | −27.2065 to +31.6576 | no |
| response time (ms), 95th percentile | 678.3 | 816.2 | +20.3% | −37.4772 to +313.3202 | no |
| response time (ms), 99th percentile | 1027 | 1264 | +23.0% | +27.2252 to +445.2580 | yes: LOSS |
| time over the response line (% of samples) | 4.835 | 6.617 | +36.9% | −0.0079 to +3.5719 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 4.9 | +58.1% | −0.6733 to +4.2733 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.2 | +127.200 (native is 0) | +66.7804 to +187.6196 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.94 | 15.28 | +18.1% | −1.0703 to +5.7603 | no |
| utilisation (used / allocatable) | 0.05693 | 0.07889 | +38.6% | +0.0133 to +0.0306 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.366 | 1.32 | −3.4% | −0.1226 to +0.0293 | no |
| Omni's own CPU (cores), mean | 0 | 0.07369 | +0.074 (native is 0) | +0.0662 to +0.0811 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.393 | +2.0% | −0.0552 to +0.1093 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.3 | 395.2 | −18.4% | −121.6091 to −56.5751 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.98 | 2.172 | +9.7% | −0.0492 to +0.4319 | no |
| pods started | 0.2 | 1.1 | +450.0% | −0.2410 to +2.0410 | no |
| pod start wait, total (s) | 0.5 | 2.7 | +440.0% | −0.6771 to +5.0771 | no |
| pod start wait, mean (s) | 0.25 | 1.2 | +380.0% | −0.2839 to +2.1839 | no |
| host CPU busy, the real machine under kind (%) | 39.71 | 43.12 | +8.6% | +2.4616 to +4.3695 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 762.4 | 775.9 | +1.8% | +1.6776 to +25.3224 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.122 | −48.0% | −3.9283 to −1.8273 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6667 | 0.8042 | +20.6% | −0.0233 to +0.2983 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.8 | +50.0% | −0.5285 to +1.7285 | no |
| queue: job turnaround, submitted to done, mean (s) | 70.74 | 86.35 | +22.1% | −1.7219 to +32.9385 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.519 | +0.2% | −0.0014 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.8 | +0.3% | +0.1373 to +1.6649 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 271.8 | +0.3% | +0.1373 to +1.6649 | yes: power given |
| response time (ms), mean | 245.5 | 206.8 | −15.8% | −62.8670 to −14.5879 | yes: GAIN |
| response time (ms), 95th percentile | 792.6 | 678.3 | −14.4% | −192.5325 to −36.0285 | yes: GAIN |
| response time (ms), 99th percentile | 1104 | 1027 | −6.9% | −252.6092 to +99.3840 | no |
| time over the response line (% of samples) | 7.93 | 4.835 | −39.0% | −5.8361 to −0.3535 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 3.1 | −47.5% | −5.6771 to +0.0771 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.8 | 12.94 | +47.0% | +1.2401 to +7.0365 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05603 | 0.05693 | +1.6% | +0.0000 to +0.0018 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.345 | 1.366 | +1.6% | +0.0008 to +0.0421 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.345 | 1.366 | +1.6% | +0.0008 to +0.0421 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492 | 484.3 | −1.6% | −15.8712 to +0.5347 | no |
| HPA replicas, mean | 1.964 | 1.98 | +0.8% | −0.1150 to +0.1475 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.25 | +0.250 (native is 0) | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 38.87 | 39.71 | +2.2% | +0.4463 to +1.2288 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.2 | 762.4 | +1.0% | −2.6529 to +17.0529 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.6667 | +1042.9% | +0.5274 to +0.6893 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.2 | +200.0% | +0.4984 to +1.1016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 60.85 | 70.74 | +16.2% | −1.8543 to +21.6293 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.476 | −25.4% | −2.3489 to −0.6997 | yes: GAIN |
| node-hours | 2.514 | 1.878 | −25.3% | −0.9824 to −0.2905 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271 | +0.0% | −0.5572 to +0.7496 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 223 | −17.7% | −74.2368 to −21.4875 | yes: GAIN |
| response time (ms), mean | 245.5 | 224.5 | −8.6% | −30.8978 to −11.1474 | yes: GAIN |
| response time (ms), 95th percentile | 792.6 | 838.3 | +5.8% | −27.3861 to +118.7621 | no |
| response time (ms), 99th percentile | 1104 | 1148 | +4.0% | −20.7848 to +109.4406 | no |
| time over the response line (% of samples) | 7.93 | 8.982 | +13.3% | −0.7911 to +2.8961 | no |
| failed requests (%) | 0 | 0.02145 | +0.021 (native is 0) | −0.0109 to +0.0538 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 6.5 | +10.2% | −0.7572 to +1.9572 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 159.8 | +159.800 (native is 0) | +79.9445 to +239.6555 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.8 | 8.717 | −0.9% | −2.3331 to +2.1664 | no |
| utilisation (used / allocatable) | 0.05603 | 0.07497 | +33.8% | +0.0079 to +0.0300 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.345 | 1.316 | −2.1% | −0.0707 to +0.0140 | no |
| Omni's own CPU (cores), mean | 0 | 0.06937 | +0.069 (native is 0) | +0.0626 to +0.0761 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.345 | 1.386 | +3.0% | −0.0067 to +0.0887 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492 | 407.8 | −17.1% | −129.2768 to −39.0612 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.237 | +13.9% | +0.0378 to +0.5076 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.6856 to +2.7144 | yes: power given |
| pod start wait, total (s) | 0 | 4.1 | +4.100 (native is 0) | +1.4353 to +6.7647 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.91 | +1.910 (native is 0) | +1.1182 to +2.7018 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.87 | 41.66 | +7.2% | +2.3896 to +3.1954 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.2 | 759.3 | +0.5% | −2.7398 to +10.9398 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.702 | −38.3% | −3.4130 to −1.1836 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.2583 | +342.9% | −0.2346 to +0.6346 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | +175.0% | −1.1485 to +2.5485 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.85 | 65.6 | +7.8% | −0.4185 to +9.9185 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.476 | −25.4% | −2.3489 to −0.6997 | yes: GAIN |
| node-hours | 2.519 | 1.878 | −25.5% | −0.9841 to −0.2994 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271 | −0.3% | −1.5052 to −0.1046 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 223 | −17.9% | −74.7243 to −22.8022 | yes: GAIN |
| response time (ms), mean | 206.8 | 224.5 | +8.6% | −5.9283 to +41.3381 | no |
| response time (ms), 95th percentile | 678.3 | 838.3 | +23.6% | +76.8765 to +243.0605 | yes: LOSS |
| response time (ms), 99th percentile | 1027 | 1148 | +11.8% | −74.7434 to +316.6244 | no |
| time over the response line (% of samples) | 4.835 | 8.982 | +85.8% | +0.6443 to +7.6504 | yes: LOSS |
| failed requests (%) | 0 | 0.02145 | +0.021 (native is 0) | −0.0109 to +0.0538 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 6.5 | +109.7% | +0.2153 to +6.5847 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 159.8 | +159.800 (native is 0) | +79.9445 to +239.6555 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.94 | 8.717 | −32.6% | −7.4059 to −1.0375 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05693 | 0.07497 | +31.7% | +0.0072 to +0.0289 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.366 | 1.316 | −3.6% | −0.0959 to −0.0037 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06937 | +0.069 (native is 0) | +0.0626 to +0.0761 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.386 | +1.4% | −0.0321 to +0.0713 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.3 | 407.8 | −15.8% | −118.4754 to −34.5263 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.98 | 2.237 | +13.0% | −0.0018 to +0.5147 | no |
| pods started | 0.2 | 1.7 | +750.0% | +0.4204 to +2.5796 | yes: power given |
| pod start wait, total (s) | 0.5 | 4.1 | +720.0% | +0.6954 to +6.5046 | yes: LOSS |
| pod start wait, mean (s) | 0.25 | 1.91 | +664.0% | +0.7002 to +2.6198 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.71 | 41.66 | +4.9% | +1.4899 to +2.4201 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 762.4 | 759.3 | −0.4% | −7.8622 to +1.6622 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.702 | −38.3% | −3.4130 to −1.1836 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6667 | 0.2583 | −61.2% | −0.7853 to −0.0314 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.1 | −8.3% | −1.8986 to +1.6986 | no |
| queue: job turnaround, submitted to done, mean (s) | 70.74 | 65.6 | −7.3% | −13.0582 to +2.7832 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.203 | −29.9% | −2.5597 to −1.0334 | yes: GAIN |
| node-hours | 2.514 | 1.762 | −29.9% | −1.0742 to −0.4295 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 270.6 | −0.1% | −1.7866 to +1.3593 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 214.2 | −20.9% | −81.7300 to −31.5514 | yes: GAIN |
| response time (ms), mean | 245.5 | 209 | −14.9% | −50.7411 to −22.2628 | yes: GAIN |
| response time (ms), 95th percentile | 792.6 | 816.2 | +3.0% | −133.1737 to +180.4557 | no |
| response time (ms), 99th percentile | 1104 | 1264 | +14.5% | −161.5999 to +480.8579 | no |
| time over the response line (% of samples) | 7.93 | 6.617 | −16.6% | −3.5399 to +0.9142 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 4.9 | −16.9% | −2.9371 to +0.9371 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.2 | +127.200 (native is 0) | +66.7804 to +187.6196 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.8 | 15.28 | +73.7% | +2.1698 to +10.7968 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05603 | 0.07889 | +40.8% | +0.0140 to +0.0317 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.345 | 1.32 | −1.9% | −0.0943 to +0.0438 | no |
| Omni's own CPU (cores), mean | 0 | 0.07369 | +0.074 (native is 0) | +0.0662 to +0.0811 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.345 | 1.393 | +3.6% | −0.0269 to +0.1238 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492 | 395.2 | −19.7% | −131.9043 to −61.6164 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.172 | +10.6% | −0.0129 to +0.4280 | no |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.3626 to +5.0374 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.2718 to +2.1282 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.87 | 43.12 | +10.9% | +3.3260 to +5.1802 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.2 | 775.9 | +2.7% | +2.6164 to +38.7836 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.122 | −48.0% | −3.9283 to −1.8273 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.8042 | +1278.6% | +0.5110 to +0.9807 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.8 | +350.0% | +0.2222 to +2.5778 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 60.85 | 86.35 | +41.9% | +2.2954 to +48.6963 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*