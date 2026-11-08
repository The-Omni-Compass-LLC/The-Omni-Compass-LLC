# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.543 | 4.605 |
| node-hours | 2.513 | 2.513 | 1.905 | 1.929 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.5 | 272.8 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 272.5 | 226.9 | 228.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 348.2 | 302.8 | 344.9 | 288.6 |
| response time (ms), 95th percentile | 1255 | 1205 | 1439 | 1354 |
| response time (ms), 99th percentile | 1795 | 1795 | 2006 | 2023 |
| time over the response line (% of samples) | 14.53 | 10.24 | 15.47 | 10.69 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6.9 | 8.1 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 129.1 | 143.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 5.263 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.643 | 15.25 | 11.54 | 20.19 |
| utilisation (used / allocatable) | 0.06057 | 0.0607 | 0.0811 | 0.08029 |
| CPU used (cores), mean | 1.454 | 1.457 | 1.431 | 1.447 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0724 | 0.07543 |
| CPU used with Omni's own (cores), mean | 1.454 | 1.457 | 1.504 | 1.522 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 459.4 | 378.5 | 379.1 |
| HPA replicas, mean | 1.966 | 1.996 | 2.094 | 2.145 |
| pods started | 0.2 | 0.4 | 0.8 | 0.7 |
| pod start wait, total (s) | 0.4 | 0.9 | 2.1 | 1.4 |
| pod start wait, mean (s) | 0.4 | 0.45 | 1.267 | 0.6667 |
| host CPU busy, the real machine under kind (%) | 41.22 | 42.51 | 44.49 | 45.62 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 786.6 | 800 | 799.5 | 811.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.879 | 3.903 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.7667 | 0.09583 | 0.8917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.9 | 0.6 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 91.92 | 108.5 | 103.4 | 121.7 |
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
| worker nodes in service, mean | 6 | 4.605 | −23.2% | −2.3437 to −0.4460 | yes: GAIN |
| node-hours | 2.513 | 1.929 | −23.2% | −0.9808 to −0.1866 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.6 | +0.1% | −0.7778 to +1.0727 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 228.8 | −16.0% | −73.7685 to −13.5158 | yes: GAIN |
| response time (ms), mean | 302.8 | 288.6 | −4.7% | −40.0388 to +11.6421 | no |
| response time (ms), 95th percentile | 1205 | 1354 | +12.4% | −58.9267 to +357.5317 | no |
| response time (ms), 99th percentile | 1795 | 2023 | +12.7% | −123.4346 to +579.8466 | no |
| time over the response line (% of samples) | 10.24 | 10.69 | +4.4% | −1.0832 to +1.9764 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.3 | +5.8% | −0.9985 to +1.7985 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.5 | +143.500 (native is 0) | +59.7535 to +227.2465 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.25 | 20.19 | +32.4% | +0.6972 to +9.1928 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0607 | 0.08029 | +32.3% | +0.0070 to +0.0322 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.457 | 1.447 | −0.7% | −0.0547 to +0.0346 | no |
| Omni's own CPU (cores), mean | 0 | 0.07543 | +0.075 (native is 0) | +0.0674 to +0.0835 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.457 | 1.522 | +4.5% | +0.0151 to +0.1157 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.4 | 379.1 | −17.5% | −130.8939 to −29.7746 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.996 | 2.145 | +7.4% | −0.1472 to +0.4444 | no |
| pods started | 0.4 | 0.7 | +75.0% | −0.9181 to +1.5181 | no |
| pod start wait, total (s) | 0.9 | 1.4 | +55.6% | −2.0290 to +3.0290 | no |
| pod start wait, mean (s) | 0.45 | 0.6667 | +48.1% | −0.9992 to +1.4325 | no |
| host CPU busy, the real machine under kind (%) | 42.51 | 45.62 | +7.3% | +2.2213 to +4.0094 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 800 | 811.3 | +1.4% | −0.6029 to +23.2029 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.903 | −34.9% | −3.3888 to −0.8049 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7667 | 0.8917 | +16.3% | −0.0340 to +0.2840 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.5 | +31.6% | −0.1689 to +1.3689 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.5 | 121.7 | +12.2% | +1.8338 to +24.5495 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.513 | 0.0% | raw −0.0083 to +0.0083 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.5 | +0.0% | −1.0184 to +1.1178 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 272.5 | +0.0% | −1.0184 to +1.1178 | no |
| response time (ms), mean | 348.2 | 302.8 | −13.0% | −83.9029 to −6.9790 | yes: GAIN |
| response time (ms), 95th percentile | 1255 | 1205 | −4.0% | −239.6425 to +138.6145 | no |
| response time (ms), 99th percentile | 1795 | 1795 | −0.0% | −200.2320 to +200.1962 | no |
| time over the response line (% of samples) | 14.53 | 10.24 | −29.5% | −7.6620 to −0.9080 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6.9 | −10.4% | −1.9583 to +0.3583 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.643 | 15.25 | +58.1% | +2.7954 to +8.4146 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06057 | 0.0607 | +0.2% | −0.0009 to +0.0012 | no |
| CPU used (cores), mean | 1.454 | 1.457 | +0.2% | −0.0227 to +0.0292 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.454 | 1.457 | +0.2% | −0.0227 to +0.0292 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 459.4 | +0.2% | −9.0196 to +10.7803 | no |
| HPA replicas, mean | 1.966 | 1.996 | +1.5% | −0.1289 to +0.1888 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | −1.1259 to +2.1259 | no |
| pod start wait, mean (s) | 0.4 | 0.45 | +12.5% | −0.9679 to +1.0679 | no |
| host CPU busy, the real machine under kind (%) | 41.22 | 42.51 | +3.1% | +0.9173 to +1.6494 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.6 | 800 | +1.7% | +4.6121 to +22.1879 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.7667 | +1740.0% | +0.5267 to +0.9233 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.9 | +533.3% | +0.2428 to +2.9572 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 91.92 | 108.5 | +18.0% | +4.6575 to +28.5009 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.543 | −24.3% | −2.4359 to −0.4786 | yes: GAIN |
| node-hours | 2.513 | 1.905 | −24.2% | −1.0168 to −0.1984 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.8 | +0.1% | −0.6581 to +1.3255 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 226.9 | −16.7% | −76.5085 to −14.4866 | yes: GAIN |
| response time (ms), mean | 348.2 | 344.9 | −1.0% | −21.7306 to +15.0662 | no |
| response time (ms), 95th percentile | 1255 | 1439 | +14.7% | +17.9740 to +349.9150 | yes: LOSS |
| response time (ms), 99th percentile | 1795 | 2006 | +11.7% | +20.4455 to +400.6823 | yes: LOSS |
| time over the response line (% of samples) | 14.53 | 15.47 | +6.5% | −1.6711 to +3.5489 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.1 | +5.2% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 129.1 | +129.100 (native is 0) | +57.3578 to +200.8422 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.643 | 11.54 | +19.7% | −1.2136 to +5.0102 | no |
| utilisation (used / allocatable) | 0.06057 | 0.0811 | +33.9% | +0.0069 to +0.0342 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.454 | 1.431 | −1.5% | −0.0678 to +0.0236 | no |
| Omni's own CPU (cores), mean | 0 | 0.0724 | +0.072 (native is 0) | +0.0650 to +0.0798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.454 | 1.504 | +3.5% | −0.0010 to +0.1016 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 378.5 | −17.5% | −132.0182 to −28.1773 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.094 | +6.5% | −0.0743 to +0.3301 | no |
| pods started | 0.2 | 0.8 | +300.0% | −0.3048 to +1.5048 | no |
| pod start wait, total (s) | 0.4 | 2.1 | +425.0% | −0.6374 to +4.0374 | no |
| pod start wait, mean (s) | 0.4 | 1.267 | +216.7% | −0.5154 to +2.2488 | no |
| host CPU busy, the real machine under kind (%) | 41.22 | 44.49 | +7.9% | +2.5031 to +4.0191 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.6 | 799.5 | +1.6% | +1.7293 to +24.0707 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.879 | −35.3% | −3.4552 to −0.7859 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.09583 | +130.0% | −0.0087 to +0.1171 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | −0.3786 to +0.9786 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.92 | 103.4 | +12.5% | +2.0576 to +20.9591 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.543 | −24.3% | −2.4359 to −0.4786 | yes: GAIN |
| node-hours | 2.513 | 1.905 | −24.2% | −1.0166 to −0.1985 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.8 | +0.1% | −0.8734 to +1.4413 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 226.9 | −16.7% | −76.2954 to −14.7992 | yes: GAIN |
| response time (ms), mean | 302.8 | 344.9 | +13.9% | +2.0235 to +82.1941 | yes: LOSS |
| response time (ms), 95th percentile | 1205 | 1439 | +19.5% | +56.4554 to +412.4616 | yes: LOSS |
| response time (ms), 99th percentile | 1795 | 2006 | +11.7% | −26.1533 to +447.3169 | no |
| time over the response line (% of samples) | 10.24 | 15.47 | +51.0% | +1.1416 to +9.3063 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 8.1 | +17.4% | −0.4101 to +2.8101 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 129.1 | +129.100 (native is 0) | +57.3578 to +200.8422 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.25 | 11.54 | −24.3% | −5.3229 to −2.0905 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0607 | 0.0811 | +33.6% | +0.0063 to +0.0345 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.457 | 1.431 | −1.7% | −0.0652 to +0.0144 | no |
| Omni's own CPU (cores), mean | 0 | 0.0724 | +0.072 (native is 0) | +0.0650 to +0.0798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.457 | 1.504 | +3.2% | +0.0032 to +0.0908 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.4 | 378.5 | −17.6% | −136.8672 to −25.0889 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.996 | 2.094 | +4.9% | −0.0627 to +0.2585 | no |
| pods started | 0.4 | 0.8 | +100.0% | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.9 | 2.1 | +133.3% | +0.2583 to +2.1417 | yes: LOSS |
| pod start wait, mean (s) | 0.45 | 1.267 | +181.5% | +0.0131 to +1.6202 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.51 | 44.49 | +4.7% | +1.3219 to +2.6335 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 800 | 799.5 | −0.1% | −6.8556 to +5.8556 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.879 | −35.3% | −3.4552 to −0.7859 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7667 | 0.09583 | −87.5% | −0.8494 to −0.4923 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.6 | −68.4% | −2.8834 to +0.2834 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.5 | 103.4 | −4.7% | −11.0141 to +0.8724 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.605 | −23.2% | −2.3437 to −0.4460 | yes: GAIN |
| node-hours | 2.513 | 1.929 | −23.2% | −0.9804 to −0.1870 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.6 | +0.1% | −0.9290 to +1.3233 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 228.8 | −16.0% | −73.9416 to −13.2434 | yes: GAIN |
| response time (ms), mean | 348.2 | 288.6 | −17.1% | −80.4262 to −38.8525 | yes: GAIN |
| response time (ms), 95th percentile | 1255 | 1354 | +7.9% | −137.8215 to +335.3985 | no |
| response time (ms), 99th percentile | 1795 | 2023 | +12.7% | −122.5120 to +578.8882 | no |
| time over the response line (% of samples) | 14.53 | 10.69 | −26.4% | −7.1098 to −0.5670 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.3 | −5.2% | −1.6251 to +0.8251 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.5 | +143.500 (native is 0) | +59.7535 to +227.2465 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.643 | 20.19 | +109.4% | +4.1247 to +16.9753 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06057 | 0.08029 | +32.6% | +0.0076 to +0.0318 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.454 | 1.447 | −0.5% | −0.0608 to +0.0473 | no |
| Omni's own CPU (cores), mean | 0 | 0.07543 | +0.075 (native is 0) | +0.0674 to +0.0835 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.454 | 1.522 | +4.7% | +0.0082 to +0.1291 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.6 | 379.1 | −17.3% | −125.5680 to −33.3399 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.145 | +9.1% | −0.1069 to +0.4640 | no |
| pods started | 0.2 | 0.7 | +250.0% | −0.5256 to +1.5256 | no |
| pod start wait, total (s) | 0.4 | 1.4 | +250.0% | −1.0232 to +3.0232 | no |
| pod start wait, mean (s) | 0.4 | 0.6667 | +66.7% | −0.8895 to +1.4228 | no |
| host CPU busy, the real machine under kind (%) | 41.22 | 45.62 | +10.7% | +3.4086 to +5.3888 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.6 | 811.3 | +3.1% | +4.6940 to +44.7060 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.903 | −34.9% | −3.3888 to −0.8049 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.8917 | +2040.0% | +0.5250 to +1.1750 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.5 | +733.3% | +0.1824 to +4.2176 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 91.92 | 121.7 | +32.4% | +7.3904 to +52.1513 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*