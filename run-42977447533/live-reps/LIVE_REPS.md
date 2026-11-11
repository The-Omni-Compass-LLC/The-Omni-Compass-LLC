# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 90 s | omni, a decision every 60 s |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 4.508 | 4.51 | 4.514 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 505.3 | 505.2 | 504.5 | 504.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.3 | 505.2 | 504.5 | 504.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 222.2 | 147.1 | 125.1 | 127.3 |
| response time (ms), 95th percentile | 600.9 | 343.7 | 237.8 | 237.1 |
| response time (ms), 99th percentile | 1479 | 1929 | 1069 | 1110 |
| time over the response line (% of samples) | 12.53 | 7.984 | 6.618 | 6.64 |
| failed requests (%) | 5.7 | 5.714 | 4.988 | 4.994 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.2 | 14.6 | 13.3 | 13.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.9 | 37.1 | 37.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 85 | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.8367 | 0.715 | 0.72 |
| utilisation (used / allocatable) | 0.08536 | 0.08492 | 0.08316 | 0.08401 |
| CPU used (cores), mean | 2.049 | 2.038 | 1.996 | 2.016 |
| Omni's own CPU (cores), mean | 0 | 0.04025 | 0.00657 | 0.00868 |
| CPU used with Omni's own (cores), mean | 2.049 | 2.078 | 2.002 | 2.025 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 364.4 | 368.4 | 375.9 | 369.6 |
| HPA replicas, mean | 9.425 | 11.73 | 9.462 | 10.15 |
| pods started | 5.8 | 10.7 | 7.3 | 7.8 |
| pod start wait, total (s) | 8.1 | 18.3 | 12.1 | 11.3 |
| pod start wait, mean (s) | 1.395 | 1.698 | 1.599 | 1.396 |
| host CPU busy, the real machine under kind (%) | 58.41 | 59.42 | 57.21 | 57.7 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.508 | 4.51 | +0.0% | −0.0039 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 505.3 | 505.2 | −0.0% | −1.3680 to +1.1548 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.3 | 505.2 | −0.0% | −1.3680 to +1.1548 | no |
| response time (ms), mean | 222.2 | 147.1 | −33.8% | −111.4369 to −38.8314 | yes: GAIN |
| response time (ms), 95th percentile | 600.9 | 343.7 | −42.8% | −399.0493 to −115.2967 | yes: GAIN |
| response time (ms), 99th percentile | 1479 | 1929 | +30.4% | −822.2203 to +1722.0101 | no |
| time over the response line (% of samples) | 12.53 | 7.984 | −36.3% | −6.8686 to −2.2250 | yes: GAIN |
| failed requests (%) | 5.7 | 5.714 | +0.2% | −0.4884 to +0.5157 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.2 | 14.6 | −27.7% | −8.1279 to −3.0721 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.9 | +51.900 (native is 0) | +38.3723 to +65.4277 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.8367 | +108.3% | +0.0551 to +0.8149 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08536 | 0.08492 | −0.5% | −0.0017 to +0.0008 | no |
| CPU used (cores), mean | 2.049 | 2.038 | −0.5% | −0.0409 to +0.0196 | no |
| Omni's own CPU (cores), mean | 0 | 0.04025 | +0.040 (native is 0) | +0.0320 to +0.0485 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.049 | 2.078 | +1.4% | −0.0054 to +0.0646 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 364.4 | 368.4 | +1.1% | −3.1886 to +11.2370 | no |
| HPA replicas, mean | 9.425 | 11.73 | +24.5% | +0.5912 to +4.0258 | yes: power given |
| pods started | 5.8 | 10.7 | +84.5% | +2.2567 to +7.5433 | yes: power given |
| pod start wait, total (s) | 8.1 | 18.3 | +125.9% | +4.4104 to +15.9896 | yes: LOSS |
| pod start wait, mean (s) | 1.395 | 1.698 | +21.7% | +0.0692 to +0.5374 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.41 | 59.42 | +1.7% | +0.0783 to +1.9419 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.508 | 4.514 | +0.1% | −0.0023 to +0.0143 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 505.3 | 504.5 | −0.1% | −1.9505 to +0.4890 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.3 | 504.5 | −0.1% | −1.9505 to +0.4890 | no |
| response time (ms), mean | 222.2 | 125.1 | −43.7% | −130.8889 to −63.4238 | yes: GAIN |
| response time (ms), 95th percentile | 600.9 | 237.8 | −60.4% | −473.1543 to −253.0847 | yes: GAIN |
| response time (ms), 99th percentile | 1479 | 1069 | −27.7% | −895.5556 to +75.8122 | no |
| time over the response line (% of samples) | 12.53 | 6.618 | −47.2% | −8.9366 to −2.8876 | yes: GAIN |
| failed requests (%) | 5.7 | 4.988 | −12.5% | −1.3569 to −0.0678 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.2 | 13.3 | −34.2% | −9.9432 to −3.8568 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.100 (native is 0) | +25.2959 to +48.9041 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.715 | +78.0% | +0.0774 to +0.5493 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08536 | 0.08316 | −2.6% | −0.0030 to −0.0014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.049 | 1.996 | −2.6% | −0.0715 to −0.0342 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00657 | +0.007 (native is 0) | +0.0053 to +0.0078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.049 | 2.002 | −2.3% | −0.0651 to −0.0274 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 364.4 | 375.9 | +3.1% | +2.5821 to +20.3702 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.425 | 9.462 | +0.4% | −0.7513 to +0.8262 | no |
| pods started | 5.8 | 7.3 | +25.9% | −1.1390 to +4.1390 | no |
| pod start wait, total (s) | 8.1 | 12.1 | +49.4% | −2.1255 to +10.1255 | no |
| pod start wait, mean (s) | 1.395 | 1.599 | +14.6% | −0.1663 to +0.5741 | no |
| host CPU busy, the real machine under kind (%) | 58.41 | 57.21 | −2.1% | −1.7885 to −0.6163 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.508 | 4.513 | +0.1% | −0.0024 to +0.0117 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 505.3 | 504.9 | −0.1% | −1.5229 to +0.7816 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.3 | 504.9 | −0.1% | −1.5229 to +0.7816 | no |
| response time (ms), mean | 222.2 | 127.3 | −42.7% | −129.2185 to −60.5445 | yes: GAIN |
| response time (ms), 95th percentile | 600.9 | 237.1 | −60.5% | −472.1733 to −255.3447 | yes: GAIN |
| response time (ms), 99th percentile | 1479 | 1110 | −24.9% | −868.3635 to +131.5835 | no |
| time over the response line (% of samples) | 12.53 | 6.64 | −47.0% | −8.9366 to −2.8450 | yes: GAIN |
| failed requests (%) | 5.7 | 4.994 | −12.4% | −1.3354 to −0.0767 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.2 | 13.4 | −33.7% | −9.5560 to −4.0440 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.900 (native is 0) | +26.3195 to +49.4805 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.72 | +79.3% | −0.2009 to +0.8376 | no |
| utilisation (used / allocatable) | 0.08536 | 0.08401 | −1.6% | −0.0027 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.049 | 2.016 | −1.6% | −0.0645 to −0.0004 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00868 | +0.009 (native is 0) | +0.0070 to +0.0103 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.049 | 2.025 | −1.2% | −0.0555 to +0.0080 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 364.4 | 369.6 | +1.4% | −5.5364 to +15.8680 | no |
| HPA replicas, mean | 9.425 | 10.15 | +7.7% | −0.3464 to +1.7963 | no |
| pods started | 5.8 | 7.8 | +34.5% | −0.1326 to +4.1326 | no |
| pod start wait, total (s) | 8.1 | 11.3 | +39.5% | −1.9449 to +8.3449 | no |
| pod start wait, mean (s) | 1.395 | 1.396 | +0.0% | −0.3519 to +0.3531 | no |
| host CPU busy, the real machine under kind (%) | 58.41 | 57.7 | −1.2% | −1.7028 to +0.2753 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.51 | 4.515 | +0.1% | −0.0026 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 505.2 | 504.5 | −0.1% | −1.9090 to +0.6607 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.2 | 504.5 | −0.1% | −1.9090 to +0.6607 | no |
| response time (ms), mean | 147.1 | 125.1 | −15.0% | −55.8290 to +11.7847 | no |
| response time (ms), 95th percentile | 343.7 | 237.8 | −30.8% | −251.6054 to +39.7124 | no |
| response time (ms), 99th percentile | 1929 | 1069 | −44.6% | −1975.4409 to +255.9077 | no |
| time over the response line (% of samples) | 7.984 | 6.618 | −17.1% | −2.6370 to −0.0936 | yes: GAIN |
| failed requests (%) | 5.714 | 4.988 | −12.7% | −1.4741 to +0.0221 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.6 | 13.3 | −8.9% | −2.1953 to −0.4047 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 51.9 | 37.1 | −28.5% | −28.9214 to −0.6786 | yes, down (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 85 | 35 | −58.8% | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8367 | 0.715 | −14.5% | −0.4771 to +0.2338 | no |
| utilisation (used / allocatable) | 0.08492 | 0.08316 | −2.1% | −0.0029 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.038 | 1.996 | −2.1% | −0.0699 to −0.0145 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.04025 | 0.00657 | −83.7% | −0.0407 to −0.0266 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.078 | 2.002 | −3.7% | −0.1074 to −0.0443 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 368.4 | 375.9 | +2.0% | +0.6237 to +14.2801 | yes, up (shown, not judged) |
| HPA replicas, mean | 11.73 | 9.462 | −19.4% | −3.5109 to −1.0312 | yes: GAIN |
| pods started | 10.7 | 7.3 | −31.8% | −6.2652 to −0.5348 | yes: GAIN |
| pod start wait, total (s) | 18.3 | 12.1 | −33.9% | −12.1063 to −0.2937 | yes: GAIN |
| pod start wait, mean (s) | 1.698 | 1.599 | −5.9% | −0.4320 to +0.2332 | no |
| host CPU busy, the real machine under kind (%) | 59.42 | 57.21 | −3.7% | −3.1204 to −1.3046 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.51 | 4.513 | +0.1% | −0.0046 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 505.2 | 504.9 | −0.1% | −1.0184 to +0.4903 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.2 | 504.9 | −0.1% | −1.0184 to +0.4903 | no |
| response time (ms), mean | 147.1 | 127.3 | −13.4% | −56.1685 to +16.6738 | no |
| response time (ms), 95th percentile | 343.7 | 237.1 | −31.0% | −256.2170 to +43.0450 | no |
| response time (ms), 99th percentile | 1929 | 1110 | −42.4% | −2129.6838 to +493.1140 | no |
| time over the response line (% of samples) | 7.984 | 6.64 | −16.8% | −2.7690 to +0.0809 | no |
| failed requests (%) | 5.714 | 4.994 | −12.6% | −1.4331 to −0.0062 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.6 | 13.4 | −8.2% | −2.0121 to −0.3879 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 51.9 | 37.9 | −27.0% | −26.8446 to −1.1554 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8367 | 0.72 | −13.9% | −0.6491 to +0.4157 | no |
| utilisation (used / allocatable) | 0.08492 | 0.08401 | −1.1% | −0.0024 to +0.0005 | no |
| CPU used (cores), mean | 2.038 | 2.016 | −1.1% | −0.0566 to +0.0130 | no |
| Omni's own CPU (cores), mean | 0.04025 | 0.00868 | −78.4% | −0.0382 to −0.0249 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.078 | 2.025 | −2.6% | −0.0929 to −0.0138 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 368.4 | 369.6 | +0.3% | −6.2867 to +8.5698 | no |
| HPA replicas, mean | 11.73 | 10.15 | −13.5% | −2.8442 to −0.3230 | yes: GAIN |
| pods started | 10.7 | 7.8 | −27.1% | −5.2228 to −0.5772 | yes: GAIN |
| pod start wait, total (s) | 18.3 | 11.3 | −38.3% | −11.5988 to −2.4012 | yes: GAIN |
| pod start wait, mean (s) | 1.698 | 1.396 | −17.8% | −0.6289 to +0.0236 | no |
| host CPU busy, the real machine under kind (%) | 59.42 | 57.7 | −2.9% | −2.9224 to −0.5252 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*