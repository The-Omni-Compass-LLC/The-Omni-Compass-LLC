# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,908 | 2,907 | -0.0% | -2.75 to 0.0989 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.0% | -2.47 to 0.195 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.351 | 0.354 | +0.7% | -0.012 to 0.0167 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.496 | 0.508 | +2.4% | -0.0222 to 0.0462 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.17 | 0.172 | +1.0% | -0.00304 to 0.00651 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 451 | -12.0% | -65.6 to -57.1 | GAIN |
| bytes in the cache, mean (MB) | 405 | 354 | -12.5% | -70.2 to -31.3 | GAIN |
| pages read into the cache (misses) | 271,393 | 288,647 | +6.4% | -12,569 to 47,076 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.202 | +23.3% | -0.0423 to 0.119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 118 | 151 | +28.5% | -37.4 to 104 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.283 | +28.4% | -0.0702 to 0.196 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
