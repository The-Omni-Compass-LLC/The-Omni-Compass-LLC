# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.714 | 4.53 |
| node-hours | 2.512 | 2.512 | 1.979 | 1.897 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.6 | 271.9 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.6 | 231.5 | 225.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 296 | 330 | 288.3 | 314.5 |
| response time (ms), 95th percentile | 1054 | 1349 | 1125 | 1429 |
| response time (ms), 99th percentile | 1512 | 1884 | 1663 | 1973 |
| time over the response line (% of samples) | 11.44 | 11.02 | 12.42 | 10.91 |
| failed requests (%) | 0 | 0 | 0.0331 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.8 | 7.5 | 7.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 160.4 | 111.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 12.5 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.292 | 20.88 | 10.88 | 25.79 |
| utilisation (used / allocatable) | 0.0579 | 0.05815 | 0.0748 | 0.07805 |
| CPU used (cores), mean | 1.39 | 1.396 | 1.361 | 1.38 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06798 | 0.07371 |
| CPU used with Omni's own (cores), mean | 1.39 | 1.396 | 1.429 | 1.454 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481 | 482.6 | 410.6 | 394.6 |
| HPA replicas, mean | 2.011 | 2.022 | 2.273 | 2.14 |
| pods started | 0 | 0 | 0.8 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 1.6 | 1.2 |
| pod start wait, mean (s) | 0 | 0 | 1 | 0.6 |
| host CPU busy, the real machine under kind (%) | 39.36 | 41.59 | 42.22 | 44.77 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 774.4 | 802.7 | 780.3 | 810.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.149 | 3.707 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 1.038 | 0.0875 | 1.096 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 2.5 | 0.7 | 3 |
| queue: job turnaround, submitted to done, mean (s) | 78.93 | 105.6 | 85.79 | 113 |
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
| worker nodes in service, mean | 6 | 4.53 | −24.5% | −2.3930 to −0.5466 | yes: GAIN |
| node-hours | 2.512 | 1.897 | −24.5% | −1.0043 to −0.2248 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.6 | +0.0% | −0.9929 to +1.0546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 225.5 | −17.0% | −75.4338 to −16.7378 | yes: GAIN |
| response time (ms), mean | 330 | 314.5 | −4.7% | −41.4995 to +10.4047 | no |
| response time (ms), 95th percentile | 1349 | 1429 | +5.9% | −23.4980 to +183.8370 | no |
| response time (ms), 99th percentile | 1884 | 1973 | +4.8% | −27.5772 to +207.3382 | no |
| time over the response line (% of samples) | 11.02 | 10.91 | −0.9% | −0.9888 to +0.7815 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.2 | +5.9% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.9 | +111.900 (native is 0) | +66.6921 to +157.1079 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.88 | 25.79 | +23.5% | +0.6694 to +9.1472 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05815 | 0.07805 | +34.2% | +0.0068 to +0.0330 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.396 | 1.38 | −1.1% | −0.0432 to +0.0114 | no |
| Omni's own CPU (cores), mean | 0 | 0.07371 | +0.074 (native is 0) | +0.0637 to +0.0837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.396 | 1.454 | +4.1% | +0.0223 to +0.0933 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.6 | 394.6 | −18.2% | −148.8265 to −27.0807 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.022 | 2.14 | +5.8% | −0.0561 to +0.2915 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.3379 to +2.7379 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| host CPU busy, the real machine under kind (%) | 41.59 | 44.77 | +7.6% | +2.7331 to +3.6257 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.7 | 810.2 | +0.9% | −0.4956 to +15.4956 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.707 | −38.2% | −3.5134 to −1.0719 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.038 | 1.096 | +5.6% | −0.0016 to +0.1183 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 3 | +20.0% | −0.1952 to +1.1952 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.6 | 113 | +7.0% | +1.2339 to +13.4744 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.512 | −0.0% | −0.0112 to +0.0102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.6 | +0.1% | −0.7650 to +1.0985 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.6 | +0.1% | −0.7650 to +1.0985 | no |
| response time (ms), mean | 296 | 330 | +11.5% | −0.8406 to +69.0084 | no |
| response time (ms), 95th percentile | 1054 | 1349 | +27.9% | +7.0943 to +582.2287 | yes: LOSS |
| response time (ms), 99th percentile | 1512 | 1884 | +24.6% | +35.9803 to +706.6819 | yes: LOSS |
| time over the response line (% of samples) | 11.44 | 11.02 | −3.7% | −3.1301 to +2.2784 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.8 | +4.6% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.292 | 20.88 | +124.7% | +2.2731 to +20.9036 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0579 | 0.05815 | +0.4% | −0.0010 to +0.0015 | no |
| CPU used (cores), mean | 1.39 | 1.396 | +0.4% | −0.0244 to +0.0365 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.39 | 1.396 | +0.4% | −0.0244 to +0.0365 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481 | 482.6 | +0.3% | −7.7511 to +10.8674 | no |
| HPA replicas, mean | 2.011 | 2.022 | +0.6% | −0.1537 to +0.1766 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 39.36 | 41.59 | +5.7% | +0.8310 to +3.6211 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 774.4 | 802.7 | +3.7% | +2.3904 to +54.2096 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 1.038 | +1815.4% | +0.5237 to +1.4430 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 2.5 | +1150.0% | +0.4515 to +4.1485 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.93 | 105.6 | +33.8% | +4.2512 to +49.1154 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.714 | −21.4% | −2.2819 to −0.2895 | yes: GAIN |
| node-hours | 2.512 | 1.979 | −21.2% | −0.9484 to −0.1186 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.9 | +0.2% | −0.0113 to +0.9517 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 231.5 | −14.7% | −71.1685 to −8.7411 | yes: GAIN |
| response time (ms), mean | 296 | 288.3 | −2.6% | −18.0701 to +2.6860 | no |
| response time (ms), 95th percentile | 1054 | 1125 | +6.7% | +12.6017 to +127.9223 | yes: LOSS |
| response time (ms), 99th percentile | 1512 | 1663 | +10.0% | −22.5559 to +324.6527 | no |
| time over the response line (% of samples) | 11.44 | 12.42 | +8.5% | −1.0298 to +2.9788 | no |
| failed requests (%) | 0 | 0.0331 | +0.033 (native is 0) | −0.0205 to +0.0867 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 7.5 | +15.4% | +0.1079 to +1.8921 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 160.4 | +160.400 (native is 0) | +93.9785 to +226.8215 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.292 | 10.88 | +17.1% | −1.3710 to +4.5410 | no |
| utilisation (used / allocatable) | 0.0579 | 0.0748 | +29.2% | +0.0029 to +0.0309 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.39 | 1.361 | −2.1% | −0.0673 to +0.0092 | no |
| Omni's own CPU (cores), mean | 0 | 0.06798 | +0.068 (native is 0) | +0.0599 to +0.0761 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.39 | 1.429 | +2.8% | −0.0058 to +0.0836 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481 | 410.6 | −14.6% | −126.5905 to −14.2074 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.273 | +13.0% | −0.0383 to +0.5624 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.0612 to +1.5388 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | +0.1225 to +3.0775 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1.000 (native is 0) | +0.2460 to +1.7540 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.36 | 42.22 | +7.3% | +2.0464 to +3.6743 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 774.4 | 780.3 | +0.8% | +0.3855 to +11.4145 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.149 | −30.9% | −3.1807 to −0.5216 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0875 | +61.5% | −0.0658 to +0.1325 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.7 | +250.0% | −0.4079 to +1.4079 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.93 | 85.79 | +8.7% | +0.3329 to +13.3921 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.714 | −21.4% | −2.2819 to −0.2895 | yes: GAIN |
| node-hours | 2.512 | 1.979 | −21.2% | −0.9546 to −0.1114 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.9 | +0.1% | −0.4474 to +1.0542 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 231.5 | −14.8% | −71.7806 to −8.4626 | yes: GAIN |
| response time (ms), mean | 330 | 288.3 | −12.7% | −76.7058 to −6.8461 | yes: GAIN |
| response time (ms), 95th percentile | 1349 | 1125 | −16.6% | −511.0885 to +62.2895 | no |
| response time (ms), 99th percentile | 1884 | 1663 | −11.7% | −509.9802 to +69.4148 | no |
| time over the response line (% of samples) | 11.02 | 12.42 | +12.7% | −0.0684 to +2.8692 | no |
| failed requests (%) | 0 | 0.0331 | +0.033 (native is 0) | −0.0205 to +0.0867 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.5 | +10.3% | −0.5181 to +1.9181 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 160.4 | +160.400 (native is 0) | +93.9785 to +226.8215 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.88 | 10.88 | −47.9% | −17.1831 to −2.8236 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05815 | 0.0748 | +28.6% | +0.0018 to +0.0315 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.396 | 1.361 | −2.5% | −0.0676 to −0.0027 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06798 | +0.068 (native is 0) | +0.0599 to +0.0761 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.396 | 1.429 | +2.4% | −0.0030 to +0.0687 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.6 | 410.6 | −14.9% | −133.8133 to −10.1009 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.022 | 2.273 | +12.4% | −0.0679 to +0.5691 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.0612 to +1.5388 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | +0.1225 to +3.0775 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1.000 (native is 0) | +0.2460 to +1.7540 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.59 | 42.22 | +1.5% | −0.3069 to +1.5756 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.7 | 780.3 | −2.8% | −43.1184 to −1.6816 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.149 | −30.9% | −3.1807 to −0.5216 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.038 | 0.0875 | −91.6% | −1.3584 to −0.5416 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 0.7 | −72.0% | −2.9583 to −0.6417 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 105.6 | 85.79 | −18.8% | −36.3415 to −3.3002 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.53 | −24.5% | −2.3930 to −0.5466 | yes: GAIN |
| node-hours | 2.512 | 1.897 | −24.5% | −0.9986 to −0.2315 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.6 | +0.1% | −0.5164 to +0.9116 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 225.5 | −16.9% | −74.9054 to −16.9327 | yes: GAIN |
| response time (ms), mean | 296 | 314.5 | +6.3% | −25.5129 to +62.5859 | no |
| response time (ms), 95th percentile | 1054 | 1429 | +35.6% | −2.9089 to +752.5709 | no |
| response time (ms), 99th percentile | 1512 | 1973 | +30.5% | +30.0174 to +892.4058 | yes: LOSS |
| time over the response line (% of samples) | 11.44 | 10.91 | −4.6% | −3.3699 to +2.3109 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 7.2 | +10.8% | +0.1111 to +1.2889 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.9 | +111.900 (native is 0) | +66.6921 to +157.1079 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.292 | 25.79 | +177.5% | +3.5063 to +29.4870 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0579 | 0.07805 | +34.8% | +0.0080 to +0.0323 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.39 | 1.38 | −0.7% | −0.0539 to +0.0343 | no |
| Omni's own CPU (cores), mean | 0 | 0.07371 | +0.074 (native is 0) | +0.0637 to +0.0837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.39 | 1.454 | +4.6% | +0.0110 to +0.1169 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481 | 394.6 | −18.0% | −141.3823 to −31.4086 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.14 | +6.4% | −0.0656 to +0.3240 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.3379 to +2.7379 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| host CPU busy, the real machine under kind (%) | 39.36 | 44.77 | +13.7% | +3.7335 to +7.0773 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 774.4 | 810.2 | +4.6% | +3.0191 to +68.5809 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.707 | −38.2% | −3.5134 to −1.0719 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 1.096 | +1923.1% | +0.5511 to +1.5322 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 3 | +1400.0% | +0.6199 to +4.9801 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.93 | 113 | +43.1% | +6.0586 to +62.0164 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*