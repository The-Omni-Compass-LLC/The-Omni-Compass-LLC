# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,904 | +0.1% | -10.9 to 15.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,910 | +0.1% | -11 to 15.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.414 | +0.3% | -0.00665 to 0.00932 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.59 | 0.594 | +0.7% | -0.00601 to 0.0147 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.156 | +0.5% | -0.00162 to 0.00331 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 492 | -3.8% | -54.3 to 14.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 392 | -3.3% | -31.8 to 5.02 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 269,898 | 278,330 | +3.1% | -15,020 to 31,885 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.145 | -2.8% | -0.105 to 0.0962 | EVEN, no difference beyond the noise |
| host CPU-seconds | 108 | 104 | -4.1% | -91.7 to 82.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.204 | 0.195 | -4.2% | -0.172 to 0.155 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
