# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f6391dbdb8ad`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,896 | -0.0% | -0.756 to 0.512 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,900 | -0.0% | -0.722 to 0.527 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.301 | -0.1% | -0.00974 to 0.00907 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.461 | 0.461 | +0.0% | -0.00497 to 0.00497 | EVEN, the same |
| latency, mean (ms) | 0.187 | 0.188 | +0.2% | -0.00879 to 0.00961 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -1.63 to 1.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,639 | 61,632 | -0.0% | -124 to 110 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.16 | -5.3% | -0.00994 to -0.00803 | GAIN |
| host CPU-seconds | 288 | 270 | -6.2% | -22.4 to -13.4 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.203 | -6.2% | -0.0168 to -0.01 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
