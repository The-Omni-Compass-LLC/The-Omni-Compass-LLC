# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
