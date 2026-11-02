# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.512 | 1.514 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 144 | 75 | 77.18 |
| response time (ms), 95th percentile | 337.4 | 113.7 | 113.2 |
| response time (ms), 99th percentile | 543.1 | 159.8 | 145.3 |
| time over the response line (% of samples) | 2.522 | 0.0122 | 0.1466 |
| failed requests (%) | 0 | 0 | 0.08627 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.4 | 19.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.1367 | 0.76 |
| utilisation (used / allocatable) | 0.03663 | 0.03456 | 0.03541 |
| CPU used (cores), mean | 0.879 | 0.8294 | 0.8499 |
| Omni's own CPU (cores), mean | 0 | 0.00858 | 0.00864 |
| CPU used with Omni's own (cores), mean | 0.879 | 0.838 | 0.8585 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.5 | 829.4 | 821.6 |
| HPA replicas, mean | 8.085 | 7.679 | 9.516 |
| pods started | 5.2 | 2.6 | 9.2 |
| pod start wait, total (s) | 7.3 | 3.8 | 16.9 |
| pod start wait, mean (s) | 1.426 | 1.433 | 1.84 |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.13 | 26.59 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.514 | +0.1% | +0.0003 to +0.0040 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | −0.1% | −0.6001 to +0.1491 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | −0.1% | −0.6001 to +0.1491 | no |
| response time (ms), mean | 144 | 75 | −47.9% | −99.4415 to −38.4952 | yes: GAIN |
| response time (ms), 95th percentile | 337.4 | 113.7 | −66.3% | −313.9207 to −133.5083 | yes: GAIN |
| response time (ms), 99th percentile | 543.1 | 159.8 | −70.6% | −536.8156 to −229.7812 | yes: GAIN |
| time over the response line (% of samples) | 2.522 | 0.0122 | −99.5% | −4.0747 to −0.9457 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.8099 to −0.7901 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.4 | +14.400 (native is 0) | +11.4373 to +17.3627 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.1367 | −69.4% | −0.5772 to −0.0428 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03663 | 0.03456 | −5.6% | −0.0034 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.879 | 0.8294 | −5.6% | −0.0825 to −0.0167 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00858 | +0.009 (native is 0) | +0.0069 to +0.0103 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.879 | 0.838 | −4.7% | −0.0723 to −0.0097 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.5 | 829.4 | +3.1% | +4.3570 to +45.3702 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.085 | 7.679 | −5.0% | −1.1192 to +0.3076 | no |
| pods started | 5.2 | 2.6 | −50.0% | −3.4396 to −1.7604 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 3.8 | −47.9% | −5.4444 to −1.5556 | yes: GAIN |
| pod start wait, mean (s) | 1.426 | 1.433 | +0.5% | −0.3505 to +0.3657 | no |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.13 | −2.2% | −1.2612 to +0.1062 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.515 | +0.2% | −0.0046 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.4 | +0.0% | −0.6761 to +0.7317 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.4 | +0.0% | −0.6761 to +0.7317 | no |
| response time (ms), mean | 144 | 77.18 | −46.4% | −96.2368 to −37.3414 | yes: GAIN |
| response time (ms), 95th percentile | 337.4 | 113.2 | −66.5% | −314.2089 to −134.2911 | yes: GAIN |
| response time (ms), 99th percentile | 543.1 | 145.3 | −73.3% | −555.7886 to −239.9808 | yes: GAIN |
| time over the response line (% of samples) | 2.522 | 0.1466 | −94.2% | −3.8961 to −0.8556 | yes: GAIN |
| failed requests (%) | 0 | 0.08627 | +0.086 (native is 0) | +0.0267 to +0.1458 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.8099 to −0.7901 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +15.1012 to +23.4988 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.76 | +70.1% | −0.2815 to +0.9081 | no |
| utilisation (used / allocatable) | 0.03663 | 0.03541 | −3.3% | −0.0020 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.879 | 0.8499 | −3.3% | −0.0487 to −0.0096 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00864 | +0.009 (native is 0) | +0.0075 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.879 | 0.8585 | −2.3% | −0.0391 to −0.0019 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.5 | 821.6 | +2.1% | +4.1578 to +29.8921 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.085 | 9.516 | +17.7% | +0.8296 to +2.0339 | yes: power given |
| pods started | 5.2 | 9.2 | +76.9% | +3.5231 to +4.4769 | yes: power given |
| pod start wait, total (s) | 7.3 | 16.9 | +131.5% | +8.2015 to +10.9985 | yes: LOSS |
| pod start wait, mean (s) | 1.426 | 1.84 | +29.1% | +0.2517 to +0.5769 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.71 | 26.59 | −0.5% | −0.5280 to +0.2767 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.515 | +0.0% | −0.0069 to +0.0083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.4 | +0.2% | −0.6631 to +1.1698 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158.4 | +0.2% | −0.6631 to +1.1698 | no |
| response time (ms), mean | 75 | 77.18 | +2.9% | −0.5502 to +4.9088 | no |
| response time (ms), 95th percentile | 113.7 | 113.2 | −0.5% | −1.8380 to +0.7670 | no |
| response time (ms), 99th percentile | 159.8 | 145.3 | −9.1% | −29.1765 to +0.0039 | no |
| time over the response line (% of samples) | 0.0122 | 0.1466 | +1101.8% | +0.0582 to +0.2106 | yes: LOSS |
| failed requests (%) | 0 | 0.08627 | +0.086 (native is 0) | +0.0267 to +0.1458 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 14.4 | 19.3 | +34.0% | −2.0307 to +11.8307 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1367 | 0.76 | +456.1% | +0.1032 to +1.1435 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03456 | 0.03541 | +2.5% | +0.0000 to +0.0017 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8294 | 0.8499 | +2.5% | +0.0006 to +0.0403 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00858 | 0.00864 | +0.7% | −0.0005 to +0.0006 | no |
| CPU used with Omni's own (cores), mean | 0.838 | 0.8585 | +2.4% | +0.0011 to +0.0399 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 829.4 | 821.6 | −0.9% | −27.5761 to +11.8988 | no |
| HPA replicas, mean | 7.679 | 9.516 | +23.9% | +0.5764 to +3.0987 | yes: power given |
| pods started | 2.6 | 9.2 | +253.8% | +5.6952 to +7.5048 | yes: power given |
| pod start wait, total (s) | 3.8 | 16.9 | +344.7% | +10.2497 to +15.9503 | yes: LOSS |
| pod start wait, mean (s) | 1.433 | 1.84 | +28.4% | −0.0459 to +0.8592 | no |
| host CPU busy, the real machine under kind (%) | 26.13 | 26.59 | +1.7% | +0.0110 to +0.8927 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*