# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,890 | -0.1% | -8.55 to 3.35 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,896 | -0.1% | -7.44 to 1.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.337 | 0.352 | +4.7% | -0.00426 to 0.0356 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.518 | 0.523 | +1.0% | -0.0116 to 0.0222 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.206 | +2.0% | -0.0018 to 0.00984 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 475 | -7.3% | -90.2 to 15.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 389 | -7.1% | -77.3 to 17.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 716,259 | 765,917 | +6.9% | -32,416 to 131,731 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.183 | +1.0% | -0.187 to 0.19 | EVEN, no difference beyond the noise |
| host CPU-seconds | 312 | 314 | +0.6% | -392 to 395 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.236 | +0.6% | -0.294 to 0.297 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -1.13 to 6.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,693 | 2,540 | -5.7% | -557 to 250 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,704 | 2,551 | -5.7% | -556 to 249 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.344 | +1.4% | -0.00902 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.59 | +3.9% | -0.0771 to 0.121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.28 | +12.0% | -0.0458 to 0.106 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 477 | -6.7% | -104 to 35.1 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 398 | 360 | -9.4% | -100 to 25.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 235,129 | 222,717 | -5.3% | -111,697 to 86,873 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.144 | +15.4% | -0.0642 to 0.103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.6 | 104 | +19.3% | -48.7 to 82.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.177 | 0.222 | +25.5% | -0.0628 to 0.153 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,894 | -0.1% | -4.24 to -1.73 | LOSS |
| throughput (operations a second) | 2,900 | 2,897 | -0.1% | -4.24 to -1.56 | LOSS |
| latency, 95th percentile (ms) | 0.317 | 0.319 | +0.6% | -0.0023 to 0.0063 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.46 | 0.459 | -0.4% | -0.0299 to 0.0266 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.203 | +1.4% | -0.000432 to 0.00588 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 470 | -8.1% | -129 to 45.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 384 | -8.4% | -118 to 47.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,006 | 753,047 | +7.9% | -152,520 to 262,602 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.187 | +7.9% | -0.0815 to 0.109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 293 | 321 | +9.4% | -169 to 224 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.241 | +9.4% | -0.127 to 0.168 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,783 | 5,780 | -0.1% | -18.7 to 12.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,796 | 5,792 | -0.1% | -17.4 to 8.72 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.298 | 0.298 | +0.1% | -0.00592 to 0.00659 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.524 | 0.512 | -2.2% | -0.0337 to 0.0111 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.147 | +1.3% | 0.000485 to 0.00326 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 411 | -19.8% | -182 to -21.1 | GAIN |
| bytes in the cache, mean (MB) | 419 | 337 | -19.5% | -148 to -14.5 | GAIN |
| pages read into the cache (misses) | 692,742 | 863,760 | +24.7% | 24,060 to 317,978 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.208 | +3.4% | -0.0413 to 0.0549 | EVEN, no difference beyond the noise |
| host CPU-seconds | 362 | 376 | +3.7% | -92.7 to 119 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.136 | 0.141 | +3.6% | -0.0348 to 0.0447 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.3 to 7.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,885 | +0.1% | -11.8 to 16.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,894 | +0.1% | -12.8 to 16.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.367 | 0.362 | -1.4% | -0.0158 to 0.00583 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.564 | 0.555 | -1.6% | -0.0327 to 0.0147 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.227 | 0.223 | -1.9% | -0.00956 to 0.00115 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 464 | -9.4% | -109 to 12.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 380 | -8.8% | -82.8 to 8.94 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 676,740 | 744,255 | +10.0% | -28,910 to 163,940 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.224 | -7.5% | -0.0404 to 0.00429 | EVEN, no difference beyond the noise |
| host CPU-seconds | 418 | 381 | -8.9% | -87.7 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.315 | 0.287 | -8.9% | -0.0674 to 0.0111 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
