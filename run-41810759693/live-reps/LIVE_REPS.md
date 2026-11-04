# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.125 | 5.066 |
| node-hours | 2.517 | 2.514 | 2.152 | 2.124 |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.2 | 274.1 | 274.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 274.2 | 246.6 | 245.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 421 | 487.5 | 399.9 | 472 |
| response time (ms), 95th percentile | 1548 | 2033 | 1648 | 2186 |
| response time (ms), 99th percentile | 2202 | 2734 | 2253 | 2917 |
| time over the response line (% of samples) | 17.61 | 16.53 | 17.86 | 16.73 |
| failed requests (%) | 0 | 0 | 0 | 0.01163 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.7 | 10.1 | 11.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 124.9 | 78.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.01 | 35.41 | 15.03 | 40.29 |
| utilisation (used / allocatable) | 0.0635 | 0.06418 | 0.07397 | 0.07718 |
| CPU used (cores), mean | 1.524 | 1.54 | 1.504 | 1.557 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07362 | 0.07988 |
| CPU used with Omni's own (cores), mean | 1.524 | 1.54 | 1.578 | 1.637 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.8 | 436.6 | 397.1 | 379.4 |
| HPA replicas, mean | 2.064 | 1.959 | 2.525 | 2.195 |
| pods started | 0 | 0.2 | 2 | 0.9 |
| pod start wait, total (s) | 0 | 0.3 | 4.3 | 2 |
| pod start wait, mean (s) | 0 | 0.3 | 1.775 | 0.7833 |
| host CPU busy, the real machine under kind (%) | 43.42 | 46.87 | 46.39 | 50.41 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 809.9 | 861.1 | 818.1 | 875.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.334 | 4.233 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 1.317 | 0.3375 | 1.554 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 3.5 | 1.4 | 5.1 |
| queue: job turnaround, submitted to done, mean (s) | 116 | 161.3 | 121.8 | 171.1 |
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
| worker nodes in service, mean | 6 | 5.066 | −15.6% | −1.5923 to −0.2758 | yes: GAIN |
| node-hours | 2.514 | 2.124 | −15.5% | −0.6632 to −0.1172 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.7 | +0.2% | −0.3411 to +1.3712 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 245.3 | −10.5% | −49.2583 to −8.5366 | yes: GAIN |
| response time (ms), mean | 487.5 | 472 | −3.2% | −33.9076 to +2.8365 | no |
| response time (ms), 95th percentile | 2033 | 2186 | +7.5% | +21.1480 to +285.3820 | yes: LOSS |
| response time (ms), 99th percentile | 2734 | 2917 | +6.7% | −20.8393 to +387.5125 | no |
| time over the response line (% of samples) | 16.53 | 16.73 | +1.2% | −1.3528 to +1.7512 | no |
| failed requests (%) | 0 | 0.01163 | +0.012 (native is 0) | −0.0147 to +0.0379 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11.3 | +5.6% | −0.0032 to +1.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.3 | +78.300 (native is 0) | +39.8947 to +116.7053 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.41 | 40.29 | +13.8% | −0.9606 to +10.7273 | no |
| utilisation (used / allocatable) | 0.06418 | 0.07718 | +20.3% | +0.0035 to +0.0225 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.54 | 1.557 | +1.1% | −0.0059 to +0.0389 | no |
| Omni's own CPU (cores), mean | 0 | 0.07988 | +0.080 (native is 0) | +0.0714 to +0.0883 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.54 | 1.637 | +6.3% | +0.0699 to +0.1228 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.6 | 379.4 | −13.1% | −98.6217 to −15.8923 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.959 | 2.195 | +12.1% | −0.0217 to +0.4944 | no |
| pods started | 0.2 | 0.9 | +350.0% | −0.3144 to +1.7144 | no |
| pod start wait, total (s) | 0.3 | 2 | +566.7% | −0.8245 to +4.2245 | no |
| pod start wait, mean (s) | 0.3 | 0.7833 | +161.1% | −0.4810 to +1.4477 | no |
| host CPU busy, the real machine under kind (%) | 46.87 | 50.41 | +7.6% | +2.9714 to +4.1172 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 861.1 | 875.1 | +1.6% | +5.7956 to +22.2044 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.233 | −29.5% | −2.8001 to −0.7345 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.317 | 1.554 | +18.0% | −0.0576 to +0.5326 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.5 | 5.1 | +45.7% | −0.7891 to +3.9891 | no |
| queue: job turnaround, submitted to done, mean (s) | 161.3 | 171.1 | +6.1% | +4.1491 to +15.4509 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.514 | −0.1% | −0.0082 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.2 | +0.1% | −0.5762 to +0.9289 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 274.2 | +0.1% | −0.5762 to +0.9289 | no |
| response time (ms), mean | 421 | 487.5 | +15.8% | +13.7207 to +119.3812 | yes: LOSS |
| response time (ms), 95th percentile | 1548 | 2033 | +31.3% | +112.5304 to +857.1106 | yes: LOSS |
| response time (ms), 99th percentile | 2202 | 2734 | +24.1% | +146.3364 to +915.9310 | yes: LOSS |
| time over the response line (% of samples) | 17.61 | 16.53 | −6.1% | −2.6786 to +0.5177 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.7 | +10.3% | +0.1079 to +1.8921 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.01 | 35.41 | +152.7% | +7.7870 to +35.0030 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0635 | 0.06418 | +1.1% | −0.0004 to +0.0017 | no |
| CPU used (cores), mean | 1.524 | 1.54 | +1.1% | −0.0088 to +0.0415 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.524 | 1.54 | +1.1% | −0.0088 to +0.0415 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.8 | 436.6 | −0.5% | −9.6438 to +5.2059 | no |
| HPA replicas, mean | 2.064 | 1.959 | −5.1% | −0.2275 to +0.0174 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 43.42 | 46.87 | +7.9% | +2.2085 to +4.6837 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.9 | 861.1 | +6.3% | +14.4750 to +87.9250 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 1.317 | +731.6% | +0.7086 to +1.6081 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 3.5 | +150.0% | −0.2228 to +4.4228 | no |
| queue: job turnaround, submitted to done, mean (s) | 116 | 161.3 | +39.1% | +16.6437 to +74.0313 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.125 | −14.6% | −1.4651 to −0.2839 | yes: GAIN |
| node-hours | 2.517 | 2.152 | −14.5% | −0.6164 to −0.1131 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.1 | +0.0% | −0.9372 to +1.1771 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 246.6 | −10.0% | −46.6772 to −8.0455 | yes: GAIN |
| response time (ms), mean | 421 | 399.9 | −5.0% | −31.7297 to −10.4339 | yes: GAIN |
| response time (ms), 95th percentile | 1548 | 1648 | +6.4% | −2.3650 to +201.6590 | no |
| response time (ms), 99th percentile | 2202 | 2253 | +2.3% | −71.7324 to +172.2068 | no |
| time over the response line (% of samples) | 17.61 | 17.86 | +1.4% | −0.2239 to +0.7109 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.1 | +4.1% | −0.7285 to +1.5285 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.9 | +124.900 (native is 0) | +52.7974 to +197.0026 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.01 | 15.03 | +7.3% | −0.8613 to +2.9047 | no |
| utilisation (used / allocatable) | 0.0635 | 0.07397 | +16.5% | +0.0027 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.504 | −1.3% | −0.0472 to +0.0079 | no |
| Omni's own CPU (cores), mean | 0 | 0.07362 | +0.074 (native is 0) | +0.0669 to +0.0804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.578 | +3.5% | +0.0204 to +0.0876 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.8 | 397.1 | −9.5% | −72.0408 to −11.4333 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.064 | 2.525 | +22.3% | +0.2477 to +0.6732 | yes: power given |
| pods started | 0 | 2 | +2.000 (native is 0) | +0.9337 to +3.0663 | yes: power given |
| pod start wait, total (s) | 0 | 4.3 | +4.300 (native is 0) | +1.8907 to +6.7093 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.775 | +1.775 (native is 0) | +1.0095 to +2.5405 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.42 | 46.39 | +6.8% | +2.5068 to +3.4338 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.9 | 818.1 | +1.0% | +1.0485 to +15.3515 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.334 | −27.8% | −2.4723 to −0.8600 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.3375 | +113.2% | −0.0867 to +0.4450 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.4 | ±0.0% | −1.5452 to +1.5452 | no |
| queue: job turnaround, submitted to done, mean (s) | 116 | 121.9 | +5.1% | +0.4019 to +11.3397 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.125 | −14.6% | −1.4651 to −0.2839 | yes: GAIN |
| node-hours | 2.514 | 2.152 | −14.4% | −0.6120 to −0.1125 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.1 | −0.0% | −0.6686 to +0.5558 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 246.6 | −10.0% | −46.3666 to −8.7088 | yes: GAIN |
| response time (ms), mean | 487.5 | 399.9 | −18.0% | −138.8689 to −36.3966 | yes: GAIN |
| response time (ms), 95th percentile | 2033 | 1648 | −18.9% | −699.1537 to −71.1933 | yes: GAIN |
| response time (ms), 99th percentile | 2734 | 2253 | −17.6% | −822.9900 to −138.8030 | yes: GAIN |
| time over the response line (% of samples) | 16.53 | 17.86 | +8.0% | −0.2706 to +2.9185 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.1 | −5.6% | −2.1888 to +0.9888 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.9 | +124.900 (native is 0) | +52.7974 to +197.0026 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.41 | 15.03 | −57.5% | −33.0956 to −7.6510 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06418 | 0.07397 | +15.3% | +0.0014 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.54 | 1.504 | −2.3% | −0.0556 to −0.0164 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07362 | +0.074 (native is 0) | +0.0669 to +0.0804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.54 | 1.578 | +2.4% | +0.0133 to +0.0619 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.6 | 397.1 | −9.1% | −74.9385 to −4.0976 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.959 | 2.525 | +28.9% | +0.3405 to +0.7905 | yes: power given |
| pods started | 0.2 | 2 | +900.0% | +0.7444 to +2.8556 | yes: power given |
| pod start wait, total (s) | 0.3 | 4.3 | +1333.3% | +1.6156 to +6.3844 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.775 | +491.7% | +0.7982 to +2.1518 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.87 | 46.39 | −1.0% | −1.4831 to +0.5316 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 861.1 | 818.1 | −5.0% | −74.7111 to −11.2889 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.334 | −27.8% | −2.4723 to −0.8600 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.317 | 0.3375 | −74.4% | −1.2488 to −0.7096 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.5 | 1.4 | −60.0% | −3.5086 to −0.6914 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 161.3 | 121.8 | −24.5% | −64.8243 to −14.1091 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.066 | −15.6% | −1.5923 to −0.2758 | yes: GAIN |
| node-hours | 2.517 | 2.124 | −15.6% | −0.6673 to −0.1181 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.7 | +0.3% | −0.0049 to +1.3876 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 245.3 | −10.5% | −49.4162 to −8.0261 | yes: GAIN |
| response time (ms), mean | 421 | 472 | +12.1% | −2.5295 to +104.5603 | no |
| response time (ms), 95th percentile | 1548 | 2186 | +41.2% | +190.5478 to +1085.6232 | yes: LOSS |
| response time (ms), 99th percentile | 2202 | 2917 | +32.4% | +207.1879 to +1221.7527 | yes: LOSS |
| time over the response line (% of samples) | 17.61 | 16.73 | −5.0% | −3.7307 to +1.9682 | no |
| failed requests (%) | 0 | 0.01163 | +0.012 (native is 0) | −0.0147 to +0.0379 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 11.3 | +16.5% | +0.5231 to +2.6769 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.3 | +78.300 (native is 0) | +39.8947 to +116.7053 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.01 | 40.29 | +187.6% | +8.5896 to +43.9671 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0635 | 0.07718 | +21.6% | +0.0048 to +0.0226 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.557 | +2.2% | +0.0084 to +0.0573 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07988 | +0.080 (native is 0) | +0.0714 to +0.0883 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.637 | +7.4% | +0.0817 to +0.1438 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.8 | 379.4 | −13.6% | −96.2870 to −22.6649 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.064 | 2.195 | +6.4% | −0.1847 to +0.4475 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.0204 to +1.8204 | no |
| pod start wait, total (s) | 0 | 2 | +2.000 (native is 0) | −0.3844 to +4.3844 | no |
| pod start wait, mean (s) | 0 | 0.7833 | +0.783 (native is 0) | −0.0273 to +1.5940 | no |
| host CPU busy, the real machine under kind (%) | 43.42 | 50.41 | +16.1% | +5.3919 to +8.5888 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.9 | 875.1 | +8.1% | +23.0423 to +107.3577 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.233 | −29.5% | −2.8001 to −0.7345 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 1.554 | +881.6% | +0.7033 to +2.0883 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 5.1 | +264.3% | −0.7868 to +8.1868 | no |
| queue: job turnaround, submitted to done, mean (s) | 116 | 171.1 | +47.5% | +23.8087 to +86.4663 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*