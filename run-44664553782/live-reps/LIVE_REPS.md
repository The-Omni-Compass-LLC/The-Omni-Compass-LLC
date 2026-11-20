# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.515 | 1.513 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.6 | 157.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.6 | 157.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 124.4 | 69.48 | 71.3 |
| response time (ms), 95th percentile | 275.4 | 100.2 | 98.89 |
| response time (ms), 99th percentile | 441.1 | 136.4 | 126.9 |
| time over the response line (% of samples) | 1.119 | 0.02403 | 0.2525 |
| failed requests (%) | 0 | 0 | 0.04908 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | 29.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.3483 | 0.1867 |
| utilisation (used / allocatable) | 0.03366 | 0.03268 | 0.03324 |
| CPU used (cores), mean | 0.8078 | 0.7842 | 0.7978 |
| Omni's own CPU (cores), mean | 0 | 0.0333 | 0.03398 |
| CPU used with Omni's own (cores), mean | 0.8078 | 0.8175 | 0.8317 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 832.1 | 847.7 | 839.2 |
| HPA replicas, mean | 8.074 | 8.182 | 8.973 |
| pods started | 5.8 | 5 | 10.8 |
| pod start wait, total (s) | 8.1 | 7.8 | 18.7 |
| pod start wait, mean (s) | 1.412 | 1.592 | 1.748 |
| host CPU busy, the real machine under kind (%) | 25.1 | 25.52 | 26.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| node-hours | 1.515 | 1.513 | −0.1% | −0.0067 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.6 | −0.3% | −1.0192 to +0.1211 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.6 | −0.3% | −1.0192 to +0.1211 | no |
| response time (ms), mean | 124.4 | 69.48 | −44.1% | −76.1070 to −33.7028 | yes: GAIN |
| response time (ms), 95th percentile | 275.4 | 100.2 | −63.6% | −234.7622 to −115.6018 | yes: GAIN |
| response time (ms), 99th percentile | 441.1 | 136.4 | −69.1% | −407.8214 to −201.7318 | yes: GAIN |
| time over the response line (% of samples) | 1.119 | 0.02403 | −97.9% | −2.1542 to −0.0351 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | −100.0% | −2.0663 to +0.0663 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.500 (native is 0) | +17.7398 to +21.2602 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.3483 | +117.7% | −0.1062 to +0.4829 | no |
| utilisation (used / allocatable) | 0.03366 | 0.03268 | −2.9% | −0.0019 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8078 | 0.7842 | −2.9% | −0.0462 to −0.0009 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0333 | +0.033 (native is 0) | +0.0280 to +0.0386 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8078 | 0.8175 | +1.2% | −0.0092 to +0.0287 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 832.1 | 847.7 | +1.9% | −5.2880 to +36.4473 | no |
| HPA replicas, mean | 8.074 | 8.182 | +1.3% | −0.2592 to +0.4761 | no |
| pods started | 5.8 | 5 | −13.8% | −1.6793 to +0.0793 | no |
| pod start wait, total (s) | 8.1 | 7.8 | −3.7% | −2.5882 to +1.9882 | no |
| pod start wait, mean (s) | 1.412 | 1.592 | +12.7% | −0.0426 to +0.4021 | no |
| host CPU busy, the real machine under kind (%) | 25.1 | 25.52 | +1.7% | +0.0097 to +0.8387 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | 0.0% | raw −0.0079 to +0.0079 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.9 | −0.1% | −0.8891 to +0.6885 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.9 | −0.1% | −0.8891 to +0.6885 | no |
| response time (ms), mean | 124.4 | 71.3 | −42.7% | −74.0417 to −32.1320 | yes: GAIN |
| response time (ms), 95th percentile | 275.4 | 98.89 | −64.1% | −235.3323 to −117.7427 | yes: GAIN |
| response time (ms), 99th percentile | 441.1 | 126.9 | −71.2% | −421.3131 to −207.1041 | yes: GAIN |
| time over the response line (% of samples) | 1.119 | 0.2525 | −77.4% | −1.9448 to +0.2124 | no |
| failed requests (%) | 0 | 0.04908 | +0.049 (native is 0) | −0.0123 to +0.1104 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0.5 | −50.0% | −1.7274 to +0.7274 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 | +29.400 (native is 0) | +23.5869 to +35.2131 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.1867 | +16.7% | −0.2498 to +0.3031 | no |
| utilisation (used / allocatable) | 0.03366 | 0.03324 | −1.2% | −0.0009 to +0.0001 | no |
| CPU used (cores), mean | 0.8078 | 0.7978 | −1.2% | −0.0222 to +0.0022 | no |
| Omni's own CPU (cores), mean | 0 | 0.03398 | +0.034 (native is 0) | +0.0291 to +0.0389 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8078 | 0.8317 | +3.0% | +0.0128 to +0.0351 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 832.1 | 839.2 | +0.9% | −4.7903 to +19.0278 | no |
| HPA replicas, mean | 8.074 | 8.973 | +11.1% | +0.8405 to +0.9571 | yes: power given |
| pods started | 5.8 | 10.8 | +86.2% | +3.6512 to +6.3488 | yes: power given |
| pod start wait, total (s) | 8.1 | 18.7 | +130.9% | +7.6373 to +13.5627 | yes: LOSS |
| pod start wait, mean (s) | 1.412 | 1.748 | +23.8% | +0.0496 to +0.6218 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 25.1 | 26.06 | +3.8% | +0.5926 to +1.3355 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0038 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 157.9 | +0.2% | −0.2553 to +0.9528 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 157.9 | +0.2% | −0.2553 to +0.9528 | no |
| response time (ms), mean | 69.48 | 71.3 | +2.6% | +0.1554 to +3.4807 | yes: LOSS |
| response time (ms), 95th percentile | 100.2 | 98.89 | −1.4% | −4.2398 to +1.5288 | no |
| response time (ms), 99th percentile | 136.4 | 126.9 | −6.9% | −19.2027 to +0.3387 | no |
| time over the response line (% of samples) | 0.02403 | 0.2525 | +950.9% | +0.0807 to +0.3762 | yes: LOSS |
| failed requests (%) | 0 | 0.04908 | +0.049 (native is 0) | −0.0123 to +0.1104 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 19.5 | 29.4 | +50.8% | +2.8474 to +16.9526 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 42.5 | −46.9% | −80.7751 to +5.7751 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3483 | 0.1867 | −46.4% | −0.4471 to +0.1237 | no |
| utilisation (used / allocatable) | 0.03268 | 0.03324 | +1.7% | −0.0001 to +0.0012 | no |
| CPU used (cores), mean | 0.7842 | 0.7978 | +1.7% | −0.0020 to +0.0291 | no |
| Omni's own CPU (cores), mean | 0.0333 | 0.03398 | +2.0% | −0.0001 to +0.0014 | no |
| CPU used with Omni's own (cores), mean | 0.8175 | 0.8317 | +1.7% | −0.0010 to +0.0295 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.7 | 839.2 | −1.0% | −27.4985 to +10.5766 | no |
| HPA replicas, mean | 8.182 | 8.973 | +9.7% | +0.4407 to +1.1400 | yes: power given |
| pods started | 5 | 10.8 | +116.0% | +4.1899 to +7.4101 | yes: power given |
| pod start wait, total (s) | 7.8 | 18.7 | +139.7% | +7.9134 to +13.8866 | yes: LOSS |
| pod start wait, mean (s) | 1.592 | 1.748 | +9.8% | −0.0458 to +0.3576 | no |
| host CPU busy, the real machine under kind (%) | 25.52 | 26.06 | +2.1% | +0.0491 to +1.0306 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*