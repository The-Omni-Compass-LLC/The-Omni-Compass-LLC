# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.975 |
| node-hours | 2.52 | 2.504 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 270.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.7 | 105 |
| response time (ms), 95th percentile | 244.8 | 237.7 |
| response time (ms), 99th percentile | 354.8 | 358.9 |
| time over the response line (% of samples) | 0.1919 | 0.2674 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1217 | 1230 |
| utilisation (used / allocatable) | 0.05838 | 0.0586 |
| CPU used (cores), mean | 1.401 | 1.401 |
| Omni's own CPU (cores), mean | 0 | 0.01237 |
| CPU used with Omni's own (cores), mean | 1.401 | 1.413 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.8 | 462 |
| HPA replicas, mean | 1.948 | 2.001 |
| pods started | 0.2 | 0 |
| pod start wait, total (s) | 0.5 | 0 |
| pod start wait, mean (s) | 0.25 | 0 |
| host CPU busy, the real machine under kind (%) | 44.62 | 44.73 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1448 | 1447 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.54 |
| queue: job wait, submitted to its first pod running, mean (s) | 173.2 | 172.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 765.4 | 759.1 |
| queue: job turnaround, submitted to done, mean (s) | 867.2 | 886 |
| queue: jobs unfinished at the window's end | 12.7 | 14.1 |

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
| worker nodes in service, mean | 6 | 5.975 | −0.4% | −0.0810 to +0.0313 | no |
| node-hours | 2.52 | 2.504 | −0.6% | −0.0407 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.5 | −0.3% | −1.8180 to +0.2765 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 270.7 | −0.6% | −3.4953 to +0.3871 | no |
| response time (ms), mean | 137.7 | 105 | −23.7% | −39.7572 to −25.5788 | yes: GAIN |
| response time (ms), 95th percentile | 244.8 | 237.7 | −2.9% | −20.2719 to +5.9709 | no |
| response time (ms), 99th percentile | 354.8 | 358.9 | +1.2% | −17.5719 to +25.8405 | no |
| time over the response line (% of samples) | 0.1919 | 0.2674 | +39.3% | −0.0273 to +0.1783 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.1 | +12.100 (native is 0) | +9.7772 to +14.4228 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1217 | 1230 | +1.1% | −72.6145 to +99.0812 | no |
| utilisation (used / allocatable) | 0.05838 | 0.0586 | +0.4% | −0.0011 to +0.0015 | no |
| CPU used (cores), mean | 1.401 | 1.401 | +0.0% | −0.0300 to +0.0300 | no |
| Omni's own CPU (cores), mean | 0 | 0.01237 | +0.012 (native is 0) | +0.0113 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.401 | 1.413 | +0.9% | −0.0171 to +0.0419 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.8 | 462 | −0.4% | −11.1524 to +7.5221 | no |
| HPA replicas, mean | 1.948 | 2.001 | +2.7% | −0.1069 to +0.2113 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.5 | 0 | −100.0% | −1.6310 to +0.6310 | no |
| pod start wait, mean (s) | 0.25 | 0 | −100.0% | −0.8155 to +0.3155 | no |
| host CPU busy, the real machine under kind (%) | 44.62 | 44.73 | +0.2% | −0.9171 to +1.1254 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1448 | 1447 | −0.1% | −14.0530 to +10.6530 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.54 | −7.7% | −6.3048 to +5.3848 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 173.2 | 172.5 | −0.4% | −43.5724 to +42.1308 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 765.4 | 759.1 | −0.8% | −170.0156 to +157.4156 | no |
| queue: job turnaround, submitted to done, mean (s) | 867.2 | 886 | +2.2% | −36.6045 to +74.1795 | no |
| queue: jobs unfinished at the window's end | 12.7 | 14.1 | +11.0% | −1.0825 to +3.8825 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*