# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.0% | -3.84 to 1.98 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -3.99 to 2.16 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.33 | +2.3% | -0.0115 to 0.0261 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.592 | 0.595 | +0.6% | -0.0143 to 0.021 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.202 | +0.7% | -0.00372 to 0.00646 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 532 | +3.9% | -65.6 to 105 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 433 | +3.6% | -59.5 to 89.8 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 708,007 | 689,861 | -2.6% | -46,896 to 10,605 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.19 | +12.0% | -0.0341 to 0.0747 | STEADY, no difference beyond the noise |
| host CPU-seconds | 286 | 328 | +14.5% | -74.6 to 158 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.246 | +14.6% | -0.056 to 0.119 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199 | 202 | +1.4% | -2.53 to 8.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 196 | 198 | +1.1% | -3.04 to 7.24 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.44 | 3.1 | +26.8% | 0.485 to 0.823 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 286 | 328 | +14.5% | -74.6 to 158 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,905 | -0.3% | -149 to 133 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,909 | -0.3% | -149 to 133 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.364 | 0.363 | -0.1% | -0.019 to 0.0183 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.525 | 0.513 | -2.2% | -0.073 to 0.0503 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.15 | 0.147 | -1.6% | -0.0394 to 0.0346 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 661 | +29.1% | -285 to 583 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 525 | +30.6% | -224 to 470 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 260,633 | 238,435 | -8.5% | -81,818 to 37,422 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.103 | -20.2% | -0.0514 to -0.000664 | GAIN |
| host CPU-seconds | 92.9 | 71.8 | -22.8% | -40.9 to -1.43 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.174 | 0.135 | -22.5% | -0.0804 to 0.00197 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 38.8 | 40.6 | +4.8% | -2.93 to 6.68 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 38 | 39.7 | +4.3% | -3.16 to 6.45 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.746 | 0.977 | +30.9% | 0.159 to 0.303 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 92.9 | 71.8 | -22.8% | -40.9 to -1.42 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,894 | +0.1% | -6.38 to 12.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,903 | 2,905 | +0.0% | -1.14 to 4.03 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.349 | -3.2% | -0.0554 to 0.0321 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.633 | 0.597 | -5.6% | -0.189 to 0.118 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.176 | 0.172 | -2.4% | -0.018 to 0.00956 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 418 | -0.4% | -7.54 to 3.98 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 705,437 | 691,505 | -2.0% | -81,895 to 54,032 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.18 | +0.7% | -0.0374 to 0.0398 | STEADY, no difference beyond the noise |
| host CPU-seconds | 321 | 325 | +1.2% | -85 to 92.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.245 | +1.1% | -0.0634 to 0.0688 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 159 | 157 | -1.2% | -10.6 to 6.92 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 156 | 154 | -1.6% | -11.1 to 6.13 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.66 | 3.31 | +24.5% | 0.517 to 0.789 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 321 | 325 | +1.2% | -85 to 92.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,736 | 5,739 | +0.1% | -15.4 to 22.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,758 | 5,761 | +0.1% | -11.7 to 17.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.354 | 0.348 | -1.8% | -0.0101 to -0.00254 | GAIN |
| latency, 99th percentile (ms) | 0.647 | 0.637 | -1.5% | -0.0214 to 0.00207 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.169 | 0.164 | -2.8% | -0.0078 to -0.00154 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,034 | +102.0% | -348 to 1,393 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 820 | +96.6% | -271 to 1,076 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 690,552 | 383,703 | -44.4% | -537,058 to -76,639 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.249 | +2.9% | -0.0163 to 0.0301 | STEADY, no difference beyond the noise |
| host CPU-seconds | 445 | 463 | +4.1% | -38.2 to 74.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.167 | 0.174 | +4.0% | -0.0139 to 0.0274 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | -4.06 to 13.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 232 | 227 | -2.2% | -12.1 to 1.85 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 228 | 222 | -2.5% | -12.7 to 1.11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.08 | 4.72 | +15.5% | 0.514 to 0.753 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 445 | 463 | +4.1% | -38.2 to 74.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,936 | -0.0% | -3.12 to 2.71 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,940 | -0.0% | -3.66 to 2.52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.143 | 0.148 | +3.5% | -0.0237 to 0.0337 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.386 | +1.0% | -0.0315 to 0.0388 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0792 | 0.0778 | -1.8% | -0.00552 to 0.00274 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 724 | +41.4% | -289 to 713 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 579 | +38.4% | -218 to 540 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 684,138 | 496,788 | -27.4% | -610,078 to 235,378 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.0859 | -19.3% | -0.0517 to 0.0106 | STEADY, no difference beyond the noise |
| host CPU-seconds | 193 | 151 | -21.5% | -109 to 26.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.144 | 0.113 | -21.5% | -0.0814 to 0.0196 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -2.97 to 6.97 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 101 | 101 | +0.6% | -7.93 to 9.2 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 99.1 | 99.2 | +0.1% | -8.42 to 8.63 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.56 | 2.09 | +34.0% | 0.478 to 0.582 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 193 | 151 | -21.5% | -109 to 26.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
