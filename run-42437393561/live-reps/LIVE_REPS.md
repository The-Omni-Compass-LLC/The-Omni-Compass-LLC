# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.512 | 1.51 | 1.511 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.9 | 158.7 | 158.7 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.9 | 158.7 | 158.7 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 155.4 | 151.3 | 148.8 | 148.4 | 79.89 |
| response time (ms), 95th percentile | 349.6 | 337.7 | 332.3 | 333.2 | 121.1 |
| response time (ms), 99th percentile | 557.4 | 546.4 | 537.9 | 558 | 166.2 |
| time over the response line (% of samples) | 2.289 | 2.098 | 2.202 | 2.414 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 2 | 2.3 | 2.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 18.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3667 | 0.1317 | 0.1867 | 0.11 | 0.35 |
| utilisation (used / allocatable) | 0.03892 | 0.03909 | 0.03875 | 0.03864 | 0.03713 |
| CPU used (cores), mean | 0.934 | 0.9381 | 0.93 | 0.9273 | 0.8911 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03735 |
| CPU used with Omni's own (cores), mean | 0.934 | 0.9381 | 0.93 | 0.9273 | 0.9284 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.1 | 729.7 | 737.1 | 739.4 | 753.9 |
| HPA replicas, mean | 8.522 | 8.918 | 9.485 | 9.87 | 8.884 |
| pods started | 4.8 | 4.7 | 2.7 | 1 | 3.5 |
| pod start wait, total (s) | 7.1 | 7.6 | 4 | 1.3 | 5.7 |
| pod start wait, mean (s) | 1.46 | 1.657 | 1.492 | 0.375 | 1.543 |
| host CPU busy, the real machine under kind (%) | 28.32 | 28.36 | 28.16 | 28.11 | 28.52 |
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
| node-hours | 1.51 | 1.511 | +0.1% | +0.0005 to +0.0025 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 | −0.2% | −0.5534 to +0.0369 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 | −0.2% | −0.5534 to +0.0369 | no |
| response time (ms), mean | 155.4 | 79.89 | −48.6% | −100.7860 to −50.2471 | yes: GAIN |
| response time (ms), 95th percentile | 349.6 | 121.1 | −65.4% | −300.8365 to −156.2265 | yes: GAIN |
| response time (ms), 99th percentile | 557.4 | 166.2 | −70.2% | −512.2308 to −270.1550 | yes: GAIN |
| time over the response line (% of samples) | 2.289 | 0 | −100.0% | −3.6707 to −0.9067 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 | −100.0% | −3.9795 to −1.0205 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | +18.600 (native is 0) | +16.9758 to +20.2242 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3667 | 0.35 | −4.5% | −0.3275 to +0.2942 | no |
| utilisation (used / allocatable) | 0.03892 | 0.03713 | −4.6% | −0.0029 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.934 | 0.8911 | −4.6% | −0.0699 to −0.0158 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03735 | +0.037 (native is 0) | +0.0318 to +0.0429 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.934 | 0.9284 | −0.6% | −0.0283 to +0.0173 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.1 | 753.9 | +3.2% | +8.5509 to +38.8837 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.522 | 8.884 | +4.2% | −0.0840 to +0.8072 | no |
| pods started | 4.8 | 3.5 | −27.1% | −2.2567 to −0.3433 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.7 | −19.7% | −3.0588 to +0.2588 | no |
| pod start wait, mean (s) | 1.46 | 1.543 | +5.7% | −0.1806 to +0.3472 | no |
| host CPU busy, the real machine under kind (%) | 28.32 | 28.52 | +0.7% | −0.1438 to +0.5406 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 349.6 | 557.4 | 8.522 | 0.934 | 6 |
| Native tuned, HPA target 40 | 337.7 | 546.4 | 8.918 | 0.9381 | 6 |
| Native tuned, HPA target 30 | 332.3 | 537.9 | 9.485 | 0.93 | 6 |
| Native tuned, HPA target 20 | 333.2 | 558 | 9.87 | 0.9273 | 6 |
| omni | 121.1 | 166.2 | 8.884 | 0.9284 | 6 |

- omni (p95 121.1 ms): no native setting tried reached it; the lowest native p95 is 332.3 ms (Native tuned, HPA target 30).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*