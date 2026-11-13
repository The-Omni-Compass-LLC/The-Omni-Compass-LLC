# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,885 | -0.1% | -3.46 to -0.0986 | LOSS |
| throughput (operations a second) | 2,896 | 2,895 | -0.1% | -1.98 to -1.27 | LOSS |
| latency, 95th percentile (ms) | 0.507 | 0.51 | +0.5% | -0.00532 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.661 | 0.662 | +0.2% | -0.000101 to 0.00277 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.23 | 0.234 | +1.7% | -0.00134 to 0.00916 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 470 | -8.2% | -120 to 35.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 399 | 368 | -7.8% | -96.8 to 34.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 261,575 | 275,904 | +5.5% | -13,044 to 41,703 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.176 | +8.5% | -0.019 to 0.0465 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 120 | +9.7% | -15 to 36.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.206 | 0.226 | +9.7% | -0.0283 to 0.0684 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
