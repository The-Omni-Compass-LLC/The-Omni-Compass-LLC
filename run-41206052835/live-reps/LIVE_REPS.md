# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.508 | 1.511 | 1.509 | 1.511 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.4 | 159.2 | 159.3 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.4 | 159.2 | 159.3 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 166.4 | 165.7 | 163.7 | 163.3 | 84.03 |
| response time (ms), 95th percentile | 376.8 | 375 | 371.7 | 372.4 | 127.8 |
| response time (ms), 99th percentile | 605.1 | 603.2 | 619 | 623.9 | 176.9 |
| time over the response line (% of samples) | 2.694 | 2.602 | 2.806 | 2.65 | 0.02403 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 2.8 | 2.9 | 2.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 18.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.1067 | 0.08167 | 0.1333 | 0.1667 |
| utilisation (used / allocatable) | 0.0416 | 0.04148 | 0.04124 | 0.04114 | 0.03893 |
| CPU used (cores), mean | 0.9985 | 0.9956 | 0.9897 | 0.9873 | 0.9343 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00988 |
| CPU used with Omni's own (cores), mean | 0.9985 | 0.9956 | 0.9897 | 0.9873 | 0.9441 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.8 | 673.6 | 674.8 | 677.2 | 706.2 |
| HPA replicas, mean | 8.656 | 9.229 | 9.598 | 9.915 | 8.282 |
| pods started | 5.4 | 3.7 | 2.4 | 0.6 | 2.9 |
| pod start wait, total (s) | 8.7 | 5.6 | 3.3 | 0.9 | 4.4 |
| pod start wait, mean (s) | 1.62 | 1.375 | 1.223 | 0.3 | 1.525 |
| host CPU busy, the real machine under kind (%) | 30.3 | 30.28 | 30.12 | 30.14 | 29.17 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.508 | 1.511 | +0.2% | −0.0021 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.8 | −0.2% | −0.9777 to +0.3474 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.8 | −0.2% | −0.9777 to +0.3474 | no |
| response time (ms), mean | 166.4 | 84.03 | −49.5% | −103.7109 to −61.1058 | yes: GAIN |
| response time (ms), 95th percentile | 376.8 | 127.8 | −66.1% | −308.8683 to −189.0867 | yes: GAIN |
| response time (ms), 99th percentile | 605.1 | 176.9 | −70.8% | −541.1776 to −315.2466 | yes: GAIN |
| time over the response line (% of samples) | 2.694 | 0.02403 | −99.1% | −3.9399 to −1.3990 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 | −100.0% | −3.7729 to −1.2271 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | +18.800 (native is 0) | +15.0330 to +22.5670 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.1667 | −38.3% | −0.3637 to +0.1570 | no |
| utilisation (used / allocatable) | 0.0416 | 0.03893 | −6.4% | −0.0035 to −0.0018 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9985 | 0.9343 | −6.4% | −0.0846 to −0.0439 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00988 | +0.010 (native is 0) | +0.0086 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9985 | 0.9441 | −5.4% | −0.0737 to −0.0351 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.8 | 706.2 | +6.1% | +29.9792 to +50.7394 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.656 | 8.282 | −4.3% | −0.9983 to +0.2500 | no |
| pods started | 5.4 | 2.9 | −46.3% | −3.2726 to −1.7274 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 4.4 | −49.4% | −6.0859 to −2.5141 | yes: GAIN |
| pod start wait, mean (s) | 1.62 | 1.525 | −5.8% | −0.5112 to +0.3221 | no |
| host CPU busy, the real machine under kind (%) | 30.3 | 29.17 | −3.7% | −1.5231 to −0.7352 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 376.8 | 605.1 | 8.656 | 0.9985 | 6 |
| Native tuned, HPA target 40 | 375 | 603.2 | 9.229 | 0.9956 | 6 |
| Native tuned, HPA target 30 | 371.7 | 619 | 9.598 | 0.9897 | 6 |
| Native tuned, HPA target 20 | 372.4 | 623.9 | 9.915 | 0.9873 | 6 |
| omni | 127.8 | 176.9 | 8.282 | 0.9441 | 6 |

- omni (p95 127.8 ms): no native setting tried reached it; the lowest native p95 is 371.7 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*