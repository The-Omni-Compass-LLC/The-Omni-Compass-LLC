# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 151.9 | 79.04 | 82.13 |
| response time (ms), 95th percentile | 342.6 | 116.6 | 113 |
| response time (ms), 99th percentile | 558.5 | 156.4 | 145.9 |
| time over the response line (% of samples) | 2.112 | 0 | 0.2548 |
| failed requests (%) | 0 | 0 | 0.06188 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | 27.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 42.86 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.2983 | 0.1317 |
| utilisation (used / allocatable) | 0.03831 | 0.03694 | 0.03718 |
| CPU used (cores), mean | 0.9194 | 0.8866 | 0.8923 |
| Omni's own CPU (cores), mean | 0 | 0.03595 | 0.03658 |
| CPU used with Omni's own (cores), mean | 0.9194 | 0.9225 | 0.9289 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.1 | 752.8 | 749.9 |
| HPA replicas, mean | 8.377 | 9.055 | 9.323 |
| pods started | 5 | 3.8 | 10.2 |
| pod start wait, total (s) | 8.2 | 5.7 | 17.7 |
| pod start wait, mean (s) | 1.63 | 1.438 | 1.746 |
| host CPU busy, the real machine under kind (%) | 27.94 | 28.5 | 28.7 |
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
| node-hours | 1.513 | 1.515 | +0.2% | +0.0003 to +0.0044 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.0% | −0.4876 to +0.3418 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.0% | −0.4876 to +0.3418 | no |
| response time (ms), mean | 151.9 | 79.04 | −48.0% | −96.6827 to −49.0696 | yes: GAIN |
| response time (ms), 95th percentile | 342.6 | 116.6 | −66.0% | −291.4729 to −160.4131 | yes: GAIN |
| response time (ms), 99th percentile | 558.5 | 156.4 | −72.0% | −528.0378 to −276.1118 | yes: GAIN |
| time over the response line (% of samples) | 2.112 | 0 | −100.0% | −3.4290 to −0.7956 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.2221 to −0.5779 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | +18.800 (native is 0) | +17.4597 to +20.1403 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.2983 | +37.7% | −0.2139 to +0.3772 | no |
| utilisation (used / allocatable) | 0.03831 | 0.03694 | −3.6% | −0.0026 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9194 | 0.8866 | −3.6% | −0.0632 to −0.0025 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03595 | +0.036 (native is 0) | +0.0309 to +0.0410 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9194 | 0.9225 | +0.3% | −0.0248 to +0.0310 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.1 | 752.8 | +2.1% | −11.8752 to +43.3288 | no |
| HPA replicas, mean | 8.377 | 9.055 | +8.1% | +0.0892 to +1.2665 | yes: power given |
| pods started | 5 | 3.8 | −24.0% | −2.8101 to +0.4101 | no |
| pod start wait, total (s) | 8.2 | 5.7 | −30.5% | −5.1174 to +0.1174 | no |
| pod start wait, mean (s) | 1.63 | 1.438 | −11.8% | −0.6137 to +0.2304 | no |
| host CPU busy, the real machine under kind (%) | 27.94 | 28.5 | +2.0% | −0.1444 to +1.2694 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0076 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.0% | −1.0868 to +0.9813 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.0% | −1.0868 to +0.9813 | no |
| response time (ms), mean | 151.9 | 82.13 | −45.9% | −93.1748 to −46.4002 | yes: GAIN |
| response time (ms), 95th percentile | 342.6 | 113 | −67.0% | −297.1128 to −162.1292 | yes: GAIN |
| response time (ms), 99th percentile | 558.5 | 145.9 | −73.9% | −548.0528 to −277.1684 | yes: GAIN |
| time over the response line (% of samples) | 2.112 | 0.2548 | −87.9% | −3.1544 to −0.5605 | yes: GAIN |
| failed requests (%) | 0 | 0.06188 | +0.062 (native is 0) | −0.0008 to +0.1246 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0.4 | −83.3% | −4.0232 to +0.0232 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.6 | +27.600 (native is 0) | +22.4617 to +32.7383 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.1317 | −39.2% | −0.2703 to +0.1003 | no |
| utilisation (used / allocatable) | 0.03831 | 0.03718 | −2.9% | −0.0019 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9194 | 0.8923 | −2.9% | −0.0447 to −0.0096 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03658 | +0.037 (native is 0) | +0.0316 to +0.0416 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9194 | 0.9289 | +1.0% | −0.0040 to +0.0229 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.1 | 749.9 | +1.7% | −7.1373 to +32.8263 | no |
| HPA replicas, mean | 8.377 | 9.323 | +11.3% | +0.6803 to +1.2122 | yes: power given |
| pods started | 5 | 10.2 | +104.0% | +3.6996 to +6.7004 | yes: power given |
| pod start wait, total (s) | 8.2 | 17.7 | +115.9% | +6.1576 to +12.8424 | yes: LOSS |
| pod start wait, mean (s) | 1.63 | 1.746 | +7.1% | −0.1695 to +0.4015 | no |
| host CPU busy, the real machine under kind (%) | 27.94 | 28.7 | +2.7% | +0.4686 to +1.0579 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | −0.0% | −0.0087 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.8 | +0.0% | −0.9381 to +0.9784 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.8 | +0.0% | −0.9381 to +0.9784 | no |
| response time (ms), mean | 79.04 | 82.13 | +3.9% | +0.7187 to +5.4585 | yes: LOSS |
| response time (ms), 95th percentile | 116.6 | 113 | −3.2% | −11.5841 to +4.2281 | no |
| response time (ms), 99th percentile | 156.4 | 145.9 | −6.7% | −29.2156 to +8.1440 | no |
| time over the response line (% of samples) | 0 | 0.2548 | +0.255 (native is 0) | +0.1446 to +0.3650 | yes: LOSS |
| failed requests (%) | 0 | 0.06188 | +0.062 (native is 0) | −0.0008 to +0.1246 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 18.8 | 27.6 | +46.8% | +3.4175 to +14.1825 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 42.86 | −57.1% | −106.5797 to −7.7060 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.1317 | −55.9% | −0.3971 to +0.0638 | no |
| utilisation (used / allocatable) | 0.03694 | 0.03718 | +0.6% | −0.0008 to +0.0012 | no |
| CPU used (cores), mean | 0.8866 | 0.8923 | +0.6% | −0.0181 to +0.0296 | no |
| Omni's own CPU (cores), mean | 0.03595 | 0.03658 | +1.8% | +0.0001 to +0.0012 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9225 | 0.9289 | +0.7% | −0.0179 to +0.0307 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.8 | 749.9 | −0.4% | −17.0858 to +11.3211 | no |
| HPA replicas, mean | 9.055 | 9.323 | +3.0% | −0.3789 to +0.9156 | no |
| pods started | 3.8 | 10.2 | +168.4% | +5.0854 to +7.7146 | yes: power given |
| pod start wait, total (s) | 5.7 | 17.7 | +210.5% | +8.0102 to +15.9898 | yes: LOSS |
| pod start wait, mean (s) | 1.438 | 1.746 | +21.4% | −0.1826 to +0.7978 | no |
| host CPU busy, the real machine under kind (%) | 28.5 | 28.7 | +0.7% | −0.4259 to +0.8274 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*