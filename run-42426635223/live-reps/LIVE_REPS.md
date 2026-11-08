# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.514 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 157.3 | 157.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 157.3 | 157.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 118.4 | 65.27 | 69.37 |
| response time (ms), 95th percentile | 260.8 | 95.11 | 95.43 |
| response time (ms), 99th percentile | 416.3 | 127.6 | 128 |
| time over the response line (% of samples) | 1.23 | 0.04848 | 0.2167 |
| failed requests (%) | 0 | 0 | 0.03711 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | 34.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.24 | 0.105 |
| utilisation (used / allocatable) | 0.03178 | 0.03082 | 0.03158 |
| CPU used (cores), mean | 0.7627 | 0.7397 | 0.7579 |
| Omni's own CPU (cores), mean | 0 | 0.0327 | 0.03402 |
| CPU used with Omni's own (cores), mean | 0.7627 | 0.7724 | 0.792 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 910.3 | 914.9 | 899.4 |
| HPA replicas, mean | 7.777 | 7.963 | 8.688 |
| pods started | 5.2 | 4.7 | 11.6 |
| pod start wait, total (s) | 7.6 | 6 | 18.3 |
| pod start wait, mean (s) | 1.47 | 1.295 | 1.592 |
| host CPU busy, the real machine under kind (%) | 23.68 | 24.24 | 24.85 |
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
| node-hours | 1.513 | 1.514 | +0.1% | −0.0007 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 157.3 | −0.1% | −0.5265 to +0.2723 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 157.3 | −0.1% | −0.5265 to +0.2723 | no |
| response time (ms), mean | 118.4 | 65.27 | −44.9% | −80.7426 to −25.5574 | yes: GAIN |
| response time (ms), 95th percentile | 260.8 | 95.11 | −63.5% | −240.3751 to −91.0649 | yes: GAIN |
| response time (ms), 99th percentile | 416.3 | 127.6 | −69.3% | −414.2839 to −163.0673 | yes: GAIN |
| time over the response line (% of samples) | 1.23 | 0.04848 | −96.1% | −2.3871 to +0.0250 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | −100.0% | −2.2158 to +0.2158 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | +19.100 (native is 0) | +16.7049 to +21.4951 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.24 | −8.9% | −0.3706 to +0.3240 | no |
| utilisation (used / allocatable) | 0.03178 | 0.03082 | −3.0% | −0.0024 to +0.0005 | no |
| CPU used (cores), mean | 0.7627 | 0.7397 | −3.0% | −0.0587 to +0.0125 | no |
| Omni's own CPU (cores), mean | 0 | 0.0327 | +0.033 (native is 0) | +0.0264 to +0.0390 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7627 | 0.7724 | +1.3% | −0.0211 to +0.0404 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 910.3 | 914.9 | +0.5% | −25.4399 to +34.5834 | no |
| HPA replicas, mean | 7.777 | 7.963 | +2.4% | −0.3070 to +0.6782 | no |
| pods started | 5.2 | 4.7 | −9.6% | −1.9405 to +0.9405 | no |
| pod start wait, total (s) | 7.6 | 6 | −21.1% | −4.0595 to +0.8595 | no |
| pod start wait, mean (s) | 1.47 | 1.295 | −11.9% | −0.4864 to +0.1355 | no |
| host CPU busy, the real machine under kind (%) | 23.68 | 24.24 | +2.4% | −0.0853 to +1.2175 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0024 to +0.0094 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 157.7 | +0.2% | −0.2018 to +0.7960 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 157.7 | +0.2% | −0.2018 to +0.7960 | no |
| response time (ms), mean | 118.4 | 69.37 | −41.4% | −73.8458 to −24.2474 | yes: GAIN |
| response time (ms), 95th percentile | 260.8 | 95.43 | −63.4% | −239.9064 to −90.9016 | yes: GAIN |
| response time (ms), 99th percentile | 416.3 | 128 | −69.3% | −418.9689 to −157.6053 | yes: GAIN |
| time over the response line (% of samples) | 1.23 | 0.2167 | −82.4% | −2.2441 to +0.2184 | no |
| failed requests (%) | 0 | 0.03711 | +0.037 (native is 0) | −0.0056 to +0.0799 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0.3 | −70.0% | −2.0924 to +0.6924 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.7 | +34.700 (native is 0) | +27.8802 to +41.5198 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.105 | −60.1% | −0.4557 to +0.1390 | no |
| utilisation (used / allocatable) | 0.03178 | 0.03158 | −0.6% | −0.0012 to +0.0008 | no |
| CPU used (cores), mean | 0.7627 | 0.7579 | −0.6% | −0.0281 to +0.0185 | no |
| Omni's own CPU (cores), mean | 0 | 0.03402 | +0.034 (native is 0) | +0.0284 to +0.0397 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7627 | 0.792 | +3.8% | +0.0098 to +0.0486 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 910.3 | 899.4 | −1.2% | −42.2293 to +20.2551 | no |
| HPA replicas, mean | 7.777 | 8.688 | +11.7% | +0.6445 to +1.1773 | yes: power given |
| pods started | 5.2 | 11.6 | +123.1% | +4.8474 to +7.9526 | yes: power given |
| pod start wait, total (s) | 7.6 | 18.3 | +140.8% | +7.7788 to +13.6212 | yes: LOSS |
| pod start wait, mean (s) | 1.47 | 1.592 | +8.3% | −0.2273 to +0.4708 | no |
| host CPU busy, the real machine under kind (%) | 23.68 | 24.85 | +5.0% | +0.6100 to +1.7358 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.516 | +0.2% | −0.0030 to +0.0083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.3 | 157.7 | +0.3% | −0.2427 to +1.0911 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.3 | 157.7 | +0.3% | −0.2427 to +1.0911 | no |
| response time (ms), mean | 65.27 | 69.37 | +6.3% | +1.1799 to +7.0270 | yes: LOSS |
| response time (ms), 95th percentile | 95.11 | 95.43 | +0.3% | −1.5508 to +2.1828 | no |
| response time (ms), 99th percentile | 127.6 | 128 | +0.3% | −9.8601 to +10.6371 | no |
| time over the response line (% of samples) | 0.04848 | 0.2167 | +346.9% | +0.0130 to +0.3234 | yes: LOSS |
| failed requests (%) | 0 | 0.03711 | +0.037 (native is 0) | −0.0056 to +0.0799 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.1 | 34.7 | +81.7% | +7.7700 to +23.4300 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 67.78 | −24.7% | −73.4667 to +29.0222 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.24 | 0.105 | −56.3% | −0.3013 to +0.0313 | no |
| utilisation (used / allocatable) | 0.03082 | 0.03158 | +2.5% | +0.0000 to +0.0015 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7397 | 0.7579 | +2.5% | +0.0003 to +0.0363 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.0327 | 0.03402 | +4.0% | +0.0004 to +0.0022 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7724 | 0.792 | +2.5% | +0.0019 to +0.0373 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 914.9 | 899.4 | −1.7% | −29.3102 to −1.8075 | yes, down (shown, not judged) |
| HPA replicas, mean | 7.963 | 8.688 | +9.1% | +0.2544 to +1.1961 | yes: power given |
| pods started | 4.7 | 11.6 | +146.8% | +5.5746 to +8.2254 | yes: power given |
| pod start wait, total (s) | 6 | 18.3 | +205.0% | +9.4980 to +15.1020 | yes: LOSS |
| pod start wait, mean (s) | 1.295 | 1.592 | +23.0% | +0.0470 to +0.5475 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 24.24 | 24.85 | +2.5% | +0.2464 to +0.9673 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*