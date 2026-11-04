# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.274 |
| node-hours | 2.513 | 2.21 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 253.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 643 | 584.5 |
| response time (ms), 95th percentile | 3482 | 3461 |
| response time (ms), 99th percentile | 4559 | 4531 |
| time over the response line (% of samples) | 19.32 | 19.41 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 217.3 | 226.4 |
| utilisation (used / allocatable) | 0.07161 | 0.08036 |
| CPU used (cores), mean | 1.719 | 1.683 |
| Omni's own CPU (cores), mean | 0 | 0.08932 |
| CPU used with Omni's own (cores), mean | 1.719 | 1.772 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 388.4 | 359.9 |
| HPA replicas, mean | 2.099 | 2.157 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 0.8 | 0 |
| pod start wait, mean (s) | 0.8 | 0 |
| host CPU busy, the real machine under kind (%) | 49.23 | 51.97 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 678.5 | 696.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.711 |
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
| worker nodes in service, mean | 6 | 5.274 | −12.1% | −1.2572 to −0.1954 | yes: GAIN |
| node-hours | 2.513 | 2.21 | −12.1% | −0.5248 to −0.0826 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.4 | −0.1% | −1.7236 to +1.0504 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 253.6 | −8.4% | −39.6337 to −6.7395 | yes: GAIN |
| response time (ms), mean | 643 | 584.5 | −9.1% | −77.3849 to −39.5285 | yes: GAIN |
| response time (ms), 95th percentile | 3482 | 3461 | −0.6% | −111.8070 to +69.7580 | no |
| response time (ms), 99th percentile | 4559 | 4531 | −0.6% | −206.0646 to +150.7626 | no |
| time over the response line (% of samples) | 19.32 | 19.41 | +0.4% | −0.2411 to +0.4093 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.7 | +0.9% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.2 | +9.200 (native is 0) | +6.8687 to +11.5313 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 217.3 | 226.4 | +4.2% | +1.2565 to +16.9568 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07161 | 0.08036 | +12.2% | +0.0012 to +0.0163 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.719 | 1.683 | −2.1% | −0.0740 to +0.0021 | no |
| Omni's own CPU (cores), mean | 0 | 0.08932 | +0.089 (native is 0) | +0.0804 to +0.0983 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.719 | 1.772 | +3.1% | +0.0187 to +0.0881 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 388.4 | 359.9 | −7.3% | −57.6678 to +0.6069 | no |
| HPA replicas, mean | 2.099 | 2.157 | +2.7% | −0.3833 to +0.4986 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.8 | 0 | −100.0% | −2.6096 to +1.0096 | no |
| pod start wait, mean (s) | 0.8 | 0 | −100.0% | −2.6096 to +1.0096 | no |
| host CPU busy, the real machine under kind (%) | 49.23 | 51.97 | +5.6% | +2.4248 to +3.0566 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 678.5 | 696.1 | +2.6% | +15.2834 to +19.9166 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.711 | −21.5% | −2.1689 to −0.4101 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*