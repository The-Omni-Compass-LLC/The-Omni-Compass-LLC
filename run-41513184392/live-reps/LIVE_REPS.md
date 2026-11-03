# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.316 | 5.471 |
| node-hours | 2.515 | 2.512 | 2.226 | 2.295 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 274.6 | 275.1 | 275.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 274.6 | 253.7 | 258.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 518.6 | 538.6 | 510.9 | 533.8 |
| response time (ms), 95th percentile | 1997 | 2117 | 2221 | 2301 |
| response time (ms), 99th percentile | 2923 | 2931 | 3173 | 3155 |
| time over the response line (% of samples) | 24.02 | 24.44 | 23.63 | 24.48 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.8 | 12.1 | 13 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 89.7 | 84.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 40 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.89 | 14.87 | 18.19 | 17.8 |
| utilisation (used / allocatable) | 0.06729 | 0.06688 | 0.07735 | 0.07516 |
| CPU used (cores), mean | 1.615 | 1.605 | 1.622 | 1.629 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07635 | 0.07903 |
| CPU used with Omni's own (cores), mean | 1.615 | 1.605 | 1.699 | 1.708 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.6 | 418.6 | 373.9 | 381.7 |
| HPA replicas, mean | 2.118 | 1.972 | 2.429 | 2.383 |
| pods started | 0 | 0 | 1.5 | 1.3 |
| pod start wait, total (s) | 0 | 0 | 3.1 | 3 |
| pod start wait, mean (s) | 0 | 0 | 1.308 | 0.9167 |
| host CPU busy, the real machine under kind (%) | 45.83 | 46.7 | 49.31 | 50.14 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 839.3 | 851.3 | 856 | 865 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.822 | 5.027 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.5292 | 0.2375 | 1.246 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 2.5 | 1.2 | 4.4 |
| queue: job turnaround, submitted to done, mean (s) | 144.6 | 155.9 | 160.5 | 168.2 |
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
| worker nodes in service, mean | 6 | 5.471 | −8.8% | −1.1473 to +0.0903 | no |
| node-hours | 2.512 | 2.295 | −8.6% | −0.4755 to +0.0434 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.5 | +0.3% | +0.1823 to +1.5378 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 258.9 | −5.7% | −35.1716 to +3.6792 | no |
| response time (ms), mean | 538.6 | 533.8 | −0.9% | −21.5612 to +12.1186 | no |
| response time (ms), 95th percentile | 2117 | 2301 | +8.7% | +14.6027 to +353.7093 | yes: LOSS |
| response time (ms), 99th percentile | 2931 | 3155 | +7.6% | +46.6479 to +400.0241 | yes: LOSS |
| time over the response line (% of samples) | 24.44 | 24.48 | +0.2% | −0.8572 to +0.9456 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 13 | +10.2% | −0.0526 to +2.4526 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.8 | +84.800 (native is 0) | +15.9199 to +153.6801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.87 | 17.8 | +19.7% | +1.3445 to +4.5055 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06688 | 0.07516 | +12.4% | −0.0011 to +0.0177 | no |
| CPU used (cores), mean | 1.605 | 1.629 | +1.5% | +0.0070 to +0.0405 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07903 | +0.079 (native is 0) | +0.0721 to +0.0860 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 1.708 | +6.4% | +0.0881 to +0.1175 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.6 | 381.7 | −8.8% | −81.0995 to +7.1930 | no |
| HPA replicas, mean | 1.972 | 2.383 | +20.8% | +0.0877 to +0.7343 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.0361 to +2.5639 | yes: power given |
| pod start wait, total (s) | 0 | 3 | +3.000 (native is 0) | −0.0160 to +6.0160 | no |
| pod start wait, mean (s) | 0 | 0.9167 | +0.917 (native is 0) | +0.0460 to +1.7873 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.7 | 50.14 | +7.4% | +3.0093 to +3.8593 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.3 | 865 | +1.6% | +4.9066 to +22.4934 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.027 | −16.2% | −1.8968 to −0.0499 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5292 | 1.246 | +135.4% | +0.1799 to +1.2535 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 4.4 | +76.0% | −1.0095 to +4.8095 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.9 | 168.2 | +7.9% | +5.9849 to +18.4984 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.515 | 2.512 | −0.1% | −0.0111 to +0.0041 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 274.6 | −0.2% | −1.4515 to +0.4076 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 274.6 | −0.2% | −1.4515 to +0.4076 | no |
| response time (ms), mean | 518.6 | 538.6 | +3.9% | −1.2029 to +41.2081 | no |
| response time (ms), 95th percentile | 1997 | 2117 | +6.0% | −67.3309 to +306.1869 | no |
| response time (ms), 99th percentile | 2923 | 2931 | +0.3% | −138.3066 to +155.5792 | no |
| time over the response line (% of samples) | 24.02 | 24.44 | +1.7% | −0.2021 to +1.0383 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.8 | +4.4% | −0.6802 to +1.6802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.89 | 14.87 | +7.1% | −1.4786 to +3.4386 | no |
| utilisation (used / allocatable) | 0.06729 | 0.06688 | −0.6% | −0.0014 to +0.0005 | no |
| CPU used (cores), mean | 1.615 | 1.605 | −0.6% | −0.0329 to +0.0129 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.615 | 1.605 | −0.6% | −0.0329 to +0.0129 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.6 | 418.6 | +1.0% | −4.7979 to +12.7802 | no |
| HPA replicas, mean | 2.118 | 1.972 | −6.9% | −0.3154 to +0.0227 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 45.83 | 46.7 | +1.9% | +0.4387 to +1.2959 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 839.3 | 851.3 | +1.4% | +4.9752 to +19.0248 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.5292 | +693.8% | −0.0759 to +1.0009 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 2.5 | +525.0% | −0.7702 to +4.9702 | no |
| queue: job turnaround, submitted to done, mean (s) | 144.6 | 155.9 | +7.8% | +4.4129 to +18.1705 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.316 | −11.4% | −1.4628 to +0.0940 | no |
| node-hours | 2.515 | 2.226 | −11.5% | −0.6199 to +0.0415 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 275.1 | −0.0% | −0.9143 to +0.8193 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 253.7 | −7.8% | −46.5174 to +3.5140 | no |
| response time (ms), mean | 518.6 | 510.9 | −1.5% | −25.0915 to +9.7211 | no |
| response time (ms), 95th percentile | 1997 | 2221 | +11.2% | +41.7157 to +405.1493 | yes: LOSS |
| response time (ms), 99th percentile | 2923 | 3173 | +8.6% | +26.5155 to +473.7981 | yes: LOSS |
| time over the response line (% of samples) | 24.02 | 23.63 | −1.6% | −1.0411 to +0.2605 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 12.1 | +7.1% | −0.3081 to +1.9081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.7 | +89.700 (native is 0) | +21.0677 to +158.3323 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.89 | 18.18 | +30.9% | +0.4951 to +8.0916 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06729 | 0.07735 | +14.9% | −0.0009 to +0.0210 | no |
| CPU used (cores), mean | 1.615 | 1.622 | +0.5% | −0.0126 to +0.0274 | no |
| Omni's own CPU (cores), mean | 0 | 0.07635 | +0.076 (native is 0) | +0.0705 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.615 | 1.699 | +5.2% | +0.0589 to +0.1086 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.6 | 373.9 | −9.8% | −84.7768 to +3.2835 | no |
| HPA replicas, mean | 2.118 | 2.429 | +14.7% | +0.0836 to +0.5375 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.5315 to +2.4685 | yes: power given |
| pod start wait, total (s) | 0 | 3.1 | +3.100 (native is 0) | +0.5665 to +5.6335 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.308 | +1.308 (native is 0) | +0.5777 to +2.0390 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.83 | 49.31 | +7.6% | +3.0620 to +3.8877 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 839.3 | 856 | +2.0% | +8.2697 to +25.1303 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.822 | −19.6% | −2.4341 to +0.0784 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.2375 | +256.2% | −0.0563 to +0.3980 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.2 | +200.0% | −0.6621 to +2.2621 | no |
| queue: job turnaround, submitted to done, mean (s) | 144.6 | 160.5 | +11.0% | +7.4273 to +24.3060 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.316 | −11.4% | −1.4628 to +0.0940 | no |
| node-hours | 2.512 | 2.226 | −11.4% | −0.6125 to +0.0410 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.1 | +0.2% | −0.3234 to +1.2723 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 253.7 | −7.6% | −45.3474 to +3.3879 | no |
| response time (ms), mean | 538.6 | 510.9 | −5.1% | −38.8809 to −16.4947 | yes: GAIN |
| response time (ms), 95th percentile | 2117 | 2221 | +4.9% | −63.3623 to +271.3713 | no |
| response time (ms), 99th percentile | 2931 | 3173 | +8.2% | +12.9118 to +470.1292 | yes: LOSS |
| time over the response line (% of samples) | 24.44 | 23.63 | −3.3% | −1.5671 to −0.0496 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 12.1 | +2.5% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.7 | +89.700 (native is 0) | +21.0677 to +158.3323 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.87 | 18.18 | +22.3% | +0.3319 to +6.2948 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06688 | 0.07735 | +15.7% | −0.0010 to +0.0220 | no |
| CPU used (cores), mean | 1.605 | 1.622 | +1.1% | +0.0035 to +0.0314 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07635 | +0.076 (native is 0) | +0.0705 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 1.699 | +5.8% | +0.0779 to +0.1096 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.6 | 373.9 | −10.7% | −94.4420 to +4.9665 | no |
| HPA replicas, mean | 1.972 | 2.429 | +23.2% | +0.2819 to +0.6320 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.5315 to +2.4685 | yes: power given |
| pod start wait, total (s) | 0 | 3.1 | +3.100 (native is 0) | +0.5665 to +5.6335 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.308 | +1.308 (native is 0) | +0.5777 to +2.0390 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.7 | 49.31 | +5.6% | +2.3648 to +2.8502 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.3 | 856 | +0.6% | +0.3679 to +9.0321 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.822 | −19.6% | −2.4341 to +0.0784 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5292 | 0.2375 | −55.1% | −0.6151 to +0.0318 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 1.2 | −52.0% | −3.0210 to +0.4210 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.9 | 160.5 | +2.9% | +0.3756 to +8.7744 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.471 | −8.8% | −1.1473 to +0.0903 | no |
| node-hours | 2.515 | 2.295 | −8.7% | −0.4813 to +0.0421 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 275.5 | +0.1% | −0.5964 to +1.2726 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 258.9 | −5.9% | −36.2783 to +3.7419 | no |
| response time (ms), mean | 518.6 | 533.8 | +2.9% | −5.6750 to +36.2377 | no |
| response time (ms), 95th percentile | 1997 | 2301 | +15.2% | +151.7520 to +455.4160 | yes: LOSS |
| response time (ms), 99th percentile | 2923 | 3155 | +7.9% | +68.7691 to +395.1755 | yes: LOSS |
| time over the response line (% of samples) | 24.02 | 24.48 | +1.9% | −0.3033 to +1.2279 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 13 | +15.0% | +0.2283 to +3.1717 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.8 | +84.800 (native is 0) | +15.9199 to +153.6801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.89 | 17.8 | +28.1% | +0.3590 to +7.4510 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06729 | 0.07516 | +11.7% | −0.0008 to +0.0165 | no |
| CPU used (cores), mean | 1.615 | 1.629 | +0.8% | −0.0055 to +0.0329 | no |
| Omni's own CPU (cores), mean | 0 | 0.07903 | +0.079 (native is 0) | +0.0721 to +0.0860 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.615 | 1.708 | +5.7% | +0.0715 to +0.1140 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.6 | 381.7 | −7.9% | −69.2184 to +3.2942 | no |
| HPA replicas, mean | 2.118 | 2.383 | +12.5% | −0.0776 to +0.6069 | no |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.0361 to +2.5639 | yes: power given |
| pod start wait, total (s) | 0 | 3 | +3.000 (native is 0) | −0.0160 to +6.0160 | no |
| pod start wait, mean (s) | 0 | 0.9167 | +0.917 (native is 0) | +0.0460 to +1.7873 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.83 | 50.14 | +9.4% | +4.0320 to +4.5712 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 839.3 | 865 | +3.1% | +14.4958 to +36.9042 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.027 | −16.2% | −1.8968 to −0.0499 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 1.246 | +1768.8% | +0.4041 to +1.9542 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 4.4 | +1000.0% | +0.6619 to +7.3381 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 144.6 | 168.2 | +16.3% | +12.9892 to +34.0775 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*