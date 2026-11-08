# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.359 | 4.523 |
| node-hours | 2.51 | 2.512 | 1.828 | 1.896 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.6 | 271.6 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 271.6 | 220 | 225.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 263.5 | 274 | 246.2 | 277.7 |
| response time (ms), 95th percentile | 877.8 | 1050 | 952.3 | 1220 |
| response time (ms), 99th percentile | 1207 | 1521 | 1326 | 1748 |
| time over the response line (% of samples) | 8.548 | 8.52 | 9.797 | 9.671 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 7.1 | 7.1 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 154.7 | 113.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 5.333 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.343 | 17.25 | 8.97 | 23.08 |
| utilisation (used / allocatable) | 0.05801 | 0.05809 | 0.07907 | 0.07677 |
| CPU used (cores), mean | 1.392 | 1.394 | 1.352 | 1.367 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06927 | 0.0733 |
| CPU used with Omni's own (cores), mean | 1.392 | 1.394 | 1.421 | 1.44 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.6 | 474.1 | 388.7 | 395.5 |
| HPA replicas, mean | 1.973 | 1.999 | 2.211 | 2.092 |
| pods started | 0.1 | 0.1 | 1.2 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.2 | 2.8 | 1.1 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.183 | 0.9 |
| host CPU busy, the real machine under kind (%) | 39.15 | 41.43 | 42.14 | 44.76 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 759.7 | 777.8 | 762 | 793.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.407 | 3.514 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.8333 | 0.0375 | 0.8667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.9 | 0.2 | 1.8 |
| queue: job turnaround, submitted to done, mean (s) | 65.84 | 84.99 | 68.63 | 96.85 |
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
| worker nodes in service, mean | 6 | 4.523 | −24.6% | −2.2189 to −0.7342 | yes: GAIN |
| node-hours | 2.512 | 1.896 | −24.5% | −0.9259 to −0.3069 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.7 | +0.0% | −0.9690 to +1.0894 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 225.3 | −17.1% | −69.9288 to −22.8091 | yes: GAIN |
| response time (ms), mean | 274 | 277.7 | +1.3% | −28.0418 to +35.4265 | no |
| response time (ms), 95th percentile | 1050 | 1220 | +16.1% | +30.7925 to +308.4305 | yes: LOSS |
| response time (ms), 99th percentile | 1521 | 1748 | +14.9% | +55.4668 to +398.9034 | yes: LOSS |
| time over the response line (% of samples) | 8.52 | 9.671 | +13.5% | −0.0140 to +2.3171 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 8.3 | +16.9% | +0.1997 to +2.2003 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.2 | +113.200 (native is 0) | +55.7199 to +170.6801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.25 | 23.08 | +33.7% | −2.7644 to +14.4077 | no |
| utilisation (used / allocatable) | 0.05809 | 0.07677 | +32.2% | +0.0085 to +0.0289 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.367 | −2.0% | −0.0754 to +0.0201 | no |
| Omni's own CPU (cores), mean | 0 | 0.0733 | +0.073 (native is 0) | +0.0648 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.44 | +3.3% | −0.0081 to +0.0994 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 395.5 | −16.6% | −120.3129 to −36.9239 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.092 | +4.7% | −0.0942 to +0.2810 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.3818 to +2.1818 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | −0.3690 to +1.7690 | no |
| host CPU busy, the real machine under kind (%) | 41.43 | 44.76 | +8.0% | +2.4480 to +4.1978 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.8 | 793.6 | +2.0% | +0.9219 to +30.6781 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.514 | −41.4% | −3.3793 to −1.5925 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8333 | 0.8667 | +4.0% | −0.0597 to +0.1263 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 1.8 | −5.3% | −0.8872 to +0.6872 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.99 | 96.85 | +14.0% | +0.0777 to +23.6390 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.512 | +0.1% | −0.0023 to +0.0056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.6 | +0.1% | −0.1501 to +0.9133 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 271.6 | +0.1% | −0.1501 to +0.9133 | no |
| response time (ms), mean | 263.5 | 274 | +4.0% | −5.6857 to +26.6017 | no |
| response time (ms), 95th percentile | 877.8 | 1050 | +19.7% | −35.9570 to +381.3010 | no |
| response time (ms), 99th percentile | 1207 | 1521 | +26.0% | −7.4491 to +635.0375 | no |
| time over the response line (% of samples) | 8.548 | 8.52 | −0.3% | −2.4662 to +2.4098 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 7.1 | +26.8% | +0.2271 to +2.7729 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.343 | 17.25 | +84.7% | +1.8072 to +14.0161 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05801 | 0.05809 | +0.1% | −0.0008 to +0.0010 | no |
| CPU used (cores), mean | 1.392 | 1.394 | +0.1% | −0.0201 to +0.0239 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.392 | 1.394 | +0.1% | −0.0201 to +0.0239 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.6 | 474.1 | +0.1% | −7.8569 to +8.8806 | no |
| HPA replicas, mean | 1.973 | 1.999 | +1.3% | −0.0852 to +0.1363 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 39.15 | 41.43 | +5.8% | +1.7334 to +2.8312 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.7 | 777.8 | +2.4% | −0.5573 to +36.7573 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.8333 | +1900.0% | +0.5574 to +1.0259 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.9 | +533.3% | +0.4715 to +2.7285 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.84 | 84.99 | +29.1% | +5.0602 to +33.2398 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.359 | −27.4% | −2.4284 to −0.8539 | yes: GAIN |
| node-hours | 2.51 | 1.828 | −27.2% | −1.0117 to −0.3537 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.6 | +0.1% | −0.5252 to +1.1447 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 220 | −18.9% | −76.2059 to −26.3496 | yes: GAIN |
| response time (ms), mean | 263.5 | 246.2 | −6.6% | −34.4260 to −0.2425 | yes: GAIN |
| response time (ms), 95th percentile | 877.8 | 952.3 | +8.5% | +22.1906 to +126.9374 | yes: LOSS |
| response time (ms), 99th percentile | 1207 | 1326 | +9.9% | −14.7391 to +253.5361 | no |
| time over the response line (% of samples) | 8.548 | 9.797 | +14.6% | −0.2424 to +2.7407 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 7.1 | +26.8% | +0.0595 to +2.9405 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.7 | +154.700 (native is 0) | +88.6916 to +220.7084 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.343 | 8.97 | −4.0% | −1.9965 to +1.2499 | no |
| utilisation (used / allocatable) | 0.05801 | 0.07907 | +36.3% | +0.0102 to +0.0319 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.352 | −2.9% | −0.0783 to −0.0031 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06927 | +0.069 (native is 0) | +0.0620 to +0.0765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.421 | +2.1% | −0.0141 to +0.0713 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.6 | 388.7 | −17.9% | −127.3517 to −42.5403 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.211 | +12.0% | +0.0245 to +0.4503 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.0100 to +2.1900 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | −0.0163 to +5.2163 | no |
| pod start wait, mean (s) | 0.2 | 1.183 | +491.7% | −0.1854 to +2.1520 | no |
| host CPU busy, the real machine under kind (%) | 39.15 | 42.14 | +7.6% | +2.1762 to +3.7932 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.7 | 762 | +0.3% | −2.0972 to +6.6972 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.407 | −43.2% | −3.7001 to −1.4853 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.0375 | −10.0% | −0.0370 to +0.0286 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | −33.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.84 | 68.63 | +4.2% | −0.0031 to +5.5781 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.359 | −27.4% | −2.4284 to −0.8539 | yes: GAIN |
| node-hours | 2.512 | 1.828 | −27.2% | −1.0149 to −0.3538 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.6 | −0.0% | −0.6925 to +0.5487 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 220 | −19.0% | −76.5990 to −26.7198 | yes: GAIN |
| response time (ms), mean | 274 | 246.2 | −10.1% | −54.7149 to −0.8697 | yes: GAIN |
| response time (ms), 95th percentile | 1050 | 952.3 | −9.3% | −300.5690 to +104.3530 | no |
| response time (ms), 99th percentile | 1521 | 1326 | −12.8% | −447.7206 to +58.9292 | no |
| time over the response line (% of samples) | 8.52 | 9.797 | +15.0% | −0.5225 to +3.0771 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.1 | ±0.0% | −0.9537 to +0.9537 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.7 | +154.700 (native is 0) | +88.6916 to +220.7084 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.25 | 8.97 | −48.0% | −14.6154 to −1.9546 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05809 | 0.07907 | +36.1% | +0.0097 to +0.0323 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.352 | −3.1% | −0.0786 to −0.0065 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06927 | +0.069 (native is 0) | +0.0620 to +0.0765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.421 | +1.9% | −0.0133 to +0.0667 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 388.7 | −18.0% | −131.7827 to −39.1330 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.211 | +10.6% | +0.0062 to +0.4174 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.0100 to +2.1900 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | −0.0163 to +5.2163 | no |
| pod start wait, mean (s) | 0.2 | 1.183 | +491.7% | −0.1854 to +2.1520 | no |
| host CPU busy, the real machine under kind (%) | 41.43 | 42.14 | +1.7% | −0.0371 to +1.4419 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.8 | 762 | −2.0% | −31.3909 to −0.2091 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.407 | −43.2% | −3.7001 to −1.4853 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8333 | 0.0375 | −95.5% | −1.0458 to −0.5459 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.2 | −89.5% | −2.9639 to −0.4361 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 84.99 | 68.63 | −19.3% | −29.6391 to −3.0859 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.523 | −24.6% | −2.2189 to −0.7342 | yes: GAIN |
| node-hours | 2.51 | 1.896 | −24.5% | −0.9225 to −0.3070 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.7 | +0.2% | −0.7837 to +1.6674 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 225.3 | −17.0% | −69.5426 to −22.4321 | yes: GAIN |
| response time (ms), mean | 263.5 | 277.7 | +5.4% | −22.5256 to +50.8264 | no |
| response time (ms), 95th percentile | 877.8 | 1220 | +39.0% | −0.2630 to +684.8300 | no |
| response time (ms), 99th percentile | 1207 | 1748 | +44.8% | +102.5333 to +979.4253 | yes: LOSS |
| time over the response line (% of samples) | 8.548 | 9.671 | +13.1% | −1.8272 to +4.0739 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 8.3 | +48.2% | +0.7615 to +4.6385 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.2 | +113.200 (native is 0) | +55.7199 to +170.6801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.343 | 23.08 | +147.0% | −0.7364 to +28.2031 | no |
| utilisation (used / allocatable) | 0.05801 | 0.07677 | +32.3% | +0.0091 to +0.0285 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.367 | −1.9% | −0.0738 to +0.0222 | no |
| Omni's own CPU (cores), mean | 0 | 0.0733 | +0.073 (native is 0) | +0.0648 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.44 | +3.4% | −0.0069 to +0.1019 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.6 | 395.5 | −16.5% | −115.1599 to −41.0533 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.092 | +6.0% | −0.0592 to +0.2973 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.3818 to +2.1818 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | −0.3690 to +1.7690 | no |
| host CPU busy, the real machine under kind (%) | 39.15 | 44.76 | +14.3% | +4.3046 to +6.9057 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.7 | 793.6 | +4.5% | +1.0539 to +66.7461 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.514 | −41.4% | −3.3793 to −1.5925 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.8667 | +1980.0% | +0.5850 to +1.0650 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.8 | +500.0% | +0.5315 to +2.4685 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.84 | 96.85 | +47.1% | +5.9947 to +56.0220 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*