# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.515 | 1.514 | 1.515 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.3 | 158.3 | 158.3 | 158 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158.3 | 158.3 | 158.3 | 158 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 135.1 | 130.6 | 128.2 | 127.5 | 72.74 |
| response time (ms), 95th percentile | 306.3 | 284.4 | 278 | 274.1 | 106.6 |
| response time (ms), 99th percentile | 500.3 | 434 | 455.7 | 441.8 | 143.2 |
| time over the response line (% of samples) | 1.715 | 1.472 | 1.406 | 1.235 | 0.06069 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 1.5 | 1.2 | 1.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 16.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3517 | 0.265 | 0.05333 | 0.1067 | 0.2217 |
| utilisation (used / allocatable) | 0.03475 | 0.03498 | 0.03508 | 0.0351 | 0.03421 |
| CPU used (cores), mean | 0.834 | 0.8394 | 0.8419 | 0.8423 | 0.8211 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00861 |
| CPU used with Omni's own (cores), mean | 0.834 | 0.8394 | 0.8419 | 0.8423 | 0.8297 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 818.8 | 810.6 | 808.2 | 808.1 | 824.8 |
| HPA replicas, mean | 7.973 | 8.775 | 9.404 | 9.815 | 7.46 |
| pods started | 5.4 | 5 | 3.3 | 1.3 | 3.8 |
| pod start wait, total (s) | 8.2 | 7.4 | 4.8 | 1.9 | 5.2 |
| pod start wait, mean (s) | 1.527 | 1.502 | 1.19 | 0.5667 | 1.393 |
| host CPU busy, the real machine under kind (%) | 25.87 | 25.97 | 25.92 | 26.04 | 25.81 |
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
| node-hours | 1.514 | 1.514 | 0.0% | raw −0.0015 to +0.0015 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158 | −0.1% | −0.3693 to +0.0761 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158 | −0.1% | −0.3693 to +0.0761 | no |
| response time (ms), mean | 135.1 | 72.74 | −46.2% | −87.4425 to −37.3420 | yes: GAIN |
| response time (ms), 95th percentile | 306.3 | 106.6 | −65.2% | −267.4372 to −131.8998 | yes: GAIN |
| response time (ms), 99th percentile | 500.3 | 143.2 | −71.4% | −493.3615 to −220.7519 | yes: GAIN |
| time over the response line (% of samples) | 1.715 | 0.06069 | −96.5% | −3.0364 to −0.2723 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −2.9572 to −0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.5 | +16.500 (native is 0) | +12.2715 to +20.7285 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3517 | 0.2217 | −37.0% | −0.4950 to +0.2350 | no |
| utilisation (used / allocatable) | 0.03475 | 0.03421 | −1.6% | −0.0015 to +0.0004 | no |
| CPU used (cores), mean | 0.834 | 0.8211 | −1.6% | −0.0350 to +0.0091 | no |
| Omni's own CPU (cores), mean | 0 | 0.00861 | +0.009 (native is 0) | +0.0070 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.834 | 0.8297 | −0.5% | −0.0258 to +0.0171 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 818.8 | 824.8 | +0.7% | −12.7958 to +24.6496 | no |
| HPA replicas, mean | 7.973 | 7.46 | −6.4% | −1.3033 to +0.2786 | no |
| pods started | 5.4 | 3.8 | −29.6% | −2.5048 to −0.6952 | yes: GAIN |
| pod start wait, total (s) | 8.2 | 5.2 | −36.6% | −4.5452 to −1.4548 | yes: GAIN |
| pod start wait, mean (s) | 1.527 | 1.393 | −8.7% | −0.4258 to +0.1591 | no |
| host CPU busy, the real machine under kind (%) | 25.87 | 25.81 | −0.2% | −0.7655 to +0.6479 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 306.3 | 500.3 | 7.973 | 0.834 | 6 |
| Native tuned, HPA target 40 | 284.4 | 434 | 8.775 | 0.8394 | 6 |
| Native tuned, HPA target 30 | 278 | 455.7 | 9.404 | 0.8419 | 6 |
| Native tuned, HPA target 20 | 274.1 | 441.8 | 9.815 | 0.8423 | 6 |
| omni | 106.6 | 143.2 | 7.46 | 0.8297 | 6 |

- omni (p95 106.6 ms): no native setting tried reached it; the lowest native p95 is 274.1 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*