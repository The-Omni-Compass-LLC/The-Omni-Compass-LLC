# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,935 | +0.0% | -6.04 to 6.08 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,937 | +0.0% | -5.75 to 5.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.168 | 0.177 | +5.1% | -0.0545 to 0.0718 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.338 | 0.347 | +2.6% | -0.0537 to 0.071 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0699 | 0.0711 | +1.7% | -0.00596 to 0.00836 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 420 | 418 | -0.5% | -4.97 to 0.799 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 726,697 | 703,318 | -3.2% | -36,968 to -9,790 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.0972 | +1.4% | -0.0124 to 0.0151 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 177 | +1.5% | -23.1 to 28.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.131 | 0.133 | +1.6% | -0.0175 to 0.0215 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 65.6 | 66.7 | +1.8% | -4.45 to 6.74 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 63.8 | 64.5 | +1.0% | -4.89 to 6.15 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.72 | 2.24 | +30.0% | 0.319 to 0.715 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 175 | 177 | +1.6% | -23.2 to 28.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | +0.0% | -4.12 to 4.94 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,938 | +0.0% | -4.95 to 7.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.256 | 0.258 | +0.9% | -0.0449 to 0.0496 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.43 | +1.2% | -0.0657 to 0.0757 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0831 | 0.0838 | +0.9% | -0.0116 to 0.0132 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 716 | +39.8% | -309 to 717 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 563 | +39.1% | -243 to 559 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 262,990 | 225,494 | -14.3% | -85,604 to 10,612 | shown, not judged |
| host CPU busy (share of the run) | 0.077 | 0.0745 | -3.2% | -0.0838 to 0.0789 | EVEN, no difference beyond the noise |
| host CPU-seconds | 55.3 | 53.2 | -3.8% | -64.8 to 60.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.103 | 0.0995 | -3.8% | -0.121 to 0.113 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1 |  | -1.48 to 3.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 26.6 | 25.4 | -4.6% | -8.4 to 5.95 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 25.9 | 24.5 | -5.3% | -8.4 to 5.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.676 | 0.835 | +23.5% | 0.00361 to 0.314 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 55.3 | 53.2 | -3.8% | -64.8 to 60.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,897 | -0.0% | -2.81 to 2.75 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% | -2.88 to 2.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.284 | 0.279 | -1.9% | -0.0171 to 0.00641 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.419 | 0.414 | -1.1% | -0.0147 to 0.00537 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.176 | 0.173 | -1.6% | -0.0115 to 0.00578 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 421 | 419 | -0.5% | -4.43 to 0.513 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 746,995 | 668,331 | -10.5% | -130,136 to -27,192 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.171 | -6.3% | -0.1 to 0.0774 | EVEN, no difference beyond the noise |
| host CPU-seconds | 321 | 297 | -7.5% | -214 to 166 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.241 | 0.223 | -7.5% | -0.161 to 0.124 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 176 | 173 | -1.8% | -14.8 to 8.3 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 174 | 170 | -2.2% | -15.2 to 7.75 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.22 | 2.73 | +22.9% | 0.45 to 0.57 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 321 | 297 | -7.5% | -214 to 166 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,665 | 5,677 | +0.2% | -7.7 to 31 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,682 | 5,694 | +0.2% | -6.92 to 30.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.435 | 0.429 | -1.3% | -0.0157 to 0.00437 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.661 | 0.659 | -0.4% | -0.0273 to 0.0227 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.249 | 0.244 | -1.7% | -0.0102 to 0.00197 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,389 | +171.3% | 619 to 1,135 | power given |
| bytes in the cache, mean (MB) | 416 | 1,087 | +161.0% | 471 to 870 | power given |
| pages read into the cache (misses) | 679,186 | 239,938 | -64.7% | -462,435 to -416,060 | shown, not judged |
| host CPU busy (share of the run) | 0.327 | 0.327 | +0.1% | -0.00558 to 0.00621 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 593 | +0.6% | -6.65 to 13.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.224 | +0.4% | -0.00377 to 0.00548 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.33 |  | 2.54 to 10.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 356 | 349 | -2.0% | -12.6 to -1.51 | GAIN |
| the server's own CPU-seconds (mongod) | 352 | 344 | -2.2% | -13.3 to -2.43 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.36 | 5.13 | +17.9% | 0.589 to 0.967 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 589 | 593 | +0.6% | -6.61 to 13.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,899 | -0.0% | -6.67 to 4.34 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,909 | -0.0% | -8.25 to 6.63 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.337 | 0.325 | -3.5% | -0.0217 to -0.00163 | GAIN |
| latency, 99th percentile (ms) | 0.567 | 0.564 | -0.4% | -0.0427 to 0.0381 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.148 | -4.5% | -0.00939 to -0.00443 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,490 | +191.0% | 890 to 1,065 | power given |
| bytes in the cache, mean (MB) | 417 | 1,163 | +178.8% | 687 to 805 | power given |
| pages read into the cache (misses) | 682,438 | 168,077 | -75.4% | -624,224 to -404,497 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.199 | +0.8% | -0.0538 to 0.0569 | EVEN, no difference beyond the noise |
| host CPU-seconds | 360 | 364 | +1.3% | -116 to 125 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.27 | 0.274 | +1.4% | -0.0867 to 0.0941 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11 |  | 3.55 to 18.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 176 | -5.3% | -11.5 to -8.17 | GAIN |
| the server's own CPU-seconds (mongod) | 184 | 173 | -5.7% | -12.2 to -8.79 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.37 | 3.02 | +27.4% | 0.435 to 0.866 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 360 | 364 | +1.3% | -116 to 125 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
