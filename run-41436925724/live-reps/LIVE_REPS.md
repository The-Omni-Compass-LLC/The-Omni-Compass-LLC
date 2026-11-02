# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.51 | 1.51 | 1.51 | 1.511 | 1.509 | 1.511 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | 158.9 | 158.9 | 159.1 | 158.8 | 159.1 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | 158.9 | 158.9 | 159.1 | 158.8 | 159.1 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 171.8 | 86.97 | 85.23 | 84.82 | 86.14 | 85.63 | 86.6 | 87.89 |
| response time (ms), 95th percentile | 387.3 | 134.1 | 130 | 128.4 | 131.2 | 129.4 | 131.2 | 134.7 |
| response time (ms), 99th percentile | 621.9 | 187.7 | 183.2 | 170.2 | 176.8 | 183.9 | 184.9 | 189.9 |
| time over the response line (% of samples) | 2.727 | 0.02424 | 0.01212 | 0.03636 | 0.0119 | 0.01212 | 0.03651 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | 15.7 | 16.3 | 18.8 | 18.7 | 22.5 | 21.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | nan | nan | nan | nan | 80 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.19 | 0.32 | 0.3033 | 0.1617 | 0.055 | 0.2783 | 0.3617 |
| utilisation (used / allocatable) | 0.04171 | 0.03976 | 0.03951 | 0.03949 | 0.04008 | 0.03965 | 0.03982 | 0.04018 |
| CPU used (cores), mean | 1.001 | 0.9542 | 0.9483 | 0.9477 | 0.9619 | 0.9516 | 0.9558 | 0.9643 |
| Omni's own CPU (cores), mean | 0 | 0.03937 | 0.00651 | 0.0073 | 0.00847 | 0.01542 | 0.02759 | 0.07481 |
| CPU used with Omni's own (cores), mean | 1.001 | 0.9935 | 0.9548 | 0.955 | 0.9704 | 0.967 | 0.9834 | 1.039 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 684.7 | 688.8 | 690.3 | 681.5 | 687.3 | 686 | 678.1 |
| HPA replicas, mean | 8.727 | 9.361 | 8.789 | 8.213 | 8.203 | 8.149 | 9.1 | 9.024 |
| pods started | 5 | 3.6 | 3.6 | 2.8 | 2.9 | 2.9 | 4 | 3.9 |
| pod start wait, total (s) | 7.5 | 5.2 | 4.3 | 4.7 | 4.8 | 4.5 | 7.3 | 5.6 |
| pod start wait, mean (s) | 1.583 | 1.353 | 1.107 | 1.672 | 1.682 | 1.597 | 1.837 | 1.353 |
| host CPU busy, the real machine under kind (%) | 30.34 | 30.65 | 29.12 | 29.18 | 29.51 | 29.48 | 30.21 | 32.06 |
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
| node-hours | 1.51 | 1.51 | +0.0% | −0.0011 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | −0.2% | −0.7344 to −0.0618 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | −0.2% | −0.7344 to −0.0618 | yes: GAIN |
| response time (ms), mean | 171.8 | 86.97 | −49.4% | −105.1077 to −64.6027 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 134.1 | −65.4% | −309.4315 to −197.1075 | yes: GAIN |
| response time (ms), 99th percentile | 621.9 | 187.7 | −69.8% | −533.7761 to −334.6475 | yes: GAIN |
| time over the response line (% of samples) | 2.727 | 0.02424 | −99.1% | −3.8797 to −1.5259 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.300 (native is 0) | +16.6989 to +23.9011 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.19 | −28.3% | −0.2950 to +0.1450 | no |
| utilisation (used / allocatable) | 0.04171 | 0.03976 | −4.7% | −0.0031 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9542 | −4.7% | −0.0743 to −0.0196 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03937 | +0.039 (native is 0) | +0.0345 to +0.0442 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 0.9935 | −0.8% | −0.0311 to +0.0158 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 684.7 | +3.1% | −0.7752 to +42.5647 | no |
| HPA replicas, mean | 8.727 | 9.361 | +7.3% | +0.0520 to +1.2175 | yes: power given |
| pods started | 5 | 3.6 | −28.0% | −2.7985 to −0.0015 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 5.2 | −30.7% | −5.3730 to +0.7730 | no |
| pod start wait, mean (s) | 1.583 | 1.353 | −14.5% | −0.7148 to +0.2548 | no |
| host CPU busy, the real machine under kind (%) | 30.34 | 30.65 | +1.0% | −0.3240 to +0.9330 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.51 | −0.0% | −0.0016 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | −0.3% | −0.8209 to −0.1600 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | −0.3% | −0.8209 to −0.1600 | yes: GAIN |
| response time (ms), mean | 171.8 | 85.23 | −50.4% | −107.1569 to −66.0363 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 130 | −66.4% | −314.4241 to −200.3089 | yes: GAIN |
| response time (ms), 99th percentile | 621.9 | 183.2 | −70.5% | −537.8605 to −339.5463 | yes: GAIN |
| time over the response line (% of samples) | 2.727 | 0.01212 | −99.6% | −3.9083 to −1.5215 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.7 | +15.700 (native is 0) | +14.8047 to +16.5953 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.32 | +20.8% | −0.3236 to +0.4336 | no |
| utilisation (used / allocatable) | 0.04171 | 0.03951 | −5.3% | −0.0034 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9483 | −5.3% | −0.0805 to −0.0251 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00651 | +0.007 (native is 0) | +0.0058 to +0.0072 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 0.9548 | −4.6% | −0.0734 to −0.0192 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 688.8 | +3.8% | +3.5891 to +46.2600 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.727 | 8.789 | +0.7% | −0.1387 to +0.2631 | no |
| pods started | 5 | 3.6 | −28.0% | −2.3048 to −0.4952 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 4.3 | −42.7% | −5.1015 to −1.2985 | yes: GAIN |
| pod start wait, mean (s) | 1.583 | 1.107 | −30.1% | −1.0209 to +0.0675 | no |
| host CPU busy, the real machine under kind (%) | 30.34 | 29.12 | −4.0% | −2.0645 to −0.3814 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.51 | −0.0% | −0.0014 to +0.0010 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | −0.3% | −0.7517 to −0.1657 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | −0.3% | −0.7517 to −0.1657 | yes: GAIN |
| response time (ms), mean | 171.8 | 84.82 | −50.6% | −107.7571 to −66.2499 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 128.4 | −66.8% | −316.8249 to −201.0011 | yes: GAIN |
| response time (ms), 99th percentile | 621.9 | 170.2 | −72.6% | −557.4606 to −345.9374 | yes: GAIN |
| time over the response line (% of samples) | 2.727 | 0.03636 | −98.7% | −3.8828 to −1.4986 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 | +16.300 (native is 0) | +13.5389 to +19.0611 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.3033 | +14.5% | −0.3804 to +0.4571 | no |
| utilisation (used / allocatable) | 0.04171 | 0.03949 | −5.3% | −0.0034 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9477 | −5.3% | −0.0812 to −0.0258 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0073 | +0.007 (native is 0) | +0.0063 to +0.0083 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 0.955 | −4.6% | −0.0731 to −0.0192 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 690.3 | +4.0% | +6.6109 to +46.2220 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.727 | 8.213 | −5.9% | −1.4941 to +0.4675 | no |
| pods started | 5 | 2.8 | −44.0% | −3.4972 to −0.9028 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 4.7 | −37.3% | −5.0060 to −0.5940 | yes: GAIN |
| pod start wait, mean (s) | 1.583 | 1.672 | +5.6% | −0.1665 to +0.3432 | no |
| host CPU busy, the real machine under kind (%) | 30.34 | 29.18 | −3.8% | −1.9565 to −0.3689 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.511 | +0.0% | −0.0007 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | −0.2% | −0.6464 to +0.0563 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.1 | −0.2% | −0.6464 to +0.0563 | no |
| response time (ms), mean | 171.8 | 86.14 | −49.9% | −106.2262 to −65.1410 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 131.2 | −66.1% | −313.0661 to −199.1729 | yes: GAIN |
| response time (ms), 99th percentile | 621.9 | 176.8 | −71.6% | −549.4089 to −340.7723 | yes: GAIN |
| time over the response line (% of samples) | 2.727 | 0.0119 | −99.6% | −3.9207 to −1.5096 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | +18.800 (native is 0) | +15.8449 to +21.7551 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.1617 | −39.0% | −0.3057 to +0.0990 | no |
| utilisation (used / allocatable) | 0.04171 | 0.04008 | −3.9% | −0.0029 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9619 | −3.9% | −0.0686 to −0.0099 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00847 | +0.008 (native is 0) | +0.0073 to +0.0097 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 0.9704 | −3.1% | −0.0595 to −0.0021 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 681.5 | +2.7% | −4.2408 to +39.4616 | no |
| HPA replicas, mean | 8.727 | 8.203 | −6.0% | −1.1185 to +0.0707 | no |
| pods started | 5 | 2.9 | −42.0% | −2.8872 to −1.3128 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 4.8 | −36.0% | −4.7246 to −0.6754 | yes: GAIN |
| pod start wait, mean (s) | 1.583 | 1.682 | +6.2% | −0.2140 to +0.4107 | no |
| host CPU busy, the real machine under kind (%) | 30.34 | 29.51 | −2.7% | −1.7543 to +0.0858 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.509 | −0.1% | −0.0024 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | −0.4% | −0.8890 to −0.3024 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | −0.4% | −0.8890 to −0.3024 | yes: GAIN |
| response time (ms), mean | 171.8 | 85.63 | −50.2% | −106.9271 to −65.4746 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 129.4 | −66.6% | −315.7580 to −200.1590 | yes: GAIN |
| response time (ms), 99th percentile | 621.9 | 183.9 | −70.4% | −538.4808 to −337.5376 | yes: GAIN |
| time over the response line (% of samples) | 2.727 | 0.01212 | −99.6% | −3.9083 to −1.5215 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.700 (native is 0) | +15.9389 to +21.4611 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.055 | −79.2% | −0.4430 to +0.0230 | no |
| utilisation (used / allocatable) | 0.04171 | 0.03965 | −5.0% | −0.0030 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9516 | −5.0% | −0.0727 to −0.0265 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01542 | +0.015 (native is 0) | +0.0134 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 0.967 | −3.4% | −0.0554 to −0.0129 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 687.3 | +3.5% | +2.4215 to +44.4197 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.727 | 8.149 | −6.6% | −1.0648 to −0.0908 | yes: GAIN |
| pods started | 5 | 2.9 | −42.0% | −2.8872 to −1.3128 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 4.5 | −40.0% | −4.6171 to −1.3829 | yes: GAIN |
| pod start wait, mean (s) | 1.583 | 1.597 | +0.8% | −0.2135 to +0.2401 | no |
| host CPU busy, the real machine under kind (%) | 30.34 | 29.48 | −2.8% | −1.5898 to −0.1292 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.511 | +0.1% | +0.0000 to +0.0023 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | −0.2% | −0.5106 to −0.0571 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.1 | −0.2% | −0.5106 to −0.0571 | yes: GAIN |
| response time (ms), mean | 171.8 | 86.6 | −49.6% | −105.5453 to −64.9119 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 131.2 | −66.1% | −312.5924 to −199.7116 | yes: GAIN |
| response time (ms), 99th percentile | 621.9 | 184.9 | −70.3% | −534.1615 to −339.7997 | yes: GAIN |
| time over the response line (% of samples) | 2.727 | 0.03651 | −98.7% | −3.8670 to −1.5141 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.5 | +22.500 (native is 0) | +17.3722 to +27.6278 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.2783 | +5.0% | −0.2344 to +0.2610 | no |
| utilisation (used / allocatable) | 0.04171 | 0.03982 | −4.5% | −0.0028 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9558 | −4.5% | −0.0666 to −0.0241 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02759 | +0.028 (native is 0) | +0.0240 to +0.0312 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 0.9834 | −1.8% | −0.0359 to +0.0003 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 686 | +3.3% | +6.2405 to +38.0302 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.727 | 9.1 | +4.3% | −0.2936 to +1.0404 | no |
| pods started | 5 | 4 | −20.0% | −2.6171 to +0.6171 | no |
| pod start wait, total (s) | 7.5 | 7.3 | −2.7% | −4.0269 to +3.6269 | no |
| pod start wait, mean (s) | 1.583 | 1.837 | +16.0% | −0.1441 to +0.6519 | no |
| host CPU busy, the real machine under kind (%) | 30.34 | 30.21 | −0.4% | −0.6668 to +0.3999 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.509 | −0.1% | −0.0067 to +0.0040 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | −0.3% | −0.8922 to −0.0279 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | −0.3% | −0.8922 to −0.0279 | yes: GAIN |
| response time (ms), mean | 171.8 | 87.89 | −48.8% | −104.0924 to −63.7709 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 134.7 | −65.2% | −308.1021 to −197.0999 | yes: GAIN |
| response time (ms), 99th percentile | 621.9 | 189.9 | −69.5% | −526.2409 to −337.7041 | yes: GAIN |
| time over the response line (% of samples) | 2.727 | 0.01212 | −99.6% | −3.9019 to −1.5280 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.7 | +21.700 (native is 0) | +19.8826 to +23.5174 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.3617 | +36.5% | −0.3698 to +0.5631 | no |
| utilisation (used / allocatable) | 0.04171 | 0.04018 | −3.7% | −0.0026 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9643 | −3.7% | −0.0631 to −0.0106 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07481 | +0.075 (native is 0) | +0.0659 to +0.0837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 1.039 | +3.8% | +0.0181 to +0.0577 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 663.9 | 678.1 | +2.1% | −9.7052 to +38.2388 | no |
| HPA replicas, mean | 8.727 | 9.024 | +3.4% | −0.0087 to +0.6034 | no |
| pods started | 5 | 3.9 | −22.0% | −1.9564 to −0.2436 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 5.6 | −25.3% | −4.3421 to +0.5421 | no |
| pod start wait, mean (s) | 1.583 | 1.353 | −14.5% | −0.6767 to +0.2167 | no |
| host CPU busy, the real machine under kind (%) | 30.34 | 32.06 | +5.7% | +1.1055 to +2.3248 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.51 | −0.0% | −0.0023 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.9 | −0.1% | −0.3413 to +0.1567 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.9 | −0.1% | −0.3413 to +0.1567 | no |
| response time (ms), mean | 86.97 | 85.23 | −2.0% | −2.7983 to −0.6845 | yes: GAIN |
| response time (ms), 95th percentile | 134.1 | 130 | −3.1% | −6.8006 to −1.3934 | yes: GAIN |
| response time (ms), 99th percentile | 187.7 | 183.2 | −2.4% | −14.0454 to +5.0622 | no |
| time over the response line (% of samples) | 0.02424 | 0.01212 | −50.0% | −0.0613 to +0.0371 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.3 | 15.7 | −22.7% | −8.3428 to −0.8572 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.32 | +68.4% | −0.1264 to +0.3864 | no |
| utilisation (used / allocatable) | 0.03976 | 0.03951 | −0.6% | −0.0006 to +0.0001 | no |
| CPU used (cores), mean | 0.9542 | 0.9483 | −0.6% | −0.0148 to +0.0031 | no |
| Omni's own CPU (cores), mean | 0.03937 | 0.00651 | −83.5% | −0.0370 to −0.0287 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9935 | 0.9548 | −3.9% | −0.0491 to −0.0283 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684.7 | 688.8 | +0.6% | −1.0891 to +9.1486 | no |
| HPA replicas, mean | 9.361 | 8.789 | −6.1% | −1.1014 to −0.0437 | yes: GAIN |
| pods started | 3.6 | 3.6 | ±0.0% | −1.5080 to +1.5080 | no |
| pod start wait, total (s) | 5.2 | 4.3 | −17.3% | −3.5433 to +1.7433 | no |
| pod start wait, mean (s) | 1.353 | 1.107 | −18.2% | −0.8380 to +0.3447 | no |
| host CPU busy, the real machine under kind (%) | 30.65 | 29.12 | −5.0% | −1.8900 to −1.1650 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.51 | −0.0% | −0.0018 to +0.0008 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.9 | −0.0% | −0.2467 to +0.1255 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.9 | −0.0% | −0.2467 to +0.1255 | no |
| response time (ms), mean | 86.97 | 84.82 | −2.5% | −3.3723 to −0.9243 | yes: GAIN |
| response time (ms), 95th percentile | 134.1 | 128.4 | −4.2% | −9.1684 to −2.1186 | yes: GAIN |
| response time (ms), 99th percentile | 187.7 | 170.2 | −9.3% | −28.3515 to −6.6229 | yes: GAIN |
| time over the response line (% of samples) | 0.02424 | 0.03636 | +50.0% | −0.0638 to +0.0880 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.3 | 16.3 | −19.7% | −8.2519 to +0.2519 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.3033 | +59.6% | −0.1765 to +0.4031 | no |
| utilisation (used / allocatable) | 0.03976 | 0.03949 | −0.7% | −0.0008 to +0.0002 | no |
| CPU used (cores), mean | 0.9542 | 0.9477 | −0.7% | −0.0188 to +0.0058 | no |
| Omni's own CPU (cores), mean | 0.03937 | 0.0073 | −81.5% | −0.0360 to −0.0281 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9935 | 0.955 | −3.9% | −0.0517 to −0.0254 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684.7 | 690.3 | +0.8% | −2.6125 to +13.6558 | no |
| HPA replicas, mean | 9.361 | 8.213 | −12.3% | −2.0452 to −0.2510 | yes: GAIN |
| pods started | 3.6 | 2.8 | −22.2% | −2.6096 to +1.0096 | no |
| pod start wait, total (s) | 5.2 | 4.7 | −9.6% | −3.6316 to +2.6316 | no |
| pod start wait, mean (s) | 1.353 | 1.672 | +23.5% | −0.2315 to +0.8681 | no |
| host CPU busy, the real machine under kind (%) | 30.65 | 29.18 | −4.8% | −1.7290 to −1.2055 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.511 | +0.0% | −0.0012 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.1 | +0.1% | −0.1658 to +0.3720 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.1 | +0.1% | −0.1658 to +0.3720 | no |
| response time (ms), mean | 86.97 | 86.14 | −1.0% | −2.0233 to +0.3665 | no |
| response time (ms), 95th percentile | 134.1 | 131.2 | −2.1% | −5.2041 to −0.4959 | yes: GAIN |
| response time (ms), 99th percentile | 187.7 | 176.8 | −5.8% | −21.3889 to −0.3687 | yes: GAIN |
| time over the response line (% of samples) | 0.02424 | 0.0119 | −50.9% | −0.0612 to +0.0365 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.3 | 18.8 | −7.4% | −5.7015 to +2.7015 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.1617 | −14.9% | −0.1952 to +0.1386 | no |
| utilisation (used / allocatable) | 0.03976 | 0.04008 | +0.8% | −0.0006 to +0.0013 | no |
| CPU used (cores), mean | 0.9542 | 0.9619 | +0.8% | −0.0148 to +0.0302 | no |
| Omni's own CPU (cores), mean | 0.03937 | 0.00847 | −78.5% | −0.0346 to −0.0272 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9935 | 0.9704 | −2.3% | −0.0456 to −0.0007 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684.7 | 681.5 | −0.5% | −15.7243 to +9.1556 | no |
| HPA replicas, mean | 9.361 | 8.203 | −12.4% | −1.7414 to −0.5759 | yes: GAIN |
| pods started | 3.6 | 2.9 | −19.4% | −2.0509 to +0.6509 | no |
| pod start wait, total (s) | 5.2 | 4.8 | −7.7% | −2.8362 to +2.0362 | no |
| pod start wait, mean (s) | 1.353 | 1.682 | +24.3% | −0.1971 to +0.8537 | no |
| host CPU busy, the real machine under kind (%) | 30.65 | 29.51 | −3.7% | −1.6688 to −0.6087 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.51 | 1.509 | −0.1% | −0.0032 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.8 | −0.1% | −0.4374 to +0.0423 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.8 | −0.1% | −0.4374 to +0.0423 | no |
| response time (ms), mean | 86.97 | 85.63 | −1.5% | −2.0903 to −0.6009 | yes: GAIN |
| response time (ms), 95th percentile | 134.1 | 129.4 | −3.5% | −7.7046 to −1.6734 | yes: GAIN |
| response time (ms), 99th percentile | 187.7 | 183.9 | −2.0% | −13.2483 to +5.6535 | no |
| time over the response line (% of samples) | 0.02424 | 0.01212 | −50.0% | −0.0613 to +0.0371 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.3 | 18.7 | −7.9% | −6.5236 to +3.3236 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.055 | −71.1% | −0.3417 to +0.0717 | no |
| utilisation (used / allocatable) | 0.03976 | 0.03965 | −0.3% | −0.0007 to +0.0005 | no |
| CPU used (cores), mean | 0.9542 | 0.9516 | −0.3% | −0.0167 to +0.0116 | no |
| Omni's own CPU (cores), mean | 0.03937 | 0.01542 | −60.8% | −0.0268 to −0.0211 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9935 | 0.967 | −2.7% | −0.0407 to −0.0124 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684.7 | 687.3 | +0.4% | −6.6558 to +11.7074 | no |
| HPA replicas, mean | 9.361 | 8.149 | −13.0% | −1.7080 to −0.7171 | yes: GAIN |
| pods started | 3.6 | 2.9 | −19.4% | −2.0924 to +0.6924 | no |
| pod start wait, total (s) | 5.2 | 4.5 | −13.5% | −3.2019 to +1.8019 | no |
| pod start wait, mean (s) | 1.353 | 1.597 | +18.0% | −0.2719 to +0.7585 | no |
| host CPU busy, the real machine under kind (%) | 30.65 | 29.48 | −3.8% | −1.4317 to −0.8964 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.511 | +0.1% | −0.0006 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.1 | +0.1% | −0.1396 to +0.3682 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.1 | +0.1% | −0.1396 to +0.3682 | no |
| response time (ms), mean | 86.97 | 86.6 | −0.4% | −1.3823 to +0.6355 | no |
| response time (ms), 95th percentile | 134.1 | 131.2 | −2.2% | −5.1870 to −0.5780 | yes: GAIN |
| response time (ms), 99th percentile | 187.7 | 184.9 | −1.5% | −15.7612 to +10.2236 | no |
| time over the response line (% of samples) | 0.02424 | 0.03651 | +50.6% | −0.0371 to +0.0617 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.3 | 22.5 | +10.8% | −4.2580 to +8.6580 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 80 | ±0.0% | −33.7199 to +33.7199 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.2783 | +46.5% | −0.0717 to +0.2484 | no |
| utilisation (used / allocatable) | 0.03976 | 0.03982 | +0.2% | −0.0005 to +0.0007 | no |
| CPU used (cores), mean | 0.9542 | 0.9558 | +0.2% | −0.0128 to +0.0161 | no |
| Omni's own CPU (cores), mean | 0.03937 | 0.02759 | −29.9% | −0.0137 to −0.0099 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9935 | 0.9834 | −1.0% | −0.0252 to +0.0049 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684.7 | 686 | +0.2% | −8.3718 to +10.8529 | no |
| HPA replicas, mean | 9.361 | 9.1 | −2.8% | −0.9791 to +0.4564 | no |
| pods started | 3.6 | 4 | +11.1% | −1.4221 to +2.2221 | no |
| pod start wait, total (s) | 5.2 | 7.3 | +40.4% | −1.6007 to +5.8007 | no |
| pod start wait, mean (s) | 1.353 | 1.837 | +35.8% | +0.0395 to +0.9282 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.65 | 30.21 | −1.4% | −0.8529 to −0.0231 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.509 | −0.1% | −0.0075 to +0.0041 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.9 | −0.0% | −0.6952 to +0.5713 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.9 | −0.0% | −0.6952 to +0.5713 | no |
| response time (ms), mean | 86.97 | 87.89 | +1.1% | −0.3347 to +2.1819 | no |
| response time (ms), 95th percentile | 134.1 | 134.7 | +0.5% | −0.9521 to +2.2891 | no |
| response time (ms), 99th percentile | 187.7 | 189.9 | +1.2% | −8.4551 to +12.9337 | no |
| time over the response line (% of samples) | 0.02424 | 0.01212 | −50.0% | −0.0613 to +0.0371 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.3 | 21.7 | +6.9% | −2.5063 to +5.3063 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 80 | 90 | +12.5% | −30.6041 to +50.6041 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.3617 | +90.4% | −0.1736 to +0.5169 | no |
| utilisation (used / allocatable) | 0.03976 | 0.04018 | +1.1% | +0.0000 to +0.0008 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9542 | 0.9643 | +1.1% | +0.0006 to +0.0196 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03937 | 0.07481 | +90.0% | +0.0312 to +0.0397 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9935 | 1.039 | +4.6% | +0.0337 to +0.0574 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684.7 | 678.1 | −1.0% | −12.6110 to −0.6450 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.361 | 9.024 | −3.6% | −1.0359 to +0.3611 | no |
| pods started | 3.6 | 3.9 | +8.3% | −1.0081 to +1.6081 | no |
| pod start wait, total (s) | 5.2 | 5.6 | +7.7% | −2.2163 to +3.0163 | no |
| pod start wait, mean (s) | 1.353 | 1.353 | ±0.0% | −0.4290 to +0.4290 | no |
| host CPU busy, the real machine under kind (%) | 30.65 | 32.06 | +4.6% | +1.0066 to +1.8147 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*