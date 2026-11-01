# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.065 | 4.922 |
| node-hours | 2.516 | 2.514 | 2.121 | 2.061 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.3 | 273.1 | 272.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.3 | 243.7 | 238.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 398.5 | 309.3 | 370.7 | 301.6 |
| response time (ms), 95th percentile | 1484 | 1218 | 1627 | 1389 |
| response time (ms), 99th percentile | 2080 | 2028 | 2205 | 2120 |
| time over the response line (% of samples) | 17.68 | 11.71 | 17.25 | 12.14 |
| failed requests (%) | 0 | 0 | 0.01111 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 7.8 | 9.1 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 34.9 | 30.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.5 | 16.35 | 11.64 | 17.55 |
| utilisation (used / allocatable) | 0.06224 | 0.06269 | 0.075 | 0.07461 |
| CPU used (cores), mean | 1.494 | 1.505 | 1.495 | 1.462 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01645 | 0.01646 |
| CPU used with Omni's own (cores), mean | 1.494 | 1.505 | 1.512 | 1.478 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 446.7 | 391.7 | 394.6 |
| HPA replicas, mean | 1.934 | 1.987 | 2.137 | 2.039 |
| pods started | 0 | 0.3 | 0.5 | 0.1 |
| pod start wait, total (s) | 0 | 0.8 | 0.6 | 0.2 |
| pod start wait, mean (s) | 0 | 0.8 | 0.6 | 0.2 |
| host CPU busy, the real machine under kind (%) | 42.46 | 43.69 | 43.54 | 44.23 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 802.5 | 815.3 | 809.3 | 819.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.502 | 4.206 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7542 | 0.1042 | 0.7917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.6 | 0.3 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 108.1 | 125.6 | 114.3 | 129.7 |
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
| worker nodes in service, mean | 6 | 4.922 | −18.0% | −1.9406 to −0.2148 | yes: GAIN |
| node-hours | 2.514 | 2.061 | −18.0% | −0.8147 to −0.0902 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 272.7 | −0.2% | −1.6572 to +0.4595 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 238.8 | −12.6% | −62.1526 to −6.7409 | yes: GAIN |
| response time (ms), mean | 309.3 | 301.6 | −2.5% | −32.6422 to +17.0898 | no |
| response time (ms), 95th percentile | 1218 | 1389 | +14.1% | −23.7340 to +366.6170 | no |
| response time (ms), 99th percentile | 2028 | 2120 | +4.6% | −88.9612 to +273.5896 | no |
| time over the response line (% of samples) | 11.71 | 12.14 | +3.7% | −0.3549 to +1.2188 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.8 | ±0.0% | −0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.4 | +30.400 (native is 0) | +21.5284 to +39.2716 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.35 | 17.55 | +7.3% | −2.1359 to +4.5293 | no |
| utilisation (used / allocatable) | 0.06269 | 0.07461 | +19.0% | +0.0025 to +0.0213 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.505 | 1.462 | −2.8% | −0.1005 to +0.0153 | no |
| Omni's own CPU (cores), mean | 0 | 0.01646 | +0.016 (native is 0) | +0.0144 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.505 | 1.478 | −1.7% | −0.0855 to +0.0332 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 394.6 | −11.7% | −94.2989 to −9.9483 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.987 | 2.039 | +2.6% | −0.1294 to +0.2336 | no |
| pods started | 0.3 | 0.1 | −66.7% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.8 | 0.2 | −75.0% | −1.7285 to +0.5285 | no |
| pod start wait, mean (s) | 0.8 | 0.2 | −75.0% | −1.7285 to +0.5285 | no |
| host CPU busy, the real machine under kind (%) | 43.69 | 44.23 | +1.2% | −0.0605 to +1.1416 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 815.3 | 819.9 | +0.6% | −0.4037 to +9.6037 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.206 | −29.9% | −3.1629 to −0.4247 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7542 | 0.7917 | +5.0% | −0.0796 to +0.1546 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.9 | +18.8% | −0.3786 to +0.9786 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.6 | 129.7 | +3.3% | −2.1559 to +10.3642 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0126 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.3 | −0.1% | −1.5562 to +1.2557 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.3 | −0.1% | −1.5562 to +1.2557 | no |
| response time (ms), mean | 398.5 | 309.3 | −22.4% | −148.6127 to −29.7406 | yes: GAIN |
| response time (ms), 95th percentile | 1484 | 1218 | −17.9% | −443.6837 to −87.5963 | yes: GAIN |
| response time (ms), 99th percentile | 2080 | 2028 | −2.5% | −230.9100 to +125.7558 | no |
| time over the response line (% of samples) | 17.68 | 11.71 | −33.8% | −9.7122 to −2.2307 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 7.8 | −12.4% | −2.6617 to +0.4617 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.5 | 16.35 | +55.8% | +3.4230 to +8.2870 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06224 | 0.06269 | +0.7% | −0.0010 to +0.0019 | no |
| CPU used (cores), mean | 1.494 | 1.505 | +0.7% | −0.0238 to +0.0455 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.494 | 1.505 | +0.7% | −0.0238 to +0.0455 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 446.7 | −0.4% | −16.3516 to +12.7042 | no |
| HPA replicas, mean | 1.934 | 1.987 | +2.7% | −0.0269 to +0.1318 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.1417 to +1.7417 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | −0.1417 to +1.7417 | no |
| host CPU busy, the real machine under kind (%) | 42.46 | 43.69 | +2.9% | +0.8751 to +1.5835 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.5 | 815.3 | +1.6% | +4.7580 to +20.8420 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7542 | +1408.3% | +0.5914 to +0.8170 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.6 | +300.0% | +0.8984 to +1.5016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 108.1 | 125.6 | +16.2% | +6.4132 to +28.5118 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.065 | −15.6% | −1.8102 to −0.0596 | yes: GAIN |
| node-hours | 2.516 | 2.121 | −15.7% | −0.7608 to −0.0294 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.1 | −0.1% | −1.3107 to +0.6977 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 243.7 | −10.8% | −57.3689 to −1.9608 | yes: GAIN |
| response time (ms), mean | 398.5 | 370.7 | −7.0% | −43.4079 to −12.1238 | yes: GAIN |
| response time (ms), 95th percentile | 1484 | 1627 | +9.7% | +47.0141 to +240.5569 | yes: LOSS |
| response time (ms), 99th percentile | 2080 | 2205 | +6.0% | −12.0104 to +261.6546 | no |
| time over the response line (% of samples) | 17.68 | 17.25 | −2.4% | −1.0844 to +0.2252 | no |
| failed requests (%) | 0 | 0.01111 | +0.011 (native is 0) | −0.0140 to +0.0362 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.1 | +2.2% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.9 | +34.900 (native is 0) | +18.3482 to +51.4518 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.5 | 11.64 | +10.9% | −2.0435 to +4.3301 | no |
| utilisation (used / allocatable) | 0.06224 | 0.075 | +20.5% | +0.0015 to +0.0240 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.494 | 1.495 | +0.1% | −0.0253 to +0.0283 | no |
| Omni's own CPU (cores), mean | 0 | 0.01645 | +0.016 (native is 0) | +0.0146 to +0.0183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.494 | 1.512 | +1.2% | −0.0092 to +0.0450 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 391.7 | −12.7% | −105.3813 to −8.2529 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.934 | 2.137 | +10.5% | +0.0003 to +0.4051 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| host CPU busy, the real machine under kind (%) | 42.46 | 43.54 | +2.5% | +0.6534 to +1.5075 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.5 | 809.3 | +0.8% | +0.6949 to +12.9051 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.502 | −25.0% | −2.8776 to −0.1189 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1042 | +108.3% | −0.0452 to +0.1536 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.1 | 114.3 | +5.8% | −0.5803 to +13.0470 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.065 | −15.6% | −1.8102 to −0.0596 | yes: GAIN |
| node-hours | 2.514 | 2.121 | −15.6% | −0.7592 to −0.0270 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.1 | −0.1% | −1.0550 to +0.7424 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 243.7 | −10.8% | −57.1465 to −1.8827 | yes: GAIN |
| response time (ms), mean | 309.3 | 370.7 | +19.9% | +8.4832 to +114.3383 | yes: LOSS |
| response time (ms), 95th percentile | 1218 | 1627 | +33.6% | +182.1365 to +636.7145 | yes: LOSS |
| response time (ms), 99th percentile | 2028 | 2205 | +8.7% | +6.3106 to +348.4878 | yes: LOSS |
| time over the response line (% of samples) | 11.71 | 17.25 | +47.3% | +2.2384 to +8.8453 | yes: LOSS |
| failed requests (%) | 0 | 0.01111 | +0.011 (native is 0) | −0.0140 to +0.0362 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9.1 | +16.7% | −0.2099 to +2.8099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.9 | +34.900 (native is 0) | +18.3482 to +51.4518 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.35 | 11.64 | −28.8% | −8.0705 to −1.3529 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06269 | 0.075 | +19.6% | +0.0006 to +0.0240 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.505 | 1.495 | −0.6% | −0.0498 to +0.0311 | no |
| Omni's own CPU (cores), mean | 0 | 0.01645 | +0.016 (native is 0) | +0.0146 to +0.0183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.505 | 1.512 | +0.5% | −0.0337 to +0.0479 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 391.7 | −12.3% | −107.7845 to −2.2024 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.987 | 2.137 | +7.6% | −0.0577 to +0.3582 | no |
| pods started | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.8 | 0.6 | −25.0% | −1.1417 to +0.7417 | no |
| pod start wait, mean (s) | 0.8 | 0.6 | −25.0% | −1.1417 to +0.7417 | no |
| host CPU busy, the real machine under kind (%) | 43.69 | 43.54 | −0.3% | −0.6935 to +0.3958 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 815.3 | 809.3 | −0.7% | −12.5472 to +0.5472 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.502 | −25.0% | −2.8776 to −0.1189 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7542 | 0.1042 | −86.2% | −0.7608 to −0.5392 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.3 | −81.2% | −1.6455 to −0.9545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 125.6 | 114.3 | −8.9% | −18.8044 to −3.6540 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.922 | −18.0% | −1.9406 to −0.2148 | yes: GAIN |
| node-hours | 2.516 | 2.061 | −18.1% | −0.8146 to −0.0943 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 272.7 | −0.3% | −1.9268 to +0.4288 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 238.8 | −12.7% | −62.1948 to −6.9991 | yes: GAIN |
| response time (ms), mean | 398.5 | 301.6 | −24.3% | −140.5032 to −53.4025 | yes: GAIN |
| response time (ms), 95th percentile | 1484 | 1389 | −6.3% | −175.7029 to −12.6941 | yes: GAIN |
| response time (ms), 99th percentile | 2080 | 2120 | +1.9% | −173.4966 to +252.9708 | no |
| time over the response line (% of samples) | 17.68 | 12.14 | −31.3% | −9.0300 to −2.0490 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 7.8 | −12.4% | −2.8667 to +0.6667 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.4 | +30.400 (native is 0) | +21.5284 to +39.2716 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.5 | 17.55 | +67.2% | +3.6192 to +10.4841 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06224 | 0.07461 | +19.9% | +0.0034 to +0.0213 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.494 | 1.462 | −2.1% | −0.0906 to +0.0270 | no |
| Omni's own CPU (cores), mean | 0 | 0.01646 | +0.016 (native is 0) | +0.0144 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.494 | 1.478 | −1.0% | −0.0758 to +0.0452 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 394.6 | −12.0% | −92.2562 to −15.6383 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.934 | 2.039 | +5.4% | −0.0605 to +0.2696 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 42.46 | 44.23 | +4.2% | +1.1828 to +2.3568 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.5 | 819.9 | +2.2% | +7.2380 to +27.5620 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.206 | −29.9% | −3.1629 to −0.4247 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7917 | +1483.3% | +0.5847 to +0.8986 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.9 | +375.0% | +0.8048 to +2.1952 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 108.1 | 129.7 | +20.0% | +8.2052 to +34.9281 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*