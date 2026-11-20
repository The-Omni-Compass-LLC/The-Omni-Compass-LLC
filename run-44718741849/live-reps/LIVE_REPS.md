# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.292 | 4.416 |
| node-hours | 2.516 | 2.518 | 1.799 | 1.849 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | 270.6 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.3 | 216.9 | 221.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 257.6 | 266.9 | 231.9 | 250.4 |
| response time (ms), 95th percentile | 856.5 | 978 | 912.8 | 1064 |
| response time (ms), 99th percentile | 1200 | 1361 | 1280 | 1514 |
| time over the response line (% of samples) | 7.808 | 6.584 | 7.933 | 7.422 |
| failed requests (%) | 0 | 0 | 0 | 0.01235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 4.7 | 5.6 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 162.2 | 91.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.43 | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.482 | 19.73 | 9.468 | 22.18 |
| utilisation (used / allocatable) | 0.05559 | 0.05578 | 0.07742 | 0.07644 |
| CPU used (cores), mean | 1.334 | 1.339 | 1.309 | 1.339 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07252 | 0.07391 |
| CPU used with Omni's own (cores), mean | 1.334 | 1.339 | 1.381 | 1.413 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 501.7 | 500.7 | 400.7 | 399.2 |
| HPA replicas, mean | 1.948 | 2.026 | 2.139 | 2.042 |
| pods started | 0 | 0 | 0.7 | 0.4 |
| pod start wait, total (s) | 0 | 0 | 1.1 | 0.6 |
| pod start wait, mean (s) | 0 | 0 | 0.8 | 0.4 |
| host CPU busy, the real machine under kind (%) | 38.73 | 40.94 | 41.64 | 44.23 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 758.9 | 778.5 | 761.7 | 786.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.387 | 3.269 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 1.15 | 0.1458 | 0.9917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 3.2 | 0.9 | 3.1 |
| queue: job turnaround, submitted to done, mean (s) | 64.8 | 81.52 | 65.69 | 90.09 |
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
| worker nodes in service, mean | 6 | 4.416 | −26.4% | −2.3125 to −0.8552 | yes: GAIN |
| node-hours | 2.518 | 1.849 | −26.5% | −0.9743 to −0.3625 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 270.9 | −0.1% | −1.4545 to +0.6419 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 221.1 | −18.5% | −73.2779 to −27.0180 | yes: GAIN |
| response time (ms), mean | 266.9 | 250.4 | −6.2% | −22.5729 to −10.4050 | yes: GAIN |
| response time (ms), 95th percentile | 978 | 1064 | +8.8% | +15.0977 to +156.1323 | yes: LOSS |
| response time (ms), 99th percentile | 1361 | 1514 | +11.2% | +18.7172 to +286.8166 | yes: LOSS |
| time over the response line (% of samples) | 6.584 | 7.422 | +12.7% | −0.2311 to +1.9070 | no |
| failed requests (%) | 0 | 0.01235 | +0.012 (native is 0) | −0.0156 to +0.0403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 6.3 | +34.0% | +0.1225 to +3.0775 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.1 | +91.100 (native is 0) | +39.7987 to +142.4013 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.73 | 22.18 | +12.4% | −2.9695 to +7.8629 | no |
| utilisation (used / allocatable) | 0.05578 | 0.07644 | +37.0% | +0.0106 to +0.0307 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.339 | 1.339 | +0.0% | −0.0365 to +0.0378 | no |
| Omni's own CPU (cores), mean | 0 | 0.07391 | +0.074 (native is 0) | +0.0660 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.339 | 1.413 | +5.6% | +0.0330 to +0.1161 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.7 | 399.2 | −20.3% | −159.3593 to −43.6189 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.042 | +0.8% | −0.1395 to +0.1730 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3048 to +1.5048 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 40.94 | 44.23 | +8.0% | +2.6306 to +3.9411 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.5 | 786.6 | +1.0% | −1.9904 to +18.1904 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.269 | −45.5% | −3.8371 to −1.6246 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.15 | 0.9917 | −13.8% | −0.8095 to +0.4928 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 3.1 | −3.1% | −3.1432 to +2.9432 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.52 | 90.09 | +10.5% | +0.0577 to +17.0840 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.518 | +0.1% | −0.0015 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | +0.2% | −0.1506 to +1.0404 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.3 | +0.2% | −0.1506 to +1.0404 | no |
| response time (ms), mean | 257.6 | 266.9 | +3.6% | −16.3461 to +34.9352 | no |
| response time (ms), 95th percentile | 856.5 | 978 | +14.2% | −107.7460 to +350.6630 | no |
| response time (ms), 99th percentile | 1200 | 1361 | +13.4% | −95.4525 to +418.1475 | no |
| time over the response line (% of samples) | 7.808 | 6.584 | −15.7% | −3.0539 to +0.6073 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 4.7 | −4.1% | −1.4064 to +1.0064 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.482 | 19.73 | +108.1% | −1.2698 to +21.7765 | no |
| utilisation (used / allocatable) | 0.05559 | 0.05578 | +0.3% | −0.0012 to +0.0016 | no |
| CPU used (cores), mean | 1.334 | 1.339 | +0.3% | −0.0282 to +0.0375 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.334 | 1.339 | +0.3% | −0.0282 to +0.0375 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 501.7 | 500.7 | −0.2% | −12.5455 to +10.3648 | no |
| HPA replicas, mean | 1.948 | 2.026 | +4.0% | −0.0755 to +0.2316 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 38.73 | 40.94 | +5.7% | +1.4591 to +2.9600 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.9 | 778.5 | +2.6% | −2.7855 to +41.9855 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 1.15 | +851.7% | +0.2571 to +1.8013 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 3.2 | +1500.0% | −0.5845 to +6.5845 | no |
| queue: job turnaround, submitted to done, mean (s) | 64.8 | 81.52 | +25.8% | −1.6592 to +35.0842 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.292 | −28.5% | −2.4688 to −0.9477 | yes: GAIN |
| node-hours | 2.516 | 1.799 | −28.5% | −1.0372 to −0.3959 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.6 | −0.1% | −1.0652 to +0.6363 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 216.9 | −19.9% | −78.2523 to −29.5600 | yes: GAIN |
| response time (ms), mean | 257.6 | 231.9 | −10.0% | −37.0374 to −14.3793 | yes: GAIN |
| response time (ms), 95th percentile | 856.5 | 912.8 | +6.6% | +20.6713 to +91.9977 | yes: LOSS |
| response time (ms), 99th percentile | 1200 | 1280 | +6.7% | +5.1812 to +155.7490 | yes: LOSS |
| time over the response line (% of samples) | 7.808 | 7.933 | +1.6% | −0.6757 to +0.9261 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 5.6 | +14.3% | −0.0578 to +1.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 162.2 | +162.200 (native is 0) | +91.3330 to +233.0670 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.482 | 9.468 | −0.1% | −2.8863 to +2.8596 | no |
| utilisation (used / allocatable) | 0.05559 | 0.07742 | +39.3% | +0.0112 to +0.0325 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.334 | 1.309 | −1.9% | −0.0640 to +0.0135 | no |
| Omni's own CPU (cores), mean | 0 | 0.07252 | +0.073 (native is 0) | +0.0639 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.334 | 1.381 | +3.5% | +0.0079 to +0.0867 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 501.7 | 400.7 | −20.1% | −152.6442 to −49.3571 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.139 | +9.8% | +0.0008 to +0.3820 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | +0.1796 to +2.0204 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1647 to +1.4353 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.73 | 41.64 | +7.5% | +2.4568 to +3.3598 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.9 | 761.7 | +0.4% | −0.9670 to +6.5670 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.387 | −43.5% | −3.6536 to −1.5723 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.1458 | +20.7% | −0.1455 to +0.1955 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.9 | +350.0% | −0.6509 to +2.0509 | no |
| queue: job turnaround, submitted to done, mean (s) | 64.8 | 65.69 | +1.4% | −3.1478 to +4.9228 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.292 | −28.5% | −2.4688 to −0.9477 | yes: GAIN |
| node-hours | 2.518 | 1.799 | −28.5% | −1.0385 to −0.3982 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 270.6 | −0.2% | −1.5052 to +0.1865 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 216.9 | −20.0% | −78.5962 to −30.1058 | yes: GAIN |
| response time (ms), mean | 266.9 | 231.9 | −13.1% | −67.6417 to −2.3641 | yes: GAIN |
| response time (ms), 95th percentile | 978 | 912.8 | −6.7% | −266.3758 to +136.1278 | no |
| response time (ms), 99th percentile | 1361 | 1280 | −5.9% | −269.0909 to +107.3261 | no |
| time over the response line (% of samples) | 6.584 | 7.933 | +20.5% | +0.0960 to +2.6009 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 5.6 | +19.1% | −0.6249 to +2.4249 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 162.2 | +162.200 (native is 0) | +91.3330 to +233.0670 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.73 | 9.468 | −52.0% | −20.2272 to −0.3062 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05578 | 0.07742 | +38.8% | +0.0105 to +0.0327 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.339 | 1.309 | −2.2% | −0.0554 to −0.0044 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07252 | +0.073 (native is 0) | +0.0639 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.339 | 1.381 | +3.2% | +0.0146 to +0.0706 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.7 | 400.7 | −20.0% | −155.7307 to −44.0898 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.139 | +5.6% | −0.0173 to +0.2440 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | +0.1796 to +2.0204 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1647 to +1.4353 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.94 | 41.64 | +1.7% | −0.2022 to +1.5997 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.5 | 761.7 | −2.2% | −39.2226 to +5.6226 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.387 | −43.5% | −3.6536 to −1.5723 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.15 | 0.1458 | −87.3% | −1.6673 to −0.3411 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 0.9 | −71.9% | −4.6129 to +0.0129 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.52 | 65.69 | −19.4% | −33.3973 to +1.7473 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.416 | −26.4% | −2.3125 to −0.8552 | yes: GAIN |
| node-hours | 2.516 | 1.849 | −26.5% | −0.9733 to −0.3598 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.9 | +0.0% | −0.8042 to +0.8813 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 221.1 | −18.4% | −72.8207 to −26.5854 | yes: GAIN |
| response time (ms), mean | 257.6 | 250.4 | −2.8% | −31.3795 to +16.9908 | no |
| response time (ms), 95th percentile | 856.5 | 1064 | +24.2% | −72.9923 to +487.1393 | no |
| response time (ms), 99th percentile | 1200 | 1514 | +26.2% | −44.3965 to +672.6253 | no |
| time over the response line (% of samples) | 7.808 | 7.422 | −4.9% | −2.8016 to +2.0310 | no |
| failed requests (%) | 0 | 0.01235 | +0.012 (native is 0) | −0.0156 to +0.0403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 6.3 | +28.6% | −0.5134 to +3.3134 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.1 | +91.100 (native is 0) | +39.7987 to +142.4013 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.482 | 22.18 | +133.9% | −0.7649 to +26.1649 | no |
| utilisation (used / allocatable) | 0.05559 | 0.07644 | +37.5% | +0.0109 to +0.0308 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.334 | 1.339 | +0.4% | −0.0279 to +0.0385 | no |
| Omni's own CPU (cores), mean | 0 | 0.07391 | +0.074 (native is 0) | +0.0660 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.334 | 1.413 | +5.9% | +0.0430 to +0.1155 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 501.7 | 399.2 | −20.4% | −158.1895 to −46.9694 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.042 | +4.9% | −0.0975 to +0.2872 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3048 to +1.5048 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 38.73 | 44.23 | +14.2% | +4.4512 to +6.5397 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.9 | 786.6 | +3.7% | −2.0138 to +57.4138 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.269 | −45.5% | −3.8371 to −1.6246 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.9917 | +720.7% | +0.5364 to +1.2052 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 3.1 | +1450.0% | −0.0866 to +5.8866 | no |
| queue: job turnaround, submitted to done, mean (s) | 64.8 | 90.09 | +39.0% | +0.8892 to +49.6775 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*