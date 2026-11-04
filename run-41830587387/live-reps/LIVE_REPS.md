# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.02 | 6.203 |
| node-hours | 5.027 | 5.029 | 4.623 | 2.605 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 504.9 | 526.8 | 506.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 504.9 | 495.8 | 323.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 768.3 | 126.8 | 850.7 | 75.55 |
| response time (ms), 95th percentile | 3087 | 171.8 | 3386 | 99.15 |
| response time (ms), 99th percentile | 4201 | 195.3 | 4622 | 131.7 |
| time over the response line (% of samples) | 27.14 | 0 | 30.97 | 0 |
| failed requests (%) | 0 | 0 | 0.02252 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 0 | 14.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 115.3 | 33.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 12.31 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.7 | 0 | 54.53 | 0.05333 |
| utilisation (used / allocatable) | 0.0373 | 0.006186 | 0.03799 | 0.01013 |
| CPU used (cores), mean | 1.791 | 0.2969 | 1.654 | 0.2516 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0556 | 0.03257 |
| CPU used with Omni's own (cores), mean | 1.791 | 0.2969 | 1.71 | 0.2842 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 724.2 | 4163 | 718.7 | 3160 |
| HPA replicas, mean | 3.966 | 4.139 | 4.879 | 4.61 |
| pods started | 0.2 | 0.5 | 3.5 | 1.9 |
| pod start wait, total (s) | 0.4 | 0.7 | 8 | 2.8 |
| pod start wait, mean (s) | 0.4 | 0.65 | 1.808 | 1.467 |
| host CPU busy, the real machine under kind (%) | 54.22 | 15.04 | 60.49 | 18.12 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 932.5 | 1506 | 987.3 | 1511 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.34 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1159 | 0.1917 | 1164 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1475 | 0.8 | 1480 |
| queue: job turnaround, submitted to done, mean (s) | 237.8 | 1159 | 294.4 | 1164 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |
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
| worker nodes in service, mean | 12 | 6.203 | −48.3% | −5.8564 to −5.7379 | yes: GAIN |
| node-hours | 5.029 | 2.605 | −48.2% | −2.4528 to −2.3955 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.9 | 506.2 | +0.3% | +0.7292 to +1.8204 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.9 | 323.6 | −35.9% | −183.5591 to −179.1162 | yes: GAIN |
| response time (ms), mean | 126.8 | 75.55 | −40.4% | −62.4715 to −40.0641 | yes: GAIN |
| response time (ms), 95th percentile | 171.8 | 99.15 | −42.3% | −84.6460 to −60.7260 | yes: GAIN |
| response time (ms), 99th percentile | 195.3 | 131.7 | −32.6% | −74.4149 to −52.7663 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +30.6404 to +36.9596 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05333 | +0.053 (native is 0) | −0.0673 to +0.1740 | no |
| utilisation (used / allocatable) | 0.006186 | 0.01013 | +63.7% | +0.0034 to +0.0045 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2969 | 0.2516 | −15.3% | −0.0526 to −0.0380 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03257 | +0.033 (native is 0) | +0.0286 to +0.0365 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2969 | 0.2842 | −4.3% | −0.0195 to −0.0060 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4163 | 3160 | −24.1% | −1127.9830 to −878.5579 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.139 | 4.61 | +11.4% | +0.1241 to +0.8185 | yes: power given |
| pods started | 0.5 | 1.9 | +280.0% | +0.0428 to +2.7572 | yes: power given |
| pod start wait, total (s) | 0.7 | 2.8 | +300.0% | +0.5383 to +3.6617 | yes: LOSS |
| pod start wait, mean (s) | 0.65 | 1.467 | +125.6% | −0.1127 to +1.7460 | no |
| host CPU busy, the real machine under kind (%) | 15.04 | 18.12 | +20.5% | +2.5027 to +3.6522 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1511 | +0.3% | +3.2393 to +6.9607 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1164 | +0.5% | +3.4184 to +7.0232 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1480 | +0.4% | +3.3904 to +7.0096 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1164 | +0.5% | +3.4184 to +7.0232 | yes: LOSS |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.027 | 5.029 | +0.0% | −0.0121 to +0.0161 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 504.9 | −4.3% | −26.7051 to −18.6409 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 504.9 | −4.3% | −26.7051 to −18.6409 | yes: GAIN |
| response time (ms), mean | 768.3 | 126.8 | −83.5% | −969.9652 to −312.9728 | yes: GAIN |
| response time (ms), 95th percentile | 3087 | 171.8 | −94.4% | −4444.6301 to −1385.6309 | yes: GAIN |
| response time (ms), 99th percentile | 4201 | 195.3 | −95.4% | −6070.7525 to −1941.0657 | yes: GAIN |
| time over the response line (% of samples) | 27.14 | 0 | −100.0% | −38.4755 to −15.8133 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 0 | −100.0% | −18.3247 to −8.2753 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.7 | 0 | −100.0% | −24.0998 to −11.3069 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0373 | 0.006186 | −83.4% | −0.0351 to −0.0271 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.791 | 0.2969 | −83.4% | −1.6846 to −1.3026 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.791 | 0.2969 | −83.4% | −1.6846 to −1.3026 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 724.2 | 4163 | +474.9% | +2995.1765 to +3883.2881 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.966 | 4.139 | +4.4% | −0.0464 to +0.3924 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.4 | 0.7 | +75.0% | −0.8209 to +1.4209 | no |
| pod start wait, mean (s) | 0.4 | 0.65 | +62.5% | −0.8841 to +1.3841 | no |
| host CPU busy, the real machine under kind (%) | 54.22 | 15.04 | −72.3% | −44.5485 to −33.8087 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 932.5 | 1506 | +61.5% | +456.0990 to +690.1010 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1159 | +1112620.0% | +1156.6065 to +1161.3519 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1475 | +294960.0% | +1472.3267 to +1477.2733 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 237.8 | 1159 | +387.4% | +807.9071 to +1034.6846 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.02 | −8.2% | −2.3045 to +0.3382 | no |
| node-hours | 5.027 | 4.623 | −8.0% | −0.9581 to +0.1501 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 526.8 | −0.2% | −2.7270 to +1.1435 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 495.8 | −6.0% | −72.5820 to +9.0485 | no |
| response time (ms), mean | 768.3 | 850.7 | +10.7% | +21.5443 to +143.2128 | yes: LOSS |
| response time (ms), 95th percentile | 3087 | 3386 | +9.7% | −16.1974 to +613.8194 | no |
| response time (ms), 99th percentile | 4201 | 4622 | +10.0% | −23.4774 to +865.1954 | no |
| time over the response line (% of samples) | 27.14 | 30.97 | +14.1% | +1.6526 to +6.0016 | yes: LOSS |
| failed requests (%) | 0 | 0.02252 | +0.023 (native is 0) | −0.0134 to +0.0584 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 14.7 | +10.5% | +0.1293 to +2.6707 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.3 | +115.300 (native is 0) | +55.6338 to +174.9662 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.7 | 54.53 | +208.0% | +0.2854 to +73.3712 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0373 | 0.03799 | +1.8% | −0.0057 to +0.0071 | no |
| CPU used (cores), mean | 1.791 | 1.654 | −7.6% | −0.2652 to −0.0069 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0556 | +0.056 (native is 0) | +0.0491 to +0.0621 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.791 | 1.71 | −4.5% | −0.2064 to +0.0455 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 724.2 | 718.7 | −0.8% | −103.2309 to +92.0764 | no |
| HPA replicas, mean | 3.966 | 4.879 | +23.0% | +0.6094 to +1.2173 | yes: power given |
| pods started | 0.2 | 3.5 | +1650.0% | +1.3615 to +5.2385 | yes: power given |
| pod start wait, total (s) | 0.4 | 8 | +1900.0% | +3.1623 to +12.0377 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.808 | +352.1% | +0.4044 to +2.4123 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.22 | 60.49 | +11.5% | +4.9715 to +7.5525 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 932.5 | 987.3 | +5.9% | +27.7529 to +81.8471 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.34 | −13.8% | −3.6561 to +0.3445 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.1917 | +84.0% | −0.0279 to +0.2029 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | −0.2889 to +0.8889 | no |
| queue: job turnaround, submitted to done, mean (s) | 237.8 | 294.4 | +23.8% | +25.0146 to +88.2688 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.02 | −8.2% | −2.3045 to +0.3382 | no |
| node-hours | 5.029 | 4.623 | −8.1% | −0.9655 to +0.1535 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.9 | 526.8 | +4.3% | +19.2735 to +24.4890 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.9 | 495.8 | −1.8% | −52.9029 to +34.7154 | no |
| response time (ms), mean | 126.8 | 850.7 | +570.8% | +346.3038 to +1101.3915 | yes: LOSS |
| response time (ms), 95th percentile | 171.8 | 3386 | +1870.4% | +1591.7529 to +4836.1301 | yes: LOSS |
| response time (ms), 99th percentile | 195.3 | 4622 | +2266.3% | +2250.8049 to +6602.7313 | yes: LOSS |
| time over the response line (% of samples) | 0 | 30.97 | +30.971 (native is 0) | +18.5598 to +43.3831 | yes: LOSS |
| failed requests (%) | 0 | 0.02252 | +0.023 (native is 0) | −0.0134 to +0.0584 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14.7 | +14.700 (native is 0) | +9.9666 to +19.4334 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.3 | +115.300 (native is 0) | +55.6338 to +174.9662 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 54.53 | +54.532 (native is 0) | +12.9429 to +96.1204 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006186 | 0.03799 | +514.1% | +0.0281 to +0.0355 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2969 | 1.654 | +457.2% | +1.2015 to +1.5137 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0556 | +0.056 (native is 0) | +0.0491 to +0.0621 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2969 | 1.71 | +476.0% | +1.2523 to +1.5740 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4163 | 718.7 | −82.7% | −3978.6254 to −2910.9938 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.139 | 4.879 | +17.9% | +0.3105 to +1.1702 | yes: power given |
| pods started | 0.5 | 3.5 | +600.0% | +0.9214 to +5.0786 | yes: power given |
| pod start wait, total (s) | 0.7 | 8 | +1042.9% | +2.9548 to +11.6452 | yes: LOSS |
| pod start wait, mean (s) | 0.65 | 1.808 | +178.2% | +0.0300 to +2.2867 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.04 | 60.49 | +302.0% | +39.0377 to +51.8434 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 987.3 | −34.4% | −660.4721 to −376.1279 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.1917 | −100.0% | −1161.3032 to −1156.4802 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.8 | −99.9% | −1477.1390 to −1471.8610 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 294.4 | −74.6% | −1006.0640 to −723.2443 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.203 | −48.3% | −5.8564 to −5.7379 | yes: GAIN |
| node-hours | 5.027 | 2.605 | −48.2% | −2.4399 to −2.4044 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 506.2 | −4.1% | −25.1300 to −17.6664 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 323.6 | −38.7% | −206.2436 to −201.7777 | yes: GAIN |
| response time (ms), mean | 768.3 | 75.55 | −90.2% | −1031.1845 to −354.2892 | yes: GAIN |
| response time (ms), 95th percentile | 3087 | 99.15 | −96.8% | −4525.2870 to −1450.3460 | yes: GAIN |
| response time (ms), 99th percentile | 4201 | 131.7 | −96.9% | −6139.7888 to −1999.2106 | yes: GAIN |
| time over the response line (% of samples) | 27.14 | 0 | −100.0% | −38.4755 to −15.8133 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 0 | −100.0% | −18.3247 to −8.2753 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +30.6404 to +36.9596 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.7 | 0.05333 | −99.7% | −24.0206 to −11.2794 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0373 | 0.01013 | −72.8% | −0.0307 to −0.0236 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.791 | 0.2516 | −85.9% | −1.7335 to −1.3443 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03257 | +0.033 (native is 0) | +0.0286 to +0.0365 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.791 | 0.2842 | −84.1% | −1.6972 to −1.3155 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 724.2 | 3160 | +336.3% | +2067.0875 to +2804.8361 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.966 | 4.61 | +16.2% | +0.3644 to +0.9243 | yes: power given |
| pods started | 0.2 | 1.9 | +850.0% | +0.3491 to +3.0509 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.8 | +600.0% | +0.5469 to +4.2531 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.467 | +266.7% | −0.0059 to +2.1392 | no |
| host CPU busy, the real machine under kind (%) | 54.22 | 18.12 | −66.6% | −41.1330 to −31.0693 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 932.5 | 1511 | +62.0% | +461.0997 to +695.3003 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1164 | +1117632.0% | +1162.0642 to +1166.3358 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1480 | +296000.0% | +1477.8147 to +1482.1853 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 237.8 | 1164 | +389.6% | +813.1617 to +1039.8717 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*