# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.509 | 1.509 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159 | 160.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159 | 160.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 181.1 | 89.42 | 92.44 |
| response time (ms), 95th percentile | 412.5 | 135.1 | 134.5 |
| response time (ms), 99th percentile | 694.5 | 190.9 | 180.3 |
| time over the response line (% of samples) | 3.037 | 0.01212 | 0.2681 |
| failed requests (%) | 0 | 0 | 0.1113 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 | 23.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.2433 | 0 |
| utilisation (used / allocatable) | 0.04309 | 0.04086 | 0.04192 |
| CPU used (cores), mean | 1.034 | 0.9807 | 1.006 |
| Omni's own CPU (cores), mean | 0 | 0.03932 | 0.04029 |
| CPU used with Omni's own (cores), mean | 1.034 | 1.02 | 1.046 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 621.3 | 650.6 | 636 |
| HPA replicas, mean | 8.922 | 9.405 | 9.719 |
| pods started | 4.9 | 3.2 | 9.4 |
| pod start wait, total (s) | 7.9 | 4.2 | 18.1 |
| pod start wait, mean (s) | 1.61 | 1.342 | 1.946 |
| host CPU busy, the real machine under kind (%) | 31.45 | 31.24 | 32.29 |
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
| node-hours | 1.509 | 1.509 | +0.0% | −0.0013 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159 | −0.3% | −0.7167 to −0.2515 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159 | −0.3% | −0.7167 to −0.2515 | yes: GAIN |
| response time (ms), mean | 181.1 | 89.42 | −50.6% | −108.1271 to −75.2392 | yes: GAIN |
| response time (ms), 95th percentile | 412.5 | 135.1 | −67.3% | −325.0818 to −229.6982 | yes: GAIN |
| response time (ms), 99th percentile | 694.5 | 190.9 | −72.5% | −620.1230 to −387.1778 | yes: GAIN |
| time over the response line (% of samples) | 3.037 | 0.01212 | −99.6% | −4.3383 to −1.7124 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0 | −100.0% | −4.4676 to −1.7324 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.9 | +18.900 (native is 0) | +17.4516 to +20.3484 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.2433 | −17.5% | −0.3170 to +0.2136 | no |
| utilisation (used / allocatable) | 0.04309 | 0.04086 | −5.2% | −0.0030 to −0.0014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.034 | 0.9807 | −5.2% | −0.0730 to −0.0338 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03932 | +0.039 (native is 0) | +0.0354 to +0.0432 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.034 | 1.02 | −1.4% | −0.0306 to +0.0025 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 621.3 | 650.6 | +4.7% | +20.7723 to +37.7226 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.922 | 9.405 | +5.4% | +0.0581 to +0.9076 | yes: power given |
| pods started | 4.9 | 3.2 | −34.7% | −3.0924 to −0.3076 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 4.2 | −46.8% | −5.9882 to −1.4118 | yes: GAIN |
| pod start wait, mean (s) | 1.61 | 1.342 | −16.7% | −0.8467 to +0.3101 | no |
| host CPU busy, the real machine under kind (%) | 31.45 | 31.24 | −0.7% | −0.6654 to +0.2538 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.516 | +0.5% | +0.0060 to +0.0090 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 160.1 | +0.3% | +0.3419 to +0.7133 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 160.1 | +0.3% | +0.3419 to +0.7133 | yes: power given |
| response time (ms), mean | 181.1 | 92.44 | −49.0% | −105.9018 to −71.4254 | yes: GAIN |
| response time (ms), 95th percentile | 412.5 | 134.5 | −67.4% | −326.4862 to −229.3928 | yes: GAIN |
| response time (ms), 99th percentile | 694.5 | 180.3 | −74.0% | −633.6465 to −394.8581 | yes: GAIN |
| time over the response line (% of samples) | 3.037 | 0.2681 | −91.2% | −4.1329 to −1.4059 | yes: GAIN |
| failed requests (%) | 0 | 0.1113 | +0.111 (native is 0) | +0.0458 to +0.1769 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0.3 | −90.3% | −4.4792 to −1.1208 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.3 | +23.300 (native is 0) | +19.9781 to +26.6219 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0 | −100.0% | −0.5255 to −0.0645 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04309 | 0.04192 | −2.7% | −0.0018 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.034 | 1.006 | −2.7% | −0.0422 to −0.0140 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04029 | +0.040 (native is 0) | +0.0366 to +0.0440 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.034 | 1.046 | +1.2% | +0.0005 to +0.0239 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 621.3 | 636 | +2.4% | +7.5734 to +21.8079 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.922 | 9.719 | +8.9% | +0.6557 to +0.9388 | yes: power given |
| pods started | 4.9 | 9.4 | +91.8% | +3.8048 to +5.1952 | yes: power given |
| pod start wait, total (s) | 7.9 | 18.1 | +129.1% | +7.0584 to +13.3416 | yes: LOSS |
| pod start wait, mean (s) | 1.61 | 1.946 | +20.9% | −0.1011 to +0.7728 | no |
| host CPU busy, the real machine under kind (%) | 31.45 | 32.29 | +2.7% | +0.6281 to +1.0561 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.509 | 1.516 | +0.5% | +0.0055 to +0.0089 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160.1 | +0.6% | +0.7991 to +1.2242 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160.1 | +0.6% | +0.7991 to +1.2242 | yes: power given |
| response time (ms), mean | 89.42 | 92.44 | +3.4% | +1.1504 to +4.8887 | yes: LOSS |
| response time (ms), 95th percentile | 135.1 | 134.5 | −0.4% | −2.4968 to +1.3978 | no |
| response time (ms), 99th percentile | 190.9 | 180.3 | −5.6% | −19.9856 to −1.2182 | yes: GAIN |
| time over the response line (% of samples) | 0.01212 | 0.2681 | +2111.7% | +0.1948 to +0.3172 | yes: LOSS |
| failed requests (%) | 0 | 0.1113 | +0.111 (native is 0) | +0.0458 to +0.1769 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.9 | 23.3 | +23.3% | +0.9911 to +7.8089 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 40 | −60.0% | −127.9978 to +7.9978 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2433 | 0 | −100.0% | −0.3831 to −0.1036 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04086 | 0.04192 | +2.6% | +0.0006 to +0.0015 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9807 | 1.006 | +2.6% | +0.0137 to +0.0370 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03932 | 0.04029 | +2.5% | +0.0003 to +0.0017 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.02 | 1.046 | +2.6% | +0.0146 to +0.0380 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 650.6 | 636 | −2.2% | −20.3959 to −8.7179 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.405 | 9.719 | +3.3% | −0.0507 to +0.6795 | no |
| pods started | 3.2 | 9.4 | +193.8% | +5.3207 to +7.0793 | yes: power given |
| pod start wait, total (s) | 4.2 | 18.1 | +331.0% | +9.9611 to +17.8389 | yes: LOSS |
| pod start wait, mean (s) | 1.342 | 1.946 | +45.0% | +0.1427 to +1.0657 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 31.24 | 32.29 | +3.4% | +0.5476 to +1.5482 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*