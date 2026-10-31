# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.514 | 1.514 | 1.517 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 157.8 | 157.8 | 158.1 | 157.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 157.8 | 157.8 | 158.1 | 157.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 123.3 | 119.2 | 115.3 | 115.6 | 66.44 |
| response time (ms), 95th percentile | 285.1 | 262.6 | 248.1 | 250.6 | 98.88 |
| response time (ms), 99th percentile | 439.2 | 433.5 | 423.8 | 396.2 | 131.7 |
| time over the response line (% of samples) | 1.691 | 1.451 | 1.291 | 1.37 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 1.4 | 1.4 | 1.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 13 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.24 | 0.1067 | 0.05333 | 0.1367 |
| utilisation (used / allocatable) | 0.03322 | 0.03342 | 0.03296 | 0.0331 | 0.03157 |
| CPU used (cores), mean | 0.7973 | 0.802 | 0.791 | 0.7945 | 0.7576 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00794 |
| CPU used with Omni's own (cores), mean | 0.7973 | 0.802 | 0.791 | 0.7945 | 0.7656 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 869.8 | 862.3 | 875.5 | 873.4 | 900.4 |
| HPA replicas, mean | 7.755 | 8.557 | 9.161 | 9.753 | 6.797 |
| pods started | 5.2 | 5.4 | 4 | 1.6 | 2.8 |
| pod start wait, total (s) | 8.3 | 7.8 | 6.3 | 2.5 | 4.7 |
| pod start wait, mean (s) | 1.617 | 1.456 | 1.587 | 0.7667 | 1.592 |
| host CPU busy, the real machine under kind (%) | 24.72 | 24.79 | 24.5 | 24.53 | 23.94 |
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
| node-hours | 1.516 | 1.517 | +0.0% | −0.0010 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 157.8 | −0.2% | −0.6270 to +0.0455 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 157.8 | −0.2% | −0.6270 to +0.0455 | no |
| response time (ms), mean | 123.3 | 66.44 | −46.1% | −86.7705 to −27.0549 | yes: GAIN |
| response time (ms), 95th percentile | 285.1 | 98.88 | −65.3% | −271.2565 to −101.0785 | yes: GAIN |
| response time (ms), 99th percentile | 439.2 | 131.7 | −70.0% | −445.6720 to −169.3522 | yes: GAIN |
| time over the response line (% of samples) | 1.691 | 0 | −100.0% | −3.2805 to −0.1016 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 0 | −100.0% | −3.5456 to −0.0544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13 | +13.000 (native is 0) | +9.8729 to +16.1271 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.1367 | −54.2% | −0.3249 to +0.0016 | no |
| utilisation (used / allocatable) | 0.03322 | 0.03157 | −5.0% | −0.0028 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.7973 | 0.7576 | −5.0% | −0.0682 to −0.0111 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00794 | +0.008 (native is 0) | +0.0062 to +0.0097 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7973 | 0.7656 | −4.0% | −0.0589 to −0.0046 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 869.8 | 900.4 | +3.5% | +4.5156 to +56.7622 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.755 | 6.797 | −12.4% | −1.8032 to −0.1126 | yes: GAIN |
| pods started | 5.2 | 2.8 | −46.2% | −3.2396 to −1.5604 | yes: GAIN |
| pod start wait, total (s) | 8.3 | 4.7 | −43.4% | −6.0128 to −1.1872 | yes: GAIN |
| pod start wait, mean (s) | 1.617 | 1.592 | −1.5% | −0.4024 to +0.3524 | no |
| host CPU busy, the real machine under kind (%) | 24.72 | 23.94 | −3.2% | −1.3769 to −0.1873 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 285.1 | 439.2 | 7.755 | 0.7973 | 6 |
| Native tuned, HPA target 40 | 262.6 | 433.5 | 8.557 | 0.802 | 6 |
| Native tuned, HPA target 30 | 248.1 | 423.8 | 9.161 | 0.791 | 6 |
| Native tuned, HPA target 20 | 250.6 | 396.2 | 9.753 | 0.7945 | 6 |
| omni | 98.88 | 131.7 | 6.797 | 0.7656 | 6 |

- omni (p95 98.88 ms): no native setting tried reached it; the lowest native p95 is 248.1 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*