# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,934 | -0.1% | -6.15 to 1.41 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,937 | -0.1% | -6.18 to 1.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.172 | 0.175 | +1.6% | -0.019 to 0.0244 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.335 | 0.335 | +0.1% | -0.0119 to 0.0126 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0807 | 0.0818 | +1.4% | -0.00416 to 0.00642 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -75.1 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 420 | 369 | -12.2% | -65.1 to -37.8 | GAIN |
| pages read into the cache (misses) | 695,613 | 764,947 | +10.0% | 20,502 to 118,166 | shown, not judged |
| host CPU busy (share of the run) | 0.0861 | 0.0918 | +6.7% | -0.0395 to 0.051 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 165 | +7.2% | -77 to 99.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.115 | 0.123 | +7.2% | -0.0575 to 0.074 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
