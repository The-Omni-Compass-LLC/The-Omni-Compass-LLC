# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,909 | +0.1% | 0.644 to 4.59 | GAIN |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | 0.588 to 3.87 | GAIN |
| latency, 95th percentile (ms) | 0.211 | 0.212 | +0.5% | -0.0187 to 0.0207 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.404 | 0.404 | +0.0% | -0.0334 to 0.0334 | STEADY, the same |
| latency, mean (ms) | 0.144 | 0.142 | -1.9% | -0.00564 to 7.51e-05 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,366 | +0.1% | -1.56 to 4.48 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,751 | 61,830 | +0.1% | -265 to 423 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.139 | -1.7% | -0.135 to 0.13 | STEADY, no difference beyond the noise |
| host CPU-seconds | 253 | 248 | -2.1% | -276 to 266 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.189 | 0.185 | -2.1% | -0.207 to 0.199 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 138 | 139 | +0.7% | -0.205 to 2.27 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 136 | 137 | +0.7% | -0.35 to 2.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.08 | 2.12 | +1.9% | -0.137 to 0.216 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 253 | 248 | -2.1% | -276 to 266 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,940 | +0.1% | -0.786 to 6.16 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,942 | +0.1% | -0.79 to 5.68 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.234 | 0.232 | -0.9% | -0.0194 to 0.0154 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.351 | 0.342 | -2.6% | -0.0546 to 0.0366 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0688 | 0.0675 | -1.9% | -0.0109 to 0.00836 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,523 | 1,522 | -0.0% | -3.31 to 2.2 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,668 | 77,708 | +0.1% | -533 to 614 | shown, not judged |
| host CPU busy (share of the run) | 0.0745 | 0.0698 | -6.3% | -0.0667 to 0.0573 | STEADY, no difference beyond the noise |
| host CPU-seconds | 54 | 50.4 | -6.7% | -51.5 to 44.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.101 | 0.0939 | -6.7% | -0.0961 to 0.0826 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 20.4 | 19.5 | -4.3% | -4.29 to 2.55 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 19.7 | 18.8 | -4.3% | -4.12 to 2.43 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.686 | 0.66 | -3.8% | -0.178 to 0.127 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 54 | 50.4 | -6.7% | -51.4 to 44.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,908 | 2,908 | +0.0% | -1.83 to 1.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | +0.0% | -1.86 to 2.24 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.246 | 0.244 | -0.9% | -0.0151 to 0.0104 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.504 | 0.5 | -0.8% | -0.028 to 0.02 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.111 | 0.112 | +0.5% | -0.00489 to 0.00591 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -2.37 to 3.32 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,616 | 61,658 | +0.1% | 1.34 to 83.3 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.134 | +19.2% | -0.015 to 0.0581 | STEADY, no difference beyond the noise |
| host CPU-seconds | 198 | 242 | +21.9% | -30 to 117 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.149 | 0.181 | +21.9% | -0.0226 to 0.0876 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 91.2 | 91.6 | +0.4% | -4.98 to 5.69 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 88.8 | 89.1 | +0.3% | -5.11 to 5.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.4 | 2.48 | +3.5% | 0.0437 to 0.124 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 198 | 242 | +21.9% | -30 to 117 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,749 | 5,753 | +0.1% | -3.46 to 13 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,760 | 5,765 | +0.1% | -0.696 to 12.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.31 | +0.0% | -0.00861 to 0.00861 | STEADY, the same |
| latency, 99th percentile (ms) | 0.471 | 0.479 | +1.6% | -0.0559 to 0.0712 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.175 | 0.179 | +2.1% | -0.0142 to 0.0217 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.0% | -10.9 to 9.54 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,027 | 63,054 | +0.0% | -436 to 490 | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.242 | +3.5% | -0.0222 to 0.0386 | STEADY, no difference beyond the noise |
| host CPU-seconds | 421 | 441 | +4.7% | -50.8 to 90.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.158 | 0.165 | +4.7% | -0.019 to 0.0339 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 243 | 243 | -0.1% | -7.75 to 7.19 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 239 | 239 | -0.1% | -7.37 to 6.88 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.59 | 3.55 | -1.0% | -0.396 to 0.326 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 421 | 441 | +4.7% | -50.9 to 90.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,884 | +0.0% | -0.456 to 2.87 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,888 | +0.0% | -0.426 to 2.72 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.337 | -0.1% | -0.0055 to 0.00484 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.494 | 0.494 | +0.0% | -0.00497 to 0.00497 | STEADY, the same |
| latency, mean (ms) | 0.203 | 0.204 | +0.1% | -0.0032 to 0.00359 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -6.5 to 4.3 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,348 | 62,975 | -0.6% | -1,316 to 570 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.219 | +3.9% | -0.0263 to 0.0428 | STEADY, no difference beyond the noise |
| host CPU-seconds | 358 | 376 | +5.2% | -55.6 to 93 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.269 | 0.283 | +5.2% | -0.0417 to 0.0697 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233 | 234 | +0.3% | -1.5 to 3.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 230 | 231 | +0.3% | -1.62 to 2.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.53 | 2.64 | +4.4% | 0.0367 to 0.185 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 358 | 376 | +5.2% | -55.6 to 93 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
