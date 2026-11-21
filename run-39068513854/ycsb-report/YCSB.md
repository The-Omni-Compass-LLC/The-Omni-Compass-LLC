# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,893 | -0.1% | -4.25 to 1.05 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -3.91 to 0.794 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.342 | -0.1% | -0.00832 to 0.00765 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.51 | 0.509 | -0.3% | -0.0166 to 0.0133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.205 | -0.5% | -0.00649 to 0.00459 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -18.3 to 7.88 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 415 | -0.7% | -20.5 to 15 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 708,387 | 710,318 | +0.3% | -153,992 to 157,856 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.181 | +0.0% | -0.0456 to 0.0457 | EVEN, no difference beyond the noise |
| host CPU-seconds | 306 | 306 | +0.0% | -92.2 to 92.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.23 | +0.0% | -0.0692 to 0.0694 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,926 | +0.0% | -6 to 6.44 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,931 | 2,931 | -0.0% | -6.07 to 5.65 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.373 | -1.5% | -0.0202 to 0.00889 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.554 | 0.539 | -2.7% | -0.078 to 0.048 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.151 | 0.148 | -2.2% | -0.0112 to 0.0045 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.3% | -25 to 1.7 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 408 | 398 | -2.4% | -31.6 to 12.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,440 | 277,554 | +5.4% | -8,485 to 36,713 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.156 | +8.8% | -0.0679 to 0.0931 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 117 | +11.0% | -58.3 to 81.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.219 | +11.0% | -0.109 to 0.152 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,934 | -0.1% | -4.38 to 0.75 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,936 | -0.1% | -4.44 to 0.92 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.219 | +2.8% | 0.00103 to 0.011 | LOSS |
| latency, 99th percentile (ms) | 0.409 | 0.408 | -0.2% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.107 | 0.109 | +1.9% | -0.00205 to 0.00615 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 489 | -4.6% | -105 to 58.1 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 403 | -3.7% | -77 to 46.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 642,545 | 738,450 | +14.9% | -62,237 to 254,047 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.115 | -2.9% | -0.0143 to 0.00759 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 209 | -3.5% | -29.8 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.156 | -3.5% | -0.0222 to 0.0108 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,688 | 5,698 | +0.2% | -2.63 to 24.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,703 | 5,714 | +0.2% | -3.25 to 25.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.441 | 0.44 | -0.2% | -0.0132 to 0.0118 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.644 | 0.642 | -0.3% | -0.0232 to 0.0192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.256 | 0.255 | -0.1% | -0.00757 to 0.00711 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.19 to -3.44 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.4% | -3 to -0.464 | GAIN |
| pages read into the cache (misses) | 673,861 | 684,981 | +1.7% | -9,444 to 31,685 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.285 | +0.5% | -0.0151 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 483 | 483 | +0.1% | -34.6 to 35.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.183 | 0.182 | -0.2% | -0.0138 to 0.0131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,874 | -0.2% | -9.39 to -0.91 | LOSS |
| throughput (operations a second) | 2,892 | 2,887 | -0.2% | -8.45 to -1.14 | LOSS |
| latency, 95th percentile (ms) | 0.445 | 0.442 | -0.7% | -0.0388 to 0.0328 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.701 | 0.695 | -0.8% | -0.0578 to 0.0465 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.241 | -0.4% | -0.00975 to 0.00761 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.98 to -2.18 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -3.32 to -0.712 | GAIN |
| pages read into the cache (misses) | 680,376 | 677,945 | -0.4% | -37,315 to 32,453 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.24 | +2.5% | -0.0684 to 0.0799 | EVEN, no difference beyond the noise |
| host CPU-seconds | 398 | 410 | +3.1% | -149 to 174 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.3 | 0.31 | +3.2% | -0.113 to 0.132 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
