# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,907 | +0.0% | -1.49 to 1.82 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,912 | +0.0% | 0.0601 to 0.468 | GAIN |
| latency, 95th percentile (ms) | 0.236 | 0.23 | -2.5% | -0.0473 to 0.0353 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.396 | -1.0% | -0.0464 to 0.0384 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.149 | -3.0% | -0.0133 to 0.00389 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 893 | +74.4% | 151 to 610 | power given |
| bytes in the cache, mean (MB) | 417 | 709 | +70.1% | 111 to 473 | power given |
| pages read into the cache (misses) | 703,721 | 412,165 | -41.4% | -407,916 to -175,195 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.152 | -4.6% | -0.0588 to 0.0443 | EVEN, no difference beyond the noise |
| host CPU-seconds | 287 | 271 | -5.4% | -130 to 98.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.203 | -5.4% | -0.0972 to 0.0738 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | -0.462 to 7.13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 153 | 148 | -3.3% | -7.42 to -2.82 | GAIN |
| the server's own CPU-seconds (mongod) | 151 | 146 | -3.8% | -8.01 to -3.39 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.1 | 2.67 | +27.6% | 0.533 to 0.623 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 287 | 271 | -5.4% | -130 to 98.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,796 | 2,897 | +3.6% | -293 to 495 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,810 | 2,911 | +3.6% | -290 to 491 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.322 | +1.2% | -0.0278 to 0.0351 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.53 | 0.52 | -1.9% | -0.117 to 0.0969 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.18 | -8.0% | -0.0592 to 0.0276 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 952 | +85.8% | 140 to 739 | power given |
| bytes in the cache, mean (MB) | 394 | 742 | +88.1% | 101 to 594 | power given |
| pages read into the cache (misses) | 249,373 | 193,790 | -22.3% | -150,687 to 39,521 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.17 | +9.0% | -0.179 to 0.207 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 126 | +12.2% | -160 to 187 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.238 | +7.6% | -0.342 to 0.375 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 60.7 | 62.9 | +3.7% | -6.08 to 10.5 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 59.9 | 61.9 | +3.3% | -6.29 to 10.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.813 | 1.06 | +29.8% | 0.193 to 0.292 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 113 | 126 | +12.2% | -160 to 187 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | +0.0% | -3.78 to 4.31 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,891 | +0.0% | -3.6 to 4.28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.306 | 0.308 | +0.4% | -0.00384 to 0.0065 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.489 | 0.493 | +0.7% | -0.00426 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.193 | +0.8% | -0.00477 to 0.00772 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 417 | 418 | +0.3% | -2.33 to 4.73 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 689,572 | 695,182 | +0.8% | -96,971 to 108,192 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.189 | +1.2% | -0.0166 to 0.0212 | EVEN, no difference beyond the noise |
| host CPU-seconds | 322 | 327 | +1.4% | -36.7 to 46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.245 | +1.4% | -0.0278 to 0.0347 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 190 | +1.8% | -3.8 to 10.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 187 | +1.5% | -4.32 to 9.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.18 | +23.8% | 0.465 to 0.755 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 322 | 327 | +1.4% | -36.7 to 46 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,679 | 5,682 | +0.1% | -33 to 40.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,695 | 5,699 | +0.1% | -33.8 to 41.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.439 | 0.431 | -2.0% | -0.0187 to 0.00137 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.694 | 0.691 | -0.4% | -0.0168 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.245 | 0.239 | -2.2% | -0.0133 to 0.00231 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,401 | +173.7% | 702 to 1,077 | power given |
| bytes in the cache, mean (MB) | 416 | 1,095 | +163.2% | 535 to 823 | power given |
| pages read into the cache (misses) | 686,562 | 244,982 | -64.3% | -495,465 to -387,695 | shown, not judged |
| host CPU busy (share of the run) | 0.322 | 0.315 | -2.1% | -0.0171 to 0.00364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 584 | 570 | -2.3% | -40.1 to 13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.215 | -2.4% | -0.0158 to 0.0053 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 349 | 338 | -3.0% | -23.6 to 2.65 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 344 | 333 | -3.2% | -24.4 to 2.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.44 | 5.04 | +13.5% | 0.364 to 0.831 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 584 | 570 | -2.3% | -40.1 to 13 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,871 | 2,872 | +0.0% | -20.9 to 23.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,884 | +0.0% | -19.4 to 21.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.365 | -3.9% | -0.0223 to -0.00708 | GAIN |
| latency, 99th percentile (ms) | 0.653 | 0.647 | -0.8% | -0.0219 to 0.0112 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.219 | -1.9% | -0.00792 to -0.000811 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,435 | +180.2% | 824 to 1,022 | power given |
| bytes in the cache, mean (MB) | 417 | 1,119 | +168.2% | 614 to 789 | power given |
| pages read into the cache (misses) | 671,116 | 232,465 | -65.4% | -496,959 to -380,341 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.252 | -1.6% | -0.0547 to 0.0466 | EVEN, no difference beyond the noise |
| host CPU-seconds | 453 | 446 | -1.6% | -124 to 109 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.342 | 0.336 | -1.6% | -0.0909 to 0.0799 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.67 |  | 2.5 to 12.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 267 | -2.4% | -19.2 to 5.91 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 271 | 263 | -2.7% | -19.8 to 5.26 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 3.17 | +25.7% | 0.598 to 0.698 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 453 | 446 | -1.6% | -124 to 109 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
