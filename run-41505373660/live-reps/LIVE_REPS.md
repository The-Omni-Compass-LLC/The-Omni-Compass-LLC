# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.268 |
| node-hours | 2.519 | 2.211 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 251.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 429.3 | 411.6 |
| response time (ms), 95th percentile | 1592 | 1724 |
| response time (ms), 99th percentile | 2164 | 2453 |
| time over the response line (% of samples) | 18.65 | 17.8 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.12 | 15.65 |
| utilisation (used / allocatable) | 0.06378 | 0.07407 |
| CPU used (cores), mean | 1.531 | 1.542 |
| Omni's own CPU (cores), mean | 0 | 0.07196 |
| CPU used with Omni's own (cores), mean | 1.531 | 1.614 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.7 | 392.6 |
| HPA replicas, mean | 2.002 | 2.353 |
| pods started | 0 | 1.3 |
| pod start wait, total (s) | 0 | 2.7 |
| pod start wait, mean (s) | 0 | 1.15 |
| host CPU busy, the real machine under kind (%) | 43.6 | 46.8 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 811.8 | 823.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.711 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.4292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 118.4 | 128.4 |
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
| worker nodes in service, mean | 6 | 5.268 | −12.2% | −1.4043 to −0.0596 | yes: GAIN |
| node-hours | 2.519 | 2.211 | −12.2% | −0.5853 to −0.0304 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.6 | +0.1% | −0.4684 to +1.0171 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 251.5 | −8.3% | −43.7426 to −1.8836 | yes: GAIN |
| response time (ms), mean | 429.3 | 411.6 | −4.1% | −37.7640 to +2.3844 | no |
| response time (ms), 95th percentile | 1592 | 1724 | +8.3% | −36.1964 to +300.2724 | no |
| response time (ms), 99th percentile | 2164 | 2453 | +13.3% | −17.3490 to +594.2416 | no |
| time over the response line (% of samples) | 18.65 | 17.8 | −4.5% | −2.1836 to +0.4981 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.5 | −0.9% | −1.7673 to +1.5673 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.3 | +113.300 (native is 0) | +49.5025 to +177.0975 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.12 | 15.65 | +29.2% | −0.6017 to +7.6717 | no |
| utilisation (used / allocatable) | 0.06378 | 0.07407 | +16.1% | +0.0010 to +0.0196 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.531 | 1.542 | +0.7% | −0.0196 to +0.0415 | no |
| Omni's own CPU (cores), mean | 0 | 0.07196 | +0.072 (native is 0) | +0.0652 to +0.0787 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.531 | 1.614 | +5.4% | +0.0471 to +0.1188 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.7 | 392.6 | −9.9% | −77.6902 to −8.5640 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.353 | +17.6% | +0.0079 to +0.6950 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.2856 to +2.3144 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.3145 to +5.0855 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.15 | +1.150 (native is 0) | +0.3951 to +1.9049 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.6 | 46.8 | +7.3% | +2.4961 to +3.8948 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.8 | 823.3 | +1.4% | +0.6925 to +22.3075 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.711 | −21.5% | −2.2969 to −0.2819 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.4292 | +171.1% | −0.1916 to +0.7333 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.5 | +177.8% | −1.6025 to +4.8025 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.4 | 128.4 | +8.5% | −1.3319 to +21.3819 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*