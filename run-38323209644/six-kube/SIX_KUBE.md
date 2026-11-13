# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1641 | 851.1 | 2193 | 1446 | 1876 | 1133 | 1931 | 1167 | 1905 | 1227 | 1600 | 928.1 |
| response time (ms), 99th percentile | 4063 | 3359 | 5248 | 4407 | 4376 | 3681 | 4717 | 3819 | 4313 | 3634 | 4180 | 3127 |
| time over the response line (% of samples) | 28.61 | 15.66 | 24.67 | 12.32 | 21.14 | 9.662 | 31.11 | 15.91 | 31.6 | 17.14 | 27.83 | 15.26 |
| failed requests (%) | 10.04 | 8.662 | 5.421 | 4.565 | 4.057 | 3.645 | 7.917 | 6.922 | 9.324 | 7.879 | 9.065 | 8 |
| HPA replicas, mean | 9.699 | 9.677 | 9.689 | 9.698 | 9.654 | 9.675 | 9.671 | 9.682 | 9.707 | 9.663 | 9.728 | 9.731 |
| pods started | 3.976 | 4.39 | 3.854 | 3.585 | 4.39 | 4.171 | 4.073 | 3.927 | 3.707 | 3.951 | 3.659 | 3.878 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 185.3 | 183.7 | 183.4 | 182.5 | 182.2 | 186.1 | 185.8 | 186.4 | 185.9 | 185.7 | 185.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 185.3 | 183.7 | 183.4 | 182.5 | 182.2 | 186.1 | 185.8 | 186.4 | 185.9 | 185.7 | 185.4 |
| CPU used with Omni's own (cores), mean | 2.472 | 2.444 | 2.366 | 2.326 | 2.259 | 2.217 | 2.553 | 2.516 | 2.562 | 2.535 | 2.485 | 2.464 |
| host CPU busy, the real machine under kind (%) | 72.11 | 71.66 | 69.09 | 68.12 | 66.06 | 65.19 | 74.16 | 73.56 | 74.72 | 74.14 | 73.06 | 72.58 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.597e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.927 | 4.251 | 4.179 | 1.42 | 1.364 | 2.303 | 2.264 | 2.431 | 2.407 | 2.401 | 2.347 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.004878 | 0.002439 | 0.01463 | 0.02683 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1641 | 851.1 | -48.1% | -972.4 to -606.8 | better |
| response time (ms), 99th percentile | 4063 | 3359 | -17.3% | -1091 to -315.4 | better |
| time over the response line (% of samples) | 28.61 | 15.66 | -45.3% | -15.74 to -10.16 | better |
| failed requests (%) | 10.04 | 8.662 | -13.7% | -2.047 to -0.7108 | better |
| HPA replicas, mean | 9.699 | 9.677 | -0.2% | -0.05242 to +0.009099 | better (inside the noise) |
| pods started | 3.976 | 4.39 | +10.4% | -0.08355 to +0.9128 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.38e-16 to +4.846e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 185.3 | -0.1% | -0.5341 to +0.01824 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 185.3 | -0.1% | -0.5341 to +0.01824 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.472 | 2.444 | -1.1% | -0.04249 to -0.01293 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.11 | 71.66 | -0.6% | -0.822 to -0.07792 | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +6.835e+06 to +6.835e+06 | WORSE |
| organism time over the line (% of steps) | 1.976 | 1.927 | -2.5% | -0.04938 to -0.04938 | better |
| organism work per energy | 1.404 | 1.403 | -0.0% | -0.0006456 to -0.0006455 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2193 | 1446 | -34.1% | -956.3 to -537.5 | better |
| response time (ms), 99th percentile | 5248 | 4407 | -16.0% | -1128 to -555.2 | better |
| time over the response line (% of samples) | 24.67 | 12.32 | -50.1% | -14.75 to -9.944 | better |
| failed requests (%) | 5.421 | 4.565 | -15.8% | -1.231 to -0.482 | better |
| HPA replicas, mean | 9.689 | 9.698 | +0.1% | -0.02098 to +0.04017 | WORSE (inside the noise) |
| pods started | 3.854 | 3.585 | -7.0% | -0.803 to +0.2664 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.715e-16 to +2.115e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.4 | -0.2% | -0.6928 to -0.007069 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.4 | -0.2% | -0.6928 to -0.007069 | better |
| CPU used with Omni's own (cores), mean | 2.366 | 2.326 | -1.7% | -0.05429 to -0.02632 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.09 | 68.12 | -1.4% | -1.392 to -0.5534 | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +9.059e+06 to +9.059e+06 | WORSE |
| organism time over the line (% of steps) | 4.251 | 4.179 | -1.7% | -0.07219 to -0.07219 | better |
| organism work per energy | 1.125 | 1.124 | -0.0% | -0.0005302 to -0.0005302 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 7, worse on 0, inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1876 | 1133 | -39.6% | -939.8 to -546.1 | better |
| response time (ms), 99th percentile | 4376 | 3681 | -15.9% | -1077 to -313.2 | better |
| time over the response line (% of samples) | 21.14 | 9.662 | -54.3% | -13.58 to -9.381 | better |
| failed requests (%) | 4.057 | 3.645 | -10.2% | -0.726 to -0.09811 | better |
| HPA replicas, mean | 9.654 | 9.675 | +0.2% | -0.01013 to +0.05145 | WORSE (inside the noise) |
| pods started | 4.39 | 4.171 | -5.0% | -0.7295 to +0.2905 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.912e-16 to +3.345e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.2 | -0.2% | -0.5149 to -0.1012 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.2 | -0.2% | -0.5149 to -0.1012 | better |
| CPU used with Omni's own (cores), mean | 2.259 | 2.217 | -1.9% | -0.05621 to -0.02846 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 66.06 | 65.19 | -1.3% | -1.238 to -0.5124 | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +6.914e+06 to +6.914e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.364 | -4.0% | -0.05642 to -0.05642 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -4.494e-09 to -4.494e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1931 | 1167 | -39.5% | -958.5 to -568.6 | better |
| response time (ms), 99th percentile | 4717 | 3819 | -19.0% | -1288 to -507.7 | better |
| time over the response line (% of samples) | 31.11 | 15.91 | -48.8% | -18.06 to -12.34 | better |
| failed requests (%) | 7.917 | 6.922 | -12.6% | -1.362 to -0.6281 | better |
| HPA replicas, mean | 9.671 | 9.682 | +0.1% | -0.01404 to +0.03677 | WORSE (inside the noise) |
| pods started | 4.073 | 3.927 | -3.6% | -0.5247 to +0.232 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.222e-16 to +3.955e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.1 | 185.8 | -0.2% | -0.6342 to -0.07588 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.1 | 185.8 | -0.2% | -0.6342 to -0.07588 | better |
| CPU used with Omni's own (cores), mean | 2.553 | 2.516 | -1.5% | -0.0497 to -0.02503 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.16 | 73.56 | -0.8% | -0.9212 to -0.2899 | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.597e+10 | +0.0% | +6.376e+06 to +6.376e+06 | WORSE |
| organism time over the line (% of steps) | 2.303 | 2.264 | -1.7% | -0.03874 to -0.03874 | better |
| organism work per energy | 0.382 | 0.382 | -0.0% | -4.352e-05 to -4.352e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 7, worse on 0, inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1905 | 1227 | -35.6% | -848.3 to -509.7 | better |
| response time (ms), 99th percentile | 4313 | 3634 | -15.8% | -1173 to -185.4 | better |
| time over the response line (% of samples) | 31.6 | 17.14 | -45.7% | -16.97 to -11.94 | better |
| failed requests (%) | 9.324 | 7.879 | -15.5% | -2.185 to -0.706 | better |
| HPA replicas, mean | 9.707 | 9.663 | -0.4% | -0.09333 to +0.006743 | better (inside the noise) |
| pods started | 3.707 | 3.951 | +6.6% | -0.2192 to +0.707 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.752e-16 to +4.785e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.4 | 185.9 | -0.3% | -0.8008 to -0.1813 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.4 | 185.9 | -0.3% | -0.8008 to -0.1813 | better |
| CPU used with Omni's own (cores), mean | 2.562 | 2.535 | -1.1% | -0.04161 to -0.01251 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.72 | 74.14 | -0.8% | -0.982 to -0.1772 | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +6.908e+06 to +6.908e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.407 | -1.0% | -0.02447 to -0.02447 | better |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -4.601e-09 to -4.601e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.004878 | 0.002439 | -50.0% | -0.01079 to +0.00591 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1600 | 928.1 | -42.0% | -812 to -532.3 | better |
| response time (ms), 99th percentile | 4180 | 3127 | -25.2% | -1393 to -713.9 | better |
| time over the response line (% of samples) | 27.83 | 15.26 | -45.2% | -14.89 to -10.25 | better |
| failed requests (%) | 9.065 | 8 | -11.7% | -1.498 to -0.6316 | better |
| HPA replicas, mean | 9.728 | 9.731 | +0.0% | -0.01974 to +0.0266 | WORSE (inside the noise) |
| pods started | 3.659 | 3.878 | +6.0% | -0.2215 to +0.6605 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.741e-16 to +2.574e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 185.4 | -0.2% | -0.6987 to +0.03016 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 185.4 | -0.2% | -0.6987 to +0.03016 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.485 | 2.464 | -0.9% | -0.03457 to -0.008474 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.06 | 72.58 | -0.7% | -0.82 to -0.1451 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +2.918e+07 to +2.918e+07 | WORSE |
| organism time over the line (% of steps) | 2.401 | 2.347 | -2.2% | -0.05328 to -0.05328 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -3.637e-08 to -3.637e-08 | WORSE |
| organism behind its window (s) | 0.01463 | 0.02683 | +83.3% | -0.004841 to +0.02923 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
