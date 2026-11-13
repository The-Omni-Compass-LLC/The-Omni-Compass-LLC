# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -6.11 to 2.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -5.25 to 2.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.343 | +2.1% | -0.021 to 0.035 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.514 | +1.2% | -0.00715 to 0.0191 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.205 | +0.4% | -0.00511 to 0.00655 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 450 | -12.2% | -63.6 to -61.2 | GAIN |
| bytes in the cache, mean (MB) | 418 | 367 | -12.2% | -60.9 to -41.4 | GAIN |
| pages read into the cache (misses) | 719,000 | 769,240 | +7.0% | -11,450 to 111,930 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.161 | -13.5% | -0.0966 to 0.0462 | EVEN, no difference beyond the noise |
| host CPU-seconds | 319 | 268 | -16.0% | -190 to 88.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.201 | -16.0% | -0.143 to 0.0663 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,908 | 2,907 | -0.0% | -2.75 to 0.0989 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.0% | -2.47 to 0.195 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.351 | 0.354 | +0.7% | -0.012 to 0.0167 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.496 | 0.508 | +2.4% | -0.0222 to 0.0462 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.17 | 0.172 | +1.0% | -0.00304 to 0.00651 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 451 | -12.0% | -65.6 to -57.1 | GAIN |
| bytes in the cache, mean (MB) | 405 | 354 | -12.5% | -70.2 to -31.3 | GAIN |
| pages read into the cache (misses) | 271,393 | 288,647 | +6.4% | -12,569 to 47,076 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.202 | +23.3% | -0.0423 to 0.119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 118 | 151 | +28.5% | -37.4 to 104 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.283 | +28.4% | -0.0702 to 0.196 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,912 | +0.4% | -48 to 71.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,916 | +0.4% | -47.5 to 70.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.237 | 0.238 | +0.6% | -0.00384 to 0.0065 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.376 | 0.372 | -1.1% | -0.0115 to 0.00345 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.171 | 0.166 | -3.1% | -0.00977 to -0.000954 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 474 | -7.5% | -140 to 63.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 390 | -6.4% | -112 to 58.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 718,852 | 740,754 | +3.0% | -222,753 to 266,557 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.149 | -9.6% | -0.056 to 0.0242 | EVEN, no difference beyond the noise |
| host CPU-seconds | 303 | 268 | -11.5% | -119 to 49.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.201 | -11.9% | -0.0853 to 0.0313 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -2.5 to 7.84 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,685 | 5,676 | -0.2% | -31 to 13.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,702 | 5,693 | -0.2% | -31.1 to 13.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.446 | 0.445 | -0.2% | -0.00757 to 0.00557 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.662 | 0.659 | -0.5% | -0.0138 to 0.00783 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.259 | 0.258 | -0.3% | -0.00618 to 0.00476 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 444 | -13.3% | -80.6 to -55.9 | GAIN |
| bytes in the cache, mean (MB) | 417 | 365 | -12.6% | -61.5 to -43.5 | GAIN |
| pages read into the cache (misses) | 676,627 | 787,410 | +16.4% | 70,543 to 151,023 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.285 | +0.3% | -0.00666 to 0.00856 | EVEN, no difference beyond the noise |
| host CPU-seconds | 478 | 481 | +0.7% | -11.7 to 18.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.182 | +0.7% | -0.00352 to 0.00615 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,899 | -0.1% | -5.18 to 1.12 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,908 | -0.1% | -6.78 to 2.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.347 | +0.1% | -0.0054 to 0.00607 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.605 | 0.601 | -0.8% | -0.0104 to 0.00107 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.156 | 0.157 | +0.7% | -0.00668 to 0.00889 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.2% | -62.6 to -62.6 | GAIN |
| bytes in the cache, mean (MB) | 417 | 369 | -11.6% | -49.5 to -47.4 | GAIN |
| pages read into the cache (misses) | 682,942 | 760,814 | +11.4% | 50,194 to 105,550 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.194 | +6.3% | -0.0246 to 0.0474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 352 | +7.8% | -56.2 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.245 | 0.264 | +7.8% | -0.0423 to 0.0804 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
