# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,919 | 2,917 | -0.1% | -6.01 to 2.07 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,923 | 2,921 | -0.1% | -5.76 to 1.84 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.25 | -1.3% | -0.031 to 0.0244 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.385 | 0.381 | -1.0% | -0.0106 to 0.00257 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.159 | 0.155 | -2.4% | -0.0193 to 0.0116 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 471 | -8.1% | -127 to 44.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 389 | -6.7% | -92.4 to 36.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,399 | 822,973 | +17.7% | 13,463 to 233,686 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.174 | +2.9% | -0.0443 to 0.0541 | EVEN, no difference beyond the noise |
| host CPU-seconds | 308 | 319 | +3.7% | -99.6 to 122 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.239 | +3.7% | -0.0743 to 0.0914 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,885 | +0.0% | -4.76 to 5.67 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,894 | 2,895 | +0.0% | -6.81 to 8.78 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.445 | 0.448 | +0.7% | -0.0144 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.655 | 0.667 | +1.9% | -0.0205 to 0.0451 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.228 | +2.0% | -0.0027 to 0.0117 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 452 | -11.8% | -67.9 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 401 | 356 | -11.1% | -57.7 to -31 | GAIN |
| pages read into the cache (misses) | 274,416 | 289,980 | +5.7% | -5,487 to 36,615 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.176 | +6.0% | -0.0298 to 0.0497 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 120 | +6.6% | -26.8 to 41.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.226 | +6.6% | -0.0504 to 0.0785 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.97 to 7.97 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,932 | -0.1% | -6.88 to 1.38 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,934 | -0.1% | -6.91 to 1.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.185 | 0.185 | +0.2% | -0.0142 to 0.0149 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.331 | 0.337 | +1.6% | -0.00964 to 0.0203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0775 | 0.0787 | +1.5% | 5.63e-05 to 0.0023 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 487 | -5.0% | -104 to 52.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 402 | -4.1% | -72.9 to 38.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 697,620 | 738,761 | +5.9% | -42,292 to 124,572 | shown, not judged |
| host CPU busy (share of the run) | 0.0878 | 0.096 | +9.3% | -0.0632 to 0.0796 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 175 | +10.4% | -128 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.118 | 0.131 | +10.5% | -0.0958 to 0.121 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -2.5 to 7.84 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,749 | 5,741 | -0.1% | -27.7 to 12.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,763 | 5,756 | -0.1% | -28 to 13.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.365 | 0.37 | +1.6% | -0.00889 to 0.0202 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.597 | 0.609 | +2.0% | -0.0288 to 0.0521 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.202 | +1.5% | -0.00434 to 0.0102 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.3% | -64.2 to -61.8 | GAIN |
| bytes in the cache, mean (MB) | 417 | 369 | -11.5% | -51.9 to -43.8 | GAIN |
| pages read into the cache (misses) | 693,965 | 788,652 | +13.6% | 59,861 to 129,513 | shown, not judged |
| host CPU busy (share of the run) | 0.27 | 0.276 | +2.0% | -0.0364 to 0.0474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 495 | 505 | +2.1% | -90.4 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.19 | +2.1% | -0.0345 to 0.0425 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,927 | 2,921 | -0.2% | -11.9 to 0.255 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,934 | 2,930 | -0.1% | -6.46 to -0.83 | LOSS |
| latency, 95th percentile (ms) | 0.243 | 0.262 | +8.0% | -0.0137 to 0.0524 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.418 | 0.466 | +11.5% | -0.0369 to 0.133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.108 | 0.117 | +8.8% | -0.00822 to 0.0271 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -75.6 to -52.7 | GAIN |
| bytes in the cache, mean (MB) | 418 | 369 | -11.7% | -53.9 to -44.1 | GAIN |
| pages read into the cache (misses) | 687,029 | 767,242 | +11.7% | 40,868 to 119,559 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.149 | +17.0% | -0.0823 to 0.125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 229 | 271 | +18.6% | -173 to 258 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.171 | 0.203 | +18.7% | -0.13 to 0.194 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
