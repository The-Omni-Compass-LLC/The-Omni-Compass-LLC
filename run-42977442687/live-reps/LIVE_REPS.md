# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 90 s | omni, a decision every 60 s |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 4.512 | 4.513 | 4.516 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 512 | 511.9 | 511 | 510.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512 | 511.9 | 511 | 510.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 267.2 | 154.4 | 138.3 | 136.3 |
| response time (ms), 95th percentile | 712.9 | 320.8 | 272.5 | 249 |
| response time (ms), 99th percentile | 2207 | 1688 | 1044 | 1059 |
| time over the response line (% of samples) | 15.1 | 9.148 | 7.538 | 7.489 |
| failed requests (%) | 6.385 | 6.587 | 5.565 | 5.659 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.2 | 17.5 | 15.7 | 16 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.2 | 42.9 | 47.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.5367 | 0.635 | 0.5433 |
| utilisation (used / allocatable) | 0.09474 | 0.09422 | 0.0926 | 0.0923 |
| CPU used (cores), mean | 2.274 | 2.261 | 2.222 | 2.215 |
| Omni's own CPU (cores), mean | 0 | 0.04372 | 0.00718 | 0.00964 |
| CPU used with Omni's own (cores), mean | 2.274 | 2.305 | 2.23 | 2.225 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314 | 316.3 | 322 | 323.1 |
| HPA replicas, mean | 9.603 | 12.02 | 9.957 | 10.71 |
| pods started | 5.4 | 10.5 | 7.7 | 9.1 |
| pod start wait, total (s) | 8.6 | 17 | 11.1 | 15.3 |
| pod start wait, mean (s) | 1.597 | 1.603 | 1.41 | 1.684 |
| host CPU busy, the real machine under kind (%) | 64.3 | 65.45 | 63.14 | 63.17 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.512 | 4.513 | +0.0% | −0.0057 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512 | 511.9 | −0.0% | −1.1505 to +0.8677 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512 | 511.9 | −0.0% | −1.1505 to +0.8677 | no |
| response time (ms), mean | 267.2 | 154.4 | −42.2% | −140.3527 to −85.2304 | yes: GAIN |
| response time (ms), 95th percentile | 712.9 | 320.8 | −55.0% | −460.6535 to −323.4805 | yes: GAIN |
| response time (ms), 99th percentile | 2207 | 1688 | −23.5% | −1188.3845 to +150.1409 | no |
| time over the response line (% of samples) | 15.1 | 9.148 | −39.4% | −7.4361 to −4.4648 | yes: GAIN |
| failed requests (%) | 6.385 | 6.587 | +3.2% | −0.2717 to +0.6761 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.2 | 17.5 | −30.6% | −9.6385 to −5.7615 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.2 | +56.200 (native is 0) | +47.5254 to +64.8746 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.5367 | +101.2% | −0.0976 to +0.6376 | no |
| utilisation (used / allocatable) | 0.09474 | 0.09422 | −0.5% | −0.0015 to +0.0005 | no |
| CPU used (cores), mean | 2.274 | 2.261 | −0.5% | −0.0364 to +0.0118 | no |
| Omni's own CPU (cores), mean | 0 | 0.04372 | +0.044 (native is 0) | +0.0385 to +0.0490 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.274 | 2.305 | +1.4% | +0.0046 to +0.0581 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314 | 316.3 | +0.8% | −0.2756 to +5.0136 | no |
| HPA replicas, mean | 9.603 | 12.02 | +25.1% | +1.1830 to +3.6435 | yes: power given |
| pods started | 5.4 | 10.5 | +94.4% | +3.5751 to +6.6249 | yes: power given |
| pod start wait, total (s) | 8.6 | 17 | +97.7% | +5.1099 to +11.6901 | yes: LOSS |
| pod start wait, mean (s) | 1.597 | 1.603 | +0.3% | −0.3201 to +0.3308 | no |
| host CPU busy, the real machine under kind (%) | 64.3 | 65.45 | +1.8% | +0.5441 to +1.7487 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.512 | 4.516 | +0.1% | −0.0015 to +0.0092 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512 | 511 | −0.2% | −1.4166 to −0.5144 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512 | 511 | −0.2% | −1.4166 to −0.5144 | yes: GAIN |
| response time (ms), mean | 267.2 | 138.3 | −48.2% | −154.3372 to −103.4840 | yes: GAIN |
| response time (ms), 95th percentile | 712.9 | 272.5 | −61.8% | −511.3310 to −369.4180 | yes: GAIN |
| response time (ms), 99th percentile | 2207 | 1044 | −52.7% | −1528.7884 to −798.8400 | yes: GAIN |
| time over the response line (% of samples) | 15.1 | 7.538 | −50.1% | −9.6148 to −5.5056 | yes: GAIN |
| failed requests (%) | 6.385 | 5.565 | −12.8% | −1.6085 to −0.0316 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.2 | 15.7 | −37.7% | −11.4444 to −7.5556 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.9 | +42.900 (native is 0) | +30.6283 to +55.1717 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.635 | +138.1% | −0.0665 to +0.8032 | no |
| utilisation (used / allocatable) | 0.09474 | 0.0926 | −2.3% | −0.0028 to −0.0014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.274 | 2.222 | −2.3% | −0.0683 to −0.0343 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00718 | +0.007 (native is 0) | +0.0064 to +0.0080 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.274 | 2.23 | −1.9% | −0.0613 to −0.0269 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314 | 322 | +2.6% | +1.9276 to +14.2440 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.603 | 9.957 | +3.7% | +0.0063 to +0.7020 | yes: power given |
| pods started | 5.4 | 7.7 | +42.6% | −0.7357 to +5.3357 | no |
| pod start wait, total (s) | 8.6 | 11.1 | +29.1% | −0.9594 to +5.9594 | no |
| pod start wait, mean (s) | 1.597 | 1.41 | −11.7% | −0.5403 to +0.1666 | no |
| host CPU busy, the real machine under kind (%) | 64.3 | 63.14 | −1.8% | −1.6213 to −0.6910 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 4.512 | 4.515 | +0.1% | −0.0064 to +0.0121 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512 | 510.7 | −0.2% | −2.2354 to −0.2799 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512 | 510.7 | −0.2% | −2.2354 to −0.2799 | yes: GAIN |
| response time (ms), mean | 267.2 | 136.3 | −49.0% | −157.3667 to −104.4540 | yes: GAIN |
| response time (ms), 95th percentile | 712.9 | 249 | −65.1% | −540.9109 to −386.8701 | yes: GAIN |
| response time (ms), 99th percentile | 2207 | 1059 | −52.0% | −1547.2305 to −749.1967 | yes: GAIN |
| time over the response line (% of samples) | 15.1 | 7.489 | −50.4% | −9.7771 to −5.4404 | yes: GAIN |
| failed requests (%) | 6.385 | 5.659 | −11.4% | −1.4038 to −0.0478 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.2 | 16 | −36.5% | −11.2456 to −7.1544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 | +47.100 (native is 0) | +37.5838 to +56.6162 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.5433 | +103.8% | −0.1125 to +0.6659 | no |
| utilisation (used / allocatable) | 0.09474 | 0.0923 | −2.6% | −0.0031 to −0.0018 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.274 | 2.215 | −2.6% | −0.0744 to −0.0428 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00964 | +0.010 (native is 0) | +0.0085 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.274 | 2.225 | −2.2% | −0.0650 to −0.0328 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314 | 323.1 | +2.9% | +2.0115 to +16.3162 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.603 | 10.71 | +11.6% | +0.1260 to +2.0929 | yes: power given |
| pods started | 5.4 | 9.1 | +68.5% | +1.2210 to +6.1790 | yes: power given |
| pod start wait, total (s) | 8.6 | 15.3 | +77.9% | +2.9142 to +10.4858 | yes: LOSS |
| pod start wait, mean (s) | 1.597 | 1.684 | +5.5% | −0.3542 to +0.5286 | no |
| host CPU busy, the real machine under kind (%) | 64.3 | 63.17 | −1.8% | −1.6023 to −0.6571 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.513 | 4.516 | +0.1% | −0.0030 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 511.9 | 511 | −0.2% | −1.9193 to +0.2712 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.9 | 511 | −0.2% | −1.9193 to +0.2712 | no |
| response time (ms), mean | 154.4 | 138.3 | −10.4% | −32.4281 to +0.1900 | no |
| response time (ms), 95th percentile | 320.8 | 272.5 | −15.1% | −97.6934 to +1.0784 | no |
| response time (ms), 99th percentile | 1688 | 1044 | −38.2% | −1257.4186 to −31.9662 | yes: GAIN |
| time over the response line (% of samples) | 9.148 | 7.538 | −17.6% | −2.6649 to −0.5545 | yes: GAIN |
| failed requests (%) | 6.587 | 5.565 | −15.5% | −2.2195 to +0.1750 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.5 | 15.7 | −10.3% | −2.6793 to −0.9207 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 56.2 | 42.9 | −23.7% | −22.1578 to −4.4422 | yes, down (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 75 | 25 | −66.7% | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5367 | 0.635 | +18.3% | −0.3714 to +0.5681 | no |
| utilisation (used / allocatable) | 0.09422 | 0.0926 | −1.7% | −0.0029 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.261 | 2.222 | −1.7% | −0.0690 to −0.0089 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.04372 | 0.00718 | −83.6% | −0.0411 to −0.0320 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.305 | 2.23 | −3.3% | −0.1072 to −0.0438 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 316.3 | 322 | +1.8% | −0.4679 to +11.9015 | no |
| HPA replicas, mean | 12.02 | 9.957 | −17.1% | −3.0455 to −1.0726 | yes: GAIN |
| pods started | 10.5 | 7.7 | −26.7% | −5.1796 to −0.4204 | yes: GAIN |
| pod start wait, total (s) | 17 | 11.1 | −34.7% | −9.4598 to −2.3402 | yes: GAIN |
| pod start wait, mean (s) | 1.603 | 1.41 | −12.0% | −0.4308 to +0.0464 | no |
| host CPU busy, the real machine under kind (%) | 65.45 | 63.14 | −3.5% | −3.1461 to −1.4590 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.513 | 4.515 | +0.0% | −0.0063 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 511.9 | 510.7 | −0.2% | −2.4988 to +0.2663 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.9 | 510.7 | −0.2% | −2.4988 to +0.2663 | no |
| response time (ms), mean | 154.4 | 136.3 | −11.7% | −33.2818 to −2.9558 | yes: GAIN |
| response time (ms), 95th percentile | 320.8 | 249 | −22.4% | −116.5060 to −27.1410 | yes: GAIN |
| response time (ms), 99th percentile | 1688 | 1059 | −37.3% | −1372.7692 to +114.5856 | no |
| time over the response line (% of samples) | 9.148 | 7.489 | −18.1% | −2.8679 to −0.4485 | yes: GAIN |
| failed requests (%) | 6.587 | 5.659 | −14.1% | −2.0236 to +0.1675 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.5 | 16 | −8.6% | −2.4685 to −0.5315 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 56.2 | 47.1 | −16.2% | −14.6145 to −3.5855 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5367 | 0.5433 | +1.2% | −0.6607 to +0.6741 | no |
| utilisation (used / allocatable) | 0.09422 | 0.0923 | −2.0% | −0.0032 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.261 | 2.215 | −2.0% | −0.0763 to −0.0162 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.04372 | 0.00964 | −78.0% | −0.0383 to −0.0299 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.305 | 2.225 | −3.5% | −0.1121 to −0.0486 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 316.3 | 323.1 | +2.1% | −0.4746 to +14.0643 | no |
| HPA replicas, mean | 12.02 | 10.71 | −10.9% | −2.3070 to −0.3006 | yes: GAIN |
| pods started | 10.5 | 9.1 | −13.3% | −3.0927 to +0.2927 | no |
| pod start wait, total (s) | 17 | 15.3 | −10.0% | −4.2245 to +0.8245 | no |
| pod start wait, mean (s) | 1.603 | 1.684 | +5.1% | −0.0990 to +0.2627 | no |
| host CPU busy, the real machine under kind (%) | 65.45 | 63.17 | −3.5% | −3.0938 to −1.4583 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*