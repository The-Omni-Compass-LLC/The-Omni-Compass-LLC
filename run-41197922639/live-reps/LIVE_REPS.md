# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.969 |
| node-hours | 4.162 | 4.157 |
| energy, parked workers still on at idle power (Wh, declared model) | 444.2 | 443.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.7 | 441.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 155.4 | 86.22 |
| response time (ms), 95th percentile | 306.1 | 111.5 |
| response time (ms), 99th percentile | 572.2 | 266.1 |
| time over the response line (% of samples) | 3.074 | 1.742 |
| failed requests (%) | 1.433 | 1.237 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4817 | 0.535 |
| utilisation (used / allocatable) | 0.04694 | 0.04603 |
| CPU used (cores), mean | 1.121 | 1.099 |
| Omni's own CPU (cores), mean | 0 | 0.00869 |
| CPU used with Omni's own (cores), mean | 1.121 | 1.108 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 603.8 | 611.7 |
| HPA replicas, mean | 8.156 | 8.107 |
| pods started | 8.8 | 10.4 |
| pod start wait, total (s) | 13.9 | 19 |
| pod start wait, mean (s) | 1.588 | 1.801 |
| host CPU busy, the real machine under kind (%) | 34.22 | 33.92 |
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
| worker nodes in service, mean | 5.97 | 5.969 | −0.0% | −0.0034 to +0.0019 | no |
| node-hours | 4.162 | 4.157 | −0.1% | −0.0132 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 444.2 | 443.3 | −0.2% | −1.7738 to −0.0974 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.7 | 441.7 | −0.2% | −1.8493 to −0.0969 | yes: GAIN |
| response time (ms), mean | 155.4 | 86.22 | −44.5% | −94.2678 to −44.1240 | yes: GAIN |
| response time (ms), 95th percentile | 306.1 | 111.5 | −63.6% | −236.7099 to −152.4771 | yes: GAIN |
| response time (ms), 99th percentile | 572.2 | 266.1 | −53.5% | −434.4851 to −177.7071 | yes: GAIN |
| time over the response line (% of samples) | 3.074 | 1.742 | −43.3% | −1.8810 to −0.7838 | yes: GAIN |
| failed requests (%) | 1.433 | 1.237 | −13.7% | −0.3600 to −0.0317 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 6.3 | −28.4% | −3.7274 to −1.2726 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.6 | +46.600 (native is 0) | +37.2055 to +55.9945 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4817 | 0.535 | +11.1% | −0.3136 to +0.4202 | no |
| utilisation (used / allocatable) | 0.04694 | 0.04603 | −1.9% | −0.0016 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.121 | 1.099 | −2.0% | −0.0385 to −0.0053 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00869 | +0.009 (native is 0) | +0.0073 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.121 | 1.108 | −1.2% | −0.0292 to +0.0028 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 603.8 | 611.7 | +1.3% | −1.2816 to +17.0538 | no |
| HPA replicas, mean | 8.156 | 8.107 | −0.6% | −0.7927 to +0.6941 | no |
| pods started | 8.8 | 10.4 | +18.2% | −0.2531 to +3.4531 | no |
| pod start wait, total (s) | 13.9 | 19 | +36.7% | +0.2199 to +9.9801 | yes: LOSS |
| pod start wait, mean (s) | 1.588 | 1.801 | +13.4% | −0.0258 to +0.4513 | no |
| host CPU busy, the real machine under kind (%) | 34.22 | 33.92 | −0.9% | −0.8009 to +0.1925 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 81 | 3.9 |  |
| machine down | omni | 26 | 0.8 | -55 s (-68%) |
| spike | native | 255 | 59.2 |  |
| spike | omni | 237 | 60.4 | -18 s (-7%) |
| runaway pod started | native | 4 | 0.4 |  |
| runaway pod started | omni | 2 | 0.0 | -2 s (-48%) |
| probe blind | native | 83 | 1.1 |  |
| probe blind | omni | 60 | 0.0 | -23 s (-27%) |
| metrics down | native | 1 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+13%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*