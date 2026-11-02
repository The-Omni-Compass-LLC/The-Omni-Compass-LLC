# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,906 | +0.0% | -2.47 to 3.73 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,909 | +0.0% | -2.51 to 3.87 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.282 | 0.287 | +1.7% | -0.0198 to 0.0292 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.518 | +0.3% | -0.0166 to 0.0193 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.119 | 0.119 | -0.0% | -0.00286 to 0.00284 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -0.94 to 1.09 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,770 | 61,847 | +0.1% | -220 to 375 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.118 | -14.9% | -0.0569 to 0.0156 | STEADY, no difference beyond the noise |
| host CPU-seconds | 250 | 207 | -17.0% | -116 to 31.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.155 | -17.0% | -0.0872 to 0.0234 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 103 | 103 | +0.0% | -2.89 to 2.97 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 101 | 101 | -0.1% | -2.94 to 2.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.39 | 2.49 | +3.9% | -0.017 to 0.205 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 250 | 207 | -17.0% | -116 to 31.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,883 | -0.0% | -1.73 to 1.05 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -2.06 to 1.05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.441 | 0.444 | +0.7% | -0.00838 to 0.0144 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.563 | 0.563 | +0.1% | -0.01 to 0.0107 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.215 | +1.1% | -0.00396 to 0.00861 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,513 | 1,512 | -0.1% | -5.76 to 3.47 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,644 | 77,755 | +0.1% | -52.3 to 276 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.202 | -10.9% | -0.0744 to 0.0251 | STEADY, no difference beyond the noise |
| host CPU-seconds | 165 | 142 | -13.7% | -67.5 to 22.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.31 | 0.268 | -13.7% | -0.127 to 0.042 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.1 | 77.9 | +1.0% | -4.31 to 5.92 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.1 | 76.9 | +1.0% | -4.39 to 5.93 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.02 | 1.05 | +3.2% | -0.0297 to 0.0951 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 165 | 142 | -13.7% | -67.5 to 22.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -2.66 to 2.61 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -2.11 to 2.34 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.295 | 0.295 | +0.0% | -0.00896 to 0.00896 | STEADY, the same |
| latency, 99th percentile (ms) | 0.5 | 0.503 | +0.6% | -0.00357 to 0.00957 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.184 | +0.4% | -0.00606 to 0.00766 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | -0.0% | -0.861 to -0.137 | GAIN |
| pages read into the cache (misses) | 61,630 | 61,612 | -0.0% | -49.7 to 13.7 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.167 | -12.3% | -0.112 to 0.0654 | STEADY, no difference beyond the noise |
| host CPU-seconds | 337 | 287 | -14.7% | -237 to 138 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.253 | 0.216 | -14.7% | -0.178 to 0.103 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 174 | 176 | +0.7% | -7.77 to 10.3 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 172 | 173 | +0.7% | -7.71 to 10.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 2.55 | +2.3% | -0.126 to 0.24 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 337 | 287 | -14.7% | -237 to 138 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,754 | 5,753 | -0.0% | -7.28 to 5.75 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,767 | 5,766 | -0.0% | -7.81 to 4.92 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.331 | +0.4% | -0.00384 to 0.0065 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.607 | 0.606 | -0.2% | -0.0267 to 0.024 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.154 | +0.1% | -0.00195 to 0.00219 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | -0.0% | -8.72 to 7.67 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,900 | 63,323 | +0.7% | 312 to 534 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.208 | -1.2% | -0.0345 to 0.0294 | STEADY, no difference beyond the noise |
| host CPU-seconds | 384 | 378 | -1.7% | -79.5 to 66.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.144 | 0.142 | -1.6% | -0.0299 to 0.0252 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 189 | +0.7% | -2.88 to 5.55 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 185 | +0.7% | -3.18 to 5.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.9 | 4.02 | +3.1% | -0.0598 to 0.305 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 384 | 378 | -1.7% | -79.5 to 66.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,878 | -0.0% | -2.66 to 1.74 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -2.01 to 1.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.347 | +2.0% | -0.0157 to 0.0291 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.62 | 0.627 | +1.1% | -0.00454 to 0.0179 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.211 | +0.9% | -0.00586 to 0.00954 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,361 | -0.1% | -5.59 to 4.19 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,163 | 63,124 | -0.1% | -592 to 513 | shown, not judged |
| host CPU busy (share of the run) | 0.218 | 0.229 | +5.2% | -0.0504 to 0.0732 | STEADY, no difference beyond the noise |
| host CPU-seconds | 379 | 405 | +6.9% | -110 to 163 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.285 | 0.305 | +6.9% | -0.0832 to 0.123 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 232 | 234 | +1.0% | -6.73 to 11.5 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 229 | 231 | +1.0% | -6.72 to 11.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 2.63 | +3.2% | -0.0144 to 0.175 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 379 | 405 | +6.9% | -110 to 163 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
