# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.754 | 4.741 |
| node-hours | 2.517 | 2.516 | 1.992 | 1.985 |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.9 | 273.9 | 273.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 273.9 | 234.8 | 234.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 417.3 | 448 | 417.7 | 443.8 |
| response time (ms), 95th percentile | 1558 | 1706 | 1782 | 1893 |
| response time (ms), 99th percentile | 2181 | 2401 | 2516 | 2636 |
| time over the response line (% of samples) | 18.72 | 19.74 | 18.93 | 20.02 |
| failed requests (%) | 0 | 0 | 0.0113 | 0.01136 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.5 | 10.1 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 124 | 128.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.9 | 12.79 | 15.81 | 16.45 |
| utilisation (used / allocatable) | 0.06336 | 0.06373 | 0.08216 | 0.08252 |
| CPU used (cores), mean | 1.521 | 1.53 | 1.523 | 1.53 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07207 | 0.07512 |
| CPU used with Omni's own (cores), mean | 1.521 | 1.53 | 1.595 | 1.605 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.9 | 438.7 | 368.2 | 366.3 |
| HPA replicas, mean | 1.961 | 1.973 | 2.356 | 2.294 |
| pods started | 0.2 | 0.2 | 1.5 | 1.4 |
| pod start wait, total (s) | 0.4 | 0.3 | 4.1 | 3.3 |
| pod start wait, mean (s) | 0.2 | 0.3 | 2.017 | 1.475 |
| host CPU busy, the real machine under kind (%) | 43.15 | 44.07 | 46.51 | 47.47 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.7 | 820 | 826.3 | 836.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.019 | 3.958 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 0.7833 | 0.3458 | 1.883 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 3.8 | 1.5 | 11.5 |
| queue: job turnaround, submitted to done, mean (s) | 117.4 | 125.9 | 130.1 | 138.5 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |
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
| worker nodes in service, mean | 6 | 4.741 | −21.0% | −2.1640 to −0.3545 | yes: GAIN |
| node-hours | 2.516 | 1.985 | −21.1% | −0.9093 to −0.1530 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.7 | −0.1% | −0.8783 to +0.4255 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 234.1 | −14.5% | −68.4520 to −11.1467 | yes: GAIN |
| response time (ms), mean | 448 | 443.8 | −0.9% | −15.1159 to +6.6153 | no |
| response time (ms), 95th percentile | 1706 | 1893 | +11.0% | +56.5342 to +317.5598 | yes: LOSS |
| response time (ms), 99th percentile | 2401 | 2636 | +9.8% | +63.6958 to +406.2692 | yes: LOSS |
| time over the response line (% of samples) | 19.74 | 20.02 | +1.4% | −0.6332 to +1.2023 | no |
| failed requests (%) | 0 | 0.01136 | +0.011 (native is 0) | −0.0143 to +0.0371 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 10.1 | +6.3% | +0.0999 to +1.1001 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.5 | +128.500 (native is 0) | +47.8740 to +209.1260 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.79 | 16.45 | +28.6% | +0.3815 to +6.9351 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06373 | 0.08252 | +29.5% | +0.0058 to +0.0318 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.53 | 1.53 | +0.0% | −0.0329 to +0.0338 | no |
| Omni's own CPU (cores), mean | 0 | 0.07512 | +0.075 (native is 0) | +0.0660 to +0.0843 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.53 | 1.605 | +4.9% | +0.0354 to +0.1157 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.7 | 366.3 | −16.5% | −122.2606 to −22.5623 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.294 | +16.3% | +0.0889 to +0.5544 | yes: power given |
| pods started | 0.2 | 1.4 | +600.0% | +0.2583 to +2.1417 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.3 | +1000.0% | +0.7380 to +5.2620 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.475 | +391.7% | −0.0351 to +2.3851 | no |
| host CPU busy, the real machine under kind (%) | 44.07 | 47.47 | +7.7% | +2.6563 to +4.1299 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820 | 836.1 | +2.0% | +6.8873 to +25.3127 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.958 | −34.0% | −3.3036 to −0.7798 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 1.883 | +140.4% | −0.1869 to +2.3869 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.8 | 11.5 | +202.6% | −2.3203 to +17.7203 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.9 | 138.5 | +10.1% | +4.1483 to +21.1934 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.516 | −0.0% | −0.0067 to +0.0050 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.9 | −0.0% | −0.5490 to +0.5197 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 273.9 | −0.0% | −0.5490 to +0.5197 | no |
| response time (ms), mean | 417.3 | 448 | +7.3% | +10.6618 to +50.6856 | yes: LOSS |
| response time (ms), 95th percentile | 1558 | 1706 | +9.5% | +43.0223 to +252.6497 | yes: LOSS |
| response time (ms), 99th percentile | 2181 | 2401 | +10.1% | +19.0871 to +419.5533 | yes: LOSS |
| time over the response line (% of samples) | 18.72 | 19.74 | +5.4% | −0.5174 to +2.5483 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.5 | +2.2% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.9 | 12.79 | −0.8% | −2.9137 to +2.6970 | no |
| utilisation (used / allocatable) | 0.06336 | 0.06373 | +0.6% | −0.0004 to +0.0012 | no |
| CPU used (cores), mean | 1.521 | 1.53 | +0.6% | −0.0106 to +0.0288 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.521 | 1.53 | +0.6% | −0.0106 to +0.0288 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.9 | 438.7 | −0.7% | −10.2289 to +3.8457 | no |
| HPA replicas, mean | 1.961 | 1.973 | +0.6% | −0.1366 to +0.1592 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.4 | 0.3 | −25.0% | −1.1900 to +0.9900 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| host CPU busy, the real machine under kind (%) | 43.15 | 44.07 | +2.1% | +0.5166 to +1.3255 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.7 | 820 | +0.9% | +1.6571 to +12.9429 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 0.7833 | +161.1% | −0.0192 to +0.9858 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 3.8 | +123.5% | −1.2116 to +5.4116 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.4 | 125.9 | +7.3% | +1.9736 to +15.0764 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.754 | −20.8% | −2.1685 to −0.3234 | yes: GAIN |
| node-hours | 2.517 | 1.992 | −20.8% | −0.9116 to −0.1372 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.9 | −0.0% | −0.8836 to +0.8089 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 234.8 | −14.3% | −68.3504 to −10.0327 | yes: GAIN |
| response time (ms), mean | 417.3 | 417.7 | +0.1% | −27.2038 to +27.9346 | no |
| response time (ms), 95th percentile | 1558 | 1782 | +14.3% | +39.6005 to +407.1415 | yes: LOSS |
| response time (ms), 99th percentile | 2181 | 2516 | +15.3% | +143.6640 to +524.7698 | yes: LOSS |
| time over the response line (% of samples) | 18.72 | 18.93 | +1.1% | −1.2706 to +1.6802 | no |
| failed requests (%) | 0 | 0.0113 | +0.011 (native is 0) | −0.0143 to +0.0369 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10.1 | +8.6% | −0.1417 to +1.7417 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124 | +124.000 (native is 0) | +47.8706 to +200.1294 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.9 | 15.81 | +22.6% | −0.8939 to +6.7239 | no |
| utilisation (used / allocatable) | 0.06336 | 0.08216 | +29.7% | +0.0048 to +0.0328 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.521 | 1.523 | +0.2% | −0.0200 to +0.0253 | no |
| Omni's own CPU (cores), mean | 0 | 0.07207 | +0.072 (native is 0) | +0.0634 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.521 | 1.595 | +4.9% | +0.0448 to +0.1047 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.9 | 368.2 | −16.7% | −127.6403 to −19.7472 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.961 | 2.356 | +20.1% | +0.1888 to +0.5996 | yes: power given |
| pods started | 0.2 | 1.5 | +650.0% | +0.6214 to +1.9786 | yes: power given |
| pod start wait, total (s) | 0.4 | 4.1 | +925.0% | +1.1981 to +6.2019 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.017 | +908.3% | +0.9672 to +2.6661 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.15 | 46.51 | +7.8% | +2.6829 to +4.0310 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.7 | 826.3 | +1.7% | +2.1541 to +25.0459 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.019 | −33.0% | −3.2464 to −0.7152 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 0.3458 | +15.3% | −0.3171 to +0.4088 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1.5 | −11.8% | −2.5796 to +2.1796 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.4 | 130.1 | +10.9% | +2.9904 to +22.5096 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.754 | −20.8% | −2.1685 to −0.3234 | yes: GAIN |
| node-hours | 2.516 | 1.992 | −20.8% | −0.9106 to −0.1365 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.9 | −0.0% | −0.6447 to +0.5992 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 234.8 | −14.3% | −68.3848 to −9.9690 | yes: GAIN |
| response time (ms), mean | 448 | 417.7 | −6.8% | −50.8385 to −9.7780 | yes: GAIN |
| response time (ms), 95th percentile | 1706 | 1782 | +4.4% | −67.7409 to +218.8109 | no |
| response time (ms), 99th percentile | 2401 | 2516 | +4.8% | +4.6417 to +225.1517 | yes: LOSS |
| time over the response line (% of samples) | 19.74 | 18.93 | −4.1% | −1.7898 to +0.1684 | no |
| failed requests (%) | 0 | 0.0113 | +0.011 (native is 0) | −0.0143 to +0.0369 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 10.1 | +6.3% | +0.0999 to +1.1001 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124 | +124.000 (native is 0) | +47.8706 to +200.1294 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.79 | 15.81 | +23.6% | +0.7338 to +5.3129 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06373 | 0.08216 | +28.9% | +0.0047 to +0.0322 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.53 | 1.523 | −0.4% | −0.0370 to +0.0242 | no |
| Omni's own CPU (cores), mean | 0 | 0.07207 | +0.072 (native is 0) | +0.0634 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.53 | 1.595 | +4.3% | +0.0291 to +0.1022 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.7 | 368.2 | −16.1% | −122.9541 to −18.0501 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.356 | +19.4% | +0.1392 to +0.6265 | yes: power given |
| pods started | 0.2 | 1.5 | +650.0% | +0.2856 to +2.3144 | yes: power given |
| pod start wait, total (s) | 0.3 | 4.1 | +1266.7% | +0.6404 to +6.9596 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.017 | +572.2% | +0.7271 to +2.7062 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.07 | 46.51 | +5.5% | +1.8873 to +2.9845 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820 | 826.3 | +0.8% | −1.3823 to +13.9823 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.019 | −33.0% | −3.2464 to −0.7152 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7833 | 0.3458 | −55.9% | −1.1979 to +0.3229 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.8 | 1.5 | −60.5% | −7.8720 to +3.2720 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.9 | 130.1 | +3.4% | −0.6253 to +9.0753 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.741 | −21.0% | −2.1640 to −0.3545 | yes: GAIN |
| node-hours | 2.517 | 1.985 | −21.1% | −0.9107 to −0.1533 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.7 | −0.1% | −0.8180 to +0.3359 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 234.1 | −14.5% | −68.4211 to −11.2068 | yes: GAIN |
| response time (ms), mean | 417.3 | 443.8 | +6.3% | −1.6578 to +54.5046 | no |
| response time (ms), 95th percentile | 1558 | 1893 | +21.5% | +141.1609 to +528.6051 | yes: LOSS |
| response time (ms), 99th percentile | 2181 | 2636 | +20.8% | +176.8974 to +731.7080 | yes: LOSS |
| time over the response line (% of samples) | 18.72 | 20.02 | +6.9% | −1.0680 to +3.6680 | no |
| failed requests (%) | 0 | 0.01136 | +0.011 (native is 0) | −0.0143 to +0.0371 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10.1 | +8.6% | −0.1417 to +1.7417 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.5 | +128.500 (native is 0) | +47.8740 to +209.1260 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.9 | 16.45 | +27.5% | −0.6909 to +7.7909 | no |
| utilisation (used / allocatable) | 0.06336 | 0.08252 | +30.2% | +0.0058 to +0.0325 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.521 | 1.53 | +0.6% | −0.0190 to +0.0381 | no |
| Omni's own CPU (cores), mean | 0 | 0.07512 | +0.075 (native is 0) | +0.0660 to +0.0843 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.521 | 1.605 | +5.6% | +0.0488 to +0.1205 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.9 | 366.3 | −17.1% | −127.5829 to −23.6232 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.961 | 2.294 | +17.0% | +0.0815 to +0.5844 | yes: power given |
| pods started | 0.2 | 1.4 | +600.0% | −0.0064 to +2.4064 | no |
| pod start wait, total (s) | 0.4 | 3.3 | +725.0% | +0.2783 to +5.5217 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.475 | +637.5% | +0.0637 to +2.4863 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.15 | 47.47 | +10.0% | +3.4652 to +5.1631 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.7 | 836.1 | +2.9% | +9.0692 to +37.7308 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.958 | −34.0% | −3.3036 to −0.7798 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3 | 1.883 | +527.8% | −0.1927 to +3.3594 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 11.5 | +576.5% | −3.0393 to +22.6393 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.4 | 138.5 | +18.1% | +7.1647 to +35.2269 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*