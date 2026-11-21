# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f6391dbdb8ad`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,910 | +0.0% | -0.385 to 1.11 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,913 | +0.0% | -0.411 to 1.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.282 | 0.282 | +0.0% | -0.0131 to 0.0131 | EVEN, the same |
| latency, 99th percentile (ms) | 0.453 | 0.45 | -0.7% | -0.00957 to 0.00357 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.115 | 0.115 | +0.1% | -0.00332 to 0.00349 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,366 | +0.0% | -4.69 to 4.74 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,798 | 61,871 | +0.1% | -485 to 629 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.14 | -6.8% | -0.0326 to 0.0122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 277 | 254 | -8.1% | -74.3 to 29.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.207 | 0.191 | -8.1% | -0.0556 to 0.0222 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f6391dbdb8ad`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,890 | +0.1% | -2.76 to 5.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,897 | +0.1% | -2.07 to 5.34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.438 | 0.434 | -1.0% | -0.0505 to 0.0418 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.589 | 0.584 | -0.7% | -0.0661 to 0.0574 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.219 | +0.1% | -0.0176 to 0.018 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,510 | 1,513 | +0.2% | -10.4 to 15.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,552 | 77,718 | +0.2% | -136 to 467 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.147 | +9.6% | -0.0332 to 0.0589 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.5 | 97.2 | +11.1% | -24.3 to 43.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.183 | +11.0% | -0.046 to 0.0823 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f6391dbdb8ad`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,896 | -0.0% | -0.756 to 0.512 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,900 | -0.0% | -0.722 to 0.527 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.301 | -0.1% | -0.00974 to 0.00907 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.461 | 0.461 | +0.0% | -0.00497 to 0.00497 | EVEN, the same |
| latency, mean (ms) | 0.187 | 0.188 | +0.2% | -0.00879 to 0.00961 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -1.63 to 1.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,639 | 61,632 | -0.0% | -124 to 110 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.16 | -5.3% | -0.00994 to -0.00803 | GAIN |
| host CPU-seconds | 288 | 270 | -6.2% | -22.4 to -13.4 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.203 | -6.2% | -0.0168 to -0.01 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f6391dbdb8ad`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,821 | 5,823 | +0.0% | -3.21 to 6.87 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,829 | 5,832 | +0.0% | -5.23 to 9.29 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.212 | -0.3% | -0.00692 to 0.00559 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.412 | 0.412 | +0.0% | -0.0326 to 0.0326 | EVEN, the same |
| latency, mean (ms) | 0.108 | 0.107 | -0.8% | -0.0051 to 0.00345 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,364 | -0.1% | -4.45 to 0.585 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,346 | 63,487 | +0.2% | -1,147 to 1,429 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.121 | -17.2% | -0.108 to 0.0583 | EVEN, no difference beyond the noise |
| host CPU-seconds | 266 | 215 | -19.3% | -223 to 121 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0994 | 0.0802 | -19.3% | -0.0833 to 0.045 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f6391dbdb8ad`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,913 | +0.2% | -7.21 to 21.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,919 | +0.2% | -8.39 to 21.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.257 | 0.258 | +0.4% | -0.00983 to 0.0118 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.408 | 0.404 | -1.0% | -0.0106 to 0.00257 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.182 | 0.177 | -2.6% | -0.00723 to -0.00225 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,362 | +0.1% | -4.38 to 7.24 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,946 | 63,290 | +0.5% | -1,013 to 1,701 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.195 | +7.7% | -0.03 to 0.0579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 328 | 359 | +9.3% | -68.4 to 129 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.246 | 0.269 | +9.2% | -0.0511 to 0.0962 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
