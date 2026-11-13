# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,912 | -0.1% | -9.74 to 6.28 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,918 | 2,917 | -0.1% | -9.84 to 6.48 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.264 | +4.6% | -0.00714 to 0.0305 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.41 | 0.418 | +1.9% | -0.0196 to 0.0349 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.174 | 0.177 | +1.9% | -0.0111 to 0.0175 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -128 to 106 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 410 | -1.3% | -105 to 94.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,869 | 734,772 | +5.1% | -114,995 to 186,802 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.153 | -2.2% | -0.0326 to 0.0255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 283 | 275 | -3.0% | -69.2 to 52.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.206 | -2.9% | -0.0519 to 0.0394 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,885 | -0.1% | -3.46 to -0.0986 | LOSS |
| throughput (operations a second) | 2,896 | 2,895 | -0.1% | -1.98 to -1.27 | LOSS |
| latency, 95th percentile (ms) | 0.507 | 0.51 | +0.5% | -0.00532 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.661 | 0.662 | +0.2% | -0.000101 to 0.00277 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.23 | 0.234 | +1.7% | -0.00134 to 0.00916 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 470 | -8.2% | -120 to 35.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 399 | 368 | -7.8% | -96.8 to 34.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 261,575 | 275,904 | +5.5% | -13,044 to 41,703 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.176 | +8.5% | -0.019 to 0.0465 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 120 | +9.7% | -15 to 36.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.206 | 0.226 | +9.7% | -0.0283 to 0.0684 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,894 | -0.1% | -5.61 to 1.61 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -5.43 to 1.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.316 | +0.5% | -0.00837 to 0.0117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.488 | +0.1% | -0.0255 to 0.0262 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.198 | +0.6% | -0.0118 to 0.0142 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 470 | -8.1% | -128 to 45.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 388 | -7.7% | -106 to 41.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,370 | 774,344 | +14.0% | -10,503 to 200,451 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.174 | +1.5% | -0.0283 to 0.0336 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 297 | +2.0% | -55.2 to 66.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.219 | 0.223 | +2.0% | -0.0416 to 0.0504 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,758 | 5,745 | -0.2% | -30.7 to 4.91 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,772 | 5,759 | -0.2% | -30.6 to 5.16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.36 | +0.9% | 0.000465 to 0.0062 | LOSS |
| latency, 99th percentile (ms) | 0.569 | 0.58 | +1.9% | -0.0152 to 0.0372 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.197 | +0.9% | -0.000778 to 0.00419 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.2% | -63 to -62.3 | GAIN |
| bytes in the cache, mean (MB) | 418 | 368 | -11.8% | -52.9 to -45.5 | GAIN |
| pages read into the cache (misses) | 692,621 | 783,876 | +13.2% | 86,067 to 96,441 | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.266 | -0.1% | -0.0304 to 0.0301 | EVEN, no difference beyond the noise |
| host CPU-seconds | 487 | 485 | -0.5% | -80.7 to 75.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.183 | 0.182 | -0.4% | -0.0301 to 0.0286 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,883 | -0.1% | -11 to 5.51 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,893 | -0.1% | -9.53 to 3.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.371 | 0.371 | -0.1% | -0.0107 to 0.01 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.581 | -0.6% | -0.053 to 0.0464 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.224 | -0.5% | -0.00643 to 0.00427 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 450 | -12.1% | -63.6 to -60.3 | GAIN |
| bytes in the cache, mean (MB) | 417 | 369 | -11.4% | -52.2 to -43.2 | GAIN |
| pages read into the cache (misses) | 686,256 | 761,296 | +10.9% | 73,140 to 76,939 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.214 | -6.0% | -0.0921 to 0.065 | EVEN, no difference beyond the noise |
| host CPU-seconds | 388 | 359 | -7.5% | -195 to 137 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.292 | 0.27 | -7.5% | -0.147 to 0.103 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -0.535 to 5.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
