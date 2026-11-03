# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.507 | 1.507 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 | 159.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 | 159.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 161.5 | 83.04 | 87.01 |
| response time (ms), 95th percentile | 358.6 | 123.8 | 121.5 |
| response time (ms), 99th percentile | 563.5 | 165.6 | 159.6 |
| time over the response line (% of samples) | 2.334 | 0.02432 | 0.2922 |
| failed requests (%) | 0 | 0 | 0.1117 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | 25.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.3517 | 0 |
| utilisation (used / allocatable) | 0.04019 | 0.03866 | 0.03926 |
| CPU used (cores), mean | 0.9644 | 0.9278 | 0.9422 |
| Omni's own CPU (cores), mean | 0 | 0.03803 | 0.03807 |
| CPU used with Omni's own (cores), mean | 0.9644 | 0.9659 | 0.9803 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.9 | 711.7 | 703.3 |
| HPA replicas, mean | 8.579 | 9.068 | 9.419 |
| pods started | 5.5 | 4.1 | 10 |
| pod start wait, total (s) | 8.8 | 6.9 | 18.2 |
| pod start wait, mean (s) | 1.602 | 1.571 | 1.824 |
| host CPU busy, the real machine under kind (%) | 29.5 | 29.54 | 30.22 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.507 | 1.507 | +0.0% | −0.0023 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 | −0.2% | −0.7627 to +0.0592 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 | −0.2% | −0.7627 to +0.0592 | no |
| response time (ms), mean | 161.5 | 83.04 | −48.6% | −102.5460 to −54.3232 | yes: GAIN |
| response time (ms), 95th percentile | 358.6 | 123.8 | −65.5% | −295.6916 to −173.7714 | yes: GAIN |
| response time (ms), 99th percentile | 563.5 | 165.6 | −70.6% | −503.5525 to −292.1847 | yes: GAIN |
| time over the response line (% of samples) | 2.334 | 0.02432 | −99.0% | −3.6439 to −0.9747 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.7326 to −0.8674 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.500 (native is 0) | +17.6150 to +21.3850 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.3517 | +64.8% | −0.1224 to +0.3991 | no |
| utilisation (used / allocatable) | 0.04019 | 0.03866 | −3.8% | −0.0025 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9644 | 0.9278 | −3.8% | −0.0590 to −0.0142 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03803 | +0.038 (native is 0) | +0.0337 to +0.0424 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9644 | 0.9659 | +0.1% | −0.0180 to +0.0209 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.9 | 711.7 | +2.7% | +5.8043 to +31.8432 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.579 | 9.068 | +5.7% | +0.1100 to +0.8674 | yes: power given |
| pods started | 5.5 | 4.1 | −25.5% | −2.5778 to −0.2222 | yes: GAIN |
| pod start wait, total (s) | 8.8 | 6.9 | −21.6% | −4.1982 to +0.3982 | no |
| pod start wait, mean (s) | 1.602 | 1.571 | −1.9% | −0.5255 to +0.4631 | no |
| host CPU busy, the real machine under kind (%) | 29.5 | 29.54 | +0.1% | −0.6568 to +0.7388 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.507 | 1.513 | +0.4% | +0.0034 to +0.0082 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.1 | +0.2% | +0.0521 to +0.7085 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.1 | +0.2% | +0.0521 to +0.7085 | yes: power given |
| response time (ms), mean | 161.5 | 87.01 | −46.1% | −98.4269 to −50.4879 | yes: GAIN |
| response time (ms), 95th percentile | 358.6 | 121.5 | −66.1% | −299.7530 to −174.2850 | yes: GAIN |
| response time (ms), 99th percentile | 563.5 | 159.6 | −71.7% | −517.6059 to −290.3113 | yes: GAIN |
| time over the response line (% of samples) | 2.334 | 0.2922 | −87.5% | −3.3926 to −0.6902 | yes: GAIN |
| failed requests (%) | 0 | 0.1117 | +0.112 (native is 0) | +0.0339 to +0.1895 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0.4 | −82.6% | −3.4249 to −0.3751 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.7 | +25.700 (native is 0) | +20.6640 to +30.7360 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0 | −100.0% | −0.4478 to +0.0211 | no |
| utilisation (used / allocatable) | 0.04019 | 0.03926 | −2.3% | −0.0015 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9644 | 0.9422 | −2.3% | −0.0372 to −0.0073 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03807 | +0.038 (native is 0) | +0.0342 to +0.0420 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9644 | 0.9803 | +1.6% | +0.0036 to +0.0281 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.9 | 703.3 | +1.5% | +1.0439 to +19.8044 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.579 | 9.419 | +9.8% | +0.7753 to +0.9054 | yes: power given |
| pods started | 5.5 | 10 | +81.8% | +3.7274 to +5.2726 | yes: power given |
| pod start wait, total (s) | 8.8 | 18.2 | +106.8% | +6.5950 to +12.2050 | yes: LOSS |
| pod start wait, mean (s) | 1.602 | 1.824 | +13.8% | +0.0048 to +0.4377 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 29.5 | 30.22 | +2.4% | +0.2383 to +1.1985 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.507 | 1.513 | +0.4% | +0.0040 to +0.0074 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 159.1 | +0.5% | +0.5554 to +0.9086 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 159.1 | +0.5% | +0.5554 to +0.9086 | yes: power given |
| response time (ms), mean | 83.04 | 87.01 | +4.8% | +0.7536 to +7.2008 | yes: LOSS |
| response time (ms), 95th percentile | 123.8 | 121.5 | −1.8% | −5.4115 to +0.8365 | no |
| response time (ms), 99th percentile | 165.6 | 159.6 | −3.7% | −19.8731 to +7.6931 | no |
| time over the response line (% of samples) | 0.02432 | 0.2922 | +1101.6% | +0.2335 to +0.3022 | yes: LOSS |
| failed requests (%) | 0 | 0.1117 | +0.112 (native is 0) | +0.0339 to +0.1895 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 19.5 | 25.7 | +31.8% | +1.1443 to +11.2557 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 33.33 | −66.7% | −120.8681 to −12.4652 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3517 | 0 | −100.0% | −0.5742 to −0.1292 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03866 | 0.03926 | +1.5% | +0.0001 to +0.0011 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9278 | 0.9422 | +1.5% | +0.0028 to +0.0259 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03803 | 0.03807 | +0.1% | −0.0007 to +0.0008 | no |
| CPU used with Omni's own (cores), mean | 0.9659 | 0.9803 | +1.5% | +0.0030 to +0.0258 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711.7 | 703.3 | −1.2% | −14.5837 to −2.2155 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.068 | 9.419 | +3.9% | −0.0392 to +0.7424 | no |
| pods started | 4.1 | 10 | +143.9% | +4.5324 to +7.2676 | yes: power given |
| pod start wait, total (s) | 6.9 | 18.2 | +163.8% | +8.2270 to +14.3730 | yes: LOSS |
| pod start wait, mean (s) | 1.571 | 1.824 | +16.1% | −0.1739 to +0.6789 | no |
| host CPU busy, the real machine under kind (%) | 29.54 | 30.22 | +2.3% | +0.3532 to +1.0016 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*