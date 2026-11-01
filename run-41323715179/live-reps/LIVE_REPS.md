# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.332 | 5.296 |
| node-hours | 2.515 | 2.518 | 2.235 | 2.221 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 | 273.7 | 273.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 274 | 252.7 | 251.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 424.3 | 429 | 379.9 | 404.1 |
| response time (ms), 95th percentile | 1581 | 1579 | 1596 | 1696 |
| response time (ms), 99th percentile | 2187 | 2264 | 2206 | 2277 |
| time over the response line (% of samples) | 19.1 | 19.83 | 18.58 | 19.02 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10 | 9.9 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 31.5 | 41.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.89 | 10.56 | 10.19 | 11.39 |
| utilisation (used / allocatable) | 0.06377 | 0.06322 | 0.07182 | 0.07222 |
| CPU used (cores), mean | 1.531 | 1.517 | 1.521 | 1.519 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01674 | 0.01805 |
| CPU used with Omni's own (cores), mean | 1.531 | 1.517 | 1.538 | 1.537 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.5 | 439.9 | 399.1 | 398.9 |
| HPA replicas, mean | 1.957 | 1.974 | 2.003 | 2.128 |
| pods started | 0 | 0.1 | 0.1 | 0.3 |
| pod start wait, total (s) | 0 | 0.2 | 0.1 | 0.5 |
| pod start wait, mean (s) | 0 | 0.2 | 0.1 | 0.5 |
| host CPU busy, the real machine under kind (%) | 43.59 | 44.21 | 44.51 | 45.22 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806 | 811.7 | 808.9 | 818.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.8 | 4.687 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2083 | 0.0625 | 0.6958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | 0.4 | 4 |
| queue: job turnaround, submitted to done, mean (s) | 111.8 | 117.1 | 114.1 | 122.8 |
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
| worker nodes in service, mean | 6 | 5.296 | −11.7% | −1.3254 to −0.0824 | yes: GAIN |
| node-hours | 2.518 | 2.221 | −11.8% | −0.5558 to −0.0390 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.7 | −0.1% | −1.0549 to +0.5545 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 251.6 | −8.2% | −41.8466 to −2.9414 | yes: GAIN |
| response time (ms), mean | 429 | 404.1 | −5.8% | −50.2206 to +0.3605 | no |
| response time (ms), 95th percentile | 1579 | 1696 | +7.4% | −46.4712 to +279.9802 | no |
| response time (ms), 99th percentile | 2264 | 2277 | +0.6% | −47.2073 to +73.5939 | no |
| time over the response line (% of samples) | 19.83 | 19.02 | −4.1% | −1.9617 to +0.3294 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.1 | +1.0% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.700 (native is 0) | +19.5241 to +63.8759 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.56 | 11.39 | +7.9% | −2.0073 to +3.6673 | no |
| utilisation (used / allocatable) | 0.06322 | 0.07222 | +14.2% | +0.0007 to +0.0173 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.517 | 1.519 | +0.1% | −0.0177 to +0.0213 | no |
| Omni's own CPU (cores), mean | 0 | 0.01805 | +0.018 (native is 0) | +0.0166 to +0.0195 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 1.537 | +1.3% | −0.0000 to +0.0397 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.9 | 398.9 | −9.3% | −81.0332 to −0.8426 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.974 | 2.128 | +7.8% | +0.0141 to +0.2924 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | −0.5294 to +1.1294 | no |
| pod start wait, mean (s) | 0.2 | 0.5 | +150.0% | −0.5294 to +1.1294 | no |
| host CPU busy, the real machine under kind (%) | 44.21 | 45.22 | +2.3% | +0.5228 to +1.4954 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.7 | 818.3 | +0.8% | −2.5864 to +15.7864 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.687 | −21.9% | −2.3465 to −0.2803 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2083 | 0.6958 | +234.0% | −0.3746 to +1.3496 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 4 | +400.0% | −4.0462 to +10.4462 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.1 | 122.8 | +4.8% | −2.8177 to +14.1677 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.518 | +0.1% | −0.0064 to +0.0131 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 | +0.1% | −1.0005 to +1.3364 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 274 | +0.1% | −1.0005 to +1.3364 | no |
| response time (ms), mean | 424.3 | 429 | +1.1% | −7.7657 to +17.0485 | no |
| response time (ms), 95th percentile | 1581 | 1579 | −0.1% | −63.1954 to +59.3334 | no |
| response time (ms), 99th percentile | 2187 | 2264 | +3.5% | −19.0808 to +174.0848 | no |
| time over the response line (% of samples) | 19.1 | 19.83 | +3.8% | −0.6383 to +2.1054 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10 | +3.1% | −0.9181 to +1.5181 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.89 | 10.56 | −11.2% | −3.2424 to +0.5724 | no |
| utilisation (used / allocatable) | 0.06377 | 0.06322 | −0.9% | −0.0015 to +0.0004 | no |
| CPU used (cores), mean | 1.531 | 1.517 | −0.9% | −0.0357 to +0.0090 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.531 | 1.517 | −0.9% | −0.0357 to +0.0090 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.5 | 439.9 | +1.0% | −2.9551 to +11.6918 | no |
| HPA replicas, mean | 1.957 | 1.974 | +0.9% | −0.1806 to +0.2144 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 43.59 | 44.21 | +1.4% | +0.3910 to +0.8632 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 811.7 | +0.7% | +0.1280 to +11.2720 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2083 | +150.0% | +0.0257 to +0.2243 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 111.8 | 117.1 | +4.7% | +0.9482 to +9.6435 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.332 | −11.1% | −1.3293 to −0.0062 | yes: GAIN |
| node-hours | 2.515 | 2.235 | −11.1% | −0.5597 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.7 | −0.1% | −1.0919 to +0.8087 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 252.7 | −7.7% | −42.3258 to +0.1218 | no |
| response time (ms), mean | 424.3 | 379.9 | −10.5% | −60.2412 to −28.6563 | yes: GAIN |
| response time (ms), 95th percentile | 1581 | 1596 | +0.9% | −56.6669 to +86.0209 | no |
| response time (ms), 99th percentile | 2187 | 2206 | +0.9% | −110.1567 to +148.0623 | no |
| time over the response line (% of samples) | 19.1 | 18.58 | −2.7% | −1.3872 to +0.3547 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.9 | +2.1% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.5 | +31.500 (native is 0) | +16.4909 to +46.5091 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.89 | 10.19 | −14.3% | −4.0766 to +0.6732 | no |
| utilisation (used / allocatable) | 0.06377 | 0.07182 | +12.6% | −0.0007 to +0.0168 | no |
| CPU used (cores), mean | 1.531 | 1.521 | −0.6% | −0.0383 to +0.0193 | no |
| Omni's own CPU (cores), mean | 0 | 0.01674 | +0.017 (native is 0) | +0.0157 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.531 | 1.538 | +0.5% | −0.0212 to +0.0357 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.5 | 399.1 | −8.4% | −74.9796 to +2.2456 | no |
| HPA replicas, mean | 1.957 | 2.003 | +2.3% | −0.1315 to +0.2224 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 43.59 | 44.51 | +2.1% | +0.6598 to +1.1931 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 808.9 | +0.4% | −2.0380 to +7.8380 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.8 | −20.0% | −2.3311 to −0.0695 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.0625 | −25.0% | −0.0955 to +0.0538 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | −20.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 111.8 | 114.1 | +2.1% | −1.5766 to +6.1849 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.332 | −11.1% | −1.3293 to −0.0062 | yes: GAIN |
| node-hours | 2.518 | 2.235 | −11.2% | −0.5592 to −0.0068 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.7 | −0.1% | −1.3308 to +0.7118 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 252.7 | −7.8% | −41.9404 to −0.5995 | yes: GAIN |
| response time (ms), mean | 429 | 379.9 | −11.4% | −63.5572 to −34.6230 | yes: GAIN |
| response time (ms), 95th percentile | 1579 | 1596 | +1.1% | −70.6950 to +103.9110 | no |
| response time (ms), 99th percentile | 2264 | 2206 | −2.6% | −134.4436 to +17.3452 | no |
| time over the response line (% of samples) | 19.83 | 18.58 | −6.3% | −2.4065 to −0.0930 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.9 | −1.0% | −0.9564 to +0.7564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.5 | +31.500 (native is 0) | +16.4909 to +46.5091 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.56 | 10.19 | −3.5% | −2.0590 to +1.3256 | no |
| utilisation (used / allocatable) | 0.06322 | 0.07182 | +13.6% | −0.0006 to +0.0178 | no |
| CPU used (cores), mean | 1.517 | 1.521 | +0.3% | −0.0192 to +0.0269 | no |
| Omni's own CPU (cores), mean | 0 | 0.01674 | +0.017 (native is 0) | +0.0157 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 1.538 | +1.4% | −0.0020 to +0.0432 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.9 | 399.1 | −9.3% | −83.8775 to +2.4068 | no |
| HPA replicas, mean | 1.974 | 2.003 | +1.4% | −0.1612 to +0.2182 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 44.21 | 44.51 | +0.7% | +0.0329 to +0.5658 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.7 | 808.9 | −0.3% | −7.6608 to +2.0608 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.8 | −20.0% | −2.3311 to −0.0695 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2083 | 0.0625 | −70.0% | −0.2106 to −0.0811 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.4 | −50.0% | −0.7694 to −0.0306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 117.1 | 114.1 | −2.6% | −6.0684 to +0.0851 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.296 | −11.7% | −1.3254 to −0.0824 | yes: GAIN |
| node-hours | 2.515 | 2.221 | −11.7% | −0.5571 to −0.0310 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.7 | −0.0% | −1.0096 to +0.8450 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 251.6 | −8.1% | −42.2639 to −2.1881 | yes: GAIN |
| response time (ms), mean | 424.3 | 404.1 | −4.8% | −45.2851 to +4.7077 | no |
| response time (ms), 95th percentile | 1581 | 1696 | +7.3% | −19.6392 to +249.2862 | no |
| response time (ms), 99th percentile | 2187 | 2277 | +4.1% | −11.7978 to +193.1884 | no |
| time over the response line (% of samples) | 19.1 | 19.02 | −0.4% | −1.0826 to +0.9174 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.1 | +4.1% | −0.8707 to +1.6707 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.700 (native is 0) | +19.5241 to +63.8759 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.89 | 11.39 | −4.2% | −2.9751 to +1.9651 | no |
| utilisation (used / allocatable) | 0.06377 | 0.07222 | +13.2% | +0.0004 to +0.0165 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.531 | 1.519 | −0.8% | −0.0358 to +0.0127 | no |
| Omni's own CPU (cores), mean | 0 | 0.01805 | +0.018 (native is 0) | +0.0166 to +0.0195 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.531 | 1.537 | +0.4% | −0.0182 to +0.0313 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.5 | 398.9 | −8.4% | −73.1784 to +0.0393 | no |
| HPA replicas, mean | 1.957 | 2.128 | +8.7% | −0.0750 to +0.4154 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| host CPU busy, the real machine under kind (%) | 43.59 | 45.22 | +3.8% | +1.1835 to +2.0888 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 818.3 | +1.5% | +1.1161 to +23.4839 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.687 | −21.9% | −2.3465 to −0.2803 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.6958 | +735.0% | −0.2077 to +1.4327 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 4 | +700.0% | −3.6789 to +10.6789 | no |
| queue: job turnaround, submitted to done, mean (s) | 111.8 | 122.8 | +9.8% | +1.0502 to +20.8914 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*