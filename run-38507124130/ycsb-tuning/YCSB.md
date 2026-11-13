# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
