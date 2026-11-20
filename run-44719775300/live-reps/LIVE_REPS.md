# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.842 | 5.981 |
| node-hours | 2.515 | 2.518 | 2.028 | 2.507 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 | 272.8 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.4 | 236.3 | 270.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 352.6 | 132 | 347.7 | 135.1 |
| response time (ms), 95th percentile | 1279 | 226.1 | 1452 | 240.4 |
| response time (ms), 99th percentile | 1804 | 323.7 | 2027 | 347 |
| time over the response line (% of samples) | 16.29 | 0.1856 | 16.57 | 0.2641 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 0 | 9.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 142.3 | 36.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.423 | 1087 | 10.65 | 1175 |
| utilisation (used / allocatable) | 0.06045 | 0.05974 | 0.0766 | 0.05855 |
| CPU used (cores), mean | 1.451 | 1.434 | 1.444 | 1.401 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07046 | 0.06532 |
| CPU used with Omni's own (cores), mean | 1.451 | 1.434 | 1.515 | 1.466 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.1 | 454 | 391.3 | 461.7 |
| HPA replicas, mean | 1.924 | 2 | 2.225 | 2.207 |
| pods started | 0.1 | 0 | 1.2 | 1.1 |
| pod start wait, total (s) | 0.1 | 0 | 2.8 | 2.7 |
| pod start wait, mean (s) | 0.1 | 0 | 1.167 | 0.7333 |
| host CPU busy, the real machine under kind (%) | 41.23 | 44.57 | 44.04 | 46.19 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 784 | 1426 | 793.9 | 1451 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.272 | 5.635 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 137.7 | 0.06667 | 173.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 591 | 0.4 | 791.3 |
| queue: job turnaround, submitted to done, mean (s) | 89.74 | 784.5 | 99.63 | 851.6 |
| queue: jobs unfinished at the window's end | 0 | 10.1 | 0 | 11 |
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
| worker nodes in service, mean | 6 | 5.981 | −0.3% | −0.0474 to +0.0097 | no |
| node-hours | 2.518 | 2.507 | −0.4% | −0.0238 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.5 | −0.3% | −2.2833 to +0.4488 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 270.9 | −0.6% | −2.8335 to −0.1925 | yes: GAIN |
| response time (ms), mean | 132 | 135.1 | +2.4% | −0.8463 to +7.0681 | no |
| response time (ms), 95th percentile | 226.1 | 240.4 | +6.3% | +2.0033 to +26.5387 | yes: LOSS |
| response time (ms), 99th percentile | 323.7 | 347 | +7.2% | +2.4052 to +44.1348 | yes: LOSS |
| time over the response line (% of samples) | 0.1856 | 0.2641 | +42.3% | −0.0560 to +0.2131 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.9 | +36.900 (native is 0) | +15.4794 to +58.3206 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1087 | 1175 | +8.0% | +33.4325 to +141.3209 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05974 | 0.05855 | −2.0% | −0.0029 to +0.0005 | no |
| CPU used (cores), mean | 1.434 | 1.401 | −2.3% | −0.0700 to +0.0045 | no |
| Omni's own CPU (cores), mean | 0 | 0.06532 | +0.065 (native is 0) | +0.0580 to +0.0726 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.434 | 1.466 | +2.3% | −0.0014 to +0.0666 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454 | 461.7 | +1.7% | −3.5043 to +18.9011 | no |
| HPA replicas, mean | 2 | 2.207 | +10.4% | +0.0166 to +0.3974 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | −0.1818 to +2.3818 | no |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | −0.5352 to +5.9352 | no |
| pod start wait, mean (s) | 0 | 0.7333 | +0.733 (native is 0) | −0.1286 to +1.5952 | no |
| host CPU busy, the real machine under kind (%) | 44.57 | 46.19 | +3.6% | +1.0445 to +2.1828 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1426 | 1451 | +1.8% | −21.0195 to +72.6195 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.635 | −6.1% | −1.1520 to +0.4215 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 137.7 | 173.9 | +26.3% | −7.2483 to +79.7566 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 591 | 791.3 | +33.9% | +25.1404 to +375.4596 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 784.5 | 851.6 | +8.6% | +28.7544 to +105.4872 | yes: LOSS |
| queue: jobs unfinished at the window's end | 10.1 | 11 | +8.9% | −0.8986 to +2.6986 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.518 | +0.1% | −0.0030 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 | −0.1% | −2.0297 to +1.6576 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.4 | −0.1% | −2.0297 to +1.6576 | no |
| response time (ms), mean | 352.6 | 132 | −62.6% | −361.4847 to −79.7250 | yes: GAIN |
| response time (ms), 95th percentile | 1279 | 226.1 | −82.3% | −1733.9761 to −370.9799 | yes: GAIN |
| response time (ms), 99th percentile | 1804 | 323.7 | −82.1% | −2436.4094 to −524.2882 | yes: GAIN |
| time over the response line (% of samples) | 16.29 | 0.1856 | −98.9% | −27.2279 to −4.9719 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 0 | −100.0% | −13.2626 to −3.9374 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.423 | 1087 | +11437.1% | +808.7373 to +1346.7694 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06045 | 0.05974 | −1.2% | −0.0061 to +0.0047 | no |
| CPU used (cores), mean | 1.451 | 1.434 | −1.2% | −0.1470 to +0.1130 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.451 | 1.434 | −1.2% | −0.1470 to +0.1130 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.1 | 454 | −1.1% | −43.4246 to +33.1961 | no |
| HPA replicas, mean | 1.924 | 2 | +3.9% | −0.1196 to +0.2711 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 41.23 | 44.57 | +8.1% | +0.5579 to +6.1253 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784 | 1426 | +81.8% | +563.8049 to +719.1951 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 137.7 | +412912.5% | +90.4020 to +184.8730 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 591 | +590900.0% | +384.8740 to +796.9260 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.74 | 784.5 | +774.1% | +574.3462 to +815.1205 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.1 | +10.100 (native is 0) | +4.4430 to +15.7570 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.842 | −19.3% | −2.0942 to −0.2219 | yes: GAIN |
| node-hours | 2.515 | 2.028 | −19.3% | −0.8783 to −0.0948 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.8 | +0.1% | −0.6758 to +1.0198 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 236.3 | −13.3% | −65.9469 to −6.7174 | yes: GAIN |
| response time (ms), mean | 352.6 | 347.7 | −1.4% | −21.6912 to +11.8188 | no |
| response time (ms), 95th percentile | 1279 | 1452 | +13.5% | +61.0326 to +285.2654 | yes: LOSS |
| response time (ms), 99th percentile | 1804 | 2027 | +12.3% | +11.6833 to +433.3689 | yes: LOSS |
| time over the response line (% of samples) | 16.29 | 16.57 | +1.7% | −0.3307 to +0.8931 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 9.4 | +9.3% | +0.0612 to +1.5388 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.3 | +142.300 (native is 0) | +41.0318 to +243.5682 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.423 | 10.65 | +13.0% | −0.2833 to +2.7299 | no |
| utilisation (used / allocatable) | 0.06045 | 0.0766 | +26.7% | +0.0033 to +0.0290 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.451 | 1.444 | −0.5% | −0.0412 to +0.0280 | no |
| Omni's own CPU (cores), mean | 0 | 0.07046 | +0.070 (native is 0) | +0.0635 to +0.0775 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.451 | 1.515 | +4.4% | +0.0228 to +0.1048 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.1 | 391.3 | −14.8% | −118.7784 to −16.7958 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.924 | 2.225 | +15.6% | +0.1095 to +0.4918 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.8 | +2700.0% | +0.4118 to +4.9882 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.167 | +1066.7% | +0.0832 to +2.0501 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.23 | 44.04 | +6.8% | +1.8640 to +3.7595 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784 | 793.9 | +1.3% | +2.5397 to +17.2603 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.272 | −28.8% | −3.0017 to −0.4535 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.06667 | +100.0% | −0.0005 to +0.0672 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.74 | 99.63 | +11.0% | +2.3675 to +17.4075 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.842 | −19.3% | −2.0942 to −0.2219 | yes: GAIN |
| node-hours | 2.518 | 2.028 | −19.4% | −0.8808 to −0.0986 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.8 | +0.1% | −1.8280 to +2.5441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 236.3 | −13.3% | −67.2190 to −5.0733 | yes: GAIN |
| response time (ms), mean | 132 | 347.7 | +163.3% | +64.6663 to +366.6711 | yes: LOSS |
| response time (ms), 95th percentile | 226.1 | 1452 | +542.0% | +440.6553 to +2010.5987 | yes: LOSS |
| response time (ms), 99th percentile | 323.7 | 2027 | +526.0% | +618.1273 to +2787.6225 | yes: LOSS |
| time over the response line (% of samples) | 0.1856 | 16.57 | +8826.5% | +5.3843 to +27.3779 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 9.4 | +9.400 (native is 0) | +4.5579 to +14.2421 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.3 | +142.300 (native is 0) | +41.0318 to +243.5682 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1087 | 10.65 | −99.0% | −1345.4040 to −807.6560 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05974 | 0.0766 | +28.2% | +0.0077 to +0.0260 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.434 | 1.444 | +0.7% | −0.1489 to +0.1696 | no |
| Omni's own CPU (cores), mean | 0 | 0.07046 | +0.070 (native is 0) | +0.0635 to +0.0775 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.434 | 1.515 | +5.6% | −0.0843 to +0.2459 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454 | 391.3 | −13.8% | −87.6634 to −37.6823 | yes, down (shown, not judged) |
| HPA replicas, mean | 2 | 2.225 | +11.2% | +0.0015 to +0.4483 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.2583 to +2.1417 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | +0.5940 to +5.0060 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.167 | +1.167 (native is 0) | +0.2816 to +2.0517 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.57 | 44.04 | −1.2% | −3.8955 to +2.8358 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1426 | 793.9 | −44.3% | −707.2538 to −555.9462 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 137.7 | 0.06667 | −100.0% | −184.8226 to −90.3858 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 591 | 0.4 | −99.9% | −796.5837 to −384.6163 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 784.5 | 99.63 | −87.3% | −800.3098 to −569.3818 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.1 | 0 | −100.0% | −15.7570 to −4.4430 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.981 | −0.3% | −0.0474 to +0.0097 | no |
| node-hours | 2.515 | 2.507 | −0.3% | −0.0178 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.5 | −0.4% | −3.3798 to +1.1733 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 270.9 | −0.6% | −3.4747 to +0.0766 | no |
| response time (ms), mean | 352.6 | 135.1 | −61.7% | −355.5604 to −79.4275 | yes: GAIN |
| response time (ms), 95th percentile | 1279 | 240.4 | −81.2% | −1711.0128 to −365.4012 | yes: GAIN |
| response time (ms), 99th percentile | 1804 | 347 | −80.8% | −2409.6674 to −504.4902 | yes: GAIN |
| time over the response line (% of samples) | 16.29 | 0.2641 | −98.4% | −27.1307 to −4.9120 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 0 | −100.0% | −13.2626 to −3.9374 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.9 | +36.900 (native is 0) | +15.4794 to +58.3206 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.423 | 1175 | +12364.3% | +913.3601 to +1416.8999 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06045 | 0.05855 | −3.1% | −0.0081 to +0.0044 | no |
| CPU used (cores), mean | 1.451 | 1.401 | −3.4% | −0.1961 to +0.0967 | no |
| Omni's own CPU (cores), mean | 0 | 0.06532 | +0.065 (native is 0) | +0.0580 to +0.0726 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.451 | 1.466 | +1.1% | −0.1241 to +0.1553 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.1 | 461.7 | +0.6% | −41.4093 to +46.5776 | no |
| HPA replicas, mean | 1.924 | 2.207 | +14.7% | +0.0363 to +0.5292 | yes: power given |
| pods started | 0.1 | 1.1 | +1000.0% | −0.3488 to +2.3488 | no |
| pod start wait, total (s) | 0.1 | 2.7 | +2600.0% | −0.6901 to +5.8901 | no |
| pod start wait, mean (s) | 0.1 | 0.7333 | +633.3% | −0.3034 to +1.5700 | no |
| host CPU busy, the real machine under kind (%) | 41.23 | 46.19 | +12.0% | +1.9021 to +8.0084 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 784 | 1451 | +85.1% | +603.6917 to +730.9083 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.635 | −6.1% | −1.1520 to +0.4215 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 173.9 | +521675.0% | +120.1741 to +227.6093 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 791.3 | +791200.0% | +575.7011 to +1006.6989 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.74 | 851.6 | +848.9% | +650.4981 to +873.2103 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11 | +11.000 (native is 0) | +4.9963 to +17.0037 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*