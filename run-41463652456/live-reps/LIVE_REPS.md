# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.514 | 1.514 | 1.513 | 1.513 | 1.514 | 1.514 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | 158.7 | 158.6 | 158.7 | 158.8 | 158.8 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | 158.7 | 158.6 | 158.7 | 158.8 | 158.8 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 151.7 | 79.1 | 78.4 | 78.09 | 78.65 | 78.83 | 78.66 | 79.19 |
| response time (ms), 95th percentile | 344.4 | 114.1 | 112.1 | 110.5 | 112.5 | 113.1 | 112.7 | 112.7 |
| response time (ms), 99th percentile | 516.5 | 154.9 | 151.3 | 149.1 | 158.1 | 153.5 | 146.9 | 149.8 |
| time over the response line (% of samples) | 2.17 | 0.01205 | 0.01212 | 0.03615 | 0.02388 | 0 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.9 | 14.9 | 17.4 | 16.5 | 16.2 | 18.9 | 20.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | nan | nan | 100 | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2683 | 0.2983 | 0.1333 | 0.02667 | 0.185 | 0.3717 | 0.2917 |
| utilisation (used / allocatable) | 0.03857 | 0.03718 | 0.03716 | 0.03681 | 0.03731 | 0.03747 | 0.03731 | 0.03747 |
| CPU used (cores), mean | 0.9257 | 0.8923 | 0.8919 | 0.8834 | 0.8954 | 0.8992 | 0.8955 | 0.8992 |
| Omni's own CPU (cores), mean | 0 | 0.03619 | 0.00605 | 0.00681 | 0.00757 | 0.014 | 0.02525 | 0.06921 |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.9284 | 0.8979 | 0.8902 | 0.903 | 0.9132 | 0.9208 | 0.9684 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 748.3 | 747.8 | 755 | 746.6 | 745 | 747.7 | 743.7 |
| HPA replicas, mean | 8.475 | 8.905 | 8.122 | 8.259 | 7.678 | 7.541 | 8.69 | 8.679 |
| pods started | 4.8 | 4.7 | 3.4 | 4 | 3.3 | 3.4 | 3.9 | 4.4 |
| pod start wait, total (s) | 7.1 | 6.3 | 5.1 | 5.7 | 5 | 5.1 | 6.5 | 6.4 |
| pod start wait, mean (s) | 1.323 | 1.333 | 1.41 | 1.41 | 1.37 | 1.563 | 1.602 | 1.492 |
| host CPU busy, the real machine under kind (%) | 28.22 | 28.67 | 27.45 | 27.43 | 27.71 | 28.01 | 28.26 | 29.86 |
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
| node-hours | 1.513 | 1.514 | +0.1% | −0.0005 to +0.0025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | −0.1% | −0.5162 to +0.0568 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | −0.1% | −0.5162 to +0.0568 | no |
| response time (ms), mean | 151.7 | 79.1 | −47.9% | −95.9050 to −49.2805 | yes: GAIN |
| response time (ms), 95th percentile | 344.4 | 114.1 | −66.9% | −298.8263 to −161.8287 | yes: GAIN |
| response time (ms), 99th percentile | 516.5 | 154.9 | −70.0% | −467.4675 to −255.6677 | yes: GAIN |
| time over the response line (% of samples) | 2.17 | 0.01205 | −99.4% | −3.6529 to −0.6623 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.6963 to −0.7037 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.9 | +19.900 (native is 0) | +18.1658 to +21.6342 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2683 | +43.7% | −0.1569 to +0.3202 | no |
| utilisation (used / allocatable) | 0.03857 | 0.03718 | −3.6% | −0.0023 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9257 | 0.8923 | −3.6% | −0.0543 to −0.0126 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03619 | +0.036 (native is 0) | +0.0314 to +0.0410 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.9284 | +0.3% | −0.0144 to +0.0199 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 748.3 | +2.2% | −1.1264 to +33.8874 | no |
| HPA replicas, mean | 8.475 | 8.905 | +5.1% | +0.0021 to +0.8566 | yes: power given |
| pods started | 4.8 | 4.7 | −2.1% | −1.6977 to +1.4977 | no |
| pod start wait, total (s) | 7.1 | 6.3 | −11.3% | −3.8868 to +2.2868 | no |
| pod start wait, mean (s) | 1.323 | 1.333 | +0.8% | −0.5068 to +0.5268 | no |
| host CPU busy, the real machine under kind (%) | 28.22 | 28.67 | +1.6% | +0.0042 to +0.9035 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.0% | −0.0009 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | −0.1% | −0.6341 to +0.1664 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | −0.1% | −0.6341 to +0.1664 | no |
| response time (ms), mean | 151.7 | 78.4 | −48.3% | −97.2484 to −49.3234 | yes: GAIN |
| response time (ms), 95th percentile | 344.4 | 112.1 | −67.5% | −301.8591 to −162.7829 | yes: GAIN |
| response time (ms), 99th percentile | 516.5 | 151.3 | −70.7% | −476.2049 to −254.1295 | yes: GAIN |
| time over the response line (% of samples) | 2.17 | 0.01212 | −99.4% | −3.6544 to −0.6606 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.6963 to −0.7037 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.9 | +14.900 (native is 0) | +12.8923 to +16.9077 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2983 | +59.8% | −0.2579 to +0.4812 | no |
| utilisation (used / allocatable) | 0.03857 | 0.03716 | −3.7% | −0.0024 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9257 | 0.8919 | −3.7% | −0.0573 to −0.0104 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00605 | +0.006 (native is 0) | +0.0053 to +0.0068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.8979 | −3.0% | −0.0506 to −0.0050 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 747.8 | +2.2% | −1.2124 to +32.8328 | no |
| HPA replicas, mean | 8.475 | 8.122 | −4.2% | −1.0224 to +0.3159 | no |
| pods started | 4.8 | 3.4 | −29.2% | −2.7985 to −0.0015 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.1 | −28.2% | −4.6336 to +0.6336 | no |
| pod start wait, mean (s) | 1.323 | 1.41 | +6.5% | −0.4588 to +0.6321 | no |
| host CPU busy, the real machine under kind (%) | 28.22 | 27.45 | −2.7% | −1.5136 to −0.0298 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.513 | +0.0% | −0.0014 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 | −0.2% | −0.6559 to −0.0337 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.6 | −0.2% | −0.6559 to −0.0337 | yes: GAIN |
| response time (ms), mean | 151.7 | 78.09 | −48.5% | −97.0468 to −50.1498 | yes: GAIN |
| response time (ms), 95th percentile | 344.4 | 110.5 | −67.9% | −303.1441 to −164.7029 | yes: GAIN |
| response time (ms), 99th percentile | 516.5 | 149.1 | −71.1% | −477.4959 to −257.2575 | yes: GAIN |
| time over the response line (% of samples) | 2.17 | 0.03615 | −98.3% | −3.6117 to −0.6553 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.6963 to −0.7037 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.400 (native is 0) | +16.0854 to +18.7146 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1333 | −28.6% | −0.2503 to +0.1437 | no |
| utilisation (used / allocatable) | 0.03857 | 0.03681 | −4.6% | −0.0029 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9257 | 0.8834 | −4.6% | −0.0684 to −0.0162 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00681 | +0.007 (native is 0) | +0.0059 to +0.0077 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.8902 | −3.8% | −0.0608 to −0.0102 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 755 | +3.2% | +6.8114 to +39.3205 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.475 | 8.259 | −2.5% | −0.5608 to +0.1292 | no |
| pods started | 4.8 | 4 | −16.7% | −2.0526 to +0.4526 | no |
| pod start wait, total (s) | 7.1 | 5.7 | −19.7% | −4.2252 to +1.4252 | no |
| pod start wait, mean (s) | 1.323 | 1.41 | +6.5% | −0.4554 to +0.6288 | no |
| host CPU busy, the real machine under kind (%) | 28.22 | 27.43 | −2.8% | −1.2793 to −0.3053 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.513 | +0.0% | −0.0016 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | −0.1% | −0.6314 to +0.1846 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | −0.1% | −0.6314 to +0.1846 | no |
| response time (ms), mean | 151.7 | 78.65 | −48.2% | −96.5186 to −49.5641 | yes: GAIN |
| response time (ms), 95th percentile | 344.4 | 112.5 | −67.3% | −300.1796 to −163.5714 | yes: GAIN |
| response time (ms), 99th percentile | 516.5 | 158.1 | −69.4% | −475.7893 to −240.9627 | yes: GAIN |
| time over the response line (% of samples) | 2.17 | 0.02388 | −98.9% | −3.6487 to −0.6428 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.6963 to −0.7037 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.5 | +16.500 (native is 0) | +13.2789 to +19.7211 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.02667 | −85.7% | −0.3443 to +0.0243 | no |
| utilisation (used / allocatable) | 0.03857 | 0.03731 | −3.3% | −0.0022 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9257 | 0.8954 | −3.3% | −0.0537 to −0.0069 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00757 | +0.008 (native is 0) | +0.0065 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.903 | −2.5% | −0.0454 to −0.0000 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 746.6 | +2.0% | −1.3617 to +30.7563 | no |
| HPA replicas, mean | 8.475 | 7.678 | −9.4% | −1.4820 to −0.1120 | yes: GAIN |
| pods started | 4.8 | 3.3 | −31.2% | −3.1259 to +0.1259 | no |
| pod start wait, total (s) | 7.1 | 5 | −29.6% | −4.1077 to −0.0923 | yes: GAIN |
| pod start wait, mean (s) | 1.323 | 1.37 | +3.5% | −0.4872 to +0.5806 | no |
| host CPU busy, the real machine under kind (%) | 28.22 | 27.71 | −1.8% | −1.1820 to +0.1633 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.0% | −0.0010 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.1% | −0.4016 to +0.0623 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.1% | −0.4016 to +0.0623 | no |
| response time (ms), mean | 151.7 | 78.83 | −48.0% | −95.8170 to −49.8962 | yes: GAIN |
| response time (ms), 95th percentile | 344.4 | 113.1 | −67.2% | −299.6895 to −162.9105 | yes: GAIN |
| response time (ms), 99th percentile | 516.5 | 153.5 | −70.3% | −467.7269 to −258.2775 | yes: GAIN |
| time over the response line (% of samples) | 2.17 | 0 | −100.0% | −3.6690 to −0.6703 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.6963 to −0.7037 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.2 | +16.200 (native is 0) | +13.1690 to +19.2310 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.185 | −0.9% | −0.2677 to +0.2644 | no |
| utilisation (used / allocatable) | 0.03857 | 0.03747 | −2.9% | −0.0021 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9257 | 0.8992 | −2.9% | −0.0504 to −0.0025 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.014 | +0.014 (native is 0) | +0.0119 to +0.0161 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.9132 | −1.3% | −0.0350 to +0.0100 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 745 | +1.8% | −3.8311 to +29.8774 | no |
| HPA replicas, mean | 8.475 | 7.541 | −11.0% | −1.4193 to −0.4487 | yes: GAIN |
| pods started | 4.8 | 3.4 | −29.2% | −2.6251 to −0.1749 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.1 | −28.2% | −4.1058 to +0.1058 | no |
| pod start wait, mean (s) | 1.323 | 1.563 | +18.1% | −0.3603 to +0.8403 | no |
| host CPU busy, the real machine under kind (%) | 28.22 | 28.01 | −0.8% | −0.7797 to +0.3535 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.1% | +0.0008 to +0.0022 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.1% | −0.4278 to +0.0663 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.1% | −0.4278 to +0.0663 | no |
| response time (ms), mean | 151.7 | 78.66 | −48.1% | −96.1042 to −49.9453 | yes: GAIN |
| response time (ms), 95th percentile | 344.4 | 112.7 | −67.3% | −300.2504 to −163.2556 | yes: GAIN |
| response time (ms), 99th percentile | 516.5 | 146.9 | −71.6% | −480.1532 to −259.0292 | yes: GAIN |
| time over the response line (% of samples) | 2.17 | 0 | −100.0% | −3.6690 to −0.6703 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.6963 to −0.7037 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 | +18.900 (native is 0) | +17.2327 to +20.5673 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.3717 | +99.1% | −0.1989 to +0.5689 | no |
| utilisation (used / allocatable) | 0.03857 | 0.03731 | −3.3% | −0.0022 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9257 | 0.8955 | −3.3% | −0.0519 to −0.0085 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02525 | +0.025 (native is 0) | +0.0219 to +0.0286 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.9208 | −0.5% | −0.0239 to +0.0140 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 747.7 | +2.1% | +1.8133 to +29.6082 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.475 | 8.69 | +2.5% | −0.0868 to +0.5160 | no |
| pods started | 4.8 | 3.9 | −18.8% | −2.1818 to +0.3818 | no |
| pod start wait, total (s) | 7.1 | 6.5 | −8.5% | −3.9244 to +2.7244 | no |
| pod start wait, mean (s) | 1.323 | 1.602 | +21.0% | −0.2067 to +0.7633 | no |
| host CPU busy, the real machine under kind (%) | 28.22 | 28.26 | +0.1% | −0.4349 to +0.5113 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.51 | −0.2% | −0.0097 to +0.0033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.4 | −0.4% | −1.1591 to +0.0315 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.4 | −0.4% | −1.1591 to +0.0315 | no |
| response time (ms), mean | 151.7 | 79.19 | −47.8% | −95.7176 to −49.2807 | yes: GAIN |
| response time (ms), 95th percentile | 344.4 | 112.7 | −67.3% | −300.4064 to −163.0306 | yes: GAIN |
| response time (ms), 99th percentile | 516.5 | 149.8 | −71.0% | −476.2297 to −257.1997 | yes: GAIN |
| time over the response line (% of samples) | 2.17 | 0 | −100.0% | −3.6690 to −0.6703 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.6963 to −0.7037 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.300 (native is 0) | +18.4515 to +22.1485 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2917 | +56.2% | −0.2437 to +0.4537 | no |
| utilisation (used / allocatable) | 0.03857 | 0.03747 | −2.9% | −0.0019 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9257 | 0.8992 | −2.9% | −0.0464 to −0.0066 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06921 | +0.069 (native is 0) | +0.0601 to +0.0783 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9257 | 0.9684 | +4.6% | +0.0278 to +0.0576 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 743.7 | +1.6% | −10.0024 to +33.5357 | no |
| HPA replicas, mean | 8.475 | 8.679 | +2.4% | −0.0147 to +0.4227 | no |
| pods started | 4.8 | 4.4 | −8.3% | −2.4566 to +1.6566 | no |
| pod start wait, total (s) | 7.1 | 6.4 | −9.9% | −4.6762 to +3.2762 | no |
| pod start wait, mean (s) | 1.323 | 1.492 | +12.7% | −0.4423 to +0.7789 | no |
| host CPU busy, the real machine under kind (%) | 28.22 | 29.86 | +5.8% | +1.1691 to +2.1081 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0023 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.7 | −0.0% | −0.2719 to +0.2636 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.7 | −0.0% | −0.2719 to +0.2636 | no |
| response time (ms), mean | 79.1 | 78.4 | −0.9% | −1.6995 to +0.3131 | no |
| response time (ms), 95th percentile | 114.1 | 112.1 | −1.7% | −3.9110 to −0.0760 | yes: GAIN |
| response time (ms), 99th percentile | 154.9 | 151.3 | −2.3% | −17.7096 to +10.5104 | no |
| time over the response line (% of samples) | 0.01205 | 0.01212 | +0.6% | −0.0407 to +0.0408 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.9 | 14.9 | −25.1% | −7.3844 to −2.6156 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.2983 | +11.2% | −0.3215 to +0.3815 | no |
| utilisation (used / allocatable) | 0.03718 | 0.03716 | −0.0% | −0.0005 to +0.0005 | no |
| CPU used (cores), mean | 0.8923 | 0.8919 | −0.0% | −0.0117 to +0.0110 | no |
| Omni's own CPU (cores), mean | 0.03619 | 0.00605 | −83.3% | −0.0342 to −0.0261 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9284 | 0.8979 | −3.3% | −0.0441 to −0.0170 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 747.8 | −0.1% | −10.9192 to +9.7787 | no |
| HPA replicas, mean | 8.905 | 8.122 | −8.8% | −1.5557 to −0.0095 | yes: GAIN |
| pods started | 4.7 | 3.4 | −27.7% | −2.5181 to −0.0819 | yes: GAIN |
| pod start wait, total (s) | 6.3 | 5.1 | −19.0% | −3.6502 to +1.2502 | no |
| pod start wait, mean (s) | 1.333 | 1.41 | +5.7% | −0.2941 to +0.4474 | no |
| host CPU busy, the real machine under kind (%) | 28.67 | 27.45 | −4.3% | −1.6992 to −0.7519 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0029 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.6 | −0.1% | −0.3814 to +0.1512 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.6 | −0.1% | −0.3814 to +0.1512 | no |
| response time (ms), mean | 79.1 | 78.09 | −1.3% | −1.8167 to −0.1946 | yes: GAIN |
| response time (ms), 95th percentile | 114.1 | 110.5 | −3.2% | −5.2110 to −1.9810 | yes: GAIN |
| response time (ms), 99th percentile | 154.9 | 149.1 | −3.7% | −14.5898 to +2.9716 | no |
| time over the response line (% of samples) | 0.01205 | 0.03615 | +200.0% | −0.0122 to +0.0604 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.9 | 17.4 | −12.6% | −4.3237 to −0.6763 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.1333 | −50.3% | −0.2965 to +0.0265 | no |
| utilisation (used / allocatable) | 0.03718 | 0.03681 | −1.0% | −0.0008 to +0.0001 | no |
| CPU used (cores), mean | 0.8923 | 0.8834 | −1.0% | −0.0190 to +0.0013 | no |
| Omni's own CPU (cores), mean | 0.03619 | 0.00681 | −81.2% | −0.0333 to −0.0255 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9284 | 0.8902 | −4.1% | −0.0511 to −0.0254 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 755 | +0.9% | −1.0582 to +14.4292 | no |
| HPA replicas, mean | 8.905 | 8.259 | −7.2% | −1.0509 to −0.2394 | yes: GAIN |
| pods started | 4.7 | 4 | −14.9% | −1.6567 to +0.2567 | no |
| pod start wait, total (s) | 6.3 | 5.7 | −9.5% | −3.5627 to +2.3627 | no |
| pod start wait, mean (s) | 1.333 | 1.41 | +5.7% | −0.4490 to +0.6023 | no |
| host CPU busy, the real machine under kind (%) | 28.67 | 27.43 | −4.3% | −1.5666 to −0.9257 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0034 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.7 | +0.0% | −0.3145 to +0.3272 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.7 | +0.0% | −0.3145 to +0.3272 | no |
| response time (ms), mean | 79.1 | 78.65 | −0.6% | −1.5143 to +0.6171 | no |
| response time (ms), 95th percentile | 114.1 | 112.5 | −1.4% | −4.2492 to +1.1532 | no |
| response time (ms), 99th percentile | 154.9 | 158.1 | +2.1% | −21.9220 to +28.3052 | no |
| time over the response line (% of samples) | 0.01205 | 0.02388 | +98.2% | −0.0151 to +0.0388 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.9 | 16.5 | −17.1% | −6.2050 to −0.5950 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.02667 | −90.1% | −0.4329 to −0.0504 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03718 | 0.03731 | +0.4% | −0.0003 to +0.0006 | no |
| CPU used (cores), mean | 0.8923 | 0.8954 | +0.4% | −0.0070 to +0.0134 | no |
| Omni's own CPU (cores), mean | 0.03619 | 0.00757 | −79.1% | −0.0324 to −0.0249 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9284 | 0.903 | −2.7% | −0.0368 to −0.0140 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 746.6 | −0.2% | −9.3388 to +5.9724 | no |
| HPA replicas, mean | 8.905 | 7.678 | −13.8% | −1.9103 to −0.5423 | yes: GAIN |
| pods started | 4.7 | 3.3 | −29.8% | −2.5285 to −0.2715 | yes: GAIN |
| pod start wait, total (s) | 6.3 | 5 | −20.6% | −3.3800 to +0.7800 | no |
| pod start wait, mean (s) | 1.333 | 1.37 | +2.7% | −0.3735 to +0.4468 | no |
| host CPU busy, the real machine under kind (%) | 28.67 | 27.71 | −3.4% | −1.3949 to −0.5315 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0030 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.8 | +0.0% | −0.1916 to +0.3117 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.8 | +0.0% | −0.1916 to +0.3117 | no |
| response time (ms), mean | 79.1 | 78.83 | −0.3% | −1.2726 to +0.7449 | no |
| response time (ms), 95th percentile | 114.1 | 113.1 | −0.9% | −3.3326 to +1.3876 | no |
| response time (ms), 99th percentile | 154.9 | 153.5 | −0.9% | −5.5096 to +2.6404 | no |
| time over the response line (% of samples) | 0.01205 | 0 | −100.0% | −0.0393 to +0.0152 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.9 | 16.2 | −18.6% | −6.7169 to −0.6831 | yes, down (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.185 | −31.1% | −0.3543 to +0.1877 | no |
| utilisation (used / allocatable) | 0.03718 | 0.03747 | +0.8% | −0.0003 to +0.0009 | no |
| CPU used (cores), mean | 0.8923 | 0.8992 | +0.8% | −0.0080 to +0.0220 | no |
| Omni's own CPU (cores), mean | 0.03619 | 0.014 | −61.3% | −0.0251 to −0.0193 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9284 | 0.9132 | −1.6% | −0.0301 to −0.0003 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 745 | −0.4% | −15.5897 to +8.8750 | no |
| HPA replicas, mean | 8.905 | 7.541 | −15.3% | −1.6613 to −1.0654 | yes: GAIN |
| pods started | 4.7 | 3.4 | −27.7% | −2.1294 to −0.4706 | yes: GAIN |
| pod start wait, total (s) | 6.3 | 5.1 | −19.0% | −2.8101 to +0.4101 | no |
| pod start wait, mean (s) | 1.333 | 1.563 | +17.2% | −0.1482 to +0.6082 | no |
| host CPU busy, the real machine under kind (%) | 28.67 | 28.01 | −2.3% | −1.1455 to −0.1883 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0011 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.8 | +0.0% | −0.1133 to +0.2112 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.8 | +0.0% | −0.1133 to +0.2112 | no |
| response time (ms), mean | 79.1 | 78.66 | −0.5% | −1.2201 to +0.3561 | no |
| response time (ms), 95th percentile | 114.1 | 112.7 | −1.2% | −2.8899 to +0.0389 | no |
| response time (ms), 99th percentile | 154.9 | 146.9 | −5.2% | −17.4293 to +1.3821 | no |
| time over the response line (% of samples) | 0.01205 | 0 | −100.0% | −0.0393 to +0.0152 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.9 | 18.9 | −5.0% | −3.6764 to +1.6764 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.3717 | +38.5% | −0.1712 to +0.3779 | no |
| utilisation (used / allocatable) | 0.03718 | 0.03731 | +0.4% | −0.0003 to +0.0006 | no |
| CPU used (cores), mean | 0.8923 | 0.8955 | +0.4% | −0.0078 to +0.0143 | no |
| Omni's own CPU (cores), mean | 0.03619 | 0.02525 | −30.2% | −0.0125 to −0.0094 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9284 | 0.9208 | −0.8% | −0.0188 to +0.0035 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 747.7 | −0.1% | −10.9378 to +9.5984 | no |
| HPA replicas, mean | 8.905 | 8.69 | −2.4% | −0.6513 to +0.2219 | no |
| pods started | 4.7 | 3.9 | −17.0% | −2.0972 to +0.4972 | no |
| pod start wait, total (s) | 6.3 | 6.5 | +3.2% | −3.0483 to +3.4483 | no |
| pod start wait, mean (s) | 1.333 | 1.602 | +20.1% | −0.1699 to +0.7066 | no |
| host CPU busy, the real machine under kind (%) | 28.67 | 28.26 | −1.4% | −0.6824 to −0.1489 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.51 | −0.3% | −0.0113 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 | −0.2% | −1.0386 to +0.3703 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 | −0.2% | −1.0386 to +0.3703 | no |
| response time (ms), mean | 79.1 | 79.19 | +0.1% | −0.6082 to +0.7953 | no |
| response time (ms), 95th percentile | 114.1 | 112.7 | −1.2% | −2.7584 to −0.0236 | yes: GAIN |
| response time (ms), 99th percentile | 154.9 | 149.8 | −3.3% | −12.3029 to +2.0087 | no |
| time over the response line (% of samples) | 0.01205 | 0 | −100.0% | −0.0393 to +0.0152 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.9 | 20.3 | +2.0% | −1.1888 to +1.9888 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.2917 | +8.7% | −0.2534 to +0.3000 | no |
| utilisation (used / allocatable) | 0.03718 | 0.03747 | +0.8% | −0.0002 to +0.0008 | no |
| CPU used (cores), mean | 0.8923 | 0.8992 | +0.8% | −0.0056 to +0.0195 | no |
| Omni's own CPU (cores), mean | 0.03619 | 0.06921 | +91.2% | +0.0286 to +0.0374 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9284 | 0.9684 | +4.3% | +0.0255 to +0.0544 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 743.7 | −0.6% | −18.8315 to +9.6039 | no |
| HPA replicas, mean | 8.905 | 8.679 | −2.5% | −0.6123 to +0.1616 | no |
| pods started | 4.7 | 4.4 | −6.4% | −0.9786 to +0.3786 | no |
| pod start wait, total (s) | 6.3 | 6.4 | +1.6% | −1.5329 to +1.7329 | no |
| pod start wait, mean (s) | 1.333 | 1.492 | +11.9% | −0.2135 to +0.5302 | no |
| host CPU busy, the real machine under kind (%) | 28.67 | 29.86 | +4.1% | +0.7041 to +1.6655 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*