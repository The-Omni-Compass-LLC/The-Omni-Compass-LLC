# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.46 |
| node-hours | 2.515 | 2.291 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 259.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 652.3 | 651.5 |
| response time (ms), 95th percentile | 2901 | 3072 |
| response time (ms), 99th percentile | 3912 | 4234 |
| time over the response line (% of samples) | 24.22 | 24.29 |
| failed requests (%) | 0.02374 | 0.01183 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.6 | 14.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 43.31 | 54.65 |
| utilisation (used / allocatable) | 0.0706 | 0.07805 |
| CPU used (cores), mean | 1.694 | 1.703 |
| Omni's own CPU (cores), mean | 0 | 0.08427 |
| CPU used with Omni's own (cores), mean | 1.694 | 1.788 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 395.7 | 365.7 |
| HPA replicas, mean | 2.044 | 2.363 |
| pods started | 0 | 1.6 |
| pod start wait, total (s) | 0 | 3.4 |
| pod start wait, mean (s) | 0 | 1.125 |
| host CPU busy, the real machine under kind (%) | 51.34 | 54.92 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 932.7 | 951.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.867 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.629 | 1.533 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.2 | 4.6 |
| queue: job turnaround, submitted to done, mean (s) | 225.6 | 241.1 |
| queue: jobs unfinished at the window's end | 0 | 0 |
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
| worker nodes in service, mean | 6 | 5.46 | −9.0% | −1.0960 to +0.0167 | no |
| node-hours | 2.515 | 2.291 | −8.9% | −0.4574 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.8 | +0.1% | −0.4851 to +1.2981 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 259.8 | −6.0% | −34.1235 to +1.0074 | no |
| response time (ms), mean | 652.3 | 651.5 | −0.1% | −59.9185 to +58.2994 | no |
| response time (ms), 95th percentile | 2901 | 3072 | +5.9% | −59.2941 to +401.1881 | no |
| response time (ms), 99th percentile | 3912 | 4234 | +8.2% | +0.1905 to +643.3575 | yes: LOSS |
| time over the response line (% of samples) | 24.22 | 24.29 | +0.3% | −1.4275 to +1.5495 | no |
| failed requests (%) | 0.02374 | 0.01183 | −50.1% | −0.0387 to +0.0148 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.6 | 14.5 | +6.6% | +0.1887 to +1.6113 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.6 | +55.600 (native is 0) | +27.0848 to +84.1152 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 43.31 | 54.65 | +26.2% | +0.5544 to +22.1323 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0706 | 0.07805 | +10.5% | +0.0007 to +0.0142 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.694 | 1.703 | +0.5% | −0.0220 to +0.0403 | no |
| Omni's own CPU (cores), mean | 0 | 0.08427 | +0.084 (native is 0) | +0.0774 to +0.0912 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.694 | 1.788 | +5.5% | +0.0574 to +0.1294 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 395.7 | 365.7 | −7.6% | −60.2923 to +0.1649 | no |
| HPA replicas, mean | 2.044 | 2.363 | +15.6% | +0.1216 to +0.5178 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.4222 to +2.7778 | yes: power given |
| pod start wait, total (s) | 0 | 3.4 | +3.400 (native is 0) | +0.3802 to +6.4198 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.125 | +1.125 (native is 0) | +0.3467 to +1.9033 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.34 | 54.92 | +7.0% | +2.4856 to +4.6838 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 932.7 | 951.1 | +2.0% | −1.7988 to +38.5988 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.867 | −18.9% | −2.1040 to −0.1625 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.629 | 1.533 | −5.9% | −0.5492 to +0.3575 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.2 | 4.6 | −25.8% | −4.4850 to +1.2850 | no |
| queue: job turnaround, submitted to done, mean (s) | 225.6 | 241.1 | +6.9% | −2.5090 to +33.6424 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*