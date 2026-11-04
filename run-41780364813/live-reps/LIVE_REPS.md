# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.512 | 1.512 | 1.511 | 1.511 | 1.511 | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | 158.7 | 158.7 | 158.7 | 158.8 | 158.9 | 159.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | 158.7 | 158.7 | 158.7 | 158.8 | 158.9 | 159.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 162.5 | 83.53 | 82.73 | 82.45 | 82.23 | 83.27 | 83.26 | 84.82 |
| response time (ms), 95th percentile | 372.1 | 128.6 | 127.4 | 126.2 | 126.2 | 127.7 | 127.4 | 129.7 |
| response time (ms), 99th percentile | 588.3 | 183.8 | 180.9 | 176.5 | 172.4 | 179 | 177.2 | 184.6 |
| time over the response line (% of samples) | 2.67 | 0.02424 | 0 | 0.02424 | 0 | 0 | 0.01212 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | 14.8 | 17.5 | 17.8 | 18.3 | 20.1 | 21 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | nan | nan | nan | nan | 90 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.085 | 0.1917 | 0.355 | 0.1083 | 0.1883 | 0.3017 | 0.3533 |
| utilisation (used / allocatable) | 0.0405 | 0.03847 | 0.03827 | 0.03838 | 0.03825 | 0.03861 | 0.03864 | 0.03918 |
| CPU used (cores), mean | 0.9721 | 0.9234 | 0.9186 | 0.9212 | 0.918 | 0.9267 | 0.9273 | 0.9402 |
| Omni's own CPU (cores), mean | 0 | 0.03868 | 0.0065 | 0.00743 | 0.00825 | 0.0152 | 0.02725 | 0.07365 |
| CPU used with Omni's own (cores), mean | 0.9721 | 0.9621 | 0.9251 | 0.9287 | 0.9263 | 0.9419 | 0.9545 | 1.014 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 720.9 | 730.6 | 727 | 731.6 | 717.4 | 722 | 714 |
| HPA replicas, mean | 8.585 | 9.069 | 8.566 | 8.391 | 7.842 | 8.138 | 8.674 | 8.687 |
| pods started | 4.5 | 3.2 | 2.9 | 3.4 | 3.3 | 3 | 3.4 | 3.3 |
| pod start wait, total (s) | 7.1 | 5.2 | 4.2 | 4.7 | 5 | 4.2 | 5.1 | 4.7 |
| pod start wait, mean (s) | 1.555 | 1.587 | 1.63 | 1.463 | 1.473 | 1.41 | 1.39 | 1.47 |
| host CPU busy, the real machine under kind (%) | 29.66 | 29.68 | 28.43 | 28.46 | 28.38 | 28.92 | 29.35 | 31.22 |
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
| node-hours | 1.512 | 1.512 | +0.0% | −0.0012 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | −0.3% | −0.7954 to −0.0133 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | −0.3% | −0.7954 to −0.0133 | yes: GAIN |
| response time (ms), mean | 162.5 | 83.53 | −48.6% | −101.9450 to −56.0698 | yes: GAIN |
| response time (ms), 95th percentile | 372.1 | 128.6 | −65.5% | −308.5967 to −178.5103 | yes: GAIN |
| response time (ms), 99th percentile | 588.3 | 183.8 | −68.8% | −523.4349 to −285.5529 | yes: GAIN |
| time over the response line (% of samples) | 2.67 | 0.02424 | −99.1% | −3.9269 to −1.3648 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.9146 to −1.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | +19.100 (native is 0) | +15.7542 to +22.4458 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.085 | −82.2% | −0.6184 to −0.1650 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0405 | 0.03847 | −5.0% | −0.0033 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9721 | 0.9234 | −5.0% | −0.0781 to −0.0193 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03868 | +0.039 (native is 0) | +0.0333 to +0.0440 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9721 | 0.9621 | −1.0% | −0.0351 to +0.0151 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 720.9 | +3.6% | +9.3653 to +41.1279 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.585 | 9.069 | +5.6% | +0.0362 to +0.9307 | yes: power given |
| pods started | 4.5 | 3.2 | −28.9% | −2.8099 to +0.2099 | no |
| pod start wait, total (s) | 7.1 | 5.2 | −26.8% | −4.7303 to +0.9303 | no |
| pod start wait, mean (s) | 1.555 | 1.587 | +2.0% | −0.2774 to +0.3407 | no |
| host CPU busy, the real machine under kind (%) | 29.66 | 29.68 | +0.1% | −0.4031 to +0.4426 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | −0.0% | −0.0023 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.7 | −0.3% | −0.9833 to −0.1116 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.7 | −0.3% | −0.9833 to −0.1116 | yes: GAIN |
| response time (ms), mean | 162.5 | 82.73 | −49.1% | −103.1885 to −56.4171 | yes: GAIN |
| response time (ms), 95th percentile | 372.1 | 127.4 | −65.8% | −311.0033 to −178.5367 | yes: GAIN |
| response time (ms), 99th percentile | 588.3 | 180.9 | −69.3% | −526.1764 to −288.6396 | yes: GAIN |
| time over the response line (% of samples) | 2.67 | 0 | −100.0% | −3.9632 to −1.3770 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.9146 to −1.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.8 | +14.800 (native is 0) | +13.7997 to +15.8003 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.1917 | −59.8% | −0.5694 to −0.0006 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0405 | 0.03827 | −5.5% | −0.0035 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9721 | 0.9186 | −5.5% | −0.0830 to −0.0241 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0065 | +0.007 (native is 0) | +0.0056 to +0.0074 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9721 | 0.9251 | −4.8% | −0.0759 to −0.0181 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 730.6 | +5.0% | +16.8513 to +52.9034 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.585 | 8.566 | −0.2% | −0.3356 to +0.2976 | no |
| pods started | 4.5 | 2.9 | −35.6% | −2.8251 to −0.3749 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 4.2 | −40.8% | −5.0446 to −0.7554 | yes: GAIN |
| pod start wait, mean (s) | 1.555 | 1.63 | +4.8% | −0.3055 to +0.4555 | no |
| host CPU busy, the real machine under kind (%) | 29.66 | 28.43 | −4.1% | −1.8405 to −0.6202 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.0% | −0.0021 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.7 | −0.3% | −0.8947 to −0.2121 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.7 | −0.3% | −0.8947 to −0.2121 | yes: GAIN |
| response time (ms), mean | 162.5 | 82.45 | −49.3% | −103.4435 to −56.7164 | yes: GAIN |
| response time (ms), 95th percentile | 372.1 | 126.2 | −66.1% | −311.6738 to −180.2572 | yes: GAIN |
| response time (ms), 99th percentile | 588.3 | 176.5 | −70.0% | −534.5020 to −289.0134 | yes: GAIN |
| time over the response line (% of samples) | 2.67 | 0.02424 | −99.1% | −3.9392 to −1.3525 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.9146 to −1.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.500 (native is 0) | +15.6763 to +19.3237 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.355 | −25.5% | −0.4427 to +0.1994 | no |
| utilisation (used / allocatable) | 0.0405 | 0.03838 | −5.2% | −0.0031 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9721 | 0.9212 | −5.2% | −0.0736 to −0.0281 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00743 | +0.007 (native is 0) | +0.0064 to +0.0085 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9721 | 0.9287 | −4.5% | −0.0654 to −0.0214 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 727 | +4.5% | +21.4375 to +41.2654 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.585 | 8.391 | −2.3% | −0.6190 to +0.2312 | no |
| pods started | 4.5 | 3.4 | −24.4% | −2.3818 to +0.1818 | no |
| pod start wait, total (s) | 7.1 | 4.7 | −33.8% | −4.8128 to +0.0128 | no |
| pod start wait, mean (s) | 1.555 | 1.463 | −5.9% | −0.4874 to +0.3040 | no |
| host CPU busy, the real machine under kind (%) | 29.66 | 28.46 | −4.0% | −1.7196 to −0.6688 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0029 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.7 | −0.4% | −0.9040 to −0.3045 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.7 | −0.4% | −0.9040 to −0.3045 | yes: GAIN |
| response time (ms), mean | 162.5 | 82.23 | −49.4% | −103.2577 to −57.3431 | yes: GAIN |
| response time (ms), 95th percentile | 372.1 | 126.2 | −66.1% | −310.9871 to −180.7919 | yes: GAIN |
| response time (ms), 99th percentile | 588.3 | 172.4 | −70.7% | −539.7474 to −292.0078 | yes: GAIN |
| time over the response line (% of samples) | 2.67 | 0 | −100.0% | −3.9632 to −1.3770 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.9146 to −1.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +14.3811 to +21.2189 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.1083 | −77.3% | −0.5904 to −0.1463 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0405 | 0.03825 | −5.6% | −0.0030 to −0.0015 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9721 | 0.918 | −5.6% | −0.0728 to −0.0353 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00825 | +0.008 (native is 0) | +0.0069 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9721 | 0.9263 | −4.7% | −0.0635 to −0.0281 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 731.6 | +5.2% | +26.4257 to +45.4354 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.585 | 7.842 | −8.7% | −1.2919 to −0.1952 | yes: GAIN |
| pods started | 4.5 | 3.3 | −26.7% | −2.7004 to +0.3004 | no |
| pod start wait, total (s) | 7.1 | 5 | −29.6% | −5.4458 to +1.2458 | no |
| pod start wait, mean (s) | 1.555 | 1.473 | −5.3% | −0.4551 to +0.2917 | no |
| host CPU busy, the real machine under kind (%) | 29.66 | 28.38 | −4.3% | −1.7725 to −0.7850 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0021 to +0.0005 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | −0.3% | −0.8854 to −0.1573 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | −0.3% | −0.8854 to −0.1573 | yes: GAIN |
| response time (ms), mean | 162.5 | 83.27 | −48.8% | −102.9327 to −55.5902 | yes: GAIN |
| response time (ms), 95th percentile | 372.1 | 127.7 | −65.7% | −309.8340 to −179.0510 | yes: GAIN |
| response time (ms), 99th percentile | 588.3 | 179 | −69.6% | −531.1393 to −287.3513 | yes: GAIN |
| time over the response line (% of samples) | 2.67 | 0 | −100.0% | −3.9632 to −1.3770 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.9146 to −1.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | +18.300 (native is 0) | +15.9384 to +20.6616 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.1883 | −60.5% | −0.5521 to −0.0246 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0405 | 0.03861 | −4.7% | −0.0030 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9721 | 0.9267 | −4.7% | −0.0725 to −0.0182 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0152 | +0.015 (native is 0) | +0.0131 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9721 | 0.9419 | −3.1% | −0.0556 to −0.0047 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 717.4 | +3.1% | +3.1758 to +40.1635 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.585 | 8.138 | −5.2% | −0.9114 to +0.0167 | no |
| pods started | 4.5 | 3 | −33.3% | −2.5256 to −0.4744 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 4.2 | −40.8% | −5.1733 to −0.6267 | yes: GAIN |
| pod start wait, mean (s) | 1.555 | 1.41 | −9.3% | −0.5649 to +0.2749 | no |
| host CPU busy, the real machine under kind (%) | 29.66 | 28.92 | −2.5% | −1.2891 to −0.1783 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0013 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | −0.2% | −0.7084 to +0.0253 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | −0.2% | −0.7084 to +0.0253 | no |
| response time (ms), mean | 162.5 | 83.26 | −48.8% | −102.5740 to −55.9719 | yes: GAIN |
| response time (ms), 95th percentile | 372.1 | 127.4 | −65.8% | −309.9988 to −179.3522 | yes: GAIN |
| response time (ms), 99th percentile | 588.3 | 177.2 | −69.9% | −531.8041 to −290.2629 | yes: GAIN |
| time over the response line (% of samples) | 2.67 | 0.01212 | −99.5% | −3.9421 to −1.3738 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.9146 to −1.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.1 | +20.100 (native is 0) | +18.7746 to +21.4254 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.3017 | −36.7% | −0.5697 to +0.2197 | no |
| utilisation (used / allocatable) | 0.0405 | 0.03864 | −4.6% | −0.0029 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9721 | 0.9273 | −4.6% | −0.0695 to −0.0201 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02725 | +0.027 (native is 0) | +0.0234 to +0.0311 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9721 | 0.9545 | −1.8% | −0.0397 to +0.0046 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 722 | +3.8% | +12.2374 to +40.3144 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.585 | 8.674 | +1.0% | −0.1313 to +0.3084 | no |
| pods started | 4.5 | 3.4 | −24.4% | −2.2898 to +0.0898 | no |
| pod start wait, total (s) | 7.1 | 5.1 | −28.2% | −4.5680 to +0.5680 | no |
| pod start wait, mean (s) | 1.555 | 1.39 | −10.6% | −0.5962 to +0.2662 | no |
| host CPU busy, the real machine under kind (%) | 29.66 | 29.35 | −1.0% | −0.8232 to +0.2028 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0000 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | −0.1% | −0.4678 to +0.2077 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.1 | −0.1% | −0.4678 to +0.2077 | no |
| response time (ms), mean | 162.5 | 84.82 | −47.8% | −100.4218 to −54.9992 | yes: GAIN |
| response time (ms), 95th percentile | 372.1 | 129.7 | −65.1% | −306.8274 to −177.9496 | yes: GAIN |
| response time (ms), 99th percentile | 588.3 | 184.6 | −68.6% | −518.6547 to −288.6729 | yes: GAIN |
| time over the response line (% of samples) | 2.67 | 0 | −100.0% | −3.9632 to −1.3770 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.9146 to −1.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21 | +21.000 (native is 0) | +19.6940 to +22.3060 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.3533 | −25.9% | −0.4260 to +0.1794 | no |
| utilisation (used / allocatable) | 0.0405 | 0.03918 | −3.3% | −0.0023 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9721 | 0.9402 | −3.3% | −0.0553 to −0.0084 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07365 | +0.074 (native is 0) | +0.0640 to +0.0833 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9721 | 1.014 | +4.3% | +0.0226 to +0.0610 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.7 | 714 | +2.6% | +5.6208 to +31.0497 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.585 | 8.687 | +1.2% | −0.0566 to +0.2609 | no |
| pods started | 4.5 | 3.3 | −26.7% | −2.2556 to −0.1444 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 4.7 | −33.8% | −3.9888 to −0.8112 | yes: GAIN |
| pod start wait, mean (s) | 1.555 | 1.47 | −5.5% | −0.5115 to +0.3415 | no |
| host CPU busy, the real machine under kind (%) | 29.66 | 31.22 | +5.3% | +1.1419 to +1.9736 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | −0.1% | −0.0025 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | −0.1% | −0.3892 to +0.1029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | −0.1% | −0.3892 to +0.1029 | no |
| response time (ms), mean | 83.53 | 82.73 | −1.0% | −1.8958 to +0.3050 | no |
| response time (ms), 95th percentile | 128.6 | 127.4 | −0.9% | −4.3561 to +1.9231 | no |
| response time (ms), 99th percentile | 183.8 | 180.9 | −1.6% | −15.9511 to +10.1229 | no |
| time over the response line (% of samples) | 0.02424 | 0 | −100.0% | −0.0608 to +0.0123 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 14.8 | −22.5% | −7.7888 to −0.8112 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.1917 | +125.5% | −0.1297 to +0.3431 | no |
| utilisation (used / allocatable) | 0.03847 | 0.03827 | −0.5% | −0.0007 to +0.0003 | no |
| CPU used (cores), mean | 0.9234 | 0.9186 | −0.5% | −0.0167 to +0.0070 | no |
| Omni's own CPU (cores), mean | 0.03868 | 0.0065 | −83.2% | −0.0367 to −0.0277 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9621 | 0.9251 | −3.8% | −0.0477 to −0.0263 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 730.6 | +1.3% | −7.6745 to +26.9360 | no |
| HPA replicas, mean | 9.069 | 8.566 | −5.5% | −0.8716 to −0.1332 | yes: GAIN |
| pods started | 3.2 | 2.9 | −9.4% | −1.3690 to +0.7690 | no |
| pod start wait, total (s) | 5.2 | 4.2 | −19.2% | −2.7521 to +0.7521 | no |
| pod start wait, mean (s) | 1.587 | 1.63 | +2.7% | −0.2941 to +0.3807 | no |
| host CPU busy, the real machine under kind (%) | 29.68 | 28.43 | −4.2% | −1.6168 to −0.8835 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0027 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | −0.1% | −0.3992 to +0.1010 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | −0.1% | −0.3992 to +0.1010 | no |
| response time (ms), mean | 83.53 | 82.45 | −1.3% | −2.0280 to −0.1171 | yes: GAIN |
| response time (ms), 95th percentile | 128.6 | 126.2 | −1.9% | −4.5715 to −0.2525 | yes: GAIN |
| response time (ms), 99th percentile | 183.8 | 176.5 | −4.0% | −16.0924 to +1.5648 | no |
| time over the response line (% of samples) | 0.02424 | 0.02424 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 17.5 | −8.4% | −5.5784 to +2.3784 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.355 | +317.6% | +0.0203 to +0.5197 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03847 | 0.03838 | −0.2% | −0.0008 to +0.0006 | no |
| CPU used (cores), mean | 0.9234 | 0.9212 | −0.2% | −0.0189 to +0.0146 | no |
| Omni's own CPU (cores), mean | 0.03868 | 0.00743 | −80.8% | −0.0356 to −0.0269 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9621 | 0.9287 | −3.5% | −0.0492 to −0.0176 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 727 | +0.8% | −7.3286 to +19.5384 | no |
| HPA replicas, mean | 9.069 | 8.391 | −7.5% | −1.0331 to −0.3216 | yes: GAIN |
| pods started | 3.2 | 3.4 | +6.3% | −1.2226 to +1.6226 | no |
| pod start wait, total (s) | 5.2 | 4.7 | −9.6% | −2.9606 to +1.9606 | no |
| pod start wait, mean (s) | 1.587 | 1.463 | −7.8% | −0.4254 to +0.1787 | no |
| host CPU busy, the real machine under kind (%) | 29.68 | 28.46 | −4.1% | −1.4989 to −0.9291 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0037 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | −0.1% | −0.5078 to +0.1080 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | −0.1% | −0.5078 to +0.1080 | no |
| response time (ms), mean | 83.53 | 82.23 | −1.5% | −1.8908 to −0.6952 | yes: GAIN |
| response time (ms), 95th percentile | 128.6 | 126.2 | −1.8% | −3.6246 to −1.0474 | yes: GAIN |
| response time (ms), 99th percentile | 183.8 | 172.4 | −6.2% | −22.8945 to +0.1271 | no |
| time over the response line (% of samples) | 0.02424 | 0 | −100.0% | −0.0608 to +0.0123 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 17.8 | −6.8% | −5.2905 to +2.6905 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.1083 | +27.5% | −0.0878 to +0.1345 | no |
| utilisation (used / allocatable) | 0.03847 | 0.03825 | −0.6% | −0.0008 to +0.0003 | no |
| CPU used (cores), mean | 0.9234 | 0.918 | −0.6% | −0.0189 to +0.0082 | no |
| Omni's own CPU (cores), mean | 0.03868 | 0.00825 | −78.7% | −0.0344 to −0.0264 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9621 | 0.9263 | −3.7% | −0.0467 to −0.0249 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 731.6 | +1.5% | −5.3672 to +26.7351 | no |
| HPA replicas, mean | 9.069 | 7.842 | −13.5% | −1.8029 to −0.6510 | yes: GAIN |
| pods started | 3.2 | 3.3 | +3.1% | −0.9366 to +1.1366 | no |
| pod start wait, total (s) | 5.2 | 5 | −3.8% | −2.4570 to +2.0570 | no |
| pod start wait, mean (s) | 1.587 | 1.473 | −7.1% | −0.4783 to +0.2516 | no |
| host CPU busy, the real machine under kind (%) | 29.68 | 28.38 | −4.4% | −1.6038 to −0.9933 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0030 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.1% | −0.3806 to +0.1466 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.1% | −0.3806 to +0.1466 | no |
| response time (ms), mean | 83.53 | 83.27 | −0.3% | −1.4595 to +0.9513 | no |
| response time (ms), 95th percentile | 128.6 | 127.7 | −0.7% | −3.2417 to +1.4637 | no |
| response time (ms), 99th percentile | 183.8 | 179 | −2.6% | −13.1063 to +3.6035 | no |
| time over the response line (% of samples) | 0.02424 | 0 | −100.0% | −0.0608 to +0.0123 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 18.3 | −4.2% | −4.5820 to +2.9820 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.1883 | +121.6% | −0.0848 to +0.2915 | no |
| utilisation (used / allocatable) | 0.03847 | 0.03861 | +0.4% | −0.0005 to +0.0007 | no |
| CPU used (cores), mean | 0.9234 | 0.9267 | +0.4% | −0.0109 to +0.0176 | no |
| Omni's own CPU (cores), mean | 0.03868 | 0.0152 | −60.7% | −0.0268 to −0.0202 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9621 | 0.9419 | −2.1% | −0.0349 to −0.0054 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 717.4 | −0.5% | −15.5773 to +8.4234 | no |
| HPA replicas, mean | 9.069 | 8.138 | −10.3% | −1.3295 to −0.5320 | yes: GAIN |
| pods started | 3.2 | 3 | −6.3% | −0.8573 to +0.4573 | no |
| pod start wait, total (s) | 5.2 | 4.2 | −19.2% | −2.4698 to +0.4698 | no |
| pod start wait, mean (s) | 1.587 | 1.41 | −11.1% | −0.5730 to +0.2196 | no |
| host CPU busy, the real machine under kind (%) | 29.68 | 28.92 | −2.5% | −1.2606 to −0.2463 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0022 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.9 | +0.0% | −0.2334 to +0.3590 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.9 | +0.0% | −0.2334 to +0.3590 | no |
| response time (ms), mean | 83.53 | 83.26 | −0.3% | −1.4189 to +0.8877 | no |
| response time (ms), 95th percentile | 128.6 | 127.4 | −0.9% | −3.3705 to +1.1265 | no |
| response time (ms), 99th percentile | 183.8 | 177.2 | −3.6% | −14.5825 to +1.5033 | no |
| time over the response line (% of samples) | 0.02424 | 0.01212 | −50.0% | −0.0613 to +0.0371 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 20.1 | +5.2% | −2.5366 to +4.5366 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 90 | +12.5% | −30.6041 to +50.6041 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.3017 | +254.9% | −0.0862 to +0.5195 | no |
| utilisation (used / allocatable) | 0.03847 | 0.03864 | +0.4% | −0.0003 to +0.0006 | no |
| CPU used (cores), mean | 0.9234 | 0.9273 | +0.4% | −0.0062 to +0.0140 | no |
| Omni's own CPU (cores), mean | 0.03868 | 0.02725 | −29.6% | −0.0130 to −0.0098 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9621 | 0.9545 | −0.8% | −0.0169 to +0.0019 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 722 | +0.1% | −12.4843 to +14.5430 | no |
| HPA replicas, mean | 9.069 | 8.674 | −4.4% | −0.8143 to +0.0246 | no |
| pods started | 3.2 | 3.4 | +6.3% | −1.3004 to +1.7004 | no |
| pod start wait, total (s) | 5.2 | 5.1 | −1.9% | −2.4228 to +2.2228 | no |
| pod start wait, mean (s) | 1.587 | 1.39 | −12.4% | −0.5509 to +0.1576 | no |
| host CPU busy, the real machine under kind (%) | 29.68 | 29.35 | −1.1% | −0.7093 to +0.0493 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0002 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.1 | +0.2% | +0.0282 to +0.5203 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.1 | +0.2% | +0.0282 to +0.5203 | yes: power given |
| response time (ms), mean | 83.53 | 84.82 | +1.6% | +0.1426 to +2.4511 | yes: LOSS |
| response time (ms), 95th percentile | 128.6 | 129.7 | +0.9% | −1.0548 to +3.3848 | no |
| response time (ms), 99th percentile | 183.8 | 184.6 | +0.5% | −7.1320 to +8.7922 | no |
| time over the response line (% of samples) | 0.02424 | 0 | −100.0% | −0.0608 to +0.0123 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 21 | +9.9% | −1.7231 to +5.5231 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 100 | +25.0% | −10.1600 to +50.1600 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.3533 | +315.7% | +0.0683 to +0.4684 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03847 | 0.03918 | +1.8% | +0.0001 to +0.0013 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9234 | 0.9402 | +1.8% | +0.0021 to +0.0316 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03868 | 0.07365 | +90.4% | +0.0305 to +0.0394 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9621 | 1.014 | +5.4% | +0.0335 to +0.0701 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 714 | −1.0% | −17.5480 to +3.7252 | no |
| HPA replicas, mean | 9.069 | 8.687 | −4.2% | −0.8292 to +0.0667 | no |
| pods started | 3.2 | 3.3 | +3.1% | −1.2254 to +1.4254 | no |
| pod start wait, total (s) | 5.2 | 4.7 | −9.6% | −2.7176 to +1.7176 | no |
| pod start wait, mean (s) | 1.587 | 1.47 | −7.4% | −0.4558 to +0.2225 | no |
| host CPU busy, the real machine under kind (%) | 29.68 | 31.22 | +5.2% | +1.0826 to +1.9935 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*