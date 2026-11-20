# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.646 | 6 |
| node-hours | 2.514 | 2.513 | 1.949 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.9 | 272.7 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.9 | 230.1 | 271.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 326.4 | 136.4 | 321.8 | 139.2 |
| response time (ms), 95th percentile | 1128 | 238.8 | 1337 | 252.4 |
| response time (ms), 99th percentile | 1627 | 341.6 | 1893 | 367.6 |
| time over the response line (% of samples) | 13.74 | 0.2244 | 14.09 | 0.3245 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 0 | 9.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 164 | 30.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 28.57 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.06 | 1118 | 9.458 | 1255 |
| utilisation (used / allocatable) | 0.05969 | 0.05998 | 0.07852 | 0.05809 |
| CPU used (cores), mean | 1.433 | 1.439 | 1.419 | 1.394 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07663 | 0.06669 |
| CPU used with Omni's own (cores), mean | 1.433 | 1.439 | 1.496 | 1.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.3 | 451.3 | 387.4 | 464.7 |
| HPA replicas, mean | 2.009 | 2.083 | 2.356 | 2.111 |
| pods started | 0 | 0 | 1.8 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 4.8 | 0.6 |
| pod start wait, mean (s) | 0 | 0 | 2.053 | 0.3 |
| host CPU busy, the real machine under kind (%) | 40.81 | 45.18 | 44.41 | 46.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 771 | 1459 | 784.4 | 1510 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.855 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 182.5 | 0.07083 | 178.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 806.2 | 0.5 | 804.2 |
| queue: job turnaround, submitted to done, mean (s) | 77.16 | 839.4 | 88.36 | 885.2 |
| queue: jobs unfinished at the window's end | 0 | 10 | 0 | 12.6 |
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
| node-hours | 2.513 | 2.515 | +0.1% | −0.0067 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.3 | −0.2% | −1.7053 to +0.5565 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.3 | −0.2% | −1.7053 to +0.5565 | no |
| response time (ms), mean | 136.4 | 139.2 | +2.1% | −2.4610 to +8.0905 | no |
| response time (ms), 95th percentile | 238.8 | 252.4 | +5.7% | −1.1531 to +28.4921 | no |
| response time (ms), 99th percentile | 341.6 | 367.6 | +7.6% | +4.1633 to +47.7611 | yes: LOSS |
| time over the response line (% of samples) | 0.2244 | 0.3245 | +44.6% | −0.0385 to +0.2388 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.7 | +30.700 (native is 0) | +20.2738 to +41.1262 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1118 | 1255 | +12.2% | +34.7107 to +238.6160 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05998 | 0.05809 | −3.1% | −0.0032 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.394 | −3.1% | −0.0765 to −0.0140 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06669 | +0.067 (native is 0) | +0.0596 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.461 | +1.5% | −0.0139 to +0.0567 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.3 | 464.7 | +3.0% | +3.9938 to +22.7754 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.083 | 2.111 | +1.4% | −0.2885 to +0.3449 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.7572 to +1.9572 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 45.18 | 46.58 | +3.1% | +0.3816 to +2.4089 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1459 | 1510 | +3.4% | −26.8563 to +127.2563 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 182.5 | 178.3 | −2.3% | −72.1426 to +63.7093 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 806.2 | 804.2 | −0.2% | −289.6318 to +285.6318 | no |
| queue: job turnaround, submitted to done, mean (s) | 839.4 | 885.2 | +5.4% | −41.4668 to +132.9168 | no |
| queue: jobs unfinished at the window's end | 10 | 12.6 | +26.0% | +0.0497 to +5.1503 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.513 | −0.0% | −0.0112 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.9 | −0.1% | −2.4072 to +1.8901 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.9 | −0.1% | −2.4072 to +1.8901 | no |
| response time (ms), mean | 326.4 | 136.4 | −58.2% | −327.2429 to −52.6944 | yes: GAIN |
| response time (ms), 95th percentile | 1128 | 238.8 | −78.8% | −1549.8955 to −229.2685 | yes: GAIN |
| response time (ms), 99th percentile | 1627 | 341.6 | −79.0% | −2233.6054 to −337.0186 | yes: GAIN |
| time over the response line (% of samples) | 13.74 | 0.2244 | −98.4% | −24.1672 to −2.8646 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 0 | −100.0% | −12.5024 to −3.8976 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.06 | 1118 | +11011.1% | +886.9265 to +1329.2368 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05969 | 0.05998 | +0.5% | −0.0060 to +0.0066 | no |
| CPU used (cores), mean | 1.433 | 1.439 | +0.5% | −0.1444 to +0.1581 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.433 | 1.439 | +0.5% | −0.1444 to +0.1581 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.3 | 451.3 | −2.4% | −55.7488 to +33.5975 | no |
| HPA replicas, mean | 2.009 | 2.083 | +3.7% | −0.2449 to +0.3926 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.81 | 45.18 | +10.7% | +1.1820 to +7.5627 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 771 | 1459 | +89.3% | +617.9667 to +758.6333 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 182.5 | +437980.0% | +129.4275 to +235.5559 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 806.2 | +268633.3% | +643.3727 to +968.4273 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 77.16 | 839.4 | +987.9% | +653.2470 to +871.3030 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10 | +10.000 (native is 0) | +3.7277 to +16.2723 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.646 | −22.6% | −2.2011 to −0.5071 | yes: GAIN |
| node-hours | 2.514 | 1.949 | −22.5% | −0.9195 to −0.2094 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.7 | +0.2% | −0.4781 to +1.4969 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 230.1 | −15.5% | −69.0059 to −15.2211 | yes: GAIN |
| response time (ms), mean | 326.4 | 321.8 | −1.4% | −25.0714 to +15.9393 | no |
| response time (ms), 95th percentile | 1128 | 1337 | +18.5% | +60.2154 to +358.0256 | yes: LOSS |
| response time (ms), 99th percentile | 1627 | 1893 | +16.3% | +39.9644 to +491.2426 | yes: LOSS |
| time over the response line (% of samples) | 13.74 | 14.09 | +2.6% | −0.6168 to +1.3261 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 9.1 | +11.0% | −0.1900 to +1.9900 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164 | +164.000 (native is 0) | +61.3984 to +266.6016 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.06 | 9.458 | −6.0% | −2.2210 to +1.0110 | no |
| utilisation (used / allocatable) | 0.05969 | 0.07852 | +31.5% | +0.0064 to +0.0313 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.433 | 1.419 | −1.0% | −0.0534 to +0.0261 | no |
| Omni's own CPU (cores), mean | 0 | 0.07663 | +0.077 (native is 0) | +0.0714 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.433 | 1.496 | +4.4% | +0.0218 to +0.1042 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.3 | 387.4 | −16.2% | −122.8267 to −27.0289 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.009 | 2.356 | +17.3% | +0.0962 to +0.5975 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.6919 to +2.9081 | yes: power given |
| pod start wait, total (s) | 0 | 4.8 | +4.800 (native is 0) | +1.3978 to +8.2022 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.053 | +2.053 (native is 0) | +1.1947 to +2.9119 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.81 | 44.41 | +8.8% | +3.1301 to +4.0621 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 771 | 784.4 | +1.7% | +4.3759 to +22.4241 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.855 | −35.7% | −3.3048 to −0.9845 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.07083 | +70.0% | −0.0253 to +0.0837 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.16 | 88.36 | +14.5% | +1.3364 to +21.0636 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.646 | −22.6% | −2.2011 to −0.5071 | yes: GAIN |
| node-hours | 2.513 | 1.949 | −22.4% | −0.9147 to −0.2129 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.7 | +0.3% | −1.5454 to +3.0813 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 230.1 | −15.4% | −69.9523 to −13.7576 | yes: GAIN |
| response time (ms), mean | 136.4 | 321.8 | +135.9% | +33.7169 to +337.0883 | yes: LOSS |
| response time (ms), 95th percentile | 238.8 | 1337 | +460.2% | +299.2742 to +1898.1308 | yes: LOSS |
| response time (ms), 99th percentile | 341.6 | 1893 | +454.0% | +409.2638 to +2692.5672 | yes: LOSS |
| time over the response line (% of samples) | 0.2244 | 14.09 | +6181.2% | +3.8153 to +23.9259 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 9.1 | +9.100 (native is 0) | +4.5578 to +13.6422 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164 | +164.000 (native is 0) | +61.3984 to +266.6016 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1118 | 9.458 | −99.2% | −1330.3200 to −887.0533 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05998 | 0.07852 | +30.9% | +0.0093 to +0.0278 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.419 | −1.4% | −0.1935 to +0.1527 | no |
| Omni's own CPU (cores), mean | 0 | 0.07663 | +0.077 (native is 0) | +0.0714 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.496 | +3.9% | −0.1201 to +0.2325 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.3 | 387.4 | −14.1% | −91.9552 to −35.7492 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.083 | 2.356 | +13.1% | −0.0249 to +0.5710 | no |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.6919 to +2.9081 | yes: power given |
| pod start wait, total (s) | 0 | 4.8 | +4.800 (native is 0) | +1.3978 to +8.2022 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.053 | +2.053 (native is 0) | +1.1947 to +2.9119 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.18 | 44.41 | −1.7% | −4.1833 to +2.6309 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1459 | 784.4 | −46.2% | −746.2600 to −603.5400 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 182.5 | 0.07083 | −100.0% | −235.5564 to −129.3686 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 806.2 | 0.5 | −99.9% | −968.4788 to −642.9212 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 839.4 | 88.36 | −89.5% | −854.6000 to −647.5500 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10 | 0 | −100.0% | −16.2723 to −3.7277 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.515 | +0.0% | −0.0060 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.3 | −0.3% | −3.1096 to +1.4437 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.3 | −0.3% | −3.1096 to +1.4437 | no |
| response time (ms), mean | 326.4 | 139.2 | −57.3% | −326.8628 to −47.4449 | yes: GAIN |
| response time (ms), 95th percentile | 1128 | 252.4 | −77.6% | −1539.1514 to −212.6736 | yes: GAIN |
| response time (ms), 99th percentile | 1627 | 367.6 | −77.4% | −2201.4948 to −317.2048 | yes: GAIN |
| time over the response line (% of samples) | 13.74 | 0.3245 | −97.6% | −23.9771 to −2.8545 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 0.1 | −98.8% | −12.3311 to −3.8689 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.7 | +30.700 (native is 0) | +20.2738 to +41.1262 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.06 | 1255 | +12369.1% | +1038.7620 to +1450.7280 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05969 | 0.05809 | −2.7% | −0.0074 to +0.0042 | no |
| CPU used (cores), mean | 1.433 | 1.394 | −2.7% | −0.1774 to +0.1005 | no |
| Omni's own CPU (cores), mean | 0 | 0.06669 | +0.067 (native is 0) | +0.0596 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.433 | 1.461 | +2.0% | −0.1042 to +0.1606 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.3 | 464.7 | +0.5% | −38.7433 to +43.3613 | no |
| HPA replicas, mean | 2.009 | 2.111 | +5.1% | −0.0648 to +0.2688 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.7572 to +1.9572 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 40.81 | 46.58 | +14.1% | +2.5703 to +8.9648 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 771 | 1510 | +95.8% | +693.8186 to +783.1814 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 178.3 | +427860.0% | +128.7140 to +227.8360 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 804.2 | +267966.7% | +593.4377 to +1014.3623 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 77.16 | 885.2 | +1047.2% | +740.9848 to +875.0152 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.6 | +12.600 (native is 0) | +7.5849 to +17.6151 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*