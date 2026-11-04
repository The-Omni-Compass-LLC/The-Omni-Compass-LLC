# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.97 |
| node-hours | 4.163 | 4.161 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.4 | 444.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.8 | 443.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 169.1 | 89.14 |
| response time (ms), 95th percentile | 312.9 | 112.1 |
| response time (ms), 99th percentile | 657.2 | 222.6 |
| time over the response line (% of samples) | 3.064 | 1.912 |
| failed requests (%) | 1.541 | 1.522 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.22 | 0.35 |
| utilisation (used / allocatable) | 0.04831 | 0.04761 |
| CPU used (cores), mean | 1.154 | 1.137 |
| Omni's own CPU (cores), mean | 0 | 0.03702 |
| CPU used with Omni's own (cores), mean | 1.154 | 1.174 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 570.2 | 576.1 |
| HPA replicas, mean | 8.484 | 8.768 |
| pods started | 8.7 | 11.9 |
| pod start wait, total (s) | 13 | 19.3 |
| pod start wait, mean (s) | 1.524 | 1.599 |
| host CPU busy, the real machine under kind (%) | 35.11 | 35.87 |
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
| worker nodes in service, mean | 5.97 | 5.97 | −0.0% | −0.0021 to +0.0020 | no |
| node-hours | 4.163 | 4.161 | −0.1% | −0.0068 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.4 | 444.8 | −0.1% | −1.4298 to +0.2736 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.8 | 443.2 | −0.1% | −1.3905 to +0.2302 | no |
| response time (ms), mean | 169.1 | 89.14 | −47.3% | −107.5015 to −52.4997 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 112.1 | −64.2% | −236.9380 to −164.5180 | yes: GAIN |
| response time (ms), 99th percentile | 657.2 | 222.6 | −66.1% | −548.4879 to −320.7179 | yes: GAIN |
| time over the response line (% of samples) | 3.064 | 1.912 | −37.6% | −1.7225 to −0.5811 | yes: GAIN |
| failed requests (%) | 1.541 | 1.522 | −1.2% | −0.1364 to +0.0980 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 7.1 | −22.0% | −3.3903 to −0.6097 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.8 | +61.800 (native is 0) | +54.3145 to +69.2855 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.22 | 0.35 | +59.1% | −0.1954 to +0.4554 | no |
| utilisation (used / allocatable) | 0.04831 | 0.04761 | −1.4% | −0.0015 to +0.0001 | no |
| CPU used (cores), mean | 1.154 | 1.137 | −1.4% | −0.0358 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0 | 0.03702 | +0.037 (native is 0) | +0.0331 to +0.0410 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.154 | 1.174 | +1.8% | +0.0025 to +0.0383 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 570.2 | 576.1 | +1.0% | −1.4080 to +13.2526 | no |
| HPA replicas, mean | 8.484 | 8.768 | +3.4% | −0.5033 to +1.0721 | no |
| pods started | 8.7 | 11.9 | +36.8% | +2.1997 to +4.2003 | yes: power given |
| pod start wait, total (s) | 13 | 19.3 | +48.5% | +2.6519 to +9.9481 | yes: LOSS |
| pod start wait, mean (s) | 1.524 | 1.599 | +4.9% | −0.2090 to +0.3591 | no |
| host CPU busy, the real machine under kind (%) | 35.11 | 35.87 | +2.2% | +0.4363 to +1.0972 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 65 | 4.0 |  |
| machine down | omni | 50 | 1.7 | -15 s (-23%) |
| spike | native | 255 | 59.0 |  |
| spike | omni | 257 | 60.5 | +2 s (+1%) |
| runaway pod started | native | 3 | 0.2 |  |
| runaway pod started | omni | 3 | 0.0 | +0 s (+17%) |
| probe blind | native | 67 | 1.2 |  |
| probe blind | omni | 60 | 0.0 | -7 s (-11%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+14%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*