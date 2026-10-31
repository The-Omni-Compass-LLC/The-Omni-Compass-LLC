# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Source: GitHub Actions workflow `big-organism`, run 37359820055 (the tower: one rented Azure machine per repetition, eastus, `Standard_D8as_v4`, 2,880 s window, commit `a004a8f`, Omni v1 for everything but the power grid) and workflow `big-organism-detached`, collection run 37575930111 (the four stacked: one rented machine, westus3, `Standard_D8as_v7`, three repetitions in turn under nohup, 2,880 s window, commit `f162ce8`, Omni v1; the machine collected and deleted when all three had finished); raw files under `results/live/raw/run-37359820055/` and `results/live/raw/run-37575930111/`. A fresh six-worker kind cluster per arm, the organism at 1,000 copies with the real cluster inside. Made by `tools/six_kube_report.py` from both. The stack's compass arm ended 300 to 615 s after its 2,880 s window in every repetition (native 14 s): marked OFF THE CLOCK; the v3 stack runs with a 10,800 s window for that reason.


Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`). The aim is lower for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). The aim is higher for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 1,000 copies: native | The whole tower, every muscle once, 1,000 copies: omni | The four stacked, duplicates kept, 1,000 copies: native | The four stacked, duplicates kept, 1,000 copies: omni |
|---|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4104 | 203.8 | 273.7 | 70.23 |
| response time (ms), 99th percentile | 6372 | 257.8 | 453.6 | 77.04 |
| time over the response line (% of samples) | 64.02 | 0.1645 | 0.7166 | 0 |
| failed requests (%) | 22.25 | 0 | 0 | 0 |
| HPA replicas, mean | 9.886 | 9.894 | 9.788 | 9.764 |
| pods started | 5 | 4.667 | 7 | 7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 541.8 | 540.8 | 504 | 504.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 541.8 | 540.8 | 504 | 504.9 |
| CPU used with Omni's own (cores), mean | 4.263 | 4.188 | 1.775 | 1.802 |
| host CPU busy, the real machine under kind (%) | 69.33 | 69.92 | 36.5 | 37.89 |
| organism work | 5.629e+13 | 5.629e+13 | 1.067e+14 | 1.067e+14 |
| organism energy (J) | 6.387e+13 | 6.375e+13 | 9.605e+13 | 9.59e+13 |
| organism time over the line (% of steps) | 2.722 | 2.714 | 2.568 | 2.546 |
| organism work per energy | 0.8814 | 0.883 | 1.111 | 1.112 |
| organism behind its window (s) | 802.5 | 408.3 | 14.5 | 456.8 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 1,000 copies: toward their aims on 6, away from them on 1 (organism work), inside the noise on 5; OFF THE CLOCK in 1 of 3 repetitions (the organism ended up to 2,392 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4104 | 203.8 | -95.0% | -6804 to -996.3 | GAIN |
| response time (ms), 99th percentile | 6372 | 257.8 | -96.0% | -8153 to -4075 | GAIN |
| time over the response line (% of samples) | 64.02 | 0.1645 | -99.7% | -99.52 to -28.19 | GAIN |
| failed requests (%) | 22.25 | 0 | -100.0% | -115.6 to +71.11 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.886 | 9.894 | +0.1% | -0.01703 to +0.0345 | STEADY, inside the noise (up) |
| pods started | 5 | 4.667 | -6.7% | -1.768 to +1.101 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.779e-16 to +1.57e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 541.8 | 540.8 | -0.2% | -6.524 to +4.494 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 541.8 | 540.8 | -0.2% | -6.524 to +4.494 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 4.263 | 4.188 | -1.8% | -0.6641 to +0.5131 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 69.33 | 69.92 | +0.9% | -6.106 to +7.288 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.629e+13 | 5.629e+13 | -0.0% | -9.426e+07 to -9.426e+07 | LOSS |
| organism energy (J) | 6.387e+13 | 6.375e+13 | -0.2% | -1.168e+11 to -1.168e+11 | GAIN |
| organism time over the line (% of steps) | 2.722 | 2.714 | -0.3% | -0.00788 to -0.00788 | GAIN |
| organism work per energy | 0.8814 | 0.883 | +0.2% | +0.001614 to +0.001614 | GAIN |
| organism behind its window (s) | 802.5 | 408.3 | -49.1% | -2104 to +1315 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 1,000 copies: toward their aims on 5, away from them on 1 (organism work), inside the noise on 4; OFF THE CLOCK in 3 of 3 repetitions (the organism ended up to 615 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 273.7 | 70.23 | -74.3% | -252.9 to -154 | GAIN |
| response time (ms), 99th percentile | 453.6 | 77.04 | -83.0% | -492.5 to -260.6 | GAIN |
| time over the response line (% of samples) | 0.7166 | 0 | -100.0% | -1.702 to +0.269 | STEADY, inside the noise (cut) |
| failed requests (%) | 0 | 0 | +0 | +0 to +0 | STEADY, the same |
| HPA replicas, mean | 9.788 | 9.764 | -0.2% | -0.08812 to +0.03989 | STEADY, inside the noise (cut) |
| pods started | 7 | 7 | +0.0% | +0 to +0 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.779e-16 to +1.57e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 504 | 504.9 | +0.2% | -4.344 to +6.001 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504 | 504.9 | +0.2% | -4.344 to +6.001 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.775 | 1.802 | +1.5% | -0.4546 to +0.5072 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 36.5 | 37.89 | +3.8% | -5.031 to +7.823 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.067e+14 | 1.067e+14 | -0.0% | -5.684e+08 to -5.684e+08 | LOSS |
| organism energy (J) | 9.605e+13 | 9.59e+13 | -0.2% | -1.539e+11 to -1.539e+11 | GAIN |
| organism time over the line (% of steps) | 2.568 | 2.546 | -0.9% | -0.02235 to -0.02235 | GAIN |
| organism work per energy | 1.111 | 1.112 | +0.2% | +0.001777 to +0.001777 | GAIN |
| organism behind its window (s) | 14.5 | 456.8 | +3050.1% | +86.26 to +798.3 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
