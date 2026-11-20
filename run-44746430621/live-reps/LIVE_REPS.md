# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.354 | 5.989 |
| node-hours | 2.513 | 2.515 | 1.825 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | 271.8 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.7 | 220.1 | 270.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 313.3 | 121.1 | 314.1 | 120.6 |
| response time (ms), 95th percentile | 1118 | 217 | 1323 | 223.4 |
| response time (ms), 99th percentile | 1612 | 316.7 | 1815 | 324.3 |
| time over the response line (% of samples) | 13.56 | 0.1923 | 14.22 | 0.1802 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 0 | 7.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 164.9 | 35.56 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.16 | 1082 | 10.54 | 1180 |
| utilisation (used / allocatable) | 0.05925 | 0.05881 | 0.0816 | 0.05732 |
| CPU used (cores), mean | 1.422 | 1.411 | 1.384 | 1.373 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07273 | 0.06413 |
| CPU used with Omni's own (cores), mean | 1.422 | 1.411 | 1.457 | 1.437 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.4 | 459.5 | 379.7 | 470.7 |
| HPA replicas, mean | 1.96 | 1.968 | 2.143 | 2.07 |
| pods started | 0 | 0 | 1.2 | 0.4444 |
| pod start wait, total (s) | 0 | 0 | 2.7 | 1.222 |
| pod start wait, mean (s) | 0 | 0 | 1.3 | 0.5556 |
| host CPU busy, the real machine under kind (%) | 40.21 | 43.83 | 43.21 | 45.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 772.4 | 1404 | 783.5 | 1458 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.496 | 5.7 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 151.8 | 0.05 | 151.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 622 | 0.3 | 637.6 |
| queue: job turnaround, submitted to done, mean (s) | 79.04 | 803.2 | 88.96 | 840.1 |
| queue: jobs unfinished at the window's end | 0 | 9.9 | 0 | 10.78 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.989 | −0.2% | −0.0366 to +0.0145 | no |
| node-hours | 2.514 | 2.508 | −0.2% | −0.0150 to +0.0034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 270.9 | −0.2% | −1.7429 to +0.5062 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 270.5 | −0.4% | −2.0388 to +0.1031 | no |
| response time (ms), mean | 116.7 | 120.6 | +3.3% | −0.1759 to +7.9045 | no |
| response time (ms), 95th percentile | 210 | 223.4 | +6.4% | −0.6662 to +27.4440 | no |
| response time (ms), 99th percentile | 310.5 | 324.3 | +4.5% | −7.0754 to +34.7851 | no |
| time over the response line (% of samples) | 0.1965 | 0.1802 | −8.3% | −0.0999 to +0.0673 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.56 | +35.556 (native is 0) | +16.1625 to +54.9486 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1028 | 1180 | +14.7% | +68.5235 to +234.6247 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05878 | 0.05732 | −2.5% | −0.0032 to +0.0003 | no |
| CPU used (cores), mean | 1.411 | 1.373 | −2.7% | −0.0802 to +0.0052 | no |
| Omni's own CPU (cores), mean | 0 | 0.06413 | +0.064 (native is 0) | +0.0561 to +0.0722 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.437 | +1.9% | −0.0147 to +0.0680 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.6 | 470.7 | +2.4% | −2.1985 to +24.2583 | no |
| HPA replicas, mean | 1.969 | 2.07 | +5.1% | −0.0629 to +0.2649 | no |
| pods started | 0 | 0.4444 | +0.444 (native is 0) | −0.3348 to +1.2237 | no |
| pod start wait, total (s) | 0 | 1.222 | +1.222 (native is 0) | −1.0766 to +3.5211 | no |
| pod start wait, mean (s) | 0 | 0.5556 | +0.556 (native is 0) | −0.3133 to +1.4244 | no |
| host CPU busy, the real machine under kind (%) | 43.57 | 45.58 | +4.6% | +1.1019 to +2.9136 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1391 | 1458 | +4.8% | −8.4907 to +142.7130 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.7 | −5.0% | −4.1118 to +3.5118 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 140.9 | 151.4 | +7.5% | −23.2836 to +44.4318 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 587.1 | 637.6 | +8.6% | −65.3350 to +166.2239 | no |
| queue: job turnaround, submitted to done, mean (s) | 769.5 | 840.1 | +9.2% | +2.7091 to +138.5780 | yes: LOSS |
| queue: jobs unfinished at the window's end | 8.778 | 10.78 | +22.8% | −0.1741 to +4.1741 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.515 | +0.1% | −0.0053 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | −0.1% | −2.2942 to +1.7837 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.7 | −0.1% | −2.2942 to +1.7837 | no |
| response time (ms), mean | 313.3 | 121.1 | −61.4% | −333.1385 to −51.4212 | yes: GAIN |
| response time (ms), 95th percentile | 1118 | 217 | −80.6% | −1580.6454 to −221.7336 | yes: GAIN |
| response time (ms), 99th percentile | 1612 | 316.7 | −80.4% | −2267.3855 to −322.8757 | yes: GAIN |
| time over the response line (% of samples) | 13.56 | 0.1923 | −98.6% | −24.1540 to −2.5893 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 0 | −100.0% | −12.0128 to −1.9872 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.16 | 1082 | +10547.7% | +762.2263 to +1381.0704 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05925 | 0.05881 | −0.7% | −0.0066 to +0.0057 | no |
| CPU used (cores), mean | 1.422 | 1.411 | −0.7% | −0.1577 to +0.1364 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.422 | 1.411 | −0.7% | −0.1577 to +0.1364 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.4 | 459.5 | −1.3% | −48.7267 to +36.8648 | no |
| HPA replicas, mean | 1.96 | 1.968 | +0.5% | −0.0728 to +0.0905 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.21 | 43.83 | +9.0% | +0.1933 to +7.0400 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772.4 | 1404 | +81.7% | +553.0572 to +709.1428 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 151.8 | +331154.5% | +101.6094 to +201.9489 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 622 | +207233.3% | +462.7293 to +780.6707 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.04 | 803.2 | +916.2% | +572.0603 to +876.2147 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.9 | +9.900 (native is 0) | +3.2285 to +16.5715 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.354 | −27.4% | −2.5769 to −0.7153 | yes: GAIN |
| node-hours | 2.513 | 1.825 | −27.3% | −1.0763 to −0.2980 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 | −0.0% | −1.0120 to +0.7595 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 220.1 | −19.1% | −81.6889 to −22.0385 | yes: GAIN |
| response time (ms), mean | 313.3 | 314.1 | +0.2% | −20.4641 to +21.9654 | no |
| response time (ms), 95th percentile | 1118 | 1323 | +18.3% | +56.2738 to +352.4612 | yes: LOSS |
| response time (ms), 99th percentile | 1612 | 1815 | +12.6% | +39.5372 to +367.1856 | yes: LOSS |
| time over the response line (% of samples) | 13.56 | 14.22 | +4.8% | −0.4135 to +1.7177 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.9 | +12.9% | −0.1900 to +1.9900 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164.9 | +164.900 (native is 0) | +65.6939 to +264.1061 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.16 | 10.54 | +3.7% | −1.8013 to +2.5547 | no |
| utilisation (used / allocatable) | 0.05925 | 0.0816 | +37.7% | +0.0102 to +0.0345 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.422 | 1.384 | −2.6% | −0.0912 to +0.0160 | no |
| Omni's own CPU (cores), mean | 0 | 0.07273 | +0.073 (native is 0) | +0.0643 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.422 | 1.457 | +2.5% | −0.0247 to +0.0950 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.4 | 379.7 | −18.4% | −130.5991 to −40.8090 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.96 | 2.143 | +9.3% | −0.0066 to +0.3730 | no |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.3879 to +2.0121 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.5928 to +4.8072 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.300 (native is 0) | +0.4536 to +2.1464 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.21 | 43.21 | +7.5% | +2.3179 to +3.6861 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772.4 | 783.5 | +1.4% | +1.8873 to +20.3127 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.496 | −41.7% | −3.7483 to −1.2590 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05 | +9.1% | −0.0413 to +0.0496 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.04 | 88.96 | +12.6% | +0.9889 to +18.8528 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.354 | −27.4% | −2.5769 to −0.7153 | yes: GAIN |
| node-hours | 2.515 | 1.825 | −27.4% | −1.0768 to −0.3032 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.8 | +0.0% | −2.3652 to +2.6232 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 220.1 | −19.0% | −83.2247 to −19.9923 | yes: GAIN |
| response time (ms), mean | 121.1 | 314.1 | +159.5% | +35.7051 to +350.3559 | yes: LOSS |
| response time (ms), 95th percentile | 217 | 1323 | +509.5% | +296.9312 to +1914.1828 | yes: LOSS |
| response time (ms), 99th percentile | 316.7 | 1815 | +473.1% | +385.8803 to +2611.1037 | yes: LOSS |
| time over the response line (% of samples) | 0.1923 | 14.22 | +7293.4% | +3.3453 to +24.7022 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 7.9 | +7.900 (native is 0) | +2.7369 to +13.0631 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164.9 | +164.900 (native is 0) | +65.6939 to +264.1061 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1082 | 10.54 | −99.0% | −1380.1065 to −762.4368 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05881 | 0.0816 | +38.8% | +0.0163 to +0.0293 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.384 | −1.9% | −0.2247 to +0.1708 | no |
| Omni's own CPU (cores), mean | 0 | 0.07273 | +0.073 (native is 0) | +0.0643 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.457 | +3.2% | −0.1581 to +0.2496 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.5 | 379.7 | −17.4% | −89.5399 to −70.0063 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.968 | 2.143 | +8.9% | +0.0037 to +0.3451 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.3879 to +2.0121 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.5928 to +4.8072 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.300 (native is 0) | +0.4536 to +2.1464 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.83 | 43.21 | −1.4% | −4.5619 to +3.3327 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1404 | 783.5 | −44.2% | −694.6628 to −545.3372 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 151.8 | 0.05 | −100.0% | −201.9623 to −101.5877 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 622 | 0.3 | −100.0% | −780.8744 to −462.5256 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 803.2 | 88.96 | −88.9% | −859.3107 to −569.1226 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.9 | 0 | −100.0% | −16.5715 to −3.2285 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.989 | −0.2% | −0.0366 to +0.0145 | no |
| node-hours | 2.513 | 2.508 | −0.2% | −0.0152 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.9 | −0.3% | −3.4447 to +1.9400 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 270.5 | −0.4% | −3.6270 to +1.4232 | no |
| response time (ms), mean | 286.4 | 120.6 | −57.9% | −316.6150 to −14.9297 | yes: GAIN |
| response time (ms), 95th percentile | 1008 | 223.4 | −77.8% | −1519.5559 to −50.0985 | yes: GAIN |
| response time (ms), 99th percentile | 1449 | 324.3 | −77.6% | −2156.4607 to −92.8669 | yes: GAIN |
| time over the response line (% of samples) | 11.59 | 0.1802 | −98.4% | −22.5922 to −0.2350 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.222 | 0 | −100.0% | −11.5723 to −0.8721 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.56 | +35.556 (native is 0) | +16.1625 to +54.9486 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.706 | 1180 | +12056.6% | +880.3119 to +1460.0029 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05821 | 0.05732 | −1.5% | −0.0076 to +0.0058 | no |
| CPU used (cores), mean | 1.397 | 1.373 | −1.7% | −0.1839 to +0.1365 | no |
| Omni's own CPU (cores), mean | 0 | 0.06413 | +0.064 (native is 0) | +0.0561 to +0.0722 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.397 | 1.437 | +2.9% | −0.1123 to +0.1932 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.8 | 470.7 | −0.4% | −49.8319 to +45.5875 | no |
| HPA replicas, mean | 1.962 | 2.07 | +5.5% | −0.0743 to +0.2914 | no |
| pods started | 0 | 0.4444 | +0.444 (native is 0) | −0.3348 to +1.2237 | no |
| pod start wait, total (s) | 0 | 1.222 | +1.222 (native is 0) | −1.0766 to +3.5211 | no |
| pod start wait, mean (s) | 0 | 0.5556 | +0.556 (native is 0) | −0.3133 to +1.4244 | no |
| host CPU busy, the real machine under kind (%) | 39.41 | 45.58 | +15.6% | +2.4333 to +9.8936 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.1 | 1458 | +90.5% | +618.6418 to +766.6915 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.7 | −5.0% | −4.1118 to +3.5118 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 151.4 | +408787.5% | +111.2766 to +191.5290 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2222 | 637.6 | +286800.0% | +474.6636 to +800.0031 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 71.7 | 840.1 | +1071.7% | +648.0360 to +888.8066 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.78 | +10.778 (native is 0) | +3.7247 to +17.8309 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*