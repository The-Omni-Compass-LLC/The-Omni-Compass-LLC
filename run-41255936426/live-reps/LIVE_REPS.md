# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.38 |
| node-hours | 2.517 | 2.255 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 255.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 391.1 | 406.1 |
| response time (ms), 95th percentile | 1591 | 1942 |
| response time (ms), 99th percentile | 2789 | 3036 |
| time over the response line (% of samples) | 16.12 | 17.65 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.98 | 20.49 |
| utilisation (used / allocatable) | 0.06706 | 0.07391 |
| CPU used (cores), mean | 1.609 | 1.593 |
| Omni's own CPU (cores), mean | 0 | 0.01832 |
| CPU used with Omni's own (cores), mean | 1.609 | 1.611 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.5 | 386.6 |
| HPA replicas, mean | 2.059 | 2.055 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.6 |
| pod start wait, mean (s) | 0.4 | 0.35 |
| host CPU busy, the real machine under kind (%) | 46.39 | 47.42 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 850.1 | 856.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.857 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8 | 0.8833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 162.1 | 169.3 |
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
| worker nodes in service, mean | 6 | 5.38 | −10.3% | −1.2639 to +0.0233 | no |
| node-hours | 2.517 | 2.255 | −10.4% | −0.5299 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 274.9 | −0.1% | −1.2041 to +0.4169 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 255.4 | −7.2% | −40.4299 to +0.5927 | no |
| response time (ms), mean | 391.1 | 406.1 | +3.8% | −13.0812 to +43.1899 | no |
| response time (ms), 95th percentile | 1591 | 1942 | +22.1% | +47.3954 to +654.9006 | yes: LOSS |
| response time (ms), 99th percentile | 2789 | 3036 | +8.9% | +72.5599 to +421.5309 | yes: LOSS |
| time over the response line (% of samples) | 16.12 | 17.65 | +9.5% | +0.1680 to +2.8990 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 11 | +5.8% | −0.3048 to +1.5048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.6 | +37.600 (native is 0) | +16.9228 to +58.2772 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.98 | 20.49 | +8.0% | −1.7158 to +4.7458 | no |
| utilisation (used / allocatable) | 0.06706 | 0.07391 | +10.2% | +0.0004 to +0.0133 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.609 | 1.593 | −1.0% | −0.0597 to +0.0267 | no |
| Omni's own CPU (cores), mean | 0 | 0.01832 | +0.018 (native is 0) | +0.0162 to +0.0204 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.609 | 1.611 | +0.1% | −0.0431 to +0.0467 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.5 | 386.6 | −7.2% | −58.9116 to −0.9482 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.059 | 2.055 | −0.2% | −0.1053 to +0.0956 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | −1.3379 to +1.7379 | no |
| pod start wait, mean (s) | 0.4 | 0.35 | −12.5% | −1.1991 to +1.0991 | no |
| host CPU busy, the real machine under kind (%) | 46.39 | 47.42 | +2.2% | +0.7510 to +1.2944 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 850.1 | 856.6 | +0.8% | +2.9594 to +10.0406 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.857 | −19.0% | −2.1984 to −0.0873 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8 | 0.8833 | +10.4% | −0.0462 to +0.2129 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.1 | +31.2% | −0.1079 to +1.1079 | no |
| queue: job turnaround, submitted to done, mean (s) | 162.1 | 169.3 | +4.5% | +1.7183 to +12.7734 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*