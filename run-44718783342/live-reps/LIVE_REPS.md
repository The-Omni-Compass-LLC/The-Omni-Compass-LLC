# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.51 | 4.539 |
| node-hours | 2.513 | 2.513 | 1.889 | 1.904 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.5 | 272 | 273.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.5 | 225.3 | 227.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 317.8 | 364.2 | 308.2 | 338.3 |
| response time (ms), 95th percentile | 1127 | 1569 | 1248 | 1653 |
| response time (ms), 99th percentile | 1639 | 2169 | 1784 | 2258 |
| time over the response line (% of samples) | 13.51 | 12.06 | 13.77 | 11.95 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 7.9 | 7.6 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 150.3 | 85.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.985 | 20.47 | 9.743 | 22.85 |
| utilisation (used / allocatable) | 0.05866 | 0.06032 | 0.08079 | 0.08106 |
| CPU used (cores), mean | 1.408 | 1.448 | 1.413 | 1.434 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06937 | 0.07437 |
| CPU used with Omni's own (cores), mean | 1.408 | 1.448 | 1.482 | 1.508 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.2 | 462.1 | 381.9 | 377.8 |
| HPA replicas, mean | 2.03 | 2.023 | 2.266 | 2.018 |
| pods started | 0.2 | 0.1 | 1.7 | 0.2 |
| pod start wait, total (s) | 0.3 | 0.2 | 3.9 | 0.4 |
| pod start wait, mean (s) | 0.3 | 0.2 | 1.267 | 0.4 |
| host CPU busy, the real machine under kind (%) | 40.54 | 43.05 | 43.68 | 46.33 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 780.5 | 813.2 | 790.5 | 824.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.715 | 3.721 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.9042 | 0.0375 | 1.087 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.8 | 0.2 | 2.9 |
| queue: job turnaround, submitted to done, mean (s) | 86.67 | 118.1 | 94.7 | 127.2 |
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
| worker nodes in service, mean | 6 | 4.539 | −24.3% | −2.3856 to −0.5358 | yes: GAIN |
| node-hours | 2.513 | 1.904 | −24.2% | −0.9980 to −0.2188 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 273.1 | +0.2% | −0.2960 to +1.3406 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 227.1 | −16.7% | −74.7852 to −16.0369 | yes: GAIN |
| response time (ms), mean | 364.2 | 338.3 | −7.1% | −46.4455 to −5.3728 | yes: GAIN |
| response time (ms), 95th percentile | 1569 | 1653 | +5.4% | −19.4877 to +187.8767 | no |
| response time (ms), 99th percentile | 2169 | 2258 | +4.1% | −40.3033 to +219.6061 | no |
| time over the response line (% of samples) | 12.06 | 11.95 | −0.9% | −1.4015 to +1.1789 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.1 | +2.5% | −0.6121 to +1.0121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.5 | +85.500 (native is 0) | +40.1982 to +130.8018 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.47 | 22.85 | +11.7% | −1.2970 to +6.0670 | no |
| utilisation (used / allocatable) | 0.06032 | 0.08106 | +34.4% | +0.0071 to +0.0344 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.448 | 1.434 | −0.9% | −0.0367 to +0.0094 | no |
| Omni's own CPU (cores), mean | 0 | 0.07437 | +0.074 (native is 0) | +0.0659 to +0.0828 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.508 | +4.2% | +0.0313 to +0.0901 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 377.8 | −18.2% | −139.5562 to −29.0189 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.018 | −0.2% | −0.1526 to +0.1437 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.6121 to +1.0121 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.6121 to +1.0121 | no |
| host CPU busy, the real machine under kind (%) | 43.05 | 46.33 | +7.6% | +2.7458 to +3.8246 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813.2 | 824.8 | +1.4% | +1.4101 to +21.7899 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.721 | −38.0% | −3.5776 to −0.9812 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9042 | 1.087 | +20.3% | +0.0236 to +0.3430 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 2.9 | +61.1% | −0.2676 to +2.4676 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.1 | 127.2 | +7.7% | +1.1844 to +17.0156 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.513 | −0.0% | −0.0083 to +0.0073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.5 | +0.2% | −0.2226 to +1.5317 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.5 | +0.2% | −0.2226 to +1.5317 | no |
| response time (ms), mean | 317.8 | 364.2 | +14.6% | +1.8846 to +90.9345 | yes: LOSS |
| response time (ms), 95th percentile | 1127 | 1569 | +39.3% | +39.2008 to +845.2692 | yes: LOSS |
| response time (ms), 99th percentile | 1639 | 2169 | +32.3% | +102.2078 to +956.9860 | yes: LOSS |
| time over the response line (% of samples) | 13.51 | 12.06 | −10.7% | −4.2206 to +1.3229 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 7.9 | +21.5% | +0.2715 to +2.5285 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.985 | 20.46 | +105.0% | +3.4277 to +17.5323 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05866 | 0.06032 | +2.8% | +0.0004 to +0.0029 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.408 | 1.448 | +2.8% | +0.0098 to +0.0696 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.408 | 1.448 | +2.8% | +0.0098 to +0.0696 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.2 | 462.1 | −2.8% | −25.5917 to −0.6177 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.03 | 2.023 | −0.4% | −0.1366 to +0.1218 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0.2 | −33.3% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 40.54 | 43.05 | +6.2% | +1.4014 to +3.6055 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.5 | 813.2 | +4.2% | +6.8937 to +58.5063 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.9042 | +2612.5% | +0.6355 to +1.1061 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.8 | +800.0% | +0.9089 to +2.2911 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 86.67 | 118.1 | +36.2% | +8.7378 to +54.0872 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.51 | −24.8% | −2.4150 to −0.5658 | yes: GAIN |
| node-hours | 2.513 | 1.889 | −24.8% | −1.0129 to −0.2360 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 | +0.1% | −1.1724 to +1.4967 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 225.3 | −17.2% | −75.8980 to −17.3652 | yes: GAIN |
| response time (ms), mean | 317.8 | 308.2 | −3.0% | −22.9898 to +3.8691 | no |
| response time (ms), 95th percentile | 1127 | 1248 | +10.7% | +37.6416 to +204.1794 | yes: LOSS |
| response time (ms), 99th percentile | 1639 | 1784 | +8.8% | +49.4403 to +239.9815 | yes: LOSS |
| time over the response line (% of samples) | 13.51 | 13.77 | +1.9% | −0.2421 to +0.7632 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 7.6 | +16.9% | −0.4617 to +2.6617 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 150.3 | +150.300 (native is 0) | +57.5353 to +243.0647 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.985 | 9.743 | −2.4% | −2.0515 to +1.5682 | no |
| utilisation (used / allocatable) | 0.05866 | 0.08079 | +37.7% | +0.0081 to +0.0361 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.408 | 1.413 | +0.4% | −0.0305 to +0.0407 | no |
| Omni's own CPU (cores), mean | 0 | 0.06937 | +0.069 (native is 0) | +0.0622 to +0.0766 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.408 | 1.482 | +5.3% | +0.0365 to +0.1125 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.2 | 381.9 | −19.6% | −153.2870 to −33.2951 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.03 | 2.266 | +11.6% | −0.0364 to +0.5083 | no |
| pods started | 0.2 | 1.7 | +750.0% | +0.1407 to +2.8593 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.9 | +1200.0% | +0.1414 to +7.0586 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.267 | +322.2% | −0.2199 to +2.1533 | no |
| host CPU busy, the real machine under kind (%) | 40.54 | 43.68 | +7.7% | +2.5626 to +3.7073 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.5 | 790.5 | +1.3% | +0.6492 to +19.3508 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.715 | −38.1% | −3.4663 to −1.1039 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.0375 | +12.5% | −0.0178 to +0.0262 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 86.67 | 94.7 | +9.3% | +0.6326 to +15.4174 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.51 | −24.8% | −2.4150 to −0.5658 | yes: GAIN |
| node-hours | 2.513 | 1.889 | −24.8% | −1.0118 to −0.2360 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272 | −0.2% | −1.6635 to +0.6787 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 225.3 | −17.4% | −76.6475 to −17.9249 | yes: GAIN |
| response time (ms), mean | 364.2 | 308.2 | −15.4% | −93.2944 to −18.6454 | yes: GAIN |
| response time (ms), 95th percentile | 1569 | 1248 | −20.5% | −656.1676 to +13.5186 | no |
| response time (ms), 99th percentile | 2169 | 1784 | −17.7% | −751.4714 to −18.3006 | yes: GAIN |
| time over the response line (% of samples) | 12.06 | 13.77 | +14.2% | −0.7919 to +4.2107 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 7.6 | −3.8% | −1.2567 to +0.6567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 150.3 | +150.300 (native is 0) | +57.5353 to +243.0647 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.47 | 9.743 | −52.4% | −17.0515 to −4.3918 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06032 | 0.08079 | +34.0% | +0.0065 to +0.0344 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.448 | 1.413 | −2.4% | −0.0685 to −0.0006 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06937 | +0.069 (native is 0) | +0.0622 to +0.0766 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.482 | +2.4% | −0.0032 to +0.0729 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 381.9 | −17.4% | −136.5320 to −23.8408 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.266 | +12.0% | −0.0642 to +0.5508 | no |
| pods started | 0.1 | 1.7 | +1600.0% | +0.3293 to +2.8707 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.9 | +1850.0% | +0.3104 to +7.0896 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.267 | +533.3% | −0.0449 to +2.1782 | no |
| host CPU busy, the real machine under kind (%) | 43.05 | 43.68 | +1.5% | −0.0309 to +1.2938 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813.2 | 790.5 | −2.8% | −39.7179 to −5.6821 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.715 | −38.1% | −3.4663 to −1.1039 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9042 | 0.0375 | −95.9% | −1.1132 to −0.6202 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 0.2 | −88.9% | −2.5048 to −0.6952 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 118.1 | 94.7 | −19.8% | −40.0762 to −6.6988 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.539 | −24.3% | −2.3856 to −0.5358 | yes: GAIN |
| node-hours | 2.513 | 1.904 | −24.2% | −0.9981 to −0.2198 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 273.1 | +0.4% | +0.4596 to +1.8941 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 227.1 | −16.5% | −73.9008 to −15.6122 | yes: GAIN |
| response time (ms), mean | 317.8 | 338.3 | +6.5% | −17.6820 to +58.6828 | no |
| response time (ms), 95th percentile | 1127 | 1653 | +46.7% | +73.0013 to +979.8577 | yes: LOSS |
| response time (ms), 99th percentile | 1639 | 2258 | +37.8% | +132.4667 to +1106.0299 | yes: LOSS |
| time over the response line (% of samples) | 13.51 | 11.95 | −11.5% | −5.2786 to +2.1583 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 8.1 | +24.6% | −0.1260 to +3.3260 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.5 | +85.500 (native is 0) | +40.1982 to +130.8018 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.985 | 22.85 | +128.8% | +4.1957 to +21.5343 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05866 | 0.08106 | +38.2% | +0.0086 to +0.0362 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.408 | 1.434 | +1.8% | −0.0037 to +0.0558 | no |
| Omni's own CPU (cores), mean | 0 | 0.07437 | +0.074 (native is 0) | +0.0659 to +0.0828 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.408 | 1.508 | +7.1% | +0.0688 to +0.1320 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.2 | 377.8 | −20.5% | −157.6586 to −37.1259 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.03 | 2.018 | −0.6% | −0.1980 to +0.1744 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.7564 to +0.9564 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.7564 to +0.9564 | no |
| host CPU busy, the real machine under kind (%) | 40.54 | 46.33 | +14.3% | +4.3823 to +7.1950 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.5 | 824.8 | +5.7% | +10.2562 to +78.3438 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.721 | −38.0% | −3.5776 to −0.9812 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 1.088 | +3162.5% | +0.7247 to +1.3837 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 2.9 | +1350.0% | +1.1166 to +4.2834 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 86.67 | 127.2 | +46.7% | +11.8020 to +69.2230 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*