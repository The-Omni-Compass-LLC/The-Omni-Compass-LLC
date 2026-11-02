# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.729 |
| node-hours | 2.513 | 1.983 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 233.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 419.8 | 400.8 |
| response time (ms), 95th percentile | 1580 | 1682 |
| response time (ms), 99th percentile | 2256 | 2388 |
| time over the response line (% of samples) | 17.33 | 17.38 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.74 | 15.34 |
| utilisation (used / allocatable) | 0.06196 | 0.08067 |
| CPU used (cores), mean | 1.487 | 1.487 |
| Omni's own CPU (cores), mean | 0 | 0.07185 |
| CPU used with Omni's own (cores), mean | 1.487 | 1.559 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.7 | 376.9 |
| HPA replicas, mean | 2 | 2.214 |
| pods started | 0 | 1 |
| pod start wait, total (s) | 0 | 2.1 |
| pod start wait, mean (s) | 0 | 1.017 |
| host CPU busy, the real machine under kind (%) | 43.08 | 46 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 816.6 | 823.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.988 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6792 | 1.013 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 5.2 | 6 |
| queue: job turnaround, submitted to done, mean (s) | 121.1 | 127.4 |
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
| worker nodes in service, mean | 6 | 4.729 | −21.2% | −2.1918 to −0.3493 | yes: GAIN |
| node-hours | 2.513 | 1.983 | −21.1% | −0.9150 to −0.1446 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.6 | +0.2% | −0.1961 to +1.4711 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 233.6 | −14.4% | −68.0663 to −10.6546 | yes: GAIN |
| response time (ms), mean | 419.8 | 400.8 | −4.5% | −37.9399 to −0.0588 | yes: GAIN |
| response time (ms), 95th percentile | 1580 | 1682 | +6.4% | +9.4650 to +193.7350 | yes: LOSS |
| response time (ms), 99th percentile | 2256 | 2388 | +5.9% | −10.9403 to +276.2829 | no |
| time over the response line (% of samples) | 17.33 | 17.38 | +0.3% | −0.7509 to +0.8470 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 9 | +11.1% | +0.2737 to +1.5263 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.6 | +143.600 (native is 0) | +58.0217 to +229.1783 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.74 | 15.34 | +11.7% | −0.8322 to +4.0455 | no |
| utilisation (used / allocatable) | 0.06196 | 0.08067 | +30.2% | +0.0043 to +0.0331 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.487 | −0.0% | −0.0134 to +0.0131 | no |
| Omni's own CPU (cores), mean | 0 | 0.07185 | +0.072 (native is 0) | +0.0630 to +0.0807 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.559 | +4.8% | +0.0550 to +0.0885 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.7 | 376.9 | −17.1% | −138.5330 to −17.0431 | yes, down (shown, not judged) |
| HPA replicas, mean | 2 | 2.214 | +10.7% | −0.1372 to +0.5647 | no |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.1740 to +1.8260 | yes: power given |
| pod start wait, total (s) | 0 | 2.1 | +2.100 (native is 0) | +0.0642 to +4.1358 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.017 | +1.017 (native is 0) | +0.1561 to +1.8772 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.08 | 46 | +6.8% | +2.4319 to +3.4025 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816.6 | 823.8 | +0.9% | −0.3083 to +14.7083 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.988 | −33.5% | −3.2494 to −0.7740 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6792 | 1.013 | +49.1% | −0.0921 to +0.7588 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 5.2 | 6 | +15.4% | −3.1869 to +4.7869 | no |
| queue: job turnaround, submitted to done, mean (s) | 121.1 | 127.4 | +5.3% | −0.4475 to +13.2058 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*