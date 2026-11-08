# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.445 | 4.297 |
| node-hours | 2.516 | 2.517 | 1.863 | 1.797 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.7 | 272 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 271.7 | 223.1 | 218 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 321.8 | 333 | 321.3 | 319.4 |
| response time (ms), 95th percentile | 1193 | 1274 | 1339 | 1344 |
| response time (ms), 99th percentile | 1686 | 1787 | 1883 | 1894 |
| time over the response line (% of samples) | 13.46 | 13.73 | 13.55 | 13.82 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 6.7 | 7 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 134 | 158.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 58.33 | 7.143 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.513 | 9.3 | 11.64 | 10.94 |
| utilisation (used / allocatable) | 0.05714 | 0.05744 | 0.08031 | 0.08141 |
| CPU used (cores), mean | 1.371 | 1.379 | 1.39 | 1.375 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06723 | 0.06991 |
| CPU used with Omni's own (cores), mean | 1.371 | 1.379 | 1.457 | 1.445 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.7 | 494.3 | 385 | 385.8 |
| HPA replicas, mean | 1.924 | 1.989 | 2.187 | 2.233 |
| pods started | 0 | 0.2 | 1.3 | 1.1 |
| pod start wait, total (s) | 0 | 0.5 | 3.4 | 2.4 |
| pod start wait, mean (s) | 0 | 0.5 | 1.25 | 1.225 |
| host CPU busy, the real machine under kind (%) | 39.24 | 39.8 | 42.64 | 43.16 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 783.4 | 788.6 | 795.8 | 797.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.803 | 3.396 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.15 | 0.1792 | 0.3417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.8 | 0.5 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 88.5 | 93.47 | 99.51 | 101.6 |
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
| worker nodes in service, mean | 6 | 4.297 | −28.4% | −2.6032 to −0.8020 | yes: GAIN |
| node-hours | 2.517 | 1.797 | −28.6% | −1.0969 to −0.3426 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.5 | −0.1% | −1.1583 to +0.6441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 218 | −19.8% | −82.0799 to −25.4468 | yes: GAIN |
| response time (ms), mean | 333 | 319.4 | −4.1% | −28.4984 to +1.3142 | no |
| response time (ms), 95th percentile | 1274 | 1344 | +5.5% | −10.5868 to +151.0518 | no |
| response time (ms), 99th percentile | 1787 | 1894 | +6.0% | −0.4738 to +213.5226 | no |
| time over the response line (% of samples) | 13.73 | 13.82 | +0.6% | −0.5690 to +0.7453 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 7.1 | +6.0% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 158.2 | +158.200 (native is 0) | +62.2571 to +254.1429 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.3 | 10.94 | +17.6% | −1.0381 to +4.3147 | no |
| utilisation (used / allocatable) | 0.05744 | 0.08141 | +41.7% | +0.0112 to +0.0367 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.379 | 1.375 | −0.2% | −0.0465 to +0.0400 | no |
| Omni's own CPU (cores), mean | 0 | 0.06991 | +0.070 (native is 0) | +0.0605 to +0.0793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.379 | 1.445 | +4.8% | +0.0184 to +0.1149 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.3 | 385.8 | −22.0% | −173.9529 to −43.1328 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.989 | 2.233 | +12.3% | +0.0623 to +0.4250 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | −0.0802 to +1.8802 | no |
| pod start wait, total (s) | 0.5 | 2.4 | +380.0% | −0.8280 to +4.6280 | no |
| pod start wait, mean (s) | 0.5 | 1.225 | +145.0% | −0.5713 to +2.0213 | no |
| host CPU busy, the real machine under kind (%) | 39.8 | 43.16 | +8.4% | +2.7122 to +4.0052 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.6 | 797.2 | +1.1% | −0.5056 to +17.7056 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.396 | −43.4% | −3.7164 to −1.4911 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.15 | 0.3417 | +127.8% | −0.1068 to +0.4901 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 | −12.5% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.47 | 101.6 | +8.7% | +0.0527 to +16.2973 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.517 | +0.0% | −0.0060 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.7 | +0.1% | −0.6068 to +1.1298 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 271.7 | +0.1% | −0.6068 to +1.1298 | no |
| response time (ms), mean | 321.8 | 333 | +3.5% | −1.2927 to +23.7824 | no |
| response time (ms), 95th percentile | 1193 | 1274 | +6.7% | −19.4910 to +180.3730 | no |
| response time (ms), 99th percentile | 1686 | 1787 | +6.0% | −64.0331 to +265.9727 | no |
| time over the response line (% of samples) | 13.46 | 13.73 | +2.0% | −0.0060 to +0.5467 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 6.7 | +1.5% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.513 | 9.3 | −2.2% | −2.2241 to +1.7974 | no |
| utilisation (used / allocatable) | 0.05714 | 0.05744 | +0.5% | −0.0012 to +0.0018 | no |
| CPU used (cores), mean | 1.371 | 1.379 | +0.5% | −0.0297 to +0.0442 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.371 | 1.379 | +0.5% | −0.0297 to +0.0442 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.7 | 494.3 | −0.9% | −21.9826 to +13.1467 | no |
| HPA replicas, mean | 1.924 | 1.989 | +3.4% | −0.0968 to +0.2263 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 39.24 | 39.8 | +1.4% | +0.2892 to +0.8409 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.4 | 788.6 | +0.7% | −0.9422 to +11.3422 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.15 | +350.0% | +0.0541 to +0.1792 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.8 | +700.0% | +0.3545 to +1.0455 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 88.5 | 93.47 | +5.6% | −0.9326 to +10.8826 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.445 | −25.9% | −2.5751 to −0.5347 | yes: GAIN |
| node-hours | 2.516 | 1.863 | −26.0% | −1.0806 to −0.2259 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272 | +0.2% | −0.5053 to +1.6186 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 223.1 | −17.8% | −80.3670 to −16.3822 | yes: GAIN |
| response time (ms), mean | 321.8 | 321.3 | −0.1% | −23.0646 to +22.2111 | no |
| response time (ms), 95th percentile | 1193 | 1339 | +12.2% | −14.7805 to +305.5445 | no |
| response time (ms), 99th percentile | 1686 | 1883 | +11.7% | +14.6345 to +379.8777 | yes: LOSS |
| time over the response line (% of samples) | 13.46 | 13.55 | +0.7% | −0.3032 to +0.4789 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7 | +6.1% | −0.2032 to +1.0032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134 | +134.000 (native is 0) | +59.8078 to +208.1922 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.513 | 11.64 | +22.4% | −0.5949 to +4.8582 | no |
| utilisation (used / allocatable) | 0.05714 | 0.08031 | +40.5% | +0.0085 to +0.0378 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.371 | 1.39 | +1.4% | −0.0323 to +0.0693 | no |
| Omni's own CPU (cores), mean | 0 | 0.06723 | +0.067 (native is 0) | +0.0589 to +0.0756 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.371 | 1.457 | +6.3% | +0.0328 to +0.1387 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.7 | 385 | −22.8% | −194.3586 to −33.0426 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.924 | 2.187 | +13.7% | +0.0126 to +0.5129 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.2310 to +2.3690 | yes: power given |
| pod start wait, total (s) | 0 | 3.4 | +3.400 (native is 0) | +0.3243 to +6.4757 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.25 | +1.250 (native is 0) | +0.2778 to +2.2222 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.24 | 42.64 | +8.7% | +2.5427 to +4.2615 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.4 | 795.8 | +1.6% | −0.3922 to +25.1922 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.803 | −36.6% | −3.5885 to −0.8053 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.1792 | +437.5% | −0.0603 to +0.3520 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.5 | +400.0% | −0.3689 to +1.1689 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.5 | 99.51 | +12.4% | +0.0191 to +22.0143 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.445 | −25.9% | −2.5751 to −0.5347 | yes: GAIN |
| node-hours | 2.517 | 1.863 | −26.0% | −1.0830 to −0.2258 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272 | +0.1% | −0.7981 to +1.3883 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 223.1 | −17.9% | −80.7603 to −16.5120 | yes: GAIN |
| response time (ms), mean | 333 | 321.3 | −3.5% | −30.0851 to +6.7418 | no |
| response time (ms), 95th percentile | 1274 | 1339 | +5.1% | −46.3396 to +176.2216 | no |
| response time (ms), 99th percentile | 1787 | 1883 | +5.4% | −47.4926 to +240.0652 | no |
| time over the response line (% of samples) | 13.73 | 13.55 | −1.3% | −0.7407 to +0.3758 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 7 | +4.5% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134 | +134.000 (native is 0) | +59.8078 to +208.1922 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.3 | 11.64 | +25.2% | −0.4597 to +5.1497 | no |
| utilisation (used / allocatable) | 0.05744 | 0.08031 | +39.8% | +0.0082 to +0.0376 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.379 | 1.39 | +0.8% | −0.0293 to +0.0519 | no |
| Omni's own CPU (cores), mean | 0 | 0.06723 | +0.067 (native is 0) | +0.0589 to +0.0756 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.379 | 1.457 | +5.7% | +0.0361 to +0.1210 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.3 | 385 | −22.1% | −185.3249 to −33.2404 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.989 | 2.187 | +10.0% | +0.0039 to +0.3921 | yes: power given |
| pods started | 0.2 | 1.3 | +550.0% | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.4 | +580.0% | +0.0899 to +5.7101 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.25 | +150.0% | −0.3588 to +1.8588 | no |
| host CPU busy, the real machine under kind (%) | 39.8 | 42.64 | +7.1% | +2.0603 to +3.6137 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.6 | 795.8 | +0.9% | −1.8593 to +16.2593 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.803 | −36.6% | −3.5885 to −0.8053 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.15 | 0.1792 | +19.4% | −0.1222 to +0.1805 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.5 | −37.5% | −0.9786 to +0.3786 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.47 | 99.51 | +6.5% | −1.4582 to +13.5416 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.297 | −28.4% | −2.6032 to −0.8020 | yes: GAIN |
| node-hours | 2.516 | 1.797 | −28.6% | −1.0945 to −0.3427 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.5 | +0.0% | −0.7973 to +0.8061 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 218 | −19.7% | −81.6684 to −25.3354 | yes: GAIN |
| response time (ms), mean | 321.8 | 319.4 | −0.7% | −22.4735 to +17.7791 | no |
| response time (ms), 95th percentile | 1193 | 1344 | +12.6% | +18.0771 to +283.2699 | yes: LOSS |
| response time (ms), 99th percentile | 1686 | 1894 | +12.3% | +26.1697 to +388.8187 | yes: LOSS |
| time over the response line (% of samples) | 13.46 | 13.82 | +2.7% | −0.2533 to +0.9703 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.1 | +7.6% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 158.2 | +158.200 (native is 0) | +62.2571 to +254.1429 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.513 | 10.94 | +15.0% | −1.1472 to +3.9972 | no |
| utilisation (used / allocatable) | 0.05714 | 0.08141 | +42.5% | +0.0116 to +0.0369 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.371 | 1.375 | +0.3% | −0.0447 to +0.0526 | no |
| Omni's own CPU (cores), mean | 0 | 0.06991 | +0.070 (native is 0) | +0.0605 to +0.0793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.371 | 1.445 | +5.4% | +0.0208 to +0.1270 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.7 | 385.8 | −22.7% | −182.4597 to −43.4619 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.924 | 2.233 | +16.0% | +0.0937 to +0.5231 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.400 (native is 0) | −0.0595 to +4.8595 | no |
| pod start wait, mean (s) | 0 | 1.225 | +1.225 (native is 0) | +0.2475 to +2.2025 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.24 | 43.16 | +10.0% | +3.0776 to +4.7700 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.4 | 797.2 | +1.8% | −0.4616 to +28.0616 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.396 | −43.4% | −3.7164 to −1.4911 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.3417 | +925.0% | −0.0356 to +0.6523 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.7 | +600.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 88.5 | 101.6 | +14.9% | −0.2818 to +26.5818 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*