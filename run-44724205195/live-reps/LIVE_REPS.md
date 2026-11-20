# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.518 | 6 |
| node-hours | 2.513 | 2.514 | 1.896 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 287.5 | 271.2 | 287.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 287.5 | 224.6 | 287.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 258.9 | 596 | 239.9 | 609.6 |
| response time (ms), 95th percentile | 861.6 | 1236 | 927.6 | 1293 |
| response time (ms), 99th percentile | 1239 | 1646 | 1298 | 1733 |
| time over the response line (% of samples) | 7.632 | 50.21 | 8.227 | 54.07 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 24.4 | 6.7 | 24.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 165.5 | 44.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 7.5 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 2.292 | 9.647 | 2.512 |
| utilisation (used / allocatable) | 0.05577 | 0.1004 | 0.07498 | 0.09932 |
| CPU used (cores), mean | 1.339 | 2.409 | 1.33 | 2.384 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07282 | 0.04043 |
| CPU used with Omni's own (cores), mean | 1.339 | 2.409 | 1.403 | 2.424 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 285.2 | 406.9 | 287.9 |
| HPA replicas, mean | 1.96 | 2.046 | 2.214 | 2.355 |
| pods started | 0 | 0.2 | 1.2 | 0.7 |
| pod start wait, total (s) | 0 | 0.3 | 2.7 | 2.3 |
| pod start wait, mean (s) | 0 | 0.15 | 1.083 | 1.9 |
| host CPU busy, the real machine under kind (%) | 39.19 | 76.05 | 42.09 | 77.37 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 757.5 | 1480 | 762.3 | 1485 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.599 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 523.3 | 0.07083 | 567 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1075 | 0.2 | 1113 |
| queue: job turnaround, submitted to done, mean (s) | 63.15 | 914.9 | 66.47 | 948.6 |
| queue: jobs unfinished at the window's end | 0 | 12.3 | 0 | 13.2 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.514 | +0.0% | −0.0115 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 287.5 | 287.1 | −0.1% | −2.0048 to +1.2380 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.5 | 287.1 | −0.1% | −2.0048 to +1.2380 | no |
| response time (ms), mean | 596 | 609.6 | +2.3% | −37.8093 to +64.8593 | no |
| response time (ms), 95th percentile | 1236 | 1293 | +4.6% | −63.6795 to +176.4775 | no |
| response time (ms), 99th percentile | 1646 | 1733 | +5.3% | −61.3427 to +235.3177 | no |
| time over the response line (% of samples) | 50.21 | 54.07 | +7.7% | −1.4933 to +9.2030 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.4 | 24.6 | +0.8% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.5 | +44.500 (native is 0) | +38.4751 to +50.5249 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.292 | 2.512 | +9.6% | −0.1060 to +0.5460 | no |
| utilisation (used / allocatable) | 0.1004 | 0.09932 | −1.1% | −0.0026 to +0.0004 | no |
| CPU used (cores), mean | 2.409 | 2.384 | −1.1% | −0.0619 to +0.0102 | no |
| Omni's own CPU (cores), mean | 0 | 0.04043 | +0.040 (native is 0) | +0.0360 to +0.0448 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.424 | +0.6% | −0.0201 to +0.0493 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 285.2 | 287.9 | +1.0% | −0.9556 to +6.4496 | no |
| HPA replicas, mean | 2.046 | 2.355 | +15.1% | +0.0509 to +0.5663 | yes: power given |
| pods started | 0.2 | 0.7 | +250.0% | −0.2726 to +1.2726 | no |
| pod start wait, total (s) | 0.3 | 2.3 | +666.7% | −0.1326 to +4.1326 | no |
| pod start wait, mean (s) | 0.15 | 1.9 | +1166.7% | +0.3470 to +3.1530 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 76.05 | 77.37 | +1.7% | +0.6006 to +2.0528 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1480 | 1485 | +0.3% | −9.3538 to +18.7538 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 523.3 | 567 | +8.4% | −51.8218 to +139.2455 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1075 | 1113 | +3.5% | −29.9554 to +106.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 914.9 | 948.6 | +3.7% | −5.1687 to +72.5270 | no |
| queue: jobs unfinished at the window's end | 12.3 | 13.2 | +7.3% | −1.0209 to +2.8209 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.514 | +0.0% | −0.0055 to +0.0068 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 287.5 | +6.2% | +13.3574 to +20.1724 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 287.5 | +6.2% | +13.3574 to +20.1724 | yes: power given |
| response time (ms), mean | 258.9 | 596 | +130.2% | +270.9570 to +403.3705 | yes: LOSS |
| response time (ms), 95th percentile | 861.6 | 1236 | +43.5% | −202.1844 to +951.7144 | no |
| response time (ms), 99th percentile | 1239 | 1646 | +32.8% | −453.9779 to +1267.5953 | no |
| time over the response line (% of samples) | 7.632 | 50.21 | +557.9% | +34.7896 to +50.3700 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 24.4 | +369.2% | +15.4330 to +22.9670 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 2.292 | −74.8% | −10.9203 to −2.6564 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05577 | 0.1004 | +80.0% | +0.0358 to +0.0535 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.339 | 2.409 | +80.0% | +0.8584 to +1.2834 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.339 | 2.409 | +80.0% | +0.8584 to +1.2834 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 285.2 | −42.4% | −269.7855 to −150.6134 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.96 | 2.046 | +4.4% | −0.1261 to +0.2995 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.15 | +0.150 (native is 0) | −0.1893 to +0.4893 | no |
| host CPU busy, the real machine under kind (%) | 39.19 | 76.05 | +94.1% | +32.7330 to +40.9883 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 757.5 | 1480 | +95.4% | +658.4800 to +787.1200 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 523.3 | +1255877.0% | +280.1435 to +766.4206 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1075 | +537374.4% | +706.4407 to +1443.0568 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 63.15 | 914.9 | +1348.7% | +745.7440 to +957.7144 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.3 | +12.300 (native is 0) | +6.6571 to +17.9429 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.518 | −24.7% | −2.2061 to −0.7578 | yes: GAIN |
| node-hours | 2.513 | 1.896 | −24.6% | −0.9202 to −0.3155 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.2 | +0.2% | −0.1262 to +1.1616 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 224.6 | −17.0% | −69.0254 to −23.1893 | yes: GAIN |
| response time (ms), mean | 258.9 | 239.9 | −7.3% | −32.0035 to −5.9831 | yes: GAIN |
| response time (ms), 95th percentile | 861.6 | 927.6 | +7.7% | +2.1601 to +129.9429 | yes: LOSS |
| response time (ms), 99th percentile | 1239 | 1298 | +4.7% | +34.3286 to +82.9666 | yes: LOSS |
| time over the response line (% of samples) | 7.632 | 8.227 | +7.8% | +0.0207 to +1.1687 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 6.7 | +28.8% | +0.0595 to +2.9405 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 165.5 | +165.500 (native is 0) | +97.1265 to +233.8735 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 9.647 | +6.2% | −0.9042 to +2.0376 | no |
| utilisation (used / allocatable) | 0.05577 | 0.07498 | +34.4% | +0.0090 to +0.0294 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.339 | 1.33 | −0.6% | −0.0360 to +0.0194 | no |
| Omni's own CPU (cores), mean | 0 | 0.07282 | +0.073 (native is 0) | +0.0672 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.339 | 1.403 | +4.8% | +0.0337 to +0.0953 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 406.9 | −17.8% | −132.8969 to −43.9212 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.96 | 2.214 | +13.0% | +0.0403 to +0.4674 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.1444 to +2.2556 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.1531 to +5.2469 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.083 | +1.083 (native is 0) | +0.2417 to +1.9249 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.19 | 42.09 | +7.4% | +2.5105 to +3.2983 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 757.5 | 762.3 | +0.6% | −0.4758 to +10.0758 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.599 | −40.0% | −3.2915 to −1.5095 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.07083 | +70.0% | −0.0412 to +0.0995 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.15 | 66.47 | +5.3% | −1.3067 to +7.9484 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.518 | −24.7% | −2.2061 to −0.7578 | yes: GAIN |
| node-hours | 2.514 | 1.896 | −24.6% | −0.9197 to −0.3173 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 287.5 | 271.2 | −5.7% | −19.6346 to −12.8599 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.5 | 224.6 | −21.9% | −87.6308 to −38.1137 | yes: GAIN |
| response time (ms), mean | 596 | 239.9 | −59.8% | −426.6818 to −285.6323 | yes: GAIN |
| response time (ms), 95th percentile | 1236 | 927.6 | −25.0% | −908.6263 to +291.1993 | no |
| response time (ms), 99th percentile | 1646 | 1298 | −21.2% | −1210.2026 to +513.8804 | no |
| time over the response line (% of samples) | 50.21 | 8.227 | −83.6% | −49.7993 to −34.1709 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.4 | 6.7 | −72.5% | −21.0728 to −14.3272 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 165.5 | +165.500 (native is 0) | +97.1265 to +233.8735 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.292 | 9.647 | +320.9% | +3.8659 to +10.8441 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1004 | 0.07498 | −25.3% | −0.0360 to −0.0148 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.409 | 1.33 | −44.8% | −1.3038 to −0.8545 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07282 | +0.073 (native is 0) | +0.0672 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.409 | 1.403 | −41.8% | −1.2347 to −0.7779 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 285.2 | 406.9 | +42.7% | +84.4289 to +159.1519 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.046 | 2.214 | +8.2% | −0.0362 to +0.3705 | no |
| pods started | 0.2 | 1.2 | +500.0% | −0.0663 to +2.0663 | no |
| pod start wait, total (s) | 0.3 | 2.7 | +800.0% | −0.0825 to +4.8825 | no |
| pod start wait, mean (s) | 0.15 | 1.083 | +622.2% | +0.1706 to +1.6961 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 76.05 | 42.09 | −44.7% | −38.2991 to −29.6134 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1480 | 762.3 | −48.5% | −785.8675 to −650.1325 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 523.3 | 0.07083 | −100.0% | −766.3507 to −280.1551 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1075 | 0.2 | −100.0% | −1443.0142 to −706.4833 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 914.9 | 66.47 | −92.7% | −953.6157 to −743.2010 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.3 | 0 | −100.0% | −17.9429 to −6.6571 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.514 | +0.0% | −0.0059 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 287.1 | +6.1% | +12.8258 to +19.9372 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 287.1 | +6.1% | +12.8258 to +19.9372 | yes: power given |
| response time (ms), mean | 258.9 | 609.6 | +135.5% | +265.4537 to +435.9238 | yes: LOSS |
| response time (ms), 95th percentile | 861.6 | 1293 | +50.0% | −222.2552 to +1084.5832 | no |
| response time (ms), 99th percentile | 1239 | 1733 | +39.8% | −477.8000 to +1465.3924 | no |
| time over the response line (% of samples) | 7.632 | 54.07 | +608.4% | +40.7613 to +52.1080 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 24.6 | +373.1% | +15.4937 to +23.3063 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.5 | +44.500 (native is 0) | +38.4751 to +50.5249 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 2.512 | −72.3% | −10.6728 to −2.4639 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05577 | 0.09932 | +78.1% | +0.0342 to +0.0528 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.339 | 2.384 | +78.1% | +0.8217 to +1.2683 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04043 | +0.040 (native is 0) | +0.0360 to +0.0448 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.339 | 2.424 | +81.1% | +0.8656 to +1.3053 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 287.9 | −41.9% | −268.4709 to −146.4339 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.96 | 2.355 | +20.2% | +0.1499 to +0.6408 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.2172 to +1.1828 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | +0.4826 to +4.1174 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.9 | +1.900 (native is 0) | +0.6633 to +3.1367 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.19 | 77.37 | +97.5% | +33.6820 to +42.6926 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 757.5 | 1485 | +96.0% | +660.5057 to +794.4943 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 567 | +1360785.4% | +320.8031 to +813.1847 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1113 | +556410.9% | +757.4767 to +1468.1670 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 63.15 | 948.6 | +1402.1% | +784.7948 to +986.0219 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.2 | +13.200 (native is 0) | +8.0001 to +18.3999 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*