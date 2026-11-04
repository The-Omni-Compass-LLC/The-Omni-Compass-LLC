# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.223 | 5.422 |
| node-hours | 2.515 | 2.518 | 2.188 | 2.275 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 275.1 | 274.7 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 275.1 | 250.4 | 256.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 511.9 | 517 | 537.3 | 523.7 |
| response time (ms), 95th percentile | 2033 | 2105 | 2088 | 2133 |
| response time (ms), 99th percentile | 2979 | 2977 | 2938 | 3053 |
| time over the response line (% of samples) | 21.65 | 20.98 | 22.6 | 20.56 |
| failed requests (%) | 0.02362 | 0 | 0 | 0.01176 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 11.3 | 12.1 | 11.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 29.8 | 25.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.98 | 24.16 | 21.04 | 29.21 |
| utilisation (used / allocatable) | 0.0671 | 0.06707 | 0.0771 | 0.07296 |
| CPU used (cores), mean | 1.61 | 1.61 | 1.6 | 1.586 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06347 | 0.06858 |
| CPU used with Omni's own (cores), mean | 1.61 | 1.61 | 1.664 | 1.655 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.8 | 418.5 | 376.4 | 393.1 |
| HPA replicas, mean | 2.138 | 2.034 | 2.476 | 2.442 |
| pods started | 0.1 | 0 | 1.3 | 1.2 |
| pod start wait, total (s) | 0.2 | 0 | 2.8 | 2.6 |
| pod start wait, mean (s) | 0.2 | 0 | 1.208 | 1.3 |
| host CPU busy, the real machine under kind (%) | 46.16 | 46.88 | 48.41 | 49.35 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 845.5 | 852.7 | 853.7 | 860.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.568 | 4.906 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.2542 | 0.8875 | 0.6042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.5 | 0.9 | 4.6 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 151.8 | 162.1 | 157.9 | 165.9 |
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
| worker nodes in service, mean | 6 | 5.422 | −9.6% | −1.1702 to +0.0134 | no |
| node-hours | 2.518 | 2.275 | −9.7% | −0.4911 to +0.0041 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 274.9 | −0.1% | −0.9066 to +0.4951 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 256.7 | −6.7% | −36.9570 to +0.1414 | no |
| response time (ms), mean | 517 | 523.7 | +1.3% | −14.5424 to +27.8909 | no |
| response time (ms), 95th percentile | 2105 | 2133 | +1.3% | −68.7970 to +124.3670 | no |
| response time (ms), 99th percentile | 2977 | 3053 | +2.6% | −76.3851 to +228.2221 | no |
| time over the response line (% of samples) | 20.98 | 20.56 | −2.0% | −1.2513 to +0.4014 | no |
| failed requests (%) | 0 | 0.01176 | +0.012 (native is 0) | −0.0148 to +0.0384 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.7 | +3.5% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.2 | +25.200 (native is 0) | +13.1369 to +37.2631 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.16 | 29.21 | +20.9% | +0.9951 to +9.1116 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06707 | 0.07296 | +8.8% | +0.0000 to +0.0118 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.586 | −1.4% | −0.0586 to +0.0121 | no |
| Omni's own CPU (cores), mean | 0 | 0.06858 | +0.069 (native is 0) | +0.0597 to +0.0775 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.655 | +2.8% | +0.0030 to +0.0876 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.5 | 393.1 | −6.1% | −52.7785 to +1.9417 | no |
| HPA replicas, mean | 2.034 | 2.442 | +20.1% | +0.1505 to +0.6663 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.3879 to +2.0121 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +0.8414 to +4.3586 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.300 (native is 0) | +0.4879 to +2.1121 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.88 | 49.35 | +5.3% | +2.0007 to +2.9341 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 852.7 | 860.9 | +1.0% | +3.6409 to +12.7591 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.906 | −18.2% | −2.0846 to −0.1027 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.6042 | +137.7% | −0.3165 to +1.0165 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1 | +11.1% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 162.1 | 165.9 | +2.3% | +0.8872 to +6.7295 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.518 | +0.1% | −0.0058 to +0.0131 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 275.1 | +0.2% | −0.8842 to +1.7336 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 275.1 | +0.2% | −0.8842 to +1.7336 | no |
| response time (ms), mean | 511.9 | 517 | +1.0% | −8.3066 to +18.5912 | no |
| response time (ms), 95th percentile | 2033 | 2105 | +3.5% | −22.4030 to +165.3810 | no |
| response time (ms), 99th percentile | 2979 | 2977 | −0.1% | −116.4830 to +111.1818 | no |
| time over the response line (% of samples) | 21.65 | 20.98 | −3.1% | −1.5265 to +0.1829 | no |
| failed requests (%) | 0.02362 | 0 | −100.0% | −0.0592 to +0.0120 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 11.3 | −5.0% | −1.3689 to +0.1689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.98 | 24.16 | +34.4% | +2.5778 to +9.7822 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0671 | 0.06707 | −0.0% | −0.0016 to +0.0015 | no |
| CPU used (cores), mean | 1.61 | 1.61 | −0.0% | −0.0385 to +0.0370 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.61 | 1.61 | −0.0% | −0.0385 to +0.0370 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.8 | 418.5 | +0.7% | −11.4193 to +16.8637 | no |
| HPA replicas, mean | 2.138 | 2.034 | −4.9% | −0.2794 to +0.0704 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 46.16 | 46.88 | +1.6% | +0.2817 to +1.1565 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 845.5 | 852.7 | +0.9% | +0.5085 to +13.8915 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.2542 | −64.9% | −1.2040 to +0.2623 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.5 | 0.9 | −86.2% | −13.5166 to +2.3166 | no |
| queue: job turnaround, submitted to done, mean (s) | 151.8 | 162.1 | +6.8% | +1.7146 to +19.0604 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.223 | −13.0% | −1.4766 to −0.0776 | yes: GAIN |
| node-hours | 2.515 | 2.189 | −13.0% | −0.6189 to −0.0331 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.7 | +0.0% | −0.7749 to +0.8741 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 250.4 | −8.9% | −46.6201 to −2.0057 | yes: GAIN |
| response time (ms), mean | 511.9 | 537.3 | +5.0% | +5.0499 to +45.8175 | yes: LOSS |
| response time (ms), 95th percentile | 2033 | 2088 | +2.7% | +2.9532 to +107.1908 | yes: LOSS |
| response time (ms), 99th percentile | 2979 | 2938 | −1.4% | −277.5631 to +194.1063 | no |
| time over the response line (% of samples) | 21.65 | 22.6 | +4.4% | −0.4224 to +2.3207 | no |
| failed requests (%) | 0.02362 | 0 | −100.0% | −0.0592 to +0.0120 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12.1 | +1.7% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.800 (native is 0) | +14.1836 to +45.4164 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.98 | 21.04 | +17.1% | −0.6458 to +6.7758 | no |
| utilisation (used / allocatable) | 0.0671 | 0.0771 | +14.9% | +0.0014 to +0.0186 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.6 | −0.6% | −0.0471 to +0.0268 | no |
| Omni's own CPU (cores), mean | 0 | 0.06347 | +0.063 (native is 0) | +0.0554 to +0.0715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.664 | +3.3% | +0.0103 to +0.0964 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.8 | 376.4 | −9.5% | −73.0068 to −5.8235 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.138 | 2.476 | +15.8% | +0.0943 to +0.5817 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.1444 to +2.2556 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | −0.0594 to +5.2594 | no |
| pod start wait, mean (s) | 0.2 | 1.208 | +504.2% | +0.2054 to +1.8112 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.16 | 48.41 | +4.9% | +1.6134 to +2.8846 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 845.5 | 853.7 | +1.0% | +3.0441 to +13.3559 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.568 | −23.9% | −2.5330 to −0.3301 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.8875 | +22.4% | −0.5304 to +0.8554 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.5 | 4.6 | −29.2% | −9.2293 to +5.4293 | no |
| queue: job turnaround, submitted to done, mean (s) | 151.8 | 157.9 | +4.0% | −1.6246 to +13.8746 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.223 | −13.0% | −1.4766 to −0.0776 | yes: GAIN |
| node-hours | 2.518 | 2.188 | −13.1% | −0.6255 to −0.0338 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 274.7 | −0.1% | −1.2512 to +0.5010 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 250.4 | −9.0% | −46.9378 to −2.5373 | yes: GAIN |
| response time (ms), mean | 517 | 537.3 | +3.9% | +2.8901 to +37.6927 | yes: LOSS |
| response time (ms), 95th percentile | 2105 | 2088 | −0.8% | −125.0533 to +92.2193 | no |
| response time (ms), 99th percentile | 2977 | 2938 | −1.3% | −266.3502 to +188.1946 | no |
| time over the response line (% of samples) | 20.98 | 22.6 | +7.7% | +0.0628 to +3.1791 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 12.1 | +7.1% | −0.2556 to +1.8556 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.800 (native is 0) | +14.1836 to +45.4164 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.16 | 21.04 | −12.9% | −5.2108 to −1.0192 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06707 | 0.0771 | +15.0% | +0.0003 to +0.0197 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.6 | −0.6% | −0.0296 to +0.0107 | no |
| Omni's own CPU (cores), mean | 0 | 0.06347 | +0.063 (native is 0) | +0.0554 to +0.0715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.664 | +3.4% | +0.0320 to +0.0760 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.5 | 376.4 | −10.1% | −85.2113 to +0.9366 | no |
| HPA replicas, mean | 2.034 | 2.476 | +21.8% | +0.1894 to +0.6956 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.2856 to +2.3144 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | +0.2143 to +5.3857 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.208 | +1.208 (native is 0) | +0.4209 to +1.9958 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.88 | 48.41 | +3.3% | +1.2315 to +1.8284 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 852.7 | 853.7 | +0.1% | −3.1845 to +5.1845 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.568 | −23.9% | −2.5330 to −0.3301 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.8875 | +249.2% | −0.2133 to +1.4799 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 4.6 | +411.1% | −0.1157 to +7.5157 | no |
| queue: job turnaround, submitted to done, mean (s) | 162.1 | 157.9 | −2.6% | −8.9229 to +0.3979 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.422 | −9.6% | −1.1702 to +0.0134 | no |
| node-hours | 2.515 | 2.275 | −9.5% | −0.4874 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.9 | +0.1% | −1.0500 to +1.4879 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 256.7 | −6.5% | −37.0973 to +1.1310 | no |
| response time (ms), mean | 511.9 | 523.7 | +2.3% | −2.9348 to +26.5679 | no |
| response time (ms), 95th percentile | 2033 | 2133 | +4.9% | +14.6577 to +183.8903 | yes: LOSS |
| response time (ms), 99th percentile | 2979 | 3053 | +2.5% | −77.0486 to +223.5844 | no |
| time over the response line (% of samples) | 21.65 | 20.56 | −5.1% | −1.9377 to −0.2558 | yes: GAIN |
| failed requests (%) | 0.02362 | 0.01176 | −50.2% | −0.0597 to +0.0360 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 11.7 | −1.7% | −0.7642 to +0.3642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.2 | +25.200 (native is 0) | +13.1369 to +37.2631 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.98 | 29.21 | +62.5% | +4.4583 to +18.0084 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0671 | 0.07296 | +8.7% | +0.0012 to +0.0105 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.586 | −1.5% | −0.0911 to +0.0432 | no |
| Omni's own CPU (cores), mean | 0 | 0.06858 | +0.069 (native is 0) | +0.0597 to +0.0775 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.655 | +2.8% | −0.0297 to +0.1189 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.8 | 393.1 | −5.5% | −40.6485 to −4.7439 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.138 | 2.442 | +14.2% | +0.0863 to +0.5215 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.6 | +1200.0% | +0.4280 to +4.3720 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.3 | +550.0% | +0.0231 to +2.1769 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.16 | 49.35 | +6.9% | +2.5131 to +3.8599 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 845.5 | 860.9 | +1.8% | +6.6510 to +24.1490 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.906 | −18.2% | −2.0846 to −0.1027 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.6042 | −16.7% | −1.1460 to +0.9044 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.5 | 1 | −84.6% | −13.4600 to +2.4600 | no |
| queue: job turnaround, submitted to done, mean (s) | 151.8 | 165.9 | +9.4% | +4.5344 to +23.8573 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*