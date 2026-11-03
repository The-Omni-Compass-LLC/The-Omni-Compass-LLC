# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.983 |
| node-hours | 2.517 | 2.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 132.6 | 109.1 |
| response time (ms), 95th percentile | 232 | 243.9 |
| response time (ms), 99th percentile | 328.9 | 371.7 |
| time over the response line (% of samples) | 0.1535 | 0.369 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1087 | 1162 |
| utilisation (used / allocatable) | 0.05933 | 0.05862 |
| CPU used (cores), mean | 1.424 | 1.403 |
| Omni's own CPU (cores), mean | 0 | 0.06987 |
| CPU used with Omni's own (cores), mean | 1.424 | 1.473 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.6 | 461.6 |
| HPA replicas, mean | 2.02 | 2.099 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.2 | 0.7 |
| pod start wait, mean (s) | 0.2 | 0.175 |
| host CPU busy, the real machine under kind (%) | 44.5 | 46.49 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1447 | 1462 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.529 |
| queue: job wait, submitted to its first pod running, mean (s) | 156 | 184.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 667.9 | 798.5 |
| queue: job turnaround, submitted to done, mean (s) | 814.2 | 836.7 |
| queue: jobs unfinished at the window's end | 9.6 | 10.9 |
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
| worker nodes in service, mean | 6 | 5.983 | −0.3% | −0.0564 to +0.0218 | no |
| node-hours | 2.517 | 2.511 | −0.2% | −0.0243 to +0.0134 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | −0.0% | −1.3781 to +1.3677 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.5 | −0.2% | −2.2599 to +1.1578 | no |
| response time (ms), mean | 132.6 | 109.1 | −17.7% | −27.4956 to −19.4784 | yes: GAIN |
| response time (ms), 95th percentile | 232 | 243.9 | +5.1% | −2.3696 to +26.1196 | no |
| response time (ms), 99th percentile | 328.9 | 371.7 | +13.0% | +20.4208 to +65.1032 | yes: LOSS |
| time over the response line (% of samples) | 0.1535 | 0.369 | +140.4% | +0.0279 to +0.4031 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104 | +104.000 (native is 0) | +90.4826 to +117.5174 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1087 | 1162 | +6.9% | +19.9917 to +130.5416 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05933 | 0.05862 | −1.2% | −0.0019 to +0.0005 | no |
| CPU used (cores), mean | 1.424 | 1.403 | −1.5% | −0.0472 to +0.0058 | no |
| Omni's own CPU (cores), mean | 0 | 0.06987 | +0.070 (native is 0) | +0.0629 to +0.0769 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.424 | 1.473 | +3.5% | +0.0231 to +0.0752 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.6 | 461.6 | +1.1% | −3.4601 to +13.4479 | no |
| HPA replicas, mean | 2.02 | 2.099 | +3.9% | −0.1806 to +0.3373 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.6567 to +1.2567 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | −1.1944 to +2.1944 | no |
| pod start wait, mean (s) | 0.2 | 0.175 | −12.5% | −0.6584 to +0.6084 | no |
| host CPU busy, the real machine under kind (%) | 44.5 | 46.49 | +4.5% | +1.3082 to +2.6636 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1447 | 1462 | +1.0% | −5.7101 to +33.9101 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.529 | −7.8% | −6.4499 to +5.5087 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 156 | 184.1 | +18.0% | −12.4255 to +68.6338 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 667.9 | 798.5 | +19.6% | −70.0281 to +331.2281 | no |
| queue: job turnaround, submitted to done, mean (s) | 814.2 | 836.7 | +2.8% | −33.1629 to +78.1796 | no |
| queue: jobs unfinished at the window's end | 9.6 | 10.9 | +13.5% | −0.7800 to +3.3800 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*