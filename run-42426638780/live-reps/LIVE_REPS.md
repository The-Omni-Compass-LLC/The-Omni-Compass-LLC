# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.516 | 1.515 | 1.515 | 1.514 | 1.514 | 1.514 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.9 | 157.7 | 157.9 | 157.6 | 157.7 | 157.6 | 157.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.9 | 157.7 | 157.9 | 157.6 | 157.7 | 157.6 | 157.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 124.3 | 68.36 | 67 | 67.39 | 66.92 | 67.89 | 67.38 | 67.97 |
| response time (ms), 95th percentile | 278.9 | 98.64 | 96.34 | 97.27 | 96.5 | 98.07 | 97.33 | 99.43 |
| response time (ms), 99th percentile | 430.8 | 137.3 | 127.7 | 123.4 | 128.1 | 128.9 | 125.3 | 129.1 |
| time over the response line (% of samples) | 1.312 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | 15.7 | 18 | 14.4 | 14.9 | 17.5 | 17.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | nan | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.16 | 0.24 | 0.2117 | 0.07667 | 0.1033 | 0.2417 | 0.2083 |
| utilisation (used / allocatable) | 0.0333 | 0.03245 | 0.03203 | 0.03247 | 0.03192 | 0.03228 | 0.03211 | 0.03255 |
| CPU used (cores), mean | 0.7992 | 0.7788 | 0.7688 | 0.7792 | 0.766 | 0.7746 | 0.7706 | 0.7812 |
| Omni's own CPU (cores), mean | 0 | 0.03344 | 0.00568 | 0.0064 | 0.00682 | 0.01286 | 0.023 | 0.06291 |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.8122 | 0.7745 | 0.7856 | 0.7728 | 0.7875 | 0.7936 | 0.8441 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 863.5 | 867.1 | 855.6 | 881.2 | 867.9 | 869.9 | 859.7 |
| HPA replicas, mean | 7.942 | 8.117 | 7.729 | 7.909 | 6.607 | 6.73 | 8.059 | 7.706 |
| pods started | 5 | 4.8 | 5 | 4.7 | 3.3 | 3.2 | 4.2 | 3.7 |
| pod start wait, total (s) | 6.4 | 6.3 | 6.6 | 5.7 | 4.3 | 4.3 | 6.4 | 4.4 |
| pod start wait, mean (s) | 1.28 | 1.353 | 1.347 | 1.264 | 1.353 | 1.357 | 1.477 | 1.21 |
| host CPU busy, the real machine under kind (%) | 24.7 | 25.31 | 24.2 | 24.48 | 24.05 | 24.53 | 24.66 | 26.25 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan | nan | nan | nan |

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
| node-hours | 1.515 | 1.516 | +0.1% | −0.0002 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.9 | −0.1% | −0.3683 to +0.1334 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.9 | −0.1% | −0.3683 to +0.1334 | no |
| response time (ms), mean | 124.3 | 68.36 | −45.0% | −81.3001 to −30.5412 | yes: GAIN |
| response time (ms), 95th percentile | 278.9 | 98.64 | −64.6% | −250.2519 to −110.1841 | yes: GAIN |
| response time (ms), 99th percentile | 430.8 | 137.3 | −68.1% | −405.0144 to −182.0296 | yes: GAIN |
| time over the response line (% of samples) | 1.312 | 0 | −100.0% | −2.7099 to +0.0850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8834 to +0.2834 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.700 (native is 0) | +17.0463 to +20.3537 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.16 | −25.0% | −0.3768 to +0.2701 | no |
| utilisation (used / allocatable) | 0.0333 | 0.03245 | −2.6% | −0.0018 to +0.0001 | no |
| CPU used (cores), mean | 0.7992 | 0.7788 | −2.6% | −0.0425 to +0.0015 | no |
| Omni's own CPU (cores), mean | 0 | 0.03344 | +0.033 (native is 0) | +0.0281 to +0.0387 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.8122 | +1.6% | −0.0054 to +0.0313 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 863.5 | +1.5% | −5.0300 to +29.9737 | no |
| HPA replicas, mean | 7.942 | 8.117 | +2.2% | −0.0624 to +0.4133 | no |
| pods started | 5 | 4.8 | −4.0% | −1.3583 to +0.9583 | no |
| pod start wait, total (s) | 6.4 | 6.3 | −1.6% | −2.1077 to +1.9077 | no |
| pod start wait, mean (s) | 1.28 | 1.353 | +5.7% | −0.3088 to +0.4555 | no |
| host CPU busy, the real machine under kind (%) | 24.7 | 25.31 | +2.5% | +0.1169 to +1.0985 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | −0.0% | −0.0010 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.7 | −0.2% | −0.6475 to +0.0176 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.7 | −0.2% | −0.6475 to +0.0176 | no |
| response time (ms), mean | 124.3 | 67 | −46.1% | −84.0349 to −30.5245 | yes: GAIN |
| response time (ms), 95th percentile | 278.9 | 96.34 | −65.5% | −253.7997 to −111.2273 | yes: GAIN |
| response time (ms), 99th percentile | 430.8 | 127.7 | −70.4% | −423.0614 to −183.0468 | yes: GAIN |
| time over the response line (% of samples) | 1.312 | 0 | −100.0% | −2.7099 to +0.0850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8834 to +0.2834 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.7 | +15.700 (native is 0) | +14.7433 to +16.6567 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.24 | +12.5% | −0.2827 to +0.3361 | no |
| utilisation (used / allocatable) | 0.0333 | 0.03203 | −3.8% | −0.0025 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.7992 | 0.7688 | −3.8% | −0.0598 to −0.0010 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00568 | +0.006 (native is 0) | +0.0048 to +0.0066 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.7745 | −3.1% | −0.0533 to +0.0039 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 867.1 | +1.9% | −4.7738 to +36.9936 | no |
| HPA replicas, mean | 7.942 | 7.729 | −2.7% | −0.4159 to −0.0091 | yes: GAIN |
| pods started | 5 | 5 | ±0.0% | −0.8921 to +0.8921 | no |
| pod start wait, total (s) | 6.4 | 6.6 | +3.1% | −1.1821 to +1.5821 | no |
| pod start wait, mean (s) | 1.28 | 1.347 | +5.2% | −0.0625 to +0.1958 | no |
| host CPU busy, the real machine under kind (%) | 24.7 | 24.2 | −2.1% | −1.1989 to +0.1836 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | ±0.0% | −0.0016 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.9 | −0.1% | −0.4518 to +0.0879 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.9 | −0.1% | −0.4518 to +0.0879 | no |
| response time (ms), mean | 124.3 | 67.39 | −45.8% | −83.7229 to −30.0543 | yes: GAIN |
| response time (ms), 95th percentile | 278.9 | 97.27 | −65.1% | −253.5355 to −109.6435 | yes: GAIN |
| response time (ms), 99th percentile | 430.8 | 123.4 | −71.3% | −432.8208 to −181.8474 | yes: GAIN |
| time over the response line (% of samples) | 1.312 | 0 | −100.0% | −2.7099 to +0.0850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8834 to +0.2834 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +16.2806 to +19.7194 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2117 | −0.8% | −0.2232 to +0.2199 | no |
| utilisation (used / allocatable) | 0.0333 | 0.03247 | −2.5% | −0.0020 to +0.0003 | no |
| CPU used (cores), mean | 0.7992 | 0.7792 | −2.5% | −0.0482 to +0.0082 | no |
| Omni's own CPU (cores), mean | 0 | 0.0064 | +0.006 (native is 0) | +0.0055 to +0.0073 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.7856 | −1.7% | −0.0411 to +0.0139 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 855.6 | +0.5% | −21.9567 to +31.2001 | no |
| HPA replicas, mean | 7.942 | 7.909 | −0.4% | −0.3695 to +0.3044 | no |
| pods started | 5 | 4.7 | −6.0% | −1.5639 to +0.9639 | no |
| pod start wait, total (s) | 6.4 | 5.7 | −10.9% | −3.0129 to +1.6129 | no |
| pod start wait, mean (s) | 1.28 | 1.264 | −1.2% | −0.4072 to +0.3758 | no |
| host CPU busy, the real machine under kind (%) | 24.7 | 24.48 | −0.9% | −0.9900 to +0.5425 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0030 to +0.0000 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.6 | −0.3% | −0.7726 to −0.0975 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.6 | −0.3% | −0.7726 to −0.0975 | yes: GAIN |
| response time (ms), mean | 124.3 | 66.92 | −46.2% | −83.5264 to −31.1959 | yes: GAIN |
| response time (ms), 95th percentile | 278.9 | 96.5 | −65.4% | −252.8402 to −111.8798 | yes: GAIN |
| response time (ms), 99th percentile | 430.8 | 128.1 | −70.3% | −419.9700 to −185.3082 | yes: GAIN |
| time over the response line (% of samples) | 1.312 | 0 | −100.0% | −2.7099 to +0.0850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8834 to +0.2834 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.4 | +14.400 (native is 0) | +10.7031 to +18.0969 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.07667 | −64.1% | −0.3650 to +0.0917 | no |
| utilisation (used / allocatable) | 0.0333 | 0.03192 | −4.2% | −0.0023 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.7992 | 0.766 | −4.2% | −0.0546 to −0.0119 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00682 | +0.007 (native is 0) | +0.0054 to +0.0082 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.7728 | −3.3% | −0.0469 to −0.0060 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 881.2 | +3.5% | +6.7004 to +53.6997 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.942 | 6.607 | −16.8% | −1.8588 to −0.8101 | yes: GAIN |
| pods started | 5 | 3.3 | −34.0% | −2.5953 to −0.8047 | yes: GAIN |
| pod start wait, total (s) | 6.4 | 4.3 | −32.8% | −3.4254 to −0.7746 | yes: GAIN |
| pod start wait, mean (s) | 1.28 | 1.353 | +5.7% | −0.1408 to +0.2874 | no |
| host CPU busy, the real machine under kind (%) | 24.7 | 24.05 | −2.6% | −1.1789 to −0.1225 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0029 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.7 | −0.2% | −0.6572 to +0.0371 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.7 | −0.2% | −0.6572 to +0.0371 | no |
| response time (ms), mean | 124.3 | 67.89 | −45.4% | −82.5827 to −30.1930 | yes: GAIN |
| response time (ms), 95th percentile | 278.9 | 98.07 | −64.8% | −251.9833 to −109.5847 | yes: GAIN |
| response time (ms), 99th percentile | 430.8 | 128.9 | −70.1% | −421.9911 to −181.6929 | yes: GAIN |
| time over the response line (% of samples) | 1.312 | 0 | −100.0% | −2.7099 to +0.0850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8834 to +0.2834 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.9 | +14.900 (native is 0) | +10.9324 to +18.8676 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.1033 | −51.6% | −0.3466 to +0.1266 | no |
| utilisation (used / allocatable) | 0.0333 | 0.03228 | −3.1% | −0.0022 to +0.0001 | no |
| CPU used (cores), mean | 0.7992 | 0.7746 | −3.1% | −0.0522 to +0.0030 | no |
| Omni's own CPU (cores), mean | 0 | 0.01286 | +0.013 (native is 0) | +0.0104 to +0.0153 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.7875 | −1.5% | −0.0378 to +0.0143 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 867.9 | +2.0% | −6.3824 to +40.2332 | no |
| HPA replicas, mean | 7.942 | 6.73 | −15.3% | −1.7947 to −0.6282 | yes: GAIN |
| pods started | 5 | 3.2 | −36.0% | −2.9081 to −0.6919 | yes: GAIN |
| pod start wait, total (s) | 6.4 | 4.3 | −32.8% | −3.8986 to −0.3014 | yes: GAIN |
| pod start wait, mean (s) | 1.28 | 1.357 | +6.0% | −0.1620 to +0.3154 | no |
| host CPU busy, the real machine under kind (%) | 24.7 | 24.53 | −0.7% | −0.7662 to +0.4266 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0020 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.6 | −0.3% | −0.6716 to −0.1288 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.6 | −0.3% | −0.6716 to −0.1288 | yes: GAIN |
| response time (ms), mean | 124.3 | 67.38 | −45.8% | −82.9714 to −30.8297 | yes: GAIN |
| response time (ms), 95th percentile | 278.9 | 97.33 | −65.1% | −251.5018 to −111.5482 | yes: GAIN |
| response time (ms), 99th percentile | 430.8 | 125.3 | −70.9% | −428.5425 to −182.4271 | yes: GAIN |
| time over the response line (% of samples) | 1.312 | 0 | −100.0% | −2.7099 to +0.0850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8834 to +0.2834 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.500 (native is 0) | +16.3690 to +18.6310 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2417 | +13.3% | −0.3031 to +0.3598 | no |
| utilisation (used / allocatable) | 0.0333 | 0.03211 | −3.6% | −0.0023 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.7992 | 0.7706 | −3.6% | −0.0551 to −0.0022 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.023 | +0.023 (native is 0) | +0.0193 to +0.0267 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.7936 | −0.7% | −0.0293 to +0.0181 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 869.9 | +2.2% | −0.5084 to +38.3800 | no |
| HPA replicas, mean | 7.942 | 8.059 | +1.5% | −0.1723 to +0.4073 | no |
| pods started | 5 | 4.2 | −16.0% | −2.0526 to +0.4526 | no |
| pod start wait, total (s) | 6.4 | 6.4 | ±0.0% | −3.1452 to +3.1452 | no |
| pod start wait, mean (s) | 1.28 | 1.477 | +15.4% | −0.2130 to +0.6063 | no |
| host CPU busy, the real machine under kind (%) | 24.7 | 24.66 | −0.2% | −0.5431 to +0.4513 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | −0.0% | −0.0015 to +0.0011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 157.8 | −0.1% | −0.4292 to +0.0259 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 157.8 | −0.1% | −0.4292 to +0.0259 | no |
| response time (ms), mean | 124.3 | 67.97 | −45.3% | −81.7848 to −30.8490 | yes: GAIN |
| response time (ms), 95th percentile | 278.9 | 99.43 | −64.3% | −248.2919 to −110.5551 | yes: GAIN |
| response time (ms), 99th percentile | 430.8 | 129.1 | −70.0% | −415.0935 to −188.2811 | yes: GAIN |
| time over the response line (% of samples) | 1.312 | 0 | −100.0% | −2.7099 to +0.0850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.8834 to +0.2834 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.400 (native is 0) | +15.0834 to +19.7166 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2083 | −2.3% | −0.3028 to +0.2928 | no |
| utilisation (used / allocatable) | 0.0333 | 0.03255 | −2.3% | −0.0016 to +0.0001 | no |
| CPU used (cores), mean | 0.7992 | 0.7812 | −2.3% | −0.0373 to +0.0012 | no |
| Omni's own CPU (cores), mean | 0 | 0.06291 | +0.063 (native is 0) | +0.0525 to +0.0733 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7992 | 0.8441 | +5.6% | +0.0333 to +0.0564 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851 | 859.7 | +1.0% | −8.0326 to +25.5425 | no |
| HPA replicas, mean | 7.942 | 7.706 | −3.0% | −0.8536 to +0.3819 | no |
| pods started | 5 | 3.7 | −26.0% | −2.4705 to −0.1295 | yes: GAIN |
| pod start wait, total (s) | 6.4 | 4.4 | −31.2% | −3.8774 to −0.1226 | yes: GAIN |
| pod start wait, mean (s) | 1.28 | 1.21 | −5.5% | −0.3254 to +0.1854 | no |
| host CPU busy, the real machine under kind (%) | 24.7 | 26.25 | +6.2% | +1.3505 to +1.7325 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.515 | −0.1% | −0.0023 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.4297 to +0.0347 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.4297 to +0.0347 | no |
| response time (ms), mean | 68.36 | 67 | −2.0% | −3.0418 to +0.3236 | no |
| response time (ms), 95th percentile | 98.64 | 96.34 | −2.3% | −4.1498 to −0.4412 | yes: GAIN |
| response time (ms), 99th percentile | 137.3 | 127.7 | −6.9% | −23.2076 to +4.1434 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 15.7 | −16.0% | −4.9075 to −1.0925 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.24 | +50.0% | −0.1751 to +0.3351 | no |
| utilisation (used / allocatable) | 0.03245 | 0.03203 | −1.3% | −0.0011 to +0.0003 | no |
| CPU used (cores), mean | 0.7788 | 0.7688 | −1.3% | −0.0260 to +0.0061 | no |
| Omni's own CPU (cores), mean | 0.03344 | 0.00568 | −83.0% | −0.0322 to −0.0233 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8122 | 0.7745 | −4.6% | −0.0570 to −0.0184 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.5 | 867.1 | +0.4% | −10.3028 to +17.5788 | no |
| HPA replicas, mean | 8.117 | 7.729 | −4.8% | −0.6154 to −0.1606 | yes: GAIN |
| pods started | 4.8 | 5 | +4.2% | −1.0526 to +1.4526 | no |
| pod start wait, total (s) | 6.3 | 6.6 | +4.8% | −2.0374 to +2.6374 | no |
| pod start wait, mean (s) | 1.353 | 1.347 | −0.5% | −0.3986 to +0.3853 | no |
| host CPU busy, the real machine under kind (%) | 25.31 | 24.2 | −4.4% | −1.5312 to −0.6994 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.515 | −0.1% | −0.0023 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.9 | −0.0% | −0.2288 to +0.0998 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.9 | −0.0% | −0.2288 to +0.0998 | no |
| response time (ms), mean | 68.36 | 67.39 | −1.4% | −2.6651 to +0.7292 | no |
| response time (ms), 95th percentile | 98.64 | 97.27 | −1.4% | −3.4761 to +0.7331 | no |
| response time (ms), 99th percentile | 137.3 | 123.4 | −10.1% | −29.9957 to +2.3715 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 18 | −3.7% | −2.6385 to +1.2385 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2117 | +32.3% | −0.2300 to +0.3334 | no |
| utilisation (used / allocatable) | 0.03245 | 0.03247 | +0.1% | −0.0007 to +0.0007 | no |
| CPU used (cores), mean | 0.7788 | 0.7792 | +0.1% | −0.0170 to +0.0180 | no |
| Omni's own CPU (cores), mean | 0.03344 | 0.0064 | −80.9% | −0.0314 to −0.0226 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8122 | 0.7856 | −3.3% | −0.0464 to −0.0067 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.5 | 855.6 | −0.9% | −34.4624 to +18.7621 | no |
| HPA replicas, mean | 8.117 | 7.909 | −2.6% | −0.5264 to +0.1104 | no |
| pods started | 4.8 | 4.7 | −2.1% | −1.4676 to +1.2676 | no |
| pod start wait, total (s) | 6.3 | 5.7 | −9.5% | −2.1155 to +0.9155 | no |
| pod start wait, mean (s) | 1.353 | 1.264 | −6.6% | −0.5794 to +0.4013 | no |
| host CPU busy, the real machine under kind (%) | 25.31 | 24.48 | −3.3% | −1.3840 to −0.2789 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.514 | −0.2% | −0.0039 to −0.0007 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.6 | −0.2% | −0.5155 to −0.1197 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.6 | −0.2% | −0.5155 to −0.1197 | yes: GAIN |
| response time (ms), mean | 68.36 | 66.92 | −2.1% | −2.6448 to −0.2363 | yes: GAIN |
| response time (ms), 95th percentile | 98.64 | 96.5 | −2.2% | −3.1980 to −1.0860 | yes: GAIN |
| response time (ms), 99th percentile | 137.3 | 128.1 | −6.6% | −18.7070 to +0.4728 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 14.4 | −23.0% | −7.7725 to −0.8275 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.07667 | −52.1% | −0.2884 to +0.1218 | no |
| utilisation (used / allocatable) | 0.03245 | 0.03192 | −1.6% | −0.0010 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.7788 | 0.766 | −1.6% | −0.0243 to −0.0013 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03344 | 0.00682 | −79.6% | −0.0305 to −0.0227 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8122 | 0.7728 | −4.9% | −0.0508 to −0.0280 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.5 | 881.2 | +2.1% | −2.4513 to +37.9077 | no |
| HPA replicas, mean | 8.117 | 6.607 | −18.6% | −1.9157 to −1.1041 | yes: GAIN |
| pods started | 4.8 | 3.3 | −31.2% | −2.7729 to −0.2271 | yes: GAIN |
| pod start wait, total (s) | 6.3 | 4.3 | −31.7% | −4.2112 to +0.2112 | no |
| pod start wait, mean (s) | 1.353 | 1.353 | ±0.0% | −0.4676 to +0.4676 | no |
| host CPU busy, the real machine under kind (%) | 25.31 | 24.05 | −5.0% | −1.5936 to −0.9231 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.514 | −0.1% | −0.0033 to −0.0004 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.3934 to +0.0081 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.3934 to +0.0081 | no |
| response time (ms), mean | 68.36 | 67.89 | −0.7% | −1.8723 to +0.9378 | no |
| response time (ms), 95th percentile | 98.64 | 98.07 | −0.6% | −3.6790 to +2.5470 | no |
| response time (ms), 99th percentile | 137.3 | 128.9 | −6.1% | −22.7426 to +6.1026 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 14.9 | −20.3% | −7.4753 to −0.1247 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.1033 | −35.4% | −0.3485 to +0.2352 | no |
| utilisation (used / allocatable) | 0.03245 | 0.03228 | −0.5% | −0.0008 to +0.0005 | no |
| CPU used (cores), mean | 0.7788 | 0.7746 | −0.5% | −0.0193 to +0.0111 | no |
| Omni's own CPU (cores), mean | 0.03344 | 0.01286 | −61.5% | −0.0235 to −0.0176 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8122 | 0.7875 | −3.0% | −0.0408 to −0.0086 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.5 | 867.9 | +0.5% | −17.1157 to +26.0228 | no |
| HPA replicas, mean | 8.117 | 6.73 | −17.1% | −1.8622 to −0.9117 | yes: GAIN |
| pods started | 4.8 | 3.2 | −33.3% | −2.7778 to −0.4222 | yes: GAIN |
| pod start wait, total (s) | 6.3 | 4.3 | −31.7% | −4.7394 to +0.7394 | no |
| pod start wait, mean (s) | 1.353 | 1.357 | +0.2% | −0.4234 to +0.4301 | no |
| host CPU busy, the real machine under kind (%) | 25.31 | 24.53 | −3.1% | −1.3251 to −0.2298 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.514 | −0.1% | −0.0028 to −0.0005 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.6 | −0.2% | −0.4491 to −0.1164 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.6 | −0.2% | −0.4491 to −0.1164 | yes: GAIN |
| response time (ms), mean | 68.36 | 67.38 | −1.4% | −2.0636 to +0.1039 | no |
| response time (ms), 95th percentile | 98.64 | 97.33 | −1.3% | −2.6964 to +0.0824 | no |
| response time (ms), 99th percentile | 137.3 | 125.3 | −8.7% | −25.5827 to +1.6571 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 17.5 | −6.4% | −2.7744 to +0.3744 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2417 | +51.0% | −0.1213 to +0.2846 | no |
| utilisation (used / allocatable) | 0.03245 | 0.03211 | −1.0% | −0.0008 to +0.0001 | no |
| CPU used (cores), mean | 0.7788 | 0.7706 | −1.0% | −0.0194 to +0.0030 | no |
| Omni's own CPU (cores), mean | 0.03344 | 0.023 | −31.2% | −0.0121 to −0.0088 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8122 | 0.7936 | −2.3% | −0.0307 to −0.0065 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.5 | 869.9 | +0.7% | −9.1746 to +22.1025 | no |
| HPA replicas, mean | 8.117 | 8.059 | −0.7% | −0.2505 to +0.1346 | no |
| pods started | 4.8 | 4.2 | −12.5% | −1.8707 to +0.6707 | no |
| pod start wait, total (s) | 6.3 | 6.4 | +1.6% | −1.6342 to +1.8342 | no |
| pod start wait, mean (s) | 1.353 | 1.477 | +9.1% | −0.3179 to +0.5646 | no |
| host CPU busy, the real machine under kind (%) | 25.31 | 24.66 | −2.6% | −1.0826 to −0.2246 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.515 | −0.1% | −0.0022 to +0.0002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.8 | −0.1% | −0.1924 to +0.0240 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.8 | −0.1% | −0.1924 to +0.0240 | no |
| response time (ms), mean | 68.36 | 67.97 | −0.6% | −1.5904 to +0.7979 | no |
| response time (ms), 95th percentile | 98.64 | 99.43 | +0.8% | −1.5653 to +3.1543 | no |
| response time (ms), 99th percentile | 137.3 | 129.1 | −5.9% | −15.9294 to −0.4012 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 17.4 | −7.0% | −4.1222 to +1.5222 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2083 | +30.2% | −0.3167 to +0.4133 | no |
| utilisation (used / allocatable) | 0.03245 | 0.03255 | +0.3% | −0.0004 to +0.0006 | no |
| CPU used (cores), mean | 0.7788 | 0.7812 | +0.3% | −0.0097 to +0.0146 | no |
| Omni's own CPU (cores), mean | 0.03344 | 0.06291 | +88.1% | +0.0243 to +0.0346 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8122 | 0.8441 | +3.9% | +0.0185 to +0.0454 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.5 | 859.7 | −0.4% | −20.0062 to +12.5724 | no |
| HPA replicas, mean | 8.117 | 7.706 | −5.1% | −1.0456 to +0.2230 | no |
| pods started | 4.8 | 3.7 | −22.9% | −2.5871 to +0.3871 | no |
| pod start wait, total (s) | 6.3 | 4.4 | −30.2% | −3.7299 to −0.0701 | yes: GAIN |
| pod start wait, mean (s) | 1.353 | 1.21 | −10.6% | −0.5144 to +0.2278 | no |
| host CPU busy, the real machine under kind (%) | 25.31 | 26.25 | +3.7% | +0.4505 to +1.4172 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*