# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.512 | 1.512 | 1.513 | 1.51 | 1.512 | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158 | 158.2 | 158.2 | 158 | 158.1 | 158.3 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158 | 158.2 | 158.2 | 158 | 158.1 | 158.3 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 144.1 | 74.98 | 75.85 | 75.59 | 76.99 | 74.96 | 75.51 | 76.54 |
| response time (ms), 95th percentile | 321.9 | 112.3 | 112 | 112.8 | 118.4 | 110.4 | 112 | 116 |
| response time (ms), 99th percentile | 503.8 | 161.3 | 150 | 152.8 | 160.7 | 150.9 | 152.3 | 156.1 |
| time over the response line (% of samples) | 1.981 | 0 | 0.01212 | 0.08529 | 0.01235 | 0 | 0.02424 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | 0 | 0.2 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 | 15 | 20.6 | 16.9 | 17.4 | 20 | 19.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | 100 | 80 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.1333 | 0.08 | 0.135 | 0.11 | 0.05333 | 0.1617 | 0.2717 |
| utilisation (used / allocatable) | 0.0369 | 0.03511 | 0.03555 | 0.03537 | 0.03583 | 0.03521 | 0.03545 | 0.03602 |
| CPU used (cores), mean | 0.8857 | 0.8427 | 0.8532 | 0.849 | 0.8598 | 0.8451 | 0.8508 | 0.8646 |
| Omni's own CPU (cores), mean | 0 | 0.00858 | 0.00591 | 0.00706 | 0.0076 | 0.01376 | 0.02456 | 0.06751 |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.8513 | 0.8591 | 0.856 | 0.8674 | 0.8589 | 0.8754 | 0.9321 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 801.9 | 792.1 | 795.5 | 793.6 | 804.2 | 793.7 | 785.4 |
| HPA replicas, mean | 8.181 | 8.1 | 8.124 | 8.262 | 7.122 | 7.323 | 8.391 | 8.193 |
| pods started | 5.4 | 3.9 | 3.9 | 4.8 | 3.4 | 3.5 | 3.8 | 3.6 |
| pod start wait, total (s) | 7.8 | 5.8 | 6.2 | 7.6 | 4.7 | 5 | 5.6 | 5.5 |
| pod start wait, mean (s) | 1.453 | 1.445 | 1.47 | 1.47 | 1.4 | 1.42 | 1.433 | 1.437 |
| host CPU busy, the real machine under kind (%) | 26.96 | 26.06 | 26.25 | 26.31 | 26.69 | 26.25 | 26.88 | 28.6 |
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
| node-hours | 1.513 | 1.511 | −0.1% | −0.0033 to +0.0010 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158 | −0.4% | −1.0173 to −0.1582 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158 | −0.4% | −1.0173 to −0.1582 | yes: GAIN |
| response time (ms), mean | 144.1 | 74.98 | −48.0% | −95.7160 to −42.5021 | yes: GAIN |
| response time (ms), 95th percentile | 321.9 | 112.3 | −65.1% | −283.4537 to −135.7773 | yes: GAIN |
| response time (ms), 99th percentile | 503.8 | 161.3 | −68.0% | −445.6092 to −239.3686 | yes: GAIN |
| time over the response line (% of samples) | 1.981 | 0 | −100.0% | −3.3431 to −0.6189 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.6171 to −0.3829 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 | +18.100 (native is 0) | +15.6813 to +20.5187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.1333 | −38.5% | −0.4347 to +0.2680 | no |
| utilisation (used / allocatable) | 0.0369 | 0.03511 | −4.9% | −0.0030 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8857 | 0.8427 | −4.9% | −0.0716 to −0.0143 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00858 | +0.009 (native is 0) | +0.0071 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.8513 | −3.9% | −0.0617 to −0.0071 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 801.9 | +3.0% | +4.5081 to +42.8116 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.181 | 8.1 | −1.0% | −0.4450 to +0.2831 | no |
| pods started | 5.4 | 3.9 | −27.8% | −2.2726 to −0.7274 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5.8 | −25.6% | −4.1326 to +0.1326 | no |
| pod start wait, mean (s) | 1.453 | 1.445 | −0.6% | −0.3823 to +0.3656 | no |
| host CPU busy, the real machine under kind (%) | 26.96 | 26.06 | −3.3% | −1.5601 to −0.2405 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.512 | −0.0% | −0.0016 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.2 | −0.2% | −0.6972 to −0.0897 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.2 | −0.2% | −0.6972 to −0.0897 | yes: GAIN |
| response time (ms), mean | 144.1 | 75.85 | −47.4% | −94.5085 to −41.9687 | yes: GAIN |
| response time (ms), 95th percentile | 321.9 | 112 | −65.2% | −283.9428 to −135.8622 | yes: GAIN |
| response time (ms), 99th percentile | 503.8 | 150 | −70.2% | −461.9761 to −245.6551 | yes: GAIN |
| time over the response line (% of samples) | 1.981 | 0.01212 | −99.4% | −3.3272 to −0.6105 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.6171 to −0.3829 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 | +15.000 (native is 0) | +13.7842 to +16.2158 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.08 | −63.1% | −0.4185 to +0.1452 | no |
| utilisation (used / allocatable) | 0.0369 | 0.03555 | −3.7% | −0.0024 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8857 | 0.8532 | −3.7% | −0.0573 to −0.0077 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00591 | +0.006 (native is 0) | +0.0049 to +0.0069 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.8591 | −3.0% | −0.0505 to −0.0026 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 792.1 | +1.8% | −4.6065 to +32.4740 | no |
| HPA replicas, mean | 8.181 | 8.124 | −0.7% | −0.3632 to +0.2485 | no |
| pods started | 5.4 | 3.9 | −27.8% | −2.5256 to −0.4744 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 6.2 | −20.5% | −4.3436 to +1.1436 | no |
| pod start wait, mean (s) | 1.453 | 1.47 | +1.1% | −0.3457 to +0.3790 | no |
| host CPU busy, the real machine under kind (%) | 26.96 | 26.25 | −2.6% | −1.4197 to −0.0088 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.513 | 0.0% | raw −0.0016 to +0.0016 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.2 | −0.3% | −0.6752 to −0.1459 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.2 | −0.3% | −0.6752 to −0.1459 | yes: GAIN |
| response time (ms), mean | 144.1 | 75.59 | −47.5% | −94.6092 to −42.3774 | yes: GAIN |
| response time (ms), 95th percentile | 321.9 | 112.8 | −65.0% | −282.5391 to −135.6509 | yes: GAIN |
| response time (ms), 99th percentile | 503.8 | 152.8 | −69.7% | −458.1853 to −243.8193 | yes: GAIN |
| time over the response line (% of samples) | 1.981 | 0.08529 | −95.7% | −3.2192 to −0.5722 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0.2 | −90.0% | −3.3379 to −0.2621 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.6 | +20.600 (native is 0) | +14.0164 to +27.1836 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.135 | −37.7% | −0.3265 to +0.1632 | no |
| utilisation (used / allocatable) | 0.0369 | 0.03537 | −4.1% | −0.0026 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8857 | 0.849 | −4.1% | −0.0630 to −0.0105 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00706 | +0.007 (native is 0) | +0.0055 to +0.0086 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.856 | −3.4% | −0.0546 to −0.0047 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 795.5 | +2.2% | +0.4284 to +34.1178 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.181 | 8.262 | +1.0% | −0.3772 to +0.5392 | no |
| pods started | 5.4 | 4.8 | −11.1% | −2.2242 to +1.0242 | no |
| pod start wait, total (s) | 7.8 | 7.6 | −2.6% | −5.9994 to +5.5994 | no |
| pod start wait, mean (s) | 1.453 | 1.47 | +1.1% | −0.5274 to +0.5608 | no |
| host CPU busy, the real machine under kind (%) | 26.96 | 26.31 | −2.4% | −1.2131 to −0.0897 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.51 | −0.2% | −0.0073 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158 | −0.4% | −1.0394 to −0.1416 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158 | −0.4% | −1.0394 to −0.1416 | yes: GAIN |
| response time (ms), mean | 144.1 | 76.99 | −46.6% | −92.9232 to −41.2747 | yes: GAIN |
| response time (ms), 95th percentile | 321.9 | 118.4 | −63.2% | −273.8783 to −132.9947 | yes: GAIN |
| response time (ms), 99th percentile | 503.8 | 160.7 | −68.1% | −445.0292 to −241.0418 | yes: GAIN |
| time over the response line (% of samples) | 1.981 | 0.01235 | −99.4% | −3.3243 to −0.6130 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.6171 to −0.3829 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | +16.900 (native is 0) | +12.7366 to +21.0634 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.11 | −49.2% | −0.4508 to +0.2375 | no |
| utilisation (used / allocatable) | 0.0369 | 0.03583 | −2.9% | −0.0026 to +0.0004 | no |
| CPU used (cores), mean | 0.8857 | 0.8598 | −2.9% | −0.0620 to +0.0102 | no |
| Omni's own CPU (cores), mean | 0 | 0.0076 | +0.008 (native is 0) | +0.0061 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.8674 | −2.1% | −0.0538 to +0.0172 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 793.6 | +2.0% | −4.4848 to +35.3439 | no |
| HPA replicas, mean | 8.181 | 7.122 | −12.9% | −1.6989 to −0.4184 | yes: GAIN |
| pods started | 5.4 | 3.4 | −37.0% | −2.6744 to −1.3256 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 4.7 | −39.7% | −4.4254 to −1.7746 | yes: GAIN |
| pod start wait, mean (s) | 1.453 | 1.4 | −3.7% | −0.2554 to +0.1487 | no |
| host CPU busy, the real machine under kind (%) | 26.96 | 26.69 | −1.0% | −1.3334 to +0.7866 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.512 | −0.1% | −0.0026 to +0.0010 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.1 | −0.3% | −0.7788 to −0.1608 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.1 | −0.3% | −0.7788 to −0.1608 | yes: GAIN |
| response time (ms), mean | 144.1 | 74.96 | −48.0% | −95.6533 to −42.5925 | yes: GAIN |
| response time (ms), 95th percentile | 321.9 | 110.4 | −65.7% | −285.3203 to −137.6317 | yes: GAIN |
| response time (ms), 99th percentile | 503.8 | 150.9 | −70.0% | −460.5766 to −245.2002 | yes: GAIN |
| time over the response line (% of samples) | 1.981 | 0 | −100.0% | −3.3431 to −0.6189 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.6171 to −0.3829 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.400 (native is 0) | +13.0660 to +21.7340 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.05333 | −75.4% | −0.4813 to +0.1547 | no |
| utilisation (used / allocatable) | 0.0369 | 0.03521 | −4.6% | −0.0026 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8857 | 0.8451 | −4.6% | −0.0631 to −0.0180 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01376 | +0.014 (native is 0) | +0.0113 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.8589 | −3.0% | −0.0471 to −0.0065 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 804.2 | +3.3% | +15.6066 to +36.4447 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.181 | 7.323 | −10.5% | −1.3705 to −0.3459 | yes: GAIN |
| pods started | 5.4 | 3.5 | −35.2% | −2.8204 to −0.9796 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5 | −35.9% | −5.4722 to −0.1278 | yes: GAIN |
| pod start wait, mean (s) | 1.453 | 1.42 | −2.3% | −0.4248 to +0.3581 | no |
| host CPU busy, the real machine under kind (%) | 26.96 | 26.25 | −2.6% | −1.3665 to −0.0572 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.513 | +0.0% | −0.0015 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.3 | −0.2% | −0.6775 to +0.0758 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.3 | −0.2% | −0.6775 to +0.0758 | no |
| response time (ms), mean | 144.1 | 75.51 | −47.6% | −95.3636 to −41.7849 | yes: GAIN |
| response time (ms), 95th percentile | 321.9 | 112 | −65.2% | −284.2192 to −135.5058 | yes: GAIN |
| response time (ms), 99th percentile | 503.8 | 152.3 | −69.8% | −461.0505 to −241.9587 | yes: GAIN |
| time over the response line (% of samples) | 1.981 | 0.02424 | −98.8% | −3.2975 to −0.6160 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.6171 to −0.3829 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20.000 (native is 0) | +18.9884 to +21.0116 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.1617 | −25.4% | −0.3935 to +0.2835 | no |
| utilisation (used / allocatable) | 0.0369 | 0.03545 | −3.9% | −0.0027 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8857 | 0.8508 | −3.9% | −0.0637 to −0.0060 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02456 | +0.025 (native is 0) | +0.0207 to +0.0284 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.8754 | −1.2% | −0.0356 to +0.0150 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 793.7 | +2.0% | −2.9602 to +33.9029 | no |
| HPA replicas, mean | 8.181 | 8.391 | +2.6% | +0.0031 to +0.4161 | yes: power given |
| pods started | 5.4 | 3.8 | −29.6% | −2.9146 to −0.2854 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5.6 | −28.2% | −4.9144 to +0.5144 | no |
| pod start wait, mean (s) | 1.453 | 1.433 | −1.4% | −0.4351 to +0.3951 | no |
| host CPU busy, the real machine under kind (%) | 26.96 | 26.88 | −0.3% | −0.7926 to +0.6230 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0011 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −0.3574 to +0.0911 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −0.3574 to +0.0911 | no |
| response time (ms), mean | 144.1 | 76.54 | −46.9% | −93.2943 to −41.7973 | yes: GAIN |
| response time (ms), 95th percentile | 321.9 | 116 | −64.0% | −277.4359 to −134.3181 | yes: GAIN |
| response time (ms), 99th percentile | 503.8 | 156.1 | −69.0% | −447.5786 to −247.8472 | yes: GAIN |
| time over the response line (% of samples) | 1.981 | 0 | −100.0% | −3.3431 to −0.6189 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.6171 to −0.3829 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.9 | +19.900 (native is 0) | +17.6018 to +22.1982 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2167 | 0.2717 | +25.4% | −0.3808 to +0.4908 | no |
| utilisation (used / allocatable) | 0.0369 | 0.03602 | −2.4% | −0.0017 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8857 | 0.8646 | −2.4% | −0.0406 to −0.0017 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06751 | +0.068 (native is 0) | +0.0557 to +0.0793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8857 | 0.9321 | +5.2% | +0.0365 to +0.0563 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.2 | 785.4 | +0.9% | −8.4070 to +22.7217 | no |
| HPA replicas, mean | 8.181 | 8.193 | +0.1% | −0.3452 to +0.3683 | no |
| pods started | 5.4 | 3.6 | −33.3% | −2.8556 to −0.7444 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5.5 | −29.5% | −4.7327 to +0.1327 | no |
| pod start wait, mean (s) | 1.453 | 1.437 | −1.1% | −0.3286 to +0.2953 | no |
| host CPU busy, the real machine under kind (%) | 26.96 | 28.6 | +6.1% | +1.2419 to +2.0231 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | +0.0% | −0.0019 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158.2 | +0.1% | −0.1644 to +0.5529 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158.2 | +0.1% | −0.1644 to +0.5529 | no |
| response time (ms), mean | 74.98 | 75.85 | +1.2% | −0.2721 to +2.0130 | no |
| response time (ms), 95th percentile | 112.3 | 112 | −0.3% | −1.4558 to +0.8818 | no |
| response time (ms), 99th percentile | 161.3 | 150 | −7.0% | −21.1578 to −1.4956 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.1 | 15 | −17.1% | −5.1909 to −1.0091 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.08 | −40.0% | −0.2879 to +0.1812 | no |
| utilisation (used / allocatable) | 0.03511 | 0.03555 | +1.2% | −0.0002 to +0.0010 | no |
| CPU used (cores), mean | 0.8427 | 0.8532 | +1.2% | −0.0037 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.00591 | −31.1% | −0.0032 to −0.0021 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8513 | 0.8591 | +0.9% | −0.0062 to +0.0218 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.9 | 792.1 | −1.2% | −24.2598 to +4.8075 | no |
| HPA replicas, mean | 8.1 | 8.124 | +0.3% | −0.3181 to +0.3654 | no |
| pods started | 3.9 | 3.9 | ±0.0% | −0.8260 to +0.8260 | no |
| pod start wait, total (s) | 5.8 | 6.2 | +6.9% | −1.3907 to +2.1907 | no |
| pod start wait, mean (s) | 1.445 | 1.47 | +1.7% | −0.3374 to +0.3874 | no |
| host CPU busy, the real machine under kind (%) | 26.06 | 26.25 | +0.7% | −0.2162 to +0.5882 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0009 to +0.0033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158.2 | +0.1% | −0.1415 to +0.4958 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158.2 | +0.1% | −0.1415 to +0.4958 | no |
| response time (ms), mean | 74.98 | 75.59 | +0.8% | −1.0174 to +2.2489 | no |
| response time (ms), 95th percentile | 112.3 | 112.8 | +0.5% | −4.9450 to +5.9860 | no |
| response time (ms), 99th percentile | 161.3 | 152.8 | −5.3% | −38.8371 to +21.8103 | no |
| time over the response line (% of samples) | 0 | 0.08529 | +0.085 (native is 0) | −0.0794 to +0.2500 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.1 | 20.6 | +13.8% | −3.3720 to +8.3720 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.135 | +1.3% | −0.2537 to +0.2570 | no |
| utilisation (used / allocatable) | 0.03511 | 0.03537 | +0.7% | −0.0002 to +0.0007 | no |
| CPU used (cores), mean | 0.8427 | 0.849 | +0.7% | −0.0045 to +0.0169 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.00706 | −17.7% | −0.0021 to −0.0009 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8513 | 0.856 | +0.6% | −0.0063 to +0.0157 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.9 | 795.5 | −0.8% | −19.9568 to +7.1832 | no |
| HPA replicas, mean | 8.1 | 8.262 | +2.0% | −0.1285 to +0.4525 | no |
| pods started | 3.9 | 4.8 | +23.1% | −0.6977 to +2.4977 | no |
| pod start wait, total (s) | 5.8 | 7.6 | +31.0% | −4.2207 to +7.8207 | no |
| pod start wait, mean (s) | 1.445 | 1.47 | +1.7% | −0.5291 to +0.5791 | no |
| host CPU busy, the real machine under kind (%) | 26.06 | 26.31 | +1.0% | −0.1917 to +0.6895 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.51 | −0.1% | −0.0074 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158 | −0.0% | −0.7789 to +0.7733 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158 | −0.0% | −0.7789 to +0.7733 | no |
| response time (ms), mean | 74.98 | 76.99 | +2.7% | −2.4929 to +6.5131 | no |
| response time (ms), 95th percentile | 112.3 | 118.4 | +5.5% | −8.7430 to +21.1010 | no |
| response time (ms), 99th percentile | 161.3 | 160.7 | −0.3% | −22.7885 to +21.6953 | no |
| time over the response line (% of samples) | 0 | 0.01235 | +0.012 (native is 0) | −0.0156 to +0.0403 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.1 | 16.9 | −6.6% | −4.4131 to +2.0131 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.11 | −17.5% | −0.2542 to +0.2075 | no |
| utilisation (used / allocatable) | 0.03511 | 0.03583 | +2.0% | −0.0010 to +0.0024 | no |
| CPU used (cores), mean | 0.8427 | 0.8598 | +2.0% | −0.0237 to +0.0579 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.0076 | −11.4% | −0.0013 to −0.0007 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8513 | 0.8674 | +1.9% | −0.0245 to +0.0567 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.9 | 793.6 | −1.0% | −29.9895 to +13.5289 | no |
| HPA replicas, mean | 8.1 | 7.122 | −12.1% | −1.6187 to −0.3367 | yes: GAIN |
| pods started | 3.9 | 3.4 | −12.8% | −1.7274 to +0.7274 | no |
| pod start wait, total (s) | 5.8 | 4.7 | −19.0% | −3.4712 to +1.2712 | no |
| pod start wait, mean (s) | 1.445 | 1.4 | −3.1% | −0.4602 to +0.3702 | no |
| host CPU busy, the real machine under kind (%) | 26.06 | 26.69 | +2.4% | −0.3912 to +1.6450 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | +0.0% | −0.0012 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158.1 | +0.1% | −0.1323 to +0.3681 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158.1 | +0.1% | −0.1323 to +0.3681 | no |
| response time (ms), mean | 74.98 | 74.96 | −0.0% | −0.6431 to +0.6153 | no |
| response time (ms), 95th percentile | 112.3 | 110.4 | −1.7% | −2.9018 to −0.8192 | yes: GAIN |
| response time (ms), 99th percentile | 161.3 | 150.9 | −6.4% | −19.9074 to −0.8916 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.1 | 17.4 | −3.9% | −4.4556 to +3.0556 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.05333 | −60.0% | −0.3012 to +0.1412 | no |
| utilisation (used / allocatable) | 0.03511 | 0.03521 | +0.3% | −0.0004 to +0.0006 | no |
| CPU used (cores), mean | 0.8427 | 0.8451 | +0.3% | −0.0098 to +0.0147 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.01376 | +60.4% | +0.0041 to +0.0063 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8513 | 0.8589 | +0.9% | −0.0052 to +0.0204 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.9 | 804.2 | +0.3% | −11.3792 to +16.1108 | no |
| HPA replicas, mean | 8.1 | 7.323 | −9.6% | −1.2284 to −0.3260 | yes: GAIN |
| pods started | 3.9 | 3.5 | −10.3% | −1.7146 to +0.9146 | no |
| pod start wait, total (s) | 5.8 | 5 | −13.8% | −3.8683 to +2.2683 | no |
| pod start wait, mean (s) | 1.445 | 1.42 | −1.7% | −0.5613 to +0.5113 | no |
| host CPU busy, the real machine under kind (%) | 26.06 | 26.25 | +0.7% | −0.2047 to +0.5815 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0005 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158.3 | +0.2% | −0.0068 to +0.5805 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158.3 | +0.2% | −0.0068 to +0.5805 | no |
| response time (ms), mean | 74.98 | 75.51 | +0.7% | −0.0854 to +1.1550 | no |
| response time (ms), 95th percentile | 112.3 | 112 | −0.2% | −2.0604 to +1.5664 | no |
| response time (ms), 99th percentile | 161.3 | 152.3 | −5.6% | −23.3136 to +5.2822 | no |
| time over the response line (% of samples) | 0 | 0.02424 | +0.024 (native is 0) | −0.0123 to +0.0608 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.1 | 20 | +10.5% | −0.0792 to +3.8792 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1617 | +21.2% | −0.2339 to +0.2906 | no |
| utilisation (used / allocatable) | 0.03511 | 0.03545 | +1.0% | −0.0001 to +0.0008 | no |
| CPU used (cores), mean | 0.8427 | 0.8508 | +1.0% | −0.0023 to +0.0185 | no |
| Omni's own CPU (cores), mean | 0.00858 | 0.02456 | +186.2% | +0.0136 to +0.0183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8513 | 0.8754 | +2.8% | +0.0134 to +0.0348 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.9 | 793.7 | −1.0% | −20.5376 to +4.1606 | no |
| HPA replicas, mean | 8.1 | 8.391 | +3.6% | +0.0069 to +0.5741 | yes: power given |
| pods started | 3.9 | 3.8 | −2.6% | −0.9564 to +0.7564 | no |
| pod start wait, total (s) | 5.8 | 5.6 | −3.4% | −1.4526 to +1.0526 | no |
| pod start wait, mean (s) | 1.445 | 1.433 | −0.8% | −0.3904 to +0.3671 | no |
| host CPU busy, the real machine under kind (%) | 26.06 | 26.88 | +3.1% | +0.3872 to +1.2438 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.514 | +0.2% | −0.0005 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 158.5 | +0.3% | +0.0248 to +0.8843 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 158.5 | +0.3% | +0.0248 to +0.8843 | yes: power given |
| response time (ms), mean | 74.98 | 76.54 | +2.1% | +0.4819 to +2.6446 | yes: LOSS |
| response time (ms), 95th percentile | 112.3 | 116 | +3.3% | +0.4606 to +7.0164 | yes: LOSS |
| response time (ms), 99th percentile | 161.3 | 156.1 | −3.2% | −18.2096 to +7.7616 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.1 | 19.9 | +9.9% | −1.0573 to +4.6573 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.2717 | +103.8% | −0.1917 to +0.4684 | no |
| utilisation (used / allocatable) | 0.03511 | 0.03602 | +2.6% | +0.0004 to +0.0014 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8427 | 0.8646 | +2.6% | +0.0106 to +0.0331 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00858 | 0.06751 | +686.8% | +0.0486 to +0.0692 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8513 | 0.9321 | +9.5% | +0.0600 to +0.1016 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.9 | 785.4 | −2.1% | −24.2397 to −8.7653 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.1 | 8.193 | +1.1% | −0.3308 to +0.5158 | no |
| pods started | 3.9 | 3.6 | −7.7% | −1.0578 to +0.4578 | no |
| pod start wait, total (s) | 5.8 | 5.5 | −5.2% | −1.7717 to +1.1717 | no |
| pod start wait, mean (s) | 1.445 | 1.437 | −0.6% | −0.3813 to +0.3647 | no |
| host CPU busy, the real machine under kind (%) | 26.06 | 28.6 | +9.7% | +1.7765 to +3.2891 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*