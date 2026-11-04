# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.982 |
| node-hours | 2.519 | 2.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.7 | 114.2 |
| response time (ms), 95th percentile | 238.7 | 254.4 |
| response time (ms), 99th percentile | 358.5 | 365 |
| time over the response line (% of samples) | 0.2149 | 0.2636 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1207 | 1283 |
| utilisation (used / allocatable) | 0.05859 | 0.05841 |
| CPU used (cores), mean | 1.406 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0.07252 |
| CPU used with Omni's own (cores), mean | 1.406 | 1.47 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.8 | 462.7 |
| HPA replicas, mean | 2.019 | 2.239 |
| pods started | 0.2 | 1.3 |
| pod start wait, total (s) | 0.3 | 2.8 |
| pod start wait, mean (s) | 0.3 | 0.8583 |
| host CPU busy, the real machine under kind (%) | 44.53 | 46.84 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1455 | 1460 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 |
| queue: job wait, submitted to its first pod running, mean (s) | 169.7 | 185.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 743 | 790.9 |
| queue: job turnaround, submitted to done, mean (s) | 869.2 | 900.4 |
| queue: jobs unfinished at the window's end | 12.8 | 13.4 |
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
| worker nodes in service, mean | 6 | 5.982 | −0.3% | −0.0599 to +0.0232 | no |
| node-hours | 2.519 | 2.509 | −0.4% | −0.0271 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | −0.1% | −1.6032 to +0.8668 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.1 | −0.3% | −2.4314 to +0.5367 | no |
| response time (ms), mean | 137.7 | 114.2 | −17.1% | −26.5041 to −20.4433 | yes: GAIN |
| response time (ms), 95th percentile | 238.7 | 254.4 | +6.6% | +6.5373 to +25.0067 | yes: LOSS |
| response time (ms), 99th percentile | 358.5 | 365 | +1.8% | −13.3434 to +26.4050 | no |
| time over the response line (% of samples) | 0.2149 | 0.2636 | +22.6% | −0.0907 to +0.1880 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.7 | +114.700 (native is 0) | +96.7965 to +132.6035 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1207 | 1283 | +6.3% | +0.7621 to +150.5812 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05859 | 0.05841 | −0.3% | −0.0016 to +0.0013 | no |
| CPU used (cores), mean | 1.406 | 1.398 | −0.6% | −0.0399 to +0.0232 | no |
| Omni's own CPU (cores), mean | 0 | 0.07252 | +0.073 (native is 0) | +0.0654 to +0.0797 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.47 | +4.6% | +0.0363 to +0.0920 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.8 | 462.7 | +0.2% | −9.1631 to +10.9816 | no |
| HPA replicas, mean | 2.019 | 2.239 | +10.9% | −0.0522 to +0.4916 | no |
| pods started | 0.2 | 1.3 | +550.0% | −0.2676 to +2.4676 | no |
| pod start wait, total (s) | 0.3 | 2.8 | +833.3% | −0.4056 to +5.4056 | no |
| pod start wait, mean (s) | 0.3 | 0.8583 | +186.1% | −0.5300 to +1.6467 | no |
| host CPU busy, the real machine under kind (%) | 44.53 | 46.84 | +5.2% | +1.5182 to +3.0953 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 1460 | +0.3% | −6.9522 to +16.7522 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 | −8.3% | −6.8530 to +5.8530 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 169.7 | 185.7 | +9.4% | −22.7079 to +54.5913 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 743 | 790.9 | +6.4% | −180.6621 to +276.4621 | no |
| queue: job turnaround, submitted to done, mean (s) | 869.2 | 900.4 | +3.6% | −28.8080 to +91.2413 | no |
| queue: jobs unfinished at the window's end | 12.8 | 13.4 | +4.7% | −2.3241 to +3.5241 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*