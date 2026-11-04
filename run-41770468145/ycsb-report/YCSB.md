# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,938 | +0.0% | -3.76 to 5.38 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,940 | +0.0% | -4.09 to 5.44 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.16 | 0.157 | -2.1% | -0.0372 to 0.0306 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.35 | 0.348 | -0.5% | -0.00792 to 0.00459 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0679 | 0.0672 | -1.0% | -0.00378 to 0.00243 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 421 | -0.0% | -6.43 to 6.1 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 714,433 | 733,829 | +2.7% | -120,496 to 159,288 | shown, not judged |
| host CPU busy (share of the run) | 0.085 | 0.0766 | -9.8% | -0.0361 to 0.0194 | STEADY, no difference beyond the noise |
| host CPU-seconds | 153 | 137 | -10.5% | -70.8 to 38.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.114 | 0.102 | -10.5% | -0.0529 to 0.0288 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.2 | 62.5 | +0.4% | -3.34 to 3.89 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 60.5 | 60.3 | -0.4% | -3.88 to 3.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.69 | 2.2 | +30.7% | 0.351 to 0.683 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 153 | 137 | -10.5% | -70.8 to 38.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | -0.0% | -6.05 to 5.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,886 | -0.0% | -4.73 to 4.19 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.418 | 0.424 | +1.4% | 0.00352 to 0.00848 | LOSS |
| latency, 99th percentile (ms) | 0.592 | 0.602 | +1.7% | -0.0334 to 0.0541 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.219 | +1.9% | -0.00448 to 0.0128 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 403 | 401 | -0.6% | -11.7 to 7.16 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 267,560 | 268,484 | +0.3% | -27,705 to 29,554 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.197 | +3.4% | -0.0662 to 0.0793 | STEADY, no difference beyond the noise |
| host CPU-seconds | 131 | 136 | +3.8% | -57 to 66.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.246 | 0.256 | +3.8% | -0.107 to 0.126 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82 | 83.6 | +2.0% | -2.48 to 5.73 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81 | 82.3 | +1.7% | -2.81 to 5.53 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.04 | 1.31 | +25.6% | 0.16 to 0.373 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 131 | 136 | +3.8% | -57 to 66.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | +0.0% | -1.99 to 2.79 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | +0.0% | -1.8 to 2.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.309 | -0.4% | -0.00759 to 0.00492 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.471 | 0.467 | -0.7% | -0.0177 to 0.011 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.191 | -0.1% | -0.0045 to 0.00414 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 421 | +0.4% | -2.36 to 5.91 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 730,234 | 725,901 | -0.6% | -104,806 to 96,138 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.189 | -2.6% | -0.0378 to 0.0277 | STEADY, no difference beyond the noise |
| host CPU-seconds | 339 | 328 | -3.3% | -84.2 to 61.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.246 | -3.4% | -0.0632 to 0.0462 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 189 | 189 | +0.3% | -4.93 to 5.91 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 186 | 186 | -0.0% | -5.36 to 5.18 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.6 | 3.18 | +22.2% | 0.411 to 0.746 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 339 | 328 | -3.3% | -84.2 to 61.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,747 | 5,717 | -0.5% | -174 to 114 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,763 | 5,733 | -0.5% | -165 to 106 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.318 | -1.8% | -0.0103 to -0.0017 | GAIN |
| latency, 99th percentile (ms) | 0.488 | 0.485 | -0.7% | -0.0402 to 0.0335 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.185 | -2.0% | -0.0211 to 0.0137 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,135 | +121.7% | 369 to 878 | power given |
| bytes in the cache, mean (MB) | 416 | 865 | +107.7% | 298 to 599 | power given |
| pages read into the cache (misses) | 687,090 | 250,042 | -63.6% | -513,043 to -361,054 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.246 | +0.8% | -0.0248 to 0.0289 | STEADY, no difference beyond the noise |
| host CPU-seconds | 439 | 446 | +1.7% | -50.8 to 65.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.168 | +2.2% | -0.0148 to 0.0221 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 15.7 |  | -7.42 to 38.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 274 | 266 | -2.6% | -14.2 to -0.193 | GAIN |
| the server's own CPU-seconds (mongod) | 270 | 262 | -2.9% | -14.5 to -0.999 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.54 | 4.08 | +15.3% | 0.272 to 0.807 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 439 | 446 | +1.7% | -50.8 to 65.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,897 | +0.1% | -2.86 to 5.95 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,907 | +0.0% | -5.03 to 7.03 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.346 | 0.34 | -1.8% | -0.0101 to -0.00254 | GAIN |
| latency, 99th percentile (ms) | 0.596 | 0.587 | -1.4% | -0.0545 to 0.0378 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.154 | -4.8% | -0.0106 to -0.00489 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,454 | +184.0% | 743 to 1,141 | power given |
| bytes in the cache, mean (MB) | 417 | 1,119 | +168.1% | 519 to 884 | power given |
| pages read into the cache (misses) | 679,376 | 168,063 | -75.3% | -595,550 to -427,077 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.183 | -10.4% | -0.116 to 0.0735 | STEADY, no difference beyond the noise |
| host CPU-seconds | 372 | 326 | -12.6% | -267 to 174 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.245 | -12.6% | -0.201 to 0.131 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 20.3 |  | 6.21 to 34.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 194 | 183 | -5.6% | -15.8 to -6.01 | GAIN |
| the server's own CPU-seconds (mongod) | 192 | 180 | -6.0% | -16.5 to -6.62 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.45 | 3.12 | +27.3% | 0.611 to 0.728 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 372 | 326 | -12.6% | -268 to 174 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
