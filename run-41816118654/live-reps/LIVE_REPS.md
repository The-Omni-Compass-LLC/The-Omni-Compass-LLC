# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.26 | 5.995 |
| node-hours | 2.515 | 2.514 | 2.207 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 286.7 | 275.5 | 285.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 286.7 | 252.2 | 285.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 510 | 761.6 | 497.2 | 747 |
| response time (ms), 95th percentile | 1973 | 1513 | 2096 | 1482 |
| response time (ms), 99th percentile | 2686 | 2013 | 2882 | 1916 |
| time over the response line (% of samples) | 22.98 | 68.83 | 23.37 | 67.26 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 24.8 | 12 | 24.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 87.2 | 30.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.75 | 2.147 | 19.18 | 2.478 |
| utilisation (used / allocatable) | 0.06707 | 0.09831 | 0.07714 | 0.09657 |
| CPU used (cores), mean | 1.61 | 2.359 | 1.605 | 2.316 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07614 | 0.04488 |
| CPU used with Omni's own (cores), mean | 1.61 | 2.359 | 1.681 | 2.361 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.1 | 290.1 | 376.9 | 294.9 |
| HPA replicas, mean | 1.925 | 1.981 | 2.399 | 2.856 |
| pods started | 0 | 0 | 1.1 | 1.1 |
| pod start wait, total (s) | 0 | 0 | 2.8 | 3 |
| pod start wait, mean (s) | 0 | 0 | 1.5 | 0.95 |
| host CPU busy, the real machine under kind (%) | 45.98 | 77.13 | 49.16 | 77.64 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 839 | 1498 | 850.5 | 1483 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.697 | 5.688 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4708 | 792.5 | 0.5625 | 773.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1283 | 2.9 | 1273 |
| queue: job turnaround, submitted to done, mean (s) | 144 | 1026 | 154.5 | 1027 |
| queue: jobs unfinished at the window's end | 0 | 17.2 | 0 | 17 |
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
| worker nodes in service, mean | 6 | 5.995 | −0.1% | −0.0167 to +0.0065 | no |
| node-hours | 2.514 | 2.508 | −0.2% | −0.0152 to +0.0033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.7 | 285.6 | −0.4% | −2.2825 to +0.0798 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.7 | 285.4 | −0.4% | −2.7660 to +0.2424 | no |
| response time (ms), mean | 761.6 | 747 | −1.9% | −72.9947 to +43.8094 | no |
| response time (ms), 95th percentile | 1513 | 1482 | −2.0% | −161.4199 to +100.3439 | no |
| response time (ms), 99th percentile | 2013 | 1916 | −4.8% | −211.2964 to +18.2558 | no |
| time over the response line (% of samples) | 68.83 | 67.26 | −2.3% | −5.0747 to +1.9388 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 24.5 | −1.2% | −0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.3 | +30.300 (native is 0) | +27.2270 to +33.3730 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.147 | 2.478 | +15.5% | −0.0587 to +0.7220 | no |
| utilisation (used / allocatable) | 0.09831 | 0.09657 | −1.8% | −0.0034 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.359 | 2.316 | −1.8% | −0.0879 to +0.0007 | no |
| Omni's own CPU (cores), mean | 0 | 0.04488 | +0.045 (native is 0) | +0.0402 to +0.0496 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.359 | 2.361 | +0.1% | −0.0460 to +0.0485 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.1 | 294.9 | +1.6% | −0.1060 to +9.6745 | no |
| HPA replicas, mean | 1.981 | 2.856 | +44.1% | +0.6240 to +1.1252 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | −0.0898 to +2.2898 | no |
| pod start wait, total (s) | 0 | 3 | +3.000 (native is 0) | −0.7092 to +6.7092 | no |
| pod start wait, mean (s) | 0 | 0.95 | +0.950 (native is 0) | −0.0432 to +1.9432 | no |
| host CPU busy, the real machine under kind (%) | 77.13 | 77.64 | +0.7% | −1.0509 to +2.0762 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1498 | 1483 | −1.0% | −48.9245 to +19.1245 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.688 | −5.2% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 792.5 | 773.7 | −2.4% | −83.2620 to +45.7306 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1283 | 1273 | −0.7% | −40.2918 to +21.2777 | no |
| queue: job turnaround, submitted to done, mean (s) | 1026 | 1027 | +0.1% | −38.2124 to +40.1957 | no |
| queue: jobs unfinished at the window's end | 17.2 | 17 | −1.2% | −1.5403 to +1.1403 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.514 | −0.0% | −0.0091 to +0.0068 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 286.7 | +4.2% | +8.6803 to +14.6227 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 286.7 | +4.2% | +8.6803 to +14.6227 | yes: power given |
| response time (ms), mean | 510 | 761.6 | +49.3% | +123.4571 to +379.7657 | yes: LOSS |
| response time (ms), 95th percentile | 1973 | 1513 | −23.3% | −1250.4657 to +330.2117 | no |
| response time (ms), 99th percentile | 2686 | 2013 | −25.1% | −1781.7890 to +434.9890 | no |
| time over the response line (% of samples) | 22.98 | 68.83 | +199.6% | +40.2269 to +51.4836 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 24.8 | +110.2% | +9.3839 to +16.6161 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.75 | 2.147 | −87.9% | −24.5093 to −6.6940 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06707 | 0.09831 | +46.6% | +0.0228 to +0.0397 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 2.359 | +46.6% | +0.5474 to +0.9522 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.61 | 2.359 | +46.6% | +0.5474 to +0.9522 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.1 | 290.1 | −30.3% | −173.0762 to −79.0579 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 1.981 | +2.9% | −0.0583 to +0.1704 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 45.98 | 77.13 | +67.7% | +26.9860 to +35.3102 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 839 | 1498 | +78.6% | +597.0220 to +721.1780 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4708 | 792.5 | +168213.4% | +541.6118 to +1042.3982 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1283 | +80061.0% | +991.1651 to +1570.7881 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 144 | 1026 | +612.3% | +799.3688 to +963.7478 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 17.2 | +17.200 (native is 0) | +11.8599 to +22.5401 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.26 | −12.3% | −1.4390 to −0.0411 | yes: GAIN |
| node-hours | 2.515 | 2.207 | −12.2% | −0.6010 to −0.0146 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275.5 | +0.2% | −0.4642 to +1.4676 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 252.2 | −8.3% | −44.9064 to −0.7611 | yes: GAIN |
| response time (ms), mean | 510 | 497.2 | −2.5% | −44.9601 to +19.4121 | no |
| response time (ms), 95th percentile | 1973 | 2096 | +6.2% | −35.4024 to +280.3534 | no |
| response time (ms), 99th percentile | 2686 | 2882 | +7.3% | +36.6042 to +354.0474 | yes: LOSS |
| time over the response line (% of samples) | 22.98 | 23.37 | +1.7% | −0.9333 to +1.7299 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 12 | +1.7% | −0.6121 to +1.0121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 87.2 | +87.200 (native is 0) | +32.3797 to +142.0203 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.75 | 19.18 | +8.1% | −3.4390 to +6.3024 | no |
| utilisation (used / allocatable) | 0.06707 | 0.07714 | +15.0% | +0.0001 to +0.0200 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.605 | −0.3% | −0.0364 to +0.0265 | no |
| Omni's own CPU (cores), mean | 0 | 0.07614 | +0.076 (native is 0) | +0.0707 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.681 | +4.4% | +0.0362 to +0.1061 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.1 | 376.9 | −9.4% | −75.0008 to −3.4211 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 2.399 | +24.6% | +0.2735 to +0.6737 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | +0.6461 to +4.9539 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | +0.5463 to +2.4537 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.98 | 49.16 | +6.9% | +2.5978 to +3.7500 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 839 | 850.5 | +1.4% | +0.0439 to +22.9561 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.697 | −21.7% | −2.3753 to −0.2313 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4708 | 0.5625 | +19.5% | −0.4092 to +0.5925 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.9 | +81.3% | −0.3189 to +2.9189 | no |
| queue: job turnaround, submitted to done, mean (s) | 144 | 154.5 | +7.3% | −1.1016 to +22.0933 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.26 | −12.3% | −1.4390 to −0.0411 | yes: GAIN |
| node-hours | 2.514 | 2.207 | −12.2% | −0.5999 to −0.0133 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 286.7 | 275.5 | −3.9% | −14.1755 to −8.1241 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.7 | 252.2 | −12.0% | −59.0581 to −9.9124 | yes: GAIN |
| response time (ms), mean | 761.6 | 497.2 | −34.7% | −379.1550 to −149.6158 | yes: GAIN |
| response time (ms), 95th percentile | 1513 | 2096 | +38.5% | −216.2672 to +1381.4722 | no |
| response time (ms), 99th percentile | 2013 | 2882 | +43.2% | −295.1567 to +2032.6083 | no |
| time over the response line (% of samples) | 68.83 | 23.37 | −66.0% | −50.3004 to −40.6136 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 12 | −51.6% | −16.3494 to −9.2506 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 87.2 | +87.200 (native is 0) | +32.3797 to +142.0203 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.147 | 19.18 | +793.5% | +7.2100 to +26.8566 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09831 | 0.07714 | −21.5% | −0.0283 to −0.0140 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.359 | 1.605 | −32.0% | −0.9683 to −0.5413 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07614 | +0.076 (native is 0) | +0.0707 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.359 | 1.681 | −28.8% | −0.8969 to −0.4605 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.1 | 376.9 | +29.9% | +61.6710 to +112.0411 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.981 | 2.399 | +21.1% | +0.2915 to +0.5437 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | +0.6461 to +4.9539 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | +0.5463 to +2.4537 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 77.13 | 49.16 | −36.3% | −32.2056 to −23.7428 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1498 | 850.5 | −43.2% | −714.0155 to −581.1845 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 792.5 | 0.5625 | −99.9% | −1042.2305 to −541.5961 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1283 | 2.9 | −99.8% | −1569.0614 to −990.2918 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1026 | 154.5 | −84.9% | −950.4303 to −791.6947 | yes: GAIN |
| queue: jobs unfinished at the window's end | 17.2 | 0 | −100.0% | −22.5401 to −11.8599 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.995 | −0.1% | −0.0167 to +0.0065 | no |
| node-hours | 2.515 | 2.508 | −0.3% | −0.0170 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 285.6 | +3.8% | +7.9593 to +13.1410 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 285.4 | +3.8% | +7.8365 to +12.9429 | yes: power given |
| response time (ms), mean | 510 | 747 | +46.5% | +117.3826 to +356.6550 | yes: LOSS |
| response time (ms), 95th percentile | 1973 | 1482 | −24.9% | −1268.2154 to +286.8854 | no |
| response time (ms), 99th percentile | 2686 | 1916 | −28.7% | −1851.8600 to +312.0194 | no |
| time over the response line (% of samples) | 22.98 | 67.26 | +192.8% | +37.0138 to +51.5608 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 24.5 | +107.6% | +9.4648 to +15.9352 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.3 | +30.300 (native is 0) | +27.2270 to +33.3730 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.75 | 2.478 | −86.0% | −24.3666 to −6.1734 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06707 | 0.09657 | +44.0% | +0.0215 to +0.0375 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 2.316 | +43.9% | +0.5146 to +0.8978 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04488 | +0.045 (native is 0) | +0.0402 to +0.0496 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 2.361 | +46.7% | +0.5631 to +0.9390 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.1 | 294.9 | −29.1% | −166.5973 to −75.9681 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 2.856 | +48.3% | +0.6624 to +1.1989 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | −0.0898 to +2.2898 | no |
| pod start wait, total (s) | 0 | 3 | +3.000 (native is 0) | −0.7092 to +6.7092 | no |
| pod start wait, mean (s) | 0 | 0.95 | +0.950 (native is 0) | −0.0432 to +1.9432 | no |
| host CPU busy, the real machine under kind (%) | 45.98 | 77.64 | +68.9% | +27.7842 to +35.5374 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 839 | 1483 | +76.8% | +575.8535 to +712.5465 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.688 | −5.2% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4708 | 773.7 | +164227.8% | +548.0034 to +998.4751 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1273 | +79466.8% | +985.8935 to +1557.0456 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 144 | 1027 | +613.0% | +782.0148 to +983.0852 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 17 | +17.000 (native is 0) | +11.9196 to +22.0804 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*