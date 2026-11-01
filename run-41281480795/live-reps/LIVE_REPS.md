# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.51 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.3 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.3 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 160 | 79.72 | 82.13 |
| response time (ms), 95th percentile | 364.4 | 118.7 | 118.2 |
| response time (ms), 99th percentile | 602.7 | 156.5 | 152.1 |
| time over the response line (% of samples) | 2.804 | 0.02424 | 0.2446 |
| failed requests (%) | 0 | 0 | 0.1114 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.7 | 17.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1283 | 0.32 | 0.5883 |
| utilisation (used / allocatable) | 0.03935 | 0.03725 | 0.0379 |
| CPU used (cores), mean | 0.9445 | 0.8941 | 0.9096 |
| Omni's own CPU (cores), mean | 0 | 0.00878 | 0.0088 |
| CPU used with Omni's own (cores), mean | 0.9445 | 0.9028 | 0.9184 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.4 | 756.4 | 741 |
| HPA replicas, mean | 8.489 | 7.967 | 9.536 |
| pods started | 5 | 3.1 | 9 |
| pod start wait, total (s) | 7.7 | 4.7 | 15 |
| pod start wait, mean (s) | 1.563 | 1.475 | 1.664 |
| host CPU busy, the real machine under kind (%) | 28.6 | 27.44 | 28.25 |
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
| node-hours | 1.51 | 1.51 | −0.0% | −0.0031 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.3 | −0.3% | −0.8301 to −0.2428 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.3 | −0.3% | −0.8301 to −0.2428 | yes: GAIN |
| response time (ms), mean | 160 | 79.72 | −50.2% | −107.6007 to −52.9155 | yes: GAIN |
| response time (ms), 95th percentile | 364.4 | 118.7 | −67.4% | −320.1954 to −171.2296 | yes: GAIN |
| response time (ms), 99th percentile | 602.7 | 156.5 | −74.0% | −592.4670 to −299.8754 | yes: GAIN |
| time over the response line (% of samples) | 2.804 | 0.02424 | −99.1% | −4.3227 to −1.2366 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.6011 to −1.1989 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.7 | +15.700 (native is 0) | +12.8778 to +18.5222 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1283 | 0.32 | +149.4% | −0.1372 to +0.5205 | no |
| utilisation (used / allocatable) | 0.03935 | 0.03725 | −5.3% | −0.0031 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9445 | 0.8941 | −5.3% | −0.0756 to −0.0252 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00878 | +0.009 (native is 0) | +0.0073 to +0.0103 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9445 | 0.9028 | −4.4% | −0.0657 to −0.0175 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.4 | 756.4 | +4.6% | +22.2368 to +43.8926 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.489 | 7.967 | −6.1% | −1.3017 to +0.2577 | no |
| pods started | 5 | 3.1 | −38.0% | −2.9900 to −0.8100 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 4.7 | −39.0% | −4.3488 to −1.6512 | yes: GAIN |
| pod start wait, mean (s) | 1.563 | 1.475 | −5.7% | −0.4362 to +0.2596 | no |
| host CPU busy, the real machine under kind (%) | 28.6 | 27.44 | −4.1% | −1.8056 to −0.5224 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.513 | +0.2% | −0.0041 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.0% | −0.6750 to +0.5660 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.0% | −0.6750 to +0.5660 | no |
| response time (ms), mean | 160 | 82.13 | −48.7% | −104.8576 to −50.8336 | yes: GAIN |
| response time (ms), 95th percentile | 364.4 | 118.2 | −67.6% | −321.7757 to −170.6003 | yes: GAIN |
| response time (ms), 99th percentile | 602.7 | 152.1 | −74.8% | −599.4226 to −301.7802 | yes: GAIN |
| time over the response line (% of samples) | 2.804 | 0.2446 | −91.3% | −4.0585 to −1.0602 | yes: GAIN |
| failed requests (%) | 0 | 0.1114 | +0.111 (native is 0) | +0.0336 to +0.1892 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0.3 | −89.7% | −4.2588 to −0.9412 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | +17.900 (native is 0) | +14.5884 to +21.2116 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1283 | 0.5883 | +358.4% | +0.2177 to +0.7023 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03935 | 0.0379 | −3.7% | −0.0024 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9445 | 0.9096 | −3.7% | −0.0581 to −0.0117 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0088 | +0.009 (native is 0) | +0.0077 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9445 | 0.9184 | −2.8% | −0.0486 to −0.0036 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.4 | 741 | +2.4% | −1.5303 to +36.7588 | no |
| HPA replicas, mean | 8.489 | 9.536 | +12.3% | +0.6547 to +1.4390 | yes: power given |
| pods started | 5 | 9 | +80.0% | +3.5231 to +4.4769 | yes: power given |
| pod start wait, total (s) | 7.7 | 15 | +94.8% | +5.0367 to +9.5633 | yes: LOSS |
| pod start wait, mean (s) | 1.563 | 1.664 | +6.5% | −0.2097 to +0.4119 | no |
| host CPU busy, the real machine under kind (%) | 28.6 | 28.25 | −1.2% | −0.8228 to +0.1190 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.514 | +0.2% | −0.0023 to +0.0096 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.8 | +0.3% | −0.1213 to +1.0853 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.8 | +0.3% | −0.1213 to +1.0853 | no |
| response time (ms), mean | 79.72 | 82.13 | +3.0% | +0.3258 to +4.4992 | yes: LOSS |
| response time (ms), 95th percentile | 118.7 | 118.2 | −0.4% | −2.7602 to +1.8092 | no |
| response time (ms), 99th percentile | 156.5 | 152.1 | −2.8% | −10.7502 to +1.8898 | no |
| time over the response line (% of samples) | 0.02424 | 0.2446 | +908.9% | +0.1064 to +0.3343 | yes: LOSS |
| failed requests (%) | 0 | 0.1114 | +0.111 (native is 0) | +0.0336 to +0.1892 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 15.7 | 17.9 | +14.0% | −3.6385 to +8.0385 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.5883 | +83.9% | −0.2448 to +0.7815 | no |
| utilisation (used / allocatable) | 0.03725 | 0.0379 | +1.7% | −0.0000 to +0.0013 | no |
| CPU used (cores), mean | 0.8941 | 0.9096 | +1.7% | −0.0005 to +0.0315 | no |
| Omni's own CPU (cores), mean | 0.00878 | 0.0088 | +0.2% | −0.0005 to +0.0005 | no |
| CPU used with Omni's own (cores), mean | 0.9028 | 0.9184 | +1.7% | −0.0006 to +0.0317 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 756.4 | 741 | −2.0% | −36.8944 to +5.9935 | no |
| HPA replicas, mean | 7.967 | 9.536 | +19.7% | +0.5246 to +2.6132 | yes: power given |
| pods started | 3.1 | 9 | +190.3% | +4.8100 to +6.9900 | yes: power given |
| pod start wait, total (s) | 4.7 | 15 | +219.1% | +7.6438 to +12.9562 | yes: LOSS |
| pod start wait, mean (s) | 1.475 | 1.664 | +12.8% | −0.2146 to +0.5935 | no |
| host CPU busy, the real machine under kind (%) | 27.44 | 28.25 | +3.0% | +0.3282 to +1.2960 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*