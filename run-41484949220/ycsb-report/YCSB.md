# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,894 | +0.0% | -0.977 to 3.36 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,903 | 2,903 | -0.0% | -3.37 to 2.94 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.369 | 0.364 | -1.4% | -0.0254 to 0.0147 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.616 | 0.59 | -4.3% | -0.1 to 0.0467 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.178 | 0.176 | -1.0% | -0.0123 to 0.00873 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 417 | -0.5% | -5.08 to 0.786 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 720,510 | 687,963 | -4.5% | -81,066 to 15,972 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.2 | -0.9% | -0.066 to 0.0623 | STEADY, no difference beyond the noise |
| host CPU-seconds | 370 | 366 | -1.1% | -149 to 140 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.275 | -1.2% | -0.112 to 0.106 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 169 | 168 | -0.2% | -8.15 to 7.58 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 166 | 165 | -0.6% | -8.88 to 6.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.67 | 3.36 | +25.6% | 0.618 to 0.75 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 370 | 366 | -1.1% | -149 to 140 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,890 | -0.3% | -45.7 to 30.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,902 | -0.3% | -45 to 29.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.32 | +2.0% | -0.0279 to 0.0406 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.495 | -0.3% | -0.0731 to 0.0704 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.168 | 0.173 | +2.6% | -0.00622 to 0.0149 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 729 | +42.5% | -290 to 725 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 571 | +42.1% | -229 to 567 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 259,774 | 231,982 | -10.7% | -115,749 to 60,165 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.141 | -11.0% | -0.105 to 0.0697 | STEADY, no difference beyond the noise |
| host CPU-seconds | 114 | 99.7 | -12.8% | -87.4 to 58.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.188 | -12.7% | -0.165 to 0.11 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -1.54 to 4.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 63.3 | 63.3 | +0.0% | -0.641 to 0.655 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 62.5 | 62.2 | -0.4% | -0.896 to 0.456 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.824 | 1.05 | +27.5% | 0.176 to 0.278 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 114 | 99.7 | -12.8% | -87.4 to 58.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | +0.0% | -1.93 to 1.95 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -1.55 to 1.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.306 | 0.308 | +0.4% | -0.00987 to 0.0125 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.572 | 0.575 | +0.5% | -0.00694 to 0.0129 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.195 | +0.3% | -0.00242 to 0.00344 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 416 | 418 | +0.4% | -0.00104 to 3.16 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 668,538 | 684,811 | +2.4% | -92,537 to 125,082 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.183 | -12.7% | -0.0778 to 0.0246 | STEADY, no difference beyond the noise |
| host CPU-seconds | 374 | 316 | -15.6% | -172 to 55.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.237 | -15.6% | -0.129 to 0.0417 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 189 | +0.8% | -2.15 to 5.06 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 185 | 186 | +0.5% | -2.65 to 4.35 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.46 | 3.07 | +24.4% | 0.483 to 0.72 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 374 | 316 | -15.6% | -172 to 55.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,680 | 5,677 | -0.0% | -25.6 to 20.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,696 | 5,694 | -0.0% | -27.3 to 22 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.431 | 0.425 | -1.2% | -0.0147 to 0.00407 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.637 | 0.636 | -0.2% | -0.0165 to 0.0145 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.244 | -1.2% | -0.00773 to 0.0017 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,421 | +177.5% | 777 to 1,040 | power given |
| bytes in the cache, mean (MB) | 416 | 1,112 | +167.1% | 604 to 788 | power given |
| pages read into the cache (misses) | 680,718 | 243,687 | -64.2% | -490,913 to -383,150 | shown, not judged |
| host CPU busy (share of the run) | 0.327 | 0.329 | +0.5% | -0.0197 to 0.0227 | STEADY, no difference beyond the noise |
| host CPU-seconds | 589 | 596 | +1.2% | -44.2 to 58.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.225 | +1.3% | -0.0169 to 0.0225 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.67 |  | 0.415 to 12.9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 356 | 350 | -1.9% | -15.3 to 1.99 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 352 | 345 | -2.1% | -15.9 to 1.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.46 | 5.15 | +15.3% | 0.51 to 0.859 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 589 | 596 | +1.2% | -44.3 to 58.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 6.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,883 | +0.1% | -5.71 to 11.2 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,891 | +0.1% | -5.56 to 10.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.337 | -2.0% | -0.0136 to -0.000427 | GAIN |
| latency, 99th percentile (ms) | 0.535 | 0.517 | -3.4% | -0.0392 to 0.00323 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.203 | -3.2% | -0.0106 to -0.00296 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,403 | +174.1% | 800 to 983 | power given |
| bytes in the cache, mean (MB) | 418 | 1,101 | +163.7% | 616 to 751 | power given |
| pages read into the cache (misses) | 673,212 | 280,769 | -58.3% | -464,525 to -320,361 | shown, not judged |
| host CPU busy (share of the run) | 0.258 | 0.252 | -2.4% | -0.0885 to 0.0761 | STEADY, no difference beyond the noise |
| host CPU-seconds | 465 | 453 | -2.6% | -207 to 183 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.35 | 0.341 | -2.7% | -0.157 to 0.138 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 3.9 to 6.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 264 | -3.1% | -14.1 to -2.81 | GAIN |
| the server's own CPU-seconds (mongod) | 270 | 261 | -3.4% | -14.6 to -3.62 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.25 | +26.3% | 0.542 to 0.814 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 465 | 453 | -2.6% | -207 to 183 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
