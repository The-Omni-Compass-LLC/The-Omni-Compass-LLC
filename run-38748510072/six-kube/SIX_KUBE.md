# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1382 | 1411 | 1913 | 1916 | 2013 | 1703 | 1628 | 1450 | 1645 | 1378 | 1356 | 1171 |
| response time (ms), 99th percentile | 4373 | 4385 | 5617 | 5609 | 5831 | 5398 | 4398 | 4252 | 3959 | 3920 | 4131 | 4041 |
| time over the response line (% of samples) | 23.49 | 17.32 | 20.54 | 14.84 | 20.97 | 14.89 | 24.65 | 17.63 | 24.08 | 17.48 | 21.92 | 15.76 |
| failed requests (%) | 9.884 | 8.854 | 7.11 | 6.223 | 6.843 | 6.122 | 8.092 | 7.449 | 9.885 | 8.235 | 9.666 | 8.145 |
| HPA replicas, mean | 9.646 | 12.19 | 9.63 | 13.46 | 9.65 | 13.62 | 9.562 | 13.2 | 9.585 | 12.31 | 9.617 | 11.96 |
| pods started | 5.22 | 10.37 | 5.049 | 9.561 | 4.756 | 9.659 | 5.512 | 9.537 | 5.122 | 9.927 | 5.293 | 9.512 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.9 | 181 | 180 | 181 | 180.2 | 180.8 | 180.5 | 179.9 | 180 | 180.2 | 180.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.9 | 181 | 180 | 181 | 180.2 | 180.8 | 180.5 | 179.9 | 180 | 180.2 | 180.3 |
| CPU used with Omni's own (cores), mean | 2.067 | 2.068 | 2.021 | 2.024 | 2.041 | 2.049 | 2.045 | 2.045 | 2.002 | 1.993 | 2.001 | 1.999 |
| host CPU busy, the real machine under kind (%) | 61.33 | 61.68 | 60.1 | 60.22 | 60.48 | 60.78 | 60.72 | 61.17 | 59.53 | 59.54 | 59.8 | 60.15 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1382 | 1411 | +2.1% | -184 to +243 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4373 | 4385 | +0.3% | -472.6 to +495.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 23.49 | 17.32 | -26.3% | -7.972 to -4.37 | GAIN |
| failed requests (%) | 9.884 | 8.854 | -10.4% | -1.753 to -0.3077 | GAIN |
| HPA replicas, mean | 9.646 | 12.19 | +26.4% | +1.968 to +3.128 | power given |
| pods started | 5.22 | 10.37 | +98.6% | +4.358 to +5.934 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.791e-16 to +2.624e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.9 | +0.1% | -0.2384 to +0.4986 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.9 | +0.1% | -0.2384 to +0.4986 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.067 | 2.068 | +0.0% | -0.01341 to +0.0139 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.33 | 61.68 | +0.6% | -0.02638 to +0.7404 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.146e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1913 | 1916 | +0.1% | -278.4 to +283.7 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5617 | 5609 | -0.1% | -331.8 to +316.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.54 | 14.84 | -27.8% | -6.879 to -4.526 | GAIN |
| failed requests (%) | 7.11 | 6.223 | -12.5% | -1.315 to -0.4599 | GAIN |
| HPA replicas, mean | 9.63 | 13.46 | +39.8% | +3.184 to +4.483 | power given |
| pods started | 5.049 | 9.561 | +89.4% | +3.646 to +5.378 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.593e-16 to +1.261e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180 | -0.5% | -1.345 to -0.5519 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180 | -0.5% | -1.345 to -0.5519 | GAIN |
| CPU used with Omni's own (cores), mean | 2.021 | 2.024 | +0.2% | -0.004581 to +0.01098 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.1 | 60.22 | +0.2% | -0.08413 to +0.3314 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2013 | 1703 | -15.4% | -536.4 to -84.15 | GAIN |
| response time (ms), 99th percentile | 5831 | 5398 | -7.4% | -819.7 to -46.5 | GAIN |
| time over the response line (% of samples) | 20.97 | 14.89 | -29.0% | -7.52 to -4.631 | GAIN |
| failed requests (%) | 6.843 | 6.122 | -10.5% | -1.341 to -0.1007 | GAIN |
| HPA replicas, mean | 9.65 | 13.62 | +41.1% | +3.398 to +4.534 | power given |
| pods started | 4.756 | 9.659 | +103.1% | +4.132 to +5.673 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.161e-16 to +4.027e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.2 | -0.4% | -1.207 to -0.4037 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.2 | -0.4% | -1.207 to -0.4037 | GAIN |
| CPU used with Omni's own (cores), mean | 2.041 | 2.049 | +0.4% | -0.004893 to +0.01985 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.48 | 60.78 | +0.5% | -0.004796 to +0.5997 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1628 | 1450 | -10.9% | -371 to +15.91 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4398 | 4252 | -3.3% | -489.4 to +196.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.65 | 17.63 | -28.5% | -8.903 to -5.126 | GAIN |
| failed requests (%) | 8.092 | 7.449 | -7.9% | -1.004 to -0.2806 | GAIN |
| HPA replicas, mean | 9.562 | 13.2 | +38.0% | +2.959 to +4.314 | power given |
| pods started | 5.512 | 9.537 | +73.0% | +3.237 to +4.812 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.373e-16 to +1.774e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.5 | -0.2% | -0.6661 to +0.1133 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.5 | -0.2% | -0.6661 to +0.1133 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.045 | 2.045 | +0.0% | -0.006964 to +0.007218 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.72 | 61.17 | +0.7% | +0.2176 to +0.6892 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1645 | 1378 | -16.2% | -480.6 to -52.9 | GAIN |
| response time (ms), 99th percentile | 3959 | 3920 | -1.0% | -431.8 to +352.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.08 | 17.48 | -27.4% | -8.716 to -4.475 | GAIN |
| failed requests (%) | 9.885 | 8.235 | -16.7% | -2.653 to -0.6461 | GAIN |
| HPA replicas, mean | 9.585 | 12.31 | +28.4% | +2.071 to +3.379 | power given |
| pods started | 5.122 | 9.927 | +93.8% | +3.936 to +5.674 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.489e-16 to +1.456e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180 | +0.0% | -0.2813 to +0.3432 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180 | +0.0% | -0.2813 to +0.3432 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.002 | 1.993 | -0.5% | -0.02142 to +0.002867 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.53 | 59.54 | +0.0% | -0.339 to +0.3508 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1356 | 1171 | -13.7% | -377.8 to +7.308 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4131 | 4041 | -2.2% | -550.3 to +371.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 21.92 | 15.76 | -28.1% | -8.016 to -4.302 | GAIN |
| failed requests (%) | 9.666 | 8.145 | -15.7% | -2.27 to -0.7727 | GAIN |
| HPA replicas, mean | 9.617 | 11.96 | +24.4% | +1.742 to +2.943 | power given |
| pods started | 5.293 | 9.512 | +79.7% | +3.388 to +5.051 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.111e-16 to +1.811e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 180.3 | +0.0% | -0.2932 to +0.4578 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 180.3 | +0.0% | -0.2932 to +0.4578 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.001 | 1.999 | -0.1% | -0.01289 to +0.009963 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.8 | 60.15 | +0.6% | -0.009704 to +0.7156 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
