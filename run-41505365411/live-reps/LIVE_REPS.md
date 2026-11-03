# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.16 |
| node-hours | 2.515 | 2.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 248.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 481.3 | 448.9 |
| response time (ms), 95th percentile | 2132 | 2183 |
| response time (ms), 99th percentile | 3014 | 3178 |
| time over the response line (% of samples) | 18.41 | 18.28 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.49 | 18.27 |
| utilisation (used / allocatable) | 0.06677 | 0.07942 |
| CPU used (cores), mean | 1.603 | 1.606 |
| Omni's own CPU (cores), mean | 0 | 0.07536 |
| CPU used with Omni's own (cores), mean | 1.603 | 1.681 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 419.1 | 370.4 |
| HPA replicas, mean | 2.066 | 2.473 |
| pods started | 0 | 1.7 |
| pod start wait, total (s) | 0 | 3.4 |
| pod start wait, mean (s) | 0 | 1.333 |
| host CPU busy, the real machine under kind (%) | 45.75 | 49.05 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 841.5 | 852.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.62 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 0.4958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 3.1 |
| queue: job turnaround, submitted to done, mean (s) | 150 | 161.7 |
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
| worker nodes in service, mean | 6 | 5.16 | −14.0% | −1.6724 to −0.0080 | yes: GAIN |
| node-hours | 2.515 | 2.16 | −14.1% | −0.7028 to −0.0063 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.9 | −0.0% | −1.3048 to +1.0814 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 248.5 | −9.6% | −52.6636 to −0.2682 | yes: GAIN |
| response time (ms), mean | 481.3 | 448.9 | −6.7% | −68.2711 to +3.3792 | no |
| response time (ms), 95th percentile | 2132 | 2183 | +2.4% | −144.4247 to +247.6177 | no |
| response time (ms), 99th percentile | 3014 | 3178 | +5.4% | −90.4714 to +417.2720 | no |
| time over the response line (% of samples) | 18.41 | 18.28 | −0.7% | −1.3824 to +1.1081 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.6 | ±0.0% | −0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.7 | +80.700 (native is 0) | +33.1776 to +128.2224 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.49 | 18.27 | +17.9% | +0.6792 to +4.8808 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06677 | 0.07942 | +18.9% | −0.0000 to +0.0253 | no |
| CPU used (cores), mean | 1.603 | 1.606 | +0.2% | −0.0153 to +0.0214 | no |
| Omni's own CPU (cores), mean | 0 | 0.07536 | +0.075 (native is 0) | +0.0689 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.603 | 1.681 | +4.9% | +0.0571 to +0.0998 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 419.1 | 370.4 | −11.6% | −98.3069 to +0.8385 | no |
| HPA replicas, mean | 2.066 | 2.473 | +19.7% | +0.0691 to +0.7446 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.6310 to +2.7690 | yes: power given |
| pod start wait, total (s) | 0 | 3.4 | +3.400 (native is 0) | +1.1330 to +5.6670 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.333 | +1.333 (native is 0) | +0.6314 to +2.0353 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.75 | 49.05 | +7.2% | +2.8185 to +3.7746 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841.5 | 852.9 | +1.4% | +1.6667 to +21.1333 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.62 | −23.0% | −2.5374 to −0.2227 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 0.4958 | +41.7% | −0.0877 to +0.3794 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 3.1 | +72.2% | −1.6980 to +4.2980 | no |
| queue: job turnaround, submitted to done, mean (s) | 150 | 161.7 | +7.8% | +1.4386 to +21.8697 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*