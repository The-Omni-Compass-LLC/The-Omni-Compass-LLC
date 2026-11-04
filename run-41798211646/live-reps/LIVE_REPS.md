# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.513 | 1.512 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.6 | 158.4 | 158.7 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.6 | 158.4 | 158.7 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 141.6 | 141.4 | 137.9 | 138.6 | 75.88 |
| response time (ms), 95th percentile | 317.7 | 305.5 | 294.1 | 304.5 | 111.7 |
| response time (ms), 99th percentile | 499.5 | 480.5 | 487.1 | 494.2 | 154.2 |
| time over the response line (% of samples) | 1.649 | 1.487 | 1.535 | 1.588 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 1.7 | 1.4 | 1.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 19 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.2083 | 0.1367 | 0.11 | 0.245 |
| utilisation (used / allocatable) | 0.03698 | 0.03687 | 0.0369 | 0.03707 | 0.03548 |
| CPU used (cores), mean | 0.8875 | 0.885 | 0.8856 | 0.8897 | 0.8514 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03593 |
| CPU used with Omni's own (cores), mean | 0.8875 | 0.885 | 0.8856 | 0.8897 | 0.8873 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.9 | 758.2 | 760.1 | 753.1 | 778.2 |
| HPA replicas, mean | 8.563 | 8.893 | 9.442 | 9.858 | 8.519 |
| pods started | 4.7 | 4.7 | 3.3 | 1 | 4.6 |
| pod start wait, total (s) | 8 | 7.8 | 5.5 | 1.5 | 7.1 |
| pod start wait, mean (s) | 1.646 | 1.65 | 1.65 | 0.475 | 1.537 |
| host CPU busy, the real machine under kind (%) | 27.33 | 27.27 | 27.11 | 27.3 | 27.64 |
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
| node-hours | 1.512 | 1.514 | +0.1% | +0.0007 to +0.0037 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.4 | −0.1% | −0.3460 to +0.1469 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.4 | −0.1% | −0.3460 to +0.1469 | no |
| response time (ms), mean | 141.6 | 75.88 | −46.4% | −88.1169 to −43.2282 | yes: GAIN |
| response time (ms), 95th percentile | 317.7 | 111.7 | −64.8% | −272.7157 to −139.3163 | yes: GAIN |
| response time (ms), 99th percentile | 499.5 | 154.2 | −69.1% | −470.8393 to −219.5953 | yes: GAIN |
| time over the response line (% of samples) | 1.649 | 0 | −100.0% | −3.0448 to −0.2523 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | −100.0% | −2.7729 to −0.2271 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19 | +19.000 (native is 0) | +17.7383 to +20.2617 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.245 | +32.4% | −0.1886 to +0.3086 | no |
| utilisation (used / allocatable) | 0.03698 | 0.03548 | −4.1% | −0.0024 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8875 | 0.8514 | −4.1% | −0.0577 to −0.0144 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03593 | +0.036 (native is 0) | +0.0306 to +0.0413 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8875 | 0.8873 | −0.0% | −0.0176 to +0.0174 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 754.9 | 778.2 | +3.1% | +14.3271 to +32.3814 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.563 | 8.519 | −0.5% | −0.3094 to +0.2208 | no |
| pods started | 4.7 | 4.6 | −2.1% | −1.3818 to +1.1818 | no |
| pod start wait, total (s) | 8 | 7.1 | −11.3% | −3.7303 to +1.9303 | no |
| pod start wait, mean (s) | 1.646 | 1.537 | −6.7% | −0.4331 to +0.2140 | no |
| host CPU busy, the real machine under kind (%) | 27.33 | 27.64 | +1.1% | −0.0909 to +0.6970 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 317.7 | 499.5 | 8.563 | 0.8875 | 6 |
| Native tuned, HPA target 40 | 305.5 | 480.5 | 8.893 | 0.885 | 6 |
| Native tuned, HPA target 30 | 294.1 | 487.1 | 9.442 | 0.8856 | 6 |
| Native tuned, HPA target 20 | 304.5 | 494.2 | 9.858 | 0.8897 | 6 |
| omni | 111.7 | 154.2 | 8.519 | 0.8873 | 6 |

- omni (p95 111.7 ms): no native setting tried reached it; the lowest native p95 is 294.1 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*