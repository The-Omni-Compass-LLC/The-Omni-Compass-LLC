# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.913 |
| node-hours | 1.495 | 1.499 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.9 | 166.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.2 | 164.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 234.8 | 134.6 |
| response time (ms), 95th percentile | 429.8 | 181.5 |
| response time (ms), 99th percentile | 1393 | 866.9 |
| time over the response line (% of samples) | 8.673 | 6.016 |
| failed requests (%) | 5.42 | 4.953 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9217 | 0.61 |
| utilisation (used / allocatable) | 0.07478 | 0.07174 |
| CPU used (cores), mean | 1.769 | 1.697 |
| Omni's own CPU (cores), mean | 0 | 0.01192 |
| CPU used with Omni's own (cores), mean | 1.769 | 1.709 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 377.7 | 390.2 |
| HPA replicas, mean | 8.794 | 11.2 |
| pods started | 4.8 | 7 |
| pod start wait, total (s) | 16.4 | 14.9 |
| pod start wait, mean (s) | 2.872 | 2.057 |
| host CPU busy, the real machine under kind (%) | 50.68 | 49.49 |
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
| worker nodes in service, mean | 5.913 | 5.913 | +0.0% | −0.0001 to +0.0008 | no |
| node-hours | 1.495 | 1.499 | +0.3% | +0.0023 to +0.0055 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 166.9 | 166.6 | −0.2% | −0.6372 to +0.0623 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.2 | 164.9 | −0.2% | −0.6336 to +0.0628 | no |
| response time (ms), mean | 234.8 | 134.6 | −42.7% | −147.6500 to −52.9350 | yes: GAIN |
| response time (ms), 95th percentile | 429.8 | 181.5 | −57.8% | −279.5881 to −217.0529 | yes: GAIN |
| response time (ms), 99th percentile | 1393 | 866.9 | −37.8% | −896.9097 to −154.6239 | yes: GAIN |
| time over the response line (% of samples) | 8.673 | 6.016 | −30.6% | −3.8731 to −1.4422 | yes: GAIN |
| failed requests (%) | 5.42 | 4.953 | −8.6% | −1.1224 to +0.1873 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 6 | −16.7% | −2.1417 to −0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.5 | +28.500 (native is 0) | +22.7256 to +34.2744 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9217 | 0.61 | −33.8% | −0.9356 to +0.3123 | no |
| utilisation (used / allocatable) | 0.07478 | 0.07174 | −4.1% | −0.0047 to −0.0014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.769 | 1.697 | −4.1% | −0.1106 to −0.0331 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01192 | +0.012 (native is 0) | +0.0105 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.769 | 1.709 | −3.4% | −0.0975 to −0.0223 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 377.7 | 390.2 | +3.3% | +5.8466 to +19.0180 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.794 | 11.2 | +27.3% | +1.3365 to +3.4684 | yes: power given |
| pods started | 4.8 | 7 | +45.8% | +0.3904 to +4.0096 | yes: power given |
| pod start wait, total (s) | 16.4 | 14.9 | −9.1% | −22.3062 to +19.3062 | no |
| pod start wait, mean (s) | 2.872 | 2.057 | −28.4% | −3.5765 to +1.9459 | no |
| host CPU busy, the real machine under kind (%) | 50.68 | 49.49 | −2.4% | −2.0556 to −0.3269 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 61 | 14.5 |  |
| machine down | omni | 49 | 10.6 | -12 s (-20%) |
| spike | native | 275 | 75.9 |  |
| spike | omni | 271 | 62.2 | -3 s (-1%) |
| runaway pod started | native | 133 | 12.9 |  |
| runaway pod started | omni | 94 | 7.5 | -39 s (-29%) |
| probe blind | native | 71 | 0.8 |  |
| probe blind | omni | 60 | 0.1 | -10 s (-15%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*