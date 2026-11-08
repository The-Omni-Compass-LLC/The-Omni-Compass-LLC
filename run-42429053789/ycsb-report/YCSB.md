# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,910 | -0.0% | -2.02 to 1.29 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,915 | -0.0% | -0.546 to -0.124 | LOSS |
| latency, 95th percentile (ms) | 0.207 | 0.208 | +0.5% | -0.0119 to 0.0139 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.37 | 0.374 | +1.3% | -0.00654 to 0.0159 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.144 | -0.7% | -0.00915 to 0.00719 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 531 | +3.8% | -64.2 to 103 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 433 | +3.2% | -47.7 to 74.8 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 699,004 | 654,138 | -6.4% | -240,067 to 150,334 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.145 | -1.3% | -0.0216 to 0.0179 | STEADY, no difference beyond the noise |
| host CPU-seconds | 261 | 257 | -1.4% | -43.4 to 36.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.195 | 0.193 | -1.4% | -0.0326 to 0.0272 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 149 | 149 | -0.0% | -3.15 to 3.07 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 147 | 146 | -0.4% | -3.78 to 2.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.01 | 2.56 | +27.3% | 0.433 to 0.667 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 261 | 257 | -1.4% | -43.4 to 36.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,895 | +0.3% | -42.4 to 59.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,909 | +0.3% | -46.9 to 62.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.341 | +1.6% | -0.022 to 0.0327 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.546 | 0.547 | +0.2% | -0.0938 to 0.0958 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.18 | -5.4% | -0.0262 to 0.00565 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 966 | +88.6% | 140 to 767 | power given |
| bytes in the cache, mean (MB) | 398 | 753 | +89.3% | 112 to 598 | power given |
| pages read into the cache (misses) | 261,535 | 196,138 | -25.0% | -92,140 to -38,653 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.162 | +8.1% | -0.0369 to 0.0611 | STEADY, no difference beyond the noise |
| host CPU-seconds | 107 | 117 | +9.6% | -30.4 to 50.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.22 | +9.3% | -0.0581 to 0.0956 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.2 | 61.6 | -1.0% | -3.43 to 2.22 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61.4 | 60.6 | -1.3% | -3.65 to 2.02 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.782 | 0.987 | +26.2% | 0.145 to 0.265 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 107 | 117 | +9.6% | -30.4 to 50.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,914 | +0.0% | -2.45 to 2.98 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,916 | +0.0% | -1.55 to 1.64 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.186 | 0.185 | -0.7% | -0.00277 to 0.000101 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.349 | 0.345 | -1.1% | -0.0357 to 0.0284 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.134 | 0.134 | +0.1% | -0.00362 to 0.00388 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 419 | -0.1% | -4.73 to 3.61 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 721,553 | 697,941 | -3.3% | -79,239 to 32,017 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.141 | +3.5% | -0.0562 to 0.0657 | STEADY, no difference beyond the noise |
| host CPU-seconds | 241 | 252 | +4.3% | -117 to 137 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.188 | +4.3% | -0.0874 to 0.103 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 138 | 139 | +1.0% | -0.429 to 3.16 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 136 | 137 | +0.6% | -0.874 to 2.55 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.97 | 2.5 | +26.8% | 0.412 to 0.642 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 241 | 252 | +4.3% | -117 to 137 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,684 | 5,692 | +0.1% | -24 to 40.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,699 | 5,707 | +0.1% | -23.8 to 40.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.416 | -1.2% | -0.0164 to 0.00638 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.619 | 0.619 | +0.0% | -0.0131 to 0.0131 | STEADY, the same |
| latency, mean (ms) | 0.242 | 0.238 | -1.4% | -0.0132 to 0.00626 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,278 | +149.6% | 284 to 1,248 | power given |
| bytes in the cache, mean (MB) | 417 | 1,006 | +141.4% | 225 to 953 | power given |
| pages read into the cache (misses) | 678,592 | 290,724 | -57.2% | -565,147 to -210,588 | shown, not judged |
| host CPU busy (share of the run) | 0.323 | 0.319 | -1.2% | -0.0125 to 0.00506 | STEADY, no difference beyond the noise |
| host CPU-seconds | 583 | 575 | -1.4% | -26.4 to 10.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.216 | -1.6% | -0.0109 to 0.00395 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 349 | 343 | -1.7% | -22 to 9.94 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 345 | 338 | -2.0% | -22.5 to 9.06 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.29 | 4.97 | +16.0% | 0.32 to 1.05 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 583 | 575 | -1.4% | -26.4 to 10.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.0% | -2.08 to 0.345 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | -0.0% | -2.29 to 1.07 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.36 | 0.352 | -2.4% | -0.0223 to 0.00502 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.557 | 0.559 | +0.2% | -0.0303 to 0.033 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.214 | -2.3% | -0.0148 to 0.00462 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,387 | +170.9% | 549 to 1,201 | power given |
| bytes in the cache, mean (MB) | 418 | 1,088 | +160.2% | 430 to 909 | power given |
| pages read into the cache (misses) | 678,934 | 264,738 | -61.0% | -578,087 to -250,304 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.242 | +2.4% | -0.0772 to 0.0888 | STEADY, no difference beyond the noise |
| host CPU-seconds | 408 | 424 | +4.0% | -166 to 199 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.307 | 0.32 | +4.0% | -0.125 to 0.15 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.33 |  | 3.46 to 9.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 264 | -3.5% | -23.9 to 4.88 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 271 | 260 | -3.7% | -24.4 to 4.19 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.49 | 3.13 | +25.5% | 0.576 to 0.695 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 408 | 424 | +4.0% | -166 to 199 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
