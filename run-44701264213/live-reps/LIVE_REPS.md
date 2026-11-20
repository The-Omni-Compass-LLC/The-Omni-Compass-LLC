# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.51 | 1.509 | 1.511 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | 158 | 158.2 | 157.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | 158 | 158.2 | 157.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 139.2 | 136.1 | 134.1 | 134 | 73.9 |
| response time (ms), 95th percentile | 298 | 283.2 | 291.6 | 276.7 | 100.8 |
| response time (ms), 99th percentile | 474.3 | 432.8 | 440.3 | 453 | 127.9 |
| time over the response line (% of samples) | 0.9896 | 0.8625 | 1.117 | 1.078 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0.6 | 1.2 | 0.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 19.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0 | 0.02833 | 0.02833 | 0.2133 |
| utilisation (used / allocatable) | 0.03647 | 0.03634 | 0.03631 | 0.03619 | 0.03508 |
| CPU used (cores), mean | 0.8753 | 0.8722 | 0.8715 | 0.8685 | 0.842 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.0336 |
| CPU used with Omni's own (cores), mean | 0.8753 | 0.8722 | 0.8715 | 0.8685 | 0.8756 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 742.6 | 746.8 | 750.3 | 750.8 | 771.7 |
| HPA replicas, mean | 8.538 | 8.961 | 9.481 | 9.917 | 8.686 |
| pods started | 5.6 | 4.6 | 2.6 | 0.6 | 5.4 |
| pod start wait, total (s) | 7.8 | 7 | 3.6 | 0.6 | 7.5 |
| pod start wait, mean (s) | 1.377 | 1.522 | 1.09 | 0.2 | 1.367 |
| host CPU busy, the real machine under kind (%) | 26.9 | 26.88 | 26.79 | 26.83 | 27.12 |
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
| node-hours | 1.511 | 1.51 | −0.1% | −0.0039 to +0.0012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | −0.3% | −0.7649 to −0.0875 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | −0.3% | −0.7649 to −0.0875 | yes: GAIN |
| response time (ms), mean | 139.2 | 73.9 | −46.9% | −84.8115 to −45.8357 | yes: GAIN |
| response time (ms), 95th percentile | 298 | 100.8 | −66.2% | −247.9025 to −146.4855 | yes: GAIN |
| response time (ms), 99th percentile | 474.3 | 127.9 | −73.0% | −479.6695 to −213.1237 | yes: GAIN |
| time over the response line (% of samples) | 0.9896 | 0 | −100.0% | −2.1036 to +0.1243 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0 | −100.0% | −2.2676 to +0.4676 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 | +19.800 (native is 0) | +18.6919 to +20.9081 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.2133 | +166.7% | −0.1249 to +0.3916 | no |
| utilisation (used / allocatable) | 0.03647 | 0.03508 | −3.8% | −0.0019 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8753 | 0.842 | −3.8% | −0.0453 to −0.0213 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0336 | +0.034 (native is 0) | +0.0298 to +0.0374 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8753 | 0.8756 | +0.0% | −0.0106 to +0.0112 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 742.6 | 771.7 | +3.9% | +15.0873 to +43.0998 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.538 | 8.686 | +1.7% | −0.2712 to +0.5666 | no |
| pods started | 5.6 | 5.4 | −3.6% | −1.0793 to +0.6793 | no |
| pod start wait, total (s) | 7.8 | 7.5 | −3.8% | −2.2676 to +1.6676 | no |
| pod start wait, mean (s) | 1.377 | 1.367 | −0.7% | −0.2623 to +0.2423 | no |
| host CPU busy, the real machine under kind (%) | 26.9 | 27.12 | +0.8% | −0.1957 to +0.6357 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 298 | 474.3 | 8.538 | 0.8753 | 6 |
| Native tuned, HPA target 40 | 283.2 | 432.8 | 8.961 | 0.8722 | 6 |
| Native tuned, HPA target 30 | 291.6 | 440.3 | 9.481 | 0.8715 | 6 |
| Native tuned, HPA target 20 | 276.7 | 453 | 9.917 | 0.8685 | 6 |
| omni | 100.8 | 127.9 | 8.686 | 0.8756 | 6 |

- omni (p95 100.8 ms): no native setting tried reached it; the lowest native p95 is 276.7 ms (Native tuned, HPA target 20).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*