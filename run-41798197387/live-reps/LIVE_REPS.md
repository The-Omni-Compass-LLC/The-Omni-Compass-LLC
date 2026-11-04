# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.514 | 1.514 | 1.512 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.8 | 158.7 | 158.5 | 158.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.8 | 158.7 | 158.5 | 158.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 145.8 | 142.1 | 139 | 139.3 | 76.69 |
| response time (ms), 95th percentile | 320.6 | 299.7 | 303.5 | 294.2 | 110.7 |
| response time (ms), 99th percentile | 516.1 | 502.7 | 493.3 | 477.3 | 155.7 |
| time over the response line (% of samples) | 1.651 | 1.533 | 1.558 | 1.372 | 0.01176 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 1.6 | 1.4 | 1.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 19.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.1883 | 0.05333 | 0.08333 | 0.2133 |
| utilisation (used / allocatable) | 0.03727 | 0.03725 | 0.03693 | 0.0369 | 0.03613 |
| CPU used (cores), mean | 0.8945 | 0.8939 | 0.8862 | 0.8857 | 0.8672 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03758 |
| CPU used with Omni's own (cores), mean | 0.8945 | 0.8939 | 0.8862 | 0.8857 | 0.9048 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.4 | 745 | 745.3 | 744.4 | 754.4 |
| HPA replicas, mean | 8.454 | 9.003 | 9.429 | 9.935 | 8.727 |
| pods started | 5.3 | 4.3 | 3 | 0.6 | 4.3 |
| pod start wait, total (s) | 9 | 6 | 4.3 | 0.9 | 6 |
| pod start wait, mean (s) | 1.703 | 1.292 | 1.442 | 0.6 | 1.425 |
| host CPU busy, the real machine under kind (%) | 27.71 | 27.66 | 27.44 | 27.67 | 28.19 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0003 to +0.0047 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.7 | −0.0% | −0.3993 to +0.3267 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.7 | −0.0% | −0.3993 to +0.3267 | no |
| response time (ms), mean | 145.8 | 76.69 | −47.4% | −89.2315 to −49.0650 | yes: GAIN |
| response time (ms), 95th percentile | 320.6 | 110.7 | −65.5% | −265.7519 to −154.0691 | yes: GAIN |
| response time (ms), 99th percentile | 516.1 | 155.7 | −69.8% | −457.3699 to −263.5159 | yes: GAIN |
| time over the response line (% of samples) | 1.651 | 0.01176 | −99.3% | −2.8047 to −0.4735 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.5329 to −0.2671 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +18.2310 to +20.3690 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.2133 | −27.7% | −0.4635 to +0.3002 | no |
| utilisation (used / allocatable) | 0.03727 | 0.03613 | −3.1% | −0.0023 to +0.0000 | no |
| CPU used (cores), mean | 0.8945 | 0.8672 | −3.1% | −0.0549 to +0.0002 | no |
| Omni's own CPU (cores), mean | 0 | 0.03758 | +0.038 (native is 0) | +0.0336 to +0.0415 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8945 | 0.9048 | +1.1% | −0.0151 to +0.0356 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.4 | 754.4 | +2.0% | −3.1502 to +33.2173 | no |
| HPA replicas, mean | 8.454 | 8.727 | +3.2% | −0.0590 to +0.6039 | no |
| pods started | 5.3 | 4.3 | −18.9% | −2.2158 to +0.2158 | no |
| pod start wait, total (s) | 9 | 6 | −33.3% | −4.9949 to −1.0051 | yes: GAIN |
| pod start wait, mean (s) | 1.703 | 1.425 | −16.3% | −0.5944 to +0.0377 | no |
| host CPU busy, the real machine under kind (%) | 27.71 | 28.19 | +1.7% | −0.0834 to +1.0386 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 320.6 | 516.1 | 8.454 | 0.8945 | 6 |
| Native tuned, HPA target 40 | 299.7 | 502.7 | 9.003 | 0.8939 | 6 |
| Native tuned, HPA target 30 | 303.5 | 493.3 | 9.429 | 0.8862 | 6 |
| Native tuned, HPA target 20 | 294.2 | 477.3 | 9.935 | 0.8857 | 6 |
| omni | 110.7 | 155.7 | 8.727 | 0.9048 | 6 |

- omni (p95 110.7 ms): no native setting tried reached it; the lowest native p95 is 294.2 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*