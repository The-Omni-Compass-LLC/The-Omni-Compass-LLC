# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% | -4.9 to 4.43 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -4.18 to 4.02 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.339 | 0.342 | +0.8% | -0.0241 to 0.0295 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.517 | -0.1% | -0.0234 to 0.0228 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.2 | +1.3% | -0.00596 to 0.0113 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | -0.1% | -8.14 to 7.45 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 696,438 | 729,548 | +4.8% | -145,501 to 211,721 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.204 | -2.8% | -0.0306 to 0.0188 | STEADY, no difference beyond the noise |
| host CPU-seconds | 370 | 356 | -3.9% | -65.5 to 37 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.268 | -3.8% | -0.0493 to 0.0279 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 200 | 204 | +2.0% | -2.15 to 10.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 197 | 200 | +1.7% | -2.63 to 9.25 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.21 | +24.9% | 0.461 to 0.819 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 370 | 356 | -3.9% | -65.5 to 37 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,937 | -0.0% | -5.21 to 4.01 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,940 | -0.0% | -5.41 to 4.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.235 | 0.241 | +2.6% | -0.0157 to 0.0277 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.369 | 0.393 | +6.4% | 0.00502 to 0.0423 | LOSS |
| latency, mean (ms) | 0.0762 | 0.0785 | +3.0% | 0.000151 to 0.00446 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 405 | 406 | +0.2% | -11.9 to 13.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 259,371 | 264,783 | +2.1% | 1,220 to 9,604 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0656 | -41.4% | -0.193 to 0.1 | STEADY, no difference beyond the noise |
| host CPU-seconds | 85.7 | 46.4 | -45.9% | -164 to 85.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.16 | 0.0866 | -45.9% | -0.307 to 0.16 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 24.4 | 25.3 | +3.9% | 0.346 to 1.57 | power given |
| the server's own CPU-seconds (mongod) | 23.8 | 24.5 | +3.2% | 0.177 to 1.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.629 | 0.832 | +32.2% | 0.162 to 0.243 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 85.7 | 46.4 | -45.9% | -164 to 85.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,907 | +0.0% | -7.46 to 8.59 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | +0.0% | -8.1 to 8.48 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.191 | 0.187 | -2.1% | -0.0171 to 0.00915 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.362 | 0.356 | -1.7% | -0.0275 to 0.0148 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.146 | 0.139 | -4.7% | -0.00964 to -0.00423 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 807 | +57.7% | -157 to 747 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 644 | +55.0% | -111 to 568 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 703,021 | 439,623 | -37.5% | -602,043 to 75,247 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.149 | -0.6% | -0.106 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 270 | 269 | -0.2% | -220 to 219 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.202 | -0.3% | -0.165 to 0.164 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 141 | 137 | -2.6% | -10.3 to 3.02 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 139 | 135 | -3.0% | -10.9 to 2.46 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.12 | 2.69 | +26.9% | 0.53 to 0.613 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 270 | 269 | -0.2% | -220 to 219 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,693 | 5,695 | +0.0% | -44 to 47.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,716 | 5,720 | +0.1% | -34.3 to 42.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.426 | +0.4% | -0.0328 to 0.0361 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.719 | 0.734 | +2.1% | -0.0755 to 0.106 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.224 | -0.4% | -0.0168 to 0.0149 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,281 | +150.2% | 372 to 1,166 | power given |
| bytes in the cache, mean (MB) | 416 | 1,006 | +141.7% | 294 to 886 | power given |
| pages read into the cache (misses) | 684,189 | 295,772 | -56.8% | -468,725 to -308,109 | shown, not judged |
| host CPU busy (share of the run) | 0.315 | 0.309 | -1.9% | -0.0431 to 0.0311 | STEADY, no difference beyond the noise |
| host CPU-seconds | 584 | 567 | -2.8% | -106 to 73.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.214 | -2.8% | -0.0416 to 0.0291 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.33 |  | 4.9 to 7.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 318 | 314 | -1.1% | -23.4 to 16.4 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 312 | 308 | -1.4% | -24 to 15 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 5.38 | 6.37 | +18.5% | 0.488 to 1.5 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 584 | 567 | -2.8% | -106 to 73.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 4.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,895 | -0.0% | -6.72 to 5.32 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,906 | -0.0% | -4.97 to 4.53 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.352 | 0.335 | -4.8% | -0.0278 to -0.00617 | GAIN |
| latency, 99th percentile (ms) | 0.602 | 0.598 | -0.7% | -0.043 to 0.035 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.153 | -4.9% | -0.0136 to -0.00202 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,501 | +193.1% | 718 to 1,260 | power given |
| bytes in the cache, mean (MB) | 417 | 1,162 | +178.5% | 534 to 956 | power given |
| pages read into the cache (misses) | 676,404 | 134,739 | -80.1% | -641,125 to -442,205 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.193 | +0.3% | -0.0312 to 0.0325 | STEADY, no difference beyond the noise |
| host CPU-seconds | 344 | 349 | +1.4% | -69.8 to 79.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.262 | +1.4% | -0.0521 to 0.0595 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 15 |  | 6.39 to 23.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 193 | 181 | -6.4% | -21.6 to -3.15 | GAIN |
| the server's own CPU-seconds (mongod) | 191 | 178 | -6.8% | -22.1 to -3.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 3.11 | +25.1% | 0.434 to 0.812 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 344 | 349 | +1.4% | -69.9 to 79.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
