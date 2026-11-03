# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.42 | 5.291 |
| node-hours | 2.514 | 2.514 | 2.268 | 2.217 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.9 | 274.6 | 275.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 274.9 | 256.3 | 252.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 485.6 | 569.8 | 485.1 | 553.1 |
| response time (ms), 95th percentile | 1860 | 2605 | 2123 | 2715 |
| response time (ms), 99th percentile | 2676 | 3591 | 2975 | 3555 |
| time over the response line (% of samples) | 23.42 | 19.85 | 23.22 | 20.26 |
| failed requests (%) | 0 | 0 | 0 | 0.01156 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.8 | 11.6 | 12.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 97.8 | 76.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 31.17 | 12.99 | 37.92 |
| utilisation (used / allocatable) | 0.06614 | 0.06687 | 0.07403 | 0.07644 |
| CPU used (cores), mean | 1.587 | 1.605 | 1.591 | 1.607 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07482 | 0.08365 |
| CPU used with Omni's own (cores), mean | 1.587 | 1.605 | 1.666 | 1.691 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.6 | 418.7 | 387.6 | 378.3 |
| HPA replicas, mean | 2.01 | 2.025 | 2.528 | 2.375 |
| pods started | 0 | 0 | 1.7 | 1.5 |
| pod start wait, total (s) | 0 | 0 | 3.8 | 3.5 |
| pod start wait, mean (s) | 0 | 0 | 1.567 | 1.167 |
| host CPU busy, the real machine under kind (%) | 44.9 | 48.33 | 48.25 | 51.82 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 829.8 | 887 | 843.2 | 903.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.021 | 4.658 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1.062 | 0.3 | 1.483 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 2.7 | 1 | 5.1 |
| queue: job turnaround, submitted to done, mean (s) | 134 | 185.4 | 147 | 199 |
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
| worker nodes in service, mean | 6 | 5.291 | −11.8% | −1.3916 to −0.0273 | yes: GAIN |
| node-hours | 2.514 | 2.217 | −11.8% | −0.5814 to −0.0111 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275.1 | +0.0% | −0.7558 to +1.0191 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 252.8 | −8.1% | −43.7501 to −0.5742 | yes: GAIN |
| response time (ms), mean | 569.8 | 553.1 | −2.9% | −43.4630 to +10.0709 | no |
| response time (ms), 95th percentile | 2605 | 2715 | +4.2% | −51.8976 to +272.6986 | no |
| response time (ms), 99th percentile | 3591 | 3555 | −1.0% | −317.1440 to +246.2992 | no |
| time over the response line (% of samples) | 19.85 | 20.26 | +2.0% | −0.2743 to +1.0771 | no |
| failed requests (%) | 0 | 0.01156 | +0.012 (native is 0) | −0.0146 to +0.0377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 12.1 | +2.5% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 76.5 | +76.500 (native is 0) | +23.4254 to +129.5746 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 31.17 | 37.92 | +21.6% | +2.3729 to +11.1105 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06687 | 0.07644 | +14.3% | +0.0007 to +0.0184 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.605 | 1.607 | +0.1% | −0.0317 to +0.0362 | no |
| Omni's own CPU (cores), mean | 0 | 0.08365 | +0.084 (native is 0) | +0.0760 to +0.0913 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 1.691 | +5.4% | +0.0478 to +0.1241 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.7 | 378.3 | −9.6% | −77.5423 to −3.2363 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.375 | +17.3% | +0.2297 to +0.4704 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.3690 to +2.6310 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | +0.7971 to +6.2029 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.167 | +1.167 (native is 0) | +0.2657 to +2.0676 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.33 | 51.82 | +7.2% | +3.1037 to +3.8743 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 887 | 903.6 | +1.9% | +8.9835 to +24.2165 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.658 | −22.4% | −2.3501 to −0.3346 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.062 | 1.483 | +39.6% | +0.1187 to +0.7230 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 5.1 | +88.9% | +0.7412 to +4.0588 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 185.4 | 199 | +7.4% | +6.3235 to +20.9265 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.514 | 0.0% | raw −0.0076 to +0.0076 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.9 | +0.2% | −0.3747 to +1.2080 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 274.9 | +0.2% | −0.3747 to +1.2080 | no |
| response time (ms), mean | 485.6 | 569.8 | +17.3% | +31.0055 to +137.3445 | yes: LOSS |
| response time (ms), 95th percentile | 1860 | 2605 | +40.0% | +343.4284 to +1146.1686 | yes: LOSS |
| response time (ms), 99th percentile | 2676 | 3591 | +34.2% | +437.0891 to +1392.9013 | yes: LOSS |
| time over the response line (% of samples) | 23.42 | 19.85 | −15.2% | −5.6498 to −1.4735 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.8 | +7.3% | +0.2358 to +1.3642 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 31.17 | +171.1% | +7.7622 to +31.5878 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06614 | 0.06687 | +1.1% | −0.0001 to +0.0015 | no |
| CPU used (cores), mean | 1.587 | 1.605 | +1.1% | −0.0018 to +0.0366 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.587 | 1.605 | +1.1% | −0.0018 to +0.0366 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.6 | 418.7 | −0.7% | −7.2840 to +1.4538 | no |
| HPA replicas, mean | 2.01 | 2.025 | +0.7% | −0.1975 to +0.2266 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 44.9 | 48.33 | +7.6% | +2.4016 to +4.4641 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 829.8 | 887 | +6.9% | +28.7235 to +85.6765 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1.062 | +1400.0% | +0.7566 to +1.2267 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 2.7 | +285.7% | +0.8319 to +3.1681 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 134 | 185.4 | +38.4% | +26.0180 to +76.7487 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.42 | −9.7% | −1.2692 to +0.1099 | no |
| node-hours | 2.514 | 2.268 | −9.8% | −0.5320 to +0.0415 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.6 | +0.0% | −1.0172 to +1.0811 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 256.3 | −6.6% | −39.7895 to +3.3409 | no |
| response time (ms), mean | 485.6 | 485.1 | −0.1% | −25.1794 to +24.1418 | no |
| response time (ms), 95th percentile | 1860 | 2123 | +14.2% | +88.5065 to +438.3135 | yes: LOSS |
| response time (ms), 99th percentile | 2676 | 2975 | +11.2% | +90.7989 to +507.1279 | yes: LOSS |
| time over the response line (% of samples) | 23.42 | 23.22 | −0.8% | −1.0224 to +0.6380 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.6 | +5.5% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 97.8 | +97.800 (native is 0) | +22.2269 to +173.3731 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 12.99 | +13.0% | −3.0214 to +6.0081 | no |
| utilisation (used / allocatable) | 0.06614 | 0.07403 | +11.9% | −0.0015 to +0.0173 | no |
| CPU used (cores), mean | 1.587 | 1.591 | +0.2% | −0.0195 to +0.0267 | no |
| Omni's own CPU (cores), mean | 0 | 0.07482 | +0.075 (native is 0) | +0.0684 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.587 | 1.666 | +4.9% | +0.0501 to +0.1067 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.6 | 387.6 | −8.1% | −71.7676 to +3.6516 | no |
| HPA replicas, mean | 2.01 | 2.528 | +25.8% | +0.2715 to +0.7652 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.5791 to +2.8209 | yes: power given |
| pod start wait, total (s) | 0 | 3.8 | +3.800 (native is 0) | +1.2811 to +6.3189 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.567 | +1.567 (native is 0) | +0.6844 to +2.4489 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.9 | 48.25 | +7.5% | +2.8770 to +3.8194 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 829.8 | 843.2 | +1.6% | +3.8733 to +22.9267 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.021 | −16.3% | −1.9987 to +0.0408 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.3 | +323.5% | −0.0947 to +0.5530 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1 | +42.9% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 134 | 147 | +9.7% | +3.0448 to +22.9552 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.42 | −9.7% | −1.2692 to +0.1099 | no |
| node-hours | 2.514 | 2.268 | −9.8% | −0.5306 to +0.0401 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.6 | −0.1% | −1.4965 to +0.7271 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 256.3 | −6.8% | −39.9732 to +2.6913 | no |
| response time (ms), mean | 569.8 | 485.1 | −14.9% | −130.7755 to −38.6123 | yes: GAIN |
| response time (ms), 95th percentile | 2605 | 2123 | −18.5% | −792.8653 to −169.9117 | yes: GAIN |
| response time (ms), 99th percentile | 3591 | 2975 | −17.2% | −1036.8996 to −195.1640 | yes: GAIN |
| time over the response line (% of samples) | 19.85 | 23.22 | +17.0% | +1.7996 to +4.9393 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 11.6 | −1.7% | −1.0793 to +0.6793 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 97.8 | +97.800 (native is 0) | +22.2269 to +173.3731 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 31.17 | 12.99 | −58.3% | −26.2203 to −10.1430 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06687 | 0.07403 | +10.7% | −0.0026 to +0.0169 | no |
| CPU used (cores), mean | 1.605 | 1.591 | −0.9% | −0.0345 to +0.0069 | no |
| Omni's own CPU (cores), mean | 0 | 0.07482 | +0.075 (native is 0) | +0.0684 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 1.666 | +3.8% | +0.0364 to +0.0856 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.7 | 387.6 | −7.4% | −71.2443 to +8.9585 | no |
| HPA replicas, mean | 2.025 | 2.528 | +24.9% | +0.2067 to +0.8009 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.5791 to +2.8209 | yes: power given |
| pod start wait, total (s) | 0 | 3.8 | +3.800 (native is 0) | +1.2811 to +6.3189 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.567 | +1.567 (native is 0) | +0.6844 to +2.4489 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.33 | 48.25 | −0.2% | −0.8457 to +0.6763 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 887 | 843.2 | −4.9% | −65.4512 to −22.1488 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.021 | −16.3% | −1.9987 to +0.0408 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.062 | 0.3 | −71.8% | −0.9930 to −0.5320 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 1 | −63.0% | −2.7144 to −0.6856 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 185.4 | 147 | −20.7% | −57.4705 to −19.2962 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.291 | −11.8% | −1.3916 to −0.0273 | yes: GAIN |
| node-hours | 2.514 | 2.217 | −11.8% | −0.5821 to −0.0104 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 275.1 | +0.2% | −0.5455 to +1.6421 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 252.8 | −7.9% | −43.5213 to +0.0303 | no |
| response time (ms), mean | 485.6 | 553.1 | +13.9% | +12.9274 to +122.0306 | yes: LOSS |
| response time (ms), 95th percentile | 1860 | 2715 | +46.0% | +416.4920 to +1293.9060 | yes: LOSS |
| response time (ms), 99th percentile | 2676 | 3555 | +32.9% | +391.1221 to +1368.0235 | yes: LOSS |
| time over the response line (% of samples) | 23.42 | 20.26 | −13.5% | −5.3105 to −1.0100 | yes: GAIN |
| failed requests (%) | 0 | 0.01156 | +0.012 (native is 0) | −0.0146 to +0.0377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 12.1 | +10.0% | +0.3887 to +1.8113 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 76.5 | +76.500 (native is 0) | +23.4254 to +129.5746 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 37.91 | +229.7% | +11.3178 to +41.5156 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06614 | 0.07644 | +15.6% | +0.0018 to +0.0187 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.587 | 1.607 | +1.2% | −0.0214 to +0.0608 | no |
| Omni's own CPU (cores), mean | 0 | 0.08365 | +0.084 (native is 0) | +0.0760 to +0.0913 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.587 | 1.691 | +6.5% | +0.0572 to +0.1495 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.6 | 378.3 | −10.3% | −77.9438 to −8.6650 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.01 | 2.375 | +18.1% | +0.1096 to +0.6197 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.3690 to +2.6310 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | +0.7971 to +6.2029 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.167 | +1.167 (native is 0) | +0.2657 to +2.0676 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.9 | 51.82 | +15.4% | +5.7465 to +8.0973 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 829.8 | 903.6 | +8.9% | +38.8144 to +108.7856 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.658 | −22.4% | −2.3501 to −0.3346 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1.483 | +1994.1% | +0.9723 to +1.8527 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 5.1 | +628.6% | +2.3434 to +6.4566 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 134 | 199 | +48.5% | +34.0170 to +95.9996 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*