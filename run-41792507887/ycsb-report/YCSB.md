# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,888 | +0.0% | -3.27 to 4.19 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,892 | +0.0% | -2.96 to 3.95 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.319 | +0.0% | -0.0179 to 0.0179 | STEADY, the same |
| latency, 99th percentile (ms) | 0.49 | 0.492 | +0.3% | -0.0129 to 0.0162 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.194 | -0.5% | -0.0116 to 0.00952 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | -0.1% | -1.91 to 1.27 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 691,994 | 686,673 | -0.8% | -33,221 to 22,579 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.218 | +13.7% | 0.0125 to 0.0399 | power given |
| host CPU-seconds | 333 | 392 | +17.7% | 22.3 to 95.5 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.294 | +17.7% | 0.0165 to 0.0719 | power given |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 197 | 197 | -0.3% | -13.4 to 12.3 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 195 | 194 | -0.6% | -14 to 11.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.46 | 3.04 | +23.9% | 0.559 to 0.613 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 333 | 392 | +17.7% | 22.3 to 95.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,880 | -0.0% | -6.17 to 4.98 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -6.39 to 4.66 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.433 | 0.433 | +0.1% | -0.0109 to 0.0115 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.612 | 0.605 | -1.1% | -0.0436 to 0.0296 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.217 | 0.219 | +0.8% | -0.000375 to 0.00372 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 402 | 403 | +0.1% | -15.4 to 16.3 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 263,950 | 277,379 | +5.1% | -1,767 to 28,625 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.192 | +3.3% | -0.0426 to 0.0548 | STEADY, no difference beyond the noise |
| host CPU-seconds | 128 | 132 | +3.3% | -36.3 to 44.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.241 | 0.249 | +3.4% | -0.0681 to 0.0843 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81.8 | 82.6 | +1.0% | 0.135 to 1.44 | power given |
| the server's own CPU-seconds (mongod) | 80.8 | 81.3 | +0.7% | -0.013 to 1.13 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.23 | +22.6% | 0.146 to 0.309 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 128 | 132 | +3.3% | -36.4 to 44.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,890 | -0.0% | -0.725 to 0.0919 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% | -0.843 to 0.476 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.306 | 0.308 | +0.5% | -0.00213 to 0.00546 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.476 | 0.481 | +1.0% | -0.0327 to 0.042 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.192 | -0.2% | -0.00137 to 0.000504 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 417 | -0.8% | -8.97 to 2.49 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 706,662 | 711,309 | +0.7% | -122,476 to 131,770 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.182 | +0.4% | -0.105 to 0.106 | STEADY, no difference beyond the noise |
| host CPU-seconds | 312 | 313 | +0.3% | -219 to 221 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.235 | +0.3% | -0.164 to 0.166 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 188 | -0.2% | -4.31 to 3.63 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 186 | 185 | -0.5% | -4.94 to 3.11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.43 | 3.01 | +23.8% | 0.502 to 0.654 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 312 | 313 | +0.3% | -219 to 221 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,677 | 5,683 | +0.1% | -6.31 to 19 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,693 | 5,699 | +0.1% | -6.29 to 18.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.434 | 0.426 | -1.9% | -0.0146 to -0.00208 | GAIN |
| latency, 99th percentile (ms) | 0.654 | 0.649 | -0.8% | -0.023 to 0.0123 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.248 | 0.243 | -2.1% | -0.0105 to 0.000249 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,430 | +179.3% | 672 to 1,164 | power given |
| bytes in the cache, mean (MB) | 417 | 1,118 | +168.5% | 520 to 884 | power given |
| pages read into the cache (misses) | 678,352 | 257,341 | -62.1% | -620,630 to -221,393 | shown, not judged |
| host CPU busy (share of the run) | 0.331 | 0.326 | -1.4% | -0.0119 to 0.00229 | STEADY, no difference beyond the noise |
| host CPU-seconds | 599 | 590 | -1.6% | -30 to 11.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.222 | -1.7% | -0.0113 to 0.00383 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 357 | 347 | -2.6% | -18.1 to -0.566 | GAIN |
| the server's own CPU-seconds (mongod) | 352 | 342 | -2.9% | -18.7 to -1.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.54 | 5.26 | +15.7% | 0.542 to 0.889 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 599 | 590 | -1.6% | -29.9 to 11.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,875 | -0.1% | -12.8 to 6.74 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,884 | -0.1% | -13.1 to 6.64 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.364 | 0.356 | -2.4% | -0.0149 to -0.00241 | GAIN |
| latency, 99th percentile (ms) | 0.561 | 0.552 | -1.6% | -0.0156 to -0.00243 | GAIN |
| latency, mean (ms) | 0.219 | 0.213 | -2.7% | -0.0106 to -0.00122 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,362 | +166.0% | 556 to 1,144 | power given |
| bytes in the cache, mean (MB) | 418 | 1,069 | +155.8% | 420 to 881 | power given |
| pages read into the cache (misses) | 679,252 | 277,966 | -59.1% | -608,350 to -194,223 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.263 | +8.1% | -0.0124 to 0.052 | STEADY, no difference beyond the noise |
| host CPU-seconds | 423 | 473 | +11.8% | -26.4 to 127 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.319 | 0.357 | +12.0% | -0.0206 to 0.0968 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 265 | -2.8% | -16.3 to 1.24 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 270 | 262 | -3.0% | -16.9 to 0.565 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.15 | +25.9% | 0.626 to 0.672 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 423 | 473 | +11.8% | -26.4 to 127 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
