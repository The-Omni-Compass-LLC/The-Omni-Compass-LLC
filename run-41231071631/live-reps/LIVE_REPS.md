# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.662 | 6 |
| node-hours | 2.512 | 2.518 | 2.374 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 272.6 | 274.6 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 272.6 | 264 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 483.6 | 153.8 | 441.4 | 116.3 |
| response time (ms), 95th percentile | 1843 | 270.7 | 1853 | 256.9 |
| response time (ms), 99th percentile | 2567 | 389.9 | 2652 | 389.1 |
| time over the response line (% of samples) | 22.83 | 0.3249 | 22.87 | 0.293 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0.2 | 12.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 29.3 | 14.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.3 | 1351 | 12.22 | 1368 |
| utilisation (used / allocatable) | 0.06548 | 0.06015 | 0.06945 | 0.06033 |
| CPU used (cores), mean | 1.572 | 1.443 | 1.571 | 1.448 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01666 | 0.0129 |
| CPU used with Omni's own (cores), mean | 1.572 | 1.443 | 1.587 | 1.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.9 | 450.3 | 404.1 | 449.2 |
| HPA replicas, mean | 1.966 | 2.056 | 2.111 | 2.115 |
| pods started | 0 | 0.1 | 0.4 | 0.2 |
| pod start wait, total (s) | 0 | 0.1 | 0.5 | 0.2 |
| pod start wait, mean (s) | 0 | 0.1 | 0.5 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.9 | 46.22 | 45.71 | 46.6 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 818.5 | 1512 | 820.4 | 1505 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 5.345 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 172.4 | 0.1083 | 157.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 932.4 | 0.6 | 805 |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 966 | 127.7 | 948.4 |
| queue: jobs unfinished at the window's end | 0 | 14.6 | 0 | 15.4 |

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
| node-hours | 2.518 | 2.508 | −0.4% | −0.0163 to −0.0037 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.6 | −0.4% | −1.7660 to −0.1581 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.6 | −0.4% | −1.7660 to −0.1581 | yes: GAIN |
| response time (ms), mean | 153.8 | 116.3 | −24.4% | −40.4504 to −34.6087 | yes: GAIN |
| response time (ms), 95th percentile | 270.7 | 256.9 | −5.1% | −28.1910 to +0.6260 | no |
| response time (ms), 99th percentile | 389.9 | 389.1 | −0.2% | −27.4038 to +25.8940 | no |
| time over the response line (% of samples) | 0.3249 | 0.293 | −9.8% | −0.1932 to +0.1293 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 | +14.100 (native is 0) | +9.0257 to +19.1743 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1351 | 1368 | +1.2% | −12.8545 to +46.5312 | no |
| utilisation (used / allocatable) | 0.06015 | 0.06033 | +0.3% | −0.0015 to +0.0018 | no |
| CPU used (cores), mean | 1.443 | 1.448 | +0.3% | −0.0350 to +0.0439 | no |
| Omni's own CPU (cores), mean | 0 | 0.0129 | +0.013 (native is 0) | +0.0118 to +0.0140 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.461 | +1.2% | −0.0224 to +0.0571 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.3 | 449.2 | −0.2% | −12.2777 to +10.1014 | no |
| HPA replicas, mean | 2.056 | 2.115 | +2.9% | −0.1524 to +0.2714 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, mean (s) | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| host CPU busy, the real machine under kind (%) | 46.22 | 46.6 | +0.8% | −0.4337 to +1.2114 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1512 | 1505 | −0.4% | −10.1439 to −2.2561 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 172.4 | 157.7 | −8.5% | −52.6277 to +23.2777 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 932.4 | 805 | −13.7% | −354.8945 to +100.0945 | no |
| queue: job turnaround, submitted to done, mean (s) | 966 | 948.4 | −1.8% | −43.5642 to +8.3808 | no |
| queue: jobs unfinished at the window's end | 14.6 | 15.4 | +5.5% | −1.1604 to +2.7604 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.518 | +0.2% | −0.0026 to +0.0142 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 272.6 | −0.6% | −3.7542 to +0.5641 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 272.6 | −0.6% | −3.7542 to +0.5641 | no |
| response time (ms), mean | 483.6 | 153.8 | −68.2% | −479.7958 to −179.8541 | yes: GAIN |
| response time (ms), 95th percentile | 1843 | 270.7 | −85.3% | −2290.7321 to −854.5069 | yes: GAIN |
| response time (ms), 99th percentile | 2567 | 389.9 | −84.8% | −3168.1933 to −1187.0293 | yes: GAIN |
| time over the response line (% of samples) | 22.83 | 0.3249 | −98.6% | −32.6892 to −12.3273 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0.2 | −98.3% | −14.6942 to −8.5058 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.3 | 1351 | +10881.6% | +1168.4187 to +1508.4646 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06548 | 0.06015 | −8.1% | −0.0115 to +0.0008 | no |
| CPU used (cores), mean | 1.572 | 1.443 | −8.1% | −0.2759 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.572 | 1.443 | −8.1% | −0.2759 to +0.0198 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.9 | 450.3 | +6.2% | −14.9665 to +67.6767 | no |
| HPA replicas, mean | 1.966 | 2.056 | +4.6% | −0.0119 to +0.1909 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 44.9 | 46.22 | +2.9% | −2.1266 to +4.7489 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818.5 | 1512 | +84.7% | +644.2074 to +741.7926 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 172.4 | +125290.9% | +142.1333 to +202.4167 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 932.4 | +77600.0% | +752.3749 to +1110.0251 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 966 | +671.9% | +791.8569 to +889.8431 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.6 | +14.600 (native is 0) | +9.4728 to +19.7272 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.662 | −5.6% | −0.8446 to +0.1694 | no |
| node-hours | 2.512 | 2.374 | −5.5% | −0.3495 to +0.0733 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.6 | +0.2% | −0.5967 to +1.4196 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 264 | −3.7% | −26.0992 to +5.6846 | no |
| response time (ms), mean | 483.6 | 441.4 | −8.7% | −64.3591 to −20.1557 | yes: GAIN |
| response time (ms), 95th percentile | 1843 | 1853 | +0.5% | −117.2410 to +135.7170 | no |
| response time (ms), 99th percentile | 2567 | 2652 | +3.3% | −122.5303 to +291.1809 | no |
| time over the response line (% of samples) | 22.83 | 22.87 | +0.2% | −0.6657 to +0.7407 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 12.1 | +2.5% | −0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 | +29.300 (native is 0) | +14.3981 to +44.2019 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.3 | 12.22 | −0.7% | −2.5175 to +2.3575 | no |
| utilisation (used / allocatable) | 0.06548 | 0.06945 | +6.1% | −0.0017 to +0.0097 | no |
| CPU used (cores), mean | 1.572 | 1.571 | −0.0% | −0.0199 to +0.0184 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.017 (native is 0) | +0.0155 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.572 | 1.587 | +1.0% | −0.0031 to +0.0349 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.9 | 404.1 | −4.7% | −48.1960 to +8.5478 | no |
| HPA replicas, mean | 1.966 | 2.111 | +7.3% | −0.0886 to +0.3774 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| host CPU busy, the real machine under kind (%) | 44.9 | 45.71 | +1.8% | +0.3998 to +1.2027 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818.5 | 820.4 | +0.2% | −5.8515 to +9.6515 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.345 | −10.9% | −1.6282 to +0.3182 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.1083 | −21.2% | −0.0607 to +0.0024 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.6 | −50.0% | −1.2911 to +0.0911 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 127.7 | +2.0% | −6.3854 to +11.4437 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.662 | −5.6% | −0.8446 to +0.1694 | no |
| node-hours | 2.518 | 2.374 | −5.7% | −0.3549 to +0.0670 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 274.6 | +0.7% | −0.1654 to +4.1784 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 264 | −3.2% | −26.2422 to +9.0177 | no |
| response time (ms), mean | 153.8 | 441.4 | +187.0% | +142.0203 to +433.1148 | yes: LOSS |
| response time (ms), 95th percentile | 270.7 | 1853 | +584.3% | +872.7408 to +2290.9742 | yes: LOSS |
| response time (ms), 99th percentile | 389.9 | 2652 | +580.2% | +1241.8849 to +3281.9883 | yes: LOSS |
| time over the response line (% of samples) | 0.3249 | 22.87 | +6939.0% | +12.4384 to +32.6532 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 12.1 | +5950.0% | +8.8382 to +14.9618 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 | +29.300 (native is 0) | +14.3981 to +44.2019 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1351 | 12.22 | −99.1% | −1508.4002 to −1168.6431 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06015 | 0.06945 | +15.5% | +0.0058 to +0.0128 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.571 | +8.8% | −0.0258 to +0.2804 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.017 (native is 0) | +0.0155 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.587 | +10.0% | −0.0094 to +0.2974 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.3 | 404.1 | −10.3% | −68.4731 to −23.8853 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.056 | 2.111 | +2.7% | −0.1400 to +0.2498 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 46.22 | 45.71 | −1.1% | −3.8294 to +2.8097 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1512 | 820.4 | −45.7% | −739.8686 to −642.3314 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 172.4 | 0.1083 | −99.9% | −202.4604 to −142.1479 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 932.4 | 0.6 | −99.9% | −1110.6773 to −752.9227 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 966 | 127.7 | −86.8% | −883.1815 to −793.4601 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.6 | 0 | −100.0% | −19.7272 to −9.4728 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.508 | −0.2% | −0.0115 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 271.6 | −0.9% | −4.8486 to −0.2656 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 271.6 | −0.9% | −4.8486 to −0.2656 | yes: GAIN |
| response time (ms), mean | 483.6 | 116.3 | −76.0% | −517.5025 to −217.2066 | yes: GAIN |
| response time (ms), 95th percentile | 1843 | 256.9 | −86.1% | −2293.9072 to −878.8968 | yes: GAIN |
| response time (ms), 99th percentile | 2567 | 389.1 | −84.8% | −3155.4581 to −1201.2743 | yes: GAIN |
| time over the response line (% of samples) | 22.83 | 0.293 | −98.7% | −32.6701 to −12.4103 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0.1 | −99.2% | −14.7914 to −8.6086 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 | +14.100 (native is 0) | +9.0257 to +19.1743 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.3 | 1368 | +11018.5% | +1184.3091 to +1526.2509 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06548 | 0.06033 | −7.9% | −0.0107 to +0.0004 | no |
| CPU used (cores), mean | 1.572 | 1.448 | −7.9% | −0.2577 to +0.0105 | no |
| Omni's own CPU (cores), mean | 0 | 0.0129 | +0.013 (native is 0) | +0.0118 to +0.0140 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.572 | 1.461 | −7.0% | −0.2438 to +0.0224 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.9 | 449.2 | +6.0% | −11.5556 to +62.0895 | no |
| HPA replicas, mean | 1.966 | 2.115 | +7.6% | −0.0197 to +0.3177 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 44.9 | 46.6 | +3.8% | −1.3450 to +4.7449 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818.5 | 1505 | +83.9% | +636.0196 to +737.5804 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 157.7 | +114618.2% | +126.1642 to +189.0358 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 805 | +66983.3% | +619.0682 to +988.5318 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 948.4 | +657.9% | +781.9909 to +864.5258 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.4 | +15.400 (native is 0) | +10.8609 to +19.9391 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*