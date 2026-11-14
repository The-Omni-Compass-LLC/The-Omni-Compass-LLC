# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.509 | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 169.9 | 170.5 | 170.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.9 | 170.5 | 170.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 401.4 | 416.3 | 351.4 |
| response time (ms), 95th percentile | 1657 | 1824 | 1643 |
| response time (ms), 99th percentile | 4256 | 4721 | 3844 |
| time over the response line (% of samples) | 17.34 | 18.79 | 16.79 |
| failed requests (%) | 2.099 | 1.104 | 1.843 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.9 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 137 | 53.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.487 | 1.417 | 1.513 |
| utilisation (used / allocatable) | 0.08859 | 0.08783 | 0.08754 |
| CPU used (cores), mean | 2.126 | 2.108 | 2.101 |
| Omni's own CPU (cores), mean | 0 | 0.05088 | 0.01295 |
| CPU used with Omni's own (cores), mean | 2.126 | 2.159 | 2.114 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 328.7 | 331.1 | 331.9 |
| HPA replicas, mean | 14.79 | 15.2 | 14.86 |
| pods started | 5.6 | 6 | 5.3 |
| pod start wait, total (s) | 9 | 9.6 | 7.9 |
| pod start wait, mean (s) | 1.642 | 1.607 | 1.474 |
| host CPU busy, the real machine under kind (%) | 61.16 | 62.4 | 61.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |
| second app: response time (ms), 95th percentile | 328 | 357.4 | 390.9 |
| second app: response time (ms), 99th percentile | 2386 | 2688 | 2436 |
| second app: time over the response line (% of samples) | 11.97 | 11.71 | 12.5 |
| second app: failed requests (%) | 8.965 | 9.151 | 8.988 |

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
| node-hours | 1.509 | 1.516 | +0.5% | +0.0018 to +0.0122 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 169.9 | 170.5 | +0.3% | +0.0398 to +1.1238 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.9 | 170.5 | +0.3% | +0.0398 to +1.1238 | yes: power given |
| response time (ms), mean | 401.4 | 416.3 | +3.7% | −38.9768 to +68.7497 | no |
| response time (ms), 95th percentile | 1657 | 1824 | +10.1% | −103.0297 to +437.7057 | no |
| response time (ms), 99th percentile | 4256 | 4721 | +10.9% | −272.6664 to +1202.0360 | no |
| time over the response line (% of samples) | 17.34 | 18.79 | +8.3% | +0.1108 to +2.7806 | yes: LOSS |
| failed requests (%) | 2.099 | 1.104 | −47.4% | −2.3613 to +0.3718 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.9 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 137 | +137.000 (native is 0) | +109.9021 to +164.0979 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.487 | 1.417 | −4.7% | −0.9549 to +0.8149 | no |
| utilisation (used / allocatable) | 0.08859 | 0.08783 | −0.9% | −0.0024 to +0.0009 | no |
| CPU used (cores), mean | 2.126 | 2.108 | −0.9% | −0.0576 to +0.0212 | no |
| Omni's own CPU (cores), mean | 0 | 0.05088 | +0.051 (native is 0) | +0.0429 to +0.0589 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.126 | 2.159 | +1.5% | −0.0055 to +0.0710 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 328.7 | 331.1 | +0.7% | −2.5864 to +7.2757 | no |
| HPA replicas, mean | 14.79 | 15.2 | +2.8% | −0.1212 to +0.9377 | no |
| pods started | 5.6 | 6 | +7.1% | −0.6228 to +1.4228 | no |
| pod start wait, total (s) | 9 | 9.6 | +6.7% | −2.2050 to +3.4050 | no |
| pod start wait, mean (s) | 1.642 | 1.607 | −2.1% | −0.3063 to +0.2358 | no |
| host CPU busy, the real machine under kind (%) | 61.16 | 62.4 | +2.0% | +0.5039 to +1.9864 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 328 | 357.4 | +9.0% | −27.5478 to +86.4908 | no |
| second app: response time (ms), 99th percentile | 2386 | 2688 | +12.7% | −810.6334 to +1415.9170 | no |
| second app: time over the response line (% of samples) | 11.97 | 11.71 | −2.2% | −0.9873 to +0.4715 | no |
| second app: failed requests (%) | 8.965 | 9.151 | +2.1% | −0.4494 to +0.8200 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.517 | +0.5% | +0.0029 to +0.0134 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 169.9 | 170.7 | +0.4% | −0.0760 to +1.5695 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.9 | 170.7 | +0.4% | −0.0760 to +1.5695 | no |
| response time (ms), mean | 401.4 | 351.4 | −12.4% | −115.8935 to +15.9609 | no |
| response time (ms), 95th percentile | 1657 | 1643 | −0.8% | −624.5688 to +597.6118 | no |
| response time (ms), 99th percentile | 4256 | 3844 | −9.7% | −1025.2015 to +201.5223 | no |
| time over the response line (% of samples) | 17.34 | 16.79 | −3.2% | −1.8762 to +0.7775 | no |
| failed requests (%) | 2.099 | 1.843 | −12.2% | −1.2167 to +0.7050 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7 | +1.4% | −0.6872 to +0.8872 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.4 | +53.400 (native is 0) | +42.6033 to +64.1967 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.487 | 1.513 | +1.8% | −0.6316 to +0.6849 | no |
| utilisation (used / allocatable) | 0.08859 | 0.08754 | −1.2% | −0.0028 to +0.0007 | no |
| CPU used (cores), mean | 2.126 | 2.101 | −1.2% | −0.0671 to +0.0169 | no |
| Omni's own CPU (cores), mean | 0 | 0.01295 | +0.013 (native is 0) | +0.0116 to +0.0143 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.126 | 2.114 | −0.6% | −0.0537 to +0.0294 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 328.7 | 331.9 | +1.0% | −4.7855 to +11.1041 | no |
| HPA replicas, mean | 14.79 | 14.86 | +0.5% | −0.2076 to +0.3499 | no |
| pods started | 5.6 | 5.3 | −5.4% | −1.4209 to +0.8209 | no |
| pod start wait, total (s) | 9 | 7.9 | −12.2% | −3.1909 to +0.9909 | no |
| pod start wait, mean (s) | 1.642 | 1.474 | −10.3% | −0.3872 to +0.0500 | no |
| host CPU busy, the real machine under kind (%) | 61.16 | 61.06 | −0.2% | −0.9713 to +0.7731 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 328 | 390.9 | +19.2% | −17.3745 to +143.2125 | no |
| second app: response time (ms), 99th percentile | 2386 | 2436 | +2.1% | −1131.0038 to +1231.9906 | no |
| second app: time over the response line (% of samples) | 11.97 | 12.5 | +4.4% | −0.8592 to +1.9204 | no |
| second app: failed requests (%) | 8.965 | 8.988 | +0.2% | −0.4244 to +0.4690 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.516 | 1.518 | +0.1% | −0.0063 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 170.5 | 170.7 | +0.1% | −0.7979 to +1.1277 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.5 | 170.7 | +0.1% | −0.7979 to +1.1277 | no |
| response time (ms), mean | 416.3 | 351.4 | −15.6% | −121.1346 to −8.5709 | yes: GAIN |
| response time (ms), 95th percentile | 1824 | 1643 | −9.9% | −683.4600 to +321.8270 | no |
| response time (ms), 99th percentile | 4721 | 3844 | −18.6% | −1779.5896 to +26.5408 | no |
| time over the response line (% of samples) | 18.79 | 16.79 | −10.6% | −3.2935 to −0.6965 | yes: GAIN |
| failed requests (%) | 1.104 | 1.843 | +66.9% | −0.2439 to +1.7216 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7 | +1.4% | −0.6872 to +0.8872 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 137 | 53.4 | −61.0% | −108.8183 to −58.3817 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.417 | 1.513 | +6.8% | −0.8033 to +0.9966 | no |
| utilisation (used / allocatable) | 0.08783 | 0.08754 | −0.3% | −0.0021 to +0.0015 | no |
| CPU used (cores), mean | 2.108 | 2.101 | −0.3% | −0.0495 to +0.0356 | no |
| Omni's own CPU (cores), mean | 0.05088 | 0.01295 | −74.5% | −0.0449 to −0.0310 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.159 | 2.114 | −2.1% | −0.0876 to −0.0021 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 331.1 | 331.9 | +0.2% | −6.3864 to +8.0158 | no |
| HPA replicas, mean | 15.2 | 14.86 | −2.2% | −0.6572 to −0.0171 | yes: GAIN |
| pods started | 6 | 5.3 | −11.7% | −1.7690 to +0.3690 | no |
| pod start wait, total (s) | 9.6 | 7.9 | −17.7% | −5.2051 to +1.8051 | no |
| pod start wait, mean (s) | 1.607 | 1.474 | −8.3% | −0.5227 to +0.2560 | no |
| host CPU busy, the real machine under kind (%) | 62.4 | 61.06 | −2.2% | −2.3082 to −0.3802 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 357.4 | 390.9 | +9.4% | −60.7137 to +127.6087 | no |
| second app: response time (ms), 99th percentile | 2688 | 2436 | −9.4% | −1779.3212 to +1275.0244 | no |
| second app: time over the response line (% of samples) | 11.71 | 12.5 | +6.7% | −0.5238 to +2.1008 | no |
| second app: failed requests (%) | 9.151 | 8.988 | −1.8% | −0.8098 to +0.4837 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*