# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.382 |
| node-hours | 2.514 | 2.254 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 254.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 455.9 | 425.1 |
| response time (ms), 95th percentile | 1712 | 1814 |
| response time (ms), 99th percentile | 2507 | 2584 |
| time over the response line (% of samples) | 20.31 | 20.05 |
| failed requests (%) | 0.01117 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.79 | 10.96 |
| utilisation (used / allocatable) | 0.0635 | 0.07171 |
| CPU used (cores), mean | 1.524 | 1.524 |
| Omni's own CPU (cores), mean | 0 | 0.01668 |
| CPU used with Omni's own (cores), mean | 1.524 | 1.54 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 403.1 |
| HPA replicas, mean | 1.921 | 2.131 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.6 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 44.13 | 44.97 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 823.4 | 826.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.997 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.1958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 128.2 | 130.6 |
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
| worker nodes in service, mean | 6 | 5.382 | −10.3% | −1.3717 to +0.1360 | no |
| node-hours | 2.514 | 2.254 | −10.3% | −0.5798 to +0.0600 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.5 | −0.0% | −0.9018 to +0.8897 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 254.2 | −7.1% | −43.3214 to +4.5260 | no |
| response time (ms), mean | 455.9 | 425.1 | −6.8% | −44.4834 to −17.0740 | yes: GAIN |
| response time (ms), 95th percentile | 1712 | 1814 | +5.9% | +18.8964 to +184.1746 | yes: LOSS |
| response time (ms), 99th percentile | 2507 | 2584 | +3.1% | −171.3366 to +324.7732 | no |
| time over the response line (% of samples) | 20.31 | 20.05 | −1.3% | −0.7314 to +0.2127 | no |
| failed requests (%) | 0.01117 | 0 | −100.0% | −0.0364 to +0.0141 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.4 | −1.1% | −0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.7 | +37.700 (native is 0) | +14.2046 to +61.1954 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.79 | 10.96 | −7.1% | −4.1801 to +2.5068 | no |
| utilisation (used / allocatable) | 0.0635 | 0.07171 | +12.9% | −0.0026 to +0.0190 | no |
| CPU used (cores), mean | 1.524 | 1.524 | −0.0% | −0.0308 to +0.0303 | no |
| Omni's own CPU (cores), mean | 0 | 0.01668 | +0.017 (native is 0) | +0.0156 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.54 | +1.1% | −0.0148 to +0.0477 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 403.1 | −9.1% | −97.2002 to +16.4107 | no |
| HPA replicas, mean | 1.921 | 2.131 | +11.0% | +0.0132 to +0.4084 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| host CPU busy, the real machine under kind (%) | 44.13 | 44.97 | +1.9% | +0.5271 to +1.1554 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.4 | 826.6 | +0.4% | −1.8894 to +8.2894 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.997 | −16.7% | −2.1631 to +0.1561 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.1958 | +11.9% | −0.0241 to +0.0658 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 | −11.1% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 128.2 | 130.6 | +1.9% | −2.8039 to +7.6623 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*