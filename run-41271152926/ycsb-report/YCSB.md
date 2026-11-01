# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,912 | +0.1% | -2.38 to 6.26 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,916 | +0.1% | -0.379 to 3.89 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.206 | 0.206 | -0.2% | -0.0193 to 0.0186 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.367 | 0.372 | +1.5% | -0.0241 to 0.0348 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.146 | 0.141 | -3.6% | -0.00823 to -0.00236 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 585 | +14.3% | -242 to 389 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 475 | +13.5% | -193 to 306 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 726,235 | 635,357 | -12.5% | -244,628 to 62,873 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.17 | +20.0% | -0.0391 to 0.0958 | STEADY, no difference beyond the noise |
| host CPU-seconds | 250 | 311 | +24.4% | -89.8 to 212 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.233 | +24.4% | -0.0671 to 0.159 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 149 | 149 | +0.2% | -3.28 to 3.87 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 147 | 147 | -0.2% | -3.81 to 3.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.97 | 2.5 | +27.0% | 0.44 to 0.624 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 250 | 311 | +24.4% | -89.8 to 212 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,884 | -0.1% | -6.71 to 2.05 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.1% | -4.23 to 1.05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.486 | 0.493 | +1.4% | 0.000415 to 0.0129 | LOSS |
| latency, 99th percentile (ms) | 0.619 | 0.628 | +1.5% | -0.00415 to 0.0221 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.216 | +0.8% | -0.00336 to 0.00661 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 617 | +20.5% | -158 to 368 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 404 | 485 | +20.0% | -117 to 279 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 275,028 | 248,572 | -9.6% | -118,459 to 65,548 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.173 | -2.8% | -0.103 to 0.0929 | STEADY, no difference beyond the noise |
| host CPU-seconds | 123 | 119 | -3.7% | -86.6 to 77.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.223 | -3.6% | -0.162 to 0.146 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.7 | 77.7 | +0.1% | -4.14 to 4.24 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.8 | 76.6 | -0.2% | -4.4 to 4.07 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.92 | 1.13 | +23.2% | 0.147 to 0.28 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 123 | 119 | -3.7% | -86.5 to 77.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,908 | 2,907 | -0.0% | -4 to 1.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.0% | -3.62 to 1.35 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.254 | 0.261 | +2.6% | -0.00454 to 0.0179 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.495 | 0.503 | +1.7% | -0.00998 to 0.0266 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.117 | 0.119 | +1.8% | -0.00219 to 0.00642 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 530 | +3.6% | -60.9 to 97.8 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 431 | +3.7% | -47.4 to 78 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 657,252 | 682,466 | +3.8% | -145,355 to 195,783 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.134 | -12.0% | -0.0677 to 0.0312 | STEADY, no difference beyond the noise |
| host CPU-seconds | 281 | 242 | -14.1% | -142 to 62.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.181 | -14.0% | -0.106 to 0.0472 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 101 | 104 | +3.4% | -0.813 to 7.77 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 98.6 | 101 | +2.9% | -1.41 to 7.08 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.36 | 3 | +27.2% | 0.593 to 0.692 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 281 | 242 | -14.1% | -142 to 62.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,678 | 5,673 | -0.1% | -35.7 to 25.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,695 | 5,690 | -0.1% | -32.7 to 23.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.436 | 0.432 | -1.0% | -0.0161 to 0.00741 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.657 | 0.658 | +0.1% | -0.0346 to 0.0352 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.246 | -1.4% | -0.00911 to 0.00229 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,321 | +158.0% | 348 to 1,270 | power given |
| bytes in the cache, mean (MB) | 416 | 1,036 | +148.8% | 275 to 964 | power given |
| pages read into the cache (misses) | 680,364 | 287,126 | -57.8% | -606,540 to -179,936 | shown, not judged |
| host CPU busy (share of the run) | 0.333 | 0.334 | +0.2% | -0.0144 to 0.0158 | STEADY, no difference beyond the noise |
| host CPU-seconds | 603 | 608 | +0.8% | -24.4 to 33.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.229 | +0.8% | -0.0097 to 0.0135 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 358 | 352 | -1.6% | -12.7 to 1.14 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 354 | 347 | -1.8% | -12.9 to -0.172 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.47 | 5.23 | +17.0% | 0.21 to 1.31 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 603 | 608 | +0.8% | -24.4 to 33.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,873 | -0.0% | -7.05 to 5.66 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -6.22 to 3.99 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.381 | 0.362 | -4.8% | -0.0555 to 0.0189 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.641 | 0.631 | -1.6% | -0.0436 to 0.0236 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.219 | -2.3% | -0.0198 to 0.00956 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,439 | +181.1% | 821 to 1,034 | power given |
| bytes in the cache, mean (MB) | 417 | 1,127 | +170.2% | 627 to 793 | power given |
| pages read into the cache (misses) | 678,061 | 237,748 | -64.9% | -515,556 to -365,070 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.245 | -5.7% | -0.0817 to 0.052 | STEADY, no difference beyond the noise |
| host CPU-seconds | 459 | 427 | -6.9% | -182 to 119 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.346 | 0.322 | -6.9% | -0.136 to 0.0887 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | 1.87 to 9.46 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275 | 268 | -2.7% | -26 to 10.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 272 | 264 | -3.0% | -26.3 to 10 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.18 | +21.9% | 0.275 to 0.867 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 459 | 427 | -6.9% | -182 to 119 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
