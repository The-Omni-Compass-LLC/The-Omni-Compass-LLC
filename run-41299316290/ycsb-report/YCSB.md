# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,889 | -0.0% | -2.91 to 0.749 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,892 | -0.0% | -3.15 to 1.28 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.314 | +1.9% | -0.00483 to 0.0168 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.46 | +1.8% | 0.000744 to 0.0159 | LOSS |
| latency, mean (ms) | 0.179 | 0.181 | +1.0% | 0.000338 to 0.00323 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 525 | +2.5% | -42.2 to 67.8 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 429 | +2.9% | -30 to 54.5 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 714,973 | 712,157 | -0.4% | -154,134 to 148,504 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.206 | -1.1% | -0.0658 to 0.0612 | STEADY, no difference beyond the noise |
| host CPU-seconds | 378 | 370 | -2.1% | -156 to 141 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.283 | 0.278 | -2.0% | -0.117 to 0.106 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 190 | 193 | +1.5% | -0.74 to 6.35 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 188 | 190 | +1.1% | -1.58 to 5.78 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.43 | 3.13 | +28.9% | 0.539 to 0.863 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 378 | 370 | -2.1% | -156 to 141 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,881 | +0.0% | -4.16 to 5.82 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,890 | +0.0% | -1.64 to 3.71 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.461 | 0.459 | -0.4% | -0.0171 to 0.0131 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.686 | 0.683 | -0.4% | -0.0317 to 0.0257 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.211 | 0.212 | +0.5% | -0.00305 to 0.00529 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 403 | 404 | +0.2% | -3.55 to 5.34 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 259,438 | 272,203 | +4.9% | -10,913 to 36,444 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.185 | +18.6% | -0.00314 to 0.0612 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 129 | +22.8% | -1.36 to 49.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.243 | +22.8% | -0.0023 to 0.0923 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 75.9 | 76.9 | +1.3% | -1.06 to 2.97 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 74.9 | 75.7 | +1.0% | -1.21 to 2.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.99 | 1.19 | +20.2% | 0.15 to 0.25 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 105 | 129 | +22.8% | -1.35 to 49.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | +0.0% | -4.38 to 5.56 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | +0.0% | -4.03 to 5.22 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.318 | +0.1% | -0.00765 to 0.00832 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.503 | 0.501 | -0.4% | -0.026 to 0.022 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.193 | -0.8% | -0.0122 to 0.00925 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 419 | -0.1% | -10.1 to 9.53 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 719,301 | 699,736 | -2.7% | -273,485 to 234,354 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.185 | -12.1% | -0.0457 to -0.00526 | GAIN |
| host CPU-seconds | 376 | 320 | -14.7% | -102 to -8.3 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.282 | 0.241 | -14.7% | -0.0765 to -0.0064 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 190 | 189 | -0.5% | -13.4 to 11.6 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 188 | 186 | -0.8% | -13.8 to 10.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 3.12 | +23.2% | 0.35 to 0.828 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 376 | 320 | -14.7% | -102 to -8.31 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,679 | 5,673 | -0.1% | -31.7 to 21.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,696 | 5,690 | -0.1% | -33 to 22 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.43 | 0.423 | -1.6% | -0.0136 to -0.000427 | GAIN |
| latency, 99th percentile (ms) | 0.655 | 0.648 | -1.0% | -0.0194 to 0.00608 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.242 | -1.8% | -0.00734 to -0.00173 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,404 | +174.1% | 761 to 1,023 | power given |
| bytes in the cache, mean (MB) | 416 | 1,098 | +163.6% | 582 to 781 | power given |
| pages read into the cache (misses) | 685,459 | 257,458 | -62.4% | -480,534 to -375,468 | shown, not judged |
| host CPU busy (share of the run) | 0.328 | 0.324 | -1.4% | -0.038 to 0.029 | STEADY, no difference beyond the noise |
| host CPU-seconds | 597 | 588 | -1.4% | -95.8 to 78.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.222 | -1.3% | -0.0349 to 0.0289 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 353 | 344 | -2.6% | -19.1 to 0.943 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 349 | 339 | -2.8% | -19.5 to 0.0751 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.45 | 5.09 | +14.3% | 0.333 to 0.944 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 597 | 588 | -1.4% | -95.8 to 78.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,897 | -0.0% | -7.05 to 5.66 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,909 | +0.0% | -3.39 to 5.37 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.239 | 0.231 | -3.6% | -0.034 to 0.0167 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.455 | 0.453 | -0.4% | -0.0473 to 0.0433 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.174 | 0.172 | -1.1% | -0.0217 to 0.0179 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,114 | +117.5% | -134 to 1,338 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 844 | +102.2% | -76.3 to 929 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 676,860 | 262,877 | -61.2% | -744,610 to -83,355 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.215 | +8.3% | -0.0894 to 0.123 | STEADY, no difference beyond the noise |
| host CPU-seconds | 355 | 398 | +12.2% | -193 to 280 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.266 | 0.299 | +12.2% | -0.145 to 0.211 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 25.7 |  | -5.79 to 57.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 218 | 211 | -3.4% | -18.1 to 3.12 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 216 | 208 | -3.7% | -18.6 to 2.52 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.2 | 2.75 | +24.6% | 0.285 to 0.801 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 355 | 398 | +12.2% | -193 to 280 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
