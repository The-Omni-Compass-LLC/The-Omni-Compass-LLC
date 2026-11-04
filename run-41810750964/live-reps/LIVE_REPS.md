# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.542 | 4.469 |
| node-hours | 2.513 | 2.514 | 1.902 | 1.87 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.8 | 271.7 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.8 | 225.9 | 223.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 327.7 | 311.5 | 327.8 | 292.6 |
| response time (ms), 95th percentile | 1169 | 1279 | 1352 | 1377 |
| response time (ms), 99th percentile | 1675 | 1828 | 1917 | 1960 |
| time over the response line (% of samples) | 13.69 | 10.04 | 13.89 | 10.47 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 6.2 | 7.6 | 7.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 142.9 | 107.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 7.143 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.138 | 10.7 | 11.7 | 11.53 |
| utilisation (used / allocatable) | 0.05791 | 0.05796 | 0.07798 | 0.08054 |
| CPU used (cores), mean | 1.39 | 1.391 | 1.383 | 1.407 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06875 | 0.06778 |
| CPU used with Omni's own (cores), mean | 1.39 | 1.391 | 1.452 | 1.474 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.4 | 486.5 | 394 | 381.7 |
| HPA replicas, mean | 1.95 | 2.067 | 2.345 | 2.373 |
| pods started | 0 | 0 | 1.6 | 1.6 |
| pod start wait, total (s) | 0 | 0 | 3.6 | 3.3 |
| pod start wait, mean (s) | 0 | 0 | 1.767 | 1.217 |
| host CPU busy, the real machine under kind (%) | 39.26 | 39.7 | 42.54 | 42.85 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 782.3 | 785.6 | 793.6 | 794.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.825 | 3.65 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0375 | 0.1917 | 0.125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0 | 1.9 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 87.73 | 93.63 | 98.31 | 103.7 |
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
| worker nodes in service, mean | 6 | 4.469 | −25.5% | −2.4700 to −0.5918 | yes: GAIN |
| node-hours | 2.514 | 1.87 | −25.6% | −1.0381 to −0.2510 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.8 | +0.0% | −0.8057 to +0.8203 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 223.7 | −17.7% | −77.4666 to −18.7063 | yes: GAIN |
| response time (ms), mean | 311.5 | 292.6 | −6.1% | −35.9331 to −1.9970 | yes: GAIN |
| response time (ms), 95th percentile | 1279 | 1377 | +7.6% | −20.8265 to +215.3295 | no |
| response time (ms), 99th percentile | 1828 | 1960 | +7.2% | −120.5071 to +385.2523 | no |
| time over the response line (% of samples) | 10.04 | 10.47 | +4.2% | −1.8361 to +2.6806 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 7.5 | +21.0% | −0.9882 to +3.5882 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.7 | +107.700 (native is 0) | +59.2382 to +156.1618 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.7 | 11.53 | +7.7% | −1.2108 to +2.8575 | no |
| utilisation (used / allocatable) | 0.05796 | 0.08054 | +38.9% | +0.0085 to +0.0367 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.391 | 1.407 | +1.1% | −0.0150 to +0.0458 | no |
| Omni's own CPU (cores), mean | 0 | 0.06778 | +0.068 (native is 0) | +0.0591 to +0.0764 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.391 | 1.474 | +6.0% | +0.0510 to +0.1154 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.5 | 381.7 | −21.6% | −174.1706 to −35.5565 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.067 | 2.373 | +14.8% | −0.0266 to +0.6396 | no |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.4715 to +2.7285 | yes: power given |
| pod start wait, total (s) | 0 | 3.3 | +3.300 (native is 0) | +0.8210 to +5.7790 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.217 | +1.217 (native is 0) | +0.4542 to +1.9791 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.7 | 42.85 | +7.9% | +2.3771 to +3.9158 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 785.6 | 794.6 | +1.1% | +0.6855 to +17.3145 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.65 | −39.2% | −3.6122 to −1.0869 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.125 | +233.3% | −0.0424 to +0.2174 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 93.63 | 103.7 | +10.7% | +0.9351 to +19.1815 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.514 | +0.1% | −0.0026 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.8 | +0.1% | −0.2417 to +0.9725 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.8 | +0.1% | −0.2417 to +0.9725 | no |
| response time (ms), mean | 327.7 | 311.5 | −4.9% | −32.8304 to +0.4574 | no |
| response time (ms), 95th percentile | 1169 | 1279 | +9.4% | −15.2077 to +235.4997 | no |
| response time (ms), 99th percentile | 1675 | 1828 | +9.1% | −35.3504 to +341.1330 | no |
| time over the response line (% of samples) | 13.69 | 10.04 | −26.6% | −6.6713 to −0.6171 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 6.2 | −15.1% | −2.9607 to +0.7607 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.138 | 10.7 | +17.1% | −0.3154 to +3.4421 | no |
| utilisation (used / allocatable) | 0.05791 | 0.05796 | +0.1% | −0.0007 to +0.0008 | no |
| CPU used (cores), mean | 1.39 | 1.391 | +0.1% | −0.0177 to +0.0202 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.39 | 1.391 | +0.1% | −0.0177 to +0.0202 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.4 | 486.5 | +0.0% | −7.1000 to +7.2749 | no |
| HPA replicas, mean | 1.95 | 2.067 | +6.0% | −0.0270 to +0.2595 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 39.26 | 39.7 | +1.1% | +0.0872 to +0.8031 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.3 | 785.6 | +0.4% | −1.1486 to +7.7486 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0375 | −30.8% | −0.0714 to +0.0381 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0 | −100.0% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 87.73 | 93.63 | +6.7% | −0.2273 to +12.0189 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.542 | −24.3% | −2.4447 to −0.4714 | yes: GAIN |
| node-hours | 2.513 | 1.902 | −24.3% | −1.0238 to −0.1970 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.7 | +0.1% | −0.6355 to +1.1142 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 225.9 | −16.8% | −76.4976 to −14.6070 | yes: GAIN |
| response time (ms), mean | 327.7 | 327.8 | +0.0% | −19.2867 to +19.3469 | no |
| response time (ms), 95th percentile | 1169 | 1352 | +15.6% | +48.9109 to +316.3241 | yes: LOSS |
| response time (ms), 99th percentile | 1675 | 1917 | +14.4% | +47.3671 to +436.6797 | yes: LOSS |
| time over the response line (% of samples) | 13.69 | 13.89 | +1.5% | −0.2958 to +0.6956 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.6 | +4.1% | −0.8209 to +1.4209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.9 | +142.900 (native is 0) | +79.9625 to +205.8375 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.138 | 11.7 | +28.0% | −1.7874 to +6.9074 | no |
| utilisation (used / allocatable) | 0.05791 | 0.07798 | +34.7% | +0.0065 to +0.0336 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.39 | 1.383 | −0.5% | −0.0369 to +0.0234 | no |
| Omni's own CPU (cores), mean | 0 | 0.06875 | +0.069 (native is 0) | +0.0607 to +0.0768 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.39 | 1.452 | +4.5% | +0.0267 to +0.0973 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.4 | 394 | −19.0% | −157.9416 to −26.9648 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.95 | 2.345 | +20.2% | +0.1358 to +0.6525 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.9089 to +2.2911 | yes: power given |
| pod start wait, total (s) | 0 | 3.6 | +3.600 (native is 0) | +1.6280 to +5.5720 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.767 | +1.767 (native is 0) | +0.9270 to +2.6063 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.26 | 42.54 | +8.4% | +2.6297 to +3.9302 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.3 | 793.6 | +1.4% | −0.3324 to +22.9324 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.825 | −36.2% | −3.5268 to −0.8232 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1917 | +253.8% | −0.2289 to +0.5039 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.9 | +533.3% | −2.2917 to +5.4917 | no |
| queue: job turnaround, submitted to done, mean (s) | 87.73 | 98.31 | +12.1% | −0.3460 to +21.5043 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.542 | −24.3% | −2.4447 to −0.4714 | yes: GAIN |
| node-hours | 2.514 | 1.902 | −24.3% | −1.0274 to −0.1967 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.7 | −0.0% | −1.0916 to +0.8396 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 225.9 | −16.9% | −77.0528 to −14.7825 | yes: GAIN |
| response time (ms), mean | 311.5 | 327.8 | +5.2% | −16.8650 to +49.2982 | no |
| response time (ms), 95th percentile | 1279 | 1352 | +5.7% | +0.5409 to +144.4021 | yes: LOSS |
| response time (ms), 99th percentile | 1828 | 1917 | +4.9% | −66.4355 to +244.6997 | no |
| time over the response line (% of samples) | 10.04 | 13.89 | +38.3% | +1.0397 to +6.6487 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 7.6 | +22.6% | −0.2242 to +3.0242 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.9 | +142.900 (native is 0) | +79.9625 to +205.8375 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.7 | 11.7 | +9.3% | −1.7927 to +3.7861 | no |
| utilisation (used / allocatable) | 0.05796 | 0.07798 | +34.5% | +0.0064 to +0.0337 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.391 | 1.383 | −0.6% | −0.0425 to +0.0264 | no |
| Omni's own CPU (cores), mean | 0 | 0.06875 | +0.069 (native is 0) | +0.0607 to +0.0768 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.391 | 1.452 | +4.4% | +0.0219 to +0.0995 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.5 | 394 | −19.0% | −159.2472 to −25.8341 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.067 | 2.345 | +13.4% | +0.0149 to +0.5409 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.9089 to +2.2911 | yes: power given |
| pod start wait, total (s) | 0 | 3.6 | +3.600 (native is 0) | +1.6280 to +5.5720 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.767 | +1.767 (native is 0) | +0.9270 to +2.6063 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.7 | 42.54 | +7.1% | +2.1026 to +3.5670 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 785.6 | 793.6 | +1.0% | −2.3713 to +18.3713 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.825 | −36.2% | −3.5268 to −0.8232 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.1917 | +411.1% | −0.1738 to +0.4822 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 1.9 | +1.900 (native is 0) | −1.9068 to +5.7068 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.63 | 98.31 | +5.0% | −3.9627 to +13.3293 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.469 | −25.5% | −2.4700 to −0.5918 | yes: GAIN |
| node-hours | 2.513 | 1.87 | −25.6% | −1.0346 to −0.2513 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.8 | +0.1% | −0.4484 to +1.1937 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 223.7 | −17.6% | −76.8938 to −18.5484 | yes: GAIN |
| response time (ms), mean | 327.7 | 292.6 | −10.7% | −56.5516 to −13.7515 | yes: GAIN |
| response time (ms), 95th percentile | 1169 | 1377 | +17.7% | +4.8290 to +409.9660 | yes: LOSS |
| response time (ms), 99th percentile | 1675 | 1960 | +17.0% | −19.1429 to +589.6707 | no |
| time over the response line (% of samples) | 13.69 | 10.47 | −23.5% | −7.6023 to +1.1583 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.5 | +2.7% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.7 | +107.700 (native is 0) | +59.2382 to +156.1618 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.138 | 11.52 | +26.1% | −0.2613 to +5.0346 | no |
| utilisation (used / allocatable) | 0.05791 | 0.08054 | +39.1% | +0.0086 to +0.0367 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.39 | 1.407 | +1.2% | −0.0173 to +0.0507 | no |
| Omni's own CPU (cores), mean | 0 | 0.06778 | +0.068 (native is 0) | +0.0591 to +0.0764 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.39 | 1.474 | +6.1% | +0.0484 to +0.1205 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.4 | 381.7 | −21.5% | −173.1378 to −36.4144 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.95 | 2.373 | +21.7% | +0.1337 to +0.7118 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.4715 to +2.7285 | yes: power given |
| pod start wait, total (s) | 0 | 3.3 | +3.300 (native is 0) | +0.8210 to +5.7790 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.217 | +1.217 (native is 0) | +0.4542 to +1.9791 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.26 | 42.85 | +9.1% | +2.7779 to +4.4052 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.3 | 794.6 | +1.6% | +2.6792 to +21.9208 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.65 | −39.2% | −3.6122 to −1.0869 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.125 | +130.8% | −0.0942 to +0.2359 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 87.73 | 103.7 | +18.2% | +4.4713 to +27.4370 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*