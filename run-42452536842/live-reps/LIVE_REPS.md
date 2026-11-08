# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.615 | 5.879 |
| node-hours | 2.518 | 2.515 | 1.935 | 2.464 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 284.5 | 273.2 | 284.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 284.5 | 229.6 | 280.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 392.6 | 625.2 | 385.8 | 613.6 |
| response time (ms), 95th percentile | 1504 | 1327 | 1690 | 1309 |
| response time (ms), 99th percentile | 2082 | 1777 | 2298 | 1790 |
| time over the response line (% of samples) | 17.07 | 52.79 | 16.81 | 53.4 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 22.5 | 8.4 | 22.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 129.5 | 34.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 2.065 | 13.04 | 2.143 |
| utilisation (used / allocatable) | 0.06203 | 0.09218 | 0.08228 | 0.09366 |
| CPU used (cores), mean | 1.489 | 2.212 | 1.474 | 2.205 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06881 | 0.04044 |
| CPU used with Omni's own (cores), mean | 1.489 | 2.212 | 1.543 | 2.246 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 309.1 | 372 | 305.1 |
| HPA replicas, mean | 2.023 | 1.978 | 2.264 | 2.28 |
| pods started | 0.1 | 0.4 | 1.7 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.9 | 4 | 1.7 |
| pod start wait, mean (s) | 0.2 | 0.75 | 1.6 | 1.7 |
| host CPU busy, the real machine under kind (%) | 42.03 | 70.56 | 44.78 | 71.59 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 805.3 | 1363 | 815.8 | 1360 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.96 | 4.864 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 538.1 | 0.2875 | 515.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 878.9 | 0.8 | 877.2 |
| queue: job turnaround, submitted to done, mean (s) | 110.6 | 827.7 | 120.8 | 808.1 |
| queue: jobs unfinished at the window's end | 0 | 11.6 | 0 | 11.4 |
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
| worker nodes in service, mean | 6 | 5.879 | −2.0% | −0.2823 to +0.0408 | no |
| node-hours | 2.515 | 2.464 | −2.0% | −0.1170 to +0.0153 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 284.5 | 284.4 | −0.0% | −0.8768 to +0.6714 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.5 | 280.6 | −1.4% | −8.9465 to +1.1620 | no |
| response time (ms), mean | 625.2 | 613.6 | −1.8% | −74.5129 to +51.4255 | no |
| response time (ms), 95th percentile | 1327 | 1309 | −1.4% | −137.6580 to +100.1650 | no |
| response time (ms), 99th percentile | 1777 | 1790 | +0.7% | −200.8248 to +227.4644 | no |
| time over the response line (% of samples) | 52.79 | 53.4 | +1.2% | −2.3058 to +3.5215 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.5 | 22.5 | ±0.0% | −0.5840 to +0.5840 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.300 (native is 0) | +28.1926 to +40.4074 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.065 | 2.143 | +3.8% | −0.3702 to +0.5268 | no |
| utilisation (used / allocatable) | 0.09218 | 0.09366 | +1.6% | −0.0008 to +0.0037 | no |
| CPU used (cores), mean | 2.212 | 2.205 | −0.3% | −0.0344 to +0.0202 | no |
| Omni's own CPU (cores), mean | 0 | 0.04044 | +0.040 (native is 0) | +0.0334 to +0.0475 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.212 | 2.246 | +1.5% | +0.0063 to +0.0604 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.1 | 305.1 | −1.3% | −9.8729 to +2.0265 | no |
| HPA replicas, mean | 1.978 | 2.28 | +15.2% | +0.1372 to +0.4651 | yes: power given |
| pods started | 0.4 | 0.5 | +25.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.9 | 1.7 | +88.9% | −0.8101 to +2.4101 | no |
| pod start wait, mean (s) | 0.75 | 1.7 | +126.7% | −0.7058 to +2.6058 | no |
| host CPU busy, the real machine under kind (%) | 70.56 | 71.59 | +1.5% | −0.0359 to +2.0945 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1363 | 1360 | −0.2% | −25.1483 to +20.3483 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.864 | −18.9% | −2.8296 to +0.5573 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 538.1 | 515.2 | −4.2% | −73.0293 to +27.3055 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 878.9 | 877.2 | −0.2% | −44.4080 to +40.9619 | no |
| queue: job turnaround, submitted to done, mean (s) | 827.7 | 808.2 | −2.4% | −57.2661 to +18.1661 | no |
| queue: jobs unfinished at the window's end | 11.6 | 11.4 | −1.7% | −1.1417 to +0.7417 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.515 | −0.1% | −0.0118 to +0.0061 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 284.5 | +4.0% | +9.3550 to +12.5391 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 284.5 | +4.0% | +9.3550 to +12.5391 | yes: power given |
| response time (ms), mean | 392.6 | 625.2 | +59.2% | +156.7914 to +308.2996 | yes: LOSS |
| response time (ms), 95th percentile | 1504 | 1327 | −11.8% | −808.0555 to +454.3415 | no |
| response time (ms), 99th percentile | 2082 | 1777 | −14.7% | −1214.7176 to +604.0282 | no |
| time over the response line (% of samples) | 17.07 | 52.79 | +209.3% | +24.6751 to +46.7625 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 22.5 | +174.4% | +10.9953 to +17.6047 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 2.065 | −79.8% | −10.9226 to −5.3507 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06203 | 0.09218 | +48.6% | +0.0253 to +0.0350 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.489 | 2.212 | +48.6% | +0.6072 to +0.8401 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.489 | 2.212 | +48.6% | +0.6072 to +0.8401 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 309.1 | −31.5% | −182.8306 to −100.7545 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 1.978 | −2.2% | −0.1813 to +0.0916 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.5639 to +1.9639 | no |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | −0.5991 to +1.6991 | no |
| host CPU busy, the real machine under kind (%) | 42.03 | 70.56 | +67.9% | +25.4578 to +31.6062 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.3 | 1363 | +69.2% | +459.0956 to +656.1044 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 538.1 | +679608.0% | +214.3027 to +861.7433 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 878.9 | +146386.2% | +403.5478 to +1353.0865 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 110.6 | 827.7 | +648.5% | +530.2377 to +904.0123 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.6 | +11.600 (native is 0) | +4.1878 to +19.0122 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.615 | −23.1% | −2.3996 to −0.3698 | yes: GAIN |
| node-hours | 2.518 | 1.935 | −23.2% | −1.0064 to −0.1601 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.2 | −0.1% | −1.3757 to +0.5990 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 229.6 | −16.1% | −76.0501 to −11.8141 | yes: GAIN |
| response time (ms), mean | 392.6 | 385.8 | −1.7% | −22.2348 to +8.5879 | no |
| response time (ms), 95th percentile | 1504 | 1690 | +12.4% | +14.5577 to +357.8603 | yes: LOSS |
| response time (ms), 99th percentile | 2082 | 2298 | +10.4% | +54.5100 to +376.7604 | yes: LOSS |
| time over the response line (% of samples) | 17.07 | 16.81 | −1.5% | −0.6701 to +0.1529 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.4 | +2.4% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 129.5 | +129.500 (native is 0) | +45.8500 to +213.1500 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 13.04 | +27.8% | −0.5478 to +6.2245 | no |
| utilisation (used / allocatable) | 0.06203 | 0.08228 | +32.6% | +0.0058 to +0.0348 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.489 | 1.474 | −1.0% | −0.0542 to +0.0243 | no |
| Omni's own CPU (cores), mean | 0 | 0.06881 | +0.069 (native is 0) | +0.0595 to +0.0781 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.489 | 1.543 | +3.6% | +0.0072 to +0.1005 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 372 | −17.5% | −135.2385 to −22.5500 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.264 | +11.9% | +0.0823 to +0.4000 | yes: power given |
| pods started | 0.1 | 1.7 | +1600.0% | +0.3749 to +2.8251 | yes: power given |
| pod start wait, total (s) | 0.2 | 4 | +1900.0% | +0.7503 to +6.8497 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.6 | +700.0% | +0.1954 to +2.6046 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.03 | 44.78 | +6.5% | +1.9233 to +3.5724 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.3 | 815.8 | +1.3% | +0.4220 to +20.5780 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.96 | −34.0% | −3.4287 to −0.6515 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.2875 | +263.2% | −0.0564 to +0.4731 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | −0.5388 to +0.9388 | no |
| queue: job turnaround, submitted to done, mean (s) | 110.6 | 120.8 | +9.3% | +0.5131 to +19.9952 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.615 | −23.1% | −2.3996 to −0.3698 | yes: GAIN |
| node-hours | 2.515 | 1.935 | −23.1% | −1.0028 to −0.1580 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 284.5 | 273.2 | −4.0% | −13.5630 to −9.1078 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.5 | 229.6 | −19.3% | −87.9947 to −21.7636 | yes: GAIN |
| response time (ms), mean | 625.2 | 385.8 | −38.3% | −315.2009 to −163.5370 | yes: GAIN |
| response time (ms), 95th percentile | 1327 | 1690 | +27.4% | −369.5783 to +1095.7103 | no |
| response time (ms), 99th percentile | 1777 | 2298 | +29.3% | −509.7401 to +1551.6999 | no |
| time over the response line (% of samples) | 52.79 | 16.81 | −68.2% | −47.2763 to −24.6785 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.5 | 8.4 | −62.7% | −17.4287 to −10.7713 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 129.5 | +129.500 (native is 0) | +45.8500 to +213.1500 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.065 | 13.04 | +531.5% | +5.8778 to +16.0722 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09218 | 0.08228 | −10.7% | −0.0225 to +0.0027 | no |
| CPU used (cores), mean | 2.212 | 1.474 | −33.4% | −0.8851 to −0.5922 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06881 | +0.069 (native is 0) | +0.0595 to +0.0781 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.212 | 1.543 | −30.3% | −0.8225 to −0.5172 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.1 | 372 | +20.4% | +39.4692 to +86.3274 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.264 | +14.5% | +0.0473 to +0.5247 | yes: power given |
| pods started | 0.4 | 1.7 | +325.0% | +0.0819 to +2.5181 | yes: power given |
| pod start wait, total (s) | 0.9 | 4 | +344.4% | +0.2298 to +5.9702 | yes: LOSS |
| pod start wait, mean (s) | 0.75 | 1.6 | +113.3% | −0.3924 to +2.0924 | no |
| host CPU busy, the real machine under kind (%) | 70.56 | 44.78 | −36.5% | −28.6527 to −22.9157 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1363 | 815.8 | −40.1% | −641.5804 to −452.6196 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 538.1 | 0.2875 | −99.9% | −861.3835 to −214.2458 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 878.9 | 0.8 | −99.9% | −1352.5948 to −403.6395 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 827.7 | 120.8 | −85.4% | −887.5346 to −526.2071 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.6 | 0 | −100.0% | −19.0122 to −4.1878 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.879 | −2.0% | −0.2823 to +0.0408 | no |
| node-hours | 2.518 | 2.464 | −2.1% | −0.1221 to +0.0148 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 284.4 | +4.0% | +9.0350 to +12.6537 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 280.6 | +2.6% | +1.8662 to +12.2433 | yes: power given |
| response time (ms), mean | 392.6 | 613.6 | +56.3% | +160.9689 to +281.0348 | yes: LOSS |
| response time (ms), 95th percentile | 1504 | 1309 | −13.0% | −841.1195 to +449.9125 | no |
| response time (ms), 99th percentile | 2082 | 1790 | −14.0% | −1247.8268 to +663.7770 | no |
| time over the response line (% of samples) | 17.07 | 53.4 | +212.8% | +25.6049 to +47.0483 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 22.5 | +174.4% | +10.9953 to +17.6047 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.300 (native is 0) | +28.1926 to +40.4074 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 2.143 | −79.0% | −10.8908 to −5.2259 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06203 | 0.09366 | +51.0% | +0.0259 to +0.0374 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.489 | 2.205 | +48.1% | +0.5999 to +0.8333 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04044 | +0.040 (native is 0) | +0.0334 to +0.0475 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.489 | 2.246 | +50.9% | +0.6450 to +0.8691 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 305.1 | −32.3% | −191.0742 to −100.3573 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.28 | +12.7% | +0.0288 to +0.4838 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.2 | 1.7 | +750.0% | −0.0174 to +3.0174 | no |
| pod start wait, mean (s) | 0.2 | 1.7 | +750.0% | −0.0174 to +3.0174 | no |
| host CPU busy, the real machine under kind (%) | 42.03 | 71.59 | +70.3% | +26.6430 to +32.4796 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.3 | 1360 | +68.9% | +456.5926 to +653.8074 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.864 | −18.9% | −2.8296 to +0.5573 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 515.2 | +650729.7% | +195.3704 to +834.9517 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 877.2 | +146099.0% | +399.1995 to +1353.9887 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 110.6 | 808.1 | +630.9% | +513.2711 to +881.8789 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.4 | +11.400 (native is 0) | +4.1037 to +18.6963 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*