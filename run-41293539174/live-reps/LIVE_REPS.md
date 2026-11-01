# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.925 |
| node-hours | 2.515 | 2.066 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 239 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 365.8 | 335.5 |
| response time (ms), 95th percentile | 1297 | 1376 |
| response time (ms), 99th percentile | 1821 | 1955 |
| time over the response line (% of samples) | 14.46 | 13.95 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.03 | 10.27 |
| utilisation (used / allocatable) | 0.06013 | 0.07423 |
| CPU used (cores), mean | 1.443 | 1.443 |
| Omni's own CPU (cores), mean | 0 | 0.0172 |
| CPU used with Omni's own (cores), mean | 1.443 | 1.46 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 398.1 |
| HPA replicas, mean | 1.986 | 2.044 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 41.99 | 42.93 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 794.7 | 797.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.142 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.275 | 0.2667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 100.1 | 102.2 |
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
| worker nodes in service, mean | 6 | 4.925 | −17.9% | −1.8796 to −0.2702 | yes: GAIN |
| node-hours | 2.515 | 2.066 | −17.9% | −0.7888 to −0.1090 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.9 | +0.2% | −0.3761 to +1.1981 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 239 | −12.3% | −58.9680 to −7.8934 | yes: GAIN |
| response time (ms), mean | 365.8 | 335.5 | −8.3% | −40.5541 to −20.0212 | yes: GAIN |
| response time (ms), 95th percentile | 1297 | 1376 | +6.1% | −2.4912 to +161.3542 | no |
| response time (ms), 99th percentile | 1821 | 1955 | +7.3% | −13.0272 to +280.6202 | no |
| time over the response line (% of samples) | 14.46 | 13.95 | −3.5% | −1.5020 to +0.4867 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.6 | +1.3% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52 | +52.000 (native is 0) | +25.0599 to +78.9401 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.03 | 10.27 | +2.4% | −2.5744 to +3.0544 | no |
| utilisation (used / allocatable) | 0.06013 | 0.07423 | +23.5% | +0.0032 to +0.0250 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.443 | +0.0% | −0.0135 to +0.0137 | no |
| Omni's own CPU (cores), mean | 0 | 0.0172 | +0.017 (native is 0) | +0.0164 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.46 | +1.2% | +0.0037 to +0.0310 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 398.1 | −14.4% | −117.9644 to −16.4527 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.986 | 2.044 | +2.9% | −0.1417 to +0.2581 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 41.99 | 42.93 | +2.2% | +0.5188 to +1.3613 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.7 | 797.6 | +0.4% | −2.4150 to +8.2150 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.142 | −31.0% | −3.1788 to −0.5376 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.275 | 0.2667 | −3.0% | −0.2429 to +0.2263 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.1 | −21.4% | −1.8834 to +1.2834 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.1 | 102.2 | +2.0% | −1.7118 to +5.7285 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*