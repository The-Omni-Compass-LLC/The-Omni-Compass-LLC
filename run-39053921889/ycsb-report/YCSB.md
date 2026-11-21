# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.1% | -4.63 to 0.901 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% | -4.42 to 0.93 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.324 | +0.2% | -0.00874 to 0.0101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.493 | 0.493 | -0.1% | -0.0115 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.2 | -1.1% | -0.00855 to 0.00408 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -15.8 to 3.7 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -1.1% | -11.6 to 2.73 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 730,732 | 706,430 | -3.3% | -115,388 to 66,783 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.176 | -9.1% | -0.0543 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 336 | 299 | -10.9% | -115 to 41.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.252 | 0.225 | -10.9% | -0.0864 to 0.0314 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | -0.0% | -3.43 to 2.23 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -4.81 to 2.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.46 | 0.462 | +0.6% | -0.00854 to 0.0139 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.649 | 0.639 | -1.4% | -0.0549 to 0.0362 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | +0.1% | -0.00194 to 0.00235 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.4% | -17.1 to -7.34 | GAIN |
| bytes in the cache, mean (MB) | 402 | 395 | -1.6% | -10.5 to -2.37 | GAIN |
| pages read into the cache (misses) | 261,404 | 276,038 | +5.6% | -46,294 to 75,561 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.183 | +10.6% | -0.154 to 0.189 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 127 | +11.9% | -130 to 157 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.239 | +11.9% | -0.244 to 0.295 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,894 | -0.1% | -3.18 to 0.109 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -3.09 to 0.12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.32 | +1.1% | -0.00465 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.561 | 0.562 | +0.2% | -0.00645 to 0.00845 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.202 | +0.9% | -0.00702 to 0.0108 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 488 | -4.8% | -110 to 61 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 400 | -3.7% | -90.3 to 59.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,541 | 722,064 | +6.4% | -2,301 to 89,349 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.184 | +0.7% | -0.0519 to 0.0545 | EVEN, no difference beyond the noise |
| host CPU-seconds | 315 | 316 | +0.5% | -108 to 111 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.238 | +0.5% | -0.0813 to 0.0836 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,704 | 5,698 | -0.1% | -30.9 to 18.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,721 | 5,714 | -0.1% | -31.8 to 18.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.429 | 0.428 | -0.1% | -0.0178 to 0.0171 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.634 | 0.632 | -0.3% | -0.0267 to 0.0233 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.249 | 0.249 | -0.1% | -0.0156 to 0.0153 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -6.76 to -2.6 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -3.75 to -0.0362 | GAIN |
| pages read into the cache (misses) | 684,603 | 685,983 | +0.2% | -34,996 to 37,757 | shown, not judged |
| host CPU busy (share of the run) | 0.279 | 0.275 | -1.2% | -0.0341 to 0.0276 | EVEN, no difference beyond the noise |
| host CPU-seconds | 472 | 465 | -1.6% | -79.8 to 65 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.178 | 0.175 | -1.5% | -0.0292 to 0.0238 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,880 | +0.0% | -23.6 to 25.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | +0.0% | -24 to 25.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.377 | 0.376 | -0.3% | -0.001 to -0.001 | GAIN |
| latency, 99th percentile (ms) | 0.585 | 0.576 | -1.5% | -0.0407 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.227 | +0.5% | -0.00285 to 0.00508 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -4.6 to -2.17 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.3% | -2.76 to 0.435 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,154 | 680,887 | +0.1% | -20,706 to 22,172 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.226 | +4.8% | -0.0185 to 0.0392 | EVEN, no difference beyond the noise |
| host CPU-seconds | 361 | 383 | +5.9% | -38.7 to 81.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.289 | +5.8% | -0.027 to 0.0588 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
