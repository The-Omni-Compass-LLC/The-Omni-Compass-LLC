# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.969 |
| node-hours | 4.158 | 4.158 |
| energy, parked workers still on at idle power (Wh, declared model) | 438.4 | 438.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 436.8 | 436.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 119.9 | 74.13 |
| response time (ms), 95th percentile | 244.6 | 91.22 |
| response time (ms), 99th percentile | 566.6 | 514.7 |
| time over the response line (% of samples) | 2.052 | 1.515 |
| failed requests (%) | 0.6993 | 0.6837 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2117 |
| utilisation (used / allocatable) | 0.03793 | 0.03764 |
| CPU used (cores), mean | 0.9057 | 0.8988 |
| Omni's own CPU (cores), mean | 0 | 0.03025 |
| CPU used with Omni's own (cores), mean | 0.9057 | 0.929 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.2 | 738.6 |
| HPA replicas, mean | 7.389 | 7.248 |
| pods started | 9.8 | 11.9 |
| pod start wait, total (s) | 15.8 | 19.2 |
| pod start wait, mean (s) | 1.626 | 1.626 |
| host CPU busy, the real machine under kind (%) | 27.91 | 28.81 |
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
| worker nodes in service, mean | 5.969 | 5.969 | −0.0% | −0.0022 to +0.0020 | no |
| node-hours | 4.158 | 4.158 | +0.0% | −0.0085 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 438.4 | 438.3 | −0.0% | −1.2807 to +1.1068 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 436.8 | 436.7 | −0.0% | −1.2126 to +1.0262 | no |
| response time (ms), mean | 119.9 | 74.13 | −38.2% | −73.6926 to −17.9457 | yes: GAIN |
| response time (ms), 95th percentile | 244.6 | 91.22 | −62.7% | −183.3672 to −123.4838 | yes: GAIN |
| response time (ms), 99th percentile | 566.6 | 514.7 | −9.2% | −324.6046 to +220.9164 | no |
| time over the response line (% of samples) | 2.052 | 1.515 | −26.1% | −1.1206 to +0.0478 | no |
| failed requests (%) | 0.6993 | 0.6837 | −2.2% | −0.1298 to +0.0985 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 4.7 | −17.5% | −2.3060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.1 | +54.100 (native is 0) | +47.8874 to +60.3126 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2117 | −0.8% | −0.3051 to +0.3017 | no |
| utilisation (used / allocatable) | 0.03793 | 0.03764 | −0.8% | −0.0011 to +0.0005 | no |
| CPU used (cores), mean | 0.9057 | 0.8988 | −0.8% | −0.0259 to +0.0121 | no |
| Omni's own CPU (cores), mean | 0 | 0.03025 | +0.030 (native is 0) | +0.0258 to +0.0347 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9057 | 0.929 | +2.6% | +0.0070 to +0.0396 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.2 | 738.6 | −0.1% | −16.9421 to +15.5913 | no |
| HPA replicas, mean | 7.389 | 7.248 | −1.9% | −0.6656 to +0.3847 | no |
| pods started | 9.8 | 11.9 | +21.4% | +0.5023 to +3.6977 | yes: power given |
| pod start wait, total (s) | 15.8 | 19.2 | +21.5% | −1.5236 to +8.3236 | no |
| pod start wait, mean (s) | 1.626 | 1.626 | −0.0% | −0.3260 to +0.3256 | no |
| host CPU busy, the real machine under kind (%) | 27.91 | 28.81 | +3.2% | +0.3564 to +1.4476 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 41 | 2.0 |  |
| machine down | omni | 37 | 1.1 | -4 s (-11%) |
| spike | native | 193 | 31.7 |  |
| spike | omni | 185 | 32.0 | -8 s (-4%) |
| runaway pod started | native | 3 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | -2 s (-49%) |
| probe blind | native | 60 | 0.6 |  |
| probe blind | omni | 60 | 0.0 | +0 s (+0%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+8%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*