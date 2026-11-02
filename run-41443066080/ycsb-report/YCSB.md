# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,903 | -0.0% | -1.78 to 1.14 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,906 | -0.0% | -1.62 to 1.21 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.307 | +1.7% | 3.13e-05 to 0.00997 | LOSS |
| latency, 99th percentile (ms) | 0.462 | 0.47 | +1.7% | -0.00283 to 0.0188 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.163 | +0.8% | -0.000958 to 0.00344 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 418 | -0.3% | -6.4 to 4.19 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 713,938 | 712,196 | -0.2% | -76,737 to 73,253 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.179 | -8.9% | -0.0884 to 0.0535 | STEADY, no difference beyond the noise |
| host CPU-seconds | 362 | 322 | -11.1% | -200 to 120 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.272 | 0.241 | -11.1% | -0.15 to 0.0899 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 160 | 161 | +0.9% | -1.78 to 4.77 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 157 | 158 | +0.6% | -2.45 to 4.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.16 | +24.2% | 0.475 to 0.757 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 362 | 322 | -11.1% | -200 to 120 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,900 | +0.0% | -6.68 to 7.53 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,913 | +0.0% | -3.66 to 4.85 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.312 | +0.8% | -0.0422 to 0.0469 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.488 | -3.9% | -0.126 to 0.0856 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.159 | -1.4% | -0.0246 to 0.0202 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 646 | +26.3% | -155 to 424 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 508 | +25.4% | -128 to 334 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 268,364 | 241,545 | -10.0% | -82,781 to 29,144 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.161 | +15.4% | -0.0636 to 0.107 | STEADY, no difference beyond the noise |
| host CPU-seconds | 97.9 | 117 | +19.8% | -53.7 to 92.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.184 | 0.22 | +19.8% | -0.1 to 0.173 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -1.54 to 4.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.4 | 61.7 | -1.0% | -1.9 to 0.61 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61.6 | 60.7 | -1.3% | -2.07 to 0.414 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.813 | 0.996 | +22.5% | 0.15 to 0.216 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 97.9 | 117 | +19.8% | -53.7 to 92.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,911 | -0.0% | -2.15 to -0.453 | LOSS |
| throughput (operations a second) | 2,915 | 2,914 | -0.0% | -1.95 to 0.0204 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.187 | 0.186 | -0.7% | -0.00759 to 0.00492 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.346 | 0.349 | +0.8% | -0.0135 to 0.0188 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.138 | 0.137 | -0.9% | -0.00303 to 0.000426 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 729 | +42.4% | 110 to 324 | power given |
| bytes in the cache, mean (MB) | 419 | 585 | +39.6% | 74.5 to 257 | power given |
| pages read into the cache (misses) | 664,151 | 472,329 | -28.9% | -256,061 to -127,581 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.139 | -11.6% | -0.104 to 0.0673 | STEADY, no difference beyond the noise |
| host CPU-seconds | 287 | 250 | -13.0% | -218 to 144 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.187 | -13.0% | -0.163 to 0.108 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 139 | 137 | -1.4% | -5.43 to 1.45 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 137 | 134 | -1.9% | -6.18 to 0.963 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.01 | 2.63 | +31.0% | 0.487 to 0.756 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 287 | 250 | -13.0% | -218 to 144 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,649 | 5,657 | +0.1% | -28.8 to 44.3 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,669 | 5,676 | +0.1% | -30.3 to 44.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.45 | 0.442 | -1.7% | -0.0213 to 0.00602 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.692 | 0.685 | -1.0% | -0.0244 to 0.0104 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.256 | 0.25 | -2.2% | -0.0116 to 0.000427 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,418 | +177.0% | 855 to 957 | power given |
| bytes in the cache, mean (MB) | 416 | 1,108 | +166.5% | 658 to 726 | power given |
| pages read into the cache (misses) | 677,651 | 260,086 | -61.6% | -453,417 to -381,713 | shown, not judged |
| host CPU busy (share of the run) | 0.346 | 0.336 | -2.7% | -0.0129 to -0.00607 | GAIN |
| host CPU-seconds | 631 | 610 | -3.3% | -31.4 to -10 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.231 | -3.4% | -0.0135 to -0.00258 | GAIN |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | 2.8 to 8.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 366 | 357 | -2.5% | -20.9 to 2.7 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 361 | 352 | -2.7% | -21.4 to 1.95 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.73 | 5.38 | +13.6% | 0.517 to 0.773 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 631 | 610 | -3.3% | -31.4 to -10 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,872 | 2,875 | +0.1% | -3.71 to 9.21 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,887 | +0.1% | -4.42 to 11.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.381 | 0.367 | -3.8% | -0.0398 to 0.0112 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.656 | 0.663 | +1.1% | -0.0253 to 0.0393 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.222 | -1.7% | -0.00885 to 0.000978 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,356 | +164.9% | 598 to 1,091 | power given |
| bytes in the cache, mean (MB) | 417 | 1,065 | +155.3% | 455 to 841 | power given |
| pages read into the cache (misses) | 671,484 | 282,377 | -57.9% | -562,316 to -215,899 | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.261 | -1.7% | -0.0269 to 0.0178 | STEADY, no difference beyond the noise |
| host CPU-seconds | 473 | 464 | -1.9% | -64.2 to 46.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.357 | 0.35 | -2.0% | -0.0491 to 0.0352 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 3.9 to 6.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 271 | -2.1% | -13.1 to 1.21 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 274 | 268 | -2.4% | -13.7 to 0.452 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.62 | 3.29 | +25.5% | 0.505 to 0.832 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 473 | 464 | -1.9% | -64.2 to 46.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
