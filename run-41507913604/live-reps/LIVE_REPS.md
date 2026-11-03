# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.937 |
| node-hours | 2.513 | 2.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 269.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 116.2 | 93.62 |
| response time (ms), 95th percentile | 204.9 | 205.4 |
| response time (ms), 99th percentile | 297 | 310.7 |
| time over the response line (% of samples) | 0.1 | 0.1821 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 924.8 | 1063 |
| utilisation (used / allocatable) | 0.05766 | 0.05746 |
| CPU used (cores), mean | 1.384 | 1.366 |
| Omni's own CPU (cores), mean | 0 | 0.06522 |
| CPU used with Omni's own (cores), mean | 1.384 | 1.431 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470 | 471.6 |
| HPA replicas, mean | 1.954 | 2.094 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 0.3 | 0.7 |
| pod start wait, mean (s) | 0.3 | 0.2333 |
| host CPU busy, the real machine under kind (%) | 42.82 | 44.81 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1344 | 1420 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.202 |
| queue: job wait, submitted to its first pod running, mean (s) | 135.3 | 153.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 642.2 | 677.9 |
| queue: job turnaround, submitted to done, mean (s) | 700.2 | 762.2 |
| queue: jobs unfinished at the window's end | 7.5 | 7.7 |
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
| worker nodes in service, mean | 6 | 5.937 | −1.1% | −0.1883 to +0.0621 | no |
| node-hours | 2.513 | 2.489 | −0.9% | −0.0768 to +0.0293 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.2 | +0.1% | −0.8734 to +1.1709 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 269.2 | −0.7% | −5.7378 to +2.0520 | no |
| response time (ms), mean | 116.2 | 93.62 | −19.4% | −27.4177 to −17.7283 | yes: GAIN |
| response time (ms), 95th percentile | 204.9 | 205.4 | +0.3% | −8.7086 to +9.8486 | no |
| response time (ms), 99th percentile | 297 | 310.7 | +4.6% | −11.6606 to +39.0580 | no |
| time over the response line (% of samples) | 0.1 | 0.1821 | +82.0% | −0.1181 to +0.2821 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.6 | +107.600 (native is 0) | +81.5959 to +133.6041 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 924.8 | 1063 | +14.9% | +100.4842 to +175.5925 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05766 | 0.05746 | −0.4% | −0.0021 to +0.0017 | no |
| CPU used (cores), mean | 1.384 | 1.366 | −1.3% | −0.0495 to +0.0136 | no |
| Omni's own CPU (cores), mean | 0 | 0.06522 | +0.065 (native is 0) | +0.0554 to +0.0751 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.384 | 1.431 | +3.4% | +0.0173 to +0.0772 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470 | 471.6 | +0.3% | −12.5841 to +15.7503 | no |
| HPA replicas, mean | 1.954 | 2.094 | +7.2% | −0.1406 to +0.4205 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 0.3 | 0.7 | +133.3% | −1.3907 to +2.1907 | no |
| pod start wait, mean (s) | 0.3 | 0.2333 | −22.2% | −0.9715 to +0.8381 | no |
| host CPU busy, the real machine under kind (%) | 42.82 | 44.81 | +4.7% | +1.4387 to +2.5495 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1344 | 1420 | +5.7% | +8.2046 to +144.1954 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.202 | −13.3% | −3.2935 to +1.6985 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 135.3 | 153.1 | +13.2% | +0.7137 to +34.8780 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 642.2 | 677.9 | +5.6% | −86.5764 to +157.9764 | no |
| queue: job turnaround, submitted to done, mean (s) | 700.2 | 762.2 | +8.9% | −1.0383 to +125.0633 | no |
| queue: jobs unfinished at the window's end | 7.5 | 7.7 | +2.7% | −1.4450 to +1.8450 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*