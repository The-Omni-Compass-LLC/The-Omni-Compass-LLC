# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.163 |
| node-hours | 2.514 | 2.166 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 248.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 426.7 | 433.9 |
| response time (ms), 95th percentile | 1842 | 2064 |
| response time (ms), 99th percentile | 2665 | 2955 |
| time over the response line (% of samples) | 16.05 | 16.77 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 62.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.77 | 28.42 |
| utilisation (used / allocatable) | 0.06616 | 0.07723 |
| CPU used (cores), mean | 1.588 | 1.586 |
| Omni's own CPU (cores), mean | 0 | 0.08048 |
| CPU used with Omni's own (cores), mean | 1.588 | 1.666 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422 | 376.7 |
| HPA replicas, mean | 2.052 | 2.296 |
| pods started | 0.2 | 1.1 |
| pod start wait, total (s) | 0.4 | 2.8 |
| pod start wait, mean (s) | 0.4 | 1.467 |
| host CPU busy, the real machine under kind (%) | 46.13 | 49.82 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 843.8 | 861.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.537 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8125 | 1.167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.9 |
| queue: job turnaround, submitted to done, mean (s) | 157.7 | 173.1 |
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
| worker nodes in service, mean | 6 | 5.163 | −13.9% | −1.5328 to −0.1404 | yes: GAIN |
| node-hours | 2.514 | 2.166 | −13.8% | −0.6388 to −0.0567 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.9 | +0.1% | −0.7608 to +1.5041 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 248.6 | −9.5% | −48.2265 to −3.6927 | yes: GAIN |
| response time (ms), mean | 426.7 | 433.9 | +1.7% | −33.6330 to +48.0232 | no |
| response time (ms), 95th percentile | 1842 | 2064 | +12.1% | −82.8319 to +526.9799 | no |
| response time (ms), 99th percentile | 2665 | 2955 | +10.9% | −13.2147 to +594.1265 | no |
| time over the response line (% of samples) | 16.05 | 16.77 | +4.5% | −0.8109 to +2.2552 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 10.3 | +13.2% | −0.1821 to +2.5821 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.9 | +96.900 (native is 0) | +35.9980 to +157.8020 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.77 | 28.42 | +24.8% | −1.5421 to +12.8488 | no |
| utilisation (used / allocatable) | 0.06616 | 0.07723 | +16.7% | +0.0024 to +0.0197 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.588 | 1.586 | −0.1% | −0.0387 to +0.0347 | no |
| Omni's own CPU (cores), mean | 0 | 0.08048 | +0.080 (native is 0) | +0.0735 to +0.0875 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.588 | 1.666 | +4.9% | +0.0372 to +0.1198 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422 | 376.7 | −10.7% | −79.7339 to −10.9810 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.052 | 2.296 | +11.9% | +0.0076 to +0.4804 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | +0.1128 to +1.6872 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.8 | +600.0% | +0.2095 to +4.5905 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.467 | +266.7% | +0.3756 to +1.7577 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.13 | 49.82 | +8.0% | +3.1518 to +4.2317 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 843.8 | 861.5 | +2.1% | +4.3346 to +31.0654 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.537 | −24.4% | −2.5264 to −0.3998 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8125 | 1.167 | +43.6% | +0.1136 to +0.5948 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.9 | +81.3% | +0.1295 to +2.4705 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 157.7 | 173.1 | +9.7% | +3.4011 to +27.3073 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*