# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.918 | 5.915 |
| node-hours | 1.492 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 164.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 163.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 239.7 | 124.8 |
| response time (ms), 95th percentile | 452.2 | 221.6 |
| response time (ms), 99th percentile | 2404 | 1057 |
| time over the response line (% of samples) | 8.126 | 5.874 |
| failed requests (%) | 4.436 | 4.112 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.307 | 0.745 |
| utilisation (used / allocatable) | 0.06847 | 0.06757 |
| CPU used (cores), mean | 1.621 | 1.599 |
| Omni's own CPU (cores), mean | 0 | 0.04335 |
| CPU used with Omni's own (cores), mean | 1.621 | 1.642 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.6 | 424.8 |
| HPA replicas, mean | 8.467 | 11.09 |
| pods started | 5.4 | 10 |
| pod start wait, total (s) | 23.3 | 19.1 |
| pod start wait, mean (s) | 4.873 | 1.918 |
| host CPU busy, the real machine under kind (%) | 46.8 | 48.09 |
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
| worker nodes in service, mean | 5.918 | 5.915 | −0.1% | −0.0086 to +0.0018 | no |
| node-hours | 1.492 | 1.492 | −0.0% | −0.0075 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 164.9 | −0.0% | −0.9691 to +0.8613 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 163.3 | −0.1% | −1.0256 to +0.7886 | no |
| response time (ms), mean | 239.7 | 124.8 | −47.9% | −166.6590 to −63.1272 | yes: GAIN |
| response time (ms), 95th percentile | 452.2 | 221.6 | −51.0% | −280.1643 to −181.0997 | yes: GAIN |
| response time (ms), 99th percentile | 2404 | 1057 | −56.0% | −2838.8971 to +144.7237 | no |
| time over the response line (% of samples) | 8.126 | 5.874 | −27.7% | −3.2675 to −1.2379 | yes: GAIN |
| failed requests (%) | 4.436 | 4.112 | −7.3% | −0.7641 to +0.1162 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.8 | −18.3% | −2.6509 to +0.0509 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 | +44.400 (native is 0) | +40.0398 to +48.7602 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.307 | 0.745 | −43.0% | −1.2626 to +0.1393 | no |
| utilisation (used / allocatable) | 0.06847 | 0.06757 | −1.3% | −0.0020 to +0.0002 | no |
| CPU used (cores), mean | 1.621 | 1.599 | −1.4% | −0.0477 to +0.0033 | no |
| Omni's own CPU (cores), mean | 0 | 0.04335 | +0.043 (native is 0) | +0.0367 to +0.0500 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.621 | 1.642 | +1.3% | −0.0042 to +0.0465 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.6 | 424.8 | +1.5% | −0.7772 to +13.1537 | no |
| HPA replicas, mean | 8.467 | 11.09 | +31.0% | +1.7376 to +3.5059 | yes: power given |
| pods started | 5.4 | 10 | +85.2% | +3.5772 to +5.6228 | yes: power given |
| pod start wait, total (s) | 23.3 | 19.1 | −18.0% | −26.9523 to +18.5523 | no |
| pod start wait, mean (s) | 4.873 | 1.918 | −60.6% | −7.8312 to +1.9211 | no |
| host CPU busy, the real machine under kind (%) | 46.8 | 48.09 | +2.8% | +0.6158 to +1.9606 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 63 | 16.3 |  |
| machine down | omni | 42 | 9.9 | -21 s (-33%) |
| spike | native | 247 | 61.3 |  |
| spike | omni | 246 | 52.2 | -1 s (-0%) |
| runaway pod started | native | 93 | 9.9 |  |
| runaway pod started | omni | 89 | 9.0 | -4 s (-4%) |
| probe blind | native | 58 | 0.6 |  |
| probe blind | omni | 60 | 0.0 | +2 s (+3%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*