# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.514 | 1.513 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.8 | 157.8 | 157.8 | 157.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.8 | 157.8 | 157.8 | 157.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 123.3 | 118.4 | 117.1 | 116.5 | 66.17 |
| response time (ms), 95th percentile | 274.8 | 256.3 | 251 | 255 | 95.97 |
| response time (ms), 99th percentile | 455 | 424 | 421.1 | 413.9 | 125.3 |
| time over the response line (% of samples) | 1.349 | 1.265 | 1.152 | 1.208 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 1.2 | 1 | 1.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 14.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.2383 | 0.05333 | 0.08 | 0.215 |
| utilisation (used / allocatable) | 0.03324 | 0.03288 | 0.03317 | 0.03289 | 0.03153 |
| CPU used (cores), mean | 0.7978 | 0.7892 | 0.7962 | 0.7893 | 0.7566 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00776 |
| CPU used with Omni's own (cores), mean | 0.7978 | 0.7892 | 0.7962 | 0.7893 | 0.7644 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 870 | 870.8 | 864.7 | 863.5 | 896.2 |
| HPA replicas, mean | 7.923 | 8.604 | 9.23 | 9.712 | 7.241 |
| pods started | 4.9 | 5.3 | 3.9 | 1.8 | 3.5 |
| pod start wait, total (s) | 6.7 | 7.3 | 5.1 | 2.4 | 5.7 |
| pod start wait, mean (s) | 1.382 | 1.403 | 1.408 | 0.675 | 1.585 |
| host CPU busy, the real machine under kind (%) | 24.61 | 24.45 | 24.52 | 24.55 | 23.92 |
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
| node-hours | 1.514 | 1.514 | −0.0% | −0.0019 to +0.0012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.5 | −0.2% | −0.7409 to −0.0397 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.5 | −0.2% | −0.7409 to −0.0397 | yes: GAIN |
| response time (ms), mean | 123.3 | 66.17 | −46.3% | −84.1707 to −30.1522 | yes: GAIN |
| response time (ms), 95th percentile | 274.8 | 95.97 | −65.1% | −256.5994 to −100.9936 | yes: GAIN |
| response time (ms), 99th percentile | 455 | 125.3 | −72.5% | −472.8095 to −186.5165 | yes: GAIN |
| time over the response line (% of samples) | 1.349 | 0 | −100.0% | −2.6773 to −0.0206 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.8775 to +0.0775 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.8 | +14.800 (native is 0) | +11.8642 to +17.7358 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.215 | −9.2% | −0.2309 to +0.1876 | no |
| utilisation (used / allocatable) | 0.03324 | 0.03153 | −5.2% | −0.0031 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.7978 | 0.7566 | −5.2% | −0.0751 to −0.0073 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00776 | +0.008 (native is 0) | +0.0063 to +0.0092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7978 | 0.7644 | −4.2% | −0.0661 to −0.0008 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 870 | 896.2 | +3.0% | −4.9274 to +57.2762 | no |
| HPA replicas, mean | 7.923 | 7.241 | −8.6% | −1.2760 to −0.0871 | yes: GAIN |
| pods started | 4.9 | 3.5 | −28.6% | −3.0588 to +0.2588 | no |
| pod start wait, total (s) | 6.7 | 5.7 | −14.9% | −4.5686 to +2.5686 | no |
| pod start wait, mean (s) | 1.382 | 1.585 | +14.7% | −0.2905 to +0.6972 | no |
| host CPU busy, the real machine under kind (%) | 24.61 | 23.92 | −2.8% | −1.4989 to +0.1106 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 274.8 | 455 | 7.923 | 0.7978 | 6 |
| Native tuned, HPA target 40 | 256.3 | 424 | 8.604 | 0.7892 | 6 |
| Native tuned, HPA target 30 | 251 | 421.1 | 9.23 | 0.7962 | 6 |
| Native tuned, HPA target 20 | 255 | 413.9 | 9.712 | 0.7893 | 6 |
| omni | 95.97 | 125.3 | 7.241 | 0.7644 | 6 |

- omni (p95 95.97 ms): no native setting tried reached it; the lowest native p95 is 251 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*