# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.915 |
| node-hours | 1.49 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.4 | 164 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 162.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 209.2 | 116.1 |
| response time (ms), 95th percentile | 387.3 | 187.8 |
| response time (ms), 99th percentile | 1229 | 638.6 |
| time over the response line (% of samples) | 7.129 | 5.162 |
| failed requests (%) | 4.097 | 3.71 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.55 | 0.62 |
| utilisation (used / allocatable) | 0.06625 | 0.06485 |
| CPU used (cores), mean | 1.567 | 1.534 |
| Omni's own CPU (cores), mean | 0 | 0.04183 |
| CPU used with Omni's own (cores), mean | 1.567 | 1.576 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.1 | 432 |
| HPA replicas, mean | 8.468 | 10.45 |
| pods started | 5.7 | 9.9 |
| pod start wait, total (s) | 7.9 | 27 |
| pod start wait, mean (s) | 1.382 | 2.653 |
| host CPU busy, the real machine under kind (%) | 45.29 | 46.15 |
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
| worker nodes in service, mean | 5.913 | 5.915 | +0.0% | −0.0022 to +0.0054 | no |
| node-hours | 1.49 | 1.489 | −0.1% | −0.0072 to +0.0057 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.4 | 164 | −0.3% | −1.2128 to +0.3581 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 162.4 | −0.2% | −1.1902 to +0.3979 | no |
| response time (ms), mean | 209.2 | 116.1 | −44.5% | −118.4802 to −67.6198 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 187.8 | −51.5% | −238.1999 to −160.8191 | yes: GAIN |
| response time (ms), 99th percentile | 1229 | 638.6 | −48.0% | −1072.2365 to −108.4557 | yes: GAIN |
| time over the response line (% of samples) | 7.129 | 5.162 | −27.6% | −2.5958 to −1.3376 | yes: GAIN |
| failed requests (%) | 4.097 | 3.71 | −9.4% | −0.6550 to −0.1193 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5.2 | −11.9% | −1.1828 to −0.2172 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 | +44.400 (native is 0) | +37.9296 to +50.8704 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.55 | 0.62 | +12.7% | −0.3529 to +0.4929 | no |
| utilisation (used / allocatable) | 0.06625 | 0.06485 | −2.1% | −0.0030 to +0.0002 | no |
| CPU used (cores), mean | 1.567 | 1.534 | −2.1% | −0.0703 to +0.0046 | no |
| Omni's own CPU (cores), mean | 0 | 0.04183 | +0.042 (native is 0) | +0.0357 to +0.0479 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.576 | +0.6% | −0.0242 to +0.0421 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.1 | 432 | +1.4% | −3.3737 to +15.3507 | no |
| HPA replicas, mean | 8.468 | 10.45 | +23.5% | +1.1114 to +2.8615 | yes: power given |
| pods started | 5.7 | 9.9 | +73.7% | +2.9028 to +5.4972 | yes: power given |
| pod start wait, total (s) | 7.9 | 27 | +241.8% | +0.7344 to +37.4656 | yes: LOSS |
| pod start wait, mean (s) | 1.382 | 2.653 | +91.9% | −0.3456 to +2.8868 | no |
| host CPU busy, the real machine under kind (%) | 45.29 | 46.15 | +1.9% | +0.1716 to +1.5503 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 59 | 15.1 |  |
| machine down | omni | 38 | 10.1 | -21 s (-36%) |
| spike | native | 235 | 48.2 |  |
| spike | omni | 233 | 40.4 | -2 s (-1%) |
| runaway pod started | native | 71 | 6.8 |  |
| runaway pod started | omni | 62 | 5.1 | -10 s (-14%) |
| probe blind | native | 65 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | -5 s (-8%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*