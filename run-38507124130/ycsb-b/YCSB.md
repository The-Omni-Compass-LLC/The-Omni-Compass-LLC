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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
