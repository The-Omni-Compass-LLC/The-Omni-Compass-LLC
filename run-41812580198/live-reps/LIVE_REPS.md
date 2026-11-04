# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.272 | 5.175 |
| node-hours | 2.513 | 2.517 | 2.211 | 2.168 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274.1 | 274 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 274.1 | 251.2 | 247.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 429 | 445.2 | 417.2 | 430.3 |
| response time (ms), 95th percentile | 1586 | 1648 | 1755 | 1782 |
| response time (ms), 99th percentile | 2208 | 2341 | 2440 | 2447 |
| time over the response line (% of samples) | 17.83 | 17.79 | 17.59 | 18.13 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 | 10.3 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 111.5 | 123 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 30.56 | 56.25 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.12 | 13.09 | 16.88 | 15.25 |
| utilisation (used / allocatable) | 0.06416 | 0.06388 | 0.07371 | 0.07462 |
| CPU used (cores), mean | 1.54 | 1.533 | 1.538 | 1.528 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07326 | 0.07686 |
| CPU used with Omni's own (cores), mean | 1.54 | 1.533 | 1.611 | 1.605 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.4 | 436.2 | 394.3 | 391.3 |
| HPA replicas, mean | 1.995 | 1.967 | 2.444 | 2.485 |
| pods started | 0 | 0 | 1.5 | 1 |
| pod start wait, total (s) | 0 | 0 | 2.6 | 2.6 |
| pod start wait, mean (s) | 0 | 0 | 1.417 | 1.7 |
| host CPU busy, the real machine under kind (%) | 43.86 | 44.51 | 46.95 | 47.84 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.3 | 819.6 | 824.9 | 831.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.695 | 4.52 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.5125 | 0.4833 | 1.367 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.2 | 2.7 | 9.5 |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 123.8 | 128.6 | 134 |
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
| worker nodes in service, mean | 6 | 5.175 | −13.8% | −1.5159 to −0.1345 | yes: GAIN |
| node-hours | 2.517 | 2.168 | −13.9% | −0.6401 to −0.0588 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.8 | −0.1% | −1.0231 to +0.5400 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 247.9 | −9.5% | −48.0243 to −4.2796 | yes: GAIN |
| response time (ms), mean | 445.2 | 430.3 | −3.4% | −27.7638 to −2.0866 | yes: GAIN |
| response time (ms), 95th percentile | 1648 | 1782 | +8.2% | +4.9130 to +264.6750 | yes: LOSS |
| response time (ms), 99th percentile | 2341 | 2447 | +4.5% | −53.7725 to +264.8631 | no |
| time over the response line (% of samples) | 17.79 | 18.13 | +1.9% | −0.5118 to +1.1948 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10.3 | +12.0% | −0.1818 to +2.3818 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123 | +123.000 (native is 0) | +52.6902 to +193.3098 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.09 | 15.25 | +16.5% | −0.8934 to +5.2134 | no |
| utilisation (used / allocatable) | 0.06388 | 0.07462 | +16.8% | +0.0018 to +0.0197 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.533 | 1.528 | −0.3% | −0.0348 to +0.0250 | no |
| Omni's own CPU (cores), mean | 0 | 0.07686 | +0.077 (native is 0) | +0.0697 to +0.0840 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.533 | 1.605 | +4.7% | +0.0404 to +0.1035 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.2 | 391.3 | −10.3% | −81.2583 to −8.5960 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.967 | 2.485 | +26.3% | +0.3179 to +0.7176 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.3256 to +1.6744 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +0.5159 to +4.6841 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.7 | +1.700 (native is 0) | +0.7433 to +2.6567 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.51 | 47.84 | +7.5% | +2.8643 to +3.7926 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 819.6 | 831.7 | +1.5% | +3.4605 to +20.7395 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.52 | −24.7% | −2.5578 to −0.4012 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5125 | 1.367 | +166.7% | +0.0802 to +1.6281 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 9.5 | +196.9% | −0.6846 to +13.2846 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.8 | 134 | +8.2% | +2.9468 to +17.3115 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.517 | +0.2% | −0.0029 to +0.0116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274.1 | +0.1% | −0.4230 to +1.0473 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 274.1 | +0.1% | −0.4230 to +1.0473 | no |
| response time (ms), mean | 429 | 445.2 | +3.8% | +0.3140 to +32.0605 | yes: LOSS |
| response time (ms), 95th percentile | 1586 | 1648 | +3.9% | −27.9858 to +151.9128 | no |
| response time (ms), 99th percentile | 2208 | 2341 | +6.0% | +15.3571 to +251.0025 | yes: LOSS |
| time over the response line (% of samples) | 17.83 | 17.79 | −0.2% | −0.4844 to +0.4031 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 | −4.2% | −1.0911 to +0.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.12 | 13.09 | −0.2% | −1.7824 to +1.7291 | no |
| utilisation (used / allocatable) | 0.06416 | 0.06388 | −0.4% | −0.0010 to +0.0004 | no |
| CPU used (cores), mean | 1.54 | 1.533 | −0.4% | −0.0243 to +0.0107 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.54 | 1.533 | −0.4% | −0.0243 to +0.0107 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.4 | 436.2 | +0.7% | −2.5737 to +8.2404 | no |
| HPA replicas, mean | 1.995 | 1.967 | −1.4% | −0.1694 to +0.1148 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.86 | 44.51 | +1.5% | +0.2186 to +1.0750 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.3 | 819.6 | +0.9% | +0.6661 to +13.9339 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.5125 | +167.4% | −0.0509 to +0.6926 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.2 | +540.0% | −2.4144 to +7.8144 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 123.8 | +5.7% | −0.1681 to +13.4931 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.272 | −12.1% | −1.3422 to −0.1139 | yes: GAIN |
| node-hours | 2.513 | 2.211 | −12.0% | −0.5596 to −0.0447 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 | +0.1% | −0.9344 to +1.4534 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 251.2 | −8.2% | −42.1416 to −3.0144 | yes: GAIN |
| response time (ms), mean | 429 | 417.2 | −2.7% | −30.6995 to +7.1288 | no |
| response time (ms), 95th percentile | 1586 | 1755 | +10.7% | −10.5894 to +349.5104 | no |
| response time (ms), 99th percentile | 2208 | 2440 | +10.5% | +26.6401 to +437.2227 | yes: LOSS |
| time over the response line (% of samples) | 17.83 | 17.59 | −1.3% | −0.6904 to +0.2113 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.3 | +7.3% | −0.1294 to +1.5294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.5 | +111.500 (native is 0) | +50.7047 to +172.2953 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.12 | 16.88 | +28.7% | −0.0645 to +7.5945 | no |
| utilisation (used / allocatable) | 0.06416 | 0.07371 | +14.9% | +0.0007 to +0.0184 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.54 | 1.538 | −0.1% | −0.0284 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0.07326 | +0.073 (native is 0) | +0.0663 to +0.0803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.54 | 1.611 | +4.6% | +0.0399 to +0.1028 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.4 | 394.3 | −9.0% | −72.0145 to −6.1617 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.444 | +22.6% | +0.1652 to +0.7346 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.7274 to +2.2726 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +1.2854 to +3.9146 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.417 | +1.417 (native is 0) | +0.7978 to +2.0355 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.86 | 46.95 | +7.0% | +2.4969 to +3.6829 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.3 | 824.9 | +1.6% | +2.8959 to +22.3041 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.695 | −21.7% | −2.1644 to −0.4450 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.4833 | +152.2% | −0.0087 to +0.5920 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.7 | +440.0% | −0.0820 to +4.4820 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 128.6 | +9.8% | +1.3831 to +21.5502 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.272 | −12.1% | −1.3422 to −0.1139 | yes: GAIN |
| node-hours | 2.517 | 2.211 | −12.2% | −0.5671 to −0.0459 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274 | −0.0% | −1.0103 to +0.9051 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 251.2 | −8.4% | −42.5312 to −3.2490 | yes: GAIN |
| response time (ms), mean | 445.2 | 417.2 | −6.3% | −37.2770 to −18.6682 | yes: GAIN |
| response time (ms), 95th percentile | 1648 | 1755 | +6.5% | −14.5277 to +229.5217 | no |
| response time (ms), 99th percentile | 2341 | 2440 | +4.2% | −66.0950 to +263.5982 | no |
| time over the response line (% of samples) | 17.79 | 17.59 | −1.1% | −0.8425 to +0.4448 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10.3 | +12.0% | +0.2436 to +1.9564 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.5 | +111.500 (native is 0) | +50.7047 to +172.2953 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.09 | 16.88 | +29.0% | +0.3518 to +7.2315 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06388 | 0.07371 | +15.4% | +0.0006 to +0.0191 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.533 | 1.538 | +0.3% | −0.0149 to +0.0247 | no |
| Omni's own CPU (cores), mean | 0 | 0.07326 | +0.073 (native is 0) | +0.0663 to +0.0803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.533 | 1.611 | +5.1% | +0.0555 to +0.1009 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.2 | 394.3 | −9.6% | −78.8691 to −4.9739 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.967 | 2.444 | +24.3% | +0.2725 to +0.6818 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.7274 to +2.2726 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +1.2854 to +3.9146 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.417 | +1.417 (native is 0) | +0.7978 to +2.0355 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.51 | 46.95 | +5.5% | +1.9285 to +2.9577 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 819.6 | 824.9 | +0.6% | +1.0075 to +9.5925 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.695 | −21.7% | −2.1644 to −0.4450 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5125 | 0.4833 | −5.7% | −0.4455 to +0.3872 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.2 | 2.7 | −15.6% | −5.4010 to +4.4010 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.8 | 128.6 | +3.9% | +0.9095 to +8.6988 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.175 | −13.8% | −1.5159 to −0.1345 | yes: GAIN |
| node-hours | 2.513 | 2.168 | −13.7% | −0.6329 to −0.0574 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.8 | +0.0% | −0.8446 to +0.9858 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 247.9 | −9.4% | −47.6081 to −4.0716 | yes: GAIN |
| response time (ms), mean | 429 | 430.3 | +0.3% | −20.8219 to +23.3459 | no |
| response time (ms), 95th percentile | 1586 | 1782 | +12.4% | +36.9211 to +356.5939 | yes: LOSS |
| response time (ms), 99th percentile | 2208 | 2447 | +10.8% | +33.1843 to +444.2659 | yes: LOSS |
| time over the response line (% of samples) | 17.83 | 18.13 | +1.7% | −0.3854 to +0.9872 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.3 | +7.3% | −0.6081 to +2.0081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123 | +123.000 (native is 0) | +52.6902 to +193.3098 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.12 | 15.25 | +16.3% | −1.5095 to +5.7761 | no |
| utilisation (used / allocatable) | 0.06416 | 0.07462 | +16.3% | +0.0018 to +0.0191 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.54 | 1.528 | −0.8% | −0.0476 to +0.0241 | no |
| Omni's own CPU (cores), mean | 0 | 0.07686 | +0.077 (native is 0) | +0.0697 to +0.0840 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.54 | 1.605 | +4.2% | +0.0259 to +0.1043 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.4 | 391.3 | −9.7% | −75.3261 to −8.8616 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.485 | +24.6% | +0.2938 to +0.6871 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.3256 to +1.6744 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +0.5159 to +4.6841 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.7 | +1.700 (native is 0) | +0.7433 to +2.6567 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.86 | 47.84 | +9.1% | +3.4097 to +4.5407 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.3 | 831.7 | +2.4% | +6.2570 to +32.5430 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.52 | −24.7% | −2.5578 to −0.4012 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 1.367 | +613.0% | +0.2367 to +2.1133 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 9.5 | +1800.0% | +1.0633 to +16.9367 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 117.2 | 134 | +14.3% | +4.3915 to +29.1918 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*