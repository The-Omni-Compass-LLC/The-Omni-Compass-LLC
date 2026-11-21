# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
