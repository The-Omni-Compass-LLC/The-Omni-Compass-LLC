# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,909 | -0.0% | -5.66 to 3.43 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,914 | -0.0% | -5.64 to 4.82 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.21 | 0.213 | +1.7% | -0.00432 to 0.0117 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.378 | 0.386 | +2.2% | -0.0125 to 0.0292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.149 | 0.148 | -0.5% | -0.0166 to 0.0153 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 764 | +49.3% | 45.6 to 459 | power given |
| bytes in the cache, mean (MB) | 419 | 608 | +45.0% | 39.7 to 338 | power given |
| pages read into the cache (misses) | 724,651 | 498,247 | -31.2% | -517,881 to 65,073 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.167 | +7.0% | -0.0234 to 0.0453 | STEADY, no difference beyond the noise |
| host CPU-seconds | 281 | 304 | +8.1% | -48.9 to 94.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.228 | +8.1% | -0.0364 to 0.0707 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 152 | 150 | -1.4% | -5.46 to 1.28 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 150 | 147 | -1.8% | -6.08 to 0.774 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2 | 2.57 | +28.3% | 0.505 to 0.627 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 281 | 304 | +8.1% | -48.9 to 94.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,880 | -0.0% | -3.58 to 1.07 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -3.14 to 0.475 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.429 | 0.432 | +0.7% | 0.000516 to 0.00548 | LOSS |
| latency, 99th percentile (ms) | 0.596 | 0.597 | +0.3% | -0.0258 to 0.0291 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.216 | +0.4% | -0.00778 to 0.00945 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 533 | +4.1% | -70.1 to 113 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 420 | +4.5% | -57.8 to 93.7 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 264,367 | 254,011 | -3.9% | -38,257 to 17,545 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.191 | -9.3% | -0.115 to 0.0758 | STEADY, no difference beyond the noise |
| host CPU-seconds | 150 | 132 | -11.7% | -99 to 64 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.282 | 0.249 | -11.7% | -0.186 to 0.12 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80.8 | 80.9 | +0.1% | -6.32 to 6.45 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79.8 | 79.6 | -0.2% | -6.52 to 6.19 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.03 | 1.26 | +22.3% | 0.192 to 0.266 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 150 | 132 | -11.7% | -99 to 64 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,936 | +0.0% | -6.25 to 6.49 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,937 | +0.0% | -6.34 to 6.59 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0953 | 0.0993 | +4.2% | -0.00461 to 0.0126 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.29 | 0.295 | +1.7% | -0.0332 to 0.0432 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0599 | 0.061 | +1.8% | -0.00158 to 0.00379 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 421 | +0.3% | -5.18 to 7.41 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 703,259 | 716,327 | +1.9% | -59,573 to 85,707 | shown, not judged |
| host CPU busy (share of the run) | 0.0879 | 0.0861 | -2.1% | -0.0156 to 0.0119 | STEADY, no difference beyond the noise |
| host CPU-seconds | 161 | 157 | -2.4% | -30.7 to 22.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.12 | 0.117 | -2.4% | -0.023 to 0.0172 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 52 | 53.3 | +2.7% | -2.06 to 4.84 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50 | 50.9 | +1.8% | -2.24 to 4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.96 | 2.47 | +26.1% | 0.178 to 0.843 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 161 | 157 | -2.4% | -30.7 to 22.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,725 | 5,724 | -0.0% | -19.7 to 18.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,740 | 5,739 | -0.0% | -19.3 to 17.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.386 | 0.377 | -2.3% | -0.014 to -0.00403 | GAIN |
| latency, 99th percentile (ms) | 0.616 | 0.607 | -1.5% | -0.0198 to 0.00183 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.202 | -2.9% | -0.00861 to -0.00335 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,422 | +177.8% | 844 to 976 | power given |
| bytes in the cache, mean (MB) | 416 | 1,115 | +167.9% | 650 to 748 | power given |
| pages read into the cache (misses) | 688,482 | 239,113 | -65.3% | -478,464 to -420,275 | shown, not judged |
| host CPU busy (share of the run) | 0.303 | 0.286 | -5.6% | -0.0492 to 0.0152 | STEADY, no difference beyond the noise |
| host CPU-seconds | 563 | 522 | -7.2% | -123 to 41.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.197 | -7.2% | -0.0466 to 0.0162 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 299 | 289 | -3.5% | -10.6 to -10 | GAIN |
| the server's own CPU-seconds (mongod) | 294 | 283 | -3.8% | -11.6 to -10.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.87 | 5.69 | +16.7% | 0.608 to 1.02 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 563 | 522 | -7.2% | -123 to 41.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,902 | -0.1% | -12.2 to 5.64 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,914 | 2,911 | -0.1% | -14 to 8.41 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.222 | 0.22 | -1.2% | -0.0216 to 0.0163 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.42 | 0.418 | -0.6% | -0.0229 to 0.0176 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.16 | -0.4% | -0.00908 to 0.00775 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 772 | +50.8% | -621 to 1,142 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 592 | +41.4% | -394 to 741 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 677,544 | 494,846 | -27.0% | -749,978 to 384,582 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.174 | -15.5% | -0.0509 to -0.0128 | GAIN |
| host CPU-seconds | 374 | 304 | -18.6% | -118 to -20.8 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.228 | -18.5% | -0.0882 to -0.0155 | GAIN |
| cache size changes written (the knob's moves) | 0 | 13.7 |  | -43 to 70.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 212 | 209 | -1.4% | -14.9 to 9.05 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 210 | 206 | -1.7% | -15.5 to 8.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.04 | 2.57 | +26.2% | 0.446 to 0.622 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 374 | 304 | -18.6% | -118 to -20.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
