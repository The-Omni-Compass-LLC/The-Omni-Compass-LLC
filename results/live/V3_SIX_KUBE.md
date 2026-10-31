# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`). The aim is lower for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). The aim is higher for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2927 | 1455 | 718.1 | 583 | 2491 | 1765 | 3487 | 1686 | 3777 | 2206 | 4965 | 4904 | 4601 | 3839 | 4746 | 3134 | 3636 | 2229 | 3089 | 2104 | 4130 | 2934 | 2922 | 2457 |
| response time (ms), 99th percentile | 5453 | 4166 | 1513 | 2112 | 5939 | 4138 | 7842 | 5312 | 7204 | 5834 | 8040 | 6935 | 6769 | 5835 | 7590 | 5543 | 5453 | 3846 | 5143 | 4608 | 6069 | 5141 | 4285 | 3813 |
| time over the response line (% of samples) | 48.28 | 33.03 | 16.38 | 9.708 | 52.15 | 35.14 | 55.34 | 35.45 | 73.09 | 58.4 | 80.38 | 70.64 | 62.7 | 56.58 | 78.85 | 72.2 | 51.02 | 43.43 | 57.22 | 44.67 | 66.65 | 60.82 | 62.16 | 53.09 |
| failed requests (%) | 26.85 | 24.04 | 8.108 | 7.487 | 27.02 | 24.16 | 25.75 | 23.63 | 47.45 | 43.49 | 65.92 | 60.33 | 49.83 | 46.95 | 61.96 | 58.8 | 36.45 | 37 | 38.11 | 36.24 | 52.79 | 52.61 | 43.92 | 39.65 |
| HPA replicas, mean | 9.716 | 9.772 | 9.538 | 9.542 | 9.777 | 9.832 | 9.791 | 9.8 | 9.88 | 9.907 | 9.919 | 9.98 | 9.85 | 9.852 | 9.947 | 9.922 | 9.859 | 9.838 | 9.882 | 9.864 | 9.822 | 9.805 | 9.767 | 9.773 |
| pods started | 3.8 | 3 | 5.6 | 6 | 3.6 | 2.6 | 3 | 3.4 | 2 | 1.4 | 1.6 | 0.4 | 3 | 3.2 | 1.2 | 1.8 | 3 | 3.4 | 2.8 | 3.2 | 4.6 | 4.6 | 5.4 | 5.4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 189.6 | 190 | 181.8 | 181.4 | 191.4 | 192.2 | 192.1 | 192.2 | 194.1 | 194 | 192.9 | 193.1 | 285.5 | 286.5 | 289.2 | 289 | 284.8 | 283.9 | 287.2 | 286.8 | 284.2 | 282.7 | 282.2 | 281.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.6 | 190 | 181.8 | 181.4 | 191.4 | 192.2 | 192.1 | 192.2 | 194.1 | 194 | 192.9 | 193.1 | 285.5 | 286.5 | 289.2 | 289 | 284.8 | 283.9 | 287.2 | 286.8 | 284.2 | 282.7 | 282.2 | 281.9 |
| CPU used with Omni's own (cores), mean | 2.952 | 2.928 | 2.176 | 2.139 | 3.178 | 3.146 | 3.219 | 3.175 | 3.361 | 3.343 | 3.307 | 3.282 | 3.034 | 2.941 | 3.311 | 3.284 | 2.958 | 2.674 | 3.139 | 3.095 | 2.901 | 2.669 | 2.801 | 2.654 |
| host CPU busy, the real machine under kind (%) | 85.04 | 84.3 | 63.48 | 62.94 | 91.72 | 91.41 | 91.94 | 91.37 | 97.27 | 97.27 | 98.52 | 98.58 | 89.21 | 89.25 | 98.28 | 98.35 | 88.06 | 88.11 | 92.13 | 91.67 | 91.22 | 91.26 | 91.33 | 93.49 |
| organism work | 2.159e+11 | 2.159e+11 | 2.147e+11 | 2.147e+11 | 6.677e+11 | 6.677e+11 | 2.159e+11 | 2.159e+11 | 6.7e+11 | 6.7e+11 | 1.294e+12 | 1.294e+12 | 2.104e+12 | 2.104e+12 | 2.093e+12 | 2.093e+12 | 6.649e+12 | 6.649e+12 | 2.105e+12 | 2.105e+12 | 6.672e+12 | 6.672e+12 | 1.294e+13 | 1.294e+13 |
| organism energy (J) | 1.518e+11 | 1.517e+11 | 1.881e+11 | 1.879e+11 | 1.103e+14 | 1.099e+14 | 5.653e+11 | 5.642e+11 | 1.108e+14 | 1.104e+14 | 1.082e+14 | 1.077e+14 | 1.48e+12 | 1.478e+12 | 1.841e+12 | 1.84e+12 | 1.098e+15 | 1.094e+15 | 5.688e+12 | 5.677e+12 | 1.103e+15 | 1.099e+15 | 1.104e+15 | 1.1e+15 |
| organism time over the line (% of steps) | 2.234 | 2.217 | 4.76 | 4.748 | 1.448 | 1.435 | 2.721 | 2.705 | 2.879 | 2.872 | 2.61 | 2.59 | 2.167 | 2.15 | 4.438 | 4.424 | 1.468 | 1.45 | 2.623 | 2.607 | 2.716 | 2.707 | 2.595 | 2.577 |
| organism work per energy | 1.422 | 1.423 | 1.142 | 1.143 | 0.006054 | 0.006075 | 0.3818 | 0.3826 | 0.006048 | 0.00607 | 0.01197 | 0.01201 | 1.422 | 1.423 | 1.137 | 1.138 | 0.006054 | 0.006076 | 0.37 | 0.3708 | 0.006047 | 0.006069 | 0.01172 | 0.01176 |
| organism behind its window (s) | 0.06 | 0.1 | 0.02 | 0 | 0.04 | 0.08 | 0.04 | 0.06 | 0.18 | 0.24 | 0.28 | 0.5 | 0.74 | 0.76 | 0.7 | 1.32 | 1.28 | 1.18 | 1.3 | 0.94 | 1.92 | 2.38 | 5.92 | 149.2 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: toward their aims on 5, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2927 | 1455 | -50.3% | -2786 to -157.8 | GAIN |
| response time (ms), 99th percentile | 5453 | 4166 | -23.6% | -3261 to +686.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 48.28 | 33.03 | -31.6% | -27.68 to -2.834 | GAIN |
| failed requests (%) | 26.85 | 24.04 | -10.5% | -6.445 to +0.8328 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.716 | 9.772 | +0.6% | -0.05165 to +0.1642 | STEADY, inside the noise (up) |
| pods started | 3.8 | 3 | -21.1% | -2.419 to +0.8187 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.533e-16 to +1.519e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.6 | 190 | +0.2% | -1.288 to +2.14 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.6 | 190 | +0.2% | -1.288 to +2.14 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.952 | 2.928 | -0.8% | -0.08273 to +0.03573 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 85.04 | 84.3 | -0.9% | -2.069 to +0.583 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 2.159e+11 | 2.159e+11 | +0.0% | +4496 to +4496 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.518e+11 | 1.517e+11 | -0.1% | -1.321e+08 to -1.321e+08 | GAIN |
| organism time over the line (% of steps) | 2.234 | 2.217 | -0.8% | -0.01715 to -0.01715 | GAIN |
| organism work per energy | 1.422 | 1.423 | +0.1% | +0.001239 to +0.001239 | GAIN |
| organism behind its window (s) | 0.06 | 0.1 | +66.7% | -0.07104 to +0.151 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: toward their aims on 3, away from them on 0, inside the noise on 8

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 718.1 | 583 | -18.8% | -668.6 to +398.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 1513 | 2112 | +39.6% | -3171 to +4370 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 16.38 | 9.708 | -40.7% | -16.32 to +2.973 | STEADY, inside the noise (cut) |
| failed requests (%) | 8.108 | 7.487 | -7.7% | -2.345 to +1.103 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.538 | 9.542 | +0.0% | -0.07798 to +0.08547 | STEADY, inside the noise (up) |
| pods started | 5.6 | 6 | +7.1% | -0.7104 to +1.51 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.386e-15 to +1.03e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.4 | -0.2% | -2.61 to +1.817 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.4 | -0.2% | -2.61 to +1.817 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.176 | 2.139 | -1.7% | -0.1759 to +0.1008 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 63.48 | 62.94 | -0.8% | -4.546 to +3.476 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 2.147e+11 | 2.147e+11 | +0.0% | +4487 to +4487 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.881e+11 | 1.879e+11 | -0.1% | -1.443e+08 to -1.443e+08 | GAIN |
| organism time over the line (% of steps) | 4.76 | 4.748 | -0.3% | -0.01197 to -0.01197 | GAIN |
| organism work per energy | 1.142 | 1.143 | +0.1% | +0.0008765 to +0.0008766 | GAIN |
| organism behind its window (s) | 0.02 | 0 | -100.0% | -0.07552 to +0.03552 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: toward their aims on 4, away from them on 1 (HPA replicas, mean), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2491 | 1765 | -29.1% | -2343 to +891 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5939 | 4138 | -30.3% | -3873 to +271.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 52.15 | 35.14 | -32.6% | -25.14 to -8.881 | GAIN |
| failed requests (%) | 27.02 | 24.16 | -10.6% | -7.912 to +2.192 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.777 | 9.832 | +0.6% | +0.01073 to +0.09959 | power given |
| pods started | 3.6 | 2.6 | -27.8% | -2.241 to +0.2415 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.038e-15 to +9.067e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 191.4 | 192.2 | +0.4% | -0.6107 to +2.148 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.4 | 192.2 | +0.4% | -0.6107 to +2.148 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 3.178 | 3.146 | -1.0% | -0.07596 to +0.0122 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 91.72 | 91.41 | -0.3% | -0.9066 to +0.3016 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 6.677e+11 | 6.677e+11 | +0.0% | +4496 to +4496 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.103e+14 | 1.099e+14 | -0.3% | -3.828e+11 to -3.828e+11 | GAIN |
| organism time over the line (% of steps) | 1.448 | 1.435 | -0.9% | -0.01348 to -0.01348 | GAIN |
| organism work per energy | 0.006054 | 0.006075 | +0.3% | +2.109e-05 to +2.109e-05 | GAIN |
| organism behind its window (s) | 0.04 | 0.08 | +100.0% | -0.07104 to +0.151 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: toward their aims on 5, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3487 | 1686 | -51.7% | -2936 to -666 | GAIN |
| response time (ms), 99th percentile | 7842 | 5312 | -32.3% | -6262 to +1201 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.34 | 35.45 | -35.9% | -28.07 to -11.72 | GAIN |
| failed requests (%) | 25.75 | 23.63 | -8.2% | -5.117 to +0.8849 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.791 | 9.8 | +0.1% | -0.08328 to +0.1005 | STEADY, inside the noise (up) |
| pods started | 3 | 3.4 | +13.3% | -0.7104 to +1.51 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.505e-15 to +1.794e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.1 | 192.2 | +0.0% | -1.405 to +1.561 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.1 | 192.2 | +0.0% | -1.405 to +1.561 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 3.219 | 3.175 | -1.4% | -0.08584 to -0.003251 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 91.94 | 91.37 | -0.6% | -1.748 to +0.6125 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 2.159e+11 | 2.159e+11 | +0.0% | +4733 to +4733 | STEADY, the same (under one part in a million) |
| organism energy (J) | 5.653e+11 | 5.642e+11 | -0.2% | -1.16e+09 to -1.16e+09 | GAIN |
| organism time over the line (% of steps) | 2.721 | 2.705 | -0.6% | -0.01629 to -0.01629 | GAIN |
| organism work per energy | 0.3818 | 0.3826 | +0.2% | +0.0007851 to +0.0007851 | GAIN |
| organism behind its window (s) | 0.04 | 0.06 | +50.0% | -0.03552 to +0.07552 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: toward their aims on 6, away from them on 0, inside the noise on 5

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3777 | 2206 | -41.6% | -3004 to -136.5 | GAIN |
| response time (ms), 99th percentile | 7204 | 5834 | -19.0% | -3929 to +1188 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 73.09 | 58.4 | -20.1% | -20.67 to -8.711 | GAIN |
| failed requests (%) | 47.45 | 43.49 | -8.4% | -6.384 to -1.541 | GAIN |
| HPA replicas, mean | 9.88 | 9.907 | +0.3% | -0.09889 to +0.151 | STEADY, inside the noise (up) |
| pods started | 2 | 1.4 | -30.0% | -3.02 to +1.82 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.916e-15 to +4.288e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 194.1 | 194 | -0.1% | -1.072 to +0.8335 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 194.1 | 194 | -0.1% | -1.072 to +0.8335 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.361 | 3.343 | -0.5% | -0.04886 to +0.01446 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 97.27 | 97.27 | -0.0% | -0.3438 to +0.3395 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 6.7e+11 | 6.7e+11 | +0.0% | +4724 to +4724 | STEADY, the same (under one part in a million) |
| organism energy (J) | 1.108e+14 | 1.104e+14 | -0.3% | -3.838e+11 to -3.838e+11 | GAIN |
| organism time over the line (% of steps) | 2.879 | 2.872 | -0.2% | -0.006746 to -0.006746 | GAIN |
| organism work per energy | 0.006048 | 0.00607 | +0.3% | +2.103e-05 to +2.103e-05 | GAIN |
| organism behind its window (s) | 0.18 | 0.24 | +33.3% | -0.1655 to +0.2855 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: toward their aims on 5, away from them on 1 (organism work), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4965 | 4904 | -1.2% | -3823 to +3701 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 8040 | 6935 | -13.7% | -3149 to +938.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 80.38 | 70.64 | -12.1% | -11.72 to -7.761 | GAIN |
| failed requests (%) | 65.92 | 60.33 | -8.5% | -9.825 to -1.357 | GAIN |
| HPA replicas, mean | 9.919 | 9.98 | +0.6% | -0.02189 to +0.1438 | STEADY, inside the noise (up) |
| pods started | 1.6 | 0.4 | -75.0% | -2.819 to +0.4187 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.1e-15 to +7.449e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.9 | 193.1 | +0.1% | -1.13 to +1.489 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.9 | 193.1 | +0.1% | -1.13 to +1.489 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 3.307 | 3.282 | -0.8% | -0.04289 to -0.007211 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 98.52 | 98.58 | +0.1% | -0.01452 to +0.1364 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.294e+12 | 1.294e+12 | -0.0% | -7.802e+06 to -7.802e+06 | LOSS |
| organism energy (J) | 1.082e+14 | 1.077e+14 | -0.4% | -4.285e+11 to -4.285e+11 | GAIN |
| organism time over the line (% of steps) | 2.61 | 2.59 | -0.8% | -0.01981 to -0.01981 | GAIN |
| organism work per energy | 0.01197 | 0.01201 | +0.4% | +4.752e-05 to +4.752e-05 | GAIN |
| organism behind its window (s) | 0.28 | 0.5 | +78.6% | -0.0631 to +0.5031 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: toward their aims on 4, away from them on 1 (organism work), inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4601 | 3839 | -16.6% | -3199 to +1675 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6769 | 5835 | -13.8% | -4867 to +3000 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 62.7 | 56.58 | -9.8% | -11.23 to -1.003 | GAIN |
| failed requests (%) | 49.83 | 46.95 | -5.8% | -7.389 to +1.633 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.85 | 9.852 | +0.0% | -0.08638 to +0.08962 | STEADY, inside the noise (up) |
| pods started | 3 | 3.2 | +6.7% | -1.641 to +2.041 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.668e-15 to -1.085e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.5 | 286.5 | +0.4% | -0.4553 to +2.513 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.5 | 286.5 | +0.4% | -0.4553 to +2.513 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.962 | 2.941 | -0.7% | -0.05218 to +0.009176 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 89.21 | 89.25 | +0.0% | -0.1135 to +0.1977 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 2.104e+12 | 2.104e+12 | -0.0% | -1.579e+07 to -1.579e+07 | LOSS |
| organism energy (J) | 1.48e+12 | 1.478e+12 | -0.1% | -1.247e+09 to -1.247e+09 | GAIN |
| organism time over the line (% of steps) | 2.167 | 2.15 | -0.8% | -0.01683 to -0.01681 | GAIN |
| organism work per energy | 1.422 | 1.423 | +0.1% | +0.001189 to +0.001189 | GAIN |
| organism behind its window (s) | 0.74 | 0.76 | +2.7% | -0.1641 to +0.2041 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: toward their aims on 4, away from them on 1 (organism work), inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4746 | 3134 | -34.0% | -3567 to +342.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7590 | 5543 | -27.0% | -5761 to +1667 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 78.85 | 72.2 | -8.4% | -9.752 to -3.566 | GAIN |
| failed requests (%) | 61.96 | 58.8 | -5.1% | -7.081 to +0.7714 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.947 | 9.922 | -0.2% | -0.09575 to +0.04619 | STEADY, inside the noise (cut) |
| pods started | 1.2 | 1.8 | +50.0% | -1.283 to +2.483 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.26e-15 to +1.615e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 289.2 | 289 | -0.0% | -1.489 to +1.218 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 289.2 | 289 | -0.0% | -1.489 to +1.218 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.301 | 3.284 | -0.5% | -0.05511 to +0.02027 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 98.28 | 98.35 | +0.1% | +0.01363 to +0.1278 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 2.093e+12 | 2.093e+12 | -0.0% | -2.232e+07 to -2.232e+07 | LOSS |
| organism energy (J) | 1.841e+12 | 1.84e+12 | -0.1% | -1.346e+09 to -1.346e+09 | GAIN |
| organism time over the line (% of steps) | 4.438 | 4.424 | -0.3% | -0.014 to -0.014 | GAIN |
| organism work per energy | 1.137 | 1.138 | +0.1% | +0.0008195 to +0.0008195 | GAIN |
| organism behind its window (s) | 0.7 | 1.32 | +88.6% | -0.1817 to +1.422 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: toward their aims on 7, away from them on 0, inside the noise on 5

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3636 | 2229 | -38.7% | -3508 to +693.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5453 | 3846 | -29.5% | -4139 to +924.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.02 | 43.43 | -14.9% | -12.25 to -2.941 | GAIN |
| failed requests (%) | 36.45 | 37 | +1.5% | -1.077 to +2.178 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.859 | 9.838 | -0.2% | -0.06704 to +0.02478 | STEADY, inside the noise (cut) |
| pods started | 3 | 3.4 | +13.3% | -1.015 to +1.815 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.612e-15 to +9.019e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.8 | 283.9 | -0.3% | -1.69 to -0.2377 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.8 | 283.9 | -0.3% | -1.69 to -0.2377 | GAIN |
| CPU used with Omni's own (cores), mean | 2.728 | 2.674 | -2.0% | -0.08059 to -0.02717 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 88.06 | 88.11 | +0.1% | -0.7103 to +0.8112 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 6.649e+12 | 6.649e+12 | +0.0% | +3.119e+07 to +3.119e+07 | GAIN |
| organism energy (J) | 1.098e+15 | 1.094e+15 | -0.4% | -3.961e+12 to -3.961e+12 | GAIN |
| organism time over the line (% of steps) | 1.468 | 1.45 | -1.2% | -0.0176 to -0.0176 | GAIN |
| organism work per energy | 0.006054 | 0.006076 | +0.4% | +2.194e-05 to +2.194e-05 | GAIN |
| organism behind its window (s) | 1.28 | 1.18 | -7.8% | -0.5966 to +0.3966 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: toward their aims on 6, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3089 | 2104 | -31.9% | -1710 to -259.4 | GAIN |
| response time (ms), 99th percentile | 5143 | 4608 | -10.4% | -1607 to +536.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 57.22 | 44.67 | -21.9% | -18.45 to -6.662 | GAIN |
| failed requests (%) | 38.11 | 36.24 | -4.9% | -4.011 to +0.2654 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.882 | 9.864 | -0.2% | -0.07718 to +0.04183 | STEADY, inside the noise (cut) |
| pods started | 2.8 | 3.2 | +14.3% | -1.015 to +1.815 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.376e-17 to +2.501e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 287.2 | 286.8 | -0.1% | -2.881 to +2.129 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.2 | 286.8 | -0.1% | -2.881 to +2.129 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.139 | 3.095 | -1.4% | -0.08674 to -0.001172 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 92.13 | 91.67 | -0.5% | -1.422 to +0.4999 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 2.105e+12 | 2.105e+12 | +0.0% | +1.498e+07 to +1.498e+07 | GAIN |
| organism energy (J) | 5.688e+12 | 5.677e+12 | -0.2% | -1.158e+10 to -1.158e+10 | GAIN |
| organism time over the line (% of steps) | 2.623 | 2.607 | -0.6% | -0.01618 to -0.01618 | GAIN |
| organism work per energy | 0.37 | 0.3708 | +0.2% | +0.0007577 to +0.0007577 | GAIN |
| organism behind its window (s) | 1.3 | 0.94 | -27.7% | -1.082 to +0.3618 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 100 copies: toward their aims on 5, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4130 | 2934 | -29.0% | -3853 to +1461 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6069 | 5141 | -15.3% | -3465 to +1608 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 66.65 | 60.82 | -8.7% | -10.12 to -1.539 | GAIN |
| failed requests (%) | 52.79 | 52.61 | -0.3% | -4.265 to +3.9 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.822 | 9.805 | -0.2% | -0.0367 to +0.003903 | STEADY, inside the noise (cut) |
| pods started | 4.6 | 4.6 | +0.0% | -0.8778 to +0.8778 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.919e-15 to +3.985e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.2 | 282.7 | -0.5% | -3.478 to +0.421 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.2 | 282.7 | -0.5% | -3.478 to +0.421 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.741 | 2.669 | -2.6% | -0.1119 to -0.03212 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 91.22 | 91.26 | +0.0% | -0.108 to +0.1832 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 6.672e+12 | 6.672e+12 | +0.0% | +3.119e+07 to +3.119e+07 | GAIN |
| organism energy (J) | 1.103e+15 | 1.099e+15 | -0.4% | -3.971e+12 to -3.971e+12 | GAIN |
| organism time over the line (% of steps) | 2.716 | 2.707 | -0.3% | -0.008417 to -0.008417 | GAIN |
| organism work per energy | 0.006047 | 0.006069 | +0.4% | +2.188e-05 to +2.188e-05 | GAIN |
| organism behind its window (s) | 1.92 | 2.38 | +24.0% | -0.2177 to +1.138 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 100 copies: toward their aims on 4, away from them on 1 (organism work), inside the noise on 6; OFF THE CLOCK in 3 of 5 repetitions (the organism ended up to 277 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2922 | 2457 | -15.9% | -938.2 to +7.994 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4285 | 3813 | -11.0% | -1618 to +674.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 62.16 | 53.09 | -14.6% | -14.48 to -3.66 | GAIN |
| failed requests (%) | 43.92 | 39.65 | -9.7% | -9.933 to +1.397 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.767 | 9.773 | +0.1% | -0.0497 to +0.06103 | STEADY, inside the noise (up) |
| pods started | 5.4 | 5.4 | +0.0% | +0 to +0 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.243e-16 to +1.79e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 282.2 | 281.9 | -0.1% | -2.282 to +1.656 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 282.2 | 281.9 | -0.1% | -2.282 to +1.656 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.672 | 2.654 | -0.7% | -0.2459 to +0.2099 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 91.33 | 93.49 | +2.4% | -1.444 to +5.766 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.294e+13 | 1.294e+13 | -0.0% | -9.978e+07 to -9.978e+07 | LOSS |
| organism energy (J) | 1.104e+15 | 1.1e+15 | -0.4% | -4.052e+12 to -4.052e+12 | GAIN |
| organism time over the line (% of steps) | 2.595 | 2.577 | -0.7% | -0.01821 to -0.01821 | GAIN |
| organism work per energy | 0.01172 | 0.01176 | +0.4% | +4.308e-05 to +4.308e-05 | GAIN |
| organism behind its window (s) | 5.92 | 149.2 | +2420.3% | -19.29 to +305.8 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
