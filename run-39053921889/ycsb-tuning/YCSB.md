# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,880 | +0.0% | -23.6 to 25.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | +0.0% | -24 to 25.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.377 | 0.376 | -0.3% | -0.001 to -0.001 | GAIN |
| latency, 99th percentile (ms) | 0.585 | 0.576 | -1.5% | -0.0407 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.227 | +0.5% | -0.00285 to 0.00508 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -4.6 to -2.17 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.3% | -2.76 to 0.435 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,154 | 680,887 | +0.1% | -20,706 to 22,172 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.226 | +4.8% | -0.0185 to 0.0392 | EVEN, no difference beyond the noise |
| host CPU-seconds | 361 | 383 | +5.9% | -38.7 to 81.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.289 | +5.8% | -0.027 to 0.0588 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
