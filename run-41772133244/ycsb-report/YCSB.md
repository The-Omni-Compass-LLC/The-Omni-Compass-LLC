# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,883 | -0.0% | -5.95 to 3.22 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,889 | -0.0% | -5.68 to 2.83 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.328 | +3.3% | -0.0248 to 0.0455 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.591 | 0.592 | +0.2% | -0.0313 to 0.0333 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.193 | +1.2% | -0.000872 to 0.00558 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | +0.0% | -1.14 to 1.39 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,761 | 61,864 | +0.2% | -286 to 492 | shown, not judged |
| host CPU busy (share of the run) | 0.177 | 0.209 | +18.1% | 0.0259 to 0.0383 | power given |
| host CPU-seconds | 304 | 374 | +22.8% | 52.5 to 86.6 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.281 | +22.9% | 0.0393 to 0.0653 | power given |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 182 | 185 | +1.7% | 1.28 to 4.89 | power given |
| the server's own CPU-seconds (mongod) | 180 | 183 | +1.6% | 1.33 to 4.57 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 2.61 | +5.5% | -0.069 to 0.339 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 304 | 374 | +22.8% | 52.5 to 86.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,887 | +0.1% | -8.85 to 15.8 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,895 | +0.1% | -7.48 to 13.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.438 | 0.443 | +1.0% | -0.022 to 0.0307 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.662 | 0.659 | -0.5% | -0.0386 to 0.0319 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.161 | -0.0% | -0.00784 to 0.00781 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,510 | 1,510 | -0.0% | -1.73 to 1.43 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,633 | 77,650 | +0.0% | -512 to 545 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.147 | -1.2% | -0.129 to 0.126 | STEADY, no difference beyond the noise |
| host CPU-seconds | 107 | 105 | -1.3% | -107 to 104 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.199 | -1.3% | -0.203 to 0.197 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50.9 | 50.5 | -0.9% | -3.28 to 2.38 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 49.9 | 49.4 | -1.0% | -3.31 to 2.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.06 | +5.3% | 0.00895 to 0.0974 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 107 | 105 | -1.3% | -107 to 104 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,886 | -0.0% | -2.61 to 1.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% | -2.71 to 1.61 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.297 | 0.297 | +0.0% | -0.0114 to 0.0114 | STEADY, the same |
| latency, 99th percentile (ms) | 0.501 | 0.505 | +0.9% | -0.0128 to 0.0221 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.184 | 0.186 | +0.7% | -0.00501 to 0.00755 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,348 | -0.0% | -3.23 to 2.49 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,659 | 61,635 | -0.0% | -153 to 105 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.172 | +2.4% | -0.0448 to 0.0528 | STEADY, no difference beyond the noise |
| host CPU-seconds | 287 | 294 | +2.6% | -90.1 to 105 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.221 | +2.6% | -0.0677 to 0.079 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 176 | 178 | +0.7% | -6.63 to 9.14 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 174 | 175 | +0.7% | -6.56 to 8.89 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.61 | +3.5% | -0.0697 to 0.248 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 287 | 294 | +2.6% | -90.1 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,673 | 5,675 | +0.0% | -1.15 to 5.09 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,685 | 5,687 | +0.0% | -0.106 to 3.65 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.418 | 0.414 | -1.0% | -0.0083 to 0.000303 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.634 | 0.632 | -0.3% | -0.0214 to 0.0174 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.239 | 0.237 | -0.9% | -0.00775 to 0.00336 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,362 | +0.1% | -9.64 to 11.5 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,665 | 62,801 | +0.2% | -277 to 547 | shown, not judged |
| host CPU busy (share of the run) | 0.306 | 0.299 | -2.2% | -0.0252 to 0.0117 | STEADY, no difference beyond the noise |
| host CPU-seconds | 552 | 536 | -2.7% | -60.4 to 30.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.203 | -2.8% | -0.0232 to 0.0117 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 317 | 313 | -1.2% | -14.2 to 6.32 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 313 | 309 | -1.3% | -14.6 to 6.51 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.35 | 4.44 | +2.1% | -0.215 to 0.395 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 552 | 536 | -2.7% | -60.4 to 30.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,881 | +0.0% | -2.83 to 5.02 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,886 | +0.0% | -2.89 to 4.84 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.346 | 0.344 | -0.4% | -0.015 to 0.0123 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.54 | 0.537 | -0.6% | -0.0138 to 0.00783 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.206 | -0.8% | -0.00933 to 0.00593 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -2.74 to 1.11 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,264 | 63,188 | -0.1% | -540 to 390 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.233 | +1.4% | -0.0469 to 0.0531 | STEADY, no difference beyond the noise |
| host CPU-seconds | 402 | 410 | +1.9% | -103 to 118 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.303 | 0.308 | +1.9% | -0.0772 to 0.0888 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 237 | 234 | -1.1% | -12.9 to 7.58 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 234 | 231 | -1.2% | -12.9 to 7.42 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 2.69 | +3.2% | -0.0462 to 0.211 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 402 | 410 | +1.9% | -103 to 118 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
