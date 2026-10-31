# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.513 | 1.514 | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.8 | 158.9 | 158.8 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.8 | 158.9 | 158.8 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 149.3 | 146.7 | 147.4 | 145.3 | 76.66 |
| response time (ms), 95th percentile | 335.1 | 325.7 | 322 | 326.5 | 115.7 |
| response time (ms), 99th percentile | 538.4 | 539.8 | 545.9 | 550 | 155.8 |
| time over the response line (% of samples) | 2.212 | 1.99 | 1.995 | 2.487 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 2.1 | 2 | 2.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 15.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.1883 | 0.1067 | 0.08167 | 0.2733 |
| utilisation (used / allocatable) | 0.0377 | 0.03759 | 0.03817 | 0.03788 | 0.03597 |
| CPU used (cores), mean | 0.9047 | 0.9022 | 0.9162 | 0.909 | 0.8632 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00898 |
| CPU used with Omni's own (cores), mean | 0.9047 | 0.9022 | 0.9162 | 0.909 | 0.8722 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.6 | 759.6 | 745.9 | 754.5 | 775.4 |
| HPA replicas, mean | 8.344 | 8.833 | 9.534 | 9.842 | 7.426 |
| pods started | 5.2 | 4.6 | 2.8 | 0.9 | 2.9 |
| pod start wait, total (s) | 8.6 | 5.9 | 3.7 | 1.1 | 4.2 |
| pod start wait, mean (s) | 1.703 | 1.342 | 1.317 | 0.4 | 1.423 |
| host CPU busy, the real machine under kind (%) | 27.84 | 27.68 | 28.07 | 27.82 | 26.96 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |

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
| node-hours | 1.514 | 1.514 | +0.0% | −0.0006 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.5 | −0.2% | −0.6082 to −0.0932 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.5 | −0.2% | −0.6082 to −0.0932 | yes: GAIN |
| response time (ms), mean | 149.3 | 76.66 | −48.6% | −97.5245 to −47.7327 | yes: GAIN |
| response time (ms), 95th percentile | 335.1 | 115.7 | −65.5% | −293.5979 to −145.0451 | yes: GAIN |
| response time (ms), 99th percentile | 538.4 | 155.8 | −71.1% | −505.6870 to −259.5158 | yes: GAIN |
| time over the response line (% of samples) | 2.212 | 0 | −100.0% | −3.5314 to −0.8931 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.7717 to −0.8283 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.4 | +15.400 (native is 0) | +12.1099 to +18.6901 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.2733 | +42.6% | −0.3275 to +0.4908 | no |
| utilisation (used / allocatable) | 0.0377 | 0.03597 | −4.6% | −0.0028 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9047 | 0.8632 | −4.6% | −0.0672 to −0.0157 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00898 | +0.009 (native is 0) | +0.0076 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9047 | 0.8722 | −3.6% | −0.0571 to −0.0079 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.6 | 775.4 | +3.0% | +7.3044 to +38.4213 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.344 | 7.426 | −11.0% | −1.5839 to −0.2521 | yes: GAIN |
| pods started | 5.2 | 2.9 | −44.2% | −3.3690 to −1.2310 | yes: GAIN |
| pod start wait, total (s) | 8.6 | 4.2 | −51.2% | −6.7410 to −2.0590 | yes: GAIN |
| pod start wait, mean (s) | 1.703 | 1.423 | −16.4% | −0.6355 to +0.0755 | no |
| host CPU busy, the real machine under kind (%) | 27.84 | 26.96 | −3.1% | −1.5671 to −0.1828 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 335.1 | 538.4 | 8.344 | 0.9047 | 6 |
| Native tuned, HPA target 40 | 325.7 | 539.8 | 8.833 | 0.9022 | 6 |
| Native tuned, HPA target 30 | 322 | 545.9 | 9.534 | 0.9162 | 6 |
| Native tuned, HPA target 20 | 326.5 | 550 | 9.842 | 0.909 | 6 |
| omni | 115.7 | 155.8 | 7.426 | 0.8722 | 6 |

- omni (p95 115.7 ms): no native setting tried reached it; the lowest native p95 is 322 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*