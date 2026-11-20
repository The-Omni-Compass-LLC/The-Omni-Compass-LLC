# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.484 | 6 |
| node-hours | 2.518 | 2.516 | 1.881 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.9 | 271 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.9 | 223.3 | 271 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 241.6 | 125.7 | 220.4 | 129.5 |
| response time (ms), 95th percentile | 758 | 218.6 | 873.5 | 232.3 |
| response time (ms), 99th percentile | 1093 | 324.4 | 1241 | 339 |
| time over the response line (% of samples) | 7.912 | 0.13 | 8.232 | 0.1987 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 0 | 8.5 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 198.5 | 26.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 8.333 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.003 | 1066 | 8.963 | 1158 |
| utilisation (used / allocatable) | 0.05515 | 0.05912 | 0.07471 | 0.05825 |
| CPU used (cores), mean | 1.324 | 1.419 | 1.312 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07739 | 0.06584 |
| CPU used with Omni's own (cores), mean | 1.324 | 1.419 | 1.39 | 1.464 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 457.4 | 407.2 | 463.7 |
| HPA replicas, mean | 1.938 | 2.03 | 2.238 | 2.104 |
| pods started | 0.1 | 0 | 1.1 | 0.7 |
| pod start wait, total (s) | 0.1 | 0 | 2.7 | 1.4 |
| pod start wait, mean (s) | 0.1 | 0 | 1.533 | 0.55 |
| host CPU busy, the real machine under kind (%) | 38.77 | 44.8 | 42.18 | 46.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 750 | 1484 | 751.5 | 1507 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.493 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 143.8 | 0.02917 | 152.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 651.6 | 0.1 | 636 |
| queue: job turnaround, submitted to done, mean (s) | 55.29 | 797.3 | 57.65 | 839.8 |
| queue: jobs unfinished at the window's end | 0 | 8.8 | 0 | 10.2 |
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
| node-hours | 2.516 | 2.51 | −0.2% | −0.0146 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271 | −0.3% | −1.6419 to −0.1442 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271 | −0.3% | −1.6419 to −0.1442 | yes: GAIN |
| response time (ms), mean | 125.7 | 129.5 | +3.0% | +1.8010 to +5.7099 | yes: LOSS |
| response time (ms), 95th percentile | 218.6 | 232.3 | +6.3% | +2.0897 to +25.3683 | yes: LOSS |
| response time (ms), 99th percentile | 324.4 | 339 | +4.5% | −21.0689 to +50.1405 | no |
| time over the response line (% of samples) | 0.13 | 0.1987 | +52.8% | −0.0959 to +0.2333 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 | +26.300 (native is 0) | +18.4493 to +34.1507 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1066 | 1158 | +8.7% | −38.3537 to +223.9803 | no |
| utilisation (used / allocatable) | 0.05912 | 0.05825 | −1.5% | −0.0025 to +0.0008 | no |
| CPU used (cores), mean | 1.419 | 1.398 | −1.5% | −0.0605 to +0.0189 | no |
| Omni's own CPU (cores), mean | 0 | 0.06584 | +0.066 (native is 0) | +0.0602 to +0.0715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.464 | +3.2% | +0.0037 to +0.0865 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.4 | 463.7 | +1.4% | −5.6288 to +18.2099 | no |
| HPA replicas, mean | 2.03 | 2.104 | +3.6% | −0.0940 to +0.2418 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | −0.6006 to +3.4006 | no |
| pod start wait, mean (s) | 0 | 0.55 | +0.550 (native is 0) | −0.1338 to +1.2338 | no |
| host CPU busy, the real machine under kind (%) | 44.8 | 46.75 | +4.4% | +1.1798 to +2.7356 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1484 | 1507 | +1.6% | −29.2177 to +75.6177 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 143.8 | 152.8 | +6.3% | −43.1401 to +61.1317 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 651.6 | 636 | −2.4% | −214.4131 to +183.2131 | no |
| queue: job turnaround, submitted to done, mean (s) | 797.3 | 839.8 | +5.3% | −37.6272 to +122.5772 | no |
| queue: jobs unfinished at the window's end | 8.8 | 10.2 | +15.9% | −2.3579 to +5.1579 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.515 | −0.1% | −0.0115 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.9 | +0.3% | −1.6088 to +3.4564 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.9 | +0.3% | −1.6088 to +3.4564 | no |
| response time (ms), mean | 241.6 | 125.7 | −48.0% | −235.4090 to +3.6072 | no |
| response time (ms), 95th percentile | 758 | 218.6 | −71.2% | −1091.7895 to +12.9785 | no |
| response time (ms), 99th percentile | 1093 | 324.4 | −70.3% | −1571.3074 to +34.7750 | no |
| time over the response line (% of samples) | 7.912 | 0.13 | −98.4% | −16.8483 to +1.2837 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 0 | −100.0% | −9.8598 to −2.5402 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.003 | 1066 | +15116.3% | +839.1601 to +1278.1299 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05515 | 0.05912 | +7.2% | −0.0019 to +0.0098 | no |
| CPU used (cores), mean | 1.324 | 1.419 | +7.2% | −0.0453 to +0.2356 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.324 | 1.419 | +7.2% | −0.0453 to +0.2356 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 457.4 | −7.8% | −80.2711 to +3.2817 | no |
| HPA replicas, mean | 1.938 | 2.03 | +4.7% | −0.1207 to +0.3038 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 38.77 | 44.8 | +15.6% | +3.1827 to +8.8758 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750 | 1484 | +97.8% | +676.0636 to +791.3364 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 143.8 | +344930.0% | +111.5657 to +175.8760 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 651.6 | +325700.0% | +565.5643 to +737.2357 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.29 | 797.3 | +1342.1% | +638.2591 to +845.7575 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.8 | +8.800 (native is 0) | +3.7555 to +13.8445 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.484 | −25.3% | −2.2101 to −0.8216 | yes: GAIN |
| node-hours | 2.518 | 1.881 | −25.3% | −0.9264 to −0.3482 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271 | +0.0% | −1.1016 to +1.1561 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 223.3 | −17.6% | −69.2932 to −26.1190 | yes: GAIN |
| response time (ms), mean | 241.6 | 220.4 | −8.8% | −26.5658 to −15.9981 | yes: GAIN |
| response time (ms), 95th percentile | 758 | 873.5 | +15.2% | +3.4960 to +227.4740 | yes: LOSS |
| response time (ms), 99th percentile | 1093 | 1241 | +13.5% | +14.3174 to +281.3236 | yes: LOSS |
| time over the response line (% of samples) | 7.912 | 8.232 | +4.0% | −0.7238 to +1.3634 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 8.5 | +37.1% | +0.8674 to +3.7326 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 198.5 | +198.500 (native is 0) | +123.0629 to +273.9371 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.003 | 8.963 | +28.0% | +0.3013 to +3.6187 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05515 | 0.07471 | +35.5% | +0.0091 to +0.0300 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.324 | 1.312 | −0.8% | −0.0343 to +0.0118 | no |
| Omni's own CPU (cores), mean | 0 | 0.07739 | +0.077 (native is 0) | +0.0712 to +0.0836 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.324 | 1.39 | +5.0% | +0.0431 to +0.0892 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 407.2 | −17.9% | −132.5852 to −44.8900 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.938 | 2.238 | +15.5% | +0.0224 to +0.5771 | yes: power given |
| pods started | 0.1 | 1.1 | +1000.0% | +0.0463 to +1.9537 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.7 | +2600.0% | +0.5159 to +4.6841 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.533 | +1433.3% | +0.3433 to +2.5234 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.77 | 42.18 | +8.8% | +3.0565 to +3.7619 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750 | 751.5 | +0.2% | −1.5767 to +4.5767 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.493 | −41.8% | −3.5296 to −1.4852 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.02917 | −30.0% | −0.0408 to +0.0158 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.1 | −50.0% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.29 | 57.65 | +4.3% | +0.1362 to +4.5805 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.484 | −25.3% | −2.2101 to −0.8216 | yes: GAIN |
| node-hours | 2.516 | 1.881 | −25.2% | −0.9243 to −0.3445 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271 | −0.3% | −2.9230 to +1.1299 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 223.3 | −17.9% | −71.9228 to −25.3371 | yes: GAIN |
| response time (ms), mean | 125.7 | 220.4 | +75.3% | −25.9165 to +215.1543 | no |
| response time (ms), 95th percentile | 218.6 | 873.5 | +299.6% | −6.8875 to +1316.6685 | no |
| response time (ms), 99th percentile | 324.4 | 1241 | +282.4% | −16.0673 to +1848.2407 | no |
| time over the response line (% of samples) | 0.13 | 8.232 | +6231.2% | −0.0163 to +16.2205 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.5 | +8.500 (native is 0) | +5.1576 to +11.8424 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 198.5 | +198.500 (native is 0) | +123.0629 to +273.9371 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1066 | 8.963 | −99.2% | −1275.6362 to −837.7338 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05912 | 0.07471 | +26.4% | +0.0080 to +0.0232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.312 | −7.5% | −0.2533 to +0.0404 | no |
| Omni's own CPU (cores), mean | 0 | 0.07739 | +0.077 (native is 0) | +0.0712 to +0.0836 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.39 | −2.0% | −0.1771 to +0.1190 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.4 | 407.2 | −11.0% | −76.6178 to −23.8680 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.03 | 2.238 | +10.3% | −0.0091 to +0.4256 | no |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.2436 to +1.9564 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.7037 to +4.6963 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.533 | +1.533 (native is 0) | +0.5522 to +2.5145 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.8 | 42.18 | −5.8% | −5.4232 to +0.1832 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1484 | 751.5 | −49.3% | −790.8531 to −673.5469 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.153 | −64.1% | −5.7917 to −1.9021 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 143.8 | 0.02917 | −100.0% | −175.9039 to −111.5628 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 651.6 | 0.1 | −100.0% | −737.3595 to −565.6405 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 797.3 | 57.65 | −92.8% | −842.3500 to −636.9500 | yes: GAIN |
| queue: jobs unfinished at the window's end | 8.8 | 0 | −100.0% | −13.8445 to −3.7555 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.51 | −0.3% | −0.0168 to −0.0005 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271 | +0.0% | −2.0724 to +2.1339 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271 | +0.0% | −2.0724 to +2.1339 | no |
| response time (ms), mean | 241.6 | 129.5 | −46.4% | −230.8894 to +6.5985 | no |
| response time (ms), 95th percentile | 758 | 232.3 | −69.4% | −1074.3102 to +22.9572 | no |
| response time (ms), 99th percentile | 1093 | 339 | −69.0% | −1560.2314 to +52.7706 | no |
| time over the response line (% of samples) | 7.912 | 0.1987 | −97.5% | −16.7616 to +1.3344 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 0.1 | −98.4% | −9.7544 to −2.4456 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 | +26.300 (native is 0) | +18.4493 to +34.1507 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.003 | 1158 | +16441.6% | +981.1125 to +1321.8042 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05515 | 0.05825 | +5.6% | −0.0023 to +0.0085 | no |
| CPU used (cores), mean | 1.324 | 1.398 | +5.6% | −0.0562 to +0.2051 | no |
| Omni's own CPU (cores), mean | 0 | 0.06584 | +0.066 (native is 0) | +0.0602 to +0.0715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.324 | 1.464 | +10.6% | +0.0143 to +0.2662 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 463.7 | −6.5% | −71.2708 to +6.8625 | no |
| HPA replicas, mean | 1.938 | 2.104 | +8.5% | −0.0438 to +0.3747 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.4228 to +1.6228 | no |
| pod start wait, total (s) | 0.1 | 1.4 | +1300.0% | −0.7525 to +3.3525 | no |
| pod start wait, mean (s) | 0.1 | 0.55 | +450.0% | −0.3124 to +1.2124 | no |
| host CPU busy, the real machine under kind (%) | 38.77 | 46.75 | +20.6% | +5.2052 to +10.7687 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750 | 1507 | +100.9% | +717.9138 to +795.8862 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 152.8 | +366520.0% | +121.1907 to +184.2427 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 636 | +317900.0% | +472.9054 to +798.6946 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.29 | 839.8 | +1418.9% | +724.1433 to +844.8233 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.2 | +10.200 (native is 0) | +6.5558 to +13.8442 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*