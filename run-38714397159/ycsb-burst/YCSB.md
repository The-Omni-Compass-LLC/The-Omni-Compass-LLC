# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -5.58 to 5.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,895 | -0.0% | -4.36 to 3.06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.433 | 0.435 | +0.5% | -0.00887 to 0.0135 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.615 | 0.612 | -0.6% | -0.0604 to 0.0531 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.226 | +0.2% | -0.00774 to 0.00855 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.6% | -77.3 to -51.8 | GAIN |
| bytes in the cache, mean (MB) | 404 | 351 | -13.1% | -66 to -39.6 | GAIN |
| pages read into the cache (misses) | 273,826 | 286,523 | +4.6% | -7,286 to 32,679 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.194 | +13.2% | -0.111 to 0.156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 115 | 134 | +16.9% | -89.3 to 128 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.253 | +16.9% | -0.168 to 0.241 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | -0.462 to 7.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
