# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.623 | 6 |
| node-hours | 2.512 | 2.515 | 1.941 | 2.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.8 | 271.2 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.8 | 227.9 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 241.7 | 124.7 | 227.3 | 102.4 |
| response time (ms), 95th percentile | 758.2 | 218.8 | 856.4 | 225.8 |
| response time (ms), 99th percentile | 1057 | 316.6 | 1224 | 334.8 |
| time over the response line (% of samples) | 8.662 | 0.1528 | 9.276 | 0.1568 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 0 | 7.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 169.7 | 94.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.343 | 1036 | 8.783 | 1131 |
| utilisation (used / allocatable) | 0.05631 | 0.05935 | 0.07393 | 0.05819 |
| CPU used (cores), mean | 1.351 | 1.424 | 1.32 | 1.397 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06925 | 0.0651 |
| CPU used with Omni's own (cores), mean | 1.351 | 1.424 | 1.389 | 1.462 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.7 | 455.8 | 411.3 | 463.8 |
| HPA replicas, mean | 1.984 | 2.036 | 2.305 | 2.048 |
| pods started | 0 | 0 | 1.3 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 2.7 | 1.1 |
| pod start wait, mean (s) | 0 | 0 | 1.35 | 0.375 |
| host CPU busy, the real machine under kind (%) | 38.85 | 43.97 | 41.4 | 46.22 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 748 | 1434 | 753.7 | 1482 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.866 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 136.1 | 0.03333 | 166.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 615.1 | 0.2 | 754.6 |
| queue: job turnaround, submitted to done, mean (s) | 53.5 | 788.9 | 60 | 848.4 |
| queue: jobs unfinished at the window's end | 0 | 7.9 | 0 | 9.3 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.518 | +0.1% | −0.0056 to +0.0130 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.7 | −0.0% | −0.9460 to +0.8079 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.7 | −0.0% | −0.9460 to +0.8079 | no |
| response time (ms), mean | 124.7 | 102.4 | −17.9% | −27.7253 to −16.9459 | yes: GAIN |
| response time (ms), 95th percentile | 218.8 | 225.8 | +3.2% | −2.8231 to +16.7941 | no |
| response time (ms), 99th percentile | 316.6 | 334.8 | +5.8% | −6.0251 to +42.4891 | no |
| time over the response line (% of samples) | 0.1528 | 0.1568 | +2.6% | −0.0784 to +0.0864 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 94.4 | +94.400 (native is 0) | +82.8306 to +105.9694 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1036 | 1131 | +9.2% | +20.8920 to +169.5080 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05935 | 0.05819 | −1.9% | −0.0026 to +0.0003 | no |
| CPU used (cores), mean | 1.424 | 1.397 | −1.9% | −0.0623 to +0.0069 | no |
| Omni's own CPU (cores), mean | 0 | 0.0651 | +0.065 (native is 0) | +0.0581 to +0.0721 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.424 | 1.462 | +2.6% | +0.0041 to +0.0706 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.8 | 463.8 | +1.8% | −2.6995 to +18.8781 | no |
| HPA replicas, mean | 2.036 | 2.048 | +0.6% | −0.2391 to +0.2628 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.6342 to +2.8342 | no |
| pod start wait, mean (s) | 0 | 0.375 | +0.375 (native is 0) | −0.1921 to +0.9421 | no |
| host CPU busy, the real machine under kind (%) | 43.97 | 46.22 | +5.1% | +1.6531 to +2.8431 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1434 | 1482 | +3.3% | −6.9326 to +101.3326 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 136.1 | 166.4 | +22.3% | −19.6633 to +80.2549 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 615.1 | 754.6 | +22.7% | −67.6688 to +346.6688 | no |
| queue: job turnaround, submitted to done, mean (s) | 788.9 | 848.4 | +7.5% | −3.1595 to +122.1845 | no |
| queue: jobs unfinished at the window's end | 7.9 | 9.3 | +17.7% | −1.2379 to +4.0379 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.514 | +0.1% | −0.0071 to +0.0115 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.8 | +0.4% | −1.0511 to +2.9866 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.8 | +0.4% | −1.0511 to +2.9866 | no |
| response time (ms), mean | 241.7 | 124.7 | −48.4% | −224.7616 to −9.3103 | yes: GAIN |
| response time (ms), 95th percentile | 758.2 | 218.8 | −71.1% | −1054.3252 to −24.4158 | yes: GAIN |
| response time (ms), 99th percentile | 1057 | 316.6 | −70.1% | −1415.4230 to −65.9224 | yes: GAIN |
| time over the response line (% of samples) | 8.662 | 0.1528 | −98.2% | −17.3945 to +0.3756 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 0 | −100.0% | −10.5497 to −2.6503 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.343 | 1036 | +12314.2% | +796.6158 to +1258.2076 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05631 | 0.05935 | +5.4% | −0.0021 to +0.0082 | no |
| CPU used (cores), mean | 1.351 | 1.424 | +5.4% | −0.0510 to +0.1971 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.351 | 1.424 | +5.4% | −0.0510 to +0.1971 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.7 | 455.8 | −6.0% | −66.0926 to +8.1574 | no |
| HPA replicas, mean | 1.984 | 2.036 | +2.6% | −0.1106 to +0.2150 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 38.85 | 43.97 | +13.2% | +2.5982 to +7.6451 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748 | 1434 | +91.8% | +614.0362 to +758.5638 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 136.1 | +362711.1% | +102.0845 to +169.9489 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 615.1 | +307450.0% | +426.4837 to +803.3163 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 53.5 | 788.9 | +1374.6% | +610.7621 to +860.0379 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 7.9 | +7.900 (native is 0) | +1.9016 to +13.8984 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.623 | −23.0% | −2.2412 to −0.5129 | yes: GAIN |
| node-hours | 2.512 | 1.941 | −22.7% | −0.9341 to −0.2084 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.2 | +0.1% | −0.3542 to +1.1443 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 227.9 | −15.8% | −70.4593 to −15.3672 | yes: GAIN |
| response time (ms), mean | 241.7 | 227.3 | −5.9% | −30.0740 to +1.3202 | no |
| response time (ms), 95th percentile | 758.2 | 856.4 | +13.0% | −5.4666 to +201.9146 | no |
| response time (ms), 99th percentile | 1057 | 1224 | +15.8% | −26.7582 to +360.9278 | no |
| time over the response line (% of samples) | 8.662 | 9.276 | +7.1% | −0.3391 to +1.5659 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.2 | +9.1% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 169.7 | +169.700 (native is 0) | +96.1898 to +243.2102 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.343 | 8.783 | +5.3% | −0.6207 to +1.5007 | no |
| utilisation (used / allocatable) | 0.05631 | 0.07393 | +31.3% | +0.0055 to +0.0297 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.351 | 1.32 | −2.3% | −0.0706 to +0.0076 | no |
| Omni's own CPU (cores), mean | 0 | 0.06925 | +0.069 (native is 0) | +0.0631 to +0.0754 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.351 | 1.389 | +2.8% | −0.0067 to +0.0822 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.7 | 411.3 | −15.1% | −120.3235 to −26.4350 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.984 | 2.305 | +16.2% | +0.1675 to +0.4751 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.4706 to +2.1294 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.6475 to +4.7525 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.35 | +1.350 (native is 0) | +0.6120 to +2.0880 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.85 | 41.4 | +6.6% | +1.7555 to +3.3558 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748 | 753.7 | +0.8% | −2.5806 to +13.9806 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.866 | −35.6% | −3.3546 to −0.9140 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.03333 | −11.1% | −0.0262 to +0.0178 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 53.5 | 60 | +12.2% | −1.8111 to +14.8194 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.623 | −23.0% | −2.2412 to −0.5129 | yes: GAIN |
| node-hours | 2.515 | 1.941 | −22.8% | −0.9364 to −0.2105 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.2 | −0.2% | −2.8213 to +1.6759 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 227.9 | −16.1% | −72.6160 to −15.1461 | yes: GAIN |
| response time (ms), mean | 124.7 | 227.3 | +82.3% | −19.6670 to +224.9851 | no |
| response time (ms), 95th percentile | 218.8 | 856.4 | +291.4% | +25.8681 to +1249.3209 | yes: LOSS |
| response time (ms), 99th percentile | 316.6 | 1224 | +286.8% | +41.9585 to +1773.5565 | yes: LOSS |
| time over the response line (% of samples) | 0.1528 | 9.276 | +5968.9% | +0.3603 to +17.8854 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 7.2 | +7.200 (native is 0) | +3.1145 to +11.2855 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 169.7 | +169.700 (native is 0) | +96.1898 to +243.2102 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1036 | 8.783 | −99.2% | −1258.0650 to −795.8784 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05935 | 0.07393 | +24.6% | +0.0051 to +0.0240 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.424 | 1.32 | −7.3% | −0.2535 to +0.0444 | no |
| Omni's own CPU (cores), mean | 0 | 0.06925 | +0.069 (native is 0) | +0.0631 to +0.0754 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.424 | 1.389 | −2.5% | −0.1894 to +0.1188 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.8 | 411.3 | −9.7% | −74.8808 to −13.9424 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.036 | 2.305 | +13.2% | +0.0606 to +0.4776 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.4706 to +2.1294 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.6475 to +4.7525 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.35 | +1.350 (native is 0) | +0.6120 to +2.0880 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.97 | 41.4 | −5.8% | −5.6664 to +0.5344 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1434 | 753.7 | −47.5% | −753.5537 to −607.6463 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.193 | −63.5% | −4.3562 to −3.2584 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 136.1 | 0.03333 | −100.0% | −169.9636 to −102.0780 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 615.1 | 0.2 | −100.0% | −803.3163 to −426.4837 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 788.9 | 60 | −92.4% | −848.3667 to −609.4250 | yes: GAIN |
| queue: jobs unfinished at the window's end | 7.9 | 0 | −100.0% | −13.8984 to −1.9016 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.518 | +0.2% | −0.0004 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.7 | +0.3% | −1.3035 to +3.1008 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.7 | +0.3% | −1.3035 to +3.1008 | no |
| response time (ms), mean | 241.7 | 102.4 | −57.7% | −249.2577 to −29.4854 | yes: GAIN |
| response time (ms), 95th percentile | 758.2 | 225.8 | −70.2% | −1046.4317 to −18.3383 | yes: GAIN |
| response time (ms), 99th percentile | 1057 | 334.8 | −68.3% | −1399.1007 to −45.7807 | yes: GAIN |
| time over the response line (% of samples) | 8.662 | 0.1568 | −98.2% | −17.3785 to +0.3675 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 0 | −100.0% | −10.5497 to −2.6503 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 94.4 | +94.400 (native is 0) | +82.8306 to +105.9694 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.343 | 1131 | +13455.2% | +916.7299 to +1328.4935 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05631 | 0.05819 | +3.4% | −0.0033 to +0.0071 | no |
| CPU used (cores), mean | 1.351 | 1.397 | +3.4% | −0.0789 to +0.1695 | no |
| Omni's own CPU (cores), mean | 0 | 0.0651 | +0.065 (native is 0) | +0.0581 to +0.0721 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.351 | 1.462 | +8.2% | −0.0071 to +0.2279 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.7 | 463.8 | −4.3% | −58.9762 to +17.2196 | no |
| HPA replicas, mean | 1.984 | 2.048 | +3.2% | −0.1396 to +0.2677 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.6342 to +2.8342 | no |
| pod start wait, mean (s) | 0 | 0.375 | +0.375 (native is 0) | −0.1921 to +0.9421 | no |
| host CPU busy, the real machine under kind (%) | 38.85 | 46.22 | +19.0% | +4.8491 to +9.8903 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748 | 1482 | +98.1% | +681.8686 to +785.1314 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 166.3 | +443500.0% | +122.0720 to +210.5530 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 754.6 | +377200.0% | +627.9593 to +880.8407 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 53.5 | 848.4 | +1485.8% | +709.1950 to +880.6300 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.3 | +9.300 (native is 0) | +4.2527 to +14.3473 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*