# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,909 | +1.0% | -103 to 163 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,915 | +1.0% | -104 to 163 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.212 | 0.207 | -2.4% | -0.014 to 0.00396 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.379 | -1.0% | -0.0113 to 0.00392 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.157 | 0.155 | -1.2% | -0.0396 to 0.0358 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 801 | +56.4% | -162 to 739 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 637 | +53.3% | -125 to 568 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 717,967 | 453,049 | -36.9% | -633,808 to 103,971 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.151 | -5.1% | -0.0425 to 0.0262 | EVEN, no difference beyond the noise |
| host CPU-seconds | 288 | 270 | -6.1% | -89.7 to 54.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.218 | 0.202 | -7.1% | -0.0761 to 0.045 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | -5.01 to 15.7 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 149 | 146 | -1.5% | -6.96 to 2.37 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 147 | 144 | -1.9% | -7.36 to 1.79 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.01 | 2.5 | +24.7% | 0.405 to 0.585 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 288 | 270 | -6.1% | -89.7 to 54.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,878 | -0.0% | -3.56 to 2.78 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,886 | -0.0% | -3.18 to 2.93 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.431 | 0.437 | +1.2% | 0.0039 to 0.00677 | LOSS |
| latency, 99th percentile (ms) | 0.601 | 0.614 | +2.1% | -0.0115 to 0.0368 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.22 | 0.223 | +1.0% | -0.000514 to 0.0049 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 399 | 403 | +1.2% | -4.31 to 13.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 258,674 | 256,453 | -0.9% | -7,699 to 3,257 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.219 | +9.4% | -0.0357 to 0.0732 | EVEN, no difference beyond the noise |
| host CPU-seconds | 140 | 156 | +11.4% | -31.8 to 63.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.293 | +11.4% | -0.0596 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83 | 84.3 | +1.6% | -0.9 to 3.51 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82 | 83 | +1.3% | -1.16 to 3.26 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.05 | 1.3 | +23.9% | 0.157 to 0.343 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 140 | 156 | +11.4% | -31.8 to 63.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -5.39 to 3.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -5.2 to 3.48 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.311 | +0.5% | -0.00868 to 0.012 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.527 | 0.518 | -1.7% | -0.0253 to 0.00729 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.196 | +0.8% | -0.00247 to 0.00544 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -9.54 to 7.66 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,114 | 696,277 | +0.7% | -181,931 to 192,256 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.207 | +6.0% | -0.0413 to 0.0647 | EVEN, no difference beyond the noise |
| host CPU-seconds | 342 | 367 | +7.3% | -92.9 to 143 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.257 | 0.276 | +7.3% | -0.0696 to 0.107 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 189 | 192 | +1.4% | -0.129 to 5.35 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 187 | 189 | +1.0% | -0.866 to 4.67 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.32 | +27.3% | 0.575 to 0.848 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 342 | 367 | +7.3% | -92.9 to 143 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,673 | 5,676 | +0.0% | -26.6 to 32 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,691 | 5,693 | +0.0% | -28.2 to 33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.434 | 0.427 | -1.7% | -0.0102 to -0.00446 | GAIN |
| latency, 99th percentile (ms) | 0.662 | 0.656 | -0.8% | -0.0133 to 0.00265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.248 | 0.243 | -2.2% | -0.00795 to -0.00315 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,352 | +164.0% | 653 to 1,026 | power given |
| bytes in the cache, mean (MB) | 417 | 1,059 | +154.1% | 500 to 785 | power given |
| pages read into the cache (misses) | 681,694 | 298,319 | -56.2% | -534,578 to -232,173 | shown, not judged |
| host CPU busy (share of the run) | 0.335 | 0.321 | -4.2% | -0.0178 to -0.0106 | GAIN |
| host CPU-seconds | 613 | 579 | -5.6% | -44.6 to -24 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.218 | -5.6% | -0.0179 to -0.00816 | GAIN |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 356 | 347 | -2.7% | -14 to -4.97 | GAIN |
| the server's own CPU-seconds (mongod) | 352 | 342 | -2.9% | -14.6 to -5.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.4 | 5.09 | +15.7% | 0.519 to 0.863 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 613 | 579 | -5.6% | -44.6 to -23.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,899 | -0.0% | -4.58 to 3.05 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,910 | +0.0% | -4.9 to 5.56 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.227 | 0.223 | -2.1% | -0.03 to 0.0207 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.436 | +0.3% | -0.0195 to 0.0222 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.178 | 0.172 | -3.7% | -0.0202 to 0.00706 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,116 | +118.0% | -159 to 1,368 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 843 | +103.2% | -80.9 to 937 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,989 | 268,529 | -60.7% | -746,532 to -84,388 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.187 | -4.2% | -0.0396 to 0.0234 | EVEN, no difference beyond the noise |
| host CPU-seconds | 350 | 333 | -4.9% | -82.5 to 48.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.25 | -4.8% | -0.0616 to 0.0364 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 23.7 |  | -24.9 to 72.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 212 | 207 | -2.0% | -13.1 to 4.48 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 210 | 205 | -2.3% | -13.8 to 4.04 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.04 | 2.63 | +28.7% | 0.382 to 0.792 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 350 | 333 | -4.9% | -82.5 to 48.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
