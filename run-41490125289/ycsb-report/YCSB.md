# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,907 | -0.0% | -6.4 to 4.83 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.0% | -5.7 to 4.63 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.302 | +0.3% | -0.0358 to 0.0378 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.515 | +2.5% | -0.0104 to 0.0358 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.131 | 0.129 | -1.3% | -0.0113 to 0.00794 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 742 | +45.0% | 116 to 345 | power given |
| bytes in the cache, mean (MB) | 418 | 594 | +42.2% | 90 to 263 | power given |
| pages read into the cache (misses) | 720,324 | 468,486 | -35.0% | -364,204 to -139,472 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.154 | +3.3% | -0.038 to 0.0478 | STEADY, no difference beyond the noise |
| host CPU-seconds | 269 | 280 | +4.2% | -83.1 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.21 | +4.2% | -0.0623 to 0.0793 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 120 | 116 | -3.0% | -14 to 6.83 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 117 | 113 | -3.6% | -14.5 to 5.99 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.4 | 3.07 | +27.9% | 0.463 to 0.875 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 269 | 280 | +4.2% | -83.1 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,879 | +0.0% | -8.92 to 11.8 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,887 | +0.0% | -8.65 to 10.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.447 | 0.445 | -0.4% | -0.0231 to 0.0198 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.623 | 0.62 | -0.4% | -0.0623 to 0.057 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | -0.1% | -0.0102 to 0.0098 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 565 | +10.3% | -175 to 281 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 399 | 441 | +10.5% | -141 to 225 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 274,517 | 248,517 | -9.5% | -76,749 to 24,749 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.227 | +11.2% | -0.0122 to 0.0581 | STEADY, no difference beyond the noise |
| host CPU-seconds | 143 | 163 | +14.3% | -10.7 to 51.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.269 | 0.307 | +14.2% | -0.02 to 0.0966 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83.2 | 83.1 | -0.2% | -6.8 to 6.53 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82.2 | 81.8 | -0.5% | -6.99 to 6.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.05 | 1.31 | +24.3% | 0.167 to 0.343 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 143 | 163 | +14.3% | -10.7 to 51.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,940 | 2,940 | +0.0% | -7.39 to 7.59 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,942 | -0.0% | -7.58 to 7.42 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0917 | 0.0927 | +1.1% | -0.0164 to 0.0184 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.287 | 0.285 | -0.7% | -0.0223 to 0.0183 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0584 | 0.0583 | -0.2% | -0.00557 to 0.00529 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 419 | -0.3% | -2.48 to -0.211 | GAIN |
| pages read into the cache (misses) | 719,940 | 723,491 | +0.5% | -60,054 to 67,156 | shown, not judged |
| host CPU busy (share of the run) | 0.0812 | 0.0815 | +0.3% | -0.0384 to 0.0389 | STEADY, no difference beyond the noise |
| host CPU-seconds | 148 | 149 | +1.0% | -76.6 to 79.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.11 | 0.111 | +1.0% | -0.0571 to 0.0593 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50.2 | 50.5 | +0.5% | -6.08 to 6.54 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 48.6 | 48.5 | -0.4% | -6.11 to 5.74 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.59 | 2 | +26.1% | 0.00715 to 0.824 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 148 | 149 | +1.0% | -76.6 to 79.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,652 | 5,660 | +0.1% | -16.8 to 32.8 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,672 | 5,680 | +0.2% | -13.8 to 31.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.459 | 0.45 | -2.1% | -0.0305 to 0.0112 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.727 | 0.727 | -0.0% | -0.0289 to 0.0282 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.254 | 0.248 | -2.4% | -0.0178 to 0.00538 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,476 | +188.3% | 835 to 1,093 | power given |
| bytes in the cache, mean (MB) | 416 | 1,149 | +176.4% | 633 to 833 | power given |
| pages read into the cache (misses) | 677,606 | 213,488 | -68.5% | -552,387 to -375,848 | shown, not judged |
| host CPU busy (share of the run) | 0.337 | 0.327 | -2.9% | -0.0127 to -0.00683 | GAIN |
| host CPU-seconds | 614 | 592 | -3.6% | -31.9 to -12.6 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.224 | -3.8% | -0.0113 to -0.00621 | GAIN |
| cache size changes written (the knob's moves) | 0 | 7 |  | 2.03 to 12 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 360 | 350 | -2.8% | -29.9 to 9.68 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 355 | 345 | -3.1% | -30.5 to 8.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.47 | 5.22 | +16.7% | 0.519 to 0.977 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 614 | 592 | -3.6% | -31.9 to -12.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 4.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,869 | 2,870 | +0.0% | -6.8 to 7.84 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,881 | 2,882 | +0.0% | -6.31 to 7.67 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.365 | -3.7% | -0.0239 to -0.00406 | GAIN |
| latency, 99th percentile (ms) | 0.655 | 0.652 | -0.5% | -0.0202 to 0.0142 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.219 | -3.0% | -0.0152 to 0.00158 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,443 | +181.8% | 790 to 1,071 | power given |
| bytes in the cache, mean (MB) | 417 | 1,124 | +169.4% | 600 to 813 | power given |
| pages read into the cache (misses) | 674,421 | 215,796 | -68.0% | -495,363 to -421,887 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.252 | -6.0% | -0.113 to 0.0805 | STEADY, no difference beyond the noise |
| host CPU-seconds | 481 | 445 | -7.5% | -273 to 201 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.364 | 0.336 | -7.5% | -0.206 to 0.151 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 9 |  | 9 to 9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 276 | 265 | -3.7% | -20.8 to 0.18 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 273 | 262 | -4.0% | -21.5 to -0.487 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.24 | +26.1% | 0.454 to 0.888 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 481 | 445 | -7.5% | -273 to 201 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
