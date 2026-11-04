# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.516 | 1.509 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160.1 | 158.6 | 160 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160.1 | 158.6 | 160 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 141.4 | 144.2 | 141.8 | 145.6 |
| response time (ms), 95th percentile | 285.3 | 287.4 | 288.2 | 284.5 |
| response time (ms), 99th percentile | 394.1 | 401.5 | 405.2 | 390.9 |
| time over the response line (% of samples) | 0.3201 | 0.3456 | 0.4225 | 0.2564 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 7.8 | 6.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.43 | 0.1383 | 0.2133 | 0.2483 |
| utilisation (used / allocatable) | 0.03794 | 0.04244 | 0.03883 | 0.04386 |
| CPU used (cores), mean | 0.9106 | 1.018 | 0.9319 | 1.053 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03223 | 0.05085 |
| CPU used with Omni's own (cores), mean | 0.9106 | 1.018 | 0.9641 | 1.103 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.6 | 623.9 | 678.7 | 605 |
| HPA replicas, mean | 8.936 | 8.923 | 10.81 | 10.43 |
| pods started | 4.9 | 4.8 | 8 | 7.5 |
| pod start wait, total (s) | 7.6 | 7.4 | 12.4 | 11.6 |
| pod start wait, mean (s) | 1.558 | 1.555 | 1.526 | 1.537 |
| host CPU busy, the real machine under kind (%) | 27.45 | 31.25 | 29.19 | 34.26 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.512 | −0.3% | −0.0111 to +0.0025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 160 | −0.1% | −0.8999 to +0.6341 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 160 | −0.1% | −0.8999 to +0.6341 | no |
| response time (ms), mean | 144.2 | 145.6 | +1.0% | −2.5756 to +5.3607 | no |
| response time (ms), 95th percentile | 287.4 | 284.5 | −1.0% | −21.0189 to +15.1579 | no |
| response time (ms), 99th percentile | 401.5 | 390.9 | −2.6% | −37.2708 to +16.0276 | no |
| time over the response line (% of samples) | 0.3456 | 0.2564 | −25.8% | −0.1963 to +0.0179 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.2 | +6.200 (native is 0) | +5.5427 to +6.8573 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1383 | 0.2483 | +79.5% | −0.2088 to +0.4288 | no |
| utilisation (used / allocatable) | 0.04244 | 0.04386 | +3.3% | +0.0010 to +0.0019 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.018 | 1.053 | +3.3% | +0.0229 to +0.0453 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05085 | +0.051 (native is 0) | +0.0451 to +0.0566 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.018 | 1.103 | +8.3% | +0.0707 to +0.0992 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 623.9 | 605 | −3.0% | −25.2164 to −12.6345 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.923 | 10.43 | +16.9% | +1.0219 to +1.9922 | yes: power given |
| pods started | 4.8 | 7.5 | +56.3% | +1.5295 to +3.8705 | yes: power given |
| pod start wait, total (s) | 7.4 | 11.6 | +56.8% | +1.8444 to +6.5556 | yes: LOSS |
| pod start wait, mean (s) | 1.555 | 1.537 | −1.1% | −0.2708 to +0.2352 | no |
| host CPU busy, the real machine under kind (%) | 31.25 | 34.26 | +9.6% | +2.4705 to +3.5544 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.516 | +0.1% | −0.0094 to +0.0114 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160.1 | +0.7% | −0.0239 to +2.2757 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160.1 | +0.7% | −0.0239 to +2.2757 | no |
| response time (ms), mean | 141.4 | 144.2 | +2.0% | +0.1975 to +5.5775 | yes: LOSS |
| response time (ms), 95th percentile | 285.3 | 287.4 | +0.7% | −10.4001 to +14.5341 | no |
| response time (ms), 99th percentile | 394.1 | 401.5 | +1.9% | −16.3093 to +31.1329 | no |
| time over the response line (% of samples) | 0.3201 | 0.3456 | +8.0% | −0.1853 to +0.2363 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.43 | 0.1383 | −67.8% | −0.7371 to +0.1538 | no |
| utilisation (used / allocatable) | 0.03794 | 0.04244 | +11.8% | +0.0036 to +0.0054 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9106 | 1.018 | +11.8% | +0.0853 to +0.1304 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9106 | 1.018 | +11.8% | +0.0853 to +0.1304 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.6 | 623.9 | −9.9% | −80.9780 to −56.3234 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.936 | 8.923 | −0.1% | −0.1526 to +0.1278 | no |
| pods started | 4.9 | 4.8 | −2.0% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 7.6 | 7.4 | −2.6% | −2.1015 to +1.7015 | no |
| pod start wait, mean (s) | 1.558 | 1.555 | −0.2% | −0.3638 to +0.3572 | no |
| host CPU busy, the real machine under kind (%) | 27.45 | 31.25 | +13.9% | +3.1277 to +4.4757 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.509 | −0.4% | −0.0149 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | −0.3% | −1.3628 to +0.5410 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | −0.3% | −1.3628 to +0.5410 | no |
| response time (ms), mean | 141.4 | 141.8 | +0.3% | −2.0088 to +2.8576 | no |
| response time (ms), 95th percentile | 285.3 | 288.2 | +1.0% | −16.6436 to +22.4346 | no |
| response time (ms), 99th percentile | 394.1 | 405.2 | +2.8% | −9.0481 to +31.2203 | no |
| time over the response line (% of samples) | 0.3201 | 0.4225 | +32.0% | −0.0378 to +0.2425 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.8 | +7.800 (native is 0) | +5.4687 to +10.1313 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.43 | 0.2133 | −50.4% | −0.6498 to +0.2165 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03883 | +2.3% | +0.0000 to +0.0017 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9106 | 0.9319 | +2.3% | +0.0007 to +0.0419 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03223 | +0.032 (native is 0) | +0.0282 to +0.0363 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9106 | 0.9641 | +5.9% | +0.0295 to +0.0775 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.6 | 678.7 | −2.0% | −27.4452 to −0.2507 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.936 | 10.81 | +20.9% | +0.9376 to +2.8025 | yes: power given |
| pods started | 4.9 | 8 | +63.3% | +0.9291 to +5.2709 | yes: power given |
| pod start wait, total (s) | 7.6 | 12.4 | +63.2% | +0.4320 to +9.1680 | yes: LOSS |
| pod start wait, mean (s) | 1.558 | 1.526 | −2.1% | −0.3713 to +0.3069 | no |
| host CPU busy, the real machine under kind (%) | 27.45 | 29.19 | +6.3% | +0.9641 to +2.5186 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.509 | −0.5% | −0.0136 to −0.0004 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 158.6 | −1.0% | −2.3995 to −0.6742 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 158.6 | −1.0% | −2.3995 to −0.6742 | yes: GAIN |
| response time (ms), mean | 144.2 | 141.8 | −1.7% | −5.5984 to +0.6722 | no |
| response time (ms), 95th percentile | 287.4 | 288.2 | +0.3% | −18.1868 to +19.8438 | no |
| response time (ms), 99th percentile | 401.5 | 405.2 | +0.9% | −21.6090 to +28.9576 | no |
| time over the response line (% of samples) | 0.3456 | 0.4225 | +22.2% | −0.1187 to +0.2724 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.8 | +7.800 (native is 0) | +5.4687 to +10.1313 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1383 | 0.2133 | +54.2% | −0.1871 to +0.3371 | no |
| utilisation (used / allocatable) | 0.04244 | 0.03883 | −8.5% | −0.0044 to −0.0029 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.018 | 0.9319 | −8.5% | −0.1045 to −0.0686 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03223 | +0.032 (native is 0) | +0.0282 to +0.0363 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.018 | 0.9641 | −5.3% | −0.0734 to −0.0353 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 623.9 | 678.7 | +8.8% | +42.9047 to +66.7008 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.923 | 10.81 | +21.1% | +1.0074 to +2.7575 | yes: power given |
| pods started | 4.8 | 8 | +66.7% | +0.7966 to +5.6034 | yes: power given |
| pod start wait, total (s) | 7.4 | 12.4 | +67.6% | +0.7214 to +9.2786 | yes: LOSS |
| pod start wait, mean (s) | 1.555 | 1.526 | −1.9% | −0.3456 to +0.2878 | no |
| host CPU busy, the real machine under kind (%) | 31.25 | 29.19 | −6.6% | −2.6642 to −1.4565 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.512 | −0.2% | −0.0100 to +0.0034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160 | +0.6% | +0.2854 to +1.7006 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160 | +0.6% | +0.2854 to +1.7006 | yes: power given |
| response time (ms), mean | 141.4 | 145.6 | +3.0% | +1.2107 to +7.3494 | yes: LOSS |
| response time (ms), 95th percentile | 285.3 | 284.5 | −0.3% | −15.9191 to +14.1921 | no |
| response time (ms), 99th percentile | 394.1 | 390.9 | −0.8% | −22.8992 to +16.4796 | no |
| time over the response line (% of samples) | 0.3201 | 0.2564 | −19.9% | −0.2082 to +0.0808 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.2 | +6.200 (native is 0) | +5.5427 to +6.8573 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.43 | 0.2483 | −42.2% | −0.6713 to +0.3080 | no |
| utilisation (used / allocatable) | 0.03794 | 0.04386 | +15.6% | +0.0047 to +0.0071 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9106 | 1.053 | +15.6% | +0.1139 to +0.1700 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05085 | +0.051 (native is 0) | +0.0451 to +0.0566 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9106 | 1.103 | +21.2% | +0.1606 to +0.2250 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.6 | 605 | −12.6% | −102.6720 to −72.4803 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.936 | 10.43 | +16.7% | +0.9561 to +2.0333 | yes: power given |
| pods started | 4.9 | 7.5 | +53.1% | +1.4715 to +3.7285 | yes: power given |
| pod start wait, total (s) | 7.6 | 11.6 | +52.6% | +1.6638 to +6.3362 | yes: LOSS |
| pod start wait, mean (s) | 1.558 | 1.537 | −1.4% | −0.2045 to +0.1622 | no |
| host CPU busy, the real machine under kind (%) | 27.45 | 34.26 | +24.8% | +5.7593 to +7.8690 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*