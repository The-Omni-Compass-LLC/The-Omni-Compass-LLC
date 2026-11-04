# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.515 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.4 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.4 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 146.2 | 76.63 | 80.15 |
| response time (ms), 95th percentile | 340.9 | 114.8 | 114.3 |
| response time (ms), 99th percentile | 529.7 | 157.7 | 161.1 |
| time over the response line (% of samples) | 2.378 | 0.03636 | 0.2418 |
| failed requests (%) | 0 | 0 | 0.07431 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.7 | 29 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3733 | 0.1667 | 0.1283 |
| utilisation (used / allocatable) | 0.03714 | 0.03541 | 0.03629 |
| CPU used (cores), mean | 0.8914 | 0.8497 | 0.871 |
| Omni's own CPU (cores), mean | 0 | 0.03662 | 0.03737 |
| CPU used with Omni's own (cores), mean | 0.8914 | 0.8863 | 0.9083 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.8 | 803.2 | 787.8 |
| HPA replicas, mean | 8.114 | 8.77 | 9.091 |
| pods started | 5.1 | 4.3 | 10.8 |
| pod start wait, total (s) | 8.5 | 6.3 | 18.5 |
| pod start wait, mean (s) | 1.67 | 1.43 | 1.771 |
| host CPU busy, the real machine under kind (%) | 27.34 | 27.68 | 28.4 |
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
| node-hours | 1.513 | 1.515 | +0.1% | −0.0030 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.4 | −0.1% | −0.7155 to +0.3039 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.4 | −0.1% | −0.7155 to +0.3039 | no |
| response time (ms), mean | 146.2 | 76.63 | −47.6% | −96.9246 to −42.1337 | yes: GAIN |
| response time (ms), 95th percentile | 340.9 | 114.8 | −66.3% | −307.9446 to −144.2394 | yes: GAIN |
| response time (ms), 99th percentile | 529.7 | 157.7 | −70.2% | −508.2196 to −235.9286 | yes: GAIN |
| time over the response line (% of samples) | 2.378 | 0.03636 | −98.5% | −3.7489 to −0.9346 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.7607 to −1.0393 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.7 | +20.700 (native is 0) | +18.7910 to +22.6090 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3733 | 0.1667 | −55.4% | −0.5936 to +0.1803 | no |
| utilisation (used / allocatable) | 0.03714 | 0.03541 | −4.7% | −0.0029 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8914 | 0.8497 | −4.7% | −0.0699 to −0.0135 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03662 | +0.037 (native is 0) | +0.0304 to +0.0428 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8914 | 0.8863 | −0.6% | −0.0290 to +0.0189 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.8 | 803.2 | +3.1% | −3.0266 to +51.9238 | no |
| HPA replicas, mean | 8.114 | 8.77 | +8.1% | +0.1459 to +1.1657 | yes: power given |
| pods started | 5.1 | 4.3 | −15.7% | −2.1403 to +0.5403 | no |
| pod start wait, total (s) | 8.5 | 6.3 | −25.9% | −4.8722 to +0.4722 | no |
| pod start wait, mean (s) | 1.67 | 1.43 | −14.4% | −0.4746 to −0.0064 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.34 | 27.68 | +1.2% | −0.1749 to +0.8412 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0030 to +0.0104 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.8 | +0.1% | −0.4911 to +0.8117 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.8 | +0.1% | −0.4911 to +0.8117 | no |
| response time (ms), mean | 146.2 | 80.15 | −45.2% | −92.3713 to −39.6388 | yes: GAIN |
| response time (ms), 95th percentile | 340.9 | 114.3 | −66.5% | −308.0287 to −145.2423 | yes: GAIN |
| response time (ms), 99th percentile | 529.7 | 161.1 | −69.6% | −506.8829 to −230.3733 | yes: GAIN |
| time over the response line (% of samples) | 2.378 | 0.2418 | −89.8% | −3.5483 to −0.7242 | yes: GAIN |
| failed requests (%) | 0 | 0.07431 | +0.074 (native is 0) | +0.0123 to +0.1363 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0.2 | −93.1% | −4.6385 to −0.7615 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29 | +29.000 (native is 0) | +21.7209 to +36.2791 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3733 | 0.1283 | −65.6% | −0.6605 to +0.1705 | no |
| utilisation (used / allocatable) | 0.03714 | 0.03629 | −2.3% | −0.0017 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8914 | 0.871 | −2.3% | −0.0399 to −0.0010 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03737 | +0.037 (native is 0) | +0.0317 to +0.0431 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8914 | 0.9083 | +1.9% | +0.0003 to +0.0336 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.8 | 787.8 | +1.2% | −7.3222 to +25.4547 | no |
| HPA replicas, mean | 8.114 | 9.091 | +12.0% | +0.7613 to +1.1912 | yes: power given |
| pods started | 5.1 | 10.8 | +111.8% | +4.1529 to +7.2471 | yes: power given |
| pod start wait, total (s) | 8.5 | 18.5 | +117.6% | +7.0798 to +12.9202 | yes: LOSS |
| pod start wait, mean (s) | 1.67 | 1.771 | +6.1% | −0.1696 to +0.3725 | no |
| host CPU busy, the real machine under kind (%) | 27.34 | 28.4 | +3.9% | +0.5601 to +1.5499 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.516 | +0.1% | −0.0067 to +0.0100 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.8 | +0.2% | −0.6296 to +1.3618 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.8 | +0.2% | −0.6296 to +1.3618 | no |
| response time (ms), mean | 76.63 | 80.15 | +4.6% | +0.2181 to +6.8301 | yes: LOSS |
| response time (ms), 95th percentile | 114.8 | 114.3 | −0.5% | −2.5706 to +1.4836 | no |
| response time (ms), 99th percentile | 157.7 | 161.1 | +2.2% | −6.0284 to +12.9204 | no |
| time over the response line (% of samples) | 0.03636 | 0.2418 | +565.1% | +0.0847 to +0.3263 | yes: LOSS |
| failed requests (%) | 0 | 0.07431 | +0.074 (native is 0) | +0.0123 to +0.1363 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.7 | 29 | +40.1% | +0.0469 to +16.5531 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 20 | −75.0% | −127.9978 to +7.9978 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1667 | 0.1283 | −23.0% | −0.2262 to +0.1495 | no |
| utilisation (used / allocatable) | 0.03541 | 0.03629 | +2.5% | +0.0002 to +0.0015 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8497 | 0.871 | +2.5% | +0.0055 to +0.0369 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03662 | 0.03737 | +2.0% | −0.0001 to +0.0016 | no |
| CPU used with Omni's own (cores), mean | 0.8863 | 0.9083 | +2.5% | +0.0065 to +0.0374 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 803.2 | 787.8 | −1.9% | −32.7321 to +1.9674 | no |
| HPA replicas, mean | 8.77 | 9.091 | +3.7% | −0.2259 to +0.8667 | no |
| pods started | 4.3 | 10.8 | +151.2% | +5.2271 to +7.7729 | yes: power given |
| pod start wait, total (s) | 6.3 | 18.5 | +193.7% | +8.8996 to +15.5004 | yes: LOSS |
| pod start wait, mean (s) | 1.43 | 1.771 | +23.9% | +0.0456 to +0.6382 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 27.68 | 28.4 | +2.6% | +0.3407 to +1.1030 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*