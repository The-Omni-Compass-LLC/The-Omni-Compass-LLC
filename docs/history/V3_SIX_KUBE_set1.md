# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Source: GitHub Actions workflow `six-kube`, run 37501769448, commit `33b15eb` (Omni v3, `tools/omni_version.py --commit 33b15eb`), 2026-10-06; raw files under `results/live/raw/run-37501769448/`; 12 cells (10 and 100 copies of all six organisms), 5 paired repetitions each, 62 of 62 jobs finished. Made by `tools/six_kube_report.py` from those files; the 1,000-copy cells run on Azure (`docs/OMNI_V3.md`).


Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3733 | 2419 | 1924 | 1315 | 2603 | 1773 | 2420 | 1722 | 2852 | 1945 | 5863 | 4413 | 2876 | 2407 | 2383 | 1310 | 3669 | 2578 | 2659 | 1616 | 4561 | 4388 | 6442 | 4929 |
| response time (ms), 99th percentile | 6813 | 6802 | 5389 | 3858 | 5650 | 4557 | 4730 | 3922 | 4574 | 3560 | 8542 | 6072 | 4234 | 4255 | 3547 | 2907 | 5518 | 5750 | 3559 | 2353 | 6553 | 7348 | 8187 | 7378 |
| time over the response line (% of samples) | 68.58 | 51.52 | 46.13 | 32.33 | 66.51 | 52.1 | 39.82 | 32.16 | 38.1 | 25.72 | 82.2 | 71.48 | 48.07 | 42.97 | 36.29 | 29.65 | 64.2 | 56.86 | 34.06 | 28.55 | 70.36 | 58.93 | 83.74 | 74.76 |
| failed requests (%) | 41.14 | 37.7 | 25.95 | 23.93 | 43.19 | 39.45 | 24.92 | 23.68 | 16.72 | 14.82 | 63.63 | 59.38 | 38.59 | 35.38 | 25.57 | 23.93 | 49.59 | 46.41 | 27.24 | 24.55 | 39.83 | 38.34 | 56.78 | 59.23 |
| HPA replicas, mean | 9.87 | 9.83 | 9.712 | 9.737 | 9.881 | 9.853 | 9.726 | 9.731 | 9.697 | 9.734 | 9.927 | 9.929 | 9.812 | 9.814 | 9.784 | 9.777 | 9.818 | 9.875 | 9.751 | 9.764 | 9.808 | 9.816 | 9.815 | 9.841 |
| pods started | 2.2 | 2.8 | 4 | 3.8 | 2 | 2.6 | 3.6 | 3.6 | 4.2 | 4.2 | 1.2 | 1.4 | 3.8 | 3.6 | 5 | 4.6 | 3.8 | 2.6 | 4.8 | 4.8 | 4.8 | 4.8 | 4.8 | 4.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 193.8 | 194 | 189.6 | 189.8 | 193.3 | 193.8 | 187.3 | 187.8 | 188.7 | 188.2 | 194.7 | 193.4 | 281.3 | 281.4 | 279.4 | 277.7 | 285 | 284.8 | 278.1 | 276.7 | 286.9 | 286.2 | 285.7 | 284.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193.8 | 194 | 189.6 | 189.8 | 193.3 | 193.8 | 187.3 | 187.8 | 188.7 | 188.2 | 194.7 | 193.4 | 281.3 | 281.4 | 279.4 | 277.7 | 285 | 284.8 | 278.1 | 276.7 | 286.9 | 286.2 | 285.7 | 284.4 |
| CPU used with Omni's own (cores), mean | 3.348 | 3.331 | 2.943 | 2.925 | 3.314 | 3.316 | 2.712 | 2.704 | 2.818 | 2.773 | 3.322 | 3.286 | 2.782 | 2.744 | 2.627 | 2.542 | 3.03 | 2.978 | 2.514 | 2.453 | 3.135 | 3.059 | 3.02 | 2.934 |
| host CPU busy, the real machine under kind (%) | 96.7 | 96.66 | 85.11 | 85.05 | 96.14 | 96.32 | 78.35 | 78.72 | 81.72 | 80.88 | 98.56 | 98.59 | 82.35 | 82.29 | 78.47 | 77.14 | 89.91 | 90.09 | 74.15 | 73.59 | 96.45 | 97.03 | 98.87 | 99.01 |
| organism work | 2.159e+11 | 2.159e+11 | 2.147e+11 | 2.147e+11 | 6.677e+11 | 6.677e+11 | 2.159e+11 | 2.159e+11 | 6.7e+11 | 6.7e+11 | 1.294e+12 | 1.294e+12 | 2.104e+12 | 2.104e+12 | 2.093e+12 | 2.093e+12 | 6.649e+12 | 6.649e+12 | 2.105e+12 | 2.105e+12 | 6.672e+12 | 6.672e+12 | 1.294e+13 | 1.294e+13 |
| organism energy (J) | 1.518e+11 | 1.517e+11 | 1.881e+11 | 1.879e+11 | 1.103e+14 | 1.099e+14 | 5.653e+11 | 5.642e+11 | 1.108e+14 | 1.104e+14 | 1.082e+14 | 1.077e+14 | 1.48e+12 | 1.478e+12 | 1.841e+12 | 1.84e+12 | 1.098e+15 | 1.094e+15 | 5.688e+12 | 5.677e+12 | 1.103e+15 | 1.099e+15 | 1.104e+15 | 1.1e+15 |
| organism time over the line (% of steps) | 2.234 | 2.217 | 4.76 | 4.748 | 1.448 | 1.435 | 2.721 | 2.705 | 2.879 | 2.872 | 2.61 | 2.59 | 2.167 | 2.15 | 4.438 | 4.424 | 1.468 | 1.45 | 2.623 | 2.607 | 2.716 | 2.707 | 2.595 | 2.577 |
| organism work per energy | 1.422 | 1.423 | 1.142 | 1.143 | 0.006054 | 0.006075 | 0.3818 | 0.3826 | 0.006048 | 0.00607 | 0.01197 | 0.01201 | 1.422 | 1.423 | 1.137 | 1.138 | 0.006054 | 0.006076 | 0.37 | 0.3708 | 0.006047 | 0.006069 | 0.01172 | 0.01176 |
| organism behind its window (s) | 0.06 | 0.08 | 0.12 | 0.04 | 0.06 | 0.06 | 0.02 | 0.04 | 0.1 | 0.16 | 0.36 | 0.54 | 1 | 0.8 | 0.64 | 0.68 | 1.18 | 1.24 | 0.84 | 0.52 | 1.82 | 2.2 | 4.8 | 167.1 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 4, worse on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3733 | 2419 | -35.2% | -3064 to +434.8 | better (inside the noise) |
| response time (ms), 99th percentile | 6813 | 6802 | -0.2% | -3715 to +3693 | better (inside the noise) |
| time over the response line (% of samples) | 68.58 | 51.52 | -24.9% | -22.43 to -11.68 | better |
| failed requests (%) | 41.14 | 37.7 | -8.4% | -9.19 to +2.315 | better (inside the noise) |
| HPA replicas, mean | 9.87 | 9.83 | -0.4% | -0.2111 to +0.1319 | better (inside the noise) |
| pods started | 2.2 | 2.8 | +27.3% | -2.754 to +3.954 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.213e-15 to +2.568e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 193.8 | 194 | +0.1% | -0.1558 to +0.4185 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193.8 | 194 | +0.1% | -0.1558 to +0.4185 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.348 | 3.331 | -0.5% | -0.02443 to -0.01082 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 96.7 | 96.66 | -0.0% | -0.5287 to +0.4528 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+11 | 2.159e+11 | +0.0% | +4496 to +4496 | same (under one part in a million) |
| organism energy (J) | 1.518e+11 | 1.517e+11 | -0.1% | -1.321e+08 to -1.321e+08 | better |
| organism time over the line (% of steps) | 2.234 | 2.217 | -0.8% | -0.01715 to -0.01715 | better |
| organism work per energy | 1.422 | 1.423 | +0.1% | +0.001239 to +0.001239 | better |
| organism behind its window (s) | 0.06 | 0.08 | +33.3% | -0.08387 to +0.1239 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 4, worse on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1924 | 1315 | -31.7% | -1746 to +527.5 | better (inside the noise) |
| response time (ms), 99th percentile | 5389 | 3858 | -28.4% | -3758 to +694.9 | better (inside the noise) |
| time over the response line (% of samples) | 46.13 | 32.33 | -29.9% | -22.99 to -4.607 | better |
| failed requests (%) | 25.95 | 23.93 | -7.8% | -4.628 to +0.5895 | better (inside the noise) |
| HPA replicas, mean | 9.712 | 9.737 | +0.3% | -0.149 to +0.1992 | WORSE (inside the noise) |
| pods started | 4 | 3.8 | -5.0% | -3.031 to +2.631 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.1e-15 to +7.449e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.6 | 189.8 | +0.1% | -0.3266 to +0.7044 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.6 | 189.8 | +0.1% | -0.3266 to +0.7044 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.943 | 2.925 | -0.6% | -0.04806 to +0.01217 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.11 | 85.05 | -0.1% | -0.56 to +0.4293 | shown, not judged (more or less is not better by itself) |
| organism work | 2.147e+11 | 2.147e+11 | +0.0% | +4487 to +4487 | same (under one part in a million) |
| organism energy (J) | 1.881e+11 | 1.879e+11 | -0.1% | -1.443e+08 to -1.443e+08 | better |
| organism time over the line (% of steps) | 4.76 | 4.748 | -0.3% | -0.01197 to -0.01197 | better |
| organism work per energy | 1.142 | 1.143 | +0.1% | +0.0008765 to +0.0008766 | better |
| organism behind its window (s) | 0.12 | 0.04 | -66.7% | -0.1839 to +0.02387 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 5, worse on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2603 | 1773 | -31.9% | -2302 to +641.5 | better (inside the noise) |
| response time (ms), 99th percentile | 5650 | 4557 | -19.4% | -3498 to +1311 | better (inside the noise) |
| time over the response line (% of samples) | 66.51 | 52.1 | -21.7% | -17.76 to -11.07 | better |
| failed requests (%) | 43.19 | 39.45 | -8.7% | -5.685 to -1.797 | better |
| HPA replicas, mean | 9.881 | 9.853 | -0.3% | -0.1629 to +0.106 | better (inside the noise) |
| pods started | 2 | 2.6 | +30.0% | -2.258 to +3.458 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.989e-15 to +1.634e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 193.3 | 193.8 | +0.3% | -0.5766 to +1.632 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193.3 | 193.8 | +0.3% | -0.5766 to +1.632 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.314 | 3.316 | +0.1% | -0.01086 to +0.01564 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 96.14 | 96.32 | +0.2% | -0.166 to +0.514 | shown, not judged (more or less is not better by itself) |
| organism work | 6.677e+11 | 6.677e+11 | +0.0% | +4496 to +4496 | same (under one part in a million) |
| organism energy (J) | 1.103e+14 | 1.099e+14 | -0.3% | -3.828e+11 to -3.828e+11 | better |
| organism time over the line (% of steps) | 1.448 | 1.435 | -0.9% | -0.01348 to -0.01348 | better |
| organism work per energy | 0.006054 | 0.006075 | +0.3% | +2.109e-05 to +2.109e-05 | better |
| organism behind its window (s) | 0.06 | 0.06 | +0.0% | -0.1241 to +0.1241 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 4, worse on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2420 | 1722 | -28.8% | -2569 to +1175 | better (inside the noise) |
| response time (ms), 99th percentile | 4730 | 3922 | -17.1% | -2792 to +1176 | better (inside the noise) |
| time over the response line (% of samples) | 39.82 | 32.16 | -19.2% | -15.27 to -0.05189 | better |
| failed requests (%) | 24.92 | 23.68 | -5.0% | -3.306 to +0.8148 | better (inside the noise) |
| HPA replicas, mean | 9.726 | 9.731 | +0.1% | -0.05484 to +0.0647 | WORSE (inside the noise) |
| pods started | 3.6 | 3.6 | +0.0% | +0 to +0 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.754e-15 to +2.819e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.3 | 187.8 | +0.2% | -0.06524 to +0.9894 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.3 | 187.8 | +0.2% | -0.06524 to +0.9894 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.712 | 2.704 | -0.3% | -0.04148 to +0.02507 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.35 | 78.72 | +0.5% | -0.5354 to +1.277 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+11 | 2.159e+11 | +0.0% | +4733 to +4733 | same (under one part in a million) |
| organism energy (J) | 5.653e+11 | 5.642e+11 | -0.2% | -1.16e+09 to -1.16e+09 | better |
| organism time over the line (% of steps) | 2.721 | 2.705 | -0.6% | -0.01629 to -0.01629 | better |
| organism work per energy | 0.3818 | 0.3826 | +0.2% | +0.000785 to +0.0007851 | better |
| organism behind its window (s) | 0.02 | 0.04 | +100.0% | -0.03552 to +0.07552 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 4, worse on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2852 | 1945 | -31.8% | -2614 to +799.4 | better (inside the noise) |
| response time (ms), 99th percentile | 4574 | 3560 | -22.2% | -3087 to +1060 | better (inside the noise) |
| time over the response line (% of samples) | 38.1 | 25.72 | -32.5% | -21.65 to -3.107 | better |
| failed requests (%) | 16.72 | 14.82 | -11.4% | -5.932 to +2.124 | better (inside the noise) |
| HPA replicas, mean | 9.697 | 9.734 | +0.4% | -0.02691 to +0.1017 | WORSE (inside the noise) |
| pods started | 4.2 | 4.2 | +0.0% | -0.8778 to +0.8778 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.46e-16 to +2.878e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.7 | 188.2 | -0.3% | -1.631 to +0.6747 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.7 | 188.2 | -0.3% | -1.631 to +0.6747 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.818 | 2.773 | -1.6% | -0.1079 to +0.01643 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.72 | 80.88 | -1.0% | -2.786 to +1.118 | shown, not judged (more or less is not better by itself) |
| organism work | 6.7e+11 | 6.7e+11 | +0.0% | +4724 to +4724 | same (under one part in a million) |
| organism energy (J) | 1.108e+14 | 1.104e+14 | -0.3% | -3.838e+11 to -3.838e+11 | better |
| organism time over the line (% of steps) | 2.879 | 2.872 | -0.2% | -0.006746 to -0.006746 | better |
| organism work per energy | 0.006048 | 0.00607 | +0.3% | +2.103e-05 to +2.103e-05 | better |
| organism behind its window (s) | 0.1 | 0.16 | +60.0% | -0.007998 to +0.128 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 5, worse on 1 (organism work), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5863 | 4413 | -24.7% | -3980 to +1079 | better (inside the noise) |
| response time (ms), 99th percentile | 8542 | 6072 | -28.9% | -3396 to -1544 | better |
| time over the response line (% of samples) | 82.2 | 71.48 | -13.0% | -12.6 to -8.834 | better |
| failed requests (%) | 63.63 | 59.38 | -6.7% | -9.099 to +0.5961 | better (inside the noise) |
| HPA replicas, mean | 9.927 | 9.929 | +0.0% | -0.07819 to +0.08358 | WORSE (inside the noise) |
| pods started | 1.2 | 1.4 | +16.7% | -1.16 to +1.56 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.137e-15 to +7.104e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 194.7 | 193.4 | -0.7% | -3.388 to +0.783 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 194.7 | 193.4 | -0.7% | -3.388 to +0.783 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.322 | 3.286 | -1.1% | -0.05192 to -0.02029 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 98.56 | 98.59 | +0.0% | -0.1253 to +0.1828 | shown, not judged (more or less is not better by itself) |
| organism work | 1.294e+12 | 1.294e+12 | -0.0% | -7.802e+06 to -7.802e+06 | WORSE |
| organism energy (J) | 1.082e+14 | 1.077e+14 | -0.4% | -4.285e+11 to -4.285e+11 | better |
| organism time over the line (% of steps) | 2.61 | 2.59 | -0.8% | -0.01981 to -0.01981 | better |
| organism work per energy | 0.01197 | 0.01201 | +0.4% | +4.752e-05 to +4.752e-05 | better |
| organism behind its window (s) | 0.36 | 0.54 | +50.0% | -0.3119 to +0.6719 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: better on 5, worse on 1 (organism work), inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2876 | 2407 | -16.3% | -787.5 to -149.7 | better |
| response time (ms), 99th percentile | 4234 | 4255 | +0.5% | -848.3 to +889.9 | WORSE (inside the noise) |
| time over the response line (% of samples) | 48.07 | 42.97 | -10.6% | -9.617 to -0.577 | better |
| failed requests (%) | 38.59 | 35.38 | -8.3% | -7.497 to +1.08 | better (inside the noise) |
| HPA replicas, mean | 9.812 | 9.814 | +0.0% | -0.0342 to +0.03928 | WORSE (inside the noise) |
| pods started | 3.8 | 3.6 | -5.3% | -0.7552 to +0.3552 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.386e-15 to +1.03e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 281.3 | 281.4 | +0.1% | -1.36 to +1.642 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 281.3 | 281.4 | +0.1% | -1.36 to +1.642 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.782 | 2.744 | -1.4% | -0.05769 to -0.01793 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 82.35 | 82.29 | -0.1% | -0.3272 to +0.2144 | shown, not judged (more or less is not better by itself) |
| organism work | 2.104e+12 | 2.104e+12 | -0.0% | -1.579e+07 to -1.579e+07 | WORSE |
| organism energy (J) | 1.48e+12 | 1.478e+12 | -0.1% | -1.247e+09 to -1.247e+09 | better |
| organism time over the line (% of steps) | 2.167 | 2.15 | -0.8% | -0.01682 to -0.01681 | better |
| organism work per energy | 1.422 | 1.423 | +0.1% | +0.001189 to +0.001189 | better |
| organism behind its window (s) | 1 | 0.8 | -20.0% | -0.6561 to +0.2561 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 4, worse on 1 (organism work), inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2383 | 1310 | -45.0% | -2797 to +650.2 | better (inside the noise) |
| response time (ms), 99th percentile | 3547 | 2907 | -18.0% | -1179 to -100.8 | better |
| time over the response line (% of samples) | 36.29 | 29.65 | -18.3% | -13.34 to +0.05664 | better (inside the noise) |
| failed requests (%) | 25.57 | 23.93 | -6.4% | -5.508 to +2.235 | better (inside the noise) |
| HPA replicas, mean | 9.784 | 9.777 | -0.1% | -0.1153 to +0.1031 | better (inside the noise) |
| pods started | 5 | 4.6 | -8.0% | -2.655 to +1.855 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.312e-15 to +2.378e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 279.4 | 277.7 | -0.6% | -3.468 to +0.1422 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 279.4 | 277.7 | -0.6% | -3.468 to +0.1422 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.627 | 2.542 | -3.2% | -0.1294 to -0.04081 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.47 | 77.14 | -1.7% | -3.294 to +0.6379 | shown, not judged (more or less is not better by itself) |
| organism work | 2.093e+12 | 2.093e+12 | -0.0% | -2.232e+07 to -2.232e+07 | WORSE |
| organism energy (J) | 1.841e+12 | 1.84e+12 | -0.1% | -1.346e+09 to -1.346e+09 | better |
| organism time over the line (% of steps) | 4.438 | 4.424 | -0.3% | -0.014 to -0.014 | better |
| organism work per energy | 1.137 | 1.138 | +0.1% | +0.0008195 to +0.0008195 | better |
| organism behind its window (s) | 0.64 | 0.68 | +6.2% | -0.1015 to +0.1815 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 6, worse on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3669 | 2578 | -29.7% | -2138 to -42.49 | better |
| response time (ms), 99th percentile | 5518 | 5750 | +4.2% | -1529 to +1993 | WORSE (inside the noise) |
| time over the response line (% of samples) | 64.2 | 56.86 | -11.4% | -13.95 to -0.7257 | better |
| failed requests (%) | 49.59 | 46.41 | -6.4% | -7.612 to +1.251 | better (inside the noise) |
| HPA replicas, mean | 9.818 | 9.875 | +0.6% | -0.02826 to +0.1434 | WORSE (inside the noise) |
| pods started | 3.8 | 2.6 | -31.6% | -3.24 to +0.8399 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.567e-15 to +3.698e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285 | 284.8 | -0.1% | -1.964 to +1.65 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285 | 284.8 | -0.1% | -1.964 to +1.65 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.03 | 2.978 | -1.7% | -0.06977 to -0.03382 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.91 | 90.09 | +0.2% | -0.23 to +0.5879 | shown, not judged (more or less is not better by itself) |
| organism work | 6.649e+12 | 6.649e+12 | +0.0% | +3.119e+07 to +3.119e+07 | better |
| organism energy (J) | 1.098e+15 | 1.094e+15 | -0.4% | -3.961e+12 to -3.961e+12 | better |
| organism time over the line (% of steps) | 1.468 | 1.45 | -1.2% | -0.0176 to -0.0176 | better |
| organism work per energy | 0.006054 | 0.006076 | +0.4% | +2.194e-05 to +2.194e-05 | better |
| organism behind its window (s) | 1.18 | 1.24 | +5.1% | -0.7232 to +0.8432 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 6, worse on 0, inside the noise on 5

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2659 | 1616 | -39.2% | -2344 to +259.1 | better (inside the noise) |
| response time (ms), 99th percentile | 3559 | 2353 | -33.9% | -2545 to +134.2 | better (inside the noise) |
| time over the response line (% of samples) | 34.06 | 28.55 | -16.2% | -11.7 to +0.6838 | better (inside the noise) |
| failed requests (%) | 27.24 | 24.55 | -9.9% | -7.723 to +2.327 | better (inside the noise) |
| HPA replicas, mean | 9.751 | 9.764 | +0.1% | -0.01947 to +0.04642 | WORSE (inside the noise) |
| pods started | 4.8 | 4.8 | +0.0% | -0.8778 to +0.8778 | same |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.358e-15 to +1.648e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.1 | 276.7 | -0.5% | -2.545 to -0.1495 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.1 | 276.7 | -0.5% | -2.545 to -0.1495 | better |
| CPU used with Omni's own (cores), mean | 2.514 | 2.453 | -2.4% | -0.09387 to -0.02717 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.15 | 73.59 | -0.8% | -1.858 to +0.7421 | shown, not judged (more or less is not better by itself) |
| organism work | 2.105e+12 | 2.105e+12 | +0.0% | +1.498e+07 to +1.498e+07 | better |
| organism energy (J) | 5.688e+12 | 5.677e+12 | -0.2% | -1.158e+10 to -1.158e+10 | better |
| organism time over the line (% of steps) | 2.623 | 2.607 | -0.6% | -0.01618 to -0.01618 | better |
| organism work per energy | 0.37 | 0.3708 | +0.2% | +0.0007577 to +0.0007577 | better |
| organism behind its window (s) | 0.84 | 0.52 | -38.1% | -0.5421 to -0.09792 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 100 copies: better on 5, worse on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4561 | 4388 | -3.8% | -777.6 to +432 | better (inside the noise) |
| response time (ms), 99th percentile | 6553 | 7348 | +12.1% | -1251 to +2841 | WORSE (inside the noise) |
| time over the response line (% of samples) | 70.36 | 58.93 | -16.2% | -18.13 to -4.723 | better |
| failed requests (%) | 39.83 | 38.34 | -3.7% | -7.707 to +4.728 | better (inside the noise) |
| HPA replicas, mean | 9.808 | 9.816 | +0.1% | -0.06291 to +0.07857 | WORSE (inside the noise) |
| pods started | 4.8 | 4.8 | +0.0% | -0.8778 to +0.8778 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.312e-15 to +2.378e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 286.9 | 286.2 | -0.2% | -3.371 to +2.084 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.9 | 286.2 | -0.2% | -3.371 to +2.084 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.135 | 3.059 | -2.4% | -0.1319 to -0.0189 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 96.45 | 97.03 | +0.6% | -0.6938 to +1.85 | shown, not judged (more or less is not better by itself) |
| organism work | 6.672e+12 | 6.672e+12 | +0.0% | +3.119e+07 to +3.119e+07 | better |
| organism energy (J) | 1.103e+15 | 1.099e+15 | -0.4% | -3.971e+12 to -3.971e+12 | better |
| organism time over the line (% of steps) | 2.716 | 2.707 | -0.3% | -0.008417 to -0.008417 | better |
| organism work per energy | 0.006047 | 0.006069 | +0.4% | +2.188e-05 to +2.188e-05 | better |
| organism behind its window (s) | 1.82 | 2.2 | +20.9% | -0.3079 to +1.068 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 100 copies: better on 6, worse on 1 (organism work), inside the noise on 5; OFF THE CLOCK in 4 of 5 repetitions (the organism ended up to 277 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 6442 | 4929 | -23.5% | -4176 to +1150 | better (inside the noise) |
| response time (ms), 99th percentile | 8187 | 7378 | -9.9% | -3013 to +1395 | better (inside the noise) |
| time over the response line (% of samples) | 83.74 | 74.76 | -10.7% | -13.25 to -4.711 | better |
| failed requests (%) | 56.78 | 59.23 | +4.3% | -9.265 to +14.15 | WORSE (inside the noise) |
| HPA replicas, mean | 9.815 | 9.841 | +0.3% | -0.01895 to +0.07137 | WORSE (inside the noise) |
| pods started | 4.8 | 4.2 | -12.5% | -1.28 to +0.07998 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.03e-15 to +1.386e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.7 | 284.4 | -0.5% | -1.943 to -0.8127 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.7 | 284.4 | -0.5% | -1.943 to -0.8127 | better |
| CPU used with Omni's own (cores), mean | 3.02 | 2.934 | -2.8% | -0.1435 to -0.02859 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 98.87 | 99.01 | +0.1% | -0.06921 to +0.349 | shown, not judged (more or less is not better by itself) |
| organism work | 1.294e+13 | 1.294e+13 | -0.0% | -9.978e+07 to -9.978e+07 | WORSE |
| organism energy (J) | 1.104e+15 | 1.1e+15 | -0.4% | -4.052e+12 to -4.052e+12 | better |
| organism time over the line (% of steps) | 2.595 | 2.577 | -0.7% | -0.01821 to -0.01821 | better |
| organism work per energy | 0.01172 | 0.01176 | +0.4% | +4.308e-05 to +4.308e-05 | better |
| organism behind its window (s) | 4.8 | 167.1 | +3381.3% | +36.19 to +288.4 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
