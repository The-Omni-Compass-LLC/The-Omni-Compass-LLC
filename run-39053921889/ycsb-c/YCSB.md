# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,894 | -0.1% | -3.18 to 0.109 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -3.09 to 0.12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.32 | +1.1% | -0.00465 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.561 | 0.562 | +0.2% | -0.00645 to 0.00845 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.202 | +0.9% | -0.00702 to 0.0108 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 488 | -4.8% | -110 to 61 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 400 | -3.7% | -90.3 to 59.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,541 | 722,064 | +6.4% | -2,301 to 89,349 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.184 | +0.7% | -0.0519 to 0.0545 | EVEN, no difference beyond the noise |
| host CPU-seconds | 315 | 316 | +0.5% | -108 to 111 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.238 | +0.5% | -0.0813 to 0.0836 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
