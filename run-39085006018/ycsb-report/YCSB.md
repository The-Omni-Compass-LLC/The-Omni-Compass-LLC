# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,931 | -0.1% | -10.9 to 3.91 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,933 | -0.1% | -9.74 to 3.16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.212 | 0.223 | +5.0% | -0.0391 to 0.0604 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.346 | 0.36 | +3.9% | -0.0721 to 0.0995 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0829 | 0.0853 | +2.9% | -0.00938 to 0.0142 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.3% | -20.7 to 7.75 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 414 | -1.5% | -17.1 to 4.85 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 719,741 | 718,158 | -0.2% | -160,417 to 157,252 | shown, not judged |
| host CPU busy (share of the run) | 0.0821 | 0.109 | +33.3% | -0.0386 to 0.0932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 146 | 199 | +36.7% | -73.9 to 181 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.109 | 0.149 | +36.7% | -0.0553 to 0.135 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,904 | +0.1% | -10.9 to 15.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,910 | +0.1% | -11 to 15.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.414 | +0.3% | -0.00665 to 0.00932 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.59 | 0.594 | +0.7% | -0.00601 to 0.0147 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.156 | +0.5% | -0.00162 to 0.00331 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 492 | -3.8% | -54.3 to 14.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 392 | -3.3% | -31.8 to 5.02 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 269,898 | 278,330 | +3.1% | -15,020 to 31,885 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.145 | -2.8% | -0.105 to 0.0962 | EVEN, no difference beyond the noise |
| host CPU-seconds | 108 | 104 | -4.1% | -91.7 to 82.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.204 | 0.195 | -4.2% | -0.172 to 0.155 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,929 | -0.1% | -7.42 to 2.94 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,934 | 2,931 | -0.1% | -6.87 to 1.94 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.206 | 0.209 | +1.1% | -0.0146 to 0.0192 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.353 | +0.2% | -0.037 to 0.0383 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0816 | 0.0817 | +0.2% | -0.00392 to 0.00424 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -15.7 to 5.59 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 421 | +0.4% | -19.1 to 22 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 696,040 | 735,186 | +5.6% | -18,640 to 96,933 | shown, not judged |
| host CPU busy (share of the run) | 0.0797 | 0.0792 | -0.7% | -0.0933 to 0.0922 | EVEN, no difference beyond the noise |
| host CPU-seconds | 142 | 141 | -0.5% | -177 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.106 | 0.105 | -0.5% | -0.132 to 0.131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,702 | 5,703 | +0.0% | -19.1 to 22.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,717 | 5,719 | +0.0% | -19.5 to 23.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.429 | 0.429 | -0.1% | -0.00607 to 0.0054 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.633 | 0.629 | -0.5% | -0.0161 to 0.00942 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.249 | 0.249 | +0.1% | -0.00235 to 0.00279 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -6.86 to -3.51 | GAIN |
| bytes in the cache, mean (MB) | 417 | 414 | -0.7% | -5.71 to -0.0769 | GAIN |
| pages read into the cache (misses) | 683,118 | 689,155 | +0.9% | -5,836 to 17,909 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.284 | +1.2% | -0.0119 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 477 | 484 | +1.6% | -26.7 to 41.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.18 | 0.182 | +1.4% | -0.0109 to 0.0161 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,879 | +0.0% | -10.7 to 13 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,889 | +0.0% | -10.5 to 12.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.37 | 0.37 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.563 | 0.564 | +0.1% | -0.00692 to 0.00826 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.224 | -0.8% | -0.00741 to 0.00374 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -3.82 to -3.13 | GAIN |
| bytes in the cache, mean (MB) | 418 | 416 | -0.3% | -1.58 to -0.939 | GAIN |
| pages read into the cache (misses) | 674,013 | 681,521 | +1.1% | 574 to 14,442 | shown, not judged |
| host CPU busy (share of the run) | 0.236 | 0.234 | -1.0% | -0.0774 to 0.0727 | EVEN, no difference beyond the noise |
| host CPU-seconds | 408 | 402 | -1.4% | -172 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.308 | 0.303 | -1.5% | -0.131 to 0.122 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
