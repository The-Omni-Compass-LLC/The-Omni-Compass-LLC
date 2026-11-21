# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
