# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2049 | 1186 | 2553 | 1518 | 2123 | 858.9 | 2895 | 1970 | 2429 | 1706 | 1526 | 936.4 |
| response time (ms), 99th percentile | 4382 | 3763 | 6716 | 7180 | 5849 | 5229 | 6216 | 5042 | 5538 | 4492 | 3994 | 2654 |
| time over the response line (% of samples) | 35.48 | 18.67 | 35.35 | 17.03 | 26.65 | 12.35 | 43.85 | 23.47 | 40.81 | 22.89 | 28.33 | 14.81 |
| failed requests (%) | 11.59 | 9.587 | 9.029 | 7.941 | 6.772 | 6.068 | 12.6 | 11.48 | 11.37 | 10.66 | 9.071 | 7.819 |
| HPA replicas, mean | 9.87 | 9.834 | 9.853 | 9.884 | 9.79 | 9.796 | 9.793 | 9.849 | 9.752 | 9.813 | 9.756 | 9.714 |
| pods started | 2 | 2.75 | 2.75 | 2.125 | 3.375 | 3.625 | 2.75 | 2 | 3.375 | 2.125 | 3.375 | 4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 188.5 | 188.3 | 188.8 | 188.5 | 185.7 | 185.4 | 190.2 | 190.1 | 188.9 | 188.5 | 186 | 185.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.5 | 188.3 | 188.8 | 188.5 | 185.7 | 185.4 | 190.2 | 190.1 | 188.9 | 188.5 | 186 | 185.5 |
| CPU used with Omni's own (cores), mean | 2.775 | 2.753 | 2.845 | 2.824 | 2.558 | 2.494 | 2.975 | 2.944 | 2.811 | 2.788 | 2.506 | 2.468 |
| host CPU busy, the real machine under kind (%) | 81.01 | 80.62 | 82.77 | 82.1 | 74.37 | 73.1 | 85.47 | 85.47 | 81.48 | 80.8 | 73.75 | 72.92 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0125 | 0 | 0.025 | 0.0125 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2049 | 1186 | -42.1% | -1474 to -252.7 | better |
| response time (ms), 99th percentile | 4382 | 3763 | -14.1% | -1656 to +417.7 | better (inside the noise) |
| time over the response line (% of samples) | 35.48 | 18.67 | -47.4% | -22.75 to -10.86 | better |
| failed requests (%) | 11.59 | 9.587 | -17.3% | -3.194 to -0.82 | better |
| HPA replicas, mean | 9.87 | 9.834 | -0.4% | -0.09369 to +0.02084 | better (inside the noise) |
| pods started | 2 | 2.75 | +37.5% | -0.4112 to +1.911 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.108e-15 to +1.331e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.5 | 188.3 | -0.1% | -0.8194 to +0.4863 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.5 | 188.3 | -0.1% | -0.8194 to +0.4863 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.775 | 2.753 | -0.8% | -0.05212 to +0.007769 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.01 | 80.62 | -0.5% | -1.011 to +0.2301 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001007 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2553 | 1518 | -40.5% | -1697 to -372.5 | better |
| response time (ms), 99th percentile | 6716 | 7180 | +6.9% | -746.6 to +1674 | WORSE (inside the noise) |
| time over the response line (% of samples) | 35.35 | 17.03 | -51.8% | -22.81 to -13.83 | better |
| failed requests (%) | 9.029 | 7.941 | -12.0% | -2.169 to -0.00573 | better |
| HPA replicas, mean | 9.853 | 9.884 | +0.3% | -0.03235 to +0.09348 | WORSE (inside the noise) |
| pods started | 2.75 | 2.125 | -22.7% | -1.884 to +0.6342 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.05e-15 to +1.05e-15 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 188.8 | 188.5 | -0.2% | -1.603 to +1.01 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.8 | 188.5 | -0.2% | -1.603 to +1.01 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.845 | 2.824 | -0.7% | -0.05705 to +0.01456 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 82.77 | 82.1 | -0.8% | -1.728 to +0.3734 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2123 | 858.9 | -59.5% | -1995 to -532.2 | better |
| response time (ms), 99th percentile | 5849 | 5229 | -10.6% | -1840 to +599.8 | better (inside the noise) |
| time over the response line (% of samples) | 26.65 | 12.35 | -53.7% | -19.92 to -8.684 | better |
| failed requests (%) | 6.772 | 6.068 | -10.4% | -1.207 to -0.201 | better |
| HPA replicas, mean | 9.79 | 9.796 | +0.1% | -0.0587 to +0.07059 | WORSE (inside the noise) |
| pods started | 3.375 | 3.625 | +7.4% | -0.8217 to +1.322 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.856e-16 to +2.195e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 185.4 | -0.2% | -1.268 to +0.5684 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 185.4 | -0.2% | -1.268 to +0.5684 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.558 | 2.494 | -2.5% | -0.1269 to -0.0007838 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.37 | 73.1 | -1.7% | -2.942 to +0.3982 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2895 | 1970 | -32.0% | -1443 to -407.9 | better |
| response time (ms), 99th percentile | 6216 | 5042 | -18.9% | -1777 to -572 | better |
| time over the response line (% of samples) | 43.85 | 23.47 | -46.5% | -27.27 to -13.5 | better |
| failed requests (%) | 12.6 | 11.48 | -8.9% | -1.907 to -0.3392 | better |
| HPA replicas, mean | 9.793 | 9.849 | +0.6% | -0.02725 to +0.1397 | WORSE (inside the noise) |
| pods started | 2.75 | 2 | -27.3% | -1.911 to +0.4112 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.462e-15 to +1.017e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.2 | 190.1 | -0.0% | -0.6825 to +0.5434 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.2 | 190.1 | -0.0% | -0.6825 to +0.5434 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.975 | 2.944 | -1.0% | -0.06149 to -0.0008536 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.47 | 85.47 | -0.0% | -0.7721 to +0.7691 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2429 | 1706 | -29.8% | -1184 to -262.8 | better |
| response time (ms), 99th percentile | 5538 | 4492 | -18.9% | -2305 to +213.7 | better (inside the noise) |
| time over the response line (% of samples) | 40.81 | 22.89 | -43.9% | -24.99 to -10.84 | better |
| failed requests (%) | 11.37 | 10.66 | -6.2% | -2.465 to +1.057 | better (inside the noise) |
| HPA replicas, mean | 9.752 | 9.813 | +0.6% | -0.005358 to +0.1273 | WORSE (inside the noise) |
| pods started | 3.375 | 2.125 | -37.0% | -2.322 to -0.1783 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.47e-16 to +6.25e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.9 | 188.5 | -0.2% | -1.567 to +0.7659 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.9 | 188.5 | -0.2% | -1.567 to +0.7659 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.811 | 2.788 | -0.8% | -0.07619 to +0.02905 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.48 | 80.8 | -0.8% | -2.054 to +0.695 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0.0125 | 0 | -100.0% | -0.04206 to +0.01706 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1526 | 936.4 | -38.6% | -927.9 to -250.9 | better |
| response time (ms), 99th percentile | 3994 | 2654 | -33.5% | -2532 to -147.9 | better |
| time over the response line (% of samples) | 28.33 | 14.81 | -47.7% | -20.78 to -6.251 | better |
| failed requests (%) | 9.071 | 7.819 | -13.8% | -2.28 to -0.2248 | better |
| HPA replicas, mean | 9.756 | 9.714 | -0.4% | -0.1124 to +0.0284 | better (inside the noise) |
| pods started | 3.375 | 4 | +18.5% | -0.4641 to +1.714 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.327e-15 to +8.831e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 185.5 | -0.3% | -1.599 to +0.4801 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 185.5 | -0.3% | -1.599 to +0.4801 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.506 | 2.468 | -1.5% | -0.06687 to -0.008981 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.75 | 72.92 | -1.1% | -1.616 to -0.03076 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.231e+07 to +4.233e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.275e-08 to -5.273e-08 | WORSE |
| organism behind its window (s) | 0.025 | 0.0125 | -50.0% | -0.06609 to +0.04109 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
