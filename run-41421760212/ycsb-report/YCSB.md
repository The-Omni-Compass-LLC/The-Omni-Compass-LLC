# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -3.93 to 2.24 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -2.3 to 0.883 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.331 | 0.336 | +1.7% | -0.00192 to 0.0133 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.592 | 0.596 | +0.6% | -0.00637 to 0.0137 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.194 | +0.6% | -0.00181 to 0.00415 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,364 | -0.0% | -2.48 to 1.24 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,791 | 61,823 | +0.1% | -200 to 264 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.205 | +18.4% | 0.000121 to 0.0636 | power given |
| host CPU-seconds | 295 | 363 | +23.0% | 1.45 to 134 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.273 | +23.0% | 0.00115 to 0.101 | power given |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 185 | 187 | +0.7% | -1.85 to 4.55 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 183 | 184 | +0.7% | -2.04 to 4.49 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 2.67 | +5.0% | 0.0212 to 0.231 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 295 | 363 | +23.0% | 1.42 to 134 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,877 | +0.0% | -3.1 to 5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,886 | +0.0% | -1.75 to 3.49 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.528 | 0.528 | -0.1% | -0.0258 to 0.0252 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.681 | 0.683 | +0.2% | -0.0356 to 0.039 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.226 | +0.5% | -0.00614 to 0.00827 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,502 | 1,502 | +0.0% | -6.68 to 7.83 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,627 | 77,635 | +0.0% | -380 to 396 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.213 | +16.8% | -0.0619 to 0.123 | STEADY, no difference beyond the noise |
| host CPU-seconds | 126 | 152 | +20.6% | -54.2 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.286 | +20.6% | -0.102 to 0.199 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 78.2 | 78.3 | +0.1% | -2.8 to 2.96 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 77.2 | 77.2 | +0.1% | -2.78 to 2.91 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.02 | 1.04 | +1.7% | -0.0167 to 0.0521 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 126 | 152 | +20.6% | -54.2 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.0% | -1.5 to 0.0103 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% | -1.48 to 0.156 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.307 | +1.7% | -0.00638 to 0.0164 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.526 | 0.54 | +2.5% | 0.00213 to 0.0245 | LOSS |
| latency, mean (ms) | 0.187 | 0.189 | +1.1% | -0.0082 to 0.0121 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,347 | -0.0% | -2.33 to 1.45 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,609 | 61,602 | -0.0% | -154 to 140 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.185 | +1.4% | -0.0593 to 0.0643 | STEADY, no difference beyond the noise |
| host CPU-seconds | 317 | 322 | +1.7% | -127 to 138 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.238 | 0.242 | +1.7% | -0.0956 to 0.104 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 176 | 178 | +1.3% | -15.5 to 19.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 174 | 176 | +1.2% | -15.5 to 19.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.6 | 2.7 | +3.9% | 0.0414 to 0.163 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 317 | 322 | +1.7% | -127 to 138 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,671 | 5,665 | -0.1% | -39.1 to 27.3 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,681 | 5,676 | -0.1% | -35.8 to 26 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.402 | 0.405 | +0.7% | -0.00854 to 0.0139 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.589 | 0.601 | +2.0% | -0.0205 to 0.0445 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.227 | +1.2% | -0.00824 to 0.0137 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,362 | -0.1% | -7.92 to 5.11 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,991 | 63,103 | +0.2% | -954 to 1,179 | shown, not judged |
| host CPU busy (share of the run) | 0.288 | 0.297 | +3.0% | -0.0277 to 0.0451 | STEADY, no difference beyond the noise |
| host CPU-seconds | 521 | 542 | +4.0% | -65.9 to 107 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.205 | +4.1% | -0.0246 to 0.0407 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 309 | 312 | +0.9% | -9.52 to 15.3 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 305 | 308 | +0.9% | -9.33 to 14.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.29 | 4.42 | +3.2% | -0.217 to 0.491 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 521 | 542 | +4.0% | -65.9 to 108 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,882 | +0.0% | -1.47 to 3.34 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,888 | +0.0% | -0.947 to 2.57 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.345 | 0.349 | +1.0% | -0.00671 to 0.0134 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.548 | 0.539 | -1.6% | -0.0212 to 0.00384 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.206 | -0.8% | -0.00462 to 0.00143 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,364 | +0.2% | -8.43 to 13.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,925 | 63,343 | +0.7% | -621 to 1,458 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.212 | -5.3% | -0.0905 to 0.0668 | STEADY, no difference beyond the noise |
| host CPU-seconds | 392 | 365 | -6.7% | -205 to 152 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.295 | 0.275 | -6.8% | -0.154 to 0.114 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 235 | 234 | -0.4% | -3.93 to 2.08 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 232 | 231 | -0.4% | -3.96 to 1.88 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.63 | +4.3% | 0.0211 to 0.195 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 392 | 365 | -6.7% | -205 to 152 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
