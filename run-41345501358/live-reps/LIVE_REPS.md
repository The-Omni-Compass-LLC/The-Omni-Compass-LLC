# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.513 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.3 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.3 | 158.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 145.6 | 76.35 | 77.61 |
| response time (ms), 95th percentile | 329.5 | 115.5 | 114.8 |
| response time (ms), 99th percentile | 545.9 | 163.3 | 154.8 |
| time over the response line (% of samples) | 2.178 | 0 | 0.1944 |
| failed requests (%) | 0 | 0 | 0.1113 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | 18.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.1667 | 0.6433 |
| utilisation (used / allocatable) | 0.03741 | 0.03561 | 0.03618 |
| CPU used (cores), mean | 0.8978 | 0.8545 | 0.8682 |
| Omni's own CPU (cores), mean | 0 | 0.00894 | 0.009 |
| CPU used with Omni's own (cores), mean | 0.8978 | 0.8635 | 0.8772 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 769.5 | 794.6 | 787.2 |
| HPA replicas, mean | 8.164 | 7.815 | 9.517 |
| pods started | 5.3 | 4 | 9 |
| pod start wait, total (s) | 8 | 6.1 | 17.7 |
| pod start wait, mean (s) | 1.507 | 1.549 | 1.967 |
| host CPU busy, the real machine under kind (%) | 27.5 | 26.6 | 27.28 |
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
| node-hours | 1.513 | 1.513 | +0.0% | −0.0011 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.3 | −0.2% | −0.7011 to −0.0861 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.3 | −0.2% | −0.7011 to −0.0861 | yes: GAIN |
| response time (ms), mean | 145.6 | 76.35 | −47.6% | −95.8142 to −42.6453 | yes: GAIN |
| response time (ms), 95th percentile | 329.5 | 115.5 | −64.9% | −291.3308 to −136.5242 | yes: GAIN |
| response time (ms), 99th percentile | 545.9 | 163.3 | −70.1% | −510.5318 to −254.6316 | yes: GAIN |
| time over the response line (% of samples) | 2.178 | 0 | −100.0% | −3.5523 to −0.8034 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.7004 to −0.6996 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.400 (native is 0) | +13.9087 to +20.8913 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.1667 | −43.2% | −0.3811 to +0.1277 | no |
| utilisation (used / allocatable) | 0.03741 | 0.03561 | −4.8% | −0.0029 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8978 | 0.8545 | −4.8% | −0.0698 to −0.0169 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00894 | +0.009 (native is 0) | +0.0075 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8978 | 0.8635 | −3.8% | −0.0597 to −0.0091 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 769.5 | 794.6 | +3.3% | +4.1363 to +45.9655 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.164 | 7.815 | −4.3% | −0.8963 to +0.1986 | no |
| pods started | 5.3 | 4 | −24.5% | −2.3690 to −0.2310 | yes: GAIN |
| pod start wait, total (s) | 8 | 6.1 | −23.8% | −3.1818 to −0.6182 | yes: GAIN |
| pod start wait, mean (s) | 1.507 | 1.549 | +2.8% | −0.3428 to +0.4275 | no |
| host CPU busy, the real machine under kind (%) | 27.5 | 26.6 | −3.3% | −1.4692 to −0.3306 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0058 to +0.0094 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.6 | −0.1% | −0.7283 to +0.5584 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.6 | −0.1% | −0.7283 to +0.5584 | no |
| response time (ms), mean | 145.6 | 77.61 | −46.7% | −94.6484 to −41.2875 | yes: GAIN |
| response time (ms), 95th percentile | 329.5 | 114.8 | −65.2% | −291.8694 to −137.4396 | yes: GAIN |
| response time (ms), 99th percentile | 545.9 | 154.8 | −71.6% | −522.1577 to −260.0543 | yes: GAIN |
| time over the response line (% of samples) | 2.178 | 0.1944 | −91.1% | −3.3233 to −0.6435 | yes: GAIN |
| failed requests (%) | 0 | 0.1113 | +0.111 (native is 0) | +0.0336 to +0.1889 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0.1 | −95.5% | −3.6977 to −0.5023 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +15.1099 to +21.6901 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.6433 | +119.3% | −0.1964 to +0.8964 | no |
| utilisation (used / allocatable) | 0.03741 | 0.03618 | −3.3% | −0.0021 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8978 | 0.8682 | −3.3% | −0.0514 to −0.0079 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.009 | +0.009 (native is 0) | +0.0080 to +0.0100 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8978 | 0.8772 | −2.3% | −0.0418 to +0.0005 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 769.5 | 787.2 | +2.3% | −6.3308 to +41.7170 | no |
| HPA replicas, mean | 8.164 | 9.517 | +16.6% | +0.9192 to +1.7874 | yes: power given |
| pods started | 5.3 | 9 | +69.8% | +3.3545 to +4.0455 | yes: power given |
| pod start wait, total (s) | 8 | 17.7 | +121.2% | +7.0653 to +12.3347 | yes: LOSS |
| pod start wait, mean (s) | 1.507 | 1.967 | +30.5% | +0.1165 to +0.8035 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 27.5 | 27.28 | −0.8% | −0.7273 to +0.2916 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0057 to +0.0090 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.6 | +0.2% | −0.5265 to +1.1438 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.6 | +0.2% | −0.5265 to +1.1438 | no |
| response time (ms), mean | 76.35 | 77.61 | +1.7% | −1.0901 to +3.6136 | no |
| response time (ms), 95th percentile | 115.5 | 114.8 | −0.6% | −2.4626 to +1.0086 | no |
| response time (ms), 99th percentile | 163.3 | 154.8 | −5.2% | −29.3406 to +12.2920 | no |
| time over the response line (% of samples) | 0 | 0.1944 | +0.194 (native is 0) | +0.1212 to +0.2676 | yes: LOSS |
| failed requests (%) | 0 | 0.1113 | +0.111 (native is 0) | +0.0336 to +0.1889 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.4 | 18.4 | +5.7% | −4.8502 to +6.8502 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1667 | 0.6433 | +286.0% | +0.1149 to +0.8384 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03561 | 0.03618 | +1.6% | +0.0001 to +0.0010 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8545 | 0.8682 | +1.6% | +0.0036 to +0.0238 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00894 | 0.009 | +0.7% | −0.0005 to +0.0006 | no |
| CPU used with Omni's own (cores), mean | 0.8635 | 0.8772 | +1.6% | +0.0040 to +0.0235 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 794.6 | 787.2 | −0.9% | −16.2484 to +1.5328 | no |
| HPA replicas, mean | 7.815 | 9.517 | +21.8% | +0.8035 to +2.6007 | yes: power given |
| pods started | 4 | 9 | +125.0% | +3.7383 to +6.2617 | yes: power given |
| pod start wait, total (s) | 6.1 | 17.7 | +190.2% | +8.2246 to +14.9754 | yes: LOSS |
| pod start wait, mean (s) | 1.549 | 1.967 | +27.0% | +0.0129 to +0.8224 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.6 | 27.28 | +2.6% | +0.3604 to +1.0037 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*