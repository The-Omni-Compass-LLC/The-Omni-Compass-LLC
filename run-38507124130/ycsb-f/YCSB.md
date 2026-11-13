# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
