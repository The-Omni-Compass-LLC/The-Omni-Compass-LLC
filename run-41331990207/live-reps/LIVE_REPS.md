# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.515 | 1.508 | 1.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160 | 158.3 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160 | 158.3 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 137.5 | 144.7 | 136.7 | 143.2 |
| response time (ms), 95th percentile | 282.4 | 291.8 | 270.3 | 287.2 |
| response time (ms), 99th percentile | 393.6 | 417.3 | 391.2 | 406.4 |
| time over the response line (% of samples) | 0.308 | 0.5547 | 0.3449 | 0.3218 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.4 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 2.1 | 2.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.02667 | 0.4283 | 0.19 |
| utilisation (used / allocatable) | 0.03786 | 0.04193 | 0.03788 | 0.0432 |
| CPU used (cores), mean | 0.9087 | 1.006 | 0.9091 | 1.037 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00634 | 0.01051 |
| CPU used with Omni's own (cores), mean | 0.9087 | 1.006 | 0.9154 | 1.047 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.6 | 631.3 | 694.6 | 614.1 |
| HPA replicas, mean | 8.985 | 8.858 | 9.982 | 10.08 |
| pods started | 4.5 | 5 | 6.8 | 7.3 |
| pod start wait, total (s) | 6.3 | 7.3 | 10 | 12.5 |
| pod start wait, mean (s) | 1.37 | 1.455 | 1.438 | 1.691 |
| host CPU busy, the real machine under kind (%) | 27.41 | 30.91 | 27.72 | 32.34 |
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

Omni-Compass stayed native in 3 of 10 repetitions (repetitions 2, 3, 4): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.508 | −0.5% | −0.0146 to −0.0007 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 159.4 | −0.3% | −1.2779 to +0.2009 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 159.4 | −0.3% | −1.2779 to +0.2009 | no |
| response time (ms), mean | 144.7 | 143.2 | −1.0% | −4.3158 to +1.3561 | no |
| response time (ms), 95th percentile | 291.8 | 287.2 | −1.6% | −14.1519 to +5.0639 | no |
| response time (ms), 99th percentile | 417.3 | 406.4 | −2.6% | −34.3961 to +12.5719 | no |
| time over the response line (% of samples) | 0.5547 | 0.3218 | −42.0% | −0.4821 to +0.0162 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0.1 | −75.0% | −0.6455 to +0.0455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.1 | +2.100 (native is 0) | +0.7746 to +3.4254 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.19 | +612.5% | −0.0453 to +0.3719 | no |
| utilisation (used / allocatable) | 0.04193 | 0.0432 | +3.0% | +0.0007 to +0.0019 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.006 | 1.037 | +3.0% | +0.0157 to +0.0453 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01051 | +0.011 (native is 0) | +0.0088 to +0.0122 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 1.047 | +4.1% | +0.0254 to +0.0567 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.3 | 614.1 | −2.7% | −24.8347 to −9.5044 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.858 | 10.08 | +13.8% | +0.6024 to +1.8373 | yes: power given |
| pods started | 5 | 7.3 | +46.0% | +1.0361 to +3.5639 | yes: power given |
| pod start wait, total (s) | 7.3 | 12.5 | +71.2% | +2.3828 to +8.0172 | yes: LOSS |
| pod start wait, mean (s) | 1.455 | 1.691 | +16.2% | +0.0065 to +0.4656 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.91 | 32.34 | +4.6% | +0.9174 to +1.9427 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0070 to +0.0113 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160 | +0.7% | +0.1811 to +2.1679 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160 | +0.7% | +0.1811 to +2.1679 | yes: power given |
| response time (ms), mean | 137.5 | 144.7 | +5.2% | +3.9710 to +10.3666 | yes: LOSS |
| response time (ms), 95th percentile | 282.4 | 291.8 | +3.3% | +2.2879 to +16.4371 | yes: LOSS |
| response time (ms), 99th percentile | 393.6 | 417.3 | +6.0% | +3.2042 to +44.3676 | yes: LOSS |
| time over the response line (% of samples) | 0.308 | 0.5547 | +80.1% | −0.0236 to +0.5170 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.02667 | −92.4% | −0.6064 to −0.0403 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03786 | 0.04193 | +10.7% | +0.0034 to +0.0047 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9087 | 1.006 | +10.7% | +0.0821 to +0.1131 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9087 | 1.006 | +10.7% | +0.0821 to +0.1131 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.6 | 631.3 | −9.1% | −71.8966 to −54.8069 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.985 | 8.858 | −1.4% | −0.2556 to +0.0027 | no |
| pods started | 4.5 | 5 | +11.1% | −0.1952 to +1.1952 | no |
| pod start wait, total (s) | 6.3 | 7.3 | +15.9% | −1.2112 to +3.2112 | no |
| pod start wait, mean (s) | 1.37 | 1.455 | +6.2% | −0.2458 to +0.4158 | no |
| host CPU busy, the real machine under kind (%) | 27.41 | 30.91 | +12.7% | +2.9182 to +4.0716 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.508 | −0.3% | −0.0117 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.3 | −0.3% | −1.1997 to +0.2603 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.3 | −0.3% | −1.1997 to +0.2603 | no |
| response time (ms), mean | 137.5 | 136.7 | −0.6% | −4.0915 to +2.5270 | no |
| response time (ms), 95th percentile | 282.4 | 270.3 | −4.3% | −25.8520 to +1.6730 | no |
| response time (ms), 99th percentile | 393.6 | 391.2 | −0.6% | −24.2118 to +19.4220 | no |
| time over the response line (% of samples) | 0.308 | 0.3449 | +12.0% | −0.1247 to +0.1985 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.1 | +2.100 (native is 0) | +0.5023 to +3.6977 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.4283 | +22.4% | −0.3040 to +0.4607 | no |
| utilisation (used / allocatable) | 0.03786 | 0.03788 | +0.0% | −0.0007 to +0.0007 | no |
| CPU used (cores), mean | 0.9087 | 0.9091 | +0.0% | −0.0162 to +0.0170 | no |
| Omni's own CPU (cores), mean | 0 | 0.00634 | +0.006 (native is 0) | +0.0055 to +0.0072 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9087 | 0.9154 | +0.7% | −0.0100 to +0.0234 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.6 | 694.6 | +0.0% | −12.4157 to +12.4336 | no |
| HPA replicas, mean | 8.985 | 9.982 | +11.1% | +0.2534 to +1.7408 | yes: power given |
| pods started | 4.5 | 6.8 | +51.1% | +0.7529 to +3.8471 | yes: power given |
| pod start wait, total (s) | 6.3 | 10 | +58.7% | +0.7983 to +6.6017 | yes: LOSS |
| pod start wait, mean (s) | 1.37 | 1.438 | +4.9% | −0.2729 to +0.4080 | no |
| host CPU busy, the real machine under kind (%) | 27.41 | 27.72 | +1.1% | −0.2335 to +0.8554 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.508 | −0.5% | −0.0157 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 158.3 | −1.0% | −2.6033 to −0.6851 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 158.3 | −1.0% | −2.6033 to −0.6851 | yes: GAIN |
| response time (ms), mean | 144.7 | 136.7 | −5.5% | −12.7355 to −3.1665 | yes: GAIN |
| response time (ms), 95th percentile | 291.8 | 270.3 | −7.4% | −36.8721 to −6.0319 | yes: GAIN |
| response time (ms), 99th percentile | 417.3 | 391.2 | −6.3% | −53.5998 to +1.2382 | no |
| time over the response line (% of samples) | 0.5547 | 0.3449 | −37.8% | −0.4887 to +0.0692 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0.1 | −75.0% | −0.8889 to +0.2889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.1 | +2.100 (native is 0) | +0.5023 to +3.6977 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.4283 | +1506.3% | +0.0626 to +0.7408 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04193 | 0.03788 | −9.7% | −0.0046 to −0.0035 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.006 | 0.9091 | −9.7% | −0.1103 to −0.0842 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00634 | +0.006 (native is 0) | +0.0055 to +0.0072 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 0.9154 | −9.0% | −0.1037 to −0.0781 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.3 | 694.6 | +10.0% | +55.1663 to +71.5551 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.858 | 9.982 | +12.7% | +0.3980 to +1.8490 | yes: power given |
| pods started | 5 | 6.8 | +36.0% | +0.1208 to +3.4792 | yes: power given |
| pod start wait, total (s) | 7.3 | 10 | +37.0% | −0.4097 to +5.8097 | no |
| pod start wait, mean (s) | 1.455 | 1.438 | −1.2% | −0.2728 to +0.2379 | no |
| host CPU busy, the real machine under kind (%) | 30.91 | 27.72 | −10.3% | −3.4905 to −2.8774 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.508 | −0.4% | −0.0123 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.4 | +0.4% | −0.1220 to +1.3940 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.4 | +0.4% | −0.1220 to +1.3940 | no |
| response time (ms), mean | 137.5 | 143.2 | +4.1% | +3.3085 to +8.0694 | yes: LOSS |
| response time (ms), 95th percentile | 282.4 | 287.2 | +1.7% | −3.3414 to +12.9784 | no |
| response time (ms), 99th percentile | 393.6 | 406.4 | +3.3% | −0.5119 to +26.2595 | no |
| time over the response line (% of samples) | 0.308 | 0.3218 | +4.5% | −0.0872 to +0.1147 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.1 | +2.100 (native is 0) | +0.7746 to +3.4254 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.19 | −45.7% | −0.4509 to +0.1309 | no |
| utilisation (used / allocatable) | 0.03786 | 0.0432 | +14.1% | +0.0047 to +0.0060 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9087 | 1.037 | +14.1% | +0.1134 to +0.1429 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01051 | +0.011 (native is 0) | +0.0088 to +0.0122 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9087 | 1.047 | +15.3% | +0.1224 to +0.1549 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.6 | 614.1 | −11.6% | −85.5688 to −75.4738 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.985 | 10.08 | +12.2% | +0.4359 to +1.7509 | yes: power given |
| pods started | 4.5 | 7.3 | +62.2% | +1.8583 to +3.7417 | yes: power given |
| pod start wait, total (s) | 6.3 | 12.5 | +98.4% | +3.8687 to +8.5313 | yes: LOSS |
| pod start wait, mean (s) | 1.37 | 1.691 | +23.4% | +0.0732 to +0.5689 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 27.41 | 32.34 | +18.0% | +4.2986 to +5.5513 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*