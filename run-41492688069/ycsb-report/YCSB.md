# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,934 | -0.1% | -6.56 to 1.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,936 | -0.1% | -6.61 to 1.72 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.161 | 0.195 | +21.6% | -0.0362 to 0.106 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.364 | 0.381 | +4.8% | -0.032 to 0.0667 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0695 | 0.0733 | +5.5% | -0.00311 to 0.0107 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 422 | +0.7% | 0.00592 to 6.11 | power given |
| pages read into the cache (misses) | 706,139 | 746,100 | +5.7% | 6,077 to 73,846 | shown, not judged |
| host CPU busy (share of the run) | 0.0961 | 0.094 | -2.3% | -0.0204 to 0.0161 | STEADY, no difference beyond the noise |
| host CPU-seconds | 175 | 170 | -3.2% | -44.4 to 33.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.131 | 0.127 | -3.1% | -0.033 to 0.0248 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 63.6 | 68.8 | +8.3% | -1.88 to 12.4 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61.9 | 66.5 | +7.5% | -2.48 to 11.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.7 | 2.32 | +36.5% | 0.521 to 0.72 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 175 | 170 | -3.2% | -44.4 to 33.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,878 | +0.0% | -0.965 to 3.16 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,888 | +0.0% | -1.87 to 4.06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.505 | 0.507 | +0.5% | -0.00914 to 0.0138 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.667 | 0.675 | +1.2% | -0.0213 to 0.0373 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.223 | -0.1% | -0.00552 to 0.00498 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 529 | +3.4% | -56.8 to 91.1 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 403 | 413 | +2.4% | -62.8 to 82.1 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 268,252 | 257,277 | -4.1% | -23,749 to 1,800 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.203 | -0.2% | -0.0973 to 0.0966 | STEADY, no difference beyond the noise |
| host CPU-seconds | 143 | 144 | +0.1% | -86.7 to 87 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.27 | 0.27 | +0.1% | -0.163 to 0.164 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81 | 80.6 | -0.5% | -3.9 to 3.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 80 | 79.4 | -0.7% | -4.05 to 2.86 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.03 | 1.23 | +19.2% | 0.153 to 0.243 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 143 | 144 | +0.1% | -86.7 to 87 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | +0.0% | -2.68 to 2.83 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,885 | +0.0% | -1.99 to 2.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.316 | -0.8% | -0.00784 to 0.0025 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.594 | 0.591 | -0.5% | -0.0185 to 0.0125 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.201 | -1.2% | -0.00858 to 0.00379 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | -0.1% | -8.57 to 7.64 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 699,903 | 667,956 | -4.6% | -72,757 to 8,863 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.203 | -7.5% | -0.122 to 0.0892 | STEADY, no difference beyond the noise |
| host CPU-seconds | 393 | 356 | -9.4% | -272 to 198 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.296 | 0.268 | -9.4% | -0.204 to 0.149 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 196 | 194 | -1.2% | -11.1 to 6.54 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 194 | 191 | -1.6% | -12 to 5.91 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.75 | 3.49 | +27.2% | 0.482 to 1.01 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 393 | 356 | -9.4% | -272 to 198 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,744 | 5,749 | +0.1% | -39.2 to 48 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,760 | 5,765 | +0.1% | -37.6 to 47.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.319 | -0.9% | -0.0105 to 0.00445 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.501 | +0.5% | -0.0475 to 0.0529 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.185 | -0.3% | -0.0146 to 0.0137 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 794 | +55.2% | 185 to 380 | power given |
| bytes in the cache, mean (MB) | 417 | 623 | +49.3% | 145 to 267 | power given |
| pages read into the cache (misses) | 685,866 | 416,109 | -39.3% | -351,292 to -188,223 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.256 | +1.6% | -0.0219 to 0.03 | STEADY, no difference beyond the noise |
| host CPU-seconds | 457 | 469 | +2.4% | -54.7 to 77.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.172 | 0.176 | +2.4% | -0.0216 to 0.0298 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 10.3 |  | 2.74 to 17.9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 274 | 271 | -1.1% | -7.58 to 1.56 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 271 | 267 | -1.3% | -8.14 to 1.03 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.49 | 4.04 | +15.6% | 0.377 to 0.716 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 458 | 469 | +2.4% | -54.7 to 77 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.1% | -9.62 to 6.57 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -7.53 to 4.97 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.373 | 0.359 | -3.8% | -0.0399 to 0.0119 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.643 | 0.644 | +0.2% | -0.0283 to 0.0303 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.215 | -3.6% | -0.0133 to -0.00266 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,379 | +169.3% | 709 to 1,025 | power given |
| bytes in the cache, mean (MB) | 417 | 1,083 | +159.6% | 548 to 783 | power given |
| pages read into the cache (misses) | 674,052 | 259,260 | -61.5% | -435,792 to -393,791 | shown, not judged |
| host CPU busy (share of the run) | 0.263 | 0.241 | -8.1% | -0.0374 to -0.00508 | GAIN |
| host CPU-seconds | 469 | 423 | -9.8% | -79.7 to -12 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.353 | 0.319 | -9.7% | -0.0594 to -0.0094 | GAIN |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 261 | -4.4% | -18.7 to -5.44 | GAIN |
| the server's own CPU-seconds (mongod) | 270 | 258 | -4.7% | -19.2 to -6.12 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 3.12 | +24.0% | 0.44 to 0.767 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 469 | 423 | -9.8% | -79.7 to -12 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
