# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | -0.0% | -9.53 to 8.18 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,936 | 2,936 | -0.0% | -8.91 to 7.38 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.209 | 0.206 | -1.4% | -0.0509 to 0.0449 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.364 | 0.361 | -0.9% | -0.0597 to 0.053 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.084 | 0.0833 | -0.8% | -0.0104 to 0.00909 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.8% | -78.3 to -52.6 | GAIN |
| bytes in the cache, mean (MB) | 419 | 366 | -12.6% | -56.3 to -49.7 | GAIN |
| pages read into the cache (misses) | 679,972 | 752,389 | +10.6% | 3,198 to 141,635 | shown, not judged |
| host CPU busy (share of the run) | 0.0791 | 0.0929 | +17.4% | -0.014 to 0.0415 | EVEN, no difference beyond the noise |
| host CPU-seconds | 140 | 167 | +19.1% | -27.4 to 80.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.105 | 0.124 | +19.1% | -0.0203 to 0.0603 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,929 | 2,928 | -0.1% | -4.07 to 0.907 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,933 | 2,932 | -0.0% | -3.17 to 0.821 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.334 | +0.6% | -0.00457 to 0.00857 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.51 | 0.522 | +2.3% | -0.0394 to 0.0627 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.126 | 0.127 | +0.5% | -8.95e-05 to 0.00146 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 461 | -10.0% | -89.8 to -12.6 | GAIN |
| bytes in the cache, mean (MB) | 403 | 362 | -10.1% | -65.8 to -15.6 | GAIN |
| pages read into the cache (misses) | 270,843 | 287,483 | +6.1% | 1,648 to 31,632 | shown, not judged |
| host CPU busy (share of the run) | 0.0972 | 0.118 | +21.6% | -0.042 to 0.0841 | EVEN, no difference beyond the noise |
| host CPU-seconds | 69.5 | 85.5 | +23.1% | -33.7 to 65.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.13 | 0.16 | +23.1% | -0.0629 to 0.123 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.1% | -3.7 to -0.432 | LOSS |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% | -3.18 to -0.725 | LOSS |
| latency, 95th percentile (ms) | 0.308 | 0.31 | +0.8% | -0.00392 to 0.00859 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.489 | 0.486 | -0.7% | -0.0394 to 0.0327 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.196 | +0.9% | -0.00871 to 0.0121 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 485 | -5.4% | -135 to 79.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 398 | -5.6% | -113 to 65.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 718,476 | 743,146 | +3.4% | -112,674 to 162,014 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.17 | -4.3% | -0.0758 to 0.0603 | EVEN, no difference beyond the noise |
| host CPU-seconds | 305 | 290 | -5.2% | -153 to 122 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.217 | -5.2% | -0.115 to 0.0912 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,646 | 5,654 | +0.1% | -7.24 to 22.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,666 | 5,673 | +0.1% | -10.7 to 25.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.458 | 0.455 | -0.7% | -0.00957 to 0.00357 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.721 | 0.717 | -0.6% | -0.0147 to 0.00537 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.261 | 0.259 | -0.7% | -0.00521 to 0.00164 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -77.8 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 416 | 365 | -12.1% | -60.3 to -40.8 | GAIN |
| pages read into the cache (misses) | 667,539 | 771,485 | +15.6% | 81,235 to 126,659 | shown, not judged |
| host CPU busy (share of the run) | 0.289 | 0.293 | +1.5% | -0.00159 to 0.01 | EVEN, no difference beyond the noise |
| host CPU-seconds | 490 | 500 | +2.2% | -5.29 to 27 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.19 | +2.0% | -0.00304 to 0.0104 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,922 | -0.1% | -9.03 to 1.16 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,933 | 2,929 | -0.1% | -8.12 to 0.839 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.247 | 0.253 | +2.3% | -0.00437 to 0.0157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.426 | 0.437 | +2.6% | -0.0238 to 0.0458 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.109 | 0.112 | +3.1% | -0.00428 to 0.011 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -75.8 to -52.7 | GAIN |
| bytes in the cache, mean (MB) | 418 | 369 | -11.9% | -59.4 to -39.7 | GAIN |
| pages read into the cache (misses) | 688,326 | 769,819 | +11.8% | 61,386 to 101,600 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.131 | +7.1% | -0.019 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 234 | +7.6% | -37.9 to 71.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.163 | 0.175 | +7.7% | -0.0285 to 0.0535 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
