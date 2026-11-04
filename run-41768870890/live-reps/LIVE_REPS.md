# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.913 |
| node-hours | 1.491 | 1.497 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 166.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 164.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 238.4 | 119.2 |
| response time (ms), 95th percentile | 400.1 | 205.9 |
| response time (ms), 99th percentile | 1843 | 697.5 |
| time over the response line (% of samples) | 8.518 | 6.014 |
| failed requests (%) | 5.266 | 4.672 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.013 | 0.69 |
| utilisation (used / allocatable) | 0.07255 | 0.07083 |
| CPU used (cores), mean | 1.716 | 1.675 |
| Omni's own CPU (cores), mean | 0 | 0.04555 |
| CPU used with Omni's own (cores), mean | 1.716 | 1.721 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 390.8 | 396.8 |
| HPA replicas, mean | 8.594 | 11.3 |
| pods started | 5.4 | 9 |
| pod start wait, total (s) | 8.5 | 16.8 |
| pod start wait, mean (s) | 1.553 | 1.827 |
| host CPU busy, the real machine under kind (%) | 49.03 | 49.97 |
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
| worker nodes in service, mean | 5.914 | 5.913 | −0.0% | −0.0049 to +0.0028 | no |
| node-hours | 1.491 | 1.497 | +0.4% | +0.0042 to +0.0084 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 166.2 | +0.2% | −0.0790 to +0.8333 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 164.5 | +0.2% | −0.0875 to +0.7877 | no |
| response time (ms), mean | 238.4 | 119.2 | −50.0% | −182.4579 to −55.8941 | yes: GAIN |
| response time (ms), 95th percentile | 400.1 | 205.9 | −48.5% | −280.2873 to −108.2357 | yes: GAIN |
| response time (ms), 99th percentile | 1843 | 697.5 | −62.2% | −2540.9198 to +249.1262 | no |
| time over the response line (% of samples) | 8.518 | 6.014 | −29.4% | −3.6860 to −1.3222 | yes: GAIN |
| failed requests (%) | 5.266 | 4.672 | −11.3% | −0.9581 to −0.2302 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 5.9 | −21.3% | −2.3689 to −0.8311 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.6 | +44.600 (native is 0) | +38.6324 to +50.5676 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.013 | 0.69 | −31.9% | −0.8897 to +0.2430 | no |
| utilisation (used / allocatable) | 0.07255 | 0.07083 | −2.4% | −0.0037 to +0.0003 | no |
| CPU used (cores), mean | 1.716 | 1.675 | −2.4% | −0.0877 to +0.0064 | no |
| Omni's own CPU (cores), mean | 0 | 0.04555 | +0.046 (native is 0) | +0.0412 to +0.0499 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.716 | 1.721 | +0.3% | −0.0394 to +0.0492 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 390.8 | 396.8 | +1.5% | −3.0591 to +14.9976 | no |
| HPA replicas, mean | 8.594 | 11.3 | +31.4% | +1.9208 to +3.4825 | yes: power given |
| pods started | 5.4 | 9 | +66.7% | +2.3749 to +4.8251 | yes: power given |
| pod start wait, total (s) | 8.5 | 16.8 | +97.6% | +3.1413 to +13.4587 | yes: LOSS |
| pod start wait, mean (s) | 1.553 | 1.827 | +17.6% | −0.1529 to +0.7011 | no |
| host CPU busy, the real machine under kind (%) | 49.03 | 49.97 | +1.9% | −0.0517 to +1.9296 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 72 | 15.7 |  |
| machine down | omni | 49 | 9.7 | -23 s (-32%) |
| spike | native | 266 | 67.4 |  |
| spike | omni | 266 | 59.2 | +0 s (+0%) |
| runaway pod started | native | 143 | 12.1 |  |
| runaway pod started | omni | 96 | 9.0 | -47 s (-33%) |
| probe blind | native | 64 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | -4 s (-6%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*