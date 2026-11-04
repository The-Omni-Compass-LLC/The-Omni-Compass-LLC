# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.178 | 5.053 |
| node-hours | 2.514 | 2.512 | 2.169 | 2.117 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.4 | 273.1 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.4 | 247.3 | 244 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 351.7 | 428.6 | 360 | 402.1 |
| response time (ms), 95th percentile | 1259 | 1785 | 1475 | 1891 |
| response time (ms), 99th percentile | 1707 | 2517 | 2040 | 2713 |
| time over the response line (% of samples) | 16.97 | 17.37 | 19.28 | 17.12 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 11 | 10.7 | 11.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 118.3 | 85 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.8 | 26.07 | 12.34 | 28.25 |
| utilisation (used / allocatable) | 0.06195 | 0.06276 | 0.07448 | 0.07674 |
| CPU used (cores), mean | 1.487 | 1.506 | 1.488 | 1.515 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07231 | 0.07932 |
| CPU used with Omni's own (cores), mean | 1.487 | 1.506 | 1.561 | 1.594 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 441.3 | 398.4 | 384.5 |
| HPA replicas, mean | 1.985 | 1.986 | 2.45 | 2.159 |
| pods started | 0 | 0 | 1.1 | 0.7 |
| pod start wait, total (s) | 0 | 0 | 2.4 | 1.2 |
| pod start wait, mean (s) | 0 | 0 | 1.4 | 0.6667 |
| host CPU busy, the real machine under kind (%) | 42.55 | 45.76 | 45.65 | 48.77 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 783.3 | 828.8 | 794.8 | 841.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.668 | 4.419 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1.113 | 0.1625 | 1.208 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.2 | 1 | 2.9 |
| queue: job turnaround, submitted to done, mean (s) | 89.07 | 133.1 | 101.6 | 142.5 |
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
| worker nodes in service, mean | 6 | 5.053 | −15.8% | −1.7725 to −0.1225 | yes: GAIN |
| node-hours | 2.512 | 2.117 | −15.8% | −0.7397 to −0.0518 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.8 | +0.1% | −0.6918 to +1.5001 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 244 | −10.8% | −55.1276 to −3.6516 | yes: GAIN |
| response time (ms), mean | 428.6 | 402.1 | −6.2% | −47.3453 to −5.6477 | yes: GAIN |
| response time (ms), 95th percentile | 1785 | 1891 | +5.9% | −40.9014 to +251.6724 | no |
| response time (ms), 99th percentile | 2517 | 2713 | +7.8% | −33.7604 to +426.3936 | no |
| time over the response line (% of samples) | 17.37 | 17.12 | −1.5% | −1.4834 to +0.9785 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.5 | +4.5% | −0.4079 to +1.4079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85 | +85.000 (native is 0) | +33.1853 to +136.8147 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.07 | 28.25 | +8.4% | −1.9778 to +6.3412 | no |
| utilisation (used / allocatable) | 0.06276 | 0.07674 | +22.3% | +0.0018 to +0.0262 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 1.515 | +0.6% | −0.0152 to +0.0330 | no |
| Omni's own CPU (cores), mean | 0 | 0.07932 | +0.079 (native is 0) | +0.0723 to +0.0863 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 1.594 | +5.9% | +0.0603 to +0.1161 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.3 | 384.5 | −12.9% | −104.7296 to −8.8768 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.986 | 2.159 | +8.7% | +0.0307 to +0.3157 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.1403 to +2.5403 | no |
| pod start wait, mean (s) | 0 | 0.6667 | +0.667 (native is 0) | +0.0210 to +1.3124 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.76 | 48.77 | +6.6% | +2.0442 to +3.9829 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 828.8 | 841.4 | +1.5% | +3.4881 to +21.7119 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.419 | −26.4% | −2.8340 to −0.3289 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.113 | 1.208 | +8.6% | −0.2187 to +0.4103 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 2.9 | −9.4% | −1.6081 to +1.0081 | no |
| queue: job turnaround, submitted to done, mean (s) | 133.1 | 142.5 | +7.1% | +2.4325 to +16.3425 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.512 | −0.1% | −0.0096 to +0.0060 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.4 | +0.1% | −0.5189 to +1.1894 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.4 | +0.1% | −0.5189 to +1.1894 | no |
| response time (ms), mean | 351.7 | 428.6 | +21.9% | +28.6445 to +125.1988 | yes: LOSS |
| response time (ms), 95th percentile | 1259 | 1785 | +41.8% | +205.9151 to +846.4739 | yes: LOSS |
| response time (ms), 99th percentile | 1707 | 2517 | +47.5% | +368.1188 to +1251.8112 | yes: LOSS |
| time over the response line (% of samples) | 16.97 | 17.37 | +2.3% | −2.8227 to +3.6166 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 11 | +10.0% | +0.4160 to +1.5840 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.8 | 26.06 | +141.3% | +4.7592 to +25.7642 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06195 | 0.06276 | +1.3% | −0.0004 to +0.0021 | no |
| CPU used (cores), mean | 1.487 | 1.506 | +1.3% | −0.0106 to +0.0494 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.487 | 1.506 | +1.3% | −0.0106 to +0.0494 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 441.3 | −1.0% | −14.1365 to +5.2971 | no |
| HPA replicas, mean | 1.985 | 1.986 | +0.0% | −0.1340 to +0.1353 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 42.55 | 45.76 | +7.6% | +2.5219 to +3.9038 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.3 | 828.8 | +5.8% | +19.3823 to +71.6177 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1.113 | +1807.1% | +0.6087 to +1.4996 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.2 | +540.0% | +0.5396 to +4.8604 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.07 | 133.1 | +49.4% | +21.0477 to +67.0190 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.178 | −13.7% | −1.6771 to +0.0324 | no |
| node-hours | 2.514 | 2.169 | −13.7% | −0.7009 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.1 | +0.0% | −0.5844 to +0.7520 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 247.3 | −9.4% | −52.5256 to +1.0806 | no |
| response time (ms), mean | 351.7 | 360 | +2.4% | −15.6506 to +32.3466 | no |
| response time (ms), 95th percentile | 1259 | 1475 | +17.2% | +103.5054 to +329.0326 | yes: LOSS |
| response time (ms), 99th percentile | 1707 | 2040 | +19.5% | +145.9687 to +521.1873 | yes: LOSS |
| time over the response line (% of samples) | 16.97 | 19.28 | +13.6% | −0.8013 to +5.4046 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.7 | +7.0% | +0.0214 to +1.3786 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.3 | +118.300 (native is 0) | +52.4356 to +184.1644 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.8 | 12.34 | +14.2% | −1.8364 to +4.9030 | no |
| utilisation (used / allocatable) | 0.06195 | 0.07448 | +20.2% | −0.0004 to +0.0255 | no |
| CPU used (cores), mean | 1.487 | 1.488 | +0.1% | −0.0231 to +0.0261 | no |
| Omni's own CPU (cores), mean | 0 | 0.07231 | +0.072 (native is 0) | +0.0656 to +0.0790 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.561 | +5.0% | +0.0447 to +0.1029 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 398.4 | −10.6% | −96.9261 to +2.1417 | no |
| HPA replicas, mean | 1.985 | 2.45 | +23.4% | +0.3027 to +0.6281 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.4737 to +1.7263 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.400 (native is 0) | +0.6414 to +4.1586 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.4 | +1.400 (native is 0) | +0.5436 to +2.2564 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.55 | 45.65 | +7.3% | +2.5305 to +3.6724 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.3 | 794.8 | +1.5% | +3.8236 to +19.1764 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.668 | −22.2% | −2.5500 to −0.1138 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.1625 | +178.6% | −0.0871 to +0.2954 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1 | +100.0% | −0.6802 to +1.6802 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.07 | 101.6 | +14.1% | +4.2627 to +20.7706 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.178 | −13.7% | −1.6771 to +0.0324 | no |
| node-hours | 2.512 | 2.169 | −13.7% | −0.7003 to +0.0138 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.1 | −0.1% | −1.2430 to +0.7400 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 247.3 | −9.5% | −52.7640 to +0.6485 | no |
| response time (ms), mean | 428.6 | 360 | −16.0% | −109.0498 to −28.0975 | yes: GAIN |
| response time (ms), 95th percentile | 1785 | 1475 | −17.4% | −564.5453 to −55.3057 | yes: GAIN |
| response time (ms), 99th percentile | 2517 | 2040 | −18.9% | −787.3068 to −165.4672 | yes: GAIN |
| time over the response line (% of samples) | 17.37 | 19.28 | +11.0% | −0.2075 to +4.0169 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 10.7 | −2.7% | −1.0578 to +0.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.3 | +118.300 (native is 0) | +52.4356 to +184.1644 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.07 | 12.34 | −52.7% | −22.9677 to −4.4889 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06276 | 0.07448 | +18.7% | −0.0017 to +0.0252 | no |
| CPU used (cores), mean | 1.506 | 1.488 | −1.2% | −0.0413 to +0.0055 | no |
| Omni's own CPU (cores), mean | 0 | 0.07231 | +0.072 (native is 0) | +0.0656 to +0.0790 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 1.561 | +3.6% | +0.0278 to +0.0810 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.3 | 398.4 | −9.7% | −95.8249 to +9.8800 | no |
| HPA replicas, mean | 1.986 | 2.45 | +23.4% | +0.2211 to +0.7084 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.4737 to +1.7263 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.400 (native is 0) | +0.6414 to +4.1586 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.4 | +1.400 (native is 0) | +0.5436 to +2.2564 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.76 | 45.65 | −0.2% | −0.7974 to +0.5746 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 828.8 | 794.8 | −4.1% | −55.9024 to −12.0976 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.668 | −22.2% | −2.5500 to −0.1138 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.113 | 0.1625 | −85.4% | −1.3225 to −0.5775 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 1 | −68.8% | −4.0714 to −0.3286 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 133.1 | 101.6 | −23.7% | −50.4082 to −12.6251 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.053 | −15.8% | −1.7725 to −0.1225 | yes: GAIN |
| node-hours | 2.514 | 2.117 | −15.8% | −0.7400 to −0.0552 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.8 | +0.3% | +0.1305 to +1.3484 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 244 | −10.6% | −54.8184 to −3.2902 | yes: GAIN |
| response time (ms), mean | 351.7 | 402.1 | +14.3% | +6.9678 to +93.8825 | yes: LOSS |
| response time (ms), 95th percentile | 1259 | 1891 | +50.2% | +275.6128 to +987.5472 | yes: LOSS |
| response time (ms), 99th percentile | 1707 | 2713 | +59.0% | +475.1361 to +1537.4271 | yes: LOSS |
| time over the response line (% of samples) | 16.97 | 17.12 | +0.9% | −2.9422 to +3.2311 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 11.5 | +15.0% | +0.3690 to +2.6310 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85 | +85.000 (native is 0) | +33.1853 to +136.8147 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.8 | 28.25 | +161.5% | +4.1117 to +30.7749 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06195 | 0.07674 | +23.9% | +0.0032 to +0.0264 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.515 | +1.9% | −0.0015 to +0.0580 | no |
| Omni's own CPU (cores), mean | 0 | 0.07932 | +0.079 (native is 0) | +0.0723 to +0.0863 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.594 | +7.2% | +0.0730 to +0.1422 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 384.5 | −13.7% | −105.7053 to −16.7406 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.985 | 2.159 | +8.8% | +0.0087 to +0.3390 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.1403 to +2.5403 | no |
| pod start wait, mean (s) | 0 | 0.6667 | +0.667 (native is 0) | +0.0210 to +1.3124 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.55 | 48.77 | +14.6% | +4.8241 to +7.6287 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.3 | 841.4 | +7.4% | +25.0572 to +91.1428 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.419 | −26.4% | −2.8340 to −0.3289 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1.208 | +1971.4% | +0.5838 to +1.7162 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.9 | +480.0% | +0.2620 to +4.5380 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.07 | 142.5 | +60.0% | +27.4633 to +79.3784 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*