# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f6391dbdb8ad`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,890 | +0.1% | -2.76 to 5.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,897 | +0.1% | -2.07 to 5.34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.438 | 0.434 | -1.0% | -0.0505 to 0.0418 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.589 | 0.584 | -0.7% | -0.0661 to 0.0574 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.219 | +0.1% | -0.0176 to 0.018 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,510 | 1,513 | +0.2% | -10.4 to 15.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,552 | 77,718 | +0.2% | -136 to 467 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.147 | +9.6% | -0.0332 to 0.0589 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.5 | 97.2 | +11.1% | -24.3 to 43.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.183 | +11.0% | -0.046 to 0.0823 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
