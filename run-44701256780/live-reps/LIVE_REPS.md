# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.509 | 1.509 | 1.51 | 1.51 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.6 | 158.5 | 158.7 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.6 | 158.5 | 158.7 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 150 | 148.2 | 143.7 | 146.8 | 78.57 |
| response time (ms), 95th percentile | 322.9 | 316.9 | 317.7 | 316.9 | 109.4 |
| response time (ms), 99th percentile | 504.4 | 480 | 471.8 | 505.6 | 146.5 |
| time over the response line (% of samples) | 1.442 | 1.464 | 1.307 | 1.44 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 1.5 | 1.3 | 1.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 19.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.05333 | 0.08 | 0.08 | 0.32 |
| utilisation (used / allocatable) | 0.0385 | 0.0385 | 0.03822 | 0.03872 | 0.03744 |
| CPU used (cores), mean | 0.9239 | 0.924 | 0.9174 | 0.9294 | 0.8986 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03579 |
| CPU used with Omni's own (cores), mean | 0.9239 | 0.924 | 0.9174 | 0.9294 | 0.9344 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704 | 702.8 | 708.4 | 699.8 | 719.6 |
| HPA replicas, mean | 8.703 | 9.078 | 9.601 | 9.964 | 9.049 |
| pods started | 5.2 | 4.4 | 2.2 | 0.3 | 4.9 |
| pod start wait, total (s) | 8.6 | 7.2 | 3 | 0.4 | 6.5 |
| pod start wait, mean (s) | 1.677 | 1.665 | 1.137 | 0.1333 | 1.375 |
| host CPU busy, the real machine under kind (%) | 28.19 | 28.28 | 28.08 | 28.38 | 28.76 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan |

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
| node-hours | 1.509 | 1.51 | +0.0% | −0.0005 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.4 | −0.1% | −0.3129 to +0.0535 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.4 | −0.1% | −0.3129 to +0.0535 | no |
| response time (ms), mean | 150 | 78.57 | −47.6% | −88.1130 to −54.7554 | yes: GAIN |
| response time (ms), 95th percentile | 322.9 | 109.4 | −66.1% | −257.4040 to −169.6680 | yes: GAIN |
| response time (ms), 99th percentile | 504.4 | 146.5 | −71.0% | −442.5019 to −273.2797 | yes: GAIN |
| time over the response line (% of samples) | 1.442 | 0 | −100.0% | −2.5176 to −0.3662 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.8775 to +0.0775 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.500 (native is 0) | +18.3690 to +20.6310 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2683 | 0.32 | +19.3% | −0.2162 to +0.3196 | no |
| utilisation (used / allocatable) | 0.0385 | 0.03744 | −2.7% | −0.0020 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9239 | 0.8986 | −2.7% | −0.0491 to −0.0015 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03579 | +0.036 (native is 0) | +0.0317 to +0.0398 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9239 | 0.9344 | +1.1% | −0.0112 to +0.0322 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704 | 719.6 | +2.2% | +2.8420 to +28.3202 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.703 | 9.049 | +4.0% | −0.0011 to +0.6930 | no |
| pods started | 5.2 | 4.9 | −5.8% | −1.5181 to +0.9181 | no |
| pod start wait, total (s) | 8.6 | 6.5 | −24.4% | −4.4228 to +0.2228 | no |
| pod start wait, mean (s) | 1.677 | 1.375 | −18.0% | −0.5954 to −0.0079 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.19 | 28.76 | +2.0% | +0.1811 to +0.9596 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 322.9 | 504.4 | 8.703 | 0.9239 | 6 |
| Native tuned, HPA target 40 | 316.9 | 480 | 9.078 | 0.924 | 6 |
| Native tuned, HPA target 30 | 317.7 | 471.8 | 9.601 | 0.9174 | 6 |
| Native tuned, HPA target 20 | 316.9 | 505.6 | 9.964 | 0.9294 | 6 |
| omni | 109.4 | 146.5 | 9.049 | 0.9344 | 6 |

- omni (p95 109.4 ms): no native setting tried reached it; the lowest native p95 is 316.9 ms (Native tuned, HPA target 40).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*