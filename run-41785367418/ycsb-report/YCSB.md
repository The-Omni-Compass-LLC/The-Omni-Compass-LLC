# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -1.58 to 1.41 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -0.901 to -0.00749 | LOSS |
| latency, 95th percentile (ms) | 0.325 | 0.325 | +0.1% | -0.0356 to 0.0363 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.521 | 0.523 | +0.5% | -0.0156 to 0.021 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.192 | +0.4% | -0.00651 to 0.00813 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -0.285 to 0.781 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,767 | 61,860 | +0.2% | -280 to 468 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.198 | +8.8% | -0.0468 to 0.0787 | STEADY, no difference beyond the noise |
| host CPU-seconds | 314 | 348 | +10.7% | -98.9 to 166 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.261 | +10.7% | -0.0744 to 0.125 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 187 | +0.5% | -4.19 to 5.95 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 184 | +0.4% | -4.37 to 5.98 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.59 | +2.9% | -0.0604 to 0.205 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 314 | 348 | +10.7% | -98.9 to 166 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,887 | +0.1% | -0.621 to 3.96 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,891 | +0.1% | -0.63 to 3.69 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.405 | 0.402 | -0.8% | -0.0145 to 0.00787 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 0.546 | +0.6% | -0.0108 to 0.0175 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.192 | +0.0% | -0.0047 to 0.00478 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,517 | +0.1% | -2.72 to 6.25 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,606 | 77,735 | +0.2% | 6.96 to 251 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.185 | -5.0% | -0.0232 to 0.0037 | STEADY, no difference beyond the noise |
| host CPU-seconds | 139 | 131 | -6.0% | -19.7 to 2.96 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.262 | 0.246 | -6.1% | -0.0372 to 0.00556 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 74.2 | 73.9 | -0.4% | -1.77 to 1.21 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 73.2 | 72.9 | -0.4% | -1.77 to 1.17 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.977 | 0.999 | +2.3% | -0.0298 to 0.0744 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 139 | 131 | -6.0% | -19.8 to 2.99 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,904 | +0.0% | -0.127 to 0.99 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,906 | +0.0% | 0.0941 to 0.706 | GAIN |
| latency, 95th percentile (ms) | 0.275 | 0.275 | -0.2% | -0.00826 to 0.00692 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.456 | +0.1% | -0.0393 to 0.04 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.145 | -0.4% | -0.00421 to 0.00302 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | -0.0% | -3.07 to 2.48 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,678 | 61,650 | -0.0% | -138 to 82.2 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.181 | +22.8% | 0.00787 to 0.0595 | power given |
| host CPU-seconds | 262 | 335 | +28.0% | 12.3 to 134 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.251 | +28.0% | 0.00916 to 0.101 | power given |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 132 | 132 | -0.2% | -3.29 to 2.83 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 129 | 129 | -0.2% | -3.26 to 2.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 2.63 | +3.1% | -0.0337 to 0.192 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 262 | 335 | +28.0% | 12.3 to 134 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,829 | 5,835 | +0.1% | -10.6 to 22.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,834 | 5,840 | +0.1% | -11 to 22.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.166 | 0.167 | +1.0% | -0.0198 to 0.0231 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.376 | 0.385 | +2.5% | -0.0114 to 0.03 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0833 | 0.0824 | -1.2% | -0.0074 to 0.00547 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,365 | +0.1% | -7.41 to 9.26 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,269 | 63,470 | +0.3% | -202 to 604 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.125 | +2.4% | -0.0259 to 0.0317 | STEADY, no difference beyond the noise |
| host CPU-seconds | 221 | 228 | +2.9% | -49.9 to 63 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0826 | 0.085 | +2.9% | -0.0187 to 0.0235 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 107 | 105 | -1.9% | -12.4 to 8.27 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 104 | 102 | -1.9% | -11.8 to 7.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.51 | 3.4 | -3.2% | -0.626 to 0.398 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 221 | 228 | +2.9% | -50 to 63 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,896 | -0.0% | -1.22 to 0.935 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,902 | +0.0% | -2.2 to 2.56 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.324 | +0.4% | -0.0128 to 0.0155 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.585 | 0.585 | +0.0% | -0.0245 to 0.0245 | STEADY, the same |
| latency, mean (ms) | 0.173 | 0.172 | -0.1% | -0.00451 to 0.00401 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | -0.0% | -5.57 to 5.22 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,022 | 63,146 | +0.2% | -86.2 to 335 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.178 | -6.7% | -0.0535 to 0.0278 | STEADY, no difference beyond the noise |
| host CPU-seconds | 341 | 314 | -8.0% | -113 to 58.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.236 | -8.0% | -0.085 to 0.0442 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 186 | -0.2% | -2.62 to 1.86 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 183 | -0.3% | -2.66 to 1.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.58 | 2.68 | +3.6% | -0.104 to 0.291 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 341 | 314 | -8.0% | -113 to 58.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
