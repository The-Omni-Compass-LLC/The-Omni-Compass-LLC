# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,897 | -0.1% | -3.71 to -0.335 | LOSS |
| throughput (operations a second) | 2,902 | 2,900 | -0.1% | -3.16 to -0.771 | LOSS |
| latency, 95th percentile (ms) | 0.354 | 0.354 | +0.1% | -0.0114 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.47 | 0.469 | -0.2% | -0.0118 to 0.00983 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.195 | +0.1% | -0.00518 to 0.00558 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 499 | -2.6% | -18.1 to -8.37 | GAIN |
| bytes in the cache, mean (MB) | 402 | 396 | -1.6% | -18.7 to 5.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 267,846 | 273,004 | +1.9% | -35,951 to 46,265 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.217 | -4.9% | -0.181 to 0.158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 170 | 158 | -6.9% | -170 to 147 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.319 | 0.297 | -6.9% | -0.319 to 0.275 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
