# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -3.31 to 2.68 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -3.1 to 2.57 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.336 | +0.2% | -0.00692 to 0.00826 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.523 | 0.523 | +0.1% | -0.0122 to 0.0128 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.199 | +0.2% | -0.00313 to 0.0038 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 417 | 418 | +0.3% | -3.74 to 6.08 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 695,381 | 710,117 | +2.1% | -31,488 to 60,960 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.217 | +14.3% | -0.0294 to 0.0836 | STEADY, no difference beyond the noise |
| host CPU-seconds | 328 | 387 | +18.0% | -63 to 181 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.247 | 0.291 | +18.0% | -0.0473 to 0.136 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 201 | 202 | +0.3% | -3.83 to 4.92 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 199 | 198 | -0.0% | -4.51 to 4.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.2 | +24.7% | 0.584 to 0.683 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 328 | 387 | +18.0% | -63 to 181 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,881 | -0.0% | -4.22 to 3.63 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -2.85 to 2.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.411 | 0.411 | +0.0% | -0.00248 to 0.00248 | STEADY, the same |
| latency, 99th percentile (ms) | 0.575 | 0.579 | +0.7% | -0.0367 to 0.0447 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.215 | -0.4% | -0.00632 to 0.00454 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 405 | 406 | +0.2% | -11.9 to 13.4 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 270,478 | 266,331 | -1.5% | -48,805 to 40,511 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.202 | -11.0% | -0.111 to 0.0604 | STEADY, no difference beyond the noise |
| host CPU-seconds | 165 | 142 | -14.0% | -102 to 55.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.31 | 0.266 | -14.0% | -0.192 to 0.105 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.5 | 81.9 | -0.6% | -2.85 to 1.78 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81.5 | 80.7 | -1.0% | -3.12 to 1.57 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.25 | +23.8% | 0.198 to 0.285 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 165 | 142 | -14.0% | -102 to 55.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | -0.0% | -8.21 to 8.07 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,898 | -0.0% | -8.68 to 6.92 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.376 | 0.375 | -0.3% | -0.0118 to 0.00983 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.692 | 0.675 | -2.4% | -0.0378 to 0.00446 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.181 | +0.2% | -0.00223 to 0.00278 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 420 | +0.1% | -7.64 to 8.54 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 725,073 | 701,497 | -3.3% | -249,959 to 202,807 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.215 | +7.7% | -0.0719 to 0.103 | STEADY, no difference beyond the noise |
| host CPU-seconds | 365 | 402 | +10.0% | -169 to 242 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.275 | 0.303 | +10.0% | -0.128 to 0.183 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 163 | 165 | +1.1% | -0.651 to 4.38 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 160 | 161 | +0.7% | -1.41 to 3.53 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.79 | 3.59 | +28.9% | 0.555 to 1.06 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 365 | 402 | +10.0% | -169 to 242 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,712 | 5,570 | -2.5% | -772 to 487 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,730 | 5,590 | -2.4% | -768 to 488 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.318 | -1.7% | -0.0171 to 0.00641 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.506 | 0.521 | +3.0% | -0.0639 to 0.0939 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.198 | +1.6% | -0.0358 to 0.042 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,348 | +163.3% | 353 to 1,319 | power given |
| bytes in the cache, mean (MB) | 414 | 961 | +131.9% | 361 to 732 | power given |
| pages read into the cache (misses) | 695,485 | 188,954 | -72.8% | -625,058 to -388,005 | shown, not judged |
| host CPU busy (share of the run) | 0.248 | 0.242 | -2.5% | -0.0568 to 0.0443 | STEADY, no difference beyond the noise |
| host CPU-seconds | 450 | 440 | -2.3% | -114 to 93.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.17 | 0.17 | +0.2% | -0.0249 to 0.0255 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 37.7 |  | 7.61 to 67.7 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 260 | -4.7% | -44.4 to 18.5 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 270 | 256 | -5.0% | -44.6 to 17.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.49 | 4.11 | +17.8% | 0.0857 to 1.16 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 450 | 440 | -2.3% | -114 to 93.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 10.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,870 | 2,876 | +0.2% | -5.92 to 17.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,884 | 2,886 | +0.1% | -11.8 to 16.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.385 | 0.352 | -8.6% | -0.0903 to 0.0243 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.641 | 0.558 | -12.9% | -0.32 to 0.154 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.229 | 0.212 | -7.4% | -0.0338 to -0.000292 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,325 | +158.9% | 287 to 1,340 | power given |
| bytes in the cache, mean (MB) | 418 | 1,042 | +149.7% | 228 to 1,022 | power given |
| pages read into the cache (misses) | 678,864 | 267,951 | -60.5% | -688,269 to -133,558 | shown, not judged |
| host CPU busy (share of the run) | 0.267 | 0.225 | -15.7% | -0.109 to 0.0257 | STEADY, no difference beyond the noise |
| host CPU-seconds | 474 | 388 | -18.3% | -240 to 65.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.358 | 0.292 | -18.4% | -0.182 to 0.0498 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 279 | 261 | -6.7% | -29 to -8.24 | GAIN |
| the server's own CPU-seconds (mongod) | 277 | 258 | -6.9% | -29.5 to -8.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.07 | +17.7% | 0.282 to 0.64 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 474 | 388 | -18.3% | -240 to 65.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
