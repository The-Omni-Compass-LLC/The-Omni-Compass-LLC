# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1889 | 2209 | 2213 | 3133 | 2213 | 2396 | 2275 | 2063 | 2486 | 2404 | 3321 | 5146 | 1561 | 3725 |
| response time (ms), 99th percentile | 3926 | 4467 | 4479 | 6041 | 4626 | 4869 | 4277 | 4441 | 4737 | 4993 | 5659 | 7028 | 3628 | 5771 |
| time over the response line (% of samples) | 41.27 | 36.85 | 43.55 | 38.26 | 40.1 | 36.06 | 35.71 | 31.27 | 44.2 | 39.4 | 56.66 | 53.7 | 42.64 | 42.07 |
| failed requests (%) | 28.1 | 27.69 | 22.27 | 20.48 | 26.93 | 26.26 | 22.19 | 21.97 | 27.85 | 26.35 | 39.13 | 34.91 | 25.04 | 22.91 |
| HPA replicas, mean | 9.641 | 11.62 | 9.649 | 13.81 | 9.65 | 11.47 | 9.602 | 11.34 | 9.637 | 12.27 | 9.748 | 13.5 | 9.721 | 12.39 |
| pods started | 4.829 | 7.771 | 5.343 | 9.371 | 4.629 | 6.543 | 5.143 | 6.971 | 5.171 | 7.857 | 3.657 | 7.543 | 3.971 | 6.743 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 6 | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 184 | 184.6 | 185.1 | 183 | 183.7 | 182.9 | 183.4 | 183.5 | 183.9 | 184.8 | 185.2 | 183.5 | 184.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 184 | 184.6 | 185.1 | 183 | 183.7 | 182.9 | 183.4 | 183.5 | 183.9 | 184.8 | 185.2 | 183.5 | 184.1 |
| CPU used with Omni's own (cores), mean | 2.32 | 2.32 | 2.411 | 2.426 | 2.297 | 2.305 | 2.252 | 2.262 | 2.328 | 2.333 | 2.457 | 2.464 | 2.342 | 2.362 |
| host CPU busy, the real machine under kind (%) | 68.69 | 69.3 | 70.85 | 71.9 | 68.27 | 68.96 | 66.99 | 67.88 | 68.38 | 69.43 | 73.29 | 74.85 | 70.45 | 73.51 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.02 | 0.02571 | 0.002857 | 0.008571 | 0.005714 | 0.01143 | 0.008571 | 0.008571 | 0.1 | 0.2457 | 0.1657 | 0.18 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1889 | 2209 | +16.9% | -170.7 to +809.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3926 | 4467 | +13.8% | -268.5 to +1352 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 41.27 | 36.85 | -10.7% | -6.134 to -2.708 | GAIN |
| failed requests (%) | 28.1 | 27.69 | -1.4% | -1.269 to +0.4568 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.641 | 11.62 | +20.6% | +1.202 to +2.764 | power given |
| pods started | 4.829 | 7.771 | +60.9% | +1.727 to +4.158 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.721e-16 to +1.631e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 184 | +0.4% | +0.2674 to +1.132 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 184 | +0.4% | +0.2674 to +1.132 | power given |
| CPU used with Omni's own (cores), mean | 2.32 | 2.32 | +0.0% | -0.01447 to +0.01554 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.69 | 69.3 | +0.9% | +0.2585 to +0.959 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2213 | 3133 | +41.6% | +514.1 to +1327 | LOSS |
| response time (ms), 99th percentile | 4479 | 6041 | +34.9% | +795.3 to +2330 | LOSS |
| time over the response line (% of samples) | 43.55 | 38.26 | -12.1% | -6.618 to -3.965 | GAIN |
| failed requests (%) | 22.27 | 20.48 | -8.0% | -2.672 to -0.9028 | GAIN |
| HPA replicas, mean | 9.649 | 13.81 | +43.1% | +3.465 to +4.849 | power given |
| pods started | 5.343 | 9.371 | +75.4% | +3.258 to +4.799 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0005162 to +0.001517 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 185.1 | +0.2% | -0.08809 to +0.9818 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 185.1 | +0.2% | -0.07917 to +0.9931 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.411 | 2.426 | +0.6% | +0.002177 to +0.02767 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.85 | 71.9 | +1.5% | +0.6477 to +1.453 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.02571 | +28.6% | -0.01459 to +0.02602 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2213 | 2396 | +8.3% | -361.6 to +727.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4626 | 4869 | +5.3% | -519.2 to +1006 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.1 | 36.06 | -10.1% | -5.829 to -2.26 | GAIN |
| failed requests (%) | 26.93 | 26.26 | -2.5% | -1.425 to +0.0823 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.65 | 11.47 | +18.8% | +0.991 to +2.645 | power given |
| pods started | 4.629 | 6.543 | +41.4% | +0.7893 to +3.039 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004555 to +0.00155 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.7 | +0.4% | +0.2425 to +1.041 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.7 | +0.3% | +0.2124 to +1.01 | power given |
| CPU used with Omni's own (cores), mean | 2.297 | 2.305 | +0.4% | +0.001714 to +0.01493 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.27 | 68.96 | +1.0% | +0.4684 to +0.9178 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2275 | 2063 | -9.3% | -693 to +270 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4277 | 4441 | +3.8% | -463.5 to +792.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 35.71 | 31.27 | -12.4% | -5.921 to -2.955 | GAIN |
| failed requests (%) | 22.19 | 21.97 | -1.0% | -1.039 to +0.5899 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.602 | 11.34 | +18.1% | +0.9194 to +2.562 | power given |
| pods started | 5.143 | 6.971 | +35.6% | +0.7667 to +2.89 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.702e-16 to +3.18e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.4 | +0.3% | +0.01404 to +1.018 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.4 | +0.3% | +0.01404 to +1.018 | power given |
| CPU used with Omni's own (cores), mean | 2.252 | 2.262 | +0.5% | +0.0001734 to +0.02121 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.99 | 67.88 | +1.3% | +0.505 to +1.28 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.005714 | 0.01143 | +100.0% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2486 | 2404 | -3.3% | -606.4 to +443.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4737 | 4993 | +5.4% | -388.5 to +899.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.2 | 39.4 | -10.9% | -6.808 to -2.792 | GAIN |
| failed requests (%) | 27.85 | 26.35 | -5.4% | -2.408 to -0.6 | GAIN |
| HPA replicas, mean | 9.637 | 12.27 | +27.4% | +1.742 to +3.532 | power given |
| pods started | 5.171 | 7.857 | +51.9% | +1.42 to +3.951 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.957e-16 to +3.419e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.9 | +0.2% | -0.09002 to +0.87 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.9 | +0.2% | -0.09002 to +0.87 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.328 | 2.333 | +0.2% | -0.006606 to +0.01655 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.38 | 69.43 | +1.5% | +0.7065 to +1.395 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3321 | 5146 | +54.9% | +1108 to +2542 | LOSS |
| response time (ms), 99th percentile | 5659 | 7028 | +24.2% | +641.2 to +2096 | LOSS |
| time over the response line (% of samples) | 56.66 | 53.7 | -5.2% | -4.293 to -1.631 | GAIN |
| failed requests (%) | 39.13 | 34.91 | -10.8% | -5.605 to -2.844 | GAIN |
| HPA replicas, mean | 9.748 | 13.5 | +38.5% | +3.14 to +4.359 | power given |
| pods started | 3.657 | 7.543 | +106.2% | +3.037 to +4.734 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.885e-16 to +5.93e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.2 | +0.2% | -0.1704 to +0.8296 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.2 | +0.2% | -0.1704 to +0.8296 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.457 | 2.464 | +0.3% | +0.0007433 to +0.01378 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.29 | 74.85 | +2.1% | +1.396 to +1.706 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2457 | +145.7% | +0.1189 to +0.1725 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1561 | 3725 | +138.5% | +1417 to +2909 | LOSS |
| response time (ms), 99th percentile | 3628 | 5771 | +59.1% | +1353 to +2933 | LOSS |
| time over the response line (% of samples) | 42.64 | 42.07 | -1.3% | -2.117 to +0.9855 | STEADY, inside the noise (cut) |
| failed requests (%) | 25.04 | 22.91 | -8.5% | -3.263 to -0.9984 | GAIN |
| HPA replicas, mean | 9.721 | 12.39 | +27.5% | +2.003 to +3.345 | power given |
| pods started | 3.971 | 6.743 | +69.8% | +1.905 to +3.637 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.988e-16 to +6.556e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.1 | +0.3% | +0.09912 to +1.11 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.1 | +0.3% | +0.09912 to +1.11 | power given |
| CPU used with Omni's own (cores), mean | 2.342 | 2.362 | +0.9% | +0.007354 to +0.03311 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.45 | 73.51 | +4.3% | +2.648 to +3.457 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1657 | 0.18 | +8.6% | -0.01813 to +0.0467 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
