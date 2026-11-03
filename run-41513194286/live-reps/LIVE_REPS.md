# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.557 | 5.565 |
| node-hours | 2.516 | 2.514 | 2.328 | 2.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 275.8 | 275.9 | 276.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 275.8 | 262 | 262.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 554.1 | 456.5 | 537.9 | 478.2 |
| response time (ms), 95th percentile | 2114 | 1927 | 2301 | 2330 |
| response time (ms), 99th percentile | 3029 | 3160 | 3315 | 3532 |
| time over the response line (% of samples) | 27.26 | 19.84 | 26.84 | 20.54 |
| failed requests (%) | 0 | 0 | 0 | 0.01058 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 11.9 | 13.3 | 12.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 66.3 | 62 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.18 | 20.03 | 15.93 | 25.61 |
| utilisation (used / allocatable) | 0.06872 | 0.06941 | 0.0747 | 0.0756 |
| CPU used (cores), mean | 1.649 | 1.666 | 1.662 | 1.681 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07918 | 0.08181 |
| CPU used with Omni's own (cores), mean | 1.649 | 1.666 | 1.742 | 1.763 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.8 | 400.3 | 378.3 | 373.7 |
| HPA replicas, mean | 2.049 | 2.056 | 2.404 | 2.318 |
| pods started | 0 | 0 | 1.6 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 4.2 | 1.2 |
| pod start wait, mean (s) | 0 | 0 | 2.033 | 0.6 |
| host CPU busy, the real machine under kind (%) | 47.09 | 48.33 | 50.41 | 51.78 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 852.2 | 869.9 | 863.1 | 885.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.126 | 5.086 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.9042 | 0.2042 | 1.054 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 2.2 | 1.6 | 3.4 |
| queue: job turnaround, submitted to done, mean (s) | 155.7 | 182.5 | 167 | 197.5 |
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
| worker nodes in service, mean | 6 | 5.565 | −7.2% | −0.9208 to +0.0513 | no |
| node-hours | 2.514 | 2.334 | −7.2% | −0.3805 to +0.0206 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 276.2 | +0.2% | −0.6393 to +1.5193 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 262.6 | −4.8% | −28.2043 to +1.7426 | no |
| response time (ms), mean | 456.5 | 478.2 | +4.7% | −17.9874 to +61.2250 | no |
| response time (ms), 95th percentile | 1927 | 2330 | +20.9% | +94.2529 to +711.8051 | yes: LOSS |
| response time (ms), 99th percentile | 3160 | 3532 | +11.7% | +159.1403 to +583.5073 | yes: LOSS |
| time over the response line (% of samples) | 19.84 | 20.54 | +3.5% | −0.9459 to +2.3344 | no |
| failed requests (%) | 0 | 0.01058 | +0.011 (native is 0) | −0.0134 to +0.0345 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12.5 | +5.0% | −0.3656 to +1.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62 | +62.000 (native is 0) | +28.9442 to +95.0558 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.03 | 25.61 | +27.8% | +2.4516 to +8.7051 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06941 | 0.0756 | +8.9% | +0.0002 to +0.0121 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.666 | 1.681 | +0.9% | −0.0022 to +0.0325 | no |
| Omni's own CPU (cores), mean | 0 | 0.08181 | +0.082 (native is 0) | +0.0772 to +0.0864 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.666 | 1.763 | +5.8% | +0.0790 to +0.1149 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.3 | 373.7 | −6.6% | −53.7361 to +0.6004 | no |
| HPA replicas, mean | 2.056 | 2.318 | +12.7% | +0.0849 to +0.4385 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.3379 to +2.7379 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| host CPU busy, the real machine under kind (%) | 48.33 | 51.78 | +7.2% | +3.0148 to +3.8991 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 869.9 | 885.2 | +1.8% | +6.3021 to +24.2979 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.086 | −15.2% | −1.8632 to +0.0357 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9042 | 1.054 | +16.6% | −0.0483 to +0.3483 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.2 | 3.4 | +54.5% | −0.2621 to +2.6621 | no |
| queue: job turnaround, submitted to done, mean (s) | 182.5 | 197.5 | +8.2% | +6.2614 to +23.7302 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0131 to +0.0088 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 275.8 | +0.0% | −1.1881 to +1.2297 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 275.8 | +0.0% | −1.1881 to +1.2297 | no |
| response time (ms), mean | 554.1 | 456.5 | −17.6% | −136.2617 to −58.8193 | yes: GAIN |
| response time (ms), 95th percentile | 2114 | 1927 | −8.8% | −427.2567 to +53.2617 | no |
| response time (ms), 99th percentile | 3029 | 3160 | +4.3% | −77.3228 to +340.8032 | no |
| time over the response line (% of samples) | 27.26 | 19.84 | −27.2% | −9.9782 to −4.8512 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 11.9 | −6.3% | −1.7417 to +0.1417 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.18 | 20.03 | +41.2% | +1.4902 to +10.2098 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06872 | 0.06941 | +1.0% | −0.0001 to +0.0015 | no |
| CPU used (cores), mean | 1.649 | 1.666 | +1.0% | −0.0033 to +0.0366 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.649 | 1.666 | +1.0% | −0.0033 to +0.0366 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.8 | 400.3 | −0.9% | −7.4408 to +0.4414 | no |
| HPA replicas, mean | 2.049 | 2.056 | +0.4% | −0.1206 to +0.1361 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 47.09 | 48.33 | +2.6% | +0.8906 to +1.5725 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 852.2 | 869.9 | +2.1% | +8.9066 to +26.4934 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.9042 | +471.1% | +0.4144 to +1.0773 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 2.2 | +214.3% | −0.1605 to +3.1605 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.7 | 182.5 | +17.2% | +16.3035 to +37.1798 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.557 | −7.4% | −0.9042 to +0.0184 | no |
| node-hours | 2.516 | 2.328 | −7.4% | −0.3790 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 275.9 | +0.1% | −0.8050 to +1.0875 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 262 | −5.0% | −28.3081 to +0.7322 | no |
| response time (ms), mean | 554.1 | 537.9 | −2.9% | −31.7122 to −0.7358 | yes: GAIN |
| response time (ms), 95th percentile | 2114 | 2301 | +8.8% | +74.9432 to +298.9618 | yes: LOSS |
| response time (ms), 99th percentile | 3029 | 3315 | +9.4% | −0.4944 to +572.6480 | no |
| time over the response line (% of samples) | 27.26 | 26.84 | −1.5% | −1.1694 to +0.3443 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 13.3 | +4.7% | −0.1689 to +1.3689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.3 | +66.300 (native is 0) | +19.7726 to +112.8274 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.18 | 15.93 | +12.3% | −0.7883 to +4.2750 | no |
| utilisation (used / allocatable) | 0.06872 | 0.0747 | +8.7% | +0.0013 to +0.0107 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.649 | 1.662 | +0.8% | −0.0101 to +0.0364 | no |
| Omni's own CPU (cores), mean | 0 | 0.07918 | +0.079 (native is 0) | +0.0756 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.649 | 1.742 | +5.6% | +0.0699 to +0.1148 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.8 | 378.3 | −6.3% | −47.1770 to −3.7774 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.049 | 2.404 | +17.4% | +0.2252 to +0.4858 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.8311 to +2.3689 | yes: power given |
| pod start wait, total (s) | 0 | 4.2 | +4.200 (native is 0) | +1.8204 to +6.5796 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.033 | +2.033 (native is 0) | +1.1982 to +2.8684 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.09 | 50.41 | +7.0% | +2.9375 to +3.6951 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 852.2 | 863.1 | +1.3% | +3.4552 to +18.3448 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.126 | −14.6% | −1.6914 to −0.0574 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.2042 | +28.9% | −0.2534 to +0.3450 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.6 | +128.6% | −0.7329 to +2.5329 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.7 | 167 | +7.2% | +4.3718 to +18.0866 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.557 | −7.4% | −0.9042 to +0.0184 | no |
| node-hours | 2.514 | 2.328 | −7.4% | −0.3746 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 275.9 | +0.0% | −0.7329 to +0.9738 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 262 | −5.0% | −27.9876 to +0.3702 | no |
| response time (ms), mean | 456.5 | 537.9 | +17.8% | +40.4918 to +122.1412 | yes: LOSS |
| response time (ms), 95th percentile | 1927 | 2301 | +19.4% | +135.7887 to +612.1113 | yes: LOSS |
| response time (ms), 99th percentile | 3160 | 3315 | +4.9% | −22.1271 to +330.8003 | no |
| time over the response line (% of samples) | 19.84 | 26.84 | +35.3% | +4.7514 to +9.2530 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 13.3 | +11.8% | −0.1888 to +2.9888 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.3 | +66.300 (native is 0) | +19.7726 to +112.8274 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.03 | 15.93 | −20.5% | −6.6957 to −1.5177 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06941 | 0.0747 | +7.6% | +0.0003 to +0.0102 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.666 | 1.662 | −0.2% | −0.0264 to +0.0194 | no |
| Omni's own CPU (cores), mean | 0 | 0.07918 | +0.079 (native is 0) | +0.0756 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.666 | 1.742 | +4.5% | +0.0531 to +0.0983 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.3 | 378.3 | −5.5% | −44.2052 to +0.2503 | no |
| HPA replicas, mean | 2.056 | 2.404 | +16.9% | +0.1557 to +0.5398 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.8311 to +2.3689 | yes: power given |
| pod start wait, total (s) | 0 | 4.2 | +4.200 (native is 0) | +1.8204 to +6.5796 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.033 | +2.033 (native is 0) | +1.1982 to +2.8684 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.33 | 50.41 | +4.3% | +1.8748 to +2.2947 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 869.9 | 863.1 | −0.8% | −10.9408 to −2.6592 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.126 | −14.6% | −1.6914 to −0.0574 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9042 | 0.2042 | −77.4% | −0.8459 to −0.5541 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.2 | 1.6 | −27.3% | −1.2032 to +0.0032 | no |
| queue: job turnaround, submitted to done, mean (s) | 182.5 | 167 | −8.5% | −21.5895 to −9.4355 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.565 | −7.2% | −0.9208 to +0.0513 | no |
| node-hours | 2.516 | 2.334 | −7.2% | −0.3864 to +0.0222 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 276.2 | +0.2% | −0.2002 to +1.1218 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 262.6 | −4.8% | −28.6235 to +2.2034 | no |
| response time (ms), mean | 554.1 | 478.2 | −13.7% | −101.9741 to −49.8692 | yes: GAIN |
| response time (ms), 95th percentile | 2114 | 2330 | +10.2% | +20.8629 to +411.2001 | yes: LOSS |
| response time (ms), 99th percentile | 3029 | 3532 | +16.6% | +228.3453 to +777.7827 | yes: LOSS |
| time over the response line (% of samples) | 27.26 | 20.54 | −24.7% | −9.2405 to −4.2005 | yes: GAIN |
| failed requests (%) | 0 | 0.01058 | +0.011 (native is 0) | −0.0134 to +0.0345 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 12.5 | −1.6% | −1.3081 to +0.9081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62 | +62.000 (native is 0) | +28.9442 to +95.0558 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.18 | 25.61 | +80.6% | +7.1136 to +15.7431 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06872 | 0.0756 | +10.0% | +0.0010 to +0.0128 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.649 | 1.681 | +1.9% | +0.0176 to +0.0460 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.08181 | +0.082 (native is 0) | +0.0772 to +0.0864 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.649 | 1.763 | +6.9% | +0.0986 to +0.1286 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.8 | 373.7 | −7.4% | −57.3805 to −2.7546 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.049 | 2.318 | +13.2% | +0.0116 to +0.5274 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | −0.3379 to +2.7379 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| host CPU busy, the real machine under kind (%) | 47.09 | 51.78 | +10.0% | +4.2261 to +5.1509 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 852.2 | 885.2 | +3.9% | +20.2755 to +45.7245 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.086 | −15.2% | −1.8632 to +0.0357 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 1.054 | +565.8% | +0.5211 to +1.2705 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 3.4 | +385.7% | +0.1981 to +5.2019 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 155.7 | 197.5 | +26.8% | +24.9934 to +58.4816 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*