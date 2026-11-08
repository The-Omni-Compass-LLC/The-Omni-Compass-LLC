# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,909 | +0.1% | -4.51 to 8.92 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | -4.13 to 8.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.221 | 0.215 | -2.4% | -0.0222 to 0.0116 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.388 | 0.389 | +0.3% | -0.00557 to 0.00757 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.15 | 0.143 | -4.4% | -0.0144 to 0.00108 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 981 | +91.6% | 297 to 641 | power given |
| bytes in the cache, mean (MB) | 416 | 779 | +87.1% | 232 to 493 | power given |
| pages read into the cache (misses) | 711,088 | 340,676 | -52.1% | -511,491 to -229,333 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.159 | +6.6% | 0.00333 to 0.0163 | power given |
| host CPU-seconds | 266 | 288 | +8.3% | 10.5 to 33.8 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.199 | 0.215 | +8.3% | 0.00756 to 0.0255 | power given |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 152 | 146 | -4.3% | -8.81 to -4.3 | GAIN |
| the server's own CPU-seconds (mongod) | 150 | 143 | -4.7% | -9.28 to -4.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.08 | 2.56 | +23.3% | 0.349 to 0.618 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 266 | 288 | +8.3% | 10.5 to 33.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,884 | +0.0% | -1.3 to 2.8 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -1.24 to 2.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.42 | 0.411 | -2.1% | -0.0165 to -0.00155 | GAIN |
| latency, 99th percentile (ms) | 0.555 | 0.547 | -1.5% | -0.0201 to 0.00341 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.212 | -1.0% | -0.0111 to 0.00674 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 405 | 403 | -0.5% | -8.4 to 4.28 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 273,122 | 278,450 | +2.0% | -46,941 to 57,598 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.223 | +8.9% | -0.112 to 0.148 | STEADY, no difference beyond the noise |
| host CPU-seconds | 145 | 161 | +10.4% | -99.9 to 130 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.302 | +10.4% | -0.188 to 0.245 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.4 | 81.4 | -1.2% | -6.53 to 4.56 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81.3 | 80.1 | -1.5% | -6.73 to 4.3 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.02 | 1.26 | +22.7% | 0.184 to 0.28 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 145 | 161 | +10.4% | -99.9 to 130 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,888 | +0.1% | -0.454 to 3.42 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,892 | +0.0% | -0.473 to 3.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.309 | +0.2% | -0.0116 to 0.0129 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.485 | -0.3% | -0.00546 to 0.00213 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.19 | -0.1% | -0.00178 to 0.00149 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 419 | +0.0% | -4.69 to 4.7 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 689,983 | 672,749 | -2.5% | -104,765 to 70,297 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.2 | +6.9% | -0.0581 to 0.084 | STEADY, no difference beyond the noise |
| host CPU-seconds | 323 | 353 | +9.3% | -127 to 187 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.243 | 0.265 | +9.3% | -0.0951 to 0.14 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 188 | +1.0% | -4.23 to 8.11 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 185 | +0.7% | -4.97 to 7.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 3.13 | +24.5% | 0.47 to 0.76 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 323 | 353 | +9.3% | -127 to 187 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,683 | 5,682 | -0.0% | -32 to 30.3 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,699 | 5,698 | -0.0% | -32.4 to 30.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.414 | -1.6% | -0.0184 to 0.00507 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.636 | 0.636 | +0.0% | -0.0282 to 0.0282 | STEADY, the same |
| latency, mean (ms) | 0.241 | 0.236 | -2.0% | -0.0128 to 0.00305 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,390 | +171.4% | 554 to 1,201 | power given |
| bytes in the cache, mean (MB) | 417 | 1,089 | +161.5% | 431 to 914 | power given |
| pages read into the cache (misses) | 683,510 | 254,662 | -62.7% | -528,236 to -329,460 | shown, not judged |
| host CPU busy (share of the run) | 0.323 | 0.314 | -2.9% | -0.0361 to 0.0176 | STEADY, no difference beyond the noise |
| host CPU-seconds | 587 | 567 | -3.5% | -89.3 to 48.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.214 | -3.5% | -0.0345 to 0.0192 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | 0.495 to 10.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 347 | 337 | -2.9% | -23.5 to 3.31 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 342 | 332 | -3.1% | -24 to 2.65 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.32 | 4.91 | +13.7% | 0.515 to 0.67 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 587 | 567 | -3.5% | -89.3 to 48.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 7.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% | -5.45 to 3.81 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,906 | +0.0% | -3.19 to 3.24 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.359 | 0.338 | -5.8% | -0.0341 to -0.00785 | GAIN |
| latency, 99th percentile (ms) | 0.616 | 0.609 | -1.1% | -0.016 to 0.00196 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.163 | 0.157 | -3.8% | -0.00805 to -0.00421 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,578 | +208.2% | 915 to 1,218 | power given |
| bytes in the cache, mean (MB) | 417 | 1,218 | +192.1% | 686 to 916 | power given |
| pages read into the cache (misses) | 680,277 | 122,555 | -82.0% | -592,417 to -523,026 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.211 | +9.7% | -0.0157 to 0.0529 | STEADY, no difference beyond the noise |
| host CPU-seconds | 343 | 388 | +13.2% | -33.2 to 124 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.258 | 0.292 | +13.2% | -0.025 to 0.0932 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 16 |  | 7.39 to 24.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 197 | 185 | -6.0% | -12.9 to -10.6 | GAIN |
| the server's own CPU-seconds (mongod) | 194 | 182 | -6.4% | -13.5 to -11.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 3.14 | +26.4% | 0.475 to 0.836 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 343 | 388 | +13.2% | -33.2 to 124 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 8.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
