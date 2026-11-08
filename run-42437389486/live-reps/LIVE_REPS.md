# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.511 | 1.509 | 1.51 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.9 | 158.7 | 158.8 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.9 | 158.7 | 158.8 | 158.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 156.8 | 155 | 152.2 | 150 | 80.43 |
| response time (ms), 95th percentile | 346.9 | 350.2 | 334.2 | 334.3 | 119.6 |
| response time (ms), 99th percentile | 573.9 | 542.3 | 577.6 | 559.5 | 163.1 |
| time over the response line (% of samples) | 2.229 | 2.397 | 2.303 | 2.188 | 0.0122 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 2.4 | 2 | 2.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 19.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.32 | 0.1583 | 0.135 | 0.2683 |
| utilisation (used / allocatable) | 0.0395 | 0.03905 | 0.03919 | 0.03897 | 0.03741 |
| CPU used (cores), mean | 0.9481 | 0.9371 | 0.9406 | 0.9354 | 0.8978 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03775 |
| CPU used with Omni's own (cores), mean | 0.9481 | 0.9371 | 0.9406 | 0.9354 | 0.9355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 721.5 | 730.6 | 725.1 | 741.3 | 753.5 |
| HPA replicas, mean | 8.324 | 9.054 | 9.542 | 9.854 | 8.883 |
| pods started | 5 | 3.9 | 2.3 | 0.8 | 4 |
| pod start wait, total (s) | 8.1 | 6.3 | 3.6 | 1.4 | 6 |
| pod start wait, mean (s) | 1.627 | 1.505 | 1.1 | 0.35 | 1.445 |
| host CPU busy, the real machine under kind (%) | 28.92 | 28.64 | 28.74 | 28.39 | 29 |
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
| node-hours | 1.51 | 1.512 | +0.2% | −0.0024 to +0.0071 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.6 | −0.2% | −0.8528 to +0.3282 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.6 | −0.2% | −0.8528 to +0.3282 | no |
| response time (ms), mean | 156.8 | 80.43 | −48.7% | −101.6342 to −51.1366 | yes: GAIN |
| response time (ms), 95th percentile | 346.9 | 119.6 | −65.5% | −296.1193 to −158.4637 | yes: GAIN |
| response time (ms), 99th percentile | 573.9 | 163.1 | −71.6% | −542.1724 to −279.3970 | yes: GAIN |
| time over the response line (% of samples) | 2.229 | 0.0122 | −99.5% | −3.5171 to −0.9166 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.6509 to −0.9491 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.500 (native is 0) | +16.3866 to +22.6134 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.2683 | −0.6% | −0.2780 to +0.2747 | no |
| utilisation (used / allocatable) | 0.0395 | 0.03741 | −5.3% | −0.0032 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9481 | 0.8978 | −5.3% | −0.0766 to −0.0241 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03775 | +0.038 (native is 0) | +0.0323 to +0.0432 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9481 | 0.9355 | −1.3% | −0.0356 to +0.0104 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 721.5 | 753.5 | +4.4% | +14.9482 to +49.1130 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.324 | 8.883 | +6.7% | −0.0343 to +1.1523 | no |
| pods started | 5 | 4 | −20.0% | −2.2617 to +0.2617 | no |
| pod start wait, total (s) | 8.1 | 6 | −25.9% | −4.5187 to +0.3187 | no |
| pod start wait, mean (s) | 1.627 | 1.445 | −11.2% | −0.5350 to +0.1717 | no |
| host CPU busy, the real machine under kind (%) | 28.92 | 29 | +0.3% | −0.4806 to +0.6600 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 346.9 | 573.9 | 8.324 | 0.9481 | 6 |
| Native tuned, HPA target 40 | 350.2 | 542.3 | 9.054 | 0.9371 | 6 |
| Native tuned, HPA target 30 | 334.2 | 577.6 | 9.542 | 0.9406 | 6 |
| Native tuned, HPA target 20 | 334.3 | 559.5 | 9.854 | 0.9354 | 6 |
| omni | 119.6 | 163.1 | 8.883 | 0.9355 | 6 |

- omni (p95 119.6 ms): no native setting tried reached it; the lowest native p95 is 334.2 ms (Native tuned, HPA target 30).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*