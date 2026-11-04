# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.136 | 5.201 |
| node-hours | 2.514 | 2.51 | 2.148 | 2.177 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 273.8 | 274 | 274.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 273.8 | 246.9 | 249.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 466.7 | 373.3 | 450.4 | 423.3 |
| response time (ms), 95th percentile | 1741 | 1570 | 1923 | 2085 |
| response time (ms), 99th percentile | 2437 | 2506 | 2660 | 2953 |
| time over the response line (% of samples) | 20.93 | 14.27 | 20.38 | 16.28 |
| failed requests (%) | 0 | 0 | 0.02312 | 0.01156 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 9.3 | 10.9 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 95.4 | 101.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 53.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.97 | 16.57 | 14.23 | 24.34 |
| utilisation (used / allocatable) | 0.06509 | 0.06491 | 0.07731 | 0.07742 |
| CPU used (cores), mean | 1.562 | 1.558 | 1.573 | 1.593 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07485 | 0.07779 |
| CPU used with Omni's own (cores), mean | 1.562 | 1.558 | 1.647 | 1.671 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.5 | 431.8 | 377.1 | 375.6 |
| HPA replicas, mean | 1.942 | 2.087 | 2.361 | 2.322 |
| pods started | 0 | 0 | 1.6 | 0.8 |
| pod start wait, total (s) | 0 | 0 | 4.6 | 2.1 |
| pod start wait, mean (s) | 0 | 0 | 1.567 | 0.9667 |
| host CPU busy, the real machine under kind (%) | 44.42 | 45.36 | 47.88 | 49.23 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 822.4 | 833.9 | 835.4 | 852.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.469 | 4.574 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.7875 | 0.4208 | 1.075 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.7 | 3.2 | 3.1 |
| queue: job turnaround, submitted to done, mean (s) | 126.9 | 143.4 | 139.5 | 162.8 |
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
| worker nodes in service, mean | 6 | 5.201 | −13.3% | −1.5410 to −0.0570 | yes: GAIN |
| node-hours | 2.51 | 2.177 | −13.3% | −0.6449 to −0.0223 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274.6 | +0.3% | −0.1180 to +1.7148 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 249.4 | −8.9% | −47.5797 to −1.0693 | yes: GAIN |
| response time (ms), mean | 373.3 | 423.3 | +13.4% | −7.1638 to +107.2276 | no |
| response time (ms), 95th percentile | 1570 | 2085 | +32.8% | +155.0197 to +873.9583 | yes: LOSS |
| response time (ms), 99th percentile | 2506 | 2953 | +17.8% | +71.7577 to +820.4757 | yes: LOSS |
| time over the response line (% of samples) | 14.27 | 16.28 | +14.1% | +0.0547 to +3.9749 | yes: LOSS |
| failed requests (%) | 0 | 0.01156 | +0.012 (native is 0) | −0.0146 to +0.0377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.9 | +6.5% | −0.2396 to +1.4396 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.8 | +101.800 (native is 0) | +48.1124 to +155.4876 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.57 | 24.34 | +46.9% | +2.4184 to +13.1182 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06491 | 0.07742 | +19.3% | +0.0014 to +0.0236 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.558 | 1.593 | +2.3% | +0.0212 to +0.0498 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07779 | +0.078 (native is 0) | +0.0698 to +0.0858 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.558 | 1.671 | +7.3% | +0.0969 to +0.1296 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 431.8 | 375.6 | −13.0% | −106.3224 to −6.0709 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.087 | 2.322 | +11.2% | +0.0300 to +0.4395 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 0 | 2.1 | +2.100 (native is 0) | −0.2228 to +4.4228 | no |
| pod start wait, mean (s) | 0 | 0.9667 | +0.967 (native is 0) | −0.0241 to +1.9574 | no |
| host CPU busy, the real machine under kind (%) | 45.36 | 49.23 | +8.5% | +3.3915 to +4.3361 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.9 | 852.6 | +2.2% | +8.4887 to +28.9113 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.574 | −23.8% | −2.6169 to −0.2346 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7875 | 1.075 | +36.5% | +0.0656 to +0.5094 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 3.1 | +82.4% | +0.0428 to +2.7572 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.4 | 162.9 | +13.6% | +9.0289 to +29.8878 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.51 | −0.1% | −0.0135 to +0.0061 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 273.8 | −0.2% | −1.5449 to +0.5743 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 273.8 | −0.2% | −1.5449 to +0.5743 | no |
| response time (ms), mean | 466.7 | 373.3 | −20.0% | −142.6175 to −44.3021 | yes: GAIN |
| response time (ms), 95th percentile | 1741 | 1570 | −9.8% | −337.6935 to −4.6435 | yes: GAIN |
| response time (ms), 99th percentile | 2437 | 2506 | +2.8% | −202.1948 to +340.3386 | no |
| time over the response line (% of samples) | 20.93 | 14.27 | −31.8% | −10.1462 to −3.1778 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 9.3 | −11.4% | −2.7744 to +0.3744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.97 | 16.57 | +38.4% | +2.0001 to +7.1999 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06509 | 0.06491 | −0.3% | −0.0016 to +0.0013 | no |
| CPU used (cores), mean | 1.562 | 1.558 | −0.3% | −0.0387 to +0.0303 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.562 | 1.558 | −0.3% | −0.0387 to +0.0303 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.5 | 431.8 | +0.8% | −7.2066 to +13.7528 | no |
| HPA replicas, mean | 1.942 | 2.087 | +7.5% | +0.0576 to +0.2326 | yes: power given |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 44.42 | 45.36 | +2.1% | +0.4198 to +1.4682 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822.4 | 833.9 | +1.4% | +0.2543 to +22.7457 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.7875 | +845.0% | +0.5565 to +0.8518 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.7 | +240.0% | +0.3207 to +2.0793 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 126.9 | 143.4 | +13.0% | +4.2998 to +28.6668 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.136 | −14.4% | −1.6016 to −0.1266 | yes: GAIN |
| node-hours | 2.514 | 2.148 | −14.6% | −0.6743 to −0.0577 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274 | −0.1% | −0.9582 to +0.5151 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 246.9 | −10.0% | −50.5651 to −4.1029 | yes: GAIN |
| response time (ms), mean | 466.7 | 450.4 | −3.5% | −43.4804 to +10.7796 | no |
| response time (ms), 95th percentile | 1741 | 1923 | +10.5% | −13.0476 to +377.1646 | no |
| response time (ms), 99th percentile | 2437 | 2660 | +9.1% | +70.6778 to +373.7934 | yes: LOSS |
| time over the response line (% of samples) | 20.93 | 20.38 | −2.6% | −1.4995 to +0.3903 | no |
| failed requests (%) | 0 | 0.02312 | +0.023 (native is 0) | −0.0292 to +0.0754 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.9 | +3.8% | −0.4396 to +1.2396 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.4 | +95.400 (native is 0) | +40.2948 to +150.5052 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.97 | 14.23 | +18.9% | −0.4905 to +5.0172 | no |
| utilisation (used / allocatable) | 0.06509 | 0.07731 | +18.8% | +0.0021 to +0.0224 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.562 | 1.573 | +0.7% | −0.0198 to +0.0406 | no |
| Omni's own CPU (cores), mean | 0 | 0.07485 | +0.075 (native is 0) | +0.0682 to +0.0815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.562 | 1.647 | +5.5% | +0.0513 to +0.1193 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.5 | 377.1 | −12.0% | −94.1158 to −8.7135 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.361 | +21.6% | +0.1574 to +0.6803 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.4715 to +2.7285 | yes: power given |
| pod start wait, total (s) | 0 | 4.6 | +4.600 (native is 0) | +0.8725 to +8.3275 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.567 | +1.567 (native is 0) | +0.4752 to +2.6582 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.42 | 47.88 | +7.8% | +2.7600 to +4.1669 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822.4 | 835.4 | +1.6% | −2.2897 to +28.2897 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.469 | −25.5% | −2.7134 to −0.3485 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.4208 | +405.0% | −0.1611 to +0.8361 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.2 | +540.0% | −2.7062 to +8.1062 | no |
| queue: job turnaround, submitted to done, mean (s) | 126.9 | 139.5 | +9.9% | −0.5822 to +25.8239 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.136 | −14.4% | −1.6016 to −0.1266 | yes: GAIN |
| node-hours | 2.51 | 2.148 | −14.4% | −0.6737 to −0.0509 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 | +0.1% | −0.7968 to +1.3243 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 246.9 | −9.8% | −50.1265 to −3.5710 | yes: GAIN |
| response time (ms), mean | 373.3 | 450.4 | +20.7% | +22.3064 to +131.9124 | yes: LOSS |
| response time (ms), 95th percentile | 1570 | 1923 | +22.5% | +159.3597 to +547.0943 | yes: LOSS |
| response time (ms), 99th percentile | 2506 | 2660 | +6.1% | −52.1794 to +358.5068 | no |
| time over the response line (% of samples) | 14.27 | 20.38 | +42.8% | +3.1596 to +9.0552 | yes: LOSS |
| failed requests (%) | 0 | 0.02312 | +0.023 (native is 0) | −0.0292 to +0.0754 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10.9 | +17.2% | −0.0242 to +3.2242 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.4 | +95.400 (native is 0) | +40.2948 to +150.5052 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.57 | 14.23 | −14.1% | −4.3213 to −0.3520 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06491 | 0.07731 | +19.1% | +0.0015 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.558 | 1.573 | +0.9% | −0.0087 to +0.0380 | no |
| Omni's own CPU (cores), mean | 0 | 0.07485 | +0.075 (native is 0) | +0.0682 to +0.0815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.558 | 1.647 | +5.7% | +0.0659 to +0.1131 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 431.8 | 377.1 | −12.7% | −104.3298 to −5.0456 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.087 | 2.361 | +13.1% | −0.0352 to +0.5827 | no |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.4715 to +2.7285 | yes: power given |
| pod start wait, total (s) | 0 | 4.6 | +4.600 (native is 0) | +0.8725 to +8.3275 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.567 | +1.567 (native is 0) | +0.4752 to +2.6582 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.36 | 47.88 | +5.6% | +2.1514 to +2.8875 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.9 | 835.4 | +0.2% | −3.4241 to +6.4241 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.469 | −25.5% | −2.7134 to −0.3485 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7875 | 0.4208 | −46.6% | −0.7475 to +0.0142 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 3.2 | +88.2% | −3.1754 to +6.1754 | no |
| queue: job turnaround, submitted to done, mean (s) | 143.4 | 139.5 | −2.7% | −8.0001 to +0.2751 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.201 | −13.3% | −1.5410 to −0.0570 | yes: GAIN |
| node-hours | 2.514 | 2.177 | −13.4% | −0.6471 to −0.0275 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.6 | +0.1% | −0.5972 to +1.2235 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 249.4 | −9.0% | −48.1647 to −1.4549 | yes: GAIN |
| response time (ms), mean | 466.7 | 423.3 | −9.3% | −83.1700 to −3.6857 | yes: GAIN |
| response time (ms), 95th percentile | 1741 | 2085 | +19.7% | −39.5490 to +726.1900 | no |
| response time (ms), 99th percentile | 2437 | 2953 | +21.1% | +100.3113 to +930.0659 | yes: LOSS |
| time over the response line (% of samples) | 20.93 | 16.28 | −22.2% | −7.5194 to −1.7750 | yes: GAIN |
| failed requests (%) | 0 | 0.01156 | +0.012 (native is 0) | −0.0146 to +0.0377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 9.9 | −5.7% | −1.7778 to +0.5778 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.8 | +101.800 (native is 0) | +48.1124 to +155.4876 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.97 | 24.34 | +103.3% | +5.2891 to +19.4475 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06509 | 0.07742 | +19.0% | +0.0019 to +0.0228 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.562 | 1.593 | +2.0% | +0.0049 to +0.0577 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07779 | +0.078 (native is 0) | +0.0698 to +0.0858 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.562 | 1.671 | +7.0% | +0.0771 to +0.1410 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.5 | 375.6 | −12.4% | −97.0571 to −8.7901 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.322 | +19.6% | +0.2064 to +0.5533 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 0 | 2.1 | +2.100 (native is 0) | −0.2228 to +4.4228 | no |
| pod start wait, mean (s) | 0 | 0.9667 | +0.967 (native is 0) | −0.0241 to +1.9574 | no |
| host CPU busy, the real machine under kind (%) | 44.42 | 49.23 | +10.8% | +4.0041 to +5.6115 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822.4 | 852.6 | +3.7% | +9.7256 to +50.6744 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.574 | −23.8% | −2.6169 to −0.2346 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1.075 | +1190.0% | +0.7448 to +1.2386 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.1 | +520.0% | +1.1615 to +4.0385 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 126.9 | 162.8 | +28.3% | +14.7697 to +57.1137 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*