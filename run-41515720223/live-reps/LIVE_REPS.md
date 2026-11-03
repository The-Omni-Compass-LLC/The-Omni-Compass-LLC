# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.986 | 4.992 |
| node-hours | 2.515 | 2.511 | 2.087 | 2.096 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.2 | 273 | 273.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.2 | 241.1 | 242 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 413.5 | 430.8 | 397.6 | 402.3 |
| response time (ms), 95th percentile | 1559 | 1591 | 1682 | 1715 |
| response time (ms), 99th percentile | 2192 | 2274 | 2329 | 2331 |
| time over the response line (% of samples) | 17.12 | 17.71 | 16.99 | 16.97 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.3 | 8.9 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 145 | 133.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.34 | 13.55 | 14.47 | 15.15 |
| utilisation (used / allocatable) | 0.06254 | 0.06319 | 0.07716 | 0.07617 |
| CPU used (cores), mean | 1.501 | 1.517 | 1.487 | 1.476 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07088 | 0.07473 |
| CPU used with Omni's own (cores), mean | 1.501 | 1.517 | 1.558 | 1.551 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.2 | 443.5 | 390.2 | 394.8 |
| HPA replicas, mean | 1.96 | 2.002 | 2.454 | 2.343 |
| pods started | 0.1 | 0.1 | 1.4 | 1.2 |
| pod start wait, total (s) | 0.2 | 0.2 | 3.2 | 3 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.317 | 1.2 |
| host CPU busy, the real machine under kind (%) | 42.68 | 43.71 | 45.48 | 46.21 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 814.5 | 821.1 | 817.3 | 823.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.51 | 4.514 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 1.583 | 0.1167 | 0.8958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 8.4 | 0.6 | 4.1 |
| queue: job turnaround, submitted to done, mean (s) | 118.6 | 124.2 | 123.7 | 126.4 |
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
| worker nodes in service, mean | 6 | 4.992 | −16.8% | −1.9568 to −0.0596 | yes: GAIN |
| node-hours | 2.511 | 2.096 | −16.5% | −0.8117 to −0.0183 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.7 | +0.2% | −0.5513 to +1.5208 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 242 | −11.4% | −61.4287 to −1.0268 | yes: GAIN |
| response time (ms), mean | 430.8 | 402.3 | −6.6% | −85.0462 to +28.0292 | no |
| response time (ms), 95th percentile | 1591 | 1715 | +7.8% | −109.8390 to +357.9420 | no |
| response time (ms), 99th percentile | 2274 | 2331 | +2.5% | −172.4555 to +286.3457 | no |
| time over the response line (% of samples) | 17.71 | 16.97 | −4.2% | −2.2010 to +0.7201 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.8 | +6.0% | −0.4685 to +1.4685 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133.1 | +133.100 (native is 0) | +58.9542 to +207.2458 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.55 | 15.15 | +11.8% | −1.9025 to +5.0992 | no |
| utilisation (used / allocatable) | 0.06319 | 0.07617 | +20.5% | +0.0003 to +0.0257 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.517 | 1.476 | −2.7% | −0.0913 to +0.0109 | no |
| Omni's own CPU (cores), mean | 0 | 0.07473 | +0.075 (native is 0) | +0.0650 to +0.0845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 1.551 | +2.3% | −0.0235 to +0.0926 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 394.8 | −11.0% | −96.9804 to −0.3078 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.343 | +17.0% | +0.1126 to +0.5694 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.1198 to +2.0802 | yes: power given |
| pod start wait, total (s) | 0.2 | 3 | +1400.0% | +0.1066 to +5.4934 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.2 | +500.0% | +0.0463 to +1.9537 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.71 | 46.21 | +5.7% | +1.1032 to +3.9037 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.1 | 823.7 | +0.3% | −19.2691 to +24.4691 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.514 | −24.8% | −2.7567 to −0.2145 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.583 | 0.8958 | −43.4% | −2.8453 to +1.4703 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8.4 | 4.1 | −51.2% | −13.5410 to +4.9410 | no |
| queue: job turnaround, submitted to done, mean (s) | 124.2 | 126.4 | +1.8% | −14.7457 to +19.1041 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.515 | 2.511 | −0.1% | −0.0120 to +0.0047 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.2 | −0.1% | −1.1254 to +0.7965 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.2 | −0.1% | −1.1254 to +0.7965 | no |
| response time (ms), mean | 413.5 | 430.8 | +4.2% | −17.2209 to +51.8334 | no |
| response time (ms), 95th percentile | 1559 | 1591 | +2.0% | −142.7766 to +205.9736 | no |
| response time (ms), 99th percentile | 2192 | 2274 | +3.7% | −129.8354 to +292.3036 | no |
| time over the response line (% of samples) | 17.12 | 17.71 | +3.4% | −0.2109 to +1.3885 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.3 | +3.8% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.34 | 13.55 | −11.6% | −4.6368 to +1.0702 | no |
| utilisation (used / allocatable) | 0.06254 | 0.06319 | +1.0% | −0.0008 to +0.0021 | no |
| CPU used (cores), mean | 1.501 | 1.517 | +1.0% | −0.0191 to +0.0503 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.501 | 1.517 | +1.0% | −0.0191 to +0.0503 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.2 | 443.5 | −1.3% | −19.3536 to +7.8790 | no |
| HPA replicas, mean | 1.96 | 2.002 | +2.1% | −0.0806 to +0.1645 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 42.68 | 43.71 | +2.4% | +0.3293 to +1.7242 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.5 | 821.1 | +0.8% | −4.6758 to +17.8758 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 1.583 | +630.8% | −1.3804 to +4.1137 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 8.4 | +546.2% | −7.2040 to +21.4040 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.6 | 124.2 | +4.7% | −5.0859 to +16.2109 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.986 | −16.9% | −1.9871 to −0.0409 | yes: GAIN |
| node-hours | 2.515 | 2.087 | −17.0% | −0.8340 to −0.0218 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273 | −0.1% | −1.1429 to +0.3938 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 241.1 | −11.8% | −62.7389 to −1.7477 | yes: GAIN |
| response time (ms), mean | 413.5 | 397.6 | −3.9% | −36.0145 to +4.0641 | no |
| response time (ms), 95th percentile | 1559 | 1682 | +7.9% | +11.3480 to +235.3550 | yes: LOSS |
| response time (ms), 99th percentile | 2192 | 2329 | +6.2% | −104.9700 to +378.7324 | no |
| time over the response line (% of samples) | 17.12 | 16.99 | −0.8% | −0.9711 to +0.7063 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.9 | +11.3% | −0.4676 to +2.2676 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 145 | +145.000 (native is 0) | +66.7379 to +223.2621 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.34 | 14.47 | −5.6% | −3.9985 to +2.2751 | no |
| utilisation (used / allocatable) | 0.06254 | 0.07716 | +23.4% | −0.0001 to +0.0294 | no |
| CPU used (cores), mean | 1.501 | 1.487 | −0.9% | −0.0423 to +0.0149 | no |
| Omni's own CPU (cores), mean | 0 | 0.07088 | +0.071 (native is 0) | +0.0618 to +0.0800 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.501 | 1.558 | +3.8% | +0.0238 to +0.0907 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.2 | 390.2 | −13.1% | −117.8254 to −0.2510 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.96 | 2.454 | +25.2% | +0.1225 to +0.8639 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.3433 to +2.2567 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.2 | +1500.0% | +0.6156 to +5.3844 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.317 | +558.3% | +0.2606 to +1.9728 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.68 | 45.48 | +6.6% | +1.9915 to +3.6048 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.5 | 817.3 | +0.3% | −9.9682 to +15.5682 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.51 | −24.8% | −2.8171 to −0.1627 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 0.1167 | −46.2% | −0.3610 to +0.1610 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.6 | −53.8% | −2.5790 to +1.1790 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.6 | 123.7 | +4.3% | −4.2499 to +14.4666 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.986 | −16.9% | −1.9871 to −0.0409 | yes: GAIN |
| node-hours | 2.511 | 2.087 | −16.9% | −0.8281 to −0.0204 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 | −0.1% | −1.0373 to +0.6170 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 241.1 | −11.7% | −62.4593 to −1.6984 | yes: GAIN |
| response time (ms), mean | 430.8 | 397.6 | −7.7% | −64.0678 to −2.4950 | yes: GAIN |
| response time (ms), 95th percentile | 1591 | 1682 | +5.8% | −7.1154 to +190.6214 | no |
| response time (ms), 99th percentile | 2274 | 2329 | +2.4% | −107.0524 to +218.3466 | no |
| time over the response line (% of samples) | 17.71 | 16.99 | −4.1% | −1.9439 to +0.5015 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.9 | +7.2% | −0.5778 to +1.7778 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 145 | +145.000 (native is 0) | +66.7379 to +223.2621 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.55 | 14.47 | +6.8% | −1.7512 to +3.5945 | no |
| utilisation (used / allocatable) | 0.06319 | 0.07716 | +22.1% | −0.0005 to +0.0284 | no |
| CPU used (cores), mean | 1.517 | 1.487 | −1.9% | −0.0711 to +0.0125 | no |
| Omni's own CPU (cores), mean | 0 | 0.07088 | +0.071 (native is 0) | +0.0618 to +0.0800 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 1.558 | +2.7% | −0.0053 to +0.0884 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 390.2 | −12.0% | −108.5019 to +1.9001 | no |
| HPA replicas, mean | 2.002 | 2.454 | +22.5% | +0.0991 to +0.8034 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.1791 to +2.4209 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.2 | +1500.0% | +0.3024 to +5.6976 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.317 | +558.3% | +0.3298 to +1.9036 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.71 | 45.48 | +4.1% | +0.6836 to +2.8592 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.1 | 817.3 | −0.5% | −18.7809 to +11.1809 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.51 | −24.8% | −2.8171 to −0.1627 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.583 | 0.1167 | −92.6% | −4.4707 to +1.5373 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8.4 | 0.6 | −92.9% | −23.9391 to +8.3391 | no |
| queue: job turnaround, submitted to done, mean (s) | 124.2 | 123.7 | −0.4% | −6.7238 to +5.8154 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.992 | −16.8% | −1.9568 to −0.0596 | yes: GAIN |
| node-hours | 2.515 | 2.096 | −16.7% | −0.8182 to −0.0192 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.7 | +0.1% | −0.7485 to +1.3891 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 242 | −11.5% | −61.8040 to −0.9805 | yes: GAIN |
| response time (ms), mean | 413.5 | 402.3 | −2.7% | −43.2901 to +20.8856 | no |
| response time (ms), 95th percentile | 1559 | 1715 | +10.0% | −22.1267 to +333.4267 | no |
| response time (ms), 99th percentile | 2192 | 2331 | +6.3% | −80.3450 to +356.7034 | no |
| time over the response line (% of samples) | 17.12 | 16.97 | −0.9% | −0.9898 to +0.6865 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.8 | +10.0% | −0.3583 to +1.9583 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 133.1 | +133.100 (native is 0) | +58.9542 to +207.2458 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.34 | 15.15 | −1.2% | −4.1137 to +3.7437 | no |
| utilisation (used / allocatable) | 0.06254 | 0.07617 | +21.8% | +0.0006 to +0.0267 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.501 | 1.476 | −1.6% | −0.0697 to +0.0206 | no |
| Omni's own CPU (cores), mean | 0 | 0.07473 | +0.075 (native is 0) | +0.0650 to +0.0845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.501 | 1.551 | +3.3% | −0.0007 to +0.1011 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.2 | 394.8 | −12.1% | −106.2782 to −2.4847 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.96 | 2.343 | +19.5% | +0.1218 to +0.6441 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.0100 to +2.1900 | yes: power given |
| pod start wait, total (s) | 0.2 | 3 | +1400.0% | −0.0573 to +5.6573 | no |
| pod start wait, mean (s) | 0.2 | 1.2 | +500.0% | −0.1681 to +2.1681 | no |
| host CPU busy, the real machine under kind (%) | 42.68 | 46.21 | +8.3% | +2.5308 to +4.5295 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.5 | 823.7 | +1.1% | −9.1140 to +27.5140 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.514 | −24.8% | −2.7567 to −0.2145 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 0.8958 | +313.5% | −0.0780 to +1.4363 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 4.1 | +215.4% | −2.2894 to +7.8894 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.6 | 126.4 | +6.5% | −7.3088 to +22.7921 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*