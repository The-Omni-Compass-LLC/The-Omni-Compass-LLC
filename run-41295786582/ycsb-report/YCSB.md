# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,942 | +0.1% | -4.17 to 10.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,944 | +0.1% | -3.92 to 9.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.126 | 0.117 | -6.6% | -0.0177 to 0.00107 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.318 | 0.312 | -1.7% | -0.019 to 0.00835 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0634 | 0.0616 | -2.8% | -0.00419 to 0.000588 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 420 | +0.1% | -5.28 to 6.09 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 709,979 | 707,554 | -0.3% | -106,291 to 101,441 | shown, not judged |
| host CPU busy (share of the run) | 0.0753 | 0.0631 | -16.2% | -0.0711 to 0.0467 | STEADY, no difference beyond the noise |
| host CPU-seconds | 135 | 112 | -16.9% | -135 to 89 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.101 | 0.0838 | -16.9% | -0.101 to 0.0665 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 58.3 | 56 | -4.0% | -2.55 to -2.07 | GAIN |
| the server's own CPU-seconds (mongod) | 56.7 | 54.2 | -4.5% | -2.86 to -2.26 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.63 | 1.89 | +15.7% | -0.0504 to 0.563 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 135 | 112 | -16.9% | -135 to 89 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,890 | +0.0% | -2.04 to 3.02 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,893 | +0.0% | -2.17 to 3.42 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.363 | 0.365 | +0.5% | 0.000232 to 0.0031 | LOSS |
| latency, 99th percentile (ms) | 0.487 | 0.488 | +0.2% | -0.00796 to 0.00996 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.193 | +0.2% | -0.00283 to 0.00353 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 405 | 404 | -0.2% | -11.2 to 9.87 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 279,363 | 268,800 | -3.8% | -39,352 to 18,227 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.22 | +6.3% | -0.0461 to 0.0721 | STEADY, no difference beyond the noise |
| host CPU-seconds | 150 | 161 | +7.7% | -41.7 to 64.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.303 | +7.7% | -0.0782 to 0.121 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 78 | 77.9 | -0.1% | -0.948 to 0.83 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 77 | 76.8 | -0.4% | -1.13 to 0.585 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.959 | 1.17 | +22.4% | 0.17 to 0.258 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 150 | 161 | +7.7% | -41.7 to 64.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.0% | -3.89 to 2.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -3.76 to 3.01 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.311 | +0.6% | -0.00545 to 0.00945 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.481 | +0.8% | -0.000969 to 0.00897 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.189 | +0.3% | -0.00565 to 0.00695 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 538 | +5.0% | -84.5 to 136 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 438 | +4.4% | -63.7 to 101 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 681,010 | 656,875 | -3.5% | -186,961 to 138,691 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.173 | -3.3% | -0.0727 to 0.0607 | STEADY, no difference beyond the noise |
| host CPU-seconds | 309 | 296 | -4.4% | -157 to 130 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.222 | -4.4% | -0.118 to 0.0972 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 185 | 186 | +0.4% | -8.69 to 10.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 183 | 183 | +0.1% | -9.29 to 9.51 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.45 | 3.06 | +25.0% | 0.576 to 0.65 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 309 | 296 | -4.4% | -157 to 129 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,687 | 5,686 | -0.0% | -33.3 to 31.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,705 | 5,703 | -0.0% | -33.9 to 30.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.43 | 0.425 | -1.2% | -0.0116 to 0.00157 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.663 | 0.657 | -0.8% | -0.0228 to 0.0121 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.242 | -1.6% | -0.00632 to -0.00174 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,293 | +152.5% | 489 to 1,073 | power given |
| bytes in the cache, mean (MB) | 416 | 1,015 | +143.7% | 379 to 818 | power given |
| pages read into the cache (misses) | 684,308 | 301,784 | -55.9% | -418,356 to -346,692 | shown, not judged |
| host CPU busy (share of the run) | 0.323 | 0.322 | -0.6% | -0.0165 to 0.0129 | STEADY, no difference beyond the noise |
| host CPU-seconds | 585 | 582 | -0.6% | -37.7 to 31.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.219 | -0.5% | -0.0152 to 0.0128 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | -0.505 to 9.84 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 351 | 344 | -2.0% | -10 to -4.31 | GAIN |
| the server's own CPU-seconds (mongod) | 347 | 339 | -2.2% | -10.7 to -4.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.22 | 4.82 | +14.3% | 0.494 to 0.711 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 585 | 582 | -0.6% | -37.7 to 31.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,900 | +0.0% | -1.93 to 3.73 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,910 | +0.0% | -1.05 to 3.19 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.318 | -5.9% | -0.0379 to -0.00209 | GAIN |
| latency, 99th percentile (ms) | 0.587 | 0.577 | -1.7% | -0.015 to -0.00503 | GAIN |
| latency, mean (ms) | 0.155 | 0.147 | -5.1% | -0.013 to -0.0028 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,523 | +197.5% | 654 to 1,368 | power given |
| bytes in the cache, mean (MB) | 417 | 1,182 | +183.5% | 519 to 1,011 | power given |
| pages read into the cache (misses) | 684,142 | 153,260 | -77.6% | -689,611 to -372,153 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.198 | +1.4% | -0.0647 to 0.0701 | STEADY, no difference beyond the noise |
| host CPU-seconds | 354 | 363 | +2.5% | -140 to 158 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.266 | 0.273 | +2.5% | -0.105 to 0.119 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 13.3 |  | 3.29 to 23.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 175 | -6.2% | -22.1 to -1.15 | GAIN |
| the server's own CPU-seconds (mongod) | 184 | 172 | -6.6% | -22.7 to -1.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.36 | 2.94 | +24.6% | 0.471 to 0.69 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 354 | 363 | +2.5% | -140 to 158 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
