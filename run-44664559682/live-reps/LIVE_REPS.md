# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.515 | 1.514 | 1.514 | 1.515 | 1.514 | 1.515 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.8 | 157.7 | 157.7 | 157.8 | 157.6 | 157.7 | 157.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.8 | 157.7 | 157.7 | 157.8 | 157.6 | 157.7 | 157.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 124.4 | 68.06 | 67.55 | 67.83 | 68.24 | 67.96 | 68.18 | 68.63 |
| response time (ms), 95th percentile | 271 | 97.96 | 97.27 | 96.52 | 98.32 | 97.38 | 98.4 | 99.43 |
| response time (ms), 99th percentile | 446.2 | 130.5 | 127.7 | 126.7 | 125.3 | 133 | 133.1 | 133 |
| time over the response line (% of samples) | 1.28 | 0.01198 | 0 | 0.02424 | 0 | 0 | 0.03622 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | 16 | 17.6 | 17 | 15.9 | 18.3 | 18.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | nan | nan | nan | nan | 70 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.265 | 0.29 | 0.08167 | 0.155 | 0.2117 | 0.3217 | 0.24 |
| utilisation (used / allocatable) | 0.03321 | 0.03235 | 0.0322 | 0.03226 | 0.03263 | 0.03229 | 0.03234 | 0.03252 |
| CPU used (cores), mean | 0.797 | 0.7764 | 0.7727 | 0.7743 | 0.7831 | 0.7751 | 0.7762 | 0.7805 |
| Omni's own CPU (cores), mean | 0 | 0.03322 | 0.00558 | 0.00632 | 0.00707 | 0.01273 | 0.02295 | 0.06306 |
| CPU used with Omni's own (cores), mean | 0.797 | 0.8097 | 0.7783 | 0.7806 | 0.7902 | 0.7878 | 0.7991 | 0.8435 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 860.8 | 863 | 856.2 | 849.9 | 857.4 | 866 | 855.7 |
| HPA replicas, mean | 7.995 | 8.28 | 7.906 | 7.83 | 7.073 | 7.061 | 7.936 | 8.154 |
| pods started | 5.7 | 5.1 | 4.9 | 5.1 | 4.4 | 4.3 | 5 | 4.9 |
| pod start wait, total (s) | 8.8 | 7.2 | 7.3 | 7.7 | 6.6 | 7.1 | 7 | 6.9 |
| pod start wait, mean (s) | 1.525 | 1.436 | 1.56 | 1.47 | 1.497 | 1.617 | 1.433 | 1.4 |
| host CPU busy, the real machine under kind (%) | 24.63 | 25.38 | 24.19 | 24.32 | 24.52 | 24.47 | 24.94 | 26.51 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.515 | +0.1% | +0.0002 to +0.0032 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.8 | −0.0% | −0.4393 to +0.3568 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.8 | −0.0% | −0.4393 to +0.3568 | no |
| response time (ms), mean | 124.4 | 68.06 | −45.3% | −81.2938 to −31.4159 | yes: GAIN |
| response time (ms), 95th percentile | 271 | 97.96 | −63.8% | −241.7637 to −104.2603 | yes: GAIN |
| response time (ms), 99th percentile | 446.2 | 130.5 | −70.8% | −432.5738 to −198.8888 | yes: GAIN |
| time over the response line (% of samples) | 1.28 | 0.01198 | −99.1% | −2.4030 to −0.1338 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | +19.700 (native is 0) | +18.3919 to +21.0081 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.265 | +156.5% | −0.0380 to +0.3613 | no |
| utilisation (used / allocatable) | 0.03321 | 0.03235 | −2.6% | −0.0020 to +0.0003 | no |
| CPU used (cores), mean | 0.797 | 0.7764 | −2.6% | −0.0490 to +0.0079 | no |
| Omni's own CPU (cores), mean | 0 | 0.03322 | +0.033 (native is 0) | +0.0280 to +0.0385 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.797 | 0.8097 | +1.6% | −0.0112 to +0.0365 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 860.8 | +0.3% | −25.6468 to +30.0504 | no |
| HPA replicas, mean | 7.995 | 8.28 | +3.6% | −0.0225 to +0.5941 | no |
| pods started | 5.7 | 5.1 | −10.5% | −1.5656 to +0.3656 | no |
| pod start wait, total (s) | 8.8 | 7.2 | −18.2% | −4.6198 to +1.4198 | no |
| pod start wait, mean (s) | 1.525 | 1.436 | −5.8% | −0.6147 to +0.4371 | no |
| host CPU busy, the real machine under kind (%) | 24.63 | 25.38 | +3.1% | +0.2206 to +1.2839 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0007 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.5786 to +0.2384 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.5786 to +0.2384 | no |
| response time (ms), mean | 124.4 | 67.55 | −45.7% | −82.4510 to −31.2845 | yes: GAIN |
| response time (ms), 95th percentile | 271 | 97.27 | −64.1% | −242.7920 to −104.6110 | yes: GAIN |
| response time (ms), 99th percentile | 446.2 | 127.7 | −71.4% | −444.7222 to −192.2316 | yes: GAIN |
| time over the response line (% of samples) | 1.28 | 0 | −100.0% | −2.4247 to −0.1360 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16.000 (native is 0) | +14.9884 to +17.0116 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.29 | +180.6% | −0.0636 to +0.4370 | no |
| utilisation (used / allocatable) | 0.03321 | 0.0322 | −3.0% | −0.0023 to +0.0003 | no |
| CPU used (cores), mean | 0.797 | 0.7727 | −3.0% | −0.0552 to +0.0067 | no |
| Omni's own CPU (cores), mean | 0 | 0.00558 | +0.006 (native is 0) | +0.0047 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.797 | 0.7783 | −2.3% | −0.0488 to +0.0114 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 863 | +0.5% | −25.0804 to +33.7980 | no |
| HPA replicas, mean | 7.995 | 7.906 | −1.1% | −0.2986 to +0.1205 | no |
| pods started | 5.7 | 4.9 | −14.0% | −1.9081 to +0.3081 | no |
| pod start wait, total (s) | 8.8 | 7.3 | −17.0% | −3.3850 to +0.3850 | no |
| pod start wait, mean (s) | 1.525 | 1.56 | +2.3% | −0.3816 to +0.4520 | no |
| host CPU busy, the real machine under kind (%) | 24.63 | 24.19 | −1.8% | −1.1826 to +0.2991 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0017 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.6673 to +0.3433 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.6673 to +0.3433 | no |
| response time (ms), mean | 124.4 | 67.83 | −45.5% | −82.0867 to −31.0753 | yes: GAIN |
| response time (ms), 95th percentile | 271 | 96.52 | −64.4% | −243.7729 to −105.1221 | yes: GAIN |
| response time (ms), 99th percentile | 446.2 | 126.7 | −71.6% | −440.4400 to −198.6126 | yes: GAIN |
| time over the response line (% of samples) | 1.28 | 0.02424 | −98.1% | −2.3754 to −0.1368 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.6 | +17.600 (native is 0) | +15.7165 to +19.4835 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.08167 | −21.0% | −0.2285 to +0.1851 | no |
| utilisation (used / allocatable) | 0.03321 | 0.03226 | −2.8% | −0.0025 to +0.0006 | no |
| CPU used (cores), mean | 0.797 | 0.7743 | −2.8% | −0.0601 to +0.0147 | no |
| Omni's own CPU (cores), mean | 0 | 0.00632 | +0.006 (native is 0) | +0.0053 to +0.0073 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.797 | 0.7806 | −2.1% | −0.0529 to +0.0201 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 856.2 | −0.3% | −44.8963 to +40.0362 | no |
| HPA replicas, mean | 7.995 | 7.83 | −2.1% | −0.3801 to +0.0505 | no |
| pods started | 5.7 | 5.1 | −10.5% | −1.5048 to +0.3048 | no |
| pod start wait, total (s) | 8.8 | 7.7 | −12.5% | −2.7329 to +0.5329 | no |
| pod start wait, mean (s) | 1.525 | 1.47 | −3.7% | −0.3342 to +0.2227 | no |
| host CPU busy, the real machine under kind (%) | 24.63 | 24.32 | −1.2% | −1.2691 to +0.6554 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.515 | +0.1% | −0.0014 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.8 | −0.0% | −0.5015 to +0.4456 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.8 | −0.0% | −0.5015 to +0.4456 | no |
| response time (ms), mean | 124.4 | 68.24 | −45.2% | −81.9817 to −30.3714 | yes: GAIN |
| response time (ms), 95th percentile | 271 | 98.32 | −63.7% | −242.3564 to −102.9496 | yes: GAIN |
| response time (ms), 99th percentile | 446.2 | 125.3 | −71.9% | −445.9345 to −195.8691 | yes: GAIN |
| time over the response line (% of samples) | 1.28 | 0 | −100.0% | −2.4247 to −0.1360 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17.000 (native is 0) | +13.3839 to +20.6161 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.155 | +50.0% | −0.1168 to +0.2201 | no |
| utilisation (used / allocatable) | 0.03321 | 0.03263 | −1.7% | −0.0019 to +0.0008 | no |
| CPU used (cores), mean | 0.797 | 0.7831 | −1.7% | −0.0467 to +0.0189 | no |
| Omni's own CPU (cores), mean | 0 | 0.00707 | +0.007 (native is 0) | +0.0058 to +0.0083 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.797 | 0.7902 | −0.9% | −0.0385 to +0.0249 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 849.9 | −1.0% | −45.6599 to +28.2073 | no |
| HPA replicas, mean | 7.995 | 7.073 | −11.5% | −1.5270 to −0.3164 | yes: GAIN |
| pods started | 5.7 | 4.4 | −22.8% | −2.2567 to −0.3433 | yes: GAIN |
| pod start wait, total (s) | 8.8 | 6.6 | −25.0% | −4.7189 to +0.3189 | no |
| pod start wait, mean (s) | 1.525 | 1.497 | −1.9% | −0.4165 to +0.3594 | no |
| host CPU busy, the real machine under kind (%) | 24.63 | 24.52 | −0.4% | −0.9807 to +0.7628 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0028 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.6 | −0.2% | −0.7537 to +0.2669 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.6 | −0.2% | −0.7537 to +0.2669 | no |
| response time (ms), mean | 124.4 | 67.96 | −45.4% | −82.0469 to −30.8669 | yes: GAIN |
| response time (ms), 95th percentile | 271 | 97.38 | −64.1% | −242.7896 to −104.3934 | yes: GAIN |
| response time (ms), 99th percentile | 446.2 | 133 | −70.2% | −432.7420 to −193.6938 | yes: GAIN |
| time over the response line (% of samples) | 1.28 | 0 | −100.0% | −2.4247 to −0.1360 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 | +15.900 (native is 0) | +12.3884 to +19.4116 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.2117 | +104.8% | −0.0568 to +0.2735 | no |
| utilisation (used / allocatable) | 0.03321 | 0.03229 | −2.7% | −0.0025 to +0.0007 | no |
| CPU used (cores), mean | 0.797 | 0.7751 | −2.7% | −0.0597 to +0.0159 | no |
| Omni's own CPU (cores), mean | 0 | 0.01273 | +0.013 (native is 0) | +0.0106 to +0.0148 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.797 | 0.7878 | −1.2% | −0.0451 to +0.0268 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 857.4 | −0.1% | −45.3701 to +43.0033 | no |
| HPA replicas, mean | 7.995 | 7.061 | −11.7% | −1.6509 to −0.2166 | yes: GAIN |
| pods started | 5.7 | 4.3 | −24.6% | −2.5285 to −0.2715 | yes: GAIN |
| pod start wait, total (s) | 8.8 | 7.1 | −19.3% | −3.7246 to +0.3246 | no |
| pod start wait, mean (s) | 1.525 | 1.617 | +6.0% | −0.3083 to +0.4911 | no |
| host CPU busy, the real machine under kind (%) | 24.63 | 24.47 | −0.7% | −0.9986 to +0.6766 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.515 | +0.1% | −0.0012 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.4371 to +0.1832 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.4371 to +0.1832 | no |
| response time (ms), mean | 124.4 | 68.18 | −45.2% | −80.4683 to −32.0122 | yes: GAIN |
| response time (ms), 95th percentile | 271 | 98.4 | −63.7% | −240.2059 to −104.9341 | yes: GAIN |
| response time (ms), 99th percentile | 446.2 | 133.1 | −70.2% | −428.7229 to −197.5739 | yes: GAIN |
| time over the response line (% of samples) | 1.28 | 0.03622 | −97.2% | −2.3632 to −0.1250 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | +18.300 (native is 0) | +17.7111 to +18.8889 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.3217 | +211.3% | −0.0870 to +0.5237 | no |
| utilisation (used / allocatable) | 0.03321 | 0.03234 | −2.6% | −0.0019 to +0.0001 | no |
| CPU used (cores), mean | 0.797 | 0.7762 | −2.6% | −0.0446 to +0.0030 | no |
| Omni's own CPU (cores), mean | 0 | 0.02295 | +0.023 (native is 0) | +0.0191 to +0.0268 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.797 | 0.7991 | +0.3% | −0.0184 to +0.0226 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 866 | +0.9% | −16.6865 to +31.4670 | no |
| HPA replicas, mean | 7.995 | 7.936 | −0.7% | −0.2858 to +0.1695 | no |
| pods started | 5.7 | 5 | −12.3% | −1.4578 to +0.0578 | no |
| pod start wait, total (s) | 8.8 | 7 | −20.5% | −4.4076 to +0.8076 | no |
| pod start wait, mean (s) | 1.525 | 1.433 | −6.0% | −0.5639 to +0.3801 | no |
| host CPU busy, the real machine under kind (%) | 24.63 | 24.94 | +1.3% | −0.1292 to +0.7575 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0060 to +0.0057 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.8642 to +0.5443 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.8642 to +0.5443 | no |
| response time (ms), mean | 124.4 | 68.63 | −44.8% | −80.3765 to −31.1861 | yes: GAIN |
| response time (ms), 95th percentile | 271 | 99.43 | −63.3% | −238.7250 to −104.3590 | yes: GAIN |
| response time (ms), 99th percentile | 446.2 | 133 | −70.2% | −426.0695 to −200.3663 | yes: GAIN |
| time over the response line (% of samples) | 1.28 | 0 | −100.0% | −2.4247 to −0.1360 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.700 (native is 0) | +17.7433 to +19.6567 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.24 | +132.3% | −0.0849 to +0.3582 | no |
| utilisation (used / allocatable) | 0.03321 | 0.03252 | −2.1% | −0.0020 to +0.0006 | no |
| CPU used (cores), mean | 0.797 | 0.7805 | −2.1% | −0.0473 to +0.0142 | no |
| Omni's own CPU (cores), mean | 0 | 0.06306 | +0.063 (native is 0) | +0.0537 to +0.0724 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.797 | 0.8435 | +5.8% | +0.0233 to +0.0697 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.6 | 855.7 | −0.3% | −36.1679 to +30.3540 | no |
| HPA replicas, mean | 7.995 | 8.154 | +2.0% | −0.0502 to +0.3693 | no |
| pods started | 5.7 | 4.9 | −14.0% | −1.8556 to +0.2556 | no |
| pod start wait, total (s) | 8.8 | 6.9 | −21.6% | −4.3421 to +0.5421 | no |
| pod start wait, mean (s) | 1.525 | 1.4 | −8.2% | −0.4831 to +0.2331 | no |
| host CPU busy, the real machine under kind (%) | 24.63 | 26.51 | +7.6% | +1.3726 to +2.3900 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0018 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.7 | −0.1% | −0.2528 to −0.0049 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.7 | −0.1% | −0.2528 to −0.0049 | yes: GAIN |
| response time (ms), mean | 68.06 | 67.55 | −0.8% | −1.4383 to +0.4125 | no |
| response time (ms), 95th percentile | 97.96 | 97.27 | −0.7% | −1.9472 to +0.5682 | no |
| response time (ms), 99th percentile | 130.5 | 127.7 | −2.1% | −14.9519 to +9.4607 | no |
| time over the response line (% of samples) | 0.01198 | 0 | −100.0% | −0.0391 to +0.0151 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.7 | 16 | −18.8% | −5.5485 to −1.8515 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.29 | +9.4% | −0.3207 to +0.3707 | no |
| utilisation (used / allocatable) | 0.03235 | 0.0322 | −0.5% | −0.0004 to +0.0001 | no |
| CPU used (cores), mean | 0.7764 | 0.7727 | −0.5% | −0.0101 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0.03322 | 0.00558 | −83.2% | −0.0321 to −0.0232 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8097 | 0.7783 | −3.9% | −0.0409 to −0.0218 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.8 | 863 | +0.3% | −8.6568 to +12.9707 | no |
| HPA replicas, mean | 8.28 | 7.906 | −4.5% | −0.5734 to −0.1762 | yes: GAIN |
| pods started | 5.1 | 4.9 | −3.9% | −1.3583 to +0.9583 | no |
| pod start wait, total (s) | 7.2 | 7.3 | +1.4% | −2.0970 to +2.2970 | no |
| pod start wait, mean (s) | 1.436 | 1.56 | +8.6% | −0.0315 to +0.2796 | no |
| host CPU busy, the real machine under kind (%) | 25.38 | 24.19 | −4.7% | −1.6249 to −0.7631 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0031 to +0.0011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.7 | −0.1% | −0.4205 to +0.1790 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.7 | −0.1% | −0.4205 to +0.1790 | no |
| response time (ms), mean | 68.06 | 67.83 | −0.3% | −1.4392 to +0.9870 | no |
| response time (ms), 95th percentile | 97.96 | 96.52 | −1.5% | −3.2034 to +0.3324 | no |
| response time (ms), 99th percentile | 130.5 | 126.7 | −2.9% | −9.8187 to +2.2287 | no |
| time over the response line (% of samples) | 0.01198 | 0.02424 | +102.4% | −0.0515 to +0.0761 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.7 | 17.6 | −10.7% | −4.3227 to +0.1227 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.08167 | −69.2% | −0.4644 to +0.0978 | no |
| utilisation (used / allocatable) | 0.03235 | 0.03226 | −0.3% | −0.0007 to +0.0005 | no |
| CPU used (cores), mean | 0.7764 | 0.7743 | −0.3% | −0.0171 to +0.0128 | no |
| Omni's own CPU (cores), mean | 0.03322 | 0.00632 | −81.0% | −0.0312 to −0.0226 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8097 | 0.7806 | −3.6% | −0.0466 to −0.0115 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.8 | 856.2 | −0.5% | −28.8415 to +19.5778 | no |
| HPA replicas, mean | 8.28 | 7.83 | −5.4% | −0.7091 to −0.1920 | yes: GAIN |
| pods started | 5.1 | 5.1 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 7.2 | 7.7 | +6.9% | −1.8903 to +2.8903 | no |
| pod start wait, mean (s) | 1.436 | 1.47 | +2.3% | −0.3426 to +0.4087 | no |
| host CPU busy, the real machine under kind (%) | 25.38 | 24.32 | −4.2% | −1.7386 to −0.3795 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | −0.1% | −0.0025 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.8 | +0.0% | −0.2073 to +0.2339 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.8 | +0.0% | −0.2073 to +0.2339 | no |
| response time (ms), mean | 68.06 | 68.24 | +0.3% | −0.9090 to +1.2656 | no |
| response time (ms), 95th percentile | 97.96 | 98.32 | +0.4% | −1.5606 to +2.2786 | no |
| response time (ms), 99th percentile | 130.5 | 125.3 | −4.0% | −19.1500 to +8.8090 | no |
| time over the response line (% of samples) | 0.01198 | 0 | −100.0% | −0.0391 to +0.0151 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.7 | 17 | −13.7% | −6.3792 to +0.9792 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.155 | −41.5% | −0.3747 to +0.1547 | no |
| utilisation (used / allocatable) | 0.03235 | 0.03263 | +0.9% | −0.0002 to +0.0007 | no |
| CPU used (cores), mean | 0.7764 | 0.7831 | +0.9% | −0.0042 to +0.0176 | no |
| Omni's own CPU (cores), mean | 0.03322 | 0.00707 | −78.7% | −0.0302 to −0.0221 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8097 | 0.7902 | −2.4% | −0.0322 to −0.0067 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.8 | 849.9 | −1.3% | −24.0752 to +2.2189 | no |
| HPA replicas, mean | 8.28 | 7.073 | −14.6% | −1.7005 to −0.7145 | yes: GAIN |
| pods started | 5.1 | 4.4 | −13.7% | −1.7144 to +0.3144 | no |
| pod start wait, total (s) | 7.2 | 6.6 | −8.3% | −2.8163 to +1.6163 | no |
| pod start wait, mean (s) | 1.436 | 1.497 | +4.2% | −0.2885 to +0.4090 | no |
| host CPU busy, the real machine under kind (%) | 25.38 | 24.52 | −3.4% | −1.3533 to −0.3691 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.513 | −0.1% | −0.0046 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.6 | −0.1% | −0.5619 to +0.1576 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.6 | −0.1% | −0.5619 to +0.1576 | no |
| response time (ms), mean | 68.06 | 67.96 | −0.1% | −1.6997 to +1.4956 | no |
| response time (ms), 95th percentile | 97.96 | 97.38 | −0.6% | −3.8563 to +2.6973 | no |
| response time (ms), 99th percentile | 130.5 | 133 | +1.9% | −11.6727 to +16.6995 | no |
| time over the response line (% of samples) | 0.01198 | 0 | −100.0% | −0.0391 to +0.0151 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.7 | 15.9 | −19.3% | −7.6712 to +0.0712 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.2117 | −20.1% | −0.2804 to +0.1737 | no |
| utilisation (used / allocatable) | 0.03235 | 0.03229 | −0.2% | −0.0007 to +0.0006 | no |
| CPU used (cores), mean | 0.7764 | 0.7751 | −0.2% | −0.0177 to +0.0149 | no |
| Omni's own CPU (cores), mean | 0.03322 | 0.01273 | −61.7% | −0.0238 to −0.0172 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8097 | 0.7878 | −2.7% | −0.0404 to −0.0033 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.8 | 857.4 | −0.4% | −31.1725 to +24.4020 | no |
| HPA replicas, mean | 8.28 | 7.061 | −14.7% | −2.0031 to −0.4360 | yes: GAIN |
| pods started | 5.1 | 4.3 | −15.7% | −2.1403 to +0.5403 | no |
| pod start wait, total (s) | 7.2 | 7.1 | −1.4% | −3.0095 to +2.8095 | no |
| pod start wait, mean (s) | 1.436 | 1.617 | +12.5% | −0.2160 to +0.5764 | no |
| host CPU busy, the real machine under kind (%) | 25.38 | 24.47 | −3.6% | −1.6607 to −0.1659 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | −0.1% | −0.0032 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.7 | −0.1% | −0.3786 to +0.2072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.7 | −0.1% | −0.3786 to +0.2072 | no |
| response time (ms), mean | 68.06 | 68.18 | +0.2% | −0.8119 to +1.0411 | no |
| response time (ms), 95th percentile | 97.96 | 98.4 | +0.5% | −1.6688 to +2.5528 | no |
| response time (ms), 99th percentile | 130.5 | 133.1 | +2.0% | −5.2524 to +10.4182 | no |
| time over the response line (% of samples) | 0.01198 | 0.03622 | +202.4% | −0.0302 to +0.0787 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.7 | 18.3 | −7.1% | −2.6707 to −0.1293 | yes, down (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 70 | −22.2% | −65.2400 to +25.2400 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.3217 | +21.4% | −0.2757 to +0.3890 | no |
| utilisation (used / allocatable) | 0.03235 | 0.03234 | −0.0% | −0.0003 to +0.0003 | no |
| CPU used (cores), mean | 0.7764 | 0.7762 | −0.0% | −0.0075 to +0.0070 | no |
| Omni's own CPU (cores), mean | 0.03322 | 0.02295 | −30.9% | −0.0118 to −0.0087 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8097 | 0.7991 | −1.3% | −0.0170 to −0.0040 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.8 | 866 | +0.6% | −4.3886 to +14.7654 | no |
| HPA replicas, mean | 8.28 | 7.936 | −4.2% | −0.6156 to −0.0722 | yes: GAIN |
| pods started | 5.1 | 5 | −2.0% | −1.1900 to +0.9900 | no |
| pod start wait, total (s) | 7.2 | 7 | −2.8% | −2.6962 to +2.2962 | no |
| pod start wait, mean (s) | 1.436 | 1.433 | −0.2% | −0.3456 to +0.3394 | no |
| host CPU busy, the real machine under kind (%) | 25.38 | 24.94 | −1.7% | −0.8517 to −0.0245 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0075 to +0.0039 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.7 | −0.1% | −0.6967 to +0.4593 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.7 | −0.1% | −0.6967 to +0.4593 | no |
| response time (ms), mean | 68.06 | 68.63 | +0.8% | −0.4700 to +1.6171 | no |
| response time (ms), 95th percentile | 97.96 | 99.43 | +1.5% | −1.3018 to +4.2418 | no |
| response time (ms), 99th percentile | 130.5 | 133 | +1.9% | −14.1139 to +19.1407 | no |
| time over the response line (% of samples) | 0.01198 | 0 | −100.0% | −0.0391 to +0.0151 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.7 | 18.7 | −5.1% | −2.1681 to +0.1681 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 100 | +11.1% | −12.6200 to +32.6200 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.24 | −9.4% | −0.1878 to +0.1378 | no |
| utilisation (used / allocatable) | 0.03235 | 0.03252 | +0.5% | −0.0002 to +0.0005 | no |
| CPU used (cores), mean | 0.7764 | 0.7805 | +0.5% | −0.0045 to +0.0125 | no |
| Omni's own CPU (cores), mean | 0.03322 | 0.06306 | +89.8% | +0.0256 to +0.0341 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8097 | 0.8435 | +4.2% | +0.0241 to +0.0437 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860.8 | 855.7 | −0.6% | −14.8816 to +4.6640 | no |
| HPA replicas, mean | 8.28 | 8.154 | −1.5% | −0.2859 to +0.0335 | no |
| pods started | 5.1 | 4.9 | −3.9% | −0.9388 to +0.5388 | no |
| pod start wait, total (s) | 7.2 | 6.9 | −4.2% | −2.5380 to +1.9380 | no |
| pod start wait, mean (s) | 1.436 | 1.4 | −2.5% | −0.3841 to +0.3117 | no |
| host CPU busy, the real machine under kind (%) | 25.38 | 26.51 | +4.4% | +0.7018 to +1.5564 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*