# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.51 | 1.51 | 1.51 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.8 | 158.7 | 158.7 | 158.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.8 | 158.7 | 158.7 | 158.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 156.4 | 152.5 | 150.2 | 148.9 | 79.57 |
| response time (ms), 95th percentile | 352.9 | 339.4 | 330.6 | 328.7 | 119.1 |
| response time (ms), 99th percentile | 583.9 | 547.4 | 548.9 | 558.5 | 162.2 |
| time over the response line (% of samples) | 2.291 | 2.033 | 2.025 | 2.003 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 2.1 | 2.1 | 1.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 18.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.1867 | 0.02667 | 0.02667 | 0.3583 |
| utilisation (used / allocatable) | 0.03897 | 0.03932 | 0.03907 | 0.03871 | 0.03702 |
| CPU used (cores), mean | 0.9353 | 0.9436 | 0.9376 | 0.9289 | 0.8884 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.0091 |
| CPU used with Omni's own (cores), mean | 0.9353 | 0.9436 | 0.9376 | 0.9289 | 0.8975 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713 | 703.3 | 708.9 | 720.2 | 738.9 |
| HPA replicas, mean | 8.55 | 9.052 | 9.563 | 9.944 | 7.849 |
| pods started | 5.2 | 4.4 | 2.7 | 0.4 | 4 |
| pod start wait, total (s) | 7 | 6.3 | 3.9 | 0.4 | 6.3 |
| pod start wait, mean (s) | 1.35 | 1.427 | 1.287 | 0.2 | 1.563 |
| host CPU busy, the real machine under kind (%) | 28.47 | 28.61 | 28.39 | 28.3 | 27.6 |
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
| node-hours | 1.51 | 1.51 | +0.0% | −0.0008 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.3 | −0.3% | −0.7236 to −0.1516 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.3 | −0.3% | −0.7236 to −0.1516 | yes: GAIN |
| response time (ms), mean | 156.4 | 79.57 | −49.1% | −100.5366 to −53.1874 | yes: GAIN |
| response time (ms), 95th percentile | 352.9 | 119.1 | −66.2% | −296.4244 to −171.1066 | yes: GAIN |
| response time (ms), 99th percentile | 583.9 | 162.2 | −72.2% | −523.9643 to −319.4573 | yes: GAIN |
| time over the response line (% of samples) | 2.291 | 0 | −100.0% | −3.5277 to −1.0541 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −3.7985 to −1.0015 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 | +18.100 (native is 0) | +14.3993 to +21.8007 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.3583 | +338.8% | −0.1196 to +0.6729 | no |
| utilisation (used / allocatable) | 0.03897 | 0.03702 | −5.0% | −0.0030 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9353 | 0.8884 | −5.0% | −0.0723 to −0.0215 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0091 | +0.009 (native is 0) | +0.0078 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9353 | 0.8975 | −4.0% | −0.0621 to −0.0136 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713 | 738.9 | +3.6% | +11.5208 to +40.3192 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.55 | 7.849 | −8.2% | −1.3535 to −0.0489 | yes: GAIN |
| pods started | 5.2 | 4 | −23.1% | −2.0121 to −0.3879 | yes: GAIN |
| pod start wait, total (s) | 7 | 6.3 | −10.0% | −2.2099 to +0.8099 | no |
| pod start wait, mean (s) | 1.35 | 1.563 | +15.8% | −0.1221 to +0.5483 | no |
| host CPU busy, the real machine under kind (%) | 28.47 | 27.6 | −3.1% | −1.5160 to −0.2385 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 352.9 | 583.9 | 8.55 | 0.9353 | 6 |
| Native tuned, HPA target 40 | 339.4 | 547.4 | 9.052 | 0.9436 | 6 |
| Native tuned, HPA target 30 | 330.6 | 548.9 | 9.563 | 0.9376 | 6 |
| Native tuned, HPA target 20 | 328.7 | 558.5 | 9.944 | 0.9289 | 6 |
| omni | 119.1 | 162.2 | 7.849 | 0.8975 | 6 |

- omni (p95 119.1 ms): no native setting tried reached it; the lowest native p95 is 328.7 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*