# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.968 |
| node-hours | 4.163 | 4.156 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.7 | 444.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.1 | 443.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 165.6 | 103.5 |
| response time (ms), 95th percentile | 333 | 117.4 |
| response time (ms), 99th percentile | 698.7 | 396.7 |
| time over the response line (% of samples) | 3.628 | 2.118 |
| failed requests (%) | 1.536 | 1.443 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 86.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.5433 |
| utilisation (used / allocatable) | 0.04904 | 0.04826 |
| CPU used (cores), mean | 1.171 | 1.152 |
| Omni's own CPU (cores), mean | 0 | 0.03977 |
| CPU used with Omni's own (cores), mean | 1.171 | 1.192 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 573.4 | 579.2 |
| HPA replicas, mean | 8.511 | 8.948 |
| pods started | 8.2 | 12.2 |
| pod start wait, total (s) | 12.9 | 21.3 |
| pod start wait, mean (s) | 1.589 | 1.726 |
| host CPU busy, the real machine under kind (%) | 35.95 | 36.85 |
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
| worker nodes in service, mean | 5.97 | 5.968 | −0.0% | −0.0044 to −0.0000 | yes: GAIN |
| node-hours | 4.163 | 4.156 | −0.1% | −0.0109 to −0.0015 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 445.7 | 444.8 | −0.2% | −1.5303 to −0.3279 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.1 | 443.1 | −0.2% | −1.6405 to −0.4470 | yes: GAIN |
| response time (ms), mean | 165.6 | 103.5 | −37.5% | −88.6686 to −35.6332 | yes: GAIN |
| response time (ms), 95th percentile | 333 | 117.4 | −64.8% | −261.5600 to −169.7570 | yes: GAIN |
| response time (ms), 99th percentile | 698.7 | 396.7 | −43.2% | −452.1291 to −151.9595 | yes: GAIN |
| time over the response line (% of samples) | 3.628 | 2.118 | −41.6% | −2.2408 to −0.7801 | yes: GAIN |
| failed requests (%) | 1.536 | 1.443 | −6.1% | −0.1663 to −0.0198 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 7 | −32.0% | −5.3800 to −1.2200 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.4 | +67.400 (native is 0) | +57.6317 to +77.1683 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.5433 | +2073.3% | +0.0945 to +0.9421 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04904 | 0.04826 | −1.6% | −0.0015 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.171 | 1.152 | −1.6% | −0.0366 to −0.0019 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03977 | +0.040 (native is 0) | +0.0346 to +0.0450 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.171 | 1.192 | +1.8% | +0.0063 to +0.0348 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 573.4 | 579.2 | +1.0% | −1.5906 to +13.1461 | no |
| HPA replicas, mean | 8.511 | 8.948 | +5.1% | −0.2037 to +1.0790 | no |
| pods started | 8.2 | 12.2 | +48.8% | +1.9768 to +6.0232 | yes: power given |
| pod start wait, total (s) | 12.9 | 21.3 | +65.1% | +4.4792 to +12.3208 | yes: LOSS |
| pod start wait, mean (s) | 1.589 | 1.726 | +8.6% | −0.0133 to +0.2865 | no |
| host CPU busy, the real machine under kind (%) | 35.95 | 36.85 | +2.5% | +0.6278 to +1.1706 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 60 | 4.1 |  |
| machine down | omni | 44 | 1.4 | -16 s (-26%) |
| spike | native | 257 | 64.8 |  |
| spike | omni | 254 | 61.6 | -3 s (-1%) |
| runaway pod started | native | 6 | 0.5 |  |
| runaway pod started | omni | 2 | 0.0 | -4 s (-65%) |
| probe blind | native | 61 | 1.5 |  |
| probe blind | omni | 61 | 0.1 | -0 s (-1%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+1%) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*