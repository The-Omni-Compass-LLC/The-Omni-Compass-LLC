# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Source: GitHub Actions workflow `six-kube`, run 37359815637, commit `a004a8f` (Omni v1 for everything but the power grid: 37 of 38 v1 files, the power-grid runner not yet written, `tools/omni_version.py --commit a004a8f`), 2026-10-05/06; raw files under `results/live/raw/run-37359815637/`; 98 of 100 cells (1, 10 and 100 copies of all six organisms, 1,000 copies of the four realms and the tower; the two 1,000-copy stack cells cut off by GitHub's six-hour job limit). Made by `tools/six_kube_report.py`.


Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`). The aim is lower for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). The aim is higher for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni | Compute / AI / Cloud, 1,000 copies: native | Compute / AI / Cloud, 1,000 copies: omni | Physics / Robotics / Autonomous, 1,000 copies: native | Physics / Robotics / Autonomous, 1,000 copies: omni | Energy / Facility / Industrial, 1,000 copies: native | Energy / Facility / Industrial, 1,000 copies: omni | Distribution / Specialized, 1,000 copies: native | Distribution / Specialized, 1,000 copies: omni | The whole tower, every muscle once, 1,000 copies: native | The whole tower, every muscle once, 1,000 copies: omni | The four stacked, duplicates kept, 1,000 copies: native | The four stacked, duplicates kept, 1,000 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4983 | 3758 | 3054 | 2501 | 1173 | 620.3 | 2089 | 1928 | 4109 | 2389 | 3416 | 2168 | 5025 | 2781 | 3994 | 2667 | 2891 | 2568 | 3539 | 2514 | 2978 | 2188 | 2263 | 2122 | 5209 | 3492 | 2714 | 1935 | 3178 | 2631 | 3160 | 1666 | 2856 | 3213 | 3842 | 2496 | 2141 | 826.6 | 2734 | 3516 | 3398 | 4005 | 2183 | 2906 | 2915 | 3198 | 2244 | 1253 |
| response time (ms), 99th percentile | 8095 | 7695 | 6227 | 5759 | 2367 | 1563 | 4905 | 4430 | 7848 | 6863 | 5069 | 4152 | 7340 | 5274 | 6606 | 6626 | 4937 | 4627 | 6784 | 5142 | 4948 | 5307 | 3829 | 3401 | 8017 | 6544 | 3968 | 3302 | 6002 | 5325 | 4486 | 3925 | 4358 | 4840 | 5942 | 4244 | 3009 | 2757 | 5491 | 5166 | 6055 | 7405 | 4756 | 4241 | 4945 | 5166 | 2923 | 2055 |
| time over the response line (% of samples) | 49.41 | 37.11 | 36.26 | 21.24 | 13.41 | 5.162 | 28.12 | 14.96 | 56.37 | 38.5 | 39.97 | 35.75 | 76.55 | 66.48 | 57.08 | 44.57 | 44.49 | 35.66 | 56.42 | 44.19 | 61.19 | 50.68 | 27.65 | 19.08 | 75.74 | 64.51 | 36.73 | 29.76 | 63.6 | 56.7 | 49.56 | 43.87 | 47.28 | 44.86 | 60.01 | 47.71 | 28.51 | 26.16 | 55.68 | 50.74 | 82.16 | 77.69 | 55.02 | 52.32 | 58.12 | 51.41 | 44.15 | 22.43 |
| failed requests (%) | 20.47 | 19.87 | 6.756 | 6.367 | 1.867 | 1.619 | 8.062 | 6.478 | 27.44 | 25.35 | 28.21 | 28.35 | 54.99 | 52.22 | 35.63 | 32.63 | 26.69 | 26.62 | 34 | 31.77 | 42.87 | 40.9 | 13.91 | 11.98 | 55.04 | 52.1 | 25.11 | 24.21 | 49.88 | 46.9 | 38.87 | 37.19 | 39.09 | 36.86 | 42.13 | 39 | 22.92 | 23.03 | 45.47 | 42.37 | 69.44 | 69.43 | 46.77 | 45.76 | 48.68 | 43.37 | 32.46 | 0 |
| HPA replicas, mean | 9.864 | 9.908 | 9.801 | 9.844 | 9.609 | 9.581 | 9.646 | 9.723 | 9.864 | 9.852 | 9.561 | 9.615 | 9.93 | 9.896 | 9.809 | 9.854 | 9.668 | 9.685 | 9.764 | 9.83 | 9.833 | 9.793 | 9.603 | 9.607 | 9.895 | 9.906 | 9.762 | 9.758 | 9.881 | 9.887 | 9.829 | 9.821 | 9.809 | 9.782 | 9.769 | 9.777 | 9.823 | 9.815 | 9.865 | 9.863 | 9.895 | 9.9 | 9.861 | 9.864 | 9.855 | 9.857 | 9.854 | 9.795 |
| pods started | 2 | 1.4 | 3 | 2.4 | 5 | 5.6 | 4.6 | 3.2 | 2.2 | 2.2 | 5 | 4.4 | 1.2 | 1.8 | 2.8 | 1.8 | 4.8 | 4 | 3.6 | 3 | 2.6 | 3.2 | 5.6 | 5.6 | 2.6 | 2.4 | 4.4 | 4.8 | 2.6 | 2.2 | 3.4 | 3.4 | 3.8 | 4.6 | 5.2 | 5.2 | 6.333 | 6 | 5.333 | 5.333 | 4.667 | 4.333 | 5 | 5.333 | 5.667 | 5.667 | 6 | 6.5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.935 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 193.4 | 192.9 | 188.1 | 188.1 | 181.4 | 180.4 | 184.5 | 184.3 | 192.4 | 191.5 | 185 | 185.1 | 194.1 | 194.1 | 190.1 | 190.5 | 188.4 | 188.3 | 192.1 | 192 | 192.6 | 192.8 | 185 | 184.2 | 290.5 | 289.9 | 279.5 | 278.2 | 285.8 | 284.6 | 281.9 | 280.7 | 281.6 | 279.7 | 282.7 | 281.6 | 549.6 | 545.8 | 558.6 | 555.5 | 571.2 | 565.5 | 559.4 | 557.5 | 557.8 | 557.9 | 558.6 | 556.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193.4 | 192.9 | 188.1 | 188.1 | 181.4 | 179.1 | 184.5 | 184.3 | 192.4 | 191.5 | 185 | 185.1 | 194.1 | 194.1 | 190.1 | 190.5 | 188.4 | 188.3 | 192.1 | 192 | 192.6 | 192.8 | 185 | 184.2 | 290.5 | 289.9 | 279.5 | 278.2 | 285.8 | 284.6 | 281.9 | 280.7 | 281.6 | 279.7 | 282.7 | 281.6 | 549.6 | 545.8 | 558.6 | 555.5 | 571.2 | 565.5 | 559.4 | 557.5 | 557.8 | 557.9 | 558.6 | 556.1 |
| CPU used with Omni's own (cores), mean | 3.198 | 3.187 | 2.779 | 2.731 | 2.09 | 2.015 | 2.387 | 2.352 | 3.242 | 3.216 | 2.566 | 2.535 | 3.425 | 3.399 | 3.021 | 3.003 | 2.804 | 2.756 | 3.186 | 3.146 | 3.213 | 3.159 | 2.415 | 2.369 | 3.375 | 3.347 | 2.608 | 2.536 | 3.052 | 3.028 | 2.754 | 2.745 | 2.773 | 2.698 | 2.883 | 2.783 | 2.342 | 2.245 | 2.655 | 2.587 | 3.069 | 2.93 | 2.701 | 2.641 | 2.659 | 2.659 | 2.685 | 2.595 |
| host CPU busy, the real machine under kind (%) | 91.64 | 91.91 | 80.2 | 79.57 | 61.48 | 59.91 | 69.9 | 69.15 | 93.72 | 93.47 | 73.57 | 73.22 | 97.95 | 97.95 | 87.43 | 87.42 | 81.14 | 80.14 | 91.16 | 90.61 | 92.66 | 91.71 | 70.51 | 69.85 | 97.86 | 98.05 | 76.64 | 74.99 | 88.89 | 89.42 | 81.09 | 81.29 | 83.81 | 83.24 | 89.26 | 89.18 | 73.92 | 73.61 | 86.17 | 86.75 | 98.75 | 98.94 | 86.04 | 87.07 | 91.02 | 92.77 | 95.14 | 93.61 |
| organism work | 1.675e+10 | 1.675e+10 | 1.665e+10 | 1.665e+10 | 5.708e+10 | 5.708e+10 | 1.674e+10 | 1.674e+10 | 5.728e+10 | 5.728e+10 | 1.075e+11 | 1.075e+11 | 1.73e+11 | 1.73e+11 | 1.719e+11 | 1.719e+11 | 5.605e+11 | 5.605e+11 | 1.729e+11 | 1.729e+11 | 5.625e+11 | 5.625e+11 | 1.065e+12 | 1.065e+12 | 1.692e+12 | 1.692e+12 | 1.682e+12 | 1.682e+12 | 5.621e+12 | 5.621e+12 | 1.691e+12 | 1.691e+12 | 5.641e+12 | 5.641e+12 | 1.067e+13 | 1.067e+13 | 1.69e+13 | 1.69e+13 | 1.68e+13 | 1.68e+13 | 5.609e+13 | 5.609e+13 | 1.69e+13 | 1.69e+13 | 5.629e+13 | 5.629e+13 | 1.067e+14 | 1.067e+14 |
| organism energy (J) | 1.129e+10 | 1.128e+10 | 1.097e+10 | 1.096e+10 | 6.237e+10 | 6.225e+10 | 1.114e+10 | 1.113e+10 | 6.473e+10 | 6.461e+10 | 9.862e+10 | 9.847e+10 | 1.2e+11 | 1.199e+11 | 1.167e+11 | 1.166e+11 | 6.18e+11 | 6.168e+11 | 1.187e+11 | 1.185e+11 | 6.411e+11 | 6.399e+11 | 9.668e+11 | 9.653e+11 | 1.17e+12 | 1.169e+12 | 1.14e+12 | 1.139e+12 | 6.163e+12 | 6.151e+12 | 1.157e+12 | 1.156e+12 | 6.396e+12 | 6.385e+12 | 9.618e+12 | 9.603e+12 | 1.169e+13 | 1.168e+13 | 1.14e+13 | 1.138e+13 | 6.153e+13 | 6.141e+13 | 1.157e+13 | 1.156e+13 | 6.387e+13 | 6.375e+13 | 9.605e+13 | 9.59e+13 |
| organism time over the line (% of steps) | 2.087 | 2.06 | 3.515 | 3.499 | 1.667 | 1.633 | 2.37 | 2.35 | 2.546 | 2.532 | 2.535 | 2.513 | 2.187 | 2.17 | 4.118 | 4.104 | 1.83 | 1.796 | 2.55 | 2.531 | 2.846 | 2.836 | 2.579 | 2.554 | 2.126 | 2.11 | 3.895 | 3.884 | 1.836 | 1.803 | 2.518 | 2.501 | 2.698 | 2.689 | 2.568 | 2.545 | 2.095 | 2.079 | 3.944 | 3.937 | 1.811 | 1.781 | 2.502 | 2.486 | 2.722 | 2.714 | 2.568 | 2.546 |
| organism work per energy | 1.484 | 1.486 | 1.518 | 1.519 | 0.9151 | 0.9169 | 1.503 | 1.505 | 0.8849 | 0.8866 | 1.09 | 1.092 | 1.441 | 1.443 | 1.473 | 1.475 | 0.907 | 0.9087 | 1.457 | 1.459 | 0.8774 | 0.879 | 1.102 | 1.104 | 1.446 | 1.447 | 1.475 | 1.476 | 0.9121 | 0.9138 | 1.462 | 1.463 | 0.8819 | 0.8835 | 1.11 | 1.112 | 1.446 | 1.447 | 1.474 | 1.476 | 0.9116 | 0.9133 | 1.461 | 1.462 | 0.8814 | 0.883 | 1.111 | 1.112 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.04 | 0.02 | 0.02 | 0 | 0 | 0.02 | 0.04 | 0.04 | 0.06 | 0.08 | 0.1 | 0.1 | 1.4 | 0.7 | 0.6 | 0.58 | 0.4 | 0.44 | 0.66 | 0.8 | 1.26 | 1.32 | 2.72 | 2.64 | 6.3 | 5.667 | 6 | 154.8 | 7.233 | 42.4 | 7.067 | 8.933 | 1508 | 2418 | 2949 | 3307 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: toward their aims on 4, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4983 | 3758 | -24.6% | -2454 to +2.637 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 8095 | 7695 | -4.9% | -1768 to +967.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 49.41 | 37.11 | -24.9% | -16.61 to -7.995 | GAIN |
| failed requests (%) | 20.47 | 19.87 | -2.9% | -4.334 to +3.133 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.864 | 9.908 | +0.4% | -0.1019 to +0.1894 | STEADY, inside the noise (up) |
| pods started | 2 | 1.4 | -30.0% | -3.174 to +1.974 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.26e-15 to +1.615e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 193.4 | 192.9 | -0.3% | -1.843 to +0.8715 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193.4 | 192.9 | -0.3% | -1.843 to +0.8715 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.198 | 3.187 | -0.3% | -0.05306 to +0.03163 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 91.64 | 91.91 | +0.3% | -0.913 to +1.436 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.675e+10 | 1.675e+10 | +0.0% | +1312 to +1312 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.129e+10 | 1.128e+10 | -0.1% | -1.195e+07 to -1.195e+07 | GAIN |
| organism time over the line (% of steps) | 2.087 | 2.06 | -1.3% | -0.02657 to -0.02657 | GAIN |
| organism work per energy | 1.484 | 1.486 | +0.1% | +0.001573 to +0.001573 | GAIN |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: toward their aims on 4, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3054 | 2501 | -18.1% | -1314 to +207.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6227 | 5759 | -7.5% | -1532 to +595.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 36.26 | 21.24 | -41.4% | -22.93 to -7.111 | GAIN |
| failed requests (%) | 6.756 | 6.367 | -5.8% | -1.301 to +0.5219 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.801 | 9.844 | +0.4% | -0.1394 to +0.2249 | STEADY, inside the noise (up) |
| pods started | 3 | 2.4 | -20.0% | -4.283 to +3.083 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.612e-15 to +9.019e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.1 | 188.1 | +0.0% | -0.8611 to +0.8746 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.1 | 188.1 | +0.0% | -0.8611 to +0.8746 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.779 | 2.731 | -1.7% | -0.08819 to -0.008504 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 80.2 | 79.57 | -0.8% | -1.387 to +0.13 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.665e+10 | 1.665e+10 | +0.0% | +1310 to +1310 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.097e+10 | 1.096e+10 | -0.1% | -1.184e+07 to -1.184e+07 | GAIN |
| organism time over the line (% of steps) | 3.515 | 3.499 | -0.5% | -0.0159 to -0.0159 | GAIN |
| organism work per energy | 1.518 | 1.519 | +0.1% | +0.001639 to +0.00164 | GAIN |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: toward their aims on 6, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1173 | 620.3 | -47.1% | -1053 to -52.78 | GAIN |
| response time (ms), 99th percentile | 2367 | 1563 | -34.0% | -1453 to -156 | GAIN |
| time over the response line (% of samples) | 13.41 | 5.162 | -61.5% | -14.99 to -1.499 | GAIN |
| failed requests (%) | 1.867 | 1.619 | -13.3% | -0.935 to +0.4398 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.609 | 9.581 | -0.3% | -0.1569 to +0.101 | STEADY, inside the noise (cut) |
| pods started | 5 | 5.6 | +12.0% | -0.5104 to +1.71 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.935 | -1.1% | -0.2444 to +0.115 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.4 | -0.5% | -2.388 to +0.4414 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 179.1 | -1.3% | -5.224 to +0.6775 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.09 | 2.015 | -3.6% | -0.1385 to -0.0115 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 61.48 | 59.91 | -2.5% | -3.338 to +0.2039 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.708e+10 | 5.708e+10 | +0.0% | +1312 to +1312 | STEADY, the same (under one part in a million) |
| organism energy (J) | 6.237e+10 | 6.225e+10 | -0.2% | -1.242e+08 to -1.242e+08 | GAIN |
| organism time over the line (% of steps) | 1.667 | 1.633 | -2.0% | -0.03398 to -0.03398 | GAIN |
| organism work per energy | 0.9151 | 0.9169 | +0.2% | +0.001825 to +0.001826 | GAIN |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: toward their aims on 3, away from them on 0, inside the noise on 8

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2089 | 1928 | -7.7% | -877.3 to +554.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4905 | 4430 | -9.7% | -2675 to +1725 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 28.12 | 14.96 | -46.8% | -27.68 to +1.358 | STEADY, inside the noise (cut) |
| failed requests (%) | 8.062 | 6.478 | -19.7% | -3.411 to +0.2408 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.646 | 9.723 | +0.8% | -0.1388 to +0.2922 | STEADY, inside the noise (up) |
| pods started | 4.6 | 3.2 | -30.4% | -4.39 to +1.59 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.79e-15 to +7.243e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.3 | -0.1% | -1.443 to +1.1 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.3 | -0.1% | -1.443 to +1.1 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.387 | 2.352 | -1.5% | -0.1049 to +0.03505 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 69.9 | 69.15 | -1.1% | -3.575 to +2.072 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.674e+10 | 1.674e+10 | +0.0% | +1312 to +1312 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.114e+10 | 1.113e+10 | -0.1% | -1.201e+07 to -1.201e+07 | GAIN |
| organism time over the line (% of steps) | 2.37 | 2.35 | -0.9% | -0.02112 to -0.01944 | GAIN |
| organism work per energy | 1.503 | 1.505 | +0.1% | +0.001622 to +0.001622 | GAIN |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: toward their aims on 6, away from them on 0, inside the noise on 4

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4109 | 2389 | -41.9% | -3125 to -316.2 | GAIN |
| response time (ms), 99th percentile | 7848 | 6863 | -12.6% | -3104 to +1133 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 56.37 | 38.5 | -31.7% | -20.77 to -14.97 | GAIN |
| failed requests (%) | 27.44 | 25.35 | -7.6% | -2.673 to -1.505 | GAIN |
| HPA replicas, mean | 9.864 | 9.852 | -0.1% | -0.04966 to +0.0258 | STEADY, inside the noise (cut) |
| pods started | 2.2 | 2.2 | +0.0% | -0.8778 to +0.8778 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.572e-16 to +2.23e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.4 | 191.5 | -0.5% | -2.597 to +0.7594 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.4 | 191.5 | -0.5% | -2.597 to +0.7594 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.242 | 3.216 | -0.8% | -0.03131 to -0.02159 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 93.72 | 93.47 | -0.3% | -0.4911 to -0.01457 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.728e+10 | 5.728e+10 | +0.0% | +1310 to +1310 | STEADY, the same (under one part in a million) |
| organism energy (J) | 6.473e+10 | 6.461e+10 | -0.2% | -1.241e+08 to -1.241e+08 | GAIN |
| organism time over the line (% of steps) | 2.546 | 2.532 | -0.5% | -0.01397 to -0.01397 | GAIN |
| organism work per energy | 0.8849 | 0.8866 | +0.2% | +0.0017 to +0.0017 | GAIN |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: toward their aims on 3, away from them on 0, inside the noise on 8

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3416 | 2168 | -36.5% | -3180 to +684.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5069 | 4152 | -18.1% | -2751 to +915.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 39.97 | 35.75 | -10.6% | -8.508 to +0.06836 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.21 | 28.35 | +0.5% | -3.311 to +3.585 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.561 | 9.615 | +0.6% | -0.04171 to +0.1492 | STEADY, inside the noise (up) |
| pods started | 5 | 4.4 | -12.0% | -2.266 to +1.066 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.449e-16 to +1.1e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 185.1 | +0.0% | -0.713 to +0.826 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 185.1 | +0.0% | -0.713 to +0.826 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.566 | 2.535 | -1.2% | -0.05932 to -0.002092 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 73.57 | 73.22 | -0.5% | -1.33 to +0.6172 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.075e+11 | 1.075e+11 | -0.0% | -42.9 to -42.9 | STEADY, the same (under one part in a million) |
| organism energy (J) | 9.862e+10 | 9.847e+10 | -0.2% | -1.56e+08 to -1.56e+08 | GAIN |
| organism time over the line (% of steps) | 2.535 | 2.513 | -0.9% | -0.02243 to -0.02243 | GAIN |
| organism work per energy | 1.09 | 1.092 | +0.2% | +0.001727 to +0.001727 | GAIN |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: toward their aims on 4, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5025 | 2781 | -44.7% | -4839 to +350 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7340 | 5274 | -28.1% | -5139 to +1008 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 76.55 | 66.48 | -13.2% | -11.74 to -8.391 | GAIN |
| failed requests (%) | 54.99 | 52.22 | -5.0% | -9.17 to +3.619 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.93 | 9.896 | -0.3% | -0.1525 to +0.0843 | STEADY, inside the noise (cut) |
| pods started | 1.2 | 1.8 | +50.0% | -1.066 to +2.266 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.249e-16 to +2.346e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 194.1 | 194.1 | -0.0% | -0.645 to +0.4691 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 194.1 | 194.1 | -0.0% | -0.645 to +0.4691 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.425 | 3.399 | -0.8% | -0.04215 to -0.0105 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 97.95 | 97.95 | -0.0% | -0.1592 to +0.1443 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.73e+11 | 1.73e+11 | +0.0% | +3175 to +3175 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.2e+11 | 1.199e+11 | -0.1% | -1.24e+08 to -1.24e+08 | GAIN |
| organism time over the line (% of steps) | 2.187 | 2.17 | -0.8% | -0.01679 to -0.01679 | GAIN |
| organism work per energy | 1.441 | 1.443 | +0.1% | +0.001491 to +0.001491 | GAIN |
| organism behind its window (s) | 0.04 | 0.02 | -50.0% | -0.07552 to +0.03552 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: toward their aims on 4, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3994 | 2667 | -33.2% | -4732 to +2079 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6606 | 6626 | +0.3% | -754.9 to +794.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 57.08 | 44.57 | -21.9% | -20.79 to -4.237 | GAIN |
| failed requests (%) | 35.63 | 32.63 | -8.4% | -7.124 to +1.131 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.809 | 9.854 | +0.5% | -0.02178 to +0.1126 | STEADY, inside the noise (up) |
| pods started | 2.8 | 1.8 | -35.7% | -2.241 to +0.2415 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.634e-15 to +1.989e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.1 | 190.5 | +0.2% | -1.033 to +1.807 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.1 | 190.5 | +0.2% | -1.033 to +1.807 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 3.021 | 3.003 | -0.6% | -0.02898 to -0.007851 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 87.43 | 87.42 | -0.0% | -0.1989 to +0.1887 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.719e+11 | 1.719e+11 | +0.0% | +3131 to +3131 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.167e+11 | 1.166e+11 | -0.1% | -1.234e+08 to -1.234e+08 | GAIN |
| organism time over the line (% of steps) | 4.118 | 4.104 | -0.3% | -0.01384 to -0.01384 | GAIN |
| organism work per energy | 1.473 | 1.475 | +0.1% | +0.001558 to +0.001558 | GAIN |
| organism behind its window (s) | 0.02 | 0 | -100.0% | -0.07552 to +0.03552 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: toward their aims on 4, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2891 | 2568 | -11.2% | -3606 to +2962 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4937 | 4627 | -6.3% | -2769 to +2148 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 44.49 | 35.66 | -19.8% | -14.37 to -3.281 | GAIN |
| failed requests (%) | 26.69 | 26.62 | -0.3% | -2.927 to +2.788 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.668 | 9.685 | +0.2% | -0.09272 to +0.1264 | STEADY, inside the noise (up) |
| pods started | 4.8 | 4 | -16.7% | -2.641 to +1.041 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.12e-16 to +1.633e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.4 | 188.3 | -0.1% | -1.62 to +1.401 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.4 | 188.3 | -0.1% | -1.62 to +1.401 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.804 | 2.756 | -1.7% | -0.1001 to +0.002981 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 81.14 | 80.14 | -1.2% | -2.699 to +0.6889 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.605e+11 | 5.605e+11 | +0.0% | +3175 to +3175 | STEADY, the same (under one part in a million) |
| organism energy (J) | 6.18e+11 | 6.168e+11 | -0.2% | -1.205e+09 to -1.205e+09 | GAIN |
| organism time over the line (% of steps) | 1.83 | 1.796 | -1.8% | -0.03369 to -0.03369 | GAIN |
| organism work per energy | 0.907 | 0.9087 | +0.2% | +0.001772 to +0.001772 | GAIN |
| organism behind its window (s) | 0 | 0.02 | +0.02 | -0.03552 to +0.07552 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: toward their aims on 4, away from them on 1 (HPA replicas, mean), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3539 | 2514 | -29.0% | -2506 to +457 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6784 | 5142 | -24.2% | -3494 to +210.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 56.42 | 44.19 | -21.7% | -21.32 to -3.151 | GAIN |
| failed requests (%) | 34 | 31.77 | -6.5% | -6.943 to +2.492 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.764 | 9.83 | +0.7% | +0.02581 to +0.1048 | power given |
| pods started | 3.6 | 3 | -16.7% | -1.71 to +0.5104 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.139e-15 to +2.205e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.1 | 192 | -0.0% | -0.9436 to +0.8371 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.1 | 192 | -0.0% | -0.9436 to +0.8371 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.186 | 3.146 | -1.3% | -0.08002 to -0.0007134 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 91.16 | 90.61 | -0.6% | -1.547 to +0.4408 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.729e+11 | 1.729e+11 | +0.0% | +3411 to +3411 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.187e+11 | 1.185e+11 | -0.1% | -1.231e+08 to -1.231e+08 | GAIN |
| organism time over the line (% of steps) | 2.55 | 2.531 | -0.8% | -0.01966 to -0.01966 | GAIN |
| organism work per energy | 1.457 | 1.459 | +0.1% | +0.001513 to +0.001513 | GAIN |
| organism behind its window (s) | 0.04 | 0.04 | +0.0% | -0.08778 to +0.08778 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: toward their aims on 4, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2978 | 2188 | -26.5% | -2201 to +619.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4948 | 5307 | +7.3% | -3175 to +3893 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 61.19 | 50.68 | -17.2% | -13.53 to -7.494 | GAIN |
| failed requests (%) | 42.87 | 40.9 | -4.6% | -5.556 to +1.617 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.833 | 9.793 | -0.4% | -0.1486 to +0.06903 | STEADY, inside the noise (cut) |
| pods started | 2.6 | 3.2 | +23.1% | -1.655 to +2.855 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.26e-15 to +1.615e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.6 | 192.8 | +0.1% | -0.2573 to +0.7689 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.6 | 192.8 | +0.1% | -0.2573 to +0.7689 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 3.213 | 3.159 | -1.7% | -0.1611 to +0.052 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 92.66 | 91.71 | -1.0% | -3.846 to +1.936 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.625e+11 | 5.625e+11 | +0.0% | +3367 to +3367 | STEADY, the same (under one part in a million) |
| organism energy (J) | 6.411e+11 | 6.399e+11 | -0.2% | -1.205e+09 to -1.205e+09 | GAIN |
| organism time over the line (% of steps) | 2.846 | 2.836 | -0.4% | -0.01061 to -0.01061 | GAIN |
| organism work per energy | 0.8774 | 0.879 | +0.2% | +0.001652 to +0.001652 | GAIN |
| organism behind its window (s) | 0.06 | 0.08 | +33.3% | -0.08387 to +0.1239 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: toward their aims on 3, away from them on 1 (organism work), inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2263 | 2122 | -6.2% | -952.6 to +670.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3829 | 3401 | -11.2% | -1130 to +273.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 27.65 | 19.08 | -31.0% | -21.95 to +4.809 | STEADY, inside the noise (cut) |
| failed requests (%) | 13.91 | 11.98 | -13.9% | -6.89 to +3.034 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.603 | 9.607 | +0.0% | -0.1243 to +0.1327 | STEADY, inside the noise (up) |
| pods started | 5.6 | 5.6 | +0.0% | -2.634 to +2.634 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.1e-15 to +7.449e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.2 | -0.4% | -2.402 to +0.7593 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.2 | -0.4% | -2.402 to +0.7593 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.369 | -1.9% | -0.1023 to +0.009593 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 70.51 | 69.85 | -0.9% | -2.835 to +1.52 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.065e+12 | 1.065e+12 | -0.0% | -2.8e+06 to -2.8e+06 | LOSS |
| organism energy (J) | 9.668e+11 | 9.653e+11 | -0.2% | -1.57e+09 to -1.57e+09 | GAIN |
| organism time over the line (% of steps) | 2.579 | 2.554 | -1.0% | -0.02529 to -0.02529 | GAIN |
| organism work per energy | 1.102 | 1.104 | +0.2% | +0.001789 to +0.001789 | GAIN |
| organism behind its window (s) | 0.1 | 0.1 | +0.0% | -0.08778 to +0.08778 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: toward their aims on 5, away from them on 1 (organism work), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5209 | 3492 | -33.0% | -3082 to -353 | GAIN |
| response time (ms), 99th percentile | 8017 | 6544 | -18.4% | -4658 to +1713 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 75.74 | 64.51 | -14.8% | -22.06 to -0.3935 | GAIN |
| failed requests (%) | 55.04 | 52.1 | -5.3% | -7.061 to +1.187 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.895 | 9.906 | +0.1% | -0.06951 to +0.08983 | STEADY, inside the noise (up) |
| pods started | 2.6 | 2.4 | -7.7% | -2.588 to +2.188 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.79e-15 to +7.243e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 290.5 | 289.9 | -0.2% | -2.365 to +1.053 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 290.5 | 289.9 | -0.2% | -2.365 to +1.053 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.375 | 3.347 | -0.8% | -0.04064 to -0.01576 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 97.86 | 98.05 | +0.2% | -0.1376 to +0.5194 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.692e+12 | 1.692e+12 | -0.0% | -1.614e+07 to -1.614e+07 | LOSS |
| organism energy (J) | 1.17e+12 | 1.169e+12 | -0.1% | -1.17e+09 to -1.17e+09 | GAIN |
| organism time over the line (% of steps) | 2.126 | 2.11 | -0.8% | -0.01628 to -0.01628 | GAIN |
| organism work per energy | 1.446 | 1.447 | +0.1% | +0.001433 to +0.001433 | GAIN |
| organism behind its window (s) | 1.4 | 0.7 | -50.0% | -1.102 to -0.2977 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: toward their aims on 5, away from them on 1 (organism work), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2714 | 1935 | -28.7% | -1944 to +384.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3968 | 3302 | -16.8% | -2452 to +1122 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 36.73 | 29.76 | -19.0% | -15.51 to +1.568 | STEADY, inside the noise (cut) |
| failed requests (%) | 25.11 | 24.21 | -3.6% | -2.493 to +0.6913 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.762 | 9.758 | -0.0% | -0.06564 to +0.05697 | STEADY, inside the noise (cut) |
| pods started | 4.4 | 4.8 | +9.1% | -0.7104 to +1.51 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.559e-15 to +1.559e-15 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 279.5 | 278.2 | -0.5% | -2.392 to -0.3148 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 279.5 | 278.2 | -0.5% | -2.392 to -0.3148 | GAIN |
| CPU used with Omni's own (cores), mean | 2.608 | 2.536 | -2.8% | -0.1806 to +0.03627 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 76.64 | 74.99 | -2.1% | -4.845 to +1.554 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.682e+12 | 1.682e+12 | -0.0% | -9.249e+06 to -9.249e+06 | LOSS |
| organism energy (J) | 1.14e+12 | 1.139e+12 | -0.1% | -1.163e+09 to -1.163e+09 | GAIN |
| organism time over the line (% of steps) | 3.895 | 3.884 | -0.3% | -0.01073 to -0.01073 | GAIN |
| organism work per energy | 1.475 | 1.476 | +0.1% | +0.001498 to +0.001498 | GAIN |
| organism behind its window (s) | 0.6 | 0.58 | -3.3% | -0.1239 to +0.08387 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: toward their aims on 5, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3178 | 2631 | -17.2% | -3222 to +2128 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6002 | 5325 | -11.3% | -3922 to +2568 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 63.6 | 56.7 | -10.8% | -11.51 to -2.28 | GAIN |
| failed requests (%) | 49.88 | 46.9 | -6.0% | -6.827 to +0.8624 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.881 | 9.887 | +0.1% | -0.05768 to +0.0697 | STEADY, inside the noise (up) |
| pods started | 2.6 | 2.2 | -15.4% | -1.815 to +1.015 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.97e-15 to +1.549e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 284.6 | -0.4% | -2.908 to +0.4552 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 284.6 | -0.4% | -2.908 to +0.4552 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.052 | 3.028 | -0.8% | -0.0699 to +0.02307 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 88.89 | 89.42 | +0.6% | -0.6584 to +1.721 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.621e+12 | 5.621e+12 | +0.0% | +6.201e+07 to +6.201e+07 | GAIN |
| organism energy (J) | 6.163e+12 | 6.151e+12 | -0.2% | -1.157e+10 to -1.157e+10 | GAIN |
| organism time over the line (% of steps) | 1.836 | 1.803 | -1.8% | -0.0328 to -0.0328 | GAIN |
| organism work per energy | 0.9121 | 0.9138 | +0.2% | +0.001726 to +0.001726 | GAIN |
| organism behind its window (s) | 0.4 | 0.44 | +10.0% | -0.1015 to +0.1815 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: toward their aims on 3, away from them on 1 (organism work), inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3160 | 1666 | -47.3% | -3791 to +802.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4486 | 3925 | -12.5% | -2036 to +914.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 49.56 | 43.87 | -11.5% | -13.32 to +1.946 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.87 | 37.19 | -4.3% | -5.227 to +1.864 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.829 | 9.821 | -0.1% | -0.08468 to +0.07017 | STEADY, inside the noise (cut) |
| pods started | 3.4 | 3.4 | +0.0% | -2.323 to +2.323 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.15e-15 to +1.795e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 281.9 | 280.7 | -0.4% | -3.6 to +1.116 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 281.9 | 280.7 | -0.4% | -3.6 to +1.116 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.754 | 2.745 | -0.3% | -0.06543 to +0.04722 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 81.09 | 81.29 | +0.2% | -1.495 to +1.886 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.691e+12 | 1.691e+12 | -0.0% | -1.06e+07 to -1.06e+07 | LOSS |
| organism energy (J) | 1.157e+12 | 1.156e+12 | -0.1% | -1.161e+09 to -1.161e+09 | GAIN |
| organism time over the line (% of steps) | 2.518 | 2.501 | -0.7% | -0.01707 to -0.01707 | GAIN |
| organism work per energy | 1.462 | 1.463 | +0.1% | +0.001459 to +0.001459 | GAIN |
| organism behind its window (s) | 0.66 | 0.8 | +21.2% | -0.4844 to +0.7644 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 100 copies: toward their aims on 6, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2856 | 3213 | +12.5% | -1982 to +2695 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4358 | 4840 | +11.1% | -1001 to +1967 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 47.28 | 44.86 | -5.1% | -4.889 to +0.04212 | STEADY, inside the noise (cut) |
| failed requests (%) | 39.09 | 36.86 | -5.7% | -4.94 to +0.4922 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.809 | 9.782 | -0.3% | -0.09619 to +0.04193 | STEADY, inside the noise (cut) |
| pods started | 3.8 | 4.6 | +21.1% | -0.2387 to +1.839 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.82e-16 to +3.424e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 281.6 | 279.7 | -0.7% | -3.123 to -0.6825 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 281.6 | 279.7 | -0.7% | -3.123 to -0.6825 | GAIN |
| CPU used with Omni's own (cores), mean | 2.773 | 2.698 | -2.7% | -0.13 to -0.02162 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 83.81 | 83.24 | -0.7% | -2.794 to +1.655 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.641e+12 | 5.641e+12 | +0.0% | +5.294e+07 to +5.294e+07 | GAIN |
| organism energy (J) | 6.396e+12 | 6.385e+12 | -0.2% | -1.158e+10 to -1.158e+10 | GAIN |
| organism time over the line (% of steps) | 2.698 | 2.689 | -0.3% | -0.009038 to -0.009038 | GAIN |
| organism work per energy | 0.8819 | 0.8835 | +0.2% | +0.001608 to +0.001608 | GAIN |
| organism behind its window (s) | 1.26 | 1.32 | +4.8% | -0.5827 to +0.7027 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 100 copies: toward their aims on 4, away from them on 1 (organism work), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3842 | 2496 | -35.0% | -4652 to +1960 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5942 | 4244 | -28.6% | -4469 to +1073 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 60.01 | 47.71 | -20.5% | -24.2 to -0.3856 | GAIN |
| failed requests (%) | 42.13 | 39 | -7.4% | -7.245 to +0.9932 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.769 | 9.777 | +0.1% | -0.03001 to +0.04598 | STEADY, inside the noise (up) |
| pods started | 5.2 | 5.2 | +0.0% | +0 to +0 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.35e-15 to +1.35e-15 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 282.7 | 281.6 | -0.4% | -2.946 to +0.8587 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 282.7 | 281.6 | -0.4% | -2.946 to +0.8587 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.883 | 2.783 | -3.5% | -0.1535 to -0.04801 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 89.26 | 89.18 | -0.1% | -1.005 to +0.8376 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.067e+13 | 1.067e+13 | -0.0% | -6.349e+07 to -6.349e+07 | LOSS |
| organism energy (J) | 9.618e+12 | 9.603e+12 | -0.2% | -1.535e+10 to -1.535e+10 | GAIN |
| organism time over the line (% of steps) | 2.568 | 2.545 | -0.9% | -0.02275 to -0.02275 | GAIN |
| organism work per energy | 1.11 | 1.112 | +0.2% | +0.001768 to +0.001768 | GAIN |
| organism behind its window (s) | 2.72 | 2.64 | -2.9% | -0.9812 to +0.8212 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 1,000 copies: toward their aims on 5, away from them on 1 (organism work), inside the noise on 6

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2141 | 826.6 | -61.4% | -5922 to +3293 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3009 | 2757 | -8.4% | -790.4 to +286.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 28.51 | 26.16 | -8.2% | -6.105 to +1.408 | STEADY, inside the noise (cut) |
| failed requests (%) | 22.92 | 23.03 | +0.5% | -0.3753 to +0.6026 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.823 | 9.815 | -0.1% | -0.04557 to +0.02961 | STEADY, inside the noise (cut) |
| pods started | 6.333 | 6 | -5.3% | -1.768 to +1.101 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.001e-15 to +5.185e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 549.6 | 545.8 | -0.7% | -4.883 to -2.673 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 549.6 | 545.8 | -0.7% | -4.883 to -2.673 | GAIN |
| CPU used with Omni's own (cores), mean | 2.342 | 2.245 | -4.1% | -0.126 to -0.06827 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 73.92 | 73.61 | -0.4% | -1.632 to +1.018 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.69e+13 | 1.69e+13 | -0.0% | -5.925e+08 to -5.925e+08 | LOSS |
| organism energy (J) | 1.169e+13 | 1.168e+13 | -0.1% | -1.144e+10 to -1.144e+10 | GAIN |
| organism time over the line (% of steps) | 2.095 | 2.079 | -0.7% | -0.01544 to -0.01544 | GAIN |
| organism work per energy | 1.446 | 1.447 | +0.1% | +0.001365 to +0.001365 | GAIN |
| organism behind its window (s) | 6.3 | 5.667 | -10.1% | -3.876 to +2.609 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 1,000 copies: toward their aims on 3, away from them on 1 (organism work), inside the noise on 7; OFF THE CLOCK in 2 of 3 repetitions (the organism ended up to 290 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2734 | 3516 | +28.6% | -4044 to +5609 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5491 | 5166 | -5.9% | -7312 to +6663 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.68 | 50.74 | -8.9% | -13.29 to +3.409 | STEADY, inside the noise (cut) |
| failed requests (%) | 45.47 | 42.37 | -6.8% | -13.64 to +7.445 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.865 | 9.863 | -0.0% | -0.008198 to +0.004748 | STEADY, inside the noise (cut) |
| pods started | 5.333 | 5.333 | +0.0% | +0 to +0 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.667e-15 to +3.074e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 558.6 | 555.5 | -0.5% | -7.505 to +1.471 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 558.6 | 555.5 | -0.5% | -7.505 to +1.471 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.655 | 2.587 | -2.5% | -0.1386 to +0.003774 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 86.17 | 86.75 | +0.7% | -0.992 to +2.154 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.68e+13 | 1.68e+13 | -0.0% | -5.354e+08 to -5.354e+08 | LOSS |
| organism energy (J) | 1.14e+13 | 1.138e+13 | -0.1% | -1.14e+10 to -1.14e+10 | GAIN |
| organism time over the line (% of steps) | 3.944 | 3.937 | -0.2% | -0.007573 to -0.007568 | GAIN |
| organism work per energy | 1.474 | 1.476 | +0.1% | +0.001429 to +0.001429 | GAIN |
| organism behind its window (s) | 6 | 154.8 | +2480.0% | -203.2 to +500.8 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 1,000 copies: toward their aims on 5, away from them on 0, inside the noise on 6

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3398 | 4005 | +17.9% | -4455 to +5669 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6055 | 7405 | +22.3% | -3217 to +5916 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 82.16 | 77.69 | -5.4% | -11.63 to +2.672 | STEADY, inside the noise (cut) |
| failed requests (%) | 69.44 | 69.43 | -0.0% | -4.362 to +4.347 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.895 | 9.9 | +0.1% | -0.06216 to +0.07261 | STEADY, inside the noise (up) |
| pods started | 4.667 | 4.333 | -7.1% | -3.202 to +2.535 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.57e-15 to +9.779e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 571.2 | 565.5 | -1.0% | -11.05 to -0.4045 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 571.2 | 565.5 | -1.0% | -11.05 to -0.4045 | GAIN |
| CPU used with Omni's own (cores), mean | 3.069 | 2.93 | -4.5% | -0.1556 to -0.1227 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 98.75 | 98.94 | +0.2% | +0.1171 to +0.2494 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.609e+13 | 5.609e+13 | +0.0% | +1.063e+07 to +1.063e+07 | STEADY, the same (under one part in a million) |
| organism energy (J) | 6.153e+13 | 6.141e+13 | -0.2% | -1.168e+11 to -1.168e+11 | GAIN |
| organism time over the line (% of steps) | 1.811 | 1.781 | -1.7% | -0.03057 to -0.03057 | GAIN |
| organism work per energy | 0.9116 | 0.9133 | +0.2% | +0.001733 to +0.001733 | GAIN |
| organism behind its window (s) | 7.233 | 42.4 | +486.2% | -76.77 to +147.1 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 1,000 copies: toward their aims on 3, away from them on 1 (organism work), inside the noise on 8

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2183 | 2906 | +33.1% | -3507 to +4954 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4756 | 4241 | -10.8% | -9207 to +8179 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.02 | 52.32 | -4.9% | -8.874 to +3.477 | STEADY, inside the noise (cut) |
| failed requests (%) | 46.77 | 45.76 | -2.2% | -4.779 to +2.752 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.861 | 9.864 | +0.0% | -0.06876 to +0.07519 | STEADY, inside the noise (up) |
| pods started | 5 | 5.333 | +6.7% | -1.101 to +1.768 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.778e-15 to +3.963e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 559.4 | 557.5 | -0.3% | -11.08 to +7.327 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 559.4 | 557.5 | -0.3% | -11.08 to +7.327 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.701 | 2.641 | -2.3% | -0.239 to +0.1171 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 86.04 | 87.07 | +1.2% | -2.839 to +4.893 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.69e+13 | 1.69e+13 | -0.0% | -5.934e+08 to -5.934e+08 | LOSS |
| organism energy (J) | 1.157e+13 | 1.156e+13 | -0.1% | -1.132e+10 to -1.132e+10 | GAIN |
| organism time over the line (% of steps) | 2.502 | 2.486 | -0.6% | -0.01532 to -0.01532 | GAIN |
| organism work per energy | 1.461 | 1.462 | +0.1% | +0.001379 to +0.001379 | GAIN |
| organism behind its window (s) | 7.067 | 8.933 | +26.4% | -2.482 to +6.215 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 1,000 copies: toward their aims on 3, away from them on 1 (organism work), inside the noise on 7; OFF THE CLOCK in 2 of 3 repetitions (the organism ended up to 3,820 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2915 | 3198 | +9.7% | -1991 to +2556 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4945 | 5166 | +4.5% | -1529 to +1971 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 58.12 | 51.41 | -11.5% | -15.64 to +2.223 | STEADY, inside the noise (cut) |
| failed requests (%) | 48.68 | 43.37 | -10.9% | -17.27 to +6.646 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.855 | 9.857 | +0.0% | -0.04659 to +0.0493 | STEADY, inside the noise (up) |
| pods started | 5.667 | 5.667 | +0.0% | +0 to +0 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.797e-15 to +7.389e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 557.8 | 557.9 | +0.0% | -2.143 to +2.359 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 557.8 | 557.9 | +0.0% | -2.143 to +2.359 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.659 | 2.659 | +0.0% | -0.04069 to +0.04191 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 91.02 | 92.77 | +1.9% | -5.489 to +8.995 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.629e+13 | 5.629e+13 | -0.0% | -9.426e+07 to -9.426e+07 | LOSS |
| organism energy (J) | 6.387e+13 | 6.375e+13 | -0.2% | -1.168e+11 to -1.168e+11 | GAIN |
| organism time over the line (% of steps) | 2.722 | 2.714 | -0.3% | -0.007881 to -0.007879 | GAIN |
| organism work per energy | 0.8814 | 0.883 | +0.2% | +0.001614 to +0.001614 | GAIN |
| organism behind its window (s) | 1508 | 2418 | +60.4% | -1175 to +2996 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 1,000 copies: ONE REPETITION; OFF THE CLOCK in 1 of 1 repetitions (the organism ended up to 1,345 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 560.3 | 191.6 | -65.8% |  | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 824.2 | 239.1 | -71.0% |  | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 6.552 | 0 | -100.0% |  | STEADY, inside the noise (cut) |
| failed requests (%) | 0 | 0 | +0 |  | STEADY, the same |
| HPA replicas, mean | 9.82 | 9.761 | -0.6% |  | STEADY, inside the noise (cut) |
| pods started | 7 | 7 | +0.0% |  | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 552.4 | 547.3 | -0.9% |  | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 552.4 | 547.3 | -0.9% |  | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.442 | 2.3 | -5.8% |  | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 90.62 | 87.99 | -2.9% |  | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.067e+14 | 1.067e+14 | -0.0% |  | STEADY, inside the noise (cut) |
| organism energy (J) | 9.605e+13 | 9.59e+13 | -0.2% |  | STEADY, inside the noise (cut) |
| organism time over the line (% of steps) | 2.568 | 2.546 | -0.9% |  | STEADY, inside the noise (cut) |
| organism work per energy | 1.111 | 1.112 | +0.2% |  | STEADY, inside the noise (up) |
| organism behind its window (s) | 602.8 | 1345 | +123.1% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
