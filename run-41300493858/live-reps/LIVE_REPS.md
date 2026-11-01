# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.969 |
| node-hours | 4.165 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.2 | 442.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.6 | 440.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 144.5 | 81.45 |
| response time (ms), 95th percentile | 290.4 | 107.6 |
| response time (ms), 99th percentile | 606.6 | 222.7 |
| time over the response line (% of samples) | 2.813 | 1.601 |
| failed requests (%) | 1.295 | 1.236 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.2383 |
| utilisation (used / allocatable) | 0.0446 | 0.04375 |
| CPU used (cores), mean | 1.065 | 1.045 |
| Omni's own CPU (cores), mean | 0 | 0.00789 |
| CPU used with Omni's own (cores), mean | 1.065 | 1.052 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 640.2 | 645.2 |
| HPA replicas, mean | 7.902 | 7.673 |
| pods started | 8.1 | 8.1 |
| pod start wait, total (s) | 12.5 | 12.9 |
| pod start wait, mean (s) | 1.537 | 1.577 |
| host CPU busy, the real machine under kind (%) | 32.53 | 32.28 |
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
| worker nodes in service, mean | 5.97 | 5.969 | −0.0% | −0.0021 to +0.0007 | no |
| node-hours | 4.165 | 4.16 | −0.1% | −0.0154 to +0.0046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.2 | 442.2 | −0.2% | −2.0753 to +0.1627 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.6 | 440.6 | −0.2% | −2.1294 to +0.1501 | no |
| response time (ms), mean | 144.5 | 81.45 | −43.6% | −79.8363 to −46.1697 | yes: GAIN |
| response time (ms), 95th percentile | 290.4 | 107.6 | −62.9% | −227.3765 to −138.1425 | yes: GAIN |
| response time (ms), 99th percentile | 606.6 | 222.7 | −63.3% | −457.1217 to −310.6965 | yes: GAIN |
| time over the response line (% of samples) | 2.813 | 1.601 | −43.1% | −1.6143 to −0.8079 | yes: GAIN |
| failed requests (%) | 1.295 | 1.236 | −4.5% | −0.1651 to +0.0476 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6.1 | −19.7% | −2.4685 to −0.5315 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.8 | +36.800 (native is 0) | +29.3373 to +44.2627 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.2383 | −25.5% | −0.3365 to +0.1732 | no |
| utilisation (used / allocatable) | 0.0446 | 0.04375 | −1.9% | −0.0018 to +0.0001 | no |
| CPU used (cores), mean | 1.065 | 1.045 | −1.9% | −0.0435 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0 | 0.00789 | +0.008 (native is 0) | +0.0067 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.065 | 1.052 | −1.2% | −0.0347 to +0.0096 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 640.2 | 645.2 | +0.8% | −11.3622 to +21.2730 | no |
| HPA replicas, mean | 7.902 | 7.673 | −2.9% | −0.8248 to +0.3670 | no |
| pods started | 8.1 | 8.1 | ±0.0% | −1.9949 to +1.9949 | no |
| pod start wait, total (s) | 12.5 | 12.9 | +3.2% | −4.1139 to +4.9139 | no |
| pod start wait, mean (s) | 1.537 | 1.577 | +2.6% | −0.2784 to +0.3587 | no |
| host CPU busy, the real machine under kind (%) | 32.53 | 32.28 | −0.8% | −0.9478 to +0.4486 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 52 | 2.9 |  |
| machine down | omni | 41 | 1.4 | -11 s (-22%) |
| spike | native | 235 | 57.2 |  |
| spike | omni | 213 | 51.7 | -22 s (-9%) |
| runaway pod started | native | 4 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | -1 s (-30%) |
| probe blind | native | 58 | 0.9 |  |
| probe blind | omni | 60 | 0.0 | +2 s (+4%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-34%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*