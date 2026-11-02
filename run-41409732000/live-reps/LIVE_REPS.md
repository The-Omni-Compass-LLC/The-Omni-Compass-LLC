# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.913 |
| node-hours | 1.493 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 163.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 224.7 | 131.3 |
| response time (ms), 95th percentile | 413.6 | 187.3 |
| response time (ms), 99th percentile | 2428 | 1351 |
| time over the response line (% of samples) | 8.04 | 5.461 |
| failed requests (%) | 4.546 | 4.084 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6633 | 0.625 |
| utilisation (used / allocatable) | 0.06852 | 0.0671 |
| CPU used (cores), mean | 1.621 | 1.587 |
| Omni's own CPU (cores), mean | 0 | 0.04349 |
| CPU used with Omni's own (cores), mean | 1.621 | 1.631 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.3 | 422.1 |
| HPA replicas, mean | 8.418 | 11.27 |
| pods started | 5.7 | 9.1 |
| pod start wait, total (s) | 8.1 | 17.3 |
| pod start wait, mean (s) | 1.405 | 1.905 |
| host CPU busy, the real machine under kind (%) | 46.52 | 47.24 |
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
| worker nodes in service, mean | 5.913 | 5.913 | −0.0% | −0.0006 to +0.0006 | no |
| node-hours | 1.493 | 1.492 | −0.0% | −0.0064 to +0.0061 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.8 | −0.2% | −1.2507 to +0.5191 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 163.2 | −0.2% | −1.2463 to +0.5146 | no |
| response time (ms), mean | 224.7 | 131.3 | −41.6% | −167.4860 to −19.3009 | yes: GAIN |
| response time (ms), 95th percentile | 413.6 | 187.3 | −54.7% | −278.2970 to −174.2860 | yes: GAIN |
| response time (ms), 99th percentile | 2428 | 1351 | −44.4% | −2886.1306 to +731.0578 | no |
| time over the response line (% of samples) | 8.04 | 5.461 | −32.1% | −3.4930 to −1.6662 | yes: GAIN |
| failed requests (%) | 4.546 | 4.084 | −10.2% | −1.1526 to +0.2287 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.6 | −12.5% | −1.5388 to −0.0612 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.1 | +45.100 (native is 0) | +38.7965 to +51.4035 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6633 | 0.625 | −5.8% | −0.5977 to +0.5211 | no |
| utilisation (used / allocatable) | 0.06852 | 0.0671 | −2.1% | −0.0032 to +0.0003 | no |
| CPU used (cores), mean | 1.621 | 1.587 | −2.1% | −0.0747 to +0.0080 | no |
| Omni's own CPU (cores), mean | 0 | 0.04349 | +0.043 (native is 0) | +0.0366 to +0.0504 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.621 | 1.631 | +0.6% | −0.0259 to +0.0461 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.3 | 422.1 | +0.9% | −6.4137 to +13.9285 | no |
| HPA replicas, mean | 8.418 | 11.27 | +33.8% | +1.8626 to +3.8319 | yes: power given |
| pods started | 5.7 | 9.1 | +59.6% | +2.0854 to +4.7146 | yes: power given |
| pod start wait, total (s) | 8.1 | 17.3 | +113.6% | +4.0441 to +14.3559 | yes: LOSS |
| pod start wait, mean (s) | 1.405 | 1.905 | +35.6% | +0.0412 to +0.9597 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.52 | 47.24 | +1.6% | −0.1390 to +1.5900 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 53 | 15.6 |  |
| machine down | omni | 47 | 9.4 | -7 s (-13%) |
| spike | native | 249 | 62.1 |  |
| spike | omni | 240 | 52.7 | -8 s (-3%) |
| runaway pod started | native | 95 | 9.5 |  |
| runaway pod started | omni | 83 | 6.8 | -11 s (-12%) |
| probe blind | native | 65 | 0.3 |  |
| probe blind | omni | 61 | 0.1 | -5 s (-7%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*