# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,932 | -0.1% | -6.88 to 1.38 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,934 | -0.1% | -6.91 to 1.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.185 | 0.185 | +0.2% | -0.0142 to 0.0149 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.331 | 0.337 | +1.6% | -0.00964 to 0.0203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0775 | 0.0787 | +1.5% | 5.63e-05 to 0.0023 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 487 | -5.0% | -104 to 52.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 402 | -4.1% | -72.9 to 38.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 697,620 | 738,761 | +5.9% | -42,292 to 124,572 | shown, not judged |
| host CPU busy (share of the run) | 0.0878 | 0.096 | +9.3% | -0.0632 to 0.0796 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 175 | +10.4% | -128 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.118 | 0.131 | +10.5% | -0.0958 to 0.121 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -2.5 to 7.84 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
