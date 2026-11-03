# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.969 |
| node-hours | 4.16 | 4.161 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.4 | 442.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.9 | 441.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 155.9 | 88.19 |
| response time (ms), 95th percentile | 299 | 106.2 |
| response time (ms), 99th percentile | 660.3 | 347.4 |
| time over the response line (% of samples) | 2.858 | 1.684 |
| failed requests (%) | 1.26 | 1.222 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 95 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.1317 |
| utilisation (used / allocatable) | 0.04568 | 0.04446 |
| CPU used (cores), mean | 1.091 | 1.062 |
| Omni's own CPU (cores), mean | 0 | 0.03585 |
| CPU used with Omni's own (cores), mean | 1.091 | 1.097 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 613.4 | 622 |
| HPA replicas, mean | 8.182 | 8.47 |
| pods started | 8.3 | 12.2 |
| pod start wait, total (s) | 12.9 | 20.4 |
| pod start wait, mean (s) | 1.53 | 1.679 |
| host CPU busy, the real machine under kind (%) | 33.26 | 33.91 |
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
| worker nodes in service, mean | 5.97 | 5.969 | −0.0% | −0.0048 to +0.0023 | no |
| node-hours | 4.16 | 4.161 | +0.0% | −0.0077 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.4 | 442.8 | −0.1% | −1.4232 to +0.2575 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.9 | 441.2 | −0.1% | −1.4649 to +0.1659 | no |
| response time (ms), mean | 155.9 | 88.19 | −43.4% | −93.7759 to −41.5740 | yes: GAIN |
| response time (ms), 95th percentile | 299 | 106.2 | −64.5% | −238.9678 to −146.6972 | yes: GAIN |
| response time (ms), 99th percentile | 660.3 | 347.4 | −47.4% | −402.5522 to −223.2714 | yes: GAIN |
| time over the response line (% of samples) | 2.858 | 1.684 | −41.1% | −1.9313 to −0.4179 | yes: GAIN |
| failed requests (%) | 1.26 | 1.222 | −3.0% | −0.1721 to +0.0964 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 6.1 | −26.5% | −4.0714 to −0.3286 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.1 | +62.100 (native is 0) | +52.9244 to +71.2756 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.1317 | −31.3% | −0.2783 to +0.1583 | no |
| utilisation (used / allocatable) | 0.04568 | 0.04446 | −2.7% | −0.0025 to +0.0001 | no |
| CPU used (cores), mean | 1.091 | 1.062 | −2.7% | −0.0596 to +0.0012 | no |
| Omni's own CPU (cores), mean | 0 | 0.03585 | +0.036 (native is 0) | +0.0313 to +0.0404 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.091 | 1.097 | +0.6% | −0.0209 to +0.0342 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 613.4 | 622 | +1.4% | −7.0055 to +24.1361 | no |
| HPA replicas, mean | 8.182 | 8.47 | +3.5% | −0.5219 to +1.0980 | no |
| pods started | 8.3 | 12.2 | +47.0% | +1.8642 to +5.9358 | yes: power given |
| pod start wait, total (s) | 12.9 | 20.4 | +58.1% | +3.4221 to +11.5779 | yes: LOSS |
| pod start wait, mean (s) | 1.53 | 1.679 | +9.7% | −0.1699 to +0.4676 | no |
| host CPU busy, the real machine under kind (%) | 33.26 | 33.91 | +2.0% | +0.0159 to +1.2888 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 68 | 3.9 |  |
| machine down | omni | 38 | 1.5 | -29 s (-44%) |
| spike | native | 243 | 51.4 |  |
| spike | omni | 233 | 48.5 | -9 s (-4%) |
| runaway pod started | native | 7 | 0.6 |  |
| runaway pod started | omni | 2 | 0.0 | -5 s (-72%) |
| probe blind | native | 57 | 0.9 |  |
| probe blind | omni | 48 | 0.0 | -9 s (-16%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | +1 s (+37%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*