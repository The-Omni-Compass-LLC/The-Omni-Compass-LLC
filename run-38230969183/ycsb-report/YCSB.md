# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,856 | 2,856 | +0.0% | -1.17 to 1.3 | no difference beyond the noise |
| throughput (operations a second) | 2,864 | 2,864 | -0.0% | -0.687 to 0.378 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.462 | 0.461 | -0.3% | -0.015 to 0.0123 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.617 | 0.614 | -0.4% | -0.0149 to 0.00959 | no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.215 | -0.6% | -0.00903 to 0.0063 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.8% | -22.8 to 4.68 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 407 | -2.3% | -19.3 to 0.266 | no difference beyond the noise |
| pages read into the cache (misses) | 502,850 | 447,904 | -10.9% | -62,655 to -47,237 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.213 | +0.1% | -0.0568 to 0.057 | no difference beyond the noise |
| host CPU-seconds | 244 | 244 | -0.0% | -82.3 to 82.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.276 | -0.0% | -0.0935 to 0.0933 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,846 | 2,831 | -0.5% | -54.2 to 24.3 | no difference beyond the noise |
| throughput (operations a second) | 2,856 | 2,843 | -0.5% | -52.2 to 25.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.466 | 0.475 | +2.0% | -0.0223 to 0.041 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.706 | 0.73 | +3.4% | -0.0239 to 0.0712 | no difference beyond the noise |
| latency, mean (ms) | 0.245 | 0.247 | +1.1% | -0.00496 to 0.0103 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 496 | -3.2% | -61.3 to 29 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 398 | 381 | -4.2% | -46.6 to 12.9 | no difference beyond the noise |
| pages read into the cache (misses) | 187,469 | 176,894 | -5.6% | -26,368 to 5,219 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.192 | -1.3% | -0.0979 to 0.093 | no difference beyond the noise |
| host CPU-seconds | 87.4 | 85.6 | -2.0% | -55.2 to 51.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.249 | 0.245 | -1.6% | -0.157 to 0.149 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,911 | -0.0% | -18.7 to 15.8 | no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -17.9 to 14.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.255 | +0.5% | -0.0152 to 0.0179 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.391 | +2.3% | -0.00502 to 0.0223 | no difference beyond the noise |
| latency, mean (ms) | 0.0864 | 0.0884 | +2.2% | -0.00603 to 0.00985 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -20 to 9.4 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 414 | -1.1% | -22 to 12.6 | no difference beyond the noise |
| pages read into the cache (misses) | 458,458 | 490,998 | +7.1% | -86,843 to 151,924 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0869 | -21.6% | -0.139 to 0.091 | no difference beyond the noise |
| host CPU-seconds | 136 | 102 | -24.7% | -191 to 124 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.153 | 0.115 | -24.7% | -0.215 to 0.139 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,328 | 5,250 | -1.5% | -665 to 509 | no difference beyond the noise |
| throughput (operations a second) | 5,348 | 5,270 | -1.5% | -663 to 506 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.346 | -0.4% | -0.00892 to 0.00626 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.572 | 0.573 | +0.1% | -0.0378 to 0.0392 | no difference beyond the noise |
| latency, mean (ms) | 0.236 | 0.241 | +2.3% | -0.0292 to 0.04 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -15.6 to 3.19 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 411 | 406 | -1.2% | -16.2 to 6.62 | no difference beyond the noise |
| pages read into the cache (misses) | 434,372 | 445,422 | +2.5% | -24,785 to 46,884 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.249 | -2.5% | -0.0549 to 0.0419 | no difference beyond the noise |
| host CPU-seconds | 311 | 302 | -2.8% | -85.2 to 67.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.188 | 0.186 | -1.5% | -0.0567 to 0.0511 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,830 | 2,836 | +0.2% | -9.09 to 22.3 | no difference beyond the noise |
| throughput (operations a second) | 2,840 | 2,847 | +0.2% | -7.64 to 21.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.401 | 0.401 | +0.2% | -0.00806 to 0.00939 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.598 | 0.601 | +0.6% | -0.0118 to 0.0185 | no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.233 | -0.6% | -0.00551 to 0.00253 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -16 to 0.742 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 411 | -1.2% | -11.9 to 2.23 | no difference beyond the noise |
| pages read into the cache (misses) | 457,352 | 471,381 | +3.1% | -12,996 to 41,054 | shown, not judged |
| host CPU busy (share of the run) | 0.264 | 0.25 | -5.3% | -0.0925 to 0.0646 | no difference beyond the noise |
| host CPU-seconds | 304 | 282 | -7.1% | -143 to 99.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.348 | 0.323 | -7.3% | -0.167 to 0.116 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
