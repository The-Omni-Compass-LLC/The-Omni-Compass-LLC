# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
