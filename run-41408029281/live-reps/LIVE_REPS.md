# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.509 | 1.509 | 1.508 | 1.509 | 1.508 | 1.509 | 1.51 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.2 | 159 | 159.1 | 159 | 159 | 159.2 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.2 | 159 | 159.1 | 159 | 159 | 159.2 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 181.7 | 89.98 | 88.68 | 89.12 | 89.07 | 88.83 | 89.39 | 91.11 |
| response time (ms), 95th percentile | 409 | 139.7 | 136.1 | 135.3 | 135.7 | 137.3 | 137.3 | 141.2 |
| response time (ms), 99th percentile | 670.1 | 196.3 | 186 | 189.9 | 184.2 | 191.7 | 200.2 | 198.4 |
| time over the response line (% of samples) | 3.291 | 0 | 0.01212 | 0.01212 | 0.01212 | 0 | 0.01212 | 0.02424 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | 16 | 17.8 | 18.8 | 19.6 | 19.2 | 22.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | nan | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.3767 | 0.4517 | 0.2567 | 0.055 | 0.08333 | 0.3517 | 0.43 |
| utilisation (used / allocatable) | 0.04391 | 0.04134 | 0.04115 | 0.04116 | 0.04113 | 0.04097 | 0.04151 | 0.04174 |
| CPU used (cores), mean | 1.054 | 0.9921 | 0.9876 | 0.988 | 0.987 | 0.9833 | 0.9962 | 1.002 |
| Omni's own CPU (cores), mean | 0 | 0.04094 | 0.00686 | 0.00784 | 0.00888 | 0.01613 | 0.02848 | 0.07839 |
| CPU used with Omni's own (cores), mean | 1.054 | 1.033 | 0.9945 | 0.9958 | 0.9959 | 0.9994 | 1.025 | 1.08 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 644.9 | 647.9 | 647.7 | 648.2 | 650.8 | 642.6 | 639.7 |
| HPA replicas, mean | 8.888 | 9.472 | 8.972 | 8.91 | 8.56 | 8.233 | 9.214 | 9.162 |
| pods started | 5.1 | 2.9 | 3.7 | 2.8 | 3.3 | 3.4 | 3 | 3.2 |
| pod start wait, total (s) | 7.3 | 4.3 | 6.2 | 4.1 | 5.4 | 5.2 | 4.5 | 5.1 |
| pod start wait, mean (s) | 1.44 | 1.5 | 1.63 | 1.452 | 1.667 | 1.51 | 1.402 | 1.683 |
| host CPU busy, the real machine under kind (%) | 31.89 | 31.66 | 30.2 | 30.37 | 30.42 | 30.57 | 31.19 | 33.32 |
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
| node-hours | 1.509 | 1.509 | 0.0% | raw −0.0016 to +0.0016 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.2 | −0.4% | −0.9016 to −0.2583 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.2 | −0.4% | −0.9016 to −0.2583 | yes: GAIN |
| response time (ms), mean | 181.7 | 89.98 | −50.5% | −105.9097 to −77.4942 | yes: GAIN |
| response time (ms), 95th percentile | 409 | 139.7 | −65.9% | −316.4273 to −222.2847 | yes: GAIN |
| response time (ms), 99th percentile | 670.1 | 196.3 | −70.7% | −562.4386 to −385.2852 | yes: GAIN |
| time over the response line (% of samples) | 3.291 | 0 | −100.0% | −4.4306 to −2.1520 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +17.0428 to +19.7572 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.3767 | +14.1% | −0.3007 to +0.3940 | no |
| utilisation (used / allocatable) | 0.04391 | 0.04134 | −5.9% | −0.0036 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.054 | 0.9921 | −5.9% | −0.0855 to −0.0380 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04094 | +0.041 (native is 0) | +0.0385 to +0.0434 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.054 | 1.033 | −2.0% | −0.0431 to +0.0015 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 644.9 | +5.2% | +19.5867 to +44.7451 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 9.472 | +6.6% | +0.2961 to +0.8717 | yes: power given |
| pods started | 5.1 | 2.9 | −43.1% | −3.2003 to −1.1997 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 4.3 | −41.1% | −5.1058 to −0.8942 | yes: GAIN |
| pod start wait, mean (s) | 1.44 | 1.5 | +4.2% | −0.2960 to +0.4160 | no |
| host CPU busy, the real machine under kind (%) | 31.89 | 31.66 | −0.7% | −0.7506 to +0.2781 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.508 | −0.1% | −0.0030 to +0.0010 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159 | −0.5% | −1.1283 to −0.3942 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159 | −0.5% | −1.1283 to −0.3942 | yes: GAIN |
| response time (ms), mean | 181.7 | 88.68 | −51.2% | −107.3390 to −78.6532 | yes: GAIN |
| response time (ms), 95th percentile | 409 | 136.1 | −66.7% | −320.2260 to −225.6570 | yes: GAIN |
| response time (ms), 99th percentile | 670.1 | 186 | −72.2% | −575.0279 to −393.2117 | yes: GAIN |
| time over the response line (% of samples) | 3.291 | 0.01212 | −99.6% | −4.4179 to −2.1405 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16.000 (native is 0) | +15.1740 to +16.8260 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.4517 | +36.9% | −0.2314 to +0.4747 | no |
| utilisation (used / allocatable) | 0.04391 | 0.04115 | −6.3% | −0.0037 to −0.0019 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.054 | 0.9876 | −6.3% | −0.0881 to −0.0445 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00686 | +0.007 (native is 0) | +0.0064 to +0.0073 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.054 | 0.9945 | −5.6% | −0.0810 to −0.0378 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 647.9 | +5.7% | +23.3168 to +47.1031 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 8.972 | +0.9% | −0.1239 to +0.2906 | no |
| pods started | 5.1 | 3.7 | −27.5% | −2.4228 to −0.3772 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 6.2 | −15.1% | −4.1245 to +1.9245 | no |
| pod start wait, mean (s) | 1.44 | 1.63 | +13.2% | −0.2530 to +0.6330 | no |
| host CPU busy, the real machine under kind (%) | 31.89 | 30.2 | −5.3% | −2.2653 to −1.1185 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.509 | −0.0% | −0.0015 to +0.0011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.1 | −0.4% | −0.9523 to −0.3857 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.1 | −0.4% | −0.9523 to −0.3857 | yes: GAIN |
| response time (ms), mean | 181.7 | 89.12 | −50.9% | −107.1192 to −77.9931 | yes: GAIN |
| response time (ms), 95th percentile | 409 | 135.3 | −66.9% | −321.1599 to −226.3221 | yes: GAIN |
| response time (ms), 99th percentile | 670.1 | 189.9 | −71.7% | −569.7909 to −390.6271 | yes: GAIN |
| time over the response line (% of samples) | 3.291 | 0.01212 | −99.6% | −4.4179 to −2.1405 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +16.2621 to +19.3379 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.2567 | −22.2% | −0.3622 to +0.2155 | no |
| utilisation (used / allocatable) | 0.04391 | 0.04116 | −6.3% | −0.0037 to −0.0018 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.054 | 0.988 | −6.3% | −0.0885 to −0.0433 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00784 | +0.008 (native is 0) | +0.0074 to +0.0083 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.054 | 0.9958 | −5.5% | −0.0805 to −0.0357 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 647.7 | +5.7% | +23.4348 to +46.6142 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 8.91 | +0.2% | −0.3928 to +0.4372 | no |
| pods started | 5.1 | 2.8 | −45.1% | −3.1953 to −1.4047 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 4.1 | −43.8% | −5.1312 to −1.2688 | yes: GAIN |
| pod start wait, mean (s) | 1.44 | 1.452 | +0.8% | −0.4226 to +0.4459 | no |
| host CPU busy, the real machine under kind (%) | 31.89 | 30.37 | −4.8% | −2.1092 to −0.9339 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.508 | −0.1% | −0.0024 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159 | −0.5% | −1.0661 to −0.4514 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159 | −0.5% | −1.0661 to −0.4514 | yes: GAIN |
| response time (ms), mean | 181.7 | 89.07 | −51.0% | −106.7797 to −78.4366 | yes: GAIN |
| response time (ms), 95th percentile | 409 | 135.7 | −66.8% | −320.6843 to −226.0427 | yes: GAIN |
| response time (ms), 99th percentile | 670.1 | 184.2 | −72.5% | −577.9985 to −393.8677 | yes: GAIN |
| time over the response line (% of samples) | 3.291 | 0.01212 | −99.6% | −4.4147 to −2.1437 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | +18.800 (native is 0) | +16.9904 to +20.6096 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.055 | −83.3% | −0.5656 to +0.0156 | no |
| utilisation (used / allocatable) | 0.04391 | 0.04113 | −6.3% | −0.0038 to −0.0017 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.054 | 0.987 | −6.3% | −0.0917 to −0.0420 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00888 | +0.009 (native is 0) | +0.0082 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.054 | 0.9959 | −5.5% | −0.0824 to −0.0335 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 648.2 | +5.8% | +22.8091 to +48.2224 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 8.56 | −3.7% | −0.7379 to +0.0816 | no |
| pods started | 5.1 | 3.3 | −35.3% | −2.4573 to −1.1427 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 5.4 | −26.0% | −3.7607 to −0.0393 | yes: GAIN |
| pod start wait, mean (s) | 1.44 | 1.667 | +15.7% | −0.1083 to +0.5616 | no |
| host CPU busy, the real machine under kind (%) | 31.89 | 30.42 | −4.6% | −2.0509 to −0.8839 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.509 | −0.1% | −0.0021 to +0.0005 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159 | −0.5% | −1.0945 to −0.4539 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159 | −0.5% | −1.0945 to −0.4539 | yes: GAIN |
| response time (ms), mean | 181.7 | 88.83 | −51.1% | −107.4234 to −78.2756 | yes: GAIN |
| response time (ms), 95th percentile | 409 | 137.3 | −66.4% | −320.3482 to −223.2208 | yes: GAIN |
| response time (ms), 99th percentile | 670.1 | 191.7 | −71.4% | −569.3220 to −387.4968 | yes: GAIN |
| time over the response line (% of samples) | 3.291 | 0 | −100.0% | −4.4306 to −2.1520 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | +19.600 (native is 0) | +17.5159 to +21.6841 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.08333 | −74.7% | −0.4967 to +0.0033 | no |
| utilisation (used / allocatable) | 0.04391 | 0.04097 | −6.7% | −0.0038 to −0.0020 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.054 | 0.9833 | −6.7% | −0.0920 to −0.0492 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01613 | +0.016 (native is 0) | +0.0150 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.054 | 0.9994 | −5.2% | −0.0750 to −0.0339 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 650.8 | +6.2% | +28.7702 to +47.3418 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 8.233 | −7.4% | −1.0084 to −0.3011 | yes: GAIN |
| pods started | 5.1 | 3.4 | −33.3% | −2.1828 to −1.2172 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 5.2 | −28.8% | −4.0209 to −0.1791 | yes: GAIN |
| pod start wait, mean (s) | 1.44 | 1.51 | +4.9% | −0.3381 to +0.4781 | no |
| host CPU busy, the real machine under kind (%) | 31.89 | 30.57 | −4.2% | −1.8870 to −0.7650 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.51 | +0.0% | −0.0017 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.2 | −0.3% | −0.8569 to −0.1968 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.2 | −0.3% | −0.8569 to −0.1968 | yes: GAIN |
| response time (ms), mean | 181.7 | 89.39 | −50.8% | −106.5607 to −78.0190 | yes: GAIN |
| response time (ms), 95th percentile | 409 | 137.3 | −66.4% | −319.3197 to −224.1053 | yes: GAIN |
| response time (ms), 99th percentile | 670.1 | 200.2 | −70.1% | −558.8744 to −380.9406 | yes: GAIN |
| time over the response line (% of samples) | 3.291 | 0.01212 | −99.6% | −4.4147 to −2.1437 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | +19.200 (native is 0) | +17.7774 to +20.6226 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.3517 | +6.6% | −0.2117 to +0.2550 | no |
| utilisation (used / allocatable) | 0.04391 | 0.04151 | −5.5% | −0.0034 to −0.0015 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.054 | 0.9962 | −5.5% | −0.0805 to −0.0349 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02848 | +0.028 (native is 0) | +0.0266 to +0.0303 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.054 | 1.025 | −2.8% | −0.0511 to −0.0074 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 642.6 | +4.9% | +16.8169 to +42.9568 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 9.214 | +3.7% | +0.1726 to +0.4782 | yes: power given |
| pods started | 5.1 | 3 | −41.2% | −3.0204 to −1.1796 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 4.5 | −38.4% | −4.5456 to −1.0544 | yes: GAIN |
| pod start wait, mean (s) | 1.44 | 1.402 | −2.7% | −0.2286 to +0.1519 | no |
| host CPU busy, the real machine under kind (%) | 31.89 | 31.19 | −2.2% | −1.2533 to −0.1541 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.51 | +0.1% | −0.0003 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.4 | −0.3% | −0.6342 to −0.1690 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.4 | −0.3% | −0.6342 to −0.1690 | yes: GAIN |
| response time (ms), mean | 181.7 | 91.11 | −49.9% | −104.2840 to −76.8599 | yes: GAIN |
| response time (ms), 95th percentile | 409 | 141.2 | −65.5% | −314.8018 to −220.9572 | yes: GAIN |
| response time (ms), 99th percentile | 670.1 | 198.4 | −70.4% | −557.4718 to −385.9600 | yes: GAIN |
| time over the response line (% of samples) | 3.291 | 0.02424 | −99.3% | −4.4037 to −2.1305 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.3 | +22.300 (native is 0) | +19.2270 to +25.3730 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.43 | +30.3% | −0.3639 to +0.5639 | no |
| utilisation (used / allocatable) | 0.04391 | 0.04174 | −4.9% | −0.0031 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.054 | 1.002 | −4.9% | −0.0746 to −0.0296 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07839 | +0.078 (native is 0) | +0.0732 to +0.0836 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.054 | 1.08 | +2.5% | +0.0067 to +0.0459 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 612.7 | 639.7 | +4.4% | +15.4907 to +38.4762 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 9.162 | +3.1% | −0.1837 to +0.7310 | no |
| pods started | 5.1 | 3.2 | −37.3% | −3.1367 to −0.6633 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 5.1 | −30.1% | −4.9969 to +0.5969 | no |
| pod start wait, mean (s) | 1.44 | 1.683 | +16.9% | −0.2401 to +0.7268 | no |
| host CPU busy, the real machine under kind (%) | 31.89 | 33.32 | +4.5% | +1.0861 to +1.7660 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.508 | −0.1% | −0.0024 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159 | −0.1% | −0.3897 to +0.0271 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159 | −0.1% | −0.3897 to +0.0271 | no |
| response time (ms), mean | 89.98 | 88.68 | −1.4% | −2.2747 to −0.3136 | yes: GAIN |
| response time (ms), 95th percentile | 139.7 | 136.1 | −2.6% | −5.8076 to −1.3634 | yes: GAIN |
| response time (ms), 99th percentile | 196.3 | 186 | −5.2% | −25.7429 to +5.2271 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 16 | −13.0% | −4.3720 to −0.4280 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.4517 | +19.9% | −0.3296 to +0.4796 | no |
| utilisation (used / allocatable) | 0.04134 | 0.04115 | −0.5% | −0.0007 to +0.0004 | no |
| CPU used (cores), mean | 0.9921 | 0.9876 | −0.5% | −0.0178 to +0.0087 | no |
| Omni's own CPU (cores), mean | 0.04094 | 0.00686 | −83.2% | −0.0361 to −0.0320 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 0.9945 | −3.7% | −0.0517 to −0.0256 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.9 | 647.9 | +0.5% | −4.7713 to +10.8594 | no |
| HPA replicas, mean | 9.472 | 8.972 | −5.3% | −0.8562 to −0.1448 | yes: GAIN |
| pods started | 2.9 | 3.7 | +27.6% | −0.8792 to +2.4792 | no |
| pod start wait, total (s) | 4.3 | 6.2 | +44.2% | −1.2713 to +5.0713 | no |
| pod start wait, mean (s) | 1.5 | 1.63 | +8.7% | −0.3804 to +0.6404 | no |
| host CPU busy, the real machine under kind (%) | 31.66 | 30.2 | −4.6% | −1.7184 to −1.1929 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.509 | −0.0% | −0.0016 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.1 | −0.1% | −0.2441 to +0.0661 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.1 | −0.1% | −0.2441 to +0.0661 | no |
| response time (ms), mean | 89.98 | 89.12 | −0.9% | −1.3511 to −0.3573 | yes: GAIN |
| response time (ms), 95th percentile | 139.7 | 135.3 | −3.1% | −6.8681 to −1.9019 | yes: GAIN |
| response time (ms), 99th percentile | 196.3 | 189.9 | −3.2% | −16.4273 to +3.7331 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 17.8 | −3.3% | −2.6841 to +1.4841 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.2567 | −31.9% | −0.4620 to +0.2220 | no |
| utilisation (used / allocatable) | 0.04134 | 0.04116 | −0.4% | −0.0005 to +0.0001 | no |
| CPU used (cores), mean | 0.9921 | 0.988 | −0.4% | −0.0109 to +0.0025 | no |
| Omni's own CPU (cores), mean | 0.04094 | 0.00784 | −80.9% | −0.0352 to −0.0310 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 0.9958 | −3.6% | −0.0434 to −0.0312 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.9 | 647.7 | +0.4% | −1.3735 to +7.0907 | no |
| HPA replicas, mean | 9.472 | 8.91 | −5.9% | −0.9483 to −0.1750 | yes: GAIN |
| pods started | 2.9 | 2.8 | −3.4% | −1.1366 to +0.9366 | no |
| pod start wait, total (s) | 4.3 | 4.1 | −4.7% | −2.0407 to +1.6407 | no |
| pod start wait, mean (s) | 1.5 | 1.452 | −3.2% | −0.4116 to +0.3149 | no |
| host CPU busy, the real machine under kind (%) | 31.66 | 30.37 | −4.1% | −1.5318 to −1.0387 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.508 | −0.1% | −0.0023 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159 | −0.1% | −0.3218 to −0.0358 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159 | −0.1% | −0.3218 to −0.0358 | yes: GAIN |
| response time (ms), mean | 89.98 | 89.07 | −1.0% | −2.0491 to +0.2367 | no |
| response time (ms), 95th percentile | 139.7 | 135.7 | −2.9% | −6.1765 to −1.8385 | yes: GAIN |
| response time (ms), 99th percentile | 196.3 | 184.2 | −6.1% | −27.3810 to +3.2386 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 18.8 | +2.2% | −1.3907 to +2.1907 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.055 | −85.4% | −0.6196 to −0.0237 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04134 | 0.04113 | −0.5% | −0.0005 to +0.0001 | no |
| CPU used (cores), mean | 0.9921 | 0.987 | −0.5% | −0.0128 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0.04094 | 0.00888 | −78.3% | −0.0339 to −0.0302 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 0.9959 | −3.6% | −0.0447 to −0.0297 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.9 | 648.2 | +0.5% | −1.1362 to +7.8359 | no |
| HPA replicas, mean | 9.472 | 8.56 | −9.6% | −1.2608 to −0.5632 | yes: GAIN |
| pods started | 2.9 | 3.3 | +13.8% | −0.7285 to +1.5285 | no |
| pod start wait, total (s) | 4.3 | 5.4 | +25.6% | −0.5673 to +2.7673 | no |
| pod start wait, mean (s) | 1.5 | 1.667 | +11.1% | −0.2247 to +0.5581 | no |
| host CPU busy, the real machine under kind (%) | 31.66 | 30.42 | −3.9% | −1.5256 to −0.9367 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.509 | −0.1% | −0.0025 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159 | −0.1% | −0.4192 to +0.0308 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159 | −0.1% | −0.4192 to +0.0308 | no |
| response time (ms), mean | 89.98 | 88.83 | −1.3% | −2.3645 to +0.0694 | no |
| response time (ms), 95th percentile | 139.7 | 137.3 | −1.7% | −5.6922 to +0.8352 | no |
| response time (ms), 99th percentile | 196.3 | 191.7 | −2.3% | −14.8216 to +5.7266 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 19.6 | +6.5% | −1.4722 to +3.8722 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.08333 | −77.9% | −0.5184 to −0.0682 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04134 | 0.04097 | −0.9% | −0.0008 to +0.0001 | no |
| CPU used (cores), mean | 0.9921 | 0.9833 | −0.9% | −0.0190 to +0.0013 | no |
| Omni's own CPU (cores), mean | 0.04094 | 0.01613 | −60.6% | −0.0262 to −0.0234 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 0.9994 | −3.3% | −0.0442 to −0.0232 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.9 | 650.8 | +0.9% | −0.7868 to +12.5670 | no |
| HPA replicas, mean | 9.472 | 8.233 | −13.1% | −1.6037 to −0.8735 | yes: GAIN |
| pods started | 2.9 | 3.4 | +17.2% | −0.5796 to +1.5796 | no |
| pod start wait, total (s) | 4.3 | 5.2 | +20.9% | −1.1358 to +2.9358 | no |
| pod start wait, mean (s) | 1.5 | 1.51 | +0.7% | −0.4061 to +0.4261 | no |
| host CPU busy, the real machine under kind (%) | 31.66 | 30.57 | −3.4% | −1.4054 to −0.7740 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.51 | +0.0% | −0.0011 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.2 | +0.0% | −0.1569 to +0.2632 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.2 | +0.0% | −0.1569 to +0.2632 | no |
| response time (ms), mean | 89.98 | 89.39 | −0.7% | −1.3591 to +0.1834 | no |
| response time (ms), 95th percentile | 139.7 | 137.3 | −1.7% | −4.3415 to −0.3715 | yes: GAIN |
| response time (ms), 99th percentile | 196.3 | 200.2 | +2.0% | −4.5929 to +12.5017 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 19.2 | +4.3% | −0.6226 to +2.2226 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.3517 | −6.6% | −0.3707 to +0.3207 | no |
| utilisation (used / allocatable) | 0.04134 | 0.04151 | +0.4% | −0.0003 to +0.0006 | no |
| CPU used (cores), mean | 0.9921 | 0.9962 | +0.4% | −0.0065 to +0.0145 | no |
| Omni's own CPU (cores), mean | 0.04094 | 0.02848 | −30.4% | −0.0132 to −0.0118 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 1.025 | −0.8% | −0.0188 to +0.0020 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.9 | 642.6 | −0.4% | −8.3345 to +3.7763 | no |
| HPA replicas, mean | 9.472 | 9.214 | −2.7% | −0.5951 to +0.0781 | no |
| pods started | 2.9 | 3 | +3.4% | −0.9900 to +1.1900 | no |
| pod start wait, total (s) | 4.3 | 4.5 | +4.7% | −1.6407 to +2.0407 | no |
| pod start wait, mean (s) | 1.5 | 1.402 | −6.6% | −0.4814 to +0.2848 | no |
| host CPU busy, the real machine under kind (%) | 31.66 | 31.19 | −1.5% | −0.8039 to −0.1310 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.51 | +0.1% | −0.0006 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.4 | +0.1% | −0.0103 to +0.3670 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.4 | +0.1% | −0.0103 to +0.3670 | no |
| response time (ms), mean | 89.98 | 91.11 | +1.3% | −0.0996 to +2.3597 | no |
| response time (ms), 95th percentile | 139.7 | 141.2 | +1.1% | −2.1794 to +5.1324 | no |
| response time (ms), 99th percentile | 196.3 | 198.4 | +1.1% | −8.8945 to +13.1865 | no |
| time over the response line (% of samples) | 0 | 0.02424 | +0.024 (native is 0) | −0.0123 to +0.0608 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.4 | 22.3 | +21.2% | +0.7108 to +7.0892 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.43 | +14.2% | −0.4277 to +0.5344 | no |
| utilisation (used / allocatable) | 0.04134 | 0.04174 | +1.0% | −0.0002 to +0.0010 | no |
| CPU used (cores), mean | 0.9921 | 1.002 | +1.0% | −0.0041 to +0.0235 | no |
| Omni's own CPU (cores), mean | 0.04094 | 0.07839 | +91.5% | +0.0346 to +0.0403 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 1.08 | +4.6% | +0.0323 to +0.0619 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.9 | 639.7 | −0.8% | −12.8178 to +2.4529 | no |
| HPA replicas, mean | 9.472 | 9.162 | −3.3% | −0.9163 to +0.2959 | no |
| pods started | 2.9 | 3.2 | +10.3% | −0.7144 to +1.3144 | no |
| pod start wait, total (s) | 4.3 | 5.1 | +18.6% | −1.9144 to +3.5144 | no |
| pod start wait, mean (s) | 1.5 | 1.683 | +12.2% | −0.3006 to +0.6672 | no |
| host CPU busy, the real machine under kind (%) | 31.66 | 33.32 | +5.3% | +1.2526 to +2.0721 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*