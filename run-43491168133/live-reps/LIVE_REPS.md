# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.345 | 9.754 |
| node-hours | 5.03 | 5.036 | 3.923 | 4.086 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.1 | 525.4 | 525.3 | 525.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.1 | 525.4 | 441.6 | 455 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 381.9 | 476.5 | 426 | 584.2 |
| response time (ms), 95th percentile | 1334 | 1865 | 1660 | 2505 |
| response time (ms), 99th percentile | 1806 | 2686 | 2314 | 3780 |
| time over the response line (% of samples) | 14.2 | 15.64 | 19.6 | 20.77 |
| failed requests (%) | 0 | 0.01732 | 0.02299 | 0.1578 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 10.5 | 10.9 | 14.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 128.4 | 52.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 34.6 | 41.34 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.7 | 19.35 | 14.97 | 30.25 |
| utilisation (used / allocatable) | 0.03205 | 0.03282 | 0.04179 | 0.04235 |
| CPU used (cores), mean | 1.538 | 1.575 | 1.533 | 1.625 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05207 | 0.0379 |
| CPU used with Omni's own (cores), mean | 1.538 | 1.575 | 1.585 | 1.663 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.6 | 813.3 | 689 | 669.5 |
| HPA replicas, mean | 4.046 | 3.921 | 4.441 | 4.493 |
| pods started | 0.2 | 0.4 | 2.7 | 2.4 |
| pod start wait, total (s) | 0.3 | 1.1 | 6.5 | 6.7 |
| pod start wait, mean (s) | 0.3 | 0.55 | 1.693 | 2.373 |
| host CPU busy, the real machine under kind (%) | 47.47 | 52.12 | 52.25 | 58.67 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 804.3 | 870.5 | 831.4 | 933.2 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 7.424 | 7.925 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 4.221 | 0.07083 | 3.233 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 31.6 | 0.5 | 33.8 |
| queue: job turnaround, submitted to done, mean (s) | 113.9 | 178.9 | 140.9 | 236.6 |
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
| worker nodes in service, mean | 12 | 9.754 | −18.7% | −3.7828 to −0.7096 | yes: GAIN |
| node-hours | 5.036 | 4.086 | −18.9% | −1.5982 to −0.3017 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 525.5 | +0.0% | −1.9435 to +2.0096 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 455 | −13.4% | −119.1535 to −21.7220 | yes: GAIN |
| response time (ms), mean | 476.5 | 584.2 | +22.6% | +20.7530 to +194.5600 | yes: LOSS |
| response time (ms), 95th percentile | 1865 | 2505 | +34.3% | +169.9133 to +1109.6787 | yes: LOSS |
| response time (ms), 99th percentile | 2686 | 3780 | +40.7% | +473.8696 to +1714.6902 | yes: LOSS |
| time over the response line (% of samples) | 15.64 | 20.77 | +32.8% | +3.0425 to +7.2079 | yes: LOSS |
| failed requests (%) | 0.01732 | 0.1578 | +811.5% | −0.0989 to +0.3799 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 14.4 | +37.1% | +1.2783 to +6.5217 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.5 | +52.500 (native is 0) | +30.7167 to +74.2833 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.35 | 30.25 | +56.4% | −9.7243 to +31.5343 | no |
| utilisation (used / allocatable) | 0.03282 | 0.04235 | +29.0% | +0.0034 to +0.0157 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.575 | 1.625 | +3.1% | −0.0372 to +0.1362 | no |
| Omni's own CPU (cores), mean | 0 | 0.0379 | +0.038 (native is 0) | +0.0302 to +0.0456 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.575 | 1.663 | +5.5% | +0.0013 to +0.1735 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 813.3 | 669.5 | −17.7% | −230.8961 to −56.7795 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.921 | 4.493 | +14.6% | +0.1674 to +0.9770 | yes: power given |
| pods started | 0.4 | 2.4 | +500.0% | +0.7383 to +3.2617 | yes: power given |
| pod start wait, total (s) | 1.1 | 6.7 | +509.1% | +1.6937 to +9.5063 | yes: LOSS |
| pod start wait, mean (s) | 0.55 | 2.373 | +331.5% | +0.5677 to +3.0790 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.12 | 58.67 | +12.6% | +5.3744 to +7.7372 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 870.5 | 933.2 | +7.2% | +36.6525 to +88.7475 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.925 | −34.0% | −6.6407 to −1.5093 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.221 | 3.233 | −23.4% | −3.3479 to +1.3729 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 31.6 | 33.8 | +7.0% | −2.7764 to +7.1764 | no |
| queue: job turnaround, submitted to done, mean (s) | 178.9 | 236.6 | +32.3% | +34.4689 to +81.0144 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.03 | 5.036 | +0.1% | −0.0163 to +0.0290 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.1 | 525.4 | +0.3% | −0.9955 to +3.6920 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.1 | 525.4 | +0.3% | −0.9955 to +3.6920 | no |
| response time (ms), mean | 381.9 | 476.5 | +24.8% | −14.2225 to +203.5066 | no |
| response time (ms), 95th percentile | 1334 | 1865 | +39.8% | −54.0812 to +1115.9682 | no |
| response time (ms), 99th percentile | 1806 | 2686 | +48.7% | +213.3829 to +1545.5099 | yes: LOSS |
| time over the response line (% of samples) | 14.2 | 15.64 | +10.1% | −0.9820 to +3.8599 | no |
| failed requests (%) | 0 | 0.01732 | +0.017 (native is 0) | −0.0219 to +0.0565 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 10.5 | +20.7% | −0.0714 to +3.6714 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.7 | 19.35 | +65.4% | −2.5838 to +17.8872 | no |
| utilisation (used / allocatable) | 0.03205 | 0.03282 | +2.4% | −0.0006 to +0.0021 | no |
| CPU used (cores), mean | 1.538 | 1.575 | +2.4% | −0.0283 to +0.1021 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.538 | 1.575 | +2.4% | −0.0283 to +0.1021 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.6 | 813.3 | −1.8% | −44.7360 to +14.1410 | no |
| HPA replicas, mean | 4.046 | 3.921 | −3.1% | −0.2934 to +0.0438 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | −0.8792 to +2.4792 | no |
| pod start wait, mean (s) | 0.3 | 0.55 | +83.3% | −0.6618 to +1.1618 | no |
| host CPU busy, the real machine under kind (%) | 47.47 | 52.12 | +9.8% | +2.5422 to +6.7510 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.3 | 870.5 | +8.2% | +16.6916 to +115.7084 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 4.221 | +6653.3% | −4.5265 to +12.8432 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 31.6 | +6220.0% | −37.4903 to +99.6903 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.9 | 178.9 | +57.0% | +17.5228 to +112.4022 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.345 | −22.1% | −4.2030 to −1.1063 | yes: GAIN |
| node-hours | 5.03 | 3.923 | −22.0% | −1.7609 to −0.4536 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.1 | 525.3 | +0.2% | −0.9591 to +3.3316 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.1 | 441.6 | −15.7% | −131.8903 to −32.9789 | yes: GAIN |
| response time (ms), mean | 381.9 | 426 | +11.6% | −9.0370 to +97.3199 | no |
| response time (ms), 95th percentile | 1334 | 1660 | +24.4% | +82.8765 to +568.3815 | yes: LOSS |
| response time (ms), 99th percentile | 1806 | 2314 | +28.1% | +105.3566 to +909.9836 | yes: LOSS |
| time over the response line (% of samples) | 14.2 | 19.6 | +38.0% | +0.9165 to +9.8824 | yes: LOSS |
| failed requests (%) | 0 | 0.02299 | +0.023 (native is 0) | −0.0290 to +0.0750 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 10.9 | +25.3% | −1.0131 to +5.4131 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.4 | +128.400 (native is 0) | +65.7506 to +191.0494 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.7 | 14.97 | +28.0% | −0.5989 to +7.1489 | no |
| utilisation (used / allocatable) | 0.03205 | 0.04179 | +30.4% | +0.0039 to +0.0156 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.538 | 1.533 | −0.3% | −0.0693 to +0.0590 | no |
| Omni's own CPU (cores), mean | 0 | 0.05207 | +0.052 (native is 0) | +0.0474 to +0.0567 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.538 | 1.585 | +3.1% | −0.0176 to +0.1115 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.6 | 689 | −16.8% | −220.2174 to −58.9402 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.046 | 4.441 | +9.8% | +0.0527 to +0.7384 | yes: power given |
| pods started | 0.2 | 2.7 | +1250.0% | +0.7398 to +4.2602 | yes: power given |
| pod start wait, total (s) | 0.3 | 6.5 | +2066.7% | +2.0592 to +10.3408 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.693 | +464.3% | +0.4467 to +2.3390 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.47 | 52.25 | +10.1% | +3.1149 to +6.4447 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.3 | 831.4 | +3.4% | +5.2354 to +48.9646 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.424 | −38.1% | −6.8728 to −2.2798 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.07083 | +13.3% | −0.0255 to +0.0422 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.9 | 140.9 | +23.7% | +5.9684 to +48.0316 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.345 | −22.1% | −4.2030 to −1.1063 | yes: GAIN |
| node-hours | 5.036 | 3.923 | −22.1% | −1.7635 to −0.4637 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 525.3 | −0.0% | −1.0371 to +0.7130 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 441.6 | −15.9% | −132.4847 to −35.0810 | yes: GAIN |
| response time (ms), mean | 476.5 | 426 | −10.6% | −128.0890 to +27.0879 | no |
| response time (ms), 95th percentile | 1865 | 1660 | −11.0% | −633.2178 to +222.5888 | no |
| response time (ms), 99th percentile | 2686 | 2314 | −13.8% | −795.2274 to +51.6748 | no |
| time over the response line (% of samples) | 15.64 | 19.6 | +25.3% | −0.9677 to +8.8887 | no |
| failed requests (%) | 0.01732 | 0.02299 | +32.8% | −0.0072 to +0.0185 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.9 | +3.8% | −1.9891 to +2.7891 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.4 | +128.400 (native is 0) | +65.7506 to +191.0494 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.35 | 14.97 | −22.6% | −11.4695 to +2.7162 | no |
| utilisation (used / allocatable) | 0.03282 | 0.04179 | +27.3% | +0.0028 to +0.0152 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.575 | 1.533 | −2.7% | −0.0916 to +0.0075 | no |
| Omni's own CPU (cores), mean | 0 | 0.05207 | +0.052 (native is 0) | +0.0474 to +0.0567 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.575 | 1.585 | +0.6% | −0.0383 to +0.0583 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 813.3 | 689 | −15.3% | −209.0330 to −39.5296 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.921 | 4.441 | +13.3% | +0.1975 to +0.8432 | yes: power given |
| pods started | 0.4 | 2.7 | +575.0% | +0.4826 to +4.1174 | yes: power given |
| pod start wait, total (s) | 1.1 | 6.5 | +490.9% | +1.0660 to +9.7340 | yes: LOSS |
| pod start wait, mean (s) | 0.55 | 1.693 | +207.8% | −0.0808 to +2.3665 | no |
| host CPU busy, the real machine under kind (%) | 52.12 | 52.25 | +0.3% | −1.2975 to +1.5639 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 870.5 | 831.4 | −4.5% | −74.3215 to −3.8785 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 7.424 | −38.1% | −6.8728 to −2.2798 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.221 | 0.07083 | −98.3% | −12.8264 to +4.5264 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 31.6 | 0.5 | −98.4% | −99.6903 to +37.4903 | no |
| queue: job turnaround, submitted to done, mean (s) | 178.9 | 140.9 | −21.2% | −75.1905 to −0.7345 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.754 | −18.7% | −3.7828 to −0.7096 | yes: GAIN |
| node-hours | 5.03 | 4.086 | −18.8% | −1.5972 to −0.2900 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.1 | 525.5 | +0.3% | −0.7301 to +3.4928 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.1 | 455 | −13.2% | −118.7835 to −19.3954 | yes: GAIN |
| response time (ms), mean | 381.9 | 584.2 | +53.0% | +50.1356 to +354.4614 | yes: LOSS |
| response time (ms), 95th percentile | 1334 | 2505 | +87.7% | +479.1324 to +1862.3466 | yes: LOSS |
| response time (ms), 99th percentile | 1806 | 3780 | +109.3% | +1007.3317 to +2940.1209 | yes: LOSS |
| time over the response line (% of samples) | 14.2 | 20.77 | +46.2% | +3.6652 to +9.4632 | yes: LOSS |
| failed requests (%) | 0 | 0.1578 | +0.158 (native is 0) | −0.0940 to +0.4096 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 14.4 | +65.5% | +3.1531 to +8.2469 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.5 | +52.500 (native is 0) | +30.7167 to +74.2833 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.7 | 30.25 | +158.7% | −3.2394 to +40.3528 | no |
| utilisation (used / allocatable) | 0.03205 | 0.04235 | +32.1% | +0.0048 to +0.0158 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.538 | 1.625 | +5.6% | +0.0301 to +0.1427 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0379 | +0.038 (native is 0) | +0.0302 to +0.0456 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.538 | 1.663 | +8.1% | +0.0677 to +0.1809 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.6 | 669.5 | −19.2% | −238.0549 to −80.2157 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.046 | 4.493 | +11.1% | +0.0031 to +0.8917 | yes: power given |
| pods started | 0.2 | 2.4 | +1100.0% | +0.9028 to +3.4972 | yes: power given |
| pod start wait, total (s) | 0.3 | 6.7 | +2133.3% | +2.2400 to +10.5600 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.373 | +691.1% | +1.0032 to +3.1434 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.47 | 58.67 | +23.6% | +9.0120 to +13.3928 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.3 | 933.2 | +16.0% | +66.8825 to +190.9175 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.925 | −34.0% | −6.6407 to −1.5093 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 3.233 | +5073.3% | −3.1547 to +9.4964 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 33.8 | +6660.0% | −40.2666 to +106.8666 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.9 | 236.6 | +107.7% | +62.2646 to +183.1438 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*