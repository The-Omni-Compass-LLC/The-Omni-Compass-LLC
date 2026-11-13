# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,934 | -0.1% | -6.15 to 1.41 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,937 | -0.1% | -6.18 to 1.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.172 | 0.175 | +1.6% | -0.019 to 0.0244 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.335 | 0.335 | +0.1% | -0.0119 to 0.0126 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0807 | 0.0818 | +1.4% | -0.00416 to 0.00642 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -75.1 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 420 | 369 | -12.2% | -65.1 to -37.8 | GAIN |
| pages read into the cache (misses) | 695,613 | 764,947 | +10.0% | 20,502 to 118,166 | shown, not judged |
| host CPU busy (share of the run) | 0.0861 | 0.0918 | +6.7% | -0.0395 to 0.051 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 165 | +7.2% | -77 to 99.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.115 | 0.123 | +7.2% | -0.0575 to 0.074 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -5.58 to 5.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,895 | -0.0% | -4.36 to 3.06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.433 | 0.435 | +0.5% | -0.00887 to 0.0135 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.615 | 0.612 | -0.6% | -0.0604 to 0.0531 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.226 | +0.2% | -0.00774 to 0.00855 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.6% | -77.3 to -51.8 | GAIN |
| bytes in the cache, mean (MB) | 404 | 351 | -13.1% | -66 to -39.6 | GAIN |
| pages read into the cache (misses) | 273,826 | 286,523 | +4.6% | -7,286 to 32,679 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.194 | +13.2% | -0.111 to 0.156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 115 | 134 | +16.9% | -89.3 to 128 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.253 | +16.9% | -0.168 to 0.241 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | -0.462 to 7.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,896 | -0.1% | -4.82 to 0.938 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,901 | -0.1% | -4.22 to 0.713 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.313 | +1.1% | 0.000465 to 0.0062 | LOSS |
| latency, 99th percentile (ms) | 0.57 | 0.569 | -0.2% | -0.0109 to 0.00894 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.203 | +0.3% | -0.00192 to 0.003 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -77.9 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 419 | 368 | -12.1% | -55.2 to -46.5 | GAIN |
| pages read into the cache (misses) | 737,547 | 799,914 | +8.5% | -105,166 to 229,900 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.189 | +11.5% | -0.0537 to 0.0927 | EVEN, no difference beyond the noise |
| host CPU-seconds | 289 | 329 | +13.8% | -110 to 190 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.247 | +13.8% | -0.0828 to 0.143 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,808 | 5,806 | -0.0% | -8.69 to 4.19 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,820 | 5,817 | -0.0% | -8.57 to 3.39 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.239 | 0.237 | -0.8% | -0.0128 to 0.00883 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.452 | 0.449 | -0.7% | -0.0158 to 0.00917 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.12 | 0.118 | -1.0% | -0.00465 to 0.00221 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 446 | -12.8% | -77.7 to -53.4 | GAIN |
| bytes in the cache, mean (MB) | 418 | 367 | -12.3% | -60.1 to -43.2 | GAIN |
| pages read into the cache (misses) | 694,723 | 795,695 | +14.5% | 52,562 to 149,380 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.158 | -6.7% | -0.0932 to 0.0708 | EVEN, no difference beyond the noise |
| host CPU-seconds | 307 | 285 | -7.1% | -196 to 153 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.115 | 0.107 | -7.1% | -0.0735 to 0.0571 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,882 | +0.1% | -11.5 to 17 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,891 | +0.1% | -11.8 to 15.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.375 | 0.374 | -0.4% | -0.0136 to 0.0109 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.583 | 0.575 | -1.4% | -0.0277 to 0.0117 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.227 | +0.2% | -0.0118 to 0.0126 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 445 | -13.0% | -75.8 to -57.8 | GAIN |
| bytes in the cache, mean (MB) | 417 | 366 | -12.2% | -55.2 to -46.8 | GAIN |
| pages read into the cache (misses) | 675,237 | 774,154 | +14.6% | 90,194 to 107,640 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.239 | -2.6% | -0.0474 to 0.0347 | EVEN, no difference beyond the noise |
| host CPU-seconds | 427 | 412 | -3.5% | -108 to 78.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.322 | 0.311 | -3.6% | -0.0806 to 0.0572 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
