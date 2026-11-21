# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,892 | -0.1% | -4.55 to 0.712 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,897 | -0.1% | -3.85 to 0.312 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.339 | 0.345 | +1.8% | 0.0017 to 0.0103 | LOSS |
| latency, 99th percentile (ms) | 0.496 | 0.509 | +2.6% | -0.00439 to 0.0304 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.207 | +1.7% | -0.00266 to 0.00977 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.5% | -3.04 to -1.6 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.5% | -11.6 to 7.04 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 726,922 | 698,435 | -3.9% | -67,168 to 10,195 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.195 | -0.2% | -0.0427 to 0.0418 | EVEN, no difference beyond the noise |
| host CPU-seconds | 337 | 335 | -0.6% | -89.6 to 85.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.253 | 0.252 | -0.6% | -0.0672 to 0.0642 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,394 | 2,437 | +1.8% | -578 to 663 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,408 | 2,452 | +1.8% | -576 to 662 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.341 | -1.5% | -0.0289 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.639 | 0.63 | -1.4% | -0.122 to 0.104 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.308 | 0.302 | -1.8% | -0.102 to 0.0911 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -13.6 to -3.11 | GAIN |
| bytes in the cache, mean (MB) | 393 | 381 | -3.1% | -20.3 to -3.94 | GAIN |
| pages read into the cache (misses) | 193,345 | 198,219 | +2.5% | -93,066 to 102,816 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.114 | -6.0% | -0.0649 to 0.0505 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.4 | 80.7 | -6.6% | -49.2 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.18 | -8.6% | -0.113 to 0.0795 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,934 | +0.0% | -4.46 to 5.59 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,935 | 2,936 | +0.0% | -4.74 to 5.83 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.2 | 0.199 | -0.2% | -0.0535 to 0.0528 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.347 | 0.344 | -0.9% | -0.044 to 0.038 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0784 | 0.0781 | -0.5% | -0.0044 to 0.00366 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 489 | -4.4% | -110 to 64.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 402 | -4.5% | -89 to 51.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 719,708 | 719,992 | +0.0% | -232,882 to 233,450 | shown, not judged |
| host CPU busy (share of the run) | 0.0856 | 0.0917 | +7.1% | -0.0693 to 0.0815 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 166 | +7.4% | -138 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.115 | 0.124 | +7.3% | -0.103 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,697 | 5,531 | -2.9% | -611 to 279 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,713 | 5,548 | -2.9% | -611 to 281 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.327 | 0.336 | +2.7% | -0.0136 to 0.0309 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.506 | 0.53 | +4.6% | -0.0194 to 0.0661 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.219 | +4.2% | -0.00567 to 0.0232 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -99.4 to 55.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 394 | -4.9% | -79.2 to 38.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,028 | 709,512 | +4.8% | -179,872 to 244,840 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.239 | -0.4% | -0.0505 to 0.0485 | EVEN, no difference beyond the noise |
| host CPU-seconds | 435 | 433 | -0.6% | -102 to 96.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.169 | +2.2% | -0.0284 to 0.0357 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,880 | -0.2% | -18.7 to 8.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,890 | -0.2% | -18.1 to 7.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.366 | 0.366 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.553 | 0.555 | +0.2% | -0.0209 to 0.0236 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.223 | +0.2% | -0.00193 to 0.00292 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -19 to 6.32 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -1.0% | -14.7 to 6.58 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,905 | 681,607 | +0.5% | -40,699 to 48,103 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.231 | -0.1% | -0.0209 to 0.0203 | EVEN, no difference beyond the noise |
| host CPU-seconds | 399 | 398 | -0.3% | -47.2 to 44.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.301 | 0.3 | -0.2% | -0.0349 to 0.0337 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
