# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.512 | 1.514 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.8 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.8 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 160.1 | 81.22 | 81.72 |
| response time (ms), 95th percentile | 367.3 | 123.1 | 122 |
| response time (ms), 99th percentile | 601.6 | 170.2 | 156.8 |
| time over the response line (% of samples) | 2.662 | 0.01205 | 0.2321 |
| failed requests (%) | 0 | 0 | 0.1362 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | 28 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | 71.43 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.19 | 0.05167 |
| utilisation (used / allocatable) | 0.03977 | 0.03732 | 0.03865 |
| CPU used (cores), mean | 0.9545 | 0.8956 | 0.9277 |
| Omni's own CPU (cores), mean | 0 | 0.03851 | 0.03945 |
| CPU used with Omni's own (cores), mean | 0.9545 | 0.9341 | 0.9671 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 715.3 | 753.8 | 730.4 |
| HPA replicas, mean | 8.593 | 9.016 | 9.301 |
| pods started | 4.8 | 3.8 | 10.6 |
| pod start wait, total (s) | 7.3 | 5.1 | 19.3 |
| pod start wait, mean (s) | 1.375 | 1.374 | 1.87 |
| host CPU busy, the real machine under kind (%) | 29.07 | 29.14 | 30.01 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.514 | +0.1% | −0.0001 to +0.0034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.8 | −0.2% | −0.6149 to −0.1637 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.8 | −0.2% | −0.6149 to −0.1637 | yes: GAIN |
| response time (ms), mean | 160.1 | 81.22 | −49.3% | −105.4553 to −52.2498 | yes: GAIN |
| response time (ms), 95th percentile | 367.3 | 123.1 | −66.5% | −312.5062 to −175.8188 | yes: GAIN |
| response time (ms), 99th percentile | 601.6 | 170.2 | −71.7% | −557.4766 to −305.2340 | yes: GAIN |
| time over the response line (% of samples) | 2.662 | 0.01205 | −99.5% | −3.9700 to −1.3307 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 | −100.0% | −3.8593 to −1.1407 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | +19.700 (native is 0) | +18.4361 to +20.9639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.19 | −10.9% | −0.3699 to +0.3233 | no |
| utilisation (used / allocatable) | 0.03977 | 0.03732 | −6.2% | −0.0033 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9545 | 0.8956 | −6.2% | −0.0803 to −0.0375 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03851 | +0.039 (native is 0) | +0.0334 to +0.0436 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9545 | 0.9341 | −2.1% | −0.0375 to −0.0033 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 715.3 | 753.8 | +5.4% | +30.9874 to +46.1617 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.593 | 9.016 | +4.9% | +0.0265 to +0.8195 | yes: power given |
| pods started | 4.8 | 3.8 | −20.8% | −2.2158 to +0.2158 | no |
| pod start wait, total (s) | 7.3 | 5.1 | −30.1% | −5.0172 to +0.6172 | no |
| pod start wait, mean (s) | 1.375 | 1.374 | −0.1% | −0.5812 to +0.5783 | no |
| host CPU busy, the real machine under kind (%) | 29.07 | 29.14 | +0.3% | −0.2946 to +0.4527 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | +0.0% | −0.0099 to +0.0102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.9 | −0.1% | −1.1583 to +0.7341 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.9 | −0.1% | −1.1583 to +0.7341 | no |
| response time (ms), mean | 160.1 | 81.72 | −49.0% | −105.6055 to −51.1144 | yes: GAIN |
| response time (ms), 95th percentile | 367.3 | 122 | −66.8% | −314.3822 to −176.2998 | yes: GAIN |
| response time (ms), 99th percentile | 601.6 | 156.8 | −73.9% | −576.2329 to −313.2913 | yes: GAIN |
| time over the response line (% of samples) | 2.662 | 0.2321 | −91.3% | −3.7271 to −1.1335 | yes: GAIN |
| failed requests (%) | 0 | 0.1362 | +0.136 (native is 0) | +0.0582 to +0.2142 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0.3 | −88.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28 | +28.000 (native is 0) | +19.0913 to +36.9087 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.05167 | −75.8% | −0.3723 to +0.0489 | no |
| utilisation (used / allocatable) | 0.03977 | 0.03865 | −2.8% | −0.0019 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9545 | 0.9277 | −2.8% | −0.0446 to −0.0090 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03945 | +0.039 (native is 0) | +0.0346 to +0.0443 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9545 | 0.9671 | +1.3% | −0.0028 to +0.0280 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 715.3 | 730.4 | +2.1% | +2.0628 to +28.2449 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.593 | 9.301 | +8.2% | +0.4110 to +1.0053 | yes: power given |
| pods started | 4.8 | 10.6 | +120.8% | +4.1899 to +7.4101 | yes: power given |
| pod start wait, total (s) | 7.3 | 19.3 | +164.4% | +8.6961 to +15.3039 | yes: LOSS |
| pod start wait, mean (s) | 1.375 | 1.87 | +36.0% | −0.0434 to +1.0327 | no |
| host CPU busy, the real machine under kind (%) | 29.07 | 30.01 | +3.3% | +0.5252 to +1.3674 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0103 to +0.0073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.9 | +0.1% | −0.7770 to +1.1314 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.9 | +0.1% | −0.7770 to +1.1314 | no |
| response time (ms), mean | 81.22 | 81.72 | +0.6% | −0.5186 to +1.5038 | no |
| response time (ms), 95th percentile | 123.1 | 122 | −1.0% | −3.6094 to +1.2524 | no |
| response time (ms), 99th percentile | 170.2 | 156.8 | −7.9% | −24.5679 to −2.2457 | yes: GAIN |
| time over the response line (% of samples) | 0.01205 | 0.2321 | +1826.2% | +0.1293 to +0.3107 | yes: LOSS |
| failed requests (%) | 0 | 0.1362 | +0.136 (native is 0) | +0.0582 to +0.2142 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.7 | 28 | +42.1% | −0.3105 to +16.9105 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 75.71 | −15.9% | −78.1084 to +49.5370 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.05167 | −72.8% | −0.3463 to +0.0696 | no |
| utilisation (used / allocatable) | 0.03732 | 0.03865 | +3.6% | +0.0008 to +0.0019 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8956 | 0.9277 | +3.6% | +0.0189 to +0.0452 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03851 | 0.03945 | +2.4% | +0.0003 to +0.0016 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9341 | 0.9671 | +3.5% | +0.0199 to +0.0462 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 753.8 | 730.4 | −3.1% | −34.6372 to −12.2042 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.016 | 9.301 | +3.2% | −0.1953 to +0.7656 | no |
| pods started | 3.8 | 10.6 | +178.9% | +5.4179 to +8.1821 | yes: power given |
| pod start wait, total (s) | 5.1 | 19.3 | +278.4% | +12.1824 to +16.2176 | yes: LOSS |
| pod start wait, mean (s) | 1.374 | 1.87 | +36.1% | +0.2922 to +0.6999 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 29.14 | 30.01 | +3.0% | +0.5111 to +1.2235 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*