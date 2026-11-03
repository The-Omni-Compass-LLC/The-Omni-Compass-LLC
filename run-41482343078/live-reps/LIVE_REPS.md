# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.904 |
| node-hours | 2.518 | 2.056 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 240.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 380.5 | 402 |
| response time (ms), 95th percentile | 1567 | 1886 |
| response time (ms), 99th percentile | 2516 | 2831 |
| time over the response line (% of samples) | 15.54 | 16.21 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.33 | 26.25 |
| utilisation (used / allocatable) | 0.06487 | 0.0814 |
| CPU used (cores), mean | 1.557 | 1.571 |
| Omni's own CPU (cores), mean | 0 | 0.07699 |
| CPU used with Omni's own (cores), mean | 1.557 | 1.648 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.1 | 366.6 |
| HPA replicas, mean | 1.963 | 2.235 |
| pods started | 0.2 | 0.9 |
| pod start wait, total (s) | 0.7 | 2 |
| pod start wait, mean (s) | 0.7 | 0.5467 |
| host CPU busy, the real machine under kind (%) | 45.43 | 48.99 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 842 | 856.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.126 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8708 | 1.092 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 3.3 |
| queue: job turnaround, submitted to done, mean (s) | 154.6 | 167.3 |
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
| worker nodes in service, mean | 6 | 4.904 | −18.3% | −1.9631 to −0.2281 | yes: GAIN |
| node-hours | 2.518 | 2.056 | −18.3% | −0.8234 to −0.0994 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.7 | +0.0% | −1.0071 to +1.2299 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 240.2 | −12.5% | −61.6919 to −7.0228 | yes: GAIN |
| response time (ms), mean | 380.5 | 402 | +5.7% | −12.9608 to +56.0652 | no |
| response time (ms), 95th percentile | 1567 | 1886 | +20.4% | +78.7504 to +559.2366 | yes: LOSS |
| response time (ms), 99th percentile | 2516 | 2831 | +12.5% | +59.4829 to +570.6261 | yes: LOSS |
| time over the response line (% of samples) | 15.54 | 16.21 | +4.3% | −1.4836 to +2.8157 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.3 | +6.9% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.1 | +96.100 (native is 0) | +32.7340 to +159.4660 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.33 | 26.25 | +29.1% | +0.9834 to +10.8633 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06487 | 0.0814 | +25.5% | +0.0041 to +0.0290 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.557 | 1.571 | +0.9% | −0.0134 to +0.0409 | no |
| Omni's own CPU (cores), mean | 0 | 0.07699 | +0.077 (native is 0) | +0.0689 to +0.0850 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.557 | 1.648 | +5.8% | +0.0578 to +0.1236 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.1 | 366.6 | −15.4% | −116.8920 to −16.1624 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 2.235 | +13.8% | +0.0473 to +0.4963 | yes: power given |
| pods started | 0.2 | 0.9 | +350.0% | −0.4209 to +1.8209 | no |
| pod start wait, total (s) | 0.7 | 2 | +185.7% | −1.0129 to +3.6129 | no |
| pod start wait, mean (s) | 0.7 | 0.5467 | −21.9% | −0.9924 to +0.6857 | no |
| host CPU busy, the real machine under kind (%) | 45.43 | 48.99 | +7.8% | +2.7440 to +4.3776 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 842 | 856.8 | +1.8% | +1.2414 to +28.3586 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.126 | −31.2% | −3.1787 to −0.5684 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8708 | 1.092 | +25.4% | −0.0301 to +0.4718 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 3.3 | +73.7% | +0.3772 to +2.4228 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 154.6 | 167.3 | +8.2% | −0.8706 to +26.1456 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*