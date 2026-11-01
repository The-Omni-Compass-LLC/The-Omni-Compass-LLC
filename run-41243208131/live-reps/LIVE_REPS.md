# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.914 |
| node-hours | 1.491 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 163.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.4 | 162.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 189.4 | 107 |
| response time (ms), 95th percentile | 445.4 | 206.4 |
| response time (ms), 99th percentile | 1602 | 608.2 |
| time over the response line (% of samples) | 6.989 | 4.415 |
| failed requests (%) | 3.389 | 2.949 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9633 | 0.4483 |
| utilisation (used / allocatable) | 0.06373 | 0.06284 |
| CPU used (cores), mean | 1.508 | 1.486 |
| Omni's own CPU (cores), mean | 0 | 0.00975 |
| CPU used with Omni's own (cores), mean | 1.508 | 1.496 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.1 | 450.8 |
| HPA replicas, mean | 8.224 | 9.8 |
| pods started | 5.8 | 7.1 |
| pod start wait, total (s) | 10.5 | 29.7 |
| pod start wait, mean (s) | 1.841 | 4.181 |
| host CPU busy, the real machine under kind (%) | 43.55 | 43.28 |
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
| worker nodes in service, mean | 5.915 | 5.914 | −0.0% | −0.0054 to +0.0028 | no |
| node-hours | 1.491 | 1.493 | +0.1% | −0.0047 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 163.9 | −0.0% | −0.7479 to +0.6238 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.4 | 162.3 | −0.1% | −0.8283 to +0.6500 | no |
| response time (ms), mean | 189.4 | 107 | −43.5% | −96.3133 to −68.4916 | yes: GAIN |
| response time (ms), 95th percentile | 445.4 | 206.4 | −53.7% | −293.4983 to −184.4607 | yes: GAIN |
| response time (ms), 99th percentile | 1602 | 608.2 | −62.0% | −1593.2846 to −394.7708 | yes: GAIN |
| time over the response line (% of samples) | 6.989 | 4.415 | −36.8% | −3.3916 to −1.7560 | yes: GAIN |
| failed requests (%) | 3.389 | 2.949 | −13.0% | −0.9424 to +0.0628 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 4.7 | −17.5% | −1.6744 to −0.3256 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 | +27.500 (native is 0) | +22.1551 to +32.8449 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9633 | 0.4483 | −53.5% | −1.3608 to +0.3308 | no |
| utilisation (used / allocatable) | 0.06373 | 0.06284 | −1.4% | −0.0029 to +0.0011 | no |
| CPU used (cores), mean | 1.508 | 1.486 | −1.4% | −0.0696 to +0.0267 | no |
| Omni's own CPU (cores), mean | 0 | 0.00975 | +0.010 (native is 0) | +0.0079 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.508 | 1.496 | −0.8% | −0.0586 to +0.0352 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.1 | 450.8 | −0.1% | −14.0386 to +13.5586 | no |
| HPA replicas, mean | 8.224 | 9.8 | +19.2% | +0.2621 to +2.8901 | yes: power given |
| pods started | 5.8 | 7.1 | +22.4% | −0.2471 to +2.8471 | no |
| pod start wait, total (s) | 10.5 | 29.7 | +182.9% | −5.4081 to +43.8081 | no |
| pod start wait, mean (s) | 1.841 | 4.181 | +127.1% | −1.2903 to +5.9694 | no |
| host CPU busy, the real machine under kind (%) | 43.55 | 43.28 | −0.6% | −1.2848 to +0.7436 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 54 | 14.5 |  |
| machine down | omni | 35 | 8.1 | -19 s (-35%) |
| spike | native | 222 | 48.4 |  |
| spike | omni | 209 | 35.4 | -13 s (-6%) |
| runaway pod started | native | 70 | 7.3 |  |
| runaway pod started | omni | 54 | 4.4 | -16 s (-23%) |
| probe blind | native | 58 | 0.2 |  |
| probe blind | omni | 60 | 0.0 | +2 s (+3%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*