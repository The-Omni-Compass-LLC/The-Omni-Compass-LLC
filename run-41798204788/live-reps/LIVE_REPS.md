# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.512 | 1.513 | 1.513 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.2 | 159.3 | 159.2 | 158.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.2 | 159.3 | 159.2 | 158.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 162.2 | 160.3 | 155 | 154.1 | 81.98 |
| response time (ms), 95th percentile | 370.9 | 351.5 | 350.2 | 354.8 | 125.9 |
| response time (ms), 99th percentile | 621 | 586 | 587.7 | 596.5 | 175.6 |
| time over the response line (% of samples) | 2.877 | 2.351 | 2.142 | 2.402 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 2.3 | 2.3 | 2.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4917 | 0.16 | 0.1083 | 0.1067 | 0.4833 |
| utilisation (used / allocatable) | 0.03982 | 0.04009 | 0.04004 | 0.03993 | 0.03792 |
| CPU used (cores), mean | 0.9557 | 0.9622 | 0.9609 | 0.9584 | 0.9101 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.03738 |
| CPU used with Omni's own (cores), mean | 0.9557 | 0.9622 | 0.9609 | 0.9584 | 0.9475 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 715 | 704.1 | 701.3 | 710.6 | 732.3 |
| HPA replicas, mean | 8.529 | 8.94 | 9.544 | 9.856 | 8.678 |
| pods started | 5.3 | 4.6 | 2.9 | 0.7 | 3.6 |
| pod start wait, total (s) | 7.8 | 7.2 | 3.9 | 1.4 | 5 |
| pod start wait, mean (s) | 1.493 | 1.573 | 1.353 | 0.4083 | 1.335 |
| host CPU busy, the real machine under kind (%) | 28.88 | 29.22 | 29.07 | 28.89 | 29.06 |
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
| node-hours | 1.511 | 1.512 | +0.1% | +0.0002 to +0.0024 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.7 | −0.2% | −0.6425 to +0.0407 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.7 | −0.2% | −0.6425 to +0.0407 | no |
| response time (ms), mean | 162.2 | 81.98 | −49.5% | −106.2945 to −54.1942 | yes: GAIN |
| response time (ms), 95th percentile | 370.9 | 125.9 | −66.1% | −320.8190 to −169.2670 | yes: GAIN |
| response time (ms), 99th percentile | 621 | 175.6 | −71.7% | −584.0126 to −306.6834 | yes: GAIN |
| time over the response line (% of samples) | 2.877 | 0 | −100.0% | −4.3277 to −1.4272 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 0 | −100.0% | −4.3004 to −1.2996 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | +17.700 (native is 0) | +16.8047 to +18.5953 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4917 | 0.4833 | −1.7% | −0.5590 to +0.5423 | no |
| utilisation (used / allocatable) | 0.03982 | 0.03792 | −4.8% | −0.0031 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9557 | 0.9101 | −4.8% | −0.0754 to −0.0158 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03738 | +0.037 (native is 0) | +0.0325 to +0.0423 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9557 | 0.9475 | −0.9% | −0.0333 to +0.0168 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 715 | 732.3 | +2.4% | −9.6136 to +44.2517 | no |
| HPA replicas, mean | 8.529 | 8.678 | +1.7% | −0.1252 to +0.4235 | no |
| pods started | 5.3 | 3.6 | −32.1% | −2.5953 to −0.8047 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5 | −35.9% | −4.2621 to −1.3379 | yes: GAIN |
| pod start wait, mean (s) | 1.493 | 1.335 | −10.6% | −0.4996 to +0.1839 | no |
| host CPU busy, the real machine under kind (%) | 28.88 | 29.06 | +0.6% | −0.4709 to +0.8368 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 370.9 | 621 | 8.529 | 0.9557 | 6 |
| Native tuned, HPA target 40 | 351.5 | 586 | 8.94 | 0.9622 | 6 |
| Native tuned, HPA target 30 | 350.2 | 587.7 | 9.544 | 0.9609 | 6 |
| Native tuned, HPA target 20 | 354.8 | 596.5 | 9.856 | 0.9584 | 6 |
| omni | 125.9 | 175.6 | 8.678 | 0.9475 | 6 |

- omni (p95 125.9 ms): no native setting tried reached it; the lowest native p95 is 350.2 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*