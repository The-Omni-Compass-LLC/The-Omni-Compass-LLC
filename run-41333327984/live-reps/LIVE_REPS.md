# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.39 | 5.367 |
| node-hours | 2.513 | 2.517 | 2.259 | 2.248 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.8 | 274.4 | 274.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 274.8 | 255.3 | 254.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 499.7 | 494.8 | 506.7 | 509.6 |
| response time (ms), 95th percentile | 2019 | 2044 | 2001 | 2112 |
| response time (ms), 99th percentile | 2822 | 2945 | 2831 | 2977 |
| time over the response line (% of samples) | 21.52 | 20.09 | 21.72 | 20 |
| failed requests (%) | 0.01149 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.7 | 11.4 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 11.2 | 9.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.37 | 19.69 | 18.95 | 24.37 |
| utilisation (used / allocatable) | 0.06727 | 0.06652 | 0.07462 | 0.07319 |
| CPU used (cores), mean | 1.614 | 1.597 | 1.589 | 1.572 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01252 | 0.01353 |
| CPU used with Omni's own (cores), mean | 1.614 | 1.597 | 1.602 | 1.586 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.5 | 421.5 | 386.4 | 392.5 |
| HPA replicas, mean | 2.048 | 2.075 | 2.252 | 2.165 |
| pods started | 0 | 0.3 | 0.6 | 0.2 |
| pod start wait, total (s) | 0 | 0.6 | 0.6 | 0.5 |
| pod start wait, mean (s) | 0 | 0.6 | 0.45 | 0.5 |
| host CPU busy, the real machine under kind (%) | 45.94 | 46.51 | 46.63 | 47.33 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 844.5 | 848.6 | 847.5 | 854.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.015 | 4.847 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.425 | 0.6958 | 0.475 | 0.525 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.7 | 3.9 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 149.7 | 157 | 153.5 | 160.2 |
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
| worker nodes in service, mean | 6 | 5.367 | −10.5% | −1.3083 to +0.0432 | no |
| node-hours | 2.517 | 2.248 | −10.7% | −0.5470 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.2 | −0.2% | −1.4542 to +0.2711 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 254.3 | −7.5% | −41.5833 to +0.6252 | no |
| response time (ms), mean | 494.8 | 509.6 | +3.0% | −3.9625 to +33.5820 | no |
| response time (ms), 95th percentile | 2044 | 2112 | +3.3% | −42.4926 to +177.6486 | no |
| response time (ms), 99th percentile | 2945 | 2977 | +1.1% | −105.9930 to +170.5044 | no |
| time over the response line (% of samples) | 20.09 | 20 | −0.5% | −1.0209 to +0.8266 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.6 | −0.9% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.7 | +9.700 (native is 0) | +7.7615 to +11.6385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.69 | 24.37 | +23.7% | +0.1216 to +9.2284 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06652 | 0.07319 | +10.0% | −0.0002 to +0.0135 | no |
| CPU used (cores), mean | 1.597 | 1.572 | −1.5% | −0.0701 to +0.0217 | no |
| Omni's own CPU (cores), mean | 0 | 0.01353 | +0.014 (native is 0) | +0.0120 to +0.0150 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.597 | 1.586 | −0.7% | −0.0578 to +0.0364 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.5 | 392.5 | −6.9% | −59.9539 to +1.8243 | no |
| HPA replicas, mean | 2.075 | 2.165 | +4.4% | −0.0962 to +0.2772 | no |
| pods started | 0.3 | 0.2 | −33.3% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.6 | 0.5 | −16.7% | −1.1900 to +0.9900 | no |
| pod start wait, mean (s) | 0.6 | 0.5 | −16.7% | −1.1900 to +0.9900 | no |
| host CPU busy, the real machine under kind (%) | 46.51 | 47.33 | +1.8% | +0.3281 to +1.3028 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 848.6 | 854.4 | +0.7% | +2.1714 to +9.4286 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.847 | −19.2% | −2.3028 to −0.0022 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.525 | −24.6% | −0.8222 to +0.4806 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 2.1 | +23.5% | −0.1001 to +0.9001 | no |
| queue: job turnaround, submitted to done, mean (s) | 157 | 160.2 | +2.0% | −2.0928 to +8.5178 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.517 | +0.2% | −0.0021 to +0.0104 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.8 | +0.1% | −0.7577 to +1.2132 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 274.8 | +0.1% | −0.7577 to +1.2132 | no |
| response time (ms), mean | 499.7 | 494.8 | −1.0% | −24.0504 to +14.1721 | no |
| response time (ms), 95th percentile | 2019 | 2044 | +1.2% | −90.6946 to +140.5596 | no |
| response time (ms), 99th percentile | 2822 | 2945 | +4.4% | −43.5495 to +290.0807 | no |
| time over the response line (% of samples) | 21.52 | 20.09 | −6.6% | −2.5030 to −0.3476 | yes: GAIN |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.7 | −1.8% | −1.0121 to +0.6121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.37 | 19.69 | +7.2% | −1.8806 to +4.5206 | no |
| utilisation (used / allocatable) | 0.06727 | 0.06652 | −1.1% | −0.0019 to +0.0004 | no |
| CPU used (cores), mean | 1.614 | 1.597 | −1.1% | −0.0452 to +0.0094 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.614 | 1.597 | −1.1% | −0.0452 to +0.0094 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.5 | 421.5 | +1.7% | −2.6107 to +16.5840 | no |
| HPA replicas, mean | 2.048 | 2.075 | +1.3% | −0.0944 to +0.1475 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| host CPU busy, the real machine under kind (%) | 45.94 | 46.51 | +1.3% | +0.1740 to +0.9748 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 844.5 | 848.6 | +0.5% | −2.4944 to +10.6944 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.425 | 0.6958 | +63.7% | −0.5075 to +1.0492 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.7 | +41.7% | −1.7431 to +2.7431 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.7 | 157 | +4.8% | −0.0352 to +14.5352 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.39 | −10.2% | −1.3670 to +0.1473 | no |
| node-hours | 2.513 | 2.259 | −10.1% | −0.5715 to +0.0633 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.4 | −0.1% | −1.0552 to +0.7029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 255.3 | −7.0% | −43.4984 to +4.9087 | no |
| response time (ms), mean | 499.7 | 506.7 | +1.4% | −17.7606 to +31.7023 | no |
| response time (ms), 95th percentile | 2019 | 2001 | −0.9% | −97.0301 to +60.0911 | no |
| response time (ms), 99th percentile | 2822 | 2831 | +0.3% | −175.4750 to +193.3690 | no |
| time over the response line (% of samples) | 21.52 | 21.72 | +0.9% | −0.4416 to +0.8368 | no |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.4 | +4.6% | −0.2726 to +1.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.2 | +11.200 (native is 0) | +10.6358 to +11.7642 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.37 | 18.95 | +3.2% | −3.0800 to +4.2433 | no |
| utilisation (used / allocatable) | 0.06727 | 0.07462 | +10.9% | −0.0022 to +0.0169 | no |
| CPU used (cores), mean | 1.614 | 1.589 | −1.5% | −0.0604 to +0.0104 | no |
| Omni's own CPU (cores), mean | 0 | 0.01252 | +0.013 (native is 0) | +0.0113 to +0.0138 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.614 | 1.602 | −0.8% | −0.0490 to +0.0240 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.5 | 386.4 | −6.8% | −63.5978 to +7.2211 | no |
| HPA replicas, mean | 2.048 | 2.252 | +9.9% | −0.0369 to +0.4436 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | +0.0218 to +0.8782 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.94 | 46.63 | +1.5% | +0.1866 to +1.1823 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 844.5 | 847.5 | +0.4% | −3.3712 to +9.3712 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.015 | −16.4% | −2.1492 to +0.1785 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.425 | 0.475 | +11.8% | −0.6965 to +0.7965 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 3.9 | +225.0% | −3.0626 to +8.4626 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.7 | 153.5 | +2.5% | −2.9761 to +10.5845 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.39 | −10.2% | −1.3670 to +0.1473 | no |
| node-hours | 2.517 | 2.259 | −10.3% | −0.5724 to +0.0559 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.4 | −0.1% | −1.4241 to +0.6164 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 255.3 | −7.1% | −42.9902 to +3.9450 | no |
| response time (ms), mean | 494.8 | 506.7 | +2.4% | −0.0589 to +23.8789 | no |
| response time (ms), 95th percentile | 2044 | 2001 | −2.1% | −129.2768 to +42.4728 | no |
| response time (ms), 99th percentile | 2945 | 2831 | −3.9% | −339.0104 to +110.3732 | no |
| time over the response line (% of samples) | 20.09 | 21.72 | +8.1% | +0.6879 to +2.5578 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11.4 | +6.5% | −0.4209 to +1.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.2 | +11.200 (native is 0) | +10.6358 to +11.7642 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.69 | 18.95 | −3.7% | −2.4232 to +0.9466 | no |
| utilisation (used / allocatable) | 0.06652 | 0.07462 | +12.2% | −0.0025 to +0.0187 | no |
| CPU used (cores), mean | 1.597 | 1.589 | −0.4% | −0.0236 to +0.0093 | no |
| Omni's own CPU (cores), mean | 0 | 0.01252 | +0.013 (native is 0) | +0.0113 to +0.0138 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.597 | 1.602 | +0.3% | −0.0118 to +0.0225 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.5 | 386.4 | −8.3% | −79.6373 to +9.2873 | no |
| HPA replicas, mean | 2.075 | 2.252 | +8.5% | +0.0018 to +0.3517 | yes: power given |
| pods started | 0.3 | 0.6 | +100.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.6 | 0.6 | ±0.0% | −0.9537 to +0.9537 | no |
| pod start wait, mean (s) | 0.6 | 0.45 | −25.0% | −0.9768 to +0.6768 | no |
| host CPU busy, the real machine under kind (%) | 46.51 | 46.63 | +0.2% | −0.2520 to +0.4722 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 848.6 | 847.5 | −0.1% | −6.9933 to +4.7933 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.015 | −16.4% | −2.1492 to +0.1785 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.475 | −31.7% | −0.6237 to +0.1820 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 3.9 | +129.4% | −3.9975 to +8.3975 | no |
| queue: job turnaround, submitted to done, mean (s) | 157 | 153.5 | −2.2% | −7.6047 to +0.7131 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.367 | −10.5% | −1.3083 to +0.0432 | no |
| node-hours | 2.513 | 2.248 | −10.5% | −0.5458 to +0.0158 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.2 | −0.1% | −1.2001 to +0.4724 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 254.3 | −7.4% | −42.0591 to +1.5564 | no |
| response time (ms), mean | 499.7 | 509.6 | +2.0% | −8.1857 to +27.9269 | no |
| response time (ms), 95th percentile | 2019 | 2112 | +4.6% | −31.4551 to +216.4761 | no |
| response time (ms), 99th percentile | 2822 | 2977 | +5.5% | −54.9082 to +365.9508 | no |
| time over the response line (% of samples) | 21.52 | 20 | −7.1% | −2.4852 to −0.5598 | yes: GAIN |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.6 | −2.8% | −1.0578 to +0.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.7 | +9.700 (native is 0) | +7.7615 to +11.6385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.37 | 24.37 | +32.6% | −0.6972 to +12.6872 | no |
| utilisation (used / allocatable) | 0.06727 | 0.07319 | +8.8% | +0.0000 to +0.0118 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.614 | 1.572 | −2.6% | −0.1046 to +0.0204 | no |
| Omni's own CPU (cores), mean | 0 | 0.01353 | +0.014 (native is 0) | +0.0120 to +0.0150 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.614 | 1.586 | −1.8% | −0.0924 to +0.0353 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.5 | 392.5 | −5.3% | −44.0128 to −0.1435 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.048 | 2.165 | +5.7% | −0.1163 to +0.3505 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 45.94 | 47.33 | +3.0% | +0.8980 to +1.8816 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 844.5 | 854.4 | +1.2% | +0.8806 to +18.9194 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.847 | −19.2% | −2.3028 to −0.0022 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.425 | 0.525 | +23.5% | −0.1205 to +0.3205 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2.1 | +75.0% | −1.7217 to +3.5217 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.7 | 160.2 | +7.0% | +1.2024 to +19.7226 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*