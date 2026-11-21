# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,911 | 2,912 | +0.0% | -1.56 to 2.29 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,914 | 2,915 | +0.0% | -1.44 to 2.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.28 | 0.28 | +0.0% | -0.00497 to 0.00497 | EVEN, the same |
| latency, 99th percentile (ms) | 0.48 | 0.479 | -0.1% | -0.0115 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.116 | 0.114 | -1.2% | -0.00197 to -0.000866 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -2.5 to 2.78 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,790 | 61,847 | +0.1% | -346 to 459 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.117 | -12.2% | -0.0799 to 0.0473 | EVEN, no difference beyond the noise |
| host CPU-seconds | 241 | 208 | -13.8% | -164 to 97.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.156 | -13.8% | -0.123 to 0.0732 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,888 | +0.1% | -6.97 to 10.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,894 | 2,896 | +0.1% | -9.61 to 12.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.422 | 0.425 | +0.9% | -0.0262 to 0.0335 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.637 | 0.639 | +0.3% | -0.0429 to 0.0469 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.152 | 0.153 | +0.1% | -0.00931 to 0.00965 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,509 | 1,514 | +0.3% | 0.972 to 9.55 | power given |
| pages read into the cache (misses) | 77,493 | 77,598 | +0.1% | -82.7 to 293 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.134 | -18.9% | -0.144 to 0.0821 | EVEN, no difference beyond the noise |
| host CPU-seconds | 122 | 96.2 | -21.1% | -122 to 70.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.181 | -21.2% | -0.23 to 0.132 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,900 | +0.0% | -0.5 to 0.954 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,903 | 2,903 | +0.0% | -0.706 to 1.18 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.293 | 0.295 | +0.8% | -0.00914 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.479 | 0.476 | -0.6% | -0.013 to 0.00768 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.185 | 0.184 | -0.5% | -0.00617 to 0.00446 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | +0.0% | -1.26 to 2.28 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,632 | 61,650 | +0.0% | -124 to 160 | shown, not judged |
| host CPU busy (share of the run) | 0.177 | 0.173 | -2.2% | -0.0814 to 0.0734 | EVEN, no difference beyond the noise |
| host CPU-seconds | 306 | 299 | -2.4% | -169 to 154 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.224 | -2.4% | -0.127 to 0.115 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,811 | 5,817 | +0.1% | -13.6 to 24.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,820 | 5,826 | +0.1% | -13.7 to 25.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.232 | 0.228 | -1.6% | -0.0237 to 0.0164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.424 | 0.428 | +1.0% | -0.0549 to 0.0636 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.112 | 0.11 | -2.0% | -0.0119 to 0.00739 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -13 to 13.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,147 | 63,428 | +0.4% | -503 to 1,066 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.145 | -6.6% | -0.053 to 0.0327 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 261 | -7.2% | -108 to 67.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.105 | 0.0974 | -7.2% | -0.0403 to 0.0252 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,891 | -0.0% | -3.77 to 3.47 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,897 | -0.0% | -4.44 to 3.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.344 | +1.3% | 0.000538 to 0.00813 | LOSS |
| latency, 99th percentile (ms) | 0.596 | 0.592 | -0.6% | -0.0051 to -0.00223 | GAIN |
| latency, mean (ms) | 0.214 | 0.214 | +0.3% | -0.00378 to 0.0049 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | +0.0% | -1.19 to 1.28 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,089 | 63,175 | +0.1% | -779 to 952 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.207 | +4.0% | -0.111 to 0.127 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 356 | +4.7% | -233 to 265 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.267 | +4.7% | -0.175 to 0.199 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
