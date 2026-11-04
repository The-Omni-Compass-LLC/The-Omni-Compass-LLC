# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,887 | +0.0% | -3.01 to 3.37 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -2.51 to 2.79 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.316 | +2.5% | -0.0103 to 0.0256 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.507 | 0.506 | -0.2% | -0.0227 to 0.0207 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.188 | +1.3% | -0.00341 to 0.00834 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.1% | 0.0294 to 1.79 | power given |
| pages read into the cache (misses) | 61,737 | 61,844 | +0.2% | -167 to 381 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.186 | +7.9% | -0.0357 to 0.0629 | STEADY, no difference beyond the noise |
| host CPU-seconds | 294 | 323 | +9.7% | -76.9 to 134 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.242 | +9.7% | -0.058 to 0.101 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 181 | 185 | +2.1% | -3.25 to 10.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 178 | 182 | +2.1% | -3.47 to 11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.56 | 2.63 | +2.7% | -0.0855 to 0.222 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 294 | 323 | +9.7% | -76.9 to 134 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,880 | +0.0% | -1.32 to 2.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,889 | +0.0% | -2.44 to 4.68 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.448 | 0.451 | +0.7% | -0.00357 to 0.00957 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.636 | 0.635 | -0.1% | -0.0481 to 0.0474 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.215 | +0.1% | -0.00526 to 0.00559 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,511 | 1,511 | +0.0% | -1.66 to 2.17 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,651 | 77,754 | +0.1% | -75.6 to 281 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.185 | -4.7% | -0.0665 to 0.0484 | STEADY, no difference beyond the noise |
| host CPU-seconds | 136 | 128 | -5.9% | -56.9 to 40.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.257 | 0.242 | -5.9% | -0.107 to 0.077 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.8 | 77.8 | -0.0% | -1.73 to 1.71 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.8 | 76.7 | -0.1% | -1.77 to 1.68 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.988 | 1.02 | +3.4% | -0.0206 to 0.0876 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 136 | 128 | -5.9% | -56.9 to 40.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | +0.0% | -0.755 to 1.98 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,892 | +0.0% | -0.713 to 1.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.296 | 0.295 | -0.6% | -0.00546 to 0.00213 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.472 | 0.468 | -0.9% | -0.0123 to 0.00365 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.181 | -0.9% | -0.00488 to 0.00168 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | +0.0% | -1.81 to 2.39 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,609 | 61,619 | +0.0% | -75.6 to 94.9 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.169 | -12.3% | -0.0542 to 0.00704 | STEADY, no difference beyond the noise |
| host CPU-seconds | 339 | 289 | -14.8% | -116 to 15.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.217 | -14.8% | -0.0872 to 0.0117 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 177 | 175 | -1.1% | -5.06 to 1.01 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 174 | 172 | -1.2% | -5.12 to 0.891 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.49 | 2.58 | +3.7% | 0.000497 to 0.184 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 339 | 289 | -14.8% | -116 to 15.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,676 | 5,678 | +0.0% | -20.7 to 23.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,690 | 5,691 | +0.0% | -20.9 to 23.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.413 | +0.2% | -0.0181 to 0.0195 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.637 | -0.2% | -0.025 to 0.023 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.236 | +0.2% | -0.0115 to 0.0126 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,362 | -0.0% | -2.45 to 2.13 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,962 | 63,023 | +0.1% | -1,358 to 1,479 | shown, not judged |
| host CPU busy (share of the run) | 0.291 | 0.301 | +3.2% | -0.0139 to 0.0326 | STEADY, no difference beyond the noise |
| host CPU-seconds | 520 | 544 | +4.7% | -29.6 to 78.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.205 | +4.7% | -0.0115 to 0.03 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 309 | 311 | +0.5% | -18.5 to 21.7 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 305 | 307 | +0.5% | -18.6 to 21.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.31 | 4.42 | +2.5% | -0.219 to 0.432 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 520 | 544 | +4.7% | -29.6 to 78.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,906 | +0.0% | -4.44 to 4.91 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | +0.0% | -3.88 to 4.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.3 | 0.303 | +0.9% | -0.00768 to 0.013 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 0.546 | +0.5% | -0.00113 to 0.00646 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.138 | 0.138 | -0.2% | -0.00173 to 0.00126 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | -0.0% | -9.76 to 9.21 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,187 | 63,149 | -0.1% | -439 to 364 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.184 | +7.5% | -0.0247 to 0.0505 | STEADY, no difference beyond the noise |
| host CPU-seconds | 312 | 341 | +9.3% | -56.1 to 114 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.256 | +9.3% | -0.0423 to 0.0858 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 145 | 145 | +0.5% | -1.18 to 2.55 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 142 | 143 | +0.4% | -1.4 to 2.57 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.27 | 2.37 | +4.2% | -0.0268 to 0.216 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 312 | 341 | +9.3% | -56.1 to 114 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
