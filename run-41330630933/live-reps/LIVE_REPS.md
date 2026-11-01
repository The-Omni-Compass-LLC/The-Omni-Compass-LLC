# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.85 | 11.16 |
| node-hours | 5.03 | 5.025 | 4.545 | 4.676 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 526.4 | 526.9 | 526.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 526.4 | 490.7 | 500.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 706.1 | 874.2 | 686.2 | 873.8 |
| response time (ms), 95th percentile | 2801 | 3645 | 2809 | 3695 |
| response time (ms), 99th percentile | 3659 | 4949 | 3703 | 5163 |
| time over the response line (% of samples) | 26.23 | 27.56 | 25.66 | 28.51 |
| failed requests (%) | 0.01493 | 0.1357 | 0.00722 | 0.1118 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 14.7 | 13 | 16.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 62.8 | 29.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.46 | 42.32 | 18.31 | 45.79 |
| utilisation (used / allocatable) | 0.03672 | 0.03587 | 0.04015 | 0.03907 |
| CPU used (cores), mean | 1.763 | 1.722 | 1.726 | 1.738 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01226 | 0.00984 |
| CPU used with Omni's own (cores), mean | 1.763 | 1.722 | 1.739 | 1.748 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.5 | 751.1 | 689.1 | 697.9 |
| HPA replicas, mean | 4.099 | 4.136 | 4.14 | 4.505 |
| pods started | 0.5 | 0.2 | 0.6 | 0.6 |
| pod start wait, total (s) | 1.3 | 0.2 | 0.8 | 1.1 |
| pod start wait, mean (s) | 1.05 | 0.1 | 0.8 | 0.8 |
| host CPU busy, the real machine under kind (%) | 53.39 | 59.49 | 54.34 | 61.33 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 910.1 | 1019 | 918.9 | 1040 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.19 | 10.55 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 7.296 | 0.1042 | 11.39 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 34 | 0.7 | 66.3 |
| queue: job turnaround, submitted to done, mean (s) | 214.9 | 322.7 | 222.4 | 338.8 |
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
| worker nodes in service, mean | 12 | 11.16 | −7.0% | −2.0422 to +0.3718 | no |
| node-hours | 5.025 | 4.676 | −6.9% | −0.8607 to +0.1632 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 526.8 | +0.1% | −2.7983 to +3.6187 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 500.5 | −4.9% | −64.5760 to +12.9339 | no |
| response time (ms), mean | 874.2 | 873.8 | −0.0% | −149.9622 to +149.1658 | no |
| response time (ms), 95th percentile | 3645 | 3695 | +1.4% | −637.0297 to +736.5467 | no |
| response time (ms), 99th percentile | 4949 | 5163 | +4.3% | −497.2299 to +925.4935 | no |
| time over the response line (% of samples) | 27.56 | 28.51 | +3.4% | −1.3047 to +3.1946 | no |
| failed requests (%) | 0.1357 | 0.1118 | −17.7% | −0.1232 to +0.0753 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.7 | 16.4 | +11.6% | −0.9347 to +4.3347 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.7 | +29.700 (native is 0) | +24.4215 to +34.9785 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 42.32 | 45.79 | +8.2% | −46.4888 to +53.4121 | no |
| utilisation (used / allocatable) | 0.03587 | 0.03907 | +8.9% | −0.0026 to +0.0090 | no |
| CPU used (cores), mean | 1.722 | 1.738 | +0.9% | −0.1877 to +0.2199 | no |
| Omni's own CPU (cores), mean | 0 | 0.00984 | +0.010 (native is 0) | +0.0084 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.722 | 1.748 | +1.5% | −0.1781 to +0.2299 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751.1 | 697.9 | −7.1% | −151.1319 to +44.7327 | no |
| HPA replicas, mean | 4.136 | 4.505 | +8.9% | +0.0120 to +0.7265 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | −0.4396 to +1.2396 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.3818 to +2.1818 | no |
| pod start wait, mean (s) | 0.1 | 0.8 | +700.0% | −0.1953 to +1.5953 | no |
| host CPU busy, the real machine under kind (%) | 59.49 | 61.33 | +3.1% | +0.9920 to +2.6841 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1019 | 1040 | +2.0% | +4.2665 to +36.5335 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.55 | −12.1% | −3.5066 to +0.6101 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.296 | 11.39 | +56.1% | −2.4630 to +10.6463 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34 | 66.3 | +95.0% | −40.5155 to +105.1155 | no |
| queue: job turnaround, submitted to done, mean (s) | 322.7 | 338.8 | +5.0% | −4.0355 to +36.2355 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.03 | 5.025 | −0.1% | −0.0213 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 526.4 | −0.2% | −4.1090 to +1.9387 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 526.4 | −0.2% | −4.1090 to +1.9387 | no |
| response time (ms), mean | 706.1 | 874.2 | +23.8% | +19.0068 to +317.0991 | yes: LOSS |
| response time (ms), 95th percentile | 2801 | 3645 | +30.1% | +164.2362 to +1523.5088 | yes: LOSS |
| response time (ms), 99th percentile | 3659 | 4949 | +35.3% | +650.4948 to +1929.6662 | yes: LOSS |
| time over the response line (% of samples) | 26.23 | 27.56 | +5.1% | −1.8832 to +4.5574 | no |
| failed requests (%) | 0.01493 | 0.1357 | +809.3% | −0.0633 to +0.3048 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 14.7 | +14.8% | +0.9796 to +2.8204 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.46 | 42.32 | +157.2% | −11.7208 to +63.4508 | no |
| utilisation (used / allocatable) | 0.03672 | 0.03587 | −2.3% | −0.0035 to +0.0018 | no |
| CPU used (cores), mean | 1.763 | 1.722 | −2.3% | −0.1691 to +0.0869 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.763 | 1.722 | −2.3% | −0.1691 to +0.0869 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.5 | 751.1 | +2.8% | −29.8364 to +71.1655 | no |
| HPA replicas, mean | 4.099 | 4.136 | +0.9% | −0.2330 to +0.3067 | no |
| pods started | 0.5 | 0.2 | −60.0% | −0.8889 to +0.2889 | no |
| pod start wait, total (s) | 1.3 | 0.2 | −84.6% | −2.4254 to +0.2254 | no |
| pod start wait, mean (s) | 1.05 | 0.1 | −90.5% | −1.9104 to +0.0104 | no |
| host CPU busy, the real machine under kind (%) | 53.39 | 59.49 | +11.4% | +4.4668 to +7.7280 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 910.1 | 1019 | +12.0% | +55.4927 to +163.1073 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 7.296 | +5371.9% | −2.3035 to +16.6285 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 34 | +4757.1% | −39.5155 to +106.1155 | no |
| queue: job turnaround, submitted to done, mean (s) | 214.9 | 322.7 | +50.2% | +56.0288 to +159.6462 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.85 | −9.6% | −2.6875 to +0.3899 | no |
| node-hours | 5.03 | 4.545 | −9.6% | −1.1305 to +0.1614 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 526.9 | −0.1% | −1.7990 to +0.6283 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 490.7 | −7.0% | −85.6406 to +12.0825 | no |
| response time (ms), mean | 706.1 | 686.2 | −2.8% | −57.1706 to +17.4110 | no |
| response time (ms), 95th percentile | 2801 | 2809 | +0.3% | −104.5284 to +119.7194 | no |
| response time (ms), 99th percentile | 3659 | 3703 | +1.2% | −230.9876 to +319.3030 | no |
| time over the response line (% of samples) | 26.23 | 25.66 | −2.2% | −2.3473 to +1.2072 | no |
| failed requests (%) | 0.01493 | 0.00722 | −51.6% | −0.0468 to +0.0314 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 13 | +1.6% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.8 | +62.800 (native is 0) | +22.9138 to +102.6862 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.46 | 18.31 | +11.3% | −2.5879 to +6.2979 | no |
| utilisation (used / allocatable) | 0.03672 | 0.04015 | +9.3% | −0.0012 to +0.0081 | no |
| CPU used (cores), mean | 1.763 | 1.726 | −2.1% | −0.1019 to +0.0291 | no |
| Omni's own CPU (cores), mean | 0 | 0.01226 | +0.012 (native is 0) | +0.0113 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.763 | 1.739 | −1.4% | −0.0894 to +0.0411 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.5 | 689.1 | −5.7% | −97.9285 to +15.2339 | no |
| HPA replicas, mean | 4.099 | 4.14 | +1.0% | −0.1517 to +0.2325 | no |
| pods started | 0.5 | 0.6 | +20.0% | −0.6113 to +0.8113 | no |
| pod start wait, total (s) | 1.3 | 0.8 | −38.5% | −1.9795 to +0.9795 | no |
| pod start wait, mean (s) | 1.05 | 0.8 | −23.8% | −1.3588 to +0.8588 | no |
| host CPU busy, the real machine under kind (%) | 53.39 | 54.34 | +1.8% | −0.0073 to +1.9058 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 910.1 | 918.9 | +1.0% | −5.9283 to +23.5283 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 10.19 | −15.1% | −4.1444 to +0.5223 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.1042 | −21.9% | −0.0818 to +0.0235 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 214.9 | 222.4 | +3.5% | −7.7588 to +22.8171 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.85 | −9.6% | −2.6875 to +0.3899 | no |
| node-hours | 5.025 | 4.545 | −9.5% | −1.1265 to +0.1680 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 526.9 | +0.1% | −1.8815 to +2.8812 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 490.7 | −6.8% | −84.7334 to +13.3456 | no |
| response time (ms), mean | 874.2 | 686.2 | −21.5% | −339.1104 to −36.7552 | yes: GAIN |
| response time (ms), 95th percentile | 3645 | 2809 | −22.9% | −1504.6631 to −167.8909 | yes: GAIN |
| response time (ms), 99th percentile | 4949 | 3703 | −25.2% | −1951.0333 to −540.8123 | yes: GAIN |
| time over the response line (% of samples) | 27.56 | 25.66 | −6.9% | −4.8922 to +1.0778 | no |
| failed requests (%) | 0.1357 | 0.00722 | −94.7% | −0.2923 to +0.0353 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.7 | 13 | −11.6% | −2.5294 to −0.8706 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.8 | +62.800 (native is 0) | +22.9138 to +102.6862 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 42.32 | 18.31 | −56.7% | −60.2905 to +12.2705 | no |
| utilisation (used / allocatable) | 0.03587 | 0.04015 | +12.0% | −0.0014 to +0.0100 | no |
| CPU used (cores), mean | 1.722 | 1.726 | +0.3% | −0.1514 to +0.1608 | no |
| Omni's own CPU (cores), mean | 0 | 0.01226 | +0.012 (native is 0) | +0.0113 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.722 | 1.739 | +1.0% | −0.1391 to +0.1730 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751.1 | 689.1 | −8.3% | −145.8820 to +21.8582 | no |
| HPA replicas, mean | 4.136 | 4.14 | +0.1% | −0.3458 to +0.3529 | no |
| pods started | 0.2 | 0.6 | +200.0% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.2396 to +1.4396 | no |
| pod start wait, mean (s) | 0.1 | 0.8 | +700.0% | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.49 | 54.34 | −8.7% | −6.5025 to −3.7937 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1019 | 918.9 | −9.9% | −146.5141 to −54.4859 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.19 | −15.1% | −4.1444 to +0.5223 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.296 | 0.1042 | −98.6% | −16.6798 to +2.2964 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34 | 0.7 | −97.9% | −106.1155 to +39.5155 | no |
| queue: job turnaround, submitted to done, mean (s) | 322.7 | 222.4 | −31.1% | −146.7915 to −53.8251 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.16 | −7.0% | −2.0422 to +0.3718 | no |
| node-hours | 5.03 | 4.676 | −7.0% | −0.8648 to +0.1566 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 526.8 | −0.1% | −2.6845 to +1.3346 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 500.5 | −5.1% | −65.4881 to +11.6756 | no |
| response time (ms), mean | 706.1 | 873.8 | +23.7% | +17.7095 to +317.6000 | yes: LOSS |
| response time (ms), 95th percentile | 2801 | 3695 | +31.9% | +261.9649 to +1525.2971 | yes: LOSS |
| response time (ms), 99th percentile | 3659 | 5163 | +41.1% | +820.1874 to +2188.2372 | yes: LOSS |
| time over the response line (% of samples) | 26.23 | 28.51 | +8.7% | −1.6513 to +6.2154 | no |
| failed requests (%) | 0.01493 | 0.1118 | +648.8% | −0.0698 to +0.2634 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 16.4 | +28.1% | +1.3582 to +5.8418 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.7 | +29.700 (native is 0) | +24.4215 to +34.9785 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.46 | 45.78 | +178.2% | −5.7471 to +64.4004 | no |
| utilisation (used / allocatable) | 0.03672 | 0.03907 | +6.4% | −0.0023 to +0.0070 | no |
| CPU used (cores), mean | 1.763 | 1.738 | −1.4% | −0.1584 to +0.1083 | no |
| Omni's own CPU (cores), mean | 0 | 0.00984 | +0.010 (native is 0) | +0.0084 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.763 | 1.748 | −0.9% | −0.1483 to +0.1179 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.5 | 697.9 | −4.5% | −105.7472 to +40.6771 | no |
| HPA replicas, mean | 4.099 | 4.505 | +9.9% | +0.0837 to +0.7286 | yes: power given |
| pods started | 0.5 | 0.6 | +20.0% | −0.7564 to +0.9564 | no |
| pod start wait, total (s) | 1.3 | 1.1 | −15.4% | −2.1604 to +1.7604 | no |
| pod start wait, mean (s) | 1.05 | 0.8 | −23.8% | −1.7509 to +1.2509 | no |
| host CPU busy, the real machine under kind (%) | 53.39 | 61.33 | +14.9% | +6.2172 to +9.6537 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 910.1 | 1040 | +14.3% | +72.4933 to +186.9067 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.55 | −12.1% | −3.5066 to +0.6101 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 11.39 | +8440.6% | −0.7015 to +23.2098 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 66.3 | +9371.4% | −31.4438 to +162.6438 | no |
| queue: job turnaround, submitted to done, mean (s) | 214.9 | 338.8 | +57.7% | +64.8605 to +183.0145 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*