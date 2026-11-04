# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.915 |
| node-hours | 1.489 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.5 | 164.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 163 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 208.8 | 118.2 |
| response time (ms), 95th percentile | 395.5 | 172.9 |
| response time (ms), 99th percentile | 1130 | 658.3 |
| time over the response line (% of samples) | 7.283 | 5.182 |
| failed requests (%) | 4.299 | 3.955 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 5.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7733 | 0.6417 |
| utilisation (used / allocatable) | 0.06765 | 0.06649 |
| CPU used (cores), mean | 1.6 | 1.573 |
| Omni's own CPU (cores), mean | 0 | 0.04205 |
| CPU used with Omni's own (cores), mean | 1.6 | 1.615 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.5 | 425.9 |
| HPA replicas, mean | 8.445 | 10.42 |
| pods started | 5.7 | 11.1 |
| pod start wait, total (s) | 18.1 | 38.6 |
| pod start wait, mean (s) | 3.093 | 3.371 |
| host CPU busy, the real machine under kind (%) | 45.83 | 46.82 |
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
| worker nodes in service, mean | 5.913 | 5.915 | +0.0% | −0.0016 to +0.0063 | no |
| node-hours | 1.489 | 1.492 | +0.2% | −0.0029 to +0.0090 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.5 | 164.6 | +0.1% | −0.6585 to +0.8772 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 163 | +0.1% | −0.6432 to +0.9452 | no |
| response time (ms), mean | 208.8 | 118.2 | −43.4% | −130.6562 to −50.5797 | yes: GAIN |
| response time (ms), 95th percentile | 395.5 | 172.9 | −56.3% | −298.3042 to −146.9478 | yes: GAIN |
| response time (ms), 99th percentile | 1130 | 658.3 | −41.8% | −882.6347 to −61.2695 | yes: GAIN |
| time over the response line (% of samples) | 7.283 | 5.182 | −28.8% | −3.6499 to −0.5508 | yes: GAIN |
| failed requests (%) | 4.299 | 3.955 | −8.0% | −1.0075 to +0.3188 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 5.4 | −14.3% | −1.9366 to +0.1366 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 | +47.300 (native is 0) | +36.1722 to +58.4278 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7733 | 0.6417 | −17.0% | −0.6855 to +0.4221 | no |
| utilisation (used / allocatable) | 0.06765 | 0.06649 | −1.7% | −0.0029 to +0.0006 | no |
| CPU used (cores), mean | 1.6 | 1.573 | −1.7% | −0.0686 to +0.0149 | no |
| Omni's own CPU (cores), mean | 0 | 0.04205 | +0.042 (native is 0) | +0.0356 to +0.0485 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.6 | 1.615 | +0.9% | −0.0215 to +0.0518 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.5 | 425.9 | +0.8% | −6.7592 to +13.5006 | no |
| HPA replicas, mean | 8.445 | 10.42 | +23.4% | +0.9786 to +2.9712 | yes: power given |
| pods started | 5.7 | 11.1 | +94.7% | +3.2620 to +7.5380 | yes: power given |
| pod start wait, total (s) | 18.1 | 38.6 | +113.3% | −15.6940 to +56.6940 | no |
| pod start wait, mean (s) | 3.093 | 3.371 | +9.0% | −3.7809 to +4.3354 | no |
| host CPU busy, the real machine under kind (%) | 45.83 | 46.82 | +2.2% | +0.3289 to +1.6522 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 81 | 13.9 |  |
| machine down | omni | 34 | 8.6 | -48 s (-59%) |
| spike | native | 241 | 53.8 |  |
| spike | omni | 231 | 51.6 | -10 s (-4%) |
| runaway pod started | native | 101 | 9.1 |  |
| runaway pod started | omni | 78 | 6.9 | -23 s (-23%) |
| probe blind | native | 58 | 0.6 |  |
| probe blind | omni | 54 | 0.1 | -4 s (-7%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*