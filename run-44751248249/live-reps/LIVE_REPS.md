# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.512 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 130.3 | 134.8 |
| response time (ms), 95th percentile | 225.7 | 238.6 |
| response time (ms), 99th percentile | 332.4 | 347.3 |
| time over the response line (% of samples) | 0.1619 | 0.1867 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1055 | 1151 |
| utilisation (used / allocatable) | 0.05994 | 0.05831 |
| CPU used (cores), mean | 1.439 | 1.399 |
| Omni's own CPU (cores), mean | 0 | 0.06461 |
| CPU used with Omni's own (cores), mean | 1.439 | 1.464 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.5 | 463.1 |
| HPA replicas, mean | 2.015 | 2.065 |
| pods started | 0.3 | 0.5 |
| pod start wait, total (s) | 0.7 | 1 |
| pod start wait, mean (s) | 0.7 | 0.5333 |
| host CPU busy, the real machine under kind (%) | 44.81 | 46.29 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1462 | 1510 |
| batch: worker machines in service after the queue finished, mean | 6 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 158.7 | 185.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 684.9 | 780.5 |
| queue: job turnaround, submitted to done, mean (s) | 780 | 854.1 |
| queue: jobs unfinished at the window's end | 7 | 10.4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.515 | +0.1% | −0.0059 to +0.0109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.4 | −0.2% | −1.2014 to +0.3226 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.4 | −0.2% | −1.2014 to +0.3226 | no |
| response time (ms), mean | 130.3 | 134.8 | +3.5% | +0.7438 to +8.3398 | yes: LOSS |
| response time (ms), 95th percentile | 225.7 | 238.6 | +5.7% | +3.5570 to +22.1980 | yes: LOSS |
| response time (ms), 99th percentile | 332.4 | 347.3 | +4.5% | +3.1491 to +26.6081 | yes: LOSS |
| time over the response line (% of samples) | 0.1619 | 0.1867 | +15.3% | −0.0862 to +0.1357 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.500 (native is 0) | +23.2974 to +37.7026 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1055 | 1151 | +9.1% | +25.0298 to +166.1268 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05994 | 0.05831 | −2.7% | −0.0027 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.399 | −2.7% | −0.0657 to −0.0128 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06461 | +0.065 (native is 0) | +0.0585 to +0.0708 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.464 | +1.8% | −0.0002 to +0.0511 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.5 | 463.1 | +2.6% | +3.8854 to +19.2126 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.015 | 2.065 | +2.5% | −0.1819 to +0.2820 | no |
| pods started | 0.3 | 0.5 | +66.7% | −0.6793 to +1.0793 | no |
| pod start wait, total (s) | 0.7 | 1 | +42.9% | −1.6963 to +2.2963 | no |
| pod start wait, mean (s) | 0.7 | 0.5333 | −23.8% | −1.4094 to +1.0761 | no |
| host CPU busy, the real machine under kind (%) | 44.81 | 46.29 | +3.3% | +0.7651 to +2.1788 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1462 | 1510 | +3.3% | −22.5176 to +117.9176 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 158.7 | 185.2 | +16.7% | +8.4506 to +44.4244 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 684.9 | 780.5 | +14.0% | −2.7363 to +193.9363 | no |
| queue: job turnaround, submitted to done, mean (s) | 780 | 854.1 | +9.5% | −5.7933 to +154.0016 | no |
| queue: jobs unfinished at the window's end | 7 | 10.4 | +48.6% | +0.2693 to +6.5307 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*