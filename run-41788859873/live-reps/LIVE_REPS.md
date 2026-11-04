# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.893 |
| node-hours | 2.514 | 2.048 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 238.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 449 | 437.2 |
| response time (ms), 95th percentile | 1676 | 1910 |
| response time (ms), 99th percentile | 2345 | 2518 |
| time over the response line (% of samples) | 17.83 | 17.49 |
| failed requests (%) | 0.01081 | 0.01117 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.67 | 17.08 |
| utilisation (used / allocatable) | 0.06302 | 0.07802 |
| CPU used (cores), mean | 1.512 | 1.517 |
| Omni's own CPU (cores), mean | 0 | 0.07626 |
| CPU used with Omni's own (cores), mean | 1.512 | 1.593 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 380.2 |
| HPA replicas, mean | 2.011 | 2.472 |
| pods started | 0 | 2.4 |
| pod start wait, total (s) | 0 | 6.5 |
| pod start wait, mean (s) | 0 | 2.08 |
| host CPU busy, the real machine under kind (%) | 43.66 | 46.98 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 821.1 | 829.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.08 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.762 | 1.733 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8.3 | 10.4 |
| queue: job turnaround, submitted to done, mean (s) | 122.6 | 131.8 |
| queue: jobs unfinished at the window's end | 0 | 0 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

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
| worker nodes in service, mean | 6 | 4.893 | −18.4% | −1.8777 to −0.3354 | yes: GAIN |
| node-hours | 2.514 | 2.048 | −18.5% | −0.7892 to −0.1423 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.5 | +0.0% | −0.7479 to +0.8373 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 238.7 | −12.7% | −59.2386 to −10.2386 | yes: GAIN |
| response time (ms), mean | 449 | 437.2 | −2.6% | −39.9232 to +16.2859 | no |
| response time (ms), 95th percentile | 1676 | 1910 | +13.9% | +50.4384 to +415.9546 | yes: LOSS |
| response time (ms), 99th percentile | 2345 | 2518 | +7.4% | −13.3564 to +358.9876 | no |
| time over the response line (% of samples) | 17.83 | 17.49 | −1.9% | −1.2536 to +0.5836 | no |
| failed requests (%) | 0.01081 | 0.01117 | +3.4% | −0.0005 to +0.0012 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 10.5 | +11.7% | −1.0709 to +3.2709 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.6 | +116.600 (native is 0) | +44.3212 to +188.8788 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.67 | 17.08 | +34.9% | +0.9179 to +7.9155 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06302 | 0.07802 | +23.8% | +0.0046 to +0.0254 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.512 | 1.517 | +0.3% | −0.0341 to +0.0428 | no |
| Omni's own CPU (cores), mean | 0 | 0.07626 | +0.076 (native is 0) | +0.0681 to +0.0844 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.512 | 1.593 | +5.3% | +0.0392 to +0.1220 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 380.2 | −14.7% | −112.7225 to −18.5543 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.472 | +22.9% | +0.2475 to +0.6740 | yes: power given |
| pods started | 0 | 2.4 | +2.400 (native is 0) | +1.0015 to +3.7985 | yes: power given |
| pod start wait, total (s) | 0 | 6.5 | +6.500 (native is 0) | +1.9105 to +11.0895 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.08 | +2.080 (native is 0) | +1.1624 to +2.9976 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.66 | 46.98 | +7.6% | +2.8363 to +3.8186 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.1 | 829.4 | +1.0% | −0.9901 to +17.5901 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.08 | −32.0% | −2.9946 to −0.8457 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.762 | 1.733 | −1.7% | −0.8703 to +0.8120 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8.3 | 10.4 | +25.3% | −0.9618 to +5.1618 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.6 | 131.8 | +7.5% | +0.0041 to +18.3625 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*