# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,688 | 5,698 | +0.2% | -2.63 to 24.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,703 | 5,714 | +0.2% | -3.25 to 25.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.441 | 0.44 | -0.2% | -0.0132 to 0.0118 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.644 | 0.642 | -0.3% | -0.0232 to 0.0192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.256 | 0.255 | -0.1% | -0.00757 to 0.00711 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.19 to -3.44 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.4% | -3 to -0.464 | GAIN |
| pages read into the cache (misses) | 673,861 | 684,981 | +1.7% | -9,444 to 31,685 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.285 | +0.5% | -0.0151 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 483 | 483 | +0.1% | -34.6 to 35.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.183 | 0.182 | -0.2% | -0.0138 to 0.0131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
