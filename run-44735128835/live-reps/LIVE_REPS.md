# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.845 | 5.239 |
| node-hours | 2.516 | 2.516 | 2.03 | 2.192 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.7 | 273.4 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 273.7 | 237.1 | 249.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 400 | 400.6 | 415.9 | 409.4 |
| response time (ms), 95th percentile | 1481 | 1540 | 1564 | 1559 |
| response time (ms), 99th percentile | 2108 | 2219 | 2229 | 2267 |
| time over the response line (% of samples) | 15.54 | 14.73 | 15.83 | 15.12 |
| failed requests (%) | 0 | 0.01124 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 9.9 | 10.3 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 15.7 | 14.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 8.571 | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.59 | 20.87 | 18.23 | 23.38 |
| utilisation (used / allocatable) | 0.06335 | 0.06392 | 0.07806 | 0.07264 |
| CPU used (cores), mean | 1.52 | 1.534 | 1.509 | 1.521 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06401 | 0.0677 |
| CPU used with Omni's own (cores), mean | 1.52 | 1.534 | 1.573 | 1.588 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.1 | 434.3 | 379 | 397 |
| HPA replicas, mean | 1.919 | 2.097 | 2.238 | 2.262 |
| pods started | 0 | 0 | 1.1 | 0.9 |
| pod start wait, total (s) | 0 | 0 | 1.9 | 1.4 |
| pod start wait, mean (s) | 0 | 0 | 0.85 | 0.8 |
| host CPU busy, the real machine under kind (%) | 43.87 | 44.83 | 46.4 | 47.53 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 805.4 | 818.6 | 812.8 | 819.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.76 | 4.436 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.7167 | 0.5625 | 0.2708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | 3.1 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 110.3 | 121.2 | 116.6 | 124.1 |
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
| worker nodes in service, mean | 6 | 5.239 | −12.7% | −1.2636 to −0.2594 | yes: GAIN |
| node-hours | 2.516 | 2.192 | −12.9% | −0.5337 to −0.1144 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.3 | −0.2% | −1.1761 to +0.2950 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 249.4 | −8.9% | −40.1170 to −8.5474 | yes: GAIN |
| response time (ms), mean | 400.6 | 409.4 | +2.2% | −18.0012 to +35.7105 | no |
| response time (ms), 95th percentile | 1540 | 1559 | +1.2% | −118.9052 to +155.9902 | no |
| response time (ms), 99th percentile | 2219 | 2267 | +2.2% | −70.8701 to +167.1217 | no |
| time over the response line (% of samples) | 14.73 | 15.12 | +2.6% | −0.5939 to +1.3718 | no |
| failed requests (%) | 0.01124 | 0 | −100.0% | −0.0367 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.1 | +2.0% | −0.7417 to +1.1417 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.7 | +14.700 (native is 0) | +12.8210 to +16.5790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.87 | 23.38 | +12.0% | −0.8932 to +5.9065 | no |
| utilisation (used / allocatable) | 0.06392 | 0.07264 | +13.6% | +0.0032 to +0.0143 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.534 | 1.521 | −0.9% | −0.0395 to +0.0129 | no |
| Omni's own CPU (cores), mean | 0 | 0.0677 | +0.068 (native is 0) | +0.0604 to +0.0750 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.534 | 1.588 | +3.5% | +0.0254 to +0.0834 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.3 | 397 | −8.6% | −61.6266 to −12.9526 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.097 | 2.262 | +7.9% | −0.0678 to +0.3971 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | +0.1887 to +1.6113 | yes: power given |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | +0.2715 to +2.5285 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1647 to +1.4353 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.83 | 47.53 | +6.0% | +2.3824 to +3.0148 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818.6 | 819.1 | +0.1% | −5.2349 to +6.2349 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.436 | −26.1% | −2.5125 to −0.6154 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7167 | 0.2708 | −62.2% | −1.1666 to +0.2750 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 121.2 | 124.1 | +2.4% | −0.7163 to +6.5080 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.516 | 0.0% | raw −0.0091 to +0.0091 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.7 | +0.0% | −0.7259 to +0.9915 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 273.7 | +0.0% | −0.7259 to +0.9915 | no |
| response time (ms), mean | 400 | 400.6 | +0.1% | −24.4695 to +25.6606 | no |
| response time (ms), 95th percentile | 1481 | 1540 | +4.0% | −97.2848 to +216.9108 | no |
| response time (ms), 99th percentile | 2108 | 2219 | +5.3% | −71.3027 to +293.9295 | no |
| time over the response line (% of samples) | 15.54 | 14.73 | −5.2% | −1.8233 to +0.2072 | no |
| failed requests (%) | 0 | 0.01124 | +0.011 (native is 0) | −0.0142 to +0.0367 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 9.9 | −2.9% | −1.4209 to +0.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.59 | 20.87 | +53.6% | +0.9605 to +13.6028 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06335 | 0.06392 | +0.9% | −0.0002 to +0.0013 | no |
| CPU used (cores), mean | 1.52 | 1.534 | +0.9% | −0.0050 to +0.0322 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.52 | 1.534 | +0.9% | −0.0050 to +0.0322 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.1 | 434.3 | −0.9% | −9.6151 to +1.9820 | no |
| HPA replicas, mean | 1.919 | 2.097 | +9.3% | +0.0950 to +0.2623 | yes: power given |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.87 | 44.83 | +2.2% | +0.5089 to +1.4147 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.4 | 818.6 | +1.6% | −0.3837 to +26.7837 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.7167 | +588.0% | −0.0827 to +1.3077 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | +125.0% | +0.1230 to +0.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 110.3 | 121.2 | +9.9% | +0.4295 to +21.3539 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.845 | −19.3% | −1.7288 to −0.5820 | yes: GAIN |
| node-hours | 2.516 | 2.03 | −19.3% | −0.7243 to −0.2479 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.4 | −0.1% | −0.7801 to +0.4692 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 237.1 | −13.3% | −54.3550 to −18.5475 | yes: GAIN |
| response time (ms), mean | 400 | 415.9 | +4.0% | −1.1738 to +32.9222 | no |
| response time (ms), 95th percentile | 1481 | 1564 | +5.7% | −34.6856 to +202.0466 | no |
| response time (ms), 99th percentile | 2108 | 2229 | +5.7% | −78.8108 to +320.2446 | no |
| time over the response line (% of samples) | 15.54 | 15.83 | +1.9% | −0.2702 to +0.8506 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.3 | +1.0% | −0.7564 to +0.9564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.7 | +15.700 (native is 0) | +10.7782 to +20.6218 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.59 | 18.23 | +34.1% | +1.2258 to +8.0509 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06335 | 0.07806 | +23.2% | +0.0072 to +0.0222 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.52 | 1.509 | −0.7% | −0.0355 to +0.0134 | no |
| Omni's own CPU (cores), mean | 0 | 0.06401 | +0.064 (native is 0) | +0.0577 to +0.0703 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.52 | 1.573 | +3.5% | +0.0255 to +0.0804 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.1 | 379 | −13.5% | −90.4473 to −27.7270 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.919 | 2.238 | +16.6% | +0.0422 to +0.5958 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.2436 to +1.9564 | yes: power given |
| pod start wait, total (s) | 0 | 1.9 | +1.900 (native is 0) | +0.2671 to +3.5329 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.85 | +0.850 (native is 0) | +0.1538 to +1.5462 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.87 | 46.4 | +5.8% | +2.1523 to +2.9131 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.4 | 812.8 | +0.9% | +2.0663 to +12.7337 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.76 | −37.3% | −3.1517 to −1.3278 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.5625 | +440.0% | −0.0104 to +0.9271 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 3.1 | +675.0% | −1.0858 to +6.4858 | no |
| queue: job turnaround, submitted to done, mean (s) | 110.3 | 116.6 | +5.7% | +1.0754 to +11.5079 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.845 | −19.3% | −1.7288 to −0.5820 | yes: GAIN |
| node-hours | 2.516 | 2.03 | −19.3% | −0.7254 to −0.2468 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.4 | −0.1% | −0.9311 to +0.3546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 237.1 | −13.4% | −54.6632 to −18.5050 | yes: GAIN |
| response time (ms), mean | 400.6 | 415.9 | +3.8% | −13.6378 to +44.1951 | no |
| response time (ms), 95th percentile | 1540 | 1564 | +1.5% | −80.1228 to +127.8578 | no |
| response time (ms), 99th percentile | 2219 | 2229 | +0.4% | −186.1440 to +204.9510 | no |
| time over the response line (% of samples) | 14.73 | 15.83 | +7.5% | +0.2374 to +1.9591 | yes: LOSS |
| failed requests (%) | 0.01124 | 0 | −100.0% | −0.0367 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.3 | +4.0% | −0.2032 to +1.0032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.7 | +15.700 (native is 0) | +10.7782 to +20.6218 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.87 | 18.23 | −12.7% | −6.6122 to +1.3256 | no |
| utilisation (used / allocatable) | 0.06392 | 0.07806 | +22.1% | +0.0070 to +0.0212 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.534 | 1.509 | −1.6% | −0.0537 to +0.0044 | no |
| Omni's own CPU (cores), mean | 0 | 0.06401 | +0.064 (native is 0) | +0.0577 to +0.0703 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.534 | 1.573 | +2.6% | +0.0082 to +0.0705 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.3 | 379 | −12.7% | −83.1928 to −27.3485 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.097 | 2.238 | +6.7% | −0.1177 to +0.3984 | no |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.2436 to +1.9564 | yes: power given |
| pod start wait, total (s) | 0 | 1.9 | +1.900 (native is 0) | +0.2671 to +3.5329 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.85 | +0.850 (native is 0) | +0.1538 to +1.5462 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.83 | 46.4 | +3.5% | +1.1728 to +1.9690 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818.6 | 812.8 | −0.7% | −16.1317 to +4.5317 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.76 | −37.3% | −3.1517 to −1.3278 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7167 | 0.5625 | −21.5% | −0.4801 to +0.1717 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 3.1 | +244.4% | −1.6712 to +6.0712 | no |
| queue: job turnaround, submitted to done, mean (s) | 121.2 | 116.6 | −3.8% | −11.0920 to +1.8920 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.239 | −12.7% | −1.2636 to −0.2594 | yes: GAIN |
| node-hours | 2.516 | 2.192 | −12.9% | −0.5329 to −0.1152 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.3 | −0.1% | −0.9195 to +0.3040 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 249.4 | −8.8% | −39.8703 to −8.5286 | yes: GAIN |
| response time (ms), mean | 400 | 409.4 | +2.4% | −9.2599 to +28.1601 | no |
| response time (ms), 95th percentile | 1481 | 1559 | +5.3% | −63.6674 to +220.3784 | no |
| response time (ms), 99th percentile | 2108 | 2267 | +7.6% | +11.2577 to +307.6207 | yes: LOSS |
| time over the response line (% of samples) | 15.54 | 15.12 | −2.7% | −1.3930 to +0.5548 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.1 | −1.0% | −1.7673 to +1.5673 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.7 | +14.700 (native is 0) | +12.8210 to +16.5790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.59 | 23.38 | +72.0% | +3.7224 to +15.8542 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06335 | 0.07264 | +14.7% | +0.0035 to +0.0151 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.52 | 1.521 | +0.0% | −0.0192 to +0.0199 | no |
| Omni's own CPU (cores), mean | 0 | 0.0677 | +0.068 (native is 0) | +0.0604 to +0.0750 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.52 | 1.588 | +4.5% | +0.0444 to +0.0916 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.1 | 397 | −9.4% | −68.3145 to −13.8978 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.919 | 2.262 | +17.9% | +0.0880 to +0.5987 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | +0.1887 to +1.6113 | yes: power given |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | +0.2715 to +2.5285 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1647 to +1.4353 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.87 | 47.53 | +8.3% | +3.2568 to +4.0639 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.4 | 819.1 | +1.7% | +3.6401 to +23.7599 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.436 | −26.1% | −2.5125 to −0.6154 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2708 | +160.0% | −0.0048 to +0.3382 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | +125.0% | −0.0058 to +1.0058 | no |
| queue: job turnaround, submitted to done, mean (s) | 110.3 | 124.1 | +12.5% | +2.8445 to +24.7305 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*