# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.968 |
| node-hours | 4.162 | 4.162 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.5 | 443.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.9 | 441.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 151.3 | 82.45 |
| response time (ms), 95th percentile | 293.5 | 110.7 |
| response time (ms), 99th percentile | 636.4 | 257.1 |
| time over the response line (% of samples) | 3.056 | 1.655 |
| failed requests (%) | 1.431 | 1.235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4183 | 0.2417 |
| utilisation (used / allocatable) | 0.04576 | 0.04478 |
| CPU used (cores), mean | 1.093 | 1.069 |
| Omni's own CPU (cores), mean | 0 | 0.00802 |
| CPU used with Omni's own (cores), mean | 1.093 | 1.077 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 635.8 | 639 |
| HPA replicas, mean | 8.004 | 7.913 |
| pods started | 8.7 | 8.2 |
| pod start wait, total (s) | 13.1 | 14.3 |
| pod start wait, mean (s) | 1.512 | 1.722 |
| host CPU busy, the real machine under kind (%) | 33.29 | 32.8 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 5.969 | 5.968 | −0.0% | −0.0031 to +0.0007 | no |
| node-hours | 4.162 | 4.162 | +0.0% | −0.0059 to +0.0062 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.5 | 443.1 | −0.1% | −1.2906 to +0.5322 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.9 | 441.5 | −0.1% | −1.4166 to +0.5332 | no |
| response time (ms), mean | 151.3 | 82.45 | −45.5% | −97.2767 to −40.4682 | yes: GAIN |
| response time (ms), 95th percentile | 293.5 | 110.7 | −62.3% | −228.8078 to −136.7862 | yes: GAIN |
| response time (ms), 99th percentile | 636.4 | 257.1 | −59.6% | −440.3979 to −318.1303 | yes: GAIN |
| time over the response line (% of samples) | 3.056 | 1.655 | −45.9% | −1.9144 to −0.8891 | yes: GAIN |
| failed requests (%) | 1.431 | 1.235 | −13.7% | −0.3240 to −0.0680 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6 | −30.2% | −3.2911 to −1.9089 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.900 (native is 0) | +29.2474 to +46.5526 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4183 | 0.2417 | −42.2% | −0.6281 to +0.2748 | no |
| utilisation (used / allocatable) | 0.04576 | 0.04478 | −2.1% | −0.0021 to +0.0002 | no |
| CPU used (cores), mean | 1.093 | 1.069 | −2.2% | −0.0508 to +0.0037 | no |
| Omni's own CPU (cores), mean | 0 | 0.00802 | +0.008 (native is 0) | +0.0065 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.093 | 1.077 | −1.4% | −0.0415 to +0.0104 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 635.8 | 639 | +0.5% | −11.4088 to +17.8932 | no |
| HPA replicas, mean | 8.004 | 7.913 | −1.1% | −0.6329 to +0.4508 | no |
| pods started | 8.7 | 8.2 | −5.7% | −1.7274 to +0.7274 | no |
| pod start wait, total (s) | 13.1 | 14.3 | +9.2% | −3.4087 to +5.8087 | no |
| pod start wait, mean (s) | 1.512 | 1.722 | +13.9% | −0.1768 to +0.5965 | no |
| host CPU busy, the real machine under kind (%) | 33.29 | 32.8 | −1.5% | −1.1074 to +0.1245 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 59 | 3.7 |  |
| machine down | omni | 39 | 1.1 | -19 s (-33%) |
| spike | native | 239 | 63.2 |  |
| spike | omni | 220 | 55.9 | -18 s (-8%) |
| runaway pod started | native | 6 | 0.3 |  |
| runaway pod started | omni | 2 | 0.0 | -4 s (-61%) |
| probe blind | native | 62 | 1.1 |  |
| probe blind | omni | 60 | 0.0 | -2 s (-4%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-28%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*