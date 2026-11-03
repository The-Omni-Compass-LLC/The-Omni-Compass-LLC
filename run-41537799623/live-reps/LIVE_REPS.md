# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.16 | 11.28 |
| node-hours | 5.029 | 5.022 | 4.677 | 4.727 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.4 | 528 | 526.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.4 | 501.8 | 504.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 771 | 986.3 | 948.1 | 1040 |
| response time (ms), 95th percentile | 3047 | 4427 | 3980 | 4584 |
| response time (ms), 99th percentile | 4117 | 5902 | 5246 | 6266 |
| time over the response line (% of samples) | 26.67 | 31.08 | 30.89 | 35.55 |
| failed requests (%) | 0 | 0.1126 | 0 | 0.264 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 17.7 | 15.7 | 17.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 118.2 | 58 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 13.33 | 20 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.42 | 37.12 | 40.69 | 84.36 |
| utilisation (used / allocatable) | 0.03652 | 0.03781 | 0.04072 | 0.03832 |
| CPU used (cores), mean | 1.753 | 1.815 | 1.81 | 1.72 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05877 | 0.0471 |
| CPU used with Omni's own (cores), mean | 1.753 | 1.815 | 1.868 | 1.767 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 709.7 | 672.5 | 708.3 |
| HPA replicas, mean | 4.267 | 4.224 | 5.099 | 5.53 |
| pods started | 0.5 | 0.1 | 3.4 | 4.4 |
| pod start wait, total (s) | 1.6 | 0.3 | 9.9 | 11.9 |
| pod start wait, mean (s) | 0.7 | 0.3 | 2.447 | 2.775 |
| host CPU busy, the real machine under kind (%) | 54.64 | 62.14 | 61.9 | 67.35 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 927.2 | 1067 | 1002 | 1113 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.56 | 10.69 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 9.988 | 0.2125 | 14.06 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 97.2 | 0.9 | 96.7 |
| queue: job turnaround, submitted to done, mean (s) | 237.2 | 365.1 | 303.5 | 421.9 |
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
| worker nodes in service, mean | 12 | 11.28 | −6.0% | −1.8112 to +0.3721 | no |
| node-hours | 5.022 | 4.727 | −5.9% | −0.7560 to +0.1675 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 526.9 | −0.1% | −2.4124 to +1.4092 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 504.4 | −4.4% | −57.5118 to +11.4252 | no |
| response time (ms), mean | 986.3 | 1040 | +5.5% | −16.0671 to +124.0892 | no |
| response time (ms), 95th percentile | 4427 | 4584 | +3.6% | −398.0470 to +712.9160 | no |
| response time (ms), 99th percentile | 5902 | 6266 | +6.2% | −566.5815 to +1294.0661 | no |
| time over the response line (% of samples) | 31.08 | 35.55 | +14.4% | +1.1109 to +7.8336 | yes: LOSS |
| failed requests (%) | 0.1126 | 0.264 | +134.6% | −0.0441 to +0.3471 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.7 | 17.5 | −1.1% | −2.7189 to +2.3189 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58 | +58.000 (native is 0) | +47.1518 to +68.8482 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 37.12 | 84.35 | +127.2% | −0.6008 to +95.0675 | no |
| utilisation (used / allocatable) | 0.03781 | 0.03832 | +1.3% | −0.0051 to +0.0061 | no |
| CPU used (cores), mean | 1.815 | 1.72 | −5.2% | −0.2742 to +0.0837 | no |
| Omni's own CPU (cores), mean | 0 | 0.0471 | +0.047 (native is 0) | +0.0389 to +0.0553 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.815 | 1.767 | −2.7% | −0.2248 to +0.1286 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 709.7 | 708.3 | −0.2% | −96.7066 to +93.9462 | no |
| HPA replicas, mean | 4.224 | 5.53 | +30.9% | +0.8242 to +1.7870 | yes: power given |
| pods started | 0.1 | 4.4 | +4300.0% | +2.9919 to +5.6081 | yes: power given |
| pod start wait, total (s) | 0.3 | 11.9 | +3866.7% | +7.6792 to +15.5208 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.775 | +824.9% | +1.4949 to +3.4546 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 62.14 | 67.35 | +8.4% | +3.4263 to +6.9923 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1067 | 1113 | +4.3% | +17.2711 to +74.9289 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.69 | −10.9% | −3.2431 to +0.6162 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 9.988 | 14.06 | +40.8% | −4.8526 to +13.0026 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 97.2 | 96.7 | −0.5% | −150.2681 to +149.2681 | no |
| queue: job turnaround, submitted to done, mean (s) | 365.1 | 421.9 | +15.6% | +26.5582 to +87.1418 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.029 | 5.022 | −0.1% | −0.0238 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.4 | +0.0% | −1.5344 to +2.0497 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.4 | +0.0% | −1.5344 to +2.0497 | no |
| response time (ms), mean | 771 | 986.3 | +27.9% | +98.4850 to +332.2098 | yes: LOSS |
| response time (ms), 95th percentile | 3047 | 4427 | +45.3% | +708.0093 to +2051.5127 | yes: LOSS |
| response time (ms), 99th percentile | 4117 | 5902 | +43.4% | +1032.8451 to +2538.0341 | yes: LOSS |
| time over the response line (% of samples) | 26.67 | 31.08 | +16.5% | +1.7704 to +7.0304 | yes: LOSS |
| failed requests (%) | 0 | 0.1126 | +0.113 (native is 0) | +0.0143 to +0.2108 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 17.7 | +34.1% | +2.0164 to +6.9836 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.42 | 37.12 | +40.5% | −2.8457 to +24.2490 | no |
| utilisation (used / allocatable) | 0.03652 | 0.03781 | +3.5% | −0.0010 to +0.0035 | no |
| CPU used (cores), mean | 1.753 | 1.815 | +3.5% | −0.0456 to +0.1691 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.753 | 1.815 | +3.5% | −0.0456 to +0.1691 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 709.7 | −2.9% | −55.4594 to +12.6034 | no |
| HPA replicas, mean | 4.267 | 4.224 | −1.0% | −0.2690 to +0.1825 | no |
| pods started | 0.5 | 0.1 | −80.0% | −1.3048 to +0.5048 | no |
| pod start wait, total (s) | 1.6 | 0.3 | −81.2% | −3.9986 to +1.3986 | no |
| pod start wait, mean (s) | 0.7 | 0.3 | −57.1% | −1.0911 to +0.2911 | no |
| host CPU busy, the real machine under kind (%) | 54.64 | 62.14 | +13.7% | +5.8510 to +9.1490 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 927.2 | 1067 | +15.1% | +87.1226 to +192.4774 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 9.988 | +7890.0% | +0.7291 to +18.9959 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 97.2 | +12050.0% | −13.4846 to +206.2846 | no |
| queue: job turnaround, submitted to done, mean (s) | 237.2 | 365.1 | +53.9% | +82.0796 to +173.6621 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.16 | −7.0% | −2.0485 to +0.3780 | no |
| node-hours | 5.029 | 4.677 | −7.0% | −0.8665 to +0.1631 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 528 | +0.2% | −2.9267 to +4.5588 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 501.8 | −4.8% | −64.8136 to +14.1415 | no |
| response time (ms), mean | 771 | 948.1 | +23.0% | +46.8265 to +307.2919 | yes: LOSS |
| response time (ms), 95th percentile | 3047 | 3980 | +30.6% | +374.9794 to +1491.3626 | yes: LOSS |
| response time (ms), 99th percentile | 4117 | 5246 | +27.4% | +405.3364 to +1854.2240 | yes: LOSS |
| time over the response line (% of samples) | 26.67 | 30.89 | +15.8% | +2.1007 to +6.3306 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 15.7 | +18.9% | +0.2824 to +4.7176 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.2 | +118.200 (native is 0) | +55.6964 to +180.7036 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.42 | 40.69 | +54.0% | −19.0836 to +47.6236 | no |
| utilisation (used / allocatable) | 0.03652 | 0.04072 | +11.5% | −0.0006 to +0.0090 | no |
| CPU used (cores), mean | 1.753 | 1.81 | +3.2% | −0.0966 to +0.2095 | no |
| Omni's own CPU (cores), mean | 0 | 0.05877 | +0.059 (native is 0) | +0.0537 to +0.0638 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.753 | 1.868 | +6.6% | −0.0399 to +0.2703 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 672.5 | −8.0% | −124.6616 to +7.4320 | no |
| HPA replicas, mean | 4.267 | 5.099 | +19.5% | +0.4222 to +1.2421 | yes: power given |
| pods started | 0.5 | 3.4 | +580.0% | +0.9791 to +4.8209 | yes: power given |
| pod start wait, total (s) | 1.6 | 9.9 | +518.8% | +3.3093 to +13.2907 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.447 | +249.5% | +0.4356 to +3.0578 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.64 | 61.9 | +13.3% | +5.4910 to +9.0110 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 927.2 | 1002 | +8.1% | +35.9676 to +114.4324 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.56 | −12.0% | −3.3381 to +0.4513 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.2125 | +70.0% | −0.0313 to +0.2063 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 237.2 | 303.5 | +27.9% | +31.3389 to +101.2028 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.16 | −7.0% | −2.0485 to +0.3780 | no |
| node-hours | 5.022 | 4.677 | −6.9% | −0.8539 to +0.1652 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 528 | +0.1% | −2.2003 to +3.3171 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 501.8 | −4.9% | −64.5196 to +13.3323 | no |
| response time (ms), mean | 986.3 | 948.1 | −3.9% | −83.5149 to +6.9384 | no |
| response time (ms), 95th percentile | 4427 | 3980 | −10.1% | −772.3550 to −120.8250 | yes: GAIN |
| response time (ms), 99th percentile | 5902 | 5246 | −11.1% | −1065.6961 to −245.6227 | yes: GAIN |
| time over the response line (% of samples) | 31.08 | 30.89 | −0.6% | −2.8146 to +2.4450 | no |
| failed requests (%) | 0.1126 | 0 | −100.0% | −0.2108 to −0.0143 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.7 | 15.7 | −11.3% | −4.3117 to +0.3117 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.2 | +118.200 (native is 0) | +55.6964 to +180.7036 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 37.12 | 40.69 | +9.6% | −32.0876 to +39.2243 | no |
| utilisation (used / allocatable) | 0.03781 | 0.04072 | +7.7% | −0.0017 to +0.0076 | no |
| CPU used (cores), mean | 1.815 | 1.81 | −0.3% | −0.1458 to +0.1351 | no |
| Omni's own CPU (cores), mean | 0 | 0.05877 | +0.059 (native is 0) | +0.0537 to +0.0638 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.815 | 1.868 | +2.9% | −0.0888 to +0.1957 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 709.7 | 672.5 | −5.2% | −97.9658 to +23.5921 | no |
| HPA replicas, mean | 4.224 | 5.099 | +20.7% | +0.3614 to +1.3894 | yes: power given |
| pods started | 0.1 | 3.4 | +3300.0% | +1.3910 to +5.2090 | yes: power given |
| pod start wait, total (s) | 0.3 | 9.9 | +3200.0% | +4.3958 to +14.8042 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.447 | +715.6% | +0.9738 to +3.3195 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 62.14 | 61.9 | −0.4% | −1.0742 to +0.5762 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1067 | 1002 | −6.1% | −83.0575 to −46.1425 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.56 | −12.0% | −3.3381 to +0.4513 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 9.988 | 0.2125 | −97.9% | −18.9037 to −0.6463 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 97.2 | 0.9 | −99.1% | −206.2336 to +13.6336 | no |
| queue: job turnaround, submitted to done, mean (s) | 365.1 | 303.5 | −16.9% | −78.0551 to −45.1449 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.28 | −6.0% | −1.8112 to +0.3721 | no |
| node-hours | 5.029 | 4.727 | −6.0% | −0.7687 to +0.1656 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 526.9 | −0.0% | −3.6070 to +3.1190 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 504.4 | −4.3% | −57.8971 to +12.3258 | no |
| response time (ms), mean | 771 | 1040 | +34.9% | +145.5542 to +393.1627 | yes: LOSS |
| response time (ms), 95th percentile | 3047 | 4584 | +50.4% | +741.0513 to +2333.3397 | yes: LOSS |
| response time (ms), 99th percentile | 4117 | 6266 | +52.2% | +1096.0770 to +3202.2868 | yes: LOSS |
| time over the response line (% of samples) | 26.67 | 35.55 | +33.3% | +4.8481 to +12.8972 | yes: LOSS |
| failed requests (%) | 0 | 0.264 | +0.264 (native is 0) | +0.0203 to +0.5078 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 17.5 | +32.6% | +1.9626 to +6.6374 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58 | +58.000 (native is 0) | +47.1518 to +68.8482 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.42 | 84.36 | +219.3% | +5.6947 to +110.1753 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03652 | 0.03832 | +4.9% | −0.0041 to +0.0077 | no |
| CPU used (cores), mean | 1.753 | 1.72 | −1.9% | −0.2372 to +0.1703 | no |
| Omni's own CPU (cores), mean | 0 | 0.0471 | +0.047 (native is 0) | +0.0389 to +0.0553 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.753 | 1.767 | +0.8% | −0.1886 to +0.2159 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.1 | 708.3 | −3.1% | −124.9844 to +79.3680 | no |
| HPA replicas, mean | 4.267 | 5.53 | +29.6% | +0.7145 to +1.8102 | yes: power given |
| pods started | 0.5 | 4.4 | +780.0% | +2.4129 to +5.3871 | yes: power given |
| pod start wait, total (s) | 1.6 | 11.9 | +643.8% | +5.4715 to +15.1285 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.775 | +296.4% | +0.6985 to +3.4510 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.64 | 67.35 | +23.3% | +10.4767 to +14.9420 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 927.2 | 1113 | +20.0% | +123.3521 to +248.4479 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.69 | −10.9% | −3.2431 to +0.6162 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 14.06 | +11150.0% | +3.9306 to +23.9444 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 96.7 | +11987.5% | −12.0987 to +203.8987 | no |
| queue: job turnaround, submitted to done, mean (s) | 237.2 | 421.9 | +77.9% | +122.9669 to +246.4747 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*