# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,912 | +0.4% | -48 to 71.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,916 | +0.4% | -47.5 to 70.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.237 | 0.238 | +0.6% | -0.00384 to 0.0065 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.376 | 0.372 | -1.1% | -0.0115 to 0.00345 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.171 | 0.166 | -3.1% | -0.00977 to -0.000954 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 474 | -7.5% | -140 to 63.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 390 | -6.4% | -112 to 58.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 718,852 | 740,754 | +3.0% | -222,753 to 266,557 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.149 | -9.6% | -0.056 to 0.0242 | EVEN, no difference beyond the noise |
| host CPU-seconds | 303 | 268 | -11.5% | -119 to 49.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.201 | -11.9% | -0.0853 to 0.0313 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -2.5 to 7.84 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
