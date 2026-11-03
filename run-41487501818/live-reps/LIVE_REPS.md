# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.971 | 5.969 |
| node-hours | 4.161 | 4.157 |
| energy, parked workers still on at idle power (Wh, declared model) | 447.2 | 446.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.7 | 444.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 185.9 | 101.5 |
| response time (ms), 95th percentile | 348.8 | 123.8 |
| response time (ms), 99th percentile | 813 | 244.3 |
| time over the response line (% of samples) | 3.774 | 2.174 |
| failed requests (%) | 1.766 | 1.689 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 71.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1833 | 0.1617 |
| utilisation (used / allocatable) | 0.05209 | 0.05104 |
| CPU used (cores), mean | 1.244 | 1.219 |
| Omni's own CPU (cores), mean | 0 | 0.04007 |
| CPU used with Omni's own (cores), mean | 1.244 | 1.259 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 544.8 | 552.9 |
| HPA replicas, mean | 8.572 | 9.868 |
| pods started | 7.8 | 10.8 |
| pod start wait, total (s) | 12 | 17.9 |
| pod start wait, mean (s) | 1.547 | 1.635 |
| host CPU busy, the real machine under kind (%) | 37.77 | 38.5 |
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
| worker nodes in service, mean | 5.971 | 5.969 | −0.0% | −0.0051 to +0.0012 | no |
| node-hours | 4.161 | 4.157 | −0.1% | −0.0101 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 447.2 | 446.4 | −0.2% | −1.7402 to +0.0428 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.7 | 444.8 | −0.2% | −1.8547 to −0.0468 | yes: GAIN |
| response time (ms), mean | 185.9 | 101.5 | −45.4% | −113.4957 to −55.4018 | yes: GAIN |
| response time (ms), 95th percentile | 348.8 | 123.8 | −64.5% | −265.1250 to −185.0180 | yes: GAIN |
| response time (ms), 99th percentile | 813 | 244.3 | −70.0% | −928.4779 to −208.9533 | yes: GAIN |
| time over the response line (% of samples) | 3.774 | 2.174 | −42.4% | −2.1266 to −1.0725 | yes: GAIN |
| failed requests (%) | 1.766 | 1.689 | −4.4% | −0.2299 to +0.0760 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 7.4 | −30.2% | −5.0096 to −1.3904 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63 | +63.000 (native is 0) | +51.9596 to +74.0404 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1833 | 0.1617 | −11.8% | −0.2929 to +0.2496 | no |
| utilisation (used / allocatable) | 0.05209 | 0.05104 | −2.0% | −0.0018 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.244 | 1.219 | −2.1% | −0.0429 to −0.0083 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04007 | +0.040 (native is 0) | +0.0352 to +0.0450 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.244 | 1.259 | +1.2% | −0.0006 to +0.0297 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 544.8 | 552.9 | +1.5% | +1.8812 to +14.3057 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.572 | 9.868 | +15.1% | +0.7459 to +1.8446 | yes: power given |
| pods started | 7.8 | 10.8 | +38.5% | +1.1841 to +4.8159 | yes: power given |
| pod start wait, total (s) | 12 | 17.9 | +49.2% | +1.1738 to +10.6262 | yes: LOSS |
| pod start wait, mean (s) | 1.547 | 1.635 | +5.7% | −0.1891 to +0.3648 | no |
| host CPU busy, the real machine under kind (%) | 37.77 | 38.5 | +1.9% | +0.1466 to +1.3104 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 85 | 4.9 |  |
| machine down | omni | 49 | 1.6 | -37 s (-43%) |
| spike | native | 271 | 79.3 |  |
| spike | omni | 270 | 77.1 | -0 s (-0%) |
| runaway pod started | native | 3 | 0.2 |  |
| runaway pod started | omni | 3 | 0.0 | -0 s (-12%) |
| probe blind | native | 65 | 1.9 |  |
| probe blind | omni | 60 | 0.1 | -4 s (-7%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -0 s (-10%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*