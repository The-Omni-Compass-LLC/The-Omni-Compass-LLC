# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,943 | +0.0% | -0.941 to 1.25 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,944 | 2,945 | +0.0% | -1.01 to 1.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.093 | 0.0963 | +3.6% | -0.00787 to 0.0145 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.235 | 0.25 | +6.4% | -0.0484 to 0.0784 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0504 | 0.0512 | +1.5% | -0.00333 to 0.00487 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | -0.1% | -1.51 to -0.0529 | GAIN |
| pages read into the cache (misses) | 61,809 | 61,844 | +0.1% | -261 to 330 | shown, not judged |
| host CPU busy (share of the run) | 0.0641 | 0.0884 | +38.0% | 0.00547 to 0.0433 | power given |
| host CPU-seconds | 115 | 164 | +41.7% | 10.7 to 85.6 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.0861 | 0.122 | +41.7% | 0.00792 to 0.0639 | power given |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 43.3 | 43.5 | +0.6% | -1.87 to 2.36 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 41.7 | 42 | +0.5% | -1.9 to 2.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.56 | 1.59 | +1.8% | 0.00525 to 0.0515 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 115 | 164 | +41.7% | 10.7 to 85.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,906 | -0.0% | -3.13 to 2.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,915 | +0.0% | -4.15 to 4.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.328 | +3.7% | -0.0395 to 0.0628 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.44 | +0.2% | -0.0284 to 0.0298 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.148 | 0.149 | +0.8% | -0.00283 to 0.00509 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,519 | 1,519 | +0.0% | -3.09 to 3.76 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,695 | 77,691 | -0.0% | -77.4 to 69.4 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.172 | +7.6% | -0.0622 to 0.0865 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 127 | +9.7% | -54.3 to 76.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.238 | +9.7% | -0.102 to 0.144 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 58.1 | 58 | -0.1% | -0.95 to 0.805 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 57.3 | 57.3 | -0.1% | -0.988 to 0.835 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.78 | 0.784 | +0.5% | -0.0753 to 0.0838 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 116 | 127 | +9.7% | -54.3 to 76.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.0% | -3.06 to 1.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,892 | -0.0% | -2.45 to 1.34 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.29 | 0.292 | +0.5% | -0.00665 to 0.00932 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.493 | 0.494 | +0.3% | -0.000101 to 0.00277 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.182 | 0.184 | +1.2% | 0.001 to 0.00322 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | +0.1% | -2.01 to 4.65 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,606 | 61,689 | +0.1% | -151 to 316 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.193 | +8.0% | -0.0531 to 0.0817 | STEADY, no difference beyond the noise |
| host CPU-seconds | 313 | 343 | +9.8% | -118 to 179 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.235 | 0.258 | +9.8% | -0.0881 to 0.134 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 174 | 176 | +1.2% | 0.901 to 3.43 | power given |
| the server's own CPU-seconds (mongod) | 172 | 174 | +1.2% | 0.881 to 3.15 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.41 | 2.56 | +6.2% | -0.0224 to 0.32 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 313 | 343 | +9.8% | -118 to 179 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,670 | 5,670 | -0.0% | -1.74 to 0.474 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,687 | 5,687 | -0.0% | -2.96 to 2.64 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.42 | 0.423 | +0.7% | -0.0108 to 0.0168 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.666 | 0.669 | +0.5% | -0.0329 to 0.0395 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.24 | 0.241 | +0.7% | -0.00658 to 0.0101 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,362 | -0.0% | -1.54 to 1.45 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,723 | 62,879 | +0.2% | -1,471 to 1,783 | shown, not judged |
| host CPU busy (share of the run) | 0.314 | 0.319 | +1.5% | -0.0173 to 0.0268 | STEADY, no difference beyond the noise |
| host CPU-seconds | 568 | 578 | +1.8% | -41.3 to 62 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.218 | +1.8% | -0.0153 to 0.0232 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 313 | 317 | +1.2% | -10.9 to 18.4 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 309 | 312 | +1.2% | -10.7 to 17.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.38 | 4.51 | +3.0% | -0.296 to 0.556 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 568 | 578 | +1.8% | -41.3 to 62 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,882 | +0.0% | -1.35 to 2.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -1.43 to 2.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.341 | 0.346 | +1.7% | 0.00187 to 0.00946 | LOSS |
| latency, 99th percentile (ms) | 0.545 | 0.546 | +0.2% | -0.0175 to 0.0201 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.207 | +0.6% | -0.0048 to 0.00716 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | +0.0% | -4.67 to 5.52 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,024 | 63,056 | +0.1% | -425 to 489 | shown, not judged |
| host CPU busy (share of the run) | 0.222 | 0.219 | -1.1% | -0.0718 to 0.0667 | STEADY, no difference beyond the noise |
| host CPU-seconds | 388 | 381 | -1.8% | -159 to 146 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.292 | 0.287 | -1.8% | -0.12 to 0.11 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 234 | 234 | +0.1% | -11.8 to 12.2 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 232 | 232 | +0.1% | -11.8 to 12.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.53 | 2.61 | +3.4% | -0.0448 to 0.215 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 388 | 381 | -1.8% | -159 to 146 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
