# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.515 | 1.512 | 1.511 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 158.3 | 158 | 157.8 | 157.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 158.3 | 158 | 157.8 | 157.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 131.3 | 126.5 | 127.3 | 125.7 | 71.46 |
| response time (ms), 95th percentile | 282.2 | 272.9 | 277 | 273.1 | 100 |
| response time (ms), 99th percentile | 476.5 | 428.6 | 441.8 | 439 | 127.4 |
| time over the response line (% of samples) | 1.388 | 1.094 | 1.41 | 1.365 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.1 | 1.2 | 1.3 | 1.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 19.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1267 | 0.1333 | 0.02833 | 0.055 | 0.1617 |
| utilisation (used / allocatable) | 0.03492 | 0.0348 | 0.03496 | 0.03467 | 0.03421 |
| CPU used (cores), mean | 0.8382 | 0.8353 | 0.8391 | 0.832 | 0.8211 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03433 |
| CPU used with Omni's own (cores), mean | 0.8382 | 0.8353 | 0.8391 | 0.832 | 0.8554 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.5 | 813 | 802 | 812.6 | 817.1 |
| HPA replicas, mean | 8.209 | 8.948 | 9.333 | 9.792 | 8.458 |
| pods started | 5.4 | 4.2 | 3.3 | 1.3 | 4.7 |
| pod start wait, total (s) | 7.8 | 6.2 | 4.5 | 1.8 | 6.6 |
| pod start wait, mean (s) | 1.475 | 1.408 | 1.267 | 0.5917 | 1.36 |
| host CPU busy, the real machine under kind (%) | 26 | 25.87 | 26.04 | 25.75 | 26.7 |
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
| node-hours | 1.51 | 1.511 | +0.1% | −0.0003 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.8 | −0.0% | −0.2859 to +0.2104 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.8 | −0.0% | −0.2859 to +0.2104 | no |
| response time (ms), mean | 131.3 | 71.46 | −45.6% | −84.4224 to −35.3564 | yes: GAIN |
| response time (ms), 95th percentile | 282.2 | 100 | −64.6% | −247.7111 to −116.5769 | yes: GAIN |
| response time (ms), 99th percentile | 476.5 | 127.4 | −73.3% | −492.2761 to −205.8753 | yes: GAIN |
| time over the response line (% of samples) | 1.388 | 0 | −100.0% | −2.6624 to −0.1132 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.1 | 0 | −100.0% | −2.2410 to +0.0410 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | +19.100 (native is 0) | +17.6129 to +20.5871 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1267 | 0.1617 | +27.6% | −0.1503 to +0.2203 | no |
| utilisation (used / allocatable) | 0.03492 | 0.03421 | −2.0% | −0.0015 to +0.0001 | no |
| CPU used (cores), mean | 0.8382 | 0.8211 | −2.0% | −0.0364 to +0.0022 | no |
| Omni's own CPU (cores), mean | 0 | 0.03433 | +0.034 (native is 0) | +0.0291 to +0.0395 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8382 | 0.8554 | +2.1% | +0.0005 to +0.0340 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.5 | 817.1 | +1.6% | −6.2535 to +31.4304 | no |
| HPA replicas, mean | 8.209 | 8.458 | +3.0% | −0.2898 to +0.7892 | no |
| pods started | 5.4 | 4.7 | −13.0% | −1.6567 to +0.2567 | no |
| pod start wait, total (s) | 7.8 | 6.6 | −15.4% | −3.5313 to +1.1313 | no |
| pod start wait, mean (s) | 1.475 | 1.36 | −7.8% | −0.4359 to +0.2050 | no |
| host CPU busy, the real machine under kind (%) | 26 | 26.7 | +2.7% | +0.4438 to +0.9516 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 282.2 | 476.5 | 8.209 | 0.8382 | 6 |
| Native tuned, HPA target 40 | 272.9 | 428.6 | 8.948 | 0.8353 | 6 |
| Native tuned, HPA target 30 | 277 | 441.8 | 9.333 | 0.8391 | 6 |
| Native tuned, HPA target 20 | 273.1 | 439 | 9.792 | 0.832 | 6 |
| omni | 100 | 127.4 | 8.458 | 0.8554 | 6 |

- omni (p95 100 ms): no native setting tried reached it; the lowest native p95 is 272.9 ms (Native tuned, HPA target 40).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*