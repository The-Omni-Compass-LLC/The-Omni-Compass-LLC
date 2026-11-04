# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.968 |
| node-hours | 4.162 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.9 | 445.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.3 | 443.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 168.2 | 96.56 |
| response time (ms), 95th percentile | 320.8 | 118.1 |
| response time (ms), 99th percentile | 575.3 | 241.5 |
| time over the response line (% of samples) | 3.175 | 1.876 |
| failed requests (%) | 1.607 | 1.373 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 6.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.555 |
| utilisation (used / allocatable) | 0.0494 | 0.0486 |
| CPU used (cores), mean | 1.18 | 1.16 |
| Omni's own CPU (cores), mean | 0 | 0.03794 |
| CPU used with Omni's own (cores), mean | 1.18 | 1.198 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 562.8 | 569 |
| HPA replicas, mean | 8.517 | 8.991 |
| pods started | 8.3 | 11.9 |
| pod start wait, total (s) | 12.5 | 20 |
| pod start wait, mean (s) | 1.509 | 1.661 |
| host CPU busy, the real machine under kind (%) | 35.79 | 36.56 |
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
| worker nodes in service, mean | 5.969 | 5.968 | −0.0% | −0.0030 to +0.0005 | no |
| node-hours | 4.162 | 4.16 | −0.1% | −0.0093 to +0.0035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.9 | 445.4 | −0.1% | −1.3209 to +0.1610 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.3 | 443.7 | −0.1% | −1.3677 to +0.0744 | no |
| response time (ms), mean | 168.2 | 96.56 | −42.6% | −89.7438 to −53.4878 | yes: GAIN |
| response time (ms), 95th percentile | 320.8 | 118.1 | −63.2% | −240.9720 to −164.5650 | yes: GAIN |
| response time (ms), 99th percentile | 575.3 | 241.5 | −58.0% | −384.4677 to −283.2731 | yes: GAIN |
| time over the response line (% of samples) | 3.175 | 1.876 | −40.9% | −1.8595 to −0.7395 | yes: GAIN |
| failed requests (%) | 1.607 | 1.373 | −14.6% | −0.3674 to −0.1005 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 6.7 | −29.5% | −4.2621 to −1.3379 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.8 | +64.800 (native is 0) | +55.0398 to +74.5602 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.555 | +420.3% | −0.0920 to +0.9887 | no |
| utilisation (used / allocatable) | 0.0494 | 0.0486 | −1.6% | −0.0015 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.18 | 1.16 | −1.6% | −0.0359 to −0.0026 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03794 | +0.038 (native is 0) | +0.0333 to +0.0426 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.18 | 1.198 | +1.6% | +0.0044 to +0.0329 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 562.8 | 569 | +1.1% | −1.4358 to +13.6836 | no |
| HPA replicas, mean | 8.517 | 8.991 | +5.6% | −0.3294 to +1.2780 | no |
| pods started | 8.3 | 11.9 | +43.4% | +2.1615 to +5.0385 | yes: power given |
| pod start wait, total (s) | 12.5 | 20 | +60.0% | +4.2091 to +10.7909 | yes: LOSS |
| pod start wait, mean (s) | 1.509 | 1.661 | +10.1% | −0.0416 to +0.3472 | no |
| host CPU busy, the real machine under kind (%) | 35.79 | 36.56 | +2.1% | +0.3920 to +1.1391 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 57 | 4.1 |  |
| machine down | omni | 36 | 0.9 | -21 s (-37%) |
| spike | native | 265 | 68.0 |  |
| spike | omni | 262 | 66.3 | -4 s (-1%) |
| runaway pod started | native | 4 | 0.5 |  |
| runaway pod started | omni | 2 | 0.0 | -2 s (-50%) |
| probe blind | native | 78 | 1.3 |  |
| probe blind | omni | 60 | 0.0 | -19 s (-24%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -0 s (-2%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*