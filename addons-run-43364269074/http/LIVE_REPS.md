# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.515 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 161 | 162 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 161 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 220.4 | 113.4 | 93.41 |
| response time (ms), 95th percentile | 516.6 | 293.7 | 141.8 |
| response time (ms), 99th percentile | 725 | 536.7 | 274.4 |
| time over the response line (% of samples) | 5.818 | 1.498 | 0.1339 |
| failed requests (%) | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 1.9 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | 6.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.08167 | 0.055 |
| utilisation (used / allocatable) | 0.03097 | 0.04538 | 0.04962 |
| CPU used (cores), mean | 0.7432 | 1.089 | 1.191 |
| Omni's own CPU (cores), mean | 0 | 0.06276 | 0.0112 |
| CPU used with Omni's own (cores), mean | 0.7432 | 1.152 | 1.202 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 840.5 | 586.5 | 538.8 |
| HPA replicas, mean | 2.998 | 2.595 | 2.443 |
| pods started | 2.8 | 2.5 | 2.3 |
| pod start wait, total (s) | 4.5 | 3.8 | 3.5 |
| pod start wait, mean (s) | 1.617 | 1.517 | 1.533 |
| host CPU busy, the real machine under kind (%) | 24.28 | 36.31 | 37.18 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.2% | −0.0065 to +0.0115 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 161 | +2.3% | +2.4601 to +4.6327 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 161 | +2.3% | +2.4601 to +4.6327 | yes: power given |
| response time (ms), mean | 220.4 | 113.4 | −48.6% | −119.2970 to −94.7643 | yes: GAIN |
| response time (ms), 95th percentile | 516.6 | 293.7 | −43.1% | −276.1613 to −169.5927 | yes: GAIN |
| response time (ms), 99th percentile | 725 | 536.7 | −26.0% | −238.8073 to −137.7537 | yes: GAIN |
| time over the response line (% of samples) | 5.818 | 1.498 | −74.2% | −5.9989 to −2.6407 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 1.9 | −66.1% | −5.2099 to −2.1901 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +74.3655 to +104.8345 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.08167 | −56.2% | −0.3800 to +0.1700 | no |
| utilisation (used / allocatable) | 0.03097 | 0.04538 | +46.6% | +0.0128 to +0.0160 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7432 | 1.089 | +46.6% | +0.3074 to +0.3847 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06276 | +0.063 (native is 0) | +0.0562 to +0.0693 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7432 | 1.152 | +55.0% | +0.3673 to +0.4503 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 840.5 | 586.5 | −30.2% | −276.2816 to −231.6426 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.998 | 2.595 | −13.4% | −0.6491 to −0.1569 | yes: GAIN |
| pods started | 2.8 | 2.5 | −10.7% | −0.7828 to +0.1828 | no |
| pod start wait, total (s) | 4.5 | 3.8 | −15.6% | −2.2471 to +0.8471 | no |
| pod start wait, mean (s) | 1.617 | 1.517 | −6.2% | −0.5874 to +0.3874 | no |
| host CPU busy, the real machine under kind (%) | 24.28 | 36.31 | +49.5% | +11.0778 to +12.9688 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0063 to +0.0116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 162 | +2.9% | +3.5497 to +5.5689 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 162 | +2.9% | +3.5497 to +5.5689 | yes: power given |
| response time (ms), mean | 220.4 | 93.41 | −57.6% | −140.5720 to −113.3699 | yes: GAIN |
| response time (ms), 95th percentile | 516.6 | 141.8 | −72.6% | −418.0432 to −331.5408 | yes: GAIN |
| response time (ms), 99th percentile | 725 | 274.4 | −62.1% | −512.4279 to −388.7279 | yes: GAIN |
| time over the response line (% of samples) | 5.818 | 0.1339 | −97.7% | −7.6514 to −3.7168 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 0.2 | −96.4% | −7.1260 to −3.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.7 | +6.700 (native is 0) | +3.5903 to +9.8097 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.055 | −70.5% | −0.3754 to +0.1120 | no |
| utilisation (used / allocatable) | 0.03097 | 0.04962 | +60.2% | +0.0179 to +0.0195 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7432 | 1.191 | +60.2% | +0.4285 to +0.4670 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0112 | +0.011 (native is 0) | +0.0100 to +0.0124 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7432 | 1.202 | +61.8% | +0.4391 to +0.4788 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 840.5 | 538.8 | −35.9% | −314.3108 to −289.1112 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.998 | 2.443 | −18.5% | −0.8238 to −0.2863 | yes: GAIN |
| pods started | 2.8 | 2.3 | −17.9% | −1.0058 to +0.0058 | no |
| pod start wait, total (s) | 4.5 | 3.5 | −22.2% | −2.4306 to +0.4306 | no |
| pod start wait, mean (s) | 1.617 | 1.533 | −5.2% | −0.5773 to +0.4106 | no |
| host CPU busy, the real machine under kind (%) | 24.28 | 37.18 | +53.1% | +12.2651 to +13.5337 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | +0.0% | −0.0030 to +0.0034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161 | 162 | +0.6% | +0.6216 to +1.4042 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161 | 162 | +0.6% | +0.6216 to +1.4042 | yes: power given |
| response time (ms), mean | 113.4 | 93.41 | −17.6% | −25.3217 to −14.5589 | yes: GAIN |
| response time (ms), 95th percentile | 293.7 | 141.8 | −51.7% | −180.3250 to −123.5050 | yes: GAIN |
| response time (ms), 99th percentile | 536.7 | 274.4 | −48.9% | −314.6928 to −209.9020 | yes: GAIN |
| time over the response line (% of samples) | 1.498 | 0.1339 | −91.1% | −1.8671 to −0.8615 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0.2 | −89.5% | −2.7144 to −0.6856 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 89.6 | 6.7 | −92.5% | −98.0831 to −67.7169 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.055 | −32.7% | −0.1349 to +0.0816 | no |
| utilisation (used / allocatable) | 0.04538 | 0.04962 | +9.3% | +0.0030 to +0.0055 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.089 | 1.191 | +9.3% | +0.0722 to +0.1313 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.06276 | 0.0112 | −82.2% | −0.0571 to −0.0460 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.152 | 1.202 | +4.4% | +0.0187 to +0.0817 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 586.5 | 538.8 | −8.1% | −63.9298 to −31.5680 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.595 | 2.443 | −5.9% | −0.3372 to +0.0331 | no |
| pods started | 2.5 | 2.3 | −8.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 3.8 | 3.5 | −7.9% | −1.3144 to +0.7144 | no |
| pod start wait, mean (s) | 1.517 | 1.533 | +1.1% | −0.2724 to +0.3057 | no |
| host CPU busy, the real machine under kind (%) | 36.31 | 37.18 | +2.4% | +0.1982 to +1.5540 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*