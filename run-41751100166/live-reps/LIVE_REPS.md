# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.515 | 1.514 | 1.514 | 1.514 | 1.513 | 1.514 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | 158.6 | 158.5 | 158.6 | 158.5 | 158.6 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | 158.6 | 158.5 | 158.6 | 158.5 | 158.6 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 151.6 | 79.97 | 78.23 | 77.62 | 78.08 | 77.93 | 78.78 | 79.46 |
| response time (ms), 95th percentile | 341.2 | 121.4 | 116.9 | 115.5 | 117.4 | 117.3 | 118 | 121.5 |
| response time (ms), 99th percentile | 546.7 | 169.2 | 160.9 | 154.6 | 159.3 | 154.6 | 167.8 | 169.8 |
| time over the response line (% of samples) | 1.947 | 0.0847 | 0.04819 | 0.01198 | 0.02424 | 0.01198 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.7 | 15.7 | 17 | 17.3 | 18.6 | 20.3 | 21.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 70 | nan | nan | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.1633 | 0.19 | 0.1333 | 0.1583 | 0.1333 | 0.2683 | 0.275 |
| utilisation (used / allocatable) | 0.03814 | 0.03665 | 0.03635 | 0.03611 | 0.03638 | 0.0365 | 0.03653 | 0.03707 |
| CPU used (cores), mean | 0.9155 | 0.8796 | 0.8723 | 0.8668 | 0.8732 | 0.876 | 0.8767 | 0.8897 |
| Omni's own CPU (cores), mean | 0 | 0.0364 | 0.00615 | 0.00686 | 0.00775 | 0.01417 | 0.02553 | 0.06973 |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.916 | 0.8784 | 0.8736 | 0.8809 | 0.8902 | 0.9022 | 0.9594 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 753 | 757.5 | 760.8 | 757.3 | 753.6 | 752.3 | 744.1 |
| HPA replicas, mean | 8.363 | 9.003 | 8.329 | 8.32 | 7.547 | 7.727 | 8.413 | 8.643 |
| pods started | 5.5 | 5.3 | 4.4 | 4 | 3.6 | 4 | 4.4 | 3.9 |
| pod start wait, total (s) | 9.7 | 9 | 5.5 | 4.2 | 4.8 | 5.7 | 7 | 5.8 |
| pod start wait, mean (s) | 1.773 | 1.742 | 1.153 | 0.965 | 1.333 | 1.452 | 1.67 | 1.531 |
| host CPU busy, the real machine under kind (%) | 27.84 | 28.24 | 26.97 | 26.93 | 27.14 | 27.24 | 27.89 | 29.61 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan | nan | nan | nan |

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
| node-hours | 1.514 | 1.515 | +0.1% | −0.0013 to +0.0033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.7 | −0.1% | −0.5254 to +0.0630 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.7 | −0.1% | −0.5254 to +0.0630 | no |
| response time (ms), mean | 151.6 | 79.97 | −47.2% | −94.1949 to −49.0378 | yes: GAIN |
| response time (ms), 95th percentile | 341.2 | 121.4 | −64.4% | −280.0617 to −159.3733 | yes: GAIN |
| response time (ms), 99th percentile | 546.7 | 169.2 | −69.1% | −504.8130 to −250.2790 | yes: GAIN |
| time over the response line (% of samples) | 1.947 | 0.0847 | −95.7% | −3.0053 to −0.7199 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0.1 | −95.0% | −3.1367 to −0.6633 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.7 | +21.700 (native is 0) | +17.8992 to +25.5008 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.1633 | −45.3% | −0.4016 to +0.1316 | no |
| utilisation (used / allocatable) | 0.03814 | 0.03665 | −3.9% | −0.0023 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9155 | 0.8796 | −3.9% | −0.0558 to −0.0159 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0364 | +0.036 (native is 0) | +0.0310 to +0.0418 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.916 | +0.1% | −0.0151 to +0.0161 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 753 | +3.1% | +10.2482 to +34.4594 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.363 | 9.003 | +7.6% | −0.0183 to +1.2970 | no |
| pods started | 5.5 | 5.3 | −3.6% | −1.0121 to +0.6121 | no |
| pod start wait, total (s) | 9.7 | 9 | −7.2% | −2.7525 to +1.3525 | no |
| pod start wait, mean (s) | 1.773 | 1.742 | −1.8% | −0.1988 to +0.1359 | no |
| host CPU busy, the real machine under kind (%) | 27.84 | 28.24 | +1.4% | +0.0543 to +0.7499 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0011 to +0.0025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 | −0.2% | −0.7049 to +0.0355 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.6 | −0.2% | −0.7049 to +0.0355 | no |
| response time (ms), mean | 151.6 | 78.23 | −48.4% | −96.6427 to −50.0683 | yes: GAIN |
| response time (ms), 95th percentile | 341.2 | 116.9 | −65.7% | −286.2264 to −162.2266 | yes: GAIN |
| response time (ms), 99th percentile | 546.7 | 160.9 | −70.6% | −509.8865 to −261.8305 | yes: GAIN |
| time over the response line (% of samples) | 1.947 | 0.04819 | −97.5% | −3.0379 to −0.7603 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.2617 to −0.7383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.7 | +15.700 (native is 0) | +14.6310 to +16.7690 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.19 | −36.3% | −0.4703 to +0.2536 | no |
| utilisation (used / allocatable) | 0.03814 | 0.03635 | −4.7% | −0.0028 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9155 | 0.8723 | −4.7% | −0.0667 to −0.0196 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00615 | +0.006 (native is 0) | +0.0054 to +0.0069 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.8784 | −4.0% | −0.0600 to −0.0140 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 757.5 | +3.7% | +12.7728 to +40.8829 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.363 | 8.329 | −0.4% | −0.3294 to +0.2602 | no |
| pods started | 5.5 | 4.4 | −20.0% | −2.2898 to +0.0898 | no |
| pod start wait, total (s) | 9.7 | 5.5 | −43.3% | −7.2122 to −1.1878 | yes: GAIN |
| pod start wait, mean (s) | 1.773 | 1.153 | −35.0% | −1.0813 to −0.1587 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.84 | 26.97 | −3.1% | −1.4106 to −0.3343 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0017 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.5 | −0.3% | −0.7855 to −0.0751 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.5 | −0.3% | −0.7855 to −0.0751 | yes: GAIN |
| response time (ms), mean | 151.6 | 77.62 | −48.8% | −97.3822 to −50.5609 | yes: GAIN |
| response time (ms), 95th percentile | 341.2 | 115.5 | −66.1% | −287.6657 to −163.6013 | yes: GAIN |
| response time (ms), 99th percentile | 546.7 | 154.6 | −71.7% | −519.6897 to −264.5223 | yes: GAIN |
| time over the response line (% of samples) | 1.947 | 0.01198 | −99.4% | −3.1048 to −0.7658 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.2617 to −0.7383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17.000 (native is 0) | +15.4184 to +18.5816 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.1333 | −55.3% | −0.4473 to +0.1173 | no |
| utilisation (used / allocatable) | 0.03814 | 0.03611 | −5.3% | −0.0030 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9155 | 0.8668 | −5.3% | −0.0720 to −0.0255 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00686 | +0.007 (native is 0) | +0.0060 to +0.0078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.8736 | −4.6% | −0.0643 to −0.0194 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 760.8 | +4.1% | +15.7872 to +44.5125 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.363 | 8.32 | −0.5% | −0.3899 to +0.3040 | no |
| pods started | 5.5 | 4 | −27.3% | −2.8168 to −0.1832 | yes: GAIN |
| pod start wait, total (s) | 9.7 | 4.2 | −56.7% | −7.5302 to −3.4698 | yes: GAIN |
| pod start wait, mean (s) | 1.773 | 0.965 | −45.6% | −1.1248 to −0.4919 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.84 | 26.93 | −3.3% | −1.4359 to −0.3801 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0018 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 | −0.2% | −0.7728 to −0.0010 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.6 | −0.2% | −0.7728 to −0.0010 | yes: GAIN |
| response time (ms), mean | 151.6 | 78.08 | −48.5% | −97.0137 to −50.0065 | yes: GAIN |
| response time (ms), 95th percentile | 341.2 | 117.4 | −65.6% | −286.3518 to −161.2332 | yes: GAIN |
| response time (ms), 99th percentile | 546.7 | 159.3 | −70.9% | −518.5018 to −256.4316 | yes: GAIN |
| time over the response line (% of samples) | 1.947 | 0.02424 | −98.8% | −3.0815 to −0.7646 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.2617 to −0.7383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.3 | +17.300 (native is 0) | +13.9441 to +20.6559 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.1583 | −46.9% | −0.4450 to +0.1650 | no |
| utilisation (used / allocatable) | 0.03814 | 0.03638 | −4.6% | −0.0028 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9155 | 0.8732 | −4.6% | −0.0665 to −0.0180 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00775 | +0.008 (native is 0) | +0.0066 to +0.0089 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.8809 | −3.8% | −0.0579 to −0.0112 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 757.3 | +3.6% | +11.0155 to +42.2884 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.363 | 7.547 | −9.8% | −1.3572 to −0.2741 | yes: GAIN |
| pods started | 5.5 | 3.6 | −34.5% | −2.7564 to −1.0436 | yes: GAIN |
| pod start wait, total (s) | 9.7 | 4.8 | −50.5% | −6.6342 to −3.1658 | yes: GAIN |
| pod start wait, mean (s) | 1.773 | 1.333 | −24.8% | −0.6689 to −0.2111 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.84 | 27.14 | −2.5% | −1.2872 to −0.1114 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0025 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.5 | −0.3% | −0.8015 to −0.0207 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.5 | −0.3% | −0.8015 to −0.0207 | yes: GAIN |
| response time (ms), mean | 151.6 | 77.93 | −48.6% | −97.2033 to −50.1009 | yes: GAIN |
| response time (ms), 95th percentile | 341.2 | 117.3 | −65.6% | −285.9980 to −161.7310 | yes: GAIN |
| response time (ms), 99th percentile | 546.7 | 154.6 | −71.7% | −520.2833 to −263.9681 | yes: GAIN |
| time over the response line (% of samples) | 1.947 | 0.01198 | −99.4% | −3.1010 to −0.7696 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.2617 to −0.7383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | +18.600 (native is 0) | +15.6181 to +21.5819 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.1333 | −55.3% | −0.5675 to +0.2375 | no |
| utilisation (used / allocatable) | 0.03814 | 0.0365 | −4.3% | −0.0026 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9155 | 0.876 | −4.3% | −0.0633 to −0.0156 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01417 | +0.014 (native is 0) | +0.0121 to +0.0162 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.8902 | −2.8% | −0.0475 to −0.0030 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 753.6 | +3.1% | +7.9800 to +37.9607 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.363 | 7.727 | −7.6% | −0.9620 to −0.3094 | yes: GAIN |
| pods started | 5.5 | 4 | −27.3% | −2.1079 to −0.8921 | yes: GAIN |
| pod start wait, total (s) | 9.7 | 5.7 | −41.2% | −6.2367 to −1.7633 | yes: GAIN |
| pod start wait, mean (s) | 1.773 | 1.452 | −18.1% | −0.8367 to +0.1934 | no |
| host CPU busy, the real machine under kind (%) | 27.84 | 27.24 | −2.2% | −1.1198 to −0.0927 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0013 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 | −0.2% | −0.7182 to +0.0922 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.6 | −0.2% | −0.7182 to +0.0922 | no |
| response time (ms), mean | 151.6 | 78.78 | −48.0% | −96.0981 to −49.5252 | yes: GAIN |
| response time (ms), 95th percentile | 341.2 | 118 | −65.4% | −285.0700 to −161.2160 | yes: GAIN |
| response time (ms), 99th percentile | 546.7 | 167.8 | −69.3% | −499.8917 to −257.9769 | yes: GAIN |
| time over the response line (% of samples) | 1.947 | 0 | −100.0% | −3.1180 to −0.7766 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.2617 to −0.7383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.300 (native is 0) | +18.1660 to +22.4340 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.2683 | −10.1% | −0.2951 to +0.2351 | no |
| utilisation (used / allocatable) | 0.03814 | 0.03653 | −4.2% | −0.0027 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9155 | 0.8767 | −4.2% | −0.0639 to −0.0136 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02553 | +0.026 (native is 0) | +0.0223 to +0.0287 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.9022 | −1.4% | −0.0360 to +0.0095 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 752.3 | +3.0% | +2.5635 to +40.7815 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.363 | 8.413 | +0.6% | −0.1691 to +0.2691 | no |
| pods started | 5.5 | 4.4 | −20.0% | −2.0204 to −0.1796 | yes: GAIN |
| pod start wait, total (s) | 9.7 | 7 | −27.8% | −4.8604 to −0.5396 | yes: GAIN |
| pod start wait, mean (s) | 1.773 | 1.67 | −5.8% | −0.3023 to +0.0957 | no |
| host CPU busy, the real machine under kind (%) | 27.84 | 27.89 | +0.2% | −0.5733 to +0.6633 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.516 | +0.1% | +0.0007 to +0.0037 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.9 | −0.0% | −0.3049 to +0.2700 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.9 | −0.0% | −0.3049 to +0.2700 | no |
| response time (ms), mean | 151.6 | 79.46 | −47.6% | −94.8429 to −49.4132 | yes: GAIN |
| response time (ms), 95th percentile | 341.2 | 121.5 | −64.4% | −280.2691 to −159.1119 | yes: GAIN |
| response time (ms), 99th percentile | 546.7 | 169.8 | −68.9% | −495.4617 to −258.4521 | yes: GAIN |
| time over the response line (% of samples) | 1.947 | 0 | −100.0% | −3.1180 to −0.7766 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.2617 to −0.7383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.3 | +21.300 (native is 0) | +19.3324 to +23.2676 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.275 | −7.8% | −0.4451 to +0.3985 | no |
| utilisation (used / allocatable) | 0.03814 | 0.03707 | −2.8% | −0.0018 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9155 | 0.8897 | −2.8% | −0.0439 to −0.0077 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06973 | +0.070 (native is 0) | +0.0603 to +0.0791 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9155 | 0.9594 | +4.8% | +0.0297 to +0.0582 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 744.1 | +1.8% | −0.9338 to +27.9566 | no |
| HPA replicas, mean | 8.363 | 8.643 | +3.4% | −0.0848 to +0.6454 | no |
| pods started | 5.5 | 3.9 | −29.1% | −2.8707 to −0.3293 | yes: GAIN |
| pod start wait, total (s) | 9.7 | 5.8 | −40.2% | −6.6693 to −1.1307 | yes: GAIN |
| pod start wait, mean (s) | 1.773 | 1.531 | −13.7% | −0.5065 to +0.0217 | no |
| host CPU busy, the real machine under kind (%) | 27.84 | 29.61 | +6.4% | +1.3623 to +2.1772 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.0% | −0.0025 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.6 | −0.1% | −0.3721 to +0.1651 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.6 | −0.1% | −0.3721 to +0.1651 | no |
| response time (ms), mean | 79.97 | 78.23 | −2.2% | −2.9939 to −0.4844 | yes: GAIN |
| response time (ms), 95th percentile | 121.4 | 116.9 | −3.7% | −8.5381 to −0.4799 | yes: GAIN |
| response time (ms), 99th percentile | 169.2 | 160.9 | −4.9% | −27.9819 to +11.3569 | no |
| time over the response line (% of samples) | 0.0847 | 0.04819 | −43.1% | −0.1715 to +0.0985 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 21.7 | 15.7 | −27.6% | −9.5366 to −2.4634 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1633 | 0.19 | +16.3% | −0.3108 to +0.3642 | no |
| utilisation (used / allocatable) | 0.03665 | 0.03635 | −0.8% | −0.0007 to +0.0001 | no |
| CPU used (cores), mean | 0.8796 | 0.8723 | −0.8% | −0.0173 to +0.0028 | no |
| Omni's own CPU (cores), mean | 0.0364 | 0.00615 | −83.1% | −0.0350 to −0.0255 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.916 | 0.8784 | −4.1% | −0.0497 to −0.0253 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 753 | 757.5 | +0.6% | −1.6136 to +10.5617 | no |
| HPA replicas, mean | 9.003 | 8.329 | −7.5% | −1.3824 to +0.0345 | no |
| pods started | 5.3 | 4.4 | −17.0% | −1.9900 to +0.1900 | no |
| pod start wait, total (s) | 9 | 5.5 | −38.9% | −5.9836 to −1.0164 | yes: GAIN |
| pod start wait, mean (s) | 1.742 | 1.153 | −33.8% | −0.9758 to −0.2013 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.24 | 26.97 | −4.5% | −1.7759 to −0.7732 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0022 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.5 | −0.1% | −0.4167 to +0.0186 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.5 | −0.1% | −0.4167 to +0.0186 | no |
| response time (ms), mean | 79.97 | 77.62 | −2.9% | −3.6539 to −1.0564 | yes: GAIN |
| response time (ms), 95th percentile | 121.4 | 115.5 | −4.9% | −9.6704 to −2.1616 | yes: GAIN |
| response time (ms), 99th percentile | 169.2 | 154.6 | −8.6% | −23.7875 to −5.3325 | yes: GAIN |
| time over the response line (% of samples) | 0.0847 | 0.01198 | −85.9% | −0.1563 to +0.0108 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 21.7 | 17 | −21.7% | −8.5895 to −0.8105 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1633 | 0.1333 | −18.4% | −0.2433 to +0.1833 | no |
| utilisation (used / allocatable) | 0.03665 | 0.03611 | −1.5% | −0.0010 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8796 | 0.8668 | −1.5% | −0.0247 to −0.0010 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.0364 | 0.00686 | −81.2% | −0.0341 to −0.0250 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.916 | 0.8736 | −4.6% | −0.0560 to −0.0287 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 753 | 760.8 | +1.0% | −2.8394 to +18.4315 | no |
| HPA replicas, mean | 9.003 | 8.32 | −7.6% | −1.3136 to −0.0510 | yes: GAIN |
| pods started | 5.3 | 4 | −24.5% | −2.5181 to −0.0819 | yes: GAIN |
| pod start wait, total (s) | 9 | 4.2 | −53.3% | −6.3379 to −3.2621 | yes: GAIN |
| pod start wait, mean (s) | 1.742 | 0.965 | −44.6% | −1.1257 to −0.4281 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.24 | 26.93 | −4.6% | −1.8368 to −0.7833 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0029 to +0.0012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.6 | −0.1% | −0.3383 to +0.0269 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.6 | −0.1% | −0.3383 to +0.0269 | no |
| response time (ms), mean | 79.97 | 78.08 | −2.4% | −2.9541 to −0.8334 | yes: GAIN |
| response time (ms), 95th percentile | 121.4 | 117.4 | −3.4% | −8.5181 to +0.3681 | no |
| response time (ms), 99th percentile | 169.2 | 159.3 | −5.9% | −24.0887 to +4.2473 | no |
| time over the response line (% of samples) | 0.0847 | 0.02424 | −71.4% | −0.1699 to +0.0490 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 21.7 | 17.3 | −20.3% | −8.7340 to −0.0660 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1633 | 0.1583 | −3.1% | −0.2265 to +0.2165 | no |
| utilisation (used / allocatable) | 0.03665 | 0.03638 | −0.7% | −0.0008 to +0.0003 | no |
| CPU used (cores), mean | 0.8796 | 0.8732 | −0.7% | −0.0196 to +0.0069 | no |
| Omni's own CPU (cores), mean | 0.0364 | 0.00775 | −78.7% | −0.0329 to −0.0244 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.916 | 0.8809 | −3.8% | −0.0492 to −0.0209 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 753 | 757.3 | +0.6% | −9.2418 to +17.8381 | no |
| HPA replicas, mean | 9.003 | 7.547 | −16.2% | −2.1683 to −0.7418 | yes: GAIN |
| pods started | 5.3 | 3.6 | −32.1% | −2.5294 to −0.8706 | yes: GAIN |
| pod start wait, total (s) | 9 | 4.8 | −46.7% | −5.6226 to −2.7774 | yes: GAIN |
| pod start wait, mean (s) | 1.742 | 1.333 | −23.5% | −0.6290 to −0.1882 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.24 | 27.14 | −3.9% | −1.5919 to −0.6109 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.513 | −0.1% | −0.0046 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.5 | −0.1% | −0.5377 to +0.1779 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.5 | −0.1% | −0.5377 to +0.1779 | no |
| response time (ms), mean | 79.97 | 77.93 | −2.5% | −3.2522 to −0.8192 | yes: GAIN |
| response time (ms), 95th percentile | 121.4 | 117.3 | −3.4% | −9.4929 to +1.1989 | no |
| response time (ms), 99th percentile | 169.2 | 154.6 | −8.6% | −30.0764 to +0.9170 | no |
| time over the response line (% of samples) | 0.0847 | 0.01198 | −85.9% | −0.1891 to +0.0436 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 21.7 | 18.6 | −14.3% | −7.0819 to +0.8819 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1633 | 0.1333 | −18.4% | −0.3511 to +0.2911 | no |
| utilisation (used / allocatable) | 0.03665 | 0.0365 | −0.4% | −0.0007 to +0.0004 | no |
| CPU used (cores), mean | 0.8796 | 0.876 | −0.4% | −0.0158 to +0.0087 | no |
| Omni's own CPU (cores), mean | 0.0364 | 0.01417 | −61.1% | −0.0256 to −0.0188 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.916 | 0.8902 | −2.8% | −0.0390 to −0.0126 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 753 | 753.6 | +0.1% | −8.9531 to +10.1861 | no |
| HPA replicas, mean | 9.003 | 7.727 | −14.2% | −1.9747 to −0.5754 | yes: GAIN |
| pods started | 5.3 | 4 | −24.5% | −2.5181 to −0.0819 | yes: GAIN |
| pod start wait, total (s) | 9 | 5.7 | −36.7% | −5.2090 to −1.3910 | yes: GAIN |
| pod start wait, mean (s) | 1.742 | 1.452 | −16.7% | −0.7100 to +0.1295 | no |
| host CPU busy, the real machine under kind (%) | 28.24 | 27.24 | −3.6% | −1.5225 to −0.4942 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.0% | −0.0022 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.6 | −0.1% | −0.3684 to +0.2047 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.6 | −0.1% | −0.3684 to +0.2047 | no |
| response time (ms), mean | 79.97 | 78.78 | −1.5% | −2.3887 to −0.0018 | yes: GAIN |
| response time (ms), 95th percentile | 121.4 | 118 | −2.8% | −7.8763 to +1.0253 | no |
| response time (ms), 99th percentile | 169.2 | 167.8 | −0.8% | −16.9150 to +14.1384 | no |
| time over the response line (% of samples) | 0.0847 | 0 | −100.0% | −0.1926 to +0.0232 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 21.7 | 20.3 | −6.5% | −4.9876 to +2.1876 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 70 | 100 | +42.9% | −4.5526 to +64.5526 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1633 | 0.2683 | +64.3% | −0.1700 to +0.3800 | no |
| utilisation (used / allocatable) | 0.03665 | 0.03653 | −0.3% | −0.0007 to +0.0004 | no |
| CPU used (cores), mean | 0.8796 | 0.8767 | −0.3% | −0.0162 to +0.0104 | no |
| Omni's own CPU (cores), mean | 0.0364 | 0.02553 | −29.9% | −0.0133 to −0.0085 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.916 | 0.9022 | −1.5% | −0.0282 to +0.0006 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 753 | 752.3 | −0.1% | −19.0444 to +17.6818 | no |
| HPA replicas, mean | 9.003 | 8.413 | −6.5% | −1.2103 to +0.0315 | no |
| pods started | 5.3 | 4.4 | −17.0% | −1.9366 to +0.1366 | no |
| pod start wait, total (s) | 9 | 7 | −22.2% | −4.0232 to +0.0232 | no |
| pod start wait, mean (s) | 1.742 | 1.67 | −4.1% | −0.2203 to +0.0765 | no |
| host CPU busy, the real machine under kind (%) | 28.24 | 27.89 | −1.3% | −0.9212 to +0.2071 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.516 | +0.1% | −0.0012 to +0.0035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.9 | +0.1% | −0.0536 to +0.4811 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.9 | +0.1% | −0.0536 to +0.4811 | no |
| response time (ms), mean | 79.97 | 79.46 | −0.6% | −1.3606 to +0.3372 | no |
| response time (ms), 95th percentile | 121.4 | 121.5 | +0.0% | −3.6916 to +3.7456 | no |
| response time (ms), 99th percentile | 169.2 | 169.8 | +0.3% | −16.5877 to +17.7659 | no |
| time over the response line (% of samples) | 0.0847 | 0 | −100.0% | −0.1926 to +0.0232 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 21.7 | 21.3 | −1.8% | −4.7340 to +3.9340 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 70 | 100 | +42.9% | −4.5526 to +64.5526 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1633 | 0.275 | +68.4% | −0.2526 to +0.4759 | no |
| utilisation (used / allocatable) | 0.03665 | 0.03707 | +1.1% | −0.0001 to +0.0009 | no |
| CPU used (cores), mean | 0.8796 | 0.8897 | +1.1% | −0.0018 to +0.0220 | no |
| Omni's own CPU (cores), mean | 0.0364 | 0.06973 | +91.6% | +0.0291 to +0.0376 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.916 | 0.9594 | +4.7% | +0.0298 to +0.0571 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 753 | 744.1 | −1.2% | −18.6817 to +0.9969 | no |
| HPA replicas, mean | 9.003 | 8.643 | −4.0% | −1.0663 to +0.3481 | no |
| pods started | 5.3 | 3.9 | −26.4% | −2.7572 to −0.0428 | yes: GAIN |
| pod start wait, total (s) | 9 | 5.8 | −35.6% | −6.0373 to −0.3627 | yes: GAIN |
| pod start wait, mean (s) | 1.742 | 1.531 | −12.1% | −0.4723 to +0.0504 | no |
| host CPU busy, the real machine under kind (%) | 28.24 | 29.61 | +4.8% | +1.0295 to +1.7058 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*