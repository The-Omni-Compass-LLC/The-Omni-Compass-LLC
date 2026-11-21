# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,895 | +0.0% | -1.2 to 3.29 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,900 | +0.0% | -0.799 to 2.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.313 | -1.9% | -0.0329 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.574 | 0.573 | -0.2% | -0.00348 to 0.00148 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.195 | -1.2% | -0.00929 to 0.00461 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -2.25 to 1.61 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,786 | 61,838 | +0.1% | -317 to 419 | shown, not judged |
| host CPU busy (share of the run) | 0.174 | 0.174 | +0.4% | -0.0181 to 0.0194 | EVEN, no difference beyond the noise |
| host CPU-seconds | 297 | 299 | +0.8% | -34.2 to 38.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.224 | +0.7% | -0.0259 to 0.0292 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,890 | +0.0% | -6.47 to 7.63 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,896 | +0.0% | -5.94 to 7.41 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.419 | 0.418 | -0.2% | -0.036 to 0.0347 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.573 | 0.57 | -0.5% | -0.0307 to 0.0247 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.217 | 0.218 | +0.4% | -0.0102 to 0.012 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,513 | 1,513 | -0.0% | -4.81 to 4.72 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,689 | 77,635 | -0.1% | -136 to 28.4 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.14 | -13.1% | -0.112 to 0.0696 | EVEN, no difference beyond the noise |
| host CPU-seconds | 108 | 92.2 | -14.6% | -85.6 to 54.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.203 | 0.173 | -14.6% | -0.161 to 0.101 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,894 | +0.0% | -1.41 to 2.21 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,899 | +0.0% | -1.91 to 3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.308 | +0.0% | -0.0108 to 0.0108 | EVEN, the same |
| latency, 99th percentile (ms) | 0.567 | 0.568 | +0.1% | -0.0122 to 0.0128 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.194 | +0.3% | -0.00411 to 0.00519 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | +0.0% | -0.102 to 1.34 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,615 | 61,653 | +0.1% | -63.5 to 139 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.155 | -11.7% | -0.0578 to 0.0168 | EVEN, no difference beyond the noise |
| host CPU-seconds | 301 | 259 | -14.0% | -119 to 34.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.195 | -14.0% | -0.0895 to 0.026 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,709 | 5,710 | +0.0% | -23.5 to 24.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,723 | 5,723 | +0.0% | -21.6 to 21.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.417 | -1.6% | -0.0264 to 0.0124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.622 | 0.617 | -0.8% | -0.0662 to 0.0562 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.243 | -1.9% | -0.0166 to 0.00749 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,362 | +0.1% | -4.21 to 6.27 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,047 | 63,019 | -0.0% | -832 to 778 | shown, not judged |
| host CPU busy (share of the run) | 0.262 | 0.26 | -0.7% | -0.0139 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 442 | 440 | -0.4% | -34.5 to 30.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.166 | 0.166 | -0.4% | -0.0126 to 0.0111 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,891 | +0.1% | -4.94 to 8.72 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,897 | +0.1% | -4.23 to 7.83 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.345 | 0.344 | -0.2% | -0.0124 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.522 | 0.516 | -1.1% | -0.0369 to 0.0256 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.212 | +0.8% | -0.0103 to 0.0136 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | -0.0% | -4.69 to 3.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,980 | 63,201 | +0.4% | 147 to 294 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.198 | -0.3% | -0.0627 to 0.0616 | EVEN, no difference beyond the noise |
| host CPU-seconds | 335 | 335 | -0.0% | -125 to 125 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.252 | 0.252 | -0.0% | -0.0943 to 0.0941 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
