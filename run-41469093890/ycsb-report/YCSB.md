# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,882 | -0.1% | -5.64 to 2.14 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -3.65 to 0.693 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.337 | 0.346 | +2.6% | -0.0103 to 0.0276 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.596 | 0.599 | +0.6% | -0.0118 to 0.0185 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.205 | +1.2% | -0.00403 to 0.00869 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | -0.0% | -8.99 to 8.61 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 717,521 | 716,850 | -0.1% | -21,254 to 19,910 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.202 | -1.5% | -0.053 to 0.0469 | STEADY, no difference beyond the noise |
| host CPU-seconds | 361 | 353 | -2.1% | -116 to 101 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.271 | 0.266 | -2.0% | -0.0875 to 0.0765 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 202 | 204 | +1.2% | -2.96 to 7.92 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 199 | 201 | +0.9% | -3.73 to 7.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.24 | +27.0% | 0.56 to 0.818 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 361 | 353 | -2.1% | -116 to 101 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,899 | -0.1% | -12.6 to 7.34 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,912 | -0.1% | -13 to 7.43 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.309 | +1.5% | -0.016 to 0.0254 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.483 | 0.483 | -0.0% | -0.0805 to 0.0805 | STEADY, the same |
| latency, mean (ms) | 0.166 | 0.166 | +0.1% | -0.0128 to 0.013 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,014 | +98.1% | -433 to 1,438 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 790 | +95.3% | -322 to 1,093 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 271,762 | 199,590 | -26.6% | -222,196 to 77,851 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.15 | -6.6% | -0.0245 to 0.00339 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 108 | -7.5% | -22.7 to 5.21 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.219 | 0.202 | -7.5% | -0.0426 to 0.00997 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 61.6 | 60.6 | -1.7% | -5.53 to 3.46 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 60.8 | 59.6 | -2.0% | -5.77 to 3.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.789 | 0.971 | +23.1% | 0.109 to 0.255 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 116 | 108 | -7.5% | -22.7 to 5.24 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,939 | -0.0% | -5.54 to 4.26 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,940 | -0.0% | -5.68 to 4.54 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.098 | 0.1 | +2.4% | -0.00992 to 0.0146 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.3 | 0.301 | +0.2% | -0.00651 to 0.00784 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0598 | 0.0599 | +0.2% | -0.00448 to 0.00471 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 419 | -0.2% | -12.7 to 10.8 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 691,570 | 708,191 | +2.4% | -135,893 to 169,135 | shown, not judged |
| host CPU busy (share of the run) | 0.0872 | 0.0718 | -17.6% | -0.046 to 0.0153 | STEADY, no difference beyond the noise |
| host CPU-seconds | 159 | 129 | -19.0% | -90 to 29.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.119 | 0.0963 | -19.0% | -0.0672 to 0.022 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50.8 | 51.9 | +2.1% | -4.47 to 6.62 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 49.2 | 49.7 | +1.1% | -4.74 to 5.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.59 | 2.11 | +32.9% | 0.188 to 0.855 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 159 | 129 | -19.0% | -90 to 29.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,731 | 5,712 | -0.3% | -167 to 130 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,747 | 5,729 | -0.3% | -168 to 132 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.316 | -2.4% | -0.0115 to -0.00387 | GAIN |
| latency, 99th percentile (ms) | 0.493 | 0.492 | -0.3% | -0.0125 to 0.00987 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.19 | +0.4% | -0.0199 to 0.0213 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,063 | +107.6% | -152 to 1,255 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 775 | +86.3% | -28.3 to 746 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 687,343 | 316,731 | -53.9% | -686,369 to -54,855 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.249 | -2.4% | -0.0447 to 0.0326 | STEADY, no difference beyond the noise |
| host CPU-seconds | 467 | 456 | -2.2% | -103 to 82.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.175 | 0.172 | -1.9% | -0.0361 to 0.0294 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 24 |  | -24.9 to 72.9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275 | 268 | -2.6% | -19.5 to 4.98 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 272 | 264 | -2.9% | -20.4 to 4.82 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.6 | 4.15 | +15.1% | 0.0941 to 0.997 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 467 | 456 | -2.2% | -103 to 82.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,870 | 2,872 | +0.1% | -10.4 to 14.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,882 | 2,885 | +0.1% | -9.66 to 14.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.377 | 0.362 | -4.1% | -0.0191 to -0.0115 | GAIN |
| latency, 99th percentile (ms) | 0.658 | 0.663 | +0.8% | -0.00587 to 0.0165 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.222 | -1.3% | -0.0056 to -0.000424 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,485 | +190.0% | 720 to 1,225 | power given |
| bytes in the cache, mean (MB) | 417 | 1,158 | +177.4% | 567 to 914 | power given |
| pages read into the cache (misses) | 678,094 | 211,037 | -68.9% | -669,278 to -264,836 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.254 | +5.6% | -0.034 to 0.061 | STEADY, no difference beyond the noise |
| host CPU-seconds | 415 | 447 | +7.9% | -77.3 to 143 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.313 | 0.337 | +7.8% | -0.0598 to 0.109 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 8.67 |  | -3.07 to 20.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 274 | 269 | -1.8% | -9.4 to -0.691 | GAIN |
| the server's own CPU-seconds (mongod) | 272 | 266 | -2.1% | -10.3 to -1.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.56 | 3.32 | +29.7% | 0.528 to 0.991 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 415 | 447 | +7.9% | -77.3 to 143 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
