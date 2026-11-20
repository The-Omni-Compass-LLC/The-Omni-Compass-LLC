# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.892 | 4.968 |
| node-hours | 2.513 | 2.513 | 2.051 | 2.082 |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.8 | 274.3 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 273.8 | 239.4 | 242 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 465.5 | 440.2 | 457.9 | 401.8 |
| response time (ms), 95th percentile | 1724 | 1948 | 1949 | 2029 |
| response time (ms), 99th percentile | 2532 | 2724 | 2810 | 2929 |
| time over the response line (% of samples) | 22.87 | 16.99 | 22.36 | 15.67 |
| failed requests (%) | 0 | 0.01093 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.2 | 10.7 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 109 | 97.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.71 | 13.84 | 14.13 | 14.87 |
| utilisation (used / allocatable) | 0.06467 | 0.064 | 0.08005 | 0.08014 |
| CPU used (cores), mean | 1.552 | 1.536 | 1.538 | 1.551 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07854 | 0.07783 |
| CPU used with Omni's own (cores), mean | 1.552 | 1.536 | 1.616 | 1.629 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.9 | 439.5 | 373.2 | 373.2 |
| HPA replicas, mean | 2.044 | 2.016 | 2.158 | 2.214 |
| pods started | 0.4 | 0.1 | 0.9 | 0.7 |
| pod start wait, total (s) | 1 | 0.2 | 2.4 | 1.2 |
| pod start wait, mean (s) | 0.75 | 0.2 | 1.25 | 0.55 |
| host CPU busy, the real machine under kind (%) | 44.41 | 44.42 | 47.58 | 47.72 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 825.1 | 825.7 | 836.6 | 839.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.22 | 4.415 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.09583 | 0.2 | 0.3083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 | 1.1 | 2.4 |
| queue: job turnaround, submitted to done, mean (s) | 130.5 | 134.3 | 140.1 | 146 |
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
| worker nodes in service, mean | 6 | 4.968 | −17.2% | −1.9755 to −0.0891 | yes: GAIN |
| node-hours | 2.513 | 2.082 | −17.2% | −0.8252 to −0.0374 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274.4 | +0.2% | −0.2474 to +1.5152 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 242 | −11.6% | −61.4086 to −2.2153 | yes: GAIN |
| response time (ms), mean | 440.2 | 401.8 | −8.7% | −71.4193 to −5.5275 | yes: GAIN |
| response time (ms), 95th percentile | 1948 | 2029 | +4.2% | −72.9793 to +236.5613 | no |
| response time (ms), 99th percentile | 2724 | 2929 | +7.5% | +13.7116 to +395.0070 | yes: LOSS |
| time over the response line (% of samples) | 16.99 | 15.67 | −7.7% | −2.8413 to +0.2120 | no |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.3 | +1.0% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 97.5 | +97.500 (native is 0) | +10.5633 to +184.4367 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.84 | 14.88 | +7.5% | −1.0313 to +3.1047 | no |
| utilisation (used / allocatable) | 0.064 | 0.08014 | +25.2% | +0.0021 to +0.0302 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.536 | 1.551 | +1.0% | −0.0175 to +0.0474 | no |
| Omni's own CPU (cores), mean | 0 | 0.07783 | +0.078 (native is 0) | +0.0736 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.536 | 1.629 | +6.0% | +0.0587 to +0.1268 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.5 | 373.2 | −15.1% | −124.4676 to −8.0507 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.214 | +9.8% | −0.0306 to +0.4261 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.4228 to +1.6228 | no |
| pod start wait, total (s) | 0.2 | 1.2 | +500.0% | −0.6860 to +2.6860 | no |
| pod start wait, mean (s) | 0.2 | 0.55 | +175.0% | −0.5105 to +1.2105 | no |
| host CPU busy, the real machine under kind (%) | 44.42 | 47.72 | +7.4% | +2.8020 to +3.7996 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.7 | 839.4 | +1.7% | +4.4221 to +22.9779 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.415 | −26.4% | −2.8240 to −0.3452 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 0.3083 | +221.7% | −0.0347 to +0.4597 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 2.4 | +300.0% | −0.8076 to +4.4076 | no |
| queue: job turnaround, submitted to done, mean (s) | 134.3 | 146 | +8.7% | +3.3277 to +19.9723 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.513 | +0.0% | −0.0076 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.8 | −0.1% | −0.8758 to +0.5144 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 273.8 | −0.1% | −0.8758 to +0.5144 | no |
| response time (ms), mean | 465.5 | 440.2 | −5.4% | −45.0322 to −5.4431 | yes: GAIN |
| response time (ms), 95th percentile | 1724 | 1948 | +13.0% | +45.2480 to +401.8250 | yes: LOSS |
| response time (ms), 99th percentile | 2532 | 2724 | +7.6% | −81.4324 to +465.3860 | no |
| time over the response line (% of samples) | 22.87 | 16.99 | −25.7% | −8.7760 to −2.9895 | yes: GAIN |
| failed requests (%) | 0 | 0.01093 | +0.011 (native is 0) | −0.0138 to +0.0357 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.2 | −2.9% | −0.6455 to +0.0455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.71 | 13.84 | +8.9% | −0.8141 to +3.0741 | no |
| utilisation (used / allocatable) | 0.06467 | 0.064 | −1.0% | −0.0016 to +0.0003 | no |
| CPU used (cores), mean | 1.552 | 1.536 | −1.0% | −0.0388 to +0.0068 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.552 | 1.536 | −1.0% | −0.0388 to +0.0068 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.9 | 439.5 | +0.8% | −3.4250 to +10.5415 | no |
| HPA replicas, mean | 2.044 | 2.016 | −1.4% | −0.1471 to +0.0909 | no |
| pods started | 0.4 | 0.1 | −75.0% | −0.8889 to +0.2889 | no |
| pod start wait, total (s) | 1 | 0.2 | −80.0% | −2.2226 to +0.6226 | no |
| pod start wait, mean (s) | 0.75 | 0.2 | −73.3% | −1.6223 to +0.5223 | no |
| host CPU busy, the real machine under kind (%) | 44.41 | 44.42 | +0.0% | −0.4075 to +0.4112 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.1 | 825.7 | +0.1% | −4.8497 to +6.0497 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.09583 | −8.0% | −0.0900 to +0.0733 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 | +20.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.5 | 134.3 | +2.9% | −1.6354 to +9.3020 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.892 | −18.5% | −1.9956 to −0.2210 | yes: GAIN |
| node-hours | 2.513 | 2.051 | −18.4% | −0.8353 to −0.0881 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.3 | +0.1% | −0.6495 to +1.3335 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 239.4 | −12.6% | −62.7038 to −6.3621 | yes: GAIN |
| response time (ms), mean | 465.5 | 457.9 | −1.6% | −24.0643 to +8.9092 | no |
| response time (ms), 95th percentile | 1724 | 1949 | +13.0% | +114.9645 to +334.0035 | yes: LOSS |
| response time (ms), 99th percentile | 2532 | 2810 | +11.0% | +117.8570 to +438.3532 | yes: LOSS |
| time over the response line (% of samples) | 22.87 | 22.36 | −2.2% | −1.4087 to +0.3866 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.7 | +1.9% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 109 | +109.000 (native is 0) | +6.0924 to +211.9076 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.71 | 14.13 | +11.2% | −0.8552 to +3.6986 | no |
| utilisation (used / allocatable) | 0.06467 | 0.08005 | +23.8% | +0.0024 to +0.0283 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.552 | 1.538 | −0.9% | −0.0562 to +0.0275 | no |
| Omni's own CPU (cores), mean | 0 | 0.07854 | +0.079 (native is 0) | +0.0744 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.552 | 1.616 | +4.1% | +0.0211 to +0.1072 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.9 | 373.2 | −14.4% | −120.5435 to −4.9207 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.044 | 2.158 | +5.5% | −0.0282 to +0.2549 | no |
| pods started | 0.4 | 0.9 | +125.0% | −0.5796 to +1.5796 | no |
| pod start wait, total (s) | 1 | 2.4 | +140.0% | −1.6198 to +4.4198 | no |
| pod start wait, mean (s) | 0.75 | 1.25 | +66.7% | −0.9698 to +1.9698 | no |
| host CPU busy, the real machine under kind (%) | 44.41 | 47.58 | +7.1% | +2.6486 to +3.6718 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.1 | 836.6 | +1.4% | +3.8682 to +19.1318 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.22 | −29.7% | −2.9406 to −0.6200 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2 | +92.0% | −0.0112 to +0.2029 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.1 | +120.0% | −0.5285 to +1.7285 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.5 | 140.1 | +7.4% | +2.8870 to +16.4296 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.892 | −18.5% | −1.9956 to −0.2210 | yes: GAIN |
| node-hours | 2.513 | 2.051 | −18.4% | −0.8317 to −0.0920 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274.3 | +0.2% | −0.5194 to +1.5649 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 239.4 | −12.5% | −62.2384 to −6.4662 | yes: GAIN |
| response time (ms), mean | 440.2 | 457.9 | +4.0% | −6.5916 to +41.9118 | no |
| response time (ms), 95th percentile | 1948 | 1949 | +0.0% | −92.8257 to +94.7207 | no |
| response time (ms), 99th percentile | 2724 | 2810 | +3.2% | −77.8105 to +250.0671 | no |
| time over the response line (% of samples) | 16.99 | 22.36 | +31.6% | +2.7808 to +7.9625 | yes: LOSS |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.7 | +4.9% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 109 | +109.000 (native is 0) | +6.0924 to +211.9076 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.84 | 14.13 | +2.1% | −0.9589 to +1.5423 | no |
| utilisation (used / allocatable) | 0.064 | 0.08005 | +25.1% | +0.0033 to +0.0288 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.536 | 1.538 | +0.1% | −0.0415 to +0.0447 | no |
| Omni's own CPU (cores), mean | 0 | 0.07854 | +0.079 (native is 0) | +0.0744 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.536 | 1.616 | +5.2% | +0.0353 to +0.1251 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.5 | 373.2 | −15.1% | −122.0282 to −10.5525 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.158 | +7.0% | −0.0222 to +0.3050 | no |
| pods started | 0.1 | 0.9 | +800.0% | −0.0793 to +1.6793 | no |
| pod start wait, total (s) | 0.2 | 2.4 | +1100.0% | −0.2962 to +4.6962 | no |
| pod start wait, mean (s) | 0.2 | 1.25 | +525.0% | −0.1710 to +2.2710 | no |
| host CPU busy, the real machine under kind (%) | 44.42 | 47.58 | +7.1% | +2.3955 to +3.9213 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.7 | 836.6 | +1.3% | +2.8534 to +18.9466 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.22 | −29.7% | −2.9406 to −0.6200 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 0.2 | +108.7% | −0.0556 to +0.2639 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.1 | +83.3% | −0.6802 to +1.6802 | no |
| queue: job turnaround, submitted to done, mean (s) | 134.3 | 140.1 | +4.3% | +0.0007 to +11.6493 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.968 | −17.2% | −1.9755 to −0.0891 | yes: GAIN |
| node-hours | 2.513 | 2.082 | −17.2% | −0.8283 to −0.0339 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.4 | +0.2% | −0.5723 to +1.4788 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 242 | −11.7% | −61.8135 to −2.1716 | yes: GAIN |
| response time (ms), mean | 465.5 | 401.8 | −13.7% | −98.2449 to −29.1771 | yes: GAIN |
| response time (ms), 95th percentile | 1724 | 2029 | +17.7% | +59.1748 to +551.4802 | yes: LOSS |
| response time (ms), 99th percentile | 2532 | 2929 | +15.7% | +93.1022 to +699.5700 | yes: LOSS |
| time over the response line (% of samples) | 22.87 | 15.67 | −31.5% | −10.6901 to −3.7047 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.3 | −1.9% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 97.5 | +97.500 (native is 0) | +10.5633 to +184.4367 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.71 | 14.88 | +17.0% | −1.0278 to +5.3612 | no |
| utilisation (used / allocatable) | 0.06467 | 0.08014 | +23.9% | +0.0012 to +0.0297 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.552 | 1.551 | −0.1% | −0.0206 to +0.0184 | no |
| Omni's own CPU (cores), mean | 0 | 0.07783 | +0.078 (native is 0) | +0.0736 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.552 | 1.629 | +4.9% | +0.0563 to +0.0972 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.9 | 373.2 | −14.4% | −122.5186 to −2.8832 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.044 | 2.214 | +8.3% | −0.0901 to +0.4294 | no |
| pods started | 0.4 | 0.7 | +75.0% | −0.9181 to +1.5181 | no |
| pod start wait, total (s) | 1 | 1.2 | +20.0% | −2.1068 to +2.5068 | no |
| pod start wait, mean (s) | 0.75 | 0.55 | −26.7% | −1.4862 to +1.0862 | no |
| host CPU busy, the real machine under kind (%) | 44.41 | 47.72 | +7.4% | +2.8297 to +3.7756 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.1 | 839.4 | +1.7% | +5.9851 to +22.6149 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.415 | −26.4% | −2.8240 to −0.3452 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.3083 | +196.0% | −0.0001 to +0.4085 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.4 | +380.0% | −0.6558 to +4.4558 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.5 | 146 | +11.9% | +7.2272 to +23.7395 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*