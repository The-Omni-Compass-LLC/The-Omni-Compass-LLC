# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.509 | 1.51 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | 159.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | 159.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 175.5 | 86.51 | 88.4 |
| response time (ms), 95th percentile | 404.7 | 132.1 | 130 |
| response time (ms), 99th percentile | 700.6 | 186.7 | 172.3 |
| time over the response line (% of samples) | 3.212 | 0.01212 | 0.245 |
| failed requests (%) | 0 | 0 | 0.149 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.8 | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | 24.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.4233 | 0.02667 |
| utilisation (used / allocatable) | 0.0419 | 0.03987 | 0.04072 |
| CPU used (cores), mean | 1.006 | 0.9568 | 0.9774 |
| Omni's own CPU (cores), mean | 0 | 0.03889 | 0.0392 |
| CPU used with Omni's own (cores), mean | 1.006 | 0.9957 | 1.017 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 656.9 | 683.4 | 671.2 |
| HPA replicas, mean | 8.67 | 9.303 | 9.586 |
| pods started | 5 | 4 | 9.7 |
| pod start wait, total (s) | 7.9 | 5.7 | 18.5 |
| pod start wait, mean (s) | 1.597 | 1.45 | 1.911 |
| host CPU busy, the real machine under kind (%) | 30.41 | 30.41 | 31.21 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.51 | +0.1% | −0.0003 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | −0.2% | −0.5913 to −0.1479 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | −0.2% | −0.5913 to −0.1479 | yes: GAIN |
| response time (ms), mean | 175.5 | 86.51 | −50.7% | −108.3871 to −69.6005 | yes: GAIN |
| response time (ms), 95th percentile | 404.7 | 132.1 | −67.4% | −330.2447 to −214.9883 | yes: GAIN |
| response time (ms), 99th percentile | 700.6 | 186.7 | −73.4% | −662.5459 to −365.3635 | yes: GAIN |
| time over the response line (% of samples) | 3.212 | 0.01212 | −99.6% | −4.3830 to −2.0169 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.8 | 0 | −100.0% | −5.3379 to −2.2621 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20.000 (native is 0) | +18.0338 to +21.9662 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.4233 | +98.4% | −0.2180 to +0.6380 | no |
| utilisation (used / allocatable) | 0.0419 | 0.03987 | −4.9% | −0.0028 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.006 | 0.9568 | −4.9% | −0.0680 to −0.0296 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03889 | +0.039 (native is 0) | +0.0343 to +0.0435 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 0.9957 | −1.0% | −0.0274 to +0.0075 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 656.9 | 683.4 | +4.0% | +12.9416 to +40.1352 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.67 | 9.303 | +7.3% | +0.1928 to +1.0736 | yes: power given |
| pods started | 5 | 4 | −20.0% | −2.3488 to +0.3488 | no |
| pod start wait, total (s) | 7.9 | 5.7 | −27.8% | −4.7189 to +0.3189 | no |
| pod start wait, mean (s) | 1.597 | 1.45 | −9.2% | −0.5523 to +0.2589 | no |
| host CPU busy, the real machine under kind (%) | 30.41 | 30.41 | −0.0% | −0.5068 to +0.5051 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.514 | +0.4% | −0.0012 to +0.0118 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.6 | +0.2% | −0.3211 to +0.8657 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.6 | +0.2% | −0.3211 to +0.8657 | no |
| response time (ms), mean | 175.5 | 88.4 | −49.6% | −106.6084 to −67.5979 | yes: GAIN |
| response time (ms), 95th percentile | 404.7 | 130 | −67.9% | −332.7734 to −216.6386 | yes: GAIN |
| response time (ms), 99th percentile | 700.6 | 172.3 | −75.4% | −677.0502 to −379.6524 | yes: GAIN |
| time over the response line (% of samples) | 3.212 | 0.245 | −92.4% | −4.1429 to −1.7913 | yes: GAIN |
| failed requests (%) | 0 | 0.149 | +0.149 (native is 0) | +0.0672 to +0.2308 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.8 | 0.2 | −94.7% | −5.2588 to −1.9412 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.3 | +24.300 (native is 0) | +18.2581 to +30.3419 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.02667 | −87.5% | −0.3887 to +0.0154 | no |
| utilisation (used / allocatable) | 0.0419 | 0.04072 | −2.8% | −0.0021 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.006 | 0.9774 | −2.8% | −0.0511 to −0.0054 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0392 | +0.039 (native is 0) | +0.0354 to +0.0430 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 1.017 | +1.1% | −0.0123 to +0.0341 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 656.9 | 671.2 | +2.2% | −5.3025 to +33.9309 | no |
| HPA replicas, mean | 8.67 | 9.586 | +10.6% | +0.6612 to +1.1716 | yes: power given |
| pods started | 5 | 9.7 | +94.0% | +3.5295 to +5.8705 | yes: power given |
| pod start wait, total (s) | 7.9 | 18.5 | +134.2% | +7.0602 to +14.1398 | yes: LOSS |
| pod start wait, mean (s) | 1.597 | 1.911 | +19.7% | −0.1307 to +0.7603 | no |
| host CPU busy, the real machine under kind (%) | 30.41 | 31.21 | +2.6% | +0.1211 to +1.4758 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.51 | 1.514 | +0.3% | −0.0022 to +0.0102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.6 | +0.4% | −0.0355 to +1.3192 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.6 | +0.4% | −0.0355 to +1.3192 | no |
| response time (ms), mean | 86.51 | 88.4 | +2.2% | +0.0938 to +3.6876 | yes: LOSS |
| response time (ms), 95th percentile | 132.1 | 130 | −1.6% | −5.7610 to +1.5820 | no |
| response time (ms), 99th percentile | 186.7 | 172.3 | −7.7% | −25.4664 to −3.3268 | yes: GAIN |
| time over the response line (% of samples) | 0.01212 | 0.245 | +1921.2% | +0.1682 to +0.2975 | yes: LOSS |
| failed requests (%) | 0 | 0.149 | +0.149 (native is 0) | +0.0672 to +0.2308 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20 | 24.3 | +21.5% | −1.5797 to +10.1797 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | -10 | −111.1% | −100.0000 to −100.0000 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4233 | 0.02667 | −93.7% | −0.7472 to −0.0462 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03987 | 0.04072 | +2.1% | +0.0001 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9568 | 0.9774 | +2.1% | +0.0030 to +0.0380 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03889 | 0.0392 | +0.8% | −0.0007 to +0.0014 | no |
| CPU used with Omni's own (cores), mean | 0.9957 | 1.017 | +2.1% | +0.0039 to +0.0377 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.4 | 671.2 | −1.8% | −22.2871 to −2.1613 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.303 | 9.586 | +3.0% | −0.1469 to +0.7135 | no |
| pods started | 4 | 9.7 | +142.5% | +4.8047 to +6.5953 | yes: power given |
| pod start wait, total (s) | 5.7 | 18.5 | +224.6% | +10.5684 to +15.0316 | yes: LOSS |
| pod start wait, mean (s) | 1.45 | 1.911 | +31.8% | +0.1734 to +0.7495 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.41 | 31.21 | +2.6% | +0.4326 to +1.1661 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*