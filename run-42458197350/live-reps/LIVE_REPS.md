# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.87 | 6 |
| node-hours | 2.508 | 2.515 | 2.039 | 2.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.6 | 271.4 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 271.6 | 235.9 | 272.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 289.9 | 115.3 | 278.3 | 114.3 |
| response time (ms), 95th percentile | 986.8 | 198.9 | 1111 | 254 |
| response time (ms), 99th percentile | 1425 | 294.5 | 1600 | 376.4 |
| time over the response line (% of samples) | 11.96 | 0.08897 | 12.23 | 0.4039 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.333 | 0 | 8.222 | 0.1667 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 150.6 | 89.17 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.67 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.131 | 909.8 | 9.38 | 1299 |
| utilisation (used / allocatable) | 0.05778 | 0.05874 | 0.07289 | 0.05871 |
| CPU used (cores), mean | 1.387 | 1.41 | 1.37 | 1.409 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07202 | 0.06967 |
| CPU used with Omni's own (cores), mean | 1.387 | 1.41 | 1.442 | 1.479 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.3 | 461 | 412.4 | 460 |
| HPA replicas, mean | 2.029 | 1.917 | 2.346 | 1.936 |
| pods started | 0.2222 | 0 | 1.778 | 0.1667 |
| pod start wait, total (s) | 0.5556 | 0 | 4.222 | 0.3333 |
| pod start wait, mean (s) | 0.2778 | 0 | 1.509 | 0.3333 |
| host CPU busy, the real machine under kind (%) | 39.28 | 43.5 | 42.63 | 47.1 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 762.1 | 1440 | 769.1 | 1512 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.385 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02778 | 113.7 | 0.04167 | 185.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2222 | 542.7 | 0.1111 | 808.8 |
| queue: job turnaround, submitted to done, mean (s) | 69.09 | 713.4 | 75.65 | 913.9 |
| queue: jobs unfinished at the window's end | 0 | 4.833 | 0 | 13.33 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.521 | +0.3% | −0.0312 to +0.0478 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 | +0.1% | −4.9994 to +5.3141 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272 | +0.1% | −4.9994 to +5.3141 | no |
| response time (ms), mean | 109.6 | 95.03 | −13.3% | −19.0542 to −10.1406 | yes: GAIN |
| response time (ms), 95th percentile | 195.1 | 211.8 | +8.6% | −14.1530 to +47.6797 | no |
| response time (ms), 99th percentile | 293.8 | 308.2 | +4.9% | −57.2930 to +86.1816 | no |
| time over the response line (% of samples) | 0.07692 | 0.1267 | +64.8% | −0.1646 to +0.2642 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95 | +95.000 (native is 0) | +57.4873 to +132.5127 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1010 | 1141 | +13.0% | −22.8227 to +285.4561 | no |
| utilisation (used / allocatable) | 0.06045 | 0.05837 | −3.4% | −0.0057 to +0.0015 | no |
| CPU used (cores), mean | 1.451 | 1.401 | −3.4% | −0.1361 to +0.0361 | no |
| Omni's own CPU (cores), mean | 0 | 0.06377 | +0.064 (native is 0) | +0.0300 to +0.0975 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.451 | 1.465 | +0.9% | −0.0747 to +0.1023 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.6 | 462.4 | +3.3% | −10.4779 to +40.0498 | no |
| HPA replicas, mean | 1.879 | 1.913 | +1.8% | −0.7754 to +0.8417 | no |
| pods started | 0 | 0.3333 | +0.333 (native is 0) | −1.1010 to +1.7677 | no |
| pod start wait, total (s) | 0 | 0.6667 | +0.667 (native is 0) | −2.2020 to +3.5353 | no |
| pod start wait, mean (s) | 0 | 0.6667 | +0.667 (native is 0) | −2.2020 to +3.5353 | no |
| host CPU busy, the real machine under kind (%) | 44.6 | 45.8 | +2.7% | −0.7591 to +3.1625 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1486 | 1511 | +1.7% | −10.1917 to +61.5250 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 125.6 | 185 | +47.3% | −90.1269 to +208.9325 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 574.7 | 848.3 | +47.6% | −101.4136 to +648.7469 | no |
| queue: job turnaround, submitted to done, mean (s) | 764.1 | 798.7 | +4.5% | −30.5649 to +99.7593 | no |
| queue: jobs unfinished at the window's end | 5 | 8 | +60.0% | −4.4530 to +10.4530 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 6 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.508 | 2.515 | +0.3% | −0.0009 to +0.0143 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 271.6 | +0.8% | −1.1216 to +5.2757 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 271.6 | +0.8% | −1.1216 to +5.2757 | no |
| response time (ms), mean | 211.5 | 115.3 | −45.5% | −266.2632 to +73.6688 | no |
| response time (ms), 95th percentile | 666 | 198.9 | −70.1% | −1259.8045 to +325.5262 | no |
| response time (ms), 99th percentile | 962.3 | 294.5 | −69.4% | −1804.3184 to +468.7024 | no |
| time over the response line (% of samples) | 6.659 | 0.08897 | −98.7% | −19.7746 to +6.6336 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.833 | 0 | −100.0% | −10.7118 to +1.0451 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.439 | 909.8 | +12130.7% | +549.0628 to +1255.7094 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05408 | 0.05874 | +8.6% | −0.0019 to +0.0112 | no |
| CPU used (cores), mean | 1.298 | 1.41 | +8.6% | −0.0453 to +0.2688 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.298 | 1.41 | +8.6% | −0.0453 to +0.2688 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 505 | 461 | −8.7% | −93.5885 to +5.6061 | no |
| HPA replicas, mean | 2.003 | 1.917 | −4.3% | −0.1973 to +0.0252 | no |
| pods started | 0.3333 | 0 | −100.0% | −1.1903 to +0.5237 | no |
| pod start wait, total (s) | 0.8333 | 0 | −100.0% | −2.9758 to +1.3092 | no |
| pod start wait, mean (s) | 0.4167 | 0 | −100.0% | −1.4879 to +0.6546 | no |
| host CPU busy, the real machine under kind (%) | 36.47 | 43.5 | +19.3% | +3.3830 to +10.6771 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 741.5 | 1440 | +94.2% | +562.7607 to +834.2393 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03472 | 113.7 | +327420.0% | +75.9069 to +151.4681 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 542.7 | +162700.0% | +318.6261 to +766.0405 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 48.57 | 713.4 | +1368.9% | +479.7589 to +849.9911 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 4.833 | +4.833 (native is 0) | −1.6510 to +11.3177 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.87 | −18.8% | −2.1240 to −0.1370 | yes: GAIN |
| node-hours | 2.508 | 2.039 | −18.7% | −0.8832 to −0.0542 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.4 | +0.2% | +0.0635 to +1.0350 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 235.9 | −12.9% | −66.3754 to −3.6929 | yes: GAIN |
| response time (ms), mean | 289.9 | 278.3 | −4.0% | −23.5466 to +0.2962 | no |
| response time (ms), 95th percentile | 986.8 | 1111 | +12.6% | +21.0348 to +227.9352 | yes: LOSS |
| response time (ms), 99th percentile | 1425 | 1600 | +12.2% | +54.4431 to +294.7649 | yes: LOSS |
| time over the response line (% of samples) | 11.96 | 12.23 | +2.2% | −0.5777 to +1.1048 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.333 | 8.222 | +12.1% | +0.1756 to +1.6022 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 150.6 | +150.556 (native is 0) | +66.8008 to +234.3103 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.131 | 9.38 | +2.7% | −1.8988 to +2.3951 | no |
| utilisation (used / allocatable) | 0.05778 | 0.07289 | +26.2% | +0.0014 to +0.0288 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.387 | 1.37 | −1.2% | −0.0532 to +0.0202 | no |
| Omni's own CPU (cores), mean | 0 | 0.07202 | +0.072 (native is 0) | +0.0666 to +0.0775 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.387 | 1.442 | +4.0% | +0.0150 to +0.0961 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.3 | 412.4 | −13.6% | −124.1096 to −5.5862 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.029 | 2.346 | +15.6% | +0.1224 to +0.5124 | yes: power given |
| pods started | 0.2222 | 1.778 | +700.0% | +0.4610 to +2.6501 | yes: power given |
| pod start wait, total (s) | 0.5556 | 4.222 | +660.0% | +0.9490 to +6.3843 | yes: LOSS |
| pod start wait, mean (s) | 0.2778 | 1.509 | +443.3% | +0.3675 to +2.0955 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.28 | 42.63 | +8.5% | +2.9308 to +3.7729 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 762.1 | 769.1 | +0.9% | −1.5163 to +15.5163 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.385 | −26.9% | −2.9912 to −0.2391 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02778 | 0.04167 | +50.0% | −0.0181 to +0.0459 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2222 | 0.1111 | −50.0% | −0.5730 to +0.3508 | no |
| queue: job turnaround, submitted to done, mean (s) | 69.09 | 75.65 | +9.5% | +0.0161 to +13.1135 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 6 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.423 | −26.3% | −3.0354 to −0.1183 | yes: GAIN |
| node-hours | 2.515 | 1.857 | −26.2% | −1.2762 to −0.0407 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.4 | −0.5% | −4.6825 to +2.1578 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 220.7 | −18.7% | −99.6154 to −2.2149 | yes: GAIN |
| response time (ms), mean | 115.3 | 197.1 | +71.0% | −93.8315 to +257.4433 | no |
| response time (ms), 95th percentile | 198.9 | 746.8 | +275.5% | −341.1964 to +1437.0247 | no |
| response time (ms), 99th percentile | 294.5 | 1067 | +262.2% | −491.2296 to +2036.0566 | no |
| time over the response line (% of samples) | 0.08897 | 6.691 | +7420.5% | −5.7249 to +18.9284 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 5.5 | +5.500 (native is 0) | −0.2008 to +11.2008 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 205.5 | +205.500 (native is 0) | +111.7478 to +299.2522 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 909.8 | 8.019 | −99.1% | −1252.6154 to −550.9957 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05874 | 0.07478 | +27.3% | −0.0008 to +0.0329 | no |
| CPU used (cores), mean | 1.41 | 1.262 | −10.5% | −0.3410 to +0.0447 | no |
| Omni's own CPU (cores), mean | 0 | 0.06955 | +0.070 (native is 0) | +0.0637 to +0.0754 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.331 | −5.6% | −0.2771 to +0.1199 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461 | 416.1 | −9.7% | −103.5094 to +13.8267 | no |
| HPA replicas, mean | 1.917 | 2.232 | +16.5% | −0.0079 to +0.6386 | no |
| pods started | 0 | 1.167 | +1.167 (native is 0) | −0.5149 to +2.8482 | no |
| pod start wait, total (s) | 0 | 2.833 | +2.833 (native is 0) | −1.6893 to +7.3560 | no |
| pod start wait, mean (s) | 0 | 1.125 | +1.125 (native is 0) | −0.2001 to +2.4501 | no |
| host CPU busy, the real machine under kind (%) | 43.5 | 39.65 | −8.9% | −7.8146 to +0.1110 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1440 | 744.3 | −48.3% | −833.7650 to −557.5684 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.055 | −65.7% | −4.1031 to −3.7864 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 113.7 | 0.02778 | −100.0% | −151.4826 to −75.9063 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 542.7 | 0 | −100.0% | −766.4349 to −318.8984 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 713.4 | 52.63 | −92.6% | −842.1222 to −479.5028 | yes: GAIN |
| queue: jobs unfinished at the window's end | 4.833 | 0 | −100.0% | −11.3177 to +1.6510 | no |

## omni on top of the orchestrator vs the organism alone, 6 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.506 | 2.52 | +0.5% | +0.0050 to +0.0222 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.2 | +0.1% | −3.4659 to +3.9278 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.2 | +0.1% | −3.4659 to +3.9278 | no |
| response time (ms), mean | 356.1 | 114.3 | −67.9% | −464.4588 to −19.2500 | yes: GAIN |
| response time (ms), 95th percentile | 1288 | 254 | −80.3% | −2044.3725 to −24.3725 | yes: GAIN |
| response time (ms), 99th percentile | 1856 | 376.4 | −79.7% | −2953.2171 to −6.6552 | yes: GAIN |
| time over the response line (% of samples) | 16.74 | 0.4039 | −97.6% | −33.3859 to +0.7074 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 0.1667 | −98.0% | −15.3795 to −1.2871 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.17 | +89.167 (native is 0) | +76.8470 to +101.4863 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 1299 | +11788.5% | +983.8996 to +1592.5393 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0611 | 0.05871 | −3.9% | −0.0114 to +0.0066 | no |
| CPU used (cores), mean | 1.466 | 1.409 | −3.9% | −0.2726 to +0.1581 | no |
| Omni's own CPU (cores), mean | 0 | 0.06967 | +0.070 (native is 0) | +0.0577 to +0.0817 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.466 | 1.479 | +0.8% | −0.1912 to +0.2161 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.9 | 460 | +1.8% | −54.0274 to +70.3188 | no |
| HPA replicas, mean | 2.008 | 1.936 | −3.6% | −0.3701 to +0.2259 | no |
| pods started | 0.3333 | 0.1667 | −50.0% | −0.5952 to +0.2618 | no |
| pod start wait, total (s) | 0.8333 | 0.3333 | −60.0% | −1.7855 to +0.7855 | no |
| pod start wait, mean (s) | 0.4167 | 0.3333 | −20.0% | −0.2976 to +0.1309 | no |
| host CPU busy, the real machine under kind (%) | 41.49 | 47.1 | +13.5% | +0.2847 to +10.9239 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.8 | 1512 | +93.3% | +662.6178 to +797.0489 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03472 | 185.5 | +534180.0% | +107.5867 to +263.3717 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 808.8 | +242550.0% | +532.8271 to +1084.1729 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.41 | 913.9 | +922.2% | +673.7458 to +975.2681 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.33 | +13.333 (native is 0) | +4.3860 to +22.2807 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*