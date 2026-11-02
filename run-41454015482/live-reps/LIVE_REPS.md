# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.011 |
| node-hours | 2.516 | 2.099 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 243.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 396.7 | 385.2 |
| response time (ms), 95th percentile | 1620 | 1772 |
| response time (ms), 99th percentile | 2638 | 2690 |
| time over the response line (% of samples) | 15.78 | 16.43 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.75 | 24.68 |
| utilisation (used / allocatable) | 0.06543 | 0.07933 |
| CPU used (cores), mean | 1.57 | 1.565 |
| Omni's own CPU (cores), mean | 0 | 0.07642 |
| CPU used with Omni's own (cores), mean | 1.57 | 1.642 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.5 | 372.6 |
| HPA replicas, mean | 2.129 | 2.173 |
| pods started | 0.5 | 0.6 |
| pod start wait, total (s) | 0.9 | 1.7 |
| pod start wait, mean (s) | 0.75 | 1.033 |
| host CPU busy, the real machine under kind (%) | 45.76 | 48.68 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 842.2 | 851 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.38 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9417 | 0.925 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 152.9 | 160.3 |
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
| worker nodes in service, mean | 6 | 5.011 | −16.5% | −1.8710 to −0.1078 | yes: GAIN |
| node-hours | 2.516 | 2.099 | −16.6% | −0.7849 to −0.0495 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.5 | −0.0% | −0.9586 to +0.7029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 243.3 | −11.4% | −59.2325 to −3.3023 | yes: GAIN |
| response time (ms), mean | 396.7 | 385.2 | −2.9% | −33.2794 to +10.2439 | no |
| response time (ms), 95th percentile | 1620 | 1772 | +9.4% | −16.5755 to +320.5425 | no |
| response time (ms), 99th percentile | 2638 | 2690 | +2.0% | −172.3530 to +275.3742 | no |
| time over the response line (% of samples) | 15.78 | 16.43 | +4.1% | −0.5758 to +1.8794 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.1 | +2.2% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96 | +96.000 (native is 0) | +31.0929 to +160.9071 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.75 | 24.68 | +13.5% | −0.5030 to +6.3697 | no |
| utilisation (used / allocatable) | 0.06543 | 0.07933 | +21.2% | +0.0023 to +0.0255 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.57 | 1.565 | −0.3% | −0.0465 to +0.0369 | no |
| Omni's own CPU (cores), mean | 0 | 0.07642 | +0.076 (native is 0) | +0.0699 to +0.0829 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.57 | 1.642 | +4.6% | +0.0247 to +0.1186 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.5 | 372.6 | −12.8% | −99.2228 to −10.5388 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.129 | 2.173 | +2.1% | −0.1457 to +0.2341 | no |
| pods started | 0.5 | 0.6 | +20.0% | −0.8802 to +1.0802 | no |
| pod start wait, total (s) | 0.9 | 1.7 | +88.9% | −1.9560 to +3.5560 | no |
| pod start wait, mean (s) | 0.75 | 1.033 | +37.8% | −1.2903 to +1.8570 | no |
| host CPU busy, the real machine under kind (%) | 45.76 | 48.68 | +6.4% | +2.3798 to +3.4507 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 842.2 | 851 | +1.0% | +3.2204 to +14.3796 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.38 | −27.0% | −2.9283 to −0.3115 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9417 | 0.925 | −1.8% | −0.1152 to +0.0819 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 1.9 | −9.5% | −0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 152.9 | 160.3 | +4.9% | +1.6346 to +13.2237 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*