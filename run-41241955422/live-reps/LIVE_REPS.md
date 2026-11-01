# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.512 | 1.512 | 1.511 | 1.511 | 1.513 | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.2 | 158 | 157.8 | 157.9 | 158.1 | 158.1 | 158.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.2 | 158 | 157.8 | 157.9 | 158.1 | 158.1 | 158.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 141.3 | 75.33 | 73.07 | 72.6 | 73.67 | 73.62 | 73.61 | 74.52 |
| response time (ms), 95th percentile | 311 | 117.7 | 106.2 | 105.5 | 107.9 | 107.3 | 107.5 | 109.6 |
| response time (ms), 99th percentile | 491.8 | 151.7 | 142.6 | 144.6 | 144.3 | 145.8 | 148.8 | 150.6 |
| time over the response line (% of samples) | 1.679 | 0 | 0 | 0 | 0.02424 | 0.01212 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | 16 | 17.1 | 16.8 | 17.9 | 20.2 | 20.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.295 | 0.3133 | 0.2933 | 0.1267 | 0.1883 | 0.51 | 0.3167 |
| utilisation (used / allocatable) | 0.0362 | 0.03556 | 0.03449 | 0.03434 | 0.03485 | 0.03475 | 0.03464 | 0.03512 |
| CPU used (cores), mean | 0.8687 | 0.8534 | 0.8279 | 0.8243 | 0.8363 | 0.834 | 0.8314 | 0.8429 |
| Omni's own CPU (cores), mean | 0 | 0.00858 | 0.00609 | 0.00669 | 0.00748 | 0.01411 | 0.02478 | 0.06815 |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.862 | 0.834 | 0.831 | 0.8438 | 0.8481 | 0.8562 | 0.911 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 787.9 | 807.3 | 814.9 | 795.4 | 805 | 806.6 | 794.4 |
| HPA replicas, mean | 8.211 | 7.968 | 7.931 | 8.11 | 7.292 | 7.322 | 8.338 | 8.491 |
| pods started | 5.4 | 4.2 | 4.9 | 4.1 | 3.2 | 3.6 | 5 | 4 |
| pod start wait, total (s) | 9.2 | 6.1 | 7.9 | 6.4 | 4.6 | 6.1 | 7.1 | 6 |
| pod start wait, mean (s) | 1.707 | 1.443 | 1.673 | 1.607 | 1.432 | 1.688 | 1.408 | 1.502 |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.55 | 25.88 | 25.72 | 26.01 | 26.21 | 26.57 | 28.32 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.512 | +0.0% | −0.0006 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.2 | −0.0% | −0.4920 to +0.3673 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.2 | −0.0% | −0.4920 to +0.3673 | no |
| response time (ms), mean | 141.3 | 75.33 | −46.7% | −90.1429 to −41.8853 | yes: GAIN |
| response time (ms), 95th percentile | 311 | 117.7 | −62.2% | −255.6477 to −131.0573 | yes: GAIN |
| response time (ms), 99th percentile | 491.8 | 151.7 | −69.1% | −462.1079 to −217.9507 | yes: GAIN |
| time over the response line (% of samples) | 1.679 | 0 | −100.0% | −3.0949 to −0.2623 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1155 to −0.0845 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | +16.900 (native is 0) | +14.5049 to +19.2951 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.295 | +55.3% | −0.1972 to +0.4072 | no |
| utilisation (used / allocatable) | 0.0362 | 0.03556 | −1.8% | −0.0022 to +0.0009 | no |
| CPU used (cores), mean | 0.8687 | 0.8534 | −1.8% | −0.0520 to +0.0213 | no |
| Omni's own CPU (cores), mean | 0 | 0.00858 | +0.009 (native is 0) | +0.0072 to +0.0100 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.862 | −0.8% | −0.0428 to +0.0292 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 787.9 | +0.2% | −27.5759 to +31.4061 | no |
| HPA replicas, mean | 8.211 | 7.968 | −3.0% | −0.8258 to +0.3405 | no |
| pods started | 5.4 | 4.2 | −22.2% | −2.2556 to −0.1444 | yes: GAIN |
| pod start wait, total (s) | 9.2 | 6.1 | −33.7% | −6.0866 to −0.1134 | yes: GAIN |
| pod start wait, mean (s) | 1.707 | 1.443 | −15.4% | −0.6439 to +0.1172 | no |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.55 | −0.6% | −0.9797 to +0.6594 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | +0.1% | −0.0005 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158 | −0.2% | −0.6722 to +0.0514 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158 | −0.2% | −0.6722 to +0.0514 | no |
| response time (ms), mean | 141.3 | 73.07 | −48.3% | −93.3410 to −43.2055 | yes: GAIN |
| response time (ms), 95th percentile | 311 | 106.2 | −65.9% | −272.2333 to −137.4797 | yes: GAIN |
| response time (ms), 99th percentile | 491.8 | 142.6 | −71.0% | −473.5975 to −224.6689 | yes: GAIN |
| time over the response line (% of samples) | 1.679 | 0 | −100.0% | −3.0949 to −0.2623 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1155 to −0.0845 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16.000 (native is 0) | +14.8319 to +17.1681 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.3133 | +64.9% | −0.0972 to +0.3438 | no |
| utilisation (used / allocatable) | 0.0362 | 0.03449 | −4.7% | −0.0030 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8687 | 0.8279 | −4.7% | −0.0727 to −0.0090 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00609 | +0.006 (native is 0) | +0.0050 to +0.0071 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.834 | −4.0% | −0.0658 to −0.0038 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 807.3 | +2.7% | +3.4165 to +39.2257 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.211 | 7.931 | −3.4% | −0.4484 to −0.1109 | yes: GAIN |
| pods started | 5.4 | 4.9 | −9.3% | −1.1079 to +0.1079 | no |
| pod start wait, total (s) | 9.2 | 7.9 | −14.1% | −3.7093 to +1.1093 | no |
| pod start wait, mean (s) | 1.707 | 1.673 | −2.0% | −0.6415 to +0.5749 | no |
| host CPU busy, the real machine under kind (%) | 26.71 | 25.88 | −3.1% | −1.4659 to −0.1939 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0027 to +0.0011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.8 | −0.3% | −0.9467 to −0.0697 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.8 | −0.3% | −0.9467 to −0.0697 | yes: GAIN |
| response time (ms), mean | 141.3 | 72.6 | −48.6% | −93.6400 to −43.8529 | yes: GAIN |
| response time (ms), 95th percentile | 311 | 105.5 | −66.1% | −272.5922 to −138.4478 | yes: GAIN |
| response time (ms), 99th percentile | 491.8 | 144.6 | −70.6% | −474.6161 to −219.6663 | yes: GAIN |
| time over the response line (% of samples) | 1.679 | 0 | −100.0% | −3.0949 to −0.2623 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1155 to −0.0845 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.100 (native is 0) | +14.8018 to +19.3982 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.2933 | +54.4% | −0.1378 to +0.3445 | no |
| utilisation (used / allocatable) | 0.0362 | 0.03434 | −5.1% | −0.0030 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8687 | 0.8243 | −5.1% | −0.0727 to −0.0163 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00669 | +0.007 (native is 0) | +0.0056 to +0.0078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.831 | −4.4% | −0.0652 to −0.0104 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 814.9 | +3.7% | +17.8704 to +39.9836 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.211 | 8.11 | −1.2% | −0.3926 to +0.1909 | no |
| pods started | 5.4 | 4.1 | −24.1% | −2.4209 to −0.1791 | yes: GAIN |
| pod start wait, total (s) | 9.2 | 6.4 | −30.4% | −5.1068 to −0.4932 | yes: GAIN |
| pod start wait, mean (s) | 1.707 | 1.607 | −5.9% | −0.5186 to +0.3186 | no |
| host CPU busy, the real machine under kind (%) | 26.71 | 25.72 | −3.7% | −1.6333 to −0.3340 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0033 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | −0.2% | −0.8638 to +0.1130 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | −0.2% | −0.8638 to +0.1130 | no |
| response time (ms), mean | 141.3 | 73.67 | −47.9% | −93.0043 to −42.3389 | yes: GAIN |
| response time (ms), 95th percentile | 311 | 107.9 | −65.3% | −271.9487 to −134.2913 | yes: GAIN |
| response time (ms), 99th percentile | 491.8 | 144.3 | −70.7% | −470.9968 to −223.9776 | yes: GAIN |
| time over the response line (% of samples) | 1.679 | 0.02424 | −98.6% | −3.0502 to −0.2584 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1155 to −0.0845 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.8 | +16.800 (native is 0) | +12.6867 to +20.9133 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.1267 | −33.3% | −0.2775 to +0.1508 | no |
| utilisation (used / allocatable) | 0.0362 | 0.03485 | −3.7% | −0.0029 to +0.0002 | no |
| CPU used (cores), mean | 0.8687 | 0.8363 | −3.7% | −0.0692 to +0.0043 | no |
| Omni's own CPU (cores), mean | 0 | 0.00748 | +0.007 (native is 0) | +0.0060 to +0.0089 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.8438 | −2.9% | −0.0604 to +0.0105 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 795.4 | +1.2% | −24.5332 to +43.3424 | no |
| HPA replicas, mean | 8.211 | 7.292 | −11.2% | −1.4988 to −0.3387 | yes: GAIN |
| pods started | 5.4 | 3.2 | −40.7% | −3.0121 to −1.3879 | yes: GAIN |
| pod start wait, total (s) | 9.2 | 4.6 | −50.0% | −6.5429 to −2.6571 | yes: GAIN |
| pod start wait, mean (s) | 1.707 | 1.432 | −16.1% | −0.6088 to +0.0588 | no |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.01 | −2.6% | −1.5521 to +0.1468 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0008 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | −0.1% | −0.6084 to +0.2126 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | −0.1% | −0.6084 to +0.2126 | no |
| response time (ms), mean | 141.3 | 73.62 | −47.9% | −92.1624 to −43.2913 | yes: GAIN |
| response time (ms), 95th percentile | 311 | 107.3 | −65.5% | −271.0423 to −136.5027 | yes: GAIN |
| response time (ms), 99th percentile | 491.8 | 145.8 | −70.3% | −467.0774 to −224.7872 | yes: GAIN |
| time over the response line (% of samples) | 1.679 | 0.01212 | −99.3% | −3.0723 to −0.2606 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1155 to −0.0845 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | +17.900 (native is 0) | +14.5884 to +21.2116 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.1883 | −0.9% | −0.1230 to +0.1197 | no |
| utilisation (used / allocatable) | 0.0362 | 0.03475 | −4.0% | −0.0026 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8687 | 0.834 | −4.0% | −0.0624 to −0.0071 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01411 | +0.014 (native is 0) | +0.0116 to +0.0166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.8481 | −2.4% | −0.0463 to +0.0051 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 805 | +2.4% | +3.1562 to +34.9297 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.211 | 7.322 | −10.8% | −1.4326 to −0.3462 | yes: GAIN |
| pods started | 5.4 | 3.6 | −33.3% | −2.6121 to −0.9879 | yes: GAIN |
| pod start wait, total (s) | 9.2 | 6.1 | −33.7% | −4.8667 to −1.3333 | yes: GAIN |
| pod start wait, mean (s) | 1.707 | 1.688 | −1.1% | −0.3305 to +0.2938 | no |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.21 | −1.9% | −1.0706 to +0.0639 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0012 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | −0.1% | −0.7013 to +0.2427 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | −0.1% | −0.7013 to +0.2427 | no |
| response time (ms), mean | 141.3 | 73.61 | −47.9% | −92.3064 to −43.1544 | yes: GAIN |
| response time (ms), 95th percentile | 311 | 107.5 | −65.4% | −270.6871 to −136.3869 | yes: GAIN |
| response time (ms), 99th percentile | 491.8 | 148.8 | −69.7% | −468.1934 to −217.8012 | yes: GAIN |
| time over the response line (% of samples) | 1.679 | 0 | −100.0% | −3.0949 to −0.2623 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1155 to −0.0845 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.2 | +20.200 (native is 0) | +18.8597 to +21.5403 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.51 | +168.4% | −0.0115 to +0.6515 | no |
| utilisation (used / allocatable) | 0.0362 | 0.03464 | −4.3% | −0.0028 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8687 | 0.8314 | −4.3% | −0.0681 to −0.0066 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02478 | +0.025 (native is 0) | +0.0209 to +0.0286 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.8562 | −1.4% | −0.0407 to +0.0155 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 806.6 | +2.6% | +4.1707 to +37.0569 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.211 | 8.338 | +1.5% | −0.0730 to +0.3262 | no |
| pods started | 5.4 | 5 | −7.4% | −1.1689 to +0.3689 | no |
| pod start wait, total (s) | 9.2 | 7.1 | −22.8% | −4.2179 to +0.0179 | no |
| pod start wait, mean (s) | 1.707 | 1.408 | −17.5% | −0.5841 to −0.0125 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.57 | −0.5% | −0.7733 to +0.4898 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0004 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | −0.1% | −0.4699 to +0.1765 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | −0.1% | −0.4699 to +0.1765 | no |
| response time (ms), mean | 141.3 | 74.52 | −47.3% | −90.8523 to −42.7930 | yes: GAIN |
| response time (ms), 95th percentile | 311 | 109.6 | −64.8% | −267.6608 to −135.2112 | yes: GAIN |
| response time (ms), 99th percentile | 491.8 | 150.6 | −69.4% | −458.2993 to −224.0777 | yes: GAIN |
| time over the response line (% of samples) | 1.679 | 0 | −100.0% | −3.0949 to −0.2623 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −3.1155 to −0.0845 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.7 | +20.700 (native is 0) | +18.7037 to +22.6963 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.3167 | +66.7% | −0.1759 to +0.4292 | no |
| utilisation (used / allocatable) | 0.0362 | 0.03512 | −3.0% | −0.0022 to +0.0000 | no |
| CPU used (cores), mean | 0.8687 | 0.8429 | −3.0% | −0.0519 to +0.0001 | no |
| Omni's own CPU (cores), mean | 0 | 0.06815 | +0.068 (native is 0) | +0.0568 to +0.0795 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8687 | 0.911 | +4.9% | +0.0245 to +0.0600 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 786 | 794.4 | +1.1% | −11.2360 to +28.2204 | no |
| HPA replicas, mean | 8.211 | 8.491 | +3.4% | +0.0795 to +0.4799 | yes: power given |
| pods started | 5.4 | 4 | −25.9% | −2.3656 to −0.4344 | yes: GAIN |
| pod start wait, total (s) | 9.2 | 6 | −34.8% | −5.8293 to −0.5707 | yes: GAIN |
| pod start wait, mean (s) | 1.707 | 1.502 | −12.0% | −0.5973 to +0.1873 | no |
| host CPU busy, the real machine under kind (%) | 26.71 | 28.32 | +6.0% | +1.3353 to +1.8880 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | +0.0% | −0.0013 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158 | −0.2% | −0.6347 to +0.1387 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158 | −0.2% | −0.6347 to +0.1387 | no |
| response time (ms), mean | 75.33 | 73.07 | −3.0% | −5.2360 to +0.7177 | no |
| response time (ms), 95th percentile | 117.7 | 106.2 | −9.8% | −30.3045 to +7.2965 | no |
| response time (ms), 99th percentile | 151.7 | 142.6 | −6.0% | −23.9085 to +5.7007 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 16 | −5.3% | −2.6667 to +0.8667 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.3133 | +6.2% | −0.3188 to +0.3555 | no |
| utilisation (used / allocatable) | 0.03556 | 0.03449 | −3.0% | −0.0025 to +0.0003 | no |
| CPU used (cores), mean | 0.8534 | 0.8279 | −3.0% | −0.0590 to +0.0079 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.00609 | −29.0% | −0.0029 to −0.0021 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.862 | 0.834 | −3.2% | −0.0616 to +0.0056 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 787.9 | 807.3 | +2.5% | −2.6129 to +41.4248 | no |
| HPA replicas, mean | 7.968 | 7.931 | −0.5% | −0.6300 to +0.5560 | no |
| pods started | 4.2 | 4.9 | +16.7% | −0.4705 to +1.8705 | no |
| pod start wait, total (s) | 6.1 | 7.9 | +29.5% | −0.7189 to +4.3189 | no |
| pod start wait, mean (s) | 1.443 | 1.673 | +15.9% | −0.3454 to +0.8054 | no |
| host CPU busy, the real machine under kind (%) | 26.55 | 25.88 | −2.5% | −1.4678 to +0.1283 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0031 to +0.0001 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 157.8 | −0.3% | −0.8922 to +0.0005 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 157.8 | −0.3% | −0.8922 to +0.0005 | no |
| response time (ms), mean | 75.33 | 72.6 | −3.6% | −5.2216 to −0.2431 | yes: GAIN |
| response time (ms), 95th percentile | 117.7 | 105.5 | −10.3% | −30.9586 to +6.6236 | no |
| response time (ms), 99th percentile | 151.7 | 144.6 | −4.7% | −19.9070 to +5.6832 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 17.1 | +1.2% | −1.6714 to +2.0714 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.2933 | −0.6% | −0.3389 to +0.3356 | no |
| utilisation (used / allocatable) | 0.03556 | 0.03434 | −3.4% | −0.0025 to +0.0000 | no |
| CPU used (cores), mean | 0.8534 | 0.8243 | −3.4% | −0.0591 to +0.0009 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.00669 | −22.0% | −0.0023 to −0.0015 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.862 | 0.831 | −3.6% | −0.0611 to −0.0009 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 787.9 | 814.9 | +3.4% | +1.6552 to +52.3686 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.968 | 8.11 | +1.8% | −0.2455 to +0.5291 | no |
| pods started | 4.2 | 4.1 | −2.4% | −1.0802 to +0.8802 | no |
| pod start wait, total (s) | 6.1 | 6.4 | +4.9% | −1.6385 to +2.2385 | no |
| pod start wait, mean (s) | 1.443 | 1.607 | +11.3% | −0.1553 to +0.4819 | no |
| host CPU busy, the real machine under kind (%) | 26.55 | 25.72 | −3.1% | −1.5475 to −0.0994 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0033 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 157.9 | −0.2% | −0.6666 to +0.0406 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 157.9 | −0.2% | −0.6666 to +0.0406 | no |
| response time (ms), mean | 75.33 | 73.67 | −2.2% | −4.3315 to +1.0165 | no |
| response time (ms), 95th percentile | 117.7 | 107.9 | −8.3% | −29.2622 to +9.7272 | no |
| response time (ms), 99th percentile | 151.7 | 144.3 | −4.9% | −28.8626 to +13.9468 | no |
| time over the response line (% of samples) | 0 | 0.02424 | +0.024 (native is 0) | −0.0306 to +0.0791 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 16.8 | −0.6% | −3.9068 to +3.7068 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.1267 | −57.1% | −0.4521 to +0.1154 | no |
| utilisation (used / allocatable) | 0.03556 | 0.03485 | −2.0% | −0.0021 to +0.0007 | no |
| CPU used (cores), mean | 0.8534 | 0.8363 | −2.0% | −0.0501 to +0.0160 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.00748 | −12.8% | −0.0015 to −0.0007 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.862 | 0.8438 | −2.1% | −0.0512 to +0.0149 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 787.9 | 795.4 | +1.0% | −10.5045 to +25.4835 | no |
| HPA replicas, mean | 7.968 | 7.292 | −8.5% | −1.4151 to +0.0630 | no |
| pods started | 4.2 | 3.2 | −23.8% | −2.3903 to +0.3903 | no |
| pod start wait, total (s) | 6.1 | 4.6 | −24.6% | −4.0064 to +1.0064 | no |
| pod start wait, mean (s) | 1.443 | 1.432 | −0.8% | −0.2763 to +0.2530 | no |
| host CPU busy, the real machine under kind (%) | 26.55 | 26.01 | −2.0% | −1.2294 to +0.1445 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0010 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.1 | −0.1% | −0.5007 to +0.2297 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158.1 | −0.1% | −0.5007 to +0.2297 | no |
| response time (ms), mean | 75.33 | 73.62 | −2.3% | −4.7245 to +1.2990 | no |
| response time (ms), 95th percentile | 117.7 | 107.3 | −8.9% | −28.9202 to +8.0802 | no |
| response time (ms), 99th percentile | 151.7 | 145.8 | −3.9% | −22.6451 to +10.8391 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 17.9 | +5.9% | −2.5686 to +4.5686 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.1883 | −36.2% | −0.4053 to +0.1919 | no |
| utilisation (used / allocatable) | 0.03556 | 0.03475 | −2.3% | −0.0022 to +0.0005 | no |
| CPU used (cores), mean | 0.8534 | 0.834 | −2.3% | −0.0517 to +0.0130 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.01411 | +64.5% | +0.0044 to +0.0066 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.862 | 0.8481 | −1.6% | −0.0461 to +0.0184 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 787.9 | 805 | +2.2% | −10.7573 to +45.0131 | no |
| HPA replicas, mean | 7.968 | 7.322 | −8.1% | −1.4603 to +0.1668 | no |
| pods started | 4.2 | 3.6 | −14.3% | −2.1155 to +0.9155 | no |
| pod start wait, total (s) | 6.1 | 6.1 | ±0.0% | −2.8212 to +2.8212 | no |
| pod start wait, mean (s) | 1.443 | 1.688 | +17.0% | −0.1811 to +0.6711 | no |
| host CPU busy, the real machine under kind (%) | 26.55 | 26.21 | −1.3% | −1.0639 to +0.3775 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0012 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.1 | −0.1% | −0.5059 to +0.1721 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158.1 | −0.1% | −0.5059 to +0.1721 | no |
| response time (ms), mean | 75.33 | 73.61 | −2.3% | −4.2209 to +0.7882 | no |
| response time (ms), 95th percentile | 117.7 | 107.5 | −8.7% | −28.9258 to +8.5568 | no |
| response time (ms), 99th percentile | 151.7 | 148.8 | −2.0% | −22.7439 to +16.8079 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 20.2 | +19.5% | +1.3037 to +5.2963 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.51 | +72.9% | −0.2048 to +0.6348 | no |
| utilisation (used / allocatable) | 0.03556 | 0.03464 | −2.6% | −0.0021 to +0.0003 | no |
| CPU used (cores), mean | 0.8534 | 0.8314 | −2.6% | −0.0500 to +0.0060 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.02478 | +188.8% | +0.0138 to +0.0186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.862 | 0.8562 | −0.7% | −0.0334 to +0.0218 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 787.9 | 806.6 | +2.4% | −5.8916 to +43.2890 | no |
| HPA replicas, mean | 7.968 | 8.338 | +4.6% | −0.1782 to +0.9167 | no |
| pods started | 4.2 | 5 | +19.0% | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 6.1 | 7.1 | +16.4% | −1.0232 to +3.0232 | no |
| pod start wait, mean (s) | 1.443 | 1.408 | −2.4% | −0.2663 to +0.1963 | no |
| host CPU busy, the real machine under kind (%) | 26.55 | 26.57 | +0.1% | −0.6942 to +0.7311 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0009 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.1 | −0.1% | −0.4731 to +0.3044 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158.1 | −0.1% | −0.4731 to +0.3044 | no |
| response time (ms), mean | 75.33 | 74.52 | −1.1% | −3.2806 to +1.6636 | no |
| response time (ms), 95th percentile | 117.7 | 109.6 | −6.9% | −27.2952 to +11.1282 | no |
| response time (ms), 99th percentile | 151.7 | 150.6 | −0.8% | −17.0921 to +14.7737 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 20.7 | +22.5% | +1.4204 to +6.1796 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.3167 | +7.3% | −0.3441 to +0.3874 | no |
| utilisation (used / allocatable) | 0.03556 | 0.03512 | −1.2% | −0.0018 to +0.0009 | no |
| CPU used (cores), mean | 0.8534 | 0.8429 | −1.2% | −0.0429 to +0.0219 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.06815 | +694.3% | +0.0497 to +0.0695 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.862 | 0.911 | +5.7% | +0.0166 to +0.0815 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 787.9 | 794.4 | +0.8% | −20.6853 to +33.8395 | no |
| HPA replicas, mean | 7.968 | 8.491 | +6.6% | −0.0313 to +1.0761 | no |
| pods started | 4.2 | 4 | −4.8% | −1.2003 to +0.8003 | no |
| pod start wait, total (s) | 6.1 | 6 | −1.6% | −2.4712 to +2.2712 | no |
| pod start wait, mean (s) | 1.443 | 1.502 | +4.0% | −0.2718 to +0.3885 | no |
| host CPU busy, the real machine under kind (%) | 26.55 | 28.32 | +6.7% | +0.8920 to +2.6517 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*