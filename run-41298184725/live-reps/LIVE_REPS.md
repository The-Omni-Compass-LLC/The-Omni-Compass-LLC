# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.97 |
| node-hours | 4.162 | 4.157 |
| energy, parked workers still on at idle power (Wh, declared model) | 446.2 | 445.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.6 | 443.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 164 | 88.66 |
| response time (ms), 95th percentile | 317.9 | 118.5 |
| response time (ms), 99th percentile | 569.5 | 219.7 |
| time over the response line (% of samples) | 3.342 | 1.961 |
| failed requests (%) | 1.746 | 1.602 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.245 | 0.2983 |
| utilisation (used / allocatable) | 0.0497 | 0.04906 |
| CPU used (cores), mean | 1.187 | 1.172 |
| Omni's own CPU (cores), mean | 0 | 0.00903 |
| CPU used with Omni's own (cores), mean | 1.187 | 1.181 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 566.8 | 570.9 |
| HPA replicas, mean | 8.452 | 8.877 |
| pods started | 8.2 | 9.7 |
| pod start wait, total (s) | 12.5 | 16.1 |
| pod start wait, mean (s) | 1.522 | 1.683 |
| host CPU busy, the real machine under kind (%) | 36.05 | 35.71 |
| host cores (the real machine under kind) | 4 | 4 |
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
| worker nodes in service, mean | 5.97 | 5.97 | +0.0% | −0.0018 to +0.0031 | no |
| node-hours | 4.162 | 4.157 | −0.1% | −0.0143 to +0.0025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 446.2 | 445.1 | −0.2% | −1.9004 to −0.2380 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.6 | 443.6 | −0.2% | −1.8871 to −0.1804 | yes: GAIN |
| response time (ms), mean | 164 | 88.66 | −46.0% | −97.9663 to −52.7860 | yes: GAIN |
| response time (ms), 95th percentile | 317.9 | 118.5 | −62.7% | −241.6996 to −157.1554 | yes: GAIN |
| response time (ms), 99th percentile | 569.5 | 219.7 | −61.4% | −406.3235 to −293.3339 | yes: GAIN |
| time over the response line (% of samples) | 3.342 | 1.961 | −41.3% | −1.8280 to −0.9339 | yes: GAIN |
| failed requests (%) | 1.746 | 1.602 | −8.3% | −0.2486 to −0.0404 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 7.3 | −19.8% | −2.9081 to −0.6919 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49 | +49.000 (native is 0) | +41.1570 to +56.8430 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.245 | 0.2983 | +21.8% | −0.1673 to +0.2740 | no |
| utilisation (used / allocatable) | 0.0497 | 0.04906 | −1.3% | −0.0015 to +0.0002 | no |
| CPU used (cores), mean | 1.187 | 1.172 | −1.3% | −0.0348 to +0.0044 | no |
| Omni's own CPU (cores), mean | 0 | 0.00903 | +0.009 (native is 0) | +0.0078 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.187 | 1.181 | −0.5% | −0.0253 to +0.0130 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 566.8 | 570.9 | +0.7% | −3.2432 to +11.4375 | no |
| HPA replicas, mean | 8.452 | 8.877 | +5.0% | −0.1897 to +1.0394 | no |
| pods started | 8.2 | 9.7 | +18.3% | +0.0205 to +2.9795 | yes: power given |
| pod start wait, total (s) | 12.5 | 16.1 | +28.8% | +0.2927 to +6.9073 | yes: LOSS |
| pod start wait, mean (s) | 1.522 | 1.683 | +10.6% | −0.0603 to +0.3817 | no |
| host CPU busy, the real machine under kind (%) | 36.05 | 35.71 | −0.9% | −0.8071 to +0.1343 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 79 | 3.8 |  |
| machine down | omni | 44 | 1.5 | -35 s (-44%) |
| spike | native | 265 | 72.3 |  |
| spike | omni | 261 | 70.4 | -4 s (-1%) |
| runaway pod started | native | 4 | 0.4 |  |
| runaway pod started | omni | 3 | 0.0 | -2 s (-43%) |
| probe blind | native | 71 | 0.8 |  |
| probe blind | omni | 60 | 0.0 | -11 s (-16%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -0 s (-22%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*