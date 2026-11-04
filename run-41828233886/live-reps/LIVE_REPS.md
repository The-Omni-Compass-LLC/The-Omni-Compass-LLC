# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.951 | 5.899 |
| node-hours | 2.517 | 2.514 | 2.07 | 2.476 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 285.5 | 272.8 | 286.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 285.5 | 239.9 | 282.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 387.4 | 656.7 | 372.5 | 655.9 |
| response time (ms), 95th percentile | 1405 | 1369 | 1575 | 1346 |
| response time (ms), 99th percentile | 2040 | 1813 | 2169 | 1816 |
| time over the response line (% of samples) | 17.56 | 58.49 | 17 | 57.94 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 23.5 | 9.4 | 23.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 106 | 32.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 33.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.18 | 2.172 | 12.03 | 2.315 |
| utilisation (used / allocatable) | 0.06249 | 0.09518 | 0.07661 | 0.09683 |
| CPU used (cores), mean | 1.5 | 2.284 | 1.493 | 2.288 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07149 | 0.04177 |
| CPU used with Omni's own (cores), mean | 1.5 | 2.284 | 1.564 | 2.329 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.5 | 300.4 | 386.6 | 295.7 |
| HPA replicas, mean | 1.929 | 1.985 | 2.296 | 2.62 |
| pods started | 0 | 0 | 1.1 | 1.5 |
| pod start wait, total (s) | 0 | 0 | 2.5 | 4 |
| pod start wait, mean (s) | 0 | 0 | 1.317 | 1.372 |
| host CPU busy, the real machine under kind (%) | 42.48 | 73.38 | 45.62 | 74.92 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 801.1 | 1423 | 808.5 | 1435 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.286 | 4.115 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 595.4 | 0.075 | 665.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1096 | 0.5 | 1125 |
| queue: job turnaround, submitted to done, mean (s) | 105.8 | 899.8 | 113.5 | 919.9 |
| queue: jobs unfinished at the window's end | 0 | 13.8 | 0 | 14.5 |
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
| worker nodes in service, mean | 6 | 5.899 | −1.7% | −0.2795 to +0.0766 | no |
| node-hours | 2.514 | 2.476 | −1.5% | −0.1156 to +0.0392 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.5 | 286.1 | +0.2% | −0.5742 to +1.7550 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.5 | 282.9 | −0.9% | −8.3880 to +3.2104 | no |
| response time (ms), mean | 656.7 | 655.9 | −0.1% | −35.1454 to +33.3939 | no |
| response time (ms), 95th percentile | 1369 | 1346 | −1.7% | −89.6799 to +43.8769 | no |
| response time (ms), 99th percentile | 1813 | 1816 | +0.1% | −110.1835 to +115.5963 | no |
| time over the response line (% of samples) | 58.49 | 57.94 | −0.9% | −4.5215 to +3.4255 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.5 | 23.6 | +0.4% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.4 | +32.400 (native is 0) | +28.4216 to +36.3784 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.172 | 2.315 | +6.6% | −0.0488 to +0.3354 | no |
| utilisation (used / allocatable) | 0.09518 | 0.09683 | +1.7% | −0.0015 to +0.0048 | no |
| CPU used (cores), mean | 2.284 | 2.288 | +0.1% | −0.0224 to +0.0291 | no |
| Omni's own CPU (cores), mean | 0 | 0.04177 | +0.042 (native is 0) | +0.0359 to +0.0476 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.284 | 2.329 | +2.0% | +0.0217 to +0.0685 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300.4 | 295.7 | −1.6% | −13.2995 to +3.9737 | no |
| HPA replicas, mean | 1.985 | 2.62 | +32.0% | +0.2737 to +0.9957 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.1832 to +2.8168 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +0.0245 to +7.9755 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.372 | +1.372 (native is 0) | +0.4269 to +2.3164 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 73.38 | 74.92 | +2.1% | +0.8143 to +2.2646 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1423 | 1435 | +0.8% | −6.9363 to +30.7363 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.115 | −31.4% | −11.2286 to +7.4579 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 595.4 | 665.7 | +11.8% | −0.7849 to +141.5818 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1096 | 1125 | +2.6% | −6.7006 to +64.3486 | no |
| queue: job turnaround, submitted to done, mean (s) | 899.8 | 919.9 | +2.2% | −17.6808 to +57.9641 | no |
| queue: jobs unfinished at the window's end | 13.8 | 14.5 | +5.1% | −0.4705 to +1.8705 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.514 | −0.1% | −0.0095 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 285.5 | +4.3% | +8.9452 to +14.6741 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 285.5 | +4.3% | +8.9452 to +14.6741 | yes: power given |
| response time (ms), mean | 387.4 | 656.7 | +69.5% | +182.9342 to +355.7121 | yes: LOSS |
| response time (ms), 95th percentile | 1405 | 1369 | −2.6% | −632.9534 to +560.6814 | no |
| response time (ms), 99th percentile | 2040 | 1813 | −11.1% | −1197.4685 to +744.6569 | no |
| time over the response line (% of samples) | 17.56 | 58.49 | +233.0% | +30.9483 to +50.9039 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 23.5 | +152.7% | +10.8314 to +17.5686 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.18 | 2.172 | −80.6% | −12.7522 to −5.2612 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06249 | 0.09518 | +52.3% | +0.0257 to +0.0397 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.5 | 2.284 | +52.3% | +0.6162 to +0.9528 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.5 | 2.284 | +52.3% | +0.6162 to +0.9528 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.5 | 300.4 | −32.6% | −187.3178 to −102.9539 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.929 | 1.985 | +2.9% | −0.0510 to +0.1626 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 42.48 | 73.38 | +72.8% | +26.6890 to +35.1181 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.1 | 1423 | +77.6% | +507.5185 to +736.0815 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 595.4 | +751921.2% | +345.6065 to +844.9355 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1096 | +156449.3% | +700.9943 to +1489.2958 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 105.8 | 899.8 | +750.6% | +625.8818 to +962.1515 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.8 | +13.800 (native is 0) | +7.9615 to +19.6385 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.951 | −17.5% | −1.8369 to −0.2614 | yes: GAIN |
| node-hours | 2.517 | 2.07 | −17.8% | −0.7770 to −0.1176 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 272.8 | −0.3% | −1.4849 to −0.2264 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 239.9 | −12.3% | −58.6775 to −8.8547 | yes: GAIN |
| response time (ms), mean | 387.4 | 372.5 | −3.8% | −29.7614 to −0.0215 | yes: GAIN |
| response time (ms), 95th percentile | 1405 | 1575 | +12.1% | +42.2940 to +296.9350 | yes: LOSS |
| response time (ms), 99th percentile | 2040 | 2169 | +6.3% | −34.1540 to +292.8586 | no |
| time over the response line (% of samples) | 17.56 | 17 | −3.2% | −1.1891 to +0.0643 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.4 | +1.1% | −1.0410 to +1.2410 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106 | +106.000 (native is 0) | +50.9931 to +161.0069 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.18 | 12.02 | +7.6% | −1.4381 to +3.1315 | no |
| utilisation (used / allocatable) | 0.06249 | 0.07661 | +22.6% | +0.0029 to +0.0253 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.5 | 1.493 | −0.5% | −0.0299 to +0.0156 | no |
| Omni's own CPU (cores), mean | 0 | 0.07149 | +0.071 (native is 0) | +0.0629 to +0.0800 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.5 | 1.564 | +4.3% | +0.0338 to +0.0949 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.5 | 386.6 | −13.2% | −103.4668 to −14.2302 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.929 | 2.296 | +19.0% | +0.1176 to +0.6162 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | +0.4980 to +4.5020 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.317 | +1.317 (native is 0) | +0.4079 to +2.2254 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.48 | 45.62 | +7.4% | +2.6730 to +3.6147 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.1 | 808.5 | +0.9% | +0.2932 to +14.5068 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.286 | −28.6% | −2.7941 to −0.6333 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.075 | −5.3% | −0.1020 to +0.0936 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.5 | −28.6% | −0.9388 to +0.5388 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.8 | 113.5 | +7.3% | +1.1386 to +14.2531 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.951 | −17.5% | −1.8369 to −0.2614 | yes: GAIN |
| node-hours | 2.514 | 2.07 | −17.7% | −0.7739 to −0.1151 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 285.5 | 272.8 | −4.4% | −15.5953 to −9.7353 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.5 | 239.9 | −16.0% | −71.2877 to −19.8637 | yes: GAIN |
| response time (ms), mean | 656.7 | 372.5 | −43.3% | −376.9314 to −191.4978 | yes: GAIN |
| response time (ms), 95th percentile | 1369 | 1575 | +15.0% | −501.6912 to +913.1922 | no |
| response time (ms), 99th percentile | 1813 | 2169 | +19.6% | −679.1509 to +1390.6671 | no |
| time over the response line (% of samples) | 58.49 | 17 | −70.9% | −51.6363 to −31.3406 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.5 | 9.4 | −60.0% | −17.2170 to −10.9830 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106 | +106.000 (native is 0) | +50.9931 to +161.0069 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.172 | 12.02 | +453.7% | +5.7751 to +13.9315 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09518 | 0.07661 | −19.5% | −0.0308 to −0.0064 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.284 | 1.493 | −34.7% | −0.9647 to −0.6186 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07149 | +0.071 (native is 0) | +0.0629 to +0.0800 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.284 | 1.564 | −31.5% | −0.8970 to −0.5434 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300.4 | 386.6 | +28.7% | +54.1314 to +118.4432 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.985 | 2.296 | +15.7% | +0.0548 to +0.5674 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | +0.4980 to +4.5020 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.317 | +1.317 (native is 0) | +0.4079 to +2.2254 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 73.38 | 45.62 | −37.8% | −31.8309 to −23.6884 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1423 | 808.5 | −43.2% | −728.6598 to −500.1402 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 595.4 | 0.075 | −100.0% | −844.9606 to −345.5897 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1096 | 0.5 | −100.0% | −1489.6281 to −701.0620 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 899.8 | 113.5 | −87.4% | −951.4854 to −621.1562 | yes: GAIN |
| queue: jobs unfinished at the window's end | 13.8 | 0 | −100.0% | −19.6385 to −7.9615 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.899 | −1.7% | −0.2795 to +0.0766 | no |
| node-hours | 2.517 | 2.476 | −1.6% | −0.1179 to +0.0358 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 286.1 | +4.5% | +9.5082 to +15.2918 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 282.9 | +3.4% | +2.4448 to +15.9969 | yes: power given |
| response time (ms), mean | 387.4 | 655.9 | +69.3% | +194.4185 to +342.4763 | yes: LOSS |
| response time (ms), 95th percentile | 1405 | 1346 | −4.2% | −634.0372 to +515.9622 | no |
| response time (ms), 99th percentile | 2040 | 1816 | −11.0% | −1126.0541 to +678.6553 | no |
| time over the response line (% of samples) | 17.56 | 57.94 | +229.9% | +31.0603 to +49.6959 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 23.6 | +153.8% | +10.8439 to +17.7561 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.4 | +32.400 (native is 0) | +28.4216 to +36.3784 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.18 | 2.315 | −79.3% | −12.6710 to −5.0556 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06249 | 0.09683 | +54.9% | +0.0270 to +0.0416 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.5 | 2.288 | +52.5% | +0.6163 to +0.9593 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04177 | +0.042 (native is 0) | +0.0359 to +0.0476 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.5 | 2.329 | +55.3% | +0.6614 to +0.9978 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.5 | 295.7 | −33.6% | −196.1435 to −103.4541 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.929 | 2.62 | +35.8% | +0.3110 to +1.0700 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.1832 to +2.8168 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +0.0245 to +7.9755 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.372 | +1.372 (native is 0) | +0.4269 to +2.3164 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.48 | 74.92 | +76.4% | +28.5171 to +36.3690 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.1 | 1435 | +79.1% | +530.6792 to +736.7208 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.115 | −31.4% | −11.2286 to +7.4579 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 665.7 | +840845.6% | +392.0201 to +939.3188 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1125 | +160567.0% | +737.7192 to +1510.2189 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 105.8 | 919.9 | +769.7% | +651.0506 to +977.2661 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.5 | +14.500 (native is 0) | +8.4187 to +20.5813 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*