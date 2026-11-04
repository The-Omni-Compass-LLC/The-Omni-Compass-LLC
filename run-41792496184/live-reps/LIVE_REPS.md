# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.971 | 5.97 |
| node-hours | 4.163 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 446.3 | 445.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.8 | 444.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 163.8 | 100.7 |
| response time (ms), 95th percentile | 335.5 | 121 |
| response time (ms), 99th percentile | 654.8 | 296.2 |
| time over the response line (% of samples) | 3.584 | 2.154 |
| failed requests (%) | 1.654 | 1.595 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 65 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.5933 |
| utilisation (used / allocatable) | 0.04996 | 0.04966 |
| CPU used (cores), mean | 1.193 | 1.186 |
| Omni's own CPU (cores), mean | 0 | 0.03791 |
| CPU used with Omni's own (cores), mean | 1.193 | 1.224 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 554.4 | 557.4 |
| HPA replicas, mean | 8.628 | 9.341 |
| pods started | 8.8 | 12.2 |
| pod start wait, total (s) | 14.6 | 24 |
| pod start wait, mean (s) | 1.671 | 1.933 |
| host CPU busy, the real machine under kind (%) | 36.29 | 37.05 |
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
| worker nodes in service, mean | 5.971 | 5.97 | −0.0% | −0.0048 to +0.0032 | no |
| node-hours | 4.163 | 4.159 | −0.1% | −0.0136 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 446.3 | 445.7 | −0.1% | −1.7935 to +0.5596 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.8 | 444.1 | −0.1% | −1.8232 to +0.5060 | no |
| response time (ms), mean | 163.8 | 100.7 | −38.5% | −81.5153 to −44.6742 | yes: GAIN |
| response time (ms), 95th percentile | 335.5 | 121 | −63.9% | −245.8656 to −183.2014 | yes: GAIN |
| response time (ms), 99th percentile | 654.8 | 296.2 | −54.8% | −460.1503 to −257.1801 | yes: GAIN |
| time over the response line (% of samples) | 3.584 | 2.154 | −39.9% | −2.0602 to −0.8005 | yes: GAIN |
| failed requests (%) | 1.654 | 1.595 | −3.6% | −0.1313 to +0.0126 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 7.4 | −22.9% | −3.8450 to −0.5550 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.4 | +66.400 (native is 0) | +56.6375 to +76.1625 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.5933 | +102.3% | −0.0940 to +0.6940 | no |
| utilisation (used / allocatable) | 0.04996 | 0.04966 | −0.6% | −0.0008 to +0.0002 | no |
| CPU used (cores), mean | 1.193 | 1.186 | −0.6% | −0.0201 to +0.0054 | no |
| Omni's own CPU (cores), mean | 0 | 0.03791 | +0.038 (native is 0) | +0.0328 to +0.0430 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.193 | 1.224 | +2.6% | +0.0175 to +0.0436 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 554.4 | 557.4 | +0.6% | −3.2997 to +9.4425 | no |
| HPA replicas, mean | 8.628 | 9.341 | +8.3% | −0.2745 to +1.7007 | no |
| pods started | 8.8 | 12.2 | +38.6% | +1.0348 to +5.7652 | yes: power given |
| pod start wait, total (s) | 14.6 | 24 | +64.4% | +4.0027 to +14.7973 | yes: LOSS |
| pod start wait, mean (s) | 1.671 | 1.933 | +15.7% | +0.0742 to +0.4499 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.29 | 37.05 | +2.1% | +0.3181 to +1.2064 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 77 | 4.6 |  |
| machine down | omni | 46 | 1.6 | -31 s (-40%) |
| spike | native | 270 | 69.0 |  |
| spike | omni | 263 | 65.8 | -7 s (-3%) |
| runaway pod started | native | 2 | 0.3 |  |
| runaway pod started | omni | 3 | 0.0 | +0 s (+16%) |
| probe blind | native | 79 | 1.2 |  |
| probe blind | omni | 61 | 0.1 | -18 s (-23%) |
| metrics down | native | 6 | 0.2 |  |
| metrics down | omni | 2 | 0.0 | -4 s (-64%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*