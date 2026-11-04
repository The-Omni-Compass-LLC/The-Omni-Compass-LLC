# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,904 | +0.0% | -1.19 to 1.19 | STEADY, the same |
| throughput (operations a second) | 2,908 | 2,908 | +0.0% | -0.909 to 0.974 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.323 | +0.0% | -0.0151 to 0.0151 | STEADY, the same |
| latency, 99th percentile (ms) | 0.544 | 0.544 | +0.1% | -0.0124 to 0.0131 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.135 | 0.134 | -0.8% | -0.00509 to 0.00285 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -122 to 196 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 446 | +6.7% | -92.2 to 148 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 698,018 | 650,083 | -6.9% | -228,300 to 132,431 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.158 | +7.9% | -0.0415 to 0.0647 | STEADY, no difference beyond the noise |
| host CPU-seconds | 261 | 285 | +9.5% | -86.6 to 136 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.214 | +9.5% | -0.0649 to 0.102 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 124 | 123 | -0.7% | -5.05 to 3.43 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 121 | 120 | -1.2% | -5.73 to 2.79 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.49 | 3.16 | +26.6% | 0.555 to 0.771 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 261 | 285 | +9.5% | -86.6 to 136 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,882 | -0.0% | -2 to 0.61 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -0.965 to -0.472 | LOSS |
| latency, 95th percentile (ms) | 0.412 | 0.41 | -0.6% | -0.00859 to 0.00392 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.562 | 0.56 | -0.5% | -0.0107 to 0.00532 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.214 | -0.3% | -0.00883 to 0.00771 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 600 | +17.2% | -113 to 289 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 404 | 471 | +16.7% | -86.4 to 221 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 257,777 | 252,566 | -2.0% | -53,236 to 42,814 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.208 | +8.4% | -0.0697 to 0.102 | STEADY, no difference beyond the noise |
| host CPU-seconds | 133 | 147 | +10.6% | -61.2 to 89.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.251 | 0.277 | +10.6% | -0.115 to 0.168 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81.4 | 81 | -0.5% | -3.53 to 2.71 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 80.4 | 79.8 | -0.8% | -3.76 to 2.5 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1 | 1.22 | +21.6% | 0.144 to 0.289 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 133 | 147 | +10.6% | -61.2 to 89.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | +0.0% | -0.269 to 0.306 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,892 | +0.0% | -0.263 to 0.337 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.307 | 0.307 | -0.1% | -0.00832 to 0.00765 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.483 | 0.48 | -0.6% | -0.0247 to 0.0187 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.188 | -1.2% | -0.00732 to 0.00265 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 419 | +0.2% | -4.56 to 6.58 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 704,762 | 715,471 | +1.5% | -27,665 to 49,083 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.178 | -10.0% | -0.103 to 0.0633 | STEADY, no difference beyond the noise |
| host CPU-seconds | 350 | 308 | -12.2% | -216 to 131 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.231 | -12.2% | -0.162 to 0.0983 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 187 | -0.9% | -13.4 to 9.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 186 | 184 | -1.2% | -13.9 to 9.27 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 3.05 | +23.7% | 0.544 to 0.627 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 350 | 308 | -12.2% | -216 to 131 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,690 | 5,685 | -0.1% | -29.7 to 20.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,707 | 5,702 | -0.1% | -30.6 to 21.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.425 | 0.42 | -1.2% | -0.0158 to 0.00583 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.643 | 0.64 | -0.5% | -0.0161 to 0.00942 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.243 | 0.24 | -1.1% | -0.0101 to 0.00482 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,420 | +177.3% | 831 to 985 | power given |
| bytes in the cache, mean (MB) | 417 | 1,111 | +166.7% | 640 to 750 | power given |
| pages read into the cache (misses) | 686,865 | 253,331 | -63.1% | -520,394 to -346,674 | shown, not judged |
| host CPU busy (share of the run) | 0.32 | 0.315 | -1.6% | -0.0224 to 0.0121 | STEADY, no difference beyond the noise |
| host CPU-seconds | 576 | 567 | -1.5% | -50.5 to 32.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.214 | -1.5% | -0.0184 to 0.012 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 3.52 to 8.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 349 | 343 | -1.5% | -17.1 to 6.61 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 344 | 338 | -1.7% | -17.5 to 5.77 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.35 | 4.96 | +14.0% | 0.359 to 0.859 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 576 | 567 | -1.5% | -50.5 to 32.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,875 | -0.1% | -6.84 to 2.91 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,885 | -0.1% | -6.4 to 1.61 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.363 | 0.351 | -3.2% | -0.0303 to 0.00698 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.568 | -2.7% | -0.0323 to 0.000291 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.214 | -3.4% | -0.0214 to 0.00623 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,357 | +165.1% | 248 to 1,442 | power given |
| bytes in the cache, mean (MB) | 418 | 1,064 | +154.9% | 200 to 1,093 | power given |
| pages read into the cache (misses) | 670,909 | 258,673 | -61.4% | -681,362 to -143,110 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.253 | -2.2% | -0.0646 to 0.0531 | STEADY, no difference beyond the noise |
| host CPU-seconds | 458 | 450 | -1.7% | -139 to 123 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.345 | 0.339 | -1.7% | -0.104 to 0.0923 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 0.162 to 10.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275 | 264 | -3.9% | -31.5 to 10.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 272 | 261 | -4.2% | -32 to 9.3 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 3.15 | +24.1% | 0.342 to 0.882 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 458 | 450 | -1.7% | -139 to 123 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
