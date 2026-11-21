# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,916 | 2,914 | -0.1% | -10.4 to 6.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,918 | -0.1% | -10.2 to 6.43 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.274 | 0.26 | -5.2% | -0.0293 to 0.000642 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.421 | 0.418 | -0.6% | -0.0238 to 0.0185 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.16 | 0.159 | -0.6% | -0.0119 to 0.0101 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -22.5 to 10.7 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 416 | -1.1% | -16.4 to 7.15 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 726,395 | 695,459 | -4.3% | -51,286 to -10,586 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.16 | -5.3% | -0.0381 to 0.0202 | EVEN, no difference beyond the noise |
| host CPU-seconds | 307 | 288 | -6.0% | -84.1 to 47.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.216 | -6.0% | -0.0634 to 0.0357 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,897 | -0.1% | -3.71 to -0.335 | LOSS |
| throughput (operations a second) | 2,902 | 2,900 | -0.1% | -3.16 to -0.771 | LOSS |
| latency, 95th percentile (ms) | 0.354 | 0.354 | +0.1% | -0.0114 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.47 | 0.469 | -0.2% | -0.0118 to 0.00983 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.195 | +0.1% | -0.00518 to 0.00558 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 499 | -2.6% | -18.1 to -8.37 | GAIN |
| bytes in the cache, mean (MB) | 402 | 396 | -1.6% | -18.7 to 5.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 267,846 | 273,004 | +1.9% | -35,951 to 46,265 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.217 | -4.9% | -0.181 to 0.158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 170 | 158 | -6.9% | -170 to 147 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.319 | 0.297 | -6.9% | -0.319 to 0.275 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,893 | -0.0% | -1.35 to 0.00126 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,898 | -0.0% | -2.72 to 0.833 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.315 | -1.3% | -0.00648 to -0.00152 | GAIN |
| latency, 99th percentile (ms) | 0.57 | 0.566 | -0.6% | -0.00746 to 0.000128 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.2 | -1.4% | -0.00728 to 0.0014 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -22.6 to 7.78 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 410 | -2.1% | -30.9 to 13.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 693,542 | 697,747 | +0.6% | -157,620 to 166,030 | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.17 | -3.7% | -0.0527 to 0.0396 | EVEN, no difference beyond the noise |
| host CPU-seconds | 301 | 288 | -4.2% | -105 to 79.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.217 | -4.2% | -0.0786 to 0.0594 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,813 | 5,809 | -0.1% | -21.8 to 14.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,824 | 5,821 | -0.0% | -21.7 to 15.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.228 | 0.233 | +2.0% | -0.0111 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.438 | +3.1% | 0.00439 to 0.0216 | LOSS |
| latency, mean (ms) | 0.115 | 0.116 | +1.3% | -0.00334 to 0.00641 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -7.83 to -1.44 | GAIN |
| bytes in the cache, mean (MB) | 419 | 416 | -0.6% | -5.84 to 1.16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,744 | 703,884 | +0.7% | -20,359 to 30,639 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.166 | +0.2% | -0.0997 to 0.1 | EVEN, no difference beyond the noise |
| host CPU-seconds | 302 | 301 | -0.2% | -217 to 216 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.113 | 0.113 | -0.2% | -0.0813 to 0.0808 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,882 | +0.1% | -8.26 to 14.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,892 | +0.1% | -8.54 to 14.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.373 | 0.375 | +0.5% | -0.000484 to 0.00448 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.578 | 0.581 | +0.4% | -0.0122 to 0.0169 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.226 | -0.1% | -0.00653 to 0.00602 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -16.3 to 1.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 413 | -1.1% | -12.2 to 2.84 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 669,409 | 683,571 | +2.1% | -9,290 to 37,615 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.229 | +6.4% | -0.0383 to 0.066 | EVEN, no difference beyond the noise |
| host CPU-seconds | 361 | 393 | +8.6% | -88.3 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.296 | +8.5% | -0.0678 to 0.114 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
