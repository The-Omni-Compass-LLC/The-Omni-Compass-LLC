# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.684 | 4.764 |
| node-hours | 2.513 | 2.511 | 1.962 | 1.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.3 | 273.6 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 273.3 | 232.2 | 234.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 417.8 | 381.3 | 412.9 | 378.7 |
| response time (ms), 95th percentile | 1569 | 1713 | 1767 | 1886 |
| response time (ms), 99th percentile | 2212 | 2450 | 2457 | 2696 |
| time over the response line (% of samples) | 19.66 | 14.43 | 19.73 | 14.73 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | 9 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 118.8 | 112.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 11.71 | 12.27 | 12.55 |
| utilisation (used / allocatable) | 0.06327 | 0.06303 | 0.08285 | 0.08178 |
| CPU used (cores), mean | 1.518 | 1.513 | 1.505 | 1.501 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07114 | 0.06969 |
| CPU used with Omni's own (cores), mean | 1.518 | 1.513 | 1.576 | 1.571 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.4 | 443.7 | 368 | 371.9 |
| HPA replicas, mean | 2.071 | 2.058 | 2.257 | 2.064 |
| pods started | 0.1 | 0 | 1.1 | 0.1 |
| pod start wait, total (s) | 0.3 | 0 | 2.2 | 0.3 |
| pod start wait, mean (s) | 0.3 | 0 | 0.9833 | 0.3 |
| host CPU busy, the real machine under kind (%) | 43.05 | 43.08 | 45.82 | 45.77 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.5 | 813 | 823.4 | 824.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.026 | 4.238 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.04583 | 0.1042 | 0.07917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | 0.4 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 119.1 | 122.2 | 128.1 | 131.6 |
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
| worker nodes in service, mean | 6 | 4.764 | −20.6% | −2.2835 to −0.1892 | yes: GAIN |
| node-hours | 2.511 | 1.998 | −20.4% | −0.9512 to −0.0740 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.8 | +0.2% | −0.3720 to +1.5253 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 234.9 | −14.0% | −71.4974 to −5.1410 | yes: GAIN |
| response time (ms), mean | 381.3 | 378.7 | −0.7% | −20.6817 to +15.4476 | no |
| response time (ms), 95th percentile | 1713 | 1886 | +10.1% | −12.7506 to +358.4196 | no |
| response time (ms), 99th percentile | 2450 | 2696 | +10.0% | −60.9073 to +552.4547 | no |
| time over the response line (% of samples) | 14.43 | 14.73 | +2.1% | −0.5301 to +1.1368 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.6 | +112.600 (native is 0) | +40.1044 to +185.0956 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.71 | 12.55 | +7.2% | −0.9240 to +2.6207 | no |
| utilisation (used / allocatable) | 0.06303 | 0.08178 | +29.7% | +0.0032 to +0.0343 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.513 | 1.501 | −0.8% | −0.0392 to +0.0165 | no |
| Omni's own CPU (cores), mean | 0 | 0.06969 | +0.070 (native is 0) | +0.0605 to +0.0789 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.513 | 1.571 | +3.9% | +0.0224 to +0.0943 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.7 | 371.9 | −16.2% | −131.5338 to −12.1045 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.058 | 2.064 | +0.3% | −0.1389 to +0.1522 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 43.08 | 45.77 | +6.3% | +1.9329 to +3.4571 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813 | 824.2 | +1.4% | +2.6309 to +19.7691 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.238 | −29.4% | −3.1646 to −0.3591 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.07917 | +72.7% | −0.0323 to +0.0989 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.2 | 131.6 | +7.7% | +1.0440 to +17.7144 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.511 | −0.1% | −0.0082 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.3 | −0.1% | −0.9118 to +0.3706 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 273.3 | −0.1% | −0.9118 to +0.3706 | no |
| response time (ms), mean | 417.8 | 381.3 | −8.7% | −62.1307 to −10.8477 | yes: GAIN |
| response time (ms), 95th percentile | 1569 | 1713 | +9.2% | +19.9175 to +267.8415 | yes: LOSS |
| response time (ms), 99th percentile | 2212 | 2450 | +10.8% | −25.0380 to +501.0198 | no |
| time over the response line (% of samples) | 19.66 | 14.43 | −26.6% | −8.5284 to −1.9286 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | −1.1% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 11.7 | +6.5% | −1.0787 to +2.5087 | no |
| utilisation (used / allocatable) | 0.06327 | 0.06303 | −0.4% | −0.0012 to +0.0007 | no |
| CPU used (cores), mean | 1.518 | 1.513 | −0.4% | −0.0283 to +0.0171 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.518 | 1.513 | −0.4% | −0.0283 to +0.0171 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.4 | 443.7 | +0.1% | −7.1456 to +7.8830 | no |
| HPA replicas, mean | 2.071 | 2.058 | −0.6% | −0.1477 to +0.1212 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 43.05 | 43.08 | +0.1% | −0.3920 to +0.4546 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 813 | +0.1% | −4.3777 to +5.3777 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.04583 | −15.4% | −0.0318 to +0.0152 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | −33.3% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 119.1 | 122.2 | +2.6% | −1.9705 to +8.1621 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.684 | −21.9% | −2.3083 to −0.3236 | yes: GAIN |
| node-hours | 2.513 | 1.962 | −21.9% | −0.9659 to −0.1361 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.6 | +0.0% | −0.6948 to +0.8239 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 232.2 | −15.1% | −72.5047 to −10.1413 | yes: GAIN |
| response time (ms), mean | 417.8 | 412.9 | −1.2% | −15.7188 to +6.0290 | no |
| response time (ms), 95th percentile | 1569 | 1767 | +12.6% | +56.9679 to +337.5041 | yes: LOSS |
| response time (ms), 99th percentile | 2212 | 2457 | +11.0% | +73.5675 to +415.2893 | yes: LOSS |
| time over the response line (% of samples) | 19.66 | 19.73 | +0.4% | −0.7392 to +0.8826 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | −1.1% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.8 | +118.800 (native is 0) | +48.6725 to +188.9275 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 12.27 | +11.6% | −0.1109 to +2.6642 | no |
| utilisation (used / allocatable) | 0.06327 | 0.08285 | +31.0% | +0.0046 to +0.0346 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.518 | 1.505 | −0.9% | −0.0394 to +0.0118 | no |
| Omni's own CPU (cores), mean | 0 | 0.07114 | +0.071 (native is 0) | +0.0610 to +0.0813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.518 | 1.576 | +3.8% | +0.0242 to +0.0905 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.4 | 368 | −17.0% | −134.8434 to −15.8011 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.071 | 2.257 | +9.0% | −0.0873 to +0.4592 | no |
| pods started | 0.1 | 1.1 | +1000.0% | −0.0116 to +2.0116 | no |
| pod start wait, total (s) | 0.3 | 2.2 | +633.3% | −0.3227 to +4.1227 | no |
| pod start wait, mean (s) | 0.3 | 0.9833 | +227.8% | −0.4854 to +1.8520 | no |
| host CPU busy, the real machine under kind (%) | 43.05 | 45.82 | +6.4% | +2.0676 to +3.4775 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 823.4 | +1.3% | +3.5397 to +18.2603 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.026 | −32.9% | −3.2559 to −0.6915 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1042 | +92.3% | −0.0559 to +0.1559 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 119.1 | 128.1 | +7.6% | +2.7650 to +15.3183 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.684 | −21.9% | −2.3083 to −0.3236 | yes: GAIN |
| node-hours | 2.511 | 1.962 | −21.8% | −0.9632 to −0.1338 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.6 | +0.1% | −0.6922 to +1.3625 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 232.2 | −15.0% | −72.3693 to −9.7355 | yes: GAIN |
| response time (ms), mean | 381.3 | 412.9 | +8.3% | +8.0888 to +55.1998 | yes: LOSS |
| response time (ms), 95th percentile | 1713 | 1767 | +3.1% | −78.6995 to +185.4125 | no |
| response time (ms), 99th percentile | 2450 | 2457 | +0.3% | −136.1463 to +149.0213 | no |
| time over the response line (% of samples) | 14.43 | 19.73 | +36.7% | +2.0594 to +8.5410 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.8 | +118.800 (native is 0) | +48.6725 to +188.9275 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.71 | 12.27 | +4.8% | −1.1304 to +2.2537 | no |
| utilisation (used / allocatable) | 0.06303 | 0.08285 | +31.4% | +0.0051 to +0.0345 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.513 | 1.505 | −0.5% | −0.0388 to +0.0224 | no |
| Omni's own CPU (cores), mean | 0 | 0.07114 | +0.071 (native is 0) | +0.0610 to +0.0813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.513 | 1.576 | +4.2% | +0.0233 to +0.1026 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.7 | 368 | −17.1% | −132.3873 to −18.9945 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.058 | 2.257 | +9.7% | −0.0653 to +0.4638 | no |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0 | 2.2 | +2.200 (native is 0) | +0.2688 to +4.1312 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9833 | +0.983 (native is 0) | +0.2284 to +1.7383 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.08 | 45.82 | +6.4% | +2.0431 to +3.4394 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813 | 823.4 | +1.3% | +3.5374 to +17.2626 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.026 | −32.9% | −3.2559 to −0.6915 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1042 | +127.3% | −0.0489 to +0.1655 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.2 | 128.1 | +4.9% | +0.7701 to +11.1216 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.764 | −20.6% | −2.2835 to −0.1892 | yes: GAIN |
| node-hours | 2.513 | 1.998 | −20.5% | −0.9547 to −0.0755 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.8 | +0.1% | −0.4317 to +1.0438 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 234.9 | −14.1% | −71.7177 to −5.4618 | yes: GAIN |
| response time (ms), mean | 417.8 | 378.7 | −9.4% | −57.3673 to −20.8451 | yes: GAIN |
| response time (ms), 95th percentile | 1569 | 1886 | +20.2% | +74.8982 to +558.5298 | yes: LOSS |
| response time (ms), 99th percentile | 2212 | 2696 | +21.9% | +119.2830 to +848.2462 | yes: LOSS |
| time over the response line (% of samples) | 19.66 | 14.73 | −25.1% | −8.0198 to −1.8306 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | −1.1% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.6 | +112.600 (native is 0) | +40.1044 to +185.0956 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 12.55 | +14.2% | −0.4182 to +3.5449 | no |
| utilisation (used / allocatable) | 0.06327 | 0.08178 | +29.3% | +0.0026 to +0.0344 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.518 | 1.501 | −1.1% | −0.0433 to +0.0094 | no |
| Omni's own CPU (cores), mean | 0 | 0.06969 | +0.070 (native is 0) | +0.0605 to +0.0789 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.518 | 1.571 | +3.5% | +0.0206 to +0.0848 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.4 | 371.9 | −16.1% | −134.0326 to −8.8685 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.071 | 2.064 | −0.3% | −0.1217 to +0.1085 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.3 | ±0.0% | −1.0116 to +1.0116 | no |
| pod start wait, mean (s) | 0.3 | 0.3 | ±0.0% | −1.0116 to +1.0116 | no |
| host CPU busy, the real machine under kind (%) | 43.05 | 45.77 | +6.3% | +2.0118 to +3.4409 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 824.2 | +1.4% | +3.3374 to +20.0626 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.238 | −29.4% | −3.1646 to −0.3591 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.07917 | +46.2% | −0.0441 to +0.0941 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 119.1 | 131.6 | +10.5% | +4.0822 to +20.8678 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*