# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.962 |
| node-hours | 2.513 | 2.081 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 240.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 379.2 | 348 |
| response time (ms), 95th percentile | 1374 | 1450 |
| response time (ms), 99th percentile | 1940 | 2015 |
| time over the response line (% of samples) | 17.46 | 16.42 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.44 | 12.79 |
| utilisation (used / allocatable) | 0.06267 | 0.07614 |
| CPU used (cores), mean | 1.504 | 1.475 |
| Omni's own CPU (cores), mean | 0 | 0.0156 |
| CPU used with Omni's own (cores), mean | 1.504 | 1.491 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.6 | 390.2 |
| HPA replicas, mean | 1.959 | 2.206 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.6 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 42.67 | 43.5 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 803.4 | 807.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.359 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2042 | 0.1417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 108.6 | 113.1 |
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
| worker nodes in service, mean | 6 | 4.962 | −17.3% | −1.9663 to −0.1089 | yes: GAIN |
| node-hours | 2.513 | 2.081 | −17.2% | −0.8218 to −0.0425 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.1 | −0.0% | −0.7922 to +0.6106 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 240.6 | −12.0% | −62.1736 to −3.1580 | yes: GAIN |
| response time (ms), mean | 379.2 | 348 | −8.2% | −48.9147 to −13.5211 | yes: GAIN |
| response time (ms), 95th percentile | 1374 | 1450 | +5.5% | −18.4074 to +169.2244 | no |
| response time (ms), 99th percentile | 1940 | 2015 | +3.9% | −70.4832 to +222.2942 | no |
| time over the response line (% of samples) | 17.46 | 16.42 | −5.9% | −1.9784 to −0.0865 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.2 | −2.4% | −1.0121 to +0.6121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.3 | +35.300 (native is 0) | +18.0829 to +52.5171 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.44 | 12.79 | +2.9% | −0.7451 to +1.4551 | no |
| utilisation (used / allocatable) | 0.06267 | 0.07614 | +21.5% | +0.0011 to +0.0258 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.504 | 1.475 | −1.9% | −0.0534 to −0.0043 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0156 | +0.016 (native is 0) | +0.0147 to +0.0165 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.504 | 1.491 | −0.9% | −0.0384 to +0.0119 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.6 | 390.2 | −12.2% | −104.7571 to −4.0332 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.959 | 2.206 | +12.6% | +0.1854 to +0.3099 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| host CPU busy, the real machine under kind (%) | 42.67 | 43.5 | +1.9% | +0.4315 to +1.2209 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 803.4 | 807.5 | +0.5% | −1.8604 to +10.0604 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.359 | −27.3% | −3.0958 to −0.1853 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2042 | 0.1417 | −30.6% | −0.2073 to +0.0823 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.1 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.6 | 113.1 | +4.1% | +0.1644 to +8.6773 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*