# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1814 | 1123 | 1291 | 724.2 | 1638 | 1066 | 1270 | 730.9 | 2330 | 1448 | 1680 | 973.3 |
| response time (ms), 99th percentile | 4981 | 3646 | 3481 | 3322 | 5594 | 5489 | 3311 | 2074 | 4912 | 3790 | 4658 | 4683 |
| time over the response line (% of samples) | 31.8 | 16.61 | 19.34 | 9.583 | 28.25 | 13.93 | 17.07 | 9.16 | 37.88 | 19.35 | 32.62 | 16.69 |
| failed requests (%) | 9.995 | 8.51 | 5.441 | 4.878 | 8.348 | 7.257 | 4.154 | 3.696 | 10.66 | 8.862 | 10.54 | 8.999 |
| HPA replicas, mean | 9.728 | 9.73 | 9.684 | 9.716 | 9.799 | 9.845 | 9.498 | 9.504 | 9.784 | 9.814 | 9.773 | 9.816 |
| pods started | 4 | 3.7 | 4.7 | 4.4 | 3.5 | 2.5 | 5.5 | 5.7 | 3.1 | 2.6 | 3.6 | 2.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 187.3 | 186.8 | 182.3 | 182.1 | 186.8 | 186.3 | 180.7 | 180.1 | 188.8 | 188.2 | 187.8 | 187.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.3 | 186.8 | 182.3 | 182.1 | 186.8 | 186.3 | 180.7 | 180.1 | 188.8 | 188.2 | 187.8 | 187.7 |
| CPU used with Omni's own (cores), mean | 2.664 | 2.61 | 2.196 | 2.16 | 2.625 | 2.586 | 2.047 | 2.013 | 2.816 | 2.76 | 2.691 | 2.654 |
| host CPU busy, the real machine under kind (%) | 77.31 | 76.08 | 64.86 | 64 | 76.29 | 75.51 | 60.62 | 59.72 | 81.05 | 79.95 | 78.45 | 77.96 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.01 | 0 | 0 | 0.03 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1814 | 1123 | -38.1% | -1010 to -373.1 | better |
| response time (ms), 99th percentile | 4981 | 3646 | -26.8% | -2277 to -391.5 | better |
| time over the response line (% of samples) | 31.8 | 16.61 | -47.8% | -20.59 to -9.787 | better |
| failed requests (%) | 9.995 | 8.51 | -14.9% | -2.47 to -0.5004 | better |
| HPA replicas, mean | 9.728 | 9.73 | +0.0% | -0.1106 to +0.1152 | WORSE (inside the noise) |
| pods started | 4 | 3.7 | -7.5% | -1.733 to +1.133 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 187.3 | 186.8 | -0.3% | -1.091 to +0.08178 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.3 | 186.8 | -0.3% | -1.091 to +0.08178 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.664 | 2.61 | -2.0% | -0.09278 to -0.01537 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 77.31 | 76.08 | -1.6% | -2.023 to -0.4224 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001007 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 2, worse on 2 (organism energy (J); organism work per energy), inside the noise on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1291 | 724.2 | -43.9% | -1309 to +174.7 | better (inside the noise) |
| response time (ms), 99th percentile | 3481 | 3322 | -4.6% | -1219 to +902.3 | better (inside the noise) |
| time over the response line (% of samples) | 19.34 | 9.583 | -50.4% | -15.41 to -4.097 | better |
| failed requests (%) | 5.441 | 4.878 | -10.3% | -2.257 to +1.131 | better (inside the noise) |
| HPA replicas, mean | 9.684 | 9.716 | +0.3% | -0.01907 to +0.08288 | WORSE (inside the noise) |
| pods started | 4.7 | 4.4 | -6.4% | -1.058 to +0.4578 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.661e-15 to +4.179e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.1 | -0.1% | -0.7768 to +0.3504 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.1 | -0.1% | -0.7768 to +0.3504 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.196 | 2.16 | -1.7% | -0.07443 to +0.001688 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 64.86 | 64 | -1.3% | -1.852 to +0.1183 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1638 | 1066 | -35.0% | -990.5 to -155.1 | better |
| response time (ms), 99th percentile | 5594 | 5489 | -1.9% | -1071 to +860.7 | better (inside the noise) |
| time over the response line (% of samples) | 28.25 | 13.93 | -50.7% | -18.92 to -9.714 | better |
| failed requests (%) | 8.348 | 7.257 | -13.1% | -2.294 to +0.113 | better (inside the noise) |
| HPA replicas, mean | 9.799 | 9.845 | +0.5% | -0.002271 to +0.09455 | WORSE (inside the noise) |
| pods started | 3.5 | 2.5 | -28.6% | -1.826 to -0.174 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.159e-15 to +4.484e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.8 | 186.3 | -0.3% | -1.026 to -0.003656 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.8 | 186.3 | -0.3% | -1.026 to -0.003656 | better |
| CPU used with Omni's own (cores), mean | 2.625 | 2.586 | -1.5% | -0.07974 to +0.002247 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 76.29 | 75.51 | -1.0% | -1.612 to +0.03588 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1270 | 730.9 | -42.5% | -829.5 to -249.2 | better |
| response time (ms), 99th percentile | 3311 | 2074 | -37.4% | -2152 to -321.6 | better |
| time over the response line (% of samples) | 17.07 | 9.16 | -46.3% | -13.82 to -2.004 | better |
| failed requests (%) | 4.154 | 3.696 | -11.0% | -1.204 to +0.2899 | better (inside the noise) |
| HPA replicas, mean | 9.498 | 9.504 | +0.1% | -0.05178 to +0.06338 | WORSE (inside the noise) |
| pods started | 5.5 | 5.7 | +3.6% | -0.6793 to +1.079 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.304e-15 to +4.161e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.1 | -0.3% | -1.098 to +0.0107 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.1 | -0.3% | -1.098 to +0.0107 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.047 | 2.013 | -1.7% | -0.06275 to -0.005959 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 60.62 | 59.72 | -1.5% | -1.644 to -0.169 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2330 | 1448 | -37.9% | -1263 to -502.8 | better |
| response time (ms), 99th percentile | 4912 | 3790 | -22.8% | -2423 to +179.6 | better (inside the noise) |
| time over the response line (% of samples) | 37.88 | 19.35 | -48.9% | -25 to -12.07 | better |
| failed requests (%) | 10.66 | 8.862 | -16.9% | -3.415 to -0.188 | better |
| HPA replicas, mean | 9.784 | 9.814 | +0.3% | -0.02579 to +0.08565 | WORSE (inside the noise) |
| pods started | 3.1 | 2.6 | -16.1% | -1.58 to +0.5796 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.264e-15 to +5.531e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.8 | 188.2 | -0.3% | -1.117 to -0.1326 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.8 | 188.2 | -0.3% | -1.117 to -0.1326 | better |
| CPU used with Omni's own (cores), mean | 2.816 | 2.76 | -2.0% | -0.09206 to -0.01976 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.05 | 79.95 | -1.4% | -1.962 to -0.2373 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1680 | 973.3 | -42.1% | -1065 to -348.6 | better |
| response time (ms), 99th percentile | 4658 | 4683 | +0.5% | -664.8 to +713.7 | WORSE (inside the noise) |
| time over the response line (% of samples) | 32.62 | 16.69 | -48.8% | -20.86 to -11 | better |
| failed requests (%) | 10.54 | 8.999 | -14.7% | -2.813 to -0.2768 | better |
| HPA replicas, mean | 9.773 | 9.816 | +0.4% | -0.01018 to +0.09578 | WORSE (inside the noise) |
| pods started | 3.6 | 2.9 | -19.4% | -1.821 to +0.4209 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.865e-16 to +1.575e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.8 | 187.7 | -0.1% | -1.004 to +0.8102 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.8 | 187.7 | -0.1% | -1.004 to +0.8102 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.691 | 2.654 | -1.4% | -0.08605 to +0.01127 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.45 | 77.96 | -0.6% | -1.496 to +0.5186 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.231e+07 to +4.233e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.275e-08 to -5.273e-08 | WORSE |
| organism behind its window (s) | 0 | 0.03 | +0.03 | -0.004553 to +0.06455 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
