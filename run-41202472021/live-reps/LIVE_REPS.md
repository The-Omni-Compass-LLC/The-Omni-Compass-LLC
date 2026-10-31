# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.97 |
| node-hours | 4.164 | 4.158 |
| energy, parked workers still on at idle power (Wh, declared model) | 446.8 | 445.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.2 | 444 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 163.3 | 90.8 |
| response time (ms), 95th percentile | 326.5 | 119.9 |
| response time (ms), 99th percentile | 564.9 | 214.8 |
| time over the response line (% of samples) | 3.131 | 1.998 |
| failed requests (%) | 1.67 | 1.599 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 7.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.165 | 0.2417 |
| utilisation (used / allocatable) | 0.05051 | 0.04938 |
| CPU used (cores), mean | 1.206 | 1.179 |
| Omni's own CPU (cores), mean | 0 | 0.00875 |
| CPU used with Omni's own (cores), mean | 1.206 | 1.188 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 549.5 | 560 |
| HPA replicas, mean | 8.645 | 8.831 |
| pods started | 8.2 | 9.7 |
| pod start wait, total (s) | 12.7 | 16.9 |
| pod start wait, mean (s) | 1.552 | 1.737 |
| host CPU busy, the real machine under kind (%) | 36.52 | 36 |
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
| worker nodes in service, mean | 5.97 | 5.97 | +0.0% | −0.0028 to +0.0039 | no |
| node-hours | 4.164 | 4.158 | −0.1% | −0.0137 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 446.8 | 445.5 | −0.3% | −2.1789 to −0.3022 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.2 | 444 | −0.3% | −2.1683 to −0.2503 | yes: GAIN |
| response time (ms), mean | 163.3 | 90.8 | −44.4% | −85.6150 to −59.3525 | yes: GAIN |
| response time (ms), 95th percentile | 326.5 | 119.9 | −63.3% | −237.5301 to −175.6509 | yes: GAIN |
| response time (ms), 99th percentile | 564.9 | 214.8 | −62.0% | −395.9467 to −304.1339 | yes: GAIN |
| time over the response line (% of samples) | 3.131 | 1.998 | −36.2% | −1.5208 to −0.7466 | yes: GAIN |
| failed requests (%) | 1.67 | 1.599 | −4.2% | −0.2848 to +0.1438 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 7.5 | −17.6% | −2.6769 to −0.5231 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 | +47.700 (native is 0) | +40.1446 to +55.2554 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.165 | 0.2417 | +46.5% | −0.2394 to +0.3927 | no |
| utilisation (used / allocatable) | 0.05051 | 0.04938 | −2.2% | −0.0019 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.206 | 1.179 | −2.2% | −0.0462 to −0.0075 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00875 | +0.009 (native is 0) | +0.0076 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.206 | 1.188 | −1.5% | −0.0371 to +0.0010 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 549.5 | 560 | +1.9% | +3.8377 to +17.1313 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.645 | 8.831 | +2.2% | −0.3811 to +0.7530 | no |
| pods started | 8.2 | 9.7 | +18.3% | +0.3198 to +2.6802 | yes: power given |
| pod start wait, total (s) | 12.7 | 16.9 | +33.1% | +1.2642 to +7.1358 | yes: LOSS |
| pod start wait, mean (s) | 1.552 | 1.737 | +12.0% | −0.0345 to +0.4054 | no |
| host CPU busy, the real machine under kind (%) | 36.52 | 36 | −1.4% | −0.8952 to −0.1429 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 57 | 3.3 |  |
| machine down | omni | 51 | 1.7 | -6 s (-10%) |
| spike | native | 268 | 68.9 |  |
| spike | omni | 253 | 64.6 | -16 s (-6%) |
| runaway pod started | native | 5 | 0.3 |  |
| runaway pod started | omni | 3 | 0.0 | -2 s (-36%) |
| probe blind | native | 70 | 1.2 |  |
| probe blind | omni | 54 | 0.0 | -16 s (-22%) |
| metrics down | native | 1 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+30%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*